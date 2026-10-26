"""Hybrid routing: deterministic rules first, then one LLM classification where interpretation is needed.
A fake classifier client (counted separately) stands in for the model; the REAL pismo_assistant pipeline runs with a
counting retriever and a fake answer-model client (see test_streaming.py). No network, no live model."""
import json
import time
from types import SimpleNamespace

import httpx
import openai
import pytest
from fastapi.testclient import TestClient

from backend.app.core.config import Settings, get_settings
from backend.app.main import create_app
from backend.app.services.assistant_service import get_assistant_service
from backend.app.services.conversation import (CLARIFY_REPLY, CLARIFY_SCOPE_REPLY, GREETING_REPLY, OUT_OF_SCOPE_REPLY)
from backend.app.services.router import (ClassifierError, IntentClassifier, Router, get_router, parse_classification)
from backend.app.services.session_guard import SessionGuard, get_session_guard
from backend.tests.test_streaming import FakeClient, FakeStream, build_service, model_json, parse_sse, pieces

WEBHOOK_Q = "How does webhook verification work?"


def policy(payload):
    """A plausible classifier: decides from the message and the earlier questions it was given."""
    m, earlier = payload["message"].lower(), payload["earlier_questions"]
    if "president" in m or "capital" in m:
        return {"route": "out_of_scope", "reason": "general_knowledge"}
    if "jwt part" in m or "its request fields" in m:
        return {"route": "follow_up", "reason": "refers_to_earlier_question"} if earlier else \
            {"route": "clarification", "reason": "ambiguous_reference"}
    if "meeting notes" in m:
        return {"route": "clarification", "reason": "no_clear_subject"}
    return {"route": "pismo_question", "reason": "pismo_concept_question"}


class FakeClassifierClient:
    def __init__(self, decide=policy, raw=None, error=None, delay=0.0):
        self.decide, self.raw, self.error, self.delay, self.calls = decide, raw, error, delay, []
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    def _create(self, **kw):
        self.calls.append(kw)
        if self.delay:
            time.sleep(self.delay)
        if self.error:
            raise self.error
        payload = json.loads(kw["messages"][1]["content"])
        content = self.raw if self.raw is not None else json.dumps(self.decide(payload))
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=content))])

    def payloads(self):
        return [json.loads(k["messages"][1]["content"]) for k in self.calls]


@pytest.fixture
def rig(engine, settings):
    clients = []

    def make(classifier_client=None, answer=None, timeout_s=1.0, model="gpt-5-mini"):
        cls = classifier_client or FakeClassifierClient()
        fake = FakeClient(stream=FakeStream(pieces(answer or model_json())), full=answer or model_json())
        app = create_app()
        svc, guard = build_service(fake), SessionGuard()
        router = Router(IntentClassifier(model, timeout_s, "minimal", client=cls), timeout_s)
        app.dependency_overrides.update({get_assistant_service: lambda: svc, get_settings: lambda: settings,
                                         get_session_guard: lambda: guard, get_router: lambda: router})
        c = TestClient(app).__enter__()
        c.cls, c.answer_model, c.retriever = cls, fake, svc._pipeline.retriever._inner
        clients.append(c)
        return c

    yield make
    for c in clients:
        c.__exit__(None, None, None)


def new_session(c):
    return c.post("/api/sessions").json()["id"]


def ask(c, sid, text, streamed=False):
    if streamed:
        r = c.post(f"/api/sessions/{sid}/messages/stream", json={"content": text})
        ev = parse_sse(r.text)
        terminal = ev[-1]
        return terminal[1]["exchange"]["assistant_message"], ev
    r = c.post(f"/api/sessions/{sid}/messages", json={"content": text})
    assert r.status_code == 201, r.text
    return r.json()["assistant_message"], None


def route_of(a):
    return {k: v for k, v in a["details"]["route"].items() if k != "classifier_ms"}


# ---- structured output validation ---------------------------------------------------------------------------------------

@pytest.mark.parametrize("raw", [
    "not json", "[]", '{"route": "pismo_question"}', '{"route": "answer_it", "reason": "pismo_api_question"}',
    '{"route": "out_of_scope", "reason": "because I said so"}', '{"route": "greeting", "reason": "greeting"}', "",
])
def test_invalid_classifier_output_is_rejected(raw):
    with pytest.raises(ClassifierError) as e:
        parse_classification(raw, has_context=True)
    assert e.value.kind == "invalid_output"


