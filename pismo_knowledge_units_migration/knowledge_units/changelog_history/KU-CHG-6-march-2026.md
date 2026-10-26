---
ku_id: KU-CHG-6-march-2026
title: 'Changelog: 6 March 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/6-march-2026.md
  sha256: f28393621e7f74648cbee09d3dc04ca859ee3996d40e294ff981ff11719a51c1
  url: https://developers.pismo.io/pismo-docs/changelog/6-march-2026
  role: changelog_post
  updated_at: ''
operations:
- CancelInstallmentAdvancement
- CreateInstallmentAdvancement
- CreateInstallmentAdvancementV2
- GetInstallmentAdvancementV2ById
- GetIntallmentAdvancementById
- ListCalendars
- ListTransactions
- PatchCreditorOperationByIdV1
- PatchTransactionFlow
- PostCreditorsOperationsV2
- PostTransactionsV1
- PutCreditorsOperationsV2
- account-parameters-find
- cancelInstallmentAdvanceV2
- corporate-get-v1-check-settlement-operations
- corporate-get-v1-checks-id
- corporate-post-v1-checks
- create-payment-agreement-simulation
- delinquent-account-closure-get
- get-accounts-v1-accounts
- get-fps-in-transaction
- get-refund-recovery
- get-v1-global-configs
- getByStatementId
- getInterestAccrualSummarization
- getTotalDue
- getTransactionTypes
- getTransactionsBalance
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-get-deposit-products
- list-account-fund-recoveries
- patch-funds-recovery
- patch-v1-account-limits
- patch-v1-global-configs-program-programId
- performClearingReconciliation
- post-acquisitions-v3-s2s-applications
- post-cancel-fps
- post-corporate-v1-checks-checkId-cancel
- post-corporate-v1-checks-release
- post-create-cob
- post-create-funds-recovery
- post-get-funds-recovery-infractions
- post-get-funds-recovery-refunds
- post-merchant-transaction-cancel
- post-merchant-transaction-sale
- post-recurrence-automatic
- post-release-fps
- post-schedule-pix-payment
- post-split-request
- post-v1-global-configs
- post-v1-sync-offline-pin
- post-v2-card
- postAccountAccrualTypesRates
- postAccrualTypesRates
- postPreAuthenticate
- post_v1-authorizations
related_kus:
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-transaction-banking--check-posting
- KU-API-card-issuing-3ds-authentication--pre-authentication
- KU-API-card-issuing-authorization--authorizations
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--pci
- KU-API-card-issuing-reconciliation--network-transactions-backoffice
- KU-API-core-platform-accounts--account-parameters
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balances-and-limits--account-limits
- KU-API-core-platform-balances-and-limits--program-limits
- KU-API-core-platform-transactions--transaction-flows
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-automatic-pix--automatic-pix
- KU-API-instant-payments-pix-management--funds-recovery
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-instant-payments-qr-code--qr-code
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-API-migrations--transaction-migration
- KU-API-revolving-credit-calendar-management--list-calendars
- KU-API-revolving-credit-configurations--account-accrual-rates
- KU-API-revolving-credit-configurations--program-accrual-rates
- KU-API-revolving-credit-delinquent-account--delinquent-account-closure
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation
- KU-API-revolving-credit-statements--accruals
- KU-API-revolving-credit-statements--statement
- KU-API-revolving-credit-statements--transaction-types
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-API-seller-management-transactions--merchant-transactions
- KU-API-seller-management-transactions--split-requests
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 6 March 2026
coverage_window: 6 February and 6 March 2026
---

# Changelog: 6 March 2026

