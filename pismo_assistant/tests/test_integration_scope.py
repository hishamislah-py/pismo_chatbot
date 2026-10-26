"""Integration scoping (pismo_assistant/integrations.py): client-webhook questions never get data-platform event-delivery
evidence, and an answer citing such evidence for them fails citation validation even when the cited text matches.

Deterministic: unit tests plus the real served index (skipped when it cannot be loaded); no network, no live model.
Each index test first shows the original failure with the fix switched off, so it exercises the reported defect."""
import os

import pytest

from pismo_assistant import citations, config, integrations
from pismo_assistant.evidence import Evidence, OperationIndex, assemble
from pismo_assistant.integrations import CLIENT_WEBHOOKS, DATA_PLATFORM_DELIVERY, question_scope
from pismo_assistant.retrieval import Hit

CERT_Q = "What certificate URL do I use to verify webhooks in production?"
DP_URL = "https://prod.pismo.io/v1/certs"
WEBHOOK_URL = "https://<Production Domain>/v1/certs"
DP_GUIDE = "docs/data-and-reporting/pismo-data-platform-http-integration-guide-beta.md"
WEBHOOK_GUIDE = "docs/get-started/verifying-webhook-requests.md"
DP_KU = "KU-EVT-pismo-data-platform-http-integration-guide-beta"
WEBHOOK_KU = "KU-EVT-verifying-webhook-requests"


# ---------------- question scope and provenance ----------------

@pytest.mark.parametrize("q,scope", [
    (CERT_Q, {CLIENT_WEBHOOKS}),
    ("How do I verify that a webhook request really came from Pismo?", {CLIENT_WEBHOOKS}),
    ("How do I verify the JWT on Pismo data platform HTTP event deliveries?", {DATA_PLATFORM_DELIVERY}),
    ("How do I verify HTTP webhook (beta) requests?", {DATA_PLATFORM_DELIVERY}),      # Pismo's name for the data-platform delivery
    ("How do I verify JWTs on event deliveries and on webhooks, and is the process the same?", {CLIENT_WEBHOOKS, DATA_PLATFORM_DELIVERY}),
    ("How does API authentication work?", set()),
    ("If my event consumer was down, can Pismo redeliver real-time events on request?", {DATA_PLATFORM_DELIVERY}),
])
def test_question_scope(q, scope):
    assert question_scope(q) == scope


def test_only_a_client_webhook_only_question_excludes_anything():
    assert integrations.excluded_integrations(CERT_Q) == {DATA_PLATFORM_DELIVERY}
    for q in ("How do I verify the JWT on Pismo data platform HTTP event deliveries?", "How does API authentication work?",
              "How do I verify JWTs on event deliveries and on webhooks, and is the process the same?"):
        assert integrations.excluded_integrations(q) == set()


def test_provenance_decides_integration_never_text():
    dp = {"source_path": DP_GUIDE, "text": "nothing about integrations"}
    wh = {"source_path": WEBHOOK_GUIDE, "text": "data platform event delivery " + DP_URL}   # text mentioning the other one
    generated = {"source_path": None, "ku_sources": [DP_GUIDE]}
    mixed = {"source_path": None, "ku_sources": [DP_GUIDE, WEBHOOK_GUIDE]}
    assert integrations.chunk_integration(dp) == DATA_PLATFORM_DELIVERY
    assert integrations.chunk_integration(generated) == DATA_PLATFORM_DELIVERY
    assert integrations.chunk_integration(wh) is None and integrations.chunk_integration(mixed) is None
    assert integrations.chunk_integration({}) is None                                   # unknown is never excluded


def test_switch_restores_old_behaviour(monkeypatch):
    monkeypatch.setattr(config, "ENABLE_INTEGRATION_SCOPE", False)
    assert integrations.excluded_integrations(CERT_Q) == set()


# ---------------- citation validation ----------------

def _ev(label, path, ku, text):
    return Evidence(label=label, chunk_id=f"{ku}::x", ku_id=ku, ku_title="t", section="s", text=text,
                    source_refs=[{"path": path, "url": "https://developers.pismo.io/x", "sha256": "0"}], flags=[],
                    origin="retrieved", reason="hybrid rank")


def test_textually_valid_citation_from_another_integration_is_rejected():
    ev = [_ev("E1", DP_GUIDE, DP_KU, f"Production environment: {DP_URL}"),
          _ev("E2", WEBHOOK_GUIDE, WEBHOOK_KU, f"Production: curl -i {WEBHOOK_URL}")]
    answer = f"Use `{DP_URL}` to fetch the public keys in production [E1]."
    plain = citations.validate(answer, ["E1"], ev, status="answered")
    assert plain.ok                                                     # the token is in the cited passage...
    scoped = citations.validate(answer, ["E1"], ev, status="answered", excluded_integrations={DATA_PLATFORM_DELIVERY})
    assert not scoped.ok and scoped.integration_mismatch               # ...but it documents another integration
    assert scoped.checks()["integration_scope"] is False