def test_valid_output_extra_keys_ignored_and_follow_up_needs_context():
    raw = '{"route": "pismo_question", "reason": "pismo_api_question", "confidence": 0.01, "answer": "made up"}'
    assert parse_classification(raw, has_context=False) == ("pismo_question", "pismo_api_question")
    raw = '{"route": "follow_up", "reason": "refers_to_earlier_question"}'
    assert parse_classification(raw, has_context=False) == ("clarification", "follow_up_without_topic")


def test_classifier_request_shape():
    cls = FakeClassifierClient()
    IntentClassifier("gpt-5-mini", 4.0, "minimal", client=cls).classify("What is a hold?", ["How do I create a transfer?"])
    kw = cls.calls[0]
    assert kw["model"] == "gpt-5-mini" and kw["response_format"] == {"type": "json_object"} and kw["reasoning_effort"] == "minimal"
    assert kw["max_completion_tokens"] == 300 and len(kw["messages"]) == 2
    assert json.loads(kw["messages"][1]["content"]) == {"message": "What is a hold?", "earlier_questions": ["How do I create a transfer?"]}
    cls2 = FakeClassifierClient()
    IntentClassifier("gpt-4.1-nano", 4.0, "minimal", client=cls2).classify("q", [])
    assert "reasoning_effort" not in cls2.calls[0]                # only sent to reasoning models


def test_router_settings_default_to_the_configured_model():
    s = Settings(_env_file=None, DATABASE_URL="sqlite://", OPENAI_MODEL="gpt-5-mini", ROUTER_ENABLED=True)
    assert s.router_model_name == "gpt-5-mini" and s.router_timeout_s == 8.0 and s.router_reasoning_effort == "minimal"
    assert Settings(_env_file=None, DATABASE_URL="sqlite://", ROUTER_MODEL="gpt-5-nano").router_model_name == "gpt-5-nano"
    assert s.router_timeout_s + s.assistant_timeout_s < 120          # stays inside the frontend's request timeout


# ---- deterministic cases never call the classifier ------------------------------------------------------------------

@pytest.mark.parametrize("text,outcome,reason", [
    ("hi", "greeting", "greeting"), ("thank you", "greeting", "thanks"), ("how are you?", "social", "social"),
    ("How do I make chicken biriyani?", "out_of_scope", "recipes"), ("Explain more", "clarification", "no_topic"),
    ("What does WEAM0029 mean?", "pismo_question", "own_identifier"),
    ("What does the x-CID header mean?", "pismo_question", "own_identifier"),
    ("Which event does post-transfers emit?", "pismo_question", "own_identifier"),
])
def test_rules_decide_the_obvious_cases_without_the_classifier(rig, text, outcome, reason):
    c = rig()
    a, _ = ask(c, new_session(c), text)
    assert route_of(a) == {"outcome": outcome, "reason": reason, "source": "rule"} and c.cls.calls == []
    assert ("index" in a["details"]) == (outcome == "pismo_question")


def test_hello_then_explain_more_is_a_clarification(rig):
    c = rig()
    sid = new_session(c)
    assert ask(c, sid, "hello")[0]["content"] == GREETING_REPLY
    a, _ = ask(c, sid, "Explain more")
    assert a["content"] == CLARIFY_REPLY and c.cls.calls == [] and c.retriever.calls == 0


# ---- classifier decisions -------------------------------------------------------------------------------------------------

def test_general_knowledge_is_out_of_scope_without_rag(rig):
    c = rig()
    a, _ = ask(c, new_session(c), "Who is the president of India?")
    assert route_of(a) == {"outcome": "out_of_scope", "reason": "general_knowledge", "source": "classifier"}
    assert a["content"] == OUT_OF_SCOPE_REPLY.format(topic="general knowledge questions")
    assert c.retriever.calls == 0 and c.answer_model.calls == [] and len(c.cls.calls) == 1
    assert a["citations"] == [] and a["details"]["evidence"] == [] and "index" not in a["details"]
    assert a["details"]["route"]["classifier_ms"] >= 0 and a["details"]["timings"]["routing_ms"] >= 0


