"""Step 0 (global interpreter, production embedder): requirement 1 + query vectors.

1. The unmodified production HybridRetriever reproduces its stored rankings:
   - top-20 of results/per_question_rrf_bm25_2to1_exact.json (experiment run, 84 benchmark questions)
   - top-10 of docs/audit_runs/retrieval_final.json (production code path, 84 + 10 diagnostic questions)
   Any ranking mismatch stops the benchmark (exit 1). Evidence-set differences against retrieval_final.json are
   reported separately: evidence assembly gained integration scoping after that audit (2026-10-22).
2. Query vectors for every question, encoded exactly as production does (one question per encode call).
3. Query-embedding latency (warm-up, then REPS timed encodes per question).
4. BackendRetriever(numpy) with the cached vectors == production ranked() (full ranking) and evidence, every question.

    python -B -s step0_reproduce.py
"""
import os
import platform
import statistics
import sys
import time

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
import numpy as np  # noqa: E402

from bench_lib import (EDGE_QUESTIONS, EXP, OUT, QUERY_VECTORS, ROOT, BackendRetriever, CachedEmbedder, dump, load,  # noqa: E402
                       load_question_sets, verify_embedding_files)

REPS = 5


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    t0 = time.time()
    files = verify_embedding_files()
    from pismo_assistant.pipeline import Assistant
    from pismo_assistant.retrieval import HybridRetriever
    prod = HybridRetriever()
    a_prod = Assistant(retriever=prod, generator=object())
    sets = load_question_sets(prod.chunks)
    ids = prod.ids
    checks = []

    # 1. reproduction of stored rankings
    exp_rows = {r["id"]: r for r in load(os.path.join(EXP, "results", "per_question_rrf_bm25_2to1_exact.json"))}
    audit = {r["id"]: r for r in load(os.path.join(ROOT, "docs", "audit_runs", "retrieval_final.json"))["questions"]}
    rank_mismatch, ev_diff, prod_cache = [], [], {}
    for q in sets["labelled"]:
        order, n_exact = prod.ranked(q["q"])
        top = [ids[i] for i in order]
        prod_cache[q["q"]] = (top, n_exact)
        if q["id"] in exp_rows and top[:20] != exp_rows[q["id"]]["ranked_chunk_ids"][:20]:
            rank_mismatch.append({"id": q["id"], "ref": "per_question_rrf_bm25_2to1_exact.json"})
        if q["id"] in audit:
            if top[:10] != [x["chunk_id"] for x in audit[q["id"]]["top10"]]:
                rank_mismatch.append({"id": q["id"], "ref": "retrieval_final.json"})
            ev = [e.chunk_id for e in a_prod.evidence(q["q"])]
            ref = [e["chunk_id"] for e in audit[q["id"]]["evidence"]]
            if ev != ref:
                ev_diff.append({"id": q["id"], "question": q["q"], "stored": ref, "current": ev})
    n_exp = sum(1 for q in sets["labelled"] if q["id"] in exp_rows)
    n_aud = sum(1 for q in sets["labelled"] if q["id"] in audit)
    checks.append({"check": "production ranking reproduces stored top-20 (experiment) and top-10 (audit)",
                   "compared": {"per_question_rrf_bm25_2to1_exact.json": n_exp, "retrieval_final.json": n_aud},
                   "mismatches": rank_mismatch, "passed": not rank_mismatch})
    if rank_mismatch:
        dump(os.path.join(OUT, "step0_reproduce.json"), {"checks": checks, "evidence_diff_vs_audit": ev_diff})
        print("RANKING REPRODUCTION FAILED - stopping:", rank_mismatch[:5])
        return 1

    # 2-3. query vectors + embedding latency
    qs = list(dict.fromkeys([q["q"] for q in sets["labelled"] + sets["unlabelled"]] + [e["q"] for e in EDGE_QUESTIONS if e["q"].strip()]))
    emb = prod.embedder
    for q in qs[:10]:  # warm-up
        emb.encode([q], normalize_embeddings=True, convert_to_numpy=True)
    vecs, lat = [], {}
    for q in qs:
        times = []
        for _ in range(REPS):
            t = time.perf_counter()
            v = emb.encode([q], normalize_embeddings=True, convert_to_numpy=True)[0]
            times.append(time.perf_counter() - t)
        vecs.append(v)
        lat[q] = times
    np.savez(QUERY_VECTORS, questions=np.array(qs), vectors=np.stack(vecs).astype(np.float32))
    allt = [x * 1000 for t in lat.values() for x in t]
    allt.sort()
    embed_timing = {"questions": len(qs), "reps": REPS, "n": len(allt), "median_ms": round(statistics.median(allt), 3),
                    "p90_ms": round(allt[int(0.9 * len(allt)) - 1], 3), "p95_ms": round(allt[int(0.95 * len(allt)) - 1], 3),
                    "max_ms": round(allt[-1], 3),
                    "per_question_median_ms": {q: round(statistics.median(t) * 1000, 3) for q, t in lat.items()}}

    # 4. numpy adapter with cached vectors == production
    br = BackendRetriever(embedder=CachedEmbedder())
    a_br = Assistant(retriever=br, generator=object())
    adapter_mismatch = []
    for q in sets["labelled"] + sets["unlabelled"]:
        top, n_exact = prod_cache.get(q["q"]) or (lambda o: ([ids[i] for i in o[0]], o[1]))(prod.ranked(q["q"]))
        o2, n2 = br.ranked(q["q"])
        if [ids[i] for i in o2] != top or n2 != n_exact:
            adapter_mismatch.append({"id": q["id"], "what": "full ranking"})
        if [e.chunk_id for e in a_br.evidence(q["q"])] != [e.chunk_id for e in a_prod.evidence(q["q"])]:
            adapter_mismatch.append({"id": q["id"], "what": "evidence"})
    checks.append({"check": "BackendRetriever(numpy, cached query vectors) == production ranked() full ranking and evidence",
                   "compared": len(sets["labelled"]) + len(sets["unlabelled"]), "mismatches": adapter_mismatch,
                   "passed": not adapter_mismatch})
    out = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "python": sys.version, "platform": platform.platform(),
           "embedding_files_sha256": files, "chunk_set_hash": prod.chunk_set_hash,
           "benchmark_sha256": sets["benchmark_sha256"], "webhook_v2_sha256": sets["webhook_v2_sha256"],
           "question_counts": {s: sum(1 for q in sets["labelled"] + sets["unlabelled"] if q["set"] == s)
                               for s in ("primary", "extension", "diagnostic", "webhook_v2", "probe", "demo")},
           "webhook_v2_label_status": {q["id"]: [l["status"] for l in q["labels"]] for q in sets["labelled"] if q["set"] == "webhook_v2"},
           "checks": checks, "evidence_diff_vs_audit_2026_10_21": ev_diff, "embedding_latency": embed_timing,
           "seconds": round(time.time() - t0, 1)}
    dump(os.path.join(OUT, "step0_reproduce.json"), out)
    for c in checks:
        print(("PASS " if c["passed"] else "FAIL ") + c["check"], c["compared"], c["mismatches"][:5])
    print("evidence differences vs stored audit (expected after 2026-10-22 scoping change):", [d["id"] for d in ev_diff])
    print("embedding latency:", {k: v for k, v in embed_timing.items() if k != "per_question_median_ms"})
    print("question counts:", out["question_counts"], " seconds:", out["seconds"])
    return 0 if all(c["passed"] for c in checks) else 1


if __name__ == "__main__":
    sys.exit(main())
