"""Greeting fast path: whole-message greetings/thanks are answered without retrieval, the LLM, citation validation or
follow-up context, and are persisted like any other exchange. Everything else still goes through the pipeline."""
import pytest

from backend.app.services.conversation import GREETING_REPLY, THANKS_REPLY, greeting_kind


def ask(c, sid, q):
    r = c.post(f"/api/sessions/{sid}/messages", json={"content": q})
    assert r.status_code == 201, r.text
    return r.json()


@pytest.mark.parametrize("text,kind", [
    ("hi", "greeting"), ("Hi!", "greeting"), ("  HELLO.  ", "greeting"), ("hey", "greeting"), ("Hey there!", "greeting"),
    ("Good morning", "greeting"), ("good   evening!!", "greeting"), ("hiya :)", "greeting"),
    ("thanks", "thanks"), ("Thank you!", "thanks"), ("thank you very much.", "thanks"), ("Many thanks", "thanks"),
])
def test_greeting_kind_matches_whole_message_greetings(text, kind):
    assert greeting_kind(text) == kind


@pytest.mark.parametrize("text", [
    "What about events?", "Hi, how do I configure a webhook?", "hello WEAM0029", "hi there, what is WEAM0029?",
    "thanks, and what about refunds?", "history", "high", "hello world api", "ok", "And the events?", "Hi?? WEAM0029",
    "How do I say hello to the API?", "help",
])
def test_greeting_kind_rejects_everything_else(text):
    assert greeting_kind(text) is None


def test_greeting_in_new_session_bypasses_pipeline_and_is_persisted(client, engine):
    s = client.post("/api/sessions").json()["id"]
    ex = ask(client, s, "Hello!")
    assert client.pipeline.questions == []                                  # no retrieval / generation call at all
    u, a = ex["user_message"], ex["assistant_message"]
    assert (u["role"], u["seq"], u["content"]) == ("user", 1, "Hello!")
    assert (a["role"], a["seq"], a["status"], a["content"], a["citations"]) == ("assistant", 2, "answered", GREETING_REPLY, [])
    d = a["details"]
    assert d["response_kind"] == "greeting" and d["warnings"] == [] and d["evidence"] == [] and d["model"] is None
    assert d["context"] == {"used": False, "prior_message_ids": [], "pipeline_question": None}
    assert d["citations_valid"] is None and d["verification"] is None    # nothing was validated, nothing claimed
    t = d["timings"]
    assert "pipeline_call_ms" not in t and "llm_ms" not in t and t["total_ms"] >= t["db_question_ms"] >= 0
    # stored exactly as returned, in order, and the session is titled from the first message as usual
    msgs = client.get(f"/api/sessions/{s}/messages").json()["messages"]
    assert [(m["seq"], m["role"], m["content"]) for m in msgs] == [(1, "user", "Hello!"), (2, "assistant", GREETING_REPLY)]
    assert client.get(f"/api/sessions/{s}").json()["title"] == "Hello!"
    act = client.get("/api/activity").json()["activity"][0]
    assert act["event"] == "message.greeting" and act["status"] == "answered" and act["http_status"] == 201
    assert act["citation_count"] == 0 and act["evidence_count"] == 0 and act["model"] is None and act["session_id"] == s


def test_greeting_after_technical_question_does_not_reuse_it(client):
    s = client.post("/api/sessions").json()["id"]
    ask(client, s, "What does WEAM0029 mean?")
    assert len(client.pipeline.questions) == 1
    ex = ask(client, s, "hi")
    assert len(client.pipeline.questions) == 1                              # the earlier question was not re-sent
    a = ex["assistant_message"]
    assert a["content"] == GREETING_REPLY and "WEAM0029" not in a["content"] and a["citations"] == []
    assert a["details"]["context"]["used"] is False and a["seq"] == 4
    thanks = ask(client, s, "Thank you!")["assistant_message"]
    assert thanks["content"] == THANKS_REPLY and thanks["seq"] == 6 and len(client.pipeline.questions) == 1


def test_question_starting_with_greeting_uses_pipeline(client):
    s = client.post("/api/sessions").json()["id"]
    # the greeting is set aside and the question itself goes to the pipeline (stored as typed)
    for q, sent in (("Hi, how do I configure a webhook?", "how do I configure a webhook?"), ("hello WEAM0029", "WEAM0029")):
        ex = ask(client, s, q)
        assert ex["assistant_message"]["details"].get("response_kind") is None
        assert client.pipeline.questions[-1] == sent and ex["user_message"]["content"] == q
    assert len(client.pipeline.questions) == 2


def test_short_follow_up_keeps_same_session_context(client):
    s = client.post("/api/sessions").json()["id"]
    first = ask(client, s, "How do I create a transfer?")
    ex = ask(client, s, "What about events?")
    sent = client.pipeline.questions[-1]
    assert sent.startswith("What about events?") and '"How do I create a transfer?"' in sent
    assert ex["assistant_message"]["details"]["context"]["prior_message_ids"] == [first["user_message"]["id"]]


def test_greeting_in_history_is_not_used_as_follow_up_context(client):
    s = client.post("/api/sessions").json()["id"]
    first = ask(client, s, "How do I create a transfer?")
    ask(client, s, "thanks")
    ask(client, s, "hello")
    ex = ask(client, s, "What about events?")
    sent = client.pipeline.questions[-1]
    assert '"How do I create a transfer?"' in sent and '"thanks"' not in sent and '"hello"' not in sent
    assert ex["assistant_message"]["details"]["context"]["prior_message_ids"] == [first["user_message"]["id"]]


def test_sessions_with_different_histories_never_share_context(client):
    a = client.post("/api/sessions").json()["id"]
    b = client.post("/api/sessions").json()["id"]
    ask(client, a, "How do I create a transfer?")
    ask(client, b, "What does WEAM0029 mean?")
    ask(client, a, "What about events?")
    sent_a = client.pipeline.questions[-1]
    ask(client, b, "And is it deprecated?")
    sent_b = client.pipeline.questions[-1]
    assert '"How do I create a transfer?"' in sent_a and "WEAM0029" not in sent_a
    assert '"What does WEAM0029 mean?"' in sent_b and "transfer" not in sent_b
    # a greeting in a third, new session gets nothing from either
    c = client.post("/api/sessions").json()["id"]
    g = ask(client, c, "hi")["assistant_message"]
    assert g["details"]["context"]["used"] is False and g["content"] == GREETING_REPLY and len(client.pipeline.questions) == 4
