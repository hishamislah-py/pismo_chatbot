"""Step 4: run every retrieval configuration on the frozen benchmark and write machine-readable results.

Primary comparison (no tuning, no reranker): bm25, semantic, rrf_equal, rrf_bm25_2to1.
Optional lexical enhancement, reported separately: bm25_exact, rrf_bm25_2to1_exact.
Usage: python -B -s scripts/run_experiment.py   (HF_HUB_OFFLINE=1 is set automatically)
"""
import os
import platform
import random
import re
import statistics
import sys
import time
from collections import Counter, defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import EXP, RESULTS, dump_json, load_json, read_jsonl, sha_bytes, sha_json  # noqa: E402
from corpus import index_text  # noqa: E402
from metrics import DEPTH, evaluate, mean  # noqa: E402
from retrievers import (BM25, RRF_K, Dense, detect_identifiers, exact_rerank, load_embedder, rank_by_score,  # noqa: E402
                        rrf)

PRIMARY_CONFIGS = ["bm25", "semantic", "rrf_equal", "rrf_bm25_2to1"]
ENHANCED_CONFIGS = ["bm25_exact", "rrf_bm25_2to1_exact"]
CONFIGS = PRIMARY_CONFIGS + ENHANCED_CONFIGS
METRIC_KEYS = ["recall@5", "recall@10", "mrr", "ndcg@5", "ndcg@10", "hit@5", "hit@10", "ku_recall@5", "ku_recall@10"]


def verify_inputs(chunks):
    bench = load_json(os.path.join(EXP, "BENCHMARK.json"))
    summary = load_json(os.path.join(RESULTS, "corpus_summary.json"))
    chunk_hash = sha_bytes("".join(f"{c['chunk_id']}\t{c['sha256']}\n" for c in chunks).encode())
    content_hash = sha_json({"primary": bench["primary"], "extension": bench["extension"]})
    frozen = open(os.path.join(EXP, "BENCHMARK.sha256"), encoding="utf-8").read().split()[0]
    problems = []
    if chunk_hash != summary["chunk_set_hash"] or chunk_hash != bench["_meta"]["chunk_set_hash"]:
        problems.append("chunk set differs from the one the benchmark was frozen against")
    if content_hash != frozen or content_hash != bench["_meta"]["benchmark_content_sha256"]:
        problems.append("benchmark content differs from the frozen hash")
    for c in chunks:
        if not (c["ku_path"].startswith("knowledge_units/") and c["ku_path"].endswith(".md") and c["ku_id"].startswith("KU-")):
            problems.append(f"non-KU chunk in index: {c['ku_path']}")
            break
    if problems:
        print("INPUT VERIFICATION FAILED:", problems)
        sys.exit(1)
    return bench, summary, chunk_hash, content_hash


def bootstrap_diff(a, b, n=2000, seed=20261021):
    """Paired bootstrap of mean(a) - mean(b): returns (diff, lo95, hi95)."""
    rng = random.Random(seed)
    idx = list(range(len(a)))
    d = [x - y for x, y in zip(a, b)]
    base = sum(d) / len(d)
    sims = sorted(sum(d[rng.choice(idx)] for _ in idx) / len(idx) for _ in range(n))
    return round(base, 4), round(sims[int(0.025 * n)], 4), round(sims[int(0.975 * n) - 1], 4)


