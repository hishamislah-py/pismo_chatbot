---
ku_id: KU-EVT-migrations-data-events
title: Migrations events
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/migrations-data-events.md
  sha256: c8e5a0825199ea76f96951f842c8907312dac948f7d5f491883a4cf316e2853a
  url: https://developers.pismo.io/pismo-docs/docs/migrations-data-events
  role: primary_guide
  updated_at: '2026-05-11T17:33:22.000Z'
operations:
- PostCardsV1
- PostStatementsV1
- PostTransactionsV1
related_kus:
- KU-API-migrations--card-migration
- KU-API-migrations--statement-migration
- KU-API-migrations--transaction-migration
- KU-EVT-catalogue-migration
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Migrations events

**KU ID:** `KU-EVT-migrations-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/migrations-data-events.md`:

> This table lists the migrations endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/migrations-data-events.md`: Migrations events

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/migrations-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/migrations-data-events · updatedAt: 2026-05-11T17:33:22.000Z

<!-- source:begin path=docs/data-and-reporting/migrations-data-events.md part=0-end -->

# Migrations events

This table lists the migrations endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                       | Event                                                                                                              |
| :--------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Accounts**                                   |                                                                                                                    |
| Migrate accounts                               | [Account migration started events](https://developers.pismo.io/events/docs/migration-account-incoming-1)           |
| Migrate accounts                               | [Account migration completed events](https://developers.pismo.io/events/docs/migration-account-outgoing-1)         |
| **Cards**                                      |                                                                                                                    |
| [Migrate cards](https://developers.pismo.io/pismo-docs/reference/postcardsv1)               | [Card migration started events](https://developers.pismo.io/events/docs/migration-card-incoming-1)                 |
| [Migrate cards](https://developers.pismo.io/pismo-docs/reference/postcardsv1)               | [Card migration completed events](https://developers.pismo.io/events/docs/migration-card-outgoing-1)               |
| **Statements**                                 |                                                                                                                    |
| [Migrate statements](https://developers.pismo.io/pismo-docs/reference/poststatementsv1)     | [Statement migration started events](https://developers.pismo.io/events/docs/migration-statement-incoming-1)       |
| [Migrate statements](https://developers.pismo.io/pismo-docs/reference/poststatementsv1)     | [Statement migration completed events](https://developers.pismo.io/events/docs/migration-statement-outgoing-1)     |
| **Transactions**                               |                                                                                                                    |
| [Migrate transactions](https://developers.pismo.io/pismo-docs/reference/posttransactionsv1) | [Transaction migration started events](https://developers.pismo.io/events/docs/migration-transaction-incoming-1)   |
| [Migrate transactions](https://developers.pismo.io/pismo-docs/reference/posttransactionsv1) | [Transaction migration completed events](https://developers.pismo.io/events/docs/migration-transaction-outgoing-1) |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/migrations/cards` | `PostCardsV1` | Migrate cards | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /v1/migrations/statements` | `PostStatementsV1` | Migrate statements | `api-specs/Migrations.yaml` | no | KU-API-migrations--statement-migration |
| `POST /v1/migrations/transactions` | `PostTransactionsV1` | Migrate transactions | `api-specs/Migrations.yaml` | no | KU-API-migrations--transaction-migration |

### Operation essentials

- **`POST /v1/migrations/cards`** (`PostCardsV1`): security `bearerAuth`; required parameters `Authorization` (header); required body fields `abu_enabled`, `bin`, `contactless_enabled`, `issuing_date`, `migration`, `mode`, `name`, `network`, `status`; response statuses 202, 400, 500; error codes in examples `MIGR00002`, `MIGR00001`; events `migration-card-incoming-1`, `migration-card-mode-outgoing-1`, `migration-card-outgoing-1`.
- **`POST /v1/migrations/statements`** (`PostStatementsV1`): security `bearerAuth`; required parameters `Authorization` (header); required body fields none declared; response statuses 202, 400, 500; error codes in examples `MIGR00002`, `MIGR00001`; events `migration-statement-incoming-1`, `migration-statement-outgoing-1`.
- **`POST /v1/migrations/transactions`** (`PostTransactionsV1`): security `bearerAuth`; required parameters `Authorization` (header); required body fields `migration`, `soft_descriptor`, `type`; response statuses 202, 400, 500; error codes in examples `MIGR00002`, `MIGR00001`; events `migration-instant-payment-outgoing-1`, `migration-organize-statement-outgoing-1`, `migration-payment-agreements-outgoing-1`, `migration-transaction-incoming-1`, `migration-transaction-outgoing-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `PostCardsV1` | `migration-card-incoming-1` |
| `PostCardsV1` | `migration-card-mode-outgoing-1` |
| `PostCardsV1` | `migration-card-outgoing-1` |
| `PostTransactionsV1` | `migration-instant-payment-outgoing-1` |
| `PostTransactionsV1` | `migration-organize-statement-outgoing-1` |
| `PostTransactionsV1` | `migration-payment-agreements-outgoing-1` |
| `PostStatementsV1` | `migration-statement-incoming-1` |
| `PostStatementsV1` | `migration-statement-outgoing-1` |
| `PostTransactionsV1` | `migration-transaction-incoming-1` |
| `PostTransactionsV1` | `migration-transaction-outgoing-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `migration-card-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-card-incoming-1 | 1 | KU-EVT-catalogue-migration |
| `migration-card-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-card-outgoing-1 | 1 | KU-EVT-catalogue-migration |
| `migration-statement-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-statement-incoming-1 | 1 | KU-EVT-catalogue-migration |
| `migration-statement-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-statement-outgoing-1 | 1 | KU-EVT-catalogue-migration |
| `migration-transaction-incoming-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-transaction-incoming-1 | 1 | KU-EVT-catalogue-migration |
| `migration-transaction-outgoing-1` | migration | 1 | https://developers.pismo.io/events/docs/migration-transaction-outgoing-1 | 1 | KU-EVT-catalogue-migration |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/migrations-data-events.md`: updatedAt 2026-05-11T17:33:22.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 8 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/migrations-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/migrations-data-events | `c8e5a0825199ea76…` | 2026-05-11T17:33:22.000Z |

## Related knowledge units

- `KU-API-migrations--card-migration` — API reference: Migrations — Card migration
- `KU-API-migrations--statement-migration` — API reference: Migrations — Statement migration
- `KU-API-migrations--transaction-migration` — API reference: Migrations — Transaction migration
- `KU-EVT-catalogue-migration` — Event catalogue: migration
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
