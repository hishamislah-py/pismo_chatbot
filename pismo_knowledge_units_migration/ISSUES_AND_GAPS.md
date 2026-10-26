# Issues and gaps

The IDs below appear in the `issues` column of `MIGRATION_MANIFEST.csv`; 94 of the 503 sources carry at least one ID. The figures were measured by `tools/issues_data.py`, which writes them to `work/issues_data.json`.

Nothing listed here was repaired in the KUs. The source text is kept verbatim, and each discrepancy is recorded here, and in the affected KU where that helps.

| Prefix | Meaning |
| --- | --- |
| SC | Contradictions or defects in the source |
| SG | Gaps in the source (information that is not documented) |
| UR | Unresolved relationships |
| MD | Migration defects (resolved and open) |
| VL | Validation limitations |

## SC: Contradictions or defects in the source

| ID | Finding | Evidence | Handling |
| --- | --- | --- | --- |
| SC-01 | Eight sources still instruct readers to use marketplace endpoints that the removal register and the 2 October 2026 changelog record as removed: <ul><li>six seller-management guides;</li><li>`marketplace-data-events.md`;</li><li>`changelog/7-july-2025.md`.</li></ul> The slugs are `postmarketplacesv2`, `postlinkmerchanttomarketplacev1`, `getmerchantsbymarketplaceidv2`, `putupdatemarketplacev1` and `getmerchantsbymarketplaceidv1`. | The slugs are absent from all 71 specs. The match to the register is by link text equal to the published endpoint name. | `KU-LIFE-marketplace-endpoint-removal` lists each link with its file and line. The guide KUs mark these links "not found … name-matched to removed endpoint". |
| SC-02 | For the `10/6/26` marketplace row, the register lists 7 endpoint names, and two of them are both "List marketplace merchants". The changelog lists 8 names, with V1/V2 suffixes and separate "Create marketplace V1" and "Create marketplace V2" entries. | `api-endpoints-removed.md`; `changelog/2-october-2026.md` | Both are quoted in the curated KU. No reconciliation was attempted. |
| SC-03 | Register row 11 (Cardsonfile, "Get card validation amount", `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount`, removed `5/12/2026`) is still present in the current spec. Its operationId there is `get-a-specific-validation-amount-for-a-given-card` in `Card_issuing_-_Cards_on_file.yaml`. | Structured removal register in `KU-LIFE-api-endpoints-removed`, column "still in current specs" | Flagged in that row. The API KU renders the operation as the spec defines it. Which source is right is not decided. |
| SC-04 | `#/components/responses/202AssetBlockedResponse` is used where a schema is expected. | `Banking_-_Assets.yaml` `POST /v1/issuer/{issuer_id}/assets/{asset_id}/block` | Logged in `work/build_log.json` (`kind_mismatch_refs`). The KU renders the 202 response as "(type not declared) (schema `202AssetBlockedResponse`)" and shows no fields. The pointer was not rewritten to a schema. |
| SC-05 | Six pairs of guides have byte-identical bodies (get-started duplicates for card issuing, core banking, DDAs, transaction banking, lending and seller management). Two more pairs share a title but differ in content: <ul><li>Control Center get-started;</li><li>transaction categories.</li></ul> | `work/analysis.json` (`identical_bodies`, `same_title_guides`) | Each pair is grouped into one KU (see `ku_plan.py`) and both bodies are kept verbatim, so both URLs stay traceable. |
| SC-06 | 18 operationIds are defined twice: `Core_platform_-_Balance_watcher.yaml` and `Core_platform_-_Payment_configurations.yaml` use the same `*-config-by-*` and `*-acceptance-by-*` IDs for different paths. | `duplicate_operation_ids` | Operations are keyed by spec plus method plus path. A guide link to a duplicated ID points to both KUs. |
| SC-07 | Three links have an empty target: <ul><li>`changelog/7-february-2025.md:78` [Fee Model account migration completed]();</li><li>`docs/card-issuing/visa-dispute-use-case.md:101` [Dispute installment created]();</li><li>`docs/core-banking/penalties-for-cd-accounts.md:444` [Create deposit product]().</li></ul> | Source text | Kept as they are. |
| SC-08 | Four sources contain bare carriage returns (`\r` not followed by `\n`): <ul><li>`azure-event-configuration-tutorial.md`;</li><li>`confluent-event-config-tutorial.md`;</li><li>`sftp-event-file-configuration-tutorial.md`;</li><li>`api-endpoints-removed.md`, where they also break table cells and paths.</li></ul> | Byte scan | Verbatim blocks keep them byte for byte. In generated tables they are shown as ` ⏎ `. Path matching joins the fragments. |
| SC-09 | Five guides are titled outdated or beta: <ul><li>`mdes-token-connect`;</li><li>`visa-flexible-credentials`;</li><li>`pix-funds-recovery`;</li><li>`legal-blocks`;</li><li>`pismo-data-platform-http-integration-guide-beta`.</li></ul> | Front-matter titles | The titles are kept. The KU header shows the source title. |

