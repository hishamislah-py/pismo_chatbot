"""Streaming endpoint (SSE). Uses the REAL pismo_assistant Assistant, the backend's streaming generator, the pipeline's
parse_output and citation validation, with a fake OpenAI client whose stream can be gated, broken or refused.
No index, network or LLM. Gates (threading.Event) make the concurrency cases deterministic; WAIT is only a safety net."""
import asyncio
import json
import os
import threading
import uuid
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import func, select

from backend.app.core.config import get_settings
from backend.app.db import session as db_session
from backend.app.main import create_app
from backend.app.models import Message
from backend.app.repositories import store
from backend.app.services.assistant_service import AssistantService, get_assistant_service, make_budgeted_generator
from backend.app.services.conversation import CLARIFY_REPLY, GREETING_REPLY, stream_exchange
from backend.app.services.session_guard import SessionGuard, get_session_guard
from backend.app.services.streaming import AnswerDeltas, partial_answer
from backend.app.services.timing import StageClock, TimedGenerator, TimedRetriever

# pismo_assistant.config loads the project .env into os.environ on import; undo that (see test_timing.py).
_ENV_BEFORE = dict(os.environ)
from pismo_assistant.evidence import OperationIndex  # noqa: E402
from pismo_assistant.pipeline import Assistant  # noqa: E402
from pismo_assistant.retrieval import Hit  # noqa: E402
os.environ.clear()
os.environ.update(_ENV_BEFORE)

WAIT = 10
HASH = "stream-index-hash"
CHUNK = {"chunk_id": "KU-EVT-verifying-webhook-requests::p01", "ku_id": "KU-EVT-verifying-webhook-requests",
         "ku_title": "Verifying webhook requests", "section_heading": "JWT", "heading_path": ["Verifying", "JWT"],
         "ku_type": "workflow_guide", "flags": [], "text": "Each webhook request carries a JWT signed by Pismo.",
         "source_refs": [{"path": "guides/webhooks.md", "url": "https://example.com/webhooks"}]}
ANSWER = "Each webhook request carries a JWT signed by Pismo [E1].\n\nVerify it before use — “trust” nothing [E1]."


def model_json(answer=ANSWER, citations=("E1",), status="answered"):
    # ensure_ascii: the dash and quotes arrive as \uXXXX escapes, which the chunking below splits mid-escape
    return json.dumps({"status": status, "answer": answer, "citations": list(citations), "missing_information": ""})


def pieces(text, size=7):
    return [text[i:i + size] for i in range(0, len(text), size)]


class FakeStream:
    def __init__(self, parts, gate_at=None, fail_at=None):
        self.parts, self.gate_at, self.fail_at = parts, gate_at, fail_at
        self.gate, self.at_gate, self.closed, self.served = threading.Event(), threading.Event(), threading.Event(), 0

    def __iter__(self):
        for i, p in enumerate(self.parts):
            if i == self.gate_at:
                self.at_gate.set()
                assert self.gate.wait(WAIT), "test never opened the gate"
            if i == self.fail_at:
                raise ConnectionError("stream dropped")
            self.served += 1
            yield SimpleNamespace(choices=[SimpleNamespace(delta=SimpleNamespace(content=p))])

    def close(self):
        self.closed.set()


class FakeClient:
    def __init__(self, stream=None, full=None, create_error=None):
        self.stream, self.full, self.create_error, self.calls = stream, full, create_error, []
        self.chat = SimpleNamespace(completions=SimpleNamespace(create=self._create))

    def _create(self, **kw):
        self.calls.append(kw)
        if kw.get("stream"):
            if self.create_error:
                raise self.create_error
            return self.stream
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=self.full))])


class StubRetriever:
    def __init__(self):
        self.chunks, self.chunk_set_hash, self.calls = [CHUNK], HASH, 0

    def search(self, question, k=6):
        self.calls += 1
        return [Hit(CHUNK, 1, "retrieved", "hybrid rank")]


def build_service(client, timeout_s=5.0):
    clock = StageClock()
    pipeline = Assistant(retriever=TimedRetriever(StubRetriever(), clock),
                         generator=TimedGenerator(make_budgeted_generator(40.0, 1, clock=clock, client=client), clock),
                         op_index=OperationIndex([CHUNK]))
    return AssistantService(pipeline=pipeline, timeout_s=timeout_s, clock=clock)


