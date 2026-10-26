"""Candidate index candidates/ku_v1_2 (KU collection v1.2: title alias, body-hash normalization N-01, source-declared
verification procedure used by the evidence assembler).

Offline: no OpenAI, no network; the generator is a deterministic fake, so these tests say nothing about real answer
quality. Skipped when the candidate index has not been built."""
import hashlib
import json
import os
import re
import sys

import pytest

from common import EXP, HANDOFF, MIG, RESULTS, read_jsonl

CAND = os.path.join(EXP, "candidates", "ku_v1_2")
CAND11 = os.path.join(EXP, "candidates", "ku_v1_1")
MIG11 = os.path.join(HANDOFF, "pismo_knowledge_units_migration_v1_1")
MIG12 = os.path.join(HANDOFF, "pismo_knowledge_units_migration_v1_2")
TARGET = "KU-EVT-verifying-webhook-requests"
KU_REL = os.path.join("knowledge_units", "events_and_webhooks", f"{TARGET}.md")
SOURCE = os.path.join(HANDOFF, "pismo_kb_release_r2", "kb_corpus", "docs", "get-started", "verifying-webhook-requests.md")
REMOVED = "A SHA256 digest of the base64 encoded request message body."
KEPT = "Apply a `SHA256` hash function on the payload and then encode the resulting hash in `base64` format."
OVERVIEW = f"{TARGET}::src-verifying-webhook-requests.verifying-webhook-requests"
PARSING = f"{OVERVIEW}.parsing-the-jwt"
KEYS = f"{OVERVIEW}.retrieving-a-list-of-public-keys"
MTLS = f"{OVERVIEW}.request-mtls-support-for-webhook-request"
BROAD = "How does webhook authentication work?"
CONTROLS = ["How does API authentication work?", "How are webhook retries handled?", "How does card tokenization work?",
            "How does the anti-fraud integration work?", "What is 3DS authentication?", "How do I configure a webhook?",
            "What security measures does the Pismo platform use?"]

pytestmark = pytest.mark.skipif(not os.path.isfile(os.path.join(CAND, "CANDIDATE.json")), reason="candidate index not built")


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


@pytest.fixture(scope="module")
def chunks12():
    return read_jsonl(os.path.join(CAND, "chunks.jsonl"))


@pytest.fixture(scope="module")
def ku12():
    return open(os.path.join(MIG12, KU_REL), encoding="utf-8").read()


class FakeGenerator:
    def __init__(self):
        self.answer, self.seen = None, []

    def generate(self, question, evidence):
        from pismo_assistant.generation import Generated
        self.seen.append((question, list(evidence)))
        status, text = self.answer(evidence)
        return Generated(status, text, [], "", json.dumps({"answer": text}), "fake")


@pytest.fixture(scope="module")
def assistants():
    """v1 (served), v1.1 and v1.2 indexes, each verified against its own KU collection; paths restored afterwards."""
    before = dict(os.environ)
    os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", OPENAI_API_KEY="")
    sys.path.insert(0, HANDOFF)
    try:
        import corpus
        from pismo_assistant import config
        from pismo_assistant.pipeline import Assistant
        from pismo_assistant.retrieval import HybridRetriever
        saved = (config.CORPUS_SUMMARY_PATH, config.EMBEDDINGS_DIR, corpus.MIG, corpus.KU_DIR)
        out = {}
        try:
            out["v1"] = Assistant(retriever=HybridRetriever(), generator=FakeGenerator())
            for tag, cand, mig in (("v1.1", CAND11, MIG11), ("v1.2", CAND, MIG12)):
                config.CORPUS_SUMMARY_PATH, config.EMBEDDINGS_DIR = os.path.join(cand, "corpus_summary.json"), os.path.join(cand, "embeddings")
                corpus.MIG, corpus.KU_DIR = mig, os.path.join(mig, "knowledge_units")
                out[tag] = Assistant(retriever=HybridRetriever(chunks_path=os.path.join(cand, "chunks.jsonl"),
                                                               embedder=out["v1"].retriever.embedder), generator=FakeGenerator())
        finally:
            config.CORPUS_SUMMARY_PATH, config.EMBEDDINGS_DIR, corpus.MIG, corpus.KU_DIR = saved
    except Exception as e:  # pragma: no cover - depends on local index/model files
        pytest.skip(f"index not available: {type(e).__name__}: {e}")
    finally:
        os.environ.clear()
        os.environ.update(before)
    return out


