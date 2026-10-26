"""Reproducible retrieval comparison of the served index (v1) and the candidates v1.1 and v1.2, with identical retrieval
settings, plus a v1.2 ablation without procedure expansion. Offline: no OpenAI calls, no network. Read-only on every
index and KU collection; writes one JSON file.

Metrics use only existing labels: the frozen benchmark (BENCHMARK.json + audit DIAGNOSTIC), and the reviewed regression
sets in benchmark_inputs/. The probe set is unlabelled: it gets rankings, evidence, noise and contamination checks only.

Usage: python -B -E -s scripts/compare_versions.py <out.json>
"""
import json
import os
import sys
import time

os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", OPENAI_API_KEY="")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
import common  # noqa: E402
import compare_candidate as cc  # noqa: E402
from pismo_assistant import audit_retrieval as ar, config  # noqa: E402
from pismo_assistant.evidence import assemble  # noqa: E402
from pismo_assistant.pipeline import Assistant  # noqa: E402
from pismo_assistant.retrieval import is_navigation  # noqa: E402
from retrievers import RRF_K, detect_identifiers, exact_rerank, rank_by_score, rrf  # noqa: E402

H, EXP = common.HANDOFF, common.EXP
VERSIONS = {  # name -> (index folder, KU collection)
    "v1": (common.RESULTS, common.MIG),
    "v1.1": (os.path.join(EXP, "candidates", "ku_v1_1"), os.path.join(H, "pismo_knowledge_units_migration_v1_1")),
    "v1.2": (os.path.join(EXP, "candidates", "ku_v1_2"), os.path.join(H, "pismo_knowledge_units_migration_v1_2")),
}
REG_SETS = {"regression_v1": "regression_webhook_auth_v1.json", "regression_v2": "regression_webhook_auth_v2.json"}
PROBES = "probe_questions_unlabelled_v1.json"
WEBHOOK_KU = "KU-EVT-verifying-webhook-requests"
DATA_PLATFORM_KU = "KU-EVT-pismo-data-platform-http-integration-guide-beta"
DATA_PLATFORM_URL = "prod.pismo.io"


class NoExpansion(Assistant):
    """Ablation: v1.2 evidence without the procedure-step expansion (everything else identical)."""

    def evidence(self, question):
        return assemble(self.retriever.search(question, k=self.top_k), self.op_index, question=question, max_procedure=0)


def detailed_ranking(r, q):
    """The retriever's own ranking (HybridRetriever.ranked) with per-method ranks and scores."""
    bm = r.bm25.scores(q)
    dn = r.dense.scores(r.embedder.encode([q], normalize_embeddings=True, convert_to_numpy=True)[0])
    b_order, d_order = rank_by_score(bm, r.ids, positive_only=True), rank_by_score(dn, r.ids)
    fused = rrf([b_order, d_order], list(config.RRF_WEIGHTS), r.ids)
    final, n_exact = exact_rerank(fused, r.texts_lower, detect_identifiers(q))
    assert (final, n_exact) == r.ranked(q), "ranking replica differs from HybridRetriever.ranked"
    pb, pd = {i: k + 1 for k, i in enumerate(b_order)}, {i: k + 1 for k, i in enumerate(d_order)}
    rows = []
    for k, i in enumerate(final[:10], 1):
        c = r.chunks[i]
        rows.append({"rank": k, "chunk_id": c["chunk_id"], "ku_id": c["ku_id"], "source": c.get("source_path") or "(KU-generated)",
                     "section": c["section_heading"], "nav": is_navigation(c),
                     "method": "exact identifier promotion + hybrid" if k <= n_exact else "hybrid (BM25 x2 + dense x1, RRF k=60)",
                     "fused_rrf": round(sum(w / (RRF_K + p[i]) for w, p in zip(config.RRF_WEIGHTS, (pb, pd)) if i in p), 6),
                     "bm25_rank": pb.get(i), "bm25": round(float(bm[i]), 3), "dense_rank": pd.get(i), "cosine": round(float(dn[i]), 4)})
    return rows, n_exact


def relevant_sets(q):
    valid = [l for l in q.get("labels", []) if l["status"] == "valid"]
    return {c for l in valid for c in l["relevant_chunk_ids"]}, {k for l in valid for k in l["relevant_ku_ids"]}


def record(a, q, labelled, by_id):
    r = a.retriever
    t = time.perf_counter()
    top10, n_exact = detailed_ranking(r, q["q"])
    ev = a.evidence(q["q"])
    ms = round((time.perf_counter() - t) * 1000)
    rel_c, rel_k = relevant_sets(q) if labelled else (set(), set())
    out = {"id": q["id"], "question": q["q"], "labelled": labelled, "n_exact": n_exact, "retrieval_and_assembly_ms": ms,
           "expected_labels": [l["key"] for l in q.get("labels", [])] if labelled else None,
           "label_status": [l["status"] for l in q.get("labels", [])] if labelled else None,
           "top10": [dict(x, relevant=(x["chunk_id"] in rel_c) if labelled else None) for x in top10],
           "evidence": [{"label": e.label, "chunk_id": e.chunk_id, "ku_id": e.ku_id, "section": e.section[-90:], "origin": e.origin,
                         "kind": "top-k retrieval" if e.origin == "retrieved" else f"expansion: {e.origin}",
                         "relevant": (e.chunk_id in rel_c) if labelled else None,
                         "same_ku_as_label": (e.ku_id in rel_k) if labelled else None} for e in ev],
           "data_platform_in_evidence": any(e.ku_id == DATA_PLATFORM_KU for e in ev),
           "data_platform_url_in_evidence": any(DATA_PLATFORM_URL in e.text for e in ev),
           "webhook_ku_passages": sum(e.ku_id == WEBHOOK_KU for e in ev)}
    if labelled:
        m = ar.evaluate_question(q, a, by_id)
        out.update({k: m.get(k) for k in ("recall@5", "recall@10", "rr", "first_relevant_rank", "evidence_label_recall",
                                          "evidence_ku_recall", "outcome", "distractors_in_evidence", "required_statement_in_evidence")})
        out["noise"] = sum(1 for e in out["evidence"] if not e["relevant"] and not e["same_ku_as_label"])
    return out


