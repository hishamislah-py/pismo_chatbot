---
ku_id: KU-EVT-marketplace-data-events
title: Seller management - Marketplace
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/marketplace-data-events.md
  sha256: d25cb8b6cad186a943cd60d5c7704964ee07a772c070e8daa389e0419b55da20
  url: https://developers.pismo.io/pismo-docs/docs/marketplace-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:19.000Z'
operations:
- DeleteCreditorOperationById
- PostCreditorsOperations
- PutUpdateCreditorOperationById
related_kus:
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-EVT-catalogue-marketplace
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Seller management - Marketplace

**KU ID:** `KU-EVT-marketplace-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/marketplace-data-events.md`:

> This table lists the marketplace endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/marketplace-data-events.md`: Seller management - Marketplace

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/marketplace-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/marketplace-data-events · updatedAt: 2026-03-18T15:15:19.000Z

<!-- source:begin path=docs/data-and-reporting/marketplace-data-events.md part=0-end -->

# Seller management - Marketplace

This table lists the marketplace endpoints and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint                                                         | Event                                                                                                                                  |
| :--------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------- |
| [Update marketplace](https://developers.pismo.io/pismo-docs/reference/putupdatemarketplacev1)                 | [Marketplace updated](https://developers.pismo.io/events/docs/marketplace-marketplace-updated-1)                                       |
| [Create creditors operation](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations)        | [Marketplace creditor operation created](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-created-1) |
| [Update creditors operation](https://developers.pismo.io/pismo-docs/reference/putupdatecreditoroperationbyid) | [Marketplace creditor operation updated](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1) |
| [Delete creditors operation](https://developers.pismo.io/pismo-docs/reference/deletecreditoroperationbyid)    | [Marketplace creditor operation deleted](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-deleted-1) |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | Create creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `PUT /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `PutUpdateCreditorOperationById` | Update creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `DELETE /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `DeleteCreditorOperationById` | Delete creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |

### Operation essentials

- **`POST /marketplaces/{marketplaceId}/creditors-operations`** (`PostCreditorsOperations`): security `BearerAuth`; required parameters `marketplaceId` (path); required body fields `creditor_id`, `first_installment_days_to_payment`, `installments`, `n_installment_days_to_payment`; response statuses 200, 400, 401, 500; error codes in examples none; events `marketplace-marketplace-creditor-operation-created-1`.
- **`PUT /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}`** (`PutUpdateCreditorOperationById`): security `BearerAuth`; required parameters `creditorOperationId` (path), `marketplaceId` (path); required body fields `creditor_id`, `first_installment_days_to_payment`, `installments`, `n_installment_days_to_payment`; response statuses 200, 400, 401, 500; error codes in examples none; events `marketplace-marketplace-creditor-operation-updated-1`.
- **`DELETE /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}`** (`DeleteCreditorOperationById`): security `BearerAuth`; required parameters `creditorOperationId` (path), `marketplaceId` (path); required body fields none declared; response statuses 200, 400, 401, 404, 500; error codes in examples none; events `marketplace-marketplace-creditor-operation-deleted-1`.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `putupdatemarketplacev1` | Update marketplace | not found in the current OpenAPI specifications. Name-based inference: link text "Update marketplace" equals the endpoint name "Update marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`updateMarketplace` (PATCH /v1/marketplaces/{marketplaceId})); no source states that it replaces the removed endpoint. |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `PostCreditorsOperations` | `marketplace-marketplace-creditor-operation-created-1` |
| `DeleteCreditorOperationById` | `marketplace-marketplace-creditor-operation-deleted-1` |
| `PutUpdateCreditorOperationById` | `marketplace-marketplace-creditor-operation-updated-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `marketplace-marketplace-creditor-operation-created-1` | marketplace | 1 | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-created-1 | 2 | KU-EVT-catalogue-marketplace |
| `marketplace-marketplace-creditor-operation-deleted-1` | marketplace | 1 | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-deleted-1 | 1 | KU-EVT-catalogue-marketplace |
| `marketplace-marketplace-creditor-operation-updated-1` | marketplace | 1 | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1 | 4 | KU-EVT-catalogue-marketplace |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/marketplace-data-events.md`: updatedAt 2026-03-18T15:15:19.000Z.
- Links to `putupdatemarketplacev1`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Update marketplace" equals the endpoint name "Update marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`updateMarketplace` (PATCH /v1/marketplaces/{marketplaceId})); no source states that it replaces the removed endpoint.

## Conflicts, caveats and evidence gaps

- The source links to 4 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/marketplace-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/marketplace-data-events | `d25cb8b6cad186a9…` | 2026-03-18T15:15:19.000Z |

## Related knowledge units

- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
