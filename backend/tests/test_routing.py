"""Deterministic routing: greetings, social messages, vague continuations, follow-ups and standalone questions.
API tests use the REAL pismo_assistant Assistant with counting stub retriever/generator, so "no retrieval, no LLM" is
asserted directly. No index, network or LLM."""
import os
import sys
from pathlib import Path

import pytest

from backend.app.services.assistant_service import AssistantService, get_assistant_service
from backend.app.services.conversation import (ACK_REPLY, CLARIFY_REFERENCE_REPLY, CLARIFY_REPLY, GREETING_REPLY,
                                               SOCIAL_REPLY, Route, is_usable_topic, is_vague, own_identifiers, route)
from backend.app.services.timing import StageClock, TimedGenerator, TimedRetriever

# pismo_assistant.config loads the project .env into os.environ on import; undo that (see test_timing.py).
_ENV_BEFORE = dict(os.environ)
from pismo_assistant.evidence import OperationIndex  # noqa: E402
from pismo_assistant.generation import Generated  # noqa: E402
from pismo_assistant.pipeline import Assistant  # noqa: E402
from pismo_assistant.retrieval import Hit  # noqa: E402
os.environ.clear()
os.environ.update(_ENV_BEFORE)

SCRIPTS = Path(__file__).resolve().parents[2] / "pismo_full_corpus_retrieval_experiment" / "scripts"
CHUNK = {"chunk_id": "KU-EVT-verifying-webhook-requests::p01", "ku_id": "KU-EVT-verifying-webhook-requests",
         "ku_title": "Verifying webhook requests", "section_heading": "JWT", "heading_path": ["Verifying", "JWT"],
         "ku_type": "workflow_guide", "flags": [], "text": "Each webhook request carries a JWT signed by Pismo.",
         "source_refs": [{"path": "guides/webhooks.md", "url": "https://example.com/webhooks"}]}


class CountingRetriever:
    def __init__(self):
        self.chunks, self.chunk_set_hash, self.queries = [CHUNK], "hash-under-test", []

    def search(self, question, k=6):
        self.queries.append(question)
        return [Hit(CHUNK, 1, "retrieved", "hybrid rank")]


class CountingGenerator:
    model = "stub-model"

    def __init__(self):
        self.questions = []

    def generate(self, question, evidence):
        self.questions.append(question)
        return Generated("answered", "Each webhook request carries a JWT [E1].", ["E1"], "", "{}", self.model)


@pytest.fixture
def rig(make_client):
    clock, retriever, generator = StageClock(), CountingRetriever(), CountingGenerator()
    pipeline = Assistant(retriever=TimedRetriever(retriever, clock), generator=TimedGenerator(generator, clock),
                         op_index=OperationIndex([CHUNK]))
    svc = AssistantService(pipeline=pipeline, timeout_s=5.0, clock=clock)
    c = make_client()
    c.app.dependency_overrides[get_assistant_service] = lambda: svc
    c.retriever, c.generator = retriever, generator
    return c


def new_session(c):
    return c.post("/api/sessions").json()["id"]


def ask(c, sid, text):
    r = c.post(f"/api/sessions/{sid}/messages", json={"content": text})
    assert r.status_code == 201, r.text
    return r.json()["assistant_message"]


def assert_direct(a, kind, reason, reply):
    d = a["details"]
    assert a["content"] == reply and a["citations"] == [] and a["status"] == "answered"
    assert d["response_kind"] == kind and d["route"] == {"outcome": kind, "reason": reason, "source": "rule"}
    assert "index" not in d and d["model"] is None and d["evidence"] == [] and d["context"]["used"] is False
    assert "llm_ms" not in d["timings"] and "retrieval_ms" not in d["timings"]


# ---- decision table (pure functions) -------------------------------------------------------------------------------