def main(argv):
    out_path = os.path.abspath(argv[0])
    bench = common.load_json(ar.BENCHMARK)
    frozen_sha = open(ar.BENCHMARK_SHA, encoding="utf-8").read().split()[0]
    assert common.sha_json({"primary": bench["primary"], "extension": bench["extension"]}) == frozen_sha, "frozen benchmark changed"
    inputs = {s: os.path.join(EXP, "benchmark_inputs", f) for s, f in list(REG_SETS.items()) + [("probe", PROBES)]}
    res = {"generated_at": time.strftime("%Y-%m-%d %H:%M:%S"), "frozen_benchmark_sha256": frozen_sha,
           "inputs_sha256": {s: common.sha_file(p) for s, p in inputs.items()},
           "settings": {"top_k": config.TOP_K, "rrf_weights": config.RRF_WEIGHTS, "rrf_k": RRF_K,
                        "exclude_nav_from_top_k": config.EXCLUDE_NAV_FROM_TOP_K, "max_linked_operations": config.MAX_LINKED_OPERATIONS,
                        "max_event_chunks": config.MAX_EVENT_CHUNKS, "max_lifecycle_chunks": config.MAX_LIFECYCLE_CHUNKS,
                        "max_procedure_steps": config.MAX_PROCEDURE_STEPS},
           "versions": {}}
    probes = common.load_json(inputs["probe"])["questions"]
    embedder = None
    for name, (idx, mig) in VERSIONS.items():
        a = cc.load(os.path.join(idx, "chunks.jsonl"), os.path.join(idx, "corpus_summary.json"), os.path.join(idx, "embeddings"), mig,
                    embedder=embedder)
        embedder = a.retriever.embedder
        runs = [(name, a)] + ([("v1.2-no-expansion", NoExpansion(retriever=a.retriever, op_index=a.op_index))] if name == "v1.2" else [])
        for tag, asst in runs:
            by_id = {c["chunk_id"]: c for c in asst.retriever.chunks}
            sets = {"frozen": bench["primary"] + bench["extension"] + ar.resolve_diagnostic(asst.retriever.chunks)}
            for s in REG_SETS:
                sets[s] = cc.regression_questions(inputs[s], asst.retriever.chunks)
            v = {"chunk_set_hash": asst.retriever.chunk_set_hash, "ku_collection": os.path.relpath(mig, H).replace(os.sep, "/"),
                 "questions": {}, "aggregates": {}}
            for s, qs in sets.items():
                rows = [record(asst, q, True, by_id) for q in qs]
                v["questions"][s] = rows
                ev_rows = [ar.evaluate_question(q, asst, by_id) for q in qs]
                agg = {}
                for sub in sorted({x["set"] for x in ev_rows}):
                    pick = [i for i, x in enumerate(ev_rows) if x["set"] == sub]
                    agg[sub] = ar.aggregate([ev_rows[i] for i in pick]) | {
                        "noise_mean": round(sum(rows[i]["noise"] for i in pick) / len(pick), 3),
                        "data_platform_url_in_evidence": sum(rows[i]["data_platform_url_in_evidence"] for i in pick)}
                v["aggregates"][s] = agg
            v["questions"]["probe"] = [record(asst, dict(q, set="probe"), False, by_id) for q in probes]
            res["versions"][tag] = v
            print(tag, v["chunk_set_hash"][:12], {s: {k: (g["recall@5"], g["recall@10"], g["mrr"], g["evidence_label_recall"])
                                                      for k, g in agg.items()} for s, agg in v["aggregates"].items()})
    ref = common.load_json(os.path.join(H, "docs", "audit_runs", "retrieval_final.json"))
    mine = {x["id"]: x for x in res["versions"]["v1"]["questions"]["frozen"]}
    keys = ("recall@5", "recall@10", "rr", "evidence_label_recall", "outcome")
    res["reproduction_of_recorded_v1_audit"] = {
        "reference": "docs/audit_runs/retrieval_final.json (" + ref["generated_at"] + ")",
        "aggregates_equal": all(all(res["versions"]["v1"]["aggregates"]["frozen"][s][k] == ref["aggregates"][s][k] for k in ref["aggregates"][s])
                                for s in ref["aggregates"]),
        "per_question_differences": [q["id"] for q in ref["questions"] if {k: q.get(k) for k in keys} != {k: mine[q["id"]].get(k) for k in keys}]}
    common.dump_json(out_path, res)
    print("reproduction:", res["reproduction_of_recorded_v1_audit"])
    print("written", out_path)


if __name__ == "__main__":
    main(sys.argv[1:])
