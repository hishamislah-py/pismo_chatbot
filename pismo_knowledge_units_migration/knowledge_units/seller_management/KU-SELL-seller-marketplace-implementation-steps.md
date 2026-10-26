---
ku_id: KU-SELL-seller-marketplace-implementation-steps
title: Seller marketplace implementation steps 1 to 6
category: seller_management
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/seller-management/step-1-plan-seller-marketplaces.md
  sha256: 462691b6aaa856105531c715af672c84935a01a7fda0100e927c1244226b33ad
  url: https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces
  role: primary_guide
  updated_at: '2026-03-18T15:24:11.000Z'
- path: docs/seller-management/step-2-create-program-marketplace.md
  sha256: db4b5f4088862ee09d85dc8e79c25b2ba3bc598bc500767c5b076598ccf137aa
  url: https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace
  role: primary_guide
  updated_at: '2026-06-10T19:23:35.000Z'
- path: docs/seller-management/step-3-define-processing-codes.md
  sha256: 98ee8b29d41cbd133672d9772696dd34dfdfe5f7c8cf008fe5bdf3fe685fbe66
  url: https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes
  role: primary_guide
  updated_at: '2026-03-18T15:24:14.000Z'
- path: docs/seller-management/step-4-running-marketplace-operations.md
  sha256: 21c9fde64e9f2b3c6c487cc300c0f689cd7438815ca2d984222b78f37b955c13
  url: https://developers.pismo.io/pismo-docs/docs/step-4-running-marketplace-operations
  role: primary_guide
  updated_at: '2026-03-18T15:24:15.000Z'
- path: docs/seller-management/step-5-test-seller-marketplace.md
  sha256: 9ce8398149ff4d70e1921ba0da79666ec9491370177f4ff52e71aa760570b692
  url: https://developers.pismo.io/pismo-docs/docs/step-5-test-seller-marketplace
  role: primary_guide
  updated_at: '2026-03-18T15:24:17.000Z'
- path: docs/seller-management/step-6-monitor-seller-marketplace.md
  sha256: 7e576c69fb9aea8879c2b782650197490a8118662bfd0cc7bf7b22799fabb6ef
  url: https://developers.pismo.io/pismo-docs/docs/step-6-monitor-seller-marketplace
  role: primary_guide
  updated_at: '2026-03-18T15:24:18.000Z'
operations:
- CreateProgramBasedOnTemplate
- PostCreditorsOperations
- createMerchant
- listMerchantTransactionsV2
- listMerchantTransactionsV3
- merchants-advancements
- post-authorization
related_kus:
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-platform-setup-programs--programs-part-01
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-API-seller-management-merchant-advance--merchant-advancement
- KU-API-seller-management-merchants--merchant
- KU-API-seller-management-merchants--merchant-transaction
- KU-EVT-catalogue-marketplace
- KU-EVT-catalogue-merchants
- KU-EVT-catalogue-other-domains
- KU-GS-setup-overview
- KU-RPT-scheduled-reports
- KU-SELL-how-merchant-settlements-are-processed
- KU-SELL-seller-management-overview-and-onboarding
grouping_rationale: One ordered implementation series.
---

# Seller marketplace implementation steps 1 to 6

**KU ID:** `KU-SELL-seller-marketplace-implementation-steps` · **Category:** Seller management · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 6 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One ordered implementation series.

Scope as stated in `docs/seller-management/step-1-plan-seller-marketplaces.md`:

> Use this planning section to identify the decisions and considerations for defining a seller marketplace. Refer to the [Seller management onboarding guide](https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding) for information about onboarding with the Pismo team.

Scope as stated in `docs/seller-management/step-2-create-program-marketplace.md`:

> After establishing an [organization](https://developers.pismo.io/pismo-docs/docs/setup-overview#organization), you create a program with type `MERCHANT`. Use the [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) endpoint with `type` set to `MERCHANT`. You must create a new program for each country where your clients operate, and new programs for all time zones and currencies. After you create a program, call the Create merchant endpoint to create a merchant in the next step.

Scope as stated in `docs/seller-management/step-3-define-processing-codes.md`:

> Processing codes identify and classify operations for accounting purposes. Examples of processing codes for the seller management API include sales operations with or without installments, settlements, transfers, and discounts related to the sale operation.

Scope as stated in `docs/seller-management/step-4-running-marketplace-operations.md`:

> For each creditor, the system follows the configured rules to determine the days to pay the merchant after a sale, the number of installments, rates and fees to discount and pay the marketplace, other fees, and balance impacts as debits or credits.

Scope as stated in `docs/seller-management/step-5-test-seller-marketplace.md`:

> Your Pismo support team will work with you to test the marketplace system to verify that it meets all security and functionality requirements. Together, we’ll build test plans and scripts, then execute them to ensure that you’ve tested merchants, settlements, and other key features.

Scope as stated in `docs/seller-management/step-6-monitor-seller-marketplace.md`:

> After configuring and starting your seller marketplace, you'll continuously monitor it to make sure it meets your business objectives. Pismo partners with your team, helping you optimize the seller marketplace and merchant experience.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/seller-management/step-1-plan-seller-marketplaces.md`: Step 1: Plan seller marketplaces; 1. Build the business case for the marketplace; 2. Ensure you meet regulatory, legal, and compliance requirements; 3. Define your marketplace strategy; 4. Discuss your creditor operations rules and Merchant Discount Rates (MDR)
- `docs/seller-management/step-2-create-program-marketplace.md`: Step 2. Create program for the marketplace; Create a merchant program; Ensure the merchant has a creditor; Link the merchants to the marketplace; Ensure proper creditor association
- `docs/seller-management/step-3-define-processing-codes.md`: Step 3: Define processing codes
- `docs/seller-management/step-4-running-marketplace-operations.md`: Step 4: Running Seller marketplace operations; Enable merchant transactions (payments on schedule with creditor operations); Display receivables schedule; Configure receivables advancement; Understand transaction settlement
- `docs/seller-management/step-5-test-seller-marketplace.md`: Step 5: Test; Oversee your marketplace with data events; Test Pismo API endpoints with Postman
- `docs/seller-management/step-6-monitor-seller-marketplace.md`: Step 6: Monitor

## Prerequisites and dependencies

- Prerequisites are described in `docs/seller-management/step-1-plan-seller-marketplaces.md` section "2. Ensure you meet regulatory, legal, and compliance requirements".
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/seller-management/step-1-plan-seller-marketplaces.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces · updatedAt: 2026-03-18T15:24:11.000Z

<!-- source:begin path=docs/seller-management/step-1-plan-seller-marketplaces.md part=0-end -->

# Step 1: Plan seller marketplaces

Use this planning section to identify the decisions and considerations for defining a seller marketplace. Refer to the [Seller management onboarding guide](https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding) for information about onboarding with the Pismo team.

# 1. Build the business case for the marketplace

Create a business plan that outlines your goals, target market, revenue model, and growth strategy. You may find that you want to configure a few different marketplaces to meet business requirements.

<h2>Considerations</h2>

**Which country is your marketplace located in?**

* [ ] Research the country’s tax laws affecting marketplace agreements.
* [ ] Determine which currencies you’ll support in the marketplace.
* [ ] Define which time zones your marketplace operates within since each time zone requires a program.

**Who are your target merchants and what rates will you charge for the marketplace?**

* [ ] Understand your merchants. Research their marketplace options and the merchant's competition to identify a new niche, create practical solutions, or leverage an existing business.
* [ ] Define your go-to-market strategy for adding merchants to the marketplace.
* [ ] Define your Merchant Discount Rates (MDR), whether they are flat fees, percentages on sales, and any defined tiers for higher-performing merchants.
* [ ] Determine a schedule that can handle settlements for all the merchants that belong to the marketplace.

**What's your model for communicating with and supporting merchants in the marketplace?**

* [ ] Determine how you’ll manage incoming merchant inquiries or disputes. Will you use a call center, web-based chat, conversational chatbots, or some combination of these support tools?
* [ ] Determine how you’ll communicate information and updates to merchants, such as settlement dates, receivables schedules, merchant discount rates, tiered promotions, and any required notifications.

# 2. Ensure you meet regulatory, legal, and compliance requirements

All countries have specific laws and regulations governing financial services such as marketplaces. There may be global rules as well. You must ensure relevant authorities have approved you for running a seller marketplace where you plan to operate.

# 3. Define your marketplace strategy

Determine whether your marketplace represents a single merchant or a group of merchants that share the same tax structure and setup. You also may consider creating multiple seller marketplaces to meet business requirements.

# 4. Discuss your creditor operations rules and Merchant Discount Rates (MDR)

**How do you want to operate your marketplace?**

* [ ] Pismo has standard processing codes that are specific to seller marketplaces. Determine any additional processing codes your business needs to support. Refer to [Step 3: Define processing codes](https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes) for details.
* [ ] What discount rates will merchants incur on sales? The charges may be different for each transaction type.
* [ ] Will charge rates differ based on transaction type, such as debit or credit, or whether the card is present? In Seller Management, these are configured inside the [marketplace  creditor operation](https://developers.pismo.io/pismo-docs/docs/seller-management-overview#marketplace-creditor-operation) object.
* [ ] What merchant settlement schedules do you expect to adhere to? You define those in [Step 4: Running seller marketplaces](https://developers.pismo.io/pismo-docs/docs/step-4-running-marketplace-operations).

You may want to set different Merchant Discount Rates for different merchants, with these factors as considerations:

* Transaction volume: Merchants with higher transaction volumes often have more negotiating power and may warrant lower MDRs.
* Risk level: Different industries have varying levels of risk associated with transactions. Higher-risk industries might face higher MDRs due to the increased likelihood of chargebacks or fraud.
* Merchant's creditworthiness: A merchant’s financial stability and credit rating can influence the MDR. Merchants perceived as lower risk may receive better rates.
* Transaction methods: The method by which you conduct transactions affect the MDR. For example, card-present transactions typically have lower MDRs than card-not-present transactions due to the reduced risk of fraud.
* Type of card used: Different types of cards such as credit, debit, or premium may carry different interchange rates, which can affect how you want to set up MDRs.
* Geographic location: Regional differences in banking regulations and market conditions can lead to variations in MDRs. Time zone differences affect settlement completion.
* Promotional or introductory rates: You can give some merchants temporary promotional rates that are lower than the standard MDR, particularly if they are newly joining a marketplace.
<!-- source:end -->

### Source 2: `docs/seller-management/step-2-create-program-marketplace.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace · updatedAt: 2026-06-10T19:23:35.000Z

<!-- source:begin path=docs/seller-management/step-2-create-program-marketplace.md part=0-end -->

# Step 2. Create program for the marketplace

# Create a merchant program

After establishing an [organization](https://developers.pismo.io/pismo-docs/docs/setup-overview#organization), you create a program with type `MERCHANT`. Use the [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) endpoint with `type` set to `MERCHANT`. You must create a new program for each country where your clients operate, and new programs for all time zones and currencies. After you create a program, call the Create merchant endpoint to create a merchant in the next step.

# Ensure the merchant has a creditor

Create a Merchant object after creating a program. Merchants are the sellers who, according to the configured commercial conditions, have their receivables schedules bound by rules such as the amounts to be received after sales and marketplace rates and fees discounts. The creditor assigned to the merchant indicates the account where the amount for each merchant is settled. This step requires configuring the merchant status workflow, which must be done by the Pismo setup team in accordance with discussions with the client.

The Merchant object represents a business that sells products or services in your organization. Each merchant has a schedule and a register of transactions in the Marketplace object.

Use the [Create merchant](https://developers.pismo.io/pismo-docs/reference/createmerchant) endpoint to create merchants. You link merchants to a marketplace when creating a Marketplace. Also understand that the Merchant creation process creates or associates the creditor. Refer to[ Ensure proper creditor association](#ensure-proper-creditor-association).

# Link the merchants to the marketplace

After creating a Marketplace object, you group merchants who share the same tax structure and setup by linking them with the  [Link merchant and marketplace](https://developers.pismo.io/pismo-docs/reference/postlinkmerchanttomarketplacev1) endpoint. Using the Marketplace object, you can also set up a schedule to handle settlements for all merchants that belong to the same marketplace and collect rates and fees over the sales performed by these merchants. Use [Create marketplace](https://developers.pismo.io/pismo-docs/reference/postmarketplacesv2) to create a Marketplace object where you can specify a program by providing its ID in the `program_id` field. Then use [Link merchant and marketplace](https://developers.pismo.io/pismo-docs/reference/postlinkmerchanttomarketplacev1) to add merchants to a given marketplace.

You can group several merchants into a marketplace for flexibility, allowing you to provide incentives for different business patterns by using multiple marketplaces.

# Ensure proper creditor association

The Creditor object represents the banking domicile of the commercial establishment. It’s associated with a Merchant object and includes a bank object, which is the merchant account. For example, a creditor could be the owner of a gas station. The owner's account receives the money from sales during the settlement process.

The owner supplies Pismo with the merchant account details for the business, which is where the funds from sales are deposited during the settlement process.

If you don't provide an existing creditor when creating the Merchant, this process creates an account and a new creditor, which is automatically assigned to the created merchant. This ensures all funding transfers to the merchant occur using this creditor account.

Usually you create the creditor at the same time you create the merchant, using the [Create merchant](https://developers.pismo.io/pismo-docs/reference/createmerchant) endpoint. You can provide an existing creditor ID to create a merchant with an already existing creditor, or fill in the creditor fields to create a new creditor for the created merchant.
<!-- source:end -->

### Source 3: `docs/seller-management/step-3-define-processing-codes.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes · updatedAt: 2026-03-18T15:24:14.000Z

<!-- source:begin path=docs/seller-management/step-3-define-processing-codes.md part=0-end -->

# Step 3: Define processing codes

Processing codes identify and classify operations for accounting purposes. Examples of processing codes for the seller management API include sales operations with or without installments, settlements, transfers, and discounts related to the sale operation.

Here are some common processing codes that represent different types of transactions. These are minimum required processing codes to get set up.

| Processing Code | Description                    |
| --------------- | ------------------------------ |
| `007400`        | Settlement transfer cash-in    |
| `007410`        | Settlement advancement cash-in |
| `999991`        | Total advancement discount     |
| `999992`        | Gross advancement amount       |
| `999993`        | Net advancement discount       |
| `999994`        | Net advancement amount         |
| `999995`        | Advancement fee                |

You must inform the Pismo setup team of the processing codes used for merchant transactions to add them to the merchant transactions filter.
<!-- source:end -->

### Source 4: `docs/seller-management/step-4-running-marketplace-operations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-4-running-marketplace-operations · updatedAt: 2026-03-18T15:24:15.000Z

<!-- source:begin path=docs/seller-management/step-4-running-marketplace-operations.md part=0-end -->

# Step 4: Running Seller marketplace operations

For each creditor, the system follows the configured rules to determine the days to pay the merchant after a sale, the number of installments, rates and fees to discount and pay the marketplace, other fees, and balance impacts as debits or credits.

Use [Create creditor operation](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations) to configure your rules. This rules configuration defines the operations used when a merchant transaction occurs and you set them up during [onboarding](https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding).

# Enable merchant transactions (payments on schedule with creditor operations)

Transactions that compose the receivables schedule usually originate from sales payments received or sales cancellations (reversal transactions). Merchant transactions aim to pay merchants and marketplaces based on the schedule and creditor operations configured.

You can use the following endpoints to request payment authorizations or list merchant transactions.

* [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization)
* [List merchant transactions (V3)](https://developers.pismo.io/pismo-docs/reference/listmerchanttransactionsv3)

# Display receivables schedule

A receivables schedule provides a list of transactions with scheduled dates to pay merchants, advance receivables scheduled for the future, rates, and fees, summarized daily for a given merchant. View this schedule with the [List merchant transactions (V2)](https://developers.pismo.io/pismo-docs/reference/listmerchanttransactionsv2)  endpoints or using a calendar interface.

<Image alt="Receivables schedule calendar" align="center" src="https://files.readme.io/370ba8aa908fba2bb1969d1f32e6b4cb0094cabeff5b8a7f368788b0713e24c3-image-20250122-200146.png">
  Figure 1: Receivables schedule calendar
</Image>

# Configure receivables advancement

Merchants might need to advance receivables scheduled for a future date. This means that even if the payment schedule is for 10 days later, the merchant can still request to receive the payment immediately. The system discounts an additional rate from the scheduled amount, and transfers the net amount to the creditor account either immediately or when the settlement process occurs. You use [Simulate Merchant Advancement](https://developers.pismo.io/pismo-docs/reference/merchants-advancements) to create an advancement schedule and apply discount rate.

# Understand transaction settlement

A scheduled batch job settles transactions on a given date. When the service executes this batch job, the marketplace system settles the transactions scheduled for the current date, meaning a cash-in occurs in the account related to the creditor, transferring the net amount after discounts of rates and fees as per creditor operations configuration. Refer to [How merchant settlements are processed](https://developers.pismo.io/pismo-docs/docs/how-merchant-settlements-are-processed) for more details about how settlement works.

What's next? [Test your seller marketplace](https://developers.pismo.io/pismo-docs/docs/step-5-test-seller-marketplace).
<!-- source:end -->

### Source 5: `docs/seller-management/step-5-test-seller-marketplace.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-5-test-seller-marketplace · updatedAt: 2026-03-18T15:24:17.000Z

<!-- source:begin path=docs/seller-management/step-5-test-seller-marketplace.md part=0-end -->

# Step 5: Test

Your Pismo support team will work with you to test the marketplace system to verify that it meets all security and functionality requirements. Together, we’ll build test plans and scripts, then execute them to ensure that you’ve tested merchants, settlements, and other key features.

# Oversee your marketplace with data events

During testing—and after—it’s important to see what’s happening with your data events. Pismo manages the data events that occur during normal processing. You might know them as notifications or alerts.

Pismo can deliver this information to you in real-time events or via downloadable files. You use this data to monitor product usage, create metrics, send notifications, and generate business intelligence. You can also build your own dashboard to monitor these data events.

For more information, refer to [Data and reporting overview](https://developers.pismo.io/pismo-docs/docs/data-reporting-overview).

# Test Pismo API endpoints with Postman

Use the Pismo Postman collections and environment to test Pismo REST APIs. While you can test all these APIs through the Pismo Developers Portal, Postman helps you customize and streamline your testing environment. Pismo has a public workspace with shared collections and an environment on the Postman Public API network.

For more information, refer to [Testing Pismo API endpoints with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman).
<!-- source:end -->

### Source 6: `docs/seller-management/step-6-monitor-seller-marketplace.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/step-6-monitor-seller-marketplace · updatedAt: 2026-03-18T15:24:18.000Z

<!-- source:begin path=docs/seller-management/step-6-monitor-seller-marketplace.md part=0-end -->

# Step 6: Monitor

After configuring and starting your seller marketplace, you'll continuously monitor it to make sure it meets your business objectives. Pismo partners with your team, helping you optimize the seller marketplace and merchant experience.

While there is no anti-fraud integration specifically for seller management, you want to monitor transactions and settlements so you can resolve any disputes.

Remember you can review when payments will go to merchants. View this schedule with the [List merchant transactions (V2)](https://developers.pismo.io/pismo-docs/reference/listmerchanttransactionsv2) endpoints or settlement calendar in Control Center. If you find you need to change some operations, you can use the [Simulate Merchant Advancement](https://developers.pismo.io/pismo-docs/reference/merchants-advancements) endpoint to create an advancement schedule and apply discount rate.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/template` | `CreateProgramBasedOnTemplate` | Create program | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01 |
| `POST /v1/merchants` | `createMerchant` | Create merchant | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant |
| `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | Create creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `GET /v3/merchants/{merchantId}/transactions` | `listMerchantTransactionsV3` | List merchant transactions (V3) | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant-transaction |
| `GET /v2/merchants/{merchantId}/transactions` | `listMerchantTransactionsV2` | List merchant transactions (V2) | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant-transaction |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements` | `merchants-advancements` | Simulate merchant advancement | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |

### Operation essentials

- **`POST /programs/v1/programs/template`** (`CreateProgramBasedOnTemplate`): security `S2SAuthentication`; required parameters none declared; required body fields `name`, `type`, `timezone`, `currency_numeric_code`, `country_code`; response statuses 200, 400, 404, 416, 500; error codes in examples `EOA0017`, `EOA0018`, `EOA0086`, `EOA0029`, `EOA0033`, `EOA0063`, `EOA0055`, `EOA0073`, `EOA0054`, `EOA0040`, `EOA0037`, `EOA0038`, `EOA0039`, `EOA0020`, `EOA0031`, `EOA0064`, `EOA0030`, `EOA0021`, `EOA0022`, `EOA0034`, `EOA0035`, `EOA0036`, `EOA0058`, `EOA0009`, `EOA0010`, `EOA0008`, `EOA0011`, `EOA0015`, `EOA0016`; events `programs-creation-1`.
- **`POST /v1/merchants`** (`createMerchant`): security `BearerAuth`; required parameters none declared; required body fields `document_number`, `name`, `email`; response statuses 201, 400, 401, 500; error codes in examples none; events `merchants-merchant-created-1`.
- **`POST /marketplaces/{marketplaceId}/creditors-operations`** (`PostCreditorsOperations`): security `BearerAuth`; required parameters `marketplaceId` (path); required body fields `creditor_id`, `first_installment_days_to_payment`, `installments`, `n_installment_days_to_payment`; response statuses 200, 400, 401, 500; error codes in examples none; events `marketplace-marketplace-creditor-operation-created-1`.
- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.
- **`GET /v3/merchants/{merchantId}/transactions`** (`listMerchantTransactionsV3`): security `BearerAuth`; required parameters `merchantId` (path); required body fields none declared; response statuses 200, 400, 401, 404, 408, 500; error codes in examples none; events none listed.
- **`GET /v2/merchants/{merchantId}/transactions`** (`listMerchantTransactionsV2`): security `BearerAuth`; required parameters `merchantId` (path); required body fields none declared; response statuses 200, 400, 401, 404, 408, 500; error codes in examples none; events none listed.
- **`POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements`** (`merchants-advancements`): security not declared; required parameters `Authorization` (header), `marketplaceId` (path), `merchantId` (path); required body fields `begin_date`, `request_date`, `amount`, `real_time_settlement`; response statuses 200, 400, 404; error codes in examples `EPT0303`, `EPT0303`; events `merchants-advancement-request-1`.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `postlinkmerchanttomarketplacev1` | Link merchant and marketplace; Link merchant to marketplace | not found in the current OpenAPI specifications. Name-based inference: link text "Link merchant and marketplace" equals the endpoint name "Link merchant and marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. |
| `postmarketplacesv2` | Create marketplace; Create your marketplace; marketplace | not found in the current OpenAPI specifications. Name-based inference: link text "Create marketplace" equals the endpoint name "Create marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `PostCreditorsOperations` | `marketplace-marketplace-creditor-operation-created-1` |
| `merchants-advancements` | `merchants-advancement-request-1` |
| `createMerchant` | `merchants-merchant-created-1` |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |
| `CreateProgramBasedOnTemplate` | `programs-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/seller-management/step-1-plan-seller-marketplaces.md`: updatedAt 2026-03-18T15:24:11.000Z.
- `docs/seller-management/step-2-create-program-marketplace.md`: updatedAt 2026-06-10T19:23:35.000Z.
- `docs/seller-management/step-3-define-processing-codes.md`: updatedAt 2026-03-18T15:24:14.000Z.
- `docs/seller-management/step-4-running-marketplace-operations.md`: updatedAt 2026-03-18T15:24:15.000Z.
- `docs/seller-management/step-5-test-seller-marketplace.md`: updatedAt 2026-03-18T15:24:17.000Z.
- `docs/seller-management/step-6-monitor-seller-marketplace.md`: updatedAt 2026-03-18T15:24:18.000Z.
- Links to `postlinkmerchanttomarketplacev1`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Link merchant and marketplace" equals the endpoint name "Link merchant and marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier.
- Links to `postmarketplacesv2`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Create marketplace" equals the endpoint name "Create marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/seller-management/step-1-plan-seller-marketplaces.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-1-plan-seller-marketplaces | `462691b6aaa85610…` | 2026-03-18T15:24:11.000Z |
| `docs/seller-management/step-2-create-program-marketplace.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-2-create-program-marketplace | `db4b5f4088862ee0…` | 2026-06-10T19:23:35.000Z |
| `docs/seller-management/step-3-define-processing-codes.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-3-define-processing-codes | `98ee8b29d41cbd13…` | 2026-03-18T15:24:14.000Z |
| `docs/seller-management/step-4-running-marketplace-operations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-4-running-marketplace-operations | `21c9fde64e9f2b3c…` | 2026-03-18T15:24:15.000Z |
| `docs/seller-management/step-5-test-seller-marketplace.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-5-test-seller-marketplace | `9ce8398149ff4d70…` | 2026-03-18T15:24:17.000Z |
| `docs/seller-management/step-6-monitor-seller-marketplace.md` | whole document | https://developers.pismo.io/pismo-docs/docs/step-6-monitor-seller-marketplace | `7e576c69fb9aea88…` | 2026-03-18T15:24:18.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-API-seller-management-merchant-advance--merchant-advancement` — API reference: Seller management - Merchant advancements — Merchant advancement
- `KU-API-seller-management-merchants--merchant` — API reference: Seller management - Merchants — Merchant
- `KU-API-seller-management-merchants--merchant-transaction` — API reference: Seller management - Merchants — Merchant transaction
- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-GS-setup-overview` — Core objects
- `KU-RPT-scheduled-reports` — Data and reporting overview and scheduled reports
- `KU-SELL-how-merchant-settlements-are-processed` — How merchant settlements and installments are processed
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