@pytest.fixture
def rig(engine, settings):
    clients = []

    def make(client, timeout_s=5.0):
        app = create_app()
        svc, guard = build_service(client, timeout_s), SessionGuard()
        app.dependency_overrides.update({get_assistant_service: lambda: svc, get_settings: lambda: settings,
                                         get_session_guard: lambda: guard})
        c = TestClient(app).__enter__()          # one event loop, like uvicorn (see test_lifecycle.py)
        c.svc, c.guard, c.fake = svc, guard, client
        clients.append(c)
        return c

    yield make
    for c in clients:
        c.__exit__(None, None, None)


def parse_sse(text):
    events = []
    for block in text.split("\n\n"):
        lines = [ln for ln in block.split("\n") if ln and not ln.startswith(":")]
        if not lines:
            continue
        fields = dict(ln.split(": ", 1) for ln in lines)
        events.append((fields["event"], json.loads(fields["data"]), int(fields["id"])))
    return events


def stream(c, sid, text):
    r = c.post(f"/api/sessions/{sid}/messages/stream", json={"content": text})
    return r, (parse_sse(r.text) if r.headers.get("content-type", "").startswith("text/event-stream") else None)


def new_session(c):
    return c.post("/api/sessions").json()["id"]


def stages(events):
    return [d["stage"] for e, d, _ in events if e == "status"]


def stored(engine, sid):
    with engine.connect() as conn:
        return conn.execute(select(Message.role, Message.status, Message.content)
                            .where(Message.session_id == uuid.UUID(sid)).order_by(Message.seq)).all()


# ---- incremental answer extraction -----------------------------------------------------------------------------------

def test_partial_answer_handles_escapes_key_order_and_decoys():
    full = model_json()
    assert partial_answer(full) == ANSWER
    for cut in range(len(full)):                                  # every prefix decodes to a prefix of the answer
        p = partial_answer(full[:cut])
        assert p is None or ANSWER.startswith(p)
    assert partial_answer('{"status": "answered", "answer": "Hel') == "Hel"
    assert partial_answer('{"answer": "a\\u20') == "a"                         # incomplete \u escape held back
    assert partial_answer('{"answer": "x\\ud83d\\ude00y"}') == "x\U0001F600y"   # surrogate pair
    assert partial_answer('{"missing_information": "the answer is", "nested": {"answer": "no"}}') is None
    assert partial_answer('{"citations": ["answer"], "answer": "yes"}') == "yes"
    assert partial_answer('{"status": "answered"') is None and partial_answer("") is None


def test_answer_deltas_append_in_order():
    d = AnswerDeltas()
    out = [d.feed(p) for p in pieces(model_json(), 3)]
    assert "".join(out) == ANSWER and d.raw == model_json()


# ---- successful stream ------------------------------------------------------------------------------------------------

def test_events_arrive_in_order_and_final_is_the_validated_answer(rig, engine):
    c = rig(FakeClient(stream=FakeStream(pieces(model_json()))))
    sid = new_session(c)
    r, ev = stream(c, sid, "How do I verify webhook requests?")
    assert r.status_code == 200 and r.headers["cache-control"] == "no-cache"
    kinds = [e for e, _, _ in ev]
    assert stages(ev) == ["accepted", "retrieving", "evidence_ready", "generating", "validating", "saving"]
    first_delta, last_delta = kinds.index("delta"), len(kinds) - 1 - kinds[::-1].index("delta")
    assert kinds.index("status") == 0 and first_delta > stages(ev).index("generating")
    assert kinds[last_delta + 1:] == ["status", "validation", "status", "final"]
    assert "".join(d["text"] for e, d, _ in ev if e == "delta") == ANSWER            # provisional text, in order
    assert len({d["request_id"] for _, d, _ in ev}) == 1 and [i for _, _, i in ev] == list(range(1, len(ev) + 1))
    accepted = ev[0][1]
    assert accepted["user_message"]["content"] == "How do I verify webhook requests?"
    assert accepted["route"] == {"outcome": "pismo_question", "reason": "standalone", "source": "rule"}
    assert [d for e, d, _ in ev if e == "status" and d["stage"] == "evidence_ready"][0]["evidence_count"] == 1
    final = ev[-1][1]
    a = final["exchange"]["assistant_message"]
    assert final["http_status"] == 201 and a["content"] == ANSWER and a["status"] == "answered"
    assert [x["label"] for x in a["citations"]] == ["E1"] and a["details"]["index"] == {"chunk_set_hash": HASH}
    assert a["details"]["timings"]["total_ms"] > 0 and a["details"]["timings"]["llm_ms"] is not None
    assert c.fake.calls[0]["stream"] is True and c.fake.calls[0]["response_format"] == {"type": "json_object"}
    assert stored(engine, sid) == [("user", None, "How do I verify webhook requests?"), ("assistant", "answered", ANSWER)]
    assert not c.guard.is_busy(uuid.UUID(sid))