def test_webhook_placeholder_answer_passes_scoped_validation():
    ev = [_ev("E1", WEBHOOK_GUIDE, WEBHOOK_KU, f"Production: curl -i {WEBHOOK_URL}")]
    rep = citations.validate(f"In production, call `{WEBHOOK_URL}` [E1].", ["E1"], ev, status="answered",
                             excluded_integrations={DATA_PLATFORM_DELIVERY})
    assert rep.ok and rep.checks()["integration_scope"] is True


# ---------------- evidence expansion cannot reintroduce excluded evidence ----------------

def _chunk(cid, ku, path, flags=()):
    return {"chunk_id": cid, "ku_id": ku, "ku_title": ku, "section_heading": "s", "heading_path": [ku, "s"], "ku_type": "workflow_guide",
            "text": "text", "flags": list(flags), "source_path": path, "ku_sources": [path], "source_refs": [], "operation": None}


def test_expansion_respects_the_exclusion():
    overview = _chunk(f"{WEBHOOK_KU}::overview", WEBHOOK_KU, WEBHOOK_GUIDE, ["procedure_overview"])
    foreign = _chunk(f"{DP_KU}::step", DP_KU, DP_GUIDE, ["procedure_step"])
    idx = OperationIndex([overview, foreign])
    idx.procedure_steps = {(WEBHOOK_KU, WEBHOOK_GUIDE): [foreign]}        # force a relationship that points at the other integration
    hits = [Hit(overview, 1, "retrieved", "hybrid rank")]
    assert [e.chunk_id for e in assemble(hits, idx)] == [overview["chunk_id"], foreign["chunk_id"]]
    exclude = lambda c: integrations.chunk_integration(c) == DATA_PLATFORM_DELIVERY  # noqa: E731
    assert [e.chunk_id for e in assemble(hits, idx, exclude=exclude)] == [overview["chunk_id"]]


# ---------------- the served index ----------------

@pytest.fixture(scope="module")
def assistant():
    before = dict(os.environ)
    os.environ.update(HF_HUB_OFFLINE="1", TRANSFORMERS_OFFLINE="1", OPENAI_API_KEY="")
    try:
        from pismo_assistant.pipeline import Assistant
        return Assistant()
    except Exception as e:  # pragma: no cover - depends on local index/model files
        pytest.skip(f"real index not available: {type(e).__name__}")
    finally:
        os.environ.clear()
        os.environ.update(before)


def _texts(ev):
    return "\n".join(e.text for e in ev)


def test_original_failure_reproduces_without_the_fix(assistant, monkeypatch):
    monkeypatch.setattr(config, "ENABLE_INTEGRATION_SCOPE", False)
    ev = assistant.evidence(CERT_Q)
    assert any(e.ku_id == DP_KU for e in ev) and DP_URL in _texts(ev)


def test_webhook_certificate_question_gets_only_webhook_configuration(assistant):
    ev = assistant.evidence(CERT_Q)
    assert all(integrations.evidence_integration(e) != DATA_PLATFORM_DELIVERY for e in ev)
    assert DP_URL not in _texts(ev)
    assert WEBHOOK_URL in _texts(ev)                                    # the documented placeholder reaches the model
    assert len(ev) >= config.TOP_K                                      # excluded slots were refilled from the ranking


def test_data_platform_question_keeps_its_own_documentation(assistant):
    ev = assistant.evidence("How do I verify the JWT on Pismo data platform HTTP event deliveries?")
    assert any(e.ku_id == DP_KU for e in ev) and DP_URL in _texts(ev)


def test_comparison_question_keeps_both_integrations(assistant):
    ev = assistant.evidence("How do I verify JWTs on event deliveries and on webhooks, and is the process the same?")
    assert {DP_KU, WEBHOOK_KU} <= {e.ku_id for e in ev}


@pytest.mark.parametrize("q", ["How does API authentication work?", "What is 3DS authentication?",
                               "How do I configure real-time event delivery to AWS SNS?", "What does WEAM0029 mean?"])
def test_unscoped_questions_are_unchanged(assistant, monkeypatch, q):
    after = [e.chunk_id for e in assistant.evidence(q)]
    monkeypatch.setattr(config, "ENABLE_INTEGRATION_SCOPE", False)
    assert [e.chunk_id for e in assistant.evidence(q)] == after


def test_pipeline_rejects_a_data_platform_url_answer_end_to_end(assistant, monkeypatch):
    """Even if a data-platform passage reached the model (fix bypassed for retrieval only), the answer is flagged."""
    from pismo_assistant.generation import Generated
    monkeypatch.setattr(config, "ENABLE_INTEGRATION_SCOPE", False)
    ev = assistant.evidence(CERT_Q)
    monkeypatch.setattr(config, "ENABLE_INTEGRATION_SCOPE", True)
    label = next(e.label for e in ev if e.ku_id == DP_KU)

    class Fake:
        def generate(self, question, evidence):
            return Generated("answered", f"Use `{DP_URL}` in production [{label}].", [label], "", "{}", "fake")
    monkeypatch.setattr(assistant, "evidence", lambda q: ev)
    monkeypatch.setattr(assistant, "generator", Fake())
    r = assistant.answer(CERT_Q)
    assert r["citations_valid"] is False and r["verification"]["integration_scope"] is False
    assert any("another integration" in w for w in r["warnings"])
