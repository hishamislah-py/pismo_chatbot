---
ku_id: KU-LIFE-marketplace-endpoint-removal
title: Marketplace endpoints removed on 10/6/26 and guides that still reference them
category: api_lifecycle
ku_type: lifecycle_reference
lifecycle: lifecycle_reference
sources:
- path: docs/resources/api-endpoints-removed.md
  sha256: 56c7e4a8ba7d9b6f7eb4a3bd48037ef82b36e19f1cacc6d7584616782a710609
  url: https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed
  role: removal_register
  updated_at: '2026-10-08T20:06:59.000Z'
- path: changelog/2-october-2026.md
  sha256: cce711f798262309b879518ef73e866361a3f64d8458d965a09a3f5b2131d871
  url: https://developers.pismo.io/pismo-docs/changelog/2-october-2026
  role: changelog_post
  updated_at: ''
- path: changelog/7-july-2025.md
  sha256: e6dfaeba8920201786e8b5da6975dbc3efcc5a15cfc4a18e0af648fc4207f55b
  url: https://developers.pismo.io/pismo-docs/changelog/7-july-2025
  role: guide_reference
  updated_at: ''
- path: docs/data-and-reporting/marketplace-data-events.md
  sha256: d25cb8b6cad186a943cd60d5c7704964ee07a772c070e8daa389e0419b55da20
  url: https://developers.pismo.io/pismo-docs/docs/marketplace-data-events
  role: guide_reference
  updated_at: '2026-03-18T15:15:19.000Z'
- path: docs/get-started/get-started-building-seller-management.md
  sha256: 5e9de8f4191262855e74fc95c15a8dba6271c60450bb70232a0ccd3084a27fe3
  url: https://developers.pismo.io/pismo-docs/docs/get-started-building-seller-management
  role: guide_reference
  updated_at: '2026-06-29T19:37:33.000Z'
- path: docs/seller-management/get-started-with-seller-management.md
  sha256: 53a35e62bf02ba3e5da9ed82da932dc60f149464206132ae76b15a82677311f0
  url: https://developers.pismo.io/pismo-docs/docs/get-started-with-seller-management
  role: guide_reference
  updated_at: '2026-06-10T18:48:00.000Z'
- path: docs/seller-management/managing-merchant-transactions.md
  sha256: b4f8a0501fdd64eff39171a765e4a2f696478e6e02e21722168583450ed3c914
  url: https://developers.pismo.io/pismo-docs/docs/managing-merchant-transactions
  role: guide_reference
  updated_at: '2026-03-18T15:24:20.000Z'
- path: docs/seller-management/seller-management-onboarding.md
  sha256: 2c1d74837f41208f7e9a820b6ce83c6f1b3cf6b41abbe6fb15b8fca5df9dc733
  url: https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding
  role: guide_reference
  updated_at: '2026-06-28T23:14:38.000Z'
- path: docs/seller-management/seller-management-overview.md
  sha256: 5bf18137ff34ed2a5560df6d88efaf65a4b9ac77067e3b4c8d61678f4ac395de
  url: https://developers.pismo.io/pismo-docs/docs/seller-management-overview
  role: guide_reference
  updated_at: '2026-03-18T15:24:07.000Z'
- path: docs/seller-management/step-2-create-program-marketplace.md
  sha256: db4b5f4088862ee09d85dc8e79c25b2ba3bc598bc500767c5b076598ccf137aa
  url: https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace
  role: guide_reference
  updated_at: '2026-06-10T19:23:35.000Z'
