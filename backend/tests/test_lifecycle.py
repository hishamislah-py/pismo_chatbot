"""Request lifecycle: short transactions around the pipeline call, one in-flight message per session, honest timeouts.
Deterministic: the blocking pipeline signals when it is inside the call and waits for an explicit release (no sleeps)."""
import threading
import uuid

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import event, func, select

from backend.app.core.config import get_settings
from backend.app.db import session as db_session
from backend.app.db.session import get_db
from backend.app.main import create_app
from backend.app.models import Activity, Message
from backend.app.repositories import store
from backend.app.services.assistant_service import AssistantService, AssistantTimeout, get_assistant_service
from backend.app.services.conversation import GREETING_REPLY
from backend.app.services.session_guard import SessionBusy, SessionGuard, get_session_guard
from backend.tests.conftest import FakePipeline, pipeline_result

WAIT = 10  # seconds; only a safety net against a hung test, never part of the logic


class BlockingPipeline:
    """Signals `entered` once inside answer(), then waits for `release`. Optionally records DB state at that moment."""

    def __init__(self, probe=None):
        self.entered, self.release, self.finished = threading.Event(), threading.Event(), threading.Event()
        self.questions, self.probe, self.observed = [], probe, None

    def answer(self, question):
        self.questions.append(question)
        if self.probe:
            self.observed = self.probe()
        self.entered.set()
        try:
            assert self.release.wait(WAIT), "test never released the pipeline"
            return pipeline_result()
        finally:
            self.finished.set()


@pytest.fixture
def lifecycle(engine, settings):
    """App + client with a fresh guard, a tracked DB session per request and pool checkout counting."""
    state = {"sessions": [], "checked_out": 0, "checkouts": 0}

    @event.listens_for(engine, "checkout")
    def _out(*_):
        state["checked_out"] += 1
        state["checkouts"] += 1

    @event.listens_for(engine, "checkin")
    def _in(*_):
        state["checked_out"] -= 1

    def tracked_db():
        for db in db_session.get_db():
            state["sessions"].append(db)
            yield db

    clients = []

    def make(pipeline, timeout_s=5.0):
        app = create_app()
        guard = SessionGuard()
        svc = AssistantService(pipeline=pipeline, timeout_s=timeout_s)
        app.dependency_overrides.update({get_assistant_service: lambda: svc, get_settings: lambda: settings,
                                         get_session_guard: lambda: guard, get_db: tracked_db})
        # entered once: one event loop for the client's lifetime, like uvicorn. (Without it every request gets its own
        # loop, whose executor shutdown would wait for an abandoned worker thread and hide timeout behaviour.)
        c = TestClient(app).__enter__()
        clients.append(c)
        c.guard, c.state = guard, state
        return c

    yield make
    for c in clients:
        c.__exit__(None, None, None)
    event.remove(engine, "checkout", _out)
    event.remove(engine, "checkin", _in)


def post(c, sid, text):
    return c.post(f"/api/sessions/{sid}/messages", json={"content": text})


def in_background(fn):
    out = {}
    t = threading.Thread(target=lambda: out.setdefault("r", fn()), daemon=True)
    t.start()
    return t, out


def rows(engine, model, sid):
    with engine.connect() as conn:
        return conn.execute(select(func.count()).select_from(model).where(model.session_id == uuid.UUID(sid))).scalar()


# ---- Fix 1: transactions -------------------------------------------------------------------------------------------

def test_no_transaction_or_connection_is_held_while_the_pipeline_runs(lifecycle):
    holder = {}
    pipe = BlockingPipeline(probe=lambda: {"in_txn": [s.in_transaction() for s in holder["c"].state["sessions"]],
                                           "checked_out": holder["c"].state["checked_out"]})
    c = holder["c"] = lifecycle(pipe)
    sid = c.post("/api/sessions").json()["id"]
    pipe.release.set()                                      # setup exchange runs straight through
    assert post(c, sid, "How do I create a transfer?").status_code == 201   # a prior question for the next one to read
    pipe.release.clear()
    pipe.entered.clear()
    t, out = in_background(lambda: post(c, sid, "What about events?"))   # follow-up: the context read happens
    assert pipe.entered.wait(WAIT)
    assert '"How do I create a transfer?"' in pipe.questions[-1]        # context really was read in step 1
    assert pipe.observed == {"in_txn": [False] * len(pipe.observed["in_txn"]), "checked_out": 0}
    assert c.state["checkouts"] > 0                         # the probe is meaningful: connections are being counted
    pipe.release.set()
    t.join(WAIT)
    assert out["r"].status_code == 201
    assert c.state["checked_out"] == 0


