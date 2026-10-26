"""Metrics on known examples, top-K cutoffs, multi-KU coverage, missing gold evidence, unanswerable and lifecycle checks,
and the frozen benchmark hash."""
import json
import math
import os

import build_benchmark
from common import EXP, RESULTS, sha_json
from labels import chunk_satisfies
from metrics import evaluate, label_hits, ndcg_at


def _c(cid, ku, text, sources=("docs/a.md",), src=None):
    return {"chunk_id": cid, "ku_id": ku, "text": text, "ku_sources": list(sources), "source_path": src}


def test_metrics_known_example():
    ranked = ["x1", "x2", "x3", "x4", "x5", "r1", "x6", "r2"]
    sets = [{"r1"}, {"r2"}]
    kus = {c: ("KU-R" if c.startswith("r") else "KU-" + c) for c in ranked}
    ev = evaluate(ranked, sets, [{"KU-R"}, {"KU-R"}], kus)
    assert ev["first_relevant_rank"] == 6
    assert ev["recall@5"] == 0 and ev["recall@10"] == 1.0
    assert math.isclose(ev["mrr"], 1 / 6)
    assert ev["hit@5"] is False and ev["hit@10"] is True
    assert ev["all_labels@5"] is False and ev["all_labels@10"] is True
    assert ev["ku_recall@5"] == 0 and ev["ku_recall@10"] == 1.0  # KU-R is the 6th distinct KU


def test_top_k_cutoffs():
    ranked = [f"c{i}" for i in range(1, 12)]
    ev = evaluate(ranked, [{"c5"}, {"c11"}], [{"K"}, {"K"}], {c: c for c in ranked})
    assert ev["recall@5"] == 0.5 and ev["recall@10"] == 0.5 and ev["first_relevant_rank"] == 5


def test_ndcg_label_level():
    hits = label_hits(["a", "b", "c"], [{"a"}, {"c"}])
    assert math.isclose(ndcg_at(hits, 2, 5), (1 + 1 / math.log2(4)) / (1 + 1 / math.log2(3)))
    assert ndcg_at(label_hits(["a", "c"], [{"a"}, {"c"}]), 2, 5) == 1.0
    hits_dup = label_hits(["a", "a2", "c"], [{"a", "a2"}, {"c"}])  # a second chunk for the same label earns nothing
    assert ndcg_at(hits_dup, 2, 5) < 1.0


def test_multi_ku_coverage():
    ranked = ["g1", "s1", "n1"]
    ev = evaluate(ranked, [{"g1"}, {"s1"}, {"z"}], [{"KU-G"}, {"KU-S"}, {"KU-Z"}], {"g1": "KU-G", "s1": "KU-S", "n1": "KU-N"})
    assert ev["all_labels@5"] is False and math.isclose(ev["recall@5"], 2 / 3)


def test_label_semantics():
    guide_block = _c("k::src", "KU-G", "Use hold funds", src="docs/a.md")
    guide_nav = _c("k::nav", "KU-G", "Related knowledge units")
    other_block = _c("k::src2", "KU-G", "Use hold funds", sources=("docs/a.md", "docs/b.md"), src="docs/b.md")
    assert chunk_satisfies(guide_block, {"file": "docs/a.md"})
    assert not chunk_satisfies(guide_nav, {"file": "docs/a.md"})  # navigation is not evidence for a no-regex guide label
    assert not chunk_satisfies(other_block, {"file": "docs/a.md"})
    api = _c("k::op", "KU-API", "POST /v1/migrations/cards-pci", sources=("api-specs/M.yaml",))
    assert chunk_satisfies(api, {"file": "api-specs/M.yaml", "match": "cards-pci"})
    assert not chunk_satisfies(api, {"file": "api-specs/M.yaml", "match": "go-live"})
    assert chunk_satisfies(_c("x", "KU-L", "Not documented"), {"ku": "KU-L", "match": "not documented"})
    assert chunk_satisfies(_c("x", "KU-S", "postmarketplacesv2", sources=("docs/seller/s.md",), src="docs/seller/s.md"),
                           {"file": "docs/seller/", "match": "postmarketplacesv2"})


