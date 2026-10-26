"""Retrieval / evidence-assembly audit over the frozen benchmark (43 primary + 41 extension questions) and a separately
labelled diagnostic set. Retrieval only: no OpenAI call is made.

For every question it records the full hybrid ranking (top 10 shown), the exact evidence set the assistant would send to
the model (top-k retrieved + assembled additions), and scores the frozen gold labels against both.

    python -B -s -m pismo_assistant.audit_retrieval --tag baseline
    python -B -s -m pismo_assistant.audit_retrieval --tag after --compare docs/audit_runs/retrieval_baseline.json
"""
import argparse
import json
import os
import re
import sys
import time

from . import config

AUDIT_DIR = os.path.join(config.ROOT, "docs", "audit_runs")
BENCHMARK = os.path.join(config.EXPERIMENT, "BENCHMARK.json")
BENCHMARK_SHA = os.path.join(config.EXPERIMENT, "BENCHMARK.sha256")

# Diagnostic questions: authored for this audit BEFORE any fix, never merged into the frozen benchmark. Labels use the
# benchmark format ({file|ku, match}) plus {chunk_prefix, match} for a specific operation's chunks.
DIAGNOSTIC = [
    {"id": "DG01", "workflow": "NL operation", "type": "natural", "q": "How do I cancel a transfer?",
     "expected": [{"chunk_prefix": "KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers-cancel"},
                  {"file": "docs/core-platform/cancel-transfer.md"}]},
    {"id": "DG02", "workflow": "NL operation (paraphrase)", "type": "natural", "q": "How do I send money from one customer account to another?",
     "expected": [{"chunk_prefix": "KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers"}]},
    {"id": "DG03", "workflow": "operationId", "type": "exact", "q": "What does post-payments-v1-hold-funds-block require?",
     "expected": [{"chunk_prefix": "KU-API-core-platform-payment-methods--hold-funds::op-post-payments-v1-hold-funds-block", "match": "Request body"}]},
    {"id": "DG04", "workflow": "endpoint path", "type": "exact", "q": "POST /payments/v1/payments/hold-funds/transfer",
     "expected": [{"chunk_prefix": "KU-API-core-platform-payment-methods--hold-funds::op-post-payments-v1-hold-funds-transfer"}]},
    {"id": "DG05", "workflow": "required fields", "type": "natural", "q": "Which fields are required to create a transfer?",
     "expected": [{"chunk_prefix": "KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers", "match": r"\| yes \|"}]},
    {"id": "DG06", "workflow": "operation to event", "type": "exact", "q": "Which events does PostPciCardsV1 generate?",
     "expected": [{"chunk_prefix": "KU-API-migrations--card-migration::op-postpcicardsv1", "match": "Events emitted"}]},
    {"id": "DG07", "workflow": "webhook troubleshooting", "type": "natural", "q": "Why does my webhook signature verification fail and how do I check the body hash?",
     "expected": [{"file": "docs/get-started/verifying-webhook-requests.md", "match": "body-hash"}]},
    {"id": "DG08", "workflow": "historical / removed", "type": "natural", "q": "Can I still use the Create marketplace V2 endpoint?",
     "expected": [{"ku": "KU-LIFE-marketplace-endpoint-removal"}, {"file": "docs/resources/api-endpoints-removed.md", "match": "10/6/26"}],
     "lifecycle_sensitive": True},
    {"id": "DG09", "workflow": "multi-KU workflow", "type": "natural", "q": "How do I migrate cards and then make the migrated accounts go live?",
     "expected": [{"chunk_prefix": "KU-API-migrations--card-migration::op-postcardsv1"}, {"chunk_prefix": "KU-API-migrations--account-migration::op-postgolivev1"}]},
    {"id": "DG10", "workflow": "error code in sentence", "type": "exact", "q": "Creating a hold returned EHLD0016 - what is wrong?",
     "expected": [{"file": "api-reference-data/error_code_index.csv", "match": "EHLD0016"}]},
]

def is_nav(chunk):
    from .retrieval import is_navigation
    return is_navigation(chunk)


def diag_satisfies(chunk, label):
    from labels import chunk_satisfies
    if "chunk_prefix" in label:
        if not chunk["chunk_id"].startswith(label["chunk_prefix"]):
            return False
        return bool(re.search(label["match"], chunk["text"], re.I)) if label.get("match") else True
    return chunk_satisfies(chunk, label)


def resolve_diagnostic(chunks):
    out = []
    for q in DIAGNOSTIC:
        labels = []
        for l in q["expected"]:
            ids = [c["chunk_id"] for c in chunks if diag_satisfies(c, l)]
            labels.append({"key": json.dumps(l, sort_keys=True), "status": "valid" if ids else "no_matching_chunk",
                           "relevant_chunk_ids": ids, "relevant_ku_ids": sorted({i.split("::")[0] for i in ids})})
        out.append(dict(q, set="diagnostic", labels=labels, scored=True, answerability="full"))
    return out