def test_user_message_kept_when_generation_fails(lifecycle, engine):
    c = lifecycle(FakePipeline(exc=RuntimeError("boom")))
    sid = c.post("/api/sessions").json()["id"]
    r = post(c, sid, "How do I create a transfer?")
    assert r.status_code == 500
    a = r.json()["assistant_message"]
    assert a["status"] == "error" and a["content"] == "" and a["details"]["error"] == {"kind": "internal", "message": "RuntimeError"}
    msgs = c.get(f"/api/sessions/{sid}/messages").json()["messages"]
    assert [(m["seq"], m["role"]) for m in msgs] == [(1, "user"), (2, "assistant")]
    assert rows(engine, Activity, sid) == 1 and not c.guard.is_busy(uuid.UUID(sid))


def test_successful_answer_and_activity_committed_together(lifecycle, engine):
    c = lifecycle(FakePipeline())
    sid = c.post("/api/sessions").json()["id"]
    ex = post(c, sid, "How do I create a transfer?").json()
    assert (ex["user_message"]["seq"], ex["assistant_message"]["seq"]) == (1, 2)
    assert rows(engine, Message, sid) == 2 and rows(engine, Activity, sid) == 1
    act = c.get("/api/activity").json()["activity"][0]
    assert act["event"] == "message.answer" and act["status"] == "answered" and act["citation_count"] == 1


def test_failure_while_storing_the_answer_rolls_back_and_releases(lifecycle, engine, monkeypatch):
    c = lifecycle(FakePipeline())
    sid = c.post("/api/sessions").json()["id"]

    def broken(*a, **k):
        raise RuntimeError("activity insert failed")
    monkeypatch.setattr(store, "add_activity", broken)
    with pytest.raises(RuntimeError):
        post(c, sid, "How do I create a transfer?")
    # the question (transaction 1) is kept; the half-written answer (transaction 2) was rolled back as a whole
    assert rows(engine, Message, sid) == 1 and rows(engine, Activity, sid) == 0
    assert all(not s.in_transaction() for s in c.state["sessions"]) and c.state["checked_out"] == 0
    assert not c.guard.is_busy(uuid.UUID(sid))
    monkeypatch.undo()
    assert post(c, sid, "How do I create a transfer?").json()["assistant_message"]["seq"] == 3   # session still usable


def test_failure_in_the_first_transaction_stores_nothing(lifecycle, engine, monkeypatch):
    pipe = FakePipeline()
    c = lifecycle(pipe)
    sid = c.post("/api/sessions").json()["id"]
    post(c, sid, "How do I create a transfer?")

    def broken(*a, **k):
        raise RuntimeError("context read failed")
    monkeypatch.setattr(store, "prior_user_questions", broken)
    with pytest.raises(RuntimeError):
        post(c, sid, "What about events?")
    # the follow-up's user message was in the rolled-back transaction: only the first exchange remains
    assert rows(engine, Message, sid) == 2 and len(pipe.questions) == 1        # the pipeline was never reached
    assert c.state["checked_out"] == 0 and not c.guard.is_busy(uuid.UUID(sid))


def test_greeting_still_bypasses_the_pipeline(lifecycle):
    pipe = FakePipeline()
    c = lifecycle(pipe)
    sid = c.post("/api/sessions").json()["id"]
    a = post(c, sid, "hi").json()["assistant_message"]
    assert a["content"] == GREETING_REPLY and pipe.questions == [] and c.state["checked_out"] == 0


# ---- Fix 2: one in-flight message per session -----------------------------------------------------------------------

def test_concurrent_post_to_same_session_gets_409_and_history_stays_ordered(lifecycle, engine):
    pipe = BlockingPipeline()
    c = lifecycle(pipe)
    sid = c.post("/api/sessions").json()["id"]
    t, out = in_background(lambda: post(c, sid, "How do I create a transfer?"))
    assert pipe.entered.wait(WAIT)
    second = post(c, sid, "How do I cancel a transfer?")      # arrives while the first is generating
    assert second.status_code == 409 and second.json()["detail"]["code"] == "session_busy"
    assert rows(engine, Message, sid) == 1                       # the rejected message stored nothing
    pipe.release.set()
    t.join(WAIT)
    assert out["r"].status_code == 201
    third = post(c, sid, "How do I cancel a transfer?")
    assert third.status_code == 201
    msgs = c.get(f"/api/sessions/{sid}/messages").json()["messages"]
    assert [(m["seq"], m["role"], m["content"][:22]) for m in msgs] == [
        (1, "user", "How do I create a trans"[:22]), (2, "assistant", msgs[1]["content"][:22]),
        (3, "user", "How do I cancel a trans"[:22]), (4, "assistant", msgs[3]["content"][:22])]
    assert len({m["seq"] for m in msgs}) == 4
    assert pipe.questions == ["How do I create a transfer?", "How do I cancel a transfer?"]   # no cross-request context


