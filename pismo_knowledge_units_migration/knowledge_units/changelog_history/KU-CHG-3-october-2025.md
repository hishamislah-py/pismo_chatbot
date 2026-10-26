---
ku_id: KU-CHG-3-october-2025
title: 'Changelog: 3 October 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/3-october-2025.md
  sha256: 358bb4abdb2a3939b50a6eb3fef843b9c70442c82762cda68fc52e7b8b8af085
  url: https://developers.pismo.io/pismo-docs/changelog/3-october-2025
  role: changelog_post
  updated_at: ''
operations:
- corporate-delete-v2-operation-block-id
- corporate-get-v1-checks-id
- corporate-get-v2-operation-blocks
- corporate-patch-v2-operation-block-id
- corporate-post-v1-checks
- corporate-post-v2-operation-blocks
- corporate-v2-list-operation-blocks
- get-corporate-v1-restricted-funds
- get-v1-interest-plans
- list-corporate-v1-restricted-funds
- patch-corporate-v1-restricted-funds
- post-corporate-v1-checks-release
- post-corporate-v1-restricted-funds
- post-v1-interest-account-cancellation
- post-v1-interest-accrual-setup
- post-v1-interest-withdrawal
related_kus:
- KU-API-banking-interest-engine--interest-accrual
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-interest-operations--interest-engine
- KU-API-banking-transaction-banking--check-posting
- KU-API-banking-transaction-banking--operations-blocks
- KU-API-banking-transaction-banking--restricted-funds
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 3 October 2025
coverage_window: 5 September and 3 October 2025
---

# Changelog: 3 October 2025