def evaluate_question(q, assistant, chunks_by_id):
    r = assistant.retriever
    order, n_exact = r.ranked(q["q"])
    top = [r.chunks[i] for i in order[:100]]
    ev = assistant.evidence(q["q"])
    ev_ids = [e.chunk_id for e in ev]
    valid = [l for l in q["labels"] if l["status"] == "valid"]
    sets = [set(l["relevant_chunk_ids"]) for l in valid]
    ku_sets = [set(l["relevant_ku_ids"]) for l in valid]

    def first_rank(ids):
        return next((i + 1 for i, c in enumerate(ids) if any(c in s for s in sets)), None)

    def label_recall(ids):
        return sum(1 for s in sets if s & set(ids)) / len(sets) if sets else None

    top_ids = [c["chunk_id"] for c in top]
    fr = first_rank(top_ids)
    ev_recall = label_recall(ev_ids)
    ev_kus = {chunks_by_id[i]["ku_id"] for i in ev_ids}
    ku_in_ev = sum(1 for s in ku_sets if s & ev_kus) / len(ku_sets) if ku_sets else None
    rec = {
        "id": q["id"], "set": q["set"], "workflow": q.get("workflow"), "type": q.get("type"), "answerability": q.get("answerability"),
        "question": q["q"], "expected_labels": [l["key"] for l in q["labels"]], "label_status": [l["status"] for l in q["labels"]],
        "expected_ku_ids": sorted({k for s in ku_sets for k in s}),
        "top10": [{"rank": i + 1, "chunk_id": c["chunk_id"], "ku_id": c["ku_id"], "title": c["ku_title"],
                   "relevant": any(c["chunk_id"] in s for s in sets), "nav": is_nav(c)} for i, c in enumerate(top[:10])],
        "first_relevant_rank": fr, "rr": (1 / fr) if fr else 0.0,
        "recall@5": label_recall(top_ids[:5]), "recall@10": label_recall(top_ids[:10]),
        "evidence": [{"label": e.label, "chunk_id": e.chunk_id, "origin": e.origin, "relevant": any(e.chunk_id in s for s in sets),
                      "nav": is_nav(chunks_by_id[e.chunk_id])} for e in ev],
        "evidence_label_recall": ev_recall, "evidence_all_labels": (ev_recall == 1.0) if sets else None,
        "evidence_ku_recall": ku_in_ev, "evidence_nav_chunks": sum(1 for e in ev if is_nav(chunks_by_id[e.chunk_id])),
        "evidence_chars": sum(len(e.text) for e in ev), "n_exact_promoted": n_exact,
    }
    # misleading near-matches / safety signals
    if q.get("distractors"):
        rec["distractors_in_evidence"] = [rx for rx in q["distractors"] if any(re.search(rx, e.text, re.I) for e in ev)]
    if q.get("required_statement_check"):
        tg = set(q["required_statement_check"]["targets"])
        rec["required_statement_in_evidence"] = bool(tg & ev_kus)
    if q.get("lifecycle_sensitive"):
        rec["lifecycle_signal_in_evidence"] = any(e.origin == "lifecycle" or {"removal_register", "unresolved_operation_link", "historical_changelog"} & set(e.flags)
                                                  or "Lifecycle note" in e.text for e in ev)
    # outcome and first-pass cause hint (refined manually in docs/FULL_RETRIEVAL_AUDIT.md)
    if not sets:
        rec["outcome"] = "unscored (unanswerable)" if q.get("answerability") == "none" else "no valid label"
    elif ev_recall == 1.0:
        rec["outcome"] = "pass"
    elif ev_recall and ev_recall > 0:
        rec["outcome"] = "partial"
    else:
        rec["outcome"] = "fail"
    if rec["outcome"] in ("partial", "fail"):
        if ku_in_ev and ku_in_ev >= (ev_recall or 0) and ku_in_ev > (ev_recall or 0):
            rec["cause_hint"] = "right KU in evidence, labelled chunk not (chunk selection/construction)"
        elif fr and fr <= 20:
            rec["cause_hint"] = f"near miss: first relevant at rank {fr} (ranking / top-k)"
        elif fr:
            rec["cause_hint"] = f"ranking miss: first relevant at rank {fr}"
        else:
            rec["cause_hint"] = "not in top 100 (query/vocabulary or missing relationship)"
        if rec["evidence_nav_chunks"]:
            rec["cause_hint"] += f"; {rec['evidence_nav_chunks']} KU-navigation chunk(s) occupy evidence slots"
    return rec


