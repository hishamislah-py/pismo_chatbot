---
ku_id: KU-EVT-catalogue-disputes
title: 'Event catalogue: disputes'
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
- post-create-on-us-dispute
- post-migration-installment
- post-migration-with-auth
- post-update-on-us-dispute
- post-v1-disputes-disputeId-event
- post-v1-disputes-disputeId-installment
- post-v1-fee
- post-v1-networkauthorization-disputes
related_kus:
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--fees
- KU-API-card-issuing-disputes--installments
- KU-API-card-issuing-disputes--migration
- KU-API-card-issuing-disputes--on-us
- KU-CARD-disputes-overview
- KU-CARD-disputes-state-machine
- KU-CARD-visa-dispute-use-case
- KU-EVT-disputes-endpoint-generated-events
events:
- disputes-dispute-fee-events-1
- disputes-dispute-installment-creation-1
- disputes-dispute-installment-status-change-1
- disputes-disputes-creation-1
---

# Event catalogue: disputes

**KU ID:** `KU-EVT-catalogue-disputes` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 4 event type(s) whose inventory domain is disputes, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `disputes-dispute-fee-events-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-fee-events-1 | 1 | Card_issuing_-_Disputes |
| `disputes-dispute-installment-creation-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-installment-creation-1 | 4 | Card_issuing_-_Disputes |
| `disputes-dispute-installment-status-change-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1 | 4 | Card_issuing_-_Disputes |
| `disputes-disputes-creation-1` | disputes | 1 | https://developers.pismo.io/events/docs/disputes-disputes-creation-1 | 1 | Card_issuing_-_Disputes |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `disputes-dispute-fee-events-1` | `POST /v1/fee` | `post-v1-fee` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--fees |
| `disputes-dispute-installment-creation-1` | `POST /v1/networkauthorization-disputes` | `post-v1-networkauthorization-disputes` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--disputes-part-01 |
| `disputes-dispute-installment-creation-1` | `POST /v1/disputes/{disputeId}/installment` | `post-v1-disputes-disputeId-installment` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--installments |
| `disputes-dispute-installment-creation-1` | `POST /v1/migration` | `post-migration-with-auth` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--migration |
| `disputes-dispute-installment-creation-1` | `POST /v1/migration/{disputeId}/installment` | `post-migration-installment` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--migration |
| `disputes-dispute-installment-status-change-1` | `POST /v1/disputes/{disputeId}/event` | `post-v1-disputes-disputeId-event` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--disputes-part-01 |
| `disputes-dispute-installment-status-change-1` | `POST /v1/migration` | `post-migration-with-auth` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--migration |
| `disputes-dispute-installment-status-change-1` | `POST /v1/migration/{disputeId}/installment` | `post-migration-installment` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--migration |
| `disputes-dispute-installment-status-change-1` | `POST /v1/disputes-on-us/{disputeId}/event` | `post-update-on-us-dispute` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--on-us |
| `disputes-disputes-creation-1` | `POST /v1/on-us-dispute` | `post-create-on-us-dispute` | `Card_issuing_-_Disputes` | KU-API-card-issuing-disputes--on-us |

## Guides that link to these events

- `disputes-dispute-fee-events-1`: `KU-CARD-disputes-overview`, `KU-EVT-disputes-endpoint-generated-events`
- `disputes-dispute-installment-creation-1`: `KU-CARD-visa-dispute-use-case`, `KU-EVT-disputes-endpoint-generated-events`
- `disputes-dispute-installment-status-change-1`: `KU-CARD-disputes-overview`, `KU-CARD-disputes-state-machine`, `KU-CARD-visa-dispute-use-case`, `KU-EVT-disputes-endpoint-generated-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: disputes-dispute-fee-events-1, disputes-dispute-installment-creation-1, disputes-dispute-installment-status-change-1, disputes-disputes-creation-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--fees` — API reference: Card issuing - Disputes — Fees
- `KU-API-card-issuing-disputes--installments` — API reference: Card issuing - Disputes — Installments
- `KU-API-card-issuing-disputes--migration` — API reference: Card issuing - Disputes — Migration
- `KU-API-card-issuing-disputes--on-us` — API reference: Card issuing - Disputes — On-Us
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-disputes-state-machine` — Disputes state machine
- `KU-CARD-visa-dispute-use-case` — Visa dispute use case
- `KU-EVT-disputes-endpoint-generated-events` — Card issuing - Disputes
