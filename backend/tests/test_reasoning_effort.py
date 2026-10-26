"""OPENAI_REASONING_EFFORT (Settings.openai_reasoning_effort): the answer call's reasoning effort. Unset keeps the request
exactly as before (no parameter); "low" is sent on streamed, non-streamed and streaming-fallback calls alike; the routing
classifier keeps ROUTER_REASONING_EFFORT; invalid values stop start-up with a clear message. No network, fake clients."""
import httpx
import openai
import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from backend.app.core.config import ANSWER_REASONING_EFFORTS, Settings, get_settings
from backend.app.main import create_app
from backend.app.services import assistant_service
from backend.app.services.assistant_service import AssistantService, get_assistant_service, make_budgeted_generator
from backend.app.services.router import IntentClassifier
from backend.app.services.session_guard import SessionGuard, get_session_guard
from backend.app.services.timing import StageClock, TimedGenerator, TimedRetriever
from backend.tests.test_router import FakeClassifierClient
from backend.tests.test_streaming import CHUNK, FakeClient, FakeStream, StubRetriever, model_json, pieces, stream
from pismo_assistant.evidence import OperationIndex
from pismo_assistant.generation import OpenAIGenerator
from pismo_assistant.pipeline import Assistant

Q = "What does WEAM0029 mean?"


def settings_with(**env):
    return Settings(_env_file=None, **env)


# ---------------- configuration ----------------

def test_unset_and_empty_mean_model_default():
    assert settings_with().openai_reasoning_effort is None
    assert settings_with(OPENAI_REASONING_EFFORT="").openai_reasoning_effort is None
    assert settings_with(OPENAI_REASONING_EFFORT="  ").openai_reasoning_effort is None


@pytest.mark.parametrize("raw,value", [("low", "low"), (" LOW ", "low"), ("minimal", "minimal")])
def test_accepted_values(raw, value):
    assert settings_with(OPENAI_REASONING_EFFORT=raw).openai_reasoning_effort == value


@pytest.mark.parametrize("raw", ["medium", "high", "none", "fast", "lowest"])
def test_invalid_values_fail_clearly(raw):
    with pytest.raises(ValidationError) as e:
        settings_with(OPENAI_REASONING_EFFORT=raw)
    msg = str(e.value)
    assert "OPENAI_REASONING_EFFORT must be one of minimal, low" in msg and repr(raw.strip().lower()) in msg


def test_accepted_values_exist_in_the_installed_sdk():
    from typing import get_args
    from openai.types.shared.reasoning_effort import ReasoningEffort
    sdk = {a for t in get_args(ReasoningEffort) for a in (get_args(t) or (t,)) if isinstance(a, str)}
    assert set(ANSWER_REASONING_EFFORTS) <= sdk


# ---------------- the answer request ----------------

def test_generator_omits_the_parameter_by_default_and_sends_low_when_set():
    for effort, expected in ((None, None), ("low", "low")):
        fake = FakeClient(full=model_json())
        OpenAIGenerator(client=fake, reasoning_effort=effort).generate(Q, [])
        kw = fake.calls[-1]
        assert kw.get("reasoning_effort") == expected and ("reasoning_effort" in kw) == (expected is not None)
        assert kw["model"] == "gpt-5-mini" and kw["response_format"] == {"type": "json_object"}   # nothing else changes


def build(client, effort):
    clock = StageClock()
    pipeline = Assistant(retriever=TimedRetriever(StubRetriever(), clock),
                         generator=TimedGenerator(make_budgeted_generator(40.0, 1, clock=clock, client=client,
                                                                          reasoning_effort=effort), clock),
                         op_index=OperationIndex([CHUNK]))
    return AssistantService(pipeline=pipeline, timeout_s=5.0, clock=clock)


@pytest.fixture
def app_with(engine, settings):
    clients = []

    def make(client, effort):
        app = create_app()
        svc, guard = build(client, effort), SessionGuard()
        app.dependency_overrides.update({get_assistant_service: lambda: svc, get_settings: lambda: settings,
                                         get_session_guard: lambda: guard})
        c = TestClient(app).__enter__()
        clients.append(c)
        return c

    yield make
    for c in clients:
        c.__exit__(None, None, None)


@pytest.mark.parametrize("effort", [None, "low"])
def test_streamed_and_non_streamed_calls_send_the_same_options(app_with, effort):
    fake = FakeClient(stream=FakeStream(pieces(model_json())), full=model_json())
    c = app_with(fake, effort)
    sid = c.post("/api/sessions").json()["id"]
    assert c.post(f"/api/sessions/{sid}/messages", json={"content": Q}).status_code == 201
    r, ev = stream(c, sid, Q)
    assert r.status_code == 200 and ev[-1][0] == "final"
    plain, streamed = fake.calls
    assert "stream" not in plain and streamed["stream"] is True
    for kw in (plain, streamed):
        assert kw.get("reasoning_effort") == effort and ("reasoning_effort" in kw) == (effort is not None)
        assert kw["model"] == "gpt-5-mini" and kw["response_format"] == {"type": "json_object"}
    assert plain["messages"] == streamed["messages"]                              # same prompt and evidence


def test_streaming_fallback_keeps_the_setting(app_with):
    refused = openai.BadRequestError("stream not allowed", response=httpx.Response(400, request=httpx.Request("POST", "http://x")),
                                     body=None)
    fake = FakeClient(full=model_json(), create_error=refused)
    c = app_with(fake, "low")
    sid = c.post("/api/sessions").json()["id"]
    r, ev = stream(c, sid, Q)
    assert ev[-1][0] == "final"
    assert [k.get("stream", False) for k in fake.calls] == [True, False]        # refused stream, then the plain call
    assert all(k.get("reasoning_effort") == "low" for k in fake.calls)


def test_the_service_dependency_reads_the_setting(monkeypatch):
    monkeypatch.setattr(assistant_service, "_service", None)
    monkeypatch.setattr("backend.app.core.config.get_settings", lambda: settings_with(OPENAI_REASONING_EFFORT="low"))
    assert get_assistant_service().llm_reasoning_effort == "low"
    monkeypatch.setattr(assistant_service, "_service", None)
    monkeypatch.setattr("backend.app.core.config.get_settings", lambda: settings_with())
    assert get_assistant_service().llm_reasoning_effort is None


# ---------------- the routing classifier is unaffected ----------------

def test_classifier_keeps_its_own_reasoning_effort():
    s = settings_with(OPENAI_REASONING_EFFORT="low")
    assert s.router_reasoning_effort == "minimal"
    fake = FakeClassifierClient()
    clf = IntentClassifier(s.router_model_name, s.router_timeout_s, s.router_reasoning_effort, client=fake)
    clf.classify("How do I create a transfer?", [])
    assert fake.calls[-1]["reasoning_effort"] == "minimal"
