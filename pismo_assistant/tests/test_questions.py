"""End-to-end questions through the real retriever and evidence assembly, with a fake OpenAI client (no network)."""
import json
import os

import pytest

from pismo_assistant import config
from pismo_assistant.generation import OpenAIGenerator, SYSTEM_PROMPT
from pismo_assistant.pipeline import Assistant
from conftest import FakeClient, model_json


def _ev(assistant, q):
    return assistant.evidence(q)


def test_index_is_ku_only_and_provenance_preserved(retriever):
    assert len(retriever.chunks) == 11026
    for c in retriever.chunks:
        assert c["ku_path"].startswith("knowledge_units/") and c["ku_path"].endswith(".md")
    with open(config.CHUNKS_PATH, encoding="utf-8") as fh:
        stored = [json.loads(l)["chunk_id"] for l in fh]
    assert stored == retriever.ids  # stable ids: identical to the frozen experiment index


def test_weam0029_exact_error_code_lookup(assistant_evidence):
    ev = _ev(assistant_evidence, "What does WEAM0029 mean?")
    assert ev[0].ku_id == "KU-CHG-2-october-2026" and "WEAM0029" in ev[0].text
    assert ev[0].reason == "exact identifier match"
    assert "historical_changelog" in ev[0].flags  # the code exists only in a changelog: answer must treat it as history


def test_release_held_funds_workflow(assistant_evidence):
    ev = _ev(assistant_evidence, "How do I release funds that I previously held on an account?")
    guide = [e for e in ev if e.ku_id == "KU-PAY-hold-funds" and e.origin == "retrieved"]
    assert guide, [e.chunk_id for e in ev]
    unblock = [e for e in ev if "post-payments-v1-hold-funds-unblock" in e.chunk_id]
    assert unblock and unblock[0].origin == "linked_operation"
    assert "/payments/v1/payments/hold-funds/unblock" in unblock[0].text


def test_operation_to_event_lookup_deterministic(assistant_evidence):
    assert assistant_evidence.op_index.events_for("post-transfers") == ["platform-authorization-platform-authorization-1"]
    assert assistant_evidence.op_index.events_for("no-such-operation") == []


def test_operation_to_event_lookup_by_identifier(assistant_evidence):
    ev = _ev(assistant_evidence, "Which event does post-transfers emit?")
    assert any("platform-authorization-platform-authorization-1" in e.text and "post-transfers" in e.chunk_id for e in ev), \
        [e.chunk_id for e in ev]


def test_operation_to_event_lookup_natural_language(assistant_evidence):
    """Regression for the demo defect: before the fix the post-transfers operation ranked 140th (fused) and only the
    'Create transfer schedule' operation and its events reached the model. The exact summary phrase 'create (a)
    transfer' now identifies post-transfers, and its events table is assembled first."""
    ev = _ev(assistant_evidence, "Which event is generated when I create a transfer?")
    named = [e for e in ev if e.origin == "named_operation"]
    assert [e.chunk_id for e in named] == ["KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers"]
    assert "operation summary 'Create transfer'" in named[0].reason
    events = [e for e in ev if e.origin == "operation_events"]
    assert "op-post-transfers" in events[0].chunk_id
    assert "platform-authorization-platform-authorization-1" in events[0].text


def test_summary_match_prefers_longest_phrase(assistant_evidence):
    from pismo_assistant.evidence import matched_operations
    idx = assistant_evidence.op_index
    assert [m["operation"] for m in matched_operations("How do I create a transfer schedule?", idx)] == ["post-v1-create-transfer-schedules"]
    for q in ("What does WEAM0029 mean?", "How do I verify webhook requests?", "How do I perform PCI card go-live?",
              "How do I release funds that I previously held on an account?"):
        assert matched_operations(q, idx) == [], q