def main():
    t0 = time.time()
    chunks = read_jsonl(os.path.join(RESULTS, "chunks.jsonl"))
    bench, summary, chunk_hash, bench_hash = verify_inputs(chunks)
    ids = [c["chunk_id"] for c in chunks]
    pos = {cid: i for i, cid in enumerate(ids)}
    chunk_ku = {c["chunk_id"]: c["ku_id"] for c in chunks}
    texts = [index_text(c) for c in chunks]
    texts_lower = [t.lower() for t in texts]
    bm25 = BM25(texts)
    emb_dir = os.path.join(RESULTS, "embeddings")
    emeta = load_json(os.path.join(emb_dir, "embedding_meta.json"))
    if emeta["chunk_set_hash"] != chunk_hash:
        print("embeddings are stale; run embed_corpus.py")
        sys.exit(1)
    dense = Dense(np.load(os.path.join(emb_dir, "window_vectors.npy")), np.load(os.path.join(emb_dir, "window_chunk.npy")), len(chunks))
    questions = bench["primary"] + bench["extension"]
    t1 = time.time()
    model = load_embedder()
    qvecs = model.encode([q["q"] for q in questions], batch_size=32, normalize_embeddings=True, convert_to_numpy=True)
    t2 = time.time()

    per_q = {c: [] for c in CONFIGS}
    diag = []
    for qi, q in enumerate(questions):
        bs = bm25.scores(q["q"])
        ds = dense.scores(qvecs[qi])
        b_order = rank_by_score(bs, ids, positive_only=True)
        d_order = rank_by_score(ds, ids)
        idents = detect_identifiers(q["q"])
        orders = {
            "bm25": b_order,
            "semantic": d_order,
            "rrf_equal": rrf([b_order, d_order], [1.0, 1.0], ids),
            "rrf_bm25_2to1": rrf([b_order, d_order], [2.0, 1.0], ids),
        }
        orders["bm25_exact"], n_exact = exact_rerank(b_order, texts_lower, idents)
        orders["rrf_bm25_2to1_exact"], _ = exact_rerank(orders["rrf_bm25_2to1"], texts_lower, idents)
        valid = [l for l in q["labels"] if l["status"] == "valid"]
        label_sets = [set(l["relevant_chunk_ids"]) for l in valid]
        label_ku = [set(l["relevant_ku_ids"]) for l in valid]
        for cfg, order in orders.items():
            top = [ids[i] for i in order[:DEPTH]]
            score_src = bs if cfg.startswith("bm25") else ds if cfg == "semantic" else None
            row = {"id": q["id"], "set": q["set"], "question": q["q"], "type": q["type"], "workflow": q["workflow"],
                   "answerability": q.get("answerability"), "scored": q["scored"], "multi_ku": q["multi_ku"],
                   "lifecycle_sensitive": bool(q.get("lifecycle_sensitive")), "migration_issue": q.get("migration_issue"),
                   "expected_labels": [l["key"] for l in valid], "expected_ku_ids": q["relevant_ku_ids"],
                   "expected_evidence_sections": sorted({s for l in valid for s in l["evidence_sections"]})[:20],
                   "identifiers_detected": idents if cfg.endswith("exact") else None,
                   "ranked_chunk_ids": top[:20], "ranked_ku_ids": [chunk_ku[c] for c in top[:20]],
                   "scores_top20": [round(float(score_src[pos[c]]), 4) for c in top[:20]] if score_src is not None else None}
            if q["scored"]:
                ev = evaluate(top, label_sets, label_ku, chunk_ku)
                row.update(ev)
                fr = ev["first_relevant_rank"]
                row["outcome"] = "hit@5" if ev["hit@5"] else "ranked_6_10" if ev["hit@10"] else (
                    "ranked_11_100" if fr else "not_in_top_100")
                if len(valid) > 1:
                    row["multi_ku_coverage@5"] = ev["all_labels@5"]
                    row["multi_ku_coverage@10"] = ev["all_labels@10"]
            else:
                row["outcome"] = "unanswerable_not_scored" if q.get("answerability") == "none" else "no_valid_label"
            per_q[cfg].append(row)
        # unanswerable / lifecycle diagnostics (retrieval behaviour only; answer correctness is not judged here)
        d = {"id": q["id"], "set": q["set"], "answerability": q.get("answerability"), "lifecycle_sensitive": bool(q.get("lifecycle_sensitive")),
             "migration_issue": q.get("migration_issue"), "question": q["q"], "configs": {}}
        if q.get("answerability") in ("none", "partial", "conflict") or q.get("lifecycle_sensitive"):
            req_targets = set((q.get("required_statement_check") or {}).get("targets") or [])
            for cfg, order in orders.items():
                top10 = [chunks[i] for i in order[:10]]
                top5 = top10[:5]
                flags = Counter(f for c in top10 for f in c["flags"])
                dis = [rx for rx in q.get("distractors", []) if any(re.search(rx, c["text"], re.I) for c in top5)]
                current = any(c["ku_type"] in ("api_reference", "lifecycle_reference") or "removal_register" in c["flags"] for c in top10)
                hist5 = any(("historical_changelog" in c["flags"] or "unresolved_operation_link" in c["flags"]) for c in top5)
                d["configs"][cfg] = {
                    "top5_ku_ids": [c["ku_id"] for c in top5],
                    "top1_score": round(float((bs if cfg.startswith("bm25") else ds)[order[0]]), 4) if cfg in ("bm25", "semantic") else None,
                    "flags_top10": dict(flags), "distractors_in_top5": dis,
                    "required_statement_ku_in_top10": bool(req_targets & {c["ku_id"] for c in top10}) if req_targets else None,
                    "not_documented_statement_in_top10": flags.get("not_documented_statement", 0) > 0,
                    "current_state_evidence_in_top10": current,
                    "historical_or_unresolved_in_top5_without_current_evidence": hist5 and not current,
                }
            diag.append(d)
    t3 = time.time()

    # ---------------- aggregates
    def agg(rows):
        rows = [r for r in rows if r["scored"]]
        out = {"n": len(rows)}
        for k in METRIC_KEYS:
            out[k] = mean([float(r[k]) if r[k] is not None else None for r in rows])
        multi = [r for r in rows if "multi_ku_coverage@5" in r]
        out["n_multi_label"] = len(multi)
        out["all_required@5"] = mean([float(r["multi_ku_coverage@5"]) for r in multi])
        out["all_required@10"] = mean([float(r["multi_ku_coverage@10"]) for r in multi])
        return out

    aggregates = {}
    for cfg in CONFIGS:
        rows = per_q[cfg]
        a = {}
        for set_name in ("primary", "extension"):
            sr = [r for r in rows if r["set"] == set_name]
            a[set_name] = {"all": agg(sr)}
            a[set_name]["by_type"] = {t: agg([r for r in sr if r["type"] == t]) for t in sorted({r["type"] for r in sr})}
            a[set_name]["by_workflow"] = {w: agg([r for r in sr if r["workflow"] == w]) for w in sorted({r["workflow"] for r in sr})}
            a[set_name]["by_answerability"] = {x: agg([r for r in sr if r["answerability"] == x]) for x in sorted({str(r["answerability"]) for r in sr})}
            a[set_name]["migration_issue_questions"] = agg([r for r in sr if r["migration_issue"]])
            a[set_name]["lifecycle_sensitive"] = agg([r for r in sr if r["lifecycle_sensitive"]])
        a["combined"] = {"all": agg(rows)}
        aggregates[cfg] = a

    # paired bootstrap on per-question MRR and recall@5 (primary set), fixed seed
    sig = {}
    prim = {cfg: [r for r in per_q[cfg] if r["set"] == "primary" and r["scored"]] for cfg in CONFIGS}
    for a_cfg, b_cfg in [("rrf_bm25_2to1", "bm25"), ("rrf_equal", "bm25"), ("semantic", "bm25"), ("rrf_bm25_2to1", "rrf_equal"),
                         ("bm25_exact", "bm25"), ("rrf_bm25_2to1_exact", "rrf_bm25_2to1"), ("rrf_bm25_2to1_exact", "bm25_exact")]:
        sig[f"{a_cfg} - {b_cfg}"] = {m: bootstrap_diff([float(r[m]) for r in prim[a_cfg]], [float(r[m]) for r in prim[b_cfg]])
                                     for m in ("mrr", "recall@5", "recall@10")}

    # score separation: top-1 score of unanswerable vs answerable questions
    sep = {}
    for cfg in ("bm25", "semantic"):
        ans, una = [], []
        for r in per_q[cfg]:
            s = r["scores_top20"][0] if r["scores_top20"] else None
            if s is None:
                continue
            (una if r["answerability"] == "none" else ans).append(s)
        sep[cfg] = {"answerable_top1_median": round(statistics.median(ans), 4), "answerable_top1_min": round(min(ans), 4),
                    "unanswerable_top1": {r["id"]: r["scores_top20"][0] for r in per_q[cfg] if r["answerability"] == "none"}}

    for cfg in CONFIGS:
        dump_json(os.path.join(RESULTS, f"per_question_{cfg}.json"), per_q[cfg])
    dump_json(os.path.join(RESULTS, "aggregate_metrics.json"), {
        "corpus_manifest_hash": summary["corpus_manifest_hash"], "chunk_set_hash": chunk_hash, "benchmark_content_sha256": bench_hash,
        "configs": {"primary_comparison": PRIMARY_CONFIGS, "lexical_enhancement": ENHANCED_CONFIGS},
        "rrf": {"k": RRF_K, "formula": "sum_m w_m / (k + rank_m)", "weights": {"rrf_equal": [1, 1], "rrf_bm25_2to1": [2, 1]},
                "bm25_list": "chunks with BM25 score > 0", "semantic_list": "all chunks"},
        "evaluation_depth": DEPTH, "aggregates": aggregates, "paired_bootstrap_primary": sig, "score_separation": sep})
    dump_json(os.path.join(RESULTS, "unanswerable_and_lifecycle.json"), diag)
    dump_json(os.path.join(RESULTS, "run_log.json"), {
        "python": platform.python_version(), "numpy": np.__version__, "embedding": emeta,
        "seconds": {"load_and_index": round(t1 - t0, 1), "query_embedding": round(t2 - t1, 1), "retrieval_and_eval": round(t3 - t2, 1)},
        "questions": len(questions), "chunks": len(chunks)})
    for cfg in CONFIGS:
        p, e = aggregates[cfg]["primary"]["all"], aggregates[cfg]["extension"]["all"]
        print(f"{cfg:22} primary n={p['n']} R@5 {p['recall@5']} R@10 {p['recall@10']} MRR {p['mrr']} nDCG@10 {p['ndcg@10']} | "
              f"ext n={e['n']} R@5 {e['recall@5']} R@10 {e['recall@10']} MRR {e['mrr']}")


if __name__ == "__main__":
    main()