## SG: Gaps in the source

| ID | Gap | Handling |
| --- | --- | --- |
| SG-01 | **Event payload schemas are not documented.** `event_type_inventory.csv` and `endpoint_event_map.csv` give names, domains and the endpoints that trigger each event, but no payload fields. | Each event catalogue KU states "Payload … not documented in the available source corpus" (retrieval test U3). |
| SG-02 | **No successor is documented for the removed marketplace endpoints** (or for any other removed endpoint). | The curated KU states "Not documented in the available source corpus". Current marketplace operations are listed with the explicit note that similar names are not evidence of replacement (U4). |
| SG-03 | **No PCI card "go-live" endpoint or step is documented.** `Migrations.yaml` documents `POST /v1/migrations/cards-pci` (`PostPciCardsV1`) only. | Nothing was invented. U1 checks that `cards-pci/go-live` does not appear in any KU. |
| SG-04 | Changelog posts describe changes at a point in time, and none states the current state. | The 22 changelog KUs carry a HISTORICAL RECORD banner that points to the API and lifecycle KUs. |
| SG-05 | **38 error codes appear in YAML response examples but are missing from `error_code_index.csv`:** EP2P\* (8), WP2P\* (25), RULREP0404, RULREP0500, RULVAL0400, RULVAL0403 and RULV10400. | They are listed in the API KUs under "Error codes shown in this operation's response examples". There is no meaning for them beyond the example message. |
| SG-06 | **126 event slugs that guides link to are not in `event_type_inventory.csv`** (for example `account-balances-balance-history-1` and `apex-*`). | The links are kept verbatim. The event catalogue covers the 243 inventoried events only. |
| SG-07 | **The removal register's dates are incomplete or inconsistent.** Row 3 (Create combo card, `POST /wallet/v1/relationship`) has no date. Dates use mixed formats: `10/6/26`, `10/17/2025`, `9/2025` and others. | Raw values are kept. The curated KU labels its month/day reading as an inference. |

## UR-01: Unresolved operation links

86 distinct operation slugs appear in 54 sources (guides and changelogs) with no matching operationId in the current specifications.

**24 are name-matched to the removal register.** The link text equals a published endpoint name. These slugs are:

- marketplace: `postmarketplacesv2`, `postlinkmerchanttomarketplacev1`, `getmerchantsbymarketplaceidv1`, `getmerchantsbymarketplaceidv2`, `putupdatemarketplacev1`;
- merchant: `createmerchantusingmerchantid`, `createreversaltransaction`, `list*ofactivemerchants` (3);
- loans: `createloanproduct`, `getloanproduct`, `listloans`, `getloandetails`;
- interest-bearing: `interest-bearing-v1-*-maturity-instruction-override` (4);
- corporate: `corporate-bulk-payments-get-aes-keys`, `corporate-post-v1-operation-blocks`, `post-corporate-float-cash-in`, `patch-corporate-float-cash-in`;
- other: `get-processing-code-by-tenant`, `getcalendarlist`.

**62 are unverified.** They are labelled "not found in the current OpenAPI specifications", not "removed". `work/issues_data.json` lists every slug with its sources. The observed patterns below are descriptive only and were not verified:

- **Guide-page slugs linked through `/reference/`:** `api-endpoints-removed`, `authentication-with-openid`, `get-started-with-pismo-apis`, `transaction-classification`, `program-parameters-reference-table` and others.
- **Slugs with a `-1` suffix:** `get-config-by-account-1`, `post-config-by-tenant-1`, `post-payments-1`, `post-v1-balances-config-1` and others. Several share a stem with the duplicated operationIds in SC-06.
- **Apparent typos in the source:** `nterest-bearing-v1-deposit-account-open`, `delinquent-ccount-closure-post` and `restrutureloan`. Not repaired.
- **Cash management, corporate and BACS slugs** from 2026 changelogs: `cash-management-v2-*`, `corporate-v2/v3-*` and `post-*-bacs-1`.

## MD: Migration defects

### Resolved during the migration

Each fix was confirmed by a rerun of `validate.py`.

| ID | Defect | Fix |
| --- | --- | --- |
| MD-01 | `CODE_RX` missed codes such as `WP2P0000`, and `error_code` keys were ignored. | Pattern broadened; both keys read. |
| MD-02 | Bare `\r` in the removal register broke the generated table cells. | `cell`/`raw_cell` escape `\r`; `joined_paths` added. |
| MD-03 | The marketplace KU pulled in unrelated decommission lists. | Lists filtered to those that mention marketplaces. |
| MD-04 | `anyOf` error schemas were missing from the "Schemas referenced" section. | Named options added for non-2xx responses. |
| MD-05 | A generic changelog caveat put `WEAM0029` into every error KU. Found by retrieval test X2. | Changelog mentions are now listed per KU. |
| MD-06 | 18 links with escaped link text (`\[beta\]`) were not accounted for. Error KUs had empty related links. | `REF_LINK` pattern fixed; `OPS_BY_MP` added. |

### Open

| ID | Defect |
| --- | --- |
| MD-07 | **Seven KUs exceed 100 KB.** The largest is `KU-EVT-client-webhooks-part-09` at 217,819 bytes. It is a single fenced code block in the source, and the splitter does not cut inside fences. The others are `KU-API-banking-transaction-banking--payments-part-01` (163,570 bytes), `client-webhooks-part-13` and `part-11`, `pix-payments--pix-part-01`, `disputes--disputes-part-01` and `payment-methods--payment-methods-part-01`. A single operation with very large schemas cannot be split further without breaking its tables. These KUs are complete, but retrieval precision on them may be lower. |
| MD-08 | **MDX and HTML components** (`<details>`, `<summary style={{…}}>`, callouts and similar) are kept unconverted inside the verbatim blocks. This was a deliberate choice for fidelity, but those KUs render less cleanly as plain Markdown. |

## VL: Validation limitations

| ID | Limitation |
| --- | --- |
| VL-01 | **One model, no independent reviewer.** One model (Claude Opus 5.5) planned, built and reviewed the migration. No independent model and no human subject-matter expert reviewed the KUs. The manual spot checks in the pilot were done by the same model. |
| VL-02 | **The deterministic checks prove mechanical fidelity, not meaning.** They show that verbatim text, field tables, examples, CSV rows and links match the sources. They do not prove that generated summaries, navigation or classifications are semantically complete or correct. |
| VL-03 | **Generated lifecycle labels are inferences.** The "name-matched to removed endpoint" label and the month/day reading of register dates rest on text matching and are labelled as such. |
| VL-04 | **Retrieval tests are lexical and small.** There are 29 questions. Exact-identifier lookup plus BM25 stands in for any production embedding retriever, and the questions were written by the same model that built the KUs. |
| VL-05 | **`api_fidelity` covers only part of each operation.** It uses its own simpler `$ref` resolver, separate from the builder's. It checks:<ul><li>method, path, operationId and deprecation;</li><li>each parameter's name, location and required flag;</li><li>each top-level request-body field, its required flag and its enum;</li><li>each response status.</li></ul>It does not cross-check nested request fields, response-body field tables or constraints other than enums. Those rely on the builder's resolver, the example checks and spot checks. |
