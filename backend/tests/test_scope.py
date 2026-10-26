"""Pismo-only scope: clearly unrelated requests are answered with a fixed scope reply BEFORE retrieval and generation,
on the regular and the streaming endpoint; Pismo questions (with or without the word "Pismo") still reach the pipeline.
Uses the REAL pismo_assistant Assistant with counting doubles (see test_streaming.py). No index, network or LLM."""
import json
import re
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from backend.app.core.config import get_settings
from backend.app.main import create_app
from backend.app.services.assistant_service import get_assistant_service
from backend.app.services.conversation import CLARIFY_REPLY, OUT_OF_SCOPE_REPLY, out_of_scope_topic, route
from backend.app.services.session_guard import SessionGuard, get_session_guard
from backend.tests.test_streaming import FakeClient, FakeStream, build_service, model_json, parse_sse, pieces

ROOT = Path(__file__).resolve().parents[2]
BIRIYANI_REPLY = ("I'm designed to help with Pismo APIs, developer documentation, integrations, events, webhooks, and "
                  "related implementation questions. I can't help with recipes or unrelated topics. What Pismo "
                  "integration question can I help you with?")
OUT_OF_SCOPE = {"how do i make chicken biriyani": "recipes", "Explain photosynthesis.": "general knowledge questions",
                "Who won yesterday's football match?": "sports", "Write a poem about my dog.": "creative writing"}
IN_SCOPE = ["How do I authenticate API requests?", "What does the x-CID header mean?",
            "How does webhook verification work in Pismo?", "Which event does post-transfers emit?",
            "How can I troubleshoot a failed transfer?", "What are the request fields for post-transfers?"]


@pytest.fixture
def rig(engine, settings):
    clients = []

    def make():
        fake = FakeClient(stream=FakeStream(pieces(model_json())), full=model_json())
        app = create_app()
        svc, guard = build_service(fake), SessionGuard()
        app.dependency_overrides.update({get_assistant_service: lambda: svc, get_settings: lambda: settings,
                                         get_session_guard: lambda: guard})
        c = TestClient(app).__enter__()
        c.fake, c.retriever = fake, svc._pipeline.retriever._inner
        clients.append(c)
        return c

    yield make
    for c in clients:
        c.__exit__(None, None, None)


def ask(c, sid, text):
    r = c.post(f"/api/sessions/{sid}/messages", json={"content": text})
    assert r.status_code == 201, r.text
    return r.json()["assistant_message"]


def new_session(c):
    return c.post("/api/sessions").json()["id"]


def assert_scope_reply(a, topic):
    d = a["details"]
    assert a["status"] == "answered" and a["citations"] == [] and d["evidence"] == []
    assert d["response_kind"] == "out_of_scope" and d["route"] == {"outcome": "out_of_scope", "reason": topic, "source": "rule"}
    assert "index" not in d and d["model"] is None and d["context"]["used"] is False
    assert "llm_ms" not in d["timings"] and "retrieval_ms" not in d["timings"] and d["timings"]["total_ms"] > 0
    assert a["content"] == OUT_OF_SCOPE_REPLY.format(topic=topic)
    assert "documented" not in a["content"].lower() and "Pismo APIs" in a["content"]


# ---- decisions -----------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("text,topic", OUT_OF_SCOPE.items())
def test_unrelated_requests_route_out_of_scope(text, topic):
    for has_topic in (False, True):                         # earlier Pismo context never rescues them
        assert route(text, has_topic=has_topic).outcome == "out_of_scope"
    assert out_of_scope_topic(text) == topic


def test_exact_reply_for_the_reported_case():
    assert OUT_OF_SCOPE_REPLY.format(topic=out_of_scope_topic("how do i make chicken biriyani")) == BIRIYANI_REPLY


@pytest.mark.parametrize("text", [
    "how do i make chicken biriyani for my API team lunch",   # one incidental domain word does not rescue a dish
    "WEAM0029 biriyani recipe",                                # nor does an identifier
    "Tell me a joke", "What's the weather tomorrow?", "how do I cook chicken soup",
])
def test_technical_looking_words_do_not_rescue_unrelated_requests(text):
    assert route(text, has_topic=True).outcome == "out_of_scope"


