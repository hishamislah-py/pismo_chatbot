---
ku_id: KU-SELL-get-started-seller-management
title: Get started with seller management
category: seller_management
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/seller-management/get-started-with-seller-management.md
  sha256: 53a35e62bf02ba3e5da9ed82da932dc60f149464206132ae76b15a82677311f0
  url: https://developers.pismo.io/pismo-docs/docs/get-started-with-seller-management
  role: primary_guide
  updated_at: '2026-06-10T18:48:00.000Z'
- path: docs/get-started/get-started-building-seller-management.md
  sha256: 5e9de8f4191262855e74fc95c15a8dba6271c60450bb70232a0ccd3084a27fe3
  url: https://developers.pismo.io/pismo-docs/docs/get-started-building-seller-management
  role: primary_guide
  updated_at: '2026-06-29T19:37:33.000Z'
operations:
- CreateProgramBasedOnTemplate
- PostCreditorsOperations
- createMerchant
related_kus:
- KU-API-platform-setup-programs--programs-part-01
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-API-seller-management-merchants--merchant
- KU-EVT-catalogue-marketplace
- KU-EVT-catalogue-merchants
- KU-EVT-catalogue-other-domains
- KU-SELL-seller-management-overview-and-onboarding
- KU-SELL-seller-marketplace-implementation-steps
grouping_rationale: Identical bodies (duplicate pages).
---

# Get started with seller management

**KU ID:** `KU-SELL-get-started-seller-management` · **Category:** Seller management · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Identical bodies (duplicate pages).

Scope as stated in `docs/seller-management/get-started-with-seller-management.md`:

> The Pismo platform offers Seller management APIs to help you manage digital marketplaces, merchants, receivables schedules, rates and fees, advancements, and settlements. This section contains detailed steps for this and other configurations within the seller management flow, which you accomplish using the API endpoints.

Scope as stated in `docs/get-started/get-started-building-seller-management.md`:

> The Pismo platform offers Seller management APIs to help you manage digital marketplaces, merchants, receivables schedules, rates and fees, advancements, and settlements. This section contains detailed steps for this and other configurations within the seller management flow, which you accomplish using the API endpoints.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/seller-management/get-started-with-seller-management.md`: Get started with Seller management; How to get started; Overview of required onboarding; Overview of Seller management; [Step 1: Plan Seller marketplaces](https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces); [Step 2: Create program for the marketplace](https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace); [Step 3: Define processing codes](https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes); [Step 4: Running Seller marketplace operations](https://developers.pismo.io/pismo-docs/docs/step-4-running-marketplace-operations); [Step 5: Test](step-5-test-seller-marketplace); [Step 6: Monitor](https://developers.pismo.io/pismo-docs/docs/step-6-monitor-seller-marketplace)
- `docs/get-started/get-started-building-seller-management.md`: Get started with Seller management; How to get started; Overview of required onboarding; Overview of Seller management; [Step 1: Plan Seller marketplaces](https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces); [Step 2: Create program for the marketplace](https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace); [Step 3: Define processing codes](https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes); [Step 4: Running Seller marketplace operations](https://developers.pismo.io/pismo-docs/docs/step-4-running-marketplace-operations); [Step 5: Test](step-5-test-seller-marketplace); [Step 6: Monitor](https://developers.pismo.io/pismo-docs/docs/step-6-monitor-seller-marketplace)

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/seller-management/get-started-with-seller-management.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-with-seller-management · updatedAt: 2026-06-10T18:48:00.000Z

<!-- source:begin path=docs/seller-management/get-started-with-seller-management.md part=0-end -->

# Get started with Seller management

The Pismo platform offers Seller management APIs to help you manage digital marketplaces, merchants, receivables schedules, rates and fees, advancements, and settlements. This section contains detailed steps for this and other configurations within the seller management flow, which you accomplish using the API endpoints.

# How to get started

The Pismo support team works closely with your team to create seller marketplaces that match your business needs. If you're already using other Pismo solutions, you can skip some steps. However, you should make sure you understand the following onboarding steps.

# Overview of required onboarding

The following steps summarize how you work with Pismo and use the Pismo platform to set up your digital marketplace. The [Seller management onboarding guide](https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding) describes these steps in detail.

1. [Create your marketplace](https://developers.pismo.io/pismo-docs/reference/postmarketplacesv2).
2. Create a Merchant program using [Create program based on template](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) with `type` set to `MERCHANT`.
3. Use [Create merchant](https://developers.pismo.io/pismo-docs/reference/createmerchant) to create one or more merchants, representing businesses, setting `program_id` to the ID of the Merchant program you created in step 2. Make sure you create a creditor for each merchant by filling out the `Creditor` object fields in the endpoint. You configure the MDR, sales tax, and any other fees the merchant has to pay in the `Creditor` object.
4. For each creditor, use [Create creditor operation](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations) to configure the MDR, sales tax, and any other fees the merchant has to pay.
5. Use [Link merchant to marketplace](https://developers.pismo.io/pismo-docs/reference/postlinkmerchanttomarketplacev1) to add the merchants to the marketplace.

# Overview of Seller management

Once you've completed the required onboarding, you can follow the rest of the steps in this get started guide starting with [planning](https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces).

### [Step 1: Plan Seller marketplaces](https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces)

Identify the business decisions to consider.

### [Step 2: Create program for the marketplace](https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace)

Build the foundational processes and rules for your marketplace.

### [Step 3: Define processing codes](https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes)

Define the processing codes that integrate with the seller rules.

### [Step 4: Running Seller marketplace operations](https://developers.pismo.io/pismo-docs/docs/step-4-running-marketplace-operations)

Understand how to manage sellers day-to-day and oversee seller marketplace operations.

### [Step 5: Test](step-5-test-seller-marketplace)

Ensure the marketplace works as expected before launch.

### [Step 6: Monitor](https://developers.pismo.io/pismo-docs/docs/step-6-monitor-seller-marketplace)

Continuously monitor your marketplace and provide ongoing seller support and settlement.

<br />
<!-- source:end -->

### Source 2: `docs/get-started/get-started-building-seller-management.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/get-started-building-seller-management · updatedAt: 2026-06-29T19:37:33.000Z

