"""Answer-prompt rules 4 (relevance and status) and 8 (writing style), revised 2026-10-22.

A. PROMPT TEXT (no model): the rules say what they should; unchanged rules keep their key wording.
B. PIPELINE / VALIDATOR (real index evidence + FAKE model outputs, no network): each outcome the rules ask for is
   carried through the pipeline correctly, and the outcomes they forbid are caught where the validator can catch them.
C. MODEL BEHAVIOUR (needs live calls; NOT run here): whether gpt-5-mini actually drops unrelated asides, labels a
   documented placeholder "answered", and escalates undocumented values. See the separately approved live check."""
import pytest

from pismo_assistant import config
from pismo_assistant.generation import SYSTEM_PROMPT, OpenAIGenerator
from pismo_assistant.pipeline import Assistant
from conftest import FakeClient, model_json

CERT_Q = "What certificate URL do I use to verify webhooks in production?"
PLACEHOLDER = "https://<Production Domain>/v1/certs"
DP_URL = "https://prod.pismo.io/v1/certs"
WEBHOOK_KU = "KU-EVT-verifying-webhook-requests"


def rule(n):
    """Text of rule n (up to the next numbered rule)."""
    start = SYSTEM_PROMPT.index(f"\n{n}. ")
    end = SYSTEM_PROMPT.find(f"\n{n + 1}. ", start)
    return SYSTEM_PROMPT[start:end if end > 0 else None]


# ---------------- A. prompt text ----------------

def test_the_related_evidence_permission_is_gone():
    assert "related evidence" not in SYSTEM_PROMPT
    assert "Use only the passages that answer the question and ignore the rest" not in SYSTEM_PROMPT   # moved into rule 4


def test_rule_4_states_relevance_once():
    r4 = rule(4)
    assert "Use only passages that directly answer the question" in r4
    assert "Do not mention other integrations, products, URLs, API operations or implementation details" in r4
    assert "do not add asides about passages that do not answer the question" in r4
    assert "do not present them as the answer" in r4                 # kept: test_questions relies on it
    assert SYSTEM_PROMPT.count("Use only passages that directly answer the question") == 1


def test_rule_4_defines_every_status_once():
    r4 = rule(4)
    for status in ("answered", "partial", "not_documented", "conflicting_sources"):
        assert r4.count(f'- "{status}":') == 1
    assert "A documented placeholder" in r4 and "still counts as answered when the procedure is otherwise complete" in r4
    assert "the customer must supply or confirm that value" in r4
    assert "a material part of the request is answered from the passages and another material part is not" in r4
    assert "the essential answer cannot be established from the passages" in r4
    assert '"conflicting_sources": see rule 5' in r4


@pytest.mark.parametrize("n,phrase", [
    (1, "Answer ONLY from the numbered evidence passages"),
    (2, "must appear verbatim in a passage you cite. If a detail is not in the evidence, say it is not documented."),
    (3, "copy them verbatim from a passage, and cite that passage on the line that introduces the block"),
    (5, 'Do not present removed or historical behaviour as current. If passages conflict, use status "conflicting_sources"'),
    (6, "Do not substitute a different operation with a similar name"),
    (7, "keys: status (one of answered, partial, not_documented, conflicting_sources), answer"),
    (8, "When the evidence is insufficient, say in one or two sentences exactly what is not documented"),
    (8, "these rules never relax rules 1 to 6"),
    (9, "Never combine labels inside one pair of brackets"),
])
def test_unrelated_rules_keep_their_wording(n, phrase):
    assert phrase in rule(n)


@pytest.mark.parametrize("phrase", [
    # answer first, no filler or commentary about the passages
    "Start with the answer itself: the operation, value, configuration or conclusion.",
    'Do not open with filler ("Sure", "Based on the documentation"), apologise, restate the question',
    '"the supplied passages contain...", "this example is verbatim from the guide"',
    # detail matched to the kind of question
    "a factual question gets a short, direct answer",
    "a how-to question gets numbered steps in the order they must be done",
    "a troubleshooting question gets the likely cause, the checks to run and the next action, keeping documented facts "
    "separate from what is uncertain",
    "a comparison explains the differences that matter",
    # concise but complete
    "Be concise but complete",
    "never drop a required operation, prerequisite, field, header, parameter or step to make an answer shorter",
    # several relevant operations: only documented distinctions
    "When multiple operations are relevant to the question, identify each operation supported by the evidence and "
    "explain the documented distinction.",
    "Do not infer which operation fits the user's task unless the evidence establishes it.",
    # identifiers exactly as documented
    "Put HTTP methods, paths, field names, headers, parameters, enum values and configuration keys in code formatting",
    "keep them, URLs and examples exactly as documented",
    # placeholders, history, insufficient evidence
    "When a documented value is a placeholder, say which value the user must supply or confirm.",
    "Say clearly when something is historical or has changed.",
    "When the evidence is insufficient, say in one or two sentences exactly what is not documented and what information "
    "would be needed.",
    # wording never overrides the evidence and citation rules
    "these rules never relax rules 1 to 6 or rule 9",
    "smoother wording never justifies moving or dropping a citation or changing a technical detail",
])
def test_rule_8_writing_style_contract(phrase):
    assert phrase in rule(8)


