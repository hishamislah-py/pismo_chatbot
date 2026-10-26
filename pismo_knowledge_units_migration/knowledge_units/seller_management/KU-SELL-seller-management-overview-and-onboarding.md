---
ku_id: KU-SELL-seller-management-overview-and-onboarding
title: Seller management overview and onboarding
category: seller_management
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/seller-management/seller-management-overview.md
  sha256: 5bf18137ff34ed2a5560df6d88efaf65a4b9ac77067e3b4c8d61678f4ac395de
  url: https://developers.pismo.io/pismo-docs/docs/seller-management-overview
  role: primary_guide
  updated_at: '2026-03-18T15:24:07.000Z'
- path: docs/seller-management/seller-management-onboarding.md
  sha256: 2c1d74837f41208f7e9a820b6ce83c6f1b3cf6b41abbe6fb15b8fca5df9dc733
  url: https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding
  role: primary_guide
  updated_at: '2026-06-28T23:14:38.000Z'
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
- KU-GS-pismo-platform-onboarding
- KU-GS-setup-overview
- KU-PAY-payment-overview-and-instant-payments
- KU-SELL-get-started-seller-management
- KU-SELL-seller-marketplace-implementation-steps
grouping_rationale: Overview and onboarding.
---

# Seller management overview and onboarding

**KU ID:** `KU-SELL-seller-management-overview-and-onboarding` · **Category:** Seller management · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Overview and onboarding.

Scope as stated in `docs/seller-management/seller-management-overview.md`:

> Pismo Seller management provides a complete solution for managing merchants that sell products through online channels and at physical points of sale. Any business that needs to manage sellers can use the Seller management platform, including merchant banks, fintechs, marketplaces, and  payment facilitators.

Scope as stated in `docs/seller-management/seller-management-onboarding.md`:

> The Pismo platform provides seller management APIs for managing digital marketplaces, merchants, receivables schedules, rates and fees, advancements, and settlements. Onboarding steps must be completed in partnership with Pismo using the API endpoints or the UI.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/seller-management/seller-management-overview.md`: Seller management overview; Two main concepts in Seller management; Benefits of Pismo Seller management; Basic object structure; Organization (Org); Program; Marketplace; Merchant; Creditor; Marketplace creditor operation
- `docs/seller-management/seller-management-onboarding.md`: Seller management onboarding; Onboard an organization (tenant); Create the merchant program; Create merchants and associate creditors; Associating creditors with merchants; Create marketplaces; Link merchants to marketplaces; Create processing codes; Configure creditor operations

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 3 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/seller-management/seller-management-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/seller-management-overview · updatedAt: 2026-03-18T15:24:07.000Z

<!-- source:begin path=docs/seller-management/seller-management-overview.md part=0-end -->

# Seller management overview

Pismo Seller management provides a complete solution for managing merchants that sell products through online channels and at physical points of sale. Any business that needs to manage sellers can use the Seller management platform, including merchant banks, fintechs, marketplaces, and  payment facilitators.

When planning and implementing your seller marketplace, refer to [Seller management onboarding](https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding) and [Get started with seller management](https://developers.pismo.io/pismo-docs/docs/get-started-with-seller-management). To access Seller management in Control Center, your user role must have **Seller management admin** permission. The following sections provide a conceptual overview of seller management and the associated data models.

## Two main concepts in Seller management

* **Marketplace** – a grouping of merchants who sell products online or at physical points of sale. The marketplace applies a fee to sales.
* **Merchant** – an individual or business that sells products or services in the marketplace.

The platform supports all transaction types, including card network transactions processed outside the institution (off‑us and open loop), card transactions processed within the same institution (on‑us), transfers between accounts in the same institution (closed loop), and transfers between different institutions through  [instant payments](https://developers.pismo.io/pismo-docs/docs/instant-payments-overview).

<Image alt="Diagram showing the areas of Seller management in the Pismo platform." align="center" src="https://files.readme.io/d8602b9-Seller_management_overview_02_V2.png" />

Pismo Seller management provides a solution for every aspect of seller management. The platform can manage:

* **Marketplaces** – a marketplace can include one or more sellers.
* **Merchants** – a merchant can link to one or more marketplaces.
* **Merchant accounts** – a merchant account receives funds from sales. In Seller management, merchant accounts are called *creditor accounts* and link to a [creditor](#creditor) object.
* **Rates and fees** – charges that the merchant incurs on sales. In Seller management, you configure these within the [marketplace  creditor operation](https://developers.pismo.io/pismo-docs/docs/seller-management-overview#marketplace-creditor-operation) object. Rates and fees may vary by transaction type.
* **Settlement** – the process of finalizing a transaction and transferring funds to the merchant’s account. Settlement can occur inside Pismo (internal transfer) or outside Pismo (external transfer).
* **Schedules** – define when  settlement occurs, such as 2 days after the sale, 30 days after the sale, or the same day as the sale.
* **Advancements** – merchants can request an advancement before the scheduled settlement date. An additional rate or fee applies.

<Image alt="Diagram showing hierarchy and transaction features for merchant and creditor" align="center" src="https://files.readme.io/e227120-Seller_management_overview_03_V4.png" />

## Benefits of Pismo Seller management

* **Manage vendors and buyers on the same platform.** Seller management manages vendors, and you can use other Pismo services such as Accounts and Core Banking to manage buyers.
* **Control all settlement processes, from authorization to payment.** Settlements can be internal to the Pismo platform or external using account identifiers.
* **Use any payment scheme.** The platform supports card network, closed-loop, and other payment methods.
* **Create flexible receivables schedules.** Use creditor operations to define conditions for each transaction type, set payment timing, and configure merchant discount rates (MDRs) and other fees.
* **Handle transactions from on-us and off-us merchants.** The platform supports all transaction types. You can use card services for off‑us transactions, payment services for on‑us transactions, or authorize transactions externally and send the authorized transactions to the Pismo platform.

# Basic object structure

This section explains the main objects that make up your digital marketplace.

## Organization (Org)

The organization object defines your company or enterprise. It contains one or more programs. For more information, refer to [Organization](https://developers.pismo.io/pismo-docs/docs/setup-overview#organization).

## Program

The program object defines a set of parameters for credit, debit, or pre-paid accounts. In Seller management, it defines parameters for a marketplace account. For more information, refer to [Program types and parameters](https://developers.pismo.io/pismo-docs/docs/setup-overview#program-types-and-parameters).

## Marketplace

The marketplace object is the top-level object in your digital marketplace. You create a marketplace and configure it to support your business needs. A merketplace can represent a single merchant or a group of merchants that share tax and setup requirements. It also defines the settlement schedule for all merchants in that marketplace.

Use the [Create marketplace](https://developers.pismo.io/pismo-docs/reference/postmarketplacesv2) endpoint to create a new marketplace.

## Merchant

The merchant object represents a business that sells products or services in your marketplace. A merchant can be any type of seller, such as a gas station or an e-commerce store. Each merchant includes a transaction register and a settlement schedule within the marketplace.

Use the [Create merchant](https://developers.pismo.io/pismo-docs/reference/createmerchant) endpoint to create a merchant, then use [Link merchant to marketplace](https://developers.pismo.io/pismo-docs/reference/postlinkmerchanttomarketplacev1) to add it to a marketplace.

## Creditor

The creditor object represents the owner of a business. It links to a merchan and includes a bank object, which contains the merchant account. This account receives the funds from sales during settlement.

You create the creditor at the same time you create the merchant using [Create merchant](https://developers.pismo.io/pismo-docs/reference/createmerchant).

> 🚧
>
> You can also create a creditor using “Create a creditor,” but creditors created in this way do not include an account. Pismo recommends using [Create merchant](https://developers.pismo.io/pismo-docs/reference/createmerchant) to ensure the creditor has an associated account.

## Marketplace creditor operation

For each sale, the merchant pays a fee or rate to the marketplace. This fee is the **merchant discount rate (MDR)**. The marketplace creditor operation object enables the creditor to configure MDR values, sales rates, and other required fees.

To create a creditor operation,  use [Create creditor operation](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations). Pass the merchant ID in `merchant_id` , the marketplace ID in `marketplace_id`, and the creditor ID in `creditor_id`.

You can create multiple creditor operations for a creditor and its merchants. Each operation can define different rates, fees, and payment intervals, depending on the transaction type (such as transactions with or without installments or interest).

> 📘
>
> A merchant links to one creditor, but a creditor can link to multiple merchants.
<!-- source:end -->

### Source 2: `docs/seller-management/seller-management-onboarding.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding · updatedAt: 2026-06-28T23:14:38.000Z

<!-- source:begin path=docs/seller-management/seller-management-onboarding.md part=0-end -->

# Seller management onboarding

The Pismo platform provides seller management APIs for managing digital marketplaces, merchants, receivables schedules, rates and fees, advancements, and settlements. Onboarding steps must be completed in partnership with Pismo using the API endpoints or the UI.