def test_webhook_troubleshooting_natural_language(assistant_evidence):
    q = ("Our webhook endpoint keeps rejecting Pismo's calls because we cannot confirm they really come from Pismo. "
         "How do we verify webhook requests?")
    ev = _ev(assistant_evidence, q)
    assert ev[0].ku_id == "KU-EVT-verifying-webhook-requests"
    assert ev[0].source_refs[0]["path"] == "docs/get-started/verifying-webhook-requests.md"


def test_navigation_chunks_do_not_take_evidence_slots(assistant_evidence):
    """Audit fix 1 (benchmark EXT-C01, E3): KU navigation chunks used to fill 3-4 of the 6 slots, pushing the answer out."""
    from pismo_assistant.retrieval import is_navigation
    ev = _ev(assistant_evidence, "Which endpoints require an account-specific token?")
    assert not any(is_navigation(assistant_evidence.retriever.by_id[e.chunk_id]) for e in ev if e.origin == "retrieved")
    assert any("src-endpoints-that-require-an-account-specific-token" in e.chunk_id for e in ev)
    ev = _ev(assistant_evidence, "What changed about configuring mTLS?")
    assert any(e.chunk_id.startswith("KU-AUTH-identity-connectivity-with-mtls::src-") for e in ev)


def test_error_code_question_includes_catalogue_row(assistant_evidence):
    """Audit fix 2 (benchmark C2, C5): the catalogue row ranked 22nd/12th behind API examples quoting the code."""
    for q, code, ku in (("Why am I getting error code EIBA0005?", "EIBA0005", "KU-ERR-codes-eiba"),
                        ("What does error WONP0001 mean when creating a transfer?", "WONP0001", "KU-ERR-codes-wiac-to-wstm")):
        rows = [e for e in _ev(assistant_evidence, q) if e.origin == "error_catalogue"]
        assert rows and rows[0].ku_id == ku and f"| `{code}` |" in rows[0].text, q


def test_removed_endpoint_questions_include_register_row(assistant_evidence):
    """Audit fix 3 (benchmark EXT-H03, EXT-A05, EXT-H02, G5): the register row stating the removal ranked 7th-15th."""
    cases = (("When was the Create combo card endpoint removed?", "Create combo card"),
             ("Can I still call GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount?", "Get card validation amount"),
             ("Was the CRM API decommissioned?", "| CRM |"),
             ("Should I use the Create marketplace endpoint postmarketplacesv2 to create a new marketplace?", "10/6/26"))
    for q, text in cases:
        reg = [e for e in _ev(assistant_evidence, q) if e.origin == "removal_register"]
        assert reg and reg[0].ku_id == "KU-LIFE-api-endpoints-removed" and text in reg[0].text, q


def test_webhook_verification_short_question(assistant_evidence):
    ev = _ev(assistant_evidence, "How do I verify webhook requests?")
    assert ev[0].ku_id == "KU-EVT-verifying-webhook-requests" and ev[0].origin == "retrieved"
    assert "JWT" in "\n".join(e.text for e in ev if e.ku_id == "KU-EVT-verifying-webhook-requests")


def test_pci_go_live_demo_phrasing_has_no_pci_go_live_evidence(assistant_evidence):
    ev = _ev(assistant_evidence, "How do I perform PCI card go-live?")
    assert "postgolivev1" in ev[0].chunk_id                  # near-match: accounts go-live, not PCI cards
    assert not any("cards-pci/go-live" in e.text for e in ev)
    assert not any(e.origin == "named_operation" for e in ev)


def test_q4_baseline_wrong_operation_answer_is_rejected(retriever):
    """Regression: the captured pre-fix live answer named the transfer-schedule operation (POST /v1/transfers) for
    'create a transfer'. It was accepted as citations_valid=True; it must now fail operation alignment."""
    wrong = ("When you create a transfer schedule (POST /v1/transfers), the platform generates the \"Scheduled payment "
             "created or modified\" event [E1].")
    client = FakeClient(model_json("answered", wrong, ["E1"]))
    r = Assistant(retriever=retriever, generator=OpenAIGenerator(client=client, model="fake")).answer(
        "Which event is generated when I create a transfer?")
    assert r["citations_valid"] is False and r["verification"]["operation_alignment"] is False
    assert any("does not name the operation the question identified" in w for w in r["warnings"])
    assert r["verification"]["semantic_support_verified"] is False


