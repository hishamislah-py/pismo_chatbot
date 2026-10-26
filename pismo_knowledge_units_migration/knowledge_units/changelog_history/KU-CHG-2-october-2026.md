---
ku_id: KU-CHG-2-october-2026
title: 'Changelog: 2 October 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/2-october-2026.md
  sha256: cce711f798262309b879518ef73e866361a3f64d8458d965a09a3f5b2131d871
  url: https://developers.pismo.io/pismo-docs/changelog/2-october-2026
  role: changelog_post
  updated_at: ''
operations:
- CreateInstallmentAdvancementV2
- PostAccountsV2
- PostAuthorizationsV1
- PostCreditorsOperationsV2
- PostPciCardsV1
- cash-management-v2-post-payments
- cash-management-v2-post-scheduled-payments
- corporate-get-v1-checks-id
- corporate-post-v1-checks
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- corporate-v2-post-scheduled-payments
- corporate-v3-post-multileg-payments
- createLoanProductV2
- dlq-get-clearing-rules
- get-accounts
- get-corporate-transaction
- get-corporate-transactions
- get-corporate-v1-restricted-funds
- get-division-by-code-v2
- get-v1-benchmark-rate-b3
- get-v1-benchmark-rate-org-b3
- get-v1-interest-account
- get-v1-interest-account-b3
- get-v1-interest-plan
- get-v1-interest-plan-b3
- get-v1-interest-plans
- getLoanProductV2
- getLoanV2
- getLoansByAccountIdV2
- interest-bearing-calculate-average-balance
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-create-savings-account-product
- interest-bearing-v1-deposit-account-open
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-attach-program
- interest-bearing-v1-deposit-detach-account
- interest-bearing-v1-deposit-update-account-attachment
- interest-bearing-v1-deposit-update-payout-account
- interest-bearing-v1-get-account-attachment
- interest-bearing-v1-get-cycle-snapshot
- interest-bearing-v1-get-deposit-products
- interest-bearing-v1-get-program-attachment
- interest-bearing-v1-list-products
- interest-bearing-v1-savings-account-attach-account
- interest-bearing-v1-savings-account-attach-program
- interest-bearing-v1-savings-account-detach-account
- interest-bearing-v1-savings-account-update-payout-account
- list-corporate-transaction-statuses
- list-corporate-v1-restricted-funds
- list-division-v2
- patch-corporate-v1-restricted-funds
- patch-corporate-v2-restricted-funds
- patch-division-v2
- patch-v1-interest-plan
- post-corporate-v1-restricted-funds
- post-division-v2
- post-payment-confirm
- post-payments
- post-payments-cancel
- post-payments-v1-force
- post-payments-v1-force-cancel
- post-payments-v1-hold-funds-block
- post-payments-v1-hold-funds-transfer
- post-payments-v1-hold-funds-transfer-cancel
- post-payments-v1-hold-funds-unblock
- post-transfers
- post-transfers-cancel
- post-transfers-confirm
- post-v1-benchmark-rate-b3
- post-v1-interest-balance
- post-v1-interest-deposit
- post-v1-interest-plan
- post-v1-interest-plan-b3
- postModel
- post_v1-authorizations
- put-v1-interest-account
- put-v1-interest-account-b3
- updateLoanProductV2
related_kus:
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--average-balance
- KU-API-banking-interest-bearing-accounts--deposit-account-lifecycle
- KU-API-banking-interest-bearing-accounts--deposit-account-open
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-bearing-accounts--program-attachment
- KU-API-banking-interest-engine--account-interest
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-interest-management--account-interest
- KU-API-banking-interest-management--benchmark-rate
- KU-API-banking-interest-management--interest-plan
- KU-API-banking-interest-operations--interest-engine
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--check-posting
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-banking-transaction-banking--transactions
- KU-API-card-issuing-authorization--authorizations
- KU-API-core-platform-payment-methods--force-operations
- KU-API-core-platform-payment-methods--hold-funds
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-migrations--account-migration
- KU-API-migrations--authorization-migration
- KU-API-migrations--card-migration
- KU-API-pismo-clearing-rules-engine--clearing-rules
- KU-API-platform-setup-rates-and-fees--fee-models
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 2 October 2026
coverage_window: 4 September and 2 October 2026
---

# Changelog: 2 October 2026