**KU ID:** `KU-CHG-3-october-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **3 October 2025** (changes between 5 September and 3 October 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated".

## Topics covered

Restrict funds; Payments; Setup; Banking operations; Transaction banking; Card network integration; Statements; Merchants

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/3-october-2025

<!-- source:begin path=changelog/3-october-2025.md part=0-end -->

# 3 October 2025

Changes between 5 September and 3 October 2025

<div class="customTab"></div>

<details>
  <summary class="tabContent" id="New features">

### Restrict funds

#### New

The restrict funds feature is now live. This feature enables financial institutions to instantly block or restore account fund access—individually or in bulk—based on regulatory, fraud, or client-driven requirements. You can block full or partial amounts in your clients’ accounts either due to request or judicial/regulatory events such as liquidation or receivership. This feature includes four endpoints:

* [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds)
* [Get fund restriction](https://developers.pismo.io/pismo-docs/reference/get-corporate-v1-restricted-funds)
* [List fund restrictions](https://developers.pismo.io/pismo-docs/reference/list-corporate-v1-restricted-funds)
* [Release restriction](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v1-restricted-funds)

</summary>
</details>

<details>
  <summary class="tabContent" id="Core platform">

### Payments

#### Updated

The new `original_authorization` request field is available on the [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-1) endpoint.

### Setup

#### Docs

The missing program parameter "Overlimit fee amount" was added to the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide.

</summary>
</details>

<details>
  <summary class="tabContent" id="Core banking">

### Banking operations

#### New

The following new endpoints are now available:

* [Withdraw money](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-withdrawal)
* [Cancel account](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-account-cancellation)
* [List Org interest plans](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plans)
* [Configure timing for division accrual calculation](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-accrual-setup)

### Transaction banking

#### New

The following new operation block endpoints (v2) are now available. They allow you to block all operations for entire account groups, while still permitting certain authorized activities—such as earmarks or check processing. This ensures that essential internal processes can continue even when most activities are frozen.

* [Create operation block](https://developers.pismo.io/pismo-docs/reference/corporate-post-v2-operation-blocks)
* [List operation blocks](https://developers.pismo.io/pismo-docs/reference/corporate-v2-list-operation-blocks)
* [Get operation block details](https://developers.pismo.io/pismo-docs/reference/corporate-get-v2-operation-blocks)
* [Update operation block](https://developers.pismo.io/pismo-docs/reference/corporate-patch-v2-operation-block-id)
* [Revoke operation block](https://developers.pismo.io/pismo-docs/reference/corporate-delete-v2-operation-block-id)

#### New

The check posting API is now available in beta release. It allows you to post a check to a specified external account, with the option to settle the amount immediately or at a future date. This API includes the following endpoints:

* [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks)
* [Get check posting](https://developers.pismo.io/pismo-docs/reference/corporate-get-v1-checks-id)
* [Release check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-release)
* [Cancel check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-cancel)

#### Docs

The following new guides are now available:

* [Get started with transaction banking](https://developers.pismo.io/pismo-docs/docs/get-started-with-transaction-banking) provides step-by-step instructions for onboarding to transaction banking.
* [Operation block](https://developers.pismo.io/pismo-docs/docs/operation-block) allows financial institutions to temporarily restrict account activity at the program, division, or organization level.
* [Restrict funds](https://developers.pismo.io/pismo-docs/docs/restrict-funds) enables financial institutions to block full or partial amounts in their clients’ accounts. This capability is essential in situations where specific funds must be excluded from the general asset pool available to unsecured creditors, ensuring they receive priority handling or special protection.
* [File-based processing](https://developers.pismo.io/pismo-docs/docs/file-based-processing) allows you to upload UTF‑8 NDJSON files that contain a specific operation type, such as RESTRICT\_FUNDS, to execute multiple transactions in bulk. Each file is processed asynchronously, line by line, ensuring that a failure in one instruction does not halt the rest.

</summary>
</details>

<details>
  <summary class="tabContent" id="Card issuing">

### Card network integration

#### Docs

The following new validation codes were added to the Validation code definitions guide:

* [CTT - Card token timeout](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#ctt---card-token-timeout)
* [OOT - Orgs-API timeout](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#oot---orgs-api-timeout)

### Statements

#### Updated

The following event files were updated and moved to the appropriate **Statement refinancing** section.

* [Payment agreement simulation processed](https://developers.pismo.io/events/docs/statement-refinancing-payment-agreement-simulation-processed-1)
* [Payment agreement simulation not processed](https://developers.pismo.io/events/docs/statement-refinancing-payment-agreement-simulation-not-processed-1)

</summary>
</details>

<details>
  <summary class="tabContent" id="Seller management">

### Merchants

#### Deprecated

The following endpoints were marked as deprecated and are scheduled to be removed 8 October, 2025. Refer to [API endpoint deprecation and removal schedule](https://developers.pismo.io/pismo-docs/docs/deprecation-schedule) for a list of deprecated endpoints.

* [List active merchant states](https://developers.pismo.io/pismo-docs/reference/liststatesofactivemerchants)
* [List active merchant cities](https://developers.pismo.io/pismo-docs/reference/listcitiesofactvemerchants)
* [List active merchant neighborhoods](https://developers.pismo.io/pismo-docs/reference/listneighborhoodsofactivemerchants)

<br />

<br />

Disputes management documentation was removed from the Control Center documentation. This feature is not released in Control Center yet and documentation for it was posted erroneously earlier.

</summary>
</details>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /corporate/v1/restricted-funds` (`post-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v1/restricted-funds/{restrictedFundsId}` (`get-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v1/restricted-funds` (`list-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` (`patch-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `POST /v1/interest/withdrawal` (`post-v1-interest-withdrawal`) | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `POST /v1/interest/account/cancellation` (`post-v1-interest-account-cancellation`) | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `GET /v1/interest/plan` (`get-v1-interest-plans`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /v1/interest/accrual/setup` (`post-v1-interest-accrual-setup`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-accrual |
| `POST /corporate/v2/operations-blocks` (`corporate-post-v2-operation-blocks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `GET /corporate/v2/operations-blocks` (`corporate-v2-list-operation-blocks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `GET /corporate/v2/operations-blocks/{operationsBlockId}` (`corporate-get-v2-operation-blocks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `PATCH /corporate/v2/operations-blocks/{operationsBlockId}` (`corporate-patch-v2-operation-block-id`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `DELETE /corporate/v2/operations-blocks/{operationsBlockId}` (`corporate-delete-v2-operation-block-id`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `POST /corporate/v1/checks` (`corporate-post-v1-checks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `GET /corporate/v1/checks/{checkId}` (`corporate-get-v1-checks-id`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/release` (`post-corporate-v1-checks-release`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-payments-1` | Create cash-in or cash-out | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-corporate-v1-checks-cancel` | Cancel check | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `liststatesofactivemerchants` | List active merchant states | not found in the current OpenAPI specifications. Name-based inference: link text "List active merchant states" equals the endpoint name "List active merchant states" in the removed-endpoints list (row Seller management - Merchants / Merchants, date removed `10/8/2025`). This is a match on the endpoint name, not on an identifier. |
| `listcitiesofactvemerchants` | List active merchant cities | not found in the current OpenAPI specifications. Name-based inference: link text "List active merchant cities" equals the endpoint name "List active merchant cities" in the removed-endpoints list (row Seller management - Merchants / Merchants, date removed `10/8/2025`). This is a match on the endpoint name, not on an identifier. |
| `listneighborhoodsofactivemerchants` | List active merchant neighborhoods | not found in the current OpenAPI specifications. Name-based inference: link text "List active merchant neighborhoods" equals the endpoint name "List active merchant neighborhoods" in the removed-endpoints list (row Seller management - Merchants / Merchants, date removed `10/8/2025`). This is a match on the endpoint name, not on an identifier. |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/3-october-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/3-october-2025 | `358bb4abdb2a3939…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-engine--interest-accrual` — API reference: Banking - Interest engine — Interest accrual
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-interest-operations--interest-engine` — API reference: Banking - Interest operations — Interest engine
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-API-banking-transaction-banking--operations-blocks` — API reference: Banking - Transaction banking — Operations blocks
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
