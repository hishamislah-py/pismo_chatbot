---
ku_id: KU-EVT-accounting-data-events
title: Core platform - Accounting
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/accounting-data-events.md
  sha256: d9d194faff76b5ab9f688486c71b2b49b605e7665eb44137afb84cdee3fab447
  url: https://developers.pismo.io/pismo-docs/docs/accounting-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:45.000Z'
operations:
- CreateAccountingEntry
related_kus:
- KU-API-core-platform-accounting--accounting-entry
- KU-EVT-catalogue-other-domains
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Core platform - Accounting

**KU ID:** `KU-EVT-accounting-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/accounting-data-events.md`:

> This table lists the accounting endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/accounting-data-events.md`: Core platform - Accounting

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/accounting-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/accounting-data-events · updatedAt: 2026-03-18T15:14:45.000Z

<!-- source:begin path=docs/data-and-reporting/accounting-data-events.md part=0-end -->

# Core platform - Accounting

This table lists the accounting endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                             | Event                                                                                           |
| :--------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| [Create accounting entry](https://developers.pismo.io/pismo-docs/reference/createaccountingentry) | [Accounting entry created](https://developers.pismo.io/events/docs/accounting-entry-creation-1) |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/accounting-entries` | `CreateAccountingEntry` | Create accounting entry | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-entry |

### Operation essentials

- **`POST /v1/accounting-entries`** (`CreateAccountingEntry`): security `BearerAuth`; required parameters none declared; required body fields `amount`, `entry_type_id`, `event_date`, `program_id`; response statuses 202, 400, 409; error codes in examples none; events `accounting-entry-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CreateAccountingEntry` | `accounting-entry-creation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `accounting-entry-creation-1` | accounting | 1 | https://developers.pismo.io/events/docs/accounting-entry-creation-1 | 4 | KU-EVT-catalogue-other-domains |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/accounting-data-events.md`: updatedAt 2026-03-18T15:14:45.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 1 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/accounting-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/accounting-data-events | `d9d194faff76b5ab…` | 2026-03-18T15:14:45.000Z |

## Related knowledge units

- `KU-API-core-platform-accounting--accounting-entry` — API reference: Core platform - Accounting — Accounting entry
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
