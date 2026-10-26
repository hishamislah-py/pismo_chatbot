"""Session-scoped follow-up context: same session only, prior USER questions only, bounded."""
from backend.app.core.config import Settings
from backend.app.services.conversation import build_pipeline_question, is_follow_up


def ask(c, sid, q):
    r = c.post(f"/api/sessions/{sid}/messages", json={"content": q})
    assert r.status_code == 201, r.text
    return r.json()


def test_follow_up_gets_prior_question_from_same_session(client):
    s = client.post("/api/sessions").json()["id"]
    first = ask(client, s, "How do I create a transfer?")
    ex = ask(client, s, "What about the required fields?")
    sent = client.pipeline.questions[-1]
    assert sent.startswith("What about the required fields?")
    assert '"How do I create a transfer?"' in sent
    ctx = ex["assistant_message"]["details"]["context"]
    assert ctx["used"] is True and ctx["prior_message_ids"] == [first["user_message"]["id"]]
    assert ex["user_message"]["content"] == "What about the required fields?"   # stored question is the user's own text


def test_context_never_crosses_sessions(client):
    a = client.post("/api/sessions").json()["id"]
    b = client.post("/api/sessions").json()["id"]
    ask(client, a, "How do I create a transfer?")
    ask(client, b, "What about the required fields?")
    assert client.pipeline.questions[-1] == "What about the required fields?"   # no context: session b has no history


def test_prior_assistant_answers_are_never_passed(make_client):
    from backend.tests.conftest import FakePipeline, pipeline_result
    c = make_client(FakePipeline([pipeline_result(answer="SECRET-ANSWER-TEXT the endpoint is X [E1]."), pipeline_result()]))
    s = c.post("/api/sessions").json()["id"]
    ask(c, s, "How do I create a transfer?")
    ask(c, s, "And what about its events?")
    assert "SECRET-ANSWER-TEXT" not in c.pipeline.questions[-1]


def test_standalone_question_gets_no_context(client):
    s = client.post("/api/sessions").json()["id"]
    ask(client, s, "How do I create a transfer?")
    q = "How do I verify webhook requests sent by Pismo to my endpoint?"
    ex = ask(client, s, q)
    assert client.pipeline.questions[-1] == q and ex["assistant_message"]["details"]["context"]["used"] is False


def test_context_window_limits(make_client, settings):
    s2 = Settings(DATABASE_URL="sqlite://", ASSISTANT_PRELOAD=False, CONTEXT_MAX_PRIOR_QUESTIONS=1, CONTEXT_MAX_CHARS=600)
    c = make_client(settings_override=s2)
    s = c.post("/api/sessions").json()["id"]
    for q in ("How do I create a transfer?", "How do I cancel a transfer?", "What about the required fields?"):
        ask(c, s, q)
    sent = c.pipeline.questions[-1]
    assert '"How do I cancel a transfer?"' in sent and "create a transfer" not in sent   # only the most recent one
    off = Settings(DATABASE_URL="sqlite://", ASSISTANT_PRELOAD=False, CONTEXT_MAX_PRIOR_QUESTIONS=0)
    c0 = make_client(settings_override=off)
    s0 = c0.post("/api/sessions").json()["id"]
    ask(c0, s0, "How do I create a transfer?")
    ask(c0, s0, "What about the required fields?")
    assert c0.pipeline.questions[-1] == "What about the required fields?"


def test_build_pipeline_question_char_budget():
    q, used = build_pipeline_question("And its events?", ["a" * 50, "b" * 500], max_chars=100)
    assert used and "b" * 100 in q and "a" not in q.split("context only:")[1]
    assert build_pipeline_question("And its events?", [], 600) == ("And its events?", False)
    assert build_pipeline_question("And its events?", ["x"], 0) == ("And its events?", False)


def test_is_follow_up():
    assert is_follow_up("What about the required fields?") and is_follow_up("And the events?") and is_follow_up("Is it deprecated?")
    assert not is_follow_up("How do I verify webhook requests sent by Pismo to my endpoint?")
