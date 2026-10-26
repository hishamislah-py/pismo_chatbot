# Demo readiness verification: Pismo Client Implementation & Ramp-Up Assistant

Verification date: 21 October 2026. Scope: three demo-readiness requirements:

1. retrieval-to-answer integration;
2. citation correctness;
3. chunking, retrieval and evidence-assembly defects that block the six demo questions.

The narrative sections below were written after the investigation. The **Results** section, between the generated markers, is rewritten by `python -B -s -m pismo_assistant.verify_demo` on every run, from the actual test runs and pipeline executions. No API key or private environment value appears in this report or in `docs/demo_runs/`.

## 1. Scope and files inspected

**Pipeline (`pismo_assistant/`):**

| File | Role |
| --- | --- |
| `retrieval.py` | Index integrity checks; hybrid RRF (2:1) with exact-identifier promotion |
| `evidence.py` | Evidence assembly |
| `generation.py` | Prompt and OpenAI client |
| `citations.py` | Citation validation |
| `pipeline.py` | Orchestration |
| `__main__.py` | Command-line entry point |
| `tests/` | Assistant tests |

**Retrieval experiment (unchanged):** `pismo_full_corpus_retrieval_experiment/scripts/{corpus,retrievers,common}.py`, `results/chunks.jsonl` (11,026 chunks), `results/embeddings/` and `tests/`.

**KU metadata (read only):** chunk metadata derived from `pismo_knowledge_units_migration/knowledge_units/`, namely operation markers, heading paths, source references and flags.

**Trace of one question through the code:**

1. `Assistant.answer` calls `HybridRetriever.search`, which does BM25 and MiniLM scoring, RRF 2:1 fusion and exact-identifier promotion.
2. `evidence.assemble` takes the retrieved chunks, then adds explicitly identified operations, linked operations, "Events emitted" tables and lifecycle warnings.
3. `generation.build_messages` puts the **full chunk text** of every evidence item into the prompt, with its KU, section, source path and URL, flags and the reason it was included.
4. `OpenAIGenerator.generate` sends the prompt (Chat Completions, JSON mode) and parses the reply strictly.
5. `citations.validate` checks the citations, and `sources_for` builds the citation list.
6. The result is returned.

## 2. Defects found and root causes

| # | Defect, as observed | Root cause |
| --- | --- | --- |
| D1 | **Q4**, "Which event is generated when I create a transfer?": the live answer named the event of the **Create transfer schedule** operation (`POST /v1/transfers`), not of `post-transfers` (captured in `docs/demo_runs/before_live.json`) | **Chunk construction:** the `post-transfers` contract is split into 16 chunks. The main chunk is 3,588 characters, mostly field tables, and the "Events emitted" table sits in a 2,987-character chunk of error examples. Best ranks: BM25 103, semantic 1,419, fused 140. **Operation matching:** the question contains the operation's exact spec summary ("create a transfer" = "Create transfer"), but evidence assembly recognised operations only by literal operationId. **Evidence assembly:** the two "Events emitted" slots went to the first operations in rank order, both transfer-schedule operations |
| D2 | Q4's wrong answer was accepted with `citations_valid=True` | **Citation checker scope:** it checked only that cited labels existed with metadata, and that API tokens occurred somewhere in the *union* of all cited passages. It had no check that the answer addressed the operation the question identified |
| D3 | Q2's live answer included an uncited, unfenced JSON example | The checker treated lines as independent and had no rule for code examples. The prompt did not require examples to be fenced and cited |
| D4 | A path followed by a full stop (`/…/unblock.`) was flagged as unsupported (found in the earlier live run) | The token regex included the sentence's full stop in the path. Fixed in the previous session; its regression test is kept |
| D7 | In the third post-fix live run, **Q6** failed `claim_token_support` because the English word "step-by-step" was treated as an API identifier | The identifier pattern accepted any word with two or more hyphens. A bare hyphenated word is now checked only when it contains a digit (event slugs) or is a known spec operationId; the pipeline passes the operation index. Regression test added |
| D6 | In the second post-fix live run, **Q1** failed `historical_marking` on "WEAM0029 *was* an error code that was *originally* returned…" | The history word list recognised only some past-tense phrasings ("was used/changed/added/updated"). It now also accepts was, were, had, originally and formerly. The exact live sentence is a regression test |
| D5 | In the first post-fix live run, **Q2** failed `claim_token_support`. The answer's verbatim example block (copied from E4) had no citation on its introducing line; the model cited E4 on the line immediately **after** the block | The new claim-unit rule was stricter than the evidence: it accepted citations only on the introducing line. A code block without its own citation may now use the citations of the line right after it, and its tokens are still checked against those passages. Positive and negative regression tests were added |

Q1, Q2, Q3, Q5 and Q6 retrieved the correct evidence before any change, so no retrieval change was needed for them. Q6 abstained correctly even before the fix, but the accounts go-live operation is its top-ranked near-match (see limitations).