**KU ID:** `KU-CHG-2-october-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **2 October 2026** (changes between 4 September and 2 October 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated".

## Topics covered

Core platform - Payments; Core platform - Rates and fees; Card issuing - Network integration; Card issuing - Statements; Client webhooks; Flex controls; General; Migrations; Payments; Rates and fees; Security; Events; Banking operations; Transaction banking; Authorization; Dispute; Statements; Lending; Marketplace; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/2-october-2026

<!-- source:begin path=changelog/2-october-2026.md part=0-end -->

# 2 October 2026

Changes between 4 September and 2 October 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### Core platform - Payments

  #### Docs

  The following new guides document a new type of program for commercial credit cards that enables multiple accounts to use a shared credit structure.

  * [Commercial cards overview](https://developers.pismo.io/pismo-docs/reference/corporate-card-programs)
  * [Transaction processing flows](https://developers.pismo.io/pismo-docs/reference/transaction-processing-flows)
  * [How to implement a Commercial cards program](https://developers.pismo.io/pismo-docs/reference/how-to-implement-a-commercial-cards-program)

  ### Core platform - Rates and fees

  #### Docs

  A new guide, [Price Table strategy calculation](https://developers.pismo.io/pismo-docs/docs/price-table-strategy-calculation), is now available. The `PRICE_TABLE` strategy is a fee calculation method that generates installment plans with compound interest, fees, and Imposto sobre Operações Financeiras (IOF - Brazilian tax) calculations. This new guide describes the various configurations and calculation process for the `PRICE_TABLE` calculation method.

  #### Docs

  A new guide, [Equal installments strategy](https://developers.pismo.io/pismo-docs/reference/equal-installments-strategy), is now available. The Equal Installments strategy is a calculation method used to calculate loans, financing agreements, or installment purchases where the customer pays a fixed installment amount throughout the contract. This calculation method is often used with simulations. This new guide describes the various configurations and calculation process for the Equal installments calculation method.

  ### Card issuing - Network integration

  #### New

  A new API, [Clearing rules engine](https://developers.pismo.io/pismo-docs/reference/dlq-get-clearing-rules), provides a set of external endpoints that allow you to configure which clearing events should be automatically processed by the Pismo platform and which should be routed to the dead letter queue (DLQ). The DLQ is the queue for all pending transactions waiting to be cleared. The new [Clearing rules engine](https://developers.pismo.io/pismo-docs/docs/clearing-rules-engine) guide is now also available.

  ### Card issuing - Statements

  #### Docs

  A new guide, [Transaction classification model](https://developers.pismo.io/pismo-docs/reference/transaction-classification), is now available. This guide explains how processing codes, transaction types, program transaction types, and transaction categories are used to classify transactions and how the Pismo platform processes them based on that classification.
</summary>

<summary class="tabContent" id="Core platform">
  ### Client webhooks

  #### Docs

  The [Client anti-fraud webhook for banking transaction](https://developers.pismo.io/pismo-docs/docs/client-webhooks#client-anti-fraud-webhook-for-banking-transaction) was updated in the Client webhooks guide to include a more exhaustive list of endpoints that call the webhook.

  ### Flex controls

  #### Docs

  The [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls) guide was rewritten for clarity and to conform to documentation standards. It now includes clarifications in the overview and in the note about Pix transactions, additional details about [flex control types](https://developers.pismo.io/pismo-docs/docs/flex-controls#flex-control-types), and links to two new guides:

  * The new [Simulate flex control creation](https://developers.pismo.io/pismo-docs/docs/simulate-flex-control-creation) guide provides the steps to simulate and verify flex controls using Postman.
  * The new [Flex controls examples](https://developers.pismo.io/pismo-docs/docs/flex-controls-examples) guide shows common flex control implementation scenarios.

  ### General

  #### Docs

  The [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview) guides was rewritten to provide additional details about entities, streamline concept definitions, refer to the API reference documentation for field specifics, and to adhere to documentation standards overall.

  ### Migrations

  #### Docs

  In the [Migrate accounts](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint, the requirements for `due_date_id`, `program_id`, and overdue account migrations were clarified.

  #### Docs

  Support for [Migrate PCI cards](https://developers.pismo.io/pismo-docs/reference/postpcicardsv1) data using encrypted PAN values was added through the new `key_id`, `encrypted_pan`, and `iv `fields. In addition, PAN requirements were updated so you can provide either a clear PAN (`pan`) or `encrypted_pan` data, helping support PCI-compliant migration workflows.

  #### Docs

  The documented value for the `authorization_status` field within the [Migrate authorizations](https://developers.pismo.io/pismo-docs/reference/postauthorizationsv1) endpoint was corrected to align with Pismo documentation standards and business practices.

  #### Docs

  The description of the `update_limit` field within the [Migrate authorizations](https://developers.pismo.io/pismo-docs/reference/postauthorizationsv1) endpoint was corrected. This new description reflects the proper field type and provides guidance on when to use it.

  #### Docs

  The description of the `open_due_date` field in the [Migrate accounts](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint was updated to clarify that for overdue accounts, this field must equal the due date of the earliest unpaid statement that originated the delinquency. Additional guidance was also added around the pre-go-live behavior when payments or qualifying credits are identified.

  #### Docs

  The payload structure of the `migration` object in the [Migrate accounts](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint was updated to be nested within the `applicant` object.

  ### Payments

  #### Updated

  The `authorization_id` field is now returned in the success 200 and 201 responses of the following endpoints.

  * [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments)
  * [Cancel cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-cancel)
  * [Confirm pre-authorized cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payment-confirm)
  * [Create transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers)
  * [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers-cancel)
  * [Confirm pre-authorized transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers-confirm)

  #### Updated

  Account validation for hold funds and force operations in the Payment methods API was updated. The `account_id` is now required to be sent in the request body to match the gateway-asserted `x-account-id `header whenever account validation is enabled. This helps strengthen account-level authorization controls and reduce the risk of requests being processed for an unintended account within the same organization.

  The affected components include the following endpoints in the Payment methods API.

  * Hold funds operations: [Block amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-block), [Unblock held amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-unblock), [Transfer held amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer), and [Cancel transfer of held amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-transfer-cancel).
  * Force operations: [Force operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force) and [Cancel forced operation](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-force-cancel).

  #### Docs

  The 200 and 201 status response of the [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments) endpoint now correctly includes the `amount` field that was previously missing in documentation.

  #### Docs

  The 202 response of the [Confirm pre-authorized cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payment-confirm) and [Confirm pre-authorized transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers-confirm) endpoints now explains that the empty body in this response is expected and that the confirmation outcome is delivered through the [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event with the `CONFIRMATION` category.

  ### Rates and fees

  #### Docs

  Reference documentation for the [Create fee model](https://developers.pismo.io/pismo-docs/reference/postmodel) endpoint was updated to change the 200 response to 201 to match the implementation.

  ### Security

  #### Updated

  The process for configuring the Mutual Transport Layer Security (mTLS) has changed. The new process is described in the [Identity connectivity with mTLS](https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls) guide.
</summary>

<summary class="tabContent" id="Data">
  ### Events

  #### Updated

  In the two Accrual event processed events (one under Interest-bearing deposit accounts, one under Savings account product), the data format for `estimated_settlement_date` and `accrual_date` was changed from `date‑time` to `date` to resolve an inconsistency in the response payload returned to clients.

  * [Accrual event processed](https://developers.pismo.io/events/docs/deposit-product-accrual-event-success-1) (interest-bearing deposit accounts)
  * [Accrual event processed](https://developers.pismo.io/events/docs/savings-account-product-accrual-event-success-1) (savings account product)
</summary>

<summary class="tabContent" id="Core banking">
  ### Banking operations

  #### Updated

  A metadata field was added to the following endpoints to standardize metadata structure at the root level for improved tracking and event correlation.

  * [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds)
  * [List fund restrictions](https://developers.pismo.io/pismo-docs/reference/list-corporate-v1-restricted-funds)

  #### Updated

  A new field `release_datetime` was added to the following endpoints, indicating when the remaining held funds are automatically released to the account.

  * [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds)
  * [List fund restrictions](https://developers.pismo.io/pismo-docs/reference/list-corporate-v1-restricted-funds)
  * [Get fund restriction](https://developers.pismo.io/pismo-docs/reference/get-corporate-v1-restricted-funds)
  * [Release restriction](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v1-restricted-funds)
  * [Update restriction](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-restricted-funds)

  #### Updated

  A `409 Conflict` error was added to the responses of the following endpoints. These errors now include clearer messages, such as "Product is already detached" and "Interest processing code already has a divergent balance‑config" to provide more context about the conflicts returned.

  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Create savings account product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-savings-account-product) 

  #### Updated

  The `PAYOUT` option in `interest_capitalization_mode` now requires a fully resolved `payout_account`. When `PAYOUT` is sent without a payout account, the Pismo platform returns error `EIBACC0379: interest_capitalization_mode PAYOUT requires a fully resolved payout_account`. This update affects the following endpoints.

  * [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account) 
  * [Open deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-account-open) 
  * [Update deposit account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment) 

  #### Updated

  A new `external_account_id` field is now included in the response of the [Update payout account for deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-payout-account) endpoint.

  #### Updated

  A `409 Conflict: Account already exists but could not be attached, status is not "NORMAL"` error was added to the response payload of the [Open deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-account-open) endpoint. This error is generated when you open a deposit account with an `external_account_id` that already exists.

  #### Updated

  The `external_account_id` field was added to the response of the following endpoints to provide the client’s custom account ID.

  * [Update payout account for deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-payout-account)
  * [Update payout account for savings account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-update-payout-account)

  #### Updated

  The `account_id` field was removed from the body parameters of the [Calculate average balance](https://developers.pismo.io/pismo-docs/reference/interest-bearing-calculate-average-balance) endpoint because it repeats the function already covered by the path parameter accountId.

  #### Updated

  In the Interest-bearing accounts API, the following `400BadRequest` error codes were removed. The examples that exposed `maturity_period` and `effective_date` validation codes on endpoints that do not accept those fields were removed as well.

  * `EIBACC0305`
  * `EIBACC0306`
  * `EIBACC0307`
  * `EIBACC0319`
  * `EIBACC0320`
  * `EIBACC0321`

  The affected API/endpoints are:

  * Average balance API
  * Product API
  * [Get account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-account-attachment)
  * [Detach deposit from account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-detach-account)
  * [Update payout account for deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-payout-account)
  * [Attach savings account to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-account)
  * [Detach savings account from account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-detach-account)
  * [Update payout account for savings account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-update-payout-account)
  * [Update deposit account attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment)
  * [Get cycle snapshot for deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-cycle-snapshot)
  * [Open deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-account-open)
  * [Get program attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-program-attachment)
  * [Attach savings accounts to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-program)

  #### Updated

  The `FIXED` enum option was added in the `benchmark` field returned in the 200 response of the following endpoints.
  • [Get account interest](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account)
  • [Get interest plan](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan)
  • [Get account interest](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account)
  • [List Org interest plans](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plans)

  #### Updated

  The `division_code` field was added to body parameters of the [Deposit money](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-deposit) and [Create balance](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-balance) endpoints.

  #### Updated

  The 403 Forbidden error was added as a possible response for the following endpoints.

  * [Get account interest](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account)
  * [Updated account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account)

  #### Updated

  The `tax_withholding.tax_rules.threshold_amount` field was added to the following endpoints.

  * [Update account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account#body-params-threshold_amount) in 200 response
  * [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan#body-params-threshold_amount) in body parameters
  * [Get interest plan](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan#response-schemas) in 200 response
  * [Get account interest](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account#response-schemas) in 200 response
  * [List Org interest plans](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plans#response-schemas) in the `items` object of 200 response

  #### Docs

  The “Banking - Interest management (B3)” section in the API reference was renamed to “Banking - Interest management for B3-listed products”.

  The endpoints in this section were renamed as follows.

  * ”Create interest plan (B3 only)” to [Create interest plan for B3-listed products](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan-b3)
  * ”Get interest plan (B3 only)” to [Get interest plan for B3-listed products](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan-b3)
  * ”Get account interest (B3 only)” to [Get account interest for B3-listed products](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account-b3)
  * ”Update account interest (B3 only)” to [Update account interest for B3-listed products](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account-b3)
  * ”Configure benchmark rate (B3 only)” to [Configure benchmark rate for B3-listed products](https://developers.pismo.io/pismo-docs/reference/post-v1-benchmark-rate-b3)
  * ”Get Org benchmark rates (B3 only)” to [Get Org benchmark rates for B3-listed products](https://developers.pismo.io/pismo-docs/reference/get-v1-benchmark-rate-org-b3)
  * ”Get specific benchmark rates (B3 only)” to [Get specific benchmark rates for B3-listed products](https://developers.pismo.io/pismo-docs/reference/get-v1-benchmark-rate-b3)

  #### Docs

  The `interest_by_tiers.tiers.amount` and `interest_by_tiers.tiers.margin_rate` fields were made nullable in the following endpoints in the request body parameters and 200 response (as indicated).

  * [Update account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account) request and 200 response
  * [Get account interest](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account) 200 response
  * [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) request
  * [List Org interest plans](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plans) 200 response
  * [Create interest plan version](https://developers.pismo.io/pismo-docs/reference/patch-v1-interest-plan) request

  #### Docs

  The titles and descriptions of the indicated fields in the following events were updated. Note that some of the events under \[Interest management] and \[Interest engine] have the same titles.

  **Interest management**

  * [Interest accrual account succeeded](https://developers.pismo.io/events/docs/interest-management-interest-accrual-account-success-1) `account_id`
  * [Interest account cancellation succeeded](https://developers.pismo.io/events/docs/interest-management-interest-account-cancellation-success-1) `external_account_cancellation_id`, `account_id`
  * [Interest account cancellation failure](https://developers.pismo.io/events/docs/interest-management-interest-account-cancellation-failure-1) `external_account_cancellation_id`, `account_id`
  * [Interest withdrawal succeeded](https://developers.pismo.io/events/docs/interest-management-interest-withdrawal-success-1) `account_id`
  * [Interest withdrawal failed](https://developers.pismo.io/events/docs/interest-management-interest-withdrawal-failure-1) `account_id`
  * [Interest deposit succeeded](https://developers.pismo.io/events/docs/interest-management-interest-deposit-success-1) `account_id`
  * [Interest deposit failed](https://developers.pismo.io/events/docs/interest-management-interest-deposit-failure-1) `account_id`
  * [Interest accrual account succeeded](https://developers.pismo.io/events/docs/interest-management-interest-accrual-account-success-1) `account_id`
  * [Interest account cancellation succeeded](https://developers.pismo.io/events/docs/interest-management-interest-account-cancellation-success-1) `external_account_cancellation_id`, `account_id`
  * [Interest account cancellation failure](https://developers.pismo.io/events/docs/interest-management-interest-account-cancellation-failure-1) `external_account_cancellation_id`, `account_id`
  * [Interest deposit failed](https://developers.pismo.io/events/docs/interest-engine-interest-deposit-failure-1) `account_id`
  * [Interest deposit succeeded](https://developers.pismo.io/events/docs/interest-management-interest-deposit-success-1) `account_id`
  * [Interest withdrawal failed](https://developers.pismo.io/events/docs/interest-management-interest-withdrawal-failure-1) `account_id`
  * [Interest withdrawal succeeded](https://developers.pismo.io/events/docs/interest-management-interest-withdrawal-success-1) `account_id`

  **Interest engine**

  * [Interest capitalization account succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-capitalization-account-success-1) `account_id`, `external_account_id`
  * [Interest balance succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-balance-success-1) `account_id`, `external_account_id`
  * [Interest balance failed](https://developers.pismo.io/events/docs/interest-engine-interest-balance-failure-1) `account_id`, `external_account_id`
  * [Interest account update succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-account-update-success-1) `account_id`, `external_account_id`
  * [Interest account cancellation succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-account-cancellation-success-1) `account_cancellation_id`, `external_account_cancellation_id`, `external_account_id`
  * [Interest account update succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-account-update-success-1) `account_id`, `external_account_id`
  * [Interest capitalization account succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-capitalization-account-success-1) `account_id`, `external_account_id`

  #### Docs

  The description of the `interest_capitalization_mode` field in the [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account) and [Attach deposit product to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-program) endpoints were updated.

  #### Docs

  The `attached_at` field was renamed to `attachment_date` in the response of the following endpoints. This fixes the mismatch between the documentation and the actual response payload, which already returns `attachment_date`.

  * [Get account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-account-attachment) (in response)
  * [Update deposit account deposit overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment) (in response)
  * [Get program attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-program-attachment) (in response)

  #### Docs

  The description of the `accrual_model` field was updated, which defines how daily interest is calculated, using either net daily balance change (`DEPOSIT_BASIS`) or the daily closing balance (`BALANCE_BASIS`). When the field is omitted, the value is derived from the interest plan’s `interest_base_model`, which defaults to `CLOSING-BALANCE` and therefore produces `BALANCE_BASIS`, while any explicit mismatch returns `HTTP 400 EIBACC0365`. This update is reflected in the following endpoints.

  * [List products](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-list-products)
  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products)

  ### Transaction banking

  #### Updated

  The following error codes were removed. Both error codes were previously documented as placeholders in the codebase and were never returned in production.

  * `WPMT0032: Validation rules conflict with internal accounts program`
  * `WPMT0020: Scheduling a payment crediting your own account isn't allowed`

  These error codes were removed from the following endpoints.

  * [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
  * [Post payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-payments)
  * [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments)
  * [Schedule payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-scheduled-payments)

  #### Updated

  The error codes `WEAM0029` and `WMLP1020` were removed from the following endpoints. These codes were originally used when the Pismo platform rejected earmark payments with back value dates, but back‑dated earmark payments are now supported by default.

  * [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
  * [Post payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-payments)
  * [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments)

  #### Updated

  The `exclusiveMinimum: 0` was changed to `minimum: 0` on the following fields because these fields are confirmed to accept zero as a valid value. The following endpoints are impacted by this change.

  * [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks) (request, `value` in the `check_amount` object)
  * [Get check posting](https://developers.pismo.io/pismo-docs/reference/corporate-get-v1-checks-id) (response, `value` in the `check_amount` object)
  * [List transactions (transaction banking)](https://developers.pismo.io/pismo-docs/reference/get-corporate-transactions)  (response, `value` in the `amount` object)
  * [Get transaction (transaction banking)](https://developers.pismo.io/pismo-docs/reference/get-corporate-transaction)  (response, `value` in the `amount` object)
  * [List transaction status details (transaction banking)](https://developers.pismo.io/pismo-docs/reference/list-corporate-transaction-statuses) (response, the `amount` field)

  #### Updated

  A note was added to the `administrative_division_id` field in the following endpoints stating that it points to the holiday calendar, and that the administrative division is deprecated and replaced by holiday calendar while both use the same underlying data structure for backward compatibility.

  * [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2)
  * [List division](https://developers.pismo.io/pismo-docs/reference/list-division-v2)
  * [Get division](https://developers.pismo.io/pismo-docs/reference/get-division-by-code-v2)
  * [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2)

  #### Updated

  The 400 error code `WCAC0005: division_code is a required field` was removed from the [Get transaction banking account information](https://developers.pismo.io/pismo-docs/reference/get-accounts) endpoint, because this error doesn’t apply.

  #### Updated

  The error codes `WEAM0029` and `WMLP1020` were removed from the following endpoints. These codes were previously returned when earmark payments with back value dates were rejected, but back‑dated earmark payments are now supported by default.

  * [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
  * [Post payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-payments)
  * [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments)
  * [Post multi-leg payment (deprecated)](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments)
</summary>

<summary class="tabContent" id="Card issuing">
  ### Authorization

  #### Updated

  Five missing fields were added to the [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) reference documentation: `arqc_present`, `track1_present`, `track2_present`, `password_present`, and `cvv_present`.

  ### Dispute

  #### Docs

  An accompanying explainer video was added to the [Visa dispute use case](https://developers.pismo.io/pismo-docs/docs/visa-dispute-use-case) guide. The video introduces dispute handling on the Pismo platform, summarizes the dispute state machine, and provides a walkthrough of a real-world Visa fraud dispute.

  ### Statements

  #### Docs

  The last sentence in the [Installment advancements](https://developers.pismo.io/pismo-docs/docs/installment-advancements-guide#advancing-installments) section of the Installment advancements guide was updated for clarity. The names of the links in the list at the end of that section were confusing because they gave the impression that they should link directly to the endpoint APIs, when they actually linked to sections of the same guide. Renamed the links to match the names of the sections they link to.

  #### Docs

  The description of the `DELINQUENT_ACCOUNT_CLOSURE_DAYS` parameter in the table in the [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters) guide was updated.

  #### Docs

  The [Recurring charges](https://developers.pismo.io/pismo-docs/docs/recurring-charges) guide was updated in the following ways.

  * Added the [Annual recurring charge](https://developers.pismo.io/pismo-docs/docs/recurring-charges#annual-recurring-charge) section.
  * Changed the titles of all the “Example” subsections to make them more specific. For example, the “Example 1” subsection of “Examples for recurring charge plans” had its title changed to “Recurring charge plan example 1”.
  * [Recurring charge plan example 3](https://developers.pismo.io/pismo-docs/docs/recurring-charges#recurring-charge-plan-example-3) was rewritten for clarity.

  #### Docs

  The description of the `tracking_id` body parameter field in the [Create installment advancement](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2) endpoint was clarified.
</summary>

<summary class="tabContent" id="Lending">
  ### Lending

  #### Updated

  The [Get loan product](https://developers.pismo.io/pismo-docs/reference/getloanproductv2) and [Update loan product](https://developers.pismo.io/pismo-docs/reference/updateloanproductv2) endpoints now include the ability to indicate when a loan product has enabled backdating. You can configure the number of days for limiting the backdate window with the `backdating_enabled` and `max_backdating_window_days` fields.

  #### Updated

  The Register repayment endpoint was updated to include a `backdating_reason` field. When the `repayment_date` is earlier than the processing date, you can provide a reason as an audit label. The enum values available are:

  * `RAIL_DELAY`: Payment was made on time, but the payment rail or bank file reporting it reached Pismo later.
  * `SYSTEM_ERROR`: A technical failure or outage delayed recording a payment that was actually made earlier.
  * `OPS_CORRECTION`: An operations team is correcting the recorded date of a payment (back-office correction).
  * `RETRY_WINDOW`: Payment was originally initiated within the expected timeframe but was temporarily unsuccessful (for example, transient bank, network, or processing failure) and subsequently reprocessed. The payment is backdated to reflect the original intended payment date.
  * `REINSTATEMENT`: A previously reversed, cancelled, returned, or otherwise invalidated payment is being reinstated and recorded using its original effective payment date to restore the loan to the correct historical state.
  * `MISAPPLIED_PAYMENT_CORRECTION`: A payment applied to the wrong loan or installment is being corrected and re-applied using its true effective payment date.
  * `OTHER`: Generic catch-all for a legitimate backdating reason not covered by the specific values above.

  #### Updated

  The [Create loan product](https://developers.pismo.io/pismo-docs/reference/createloanproductv2) and [Update loan product](https://developers.pismo.io/pismo-docs/reference/updateloanproductv2) endpoints were updated to require `present_value_discount` (processing code) when `bring_to_present_value_on_delinquency` is `true`. This setting ensures the platform brings future installments to present value before cancellation when closing due to delinquency.

  #### Docs

  More detail was added to the [Create processing codes](https://developers.pismo.io/pismo-docs/docs/create-loan-products#create-processing-codes) section of the Create loan products
  guide for Booking and Repayment processing codes.

  #### Docs

  The following statuses were previously shown in error and were now removed from the [Get loan](https://developers.pismo.io/pismo-docs/reference/getloanv2), [List loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2), and [List account loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2) endpoints.

  * `SCHEDULED`
  * `PROCESSING`
  * `PAID`
  * `PARTIALLY_PAID`
  * `PAST_DUE`
  * `NOT_PAID`
</summary>

<summary class="tabContent" id="Seller management">
  ### Marketplace

  #### Docs

  Added documentation for HTTP 409 Conflict responses on the [Create marketplace creditor operations](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperationsv2) endpoint. This response updates duplicate creditor operation handling from a generic 500 Internal Server Error to a business-specific conflict response when submitted creditor operations already exist for one or more specified merchants.

  #### Deprecated

  The following endpoints were decommissioned and removed from the Developers Portal and added to the [API endpoints removed](https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed) list.

  * List marketplace merchants V1
  * List marketplace merchants V2
  * Link merchant and marketplace
  * Delete merchant and marketplace link
  * Get marketplace V1
  * Update marketplace
  * Create marketplace V1
  * Create marketplace V2
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### Updated

  The [dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval) feature was updated in Control Center. You can now request Pismo to enable dual approval for [editing an address](https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center#addresses).

  #### Docs

  The [Account configurations](https://developers.pismo.io/pismo-docs/docs/account-configurations-in-control-center) guide was updated to align with Pismo documentation and style standards.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `GET /v1/rules` (`dlq-get-clearing-rules`) | `api-specs/Pismo_clearing_rules_engine.yaml` | no | KU-API-pismo-clearing-rules-engine--clearing-rules |
| `POST /v2/migrations/accounts` (`PostAccountsV2`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--account-migration |
| `POST /v1/migrations/cards-pci` (`PostPciCardsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /v1/migrations/authorizations` (`PostAuthorizationsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--authorization-migration |
| `POST /payment-methods/v2/payments` (`post-payments`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payment-methods/v2/payments/cancel` (`post-payments-cancel`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payment-methods/v2/payments/confirm` (`post-payment-confirm`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payment-methods/v2/transfers` (`post-transfers`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payment-methods/v2/transfers/cancel` (`post-transfers-cancel`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payment-methods/v2/transfers/confirm` (`post-transfers-confirm`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payments/v1/payments/hold-funds/block` (`post-payments-v1-hold-funds-block`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /payments/v1/payments/hold-funds/unblock` (`post-payments-v1-hold-funds-unblock`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /payments/v1/payments/hold-funds/transfer` (`post-payments-v1-hold-funds-transfer`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /payments/v1/payments/hold-funds/transfer/cancel` (`post-payments-v1-hold-funds-transfer-cancel`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /payments/v1/payments/force` (`post-payments-v1-force`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--force-operations |
| `POST /payments/v1/payments/force/cancel` (`post-payments-v1-force-cancel`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--force-operations |
| `POST /v1/fee/models` (`postModel`) | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--fee-models |
| `POST /corporate/v1/restricted-funds` (`post-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v1/restricted-funds` (`list-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v1/restricted-funds/{restrictedFundsId}` (`get-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` (`patch-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `PATCH /corporate/v2/restricted-funds/{restrictedFundsId}` (`patch-corporate-v2-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/savings-accounts` (`interest-bearing-v1-create-savings-account-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/deposits/accounts/{accountId}/attach` (`interest-bearing-v1-deposit-attach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits/accounts/open` (`interest-bearing-v1-deposit-account-open`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--deposit-account-open |
| `PATCH /v1/deposits/accounts/{accountId}/attachment` (`interest-bearing-v1-deposit-update-account-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/deposits/accounts/{accountId}` (`interest-bearing-v1-deposit-update-payout-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/savings-accounts/accounts/{accountId}` (`interest-bearing-v1-savings-account-update-payout-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/accounts/{accountId}/average-balance` (`interest-bearing-calculate-average-balance`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--average-balance |
| `GET /v1/products/attachments/accounts/{accountId}` (`interest-bearing-v1-get-account-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits/accounts/{accountId}/detach` (`interest-bearing-v1-deposit-detach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/savings-accounts/accounts/{accountId}/attach` (`interest-bearing-v1-savings-account-attach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/savings-accounts/accounts/{accountId}/detach` (`interest-bearing-v1-savings-account-detach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `GET /v1/deposits/accounts/{accountId}/cycle-snapshot` (`interest-bearing-v1-get-cycle-snapshot`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--deposit-account-lifecycle |
| `GET /v1/products/attachments/programs/{programId}` (`interest-bearing-v1-get-program-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `POST /v1/savings-accounts/programs/{programId}/attach` (`interest-bearing-v1-savings-account-attach-program`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `GET /v1/interest/account/{accountId}` (`get-v1-interest-account`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--account-interest |
| `GET /v1/interest/plan/{interestPlanId}` (`get-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `GET /v1/interest/plan` (`get-v1-interest-plans`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /v1/interest/deposit` (`post-v1-interest-deposit`) | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `POST /v1/interest/balance` (`post-v1-interest-balance`) | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `PUT /v1/interest/account/{accountId}` (`put-v1-interest-account`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--account-interest |
| `POST /v1/interest/plan` (`post-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /v1/interest/plan` (`post-v1-interest-plan-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--interest-plan |
| `GET /v1/interest/plan/{interestPlanId}` (`get-v1-interest-plan-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--interest-plan |
| `GET /v1/interest/account/{accountId}` (`get-v1-interest-account-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--account-interest |
| `PUT /v1/interest/account/{accountId}` (`put-v1-interest-account-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--account-interest |
| `POST /v1/interest/benchmark-rate` (`post-v1-benchmark-rate-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--benchmark-rate |
| `GET /v1/interest/benchmark-rate` (`get-v1-benchmark-rate-org-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--benchmark-rate |
| `GET /v1/interest/benchmark-rate/{benchmark}` (`get-v1-benchmark-rate-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--benchmark-rate |
| `PATCH /v1/interest/plan/{interestPlanId}` (`patch-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /v1/deposits/programs/{programId}/attach` (`interest-bearing-v1-deposit-attach-program`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `GET /v1/products` (`interest-bearing-v1-list-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/deposits/{productId}` (`interest-bearing-v1-get-deposit-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /cash-management/v2/payments` (`cash-management-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `POST /corporate/v2/scheduled-payments` (`corporate-v2-post-scheduled-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /cash-management/v2/scheduled-payments` (`cash-management-v2-post-scheduled-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `POST /corporate/v3/payments/multileg` (`corporate-v3-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v1/checks` (`corporate-post-v1-checks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `GET /corporate/v1/checks/{checkId}` (`corporate-get-v1-checks-id`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `GET /corporate/v1/corporate-transactions` (`get-corporate-transactions`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |
| `GET /corporate/v1/corporate-transactions/{transactionId}` (`get-corporate-transaction`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |
| `GET /corporate/v1/corporate-transactions/status/{trackingId}` (`list-corporate-transaction-statuses`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |
| `POST /corporate/v2/divisions` (`post-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v2/divisions` (`list-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v2/divisions/{divisionCode}` (`get-division-by-code-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PATCH /corporate/v2/divisions/{divisionCode}` (`patch-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v1/corporate-accounts/{externalAccountId}` (`get-accounts`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v2/payments/multileg` (`corporate-v2-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /networktransactions/v1/authorizations` (`post_v1-authorizations`) | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `POST /v2/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancementV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `GET /v2/loan-products/{productId}` (`getLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `PATCH /v2/loan-products/{productId}` (`updateLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v2/loan-products` (`createLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /v2/loans/{loanId}` (`getLoanV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/accounts/{accountId}/loans` (`getLoansByAccountIdV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/marketplaces/{marketplaceId}/creditors-operations` (`PostCreditorsOperationsV2`) | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `corporate-card-programs` | Commercial cards overview | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `transaction-processing-flows` | Transaction processing flows | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `how-to-implement-a-commercial-cards-program` | How to implement a Commercial cards program | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `equal-installments-strategy` | Equal installments strategy | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `transaction-classification` | Transaction classification model | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/2-october-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/2-october-2026 | `cce711f798262309…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--average-balance` — API reference: Banking - Interest-bearing accounts — Average balance
- `KU-API-banking-interest-bearing-accounts--deposit-account-lifecycle` — API reference: Banking - Interest-bearing accounts — Deposit account lifecycle
- `KU-API-banking-interest-bearing-accounts--deposit-account-open` — API reference: Banking - Interest-bearing accounts — Deposit account open
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-bearing-accounts--program-attachment` — API reference: Banking - Interest-bearing accounts — Program attachment
- `KU-API-banking-interest-engine--account-interest` — API reference: Banking - Interest engine — Account interest
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-interest-management--account-interest` — API reference: Banking - Interest management for B3-listed products — Account interest
- `KU-API-banking-interest-management--benchmark-rate` — API reference: Banking - Interest management for B3-listed products — Benchmark rate
- `KU-API-banking-interest-management--interest-plan` — API reference: Banking - Interest management for B3-listed products — Interest plan
- `KU-API-banking-interest-operations--interest-engine` — API reference: Banking - Interest operations — Interest engine
- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-banking-transaction-banking--transactions` — API reference: Banking - Transaction banking — Transactions
- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-core-platform-payment-methods--force-operations` — API reference: Core platform - Payment methods — Force operations
- `KU-API-core-platform-payment-methods--hold-funds` — API reference: Core platform - Payment methods — Hold funds
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-migrations--account-migration` — API reference: Migrations — Account migration
- `KU-API-migrations--authorization-migration` — API reference: Migrations — Authorization migration
- `KU-API-migrations--card-migration` — API reference: Migrations — Card migration
- `KU-API-pismo-clearing-rules-engine--clearing-rules` — API reference: Pismo clearing rules engine — Clearing rules
- `KU-API-platform-setup-rates-and-fees--fee-models` — API reference: Platform setup - Rates and fees — Fee models
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
