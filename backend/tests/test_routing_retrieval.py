"""Routing checked against the REAL index and retriever (no generation, no network; ~15 s to load).

Builds each retrieval query exactly as the backend does (route() then build_pipeline_question) and checks the evidence:
vague messages never reach retrieval on their own, resolved follow-ups find the earlier topic's documentation, and
standalone identifier questions keep their own evidence. Skipped if the local index or embedding model is unavailable."""
import os

import pytest

from backend.app.services.conversation import build_pipeline_question, route


@pytest.fixture(scope="module")
def pipeline():
    before = dict(os.environ)
    os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", OPENAI_API_KEY="")   # never any network
    try:
        from pismo_assistant.evidence import matched_operations
        from pismo_assistant.pipeline import Assistant
        a = Assistant()
    except Exception as e:  # pragma: no cover - depends on local index/model files
        pytest.skip(f"real index not available: {type(e).__name__}")
    finally:
        os.environ.clear()                       # pismo_assistant.config loaded the project .env; undo that
        os.environ.update(before)
    return a, matched_operations


def backend_query(message, history):
    """(route, retrieval query) as conversation._exchange builds them; history = usable earlier user questions."""
    r = route(message, has_topic=bool(history))
    if r.outcome != "rag":
        return r, None
    return r, build_pipeline_question(message, history if r.use_context else [], 600, follow_up=r.use_context)[0]


def kus(a, q):
    return [e.ku_id for e in a.evidence(q)]


def test_case1_vague_message_never_reaches_retrieval(pipeline):
    a, _ = pipeline
    r, q = backend_query("yes explain more", [])               # only "hi" before it: no usable topic
    assert r.outcome == "clarification" and q is None
    # the hazard this prevents: as typed, the message retrieves nothing but incident-management passages
    assert set(kus(a, "yes explain more")) == {"KU-SUP-incidents"}


@pytest.mark.parametrize("message", ["yes explain more", "tell me more", "what do you mean?"])
def test_continuation_resolves_to_the_earlier_topic(pipeline, message):
    a, _ = pipeline
    r, q = backend_query(message, ["How do I verify webhook requests?"])
    assert r.reason == "continuation"
    ev = kus(a, q)
    assert sum("webhook" in k.lower() for k in ev) >= 3 and "KU-SUP-incidents" not in ev


def test_case3_jwt_follow_up_finds_webhook_verification(pipeline):
    a, _ = pipeline
    r, q = backend_query("Can you explain the JWT part?", ["How does webhook verification work in Pismo?"])
    assert r.reason == "referential_cue"
    ev = a.evidence(q)
    assert sum(e.ku_id == "KU-EVT-verifying-webhook-requests" for e in ev) >= 3
    assert any("jwt" in e.text.lower() for e in ev)
    # without the topic the same words retrieve mostly unrelated authorization material
    assert sum(k == "KU-EVT-verifying-webhook-requests" for k in kus(a, "Can you explain the JWT part?")) <= 1


def test_case4_request_fields_follow_up_resolves_the_operation(pipeline):
    a, matched_operations = pipeline
    r, q = backend_query("What about its request fields?", ["What does the post-transfers endpoint do?"])
    assert r.reason == "referential_cue"
    assert [m["operation"] for m in matched_operations(q, a.op_index)] == ["post-transfers"]
    ev = a.evidence(q)
    # the operation's API reference is retrieved directly (so assembly does not re-add it as named_operation) ...
    assert any(e.ku_id.startswith("KU-API-core-platform-payment-methods") and "post-transfers" in e.text.lower() for e in ev)
    # ... and its events table is attached for the operation the earlier question named
    assert any(e.origin == "operation_events" and "post-transfers" in e.reason for e in ev)
    assert "KU-SUP-service-desk-requests" not in [e.ku_id for e in ev]     # what the message alone retrieves


def test_case5_header_question_stays_standalone(pipeline):
    a, _ = pipeline
    r, q = backend_query("What does the x-CID header mean?", ["How do I verify webhook requests?"])
    assert r.reason == "own_identifier" and q == "What does the x-CID header mean?"
    ev = a.evidence(q)
    assert any("x-cid" in e.text.lower() for e in ev[:3])                   # exact-identifier promotion intact
    assert not any(e.ku_id == "KU-EVT-verifying-webhook-requests" for e in ev)


@pytest.mark.parametrize("message,expected_ku", [
    ("What does WEAM0029 mean?", "KU-CHG-2-october-2026"),
    ("Which event does post-transfers emit?", None),
])
def test_case6_identifier_questions_after_another_topic(pipeline, message, expected_ku):
    a, matched_operations = pipeline
    r, q = backend_query(message, ["How do I verify webhook requests?"])
    assert r.outcome == "rag" and q == message
    if expected_ku:
        assert kus(a, q)[0] == expected_ku
    else:
        assert [m["operation"] for m in matched_operations(q, a.op_index)] == ["post-transfers"]