- path: api-specs/Seller_management_-_Marketplace.yaml
  sha256: 8ffe617b35e772cca857f195c1384b6d7287d6e8bcbf553ed99c3eed14924d2b
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-specs/Seller_management_-_Merchant_advance.yaml
  sha256: 73496f0c5425362468ba3bad070f5b51fa7d9f17ffe9ac6c43558a3ac3ee86ed
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-specs/Seller_management_-_Sellers.yaml
  sha256: eb5d18c21f5848fe7db87917b88dfe2d23206e9b68f8382dc8c41745d518c00d
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-specs/Seller_management_-_Transactions.yaml
  sha256: f064908196c8f7cdd21e34e27572c6f95f92f3503251232b87c3d12d769ca000
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- DeleteCreditorOperationById
- DeleteMdrTaxV1
- GetCreditorOperationById
- GetCreditorOperationsByMerchantIDAndMarketplaceID
- GetCreditorsOperationsV2
- GetMarketPlaceByIdV2
- GetMarketplacesV1
- GetMdrTaxByIdV1
- GetMerchantsCreditorsV1
- PatchCreditorOperationByIdV1
- PostCreditorsOperations
- PostCreditorsOperationsV2
- PostMdrTaxV1
- PutCreditorsOperationsV2
- PutUpdateCreditorOperationById
- createMarketplace
- createMarketplaceMerchantsLink
- deleteMarketplaceMerchantLink
- get-merchant-balance
- get-sale-split-request-totals
- get-split-details
- get-split-requests
- getMarketplaceById
- getMarketplaces
- listMarketplaceMerchantsLinked
- merchant-transaction-advancement
- merchants-advancements
- merchants-advancements-data
- merchants-transactions
- post-merchant-transaction-cancel
- post-merchant-transaction-sale
- updateMarketplace
related_kus:
- KU-API-seller-management-marketplace--marketplace
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-API-seller-management-marketplace--marketplace-mdr-tax
- KU-API-seller-management-merchant-advance--merchant-advancement
- KU-API-seller-management-merchant-advance--merchant-advancement-transaction
- KU-API-seller-management-sellers--marketplace
- KU-API-seller-management-sellers--marketplace-merchants-links
- KU-API-seller-management-transactions--balance
- KU-API-seller-management-transactions--merchant-transactions
- KU-API-seller-management-transactions--split-requests
- KU-CHG-2-october-2026
- KU-EVT-marketplace-data-events
- KU-LIFE-api-endpoints-removed
- KU-SELL-get-started-seller-management
- KU-SELL-managing-merchant-transactions
- KU-SELL-seller-management-overview-and-onboarding
- KU-SELL-seller-marketplace-implementation-steps
---

# Marketplace endpoints removed on 10/6/26 and guides that still reference them

**KU ID:** `KU-LIFE-marketplace-endpoint-removal` · **Category:** API lifecycle · **Type:** lifecycle reference (assembled from quoted evidence)

## Purpose and scope

Answers: which marketplace endpoints were removed, when, which guides still instruct their use, and what the corpus says about replacements. Every statement below is a quotation or a structured extract of the cited source; nothing is inferred beyond what is labelled as inference.

## Removal evidence

### Removed-endpoints register (`docs/resources/api-endpoints-removed.md`)

| API | API section | Endpoint names (as published) | Endpoint URLs (as published; line breaks inside the source cell kept as ` ⏎ `) | Date removed (raw) |
| --- | --- | --- | --- | --- |
| Marketplace | Seller Management - Marketplace | List marketplace merchants; List marketplace merchants; Link merchant and marketplace; Delete merchant and marketplace link; Get marketplace; Update marketplace; Create marketplace | GET /marketplaces/v1/{'{marketplaceId}'}/ ⏎ merchants ⏎ GET /marketplace/v2/market ⏎ places/{'{marketplaceId'}/ ⏎ merchants ⏎ POST  /marketplaces/v1/{'{marketplaceId}'}/ ⏎ merchants/{'{merchantId}'} ⏎ DELETE /market ⏎ places/v1/{'{marketplaceId}'}/merchants/{'{merchantId}'} ⏎ GET /marketplace/v1/ ⏎ marketplaces/{'{marketplaceId}'} ⏎ PUT /marketplace/v1/ ⏎ marketplaces/{'{marketplaceId}'} ⏎ POST /marketplace/v2/ ⏎ marketplaces ⏎ <br /> | `10/6/26` |
| Seller Management - Marketplace | Marketplace | Create merchants relationships; Remove merchant relationship with all branches; Disable the merchant-branch relationship | POST marketplaces/\\{marketplaceId}/merchants/\\{merchantId}/branches ⏎ DELETE marketplaces/\\{marketplaceId}/merchants/\\{merchantId}/branches ⏎ DELETE\\ ⏎ marketplaces/\\{marketplaceId}/merchants/\\{merchantId}/branches/\\{merchantBranchId} | `2/11/2026` |

