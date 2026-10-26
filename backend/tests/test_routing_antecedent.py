"""route(): a pronoun with no earlier topic asks for clarification only when the message names no subject of its own
before the pronoun. Pure decision-function tests; the existing table in test_routing.py runs unchanged."""
import pytest

from backend.app.services.conversation import Route, has_own_antecedent, route


@pytest.mark.parametrize("text", [
    "Which signature header does Pismo send on webhooks, and its format?",                        # live 2026-10-23
    "How do I verify JWTs on event deliveries and on webhooks, and is the process the same?",     # audit F4 2026-10-22
])
def test_pronoun_with_an_antecedent_in_the_message_is_answered(text):
    assert route(text, has_topic=False) == Route("rag", "standalone")


@pytest.mark.parametrize("text", [
    "Is it deprecated?", "Can they be retried?", "Is this still supported?", "What is its rate limit?",
    "How do I call it from Postman?", "Does Pismo support it?",
])
def test_genuinely_unresolved_references_still_ask_for_clarification(text):
    assert route(text, has_topic=False) == Route("clarification", "unresolved_reference")


def test_pismo_alone_is_not_an_antecedent():
    assert has_own_antecedent("Does Pismo support ") is False
    assert has_own_antecedent("Which signature header does Pismo send on webhooks, and ") is True


def test_with_an_earlier_topic_the_referential_route_is_unchanged():
    assert route("Which signature header does Pismo send on webhooks, and its format?", has_topic=True) == \
        Route("rag", "referential_cue", use_context=True)