**KU ID:** `KU-CHG-6-march-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **6 March 2026** (changes between 6 February and 6 March 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated".

## Topics covered

General; Core platform - Account parameters; Core platform - Program limits; Core banking - Transaction banking; Card issuing - Reconciliation; Card issuing - Statements; Control Center; Lending; Accounts; Client webhooks; General; Migrations; Payments; Rates and fees; Security; Setup; Transactions; Events; Instant payments; Transaction banking; 3DS authentication; Card network integration; Cards; Cards management; Full balance credit program; Statements; Marketplace; Transactions; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/6-march-2026

<!-- source:begin path=changelog/6-march-2026.md part=0-end -->

# 6 March 2026

Changes between 6 February and 6 March 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### General

  #### Docs

  The new [Get started with the Pismo Developers Portal](https://developers.pismo.io/pismo-docs/docs/welcome) guide is now available. It replaces the previous **Welcome to Pismo** guide and introduces the following improvements.

  * Improved introductory content to better orient new users to the Pismo Developers Portal
  * Restructured content to highlight the four main areas of the Developers Portal and their use cases
  * Additional visual aids to support written content

  On the [landing page](https://developers.pismo.io/pismo-docs), the **Get started with card issuing** feature card was replaced with a **New to the Developers Portal?** feature card to highlight the new guide.

  ### Core platform - Account parameters

  #### New

  The new guide [Account parameters](https://developers.pismo.io/pismo-docs/docs/account-parameters-reference-table) is now available to list available account parameters, which are configurable properties that manage how an account is set up and how it behaves. All account parameters have corresponding [program parameters](https://developers.pismo.io/pismo-docs/reference/program-parameters-reference-table). Account parameters give you the option of configuring the same properties differently for specific accounts. The link to the new guide was added to the [account parameters](https://developers.pismo.io/pismo-docs/reference/account-parameters-find) endpoints.

  ### Core platform - Program limits

  #### New

  The Pismo platform now allows you to control the total granted limit distributed across all accounts within a program. This feature ensures that the program-level global limit is enforced during operations that increase or decrease limit values, such as account creation, limit updates, or program transfers.

  The following new endpoints support this functionality.

  * [Configure program limit](https://developers.pismo.io/pismo-docs/reference/post-v1-global-configs)
  * [Get program limits](https://developers.pismo.io/pismo-docs/reference/get-v1-global-configs)
  * [Update program limit](https://developers.pismo.io/pismo-docs/reference/patch-v1-global-configs-program-programid)
  * [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits)

  Refer to the [Program limits](https://developers.pismo.io/pismo-docs/docs/program-limits) guide for details.

  ### Core banking - Transaction banking

  #### Docs

  The following new guides are now available.

  * [Check posting and settlement](https://developers.pismo.io/pismo-docs/docs/check-posting-and-settlement)
  * [File-based check processing and bulk settlement](https://developers.pismo.io/pismo-docs/docs/file-based-check-processing-and-bulk-settlement)

  ### Card issuing - Reconciliation

  #### New

  The new endpoint [Perform clearing reconciliation](https://developers.pismo.io/pismo-docs/reference/performclearingreconciliation) is now available. If a problem is encountered during the clearing process for Clearing/Base II authorization events, you can use this endpoint to reconcile the clearing, taking over the reprocessing of messages in the Dead Letter Queue (DLQ), assuming the responsibility to reconcile unprocessed clearing messages. All messages that have been sent to the DLQ can be reconciled through this endpoint. Clearing reconciliation is available for Visa and Mastercard only. Clearing reconciliation details were added to the updated [Clearing / Base II](https://developers.pismo.io/pismo-docs/docs/clearingbase#clearingbase-ii-workflow) and the [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events#clearingbase-ii-events) guides.

  ### Card issuing - Statements

  #### New

  The new endpoint [List calendars](https://developers.pismo.io/pismo-docs/reference/listcalendars) is now available. Use this endpoint to list the calendars for a program, optionally filtering on due date, program calendar strategy ID, or division ID.

  ### Control Center

  #### Updated

  Processing codes and transaction types were updated in Control Center to align with the updated Processing code API. With this change, you can now do more with processing codes and transaction types with Control Center, including:

  * Link authorization, reversal, and partial reversal processing codes
  * Replace assigned reversal processing codes
  * Edit processing code and transaction type names
  * Adjust transaction flows
  * Filter processing codes by any field

  The [Create processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/create-processing-codes-and-transaction-types) guide and the [Add a transaction type to an existing processing code](https://developers.pismo.io/pismo-docs/docs/add-a-transaction-type-to-an-existing-processing-code) guide were updated to reflect the new functionality.

  ### Lending

  #### Docs

  The new guide [Loan product setup](https://developers.pismo.io/pismo-docs/docs/loan-product-setup) is now available. It provides information on setting up loan products on the Pismo platform, covering required product attributes and configuration needed to support loan simulation, booking, disbursement, and lifecycle management via the lending APIs.

  #### Docs

  The new guide [Loan simulation](https://developers.pismo.io/pismo-docs/docs/loan-simulation) is now available. It explains how to create draft loan simulations on the Pismo platform, enabling lenders to model loan terms and repayment schedules before finalizing a loan. The guide shows how draft simulations support customer review and iteration prior to booking and disbursement.
</summary>

<summary class="tabContent" id="Core platform">
  ### Accounts

  #### Docs

  In the [accounts](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoints, `person` object, the `document_issued_date`’s format was incorrectly listed as being “yyyy-mm-dd” when it should have been “dd/mm/yyyy”.

  #### Docs

  In the [Get account  endpoint](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts) response, the misnamed `collection_status` field has been corrected to `collections_status`.

  ### Client webhooks

  #### Docs

  The descriptions for the request fields for [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) were updated to provide clarifying details.

  #### Docs

  The [Client webhooks for VCAS](https://developers.pismo.io/pismo-docs/docs/vcas-client-webhooks) guide was updated to include an overview flow diagram and updated overview text to help clarify the Visa Consumer Authentication Service (VCAS) as used within the Pismo platform.

  ### General

  #### Docs

  The abbreviation format for Not Applicable (N/A) was standardized and explicitly defined in the following guides to improve accessibility.

  * [Request types and common fields](https://developers.pismo.io/pismo-docs/docs/request-types)
  * [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table)
  * [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations)
  * [Core platform - Payments](https://developers.pismo.io/pismo-docs/docs/payments-data-events)
  * [Core platform - Transactions](https://developers.pismo.io/pismo-docs/docs/transactions-data-events)
  * [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list)
  * [Overdue tolerance](https://developers.pismo.io/pismo-docs/docs/overdue-tolerance)
  * [Visa collaboration and allocation questionnaires](https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire)

  ### Migrations

  #### Docs

  The [Migrate transactions](https://developers.pismo.io/pismo-docs/reference/posttransactionsv1) field descriptions have been updated for clarity and order.

  ### Payments

  #### Updated

  In the Authorization validation rules for platform operations guide, the new `RATES_LOGICAL_ERROR` reason was added to the [Operation amount calculation](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations#operation-amount-calculation) rule.

  ### Rates and fees

  #### Docs

  The new section [Use Merchant Category Codes to allow or disallow over-limits](https://developers.pismo.io/pismo-docs/docs/over-limit-fee#use-merchant-category-codes-to-allow-or-disallow-over-limits) was added to the Over-limit fees guide.

  ### Security

  #### Docs

  A new section, [PGP encryption for card embossing](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide#pgp-encryption-for-card-embossing), was added to the Pismo platform security guide to define and describe the use of Pretty Good Privacy (PGP) encryption for card embossing.

  ### Setup

  #### Docs

  The [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide was updated for documentation standards. One note was updated to better explain account parameters and a link was added to the new [Account parameters](https://developers.pismo.io/pismo-docs/docs/account-parameters-reference-table) guide.

  #### Docs

  The value in the **Category** column of the **Fine amount for late payment** program parameter was updated in [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table). It was incorrectly listed as "Rate". It is now correctly listed as "Parameter".

  ### Transactions

  #### Updated

  In the [Update transaction flow](https://developers.pismo.io/pismo-docs/reference/patchtransactionflow) endpoint, the following responses are now available.

  * Status code 400 - Error WTRC05003 - Transaction type doesn't exist.
  * Status code 409 - Error ETRC04004 - The provided transaction type is already configured for the processing code.
  * Status code 409 - Error ETRC04005 - The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract.

  #### Docs

  In the [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions) endpoint, the following 400 response examples for error WTRC00001 were added:

  * Number of latest transactions should not have another filter
  * Number of latest transactions should be an integer
  * Invalid range for number of latest transactions
  * Invalid authorization type
  * Account is required when querying by card ID
  * Event date start not provided
  * Invalid event date start format
  * Invalid event date end format
  * Invalid time range
</summary>

<summary class="tabContent" id="Data and reporting">
  ### Events

  #### New

  The following events were added to simplify notifications for processing interest-bearing accounts credit accruals.

  For deposit products:

  * [Capitalization credit processing failed](https://developers.pismo.io/events/docs/deposit-product-capitalization-failure-1)
  * [Capitalization payment processed](https://developers.pismo.io/events/docs/deposit-product-capitalization-payout-1)
  * [Capitalization credit processed](https://developers.pismo.io/events/docs/deposit-product-capitalization-success-1)

  For savings account products:

  * [Capitalization credit processing failed](https://developers.pismo.io/events/docs/savings-account-product-capitalization-failure-1)
  * [Capitalization credit processed](https://developers.pismo.io/events/docs/savings-account-product-capitalization-success-1)
</summary>

<summary class="tabContent" id="Core banking">
  ### Instant payments

  #### New

  The following new Faster Payment System (UK) endpoints are now available in beta release.

  * [Cancel FPS inbound transaction](https://developers.pismo.io/pismo-docs/reference/post-cancel-fps)
  * [Release FPS inbound transaction](https://developers.pismo.io/pismo-docs/reference/post-release-fps)
  * [Get FPS transaction](https://developers.pismo.io/pismo-docs/reference/get-fps-in-transaction)

  #### Updated

  The following instant payment API/sections and their endpoints that were previously in beta release are now available in regular release.

  * [Instant payments - Pix payments > Schedule transfers V2](https://developers.pismo.io/pismo-docs/reference/post-schedule-pix-payment)
  * [Instant payments - Automatic Pix](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic) (this API was also moved from under **Instant payments - Pix payments** to its own section in the API reference)
  * [Instant payments - QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-cob)

  #### New

  The following new Pix Dict API funds recovery endpoints are now available.

  * [List account fund recoveries](https://developers.pismo.io/pismo-docs/reference/list-account-fund-recoveries) -  Gets all funds recovery records for an account.
  * [List funds recovery infractions](https://developers.pismo.io/pismo-docs/reference/post-get-funds-recovery-infractions) - Gets a list of infractions for a funds recovery
  * [List funds recovery refund requests](https://developers.pismo.io/pismo-docs/reference/post-get-funds-recovery-refunds) -  Gets a list of refund requests for a funds recovery
  * [Update funds recovery](https://developers.pismo.io/pismo-docs/reference/patch-funds-recovery) - Updates some funds recovery fields.

  #### Docs

  The new [Suspense transaction flow](https://developers.pismo.io/pismo-docs/docs/faster-payment-system#suspense-transaction-flow) section was added to the Faster Payment System (UK) guide that details the flow for a transaction that fails an anti-fraud check and is put on hold.

  #### Updated

  Interactive flow for Pix DICT [funds recovery](https://developers.pismo.io/pismo-docs/reference/pix-funds-recovery) endpoints is no longer supported. Only the Automatic flow, where the Diretório de Identificadores de Contas Transacionais (DICT)—a national Pix key registry and database—automatically manages tracking and blocking using a standard algorithm is now supported. The `flow_type` parameter, which specified interactive or automatic, was removed from the [Create funds recovery](https://developers.pismo.io/pismo-docs/reference/post-create-funds-recovery) endpoint. The **Create tracking graph** and **Block funds recovery** endpoints were removed.

  For the [Get tracking graph](https://developers.pismo.io/pismo-docs/reference/get-refund-recovery) endpoint, the following changes were made.

  * Query parameter `graphId` has been removed
  * The `fundsRecoveryId` query parameter was renamed to `funds_recovery_id`
  * A new `created_at` field was added to the response
  * The `graph_id` parameter was removed from the response
  * Fields `created_at` in the `person` and `account` objects are now optional
  * The `hop` field  was removed from the `transaction` object

  ### Transaction banking

  #### Updated

  As part of the migration to transaction banking with a single balance, the `PAY` maturity instruction was removed so that deposit products accept only `ROLLOVER` or `NULL` to support rollover behavior or no action at maturity. All `PAY`‑related functionality was fully removed. This effort impacts the `maturity_instructions` object of the following endpoints.

  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products)

  #### Updated

  The following endpoints are now available in general release and the \[beta] tag was removed from them.

  * [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks)
  * [Get check posting](https://developers.pismo.io/pismo-docs/reference/corporate-get-v1-checks-id)
  * [Release check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-release)
  * [Cancel check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-checkid-cancel)
  * [List check settlement operations](https://developers.pismo.io/pismo-docs/reference/corporate-get-v1-check-settlement-operations)

  #### Deprecated

  The endpoint **Get AES key** (`GET /corporate/v1/bulk-payments/encryption-keys/{bulkId}`) was decommissioned.

  * Its documentation was removed from the API reference.
  * Its entry was removed from [API endpoint deprecation and removal schedule](https://developers.pismo.io/pismo-docs/docs/deprecation-schedule).
  * An entry for it was added to [API endpoints removed](https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed).
</summary>

<summary class="tabContent" id="Card issuing">
  ### 3DS authentication

  #### Docs

  The path for the [Send pre-authentication info ](https://developers.pismo.io/pismo-docs/reference/postpreauthenticate)  endpoint was updated to remove a duplicated section. It now correctly displays the path: `https://api-sandbox.pismolabs.io/3ds-acs/v1/preauthenticate`.

  ### Card network integration

  #### Docs

  The [Authorization validation rules for card network operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations#list-of-rules) guide and the [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list#flex-controls-validation) guide were updated to correctly reflect that flex controls validation is available for both Full balance and Zero balance integrations.

  #### Docs

  The [Visa Consumer Authentication Service (VCAS)](https://developers.pismo.io/pismo-docs/docs/visa-consumer-authentication-service-vcas) guide was updated to include additional overview information and flow diagrams for each of the use cases for VCAS as used within the Pismo platform.

  #### Docs

  The [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint was updated to mention the ability to cancel a simulation in the test environment and examples for Create authorization and Cancel authorization were updated for clarification. The `processing_julian_date` field was corrected to properly show the format as YYDDD.

  #### Docs

  The [List of rules](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations#list-of-rules) table in the Authorization validation rules for card network operations guide now correctly reflects that Flex controls are valid for Zero balance, with limitations. A note was added to the [Flex controls validation](https://developers.pismo.io/pismo-docs/docs/rule-list#flex-controls-validation) section of the Rule list guide to explain how Flex controls work with Zero balance.

  ### Cards

  #### New

  A new Cards API section (**Migration**) and two new endpoints are now available in beta release.

  * [Migrate card to different program](https://developers.pismo.io/pismo-docs/reference/post-migrate-card) - You can use this endpoint to transfer a card to a different program. Prior to this, you could only migrate between programs at the account level. In other words, the issuer can migrate an account from program A to program B, but cards cannot. Reissues are required to ensure the new card has the same program as the account.
  * [Migrate card mode](https://developers.pismo.io/pismo-docs/reference/post-migrate-card-mode) - Migrate a card's secondary mode (debit or credit) to a new program. If a combination card is initially created with a credit account (has a `CREDIT` mode), it gets migrated when the Migrate card to different program endpoint is called. However, if you wish to migrate the debit (secondary) mode, you need to call this endpoint.

  #### Updated

  The `template_id` field was added to the 200 and 201 responses for the [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card) endpoint. Templates are used to implement the [BIN override feature](https://developers.pismo.io/pismo-docs/docs/bin-override-feature).

  #### Updated

  The [Synchronize offline pin](https://developers.pismo.io/pismo-docs/reference/post-v1-sync-offline-pin) endpoint no longer requires creating a Jira ticket to use.

  ### Cards management

  #### Docs

  A new section was added to the Embossing rules in the [Physical card embossing](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing#pretty-good-privacy-pgp-key-encryption) guide to describe the use of Pretty Good Privacy (PGP) encryption for card embossing.

  ### Full balance credit program

  #### Docs

  The [Program transaction types](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#program-transaction-types) section of the Full balance credit program guide was updated to add clarity on how program transaction types are mapped to program transaction categories.

  ### Statements

  #### Updated

  The `overridden_amount_due` body parameter is now available in the [Create payment agreement simulation](https://developers.pismo.io/pismo-docs/reference/create-payment-agreement-simulation) endpoint.

  #### Docs

  In the [List transaction balances](https://developers.pismo.io/pismo-docs/reference/gettransactionsbalance) endpoint, the following updates were made.

  * The minimum attribute of 1 was added to the `accountID` path parameter.
  * The `transactionTypeId` path parameter was changed to an array of int64s. It was incorrectly listed as just an int64 previously.

  #### Updated

  A new program parameter, **Ignore grace days on pending accruals reversal for revolving accounts**, was added to the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide.

  #### Docs

  The description of the `status` body parameter in the [Get delinquent account closure process information](https://developers.pismo.io/pismo-docs/reference/delinquent-account-closure-get) endpoint was updated in the following ways.

  * A description was added for every possible value of the enum.
  * `CREDIT_SEPARATED_TRANSACTION_REQUESTED`, which was missing from the enum list, was added.

  #### Docs

  A row for **Ignore grace days on pending accruals reversal for revolving accounts** was added to the table in the [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals) guide.

  #### Docs

  The description of the `period_to_calculate` body parameter was updated in the [Configure program accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates) and [Configure account accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates) endpoints.

  #### Docs

  The [List transaction types](https://developers.pismo.io/pismo-docs/reference/gettransactiontypes) endpoint was incorrectly marked as deprecated and was updated to remove the DEPRECATED tag. It is scheduled to be deprecated, but it hasn’t been deprecated yet. The note in the endpoint description was updated to explain that it will be deprecated. The first line of the description was also rewritten to better conform to documentation standards.

  #### Docs

  The [Credit liquidation](https://developers.pismo.io/pismo-docs/docs/credit-liquidation) and [Managing due date, cycle closing date, and additional grace periods](https://developers.pismo.io/pismo-docs/docs/managing-grace-period) guides were rewritten to clarify the grace days logic.

  #### Docs

  The capitalization of a body parameter in the [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid) was corrected from `presenttoPast`  to `presentToPast`.

  #### Updated

  The `omitId` query parameter was added to the [Get interest accrual summary](https://developers.pismo.io/pismo-docs/reference/getinterestaccrualsummarization) endpoint.

  #### Updated

  A deprecated endpoint for the Statements API was added to the [API endpoint deprecation and removal schedule](https://developers.pismo.io/pismo-docs/docs/deprecation-schedule).

  * Deprecated endpoint: GET /statements/v1/accounts/\{accountId}/total-due
  * Replacement endpoint: [Get account total due](https://developers.pismo.io/pismo-docs/reference/gettotaldue)

  #### Docs

  The list of enums for the `status` field in the 202 response for the [Create installment advancement](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2) endpoint was updated. The original list was incorrect.

  #### Docs

  All the guides under [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements) were reorganized to improve the ordering. [Fixed due date calendars](https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars) and [Fixed cycle closing calendar management strategy](https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy) were moved underneath [Calendar management strategies](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies).

  #### Docs

  **(V2)** was removed from the names of the following endpoints.

  * [Create installment advancement](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2)
  * [Get installment advancement](https://developers.pismo.io/pismo-docs/reference/getinstallmentadvancementv2byid)
  * [Cancel installment advancement](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentadvancev2)

  The names of the following endpoints were updated with the word **(outdated)** and notes were added in the endpoint descriptions explaining why that the above endpoints should be used instead.

  * [Create installment advancement (outdated)](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancement)
  * [Get installment advancement (outdated)](https://developers.pismo.io/pismo-docs/reference/getintallmentadvancementbyid)
  * [Cancel installment advancement (outdated)](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentadvancement)
</summary>

<summary class="tabContent" id="Seller management">
  ### Marketplace

  #### Updated

  An additional `fees` field was added to the following creditor operations endpoints.

  * [Create marketplace creditor operations](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperationsv2)
  * [Update creditor operations](https://developers.pismo.io/pismo-docs/reference/putcreditorsoperationsv2)
  * [Update creditor operation](https://developers.pismo.io/pismo-docs/reference/patchcreditoroperationbyidv1)

  #### Docs

  The following outdated and unused endpoints relating to head branch configurations were removed.

  * **Create merchants relationships**
  * **Delete merchant branches**
  * **Delete merchant branch relationships**

  The following corresponding events relating to head branch configurations were also removed.

  * **Merchant head branch relationship disabled**
  * **Merchant head branch relationship created**

  ### Transactions

  #### Updated

  The new `currency_code` field was added to the [Create merchant transaction](https://developers.pismo.io/pismo-docs/reference/post-merchant-transaction-sale) and [Cancel merchant transaction](https://developers.pismo.io/pismo-docs/reference/post-merchant-transaction-cancel) endpoints. This field represents the currency of a transaction with an alphabetic or numeric string.

  #### Updated

  Corrected description for a successful call response in [Create merchant transaction](https://developers.pismo.io/pismo-docs/reference/post-merchant-transaction-sale) and [Cancel merchant transaction](https://developers.pismo.io/pismo-docs/reference/post-merchant-transaction-cancel) endpoints.

  #### Docs

  The `definitions` field description was revised for clarity and accuracy within the [Create split request](https://developers.pismo.io/pismo-docs/reference/post-split-request) endpoint.
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### New

  A new user role, API keys approver (controlc-api-approver), was added to Control Center. This new role is listed and defined in the [User permissions and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles) guide and the [Get started with SSO for Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-sso-for-control-center) guide.

  #### Docs

  The [Access keys for basic authentication](https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication) guide was updated to correctly identify the basic server-to-server key pair as `server_key` and `server_secret`, with updated descriptions of each key for clarification.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `GET /accounts/v1/accounts/{accountId}/parameters` (`account-parameters-find`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--account-parameters |
| `POST /v1/global-configs` (`post-v1-global-configs`) | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--program-limits |
| `GET /v1/global-configs` (`get-v1-global-configs`) | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--program-limits |
| `PATCH /v1/global-configs/program/{programId}` (`patch-v1-global-configs-program-programId`) | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--program-limits |
| `PATCH /v1/accounts/{accountId}/limits` (`patch-v1-account-limits`) | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--account-limits |
| `POST /v1/clearing-reconciliation` (`performClearingReconciliation`) | `api-specs/Card_issuing_-_Reconciliation.yaml` | no | KU-API-card-issuing-reconciliation--network-transactions-backoffice |
| `GET /v1/programs/{programId}/calendars` (`ListCalendars`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--list-calendars |
| `POST /acquisitions/v3/s2s/applications` (`post-acquisitions-v3-s2s-applications`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `GET /accounts/v1/accounts/{accountId}` (`get-accounts-v1-accounts`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v1/migrations/transactions` (`PostTransactionsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--transaction-migration |
| `PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId}` (`PatchTransactionFlow`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `GET /v2/transactions` (`ListTransactions`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `POST /v1/payments/fps/cancel/{endToEndId}` (`post-cancel-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/fps/release/{endToEndId}` (`post-release-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `GET /v1/payments/fps/{endToEndId}` (`get-fps-in-transaction`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /pix/v2/pix/out/scheduler` (`post-schedule-pix-payment`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `POST /inst-pull-pay/v1/pix/automatic` (`post-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /v1/pix/qrcode/cob` (`post-create-cob`) | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--qr-code |
| `GET /v1/pix/funds-recoveries` (`list-account-fund-recoveries`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `GET /v1/pix/funds-recoveries/{funds_recovery_id}/infractions` (`post-get-funds-recovery-infractions`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `GET /v1/pix/funds-recoveries/{funds_recovery_id}/refunds` (`post-get-funds-recovery-refunds`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `PATCH /v1/pix/funds-recoveries/{funds_recovery_id}` (`patch-funds-recovery`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `POST /v1/pix/funds-recoveries` (`post-create-funds-recovery`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `GET /v1/pix/funds-recoveries/{funds_recovery_id}/tracking-graph` (`get-refund-recovery`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/deposits/{productId}` (`interest-bearing-v1-get-deposit-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /corporate/v1/checks` (`corporate-post-v1-checks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `GET /corporate/v1/checks/{checkId}` (`corporate-get-v1-checks-id`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/release` (`post-corporate-v1-checks-release`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/{checkId}/cancel` (`post-corporate-v1-checks-checkId-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `GET /corporate/v1/checks/{checkId}/settlement-operations` (`corporate-get-v1-check-settlement-operations`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /v1/preauthenticate` (`postPreAuthenticate`) | `api-specs/Card_issuing_-_3DS_authentication.yaml` | no | KU-API-card-issuing-3ds-authentication--pre-authentication |
| `POST /networktransactions/v1/authorizations` (`post_v1-authorizations`) | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `POST /wallet/v2/cards` (`post-v2-card`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /pcicards/v1/pcicards/{cardId}/scripts/sync-offline-pin` (`post-v1-sync-offline-pin`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--pci |
| `POST /v1/accounts/{accountId}/payment-agreement-simulations` (`create-payment-agreement-simulation`) | `api-specs/Revolving_credit_-_Statement_refinancing_API.yaml` | no | KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation |
| `GET /statements-v2/v1/accounts/{accountId}/transactions-balance` (`getTransactionsBalance`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `GET /v1/accounts/{account_id}` (`delinquent-account-closure-get`) | `api-specs/Revolving_credit_-_Delinquent_account.yaml` | no | KU-API-revolving-credit-delinquent-account--delinquent-account-closure |
| `POST /v1/programs/{programId}/accrual-type-rates` (`postAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `POST /v1/accounts/{accountId}/accrual-type-rates` (`postAccountAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `GET /statements-v2/v1/transactions-types` (`getTransactionTypes`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--transaction-types |
| `GET /statements-v2/v3/accounts/{accountId}/statements` (`getByStatementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals/summarization` (`getInterestAccrualSummarization`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `GET /statements-v2/v2/accounts/{accountId}/total-due` (`getTotalDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /v2/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancementV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `GET /v2/accounts/{accountId}/installment-advance/{advancementId}` (`GetInstallmentAdvancementV2ById`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}` (`cancelInstallmentAdvanceV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `POST /v1/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancement`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | **yes** | KU-API-revolving-credit-installment-management--installment-advancements |
| `GET /v1/accounts/{accountId}/installment-advance/{advancementId}` (`GetIntallmentAdvancementById`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | **yes** | KU-API-revolving-credit-installment-management--installment-advancements |
| `DELETE /v1/accounts/{accountId}/installment-advance/{advancementId}` (`CancelInstallmentAdvancement`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | **yes** | KU-API-revolving-credit-installment-management--installment-advancements |
| `POST /v2/marketplaces/{marketplaceId}/creditors-operations` (`PostCreditorsOperationsV2`) | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `PUT /v2/marketplaces/{marketplaceId}/creditors-operations` (`PutCreditorsOperationsV2`) | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `PATCH /v1/marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` (`PatchCreditorOperationByIdV1`) | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` (`post-merchant-transaction-sale`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--merchant-transactions |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel` (`post-merchant-transaction-cancel`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--merchant-transactions |
| `POST /v1/transactions/{merchantTransactionId}/split` (`post-split-request`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `program-parameters-reference-table` | Program parameters; program parameters | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `pix-funds-recovery` | funds recovery | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-migrate-card` | Migrate card to different program | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-migrate-card-mode` | Migrate card mode | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/6-march-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/6-march-2026 | `f28393621e7f7464…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-API-card-issuing-3ds-authentication--pre-authentication` — API reference: Card issuing - 3DS authentication — Pre-authentication
- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--pci` — API reference: Card issuing - Cards — PCI
- `KU-API-card-issuing-reconciliation--network-transactions-backoffice` — API reference: Card issuing - Reconciliation — Network transactions backoffice
- `KU-API-core-platform-accounts--account-parameters` — API reference: Core platform - Accounts — Account parameters
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balances-and-limits--account-limits` — API reference: Core platform - Balances and limits — Account limits
- `KU-API-core-platform-balances-and-limits--program-limits` — API reference: Core platform - Balances and limits — Program limits
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-automatic-pix--automatic-pix` — API reference: Instant payments - Automatic Pix — Automatic Pix
- `KU-API-instant-payments-pix-management--funds-recovery` — API reference: Instant payments - Pix management — Funds recovery
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-instant-payments-qr-code--qr-code` — API reference: Instant payments - QR Code — QR Code
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-API-migrations--transaction-migration` — API reference: Migrations — Transaction migration
- `KU-API-revolving-credit-calendar-management--list-calendars` — API reference: Revolving credit - Calendar management — List calendars
- `KU-API-revolving-credit-configurations--account-accrual-rates` — API reference: Revolving credit - Configurations — Account accrual rates
- `KU-API-revolving-credit-configurations--program-accrual-rates` — API reference: Revolving credit - Configurations — Program accrual rates
- `KU-API-revolving-credit-delinquent-account--delinquent-account-closure` — API reference: Revolving credit - Delinquent account — Delinquent account closure
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation` — API reference: Revolving credit - Statement refinancing — Payment agreement simulation
- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-API-revolving-credit-statements--transaction-types` — API reference: Revolving credit - Statements — Transaction types
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-API-seller-management-transactions--merchant-transactions` — API reference: Seller management - Transactions — Merchant transactions
- `KU-API-seller-management-transactions--split-requests` — API reference: Seller management - Transactions — Split requests
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