This onboarding guide contains details about each seller management component, as well as which endpoints or methods you use to set them up. For a more detailed planning, implementing, testing, and monitoring guide, refer to [Get started with seller management](https://developers.pismo.io/pismo-docs/docs/get-started-with-seller-management).

# Onboard an organization (tenant)

Work with Pismo to onboard your organization and create your first program on the Pismo platform. Once those are in place, you can start creating accounts and customers and calling Pismo API endpoints. For more information about all onboarding tasks, refer to [Onboarding for new customers](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding).

# Create the merchant program

Next, create a merchant program. Use the [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) endpoint with `type` set to `MERCHANT`. You must create a new program for each country where your clients operate, plus create a new program for each country's additional time zones. If the client's country has multiple currencies, then you also create a new program for each currency.

# Create merchants and associate creditors

The Merchant object represents a business that sells products or services in your marketplace. Each merchant has a schedule and a register of transactions in the Marketplace object.

According to the configured commercial conditions, the system updates receivables schedules with the net amounts due. The system assigns the settlement account as indicated through the creditor created and assigned to the merchants. This step requires configuring the merchant status workflow, which the setup team must configure in accordance with discussions with you, the client.

Use the [Create merchant](https://developers.pismo.io/pismo-docs/reference/createmerchant) endpoint to create merchants and their associated creditors. Then use [Link merchant and marketplace](https://developers.pismo.io/pismo-docs/reference/postlinkmerchanttomarketplacev1) to add the merchants to your marketplace.

## Associating creditors with merchants

The creditor object represents the owner of a business. It’s associated with a merchant object and includes a bank object, which is the merchant account. For example, a creditor could be the owner of a gas station. The owner provides Pismo with the merchant account information for the business. This account receives money from sales during the settlement process.

If a creditor is not provided during the Merchant creation process, this process creates an account and a new creditor, which is automatically assigned to the new merchant. This assignment ensures all funding transfers to the merchant occur using this creditor account.

# Create marketplaces

Use [Create marketplace](https://developers.pismo.io/pismo-docs/reference/postmarketplacesv2) to create a Marketplace object and a scheduler for that Marketplace. You use the Marketplace to group merchants who share the same tax structure and setup. You use the scheduler when you want to split transactions between multiple merchants. You can also set up a calendar schedule to handle settlements for all the merchants that belong to the Marketplace object, and collect rates and fees over the sales performed by those merchants. You can create multiple marketplaces depending on your business needs.

# Link merchants to marketplaces

Once you have merchants and marketplaces set up, you link the merchants to the marketplace using the [Link merchant and marketplace](https://developers.pismo.io/pismo-docs/reference/postlinkmerchanttomarketplacev1) endpoint to add merchants to a given marketplace.

# Create processing codes

Processing codes identify and classify operations for accounting purposes. Examples of processing codes for the seller management API include sales operations with or without installments, settlements, transfers, and discounts related to the sale operation. You must inform the Pismo team of the processing codes used for merchant transactions to add them to the merchant transactions filter. Refer to common processing codes in the [Define processing codes](https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes) step of the [Get started with seller management guide](https://developers.pismo.io/pismo-docs/docs/get-started-with-seller-management).

# Configure creditor operations

The seller marketplace rules engine defines the creditor operations used when a merchant transaction occurs. For each creditor, the rules engine determines the days to pay the merchant after a sale, the number of installments, rates and fees to discount and pay the marketplace, other fees, and balance impacts as debit or credit. Use [Create creditor operation](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations) to configure your rules.

Now that all the configuration and onboarding is complete, you can learn more about day-to-day operations in [Running seller marketplaces](step-4-running-marketplace-operations).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/merchants` | `createMerchant` | Create merchant | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant |
| `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | Create creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |

### Operation essentials

- **`POST /v1/merchants`** (`createMerchant`): security `BearerAuth`; required parameters none declared; required body fields `document_number`, `name`, `email`; response statuses 201, 400, 401, 500; error codes in examples none; events `merchants-merchant-created-1`.
- **`POST /marketplaces/{marketplaceId}/creditors-operations`** (`PostCreditorsOperations`): security `BearerAuth`; required parameters `marketplaceId` (path); required body fields `creditor_id`, `first_installment_days_to_payment`, `installments`, `n_installment_days_to_payment`; response statuses 200, 400, 401, 500; error codes in examples none; events `marketplace-marketplace-creditor-operation-created-1`.
- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.

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

- `docs/seller-management/seller-management-overview.md`: updatedAt 2026-03-18T15:24:07.000Z.
- `docs/seller-management/seller-management-onboarding.md`: updatedAt 2026-06-28T23:14:38.000Z.
- Links to `postmarketplacesv2`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Create marketplace" equals the endpoint name "Create marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier.
- Links to `postlinkmerchanttomarketplacev1`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Link merchant and marketplace" equals the endpoint name "Link merchant and marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/seller-management/seller-management-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/seller-management-overview | `5bf18137ff34ed2a…` | 2026-03-18T15:24:07.000Z |
| `docs/seller-management/seller-management-onboarding.md` | whole document | https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding | `2c1d74837f41208f…` | 2026-06-28T23:14:38.000Z |

## Related knowledge units

- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-API-seller-management-merchants--merchant` — API reference: Seller management - Merchants — Merchant
- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-pismo-platform-onboarding` — Onboarding for new customers
- `KU-GS-setup-overview` — Core objects
- `KU-PAY-payment-overview-and-instant-payments` — Banking payment overview, instant payments and integrated payments
- `KU-SELL-get-started-seller-management` — Get started with seller management
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