def test_missing_gold_evidence_is_classified(chunks):
    build_benchmark.ku_files = {}
    for c in chunks:
        build_benchmark.ku_files[c["ku_id"]] = c["ku_sources"]
    ku_text = {}
    for c in chunks:
        ku_text[c["ku_id"]] = ku_text.get(c["ku_id"], "") + "\n" + c["text"]
    bad = build_benchmark.verify_label({"file": "docs/core-platform/hold-funds.md", "match": "ZZZ-NOT-IN-SOURCE"}, chunks, ku_text)
    assert bad["status"] == "invalid_label" and not bad["relevant_chunk_ids"]
    missing = build_benchmark.verify_label({"file": "docs/does-not-exist.md"}, chunks, ku_text)
    assert missing["status"] == "invalid_label" and missing["source_evidence"] == "source_file_missing"
    ok = build_benchmark.verify_label({"file": "docs/core-platform/hold-funds.md"}, chunks, ku_text)
    assert ok["status"] == "valid" and ok["relevant_ku_ids"] == ["KU-PAY-hold-funds"]


def test_benchmark_frozen_hash(bench):
    frozen = open(os.path.join(EXP, "BENCHMARK.sha256"), encoding="utf-8").read().split()[0]
    assert sha_json({"primary": bench["primary"], "extension": bench["extension"]}) == frozen
    assert bench["_meta"]["primary_source"]["member_sha256"] == "71a969f3d180f6f9f8156e335328eddf43eea3dc21bf5ee5bc975c2a994c04da"


def test_primary_ids_and_labels_preserved(bench):
    import zipfile
    from common import PRIOR_BENCH_MEMBER, PRIOR_ZIP
    prior = json.loads(zipfile.ZipFile(PRIOR_ZIP).read(PRIOR_BENCH_MEMBER))
    assert [q["id"] for q in prior["questions"]] == [q["id"] for q in bench["primary"]]
    for p, b in zip(prior["questions"], bench["primary"]):
        assert p["q"] == b["q"]
        assert p["expected"] == [l["label"] for l in b["labels"]]


def test_unanswerable_questions_not_scored(bench):
    for q in bench["primary"] + bench["extension"]:
        if q.get("answerability") == "none":
            assert q["scored"] is False and not q["labels"]
        if q.get("absent_identifier"):
            assert q["absent_identifier_check"]["absent"] is True, q["id"]
        if q.get("required_statement"):
            assert q["required_statement_check"]["present"] is True, q["id"]


def test_extension_set_kept_separate(bench):
    assert all(q["set"] == "primary" for q in bench["primary"])
    assert all(q["set"] == "extension" and q["id"].startswith("EXT-") for q in bench["extension"])


def test_lifecycle_flags_and_diagnostics(chunks):
    reg = [c for c in chunks if c["ku_id"] == "KU-LIFE-api-endpoints-removed"]
    assert reg and all("removal_register" in c["flags"] for c in reg)
    assert any("unresolved_operation_link" in c["flags"] for c in chunks if c["ku_id"].startswith("KU-SELL-"))
    assert all("historical_changelog" in c["flags"] for c in chunks if c["ku_type"] == "changelog_history")
    diag = json.load(open(os.path.join(RESULTS, "unanswerable_and_lifecycle.json"), encoding="utf-8"))
    by_id = {d["id"]: d for d in diag}
    for qid in ("G5", "E1", "E2", "EXT-A05", "EXT-U01", "EXT-I01"):
        assert qid in by_id and set(by_id[qid]["configs"]) >= {"bm25", "semantic", "rrf_equal", "rrf_bm25_2to1"}


def test_results_cover_every_question_and_config(bench):
    agg = json.load(open(os.path.join(RESULTS, "aggregate_metrics.json"), encoding="utf-8"))
    n = len(bench["primary"]) + len(bench["extension"])
    for cfg in ("bm25", "semantic", "rrf_equal", "rrf_bm25_2to1", "bm25_exact", "rrf_bm25_2to1_exact"):
        rows = json.load(open(os.path.join(RESULTS, f"per_question_{cfg}.json"), encoding="utf-8"))
        assert len(rows) == n
        assert agg["aggregates"][cfg]["primary"]["all"]["n"] == sum(q["scored"] for q in bench["primary"])
        for r in rows:
            if r["scored"]:
                assert r["first_relevant_rank"] is None or 1 <= r["first_relevant_rank"] <= 100
