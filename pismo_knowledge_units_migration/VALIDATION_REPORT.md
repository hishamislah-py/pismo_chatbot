# Validation report

**Status: migration complete.** 503 of 503 sources are migrated and accounted for, and none are excluded. All 22 deterministic checks pass with 0 failures, and all 29 retrieval tests pass.

This report keeps two things apart: file-level integrity (sections 3–4) and content-level validation (sections 5–6). Matching counts and hashes do not prove that the meaning was carried over intact; section 8 sets out what these results do not show.

Machine-readable results are in:

- `work/validation_results.json` and `work/validation_results_pilot.json`;
- `work/retrieval_test_results.json`;
- `work/issues_data.json`.

## 1. Source inventory

| Item | Value |
| --- | --- |
| Corpus | `pismo_kb_release_r2/kb_corpus/` |
| Files | 503 |
| Fingerprint P | `7080b549e8160a2bc555ae1c0646b4d9a807414cd12dbd1943e712f5031f0e62` |
| Matches the accepted value | yes |
| Allowlist and source map | both equal the corpus; 0 hash mismatches |

Breakdown by type:

| Type | Files |
| --- | --- |
| guide Markdown (`docs/`) | 404 |
| changelog Markdown | 22 |
| OpenAPI YAML | 71 |
| spec repository README | 1 |
| reference CSV | 5 |

The OpenAPI files define 999 operations with 981 distinct operationIds; 18 operationIds are used twice (SC-06).

The corpus was re-hashed at the start and end of every validation run. It is unchanged. Nothing in r1 and no candidate material was used.

## 2. Knowledge units produced

**623 KUs**, 17.66 MB in total.

| Type | Count |
| --- | --- |
| workflow_guide | 284 (73 of them combine more than one guide) |
| api_reference | 266 |
| error_catalogue | 27 |
| event_catalogue | 23 |
| changelog_history | 22 |
| lifecycle_reference | 1 |

| Category | Count | Category | Count |
| --- | --- | --- | --- |
| api_reference | 266 | banking | 21 |
| events_and_webhooks | 79 | getting_started | 9 |
| card_issuing | 55 | lending | 9 |
| core_platform | 32 | reports_and_data_files | 7 |
| errors_and_troubleshooting | 30 | api_lifecycle | 5 |
| transfers_and_payments | 26 | seller_management | 5 |
| revolving_credit | 23 | rate_limits_and_support | 4 |
| changelog_history | 22 | | |
| control_center | 20 | | |
| authentication_and_security | 10 | | |

Five oversized guides are split into 29 contiguous parts. The specifications mark 45 operations as deprecated; the KUs show them as deprecated.

## 3. Pilot (Phase B)

The pilot built 19 KUs with `build_kus.py --only …`, then ran `validate.py --pilot`.

| Case | Content |
| --- | --- |
| P1 | hold funds guide with the Payment methods API |
| P2 | transfers (make and cancel) |
| P3 | authentication methods with the Platform-authentication API |
| P4 | real-time event delivery, payments data events and event catalogue KUs |
| P5 | `api-endpoints-removed`, the curated marketplace removal KU, changelog 2 October 2026 and the seller-management overview |
| P6 | PCI card migration (`PostPciCardsV1`) with the Accumulator API KUs |
| P7 | `KU-ERR-codes-weam` and `KU-ERR-validation-code-definitions` |

**Result: 0 failures across 20 checks.**

| Check | Items |
| --- | --- |
| Verbatim blocks | 17 |
| API operations | 15 |
| Examples (17 `$ref`-only, resolved by full pointer) | 110 |
| Error-code rows | 37 |
| Event types | 35 |
| Lifecycle checks | 4 |

Manual spot checks, all by the same model (see VL-01):

- **P6:** the `pan`/`encrypted_pan` + `key_id` + `iv` rule is rendered in full, and the example pointers resolve to concrete values.
- **P5:** the marketplace KU makes no claim beyond its quotations, and the missing successor is stated as undocumented.
- **P7:** each error row matches the CSV.

The pilot and the steps that followed exposed defects MD-01 to MD-06. All six were fixed, and the fixes were confirmed by reruns (see ISSUES_AND_GAPS.md).

## 4. Full corpus: file-level integrity

| Check | Checked | Failures |
| --- | --- | --- |
| corpus_integrity (re-hash of all sources, fingerprint P) | 503 | 0 |
| ku_files (one KU per file, IDs unique, path matches category) | 623 | 0 |
| ku_front_matter (required fields, allowed categories and types) | 623 | 0 |
| traceability_sources (each source reference has the correct path, sha256 and URL) | 1,480 | 0 |
| traceability_related (every related_kus target exists) | 623 | 0 |
| traceability_operations (each listed operationId exists in a spec) | 623 | 0 |
| no_r1_or_candidates | 623 | 0 |
| no_source_copies_in_ku_dir (no KU is a byte copy of a source file) | 623 | 0 |
| manifest (503 rows, all migrated, every KU exists) | 503 | 0 |
| coverage (every source unit maps to a KU and an anchor that exist) | 6,226 | 0 |

## 5. Full corpus: content-level validation (deterministic)