## 3. Changes made

| File | Change | Why it addresses the root cause |
| --- | --- | --- |
| `pismo_assistant/evidence.py` | <ul><li>`OperationIndex` now parses each operation's method, path and summary from its heading (981 of 981 operations)</li><li>New `summary_operation_ids` and `matched_operations`: an operation is identified when its summary of two or more words appears as a whole phrase in the question (ignoring case, punctuation and articles); only the longest phrases are kept, and a phrase shared by more than 2 operations is skipped as ambiguous</li><li>Explicitly identified operations now get first claim on the "Events emitted" slots</li></ul> | Deterministic operation matching fixes D1 without changing chunking, ranking or the index. It is additive: retrieved chunks keep their order and are never dropped |
| `pismo_assistant/config.py` | Adds `MAX_SUMMARY_OPERATIONS = 2` | Bounds the new step |
| `pismo_assistant/citations.py` | <ul><li>**Claim-level** token support: each claim unit (a line or bullet, plus any fenced or unfenced code block it introduces) must cite passages containing its own API tokens</li><li>Token types: paths, operationIds and event slugs, snake_case fields, error codes and back-ticked text</li><li>Claims with API details but no citation are flagged</li><li>Grouped labels such as `[E1, E2]` are parsed</li><li>**Operation alignment:** an answer that names other paths but never the operation the question identified is flagged</li><li>**Historical marking:** a claim supported only by changelog passages must say it is removed, historical or changed</li><li>`checks()` reports each check separately, and `semantic_support_verified` is always `False`</li><li>A code block without its own citation may use the citations of the line right after it (D5)</li></ul> | Fixes D2, D3 and D5. The captured pre-fix Q4 answer is now rejected (regression test) |
| `pismo_assistant/pipeline.py` | Computes the matched operations, passes them and the status to the validator, and returns `matched_operations`, a `verification` dict and one warning per failed check | Makes each check visible to callers and the CLI |
| `pismo_assistant/generation.py` | Two prompt rules added: rule 3, examples go in fenced code blocks copied verbatim with a cited introducing line; rule 6, answer about the operation the question names and do not substitute a similarly named one | Reduces D1 and D3 at generation time. The validator still enforces them |
| `pismo_assistant/tests/test_questions.py` | The former strict-xfail Q4 test is now a passing regression test. Added: longest-phrase matching, the short webhook question, the PCI demo phrasing, and the pre-fix Q4 answer being rejected | Regression coverage for D1 and D2 |
| `pismo_assistant/tests/test_edge_cases.py` | Added: claim-level support, uncited claims, event-slug and field tokens, operation alignment, historical marking, grouped labels with an unfenced JSON example, explicitly identified operations getting events first, and semantic support never being claimed. One assertion updated for the new token record format | Regression coverage for D2 and D3 |
| `pismo_assistant/verify_demo.py` (new) | Runs both test suites (counts from JUnit XML), runs the six questions through the real pipeline (live if a key is configured, otherwise mocked and labelled), checks fixed expectations, writes `docs/demo_runs/verification_results.json`, refreshes the Results section below, and prints the terminal summary | Results come from execution, not hand-typed counts |
| `pismo_assistant/README.md` | Adds the verify command and updates the limitations | The run instructions were incomplete |

**Unchanged:** the approved KUs, the chunk index, the embeddings, the benchmark and its labels, the retrieval strategy, and the experiment code. No dependencies were installed.

## 4. What the citation checker does and does not prove

| Check | Deterministic? | Meaning |
| --- | --- | --- |
| `source_mapping` | yes | Each cited `[E#]` exists and maps to a KU ID, title, section, source path (the file exists in `kb_corpus`) and an `https://` URL |
| `claim_token_support` | yes | Every API-like token in a claim appears verbatim in a passage cited *by that claim* |
| `operation_alignment` | yes | When the question identified an operation, the answer names it and not only other operations |
| `historical_marking` | yes | Claims backed only by changelogs say the behaviour is historical, removed or changed |
| `semantic_support_verified` | **no, always `False`** | Whether a passage actually *supports the meaning* of the claim is **not** verified automatically |

As a substitute for the missing semantic check, I (the same model that built the pipeline) reviewed the final live answers by hand: about 20 claims across Q1–Q6, each compared with the text of its cited passage. Every claim checked was found in the passage it cites. This was a spot-check by the same model, not an independent review.

## 5. Live versus mocked

The Results section states the mode of the run that produced it. With `OPENAI_API_KEY` in the project `.env`, the six questions run **live** against the configured model. Otherwise they run **mocked**: a fixed `not_documented` reply, with the answer checks marked "not judged". The automated test suites always use fake clients and never call the network.

## 6. Known limitations and deferred work

