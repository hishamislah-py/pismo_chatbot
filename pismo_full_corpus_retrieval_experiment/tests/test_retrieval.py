"""Exact identifier matching, BM25, semantic ranking logic, RRF and tie-breaking."""
import json
import os

import numpy as np

from common import RESULTS
from retrievers import BM25, Dense, detect_identifiers, exact_rerank, rank_by_score, rrf, tokenize, windows_for


def test_tokenizer_keeps_identifiers():
    toks = tokenize("Send x-account-id with encrypted_pan to POST /v1/migrations/cards-pci (post-transfers-cancel)")
    for t in ("x-account-id", "encrypted_pan", "v1/migrations/cards-pci", "post-transfers-cancel", "account", "pan"):
        assert t in toks


def test_detect_identifiers():
    assert detect_identifiers("Why would a back-dated earmark payment fail with error WEAM0029?") == ["WEAM0029"]
    assert "mTLS" not in detect_identifiers("What changed about configuring mTLS?")
    ids = detect_identifiers("POST /v1/migrations/cards-pci and post-payments-v1-hold-funds-unblock and createMarketplace")
    assert "/v1/migrations/cards-pci" in ids and "post-payments-v1-hold-funds-unblock" in ids and "createMarketplace" in ids
    assert "x-account-id" in detect_identifiers("which field must match the x-account-id header")
    assert detect_identifiers("How do I cancel a transfer?") == []


def test_exact_rerank_promotes_literal_matches_stably():
    texts = ["nothing here", "contains weam0029 once", "other", "weam0029 again"]
    order, n = exact_rerank([0, 2, 3, 1], texts, ["WEAM0029"])
    assert order == [3, 1, 0, 2] and n == 2
    assert exact_rerank([2, 0, 1], texts, [])[0] == [2, 0, 1]


def test_bm25_ranking_known_example():
    docs = ["hold funds block an amount", "transfer money between accounts", "cancel a transfer", "error code WEAM0001 earmark"]
    bm = BM25(docs)
    ids = ["d0", "d1", "d2", "d3"]
    assert [ids[i] for i in rank_by_score(bm.scores("cancel transfer"), ids, positive_only=True)][:2] == ["d2", "d1"]
    assert [ids[i] for i in rank_by_score(bm.scores("WEAM0001"), ids, positive_only=True)] == ["d3"]
    s = bm.scores("hold funds")
    assert s[0] > 0 and s[1] == 0


def test_bm25_idf_non_negative():
    bm = BM25(["the same word"] * 5)
    assert all(v >= 0 for v in bm.idf.values())


def test_rank_by_score_tie_break_by_id():
    ids = ["b", "a", "c"]
    assert rank_by_score(np.array([1.0, 1.0, 0.0]), ids) == [1, 0, 2]
    assert rank_by_score(np.array([1.0, 1.0, 0.0]), ids, positive_only=True) == [1, 0]


def test_dense_max_over_windows():
    V = np.array([[1, 0], [0, 1], [0.6, 0.8]], dtype=np.float32)
    d = Dense(V, np.array([0, 0, 1]), 3)
    s = d.scores(np.array([0, 1.0]))
    assert s[0] == 1.0 and abs(s[1] - 0.8) < 1e-6 and s[2] == -1.0
    assert rank_by_score(s, ["c0", "c1", "c2"]) == [0, 1, 2]


def test_windows_cover_long_bodies():
    w = windows_for("H\n", "x" * 2500)
    assert len(w) == 3 and all(x.startswith("H\n") for x in w)
    assert windows_for("H\n", "short") == ["H\nshort"]


def test_rrf_formula_and_weights():
    ids = ["a", "b", "c"]
    fused = rrf([[0, 1, 2], [2, 1, 0]], [1.0, 1.0], ids, k=60)
    # a: 1/61 + 1/63, b: 2/62, c: 1/63 + 1/61 -> a ties c, b is lowest; tie broken by best rank (both 1), then first-list rank
    assert fused == [0, 2, 1]
    w = rrf([[0, 1, 2], [2, 1, 0]], [2.0, 1.0], ids, k=60)
    assert w[0] == 0 and abs((2 / 61 + 1 / 63) - (2 / 63 + 1 / 61)) > 0


def test_rrf_items_missing_from_one_list():
    ids = ["a", "b", "c"]
    assert rrf([[1], [0, 1, 2]], [1.0, 1.0], ids, k=60)[0] == 1


def test_rrf_deterministic_tie_break_by_id():
    ids = ["z", "y"]
    assert rrf([[0], [1]], [1.0, 1.0], ids, k=60) == [0, 1]  # equal score, equal best rank; first-list rank decides
    assert rrf([[], [0, 1]], [1.0, 1.0], ids, k=60) == [0, 1]


def test_semantic_sanity_ran():
    p = os.path.join(RESULTS, "semantic_sanity.json")
    d = json.load(open(p, encoding="utf-8"))
    assert d["self_similarity"]["pass"] is True
    assert len(d["rank_checks"]) == 5 and len(d["pair_checks"]) == 3


def test_embedding_provenance():
    m = json.load(open(os.path.join(RESULTS, "embeddings", "embedding_meta.json"), encoding="utf-8"))
    assert m["model"] == "sentence-transformers/all-MiniLM-L6-v2" and m["dimension"] == 384
    assert m["revision"] == "1110a243fdf4706b3f48f1d95db1a4f5529b4d41"
    v = np.load(os.path.join(RESULTS, "embeddings", "window_vectors.npy"))
    assert v.shape == (m["n_windows"], 384)
    assert np.allclose(np.linalg.norm(v[:50], axis=1), 1.0, atol=1e-3)