@pytest.mark.parametrize("text", [WEBHOOK_Q, "How do I authenticate API requests?", "How can I troubleshoot a failed transfer?"])
def test_pismo_questions_reach_rag_once_classified(rig, text):
    c = rig()
    a, _ = ask(c, new_session(c), text)
    assert route_of(a) == {"outcome": "pismo_question", "reason": "pismo_concept_question", "source": "classifier"}
    assert c.retriever.calls == 1 and len(c.answer_model.calls) == 1 and len(c.cls.calls) == 1
    assert c.cls.payloads()[0] == {"message": text, "earlier_questions": []}          # standalone: no context sent
    assert a["details"]["context"]["pipeline_question"] == text and a["details"]["index"]["chunk_set_hash"]


def test_follow_up_uses_same_session_context(rig):
    c = rig()
    sid = new_session(c)
    ask(c, sid, WEBHOOK_Q)
    a, _ = ask(c, sid, "Can you explain the JWT part?")
    assert route_of(a) == {"outcome": "follow_up", "reason": "refers_to_earlier_question", "source": "classifier"}
    assert c.cls.payloads()[-1] == {"message": "Can you explain the JWT part?", "earlier_questions": [WEBHOOK_Q]}
    ctx = a["details"]["context"]
    assert ctx["used"] is True and WEBHOOK_Q in ctx["pipeline_question"]


def test_standalone_question_is_not_contaminated_and_sessions_stay_isolated(rig):
    c = rig()
    a_sid, b_sid = new_session(c), new_session(c)
    ask(c, a_sid, WEBHOOK_Q)
    ask(c, a_sid, "How do I make chicken biriyani?")
    a, _ = ask(c, a_sid, "How do I authenticate API requests?")
    assert a["details"]["context"]["pipeline_question"] == "How do I authenticate API requests?"
    b, _ = ask(c, b_sid, "Can you explain the JWT part?")                  # other session has no topic
    assert route_of(b) == {"outcome": "clarification", "reason": "ambiguous_reference", "source": "classifier"}
    assert c.cls.payloads()[-1] == {"message": "Can you explain the JWT part?", "earlier_questions": []}   # nothing from a
    assert all("biriyani" not in " ".join(p["earlier_questions"]).lower() for p in c.cls.payloads())
    assert c.retriever.calls == 2                                          # webhook + authenticate, nothing else


def test_classifier_clarification_and_no_reply_text_from_the_model(rig):
    c = rig()
    assert ask(c, new_session(c), "Can you help me with something?")[0]["details"]["route"]["source"] == "rule"  # filler only
    a, _ = ask(c, new_session(c), "Quick question about the meeting notes")
    assert route_of(a) == {"outcome": "clarification", "reason": "no_clear_subject", "source": "classifier"}
    assert a["content"] == CLARIFY_SCOPE_REPLY and c.retriever.calls == 0
    injected = FakeClassifierClient(raw='{"route": "out_of_scope", "reason": "unrelated_topic", "answer": "Here is a recipe"}')
    c2 = rig(injected)
    a2, _ = ask(c2, new_session(c2), "Tell me about chess openings")
    assert "recipe" not in a2["content"].lower() and a2["content"].startswith("I'm designed to help with Pismo")


def test_classifier_cannot_bypass_citation_validation(rig):
    bad = "Webhook requests carry a JWT signed by Pismo [E1]. See also [E9]."
    c = rig(answer=model_json(bad, ("E1", "E9")))
    a, _ = ask(c, new_session(c), WEBHOOK_Q)
    assert route_of(a)["source"] == "classifier"
    assert [x["label"] for x in a["citations"]] == ["E1"] and any("not supplied" in w for w in a["details"]["warnings"])


# ---- failures: one attempt, documented fallback ------------------------------------------------------------------------

def _timeout_error():
    return openai.APITimeoutError(request=httpx.Request("POST", "https://api.invalid/v1/chat/completions"))


