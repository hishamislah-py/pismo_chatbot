"""Stage-level tests with synthetic data: no model, no index, no network."""
from types import SimpleNamespace

import httpx
import openai
import pytest

from pismo_assistant import citations
from pismo_assistant.evidence import Evidence, OperationIndex, assemble, linked_operation_ids
from pismo_assistant.generation import GenerationError, OpenAIGenerator, build_messages, parse_output
from pismo_assistant.pipeline import Assistant
from pismo_assistant.retrieval import Hit, IndexIntegrityError, verify_index
from conftest import FakeClient, model_json

REF = {"path": "docs/a.md", "url": "https://developers.pismo.io/a", "sha256": "x"}


def chunk(cid, text="t", ku="KU-A", op=None, src="docs/a.md", ku_type="workflow_guide", heading="Body", flags=()):
    return {"chunk_id": cid, "ku_id": ku, "ku_title": "Title " + ku, "ku_path": f"knowledge_units/c/{ku}.md", "text": text,
            "heading_path": ["Title", heading], "section_heading": heading, "source_refs": [REF], "flags": list(flags),
            "operation": op, "source_path": src, "ku_type": ku_type, "ku_sources": ["docs/a.md"], "sha256": "h"}


class FakeRetriever:
    def __init__(self, hits_chunks, chunks=None):
        self.hits_chunks = hits_chunks
        self.chunks = chunks if chunks is not None else hits_chunks

    def search(self, q, k=6):
        if not q.strip():
            return []
        return [Hit(c, i) for i, c in enumerate(self.hits_chunks[:k], 1)]


def ev(label, text="body", refs=(REF,), ku="KU-A"):
    return Evidence(label, f"{ku}::{label}", ku, "Title", "Sec", text, list(refs), [], "retrieved", "")


# ---------------- missing retrieval results
def test_no_retrieval_results_skips_generation():
    client = FakeClient(model_json())
    r = Assistant(retriever=FakeRetriever([]), generator=OpenAIGenerator(client=client)).answer("anything")
    assert r["status"] == "no_evidence" and client.calls == [] and r["citations"] == []


def test_empty_question():
    r = Assistant(retriever=FakeRetriever([chunk("c1")]), generator=OpenAIGenerator(client=FakeClient(model_json()))).answer("  ")
    assert r["status"] == "no_evidence"


# ---------------- malformed model output
@pytest.mark.parametrize("raw", ["not json", "[1, 2]", '{"status": "maybe", "answer": "x", "citations": []}',
                                 '{"status": "answered", "answer": "", "citations": []}',
                                 '{"status": "answered", "answer": "x", "citations": "E1"}', None])
def test_malformed_output_is_reported_not_answered(raw):
    a = Assistant(retriever=FakeRetriever([chunk("c1")]), generator=OpenAIGenerator(client=FakeClient(raw)))
    r = a.answer("q")
    assert r["status"] == "generation_error" and r["error"]["kind"] == "malformed_output" and r["answer"] == ""


def test_unexpected_response_shape():
    a = Assistant(retriever=FakeRetriever([chunk("c1")]), generator=OpenAIGenerator(client=FakeClient(SimpleNamespace(choices=[]))))
    r = a.answer("q")
    assert r["status"] == "generation_error" and r["error"]["kind"] == "malformed_output"


def test_parse_output_accepts_valid():
    assert parse_output(model_json("partial", "x [E1]", ["E1"], "y")) == ("partial", "x [E1]", ["E1"], "y")


