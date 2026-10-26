"""Metrics, paired bootstrap, equivalence and latency tables from out/run_<backend>.json (global interpreter).

Label metrics use the project's definitions (scripts/metrics.py): a question's valid gold labels are sets of chunk ids;
label recall@6 = share of labels with a satisfying chunk in the top 6; nDCG@6 = label-level gain (a chunk earns 1 per
newly covered label); MRR = 1/rank of the first chunk satisfying any label (depth 100; within the 6 slots for the
final top-6); hit@6. Chunk precision@6 (supplementary, binary) = share of the top 6 chunks that satisfy any valid label.
Evidence label recall / all labels = the audit's measure over the evidence actually sent to the model.

    python -B -s analyze.py
"""
import csv
import os
import statistics
import sys
from collections import defaultdict

from bench_lib import OUT, dump, load, load_question_sets, read_jsonl
from pismo_assistant import config

from metrics import label_hits, label_recall_at, mrr, ndcg_at  # noqa: E402
from run_experiment import bootstrap_diff  # noqa: E402

K = 6
BASE = "numpy"
LISTS = ("dense", "bm25", "hybrid", "final")
LABELLED_SETS = ("benchmark", "diagnostic", "webhook_v2")


def set_group(s):
    return "benchmark" if s in ("primary", "extension") else s


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, int(round(p / 100 * len(xs))) - 1))] if xs else None


def r4(x):
    return None if x is None else round(x, 4)