@pytest.mark.parametrize("client,kind", [
    (FakeClassifierClient(raw="I think this is a Pismo question"), "invalid_output"),
    (FakeClassifierClient(raw='{"route": "pismo_question", "reason": "trust me"}'), "invalid_output"),
    (FakeClassifierClient(error=RuntimeError("503 from provider")), "provider_error"),
    (FakeClassifierClient(error=_timeout_error()), "timeout"),
])
def test_fallback_policy(rig, client, kind):
    c = rig(client)
    sid = new_session(c)
    domain, _ = ask(c, sid, WEBHOOK_Q)                          # Pismo vocabulary: proceeds to RAG
    assert route_of(domain) == {"outcome": "pismo_question", "reason": "standalone", "source": "fallback", "fallback": kind}
    assert c.retriever.calls == 1
    unclear, _ = ask(c, sid, "Who is the president of India?")  # no Pismo vocabulary: clarification, never RAG
    assert route_of(unclear) == {"outcome": "clarification", "reason": "unclear_scope", "source": "fallback", "fallback": kind}
    assert unclear["content"] == CLARIFY_SCOPE_REPLY and c.retriever.calls == 1 and len(c.answer_model.calls) == 1
    follow, _ = ask(c, sid, "Can you explain the JWT part?")    # referential with a topic: same-session follow-up
    assert route_of(follow) == {"outcome": "follow_up", "reason": "referential_cue", "source": "fallback", "fallback": kind}
    assert follow["details"]["context"]["used"] is True
    assert len(client.calls) == 3                              # exactly one attempt per message, no retries


def test_slow_classifier_times_out_within_the_router_budget(rig):
    c = rig(FakeClassifierClient(delay=1.5), timeout_s=0.2)    # safety net: router timeout + 1 s
    t0 = time.perf_counter()
    a, _ = ask(c, new_session(c), "Who is the president of India?")
    assert route_of(a) == {"outcome": "clarification", "reason": "unclear_scope", "source": "fallback", "fallback": "timeout"}
    assert time.perf_counter() - t0 < 1.5 + 1.0 and c.retriever.calls == 0


def test_classifier_unavailable_falls_back(rig):
    class Unavailable(IntentClassifier):
        @property
        def client(self):
            raise ClassifierError("unavailable")               # e.g. no API key configured
    c = rig()
    c.app.dependency_overrides[get_router] = lambda: Router(Unavailable("gpt-5-mini", 1.0), 1.0)
    a, _ = ask(c, new_session(c), "Who is the president of India?")
    assert route_of(a) == {"outcome": "clarification", "reason": "unclear_scope", "source": "fallback", "fallback": "unavailable"}


# ---- streaming and non-streaming use the same policy ---------------------------------------------------------------------

MESSAGES = ["hi", "How do I make chicken biriyani?", "Who is the president of India?", WEBHOOK_Q,
            "What does WEAM0029 mean?", "Explain more", "Quick question about the meeting notes"]


def test_streaming_and_regular_endpoints_route_identically(rig):
    c = rig()
    regular, streamed = new_session(c), new_session(c)
    for m in MESSAGES:
        a, _ = ask(c, regular, m)
        s, _ = ask(c, streamed, m, streamed=True)
        assert route_of(a) == route_of(s), m
        assert a["content"] == s["content"] or route_of(a)["outcome"] == "pismo_question", m


def test_streamed_out_of_scope_after_classification_terminates_cleanly(rig):
    c = rig()
    s, ev = ask(c, new_session(c), "Who is the president of India?", streamed=True)
    kinds = [e for e, _, _ in ev]
    stages = [d["stage"] for e, d, _ in ev if e == "status"]
    assert kinds == ["status", "status", "status", "final"] and stages == ["routing", "accepted", "saving"]
    assert ev[1][1]["route"]["outcome"] == "out_of_scope" and ev[1][1]["route"]["source"] == "classifier"
    assert "delta" not in kinds and c.retriever.calls == 0 and c.answer_model.calls == [] and len(c.cls.calls) == 1
    assert s["content"] == OUT_OF_SCOPE_REPLY.format(topic="general knowledge questions") and "index" not in s["details"]


def test_streamed_technical_question_routes_then_streams(rig):
    c = rig()
    s, ev = ask(c, new_session(c), WEBHOOK_Q, streamed=True)
    stages = [d["stage"] for e, d, _ in ev if e == "status"]
    assert stages[:3] == ["routing", "accepted", "retrieving"] and ev[-1][0] == "final"
    first_delta = [e for e, _, _ in ev].index("delta")
    assert first_delta > [e for e, _, _ in ev].index("status") + 1     # no answer text before routing completed
    assert route_of(s)["source"] == "classifier" and s["details"]["index"]