def test_validation_runs_and_can_change_the_answer_metadata(rig):
    bad = "Each webhook request carries a JWT signed by Pismo [E1]. See also [E9]."
    c = rig(FakeClient(stream=FakeStream(pieces(model_json(bad, ("E1", "E9"))))))
    _, ev = stream(c, new_session(c), "How do I verify webhook requests?")
    v = [d for e, d, _ in ev if e == "validation"][0]
    assert v["citations_valid"] is False and v["warning_count"] >= 1 and v["citation_count"] == 1
    a = ev[-1][1]["exchange"]["assistant_message"]
    assert [x["label"] for x in a["citations"]] == ["E1"]                            # unsupplied E9 dropped
    assert any("not supplied" in w for w in a["details"]["warnings"])


def test_markers_are_kept_and_validated_on_both_paths(rig):
    """The [E#] markers tie claims to evidence; the API keeps them (the UI renders them as numbered sources) and
    validation drops a label that was never supplied, on the regular and the streaming endpoint alike."""
    bad = "WEAM0029 was removed; supported by default [E1][E9]."
    for streamed in (False, True):
        c = rig(FakeClient(stream=FakeStream(pieces(model_json(bad, ("E1", "E9")))), full=model_json(bad, ("E1", "E9"))))
        sid = new_session(c)
        if streamed:
            a = stream(c, sid, "What does WEAM0029 mean?")[1][-1][1]["exchange"]["assistant_message"]
        else:
            a = c.post(f"/api/sessions/{sid}/messages", json={"content": "What does WEAM0029 mean?"}).json()["assistant_message"]
        assert a["content"] == bad                                                   # markers preserved, nothing stripped
        assert [x["label"] for x in a["citations"]] == ["E1"]
        assert any("not supplied" in w for w in a["details"]["warnings"]), streamed


def test_regular_endpoint_is_unchanged_and_not_streamed(rig, engine):
    c = rig(FakeClient(full=model_json()))
    sid = new_session(c)
    r = c.post(f"/api/sessions/{sid}/messages", json={"content": "How do I verify webhook requests?"})
    assert r.status_code == 201 and r.json()["assistant_message"]["content"] == ANSWER
    assert "stream" not in c.fake.calls[0]


def test_streaming_refused_falls_back_to_the_regular_request(rig):
    import httpx
    import openai
    refused = openai.BadRequestError("streaming not allowed", response=httpx.Response(400, request=httpx.Request(
        "POST", "https://api.invalid/v1/chat/completions")), body=None)
    c = rig(FakeClient(full=model_json(), create_error=refused))
    _, ev = stream(c, new_session(c), "How do I verify webhook requests?")
    assert ev[-1][0] == "final" and ev[-1][1]["exchange"]["assistant_message"]["content"] == ANSWER
    assert [e for e, _, _ in ev].count("delta") == 0
    assert [k.get("stream") for k in c.fake.calls] == [True, None]


@pytest.mark.parametrize("text,route,reply", [("hi", "greeting", GREETING_REPLY), ("yes explain more", "clarification", CLARIFY_REPLY)])
def test_direct_routes_stream_without_retrieval_or_model(rig, text, route, reply):
    c = rig(FakeClient(stream=FakeStream(pieces(model_json()))))
    _, ev = stream(c, new_session(c), text)
    assert stages(ev) == ["accepted", "saving"] and [e for e, _, _ in ev] == ["status", "status", "final"]
    a = ev[-1][1]["exchange"]["assistant_message"]
    assert a["content"] == reply and a["details"]["response_kind"] == route and "index" not in a["details"]
    assert c.fake.calls == [] and c.svc._pipeline.retriever._inner.calls == 0