def qmetrics(ranked, label_sets, k=K):
    hits = label_hits(ranked, label_sets)
    n = len(label_sets)
    union = set().union(*label_sets)
    top = ranked[:k]
    return {"recall@6": label_recall_at(hits, n, k), "mrr": mrr(hits), "ndcg@6": ndcg_at(hits, n, k),
            "hit@6": float(any(hits[:k])), "chunk_precision@6": (sum(c in union for c in top) / len(top)) if top else 0.0}


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    runs = {b: load(os.path.join(OUT, f"run_{b}.json")) for b in ("numpy", "faiss", "chroma")}
    step0 = load(os.path.join(OUT, "step0_reproduce.json"))
    chunks = read_jsonl(config.CHUNKS_PATH)
    by_id = {c["chunk_id"]: c for c in chunks}
    sets = load_question_sets(chunks)
    qinfo = {q["id"]: q for q in sets["labelled"]}
    cfg_rows = {}
    for b, r in runs.items():
        for cfg, v in r["runs"].items():
            cfg_rows[cfg] = {row["id"]: row for row in v["rows"]}
    configs = list(cfg_rows)
    base = cfg_rows[BASE]

    # ---------------- per-question label metrics
    per_q = []
    for cfg in configs:
        for qid, q in qinfo.items():
            valid = [l for l in q["labels"] if l["status"] == "valid"]
            if not valid or q.get("answerability") == "none":
                continue
            row = cfg_rows[cfg][qid]
            ls = [set(l["relevant_chunk_ids"]) for l in valid]
            rec = {"config": cfg, "id": qid, "set": set_group(q["set"]), "subset": q["set"], "workflow": q.get("workflow"),
                   "type": q.get("type"), "answerability": q.get("answerability"), "n_labels": len(valid)}
            for lst, ranked in (("dense", row["dense_top100"]), ("bm25", row["bm25_top100"]), ("hybrid", row["hybrid_top100"]),
                                ("final", row["final_top6"])):
                for m, v in qmetrics(ranked, ls).items():
                    rec[f"{lst}_{m}"] = v
            ev = [c for c, _ in row["evidence"]]
            ev_cov = sum(1 for s in ls if s & set(ev)) / len(ls)
            rec["evidence_label_recall"] = ev_cov
            rec["evidence_all_labels"] = float(ev_cov == 1.0)
            rec["final_top6"] = " ".join(row["final_top6"])
            rec["final_top6_same_as_numpy"] = row["final_top6"] == base[qid]["final_top6"]
            rec["evidence_same_as_numpy"] = row["evidence"] == base[qid]["evidence"]
            per_q.append(rec)

    metric_cols = [f"{l}_{m}" for l in LISTS for m in ("recall@6", "mrr", "ndcg@6", "hit@6", "chunk_precision@6")] + \
                  ["evidence_label_recall", "evidence_all_labels"]

    def agg(rows):
        out = {"n": len(rows)}
        for m in metric_cols:
            xs = [r[m] for r in rows if r[m] is not None]
            out[m] = r4(sum(xs) / len(xs)) if xs else None
        return out

    aggregates = {cfg: {s: agg([r for r in per_q if r["config"] == cfg and r["set"] == s]) for s in LABELLED_SETS} for cfg in configs}
    for cfg in configs:
        for sub in ("primary", "extension"):
            aggregates[cfg][sub] = agg([r for r in per_q if r["config"] == cfg and r["subset"] == sub])
    by_cat = {cfg: {w: agg([r for r in per_q if r["config"] == cfg and r["set"] == "benchmark" and r["workflow"] == w])
                    for w in sorted({r["workflow"] for r in per_q if r["set"] == "benchmark"})} for cfg in configs}

    # ---------------- paired bootstrap vs numpy (benchmark set, fixed seed from run_experiment)
    boot = {}
    bq = sorted({r["id"] for r in per_q if r["set"] == "benchmark"})
    idx = {(r["config"], r["id"]): r for r in per_q}
    for cfg in configs:
        if cfg == BASE:
            continue
        boot[cfg] = {}
        for m in ("final_recall@6", "final_mrr", "final_ndcg@6", "hybrid_recall@6", "hybrid_mrr", "dense_recall@6", "dense_mrr",
                  "evidence_label_recall"):
            boot[cfg][m] = bootstrap_diff([idx[(cfg, q)][m] for q in bq], [idx[(BASE, q)][m] for q in bq])

    # ---------------- equivalence with the baseline over every question (labelled + unlabelled + edge)
    equiv = {}
    for cfg in configs:
        rows = cfg_rows[cfg]
        e = {"questions": len(rows)}
        for key in ("dense_top100", "hybrid_top100", "final_top6", "evidence"):
            e[f"{key}_identical"] = sum(rows[q][key] == base[q][key] for q in rows)
        e["dense_top6_identical"] = sum(rows[q]["dense_top100"][:6] == base[q]["dense_top100"][:6] for q in rows)
        e["n_exact_identical"] = sum(rows[q]["n_exact"] == base[q]["n_exact"] for q in rows)
        e["fused_len_mean"] = r4(statistics.mean(rows[q]["fused_len"] for q in rows if rows[q]["fused_len"]))
        e["dense_len_mean"] = r4(statistics.mean(rows[q]["dense_len"] for q in rows if rows[q]["dense_len"]))
        e["deterministic"] = sum(rows[q]["deterministic"] for q in rows)
        equiv[cfg] = e

    # differing questions: final top-6 or evidence differs from numpy
    diffs = []
    for cfg in configs:
        if cfg == BASE:
            continue
        for qid, row in cfg_rows[cfg].items():
            b = base[qid]
            if row["final_top6"] != b["final_top6"] or row["evidence"] != b["evidence"]:
                d = {"config": cfg, "id": qid, "set": row["set"], "q": row["q"],
                     "removed_from_top6": [c for c in b["final_top6"] if c not in row["final_top6"]],
                     "added_to_top6": [c for c in row["final_top6"] if c not in b["final_top6"]],
                     "top6_same_set_reordered": set(row["final_top6"]) == set(b["final_top6"]) and row["final_top6"] != b["final_top6"],
                     "evidence_removed": [c for c, _ in b["evidence"] if c not in {x for x, _ in row["evidence"]}],
                     "evidence_added": [c for c, _ in row["evidence"] if c not in {x for x, _ in b["evidence"]}]}
                if (cfg, qid) in idx:
                    for m in ("final_recall@6", "final_mrr", "final_ndcg@6", "evidence_label_recall"):
                        d[m] = [r4(idx[(BASE, qid)][m]), r4(idx[(cfg, qid)][m])]
                # cause attribution for chroma: same as exact FAISS at the same depth -> truncation; else HNSW approximation
                if cfg.startswith("chroma"):
                    twin = "faiss_flat" + ("" if cfg == "chroma_full" else cfg[len("chroma"):])
                    d["same_as_faiss_exact_same_depth"] = (row["final_top6"] == cfg_rows[twin][qid]["final_top6"]
                                                           and row["evidence"] == cfg_rows[twin][qid]["evidence"])
                diffs.append(d)

    # demo evidence checks (verify_demo.QUESTIONS predicates) and unlabelled overlap
    demo = {}
    for cfg in configs:
        res = {}
        for spec in sets["demo"]:
            row = cfg_rows[cfg]["DEMO-" + spec["id"]]
            ev = [{"label": f"E{i}", "chunk_id": c, "origin": o, "ku_id": by_id[c]["ku_id"]} for i, (c, o) in enumerate(row["evidence"], 1)]
            res[spec["id"]] = bool(spec["evidence"](ev))
        demo[cfg] = res
    unl = {}
    for cfg in configs:
        ov = []
        for qid, row in cfg_rows[cfg].items():
            if row["set"] in ("probe", "demo") or (qinfo.get(qid) or {}).get("answerability") == "none":
                b = set(base[qid]["final_top6"])
                ov.append(len(b & set(row["final_top6"])) / len(b) if b else 1.0)
        unl[cfg] = {"n": len(ov), "mean_top6_overlap_with_numpy": r4(statistics.mean(ov)), "identical": sum(x == 1.0 for x in ov)}

    # ---------------- latency (all non-edge questions x reps)
    emb = step0["embedding_latency"]["per_question_median_ms"]
    lat = {}
    for b, r in runs.items():
        for cfg, v in r["runs"].items():
            parts = defaultdict(list)
            per_question = []
            for row in v["rows"]:
                if row["set"] == "edge":
                    continue
                t = row["timing_s"]
                for k in ("total", "bm25", "dense", "fusion", "post"):
                    parts[k] += [x * 1000 for x in t[k] if x is not None]
                parts["total_plus_embedding"] += [x * 1000 + emb[row["q"]] for x in t["total"]]
                per_question.append((statistics.median(t["total"]) * 1000, row["id"], row["q"][:70]))
            lat[cfg] = {k: {"n": len(xs), "median": r4(statistics.median(xs)), "p90": r4(pct(xs, 90)), "p95": r4(pct(xs, 95)),
                            "max": r4(max(xs))} for k, xs in parts.items()}
            lat[cfg]["slowest_questions_median_ms"] = [[r4(a), i, q] for a, i, q in sorted(per_question, reverse=True)[:5]]
            lat[cfg]["micro"] = r["dense_micro"].get(cfg)

    # ---------------- check summary
    checks = []
    checks += [{"backend": "all", "config": "-", "check": c["check"], "passed": c["passed"], "detail": str(c["mismatches"][:3]) if c["mismatches"] else ""}
               for c in step0["checks"]]
    for b, r in runs.items():
        for c in r["integrity_checks"]:
            checks.append({"backend": b, "config": "-", "check": c["check"], "passed": c["passed"],
                           "detail": "; ".join(f"{k}={v}" for k, v in c.items() if k in ("max_abs_err", "count", "checked", "ntotal"))})
        for cfg, v in r["runs"].items():
            names = sorted({k for row in v["rows"] for k in row["checks"]})
            for n in names:
                fails = [row["id"] for row in v["rows"] if not row["checks"][n]]
                checks.append({"backend": b, "config": cfg, "check": n, "passed": not fails,
                               "detail": f"{len(v['rows']) - len(fails)}/{len(v['rows'])} questions" + (f"; failing: {fails[:8]}" if fails else "")})
            nd = [row["id"] for row in v["rows"] if not row["deterministic"]]
            checks.append({"backend": b, "config": cfg, "check": f"deterministic across {r['reps']} repetitions (top-100 ranking + evidence)",
                           "passed": not nd, "detail": f"non-deterministic: {nd}" if nd else f"{len(v['rows'])} questions"})
            checks.append({"backend": b, "config": cfg, "check": "no exceptions", "passed": not v["errors"],
                           "detail": "; ".join(e["error"] for e in v["errors"][:3])})
            empty = [row for row in v["rows"] if row["id"] in ("EDGE-empty", "EDGE-blank")]
            checks.append({"backend": b, "config": cfg, "check": "empty / blank query returns no evidence (no dense call)",
                           "passed": all(not row["evidence"] and not row["dense_top100"] for row in empty), "detail": f"{len(empty)} queries"})
        sc = r["score_equivalence"]
        if b != "numpy":
            checks.append({"backend": b, "config": "-", "check": "similarity == NumPy cosine for identical window ids (|err| < 1e-5)",
                           "passed": sc["max_abs_score_err"] < 1e-5, "detail": f"max |err| = {sc['max_abs_score_err']:.3g}"})
            checks.append({"backend": b, "config": "full", "check": "full-depth query returns all 25,325 windows",
                           "passed": sc["returned_counts_full"]["min"] == 25325, "detail": str(sc["returned_counts_full"])})
    for cfg, res in demo.items():
        checks.append({"backend": cfg.split("_")[0].split("@")[0], "config": cfg, "check": "6 demo evidence checks (verify_demo.QUESTIONS)",
                       "passed": all(res.values()), "detail": str({k: v for k, v in res.items() if not v}) or "all 6"})

    out = {"aggregates": aggregates, "by_category": by_cat, "bootstrap_vs_numpy": boot, "equivalence": equiv, "differences": diffs,
           "demo_evidence_checks": demo, "unlabelled_overlap": unl, "latency_ms": lat, "checks": checks,
           "load": {b: r["load"] for b, r in runs.items()}, "memory_mb": {b: r["memory_mb"] for b, r in runs.items()},
           "persistent_size_bytes": {b: r["persistent_size_bytes"] for b, r in runs.items()},
           "score_equivalence": {b: r["score_equivalence"] for b, r in runs.items()}, "concurrency": {b: r["concurrency"] for b, r in runs.items()},
           "libraries": {b: r["libraries"] for b, r in runs.items()},
           "builds": {"faiss": load(os.path.join(OUT, "faiss", "flat_ip.index.meta.json")), "chroma": load(os.path.join(OUT, "chroma_build.json"))},
           "embedding_latency": {k: v for k, v in step0["embedding_latency"].items() if k != "per_question_median_ms"}}
    dump(os.path.join(OUT, "analysis.json"), out)

    def wcsv(name, rows, cols=None):
        cols = cols or list(rows[0].keys())
        with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)

    wcsv("per_query_metrics.csv", per_q)
    wcsv("aggregate_metrics.csv", [dict(config=c, set=s, **v) for c in configs for s, v in aggregates[c].items()])
    wcsv("per_category_metrics.csv", [dict(config=c, workflow=w, **v) for c in configs for w, v in by_cat[c].items()])
    wcsv("latency.csv", [dict(config=c, stage=k, **v) for c in configs for k, v in lat[c].items() if isinstance(v, dict) and "median" in v])
    wcsv("checks.csv", checks, ["backend", "config", "check", "passed", "detail"])
    wcsv("differences.csv", [{k: (" ".join(v) if isinstance(v, list) and v and isinstance(v[0], str) else v) for k, v in d.items()} for d in diffs])
    wcsv("bootstrap_vs_numpy.csv", [dict(config=c, metric=m, diff=v[0], lo95=v[1], hi95=v[2]) for c in boot for m, v in boot[c].items()])

    print("configs:", configs)
    for c in configs:
        a = aggregates[c]["benchmark"]
        e = equiv[c]
        print(f"{c:16} n={a['n']} final R@6={a['final_recall@6']} MRR={a['final_mrr']} nDCG@6={a['final_ndcg@6']} hit={a['final_hit@6']} "
              f"P@6={a['final_chunk_precision@6']} evR={a['evidence_label_recall']} | hybrid R@6={a['hybrid_recall@6']} MRR={a['hybrid_mrr']} "
              f"| dense R@6={a['dense_recall@6']} MRR={a['dense_mrr']} | identical final/ev {e['final_top6_identical']}/{e['evidence_identical']} of {e['questions']}")
    print("failed checks:", [(c["backend"], c["config"], c["check"], c["detail"]) for c in checks if not c["passed"]])
    print("differences:", len(diffs))


if __name__ == "__main__":
    main()
