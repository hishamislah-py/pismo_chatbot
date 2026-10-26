---
ku_id: KU-EVT-catalogue-fps
title: 'Event catalogue: fps'
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
- post-cancel-fps
- post-cop-verification
- post-create-fps
- post-release-fps
- post-return-fps
related_kus:
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-PAY-faster-payment-system
events:
- fps-cop-name-verification-admissions-1
- fps-cop-name-verification-submissions-1
- fps-fps-in-return-status-change-1
- fps-fps-in-status-change-1
- fps-fps-out-return-status-change-1
- fps-fps-out-status-change-1
---

# Event catalogue: fps

**KU ID:** `KU-EVT-catalogue-fps` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 6 event type(s) whose inventory domain is fps, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `fps-cop-name-verification-admissions-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-cop-name-verification-admissions-1 | 1 | Instant_payments_-_UK_FPS_beta |
| `fps-cop-name-verification-submissions-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-cop-name-verification-submissions-1 | 1 | Instant_payments_-_UK_FPS_beta |
| `fps-fps-in-return-status-change-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-fps-in-return-status-change-1 | 1 | Instant_payments_-_UK_FPS_beta |
| `fps-fps-in-status-change-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-fps-in-status-change-1 | 2 | Instant_payments_-_UK_FPS_beta |
| `fps-fps-out-return-status-change-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-fps-out-return-status-change-1 | 1 | Instant_payments_-_UK_FPS_beta |
| `fps-fps-out-status-change-1` | fps | 1 | https://developers.pismo.io/events/docs/fps-fps-out-status-change-1 | 1 | Instant_payments_-_UK_FPS_beta |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `fps-cop-name-verification-admissions-1` | `POST /v1/payments/fps/cop` | `post-cop-verification` | `Instant_payments_-_UK_FPS_beta` | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `fps-cop-name-verification-submissions-1` | `POST /v1/payments/fps/cop` | `post-cop-verification` | `Instant_payments_-_UK_FPS_beta` | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `fps-fps-in-return-status-change-1` | `POST /v1/payments/fps/return/{endToEndId}` | `post-return-fps` | `Instant_payments_-_UK_FPS_beta` | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `fps-fps-in-status-change-1` | `POST /v1/payments/fps/cancel/{endToEndId}` | `post-cancel-fps` | `Instant_payments_-_UK_FPS_beta` | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `fps-fps-in-status-change-1` | `POST /v1/payments/fps/release/{endToEndId}` | `post-release-fps` | `Instant_payments_-_UK_FPS_beta` | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `fps-fps-out-return-status-change-1` | `POST /v1/payments/fps/out` | `post-create-fps` | `Instant_payments_-_UK_FPS_beta` | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `fps-fps-out-status-change-1` | `POST /v1/payments/fps/out` | `post-create-fps` | `Instant_payments_-_UK_FPS_beta` | KU-API-instant-payments-uk-fps-beta--faster-payments |

## Guides that link to these events

- `fps-cop-name-verification-admissions-1`: `KU-PAY-faster-payment-system`
- `fps-cop-name-verification-submissions-1`: `KU-PAY-faster-payment-system`
- `fps-fps-in-return-status-change-1`: `KU-PAY-faster-payment-system`
- `fps-fps-in-status-change-1`: `KU-PAY-faster-payment-system`
- `fps-fps-out-return-status-change-1`: `KU-PAY-faster-payment-system`
- `fps-fps-out-status-change-1`: `KU-PAY-faster-payment-system`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: fps-cop-name-verification-admissions-1, fps-cop-name-verification-submissions-1, fps-fps-in-return-status-change-1, fps-fps-in-status-change-1, fps-fps-out-return-status-change-1, fps-fps-out-status-change-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