| Check | Checked | Failures | What it compares |
| --- | --- | --- | --- |
| verbatim_fidelity | 451 blocks | 0 | Each `source:begin/end` block, byte for byte, against the source body (front matter removed; `\r` kept). |
| verbatim_completeness | 427 Markdown sources | 0 | Every guide, changelog and README body is fully present. Split parts join back without gaps or overlaps. |
| api_fidelity | 999 operations | 0 | Method, path, operationId and deprecation. Each parameter's name, location and required flag. Top-level request fields, their required flags and their enums. Response statuses. Checked with a resolver independent of the builder's. |
| api_coverage | 999 | 0 | Each operation is rendered exactly once. |
| examples | 4,346 | 0 | Each rendered example equals the YAML value. The 426 `$ref`-only examples are resolved through the full `#/components/examples/…` pointer. 0 rows were not JSON-parsable. |
| csv_error_codes | 1,216 rows | 0 | The full CSV row (code, HTTP status, message, spec files, operation count and sample) appears in exactly one error KU. |
| csv_event_types | 243 | 0 | The full CSV row appears in exactly one event catalogue KU. |
| csv_endpoint_event_map | 482 | 0 | Each endpoint–event pair appears both in the operation's API KU and in the event catalogue. |
| csv_operations_catalog | 999 | 0 | Each catalogue line is present in its API KU. |
| lifecycle | 29 | 0 | <ul><li>Every changelog KU has the HISTORICAL RECORD banner and `lifecycle: historical`.</li><li>Every guide KU that links a removed marketplace slug carries a lifecycle warning.</li><li>The marketplace KU contains the "Not documented" successor statement and no successor wording outside quotations.</li><li>The structured removal register has the same number of rows as the source table.</li></ul> |
| quote_fidelity | 1 curated KU | 0 | Every `>` quotation in the marketplace KU occurs in the changelog sources it cites, compared with whitespace normalised. |
| link_accounting | 3,213 links | 0 | Each operation link in a guide or changelog appears in its KU's link table, with the correct resolved or unresolved status. |

**Total: 22 checks, 0 failures.**

A rebuild of the collection is deterministic. Running `build_kus.py` twice gives an identical KU tree and an identical `SOURCE_COVERAGE.csv` (determinism check at the final audit).

## 6. Retrieval usability (Phase D)

`tools/retrieval_tests.py` ranks KUs in two steps:

1. exact identifier lookup;
2. BM25 over the KU text (k1 = 1.5, b = 0.75), with a tokenizer that keeps identifiers intact.

It makes no network calls and uses no embeddings. Each question cites its evidence in the corpus.

**Result: 29/29 pass.**

| Group | Questions | Result |
| --- | --- | --- |
| Exact identifiers: operationId, error code, path, removed slug | X1–X7 | all within the top 5. X1 is at rank 2; the others are at rank 1. |
| Natural-language how-to | N1–N11 | all within the top 10. N5 and N10 are at rank 2; the others are at rank 1. |
| Request and response | R1, R2 | rank 1 |
| Lifecycle | L1–L3 | L1 at rank 3, L2 at rank 4, L3 at rank 1 |
| Error codes | E1, E2 | E1 at rank 4, E2 at rank 1 |
| Not documented | U1–U4 | pass |

The not-documented questions pass as follows:

- **U1:** `cards-pci/go-live` appears in no KU.
- **U2:** `MIGR-0400` appears in no KU.
- **U3:** the event catalogue KU states that the payload is not documented.
- **U4:** the marketplace KU states that no successor is documented.

**Correction to a test expectation.** X2 first expected `KU-ERR-codes-weam` for `WEAM0029`. That was a mistake in the test, not in the KUs. `WEAM0029` occurs only in `changelog/2-october-2026.md`, as a removed code, and is absent from the specs and from `error_code_index.csv`. The expectation was changed to `KU-CHG-2-october-2026`, and X7 (`WEAM0001` → `KU-ERR-codes-weam`) was added.

The same run exposed a real defect: every error KU carried a generic `WEAM0029` caveat, which polluted retrieval (MD-05). That defect was fixed in the builder.

## 7. Source accounting

| Source group | Files | Where it went |
| --- | --- | --- |
| Guide and changelog Markdown, spec README | 427 | Body kept verbatim in a KU, in 451 blocks |
| OpenAPI specifications | 71 | All 999 operations and their named schemas rendered in API KUs |
| CSV files | 5 | Every row rendered in the event, error or API KUs |

0 sources are excluded. `MIGRATION_MANIFEST.csv` gives each source's KUs and issue IDs. `SOURCE_COVERAGE.csv` maps each of the 6,226 source units to a KU and an anchor.

## 8. What these results do not show

See ISSUES_AND_GAPS.md, VL-01 to VL-05.

- **A single reviewer.** One model planned, built, tested and reviewed this migration. No independent model and no human subject-matter expert reviewed the KUs.
- **Mechanical, not semantic, fidelity.** The 0-failure results show that the verbatim text, rendered fields, examples, CSV rows, links and lifecycle quotations match the sources. They do not show that generated text (purpose lines, navigation, link classifications) is semantically complete.
- **Partial API checks.** `api_fidelity` does not cross-check nested request fields or response-body field tables.
- **Small retrieval tests.** The 29 tests use a lexical retriever, and the questions were written by the same model. They show the collection is usable, not how a production retriever will perform.
- **Open defects.** MD-07 (seven KUs over 100 KB) and MD-08 (MDX/HTML left unconverted) remain open.
