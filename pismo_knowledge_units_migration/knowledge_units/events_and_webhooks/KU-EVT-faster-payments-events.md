---
ku_id: KU-EVT-faster-payments-events
title: Instant payments - Faster Payments
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/faster-payments-events.md
  sha256: 40c5fceac36da3982d643706fa47b3fea2b954ed4a41148a6797c4602302e412
  url: https://developers.pismo.io/pismo-docs/docs/faster-payments-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:15.000Z'
operations:
- post-create-fps
related_kus:
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-EVT-catalogue-fps
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Instant payments - Faster Payments

**KU ID:** `KU-EVT-faster-payments-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/faster-payments-events.md`:

> This table lists the Faster Payments endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/faster-payments-events.md`: Instant payments - Faster Payments

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/faster-payments-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/faster-payments-events · updatedAt: 2026-03-18T15:15:15.000Z

<!-- source:begin path=docs/data-and-reporting/faster-payments-events.md part=0-end -->

# Instant payments - Faster Payments

This table lists the Faster Payments endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                                                                | Event                                                                                     |
| :-------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| [Send Faster payment](https://developers.pismo.io/pismo-docs/reference/post-create-fps) | [Faster Payment payment processed](https://developers.pismo.io/events/docs/fps-fps-out-1) |
| When Faster inbound payment is received                                                 | [FPS inbound payment processed](https://developers.pismo.io/events/docs/fps-fps-in-1)     |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/payments/fps/out` | `post-create-fps` | Send Faster Payment [beta] | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |

### Operation essentials

- **`POST /v1/payments/fps/out`** (`post-create-fps`): security not declared; required parameters `Authorization` (header), `Idempotency-key` (header); required body fields `end_to_end_id`, `creditor_account`, `scheme_payment_type`, `currency`; response statuses 201, 400, 403, 404, 409, 429, 500, 502; error codes in examples `EFPS0004`, `EFPS0016`, `EFPS0019`, `EFPS0025`, `EFPS0029`, `EFPS0037`, `EFPS0038`, `EFPS0039`, `EFPS0046`, `EFPS0047`, `EFPS0073`, `EFPS0002`, `EFPS0021`, `EFPS0033`, `EFPS0034`, `EFPS0035`, `EFPS0040`, `EFPS0041`, `EFPS0010`, `EFPS0018`, `EFPS0028`, `EFPS0031`, `EFPS0022`, `EFPS0036`, `EFPS0015`, `EFPS0006`, `EFPS0009`, `EFPS0011`, `EFPS0012`, `EFPS0017`, `EFPS0020`, `EFPS0023`, `EFPS0024`, `EFPS0026`, `EFPS0027`, `EFPS0030`, `EFPS0032`, `EFPS0014`; events `fps-fps-out-return-status-change-1`, `fps-fps-out-status-change-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-create-fps` | `fps-fps-out-return-status-change-1` |
| `post-create-fps` | `fps-fps-out-status-change-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/faster-payments-events.md`: updatedAt 2026-03-18T15:15:15.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/faster-payments-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/faster-payments-events | `40c5fceac36da398…` | 2026-03-18T15:15:15.000Z |

## Related knowledge units

- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-EVT-catalogue-fps` — Event catalogue: fps
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