Date format: the register mixes formats (`10/6/26`, `7/24/2026`, `9/2025`). Rows such as `7/24/2026` and `6/30/2025` show month/day order, so `10/6/26` is read as 6 October 2026. This reading is a migration inference from the register itself; the raw value is kept above.

### Changelog record

`changelog/2-october-2026.md` (post dated “2 October 2026”):

> The following endpoints were decommissioned and removed from the Developers Portal and added to the [API endpoints removed](https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed) list.

> - List marketplace merchants V1
> - List marketplace merchants V2
> - Link merchant and marketplace
> - Delete merchant and marketplace link
> - Get marketplace V1
> - Update marketplace
> - Create marketplace V1
> - Create marketplace V2

Count conflict: the register lists the endpoint names `List marketplace merchants`, `List marketplace merchants`, `Link merchant and marketplace`, `Delete merchant and marketplace link`, `Get marketplace`, `Update marketplace`, `Create marketplace` for the 10/6/26 row, while the changelog lists 8 names (it separates “Create marketplace V1” and “Create marketplace V2”). Both are kept; see ISSUES_AND_GAPS.md.

## Guides and pages that still link to these endpoints

These links are to operation slugs that are not in the current OpenAPI specifications. The match between a slug and a removed endpoint is by the link text equal to the published endpoint name (inference, not an identifier match).

| Source file | Line | Link text | Slug | Knowledge unit |
| --- | --- | --- | --- | --- |
| `changelog/7-july-2025.md` | 343 | Link merchant and marketplace | `postlinkmerchanttomarketplacev1` | KU-CHG-7-july-2025 |
| `docs/data-and-reporting/marketplace-data-events.md` | 14 | Update marketplace | `putupdatemarketplacev1` | KU-EVT-marketplace-data-events |
| `docs/get-started/get-started-building-seller-management.md` | 20 | Create your marketplace | `postmarketplacesv2` | KU-SELL-get-started-seller-management |
| `docs/get-started/get-started-building-seller-management.md` | 24 | Link merchant to marketplace | `postlinkmerchanttomarketplacev1` | KU-SELL-get-started-seller-management |
| `docs/seller-management/get-started-with-seller-management.md` | 20 | Create your marketplace | `postmarketplacesv2` | KU-SELL-get-started-seller-management |
| `docs/seller-management/get-started-with-seller-management.md` | 24 | Link merchant to marketplace | `postlinkmerchanttomarketplacev1` | KU-SELL-get-started-seller-management |
| `docs/seller-management/managing-merchant-transactions.md` | 20 | marketplace | `postmarketplacesv2` | KU-SELL-managing-merchant-transactions |
| `docs/seller-management/managing-merchant-transactions.md` | 97 | Create marketplace | `postmarketplacesv2` | KU-SELL-managing-merchant-transactions |
| `docs/seller-management/managing-merchant-transactions.md` | 101 | List marketplace merchants | `getmerchantsbymarketplaceidv2` | KU-SELL-managing-merchant-transactions |
| `docs/seller-management/managing-merchant-transactions.md` | 101 | Create marketplace | `postmarketplacesv2` | KU-SELL-managing-merchant-transactions |
| `docs/seller-management/seller-management-onboarding.md` | 28 | Link merchant and marketplace | `postlinkmerchanttomarketplacev1` | KU-SELL-seller-management-overview-and-onboarding |
| `docs/seller-management/seller-management-onboarding.md` | 38 | Create marketplace | `postmarketplacesv2` | KU-SELL-seller-management-overview-and-onboarding |
| `docs/seller-management/seller-management-onboarding.md` | 42 | Link merchant and marketplace | `postlinkmerchanttomarketplacev1` | KU-SELL-seller-management-overview-and-onboarding |
| `docs/seller-management/seller-management-overview.md` | 59 | Create marketplace | `postmarketplacesv2` | KU-SELL-seller-management-overview-and-onboarding |
| `docs/seller-management/seller-management-overview.md` | 65 | Link merchant to marketplace | `postlinkmerchanttomarketplacev1` | KU-SELL-seller-management-overview-and-onboarding |
| `docs/seller-management/step-2-create-program-marketplace.md` | 24 | Link merchant and marketplace | `postlinkmerchanttomarketplacev1` | KU-SELL-seller-marketplace-implementation-steps |
| `docs/seller-management/step-2-create-program-marketplace.md` | 24 | Create marketplace | `postmarketplacesv2` | KU-SELL-seller-marketplace-implementation-steps |
| `docs/seller-management/step-2-create-program-marketplace.md` | 24 | Link merchant and marketplace | `postlinkmerchanttomarketplacev1` | KU-SELL-seller-marketplace-implementation-steps |