@pytest.mark.parametrize("phrase", [
    # no commentary about the passages or the answer itself
    "Never comment on the passages or on your own answer.",
    'Do not call an example or line "verbatim", "copied", "from the guide" or "from the documentation"',
    'do not add parenthetical notes such as "(Example verbatim above.)"',
    'do not refer to "the supplied passages", "the provided passages" or "the docs"',
    "The citation label is the only attribution needed.",
    # each fact once, no padding
    "Say each fact once.",
    "Do not repeat a step, end with a summary that restates the answer, or describe the same operation both in prose and "
    "in a list.",
    "Leave out optional fields, extra headers and lists of error codes unless the question asks for them or a step "
    "depends on them.",
    "give no more than one example per distinct request shape",
    # code formatting only for documented identifiers; plain-text abstention for undocumented ones
    "in code formatting when they are documented in the evidence",
    "When the user asks about a specific identifier that is not in the evidence, say in its own sentence, without a "
    "citation, that it is not documented for the integration the user asked about, naming it in plain text (not in code "
    "formatting).",
    "Do not show a guessed, hypothetical or example format or value for it",
])
def test_rule_8_follow_up_clauses(phrase):
    assert phrase in rule(8)


@pytest.mark.parametrize("n,phrase", [
    # rule 2: requirements stay with the operation that documents them
    (2, "A requirement documented for one operation (an authentication scheme, header, field, default or limit) applies "
        "only to that operation"),
    (2, "do not state it for another operation unless a passage about that operation also documents it"),
    (2, "cite each operation's requirements to that operation's own passage"),
    # rule 4: only passages about the requested integration / API / operation answer it
    (4, "A passage answers the question only when it is about the integration, API or operation the question asks about"),
    (4, "a similar header, field, signature or flow documented for a different API or integration is not an answer, not "
        "even a partial one"),
    # rule 8: name the undocumented identifier, never substitute another API's
    (8, "that it is not documented for the integration the user asked about"),
    (8, "do not offer a similar identifier or format from another API in its place"),
])
def test_accuracy_clauses(n, phrase):
    assert phrase in rule(n)


def test_accuracy_clauses_keep_the_original_rule_text():
    assert "If a detail is not in the evidence, say it is not documented. A requirement documented" in rule(2)
    assert "do not present them as the answer. A passage answers the question" in rule(4)
    assert "name it in plain text (not in code formatting), in its own sentence" not in rule(8)     # replaced sentence
    assert "Rule 8 governs wording only" in rule(8) and "Say each fact once." in rule(8)            # style bullets kept


def test_trimming_never_lists_operations_or_required_items_as_removable():
    r8 = rule(8)
    trim = r8[r8.index("Say each fact once."):r8.index("- Use plain, professional English")]
    for word in ("operation", "prerequisite", "required", "step to"):
        assert f"Leave out {word}" not in trim and f"leave out {word}" not in trim
    assert "never drop a required operation, prerequisite, field, header, parameter or step" in r8   # protection kept


@pytest.mark.parametrize("phrase", ["always be concise", "be brief", "keep answers short", "as short as possible"])
def test_no_bare_brevity_instruction(phrase):
    assert phrase not in SYSTEM_PROMPT.lower()


def test_rule_8_does_not_restate_relevance_or_status_rules():
    r8 = rule(8)
    assert "Use only passages that directly answer the question" not in r8
    for status in ("answered", "partial", "not_documented", "conflicting_sources"):
        assert f'"{status}"' not in r8
    assert "Rule 8 governs wording only" in r8 and rule(9).startswith("\n9. Citation format")   # guard stays inside rule 8


def test_rule_numbering_is_intact():
    assert [SYSTEM_PROMPT.count(f"\n{n}. ") for n in range(1, 10)] == [1] * 9 and "\n10. " not in SYSTEM_PROMPT


