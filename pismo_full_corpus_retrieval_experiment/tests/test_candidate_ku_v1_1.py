"""Candidate index candidates/ku_v1_1 (KU collection v1.1: webhook-verification title alias + SC-10 caveat).

Checks the change itself, the evidence it delivers to answer generation, and that citation validation still rejects
invented webhook details. The generator is a deterministic fake: these tests say nothing about real answer quality.
Offline (no OpenAI, no network). Skipped when the candidate index has not been built."""
import json
import os
import sys

import pytest

from common import EXP, HANDOFF, RESULTS, read_jsonl

CAND = os.path.join(EXP, "candidates", "ku_v1_1")
MIG_V11 = os.path.join(HANDOFF, "pismo_knowledge_units_migration_v1_1")
TARGET = "KU-EVT-verifying-webhook-requests"
ALIAS = "(authentication of incoming requests)"
SOURCE = os.path.join(HANDOFF, "pismo_kb_release_r2", "kb_corpus", "docs", "get-started", "verifying-webhook-requests.md")
QUOTES = {156: "A SHA256 digest of the base64 encoded request message body.",
          229: "Apply a `SHA256` hash function on the payload and then encode the resulting hash in `base64` format."}
CONTROLS = ["How does API authentication work?", "How are webhook retries handled?", "What is 3DS authentication?",
            "How does card tokenization work?", "How does the anti-fraud integration work?",
            "What security measures does the Pismo platform use?"]

pytestmark = pytest.mark.skipif(not os.path.isfile(os.path.join(CAND, "CANDIDATE.json")), reason="candidate index not built")


@pytest.fixture(scope="module")
def cand_chunks():
    return read_jsonl(os.path.join(CAND, "chunks.jsonl"))


class FakeGenerator:
    """Returns a fixed answer and records the evidence it was given."""

    def __init__(self):
        self.answer, self.seen = None, []

    def generate(self, question, evidence):
        from pismo_assistant.generation import Generated
        self.seen.append((question, list(evidence)))
        status, text = self.answer(evidence)
        return Generated(status, text, [], "", json.dumps({"answer": text}), "fake")


@pytest.fixture(scope="module")
def assistants():
    before = dict(os.environ)
    os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", OPENAI_API_KEY="")
    sys.path.insert(0, HANDOFF)
    try:
        import corpus
        from pismo_assistant import config
        from pismo_assistant.pipeline import Assistant
        from pismo_assistant.retrieval import HybridRetriever
        saved = (config.CORPUS_SUMMARY_PATH, config.EMBEDDINGS_DIR, corpus.MIG, corpus.KU_DIR)
        try:
            base = Assistant(retriever=HybridRetriever(), generator=FakeGenerator())
            config.CORPUS_SUMMARY_PATH, config.EMBEDDINGS_DIR = os.path.join(CAND, "corpus_summary.json"), os.path.join(CAND, "embeddings")
            corpus.MIG, corpus.KU_DIR = MIG_V11, os.path.join(MIG_V11, "knowledge_units")
            cand = Assistant(retriever=HybridRetriever(chunks_path=os.path.join(CAND, "chunks.jsonl"), embedder=base.retriever.embedder),
                             generator=FakeGenerator())
        finally:
            config.CORPUS_SUMMARY_PATH, config.EMBEDDINGS_DIR, corpus.MIG, corpus.KU_DIR = saved
    except Exception as e:  # pragma: no cover - depends on local index/model files
        pytest.skip(f"index not available: {type(e).__name__}: {e}")
    finally:
        os.environ.clear()
        os.environ.update(before)
    return base, cand


# ---------------- the change itself ----------------

def test_only_the_target_ku_changes(cand_chunks):
    base = read_jsonl(os.path.join(RESULTS, "chunks.jsonl"))
    assert [c["chunk_id"] for c in base] == [c["chunk_id"] for c in cand_chunks]
    changed = {b["ku_id"] for b, c in zip(base, cand_chunks) if b != c}
    assert changed == {TARGET}