- **No answerability judge.** For Q6, abstention depends on the model following prompt rule 4, because the accounts go-live operation is the top-ranked near-match. `test_pci_go_live_limitation_model_can_answer_from_near_match` shows that a wrong answer based on it would pass every deterministic check.
- **Semantic claim support is not verified** automatically (see §4).
- **Summary matching is phrase-exact.** Paraphrases ("send money to another account") do not identify `post-transfers`, so those questions still depend on retrieval rank. It can also match short, generic summaries ("get account balance" matches "Get account"). That only adds evidence; nothing is removed.
- **Lower-ranked retrieved passages can be off-topic**, for example the loan "topics covered" chunks for WEAM0029. Retrieval was deliberately not changed.
- **Live answers vary between runs.** The verification records one run; rerun `verify_demo` before a demo.
- **The deterministic checker is heuristic and fails closed.** Each of the three post-fix live runs exposed a new false positive (D5, D6, D7), and each was fixed with a regression test. New phrasings may still be flagged; a flagged answer is shown with warnings and `citations_valid=false`, never silently accepted. Across all captured live answers (the pre-fix run and the final run), the only one rejected is the pre-fix wrong Q4 answer.

## 7. Reproduce

```powershell
cd C:\Users\artlptp263user\Downloads\pismo_claude_code_handoff
$env:HF_HUB_OFFLINE='1'; $env:TRANSFORMERS_OFFLINE='1'
python -B -s -m pismo_assistant.verify_demo                     # tests + six questions + terminal summary + this report
python -B -s -m pismo_assistant.verify_demo --mock              # same without OpenAI calls
python -B -s -m pytest pismo_assistant/tests -q -p no:cacheprovider
cd pismo_full_corpus_retrieval_experiment; python -B -s -m pytest tests -q -p no:cacheprovider; cd ..
python -B -s -m pismo_assistant "Which event is generated when I create a transfer?"
```

The OpenAI key is read from `.env` in the project root (`OPENAI_API_KEY`, `OPENAI_MODEL`). Do not pass it on the command line.

## 7a. Final citation verification pass (21 October 2026, time-boxed)

This pass used the saved final live run (`docs/demo_runs/verification_results.json`: gpt-5-mini, generated 2026-10-21 12:21:18). No new OpenAI call was made, and no code was changed.

| Check | Method | Result |
| --- | --- | --- |
| 1. Citation mapping | Each of the **20** citations in the six answers was compared with the evidence item supplied to the model (label → chunk), with the chunk index (KU ID, title, section from the heading path, source paths), and with the KB release's independent `internal/provenance/source_map.csv`. **53** source references were checked against the source map URL, the source map `corpus_sha256`, and the SHA-256 of the file on disk | **20/20 correct, 0 mismatches.** The first attempt reported 20 mismatches because my check script omitted the source map's `kb_corpus/` path prefix. That was a script error, not a product defect, and was corrected before the result above |
| 2. Claim support (manual) | Every claim unit in the six answers was printed with the exact text of the passage(s) it cites, and checked by reading, with priority on paths, operationIds, required fields, event names, error codes, historical claims and examples | **52 targeted checks, 52 supported, 0 unsupported.** See below |
| 3. Q4 wrong-answer regression | The captured pre-fix live answer (`before_live.json`) was replayed through the current checker, and `test_q4_baseline_wrong_operation_answer_is_rejected` was run | Rejected: `operation_mismatch` (expected `POST /payment-methods/v2/transfers`, answer names `/v1/transfers`). Test passed |
| 4. PCI negative | Saved Q6 answer inspected; PCI tests run | Status `not_documented`. The first claim says the go-live operation "is for accounts … and does not document a PCI card go-live flow" [E1]. Accounts go-live is presented only as related context. Tests passed |

**Claims inspected, with the supporting passage text found:**

- **Q1:**
  - "was an error code … rejected earmark payments with back value dates" → E1 and E2: "These codes were originally used / previously returned when … earmark payments with back value dates were rejected".
  - "removed from Post payment, Post payment (Pismo account ID), Post multi-leg payment … supported by default" → the E1 endpoint list and E2's "now supported by default".
- **Q2:**
  - The path → E9 heading `POST /payments/v1/payments/hold-funds/unblock`.
  - Required `tracking_id`, `account_id`, `amount`, `processing_code`; optional `description`, the skip flags and `metadata` → E9's `HoldFundsRequest` table (Required column).
  - "moved back to `available_credit_limit`" → E2: "The amount released is fully moved to the `available_credit_limit` balance".
  - The JSON example → **byte-equivalent (whitespace-normalised) to the unblock example in E4**; E4 also holds a *block* example with the same account ID, and the right one was used.
  - The events → E9 description: "generates Authorization created and Account balance changed".
  - `GET /v1/accounts/{accountId}/limits` and `held_funds` → the E7 heading and field table, plus E5: "checking the field `held_funds` in the response of List account limits".
  - The Control Center "Release held funds" action, debit accounts only → E1.