def test_other_sessions_are_not_blocked_by_the_guard(lifecycle):
    pipe = BlockingPipeline()
    c = lifecycle(pipe)
    a = c.post("/api/sessions").json()["id"]
    b = c.post("/api/sessions").json()["id"]
    t_a, out_a = in_background(lambda: post(c, a, "How do I create a transfer?"))
    assert pipe.entered.wait(WAIT)
    assert post(c, b, "hello").status_code == 201               # different session, no pipeline: completes now
    t_b, out_b = in_background(lambda: post(c, b, "What does WEAM0029 mean?"))   # accepted; waits for the pipeline lock
    assert c.guard.is_busy(uuid.UUID(a))
    pipe.release.set()
    t_a.join(WAIT)
    t_b.join(WAIT)
    assert out_a["r"].status_code == 201 and out_b["r"].status_code == 201
    assert pipe.questions == ["How do I create a transfer?", "What does WEAM0029 mean?"]


def test_failed_request_releases_the_guard(lifecycle):
    c = lifecycle(FakePipeline([{"status": "generation_error", "answer": "", "citations": [], "evidence": [],
                                 "error": {"kind": "api_error", "message": "x"}}]))
    sid = c.post("/api/sessions").json()["id"]
    assert post(c, sid, "How do I create a transfer?").status_code == 502
    assert not c.guard.is_busy(uuid.UUID(sid))
    assert post(c, sid, "thanks").status_code == 201


def test_missing_session_is_404_and_leaves_no_guard(lifecycle):
    c = lifecycle(FakePipeline())
    sid = str(uuid.uuid4())
    r = post(c, sid, "How do I create a transfer?")
    assert r.status_code == 404 and r.json()["detail"]["code"] == "session_not_found"
    assert not c.guard.is_busy(uuid.UUID(sid))


def test_session_deleted_while_generating_stores_nothing(lifecycle, engine):
    pipe = BlockingPipeline()
    c = lifecycle(pipe)
    sid = c.post("/api/sessions").json()["id"]
    t, out = in_background(lambda: post(c, sid, "How do I create a transfer?"))
    assert pipe.entered.wait(WAIT)
    assert c.delete(f"/api/sessions/{sid}").status_code == 204   # deletion is not blocked by an in-flight message
    pipe.release.set()
    t.join(WAIT)
    assert out["r"].status_code == 404 and out["r"].json()["detail"]["code"] == "session_not_found"
    assert rows(engine, Message, sid) == 0 and rows(engine, Activity, sid) == 0
    assert not c.guard.is_busy(uuid.UUID(sid))


def test_guard_test_and_set_is_atomic():
    guard, sid, wins, start = SessionGuard(), uuid.uuid4(), [], threading.Barrier(16)

    def contender():
        start.wait()
        try:
            with guard.hold(sid):
                wins.append(1)
                hold.wait(WAIT)
        except SessionBusy:
            pass

    hold = threading.Event()
    threads = [threading.Thread(target=contender) for _ in range(16)]
    for th in threads:
        th.start()
    for _ in range(1000):                 # wait until the winner holds it and every loser has given up
        if sum(th.is_alive() for th in threads) == 1:
            break
        threading.Event().wait(0.005)
    assert len(wins) == 1 and guard.is_busy(sid)
    hold.set()
    for th in threads:
        th.join(WAIT)
    assert not guard.is_busy(sid)


# ---- Fix 3: timeouts --------------------------------------------------------------------------------------------------

def test_timeout_is_reported_honestly_and_releases_the_guard(lifecycle, engine):
    pipe = BlockingPipeline()
    c = lifecycle(pipe, timeout_s=0.3)
    sid = c.post("/api/sessions").json()["id"]
    r = post(c, sid, "How do I create a transfer?")
    assert r.status_code == 504
    err = r.json()["assistant_message"]["details"]["error"]
    assert err["kind"] == "timeout" and err["worker_still_running"] is True
    assert "could not be cancelled and is still running in the background" in err["message"]
    assert "was cancelled" not in err["message"] and "has since finished" not in err["message"]
    assert not pipe.finished.is_set()                          # it really is still running: nothing was cancelled
    assert not c.guard.is_busy(uuid.UUID(sid)) and c.state["checked_out"] == 0
    assert post(c, sid, "thanks").status_code == 201          # the session is usable again right away
    pipe.release.set()
    assert pipe.finished.wait(WAIT)
    msgs = c.get(f"/api/sessions/{sid}/messages").json()["messages"]
    assert [(m["role"], m["status"]) for m in msgs] == [("user", None), ("assistant", "error"), ("user", None),
                                                         ("assistant", "answered")]   # the late result was discarded


def test_timeout_message_when_the_worker_already_finished():
    e = AssistantTimeout(90, still_running=False)
    assert "has since finished" in str(e) and e.still_running is False
    e = AssistantTimeout(90, still_running=True)
    assert "could not be cancelled and is still running" in str(e)
