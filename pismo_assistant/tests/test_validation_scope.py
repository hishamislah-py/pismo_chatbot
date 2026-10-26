"""Citation validation checks 6 (operation scope) and 7 (abstentions) in pismo_assistant/citations.py.

Synthetic evidence for the rules themselves, plus replays of the live failures of 2026-10-22/23 against the real
index (evidence is deterministic; no network, no model)."""
import pytest

from pismo_assistant import citations as C
from pismo_assistant.evidence import Evidence
from pismo_assistant.pipeline import Assistant

REFS = [{"path": "p", "url": "u"}]


def ev(label, chunk_id, text):
    return Evidence(label, chunk_id, chunk_id.split("::")[0], "t", "s", text, REFS, [], "retrieved", "hybrid rank")


PAYMENTS = ev("E1", "KU-API-pay::op-post-payments-v2-cancel", "POST /payments/v2/cancel | `x-tenant` | header | yes | BearerAuth")
METHODS = ev("E2", "KU-API-pm::op-post-transfers-cancel", "POST /payment-methods/v2/transfers/cancel requires BearerAuth")
GUIDE = ev("E3", "KU-PAY-guide::src-cancel.headers", "Every cancellation request must send the `x-tenant` header.")


# ---------------- check 6: operation scope ----------------

def test_generalized_requirement_missing_from_one_operation_fails():
    rep = C.validate("Both endpoints require the `x-tenant` header [E1][E2].", [], [PAYMENTS, METHODS], status="answered")
    assert not rep.ok and rep.checks()["operation_scope"] is False
    assert rep.cross_operation_claims == [{"token": "x-tenant", "operations": ["post-payments-v2-cancel", "post-transfers-cancel"],
                                           "not_documented_for": ["post-transfers-cancel"]}]
    assert rep.unsupported_tokens == []                     # the existing union check alone would have passed it


def test_requirement_shared_by_every_cited_operation_passes():
    rep = C.validate("Both operations require `BearerAuth` [E1][E2].", [], [PAYMENTS, METHODS], status="answered")
    assert rep.ok and rep.checks()["operation_scope"] is True


def test_requirement_stated_by_a_cited_general_guide_passage_passes():
    rep = C.validate("Both endpoints require the `x-tenant` header [E1][E2][E3].", [], [PAYMENTS, METHODS, GUIDE], status="answered")
    assert rep.ok and rep.cross_operation_claims == []


def test_requirements_attributed_per_operation_pass():
    answer = ("Each endpoint has its own headers: `POST /payments/v2/cancel` requires `x-tenant` [E1], and "
              "`POST /payment-methods/v2/transfers/cancel` requires `BearerAuth` [E2].")
    rep = C.validate(answer, [], [PAYMENTS, METHODS], status="answered")
    assert rep.ok and rep.cross_operation_claims == []


def test_event_slug_in_a_generalized_sentence_is_not_a_requirement():
    a = ev("E1", "KU-API-mig::op-post-v1-migrations-cards", "POST /v1/migrations/cards")
    b = ev("E2", "KU-API-mig::op-post-v1-migrations-go-live", "Emits `migration-account-go-live-outgoing-1` per account.")
    rep = C.validate("Each unique Go-Live request generates one `migration-account-go-live-outgoing-1` event per account "
                     "[E1][E2].", [], [a, b], status="answered")
    assert rep.cross_operation_claims == []


def test_paths_and_error_codes_are_not_checked_across_operations():
    a = ev("E1", "KU-A::op-get-a", "GET /v1/a returns EHLD0016")
    b = ev("E2", "KU-B::op-get-b", "GET /v1/b returns EHLD0016")
    rep = C.validate("Both `GET /v1/a` and `GET /v1/b` return EHLD0016 [E1][E2].", [], [a, b], status="answered")
    assert rep.cross_operation_claims == []


def test_single_operation_citations_are_unaffected():
    rep = C.validate("All requests require the `x-tenant` header [E1].", [], [PAYMENTS], status="answered")
    assert rep.ok and rep.cross_operation_claims == []


# ---------------- check 7: abstentions ----------------

WEBHOOK = ev("E1", "KU-EVT-verifying-webhook-requests::src-x", "Webhook requests use a JWT with a kid claim and a body-hash claim.")
OTHER = ev("E2", "KU-BANK-file::src-sig", "The bulk upload uses a `Signature` header. X-Pismo-Trace is sent by the gateway.")
Q = "What is the exact X-Pismo-Signature header format for Pismo webhooks?"


def test_requested_identifier_named_as_undocumented_on_its_own_line_passes():
    answer = "The `X-Pismo-Signature` header format is not documented.\nWebhook requests carry a JWT with a kid claim [E1]."
    rep = C.validate(answer, [], [WEBHOOK], status="not_documented", question=Q)
    assert rep.ok and rep.abstained_identifiers == ["X-Pismo-Signature"] and rep.uncited_claims == []