# ---- failures: nothing provisional is ever stored -----------------------------------------------------------------------

@pytest.mark.parametrize("parts,code", [
    (['{"status": "answered", "answer": "Partial te', 'xt that never ends'], "malformed_output"),   # truncated JSON
    ([], "malformed_output"),                                                                         # empty output
    (['not json at all'], "malformed_output"),
])
def test_malformed_or_empty_output_is_an_error_not_an_answer(rig, engine, parts, code):
    c = rig(FakeClient(stream=FakeStream(parts)))
    sid = new_session(c)
    _, ev = stream(c, sid, "How do I verify webhook requests?")
    assert ev[-1][0] == "error" and ev[-1][1]["code"] == code and ev[-1][1]["http_status"] == 502
    assert "final" not in [e for e, _, _ in ev] and "validation" not in [e for e, _, _ in ev]
    a = ev[-1][1]["exchange"]["assistant_message"]
    assert a["status"] == "error" and a["content"] == ""
    assert all("Partial" not in row.content for row in stored(engine, sid))        # provisional text never stored
    assert ev[-1][1]["message"] == "The language model returned output that could not be used."


def test_model_error_at_start_and_mid_stream(rig, engine):
    c = rig(FakeClient(create_error=RuntimeError("provider unavailable: secret-ish detail")))
    _, ev = stream(c, new_session(c), "How do I verify webhook requests?")
    assert ev[-1][0] == "error" and ev[-1][1]["code"] == "api_error" and "secret-ish" not in ev[-1][1]["message"]
    s = FakeStream(pieces(model_json()), fail_at=8)               # breaks ~20 characters into the answer text
    c2 = rig(FakeClient(stream=s))
    sid = new_session(c2)
    _, ev2 = stream(c2, sid, "How do I verify webhook requests?")
    assert [e for e, _, _ in ev2].count("delta") >= 1 and ev2[-1][0] == "error" and ev2[-1][1]["code"] == "api_error"
    assert s.closed.is_set() and stored(engine, sid)[-1][1:] == ("error", "")


def test_timeout_keeps_the_budget_and_stops_the_model_stream(rig, engine):
    s = FakeStream(pieces(model_json()), gate_at=3)
    c = rig(FakeClient(stream=s), timeout_s=0.3)
    sid = new_session(c)
    _, ev = stream(c, sid, "How do I verify webhook requests?")
    err = ev[-1][1]
    assert ev[-1][0] == "error" and err["code"] == "timeout" and err["http_status"] == 504
    details = err["exchange"]["assistant_message"]["details"]["error"]
    assert details["worker_still_running"] is True and "a stop was requested" in details["message"]
    assert not c.guard.is_busy(uuid.UUID(sid))
    s.gate.set()                                                   # the model would continue ...
    assert s.closed.wait(WAIT) and s.served <= 4                   # ... but the stream stops at the next chunk
    assert c.svc._call_lock.acquire(timeout=WAIT)                  # pipeline lock released, not held indefinitely
    c.svc._call_lock.release()
    assert [row[1] for row in stored(engine, sid)] == [None, "error"]


# ---- guard, 409, 404, deletion ------------------------------------------------------------------------------------------

def test_busy_session_is_409_before_the_stream_starts(rig, engine):
    c = rig(FakeClient(stream=FakeStream(pieces(model_json()))))
    sid = new_session(c)
    with c.guard.hold(uuid.UUID(sid)):
        r, ev = stream(c, sid, "How do I verify webhook requests?")
    assert r.status_code == 409 and r.json()["detail"]["code"] == "session_busy" and ev is None
    assert stored(engine, sid) == []


def test_missing_session_and_invalid_body_keep_http_status(rig):
    c = rig(FakeClient())
    r, _ = stream(c, str(uuid.uuid4()), "How do I verify webhook requests?")
    assert r.status_code == 404 and r.json()["detail"]["code"] == "session_not_found"
    assert c.post(f"/api/sessions/{new_session(c)}/messages/stream", json={"content": "   "}).status_code == 422