**Implementation guidance:** do not use these links as current instructions. The guides above are migrated verbatim and still describe the removed calls; their KUs carry a lifecycle warning.

## Current marketplace operations in the specifications

Operations whose path contains `marketplace` in the current Seller management specifications. **No source in the corpus states that any of them replaces a removed endpoint.** Similar names are not evidence of replacement.

| Method and path | operationId | Summary | Specification | Deprecated | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /v2/marketplaces/{marketplaceId}` | `GetMarketPlaceByIdV2` | Get marketplace V2 (deprecated) | `api-specs/Seller_management_-_Marketplace.yaml` | **yes** | KU-API-seller-management-marketplace--marketplace |
| `GET /v1/marketplaces` | `GetMarketplacesV1` | List marketplaces V1 (deprecated) | `api-specs/Seller_management_-_Marketplace.yaml` | **yes** | KU-API-seller-management-marketplace--marketplace |
| `GET /v2/marketplaces/{marketplaceId}/creditors-operations` | `GetCreditorsOperationsV2` | List marketplace creditor operations | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `PUT /v2/marketplaces/{marketplaceId}/creditors-operations` | `PutCreditorsOperationsV2` | Update creditor operations | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `POST /v2/marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperationsV2` | Create marketplace creditor operations | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | Create creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `PATCH /v1/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `PatchCreditorOperationByIdV1` | Patch creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `GET /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `GetCreditorOperationById` | Get creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `PUT /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `PutUpdateCreditorOperationById` | Update creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `DELETE /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` | `DeleteCreditorOperationById` | Delete creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `GET /marketplaces/{marketplaceId}/merchants/{merchantId}/creditors-operations` | `GetCreditorOperationsByMerchantIDAndMarketplaceID` | List creditor operations for marketplace and merchant | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `GET /marketplaces/v1/{marketplaceId}/merchants-creditors` | `GetMerchantsCreditorsV1` | List merchant creditors | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `GET /v1/marketplaces/{marketplaceId}/mdrtax` | `GetMdrTaxByIdV1` | Get MDR tax information | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-mdr-tax |
| `POST /v1/marketplaces/{marketplaceId}/mdrtax` | `PostMdrTaxV1` | Create MDR tax information | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-mdr-tax |
| `DELETE /v1/marketplaces/{marketplaceId}/mdrtax` | `DeleteMdrTaxV1` | Delete MDR tax information | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-mdr-tax |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements` | `merchants-advancements` | Simulate merchant advancement | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/transactions` | `merchant-transaction-advancement` | Simulate transaction advancement | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/{advancementId}` | `merchants-advancements-data` | Get advancement | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` | `merchants-transactions` | List transactions | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement-transaction |
| `GET /v3/marketplaces` | `getMarketplaces` | List marketplaces | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace |
| `POST /v3/marketplaces` | `createMarketplace` | Create marketplace V3 | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace |
| `GET /v3/marketplaces/{marketplaceId}` | `getMarketplaceById` | Get marketplace by ID | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace |
| `PATCH /v1/marketplaces/{marketplaceId}` | `updateMarketplace` | Update marketplace | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace |
| `GET /v1/marketplaces/{marketplaceId}/merchants` | `listMarketplaceMerchantsLinked` | List merchants linked to a marketplace | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace-merchants-links |
| `POST /v1/marketplaces/{marketplaceId}/merchants` | `createMarketplaceMerchantsLink` | Link marketplace to merchants | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace-merchants-links |
| `DELETE /v1/marketplaces/{marketplaceId}/merchants/{merchantId}` | `deleteMarketplaceMerchantLink` | Unlink marketplace and merchant | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace-merchants-links |
| `GET /v1/marketplaces/{marketplaceId}/split-requests` | `get-split-requests` | List split requests | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `GET /v1/marketplaces/{marketplaceId}/split-requests/{splitId}` | `get-split-details` | Get split request details | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `GET /v1/marketplaces/{marketplaceId}/split-requests/{parentId}/totals` | `get-sale-split-request-totals` | Get split request totals | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/balance` | `get-merchant-balance` | Get merchant balance | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--balance |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` | `post-merchant-transaction-sale` | Create merchant transaction | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--merchant-transactions |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel` | `post-merchant-transaction-cancel` | Cancel merchant transaction | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--merchant-transactions |

## Successor or replacement

Not documented in the available source corpus. The corpus contains no statement that a removed marketplace endpoint is replaced by another endpoint.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/resources/api-endpoints-removed.md` | whole document | https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed | `56c7e4a8ba7d9b6f…` | 2026-10-08T20:06:59.000Z |
| `changelog/2-october-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/2-october-2026 | `cce711f798262309…` | not stated |
| `changelog/7-july-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/7-july-2025 | `e6dfaeba89202017…` | not stated |
| `docs/data-and-reporting/marketplace-data-events.md` | whole document | https://developers.pismo.io/pismo-docs/docs/marketplace-data-events | `d25cb8b6cad186a9…` | 2026-03-18T15:15:19.000Z |
| `docs/get-started/get-started-building-seller-management.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-building-seller-management | `5e9de8f419126285…` | 2026-06-29T19:37:33.000Z |
| `docs/seller-management/get-started-with-seller-management.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-with-seller-management | `53a35e62bf02ba3e…` | 2026-06-10T18:48:00.000Z |
| `docs/seller-management/managing-merchant-transactions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/managing-merchant-transactions | `b4f8a0501fdd64ef…` | 2026-03-18T15:24:20.000Z |
| `docs/seller-management/seller-management-onboarding.md` | whole document | https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding | `2c1d74837f41208f…` | 2026-06-28T23:14:38.000Z |
| `docs/seller-management/seller-management-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/seller-management-overview | `5bf18137ff34ed2a…` | 2026-03-18T15:24:07.000Z |
| `docs/seller-management/step-2-create-program-marketplace.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace | `db4b5f4088862ee0…` | 2026-06-10T19:23:35.000Z |
| `api-specs/Seller_management_-_Marketplace.yaml` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `8ffe617b35e772cc…` | 2026-10-13T20:51:51+00:00 |
| `api-specs/Seller_management_-_Merchant_advance.yaml` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `73496f0c54253624…` | 2026-10-13T20:51:51+00:00 |
| `api-specs/Seller_management_-_Sellers.yaml` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `eb5d18c21f5848fe…` | 2026-10-13T20:51:51+00:00 |
| `api-specs/Seller_management_-_Transactions.yaml` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `f064908196c8f7cd…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-API-seller-management-marketplace--marketplace` — API reference: Seller management - Marketplace — Marketplace
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-API-seller-management-marketplace--marketplace-mdr-tax` — API reference: Seller management - Marketplace — Marketplace MDR tax
- `KU-API-seller-management-merchant-advance--merchant-advancement` — API reference: Seller management - Merchant advancements — Merchant advancement
- `KU-API-seller-management-merchant-advance--merchant-advancement-transaction` — API reference: Seller management - Merchant advancements — Merchant advancement transaction
- `KU-API-seller-management-sellers--marketplace` — API reference: Seller management - Sellers — Marketplace
- `KU-API-seller-management-sellers--marketplace-merchants-links` — API reference: Seller management - Sellers — Marketplace merchants links
- `KU-API-seller-management-transactions--balance` — API reference: Seller management - Transactions — Balance
- `KU-API-seller-management-transactions--merchant-transactions` — API reference: Seller management - Transactions — Merchant transactions
- `KU-API-seller-management-transactions--split-requests` — API reference: Seller management - Transactions — Split requests
- `KU-CHG-2-october-2026` — Changelog: 2 October 2026
- `KU-EVT-marketplace-data-events` — Seller management - Marketplace
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-SELL-get-started-seller-management` — Get started with seller management
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