# ---------------- B. pipeline / validator with fake model outputs ----------------

def run(retriever, question, output):
    client = FakeClient(output)
    return Assistant(retriever=retriever, generator=OpenAIGenerator(client=client, model="fake")).answer(question), client


def label_of(retriever, question, predicate):
    ev = Assistant(retriever=retriever, generator=None).evidence(question)
    return next(e.label for e in ev if predicate(e))


def test_certificate_question_placeholder_answer_is_answered_and_valid(retriever):
    ev = Assistant(retriever=retriever, generator=None).evidence(CERT_Q)
    assert any(PLACEHOLDER in e.text for e in ev) and not any(DP_URL in e.text for e in ev)    # scoping fix intact
    lab = next(e.label for e in ev if PLACEHOLDER in e.text)
    r, client = run(retriever, CERT_Q, model_json(
        "answered", f"Call `{PLACEHOLDER}`; supply or confirm your production domain [{lab}].", [lab]))
    assert client.calls[0]["messages"][0]["content"] == SYSTEM_PROMPT
    assert r["status"] == "answered" and r["citations_valid"] is True and r["warnings"] == []


def test_certificate_question_data_platform_url_is_rejected(retriever):
    lab = label_of(retriever, CERT_Q, lambda e: PLACEHOLDER in e.text)
    r, _ = run(retriever, CERT_Q, model_json("answered", f"Call `{DP_URL}` in production [{lab}].", [lab]))
    assert r["citations_valid"] is False                              # not in the cited webhook passage
    assert any(DP_URL in w for w in r["warnings"])


def test_partial_status_and_missing_information_are_kept(retriever):
    lab = label_of(retriever, CERT_Q, lambda e: PLACEHOLDER in e.text)
    r, _ = run(retriever, CERT_Q, model_json("partial", f"Fetch keys from `{PLACEHOLDER}` [{lab}].", [lab],
                                             "The certificate rotation schedule is not documented."))
    assert r["status"] == "partial" and r["missing_information"] == "The certificate rotation schedule is not documented."
    assert r["citations_valid"] is True


def test_undocumented_value_escalation_is_valid_and_an_invented_value_is_flagged(retriever):
    q = "What is the exact X-Pismo-Signature header format for Pismo webhooks?"
    r, _ = run(retriever, q, model_json("not_documented", "The X-Pismo-Signature header format is not documented.", []))
    assert r["status"] == "not_documented" and not any("not found in the passages" in w for w in r["warnings"])
    lab = label_of(retriever, q, lambda e: e.ku_id == WEBHOOK_KU)
    r, _ = run(retriever, q, model_json("answered", f"Send `X-Pismo-Signature: v1=<hmac>` [{lab}].", [lab]))
    assert r["citations_valid"] is False and any("X-Pismo-Signature" in w for w in r["warnings"])


def test_cancel_transfer_named_operation_cannot_be_replaced(retriever):
    q = "How do I cancel a transfer?"
    ev = Assistant(retriever=retriever, generator=None).evidence(q)
    assert any(e.origin == "named_operation" and "post-transfers-cancel" in e.chunk_id for e in ev)
    older = next(e.label for e in ev if "/payments/v2/cancel" in e.text)
    r, _ = run(retriever, q, model_json("answered", f"Call `POST /payments/v2/cancel` [{older}].", [older]))
    assert r["citations_valid"] is False and r["verification"]["operation_alignment"] is False
    named = next(e.label for e in ev if e.origin == "named_operation")
    r, _ = run(retriever, q, model_json("answered", f"Call `POST /payment-methods/v2/transfers/cancel` [{named}].", [named]))
    assert r["verification"]["operation_alignment"] is True


def test_conflicting_sources_status_is_carried_through(retriever):
    lab = label_of(retriever, CERT_Q, lambda e: PLACEHOLDER in e.text)
    r, _ = run(retriever, CERT_Q, model_json("conflicting_sources", f"The sources disagree [{lab}].", [lab]))
    assert r["status"] == "conflicting_sources"


def _webhook_evidence():
    from pismo_assistant.evidence import Evidence
    return [Evidence("E1", "KU-W::a", "KU-W", "t", "s", "Webhook requests use a JWT with a kid claim and a body-hash claim.",
                     [{"path": "p", "url": "u"}], [], "retrieved", "hybrid rank")]


