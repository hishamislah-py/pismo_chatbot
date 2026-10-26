"""Index version: answers and /api/health report the chunk_set_hash of the index actually held in memory, never a
recomputed or invented value. Uses the REAL pismo_assistant Assistant with a stub retriever (no index files, no network)."""
import os
import threading

from backend.app.services.assistant_service import AssistantService, get_assistant_service
from backend.app.services.conversation import GREETING_REPLY
from backend.app.services.timing import StageClock, TimedGenerator, TimedRetriever
from backend.tests.conftest import FakePipeline

# pismo_assistant.config loads the project .env into os.environ on import; undo that (see test_timing.py).
_ENV_BEFORE = dict(os.environ)
from pismo_assistant.evidence import OperationIndex  # noqa: E402
from pismo_assistant.generation import Generated  # noqa: E402
from pismo_assistant.pipeline import Assistant  # noqa: E402
from pismo_assistant.retrieval import Hit  # noqa: E402
os.environ.clear()
os.environ.update(_ENV_BEFORE)

HASH = "8db472c58e43" + "0" * 52          # stand-in for HybridRetriever.chunk_set_hash (sha256 hex)
CHUNK = {"chunk_id": "KU-T::p01", "ku_id": "KU-T", "ku_title": "Transfers guide", "section_heading": "Events",
         "heading_path": ["Transfers guide", "Events"], "ku_type": "workflow_guide", "flags": [],
         "text": "Creating a transfer emits the transfer-created-1 event.",
         "source_refs": [{"path": "guides/transfers.md", "url": "https://example.com/transfers"}]}


class StubRetriever:
    """Has the attributes the pipeline and the backend read from HybridRetriever: chunks, search(), chunk_set_hash."""

    def __init__(self):
        self.chunks, self.chunk_set_hash, self.searches = [CHUNK], HASH, 0

    def search(self, question, k=6):
        self.searches += 1
        return [Hit(CHUNK, 1, "retrieved", "hybrid rank")]


class StubGenerator:
    model = "stub-model"

    def __init__(self):
        self.calls = 0

    def generate(self, question, evidence):
        self.calls += 1
        return Generated("answered", "Creating a transfer emits `transfer-created-1` [E1].", ["E1"], "", "{}", self.model)


def real_service(timeout_s=5.0):
    clock, retriever, generator = StageClock(), StubRetriever(), StubGenerator()
    pipeline = Assistant(retriever=TimedRetriever(retriever, clock), generator=TimedGenerator(generator, clock),
                         op_index=OperationIndex([CHUNK]))
    return AssistantService(pipeline=pipeline, timeout_s=timeout_s, clock=clock), retriever, generator


def client_with(make_client, svc):
    c = make_client()
    c.app.dependency_overrides[get_assistant_service] = lambda: svc
    return c


def ask(c, text):
    sid = c.post("/api/sessions").json()["id"]
    return c.post(f"/api/sessions/{sid}/messages", json={"content": text})


def test_pipeline_answer_records_the_loaded_index(make_client):
    svc, retriever, _ = real_service()
    c = client_with(make_client, svc)
    a = ask(c, "Which event is emitted when I create a transfer?").json()["assistant_message"]
    assert a["details"]["index"] == {"chunk_set_hash": HASH} and retriever.searches == 1
    # existing details unchanged alongside it
    assert a["citations"][0]["label"] == "E1" and a["details"]["timings"]["stages_measured"] is True
    assert a["details"]["citations_valid"] is not None and isinstance(a["details"]["warnings"], list)
    stored = c.get(f"/api/sessions/{a['session_id']}/messages").json()["messages"][1]
    assert stored["details"]["index"] == {"chunk_set_hash": HASH}                       # persisted in the JSON column


def test_index_hash_is_read_not_recomputed(make_client):
    svc, retriever, _ = real_service()
    c = client_with(make_client, svc)
    retriever.chunk_set_hash = "changed-in-memory"          # whatever the loaded object holds is what gets reported
    a = ask(c, "Which event is emitted when I create a transfer?").json()["assistant_message"]
    assert a["details"]["index"]["chunk_set_hash"] == "changed-in-memory"


def test_health_reports_the_loaded_index(make_client):
    svc, _, _ = real_service()
    body = client_with(make_client, svc).get("/api/health").json()
    assert body["assistant"] == "loaded" and body["index"] == {"chunk_set_hash": HASH}
    assert {"status", "app", "database", "assistant"} <= body.keys()


def test_health_before_load_reports_null_and_does_not_load(make_client):
    svc = AssistantService(timeout_s=5.0)                    # nothing injected: real pipeline not loaded yet
    body = client_with(make_client, svc).get("/api/health").json()
    assert body["assistant"] == "not_loaded" and body["index"] == {"chunk_set_hash": None}
    assert svc.loaded is False                               # the health check did not trigger the ~15 s load


def test_health_after_failed_load_reports_null(make_client):
    svc = AssistantService(timeout_s=5.0)
    svc.load_error = "IndexIntegrityError: embeddings were built for a different chunk set"
    body = client_with(make_client, svc).get("/api/health").json()
    assert body["assistant"] == "error" and body["index"] == {"chunk_set_hash": None}


def test_pipeline_without_index_reports_null(client):
    a = ask(client, "How do I create a transfer?").json()["assistant_message"]   # FakePipeline: no retriever
    assert a["details"]["index"] == {"chunk_set_hash": None}


def test_greeting_claims_no_index_and_no_llm(make_client):
    svc, retriever, generator = real_service()
    a = ask(client_with(make_client, svc), "hi").json()["assistant_message"]
    assert a["content"] == GREETING_REPLY and "index" not in a["details"]
    assert a["details"]["model"] is None and "llm_ms" not in a["details"]["timings"]
    assert retriever.searches == 0 and generator.calls == 0


def test_timeout_does_not_claim_an_index(make_client):
    release = threading.Event()

    class Blocking:   # outlives the 0.2 s deadline; short so the per-request test loop is not held up for long
        def answer(self, q):
            release.wait(0.6)
            return {}

    c = client_with(make_client, AssistantService(pipeline=Blocking(), timeout_s=0.2))
    try:
        r = ask(c, "How do I create a transfer?")
        assert r.status_code == 504 and "index" not in r.json()["assistant_message"]["details"]
    finally:
        release.set()


def test_generation_error_still_records_index(make_client):
    c = client_with(make_client, AssistantService(pipeline=FakePipeline([{
        "status": "generation_error", "answer": "", "citations": [], "evidence": [],
        "error": {"kind": "api_error", "message": "x"}}])))
    a = ask(c, "How do I create a transfer?").json()["assistant_message"]
    assert a["status"] == "error" and a["details"]["index"] == {"chunk_set_hash": None}   # pipeline returned; no retriever
