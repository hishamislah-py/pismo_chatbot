"""Per-stage timing: the REAL pismo_assistant Assistant, built with stub retriever/generator wrapped in the backend's
timing proxies, exactly as AssistantService builds the production pipeline. No index, model or network is used."""
import os
import time

import pytest

from backend.app.services.assistant_service import AssistantService
from backend.app.services.timing import StageClock, TimedGenerator, TimedRetriever

# pismo_assistant.config loads the project .env into os.environ on import. Undo that immediately so the rest of the test
# process (conftest's SQLite pin, test_config) never sees real settings or keys.
_ENV_BEFORE = dict(os.environ)
from pismo_assistant.evidence import OperationIndex  # noqa: E402
from pismo_assistant.generation import GenerationError, Generated  # noqa: E402
from pismo_assistant.pipeline import Assistant  # noqa: E402
from pismo_assistant.retrieval import Hit  # noqa: E402
os.environ.clear()
os.environ.update(_ENV_BEFORE)

CHUNK = {"chunk_id": "KU-T::p01", "ku_id": "KU-T", "ku_title": "Transfers guide", "section_heading": "Events",
         "heading_path": ["Transfers guide", "Events"], "ku_type": "workflow_guide", "flags": [],
         "text": "Creating a transfer emits the transfer-created-1 event.",
         "source_refs": [{"path": "guides/transfers.md", "url": "https://example.com/transfers"}]}


class StubRetriever:
    def __init__(self, hits=True, delay=0.03):
        self.chunks, self.hits, self.delay, self.calls = [CHUNK], hits, delay, 0

    def search(self, question, k=6):
        self.calls += 1
        time.sleep(self.delay)
        return [Hit(CHUNK, 1, "retrieved", "hybrid rank")] if self.hits else []


class StubGenerator:
    def __init__(self, delay=0.06, fail=False):
        self.delay, self.fail, self.calls, self.model = delay, fail, 0, "stub-model"

    def generate(self, question, evidence):
        self.calls += 1
        time.sleep(self.delay)
        if self.fail:
            raise GenerationError("api_error", "boom")
        return Generated("answered", "Creating a transfer emits `transfer-created-1` [E1].", ["E1"], "", "{}", self.model)


def build(retriever, generator, timeout_s=5.0):
    clock = StageClock()
    pipeline = Assistant(retriever=TimedRetriever(retriever, clock), generator=TimedGenerator(generator, clock),
                         op_index=OperationIndex([CHUNK]))
    return AssistantService(pipeline=pipeline, timeout_s=timeout_s, clock=clock)


def ask(c, q):
    s = c.post("/api/sessions").json()["id"]
    r = c.post(f"/api/sessions/{s}/messages", json={"content": q})
    return r


@pytest.fixture
def svc_client(make_client):
    def _make(retriever, generator):
        c = make_client()
        from backend.app.services.assistant_service import get_assistant_service
        svc = build(retriever, generator)
        c.app.dependency_overrides[get_assistant_service] = lambda: svc
        return c
    return _make


def test_proxies_are_transparent():
    r, clock = StubRetriever(), StageClock()
    t = TimedRetriever(r, clock)
    assert t.chunks is r.chunks and t.delay == r.delay           # other attributes forwarded
    assert t.search("q")[0].chunk is CHUNK and clock.search is not None
    g = TimedGenerator(StubGenerator(fail=True), clock)
    with pytest.raises(GenerationError):                          # exceptions unchanged, timing still recorded
        g.generate("q", [])
    assert clock.generate is not None and g.model == "stub-model"


def test_all_stages_measured_for_a_real_pipeline_answer(svc_client):
    retriever, generator = StubRetriever(delay=0.03), StubGenerator(delay=0.06)
    r = ask(svc_client(retriever, generator), "Which event is emitted when I create a transfer?")
    assert r.status_code == 201, r.text
    a = r.json()["assistant_message"]
    assert a["status"] == "answered" and a["citations"][0]["label"] == "E1"   # pipeline behaviour unchanged by proxies
    t = a["details"]["timings"]
    assert t["stages_measured"] is True and retriever.calls == 1 and generator.calls == 1
    assert t["retrieval_ms"] >= 25 and t["llm_ms"] >= 55
    for k in ("evidence_and_operations_ms", "post_generation_ms", "lock_wait_ms", "load_wait_ms", "db_question_ms",
              "db_context_ms", "db_answer_ms"):
        assert t[k] is not None and t[k] >= 0, k
    stages = t["retrieval_ms"] + t["evidence_and_operations_ms"] + t["llm_ms"] + t["post_generation_ms"]
    assert abs(stages - t["pipeline_ms"]) < 2                    # the stages partition the pipeline call
    assert t["pipeline_call_ms"] >= t["pipeline_ms"] and t["total_ms"] >= t["pipeline_call_ms"]
    assert abs(a["details"]["duration_ms"] - t["pipeline_call_ms"]) <= 1   # existing field keeps its meaning (int ms)


def test_no_evidence_has_no_llm_stage(svc_client):
    generator = StubGenerator()
    a = ask(svc_client(StubRetriever(hits=False), generator), "zzz qqq").json()["assistant_message"]
    t = a["details"]["timings"]
    assert a["status"] == "no_evidence" and generator.calls == 0
    assert t["llm_ms"] is None and t["post_generation_ms"] is None and t["retrieval_ms"] >= 25


def test_generation_error_keeps_timings(svc_client):
    r = ask(svc_client(StubRetriever(), StubGenerator(fail=True)), "Which event is emitted when I create a transfer?")
    assert r.status_code == 502
    t = r.json()["assistant_message"]["details"]["timings"]
    assert t["llm_ms"] >= 55 and t["retrieval_ms"] >= 25


def test_greeting_never_touches_retriever_or_generator(svc_client):
    retriever, generator = StubRetriever(), StubGenerator()
    r = ask(svc_client(retriever, generator), "Good morning!")
    assert r.status_code == 201 and retriever.calls == 0 and generator.calls == 0
    assert r.json()["assistant_message"]["details"]["response_kind"] == "greeting"


def test_injected_pipeline_without_clock_reports_no_stages(client):
    a = ask(client, "How do I create a transfer?").json()["assistant_message"]
    t = a["details"]["timings"]
    assert t["stages_measured"] is False and "retrieval_ms" not in t and t["lock_wait_ms"] >= 0