- **Q3 and Q4:** `POST /payment-methods/v2/transfers` "Create transfer" → E7 heading. "Platform authorization created" → E7: "This endpoint generates a Platform authorization created event". The slug `platform-authorization-platform-authorization-1` → E8 "Events emitted" table.
- **Q5:** JWTs, the key pair, the body hash → E1. The `kid` claim, the cache, `/v1/certs` (Sandbox and Production), "5 requests per second", `max-age=23638`, deny and notify the security team, SHA256 then base64 compared with `body-hash`, and the JWS/RSA example reference → E4. Both code blocks are verbatim from E4.
- **Q6:**
  - Accounts Go-live, `MIGRATED`, "Account go-live completed" → E1 (and the E7 events table).
  - The enum `["ACCOUNT", "PRE_GO_LIVE"]` and "`PCI_CARD` type is deprecated" → E1.
  - "Start migration of non-PCI cards" → E3; the card migration events → E8.
  - "PCI endpoint, use the https://gw-pci.pismolabs.io environment" → E2.

**Defects found:** none in the citation mapping or the checker. No code was changed in this pass.

**Limitations recorded in this pass:**

- **Manual review, not independent.** Semantic support was verified **by manual inspection only**, by the model that built the pipeline. The automated checker still does not verify meaning; `semantic_support_verified` stays `False`.
- **The checker's granularity is one line.** When a line holds two sentences with different citations (Q4: "... [E7] ... [E8]"), their tokens are checked against both passages together. All Q4 tokens were confirmed manually against the right passage.
- **One run, one model.** The inspection covers this saved run only. Other runs can phrase claims differently, and only the deterministic checks apply to them.

**Assessment for the demo:** acceptable. Every citation in the final run maps to the correct KU, section, source file and URL. Every important claim inspected is supported by the passage it cites. The known wrong-operation failure is caught automatically. The PCI question abstains. The residual risk is a new live phrasing that the deterministic checks can't judge semantically; such an answer would at worst be shown with warnings, not silently passed as verified.

## 8. Results

<!-- BEGIN GENERATED: verify_demo.py -->
_Generated 2026-10-21 12:21:18 by `python -B -s -m pismo_assistant.verify_demo` - generation was **LIVE** (model gpt-5-mini)._

### Requirement status

| Requirement | Status |
| --- | --- |
| 1. Retrieval-to-answer integration | **verified** |
| 2. Citation correctness | **partially verified** |
| 3. Demo-blocking chunking/retrieval/evidence defects | **verified** |

### Test runs

| Suite | Tests | Passed | Failed | Errors | Skipped |
| --- | ---: | ---: | ---: | ---: | ---: |
| `pismo_assistant/tests` | 51 | 51 | 0 | 0 | 0 |
| `pismo_full_corpus_retrieval_experiment/tests` | 38 | 38 | 0 | 0 | 0 |

### Demo questions

#### Q1 - Exact error lookup: "What does WEAM0029 mean?"

- Status: `answered` (live, 9.9 s); expected evidence (KU-CHG-2-october-2026 passage containing WEAM0029 ranked 1-2): **yes**; expected answer (answered; explains WEAM0029 and marks it as removed/historical): **yes**
- Complete passage text in prompt: **yes** (14476 chars)
- Matched operations: none
- Citation checks: valid=True; source_mapping=True, claim_token_support=True, operation_alignment=True, historical_marking=True, semantic_support_verified=False
- Warnings: none

| Label | Origin | Chunk | KU title |
| --- | --- | --- | --- |
| E1 | retrieved | `KU-CHG-2-october-2026::src-2-october-2026.change-record-source-content-verbatim.2-october-2026::p08` | Changelog: 2 October 2026 |
| E2 | retrieved | `KU-CHG-2-october-2026::src-2-october-2026.change-record-source-content-verbatim.2-october-2026::p09` | Changelog: 2 October 2026 |
| E3 | retrieved | `KU-LEND-simulate-loans::topics-covered` | Simulate loans |
| E4 | retrieved | `KU-LEND-book-a-loan::topics-covered` | Book loans |
| E5 | retrieved | `KU-CARD-zero-balance-integration::src-zero-balance-integration.single-and-dual-message-system-considera` | Zero balance integration and anti-fraud validations |
| E6 | retrieved | `KU-LEND-loan-statuses-overview::src-loan-statuses-overview.loan-statuses-overview` | Loan statuses overview |

Cited: E1 -> KU-CHG-2-october-2026 / Change record (source content, verbatim) > 2 October 2026 (changelog/2-october-2026.md), E2 -> KU-CHG-2-october-2026 / Change record (source content, verbatim) > 2 October 2026 (changelog/2-october-2026.md)

<details><summary>Answer</summary>

WEAM0029 was an error code returned when the Pismo platform rejected earmark payments that had back value dates. [E1][E2]

This error code was removed from the Post payment, Post payment (Pismo account ID), and Post multi-leg payment endpoints because back‑dated earmark payments are now supported by default. [E1][E2]

