"""Run one dense backend through the production retrieval + evidence path (no OpenAI call). One process per backend.

    python -B -s run_backend.py --backend numpy
    python -B -s run_backend.py --backend faiss
    %USERPROFILE%\\.venvs\\pismo_chroma_bench\\Scripts\\python -B -s run_backend.py --backend chroma

Per backend: cold/warm index load, integrity + mapping checks, window-score equivalence against NumPy, then for each
configuration (full ranking, and @100/@500/@2000 windows for FAISS and Chroma) every question through
Assistant.evidence (BM25, RRF 2:1, identifier promotion, navigation exclusion, webhook scoping, evidence expansion).
Warm-up once, then REPS timed repetitions per question. Concurrency (1/5/10 threads) for the full configuration and
the @2000 configuration. Writes out/run_<backend>.json.
"""
import argparse
import os
import platform
import statistics
import sys
import time
import traceback
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import psutil

from bench_lib import (DEPTHS, EDGE_QUESTIONS, OUT, VECTORS, WINDOW_CHUNK, BackendRetriever, CachedEmbedder, ChromaDense,
                       FaissDense, NumpyDense, dir_size, dump, load, load_question_sets, verify_embedding_files)
from pismo_assistant import config, integrations
from pismo_assistant.pipeline import Assistant
from pismo_assistant.retrieval import is_navigation
from retrievers import detect_identifiers

REPS = 5
SEED = 20261026
PROC = psutil.Process()


def mb(x):
    return round(x / 2**20, 1)


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, int(round(p / 100 * len(xs))) - 1))] if xs else None


def summary_ms(xs):
    xs = [x * 1000 for x in xs]
    if not xs:
        return None
    return {"n": len(xs), "median": round(statistics.median(xs), 3), "p90": round(pct(xs, 90), 3), "p95": round(pct(xs, 95), 3),
            "mean": round(statistics.mean(xs), 3), "min": round(min(xs), 3), "max": round(max(xs), 3)}


# ---------------------------------------------------------------- backend loading
def open_backend(name):
    """Returns (handle, info) with the time to open the persistent index (no query)."""
    t = time.perf_counter()
    if name == "numpy":
        V = np.load(VECTORS).astype(np.float32)
        h = {"V": V, "wc": np.load(WINDOW_CHUNK)}
    elif name == "faiss":
        import faiss
        h = {"index": faiss.read_index(os.path.join(OUT, "faiss", "flat_ip.index")), "wc": np.load(WINDOW_CHUNK)}
    else:
        import chromadb
        from chromadb.config import Settings
        client = chromadb.PersistentClient(path=os.path.join(OUT, "chroma_db"), settings=Settings(anonymized_telemetry=False))
        h = {"client": client, "col": client.get_collection("pismo_windows_v1"), "wc": np.load(WINDOW_CHUNK)}
    return h, time.perf_counter() - t


def make_configs(name, h, ids):
    if name == "numpy":
        return [NumpyDense(h["V"], h["wc"], ids)]
    cls = FaissDense if name == "faiss" else ChromaDense
    key = "index" if name == "faiss" else "col"
    return [cls(h[key], h["wc"], ids)] + [cls(h[key], h["wc"], ids, depth=d) for d in DEPTHS]


