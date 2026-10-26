---
ku_id: KU-EVT-payments-data-events
title: Core platform - Payments
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/payments-data-events.md
  sha256: a866477d5b82e5e3b90a43830b29d56c5ecc2ce9d0870902fc6b7ed98f9c8cc4
  url: https://developers.pismo.io/pismo-docs/docs/payments-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:53.000Z'
operations:
- post-bulk-pre-schedules
- post-payments-v1-force
- post-payments-v1-force-cancel
- post-payments-v1-payments
- post-payments-v2-cancel
- post-pre-schedules
- post-v1-create-single-schedule
- post-v1-create-transfer-schedules
related_kus:
- KU-API-core-platform-payment-methods--force-operations
- KU-API-core-platform-payment-methods--payments
- KU-API-core-platform-payment-scheduler-beta--schedules
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-scheduler
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Core platform - Payments

**KU ID:** `KU-EVT-payments-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/payments-data-events.md`:

> This table lists the endpoints or other sources for payments and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/payments-data-events.md`: Core platform - Payments

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 8 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/payments-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payments-data-events · updatedAt: 2026-03-18T15:14:53.000Z

<!-- source:begin path=docs/data-and-reporting/payments-data-events.md part=0-end -->

# Core platform - Payments

This table lists the endpoints or other sources for payments and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

**Note:** Table entries marked **N/A** indicate **Not Applicable**.

| Endpoint                                                                                                                                                                                                                                                                                                                                                                                   | Event                                                                                                                                                                                                                                         |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments)                                                                                                                                                                                                                                                                                                                                            | [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1)                                                                                                                                          |
| [Force operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force)                                                                                                                                                                                                                                                                                                                                              | [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) with `authorization > type "FORCE"`                                                                                                      |
| [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-payments-v2-cancel)                                                                                                                                                                                                                                                                                                                                             | [Authorization cancelled](https://developers.pismo.io/events/docs/authorization-authorization-cancellation-event-1)                                                                                                                           |
| [Cancel forced operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force-cancel)                                                                                                                                                                                                                                                                                                                               | [Authorization cancelled](https://developers.pismo.io/events/docs/authorization-authorization-cancellation-event-1) with `authorization > type "FORCE"`                                                                                       |
| N/A                                                                                                                                                                                                                                                                                                                                                                                        | [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) occurs asynchronously when the Pismo platform creates a platform authorization                                      |
| - [Create single schedule](https://developers.pismo.io/pismo-docs/reference/post-v1-create-single-schedule)  - [Create transfer schedule](https://developers.pismo.io/pismo-docs/reference/post-v1-create-transfer-schedules)    - [Create pre-schedule](https://developers.pismo.io/pismo-docs/reference/post-pre-schedules)   - [Create bulk pre-schedules](https://developers.pismo.io/pismo-docs/reference/post-bulk-pre-schedules) | [Scheduled payment created or modified](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1)                                                                                                                      |
| N/A                                                                                                                                                                                                                                                                                                                                                                                        | [Scheduled payment executed](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1) occurs asynchronously when the Pismo platform executes a scheduled payment                                            |
| N/A                                                                                                                                                                                                                                                                                                                                                                                        | [Bulk pre-schedules created](https://developers.pismo.io/events/docs/scheduler-payments-bulk-pre-scheduled-payments-1) occurs when bulk pre-schedule processing has finished                                                                  |
| N/A                                                                                                                                                                                                                                                                                                                                                                                        | [Payment methods multiple transfers completed](https://developers.pismo.io/events/docs/payment-methods-multiple-transfers-1) occurs when the Pismo platform completes a multiple transfer process which moves funds between multiple accounts |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /payments/v1/payments/force` | `post-payments-v1-force` | Force operation | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--force-operations |
| `POST /payments/v2/cancel` | `post-payments-v2-cancel` | Cancel transfer funds | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /payments/v1/payments/force/cancel` | `post-payments-v1-force-cancel` | Cancel forced operation | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--force-operations |
| `POST /v1/schedules` | `post-v1-create-single-schedule` | Create single schedule | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/transfers` | `post-v1-create-transfer-schedules` | Create transfer schedule | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/pre-schedules` | `post-pre-schedules` | Create pre-schedule | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/pre-schedules/bulk` | `post-bulk-pre-schedules` | Create bulk pre-schedules | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |

### Operation essentials

