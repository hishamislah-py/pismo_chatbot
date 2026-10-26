---
ku_id: KU-EVT-catalogue-pix
title: 'Event catalogue: pix'
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
- patch-v2-pix-infraction
- patch-v2-pix-keys
- post-cancel-dict-claim
- post-cancel-dict-refund
- post-cancel-funds-recovery
- post-close-dict-refund
- post-complete-dict-claim
- post-confirm-dict-claim
- post-create-funds-recovery
- post-dict-key-claim
- post-pix-out-transfer
- post-pix-reversal
- post-refund-recovery
- post-register-dict-refund
- post-schedule
- post-schedule-pix-payment
- post-v2-pix-fraud-marker-cancel
- post-v2-pix-fraud-marker-create
- post-v2-pix-infraction-cancel
- post-v2-pix-infraction-close
- post-v2-pix-infraction-create
- post-v2-pix-keys-create
- post-v2-pix-keys-delete
related_kus:
- KU-API-instant-payments-pix-management--anti-fraud
- KU-API-instant-payments-pix-management--claims
- KU-API-instant-payments-pix-management--funds-recovery
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-instant-payments-pix-management--keys-part-01
- KU-API-instant-payments-pix-management--refunds
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--scheduled-transfers
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-EVT-pix-payments-data-events
- KU-PAY-pix-automatic
- KU-PAY-pix-funds-recovery
- KU-PAY-pix-instant-payments
events:
- pix-dict-claim-status-change-1
- pix-dict-fraud-marker-registration-1
- pix-dict-fraud-marker-registration-failure-1
- pix-dict-fraud-marker-status-change-1
- pix-dict-fraud-marker-status-change-failure-1
- pix-dict-funds-recoveries-status-change-1
- pix-dict-infraction-status-change-1
- pix-dict-key-status-change-1
- pix-dict-refund-status-change-1
- pix-financial-reconciliation-1
- pix-pix-in-1
- pix-pix-in-reversal-1
- pix-pix-out-1
- pix-pix-out-reversal-1
---

# Event catalogue: pix

**KU ID:** `KU-EVT-catalogue-pix` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 14 event type(s) whose inventory domain is pix, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `pix-dict-claim-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1 | 4 | Instant_payments_-_Pix_management |
| `pix-dict-fraud-marker-registration-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-fraud-marker-registration-1 | 1 | Instant_payments_-_Pix_management |
| `pix-dict-fraud-marker-registration-failure-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-fraud-marker-registration-failure-1 | 1 | Instant_payments_-_Pix_management |
| `pix-dict-fraud-marker-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-fraud-marker-status-change-1 | 1 | Instant_payments_-_Pix_management |
| `pix-dict-fraud-marker-status-change-failure-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-fraud-marker-status-change-failure-1 | 1 | Instant_payments_-_Pix_management |
| `pix-dict-funds-recoveries-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1 | 3 | Instant_payments_-_Pix_management |
| `pix-dict-infraction-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1 | 4 | Instant_payments_-_Pix_management |
| `pix-dict-key-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-key-status-change-1 | 3 | Instant_payments_-_Pix_management |
| `pix-dict-refund-status-change-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-dict-refund-status-change-1 | 3 | Instant_payments_-_Pix_management |
| `pix-financial-reconciliation-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-financial-reconciliation-1 | 5 | Instant_payments_-_Pix_management;Instant_payments_-_Pix_payments |
| `pix-pix-in-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-in-1 | 3 | Instant_payments_-_Pix_payments |
| `pix-pix-in-reversal-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-in-reversal-1 | 1 | Instant_payments_-_Pix_payments |
| `pix-pix-out-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-out-1 | 3 | Instant_payments_-_Pix_payments |
| `pix-pix-out-reversal-1` | pix | 1 | https://developers.pismo.io/events/docs/pix-pix-out-reversal-1 | 1 | Instant_payments_-_Pix_payments |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `pix-dict-claim-status-change-1` | `POST /v2/pix/claims` | `post-dict-key-claim` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--claims |
| `pix-dict-claim-status-change-1` | `POST /v2/pix/claims/confirm` | `post-confirm-dict-claim` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--claims |
| `pix-dict-claim-status-change-1` | `POST /v2/pix/claims/cancel` | `post-cancel-dict-claim` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--claims |
| `pix-dict-claim-status-change-1` | `POST /v2/pix/claims/complete` | `post-complete-dict-claim` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--claims |
| `pix-dict-fraud-marker-registration-1` | `POST /v2/pix/fraud-markers` | `post-v2-pix-fraud-marker-create` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--anti-fraud |
| `pix-dict-fraud-marker-registration-failure-1` | `POST /v2/pix/fraud-markers` | `post-v2-pix-fraud-marker-create` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--anti-fraud |
| `pix-dict-fraud-marker-status-change-1` | `POST /v2/pix/fraud-markers/{id}/cancel` | `post-v2-pix-fraud-marker-cancel` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--anti-fraud |
| `pix-dict-fraud-marker-status-change-failure-1` | `POST /v2/pix/fraud-markers/{id}/cancel` | `post-v2-pix-fraud-marker-cancel` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--anti-fraud |
| `pix-dict-funds-recoveries-status-change-1` | `POST /v1/pix/funds-recoveries` | `post-create-funds-recovery` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--funds-recovery |
| `pix-dict-funds-recoveries-status-change-1` | `POST /v1/pix/funds-recoveries/{funds_recovery_id}/refund` | `post-refund-recovery` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--funds-recovery |
| `pix-dict-funds-recoveries-status-change-1` | `POST /v1/pix/funds-recoveries/{funds_recovery_id}/cancel` | `post-cancel-funds-recovery` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--funds-recovery |
| `pix-dict-infraction-status-change-1` | `POST /v2/pix/infraction-reports` | `post-v2-pix-infraction-create` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `pix-dict-infraction-status-change-1` | `POST /v2/pix/infraction-reports/{id}/close` | `post-v2-pix-infraction-close` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `pix-dict-infraction-status-change-1` | `POST /v2/pix/infraction-reports/{id}/cancel` | `post-v2-pix-infraction-cancel` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--infraction-reports-part-01 |
| `pix-dict-infraction-status-change-1` | `PATCH /v2/pix/infraction-reports/{id}` | `patch-v2-pix-infraction` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `pix-dict-key-status-change-1` | `POST /v2/pix/keys` | `post-v2-pix-keys-create` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--keys-part-01 |
| `pix-dict-key-status-change-1` | `PATCH /v2/pix/keys` | `patch-v2-pix-keys` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--keys-part-01 |
| `pix-dict-key-status-change-1` | `POST /v2/pix/keys/delete` | `post-v2-pix-keys-delete` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--keys-part-01 |
| `pix-dict-refund-status-change-1` | `POST /v2/pix/refunds` | `post-register-dict-refund` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--refunds |
| `pix-dict-refund-status-change-1` | `POST /v2/pix/refunds/{refundId}/cancel` | `post-cancel-dict-refund` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--refunds |
| `pix-dict-refund-status-change-1` | `POST /v2/pix/refunds/{refundId}/close` | `post-close-dict-refund` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--refunds |
| `pix-financial-reconciliation-1` | `POST /v2/pix/refunds/{refundId}/close` | `post-close-dict-refund` | `Instant_payments_-_Pix_management` | KU-API-instant-payments-pix-management--refunds |
| `pix-financial-reconciliation-1` | `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--pix-part-01 |
| `pix-financial-reconciliation-1` | `POST /pix/v1/pix/out/schedule` | `post-schedule` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers |
| `pix-financial-reconciliation-1` | `POST /pix/v1/pix/in/reversal` | `post-pix-reversal` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--pix-part-01 |
| `pix-financial-reconciliation-1` | `POST /pix/v2/pix/out/scheduler` | `post-schedule-pix-payment` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `pix-pix-in-1` | `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--pix-part-01 |
| `pix-pix-in-1` | `POST /pix/v1/pix/out/schedule` | `post-schedule` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers |
| `pix-pix-in-1` | `POST /pix/v2/pix/out/scheduler` | `post-schedule-pix-payment` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `pix-pix-in-reversal-1` | `POST /pix/v1/pix/in/reversal` | `post-pix-reversal` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--pix-part-01 |
| `pix-pix-out-1` | `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--pix-part-01 |
| `pix-pix-out-1` | `POST /pix/v1/pix/out/schedule` | `post-schedule` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers |
| `pix-pix-out-1` | `POST /pix/v2/pix/out/scheduler` | `post-schedule-pix-payment` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `pix-pix-out-reversal-1` | `POST /pix/v1/pix/in/reversal` | `post-pix-reversal` | `Instant_payments_-_Pix_payments` | KU-API-instant-payments-pix-payments--pix-part-01 |