def integrity_checks(name, h, ids, V, wc):
    checks = []

    def add(check, passed, **kw):
        checks.append(dict(check=check, passed=bool(passed), **kw))

    if name == "faiss":
        meta = load(os.path.join(OUT, "faiss", "flat_ip.index.meta.json"))
        ix = h["index"]
        add("faiss index size/dimension match the production vectors", ix.ntotal == len(V) and ix.d == V.shape[1], ntotal=int(ix.ntotal), d=int(ix.d))
        add("faiss index built from the current window_vectors.npy (sha256)", meta["vectors_sha256"] == verify_embedding_files()["window_vectors.npy"])
        rec = np.vstack([ix.reconstruct(int(i)) for i in range(0, len(V), 997)])
        err = float(np.abs(rec - V[::997]).max())
        add("faiss stored vectors == production vectors (every 997th row)", err == 0.0, max_abs_err=err)
    elif name == "chroma":
        col = h["col"]
        md = col.metadata or {}
        add("chroma collection count == 25,325 windows", col.count() == len(V), count=col.count())
        add("chroma collection built from the current window_vectors.npy (sha256)",
            md.get("vectors_sha256") == verify_embedding_files()["window_vectors.npy"])
        add("chroma distance space is cosine", (col.configuration.get("hnsw") or {}).get("space") == "cosine",
            configuration=col.configuration)
        bad, n = [], 0
        for s in range(0, len(V), 5000):
            want = [f"w{i:05d}" for i in range(s, min(s + 5000, len(V)))]
            r = col.get(ids=want, include=["metadatas"])
            got = dict(zip(r["ids"], r["metadatas"]))
            for wid in want:
                i = int(wid[1:])
                m = got.get(wid)
                n += 1
                if not m or m["chunk_id"] != ids[wc[i]] or m["chunk_index"] != int(wc[i]):
                    bad.append(wid)
        add("chroma window id -> parent chunk mapping == window_chunk.npy (all windows)", not bad and n == len(V), checked=n, mismatches=bad[:10])
        rng = np.random.RandomState(SEED)
        sample = sorted(rng.choice(len(V), 2000, replace=False).tolist())
        r = col.get(ids=[f"w{i:05d}" for i in sample], include=["embeddings"])
        E = np.asarray(r["embeddings"], dtype=np.float32)
        order = [int(x[1:]) for x in r["ids"]]
        err = float(np.abs(E - V[order]).max())
        add("chroma stored embeddings == production vectors (2,000 random windows, seed 20261026)", err < 1e-6, max_abs_err=err)
    return checks


def score_equivalence(name, configs, qvecs, V):
    """For identical window ids: backend similarity vs NumPy V @ q; and approximate top-N window recall vs exact top-N."""
    out = {"max_abs_score_err": 0.0, "window_recall": {}, "returned_counts_full": []}
    rec = {d: [] for d in DEPTHS}
    for qv in qvecs:
        exact = V @ qv
        for cfg in configs:
            if name == "numpy":
                continue  # NumPy is the reference
            wi, ws = cfg.search(qv)
            out["max_abs_score_err"] = max(out["max_abs_score_err"], float(np.abs(ws - exact[wi]).max()))
            if name != "numpy" and cfg.depth is None:
                out["returned_counts_full"].append(int(len(wi)))
            if name != "numpy" and cfg.depth:
                top = np.argsort(-exact, kind="stable")[:cfg.depth]
                rec[cfg.depth].append(len(set(wi.tolist()) & set(top.tolist())) / cfg.depth)
    out["window_recall"] = {f"@{d}": {"mean": round(float(np.mean(v)), 5), "min": round(float(np.min(v)), 5)} for d, v in rec.items() if v}
    rc = out["returned_counts_full"]
    out["returned_counts_full"] = {"min": min(rc), "max": max(rc)} if rc else None
    return out