@pytest.mark.parametrize("text", IN_SCOPE + [
    "How do I bake a request signature?", "How do I cook up a test payment in the sandbox?",
    "Is there a recipe for retrying failed webhooks?", "Write a poem about Pismo webhooks",
])
def test_pismo_questions_are_never_rejected(text):
    assert out_of_scope_topic(text) is None and route(text, has_topic=False).outcome == "rag"


def test_no_benchmark_or_demo_question_is_rejected():
    bench = json.loads((ROOT / "pismo_full_corpus_retrieval_experiment" / "BENCHMARK.json").read_text(encoding="utf-8"))
    questions = [i["q"] for part in ("primary", "extension") for i in bench[part]]
    questions += re.findall(r'"q": "([^"]+)"', (ROOT / "pismo_assistant" / "verify_demo.py").read_text(encoding="utf-8"))
    assert len(questions) == 90
    assert [q for q in questions if out_of_scope_topic(q)] == []


# ---- regular endpoint ------------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("text,topic", OUT_OF_SCOPE.items())
def test_out_of_scope_skips_retrieval_and_generation(rig, text, topic):
    c = rig()
    sid = new_session(c)
    a = ask(c, sid, text)
    assert_scope_reply(a, topic)
    assert c.retriever.calls == 0 and c.fake.calls == []                       # zero retrieval, zero model calls
    act = c.get("/api/activity").json()["activity"][0]
    assert act["event"] == "message.out_of_scope" and act["evidence_count"] == 0 and act["model"] is None
    msgs = c.get(f"/api/sessions/{sid}/messages").json()["messages"]
    assert [m["role"] for m in msgs] == ["user", "assistant"] and msgs[0]["content"] == text


def test_in_scope_questions_reach_retrieval(rig):
    c = rig()
    sid = new_session(c)
    for i, q in enumerate(IN_SCOPE, 1):
        a = ask(c, sid, q)
        assert a["details"]["route"]["outcome"] == "pismo_question" and c.retriever.calls == i
        assert a["details"]["index"] == {"chunk_set_hash": "stream-index-hash"}


# ---- streaming endpoint ----------------------------------------------------------------------------------------------------

def test_streamed_out_of_scope_request_is_a_normal_final_reply(rig):
    c = rig()
    sid = new_session(c)
    r = c.post(f"/api/sessions/{sid}/messages/stream", json={"content": "how do i make chicken biriyani"})
    ev = parse_sse(r.text)
    assert r.status_code == 200 and [e for e, _, _ in ev] == ["status", "status", "final"]       # no deltas, no errors
    assert [d["stage"] for e, d, _ in ev if e == "status"] == ["accepted", "saving"]
    assert ev[0][1]["route"] == {"outcome": "out_of_scope", "reason": "recipes", "source": "rule"}
    assert len({d["request_id"] for _, d, _ in ev}) == 1
    a = ev[-1][1]["exchange"]["assistant_message"]
    assert ev[-1][1]["http_status"] == 201 and a["content"] == BIRIYANI_REPLY
    assert_scope_reply(a, "recipes")
    assert c.retriever.calls == 0 and c.fake.calls == []


# ---- follow-ups and sessions -----------------------------------------------------------------------------------------------

def test_follow_ups_around_an_unrelated_request(rig):
    c = rig()
    sid = new_session(c)
    ask(c, sid, "How does webhook verification work in Pismo?")
    a = ask(c, sid, "Can you explain the JWT part?")                          # genuine follow-up keeps context
    assert a["details"]["context"]["used"] is True and c.retriever.calls == 2
    assert_scope_reply(ask(c, sid, "how do i make chicken biriyani"), "recipes")   # not pulled into the old topic
    assert c.retriever.calls == 2
    a = ask(c, sid, "tell me more")                                          # continues the webhook topic, not biriyani
    assert a["details"]["route"] == {"outcome": "follow_up", "reason": "continuation", "source": "rule"}
    q = a["details"]["context"]["pipeline_question"]
    assert "webhook" in q.lower() and "biriyani" not in q.lower()


def test_unrelated_request_never_becomes_a_topic_and_sessions_stay_isolated(rig):
    c = rig()
    a, b = new_session(c), new_session(c)
    ask(c, a, "How does webhook verification work in Pismo?")
    ask(c, b, "how do i make chicken biriyani")
    r = ask(c, b, "tell me more")                                            # only biriyani before it, in this session
    assert r["content"] == CLARIFY_REPLY and r["details"]["route"]["outcome"] == "clarification"
    assert c.retriever.calls == 1                                            # session a's question never reached b
