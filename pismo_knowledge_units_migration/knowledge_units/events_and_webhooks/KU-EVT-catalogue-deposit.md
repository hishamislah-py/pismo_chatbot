---
ku_id: KU-EVT-catalogue-deposit
title: 'Event catalogue: deposit'
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
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-deposit-account-open
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-attach-program
- interest-bearing-v1-deposit-detach-account
- interest-bearing-v1-deposit-update-account-attachment
- interest-bearing-v1-deposit-update-program-attachment
- interest-bearing-v1-patch-deposit-product
- interest-bearing-v1-savings-account-attach-account
- interest-bearing-v1-savings-account-attach-program
- interest-bearing-v1-savings-account-detach-account
related_kus:
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--deposit-account-open
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-bearing-accounts--program-attachment
- KU-EVT-interest-management-data-events
events:
- deposit-product-account-attach-1
- deposit-product-account-attachment-updated-1
- deposit-product-account-detach-1
- deposit-product-creation-1
- deposit-product-deposit-account-opened-1
- deposit-product-program-attach-1
- deposit-product-program-attachment-updated-1
- deposit-product-update-1
---

# Event catalogue: deposit

**KU ID:** `KU-EVT-catalogue-deposit` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 8 event type(s) whose inventory domain is deposit, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `deposit-product-account-attach-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-account-attach-1 | 3 | Banking_-_Interest-bearing_accounts |
| `deposit-product-account-attachment-updated-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-account-attachment-updated-1 | 1 | Banking_-_Interest-bearing_accounts |
| `deposit-product-account-detach-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-account-detach-1 | 2 | Banking_-_Interest-bearing_accounts |
| `deposit-product-creation-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-creation-1 | 1 | Banking_-_Interest-bearing_accounts |
| `deposit-product-deposit-account-opened-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-deposit-account-opened-1 | 1 | Banking_-_Interest-bearing_accounts |
| `deposit-product-program-attach-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-program-attach-1 | 2 | Banking_-_Interest-bearing_accounts |
| `deposit-product-program-attachment-updated-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-program-attachment-updated-1 | 1 | Banking_-_Interest-bearing_accounts |
| `deposit-product-update-1` | deposit | 1 | https://developers.pismo.io/events/docs/deposit-product-update-1 | 1 | Banking_-_Interest-bearing_accounts |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `deposit-product-account-attach-1` | `POST /v1/deposits/accounts/{accountId}/attach` | `interest-bearing-v1-deposit-attach-account` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--account-attachment |
| `deposit-product-account-attach-1` | `POST /v1/deposits/accounts/open` | `interest-bearing-v1-deposit-account-open` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--deposit-account-open |
| `deposit-product-account-attach-1` | `POST /v1/savings-accounts/accounts/{accountId}/attach` | `interest-bearing-v1-savings-account-attach-account` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--account-attachment |
| `deposit-product-account-attachment-updated-1` | `PATCH /v1/deposits/accounts/{accountId}/attachment` | `interest-bearing-v1-deposit-update-account-attachment` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--account-attachment |
| `deposit-product-account-detach-1` | `POST /v1/deposits/accounts/{accountId}/detach` | `interest-bearing-v1-deposit-detach-account` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--account-attachment |
| `deposit-product-account-detach-1` | `POST /v1/savings-accounts/accounts/{accountId}/detach` | `interest-bearing-v1-savings-account-detach-account` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--account-attachment |
| `deposit-product-creation-1` | `POST /v1/deposits` | `interest-bearing-v1-create-deposit-product` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--product |
| `deposit-product-deposit-account-opened-1` | `POST /v1/deposits/accounts/open` | `interest-bearing-v1-deposit-account-open` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--deposit-account-open |
| `deposit-product-program-attach-1` | `POST /v1/deposits/programs/{programId}/attach` | `interest-bearing-v1-deposit-attach-program` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--program-attachment |
| `deposit-product-program-attach-1` | `POST /v1/savings-accounts/programs/{programId}/attach` | `interest-bearing-v1-savings-account-attach-program` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--program-attachment |
| `deposit-product-program-attachment-updated-1` | `PATCH /v1/deposits/programs/{programId}/attachment` | `interest-bearing-v1-deposit-update-program-attachment` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--program-attachment |
| `deposit-product-update-1` | `PATCH /v1/deposits/{productId}` | `interest-bearing-v1-patch-deposit-product` | `Banking_-_Interest-bearing_accounts` | KU-API-banking-interest-bearing-accounts--product |

## Guides that link to these events

- `deposit-product-account-attach-1`: `KU-EVT-interest-management-data-events`
- `deposit-product-account-detach-1`: `KU-EVT-interest-management-data-events`
- `deposit-product-program-attach-1`: `KU-EVT-interest-management-data-events`
- `deposit-product-update-1`: `KU-EVT-interest-management-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: deposit-product-account-attach-1, deposit-product-account-attachment-updated-1, deposit-product-account-detach-1, deposit-product-creation-1, deposit-product-deposit-account-opened-1, deposit-product-program-attach-1, deposit-product-program-attachment-updated-1, deposit-product-update-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--deposit-account-open` — API reference: Banking - Interest-bearing accounts — Deposit account open
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-bearing-accounts--program-attachment` — API reference: Banking - Interest-bearing accounts — Program attachment
- `KU-EVT-interest-management-data-events` — Banking - Interest management
