"""Fair latency comparison: backends alternate query by query inside ONE process, so machine noise hits all equally.

    python -B -s latency_interleaved.py --backend faiss       # numpy vs FAISS configurations (global interpreter)
    %USERPROFILE%\\.venvs\\pismo_chroma_bench\\Scripts\\python -B -s latency_interleaved.py --backend chroma

Measures, for the 84 benchmark questions x REPS rounds (configuration order rotated every round): dense ranking and the
hybrid ranking (BM25 + dense + RRF + identifier promotion). Then repeated 10-thread dense runs that count per-call
exceptions (failure rate), and --memory: index-only RSS of a clean open in this fresh process (no pipeline loaded).
"""
import argparse
import os
import statistics
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import psutil

from bench_lib import OUT, VECTORS, WINDOW_CHUNK, BackendRetriever, CachedEmbedder, Dense, NumpyDense, dump, load_question_sets

REPS = 7


def ms_summary(xs):
    xs = sorted(x * 1000 for x in xs)
    return {"n": len(xs), "median": round(statistics.median(xs), 3), "p90": round(xs[int(0.9 * len(xs)) - 1], 3),
            "p95": round(xs[int(0.95 * len(xs)) - 1], 3), "max": round(xs[-1], 3)}


def memory_probe(backend):
    """Index-only memory in a process that has loaded nothing else (production-equivalent load for NumPy)."""
    p = psutil.Process()
    r0 = p.memory_info().rss
    t = time.perf_counter()
    if backend == "numpy":
        d = Dense(np.load(VECTORS), np.load(WINDOW_CHUNK), 11026)   # exactly what HybridRetriever keeps
        q = d.V[0]
        d.scores(q)
    elif backend == "faiss":
        import faiss
        ix = faiss.read_index(os.path.join(OUT, "faiss", "flat_ip.index"))
        ix.search(ix.reconstruct(0).reshape(1, -1), 10)
    else:
        import chromadb
        from chromadb.config import Settings
        c = chromadb.PersistentClient(path=os.path.join(OUT, "chroma_db"), settings=Settings(anonymized_telemetry=False))
        col = c.get_collection("pismo_windows_v1")
        col.query(query_embeddings=[np.load(VECTORS, mmap_mode="r")[0].tolist()], n_results=10, include=["distances"])
    secs = time.perf_counter() - t
    mi = p.memory_info()
    return {"backend": backend, "rss_before_mb": round(r0 / 2**20, 1), "rss_after_open_and_query_mb": round(mi.rss / 2**20, 1),
            "index_rss_delta_mb": round((mi.rss - r0) / 2**20, 1), "peak_working_set_mb": round(getattr(mi, "peak_wset", 0) / 2**20, 1),
            "open_and_first_query_s": round(secs, 4)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=("numpy", "faiss", "chroma"), required=True)
    ap.add_argument("--memory", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    if a.memory:
        r = memory_probe(a.backend)
        dump(os.path.join(OUT, f"memory_{a.backend}.json"), r)
        print(r)
        return
    from run_backend import make_configs, open_backend
    base = BackendRetriever(embedder=CachedEmbedder())
    sets = load_question_sets(base.chunks)
    qs = [q["q"] for q in sets["labelled"] if q["set"] in ("primary", "extension")]
    qv = [base.embedder.vec[q] for q in qs]
    h, _ = open_backend(a.backend)
    cfgs = [NumpyDense(base.dense.V, base.dense.wc, base.ids)] + make_configs(a.backend, h, base.ids)
    retr = {c.name: BackendRetriever(backend=c, embedder=base.embedder) for c in cfgs}
    for c in cfgs:  # warm-up
        for v, q in zip(qv[:10], qs[:10]):
            c.order(v)
            retr[c.name].parts(q)
    dense = {c.name: [] for c in cfgs}
    hybrid = {c.name: [] for c in cfgs}
    for rnd in range(REPS):
        for i, (v, q) in enumerate(zip(qv, qs)):
            k = (i + rnd) % len(cfgs)
            for c in cfgs[k:] + cfgs[:k]:   # rotate order to cancel position effects
                t = time.perf_counter(); c.order(v); dense[c.name].append(time.perf_counter() - t)
                t = time.perf_counter(); retr[c.name].parts(q); hybrid[c.name].append(time.perf_counter() - t)
    # concurrency failure rate: 10 threads, every call wrapped
    conc = {}
    for c in cfgs:
        if getattr(c, "depth", None) not in (None, 2000):
            continue
        ok, fail, errs, lat = 0, 0, {}, []

        def job(i):
            t = time.perf_counter()
            try:
                c.order(qv[i % len(qv)])
                return True, time.perf_counter() - t, None
            except Exception as e:
                return False, time.perf_counter() - t, f"{type(e).__name__}: {e}"[:200]
        for trial in range(5):
            with ThreadPoolExecutor(max_workers=10) as ex:
                for good, dt, err in ex.map(job, range(len(qv) * 2)):
                    if good:
                        ok += 1
                        lat.append(dt)
                    else:
                        fail += 1
                        errs[err] = errs.get(err, 0) + 1
        conc[c.name] = {"threads": 10, "trials": 5, "calls": ok + fail, "failed_calls": fail, "failure_rate": round(fail / (ok + fail), 4),
                        "errors": errs, "latency_ms_ok_calls": ms_summary(lat) if lat else None}
    out = {"backend": a.backend, "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "reps": REPS, "queries": len(qs),
           "dense_ms": {k: ms_summary(v) for k, v in dense.items()}, "hybrid_ranking_ms": {k: ms_summary(v) for k, v in hybrid.items()},
           "concurrency_10_threads": conc}
    dump(os.path.join(OUT, f"latency_interleaved_{a.backend}.json"), out)
    for k in dense:
        print(f"{k:16} dense med {out['dense_ms'][k]['median']:8.3f} p90 {out['dense_ms'][k]['p90']:8.3f} | hybrid med "
              f"{out['hybrid_ranking_ms'][k]['median']:8.3f} p90 {out['hybrid_ranking_ms'][k]['p90']:8.3f}")
    for k, v in conc.items():
        print(k, {x: v[x] for x in ("calls", "failed_calls", "failure_rate", "errors")})


if __name__ == "__main__":
    main()