@pytest.mark.parametrize("answer,ok,why", [
    # rule 8's abstention wording: plain-text name in its own uncited sentence -> passes
    ("The X-Pismo-Signature header format is not documented.\nWebhook requests carry a JWT with a kid claim [E1].",
     True, "plain text, own line"),
    # the live failure 2026-10-22: requested name in code formatting plus a hypothetical example on a cited line
    ("The `X-Pismo-Signature` header format is not documented. Requests carry a JWT [E1]. It may look like "
     "`X-Pismo-Signature: <jwt>`.", False, "unsupported"),
    # code formatting alone, on an uncited line
    ("The `X-Pismo-Signature` header format is not documented.\nWebhook requests carry a JWT [E1].", False, "uncited"),
])
def test_validator_on_abstentions_about_an_undocumented_identifier(answer, ok, why):
    """Documents EXISTING validator behaviour (pismo_assistant/citations.py is not changed): the status does not exempt
    any line, so a backticked undocumented name is checked like any API detail."""
    from pismo_assistant import citations
    rep = citations.validate(answer, ["E1"], _webhook_evidence(), status="not_documented")
    assert rep.ok is ok
    if why == "unsupported":
        assert {t["token"] for t in rep.unsupported_tokens} == {"X-Pismo-Signature", "X-Pismo-Signature: <jwt>"}
    if why == "uncited":
        assert rep.uncited_claims and not rep.unsupported_tokens


@pytest.mark.parametrize("name", ["pismo_signature_header", "/v1/webhooks/signature"])
def test_known_limitation_identifier_shaped_names_fail_even_in_plain_text(name):
    """LIMITATION (documented, not fixed): names shaped like API tokens (snake_case, paths, error codes, ...) are
    detected without code formatting, so even a correct plain-text abstention about them fails validation."""
    from pismo_assistant import citations
    rep = citations.validate(f"The {name} value is not documented.\nWebhook requests carry a JWT [E1].", ["E1"],
                             _webhook_evidence(), status="not_documented")
    assert rep.ok is False and rep.uncited_claims


XSIG_Q = "What is the exact X-Pismo-Signature header format for Pismo webhooks?"


def test_supported_answer_for_the_requested_integration_passes(retriever):
    lab = label_of(retriever, XSIG_Q, lambda e: e.ku_id == WEBHOOK_KU and "JWT" in e.text)
    r, _ = run(retriever, XSIG_Q, model_json("partial", f"Pismo webhook requests carry a JWT [{lab}].", [lab]))
    assert r["citations_valid"] is True


def test_limitation_another_apis_signature_format_passes_validation(retriever):
    """LIMITATION (documented, not fixed): the bulk-file `Signature` header is in the cited passage, so presenting it as
    the webhook answer passes validation. Only prompt rules 4 and 8 guard against this substitution."""
    ev = Assistant(retriever=retriever, generator=None).evidence(XSIG_Q)
    bulk = next(e for e in ev if 'keyId="{key_id}"' in e.text)
    assert bulk.ku_id != WEBHOOK_KU and "bulk" in bulk.ku_id                       # a different API's passage
    r, _ = run(retriever, XSIG_Q, model_json(
        "partial", f'Signature header format: `keyId="{{key_id}}",signature="{{signature_base64}}"` [{bulk.label}].', [bulk.label]))
    assert r["citations_valid"] is True


def test_cross_endpoint_requirement_is_caught_only_when_cited_per_operation(retriever):
    q = "How do I cancel a transfer?"
    ev = Assistant(retriever=retriever, generator=None).evidence(q)
    payments = next(e for e in ev if e.chunk_id.endswith("::op-post-payments-v2-cancel"))
    methods = next(e for e in ev if e.chunk_id.endswith("::op-post-transfers-cancel"))
    assert "x-tenant" in payments.text and "x-tenant" not in methods.text
    both = f"Both cancel endpoints require the `x-tenant` header [{payments.label}][{methods.label}]."
    r, _ = run(retriever, q, model_json("answered", both, [payments.label, methods.label]))
    # was a documented LIMITATION (union of cited passages); citations check 6 (operation scope) now catches it
    assert r["citations_valid"] is False and r["verification"]["operation_scope"] is False
    own = f"`POST /payment-methods/v2/transfers/cancel` requires the `x-tenant` header [{methods.label}]."
    r, _ = run(retriever, q, model_json("answered", own, [methods.label]))
    assert r["citations_valid"] is False and any("x-tenant" in w for w in r["warnings"])   # rule 2's per-operation citation


def test_scoping_is_still_on():
    assert config.ENABLE_INTEGRATION_SCOPE is True