</details>

#### Q2 - Documented workflow: "How do I release funds that I previously held on an account?"

- Status: `answered` (live, 17.7 s); expected evidence (KU-PAY-hold-funds guide + the post-payments-v1-hold-funds-unblock operation): **yes**; expected answer (answered; names POST /payments/v1/payments/hold-funds/unblock): **yes**
- Complete passage text in prompt: **yes** (39992 chars)
- Matched operations: none
- Citation checks: valid=True; source_mapping=True, claim_token_support=True, operation_alignment=True, historical_marking=True, semantic_support_verified=False
- Warnings: none

| Label | Origin | Chunk | KU title |
| --- | --- | --- | --- |
| E1 | retrieved | `KU-CC-accounts::src-account-actions.hold-funds` | Control Center accounts: overview, management, actions and configurations |
| E2 | retrieved | `KU-PAY-hold-funds::src-hold-funds.hold-funds` | Hold funds |
| E3 | retrieved | `KU-PAY-hold-funds::src-hold-funds.processing-codes-and-transaction-types` | Hold funds |
| E4 | retrieved | `KU-PAY-hold-funds::src-hold-funds.events.account-balance-changed` | Hold funds |
| E5 | retrieved | `KU-PAY-hold-funds::src-hold-funds.example-of-hold-funds-actions.transfer-held-funds` | Hold funds |
| E6 | retrieved | `KU-API-banking-transaction-banking--restricted-funds::op-patch-corporate-v2-restricted-funds` | API reference: Banking - Transaction banking — Restricted funds |
| E7 | linked_operation | `KU-API-core-platform-ledger--account-limits::op-get-v1-account-limit` | API reference: Core platform - Ledger — Account limits |
| E8 | linked_operation | `KU-API-core-platform-payment-methods--hold-funds::op-post-payments-v1-hold-funds-block` | API reference: Core platform - Payment methods — Hold funds |
| E9 | linked_operation | `KU-API-core-platform-payment-methods--hold-funds::op-post-payments-v1-hold-funds-unblock` | API reference: Core platform - Payment methods — Hold funds |
| E10 | operation_events | `KU-API-banking-transaction-banking--restricted-funds::op-patch-corporate-v2-restricted-funds.response-400` | API reference: Banking - Transaction banking — Restricted funds |
| E11 | operation_events | `KU-API-core-platform-payment-methods--hold-funds::op-post-payments-v1-hold-funds-block.response-201` | API reference: Core platform - Payment methods — Hold funds |