def test_concurrent_stream_on_same_session_and_deletion_during_generation(rig, engine):
    s = FakeStream(pieces(model_json()), gate_at=3)
    c = rig(FakeClient(stream=s))
    sid = new_session(c)
    out = {}
    t = threading.Thread(target=lambda: out.setdefault("r", stream(c, sid, "How do I verify webhook requests?")))
    t.start()
    assert s.at_gate.wait(WAIT)                                    # generating, guard held
    r2, _ = stream(c, sid, "And the JWT part?")
    assert r2.status_code == 409
    assert c.delete(f"/api/sessions/{sid}").status_code == 204    # deletion is not blocked
    s.gate.set()
    t.join(WAIT)
    ev = out["r"][1]
    assert ev[-1][0] == "error" and ev[-1][1]["code"] == "session_deleted" and "final" not in [e for e, _, _ in ev]
    assert stored(engine, sid) == [] and not c.guard.is_busy(uuid.UUID(sid))


# ---- disconnect / cancellation (stream_exchange driven directly) -------------------------------------------------------

def _drive(engine, settings, svc, guard, sid, text, stop_after, disconnect_flag=None, poll_s=1.0):
    async def run():
        db = db_session._factory()
        events = []
        flag = disconnect_flag or {"gone": False}

        async def is_disconnected():
            return flag["gone"]
        agen = stream_exchange(db, settings, svc, uuid.UUID(sid), text, guard, is_disconnected, poll_s=poll_s)
        try:
            async for event, data in agen:
                events.append((event, data))
                if stop_after(event, data, flag):
                    break
        finally:
            await agen.aclose()                     # what Starlette's cancellation / generator finalisation does
            db.close()
        return events
    return asyncio.run(run())


def test_client_disconnect_mid_answer_stops_generation_and_stores_nothing(engine, settings):
    s = FakeStream(pieces(model_json()), gate_at=6)
    svc, guard = build_service(FakeClient(stream=s)), SessionGuard()
    db = db_session._factory()
    sid = str(store.create_session(db).id)
    db.commit()
    db.close()
    opener = threading.Timer(0.2, s.gate.set)                    # let the worker run on after the client has gone
    opener.start()
    events = _drive(engine, settings, svc, guard, sid, "How do I verify webhook requests?",
                    stop_after=lambda e, d, f: e == "delta")
    opener.join()
    assert events[-1][0] == "delta"                              # the client saw provisional text, then left
    assert not guard.is_busy(uuid.UUID(sid))
    assert s.closed.wait(WAIT) and s.served < len(s.parts)       # model stream stopped early
    assert svc._call_lock.acquire(timeout=WAIT)
    svc._call_lock.release()
    assert stored(engine, sid) == [("user", None, "How do I verify webhook requests?")]   # no answer row at all


def test_disconnect_detected_while_waiting(engine, settings):
    s = FakeStream(pieces(model_json()), gate_at=0)              # model has not produced anything yet
    svc, guard = build_service(FakeClient(stream=s)), SessionGuard()
    db = db_session._factory()
    sid = str(store.create_session(db).id)
    db.commit()
    db.close()

    def stop_after(event, data, flag):
        if event == "status" and data["stage"] == "generating":
            flag["gone"] = True                                  # client disappears while the model is silent
        return False
    opener = threading.Timer(0.5, s.gate.set)
    opener.start()
    events = _drive(engine, settings, svc, guard, sid, "How do I verify webhook requests?", stop_after, poll_s=0.05)
    opener.join()
    assert events[-1][0] == "status" and events[-1][1]["stage"] == "generating"   # ended without final or error
    assert s.closed.wait(WAIT) and not guard.is_busy(uuid.UUID(sid))
    assert [r[0] for r in stored(engine, sid)] == ["user"]


def test_guard_race_inside_the_stream_is_an_error_event(engine, settings):
    svc, guard = build_service(FakeClient()), SessionGuard()
    db = db_session._factory()
    sid = str(store.create_session(db).id)
    db.commit()
    db.close()
    with guard.hold(uuid.UUID(sid)):
        events = _drive(engine, settings, svc, guard, sid, "How do I verify webhook requests?", lambda e, d, f: False)
    assert events == [("error", {"code": "session_busy", "message": events[0][1]["message"], "http_status": 409})]
    with engine.connect() as conn:
        assert conn.execute(select(func.count()).select_from(Message)).scalar() == 0