# ---------------- protected originals ----------------

def test_raw_source_and_earlier_collections_are_unchanged():
    assert sha(SOURCE) == "6b7990115348f73b398fcc06ad7b16e067ecc0f1fec777296eed17b373c7c964"
    assert sha(os.path.join(MIG, KU_REL)) == "017e89d144e5d27bf1b94587b84989eb5a5e5f5720a087e403b4f1809664619b"      # v1
    assert sha(os.path.join(MIG11, KU_REL)) == "204c9162d898e7c15cf44f2b92d9e4030e308625af2614500824c7bfc5295fff"    # v1.1
    lines = open(SOURCE, encoding="utf-8").read().split("\n")
    assert REMOVED in lines[155] and KEPT in lines[228]          # the raw source still has both statements


def test_chunker_change_is_inert_for_v1_and_v1_1():
    import corpus
    saved = (corpus.MIG, corpus.KU_DIR)
    try:
        for mig, stored in ((MIG, os.path.join(RESULTS, "chunks.jsonl")), (MIG11, os.path.join(CAND11, "chunks.jsonl"))):
            corpus.MIG, corpus.KU_DIR = mig, os.path.join(mig, "knowledge_units")
            kus = sorted((corpus.load_ku(r) for r in corpus.approved_ku_files()[0]), key=lambda k: k["path"])
            assert [c for k in kus for c in corpus.chunk_ku(k)] == read_jsonl(stored)
    finally:
        corpus.MIG, corpus.KU_DIR = saved


def test_only_the_target_ku_changes_between_v1_1_and_v1_2(chunks12):
    old = read_jsonl(os.path.join(CAND11, "chunks.jsonl"))
    assert [c["chunk_id"] for c in old] == [c["chunk_id"] for c in chunks12]
    assert {b["ku_id"] for b, c in zip(old, chunks12) if b != c} == {TARGET}


# ---------------- the derived KU ----------------

@pytest.mark.parametrize("text", [
    "## Verification process", "## Parsing the JWT", "`Authorization` header containing a JWT",
    "## Retrieving a list of public keys", "https://sandbox.pismolabs.io/v1/certs", "rate limit of 5 requests per second",
    "## Renewing your list of public keys", "`Cache-Control` header", "max-age=23638", "## Verifying the token signature",
    "`kid` (key id) claim", "## Checking message integrity", KEPT, "## Request mTLS support for webhook requests",
    "Certificate Sign Request (CSR)"])
def test_every_workflow_section_is_in_the_derived_ku_and_its_chunks(ku12, chunks12, text):
    assert text in ku12
    assert any(text in c["text"] for c in chunks12 if c["ku_id"] == TARGET)


@pytest.mark.parametrize("claim", ["alg", "kid", "iss", "sub", "iat", "exp", "body-hash"])
def test_every_documented_claim_is_kept(chunks12, claim):
    parsing = next(c for c in chunks12 if c["chunk_id"] == PARSING)
    assert re.search(rf"^\s*{re.escape(claim)}\s*$", parsing["text"], re.M)


def test_body_hash_procedure_is_one_unambiguous_instruction(chunks12, ku12):
    assert all(REMOVED not in c["text"] for c in chunks12)                      # nowhere in the index
    assert [c["chunk_id"] for c in chunks12 if KEPT in c["text"]] == [KEYS]     # exactly one place
    assert "Source contradiction (SC-10)" not in ku12                          # no user-facing caveat
    assert "Example: dX5GKSLmA9o7lijdQrm7kR4om6rLTHssk1GJQiDGuUk=" in ku12       # the claim row keeps its example