def test_alias_is_in_the_title_of_every_target_chunk_and_nowhere_else(cand_chunks):
    for c in cand_chunks:
        if c["ku_id"] == TARGET:
            assert c["ku_title"] == f"Verifying webhook requests {ALIAS}"
            if c.get("source_path"):                      # verbatim source text is untouched
                assert ALIAS not in c["text"]
        else:
            assert ALIAS not in c["ku_title"] and ALIAS not in c["text"]
    assert "webhook" not in ALIAS.lower()


def test_sc10_caveat_quotes_both_source_lines_without_choosing(cand_chunks):
    cav = next(c for c in cand_chunks if c["chunk_id"] == f"{TARGET}::conflicts-caveats-and-evidence-gaps")
    lines = open(SOURCE, encoding="utf-8").read().split("\n")
    for n, q in QUOTES.items():
        assert q in lines[n - 1]                         # quote is on the stated source line
        assert f'"{q}"' in cav["text"] and f"line {n}" in cav["text"]
    assert "Source contradiction (SC-10)" in cav["text"]
    assert "not documented in the available source corpus" in cav["text"] and "not_documented_statement" in cav["flags"]
    for word in ("correct procedure is", "use the first", "use the second", "should be used"):
        assert word not in cav["text"]


# ---------------- evidence that reaches answer generation ----------------

def test_target_question_delivers_webhook_verification_evidence_to_generation(assistants):
    _, cand = assistants
    q = "How does webhook authentication work?"
    cand.generator.answer = lambda ev: ("not_documented", "Not documented.")
    cand.answer(q)
    sent_q, ev = cand.generator.seen[-1]
    assert sent_q == q
    ids = [e.chunk_id for e in ev]
    assert sum(e.ku_id == TARGET for e in ev) >= 4
    assert f"{TARGET}::src-verifying-webhook-requests.verifying-webhook-requests" in ids          # overview + verification process
    assert [e.chunk_id for e in cand.evidence(q)] == ids                                          # exactly what retrieval selected


def test_target_question_baseline_had_no_webhook_verification_evidence(assistants):
    base, _ = assistants
    assert sum(e.ku_id == TARGET for e in base.evidence("How does webhook authentication work?")) == 0


def test_body_hash_question_gets_both_statements_and_the_caveat(assistants):
    _, cand = assistants
    ev = cand.evidence("How is the body-hash of a Pismo webhook request computed and checked?")
    text = "\n".join(e.text for e in ev)
    assert all(q in text for q in QUOTES.values())
    assert any("Source contradiction (SC-10)" in e.text for e in ev)


@pytest.mark.parametrize("q", CONTROLS)
def test_control_questions_get_the_same_evidence(assistants, q):
    base, cand = assistants
    assert [e.chunk_id for e in cand.evidence(q)] == [e.chunk_id for e in base.evidence(q)]


def test_configure_a_webhook_keeps_the_same_sources(assistants):
    base, cand = assistants
    q = "How do I configure a webhook?"
    assert sorted(e.chunk_id for e in cand.evidence(q)) == sorted(e.chunk_id for e in base.evidence(q))


# ---------------- citation validation still guards the answer ----------------

def _label(ev, chunk_suffix):
    return next(e.label for e in ev if e.chunk_id.endswith(chunk_suffix))


def test_invented_webhook_header_is_flagged(assistants):
    _, cand = assistants
    cand.generator.answer = lambda ev: ("answered", "Pismo signs each webhook with an `X-Pismo-Signature` header "
                                        f"[{_label(ev, '::src-verifying-webhook-requests.verifying-webhook-requests')}].")
    r = cand.answer("How does webhook authentication work?")
    assert r["citations_valid"] is False
    assert any("X-Pismo-Signature" in w for w in r["warnings"])


def test_supported_answer_passes_validation(assistants):
    _, cand = assistants
    cand.generator.answer = lambda ev: ("answered", "Webhook requests carry a `JWT` signed with a public/private key pair "
                                        f"[{_label(ev, '::src-verifying-webhook-requests.verifying-webhook-requests')}].")
    r = cand.answer("How does webhook authentication work?")
    assert r["citations_valid"] is True and r["warnings"] == []
    assert [c["ku_id"] for c in r["citations"]] == [TARGET]
