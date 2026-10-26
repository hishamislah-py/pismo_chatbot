# Migration plan: Pismo KB r2 corpus to knowledge units

## 1. Scope and sources

- **Source:** `pismo_kb_release_r2/kb_corpus/`, 503 files, fingerprint P `7080b549…f0e62`. The allowlist and the source map both equal the corpus.

  | Folder | Files | Contents |
  | --- | --- | --- |
  | `docs/` | 404 | guide Markdown |
  | `changelog/` | 22 | changelog Markdown |
  | `api-specs/` | 72 | 71 OpenAPI YAML files plus `README.md` |
  | `api-reference-data/` | 5 | CSV files |

- **Excluded as sources:**
  - r1 material (`pismo_dataset_final`, `pismo_kb_release`);
  - candidate data that was never promoted;
  - the retrieval experiment and earlier reports.

  The validator checks that no KU references any of them (`no_r1_or_candidates`).

- **Corpus treatment:** the corpus is read-only. Every run re-checks the fingerprint (`corpus_integrity`).

## 2. Taxonomy

There are 17 category folders. Each folder has a code that is used in KU IDs (`KU-<CODE>-<slug>`).

| Folder | Code | Main content |
| --- | --- | --- |
| getting_started | GS | platform and API introductions |
| authentication_and_security | AUTH | OpenID, mTLS, access tokens, encryption |
| events_and_webhooks | EVT | event delivery, webhooks, data events, event catalogue |
| reports_and_data_files | RPT | reports, data files, SFTP and cloud file delivery |
| errors_and_troubleshooting | ERR | error-code catalogue, validation codes |
| rate_limits_and_support | SUP | rate limiting, the Service Desk |
| api_lifecycle | LIFE | deprecation, removal register, curated marketplace removal KU |
| changelog_history | CHG | 22 changelog posts, kept as historical records |
| transfers_and_payments | PAY | transfers, payments, Pix, hold funds |
| core_platform | CORE | accounts, customers, programs, platform rules |
| banking | BANK | core and transaction banking |
| card_issuing | CARD | cards, authorization, networks, disputes |
| revolving_credit | CRED | statements, cycles, credit products |
| lending | LEND | loans |
| seller_management | SELL | sellers, merchants, marketplaces |
| control_center | CC | Control Center UI guides |
| api_reference | API | one KU per OpenAPI specification tag |

**Deviations from the requested structure:**

| Requested | What was done | Reason |
| --- | --- | --- |
| `reference_data` folder | no folder | The CSV rows are rendered into the event catalogue KUs (EVT) and the error catalogue KUs (ERR). Operation catalogue rows go into the API KUs. |
| `cross_cutting` folder | no folder | Cross-cutting guides are placed by topic (AUTH, SUP, EVT). |
| `marketplaces_and_lifecycle` folder | renamed `api_lifecycle` | Marketplace product guides belong in SELL, and lifecycle evidence belongs in LIFE. |
| — | added `changelog_history` folder | Separating historical changelogs from current guidance reduces the risk of retrieving them as current answers. |

## 3. KU types and construction rules

| Type | Built from | Rule |
| --- | --- | --- |
| `workflow_guide` | guide Markdown, alone or as a group | The body is included **byte for byte** with its front matter removed, inside `source:begin/end` markers. Heading levels and MDX/HTML are left unchanged. Generated navigation and an operation-link table go before the body. |
| `changelog_history` | one changelog post | Verbatim, as above, plus a HISTORICAL RECORD banner. |
| `api_reference` | OpenAPI YAML | One KU per (spec, tag), split into parts above 70 KB. Rendering: <ul><li>`$ref`s resolved by full JSON pointer with the correct component type</li><li>allOf merged; oneOf/anyOf listed as options</li><li>field tables with constraints</li><li>examples only from concrete `example`/`examples` values or `#/components/examples` targets, never synthesised from a schema</li><li>error codes taken from the `code`/`error_code` example keys</li></ul> |
| `event_catalogue` | `event_type_inventory.csv`, `endpoint_event_map.csv` | One KU per event domain. Domains with fewer than 3 events go into `other-domains`. |
| `error_catalogue` | `error_code_index.csv` | One KU per code prefix. Prefixes with fewer than 15 codes are chunked alphabetically. Codes that appear only in changelogs are listed per KU. |
| `lifecycle_reference` | removal register, changelog, guides, specs | Curated. Contains only quotations and structured extracts. An undocumented successor is stated as "Not documented in the available source corpus". |