def test_normalization_is_recorded_internally_and_not_presented_as_a_pismo_correction(ku12):
    changes = open(os.path.join(MIG12, "CHANGES_v1_2.md"), encoding="utf-8").read()
    issues = open(os.path.join(MIG12, "ISSUES_AND_GAPS.md"), encoding="utf-8").read()
    assert "N-01" in changes and "not a correction confirmed by Pismo" in changes
    assert "N-01" in issues and "not a correction confirmed by Pismo" in issues
    assert "except for editorial normalization N-01 recorded in the KB change log" in ku12
    for phrase in ("Pismo corrected", "official correction", "confirmed by Pismo", "SC-10"):
        assert phrase not in ku12


def test_mtls_section_is_verbatim(chunks12):
    lines = open(SOURCE, encoding="utf-8").read().split("\n")
    mtls = next(c for c in chunks12 if c["chunk_id"] == MTLS)
    assert mtls["text"] == "\n".join(lines[232:242]).strip("\n")
    assert not any(f.startswith("procedure") for f in mtls["flags"])


def test_procedure_flags_mark_exactly_the_overview_and_the_step_chunks(chunks12):
    flagged = {c["chunk_id"]: [f for f in c["flags"] if f.startswith("procedure")] for c in chunks12
               if any(f.startswith("procedure") for f in c["flags"])}
    assert flagged == {OVERVIEW: ["procedure_overview"], PARSING: ["procedure_step"], KEYS: ["procedure_step"]}


def test_no_invented_header_anywhere(chunks12):
    assert all("X-Pismo-Signature" not in c["text"] for c in chunks12)


# ---------------- evidence that reaches answer generation ----------------

def test_broad_question_gets_overview_parsing_and_public_key_evidence(assistants):
    a = assistants["v1.2"]
    a.generator.answer = lambda ev: ("not_documented", "Not documented.")
    a.answer(BROAD)
    ids = [e.chunk_id for e in a.generator.seen[-1][1]]
    assert {OVERVIEW, PARSING, KEYS} <= set(ids)
    steps = [e for e in a.generator.seen[-1][1] if e.origin == "procedure_step"]
    assert all(e.chunk_id in (PARSING, KEYS) for e in steps)


def test_procedure_relationship_is_inert_for_v1_and_v1_1(assistants):
    for tag in ("v1", "v1.1"):
        assert all(e.origin != "procedure_step" for e in assistants[tag].evidence(BROAD))


def test_body_hash_question_gets_the_single_procedure(assistants):
    ev = assistants["v1.2"].evidence("How do I calculate the webhook body-hash?")
    text = "\n".join(e.text for e in ev)
    assert KEPT in text and REMOVED not in text


@pytest.mark.parametrize("q", CONTROLS)
def test_controls_get_the_same_evidence_as_v1_1(assistants, q):
    assert [e.chunk_id for e in assistants["v1.2"].evidence(q)] == [e.chunk_id for e in assistants["v1.1"].evidence(q)]


def test_invented_webhook_header_is_still_flagged(assistants):
    a = assistants["v1.2"]
    a.generator.answer = lambda ev: ("answered", "Pismo sends an `X-Pismo-Signature` header "
                                    f"[{next(e.label for e in ev if e.chunk_id == OVERVIEW)}].")
    r = a.answer(BROAD)
    assert r["citations_valid"] is False and any("X-Pismo-Signature" in w for w in r["warnings"])


def test_documented_header_answer_passes(assistants):
    a = assistants["v1.2"]
    a.generator.answer = lambda ev: ("answered", "The request includes an `Authorization` header containing a JWT "
                                    f"[{next(e.label for e in ev if e.chunk_id == PARSING)}].")
    r = a.answer(BROAD)
    assert r["citations_valid"] is True and r["warnings"] == []