@pytest.mark.parametrize("text,topic,expected", [
    ("hi", False, Route("greeting", "greeting")), ("Thank you!", True, Route("greeting", "thanks")),
    ("how are you?", False, Route("social", "social")), ("How's it going?", True, Route("social", "social")),
    ("got it, thanks", True, Route("social", "acknowledgement")), ("ok", True, Route("social", "acknowledgement")),
    ("yes explain more", False, Route("clarification", "no_topic")),
    ("explain more", False, Route("clarification", "no_topic")), ("tell me more", False, Route("clarification", "no_topic")),
    ("more details please", False, Route("clarification", "no_topic")),
    ("what do you mean?", False, Route("clarification", "no_topic")),
    ("yes", True, Route("clarification", "no_subject")),
    ("Is it deprecated?", False, Route("clarification", "unresolved_reference")),
    ("yes explain more", True, Route("rag", "continuation", True)), ("tell me more", True, Route("rag", "continuation", True)),
    ("what do you mean?", True, Route("rag", "continuation", True)),
    ("Can you explain the JWT part?", True, Route("rag", "referential_cue", True)),
    ("What about its request fields?", True, Route("rag", "referential_cue", True)),
    ("Is it deprecated?", True, Route("rag", "referential_cue", True)),
    ("Can you explain the JWT part?", False, Route("rag", "standalone")),
    ("What about events?", False, Route("rag", "standalone")),
    ("What does the x-CID header mean?", True, Route("rag", "own_identifier")),
    ("Which event does post-transfers emit?", True, Route("rag", "own_identifier")),
    ("How do I authenticate API requests?", True, Route("rag", "standalone")),
    ("hello WEAM0029", False, Route("rag", "own_identifier")),
    ("Hi, how do I configure a webhook?", True, Route("rag", "standalone")),
])
def test_route_decisions(text, topic, expected):
    assert route(text, has_topic=topic) == expected


@pytest.mark.parametrize("text", [
    "What does the x-CID header mean?", "Which event does post-transfers emit?", "WEAM0029?", "What is account_id?",
    "What does getAccountById return?", "Is GET /cardsonfile/v2/cardsonfile/cards/{uuid} deprecated?",
    "explain transfer-created-1", "x-tenant", "How do I authenticate API requests?", "Rate limits?", "JWT?",
    "What is a hold?", "webhook retries", "PCI card go-live steps?",
])
def test_technical_questions_are_never_sent_to_clarification(text):
    for topic in (False, True):
        assert route(text, has_topic=topic).outcome == "rag", (text, topic)


def test_identifier_detection_matches_the_retriever():
    sys.path.insert(0, str(SCRIPTS))
    try:
        from retrievers import detect_identifiers
    finally:
        sys.path.remove(str(SCRIPTS))
    samples = ["What does the x-CID header mean?", "WEAM0029 and WMLP1020", "GET /v1/accounts/{accountId}/holds",
               "What is account_id?", "What does getAccountById return?", "transfer-created-1 event", "mTLS setup",
               "iOS SDK", "the eCommerce flow"]
    for s in samples:
        assert set(detect_identifiers(s)) <= set(own_identifiers(s)), s
    # deliberate difference: English multi-hyphen words are retrieval identifiers but do not name a subject
    assert detect_identifiers("explain it step-by-step") == ["step-by-step"] and own_identifiers("explain it step-by-step") == []


def test_vague_and_usable_topic():
    assert all(is_vague(t) for t in ("yes explain more", "explain more", "tell me more", "what do you mean?", "go on", "why?"))
    assert not any(is_vague(t) for t in ("explain the JWT part", "explain x-CID", "tell me about holds", "WEAM0029"))
    assert not any(is_usable_topic(t) for t in ("hi", "thanks", "how are you?", "yes explain more", "got it"))
    assert is_usable_topic("How do I verify webhook requests?")


# ---- API: no retrieval / no LLM for direct routes (cases 1, 2, 7) ---------------------------------------------------

def test_case1_greeting_then_vague_continuation_asks_for_clarification(rig):
    sid = new_session(rig)
    assert_direct(ask(rig, sid, "hi"), "greeting", "greeting", GREETING_REPLY)
    a = ask(rig, sid, "yes explain more")
    assert_direct(a, "clarification", "no_topic", CLARIFY_REPLY)
    assert rig.retriever.queries == [] and rig.generator.questions == []          # nothing searched, no LLM
    assert "documented" not in a["content"].lower()                               # no claim about the KB contents
    act = rig.get("/api/activity").json()["activity"][0]
    assert act["event"] == "message.clarification" and act["evidence_count"] == 0 and act["model"] is None


