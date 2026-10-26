---
ku_id: KU-EVT-catalogue-transaction
title: 'Event catalogue: transaction'
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
- PostSetupTransactionType
- patch-cash-management-v2-earmarks-earmarkid
- patch-corporate-v2-earmarks-earmarkid
- post-cash-management-v2-earmarks
- post-cash-management-v2-earmarks-earmarkid-cancel
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-shift-transactions
- postInterestAccruals
related_kus:
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-core-platform-transactions--transaction-types
- KU-API-revolving-credit-interest-accruals--post-interest-accruals
- KU-API-revolving-credit-statements--transaction-shift
- KU-CORE-accounting-events
- KU-CORE-transactions-overview
- KU-CORE-transactiontypes
- KU-CRED-understanding-statements
- KU-EVT-corporate-banking-data-events
- KU-EVT-transactions-data-events
- KU-PAY-hold-funds
events:
- transaction-creation-1
- transaction-types-creation-1
- transaction-update-1
---

# Event catalogue: transaction

**KU ID:** `KU-EVT-catalogue-transaction` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 3 event type(s) whose inventory domain is transaction, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `transaction-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-creation-1 | 7 | Banking_-_Transaction_banking;Revolving_credit_-_Interest_accruals |
| `transaction-types-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-types-creation-1 | 1 | Core_platform_-_Transactions |
| `transaction-update-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-update-1 | 1 | Revolving_credit_-_Statements |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `transaction-creation-1` | `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `transaction-creation-1` | `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `transaction-creation-1` | `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `transaction-creation-1` | `POST /cash-management/v2/earmarks` | `post-cash-management-v2-earmarks` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `transaction-creation-1` | `PATCH /cash-management/v2/earmarks/{earmarkId}` | `patch-cash-management-v2-earmarks-earmarkid` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `transaction-creation-1` | `POST /cash-management/v2/earmarks/{earmarkId}/cancel` | `post-cash-management-v2-earmarks-earmarkid-cancel` | `Banking_-_Transaction_banking` | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `transaction-creation-1` | `POST /v1/accounts/{accountId}/interest-accruals` | `postInterestAccruals` | `Revolving_credit_-_Interest_accruals` | KU-API-revolving-credit-interest-accruals--post-interest-accruals |
| `transaction-types-creation-1` | `POST /v1/transaction-types` | `PostSetupTransactionType` | `Core_platform_-_Transactions` | KU-API-core-platform-transactions--transaction-types |
| `transaction-update-1` | `POST /statements-v2/v1/accounts/{accountId}/transactions/shifts` | `post-shift-transactions` | `Revolving_credit_-_Statements` | KU-API-revolving-credit-statements--transaction-shift |

## Guides that link to these events

- `transaction-creation-1`: `KU-CORE-accounting-events`, `KU-CORE-transactions-overview`, `KU-CORE-transactiontypes`, `KU-CRED-understanding-statements`, `KU-EVT-corporate-banking-data-events`, `KU-EVT-transactions-data-events`, `KU-PAY-hold-funds`
- `transaction-types-creation-1`: `KU-EVT-transactions-data-events`
- `transaction-update-1`: `KU-EVT-transactions-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: transaction-creation-1, transaction-types-creation-1, transaction-update-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-revolving-credit-interest-accruals--post-interest-accruals` — API reference: Revolving credit - Interest accruals — Post interest accruals
- `KU-API-revolving-credit-statements--transaction-shift` — API reference: Revolving credit - Statements — Transaction shift
- `KU-CORE-accounting-events` — Accounting events
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-CORE-transactiontypes` — Transaction types
- `KU-CRED-understanding-statements` — Understanding statements
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-EVT-transactions-data-events` — Core platform - Transactions
- `KU-PAY-hold-funds` — Hold funds