def test_requested_identifier_named_as_undocumented_on_a_cited_line_passes():
    answer = ("The documentation does not specify an exact `X-Pismo-Signature` header format. Webhook requests carry a "
              "JWT with a kid claim [E1].")
    rep = C.validate(answer, [], [WEBHOOK], status="not_documented", question=Q)
    assert rep.ok and rep.unsupported_tokens == []


def test_invented_example_is_still_flagged():
    answer = ("The `X-Pismo-Signature` header format is not documented. It may look like `X-Pismo-Signature: <jwt>` "
              "[E1].")
    rep = C.validate(answer, [], [WEBHOOK], status="not_documented", question=Q)
    flagged = [t["token"] for t in rep.unsupported_tokens]
    assert not rep.ok and "X-Pismo-Signature: <jwt>" in flagged
    # the requested name also appears in that non-negating sentence, so it is not exempt either (stricter, by design)
    assert "X-Pismo-Signature" in flagged and rep.abstained_identifiers == []


def test_non_negated_use_is_flagged():
    rep = C.validate("Send the `X-Pismo-Signature` header with each request [E1].", [], [WEBHOOK], status="answered", question=Q)
    assert not rep.ok and rep.abstained_identifiers == []


def test_identifier_used_both_as_undocumented_and_as_a_claim_is_flagged():
    answer = "The `X-Pismo-Signature` format is not documented. Verify the `X-Pismo-Signature` value with the JWT [E1]."
    rep = C.validate(answer, [], [WEBHOOK], status="partial", question=Q)
    assert not rep.ok and rep.abstained_identifiers == []


def test_identifier_absent_from_the_question_is_flagged():
    answer = "The `X-Pismo-Signature` header format is not documented.\nWebhook requests carry a JWT [E1]."
    rep = C.validate(answer, [], [WEBHOOK], status="not_documented", question="How are Pismo webhooks verified?")
    assert not rep.ok and rep.uncited_claims


def test_identifier_present_in_the_evidence_is_checked_normally():
    q = "What is the X-Pismo-Trace header?"
    answer = "The `X-Pismo-Trace` header is not documented.\nWebhook requests carry a JWT [E1]."
    rep = C.validate(answer, [], [WEBHOOK, OTHER], status="not_documented", question=q)
    assert not rep.ok and rep.abstained_identifiers == []               # E2 contains it, so it is not exempt


def test_without_the_question_behaviour_is_unchanged():
    answer = "The `X-Pismo-Signature` header format is not documented.\nWebhook requests carry a JWT [E1]."
    rep = C.validate(answer, [], [WEBHOOK], status="not_documented")
    assert not rep.ok and rep.uncited_claims and rep.abstained_identifiers == []


# ---------------- replays of the live failures (real index) ----------------

@pytest.fixture(scope="module")
def real():
    return Assistant(generator=None)


CANCEL_Q = "How do I cancel a transfer?"


@pytest.mark.parametrize("line", [
    "   - Both operations require the `x-tenant` header with your tenant ID. [E4][E7]",                       # 2026-10-23
    "Required headers and security: both endpoints require BearerAuth and the `x-tenant` header; the Payment methods "
    "endpoints are PCI and the spec notes the `https://gw-pci.pismolabs.io` environment should be used. [E4][E7]",  # 2026-10-22
])
def test_live_x_tenant_generalizations_are_now_flagged(real, line):
    evidence = real.evidence(CANCEL_Q)
    assert evidence[3].chunk_id.endswith("::op-post-payments-v2-cancel") and evidence[6].chunk_id.endswith("::op-post-transfers-cancel")
    rep = C.validate(line, [], evidence, status="answered", question=CANCEL_Q)
    assert rep.unsupported_tokens == [] and "x-tenant" in [c["token"] for c in rep.cross_operation_claims]
    assert rep.checks()["operation_scope"] is False


def test_live_correct_abstention_now_passes(real):
    q = "What is the exact X-Pismo-Signature header format for Pismo webhooks?"
    answer = ("The documentation does not specify an exact `X-Pismo-Signature` header format for Pismo webhooks. The docs "
              "state that webhook requests use JSON Web Tokens (JWTs) signed with Pismo-held private keys and that the JWT "
              "contains a `kid` (key id) claim and a `body-hash` claim for payload-integrity verification [E1][E3].")
    rep = C.validate(answer, [], real.evidence(q), status="not_documented", question=q)
    assert rep.ok and rep.abstained_identifiers == ["X-Pismo-Signature"]


def test_live_abstention_with_an_invented_example_still_fails(real):
    q = "What is the exact X-Pismo-Signature header format for Pismo webhooks?"
    answer = ("The documentation does not provide the exact `X-Pismo-Signature` header format. Webhook requests include "
              "a JWT with a `kid` claim and a `body-hash` claim [E1][E3]. We would need to know whether the JWT appears "
              "raw in `X-Pismo-Signature: <jwt>`.")
    rep = C.validate(answer, [], real.evidence(q), status="not_documented", question=q)
    assert not rep.ok and "X-Pismo-Signature: <jwt>" in [t["token"] for t in rep.unsupported_tokens]
