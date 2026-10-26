"""Compare the served index (results/) with a candidate index (candidates/<name>/) using identical retrieval settings,
the frozen benchmark (unchanged) and a separate regression set. Offline: no OpenAI calls, no network. Read-only on both
indexes and on the KU collections; writes candidates/<name>/evaluation.json, or <out.json> when given.

Usage: python -B -E -s scripts/compare_candidate.py <ku_collection_dir> <name> <regression_set.json> [<out.json>]
"""
import json
import os
import sys

os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", OPENAI_API_KEY="")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
import common  # noqa: E402
import corpus  # noqa: E402
from pismo_assistant import audit_retrieval as ar, config  # noqa: E402
from pismo_assistant.pipeline import Assistant  # noqa: E402
from pismo_assistant.retrieval import HybridRetriever, is_navigation  # noqa: E402

TARGET = "KU-EVT-verifying-webhook-requests"


def load(chunks_path, summary_path, emb_dir, mig, embedder=None):
    """HybridRetriever reads these module paths; each index is verified against its own KU collection."""
    config.CORPUS_SUMMARY_PATH, config.EMBEDDINGS_DIR = summary_path, emb_dir
    corpus.MIG, corpus.KU_DIR = mig, os.path.join(mig, "knowledge_units")
    return Assistant(retriever=HybridRetriever(chunks_path=chunks_path, check_ku_files=True, embedder=embedder))


def regression_questions(path, chunks):
    import build_benchmark
    raw = common.load_json(path)
    ku_text, build_benchmark.ku_files = {}, {}
    for c in chunks:
        ku_text[c["ku_id"]] = ku_text.get(c["ku_id"], "") + "\n" + c["text"]
        build_benchmark.ku_files[c["ku_id"]] = c["ku_sources"]
    return [build_benchmark.build_question(q, chunks, ku_text, "regression") for q in raw["questions"]]


def trace(a, q):
    r = a.retriever
    order, _ = r.ranked(q)
    pos = [k + 1 for k, i in enumerate(order) if r.chunks[i]["ku_id"] == TARGET]
    content = [k + 1 for k, i in enumerate(order) if r.chunks[i]["ku_id"] == TARGET and not is_navigation(r.chunks[i])]
    ev = a.evidence(q)
    return {"top10": [{"rank": k + 1, "chunk_id": r.chunks[i]["chunk_id"], "ku_id": r.chunks[i]["ku_id"],
                       "title": r.chunks[i]["ku_title"], "nav": is_navigation(r.chunks[i])} for k, i in enumerate(order[:10])],
            "target_best_rank": pos[0] if pos else None, "target_best_content_rank": content[0] if content else None,
            "evidence": [{"label": e.label, "chunk_id": e.chunk_id, "ku_id": e.ku_id, "origin": e.origin, "flags": e.flags} for e in ev],
            "target_in_evidence": sum(e.ku_id == TARGET for e in ev),
            "sc10_caveat_in_evidence": any("Source contradiction (SC-10)" in e.text for e in ev)}


def run(a, questions):
    by_id = {c["chunk_id"]: c for c in a.retriever.chunks}
    rows = [ar.evaluate_question(q, a, by_id) for q in questions]
    return rows, {s: ar.aggregate([x for x in rows if x["set"] == s]) for s in sorted({x["set"] for x in rows})}


def main(argv):
    mig, name, reg_path = os.path.abspath(argv[0]), argv[1], os.path.abspath(argv[2])
    cand = os.path.join(common.EXP, "candidates", name)
    bench = common.load_json(ar.BENCHMARK)
    frozen = open(ar.BENCHMARK_SHA, encoding="utf-8").read().split()[0]
    assert common.sha_json({"primary": bench["primary"], "extension": bench["extension"]}) == frozen, "frozen benchmark changed"
    out = {"benchmark_sha256": frozen, "regression_set": os.path.relpath(reg_path, common.EXP).replace(os.sep, "/"),
           "regression_set_sha256": common.sha_file(reg_path),
           "settings": {"top_k": config.TOP_K, "rrf_weights": config.RRF_WEIGHTS,
                        "exclude_nav_from_top_k": config.EXCLUDE_NAV_FROM_TOP_K}, "indexes": {}}
    base = load(config.CHUNKS_PATH, config.CORPUS_SUMMARY_PATH, config.EMBEDDINGS_DIR, common.MIG)
    new = load(os.path.join(cand, "chunks.jsonl"), os.path.join(cand, "corpus_summary.json"), os.path.join(cand, "embeddings"), mig,
               embedder=base.retriever.embedder)
    for tag, a in (("baseline", base), ("candidate", new)):
        qs = bench["primary"] + bench["extension"] + ar.resolve_diagnostic(a.retriever.chunks)
        rows, agg = run(a, qs)
        reg_qs = regression_questions(reg_path, a.retriever.chunks)
        reg_rows, reg_agg = run(a, reg_qs)
        out["indexes"][tag] = {
            "chunk_set_hash": a.retriever.chunk_set_hash, "frozen_aggregates": agg, "regression_aggregates": reg_agg,
            "frozen_rows": {x["id"]: {k: x.get(k) for k in ("recall@5", "recall@10", "rr", "evidence_label_recall", "outcome")}
                            | {"evidence": [e["chunk_id"] for e in x["evidence"]]} for x in rows},
            "regression_rows": {x["id"]: {k: x.get(k) for k in ("question", "recall@5", "recall@10", "rr", "evidence_label_recall",
                                                                "evidence_ku_recall", "outcome", "first_relevant_rank",
                                                                "distractors_in_evidence", "required_statement_in_evidence")}
                                | trace(a, x["question"]) for x in reg_rows},
            "regression_label_status": {q["id"]: [l["status"] for l in q["labels"]] for q in reg_qs},
        }
    path = os.path.abspath(argv[3]) if len(argv) > 3 else os.path.join(cand, "evaluation.json")
    common.dump_json(path, out)
    print("written", path)
    return out


if __name__ == "__main__":
    main(sys.argv[1:])
