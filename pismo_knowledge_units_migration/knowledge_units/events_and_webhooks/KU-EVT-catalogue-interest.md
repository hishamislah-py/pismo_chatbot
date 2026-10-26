---
ku_id: KU-EVT-catalogue-interest
title: 'Event catalogue: interest'
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
- patch-v1-interest-plan
- post-v1-interest-account-cancellation
- post-v1-interest-deposit
- post-v1-interest-plan
- post-v1-interest-plan-b3
- post-v1-interest-withdrawal
related_kus:
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-interest-management--interest-plan
- KU-API-banking-interest-operations--interest-engine
- KU-EVT-interest-management-data-events
- KU-LEND-loan-products
events:
- interest-engine-interest-account-cancellation-failure-1
- interest-engine-interest-account-cancellation-success-1
- interest-engine-interest-deposit-failure-1
- interest-engine-interest-deposit-success-1
- interest-engine-interest-plan-creation-success-1
- interest-engine-interest-registration-failure-1
- interest-engine-interest-registration-success-1
- interest-engine-interest-withdrawal-failure-1
- interest-engine-interest-withdrawal-success-1
- interest-management-interest-plan-creation-success-1
---

# Event catalogue: interest

**KU ID:** `KU-EVT-catalogue-interest` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 10 event type(s) whose inventory domain is interest, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `interest-engine-interest-account-cancellation-failure-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-account-cancellation-failure-1 | 1 | Banking_-_Interest_operations |
| `interest-engine-interest-account-cancellation-success-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-account-cancellation-success-1 | 1 | Banking_-_Interest_operations |
| `interest-engine-interest-deposit-failure-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-deposit-failure-1 | 1 | Banking_-_Interest_operations |
| `interest-engine-interest-deposit-success-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-deposit-success-1 | 1 | Banking_-_Interest_operations |
| `interest-engine-interest-plan-creation-success-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-plan-creation-success-1 | 2 | Banking_-_Interest_engine |
| `interest-engine-interest-registration-failure-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-registration-failure-1 | 1 | Banking_-_Interest_operations |
| `interest-engine-interest-registration-success-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-registration-success-1 | 1 | Banking_-_Interest_operations |
| `interest-engine-interest-withdrawal-failure-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-withdrawal-failure-1 | 1 | Banking_-_Interest_operations |
| `interest-engine-interest-withdrawal-success-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-engine-interest-withdrawal-success-1 | 1 | Banking_-_Interest_operations |
| `interest-management-interest-plan-creation-success-1` | interest | 1 | https://developers.pismo.io/events/docs/interest-management-interest-plan-creation-success-1 | 1 | Banking_-_Interest_management |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `interest-engine-interest-account-cancellation-failure-1` | `POST /v1/interest/account/cancellation` | `post-v1-interest-account-cancellation` | `Banking_-_Interest_operations` | KU-API-banking-interest-operations--interest-engine |
| `interest-engine-interest-account-cancellation-success-1` | `POST /v1/interest/account/cancellation` | `post-v1-interest-account-cancellation` | `Banking_-_Interest_operations` | KU-API-banking-interest-operations--interest-engine |
| `interest-engine-interest-deposit-failure-1` | `POST /v1/interest/deposit` | `post-v1-interest-deposit` | `Banking_-_Interest_operations` | KU-API-banking-interest-operations--interest-engine |
| `interest-engine-interest-deposit-success-1` | `POST /v1/interest/deposit` | `post-v1-interest-deposit` | `Banking_-_Interest_operations` | KU-API-banking-interest-operations--interest-engine |
| `interest-engine-interest-plan-creation-success-1` | `POST /v1/interest/plan` | `post-v1-interest-plan` | `Banking_-_Interest_engine` | KU-API-banking-interest-engine--interest-engine |
| `interest-engine-interest-plan-creation-success-1` | `PATCH /v1/interest/plan/{interestPlanId}` | `patch-v1-interest-plan` | `Banking_-_Interest_engine` | KU-API-banking-interest-engine--interest-engine |
| `interest-engine-interest-registration-failure-1` | `POST /v1/interest/deposit` | `post-v1-interest-deposit` | `Banking_-_Interest_operations` | KU-API-banking-interest-operations--interest-engine |
| `interest-engine-interest-registration-success-1` | `POST /v1/interest/deposit` | `post-v1-interest-deposit` | `Banking_-_Interest_operations` | KU-API-banking-interest-operations--interest-engine |
| `interest-engine-interest-withdrawal-failure-1` | `POST /v1/interest/withdrawal` | `post-v1-interest-withdrawal` | `Banking_-_Interest_operations` | KU-API-banking-interest-operations--interest-engine |
| `interest-engine-interest-withdrawal-success-1` | `POST /v1/interest/withdrawal` | `post-v1-interest-withdrawal` | `Banking_-_Interest_operations` | KU-API-banking-interest-operations--interest-engine |
| `interest-management-interest-plan-creation-success-1` | `POST /v1/interest/plan` | `post-v1-interest-plan-b3` | `Banking_-_Interest_management` | KU-API-banking-interest-management--interest-plan |

## Guides that link to these events

- `interest-management-interest-plan-creation-success-1`: `KU-EVT-interest-management-data-events`, `KU-LEND-loan-products`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: interest-engine-interest-account-cancellation-failure-1, interest-engine-interest-account-cancellation-success-1, interest-engine-interest-deposit-failure-1, interest-engine-interest-deposit-success-1, interest-engine-interest-plan-creation-success-1, interest-engine-interest-registration-failure-1, interest-engine-interest-registration-success-1, interest-engine-interest-withdrawal-failure-1, interest-engine-interest-withdrawal-success-1, interest-management-interest-plan-creation-success-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-interest-management--interest-plan` — API reference: Banking - Interest management for B3-listed products — Interest plan
- `KU-API-banking-interest-operations--interest-engine` — API reference: Banking - Interest operations — Interest engine
- `KU-EVT-interest-management-data-events` — Banking - Interest management
- `KU-LEND-loan-products` — Loan products: overview and creation