def test_case2_social_message_after_greeting(rig):
    sid = new_session(rig)
    ask(rig, sid, "hi")
    assert_direct(ask(rig, sid, "how are you?"), "social", "social", SOCIAL_REPLY)
    assert_direct(ask(rig, sid, "Got it, thanks!"), "social", "acknowledgement", ACK_REPLY)
    assert rig.retriever.queries == [] and rig.generator.questions == []


@pytest.mark.parametrize("text", ["explain more", "tell me more", "what do you mean?", "more details please"])
def test_case7_vague_message_without_context(rig, text):
    assert_direct(ask(rig, new_session(rig), text), "clarification", "no_topic", CLARIFY_REPLY)
    assert rig.retriever.queries == [] and rig.generator.questions == []


def test_unresolved_pronoun_without_topic(rig):
    sid = new_session(rig)
    ask(rig, sid, "hi")
    assert_direct(ask(rig, sid, "Is it deprecated?"), "clarification", "unresolved_reference", CLARIFY_REFERENCE_REPLY)
    assert rig.retriever.queries == []


def test_earlier_vague_and_social_messages_are_not_topics(rig):
    sid = new_session(rig)
    for t in ("hi", "how are you?", "yes explain more"):
        ask(rig, sid, t)
    assert_direct(ask(rig, sid, "tell me more"), "clarification", "no_topic", CLARIFY_REPLY)
    assert rig.retriever.queries == []


# ---- API: RAG routes keep context, citations and index (cases 3, 4, 5) ---------------------------------------------

def test_case3_follow_up_uses_same_session_topic(rig):
    sid = new_session(rig)
    ask(rig, sid, "How does webhook verification work in Pismo?")
    a = ask(rig, sid, "Can you explain the JWT part?")
    q = rig.retriever.queries[-1]
    assert q.startswith("Can you explain the JWT part?") and '"How does webhook verification work in Pismo?"' in q
    assert rig.generator.questions[-1] == q                                       # generation sees the same question
    d = a["details"]
    assert d["route"] == {"outcome": "follow_up", "reason": "referential_cue", "source": "rule"} and d["context"]["used"] is True
    assert a["citations"][0]["label"] == "E1" and d["citations_valid"] is not None
    assert d["index"] == {"chunk_set_hash": "hash-under-test"} and "response_kind" not in d


def test_continuation_after_a_real_topic_resolves_it(rig):
    sid = new_session(rig)
    ask(rig, sid, "hi")
    ask(rig, sid, "How do I verify webhook requests?")
    ask(rig, sid, "thanks")
    a = ask(rig, sid, "yes explain more")
    q = rig.retriever.queries[-1]
    assert q.startswith("yes explain more") and '"How do I verify webhook requests?"' in q
    assert '"hi"' not in q and '"thanks"' not in q
    assert a["details"]["route"] == {"outcome": "follow_up", "reason": "continuation", "source": "rule"}
    assert a["details"]["context"]["pipeline_question"] == q
    stored = rig.get(f"/api/sessions/{sid}/messages").json()["messages"]
    assert stored[-2]["content"] == "yes explain more"                            # the user's text is stored as typed


def test_case4_api_follow_up(rig):
    sid = new_session(rig)
    ask(rig, sid, "What does the post-transfers endpoint do?")
    ask(rig, sid, "What about its request fields?")
    assert '"What does the post-transfers endpoint do?"' in rig.retriever.queries[-1]


def test_case5_standalone_identifier_question_is_not_contaminated(rig):
    sid = new_session(rig)
    ask(rig, sid, "How do I verify webhook requests?")
    a = ask(rig, sid, "What does the x-CID header mean?")
    assert rig.retriever.queries[-1] == "What does the x-CID header mean?"
    assert a["details"]["route"] == {"outcome": "pismo_question", "reason": "own_identifier", "source": "rule"} and a["details"]["context"]["used"] is False


def test_follow_up_never_uses_another_sessions_topic(rig):
    a, b = new_session(rig), new_session(rig)
    ask(rig, a, "How do I verify webhook requests?")
    assert_direct(ask(rig, b, "tell me more"), "clarification", "no_topic", CLARIFY_REPLY)
    assert len(rig.retriever.queries) == 1