# ---------------------------------------------------------------- per-question run
def run_config(cfg, chunks_kwargs, questions, by_id):
    br = BackendRetriever(backend=cfg, **chunks_kwargs)
    a = Assistant(retriever=br, generator=object())
    ids = br.ids
    rows, errors = [], []
    for q in questions:
        try:
            a.evidence(q["q"])  # warm-up
            times, parts, first = [], [], None
            stable = True
            for rep in range(REPS):
                t = time.perf_counter()
                ev = a.evidence(q["q"])
                total = time.perf_counter() - t
                p = br.last or {"t": {}}
                times.append(total)
                parts.append(p["t"])
                sig = ([ids[i] for i in p.get("order", [])[:100]], [e.chunk_id for e in ev])
                if first is None:
                    first, ev0, p0 = sig, ev, p
                elif sig != first:
                    stable = False
            excluded = sorted(integrations.excluded_integrations(q["q"]))
            final = [e.chunk_id for e in ev0 if e.origin == "retrieved"]
            idents_ok = all(any(x.lower() in br.texts_lower[i] for x in detect_identifiers(q["q"]))
                            for i in p0.get("order", [])[:p0.get("n_exact", 0)])
            row = {"id": q["id"], "set": q["set"], "q": q["q"],
                   "dense_top100": [ids[i] for i in p0.get("d_order", [])[:100]], "dense_len": len(p0.get("d_order", [])),
                   "bm25_top100": [ids[i] for i in p0.get("b_order", [])[:100]],
                   "hybrid_top100": first[0], "n_exact": p0.get("n_exact", 0), "fused_len": len(p0.get("order", [])),
                   "final_top6": final, "evidence": [[e.chunk_id, e.origin] for e in ev0], "excluded_integrations": excluded,
                   "deterministic": stable,
                   "checks": {
                       "no_navigation_in_final_top6": not any(is_navigation(by_id[c]) for c in final),
                       "evidence_deduplicated": len({e.chunk_id for e in ev0}) == len(ev0),
                       "evidence_text_maps_to_source_chunk": all(e.text == by_id[e.chunk_id]["text"] and e.ku_id == by_id[e.chunk_id]["ku_id"]
                                                                and e.source_refs == (by_id[e.chunk_id].get("source_refs") or []) for e in ev0),
                       "evidence_labels_sequential": [e.label for e in ev0] == [f"E{i}" for i in range(1, len(ev0) + 1)],
                       "webhook_scope_respected": not excluded or not any(integrations.chunk_integration(by_id[e.chunk_id]) in excluded for e in ev0),
                       "promoted_chunks_contain_identifier": idents_ok,
                       "final_top6_full": len(final) == config.TOP_K if q["q"].strip() else len(ev0) == 0,
                   },
                   "timing_s": {"total": times, "bm25": [x.get("bm25") for x in parts], "dense": [x.get("dense") for x in parts],
                                "fusion": [x.get("fusion") for x in parts],
                                "post": [tt - sum(v for v in x.values() if v) for tt, x in zip(times, parts)]}}
            rows.append(row)
        except Exception as e:  # recorded, never silently dropped
            errors.append({"id": q["id"], "error": f"{type(e).__name__}: {e}", "trace": traceback.format_exc()[-1500:]})
    return br, rows, errors