<!-- source:begin path=docs/get-started/get-started-building-seller-management.md part=0-end -->

# Get started with Seller management  

The Pismo platform offers Seller management APIs to help you manage digital marketplaces, merchants, receivables schedules, rates and fees, advancements, and settlements. This section contains detailed steps for this and other configurations within the seller management flow, which you accomplish using the API endpoints.

# How to get started

The Pismo support team works closely with your team to create seller marketplaces that match your business needs. If you're already using other Pismo solutions, you can skip some steps. However, you should make sure you understand the following onboarding steps.

# Overview of required onboarding

The following steps summarize how you work with Pismo and use the Pismo platform to set up your digital marketplace. The [Seller management onboarding guide](https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding) describes these steps in detail.

1. [Create your marketplace](https://developers.pismo.io/pismo-docs/reference/postmarketplacesv2).
2. Create a Merchant program using [Create program based on template](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) with `type` set to `MERCHANT`.
3. Use [Create merchant](https://developers.pismo.io/pismo-docs/reference/createmerchant) to create one or more merchants, representing businesses, setting `program_id` to the ID of the Merchant program you created in step 2. Make sure you create a creditor for each merchant by filling out the `Creditor` object fields in the endpoint. You configure the MDR, sales tax, and any other fees the merchant has to pay in the `Creditor` object.
4. For each creditor, use [Create creditor operation](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations) to configure the MDR, sales tax, and any other fees the merchant has to pay.
5. Use [Link merchant to marketplace](https://developers.pismo.io/pismo-docs/reference/postlinkmerchanttomarketplacev1) to add the merchants to the marketplace.

# Overview of Seller management

Once you've completed the required onboarding, you can follow the rest of the steps in this get started guide starting with [planning](https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces).

### [Step 1: Plan Seller marketplaces](https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces)

Identify the business decisions to consider.

### [Step 2: Create program for the marketplace](https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace)

Build the foundational processes and rules for your marketplace.

### [Step 3: Define processing codes](https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes)

Define the processing codes that integrate with the seller rules.

### [Step 4: Running Seller marketplace operations](https://developers.pismo.io/pismo-docs/docs/step-4-running-marketplace-operations)

Understand how to manage sellers day-to-day and oversee seller marketplace operations.

### [Step 5: Test](step-5-test-seller-marketplace)

Ensure the marketplace works as expected before launch.

### [Step 6: Monitor](https://developers.pismo.io/pismo-docs/docs/step-6-monitor-seller-marketplace)

Continuously monitor your marketplace and provide ongoing seller support and settlement.

<br />
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /v1/merchants` | `createMerchant` | Create merchant | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant |
| `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | Create creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |

### Operation essentials

- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /v1/merchants`** (`createMerchant`): security `BearerAuth`; required parameters none declared; required body fields `document_number`, `name`, `email`; response statuses 201, 400, 401, 500; error codes in examples none; events `merchants-merchant-created-1`.
- **`POST /marketplaces/{marketplaceId}/creditors-operations`** (`PostCreditorsOperations`): security `BearerAuth`; required parameters `marketplaceId` (path); required body fields `creditor_id`, `first_installment_days_to_payment`, `installments`, `n_installment_days_to_payment`; response statuses 200, 400, 401, 500; error codes in examples none; events `marketplace-marketplace-creditor-operation-created-1`.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `postmarketplacesv2` | Create marketplace; Create your marketplace; marketplace | not found in the current OpenAPI specifications. Name-based inference: link text "Create marketplace" equals the endpoint name "Create marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. |
| `postlinkmerchanttomarketplacev1` | Link merchant and marketplace; Link merchant to marketplace | not found in the current OpenAPI specifications. Name-based inference: link text "Link merchant and marketplace" equals the endpoint name "Link merchant and marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `PostCreditorsOperations` | `marketplace-marketplace-creditor-operation-created-1` |
| `createMerchant` | `merchants-merchant-created-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/seller-management/get-started-with-seller-management.md`: updatedAt 2026-06-10T18:48:00.000Z.
- `docs/get-started/get-started-building-seller-management.md`: updatedAt 2026-06-29T19:37:33.000Z.
- Links to `postmarketplacesv2`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Create marketplace" equals the endpoint name "Create marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier.
- Links to `postlinkmerchanttomarketplacev1`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Link merchant and marketplace" equals the endpoint name "Link merchant and marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier.

## Conflicts, caveats and evidence gaps

- The grouped source pages have identical bodies (published twice under different URLs); both are kept verbatim for traceability.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/seller-management/get-started-with-seller-management.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-with-seller-management | `53a35e62bf02ba3e…` | 2026-06-10T18:48:00.000Z |
| `docs/get-started/get-started-building-seller-management.md` | whole document | https://developers.pismo.io/pismo-docs/docs/get-started-building-seller-management | `5e9de8f419126285…` | 2026-06-29T19:37:33.000Z |

## Related knowledge units

- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-API-seller-management-merchants--merchant` — API reference: Seller management - Merchants — Merchant
- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
