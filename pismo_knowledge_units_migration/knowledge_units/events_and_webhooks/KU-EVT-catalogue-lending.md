---
ku_id: KU-EVT-catalogue-lending
title: 'Event catalogue: lending'
category: events_and_webhooks
ku_type: event_catalogue
lifecycle: current
sources:
- path: api-reference-data/event_type_inventory.csv
  sha256: 7eed7e3056f6f22e154bae7f22d25760a66c9e243ee0367953d1e935f823aed5
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- bookLoanV2
- cancelAllLoansByAccountV2
- cancelLoanV2
- createLoanProductV2
- createPrepayment
- deleteLoanProductV2
- registerPrepaymentSimulationV2
- simulatePrepaymentV2
- updateLoanProductV2
related_kus:
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-lending--prepayment
- KU-LEND-book-a-loan
- KU-LEND-disburse-loan
- KU-LEND-manage-loan-repayment-and-settlement
events:
- lending-lending-loan-update-1
- lending-lending-prepayment-v2-creation-1
- lending-lending-prepayment-v2-status-changed-1
- lending-loan-booked-1
- lending-loan-product-creation-3
- lending-loan-product-update-1
- lending-prepayment-creation-1
---

# Event catalogue: lending

**KU ID:** `KU-EVT-catalogue-lending` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 7 event type(s) whose inventory domain is lending, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `lending-lending-loan-update-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-lending-loan-update-1 | 2 | Lending |
| `lending-lending-prepayment-v2-creation-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-lending-prepayment-v2-creation-1 | 1 | Lending |
| `lending-lending-prepayment-v2-status-changed-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-lending-prepayment-v2-status-changed-1 | 1 | Lending |
| `lending-loan-booked-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-loan-booked-1 | 1 | Lending |
| `lending-loan-product-creation-3` | lending | 3 | https://developers.pismo.io/events/docs/lending-loan-product-creation-3 | 1 | Lending |
| `lending-loan-product-update-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-loan-product-update-1 | 2 | Lending |
| `lending-prepayment-creation-1` | lending | 1 | https://developers.pismo.io/events/docs/lending-prepayment-creation-1 | 1 | Lending |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `lending-lending-loan-update-1` | `POST /v2/accounts/{accountId}/loans/cancel` | `cancelAllLoansByAccountV2` | `Lending` | KU-API-lending--loans |
| `lending-lending-loan-update-1` | `POST /v2/loans/{loanId}/cancel` | `cancelLoanV2` | `Lending` | KU-API-lending--loans |
| `lending-lending-prepayment-v2-creation-1` | `POST /v2/loans/{loanId}/prepayment/simulate` | `simulatePrepaymentV2` | `Lending` | KU-API-lending--prepayment |
| `lending-lending-prepayment-v2-status-changed-1` | `POST /v2/loans/{loanId}/prepayment/{simulationId}/register` | `registerPrepaymentSimulationV2` | `Lending` | KU-API-lending--prepayment |
| `lending-loan-booked-1` | `POST /v2/loans` | `bookLoanV2` | `Lending` | KU-API-lending--loans |
| `lending-loan-product-creation-3` | `POST /v2/loan-products` | `createLoanProductV2` | `Lending` | KU-API-lending--loan-products |
| `lending-loan-product-update-1` | `PATCH /v2/loan-products/{productId}` | `updateLoanProductV2` | `Lending` | KU-API-lending--loan-products |
| `lending-loan-product-update-1` | `DELETE /v2/loan-products/{productId}` | `deleteLoanProductV2` | `Lending` | KU-API-lending--loan-products |
| `lending-prepayment-creation-1` | `POST /v2/prepayments` | `createPrepayment` | `Lending` | KU-API-lending--prepayment |

## Guides that link to these events

- `lending-lending-loan-update-1`: `KU-LEND-book-a-loan`, `KU-LEND-disburse-loan`, `KU-LEND-manage-loan-repayment-and-settlement`
- `lending-loan-booked-1`: `KU-LEND-book-a-loan`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: lending-lending-loan-update-1, lending-lending-prepayment-v2-creation-1, lending-lending-prepayment-v2-status-changed-1, lending-loan-booked-1, lending-loan-product-creation-3, lending-loan-product-update-1, lending-prepayment-creation-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-lending--prepayment` — API reference: Lending — Prepayment
- `KU-LEND-book-a-loan` — Book loans
- `KU-LEND-disburse-loan` — Disburse loans
- `KU-LEND-manage-loan-repayment-and-settlement` — Manage loan repayment and settlement
