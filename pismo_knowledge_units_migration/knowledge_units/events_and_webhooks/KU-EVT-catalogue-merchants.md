---
ku_id: KU-EVT-catalogue-merchants
title: 'Event catalogue: merchants'
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
- cancel-split-request
- createAdvancementRequestForMerchant
- createMerchant
- merchant-transaction-advancement
- merchants-advancements
- post-merchant-transaction-cancel
- post-merchant-transaction-sale
- post-split-request
- updateMerchant
- updateMerchantStatus
related_kus:
- KU-API-seller-management-merchant-advance--merchant-advancement
- KU-API-seller-management-merchants--merchant
- KU-API-seller-management-merchants--merchant-advancement
- KU-API-seller-management-transactions--merchant-transactions
- KU-API-seller-management-transactions--split-requests
- KU-EVT-merchant-advancements-data-events
- KU-EVT-merchants-data-events
- KU-SELL-managing-merchant-transactions
events:
- merchants-advancement-request-1
- merchants-advancement-transaction-create-1
- merchants-merchant-created-1
- merchants-merchant-transaction-created-1
- merchants-merchant-updated-1
---

# Event catalogue: merchants

**KU ID:** `KU-EVT-catalogue-merchants` · **Category:** Events and webhooks · **Type:** event catalogue (from reference tables)

## Purpose and scope

Catalogue of 5 event type(s) whose inventory domain is merchants, with the operations that emit them. The domain and version columns are guesses recorded in the inventory table itself (`domain_guess`, `version_guess`), not Pismo classifications.

**Payload fields, delivery guarantees and ordering for these events are not documented in the available source corpus**: the event pages under `/events/` were not collected (robots.txt disallows them). For delivery mechanics see the event-delivery guide KUs.

## Event types

| Event slug | Domain (guess) | Version (guess) | Event page | Emitting operations (count in inventory) | Specification files |
| --- | --- | --- | --- | --- | --- |
| `merchants-advancement-request-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-advancement-request-1 | 2 | Seller_management_-_Merchant_advance;Seller_management_-_Merchants |
| `merchants-advancement-transaction-create-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-advancement-transaction-create-1 | 1 | Seller_management_-_Merchant_advance |
| `merchants-merchant-created-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-merchant-created-1 | 1 | Seller_management_-_Merchants |
| `merchants-merchant-transaction-created-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 | 5 | Seller_management_-_Merchant_advance;Seller_management_-_Transactions |
| `merchants-merchant-updated-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-merchant-updated-1 | 2 | Seller_management_-_Merchants |

## Operations that emit these events

From `api-reference-data/endpoint_event_map.csv`.

| Event slug | Method and path | operationId | Specification | API-reference KU |
| --- | --- | --- | --- | --- |
| `merchants-advancement-request-1` | `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements` | `merchants-advancements` | `Seller_management_-_Merchant_advance` | KU-API-seller-management-merchant-advance--merchant-advancement |
| `merchants-advancement-request-1` | `POST /v2/merchants/{merchantId}/advancements` | `createAdvancementRequestForMerchant` | `Seller_management_-_Merchants` | KU-API-seller-management-merchants--merchant-advancement |
| `merchants-advancement-transaction-create-1` | `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/transactions` | `merchant-transaction-advancement` | `Seller_management_-_Merchant_advance` | KU-API-seller-management-merchant-advance--merchant-advancement |
| `merchants-merchant-created-1` | `POST /v1/merchants` | `createMerchant` | `Seller_management_-_Merchants` | KU-API-seller-management-merchants--merchant |
| `merchants-merchant-transaction-created-1` | `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/transactions` | `merchant-transaction-advancement` | `Seller_management_-_Merchant_advance` | KU-API-seller-management-merchant-advance--merchant-advancement |
| `merchants-merchant-transaction-created-1` | `POST /v1/transactions/{merchantTransactionId}/split` | `post-split-request` | `Seller_management_-_Transactions` | KU-API-seller-management-transactions--split-requests |
| `merchants-merchant-transaction-created-1` | `POST /v1/transactions/{merchantTransactionId}/split/cancel` | `cancel-split-request` | `Seller_management_-_Transactions` | KU-API-seller-management-transactions--split-requests |
| `merchants-merchant-transaction-created-1` | `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` | `post-merchant-transaction-sale` | `Seller_management_-_Transactions` | KU-API-seller-management-transactions--merchant-transactions |
| `merchants-merchant-transaction-created-1` | `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel` | `post-merchant-transaction-cancel` | `Seller_management_-_Transactions` | KU-API-seller-management-transactions--merchant-transactions |
| `merchants-merchant-updated-1` | `PUT /v1/merchants/{merchantId}` | `updateMerchant` | `Seller_management_-_Merchants` | KU-API-seller-management-merchants--merchant |
| `merchants-merchant-updated-1` | `PUT /v1/merchants/{merchantId}/workflow/status` | `updateMerchantStatus` | `Seller_management_-_Merchants` | KU-API-seller-management-merchants--merchant |

## Guides that link to these events

- `merchants-advancement-request-1`: `KU-EVT-merchant-advancements-data-events`
- `merchants-advancement-transaction-create-1`: `KU-EVT-merchant-advancements-data-events`
- `merchants-merchant-transaction-created-1`: `KU-EVT-merchant-advancements-data-events`, `KU-EVT-merchants-data-events`, `KU-SELL-managing-merchant-transactions`

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-reference-data/event_type_inventory.csv` | rows: merchants-advancement-request-1, merchants-advancement-transaction-create-1, merchants-merchant-created-1, merchants-merchant-transaction-created-1, merchants-merchant-updated-1 | https://github.com/PismoDevEx/pismo-api-specs | `7eed7e3056f6f22e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | rows for these event slugs | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-seller-management-merchant-advance--merchant-advancement` — API reference: Seller management - Merchant advancements — Merchant advancement
- `KU-API-seller-management-merchants--merchant` — API reference: Seller management - Merchants — Merchant
- `KU-API-seller-management-merchants--merchant-advancement` — API reference: Seller management - Merchants — Merchant advancement
- `KU-API-seller-management-transactions--merchant-transactions` — API reference: Seller management - Transactions — Merchant transactions
- `KU-API-seller-management-transactions--split-requests` — API reference: Seller management - Transactions — Split requests
- `KU-EVT-merchant-advancements-data-events` — Seller management - Merchant advance
- `KU-EVT-merchants-data-events` — Seller management - Merchants
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
