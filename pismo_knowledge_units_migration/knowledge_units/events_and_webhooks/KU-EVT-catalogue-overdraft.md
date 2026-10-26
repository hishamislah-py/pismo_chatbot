---
ku_id: KU-EVT-catalogue-overdraft
title: 'Event catalogue: overdraft'
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
- post-attach-product-to-account
- post-attach-product-to-program
- post-detach-product-from-account
- post-overdraft-product
related_kus:
- KU-API-banking-overdraft--account
- KU-API-banking-overdraft--product
- KU-API-banking-overdraft--program
- KU-GS-welcome
events:
- overdraft-product-account-attach-1
- overdraft-product-account-detach-1
- overdraft-product-creation-1
- overdraft-product-program-attach-1
---

# Event catalogue: overdraft

**KU ID:** `KU-EVT-catalogue-overdraft` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 4 event type(s) whose inventory domain is overdraft, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `overdraft-product-account-attach-1` | overdraft | 1 | https://developers.pismo.io/events/docs/overdraft-product-account-attach-1 | 1 | Banking_-_Overdraft |
| `overdraft-product-account-detach-1` | overdraft | 1 | https://developers.pismo.io/events/docs/overdraft-product-account-detach-1 | 1 | Banking_-_Overdraft |
| `overdraft-product-creation-1` | overdraft | 1 | https://developers.pismo.io/events/docs/overdraft-product-creation-1 | 1 | Banking_-_Overdraft |
| `overdraft-product-program-attach-1` | overdraft | 1 | https://developers.pismo.io/events/docs/overdraft-product-program-attach-1 | 1 | Banking_-_Overdraft |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `overdraft-product-account-attach-1` | `POST /v1/overdraft/accounts/{accountId}/attach` | `post-attach-product-to-account` | `Banking_-_Overdraft` | KU-API-banking-overdraft--account |
| `overdraft-product-account-detach-1` | `POST /v1/overdraft/accounts/{accountId}/detach` | `post-detach-product-from-account` | `Banking_-_Overdraft` | KU-API-banking-overdraft--account |
| `overdraft-product-creation-1` | `POST /v1/overdraft` | `post-overdraft-product` | `Banking_-_Overdraft` | KU-API-banking-overdraft--product |
| `overdraft-product-program-attach-1` | `POST /v1/overdraft/programs/{programId}/attach` | `post-attach-product-to-program` | `Banking_-_Overdraft` | KU-API-banking-overdraft--program |

## Guides that link to these events

- `overdraft-product-creation-1`: `KU-GS-welcome`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: overdraft-product-account-attach-1, overdraft-product-account-detach-1, overdraft-product-creation-1, overdraft-product-program-attach-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-banking-overdraft--account` — API reference: Banking - Overdraft — Account
- `KU-API-banking-overdraft--product` — API reference: Banking - Overdraft — Product
- `KU-API-banking-overdraft--program` — API reference: Banking - Overdraft — Program
- `KU-GS-welcome` — Get started with the Pismo Developers Portal