- **`POST /payments/v1/payments`** (`post-payments-v1-payments`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `from`, `to`; response statuses 201, 202, 400, 409, 422, 500, 502; error codes in examples `WP2P0000`, `WP2P0019`, `EP2P9999`, `WP2P0005`, `WP2P0006`, `WP2P0003`, `WP2P0002`, `WLDG0019`, `ERUL0404`, `RULV10400`, `WP2P0020`, `WP2P0013`, `WLDG0006`, `WP2P0010`, `WP2P0000`, `WP2P0000`, `ELDG500`, `EPCG501`, `EP2P9999`, `EP2P0001`, `EP2P0002`; events `authorization-authorization-event-1`.
- **`POST /payments/v1/payments/force`** (`post-payments-v1-force`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields none declared; response statuses 201, 202, 400, 409, 500; error codes in examples `WP2P0000`, `WP2P1005`, `WRAT00001`, `WP2P0022`, `WP2P0023`, `WP2P0000`, `ERAT00001`, `ERAT00002`, `ERAT00003`, `EP2P0012`; events `authorization-authorization-event-1`.
- **`POST /payments/v2/cancel`** (`post-payments-v2-cancel`): security `BearerAuth`; required parameters `x-tenant` (header); required body fields `amount`; response statuses 200, 202, 208, 400, 404, 409, 500, 502; error codes in examples `AMON0004`, `WP2P0009`, `WP2P0000`, `AMON0000`, `WP2P0000`, `WP2P1005`, `EP2P0005`, `WP2P1111`, `EP2P0011`, `EP2P0013`, `WP2P0003`, `EP2P9999`, `WP2P3003`, `WP2P0033`, `WP2P0008`, `WP2P0000`, `WLDG0019`, `WLDG0004`, `WLDG0006`, `WLDG0005`, `WP2P0010`, `AMON0004`, `WP2P0009`, `WP2P0000`, `WP2P0000`, `ACQ0001`, `ACQ0000`, `EP2P9999`, `ELDG500`, `EP2P0001`; events `authorization-authorization-cancellation-event-1`.
- **`POST /payments/v1/payments/force/cancel`** (`post-payments-v1-force-cancel`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 202, 400, 404, 409, 500; error codes in examples `WP2P0000`, `WP2P0022`, `WP2P0003`, `WP2P1005`, `EP2P0005`, `EP2P0014`, `WP2P0008`, `WP2P0000`; events `authorization-authorization-cancellation-event-1`.
- **`POST /v1/schedules`** (`post-v1-create-single-schedule`): security `BearerAuth`; required parameters none declared; required body fields `schedule_id`, `schedule_details`, `account_id`, `amount`, `currency_code`, `processing_code`; response statuses 200, 201, 400, 403, 500; error codes in examples none; events `scheduler-payments-scheduled-payments-1`, `scheduler-payments-scheduled-payments-execution-1`.
- **`POST /v1/transfers`** (`post-v1-create-transfer-schedules`): security `BearerAuth`; required parameters none declared; required body fields `schedule_id`, `schedule_details`, `transfers`; response statuses 200, 201, 400, 403, 500; error codes in examples none; events `scheduler-payments-scheduled-payments-1`, `scheduler-payments-scheduled-payments-execution-1`.
- **`POST /v1/pre-schedules`** (`post-pre-schedules`): security `BearerAuth`; required parameters none declared; required body fields `schedule_id`, `schedule_details`, `account_id`, `amount`, `currency_code`, `processing_code`; response statuses 200, 201, 400, 403, 500; error codes in examples none; events `scheduler-payments-scheduled-payments-1`, `scheduler-payments-scheduled-payments-execution-1`.
- **`POST /v1/pre-schedules/bulk`** (`post-bulk-pre-schedules`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 202, 400, 403, 500; error codes in examples none; events `scheduler-payments-bulk-pre-scheduled-payments-1`, `scheduler-payments-scheduled-payments-1`, `scheduler-payments-scheduled-payments-execution-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-payments-v1-force-cancel` | `authorization-authorization-cancellation-event-1` |
| `post-payments-v2-cancel` | `authorization-authorization-cancellation-event-1` |
| `post-payments-v1-force` | `authorization-authorization-event-1` |
| `post-payments-v1-payments` | `authorization-authorization-event-1` |
| `post-bulk-pre-schedules` | `scheduler-payments-bulk-pre-scheduled-payments-1` |
| `post-bulk-pre-schedules` | `scheduler-payments-scheduled-payments-1` |
| `post-pre-schedules` | `scheduler-payments-scheduled-payments-1` |
| `post-v1-create-single-schedule` | `scheduler-payments-scheduled-payments-1` |
| `post-v1-create-transfer-schedules` | `scheduler-payments-scheduled-payments-1` |
| `post-bulk-pre-schedules` | `scheduler-payments-scheduled-payments-execution-1` |
| `post-pre-schedules` | `scheduler-payments-scheduled-payments-execution-1` |
| `post-v1-create-single-schedule` | `scheduler-payments-scheduled-payments-execution-1` |
| `post-v1-create-transfer-schedules` | `scheduler-payments-scheduled-payments-execution-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `authorization-authorization-cancellation-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-cancellation-event-1 | 2 | KU-EVT-catalogue-other-domains |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |
| `platform-authorization-platform-authorization-1` | platform | 1 | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 | 32 | KU-EVT-catalogue-other-domains |
| `scheduler-payments-bulk-pre-scheduled-payments-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-bulk-pre-scheduled-payments-1 | 1 | KU-EVT-catalogue-scheduler |
| `scheduler-payments-scheduled-payments-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1 | 7 | KU-EVT-catalogue-scheduler |
| `scheduler-payments-scheduled-payments-execution-1` | scheduler | 1 | https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-execution-1 | 7 | KU-EVT-catalogue-scheduler |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/payments-data-events.md`: updatedAt 2026-03-18T15:14:53.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 7 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/payments-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payments-data-events | `a866477d5b82e5e3…` | 2026-03-18T15:14:53.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--force-operations` — API reference: Core platform - Payment methods — Force operations
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-core-platform-payment-scheduler-beta--schedules` — API reference: Core platform - Payment scheduler — Schedules
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-scheduler` — Event catalogue: scheduler
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
