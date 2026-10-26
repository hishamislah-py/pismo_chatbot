---
ku_id: KU-EVT-catalogue-marketplace
title: 'Event catalogue: marketplace'
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
- DeleteCreditorOperationById
- PatchCreditorOperationByIdV1
- PostCreditorsOperations
- PostCreditorsOperationsV2
- PutCreditorsOperationsV2
- PutUpdateCreditorOperationById
- createMarketplace
- updateCreditor
- updateMarketplace
related_kus:
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-API-seller-management-merchants--merchant-creditor
- KU-API-seller-management-sellers--marketplace
- KU-EVT-marketplace-data-events
events:
- marketplace-marketplace-created-2
- marketplace-marketplace-creditor-operation-created-1
- marketplace-marketplace-creditor-operation-deleted-1
- marketplace-marketplace-creditor-operation-updated-1
- marketplace-marketplace-updated-2
---

# Event catalogue: marketplace

**KU ID:** `KU-EVT-catalogue-marketplace` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 5 event type(s) whose inventory domain is marketplace, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `marketplace-marketplace-created-2` | marketplace | 2 | https://developers.pismo.io/events/docs/marketplace-marketplace-created-2 | 1 | Seller_management_-_Sellers |
| `marketplace-marketplace-creditor-operation-created-1` | marketplace | 1 | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-created-1 | 2 | Seller_management_-_Marketplace |
| `marketplace-marketplace-creditor-operation-deleted-1` | marketplace | 1 | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-deleted-1 | 1 | Seller_management_-_Marketplace |
| `marketplace-marketplace-creditor-operation-updated-1` | marketplace | 1 | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1 | 4 | Seller_management_-_Marketplace;Seller_management_-_Merchants |
| `marketplace-marketplace-updated-2` | marketplace | 2 | https://developers.pismo.io/events/docs/marketplace-marketplace-updated-2 | 1 | Seller_management_-_Sellers |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `marketplace-marketplace-created-2` | `POST /v3/marketplaces` | `createMarketplace` | `Seller_management_-_Sellers` | KU-API-seller-management-sellers--marketplace |
| `marketplace-marketplace-creditor-operation-created-1` | `POST /v2/marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperationsV2` | `Seller_management_-_Marketplace` | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `marketplace-marketplace-creditor-operation-created-1` | `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | `Seller_management_-_Marketplace` | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `marketplace-marketplace-creditor-operation-deleted-1` | `DELETE /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `DeleteCreditorOperationById` | `Seller_management_-_Marketplace` | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `marketplace-marketplace-creditor-operation-updated-1` | `PUT /v2/marketplaces/{marketplaceId}/creditors-operations` | `PutCreditorsOperationsV2` | `Seller_management_-_Marketplace` | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `marketplace-marketplace-creditor-operation-updated-1` | `PATCH /v1/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `PatchCreditorOperationByIdV1` | `Seller_management_-_Marketplace` | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `marketplace-marketplace-creditor-operation-updated-1` | `PUT /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `PutUpdateCreditorOperationById` | `Seller_management_-_Marketplace` | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `marketplace-marketplace-creditor-operation-updated-1` | `PUT /v1/creditors/{creditorId}` | `updateCreditor` | `Seller_management_-_Merchants` | KU-API-seller-management-merchants--merchant-creditor |
| `marketplace-marketplace-updated-2` | `PATCH /v1/marketplaces/{marketplaceId}` | `updateMarketplace` | `Seller_management_-_Sellers` | KU-API-seller-management-sellers--marketplace |

## Guides that link to these events

- `marketplace-marketplace-creditor-operation-created-1`: `KU-EVT-marketplace-data-events`
- `marketplace-marketplace-creditor-operation-deleted-1`: `KU-EVT-marketplace-data-events`
- `marketplace-marketplace-creditor-operation-updated-1`: `KU-EVT-marketplace-data-events`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: marketplace-marketplace-created-2, marketplace-marketplace-creditor-operation-created-1, marketplace-marketplace-creditor-operation-deleted-1, marketplace-marketplace-creditor-operation-updated-1, marketplace-marketplace-updated-2 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-API-seller-management-merchants--merchant-creditor` — API reference: Seller management - Merchants — Merchant creditor
- `KU-API-seller-management-sellers--marketplace` — API reference: Seller management - Sellers — Marketplace
- `KU-EVT-marketplace-data-events` — Seller management - Marketplace
