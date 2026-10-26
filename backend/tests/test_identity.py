"""Identity, capabilities and greetings are application facts with fixed, approved replies: never retrieval, never the
answer model, never the classifier. A greeting in front of a real question never causes the question to be dropped.
Counting doubles as in test_router.py; no network, no live model."""
import pytest
from fastapi.testclient import TestClient

from backend.app.core.config import get_settings
from backend.app.main import create_app
from backend.app.services.assistant_service import get_assistant_service
from backend.app.services.conversation import (CAPABILITIES_REPLY, CLARIFY_REPLY, GREETING_REPLY, IDENTITY_REPLY,
                                               SOCIAL_REPLY, THANKS_REPLY, core_message, route)
from backend.app.services.router import IntentClassifier, Router, get_router
from backend.app.services.session_guard import SessionGuard, get_session_guard
from backend.tests.test_router import FakeClassifierClient
from backend.tests.test_streaming import FakeClient, FakeStream, build_service, model_json, parse_sse, pieces

FIXED = [  # message, route outcome, reason, reply
    ("hi", "greeting", "greeting", GREETING_REPLY),
    ("hi who are you", "social", "identity", IDENTITY_REPLY),
    ("Who are you?", "social", "identity", IDENTITY_REPLY),
    ("hey, are you a bot?", "social", "identity", IDENTITY_REPLY),
    ("What can you help me with?", "social", "capabilities", CAPABILITIES_REPLY),
    ("Good morning, what can you do for me?", "social", "capabilities", CAPABILITIES_REPLY),
    ("Thanks", "greeting", "thanks", THANKS_REPLY),
    ("how are you?", "social", "social", SOCIAL_REPLY),
]


@pytest.fixture
def rig(engine, settings):
    clients = []

    def make():
        cls = FakeClassifierClient()
        fake = FakeClient(stream=FakeStream(pieces(model_json())), full=model_json())
        app = create_app()
        svc, guard = build_service(fake), SessionGuard()
        router = Router(IntentClassifier("gpt-5-mini", 1.0, "minimal", client=cls), 1.0)
        app.dependency_overrides.update({get_assistant_service: lambda: svc, get_settings: lambda: settings,
                                         get_session_guard: lambda: guard, get_router: lambda: router})
        c = TestClient(app).__enter__()
        c.cls, c.answer_model, c.retriever = cls, fake, svc._pipeline.retriever._inner
        clients.append(c)
        return c

    yield make
    for c in clients:
        c.__exit__(None, None, None)


def post(c, text, streamed):
    sid = c.post("/api/sessions").json()["id"]
    if streamed:
        ev = parse_sse(c.post(f"/api/sessions/{sid}/messages/stream", json={"content": text}).text)
        return ev[-1][1]["exchange"], ev
    return c.post(f"/api/sessions/{sid}/messages", json={"content": text}).json(), None


@pytest.mark.parametrize("streamed", [False, True])
@pytest.mark.parametrize("text,outcome,reason,reply", FIXED)
def test_fixed_replies_never_search_or_generate(rig, text, outcome, reason, reply, streamed):
    c = rig()
    ex, ev = post(c, text, streamed)
    a = ex["assistant_message"]
    assert a["content"] == reply and a["status"] == "answered" and a["citations"] == []
    assert a["details"]["route"] == {"outcome": outcome, "reason": reason, "source": "rule"}
    assert "index" not in a["details"] and a["details"]["model"] is None and a["details"]["timings"]["total_ms"] > 0
    assert c.retriever.calls == 0 and c.answer_model.calls == [] and c.cls.calls == []
    assert ex["user_message"]["content"] == text                                    # stored exactly as typed
    if streamed:
        assert [e for e, _, _ in ev] == ["status", "status", "final"]               # accepted, saving, final: no drafts


def test_identity_reply_states_only_what_the_app_does():
    assert IDENTITY_REPLY.startswith("I'm Pismo Assist") and "approved developer documentation" in IDENTITY_REPLY
    for claim in ("guarantee", "100%", "always correct", "real-time", "access your account"):
        assert claim not in IDENTITY_REPLY.lower() and claim not in CAPABILITIES_REPLY.lower()


@pytest.mark.parametrize("text,sent", [
    ("Hi, how do I configure a webhook?", "how do I configure a webhook?"),
    ("hello WEAM0029", "WEAM0029"),
    ("Hey there, what does the x-CID header mean?", "what does the x-CID header mean?"),
])
def test_greeting_plus_question_keeps_the_question(rig, text, sent):
    c = rig()
    ex, _ = post(c, text, False)
    a = ex["assistant_message"]
    assert a["details"]["route"]["outcome"] == "pismo_question" and c.retriever.calls == 1
    assert a["details"]["context"]["pipeline_question"] == sent and ex["user_message"]["content"] == text
    assert c.retriever.calls == 1 and len(c.answer_model.calls) == 1


def test_brief_routing_table():
    """The cases in the brief, decided by the deterministic layer (classifier cases are covered in test_router.py)."""
    assert route("hi", False).outcome == "greeting"
    assert route("hi who are you", False).reason == "identity"
    assert route("What does WEAM0029 mean?", False).reason == "own_identifier"
    assert route("Explain more", has_topic=False).outcome == "clarification"
    assert route("Can you explain the JWT part?", has_topic=True).use_context is True
    for text in ("Who is the president of India?", "How does webhook authentication work?"):
        assert route(text, False).reason == "standalone"                         # left to the classifier
    assert core_message("hi-res card images?") == "hi-res card images?"           # not a greeting prefix
    assert core_message("highlight the fields") == "highlight the fields"


def test_explain_more_after_hello_asks_what_to_explain(rig):
    c = rig()
    sid = c.post("/api/sessions").json()["id"]
    c.post(f"/api/sessions/{sid}/messages", json={"content": "hello"})
    a = c.post(f"/api/sessions/{sid}/messages", json={"content": "Explain more"}).json()["assistant_message"]
    assert a["content"] == CLARIFY_REPLY and c.retriever.calls == 0 and c.cls.calls == []
