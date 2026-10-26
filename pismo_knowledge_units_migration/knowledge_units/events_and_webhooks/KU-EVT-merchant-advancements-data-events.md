---
ku_id: KU-EVT-merchant-advancements-data-events
title: Seller management - Merchant advance
category: events_and_webhooks
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/data-and-reporting/merchant-advancements-data-events.md
  sha256: 836b5f704e8b82479ca0f4fe19bbcb9893b06f64635120e1feacd3f81c58706d
  url: https://developers.pismo.io/pismo-docs/docs/merchant-advancements-data-events
  role: primary_guide
  updated_at: '2026-03-18T15:15:22.000Z'
operations:
- merchants-advancements
related_kus:
- KU-API-seller-management-merchant-advance--merchant-advancement
- KU-EVT-catalogue-merchants
- KU-RPT-scheduled-reports
grouping_rationale: single source page
---

# Seller management - Merchant advance

**KU ID:** `KU-EVT-merchant-advancements-data-events` · **Category:** Events and webhooks · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/data-and-reporting/merchant-advancements-data-events.md`:

> This table lists the merchant advancement endpoints and triggers and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/data-and-reporting/merchant-advancements-data-events.md`: Seller management - Merchant advance

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/data-and-reporting/merchant-advancements-data-events.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/merchant-advancements-data-events · updatedAt: 2026-03-18T15:15:22.000Z

<!-- source:begin path=docs/data-and-reporting/merchant-advancements-data-events.md part=0-end -->

# Seller management - Merchant advance

This table lists the merchant advancement endpoints and triggers and the events they generate. For information on setting up event notifications, see the [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

| Endpoint/Trigger                                            | Event                                                                                                                                                                                                                                               |
| :---------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Simulate merchant advancement](https://developers.pismo.io/pismo-docs/reference/merchants-advancements) | [Merchant advancement request created](https://developers.pismo.io/events/docs/merchants-advancement-request-1)                                                                                                                                     |
| Merchant advancement transaction is created.                | [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) and [Merchant advancement transaction created](https://developers.pismo.io/events/docs/merchants-advancement-transaction-create-1) |
|                                                             |                                                                                                                                                                                                                                                     |
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements` | `merchants-advancements` | Simulate merchant advancement | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |

### Operation essentials

- **`POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements`** (`merchants-advancements`): security not declared; required parameters `Authorization` (header), `marketplaceId` (path), `merchantId` (path); required body fields `begin_date`, `request_date`, `amount`, `real_time_settlement`; response statuses 200, 400, 404; error codes in examples `EPT0303`, `EPT0303`; events `merchants-advancement-request-1`.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `merchants-advancements` | `merchants-advancement-request-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `merchants-advancement-request-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-advancement-request-1 | 2 | KU-EVT-catalogue-merchants |
| `merchants-advancement-transaction-create-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-advancement-transaction-create-1 | 1 | KU-EVT-catalogue-merchants |
| `merchants-merchant-transaction-created-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 | 5 | KU-EVT-catalogue-merchants |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/data-and-reporting/merchant-advancements-data-events.md`: updatedAt 2026-03-18T15:15:22.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- The source links to 3 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/data-and-reporting/merchant-advancements-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/merchant-advancements-data-events | `836b5f704e8b8247…` | 2026-03-18T15:15:22.000Z |

## Related knowledge units

- `KU-API-seller-management-merchant-advance--merchant-advancement` — API reference: Seller management - Merchant advancements — Merchant advancement
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
