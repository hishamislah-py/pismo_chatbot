---
ku_id: KU-EVT-catalogue-scheduler
title: 'Event catalogue: scheduler'
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
- delete-schedule
- post-bulk-pre-schedules
- post-execute-pre-schedule
- post-pre-schedules
- post-v1-create-bulk-single-schedules
- post-v1-create-bulk-transfer-schedules
- post-v1-create-single-schedule
- post-v1-create-transfer-schedules
related_kus:
- KU-API-core-platform-payment-scheduler-beta--schedules
- KU-EVT-payments-data-events
- KU-PAY-payment-scheduler
events:
- scheduler-payments-bulk-pre-scheduled-payments-1
- scheduler-payments-bulk-scheduled-payments-1
- scheduler-payments-bulk-transfer-scheduled-payments-1
- scheduler-payments-scheduled-payments-1
- scheduler-payments-scheduled-payments-execution-1
---

# Event catalogue: scheduler

**KU ID:** `KU-EVT-catalogue-scheduler` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 5 event type(s) whose inventory domain is scheduler, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `scheduler-payments-bulk-pre-scheduled-payments-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-bulk-pre-scheduled-payments-1 | 1 | Core_platform_-_Payment_scheduler_beta |
| `scheduler-payments-bulk-scheduled-payments-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-bulk-scheduled-payments-1 | 1 | Core_platform_-_Payment_scheduler_beta |
| `scheduler-payments-bulk-transfer-scheduled-payments-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-bulk-transfer-scheduled-payments-1 | 1 | Core_platform_-_Payment_scheduler_beta |
| `scheduler-payments-scheduled-payments-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 | 7 | Core_platform_-_Payment_scheduler_beta |
| `scheduler-payments-scheduled-payments-execution-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 | 7 | Core_platform_-_Payment_scheduler_beta |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `scheduler-payments-bulk-pre-scheduled-payments-1` | `POST /v1/pre-schedules/bulk` | `post-bulk-pre-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-bulk-scheduled-payments-1` | `POST /v1/schedules/bulk` | `post-v1-create-bulk-single-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-bulk-transfer-scheduled-payments-1` | `POST /v1/transfers/bulk` | `post-v1-create-bulk-transfer-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-1` | `POST /v1/schedules` | `post-v1-create-single-schedule` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-1` | `POST /v1/schedules/bulk` | `post-v1-create-bulk-single-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-1` | `POST /v1/transfers` | `post-v1-create-transfer-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-1` | `POST /v1/transfers/bulk` | `post-v1-create-bulk-transfer-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-1` | `POST /v1/pre-schedules` | `post-pre-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-1` | `POST /v1/pre-schedules/bulk` | `post-bulk-pre-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-1` | `DELETE /v1/accounts/{accountId}/schedules/{scheduleId}` | `delete-schedule` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-execution-1` | `POST /v1/schedules` | `post-v1-create-single-schedule` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-execution-1` | `POST /v1/schedules/bulk` | `post-v1-create-bulk-single-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-execution-1` | `POST /v1/transfers` | `post-v1-create-transfer-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-execution-1` | `POST /v1/transfers/bulk` | `post-v1-create-bulk-transfer-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-execution-1` | `POST /v1/pre-schedules` | `post-pre-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-execution-1` | `POST /v1/pre-schedules/bulk` | `post-bulk-pre-schedules` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |
| `scheduler-payments-scheduled-payments-execution-1` | `POST /v1/accounts/{accountId}/pre-schedules/{scheduleId}/execute` | `post-execute-pre-schedule` | `Core_platform_-_Payment_scheduler_beta` | KU-API-core-platform-payment-scheduler-beta--schedules |

## Guides that link to these events

- `scheduler-payments-bulk-pre-scheduled-payments-1`: `KU-EVT-payments-data-events`
- `scheduler-payments-scheduled-payments-1`: `KU-EVT-payments-data-events`, `KU-PAY-payment-scheduler`
- `scheduler-payments-scheduled-payments-execution-1`: `KU-EVT-payments-data-events`, `KU-PAY-payment-scheduler`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: scheduler-payments-bulk-pre-scheduled-payments-1, scheduler-payments-bulk-scheduled-payments-1, scheduler-payments-bulk-transfer-scheduled-payments-1, scheduler-payments-scheduled-payments-1, scheduler-payments-scheduled-payments-execution-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-core-platform-payment-scheduler-beta--schedules` — API reference: Core platform - Payment scheduler — Schedules
- `KU-EVT-payments-data-events` — Core platform - Payments
- `KU-PAY-payment-scheduler` — Payment scheduler
