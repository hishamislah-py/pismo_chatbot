"""Executive table (out/executive_summary.csv) and Markdown tables for REPORT.md, from measured outputs only.

    python -B -s report_tables.py > out/report_tables.md
"""
import csv
import os
import sys

from bench_lib import OUT, load

COLS = [("NumPy baseline", "numpy", "numpy"), ("FAISS exact (IndexFlatIP, full)", "faiss", "faiss_flat"),
        ("Chroma (HNSW, full depth)", "chroma", "chroma_full"), ("Chroma (HNSW, top-2,000 windows)", "chroma", "chroma@2000"),
        ("FAISS exact, top-2,000 windows", "faiss", "faiss_flat@2000")]


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    a = load(os.path.join(OUT, "analysis.json"))
    li = {b: load(os.path.join(OUT, f"latency_interleaved_{b}.json")) for b in ("faiss", "chroma")}
    mem = {b: load(os.path.join(OUT, f"memory_{b}.json")) for b in ("numpy", "faiss", "chroma")}
    e2e = {b: load(os.path.join(OUT, f"e2e_{b}.json"))["rows"] for b in ("numpy", "faiss", "chroma")}

    def inter(cfg, key, stat):
        src = li["chroma"] if cfg.startswith("chroma") else li["faiss"]
        return src[key][cfg][stat]

    def fails(backend, cfg):
        return sum(1 for c in a["checks"] if not c["passed"] and c["backend"] == backend and c["config"] in (cfg, "-", "full"))

    rows = []

    def row(name, f, unit=""):
        rows.append([name] + [f(b, c) for _, b, c in COLS] + [unit])

    agg = lambda c, m: a["aggregates"][c]["benchmark"][m]
    row("Label Recall@6 (final top-6)", lambda b, c: agg(c, "final_recall@6"))
    row("Chunk Precision@6 (final top-6, supplementary)", lambda b, c: agg(c, "final_chunk_precision@6"))
    row("MRR (final top-6)", lambda b, c: agg(c, "final_mrr"))
    row("nDCG@6 (label gain, final top-6)", lambda b, c: agg(c, "final_ndcg@6"))
    row("Hit rate@6 (final top-6)", lambda b, c: agg(c, "final_hit@6"))
    row("Evidence label recall (evidence sent to the model)", lambda b, c: agg(c, "evidence_label_recall"))
    row("Dense-only Label Recall@6", lambda b, c: agg(c, "dense_recall@6"))
    row("Dense-only MRR (depth 100)", lambda b, c: agg(c, "dense_mrr"))
    row("Final top-6 identical to baseline (of 132 questions)", lambda b, c: a["equivalence"][c]["final_top6_identical"])
    row("Dense-search median latency, interleaved", lambda b, c: inter(c, "dense_ms", "median"), "ms")
    row("Dense-search p90 latency, interleaved", lambda b, c: inter(c, "dense_ms", "p90"), "ms")
    row("Hybrid ranking median latency, interleaved (BM25+dense+RRF+promotion)", lambda b, c: inter(c, "hybrid_ranking_ms", "median"), "ms")
    row("Hybrid ranking p90 latency, interleaved", lambda b, c: inter(c, "hybrid_ranking_ms", "p90"), "ms")
    row("Full retrieval + evidence assembly median, per-process run", lambda b, c: a["latency_ms"][c]["total"]["median"], "ms")
    row("Full retrieval + evidence assembly p90, per-process run", lambda b, c: a["latency_ms"][c]["total"]["p90"], "ms")
    row("Index build/import time", lambda b, c: {"numpy": "0 (existing .npy)", "faiss": a["builds"]["faiss"]["build_and_write_seconds"],
                                                  "chroma": a["builds"]["chroma"]["add_and_first_query_seconds"]}[b], "s")
    row("Cold open + first query (fresh process)", lambda b, c: mem[b]["open_and_first_query_s"], "s")
    row("Index memory (RSS delta, clean process)", lambda b, c: mem[b]["index_rss_delta_mb"], "MB")
    row("Persistent index size", lambda b, c: round(a["persistent_size_bytes"][b] / 1e6, 1), "MB")
    row("Failed checks (integrity, equivalence, hybrid invariants, determinism, edge cases, demo evidence)", fails)
    row("Concurrency failures, 10 threads (calls failed / calls)",
        lambda b, c: (lambda v: f"{v['failed_calls']}/{v['calls']}" if v else "not run")(
            (li["chroma"] if b == "chroma" else li["faiss"])["concurrency_10_threads"].get(c)))
    row("E2E demo: evidence checks passed / answer checks passed (of 6)",
        lambda b, c: (lambda rs: f"{sum(r['evidence_ok'] for r in rs)}/{sum(r['answer_ok'] for r in rs)}" if rs else "not run")(
            [r for r in e2e[b] if r["config"] == c]))

    with open(os.path.join(OUT, "executive_summary.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["metric"] + [n for n, _, _ in COLS] + ["unit"])
        w.writerows(rows)
    print("| Metric | " + " | ".join(n for n, _, _ in COLS) + " |")
    print("|---|" + "---:|" * len(COLS))
    for r in rows:
        unit = f" ({r[-1]})" if r[-1] else ""
        print(f"| {r[0]}{unit} | " + " | ".join(str(x) for x in r[1:-1]) + " |")

    print("\n### Per-set results (final top-6 label Recall@6 / MRR / nDCG@6 / evidence label recall)\n")
    cfgs = list(a["aggregates"])
    print("| Config | " + " | ".join(f"{s} (n={a['aggregates']['numpy'][s]['n']})" for s in ("primary", "extension", "diagnostic", "webhook_v2")) + " |")
    print("|---|" + "---|" * 4)
    for c in cfgs:
        print(f"| {c} | " + " | ".join(f"{a['aggregates'][c][s]['final_recall@6']} / {a['aggregates'][c][s]['final_mrr']} / "
                                       f"{a['aggregates'][c][s]['final_ndcg@6']} / {a['aggregates'][c][s]['evidence_label_recall']}"
                                       for s in ("primary", "extension", "diagnostic", "webhook_v2")) + " |")

    print("\n### Per-category (benchmark, final top-6 label Recall@6; n per category)\n")
    cats = list(a["by_category"]["numpy"])
    show = ["numpy", "faiss_flat", "chroma_full", "faiss_flat@100", "chroma@100", "faiss_flat@500", "chroma@500", "faiss_flat@2000", "chroma@2000"]
    print("| Category | n | " + " | ".join(show) + " |")
    print("|---|---:|" + "---:|" * len(show))
    for w in cats:
        print(f"| {w} | {a['by_category']['numpy'][w]['n']} | " + " | ".join(str(a["by_category"][c][w]["final_recall@6"]) for c in show) + " |")

    print("\n### Paired bootstrap vs NumPy (benchmark, n=76, 2,000 resamples, seed 20261021): diff [95% CI]\n")
    ms = ("final_recall@6", "final_mrr", "final_ndcg@6", "evidence_label_recall", "dense_recall@6")
    print("| Config | " + " | ".join(ms) + " |")
    print("|---|" + "---|" * len(ms))
    for c, v in a["bootstrap_vs_numpy"].items():
        print(f"| {c} | " + " | ".join(f"{v[m][0]:+.4f} [{v[m][1]:+.4f}, {v[m][2]:+.4f}]" for m in ms) + " |")

    print("\n### Equivalence with the baseline (132 questions: 109 labelled, 18 unlabelled, 5 edge)\n")
    keys = ("dense_top6_identical", "dense_top100_identical", "hybrid_top100_identical", "final_top6_identical", "evidence_identical",
            "n_exact_identical", "dense_len_mean", "fused_len_mean", "deterministic")
    print("| Config | " + " | ".join(keys) + " |")
    print("|---|" + "---:|" * len(keys))
    for c, v in a["equivalence"].items():
        print(f"| {c} | " + " | ".join(str(v[k]) for k in keys) + " |")

    print("\n### Interleaved latency (ms; 84 benchmark questions x 7 rounds, same process)\n")
    print("| Process | Config | dense median | dense p90 | dense p95 | hybrid median | hybrid p90 | hybrid p95 |")
    print("|---|---|---:|---:|---:|---:|---:|---:|")
    for b, v in li.items():
        for c in v["dense_ms"]:
            d, h = v["dense_ms"][c], v["hybrid_ranking_ms"][c]
            print(f"| {b} run | {c} | {d['median']} | {d['p90']} | {d['p95']} | {h['median']} | {h['p90']} | {h['p95']} |")

    print("\n### Stage latency, per-process runs (ms; 127 questions x 5 reps; cross-process noise ~+/-40%)\n")
    print("| Config | BM25 med | dense med | fusion med | post (nav/scope/assembly) med | total med | total p90 | total p95 | total max | total + query embedding med |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|")
    for c, v in a["latency_ms"].items():
        print(f"| {c} | {v['bm25']['median']} | {v['dense']['median']} | {v['fusion']['median']} | {v['post']['median']} | "
              f"{v['total']['median']} | {v['total']['p90']} | {v['total']['p95']} | {v['total']['max']} | {v['total_plus_embedding']['median']} |")

    print("\n### Concurrency, per-process runs (throughput qps / median latency ms)\n")
    print("| Config | dense@1 | dense@5 | dense@10 | hybrid@1 | hybrid@5 | hybrid@10 |")
    print("|---|---|---|---|---|---|---|")
    for b, v in a["concurrency"].items():
        for c, cc in v.items():
            cell = lambda k: (f"{cc[k]['throughput_qps']} / {cc[k]['latency_ms']['median']}" if "throughput_qps" in cc[k] else f"FAILED: {cc[k]['error'][:60]}")
            print(f"| {c} | " + " | ".join(cell(f"{k}@{n}") for k in ("dense", "hybrid_ranking") for n in (1, 5, 10)) + " |")


if __name__ == "__main__":
    main()