## Guides that link to these events

- `pix-dict-claim-status-change-1`: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`
- `pix-dict-funds-recoveries-status-change-1`: `KU-PAY-pix-funds-recovery`
- `pix-dict-infraction-status-change-1`: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`
- `pix-dict-key-status-change-1`: `KU-EVT-pix-payments-data-events`
- `pix-dict-refund-status-change-1`: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`
- `pix-financial-reconciliation-1`: `KU-EVT-pix-payments-data-events`
- `pix-pix-in-1`: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`
- `pix-pix-in-reversal-1`: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`
- `pix-pix-out-1`: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-automatic`, `KU-PAY-pix-instant-payments`
- `pix-pix-out-reversal-1`: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: pix-dict-claim-status-change-1, pix-dict-fraud-marker-registration-1, pix-dict-fraud-marker-registration-failure-1, pix-dict-fraud-marker-status-change-1, pix-dict-fraud-marker-status-change-failure-1, pix-dict-funds-recoveries-status-change-1, pix-dict-infraction-status-change-1, pix-dict-key-status-change-1, pix-dict-refund-status-change-1, pix-financial-reconciliation-1, pix-pix-in-1, pix-pix-in-reversal-1, pix-pix-out-1, pix-pix-out-reversal-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-instant-payments-pix-management--anti-fraud` — API reference: Instant payments - Pix management — Anti-fraud
- `KU-API-instant-payments-pix-management--claims` — API reference: Instant payments - Pix management — Claims
- `KU-API-instant-payments-pix-management--funds-recovery` — API reference: Instant payments - Pix management — Funds recovery
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-instant-payments-pix-management--keys-part-01` — API reference: Instant payments - Pix management — Keys (part 1 of 2)
- `KU-API-instant-payments-pix-management--refunds` — API reference: Instant payments - Pix management — Refunds
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--scheduled-transfers` — API reference: Instant payments - Pix payments — Scheduled transfers
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
- `KU-PAY-pix-automatic` — Pix Automatic
- `KU-PAY-pix-funds-recovery` — Pix funds recovery [beta]
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