PCI_Q = "After migrating PCI cards, which endpoint sets their migration status to MIGRATED (PCI card go-live)?"


def test_pci_go_live_unanswerable_current_behaviour(retriever):
    """Records current behaviour. The corpus has no PCI card go-live endpoint; retrieval returns the accounts go-live
    operation as a near-match. Abstention depends entirely on the model following prompt rule 4 - there is no
    answerability judge yet."""
    client = FakeClient(model_json("not_documented", "A PCI card go-live endpoint is not documented. The related accounts "
                                   "go-live operation [E1] applies to accounts, not PCI cards.", ["E1"], "PCI card go-live"))
    a = Assistant(retriever=retriever, generator=OpenAIGenerator(client=client, model="fake"))
    r = a.answer(PCI_Q)
    assert "postgolivev1" in r["evidence"][0]["chunk_id"]          # near-match ranked first (accounts go-live)
    assert "cards-pci/go-live" not in json.dumps(client.calls[0]["messages"])  # nothing in evidence documents it
    assert "do not present them as the answer" in SYSTEM_PROMPT    # prompt rule 4 is the only abstention mechanism
    assert r["status"] == "not_documented" and r["citations_valid"] is True


def test_pci_go_live_limitation_model_can_answer_from_near_match(retriever):
    """LIMITATION (documented, not fixed): if the model wrongly answers from the near-match, the pipeline cannot tell -
    the citation is valid and the path is in the cited passage. Needs the planned answerability judge."""
    import re
    e1 = retriever.by_id[Assistant(retriever=retriever, generator=None).evidence(PCI_Q)[0].chunk_id]["text"]
    path = re.search(r"^### `([A-Z]+ [^`]+)`", e1, re.M).group(1)          # the accounts go-live operation
    client = FakeClient(model_json("answered", f"Use `{path}` [E1].", ["E1"]))
    r = Assistant(retriever=retriever, generator=OpenAIGenerator(client=client, model="fake")).answer(PCI_Q)
    assert r["status"] == "answered" and r["citations_valid"] is True and r["warnings"] == []


def test_exact_retrieved_text_is_sent_to_generator(retriever):
    client = FakeClient(model_json())
    a = Assistant(retriever=retriever, generator=OpenAIGenerator(client=client, model="fake"))
    r = a.answer("What does WEAM0029 mean?")
    sent = client.calls[0]["messages"][1]["content"]
    for e in r["evidence"]:
        assert retriever.by_id[e["chunk_id"]]["text"] in sent   # full chunk text, not just ids or scores
        assert f"[{e['label']}] KU: {e['ku_id']}" in sent
    assert client.calls[0]["messages"][0]["content"] == SYSTEM_PROMPT
    assert client.calls[0]["response_format"] == {"type": "json_object"}


def test_citations_map_to_real_sources(retriever):
    client = FakeClient(model_json("answered", "WEAM0029 was removed [E1][E2].", ["E1", "E2"]))
    a = Assistant(retriever=retriever, generator=OpenAIGenerator(client=client, model="fake"))
    r = a.answer("What does WEAM0029 mean?")
    assert r["citations_valid"] is True and [c["label"] for c in r["citations"]] == ["E1", "E2"]
    for c in r["citations"]:
        chunk = retriever.by_id[c["chunk_id"]]
        assert c["ku_id"] == chunk["ku_id"] and c["title"] == chunk["ku_title"]
        for s in c["sources"]:
            assert s["path"] in chunk["ku_sources"] and s["url"].startswith("https://")
            assert os.path.isfile(os.path.join(config.ROOT, "pismo_kb_release_r2", "kb_corpus", s["path"]))
