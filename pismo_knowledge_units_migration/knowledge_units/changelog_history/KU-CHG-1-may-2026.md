---
ku_id: KU-CHG-1-may-2026
title: 'Changelog: 1 May 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/1-may-2026.md
  sha256: 0ec3fc53459be637c93f13714b9c2df91c3137d0ae1bd47bbb399f9bedf879a1
  url: https://developers.pismo.io/pismo-docs/changelog/1-may-2026
  role: changelog_post
  updated_at: ''
operations:
- AssetRegistration
- CreateAccountingEntry
- CreateAccountingScript
- CreateAccountingScriptV2
- GetTransactionById
- InstallmentPaymentsv4
- ListTransactions
- PostAuthorizationsV1
- PostMerchantTransactionsV1
- SearchTransactionTypes
- UpdateAcountCalendarStrategy
- corporate-v2-post-cancel-payments
- corporate-v2-post-confirm-payments
- corporate-v2-post-payments
- create-bulk
- delete-v1-bulletin
- find-cash-management-earmark
- get-account-balance-history
- get-account-balance-history-config-by-id-v2
- get-account-balance-history-config-by-target-v2
- get-account-balances
- get-cash-management-earmarks
- get-corporate-transaction
- get-corporate-transactions
- get-v1-bulletin
- get-v1-disputes-disputeId
- get-v1-disputes-installment
- list-account-balance-history-configv2
- list-corporate-transaction-statuses
- patch-account-balances-history-configv2
- patch-cash-management-v2-earmarks-earmarkid
- patch-corporate-v2-earmarks-earmarkid
- patch-funds-recovery
- patch-v2-pix-infraction
- performClearingReconciliation
- post-account-balance-history-configv2
- post-acquisitions-v3-s2s-applications
- post-attach-product-to-account
- post-attach-product-to-program
- post-cash-management-v2-earmarks
- post-cash-management-v2-earmarks-earmarkid-cancel
- post-config-by-tenant
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-create-funds-recovery
- post-encrypted-applepay-data
- post-v1-balances-config
- post-v1-benefits-segments-assign
- post-v1-clicktopay-enroll_customer
- post-v1-disputes-disputeId-forms
- post-v2-admin-division
- post-v2-holiday
- post-v2-pix-infraction-create
- post-v2-reset-cvv
- postAccrualTypesConfigurations
- postInterestAccruals
- post_v1-authorizations
related_kus:
- KU-API-banking-assets--assets
- KU-API-banking-overdraft--account
- KU-API-banking-overdraft--program
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--transactions
- KU-API-card-issuing-authorization--authorizations
- KU-API-card-issuing-cards--cvv-rotation
- KU-API-card-issuing-cards--mastercard-benefits
- KU-API-card-issuing-cards--noname
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--disputes-part-02
- KU-API-card-issuing-disputes--installments
- KU-API-card-issuing-disputes--supporting-forms
- KU-API-card-issuing-protection-bulletin--bulletin
- KU-API-card-issuing-reconciliation--network-transactions-backoffice
- KU-API-card-issuing-tokenization--pre-digitalization
- KU-API-card-issuing-tokenization--visa-click-to-pay
- KU-API-core-platform-accounting--accounting-entry
- KU-API-core-platform-accounting--accounting-scripts-v1
- KU-API-core-platform-accounting--accounting-scripts-v2
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balance-config-beta--balance-configurations
- KU-API-core-platform-balance-watcher--limit-configurations
- KU-API-core-platform-payment-configurations--payment-method-configurations
- KU-API-core-platform-transactions--transaction-types
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-pix-management--funds-recovery
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-migrations--authorization-migration
- KU-API-migrations--merchant-transaction-migration
- KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated
- KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat
- KU-API-revolving-credit-calendar-management--account-calendar-strategies
- KU-API-revolving-credit-configurations--additional-accrual-type-configurations
- KU-API-revolving-credit-interest-accruals--post-interest-accruals
- KU-API-revolving-credit-statements--refinancing
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 1 May 2026
coverage_window: 3 April and 1 May 2026
---

# Changelog: 1 May 2026