def aggregate(rows):
    sc = [r for r in rows if r["evidence_label_recall"] is not None]
    mean = lambda xs: round(sum(xs) / len(xs), 4) if xs else None
    return {"n": len(rows), "scored": len(sc),
            "pass": sum(r["outcome"] == "pass" for r in sc), "partial": sum(r["outcome"] == "partial" for r in sc),
            "fail": sum(r["outcome"] == "fail" for r in sc),
            "evidence_label_recall": mean([r["evidence_label_recall"] for r in sc]),
            "evidence_all_labels": mean([float(r["evidence_all_labels"]) for r in sc]),
            "recall@5": mean([r["recall@5"] for r in sc]), "recall@10": mean([r["recall@10"] for r in sc]),
            "mrr": mean([r["rr"] for r in sc]),
            "evidence_nav_chunks_mean": mean([r["evidence_nav_chunks"] for r in rows]),
            "evidence_chars_mean": mean([r["evidence_chars"] for r in rows])}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tag", default="run")
    ap.add_argument("--compare", default=None)
    a = ap.parse_args(argv)
    sys.stdout.reconfigure(encoding="utf-8")
    os.environ.setdefault("HF_HUB_OFFLINE", "1")
    os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
    config.ensure_experiment_on_path()
    from common import sha_json
    from .pipeline import Assistant
    bench = json.load(open(BENCHMARK, encoding="utf-8"))
    frozen = open(BENCHMARK_SHA, encoding="utf-8").read().split()[0]
    if sha_json({"primary": bench["primary"], "extension": bench["extension"]}) != frozen:
        print("FROZEN BENCHMARK HASH MISMATCH - refusing to run")
        return 2
    t = time.time()
    assistant = Assistant()
    by_id = {c["chunk_id"]: c for c in assistant.retriever.chunks}
    questions = bench["primary"] + bench["extension"] + resolve_diagnostic(assistant.retriever.chunks)
    rows = [evaluate_question(q, assistant, by_id) for q in questions]
    out = {"tag": a.tag, "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "benchmark_sha256": frozen,
           "config": {"top_k": config.TOP_K, "rrf_weights": config.RRF_WEIGHTS,
                      "exclude_nav_from_top_k": getattr(config, "EXCLUDE_NAV_FROM_TOP_K", False)},
           "aggregates": {s: aggregate([r for r in rows if r["set"] == s]) for s in ("primary", "extension", "diagnostic")},
           "questions": rows, "seconds": round(time.time() - t, 1)}
    os.makedirs(AUDIT_DIR, exist_ok=True)
    path = os.path.join(AUDIT_DIR, f"retrieval_{a.tag}.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    base = json.load(open(a.compare, encoding="utf-8")) if a.compare else None
    print(f"\nRETRIEVAL AUDIT [{a.tag}]  config={out['config']}  ({out['seconds']}s, no OpenAI calls)")
    for s, g in out["aggregates"].items():
        line = (f"  {s:10} n={g['n']:2} scored={g['scored']:2} pass={g['pass']:2} partial={g['partial']:2} fail={g['fail']:2} | "
                f"evidence label recall={g['evidence_label_recall']} all-labels={g['evidence_all_labels']} | "
                f"R@5={g['recall@5']} R@10={g['recall@10']} MRR={g['mrr']} | nav chunks/evidence={g['evidence_nav_chunks_mean']}")
        print(line)
        if base:
            b = base["aggregates"][s]
            print(f"  {'':10} baseline: pass={b['pass']} partial={b['partial']} fail={b['fail']} evidence label recall={b['evidence_label_recall']} "
                  f"all-labels={b['evidence_all_labels']} R@5={b['recall@5']} MRR={b['mrr']} nav={b['evidence_nav_chunks_mean']}")
    print("  failed / partial questions:")
    for r in rows:
        if r["outcome"] in ("partial", "fail"):
            print(f"    {r['id']:8} {r['outcome']:7} ev-recall={r['evidence_label_recall']:.2f} rank={r['first_relevant_rank']}  {r['question'][:60]}  -> {r.get('cause_hint')}")
    if base:
        bb = {r["id"]: r for r in base["questions"]}
        ch = [(r["id"], bb[r["id"]]["outcome"], r["outcome"], bb[r["id"]]["evidence_label_recall"], r["evidence_label_recall"])
              for r in rows if r["id"] in bb and (bb[r["id"]]["outcome"] != r["outcome"] or bb[r["id"]]["evidence_label_recall"] != r["evidence_label_recall"])]
        print("  changed vs baseline:" + ("" if ch else " none"))
        for c in ch:
            print(f"    {c[0]:8} {c[1]} -> {c[2]}   evidence label recall {c[3]} -> {c[4]}")
    print(f"  written: {os.path.relpath(path, config.ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
