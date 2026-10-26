---
ku_id: KU-EVT-catalogue-bacs
title: 'Event catalogue: bacs'
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
- patch-amend-mandate
- post-bacs-client-return
- post-cancel-bacs
- post-cancel-mandate
- post-create-bacs
- post-create-claim
- post-create-mandate
- post-raise-claim-reversal
- post-release-bacs
- post-reversal-bacs
related_kus:
- KU-API-payment-rails-bacs-payments--bacs-direct-credit
- KU-API-payment-rails-bacs-payments--bacs-direct-debit
- KU-PAY-bacs
events:
- bacs-direct-credit-in-return-status-change-1
- bacs-direct-credit-in-status-change-1
- bacs-direct-credit-out-return-status-change-1
- bacs-direct-credit-out-reversal-status-change-1
- bacs-direct-credit-out-status-change-1
- bacs-direct-debit-claim-reversal-status-change-1
- bacs-direct-debit-claim-status-change-1
- bacs-mandate-status-change-1
---

# Event catalogue: bacs

**KU ID:** `KU-EVT-catalogue-bacs` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 8 event type(s) whose inventory domain is bacs, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `bacs-direct-credit-in-return-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-in-return-status-change-1 | 1 | Payment_rails_-_BACS_payments |
| `bacs-direct-credit-in-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-in-status-change-1 | 2 | Payment_rails_-_BACS_payments |
| `bacs-direct-credit-out-return-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-out-return-status-change-1 | 1 | Payment_rails_-_BACS_payments |
| `bacs-direct-credit-out-reversal-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-out-reversal-status-change-1 | 1 | Payment_rails_-_BACS_payments |
| `bacs-direct-credit-out-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-credit-out-status-change-1 | 1 | Payment_rails_-_BACS_payments |
| `bacs-direct-debit-claim-reversal-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-debit-claim-reversal-status-change-1 | 1 | Payment_rails_-_BACS_payments |
| `bacs-direct-debit-claim-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-direct-debit-claim-status-change-1 | 1 | Payment_rails_-_BACS_payments |
| `bacs-mandate-status-change-1` | bacs | 1 | https://developers.pismo.io/events/docs/bacs-mandate-status-change-1 | 3 | Payment_rails_-_BACS_payments |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `bacs-direct-credit-in-return-status-change-1` | `POST /v1/payments/bacs/directcredit/return/{id}` | `post-bacs-client-return` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `bacs-direct-credit-in-status-change-1` | `POST /v1/payments/bacs/directcredit/cancel/{id}` | `post-cancel-bacs` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `bacs-direct-credit-in-status-change-1` | `POST /v1/payments/bacs/directcredit/release/{id}` | `post-release-bacs` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `bacs-direct-credit-out-return-status-change-1` | `POST /v1/payments/bacs/directcredit/out` | `post-create-bacs` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `bacs-direct-credit-out-reversal-status-change-1` | `POST /v1/payments/bacs/directcredit/{id}/reversal` | `post-reversal-bacs` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `bacs-direct-credit-out-status-change-1` | `POST /v1/payments/bacs/directcredit/out` | `post-create-bacs` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `bacs-direct-debit-claim-reversal-status-change-1` | `POST /v1/payments/bacs/directdebit/claims/reversal/{id}` | `post-raise-claim-reversal` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-debit |
| `bacs-direct-debit-claim-status-change-1` | `POST /v1/payments/bacs/directdebit/claims` | `post-create-claim` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-debit |
| `bacs-mandate-status-change-1` | `POST /v1/payments/bacs/directdebit/paper-mandates` | `post-create-mandate` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-debit |
| `bacs-mandate-status-change-1` | `PATCH /v1/payments/bacs/directdebit/mandates/{id}` | `patch-amend-mandate` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-debit |
| `bacs-mandate-status-change-1` | `POST /v1/payments/bacs/directdebit/mandates/{id}/cancel` | `post-cancel-mandate` | `Payment_rails_-_BACS_payments` | KU-API-payment-rails-bacs-payments--bacs-direct-debit |

## Guides that link to these events

- `bacs-direct-credit-in-return-status-change-1`: `KU-PAY-bacs`
- `bacs-direct-credit-in-status-change-1`: `KU-PAY-bacs`
- `bacs-direct-credit-out-return-status-change-1`: `KU-PAY-bacs`
- `bacs-direct-credit-out-status-change-1`: `KU-PAY-bacs`
- `bacs-direct-debit-claim-reversal-status-change-1`: `KU-PAY-bacs`
- `bacs-direct-debit-claim-status-change-1`: `KU-PAY-bacs`
- `bacs-mandate-status-change-1`: `KU-PAY-bacs`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: bacs-direct-credit-in-return-status-change-1, bacs-direct-credit-in-status-change-1, bacs-direct-credit-out-return-status-change-1, bacs-direct-credit-out-reversal-status-change-1, bacs-direct-credit-out-status-change-1, bacs-direct-debit-claim-reversal-status-change-1, bacs-direct-debit-claim-status-change-1, bacs-mandate-status-change-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-payment-rails-bacs-payments--bacs-direct-credit` — API reference: Payment rails - BACS payments — BACS direct credit
- `KU-API-payment-rails-bacs-payments--bacs-direct-debit` — API reference: Payment rails - BACS payments — BACS direct debit
- `KU-PAY-bacs` — BACS: clearing, Direct Debit mandates and indemnity claims
