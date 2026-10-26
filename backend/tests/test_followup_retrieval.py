"""Follow-up rule checked against the REAL index and retriever (no generation, no network; ~15 s to load).

Pins the evidence behind the rule in conversation.py: real follow-ups need the earlier question to retrieve anything
relevant, while self-contained short questions are hurt by it; and the six verified demo questions keep their expected
evidence when asked in the middle of a session. Skipped if the local index or embedding model cannot be loaded."""
import os
from dataclasses import asdict

import pytest

from backend.app.services.conversation import build_pipeline_question

PRIOR_LIMIT = 600


@pytest.fixture(scope="module")
def pipeline():
    before = dict(os.environ)
    os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", OPENAI_API_KEY="")   # never any network
    try:
        from pismo_assistant.evidence import matched_operations
        from pismo_assistant.pipeline import Assistant
        from pismo_assistant.verify_demo import QUESTIONS
        a = Assistant()
    except Exception as e:  # pragma: no cover - depends on local index/model files
        pytest.skip(f"real index not available: {type(e).__name__}")
    finally:
        os.environ.clear()                       # pismo_assistant.config loaded the project .env; undo that
        os.environ.update(before)
    return a, matched_operations, QUESTIONS


def sent(question, prior):
    return build_pipeline_question(question, [prior], PRIOR_LIMIT)[0]


def relevant(a, q, needle):
    return sum(needle.lower() in (e.ku_id + " " + e.chunk_id).lower() for e in a.evidence(q))


@pytest.mark.parametrize("prior,msg,needle", [
    ("How do I create a transfer?", "What about events?", "transfer"),
    ("Which event does post-transfers emit?", "And its required fields?", "transfer"),
    ("Can I still call GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount?", "Is it deprecated?", "card"),
])
def test_real_follow_ups_need_context_to_retrieve_anything(pipeline, prior, msg, needle):
    a, _, _ = pipeline
    q = sent(msg, prior)
    assert q != msg                                          # the rule does add context here
    assert relevant(a, msg, needle) == 0 < relevant(a, q, needle)


@pytest.mark.parametrize("prior,msg", [
    ("What does WEAM0029 mean?", "PCI card go-live steps?"),
    ("How do I create a transfer?", "Rate limits?"),
    ("How do I create a transfer?", "What does WEAM0029 mean?"),
    ("What does WEAM0029 mean?", "And WMLP1020?"),
])
def test_self_contained_questions_are_not_contaminated(pipeline, prior, msg):
    a, matched_operations, _ = pipeline
    assert sent(msg, prior) == msg                           # sent exactly as typed
    # what the old length rule would have sent pulls in the earlier topic
    old = f"{msg}\n\n(Follow-up in the same conversation. Earlier questions, for context only: \"{prior}\")"
    assert [e.chunk_id for e in a.evidence(old)] != [e.chunk_id for e in a.evidence(msg)]


def test_identifier_questions_keep_their_own_evidence(pipeline):
    a, matched_operations, _ = pipeline
    q = sent("And WMLP1020?", "What does WEAM0029 mean?")
    assert any(e.ku_id == "KU-ERR-codes-wmlp" for e in a.evidence(q))      # its own error-catalogue entry
    q = sent("What does WEAM0029 mean?", "How do I create a transfer?")
    assert matched_operations(q, a.op_index) == [] and a.evidence(q)[0].ku_id == "KU-CHG-2-october-2026"


def test_demo_questions_keep_expected_evidence_mid_session(pipeline):
    a, matched_operations, questions = pipeline
    for spec in questions:
        prior = "How do I create a transfer?" if spec["id"] == "Q1" else "What does WEAM0029 mean?"
        q = sent(spec["q"], prior)
        assert q == spec["q"], spec["id"]
        assert spec["evidence"]([asdict(e) for e in a.evidence(q)]), spec["id"]