**Grouping:** 73 KUs combine more than one guide. Each group is defined in `tools/ku_plan.py` with a written reason, for example a step-1 to step-6 series or a guide duplicated across `get-started/`. The group KU keeps every member body verbatim, in its own block.

**Splitting:** a guide larger than 90 KB is split at H2, H3 or H4 boundaries (falling back to blank lines) into parts of about 60 KB. The validator checks that the parts join back into the exact original. Five guides are split this way (29 parts).

**Operation linking:**

- A guide link slug that matches an operationId (case-insensitive) becomes a cross-reference to the API KU.
- An unmatched slug is labelled "not found in the current OpenAPI specifications".
- The register match is applied only when the link text equals an endpoint name in `api-endpoints-removed.md`. It is a name match, never presented as an identifier match. Unmatched slugs are labelled "unverified" and are never assumed to be removed.

## 4. Phases and batches

| Phase | Work | Gate |
| --- | --- | --- |
| A | inventory (`a1_inventory.py`), structural analysis (`a2_analyse.py`), probes (`a3`, `a4`), taxonomy and groups (`ku_plan.py`) | fingerprint matches; allowlist = source map = corpus |
| B | pilot of 19 KUs covering 7 representative cases (P1–P7) built with `build_kus.py --only …` | `validate.py --pilot` passes with 0 failures, plus manual spot checks |
| C | full build in batches by KU type: guides (by category), changelogs, API reference (by spec), event catalogue, error catalogue, lifecycle | `validate.py` passes with 0 failures on the whole collection before a batch counts as complete |
| D | retrieval usability (`retrieval_tests.py`): 25 answerable questions and 4 not-documented questions | 29/29 |
| E | final audit: rerun the full chain, recheck the fingerprint, run the issue analysis, annotate the manifest | all checks pass and the fingerprint is unchanged |

Pilot cases: P1 hold funds, P2 transfers, P3 authentication with the Platform-authentication API, P4 event delivery with the event catalogue, P5 lifecycle and marketplace removal, P6 PCI card migration with the Accumulator API, P7 error catalogue with validation codes.

## 5. Validation strategy

Two kinds of check are reported separately.

- **File-level integrity:** corpus fingerprint, manifest and coverage completeness, front-matter schema, and source SHA-256 values.
- **Content-level fidelity:**
  - each verbatim block compared byte for byte with the source body;
  - each split checked for completeness;
  - each operation's rendered method, path, operationId, parameters, required fields and deprecation checked against the YAML;
  - each example value checked against the YAML;
  - each CSV row checked for presence in its KU;
  - lifecycle markers checked: changelog banners, warnings on removed-endpoint links, the successor statement and the register row count;
  - each quotation in the curated KU checked against its cited changelog;
  - each guide link checked for presence in its KU.

`VALIDATION_REPORT.md` lists the limits of these checks.

## 6. Risks and mitigations

| Risk | Mitigation |
| --- | --- |
| Removed endpoints presented as current | The register is rendered as a structured table. The curated marketplace KU and lifecycle warnings sit in the affected guide KUs. Changelog KUs carry a banner. |
| Invented replacements or payloads | Statements that something is not documented are explicit and checked by tests (U3, U4). Examples are never synthesised. |
| Silent repair of source errors | Sources are kept verbatim, and discrepancies are recorded in ISSUES_AND_GAPS.md. |
| Oversized KUs reduce retrieval precision | Size-based splitting. Seven KUs are still larger than 100 KB (MD-07). |
| Single reviewer | Recorded as limitation VL-01. |