**KU ID:** `KU-CHG-1-may-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **1 May 2026** (changes between 3 April and 1 May 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

## Topics covered

General; Disputes; Transaction banking; Accounts; Accounting; Fee management; Migration; Payments; Security; Setup; Support; Transactions; Reports; Banking operations; Transaction banking; Authorization; Cards; Cards management; Card network integration; Disputes; Instant payments; Protection Bulletin; Reconciliation; Statements; Tokenization; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/1-may-2026

<!-- source:begin path=changelog/1-may-2026.md part=0-end -->

# 1 May 2026

Changes between 3 April and 1 May 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### General

  #### Docs

  We’re pleased to announce the new [Pismo platform onboarding](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding) guide. It walks new Pismo customers through the onboarding process, including organization creation, required tool and system access, and authentication setup.

  All onboarding information is now consolidated in one place. As part of this update, onboarding content was removed from the following guides, which now link to the new onboarding guide instead:

  * Get started with core banking
  * Get started with transaction banking
  * Getting started with demand deposit accounts (DDAs)
  * Get started with card issuing
  * Get started with lending
  * Seller management onboarding

  #### Docs

  An introductory explainer video was added to the [Get started with the Pismo Developers Portal](https://developers.pismo.io/pismo-docs/docs/welcome) guide. The video introduces the Developers Portal and provides an overview, including:

  * The purpose of the portal and who it’s for
  * An outline of the key sections and features
  * Guidance on where to start and what to explore based on your role

  #### Docs

  A feature overview video, “Understanding fee models in the Pismo platform,” was added to the [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-models) guide. The video introduces the basic concepts and benefits of fee models, including:

  * Business benefits
  * Calculation rules and triggers
  * Hierarchy of control

  ### Disputes

  #### New

  **The new Mastercard dispute lifecycle management for Control Center is available in test environment (EXT)**

  The new experience helps you manage Mastercard disputes more easily, with a clearer interface and better tools. This feature is available from the main menu under **Customer operations -> Disputes**.

  **With this feature, you can:**

  * Open disputes for transactions with or without installments using automated control
  * Select reason codes aligned with Mastercard standards
  * Create partial disputes
  * Update dispute statuses
  * Create fraud reports
  * Create Expedited Billing Dispute Forms (EBDF)
  * Upload supporting evidence files
  * Track dispute status and progress

  **To use this feature, you must have one of these roles assigned to your user account:**

  * To view disputes: backoffice-viewer
  * To open and update disputes: backoffice-operator

  **What else can you expect?**
  Look for Disputes in Control Center production soon.

  **How can you learn more?**
  Explore how disputes management works in [Disputes](https://developers.pismo.io/pismo-docs/docs/disputes).

  ### Transaction banking

  #### New

  Bank statements API v2 is now available. The new version allows you to create or update account balance history configurations at the division, organization, and program levels using a configuration ID. Previously, this was supported only at the division level. Bank statements API v2 includes the following endpoints:

  * [Create account account balance history config v2](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configv2)
  * [List account balance history config v2](https://developers.pismo.io/pismo-docs/reference/list-account-balance-history-configv2)
  * [Get account balance history config by ID v2](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history-config-by-id-v2)
  * [Update account balance history config v2](https://developers.pismo.io/pismo-docs/reference/patch-account-balances-history-configv2)
  * [Get account balance history config by target type v2](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history-config-by-target-v2)

  #### New

  The following endpoints were created that work specifically with Pismo account IDs. Their original counterparts remain active.

  **Earmarking**

  * [Create earmark (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/post-cash-management-v2-earmarks)
  * [List earmarks (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/get-cash-management-earmarks)
  * [Get earmark (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/find-cash-management-earmark)
  * [Update earmark (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/patch-cash-management-v2-earmarks-earmarkid)
  * [Cancel earmark (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/post-cash-management-v2-earmarks-earmarkid-cancel)

  **Payment**

  * [Post payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-payments-1)
  * [Confirm payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-confirm-payments-1)
  * [Cancel payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-cancel-payments-1)
  * [Schedule payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-scheduled-payments-1)
  * [Get scheduled payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-get-scheduled-payment-1)
  * [Post float cash-in (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/post-corporate-float-cash-in)

  #### Docs

  The new [Channel Control for back-business-date and cutoff exceptions](https://developers.pismo.io/pismo-docs/reference/channel-control-for-back-business-date-and-cutoff-exceptions) guide explains how channel-based access and execution controls work, including configuration of channel-based exceptions for back business dates and cutoff processing.

  #### Docs

  The new guide [Penalties for CD accounts](https://developers.pismo.io/pismo-docs/docs/penalties-for-cd-accounts) is now available, This guide explains how you can define and combine rules that apply specific charges when certain withdrawal events occur, with the Pismo platform evaluating these conditions at withdrawal time based on the product’s configuration.
</summary>

<summary class="tabContent" id="Core platform">
  ### Accounts

  #### New

  The new field `is_centralizer` was added to the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) request. This boolean field indicates if the account is a centralizer account. A centralizer account, within the account hierarchy, is the account responsible for invoice billing.

  ### Accounting

  #### Docs

  The accounting API documentation was enhanced in the following ways.

  * The [Accounting scripts V2](https://developers.pismo.io/pismo-docs/reference/createaccountingscriptv2) endpoints were moved into a separate section, the majority of their field descriptions were added or enhanced, and the unused `cosif` field was removed.
  * In the [Create accounting script V1](https://developers.pismo.io/pismo-docs/reference/createaccountingscript) endpoint, the `cost_center` field was marked as optional instead of required and the `entry_name` field was updated with the list of enum values and their descriptions.
  * In the [Create accounting entry](https://developers.pismo.io/pismo-docs/reference/createaccountingentry) endpoint, the `tracking_id` field description was updated to indicate that it's a UUID field and with the link to the random UUID generator.

  #### Docs

  In the [Accounting events report files](https://developers.pismo.io/pismo-docs/docs/accounting-events-report-files) guide, the descriptions for the `CreatedAt`, `EventDate`, and `RefDate` date fields were updated to include formats and the data type for the `AuthorizationDate` field was corrected to be `date` instead of `string`.

  ### Fee management

  #### Docs

  The [Fee management](https://developers.pismo.io/pismo-docs/docs/fee-management) guide and [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-models) guide were rewritten for clarification and to provide more in-depth details about fee models in the Pismo platform. In addition, three new guides related to fee models are now available.

  * [Creating and applying fee models](https://developers.pismo.io/pismo-docs/docs/create-fee-model)
  * [IOF fee model for Brazil](https://developers.pismo.io/pismo-docs/docs/iof-fee-model)
  * [Simulating and testing fee models](https://developers.pismo.io/pismo-docs/docs/simulating-fee-models)

  ### Migration

  #### Docs

  The [Migrate authorizations](https://developers.pismo.io/pismo-docs/reference/postauthorizationsv1) and [Migrate merchant transactions](https://developers.pismo.io/pismo-docs/reference/postmerchanttransactionsv1) property fields were revised for general editorial updates to better adhere to Pismo documentation standards.

  ### Payments

  #### New

  The new API with 4 endpoints is now available in beta release- [Payment rails - BACS payments](https://developers.pismo.io/pismo-docs/reference/post-create-bacs-1). BACS stands for [Banking Automated Clearing System](https://www.moderntreasury.com/learn/what-is-bacs). BACS is a UK service that facilitates electronic money transfers between banks within a 3-day settlement cycle— Day 1 (submission), Day 2 (processing), and Day 3 (clearing/credit).

  #### Docs

  The [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods) guide was enhanced with the diagram that illustrates transaction categories.

  #### Docs

  In the [Payment configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) API documentation, the titles were updated to avoid duplication and descriptions of boolean fields were updated according to standards.

  ### Security

  #### Docs

  The [Verifying webhook requests](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests) guide was updated in the following sections.

  * The public key request sample in the **Retrieving a list of public keys** section was updated to reflect the correct URLs.
  * The `cache-control` sample in the **Renewing your public keys** section was updated to reflect a correct `max-age` example.

  #### Docs

  The [Get an account-specific token](https://developers.pismo.io/pismo-docs/reference/get-an-account-specific-token-basic-authentication) guide is now available.

  ### Setup

  #### Docs

  In the [Environments](https://developers.pismo.io/pismo-docs/docs/environments#pci-endpoints-vs-non-pci-endpoints) guide, the following were added to the list of PCI services.

  * `/payment-methods/`
  * `/payment-methods-configs/`

  #### Docs

  In the [Balance configurations](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config) API documentation, the `global_configs` field name was corrected throughout. Some instances previously incorrectly listed this field as `global_config`.

  ### Support

  #### Docs

  The description of the `Occurrence` field in the [Request types and common fields](https://developers.pismo.io/pismo-docs/docs/request-types) guide for the Pismo Service Desk was updated for clarification.

  ### Transactions

  #### Fixed

  The `createdAt` field was standardized in how it's handled and delivered across transaction events and endpoints. This change ensures that all `createdAt` date values sent in the events and returned by the transaction search endpoints are consistently expressed in Coordinated Universal Time (UTC), as denoted by the suffix Z.

  At the time the [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) and [Transaction updated](https://developers.pismo.io/events/docs/transaction-update-1) events are sent, `createdAt` is now converted to UTC and correctly suffixed with Z. For example, in database timezone UTC−3, if the recorded time is `2025-01-01 12:00:00`, `createdAt` is now correctly converted and sent as `2025-01-01T15:00:00Z`.

  Previously, these events were sent with `createdAt` in the database’s configured timezone but erroneously suffixed with Z. For example, in database timezone UTC−3, if recorded time was `2025-01-01 12:00:00`, `createdAt` was sent as `2025-01-01T12:00:00Z`.

  In the [Get transaction](https://developers.pismo.io/pismo-docs/reference/gettransactionbyid) and [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions) endpoints, the response now converts from the actual database-configured timezone to UTC. For example, in database timezone UTC−5, if the recorded time is `2025-01-01 12:00:00`, `createdAt` is now correctly returned as `2025-01-01T17:00:00Z`.

  Previously, the responses always converted as if the timezone was UTC−3, which could have impacted organizations configured with other timezones. For example, in database timezone UTC−5, if the recorded time was `2025-01-01 12:00:00`, `createdAt` was incorrectly recorded as `2025-01-01T15:00:00Z` (the platform should have added 5 hours instead of 3).

  #### Docs

  In the [List transaction types](https://developers.pismo.io/pismo-docs/reference/searchtransactiontypes) endpoint, in the 200 response example, the `description` field was corrected. One instance of it was previously incorrectly listed as `processing_code`.
</summary>

<summary class="tabContent" id="Data and reporting">
  ### Reports

  #### Docs

  The description for Form 1042-S in the table in [Reports for the United States](https://developers.pismo.io/pismo-docs/docs/reports-for-the-united-states) was updated.
</summary>

<summary class="tabContent" id="Banking">
  ### Banking operations

  #### Docs

  The following banking endpoints were renamed to avoid title duplication.

  All endpoints in the Banking - Assets > [Assets](https://developers.pismo.io/pismo-docs/reference/assetregistration) section.

  All endpoints in the Banking - Overdraft > [Account](https://developers.pismo.io/pismo-docs/reference/post-attach-product-to-account) and [Program](https://developers.pismo.io/pismo-docs/reference/post-attach-product-to-program) sections.

  The following endpoints in the Transactions banking API.

  * [Get transaction banking account balance](https://developers.pismo.io/pismo-docs/reference/get-account-balances)
  * [Get transaction banking account balance history](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history)
  * [List transactions (transaction banking)](https://developers.pismo.io/pismo-docs/reference/get-corporate-transactions)
  * [Get transaction (transaction banking)](https://developers.pismo.io/pismo-docs/reference/get-corporate-transaction)
  * [List transaction status details (transaction banking)](https://developers.pismo.io/pismo-docs/reference/list-corporate-transaction-statuses)

  ### Transaction banking

  #### Updated

  The following fields are now required in the body parameters section of the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint.

  * `account_id`
  * `external_account_id`
  * `internal_operation`

  #### Updated

  The following `400` error message are now available in the following endpoints.

  `WEAM0047: The payment date cannot be earlier than the account migration date. `

  * [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
  * [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
  * [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)

  `WEAM0047: The payment date cannot be earlier than the account migration date`
  `WPMT0001: The payment date cannot be earlier than the account creation date`

  * [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
  * [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments)
  * [Cancel payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-cancel-payments)

  #### Updated

  Two new parameters for back‑value and future‑value dated transactions were added. You can now include these parameters in the metadata of [Create administrative division](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) and [Create holiday](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday) to reject specific back‑value or future‑value dated transactions.

  * `reject_back_value_dating`
  * `reject_future_value_dating`

  #### Docs

  The table of contents in the [core banking](https://developers.pismo.io/pismo-docs/docs/banking-overview) guides was reorganized, and each guide is now grouped under its appropriate category.
</summary>

<summary class="tabContent" id="Card issuing">
  ### Authorization

  #### Docs

  In the [Simulate autnorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint documentation, the following updates were made.

  * The `local_currency` body parameter was modified so that any currency code can be entered. Previously, it was incorrectly limited to two specific codes.
  * The description for the `clearing_s3_path` body parameter was updated to clarify the required format.
  * Links were added to the descriptions of the `atc` and `processing_code` body parameters.

  ### Cards

  #### New

  The new `template_id` field was added to the [Create noname card bulk](https://developers.pismo.io/pismo-docs/reference/create-bulk) request. Templates are used to implement the BIN override feature. For more information, refer to the [BIN override](https://developers.pismo.io/pismo-docs/docs/bin-override-feature) guide.

  #### New

  The following new sections and endpoints are now available.

  * Card issuing - Cards > [Mastercard benefits](https://developers.pismo.io/pismo-docs/reference/post-v1-benefits-segments-assign). You can use this section’s endpoints to manage Mastercard card benefits.
  * Card issuing - Cards > [CVV rotation](https://developers.pismo.io/pismo-docs/reference/post-v2-reset-cvv). You can use this section’s endpoints to manage CVV rotation intervals.

  ### Cards management

  #### Docs

  A new scenario (#6) for reissuing a physical card was added to the [Card reissuing](https://developers.pismo.io/pismo-docs/docs/card-reissuing) guide.

  ### Card network integration

  #### Updated

  For transactions declined with **Custom Code Z22** (Token suspended), the Merchant Denial Code was changed to `02` (the code was previously `03`). This change is reflected in the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events#card-token-validations) guide.

  ### Disputes

  #### New

  New fields were added to Visa’s [questionnaires](https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire) and objects for creating a dispute form:

  * `oneAuthForMultipleSalesInd` was added to the allocation questionnaire. This field takes a `Y` or `N` value and indicates whether one authorization was used for multiple sales.
  * `merchantAcceptInd` was added to the collaboration questionnaire under `dispute_due_to` = CS (Cancelled merchandise/services). This field takes a `Y` or `N` value and indicates whether the merchant has accepted a cancellation.
  * `explainCreditIssuedLateDetailsOfNegotiations` was added to the collaboration questionnaire under `dispute_due_to` = CN (Credit not processed). This field is used to explain the credit issued late details of negotiation.
  * `merchantRefuseAdvise` was updated for the collaboration questionnaire. It no longer supports the MRRA reason.
  * `issuerCertifiesCardholderContactedInd` was added to the `preArbitration` object for the [Create dispute form](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-forms) endpoint. It takes a `Y` or `N` value and indicates whether the issuer has certified the cardholder contact.

  #### New

  Three new fields were added to the `pre_arbitration` object that is returned in the [Get dispute](https://developers.pismo.io/pismo-docs/reference/get-v1-disputes-disputeid) and [Get dispute installment](https://developers.pismo.io/pismo-docs/reference/get-v1-disputes-installment) endpoint responses.

  * `acquirer_memo` - A string containing a memo from the acquirer included in the Mastercard pre-arbitration rejection response.
  * `action` - An enum string indicating the network pre-arbitration action,
  * `response_date` - Date of the network's pre-arbitration response.

  ### Instant payments

  #### Updated

  The following endpoints are now outdated:

  * [Create infraction report (outdated)](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-create) - It is recommended you call [Create funds recovery](https://developers.pismo.io/pismo-docs/reference/post-create-funds-recovery) instead.
  * [Update infraction report (outdated)](https://developers.pismo.io/pismo-docs/reference/patch-v2-pix-infraction) - It is recommended you call [Update funds recovery](https://developers.pismo.io/pismo-docs/reference/patch-funds-recovery) instead.

  ### Protection Bulletin

  #### Updated

  The `x-customer-id` header was removed from the [Get Protection Bulletin card](https://developers.pismo.io/pismo-docs/reference/get-v1-bulletin) and [Delete card from Protection Bulletin](https://developers.pismo.io/pismo-docs/reference/delete-v1-bulletin) endpoints.

  ### Reconciliation

  #### Docs

  The `adjustments` parameter is no longer incorrectly flagged as a required field in the [Perform clearing reconciliation](https://developers.pismo.io/pismo-docs/reference/performclearingreconciliation) endpoint.

  ### Statements

  #### Updated

  The body parameters `accrual_type` and `processing_code` were added to the [Post interest accruals](https://developers.pismo.io/pismo-docs/reference/postinterestaccruals) endpoint.

  #### Docs

  A note was added to the endpoint description for the following endpoints.

  * [Enable additional configurations on accrual types](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesconfigurations)
  * [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4)

  #### Docs

  The endpoint description for [Update account calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateacountcalendarstrategy) was updated.

  #### Docs

  The \[How payments are applied to accruals]\(doc:how-payments-are-applied-to-accruals was updated in the following ways.

  * The explanation of the Real Due Date was updated to include adjustments for holidays, weekends, and an additional buffer as defined by the program parameter.
  * A sentence in parentheses was added to Scenario 1 of Example 2, Step 3 to cover a complicating factor.

  #### Docs

  The title and the text of the last section of [Account collection status](https://developers.pismo.io/pismo-docs/docs/account-collection-status) were updated.

  ### Tokenization

  #### New

  The `product_type` field was added to the [Create encrypted card data for Apple Pay](https://developers.pismo.io/pismo-docs/reference/post-encrypted-applepay-data) endpoint. This field is a product type identifier from the Apple SDK.

  #### Updated

  The [Visa Click to Pay](https://developers.pismo.io/pismo-docs/reference/post-v1-clicktopay-enroll_customer) endpoints are no longer in beta release.
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### Docs

  Several guides were updated with information related to setting account limits.

  In the [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters) guide:

  * Added information about setting limits, now located on a dedicated Limits tab on the Program details screen in Control Center.
  * Consolidated program parameter information into this guide, removing the separate parameters guide.

  In the [Program limits](https://developers.pismo.io/pismo-docs/docs/program-limits) guide, added references to Control Center to clarify when program limits can be managed in Control Center in addition to the related APIs.

  #### Docs

  A new list item was added at the beginning of the [Get started with Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) guide - “Create, view, and manage cardholder transaction disputes“.

  #### Docs

  In [Navigating Control Center](https://developers.pismo.io/pismo-docs/docs/control-center-navigation), the first paragraph and figure in the **Customer operations** section were updated to mention disputes.

  #### Docs

  The layout and content of the [Customer operations](https://developers.pismo.io/pismo-docs/docs/customer-operations) guide were updated for consistency with other similar Control Center guides.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /bank-statements/v2/account-balances/history/config` (`post-account-balance-history-configv2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v2/account-balances/history/config` (`list-account-balance-history-configv2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` (`get-account-balance-history-config-by-id-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` (`patch-account-balances-history-configv2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v2/account-balances/history/config/{targetType}/{targetId}` (`get-account-balance-history-config-by-target-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `POST /cash-management/v2/earmarks` (`post-cash-management-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `GET /cash-management/v1/earmarks` (`get-cash-management-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `GET /cash-management/v1/earmarks/{earmarkId}` (`find-cash-management-earmark`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `PATCH /cash-management/v2/earmarks/{earmarkId}` (`patch-cash-management-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `POST /cash-management/v2/earmarks/{earmarkId}/cancel` (`post-cash-management-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `POST /acquisitions/v3/s2s/applications` (`post-acquisitions-v3-s2s-applications`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v2/accounting-scripts` (`CreateAccountingScriptV2`) | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-scripts-v2 |
| `POST /v1/accounting-scripts` (`CreateAccountingScript`) | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-scripts-v1 |
| `POST /v1/accounting-entries` (`CreateAccountingEntry`) | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-entry |
| `POST /v1/migrations/authorizations` (`PostAuthorizationsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--authorization-migration |
| `POST /v1/migrations/merchants/transactions` (`PostMerchantTransactionsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--merchant-transaction-migration |
| `POST /v1/config` (`post-config-by-tenant`) | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `POST /payment-methods-configs/v1/configs` (`post-config-by-tenant`) | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /v1/balances-config` (`post-v1-balances-config`) | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--balance-configurations |
| `GET /v2/transactions/{transactionId}` (`GetTransactionById`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `GET /v2/transactions` (`ListTransactions`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `GET /v1/transaction-types` (`SearchTransactionTypes`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `POST /v1/issuer/{issuer_id}/assets` (`AssetRegistration`) | `api-specs/Banking_-_Assets.yaml` | no | KU-API-banking-assets--assets |
| `POST /v1/overdraft/accounts/{accountId}/attach` (`post-attach-product-to-account`) | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--account |
| `POST /v1/overdraft/programs/{programId}/attach` (`post-attach-product-to-program`) | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--program |
| `GET /bank-statements/v1/account-balances/{externalAccountId}` (`get-account-balances`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v1/account-balances/{externalAccountId}/history` (`get-account-balance-history`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /corporate/v1/corporate-transactions` (`get-corporate-transactions`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |
| `GET /corporate/v1/corporate-transactions/{transactionId}` (`get-corporate-transaction`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |
| `GET /corporate/v1/corporate-transactions/status/{trackingId}` (`list-corporate-transaction-statuses`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/confirm` (`corporate-v2-post-confirm-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/cancel` (`corporate-v2-post-cancel-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /divisions-core/v2/administrative-division` (`post-v2-admin-division`) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated |
| `POST /holidays-core/v2/holiday` (`post-v2-holiday`) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat |
| `POST /networktransactions/v1/authorizations` (`post_v1-authorizations`) | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `POST /cards/v1/bulks` (`create-bulk`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `POST /pcicards/v1/pcicards/benefits/segments/assign` (`post-v1-benefits-segments-assign`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--mastercard-benefits |
| `POST /pcicards/v2/pcicards/cvv/{cardId}/reset` (`post-v2-reset-cvv`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cvv-rotation |
| `POST /v1/disputes/{disputeId}/forms` (`post-v1-disputes-disputeId-forms`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--supporting-forms |
| `GET /v1/disputes/{disputeId}` (`get-v1-disputes-disputeId`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01, KU-API-card-issuing-disputes--disputes-part-02 |
| `GET /v1/disputes/{disputeId}/installment/{disputeInstallmentId}` (`get-v1-disputes-installment`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--installments |
| `POST /v2/pix/infraction-reports` (`post-v2-pix-infraction-create`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01, KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `POST /v1/pix/funds-recoveries` (`post-create-funds-recovery`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `PATCH /v2/pix/infraction-reports/{id}` (`patch-v2-pix-infraction`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01, KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `PATCH /v1/pix/funds-recoveries/{funds_recovery_id}` (`patch-funds-recovery`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `GET /v1/bulletin/{card_id}` (`get-v1-bulletin`) | `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | no | KU-API-card-issuing-protection-bulletin--bulletin |
| `DELETE /v1/bulletin/{card_id}` (`delete-v1-bulletin`) | `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | no | KU-API-card-issuing-protection-bulletin--bulletin |
| `POST /v1/clearing-reconciliation` (`performClearingReconciliation`) | `api-specs/Card_issuing_-_Reconciliation.yaml` | no | KU-API-card-issuing-reconciliation--network-transactions-backoffice |
| `POST /v1/accounts/{accountId}/interest-accruals` (`postInterestAccruals`) | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--post-interest-accruals |
| `POST /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` (`postAccrualTypesConfigurations`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--additional-accrual-type-configurations |
| `POST /statements/v4/accounts/{accountId}/installment-payments` (`InstallmentPaymentsv4`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `PUT /v1/accounts/{accountId}/calendar-strategies` (`UpdateAcountCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--account-calendar-strategies |
| `POST /v1/cards/{cardId}/network-tokens/push-provisioning/wallets/applepay` (`post-encrypted-applepay-data`) | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--pre-digitalization |
| `POST /v1/clicktopay/visa/enroll/customer` (`post-v1-clicktopay-enroll_customer`) | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--visa-click-to-pay |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `cash-management-v2-post-payments-1` | Post payment (Pismo account ID) | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `cash-management-v2-post-confirm-payments-1` | Confirm payment (Pismo account ID) | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `cash-management-v2-post-cancel-payments-1` | Cancel payment (Pismo account ID) | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `cash-management-v2-post-scheduled-payments-1` | Schedule payment (Pismo account ID) | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `cash-management-v2-get-scheduled-payment-1` | Get scheduled payment (Pismo account ID) | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-corporate-float-cash-in` | Post float cash-in (Pismo account ID) | not found in the current OpenAPI specifications. Name-based inference: link text "Post float cash-in (Pismo account ID)" equals the endpoint name "Post float cash-in (Pismo account ID)" in the removed-endpoints list (row Transaction banking / Payments and Payment (Pismo account ID), date removed `8/12/2026`). This is a match on the endpoint name, not on an identifier. |
| `channel-control-for-back-business-date-and-cutoff-exceptions` | Channel Control for back-business-date and cutoff exceptions | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-create-bacs-1` | BACS API; Payment rails - BACS payments | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `get-an-account-specific-token-basic-authentication` | Get an account-specific token | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/1-may-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/1-may-2026 | `0ec3fc53459be637…` | not stated |

## Related knowledge units

- `KU-API-banking-assets--assets` — API reference: Banking - Assets — Assets
- `KU-API-banking-overdraft--account` — API reference: Banking - Overdraft — Account
- `KU-API-banking-overdraft--program` — API reference: Banking - Overdraft — Program
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--transactions` — API reference: Banking - Transaction banking — Transactions
- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-card-issuing-cards--cvv-rotation` — API reference: Card issuing - Cards — CVV rotation
- `KU-API-card-issuing-cards--mastercard-benefits` — API reference: Card issuing - Cards — Mastercard benefits
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--disputes-part-02` — API reference: Card issuing - Disputes — Disputes (part 2 of 2)
- `KU-API-card-issuing-disputes--installments` — API reference: Card issuing - Disputes — Installments
- `KU-API-card-issuing-disputes--supporting-forms` — API reference: Card issuing - Disputes — Supporting forms
- `KU-API-card-issuing-protection-bulletin--bulletin` — API reference: Card issuing - Protection Bulletin — Bulletin
- `KU-API-card-issuing-reconciliation--network-transactions-backoffice` — API reference: Card issuing - Reconciliation — Network transactions backoffice
- `KU-API-card-issuing-tokenization--pre-digitalization` — API reference: Card issuing - Tokenization — Pre-digitalization
- `KU-API-card-issuing-tokenization--visa-click-to-pay` — API reference: Card issuing - Tokenization — Visa Click to Pay
- `KU-API-core-platform-accounting--accounting-entry` — API reference: Core platform - Accounting — Accounting entry
- `KU-API-core-platform-accounting--accounting-scripts-v1` — API reference: Core platform - Accounting — Accounting scripts V1
- `KU-API-core-platform-accounting--accounting-scripts-v2` — API reference: Core platform - Accounting — Accounting scripts V2
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balance-config-beta--balance-configurations` — API reference: Core platform - Balance configurations — Balance configurations
- `KU-API-core-platform-balance-watcher--limit-configurations` — API reference: Core platform - Balance watcher — Limit configurations
- `KU-API-core-platform-payment-configurations--payment-method-configurations` — API reference: Core platform - Payment configurations — Payment method configurations
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-pix-management--funds-recovery` — API reference: Instant payments - Pix management — Funds recovery
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-migrations--authorization-migration` — API reference: Migrations — Authorization migration
- `KU-API-migrations--merchant-transaction-migration` — API reference: Migrations — Merchant transaction migration
- `KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated` — API reference: Platform setup - Divisions — Administrative divisions V2 (deprecated)
- `KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat` — API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)
- `KU-API-revolving-credit-calendar-management--account-calendar-strategies` — API reference: Revolving credit - Calendar management — Account calendar strategies
- `KU-API-revolving-credit-configurations--additional-accrual-type-configurations` — API reference: Revolving credit - Configurations — Additional accrual type configurations
- `KU-API-revolving-credit-interest-accruals--post-interest-accruals` — API reference: Revolving credit - Interest accruals — Post interest accruals
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