def concurrency(br, cfg, qvecs, questions):
    res = {}
    for workers in (1, 5, 10):
        for kind in ("dense", "hybrid_ranking"):
            lat = []

            def job(i):
                t = time.perf_counter()
                if kind == "dense":
                    cfg.order(qvecs[i])
                else:
                    br.parts(questions[i])
                return time.perf_counter() - t
            idx = list(range(len(questions))) * 2
            t0 = time.perf_counter()
            try:
                with ThreadPoolExecutor(max_workers=workers) as ex:
                    lat = list(ex.map(job, idx))
                wall = time.perf_counter() - t0
                res[f"{kind}@{workers}"] = {"calls": len(idx), "wall_s": round(wall, 3), "throughput_qps": round(len(idx) / wall, 2),
                                            "latency_ms": summary_ms(lat), "errors": 0}
            except Exception as e:
                res[f"{kind}@{workers}"] = {"error": f"{type(e).__name__}: {e}"}
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=("numpy", "faiss", "chroma"), required=True)
    ap.add_argument("--no-concurrency", action="store_true")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8")
    t_proc = time.time()
    rss = {"process_start": mb(PROC.memory_info().rss)}
    files = verify_embedding_files()
    V = np.load(VECTORS).astype(np.float32)
    wc = np.load(WINDOW_CHUNK)

    # shared production pipeline objects (chunks, BM25, verify_index) - identical for every backend
    t = time.perf_counter()
    base = BackendRetriever(embedder=CachedEmbedder())
    t_base = time.perf_counter() - t
    rss["after_pipeline_load"] = mb(PROC.memory_info().rss)
    ids, by_id = base.ids, base.by_id
    sets = load_question_sets(base.chunks)
    questions = sets["labelled"] + sets["unlabelled"] + [dict(e, set="edge") for e in EDGE_QUESTIONS]
    emb = base.embedder
    bench_q = [q["q"] for q in sets["labelled"] if q["set"] in ("primary", "extension")]
    qvecs = [emb.vec[q] for q in bench_q]

    # cold open (first in this process) + first query, then warm re-open
    rss_before = PROC.memory_info().rss
    h, t_open_cold = open_backend(a.backend)
    configs = make_configs(a.backend, h, ids)
    t = time.perf_counter()
    configs[0].order(qvecs[0])
    t_first_query = time.perf_counter() - t
    rss["after_index_open_and_first_query"] = mb(PROC.memory_info().rss)
    index_rss_delta = mb(PROC.memory_info().rss - rss_before)
    h2, t_open_warm = open_backend(a.backend)
    t = time.perf_counter()
    make_configs(a.backend, h2, ids)[0].order(qvecs[0])
    t_first_query_warm = time.perf_counter() - t
    del h2

    checks = integrity_checks(a.backend, h, ids, V, wc)
    equiv = score_equivalence(a.backend, configs, qvecs, V)

    # dense-only microbenchmark: library search call vs search + window->chunk ranking
    micro = {}
    for cfg in configs:
        s_lat, o_lat = [], []
        for qv in qvecs:
            cfg.order(qv)
            for _ in range(REPS):
                if hasattr(cfg, "search"):
                    t = time.perf_counter(); cfg.search(qv); s_lat.append(time.perf_counter() - t)
                else:
                    t = time.perf_counter(); cfg.dense.scores(qv); s_lat.append(time.perf_counter() - t)
                t = time.perf_counter(); cfg.order(qv); o_lat.append(time.perf_counter() - t)
        micro[cfg.name] = {"index_search_ms": summary_ms(s_lat), "dense_ranking_ms": summary_ms(o_lat), "reps": REPS, "queries": len(qvecs)}

    kw = {"embedder": emb}
    runs, conc = {}, {}
    for cfg in configs:
        br, rows, errors = run_config(cfg, kw, questions, by_id)
        runs[cfg.name] = {"rows": rows, "errors": errors}
        if not a.no_concurrency and getattr(cfg, "depth", None) in (None, 2000):
            conc[cfg.name] = concurrency(br, cfg, qvecs, bench_q)
        print(f"{cfg.name}: {len(rows)} questions, {len(errors)} errors")
        del br
    rss["end"] = mb(PROC.memory_info().rss)
    mi = PROC.memory_info()
    persist = {"numpy": os.path.getsize(VECTORS) + os.path.getsize(WINDOW_CHUNK),
               "faiss": os.path.getsize(os.path.join(OUT, "faiss", "flat_ip.index")) + os.path.getsize(WINDOW_CHUNK),
               "chroma": dir_size(os.path.join(OUT, "chroma_db"))}[a.backend]
    lib = {"numpy": np.__version__}
    if a.backend == "faiss":
        import faiss
        lib.update(faiss=faiss.__version__, faiss_omp_threads=faiss.omp_get_max_threads())
    if a.backend == "chroma":
        import chromadb
        lib.update(chromadb=chromadb.__version__, configuration=h["col"].configuration)
    out = {"backend": a.backend, "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "python": sys.version, "executable": sys.executable,
           "platform": platform.platform(), "cpu_count": os.cpu_count(), "libraries": lib, "reps": REPS, "seed": SEED,
           "embedding_files_sha256": files, "chunk_set_hash": base.chunk_set_hash, "benchmark_sha256": sets["benchmark_sha256"],
           "env_threads": {k: os.environ.get(k) for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "OPENBLAS_NUM_THREADS")},
           "load": {"pipeline_load_s": round(t_base, 3), "index_open_cold_s": round(t_open_cold, 4), "first_query_cold_s": round(t_first_query, 4),
                    "index_open_warm_s": round(t_open_warm, 4), "first_query_warm_s": round(t_first_query_warm, 4),
                    "note": "cold = first open in a fresh process (OS file cache not flushed: no admin rights)"},
           "memory_mb": dict(rss, index_open_rss_delta=index_rss_delta, peak_working_set=mb(getattr(mi, "peak_wset", 0))),
           "persistent_size_bytes": persist, "integrity_checks": checks, "score_equivalence": equiv, "dense_micro": micro,
           "concurrency": conc, "runs": runs, "seconds": round(time.time() - t_proc, 1)}
    dump(os.path.join(OUT, f"run_{a.backend}.json"), out)
    for c in checks:
        print(("PASS " if c["passed"] else "FAIL ") + c["check"])
    print("score equivalence:", equiv)
    print("load:", out["load"], "memory:", out["memory_mb"], "size:", persist, "seconds:", out["seconds"])


if __name__ == "__main__":
    main()
