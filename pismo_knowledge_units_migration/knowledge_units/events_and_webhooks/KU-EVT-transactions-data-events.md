---
ku_id: KU-EVT-transactions-data-events
title: Core platform - Transactions
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/transactions-data-events.md
  sha256: d4ddc80e5a16f35545d53205356611c0a97b8f4cb13dbed34f9cdd93b0aecef3
  url: https://developers.pismo.io/pismo-docs/docs/transactions-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:14:55.000Z'
operations:
- PostSetupTransactionType
related_kus:
- KU-API-core-platform-transactions--transaction-types
- KU-EVT-catalogue-transaction
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Core platform - Transactions

**KU ID:** `KU-EVT-transactions-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/transactions-data-events.md`:

> This table lists the endpoints or other source for transactions, transaction types, and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/transactions-data-events.md`: Core platform - Transactions

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/transactions-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transactions-data-events · updatedAt: 2026-03-18T15:14:55.000Z

<!-- source:begin path=docs/data-and-reporting/transactions-data-events.md part=0-end -->

# Core platform - Transactions

This table lists the endpoints or other source for transactions, transaction types, and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

**Note:** Table entries marked **N/A** indicate **Not Applicable**.

| Endpoint                                                | Event                                                                                                                                        |
| :------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------- |
| N/A                                                     | [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) occurs asynchronously when a transaction is created \* |
| N/A                                                     | [Transaction updated](https://developers.pismo.io/events/docs/transaction-update-1) occurs asynchronously when a transaction is updated      |
| **Transaction types**                                   |                                                                                                                                              |
| [Create transaction type](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) | [Transaction type created](https://developers.pismo.io/events/docs/transaction-types-creation-1)                                             |

> 🚧
>
> \* At this time, idempotency for the transaction [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) event must be controlled by the transaction `id` field.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/transaction-types` | `PostSetupTransactionType` | Create transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |

### Operation essentials

- **`POST /v1/transaction-types`** (`PostSetupTransactionType`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `description`, `credit`, `posted_transaction`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05001`, `WTRC08001`, `ETRC00001`; events `transaction-types-creation-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `PostSetupTransactionType` | `transaction-types-creation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `transaction-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-creation-1 | 7 | KU-EVT-catalogue-transaction |
| `transaction-types-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-types-creation-1 | 1 | KU-EVT-catalogue-transaction |
| `transaction-update-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-update-1 | 1 | KU-EVT-catalogue-transaction |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/transactions-data-events.md`: updatedAt 2026-03-18T15:14:55.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 3 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/transactions-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transactions-data-events | `d4ddc80e5a16f355…` | 2026-03-18T15:14:55.000Z |

## Related knowledge units

- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
