"""Follow-up classification: only messages that refer back (connective or pronoun) and name no identifier of their own
get same-session context. Message length alone never does. The stored user message is always the text as typed."""
import pytest

from backend.app.services.conversation import GREETING_REPLY, core_message, follow_up_rule, is_follow_up

DEMO_QUESTIONS = [  # pismo_assistant/verify_demo.py Q1-Q6, verbatim
    "What does WEAM0029 mean?", "How do I release funds that I previously held on an account?",
    "Which event does post-transfers emit?", "Which event is generated when I create a transfer?",
    "How do I verify webhook requests?", "How do I perform PCI card go-live?",
]


def ask(c, sid, q):
    r = c.post(f"/api/sessions/{sid}/messages", json={"content": q})
    assert r.status_code == 201, r.text
    return r.json()


@pytest.mark.parametrize("q", [
    "What about events?", "And its required fields?", "Is it deprecated?", "What does that mean?", "Is this still supported?",
    "Which of these events is emitted first?", "And the events?", "What about the second endpoint?", "Can they be retried?",
])
def test_referential_follow_ups(q):
    assert follow_up_rule(q) == "referential_cue" and is_follow_up(q)


@pytest.mark.parametrize("q,rule", [
    ("Rate limits?", "standalone"), ("PCI card go-live steps?", "standalone"), ("Webhook retries?", "standalone"),
    ("How do I release funds that I previously held on an account?", "standalone"),   # relative "that"
    ("Where is the endpoint that creates transfers?", "standalone"),
    ("hello WEAM0029", "own_identifier"), ("And WMLP1020?", "own_identifier"), ("What about post-transfers?", "own_identifier"),
    ("Is GET /cardsonfile/v2/cardsonfile/cards/{uuid} deprecated?", "own_identifier"),
])
def test_self_contained_messages(q, rule):
    assert follow_up_rule(q) == rule and not is_follow_up(q)


def test_no_demo_question_is_treated_as_a_follow_up():
    assert [q for q in DEMO_QUESTIONS if is_follow_up(q)] == []


def test_genuine_follow_up_uses_same_session_context(client):
    s = client.post("/api/sessions").json()["id"]
    first = ask(client, s, "How do I create a transfer?")
    ex = ask(client, s, "What about events?")
    sent = client.pipeline.questions[-1]
    assert sent.startswith("What about events?") and '"How do I create a transfer?"' in sent
    ctx = ex["assistant_message"]["details"]["context"]
    assert ctx["used"] and ctx["rule"] == "referential_cue" and ctx["prior_message_ids"] == [first["user_message"]["id"]]
    assert ex["user_message"]["content"] == "What about events?"            # stored exactly as typed


@pytest.mark.parametrize("q", ["Rate limits?", "PCI card go-live steps?", "What does WEAM0029 mean?", "hello WEAM0029",
                               "And WMLP1020?"])
def test_unrelated_or_self_contained_question_gets_no_context(client, q):
    s = client.post("/api/sessions").json()["id"]
    ask(client, s, "How do I create a transfer?")
    ex = ask(client, s, q)
    assert client.pipeline.questions[-1] == core_message(q)                  # as typed, minus a leading greeting
    assert ex["assistant_message"]["details"]["context"]["used"] is False


def test_demo_questions_in_one_session_are_sent_exactly_as_typed(client):
    s = client.post("/api/sessions").json()["id"]
    for q in DEMO_QUESTIONS:
        ask(client, s, q)
    assert client.pipeline.questions == DEMO_QUESTIONS


def test_hi_after_technical_question_is_a_greeting_without_pipeline(client):
    s = client.post("/api/sessions").json()["id"]
    ask(client, s, "What does WEAM0029 mean?")
    a = ask(client, s, "hi")["assistant_message"]
    assert a["content"] == GREETING_REPLY and len(client.pipeline.questions) == 1