# ---------------- API errors and configuration
def test_api_error_is_reported():
    err = openai.APIConnectionError(request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions"))
    a = Assistant(retriever=FakeRetriever([chunk("c1")]), generator=OpenAIGenerator(client=FakeClient(err)))
    r = a.answer("q")
    assert r["status"] == "generation_error" and r["error"]["kind"] == "api_error" and "APIConnectionError" in r["error"]["message"]


def test_timeout_is_reported():
    err = openai.APITimeoutError(request=httpx.Request("POST", "https://api.openai.com/v1/chat/completions"))
    r = Assistant(retriever=FakeRetriever([chunk("c1")]), generator=OpenAIGenerator(client=FakeClient(err))).answer("q")
    assert r["error"]["kind"] == "api_error"


def test_missing_api_key_is_configuration_error(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    r = Assistant(retriever=FakeRetriever([chunk("c1")]), generator=OpenAIGenerator(client=None)).answer("q")
    assert r["status"] == "generation_error" and r["error"]["kind"] == "configuration"
    assert "OPENAI_API_KEY is not set" in r["error"]["message"]


# ---------------- citation validation
def test_valid_citations():
    rep = citations.validate("Use `POST /v1/x` [E1].", ["E1"], [ev("E1", "POST /v1/x does it")])
    assert rep.ok and rep.valid == ["E1"]


def test_missing_citation_metadata_is_flagged():
    e = [ev("E1", refs=()), ev("E2", refs=({"path": "docs/a.md", "url": ""},))]
    rep = citations.validate("A [E1] B [E2]", ["E1", "E2"], e)
    assert rep.missing_metadata == ["E1", "E2"] and not rep.ok and rep.valid == []


def test_unknown_label_is_flagged():
    rep = citations.validate("A [E7]", ["E7"], [ev("E1")])
    assert rep.unknown == ["E7"] and not rep.ok


def test_unsupported_api_details_are_flagged():
    rep = citations.validate("Call `POST /v9/fake` and handle WXYZ0001 [E1].", ["E1"], [ev("E1", "nothing relevant")])
    toks = [t["token"] for t in rep.unsupported_tokens]
    assert "POST /v9/fake" in toks and "WXYZ0001" in toks and not rep.ok


def test_claim_level_support_uses_only_the_claims_own_citations():
    e = [ev("E1", "POST /v1/a creates it"), ev("E2", "POST /v1/b deletes it")]
    rep = citations.validate("Create with `POST /v1/b` [E1].\nDelete with `POST /v1/a` [E2].", ["E1", "E2"], e)
    assert {t["token"] for t in rep.unsupported_tokens} == {"POST /v1/b", "POST /v1/a"} and not rep.ok


def test_uncited_claim_with_api_detail_is_flagged():
    rep = citations.validate("Intro [E1].\nThen call `/v1/a` with `account_id`.", ["E1"], [ev("E1", "/v1/a account_id")])
    assert rep.uncited_claims and not rep.ok and rep.checks()["claim_token_support"] is False


def test_event_slug_and_field_tokens_are_checked():
    rep = citations.validate("It emits platform-authorization-platform-authorization-9 and needs tracking_id [E1].", ["E1"],
                             [ev("E1", "emits platform-authorization-platform-authorization-1, field tracking_id")])
    assert [t["token"] for t in rep.unsupported_tokens] == ["platform-authorization-platform-authorization-9"]


def test_hyphenated_english_words_are_not_identifiers():
    # regression from the live gpt-5-mini run (Q6): "step-by-step" was checked as an API token
    e = [ev("E1", "post-transfers-cancel cancels a transfer")]
    rep = citations.validate("No step-by-step PCI procedure is documented [E1].", ["E1"], e, known_identifiers={"post-transfers-cancel"})
    assert rep.unsupported_tokens == [] and rep.ok
    rep = citations.validate("Use post-transfers-cancel or post-transfers-revert [E1].", ["E1"], e,
                             known_identifiers={"post-transfers-cancel", "post-transfers-revert"})
    assert [t["token"] for t in rep.unsupported_tokens] == ["post-transfers-revert"]


def test_operation_alignment():
    exp = [{"operation": "post-transfers", "method": "POST", "path": "/payment-methods/v2/transfers", "matched_by": "summary"}]
    e = [ev("E1", "POST /v1/transfers schedule; POST /payment-methods/v2/transfers")]
    bad = citations.validate("Use POST /v1/transfers [E1].", ["E1"], e, exp, "answered")
    assert bad.operation_mismatch and not bad.ok
    good = citations.validate("Use POST /payment-methods/v2/transfers [E1].", ["E1"], e, exp, "answered")
    assert not good.operation_mismatch and good.ok
    assert not citations.validate("Not documented [E1].", ["E1"], e, exp, "not_documented").operation_mismatch


def test_historical_only_support_must_be_marked():
    h = Evidence("E1", "KU-CHG::x", "KU-CHG", "Changelog", "S", "WEAM0029 rejected back-dated earmarks", [REF],
                 ["historical_changelog"], "retrieved", "")
    assert citations.validate("WEAM0029 rejects back-dated earmarks [E1].", ["E1"], [h], status="answered").unmarked_historical
    assert not citations.validate("WEAM0029 was removed; it rejected back-dated earmarks [E1].", ["E1"], [h],
                                  status="answered").unmarked_historical
    # regression from the live gpt-5-mini run (Q1): past tense "was ... originally" is a historical marking
    live = ("WEAM0029 was an error code that was originally returned when the Pismo platform rejected earmark payments "
            "with back value dates. [E1]")
    assert not citations.validate(live, ["E1"], [h], status="answered").unmarked_historical


def test_grouped_labels_and_unfenced_json_example():
    e = [ev("E1", 'example {"account_id": 1, "tracking_id": "x"}'), ev("E2", "more")]
    ans = 'Example request [E1, E2]:\n{\n  "account_id": 1,\n  "tracking_id": "x"\n}'
    rep = citations.validate(ans, [], e)
    assert rep.valid == ["E1", "E2"] and rep.ok and rep.uncited_claims == []


def test_code_block_cited_on_following_line():
    # regression from the live gpt-5-mini run (Q2): example block cited by the sentence right after it
    e = [ev("E4", 'Release funds {"account_id": 111507785, "tracking_id": "c852"}'), ev("E5", "unrelated text")]
    ok = 'Below is the example request:\n```json\n{"account_id": 111507785, "tracking_id": "c852"}\n```\nThis example is from the docs [E4].'
    rep = citations.validate(ok, [], e)
    assert rep.uncited_claims == [] and rep.unsupported_tokens == [] and rep.ok
    bad = ok.replace("[E4]", "[E5]")   # following line cites a passage that does not contain the example
    rep = citations.validate(bad, [], e)
    assert {t["token"] for t in rep.unsupported_tokens} >= {"account_id", "tracking_id"} and not rep.ok
    lone = 'Example:\n```json\n{"account_id": 1}\n```\nNo citation anywhere.'
    assert citations.validate(lone, [], e).uncited_claims


def test_semantic_support_is_never_claimed():
    assert citations.validate("x [E1]", ["E1"], [ev("E1")]).checks()["semantic_support_verified"] is False


def test_trailing_punctuation_is_not_an_unsupported_detail():
    # regression from the live gpt-5-mini run: "POST /payments/v1/payments/hold-funds/unblock." was flagged
    rep = citations.validate("Call POST /payments/v1/payments/hold-funds/unblock. [E1]", ["E1"],
                             [ev("E1", "### `POST /payments/v1/payments/hold-funds/unblock` - Unblock")])
    assert rep.unsupported_tokens == [] and rep.ok


def test_pipeline_surfaces_citation_warnings():
    client = FakeClient(model_json("answered", "Use `/v9/fake` [E5].", ["E5"]))
    r = Assistant(retriever=FakeRetriever([chunk("c1")]), generator=OpenAIGenerator(client=client)).answer("q")
    assert r["citations_valid"] is False and r["citations"] == []
    assert any("not supplied" in w for w in r["warnings"]) and any("not found in the passages cited" in w for w in r["warnings"])


def test_pipeline_excludes_citation_without_metadata():
    bad = chunk("c1")
    bad["source_refs"] = []
    client = FakeClient(model_json("answered", "x [E1]", ["E1"]))
    r = Assistant(retriever=FakeRetriever([bad]), generator=OpenAIGenerator(client=client)).answer("q")
    assert r["citations"] == [] and any("lacks source metadata" in w for w in r["warnings"])


# ---------------- evidence assembly (independent of retrieval and generation)
def test_assemble_preserves_retrieved_order_and_adds_links_events_lifecycle():
    guide = chunk("g1", "Release with [Unblock](https://developers.pismo.io/pismo-docs/reference/post-unblock).", ku="KU-G")
    op = chunk("api::op", "### `POST /unblock`", ku="KU-API", op="post-unblock", src=None, ku_type="api_reference")
    op_ev = chunk("api::op.ev", "#### Events emitted (x)\n\n| Event slug | Event page |\n| --- | --- |\n| `evt-one-1` | u |",
                  ku="KU-API", op="post-unblock", src=None, ku_type="api_reference")
    life = chunk("KU-G::lifecycle-status", "Links to `x` are not found in the current OpenAPI specifications.", ku="KU-G",
                 src=None, heading="Lifecycle status")
    idx = OperationIndex([guide, op, op_ev, life])
    out = assemble([Hit(guide, 1)], idx)
    assert [e.chunk_id for e in out] == ["g1", "api::op", "api::op.ev", "KU-G::lifecycle-status"]
    assert [e.origin for e in out] == ["retrieved", "linked_operation", "operation_events", "lifecycle"]
    assert [e.label for e in out] == ["E1", "E2", "E3", "E4"]
    assert idx.events_for("POST-UNBLOCK") == ["evt-one-1"]


def test_assemble_ignores_links_in_navigation_or_low_ranks():
    nav = chunk("g1", "[x](ref:post-unblock)", src=None)
    op = chunk("api::op", "op", ku="KU-API", op="post-unblock", src=None, ku_type="api_reference")
    idx = OperationIndex([nav, op])
    assert [e.chunk_id for e in assemble([Hit(nav, 1)], idx)] == ["g1"]
    hits = [Hit(chunk(f"c{i}"), i) for i in range(1, 4)] + [Hit(chunk("g4", "[x](ref:post-unblock)"), 4)]
    assert "api::op" not in [e.chunk_id for e in assemble(hits, idx)]


def test_named_operation_lookup_adds_operation_and_events():
    op = chunk("api::op", "### `POST /t`", ku="KU-API", op="post-transfers", src=None, ku_type="api_reference")
    op_ev = chunk("api::op.ev", "#### Events emitted (x)\n\n| Event slug | Event page |\n| --- | --- |\n| `evt-1` | u |",
                  ku="KU-API", op="post-transfers", src=None, ku_type="api_reference")
    other = chunk("c1", "unrelated")
    idx = OperationIndex([op, op_ev, other])
    out = assemble([Hit(other, 1)], idx, question="Which event does post-transfers emit?")
    assert [(e.chunk_id, e.origin) for e in out] == [("c1", "retrieved"), ("api::op", "named_operation"), ("api::op.ev", "operation_events")]
    assert [e.chunk_id for e in assemble([Hit(other, 1)], idx, question="how do transfers work")] == ["c1"]


def _fake_retriever(chunks, order):
    from pismo_assistant.retrieval import HybridRetriever
    r = object.__new__(HybridRetriever)          # no index/model load: only search()'s slot-filling logic is tested
    r.chunks = chunks
    r.ranked = lambda q: (order, 0)
    return r


def test_search_skips_navigation_chunks(monkeypatch):
    from pismo_assistant import config as cfg
    nav = [chunk("K::intro", heading="Title"), chunk("K::topics-covered", heading="Topics covered"),
           chunk("K::source-references", heading="Source references"), chunk("K::related-knowledge-units", heading="Related knowledge units")]
    content = [chunk(f"K::src-{i}", heading=f"Body {i}") for i in range(3)]
    r = _fake_retriever(nav + content, list(range(7)))
    monkeypatch.setattr(cfg, "EXCLUDE_NAV_FROM_TOP_K", True)
    hits = r.search("q", k=3)
    assert [h.chunk_id for h in hits] == ["K::src-0", "K::src-1", "K::src-2"]
    assert [h.rank for h in hits] == [5, 6, 7]                # rank keeps the position in the full ranking
    monkeypatch.setattr(cfg, "EXCLUDE_NAV_FROM_TOP_K", False)  # the flag restores the previous behaviour
    assert [h.chunk_id for h in r.search("q", k=3)] == ["K::intro", "K::topics-covered", "K::source-references"]


def test_search_keeps_relationship_sections():
    from pismo_assistant.retrieval import is_navigation
    for h in ("Purpose and scope", "Operations in this unit", "API operations referenced", "Events", "Lifecycle status"):
        assert not is_navigation(chunk("K::x", heading=h)), h


def test_error_code_lookup_adds_catalogue_row():
    row = chunk("KU-ERR-codes-eiba::error-codes", "| Code | HTTP | Message |\n| --- | --- | --- |\n| `EIBA0005` | 400 | Invalid account |",
                ku="KU-ERR-codes-eiba", ku_type="error_catalogue", src=None)
    api = chunk("api::op", "example error_code EIBA0005", ku="KU-API", ku_type="api_reference", op="get-x", src=None)
    idx = OperationIndex([row, api])
    out = assemble([Hit(api, 1)], idx, question="Why am I getting error code EIBA0005?")
    assert [(e.chunk_id, e.origin) for e in out] == [("api::op", "retrieved"), ("KU-ERR-codes-eiba::error-codes", "error_catalogue")]
    assert [e.chunk_id for e in assemble([Hit(api, 1)], idx, question="What does ZZZZ9999 mean?")] == ["api::op"]


def _register_index():
    reg = chunk("KU-LIFE-api-endpoints-removed::structured-removal-register-migration-ex::p01",
                "| # | API | Section | Names | URLs | Date | In specs |\n| --- | --- | --- | --- | --- | --- | --- |\n"
                "| 3 | Cards | Cards | Create combo card | POST /wallet/v1/relationship | `(blank)` | no match |\n"
                "| 8 | CRM | Core platform | All endpoints | /crm/\\\\* | `6/26/2026` | no match |\n"
                "| 11 | Cardsonfile | Validation | Get card validation amount | <br />GET /cardsonfile/v2/cards/\\\\{uuid}/amount | `5/12/2026` | yes |",
                ku="KU-LIFE-api-endpoints-removed", ku_type="lifecycle_reference", src=None)
    return reg, OperationIndex([reg])


def test_removed_endpoint_lookup_by_name_path_and_api():
    from pismo_assistant.evidence import removed_endpoint_rows
    reg, idx = _register_index()
    rows = lambda q: [r["row"] for r in removed_endpoint_rows(q, idx)]
    assert rows("When was the Create combo card endpoint removed?") == [3]
    assert rows("Can I still call GET /cardsonfile/v2/cards/{cardId}/amount?") == [11]   # placeholder names ignored
    assert rows("Was the CRM API decommissioned?") == [8]
    assert rows("What is the CRM API?") == []          # API-name rule needs lifecycle intent
    assert rows("How do I create a card?") == []       # one-word overlap is not a name match
    out = assemble([], idx, question="When was the Create combo card endpoint removed?")
    assert [(e.chunk_id, e.origin) for e in out] == [(reg["chunk_id"], "removal_register")]


def test_linked_operation_ids():
    t = "[a](https://developers.pismo.io/pismo-docs/reference/post-x) [b](ref:get-y) [c](https://example.com/z)"
    assert linked_operation_ids(t) == ["post-x", "get-y"]


def test_build_messages_contains_exact_text_and_sources():
    m = build_messages("Q?", [ev("E1", "exact passage text")])
    assert "exact passage text" in m[1]["content"] and "docs/a.md (https://developers.pismo.io/a)" in m[1]["content"]


# ---------------- index integrity
def test_verify_index_rejects_non_ku_chunks():
    c = chunk("c1")
    c["ku_path"] = "pismo_kb_release_r2/kb_corpus/docs/a.md"
    with pytest.raises(IndexIntegrityError, match="non-KU"):
        verify_index([c], {"chunk_set_hash": "x"}, {"chunk_set_hash": "x"}, check_ku_files=False)


def test_verify_index_rejects_hash_mismatch():
    with pytest.raises(IndexIntegrityError, match="does not match"):
        verify_index([chunk("c1")], {"chunk_set_hash": "wrong"}, {"chunk_set_hash": "wrong"}, check_ku_files=False)