Cited: E9 -> KU-API-core-platform-payment-methods--hold-funds / Operation contracts > `POST /payments/v1/payments/hold-funds/unblock` — Unblock held amount (api-specs/Core_platform_-_Payment_methods.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E2 -> KU-PAY-hold-funds / Current implementation guidance (source content, verbatim) > Source 1: `docs/core-platform/hold-funds.md` > Hold funds (docs/core-platform/hold-funds.md), E4 -> KU-PAY-hold-funds / Current implementation guidance (source content, verbatim) > Source 1: `docs/core-platform/hold-funds.md` > Events > Account balance changed (docs/core-platform/hold-funds.md), E7 -> KU-API-core-platform-ledger--account-limits / Operation contracts > `GET /v1/accounts/{accountId}/limits` — List account limits (api-specs/Core_platform_-_Ledger.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E5 -> KU-PAY-hold-funds / Current implementation guidance (source content, verbatim) > Source 1: `docs/core-platform/hold-funds.md` > Example of hold funds actions > Transfer held funds (docs/core-platform/hold-funds.md), E1 -> KU-CC-accounts / Current implementation guidance (source content, verbatim) > Source 3: `docs/control-center/account-actions.md` > Hold funds (docs/control-center/account-actions.md)

<details><summary>Answer</summary>

Call the Unblock held amount endpoint to release held funds: POST /payments/v1/payments/hold-funds/unblock. [E9]

This operation (Unblock held amount) releases the total or a partial amount from held funds back to the available_credit_limit. [E2]

Required request fields include tracking_id, account_id, amount and processing_code; description is optional and there are optional flags like skip_balance_validation and skip_status_account_validation and an optional metadata object. [E9]

Example request (from the docs): [E4]
```json
{  
    "account_id": 111507785,  
    "tracking_id":"c852a2b1-9ad0-5a57-9d1e-a512f1ae7df8",  
    "amount":30.22,  
    "processing_code":283506,  
    "description":"Legal unblock",  
    "metadata":{  
        "message":"Unblock requested"  
    }  
}
```

The Unblock endpoint generates an Authorization created event and an Account balance changed event when the authorization completes. [E9]

To check the current held_funds amount before or after the unblock call, query the account limits endpoint GET /v1/accounts/{accountId}/limits and inspect the held_funds field. [E7] [E5]

In the Control Center UI the same action is called "Release held funds" and is available for debit accounts only. [E1]


</details>

#### Q3 - Operation-to-event (operationId): "Which event does post-transfers emit?"

- Status: `answered` (live, 5.4 s); expected evidence (post-transfers operation + its 'Events emitted' table): **yes**; expected answer (answered; names platform-authorization-platform-authorization-1): **yes**
- Complete passage text in prompt: **yes** (11831 chars)
- Matched operations: post-transfers via operationId
- Citation checks: valid=True; source_mapping=True, claim_token_support=True, operation_alignment=True, historical_marking=True, semantic_support_verified=False
- Warnings: none

| Label | Origin | Chunk | KU title |
| --- | --- | --- | --- |
| E1 | retrieved | `KU-PAY-payment-configurations::events` | Payment methods configurations overview |
| E2 | retrieved | `KU-EVT-catalogue-migration::operations-that-emit-these-events::p01` | Event catalogue: migration |
| E3 | retrieved | `KU-PAY-transfers-make-and-cancel::events` | Transfers: making and cancelling transfers |
| E4 | retrieved | `KU-EVT-catalogue-account::operations-that-emit-these-events::p01` | Event catalogue: account |
| E5 | retrieved | `KU-EVT-catalogue-other-domains::operations-that-emit-these-events::p01` | Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement) |
| E6 | retrieved | `KU-EVT-catalogue-balance::operations-that-emit-these-events::p01` | Event catalogue: balance |
| E7 | named_operation | `KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers` | API reference: Core platform - Payment methods — Payment methods (part 2 of 3) |
| E8 | operation_events | `KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers.response-400` | API reference: Core platform - Payment methods — Payment methods (part 2 of 3) |

Cited: E8 -> KU-API-core-platform-payment-methods--payment-methods-part-02 / Operation contracts > `POST /payment-methods/v2/transfers` — Create transfer > Responses > Response 400 (api-specs/Core_platform_-_Payment_methods.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E7 -> KU-API-core-platform-payment-methods--payment-methods-part-02 / Operation contracts > `POST /payment-methods/v2/transfers` — Create transfer (api-specs/Core_platform_-_Payment_methods.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv)

<details><summary>Answer</summary>

The post-transfers operation emits the event with slug `platform-authorization-platform-authorization-1` [E8]. This is the "Platform authorization created" event [E7].

</details>

#### Q4 - Operation-to-event (natural language): "Which event is generated when I create a transfer?"

- Status: `answered` (live, 5.6 s); expected evidence (post-transfers operation (Create transfer) + its 'Events emitted' table): **yes**; expected answer (names platform-authorization-platform-authorization-1 for POST /payment-methods/v2/transfers, not the transfer-schedule operation): **yes**
- Complete passage text in prompt: **yes** (29326 chars)
- Matched operations: post-transfers via summary
- Citation checks: valid=True; source_mapping=True, claim_token_support=True, operation_alignment=True, historical_marking=True, semantic_support_verified=False
- Warnings: none

| Label | Origin | Chunk | KU title |
| --- | --- | --- | --- |
| E1 | retrieved | `KU-API-core-platform-payment-scheduler-beta--schedules::op-post-v1-create-transfer-schedules` | API reference: Core platform - Payment scheduler — Schedules |
| E2 | retrieved | `KU-PAY-payment-scheduler::events` | Payment scheduler |
| E3 | retrieved | `KU-CORE-accounting-events::src-accounting-events.accounting-events` | Accounting events |
| E4 | retrieved | `KU-PAY-transfers-make-and-cancel::src-make-transfer.how-to-make-transfer` | Transfers: making and cancelling transfers |
| E5 | retrieved | `KU-CORE-accounting-events::src-accounting-events.debit-full-balance` | Accounting events |
| E6 | retrieved | `KU-API-instant-payments-pix-payments--scheduled-transfers::op-post-schedule` | API reference: Instant payments - Pix payments — Scheduled transfers |
| E7 | named_operation | `KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers` | API reference: Core platform - Payment methods — Payment methods (part 2 of 3) |
| E8 | operation_events | `KU-API-core-platform-payment-methods--payment-methods-part-02::op-post-transfers.response-400` | API reference: Core platform - Payment methods — Payment methods (part 2 of 3) |
| E9 | operation_events | `KU-API-core-platform-payment-scheduler-beta--schedules::op-post-v1-create-transfer-schedules.response-200` | API reference: Core platform - Payment scheduler — Schedules |

Cited: E7 -> KU-API-core-platform-payment-methods--payment-methods-part-02 / Operation contracts > `POST /payment-methods/v2/transfers` — Create transfer (api-specs/Core_platform_-_Payment_methods.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E8 -> KU-API-core-platform-payment-methods--payment-methods-part-02 / Operation contracts > `POST /payment-methods/v2/transfers` — Create transfer > Responses > Response 400 (api-specs/Core_platform_-_Payment_methods.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv)

<details><summary>Answer</summary>

The Create transfer (POST /payment-methods/v2/transfers) endpoint generates a "Platform authorization created" event. [E7] The event slug for this event is `platform-authorization-platform-authorization-1`. [E8]

</details>

#### Q5 - Webhook troubleshooting: "How do I verify webhook requests?"

- Status: `answered` (live, 18.6 s); expected evidence (KU-EVT-verifying-webhook-requests ranked 1): **yes**; expected answer (answered; JWT verification steps): **yes**
- Complete passage text in prompt: **yes** (9085 chars)
- Matched operations: none
- Citation checks: valid=True; source_mapping=True, claim_token_support=True, operation_alignment=True, historical_marking=True, semantic_support_verified=False
- Warnings: none

| Label | Origin | Chunk | KU title |
| --- | --- | --- | --- |
| E1 | retrieved | `KU-EVT-verifying-webhook-requests::src-verifying-webhook-requests.verifying-webhook-requests` | Verifying webhook requests |
| E2 | retrieved | `KU-EVT-verifying-webhook-requests::intro` | Verifying webhook requests |
| E3 | retrieved | `KU-EVT-verifying-webhook-requests::topics-covered` | Verifying webhook requests |
| E4 | retrieved | `KU-EVT-verifying-webhook-requests::src-verifying-webhook-requests.verifying-webhook-requests.retrieving-a-list-of-public-keys` | Verifying webhook requests |
| E5 | retrieved | `KU-EVT-verifying-webhook-requests::lifecycle-status` | Verifying webhook requests |
| E6 | retrieved | `KU-EVT-verifying-webhook-requests::source-references` | Verifying webhook requests |

Cited: E1 -> KU-EVT-verifying-webhook-requests / Current implementation guidance (source content, verbatim) > Source 1: `docs/get-started/verifying-webhook-requests.md` > Verifying webhook requests (docs/get-started/verifying-webhook-requests.md), E4 -> KU-EVT-verifying-webhook-requests / Current implementation guidance (source content, verbatim) > Source 1: `docs/get-started/verifying-webhook-requests.md` > Verifying webhook requests > Retrieving a list of public keys (docs/get-started/verifying-webhook-requests.md)

<details><summary>Answer</summary>

High-level summary

- Webhook requests use JSON Web Tokens (JWTs). [E1]
- Each JWT is signed with a public/private key pair; Pismo keeps the private key and shares the public key with clients. [E1]
- Each JWT includes a body-hash claim you can use to verify payload integrity. [E1]

Verification steps

1. Cache / retrieve public keys
   - Check your cache for the public key named in the JWT (kid). [E4]
   - If you don't have the key, call the public keys endpoint to retrieve the list of Pismo public keys. [E4]
   - Example public-keys request: [E4]
```shell Public key request
# These are endpoints where you can get Pismo's public keys:
Sandbox: curl -i https://sandbox.pismolabs.io/v1/certs
Production: curl -i https://<Production Domain>/v1/certs
```
   - Do not call the public keys endpoint for every webhook request; it has a rate limit of 5 requests per second. [E4]
   - Only call the public keys endpoint when you don't yet have a list (e.g., first login) or when your cached list has expired per the cache-control guidance. [E4]
   - The Pismo platform uses the Cache-Control header to indicate when to renew keys; for example: [E4]
```
cache-control: public, max-age=23638, must-revalidate, no-transform
```

2. Verify the JWT signature
   - Parse the JWT and read the kid claim to determine which public key was used. [E4]
   - If the key is present in your cache, use it to verify the JWT signature. [E4]
   - If the key is not present, retrieve the public keys as described above and then verify the signature. [E4]
   - Pismo recommends using one of the JWT/JWS libraries listed in the "Parsing the JWT" section to verify signatures and gives an example reference for JWS with RSA. [E4]
   - If the key names match but the signature does not, deny the request and notify your security team. [E4]

3. Verify message integrity (body-hash)
   - Take the full request payload Pismo sent. [E4]
   - Compute a SHA256 hash of that payload and encode the resulting hash in base64. [E4]
   - Compare that computed base64-encoded SHA256 value to the JWT claim body-hash. [E4]
   - If they match, the payload integrity check is successful and the request is verified. [E4]

Notes

- The documentation describes the overall process, caching/renewal of public keys, how to verify signatures, and how to check the body-hash integrity. [E1] [E4]


</details>

#### Q6 - Negative (not documented): "How do I perform PCI card go-live?"

- Status: `not_documented` (live, 30.5 s); expected evidence (no evidence documents a PCI card go-live (accounts go-live is only a near-match)): **yes**; expected answer (not_documented/partial; does not present accounts go-live as the procedure): **yes**
- Complete passage text in prompt: **yes** (19755 chars)
- Matched operations: none
- Citation checks: valid=True; source_mapping=True, claim_token_support=True, operation_alignment=True, historical_marking=True, semantic_support_verified=False
- Warnings: none

| Label | Origin | Chunk | KU title |
| --- | --- | --- | --- |
| E1 | retrieved | `KU-API-migrations--account-migration::op-postgolivev1` | API reference: Migrations — Account migration |
| E2 | retrieved | `KU-API-card-issuing-cards--pci::op-get-v2-card-info` | API reference: Card issuing - Cards — PCI |
| E3 | retrieved | `KU-API-migrations--card-migration::op-postcardsv1` | API reference: Migrations — Card migration |
| E4 | retrieved | `KU-API-card-issuing-cards--pci::intro` | API reference: Card issuing - Cards — PCI |
| E5 | retrieved | `KU-CARD-cards-overview-1::src-cards-overview-1.cards-management` | Cards management |
| E6 | retrieved | `KU-API-migrations--account-migration::op-postpregolivev1` | API reference: Migrations — Account migration |
| E7 | operation_events | `KU-API-migrations--account-migration::op-postgolivev1.events-emitted-api-reference-data-endpoi` | API reference: Migrations — Account migration |
| E8 | operation_events | `KU-API-migrations--card-migration::op-postcardsv1.responses` | API reference: Migrations — Card migration |

Cited: E1 -> KU-API-migrations--account-migration / Operation contracts > `POST /v1/migrations/go-live` — Migrate accounts Go-live (api-specs/Migrations.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E7 -> KU-API-migrations--account-migration / Operation contracts > `POST /v1/migrations/go-live` — Migrate accounts Go-live > Events emitted (api-reference-data/endpoint_event_map.csv) (api-specs/Migrations.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E3 -> KU-API-migrations--card-migration / Operation contracts > `POST /v1/migrations/cards` — Migrate cards (api-specs/Migrations.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E8 -> KU-API-migrations--card-migration / Operation contracts > `POST /v1/migrations/cards` — Migrate cards > Responses (api-specs/Migrations.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E2 -> KU-API-card-issuing-cards--pci / Operation contracts > `GET /pcicards/v2/pcicards/info/{cardId}` — Get card PCI information (api-specs/Card_issuing_-_Cards.yaml; api-reference-data/operations_catalog.csv; api-reference-data/request_response_examples.csv; api-reference-data/endpoint_event_map.csv), E5 -> KU-CARD-cards-overview-1 / Current implementation guidance (source content, verbatim) > Source 1: `docs/card-issuing/cards-overview-1.md` > Cards management (docs/card-issuing/cards-overview-1.md)

<details><summary>Answer</summary>

No operation is documented that explicitly performs a "PCI card go-live". The migrations Go-live operation described in the API is for accounts (POST /v1/migrations/go-live) and does not document a PCI card go-live flow [E1].

The POST /v1/migrations/go-live endpoint marks migrated accounts as MIGRATED and generates an "Account go-live completed" event for each account in the specified phase ID [E1][E7].

That Go-live operation accepts a migration.type field whose documented enum values are "ACCOUNT" and "PRE_GO_LIVE", and the specification explicitly notes that the "PCI_CARD" type is deprecated [E1].

Card migration itself is handled by POST /v1/migrations/cards, but the documentation for that endpoint states it starts migration of non-PCI cards (i.e., it is not for PCI cards) and it emits card-migration events [E3][E8].

The platform does include PCI-designated endpoints (for example, PCI card data retrieval must be called in the gw-pci environment), but those passages do not describe a PCI card go-live procedure [E2][E5].

</details>

### Q4 before/after (captured live before the fix: `docs/demo_runs/before_live.json`)

- Before: status `answered`, citations_valid `True`, post-transfers in evidence: **False**
- Before evidence: `E1 retrieved KU-API-core-platform-payment-scheduler-beta--schedules::op-post-v1-create-transfer-schedules`; `E2 retrieved KU-PAY-payment-scheduler::events`; `E3 retrieved KU-CORE-accounting-events::src-accounting-events.accounting-events`; `E4 retrieved KU-PAY-transfers-make-and-cancel::src-make-transfer.how-to-make-transfer`; `E5 retrieved KU-CORE-accounting-events::src-accounting-events.debit-full-balance`; `E6 retrieved KU-API-instant-payments-pix-payments--scheduled-transfers::op-post-schedule`; `E7 operation_events KU-API-core-platform-payment-scheduler-beta--schedules::op-post-v1-create-transfer-schedules.response-200`; `E8 operation_events KU-API-instant-payments-pix-payments--scheduled-transfers::op-post-schedule.events-emitted-api-reference-data-endpoi`
- Before answer: When you create a transfer schedule (POST /v1/transfers), the platform generates the "Scheduled payment created or modified" event with the `status` field set to `CREATED` [E1]. This corresponds to the event slug `scheduler-payments-scheduled-payments-1` in the events mapping for that operation [E2][E7].

<!-- END GENERATED: verify_demo.py -->
