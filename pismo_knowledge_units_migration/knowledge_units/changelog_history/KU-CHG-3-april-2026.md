---
ku_id: KU-CHG-3-april-2026
title: 'Changelog: 3 April 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/3-april-2026.md
  sha256: 0b5ad08a2fec4a85911fe9d97a804486a7324aaed13f29eb37a67d18da3b81c3
  url: https://developers.pismo.io/pismo-docs/changelog/3-april-2026
  role: changelog_post
  updated_at: ''
operations:
- ChangeAccountCollectionStatus
- CreateInstallmentAdvancement
- CreateInstallmentAdvancementV2
- InstallmentPaymentsv4
- PostMerchantsV1
- PostRecurringChargePlansV1
- PostSetupTransactionType
- PostTokensV1
- PostTransactionFlow
- UpdateStatementsDueDate
- corporate-post-v1-checks
- corporate-put-bulk-file
- corporate-v2-post-payments
- createTransactionCategory
- get-account-balance-history-config-by-id-v2
- get-account-balance-history-config-by-target-v2
- get-integrated-payments-api-v1-bankslips-issue
- get-integrated-payments-api-v1-bankslips-issue-retrieve
- get-protection-source
- get-v1-flex-controls
- getAccountsTransactionsInterest_1
- getLoansByAccountIdV2
- getMarketplaces
- getTransactionTypes_1
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-create-savings-account-product
- interest-bearing-v1-get-deposit-products
- interest-bearing-v1-get-savings-account-products
- list-account-balance-history-configv2
- listTransactionCategoryInterest
- patch-account-balances-history-configv2
- patch-v1-account-limit
- patch-v1-account-limits
- post-account-balance-history-configv2
- post-corporate-v1-restricted-funds
- post-corporate-v2-earmarks
- post-corporate-v2-register-account
- post-integrated-payments-api-v1-bankslips-issue
- post-pre-schedules
- post-protection-source
- postPreAuthenticate
- update-protection-source
- updateTransactionCategoryInterest
related_kus:
- KU-API-banking-funds-coverage--protection-sources
- KU-API-banking-integrated-payments--bank-slip-issuance
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-banking-transaction-banking--bulk-payment-files
- KU-API-banking-transaction-banking--check-posting
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--register-banking-account
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-card-issuing-3ds-authentication--pre-authentication
- KU-API-core-platform-balances-and-limits--account-limits
- KU-API-core-platform-flex-controls--program-flex-controls
- KU-API-core-platform-ledger--account-limits
- KU-API-core-platform-payment-scheduler-beta--schedules
- KU-API-core-platform-transactions--transaction-flows
- KU-API-core-platform-transactions--transaction-types
- KU-API-lending--loans
- KU-API-migrations--merchant-migration
- KU-API-migrations--recurring-charge-plan-migration
- KU-API-migrations--token-migration
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-statements--account
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-API-revolving-credit-statements--refinancing
- KU-API-revolving-credit-statements--transaction-types
- KU-API-seller-management-sellers--marketplace
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 3 April 2026
coverage_window: 6 March and 3 April 2026
---

# Changelog: 3 April 2026

**KU ID:** `KU-CHG-3-april-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **3 April 2026** (changes between 6 March and 3 April 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated"; "Deprecated".

## Topics covered

General; Core banking - Transaction banking; Control Center; Client webhooks; Flex controls; Migrations; Payments; Transactions; Security; Setup; Events; Integrated payments; Interest-bearing accounts; Transaction banking; Authorizations; Card network integration; Cards; Embossing; Statements; Lending; Marketplace; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/3-april-2026

<!-- source:begin path=changelog/3-april-2026.md part=0-end -->

# 3 April 2026

Changes between 6 March and 3 April 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### General

  #### Docs

  The new [Pismo API reference overview](https://developers.pismo.io/pismo-docs/docs/pismo-api-reference-overview) guide is now available. The guide orients new users to Pismo’s API reference documentation and serves as a reference guide for existing users looking for specific information. The guide:

  * Outlines the standard elements present on a typical endpoint page in the Pismo Developers Portal
  * Summarizes key REST API and Pismo-specific standards and attributes
  * Describes how to build and test API requests using the interactive console

  #### Docs

  The AI-powered search feature was updated in the Pismo Developers Portal. The Developers Portal now features a standalone AI assistant called Ask AI.

  The [Get started with Ask AI](https://developers.pismo.io/pismo-docs/docs/get-started-with-ask-ai) and [Get started with the Pismo Developers Portal](https://developers.pismo.io/pismo-docs/docs/welcome) guides were updated to reflect this new functionality.

  ### Core banking - Transaction banking

  #### New

  The new Funds coverage API is now available and includes the following endpoints.

  * [Create protection source](https://developers.pismo.io/pismo-docs/reference/post-protection-source)
  * [Update protection source](https://developers.pismo.io/pismo-docs/reference/update-protection-source)
  * [Get protection source](https://developers.pismo.io/pismo-docs/reference/get-protection-source)

  The new [Funds coverage](https://developers.pismo.io/pismo-docs/docs/funds-coverage) guide explains this functionality.

  #### New

  The following v2 account balance history configuration endpoints are now available to configure account balance history settings using division, organization, and program IDs.

  * [Create account balance history configuration v2](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configv2)
  * [List account balance history configuration v2](https://developers.pismo.io/pismo-docs/reference/list-account-balance-history-configv2)
  * [Get account balance history configuration by ID v2](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history-config-by-id-v2)
  * [Update account balance history configuration v2](https://developers.pismo.io/pismo-docs/reference/patch-account-balances-history-configv2)
  * [Get account balance history configuration by target type v2](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history-config-by-target-v2)

  #### New

  The new [Register banking accounts with transaction banking](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-register-account) endpoint allows you to register existing Pismo banking accounts for transaction banking, which gives you access to transaction banking APIs and features.

  ### Control Center

  #### New

  You can now create and manage Buy Now, Pay Later (BNPL) loan products in Control Center. The new [Loan products](https://developers.pismo.io/pismo-docs/docs/loan-products-cc) guide explains this functionality. This feature is currently available in the PROD-US environment.

  #### Updated

  The [dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval) feature was updated in Control Center. You can now request Pismo to enable dual approval for [holding, releasing, or transferring](https://developers.pismo.io/pismo-docs/docs/account-actions#hold-funds) funds.
</summary>

<summary class="tabContent" id="Core platform">
  ### Client webhooks

  #### Updated

  The client webhook for tokenization was updated with a `network_call_method`  field. Possible values: `VTS_DEVICE_BINDING` | `TA` | `VTS_APPROVE_PROVISIONING` | `VTS_APPROVE_PROVISIONING_ISO`. The Visa example for the `original_network_data` field was updated. The following new custom codes were added.

  | Custom code | Description                             | VTS action code | MDES action code |
  | :---------- | :-------------------------------------- | :-------------- | :--------------- |
  | ELFR2       | CVV2 retry limit exceeded               | 05              | 05               |
  | MATPC       | Exceeded maximum active tokens per card | 05              | 05               |
  | FRE         | Cryptogram data validation failed       | 05              | 05               |

  ### Flex controls

  #### New

  The new [List program flex controls](https://developers.pismo.io/pismo-docs/reference/get-v1-flex-controls) endpoint is now available.

  ### Migrations

  #### Updated

  The following fields were added to the [Migrate tokens](https://developers.pismo.io/pismo-docs/reference/posttokensv1) endpoint.

  * `expiry_date`
  * `network`
  * `status`
  * `tc_date_time`
  * `token`
  * `token_unique_ref`
  * `wallet_identifier`
  * `device_id`
  * `correlation_id`

  #### Docs

  The field descriptions in the following endpoints were updated for editorial enhancements to align with Pismo documentation standards and best practices.

  * [Migrate merchants](https://developers.pismo.io/pismo-docs/reference/postmerchantsv1)
  * [Migrate recurring charge plans](https://developers.pismo.io/pismo-docs/reference/postrecurringchargeplansv1)

  ### Payments

  #### Docs

  The denial codes list in the [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations#response-and-denial-codes) guide was updated to correctly list and define `CBD` (card broken) and `CDB` (card blocked).

  #### Deprecated

  The deprecated `currency` field was removed throughout the [payment scheduler](https://developers.pismo.io/pismo-docs/reference/post-pre-schedules) API.

  ### Transactions

  #### Updated

  In the [Create transaction type](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) and [Create transaction flow](https://developers.pismo.io/pismo-docs/reference/posttransactionflow) endpoints, the following new response is now available.

  * Status code 409 - Error WTRC08001 - The provided `transaction_type_id` is reserved by the platform and cannot be used.

  ### Security

  #### Updated

  Due to security issues, you can no longer generate your own certificate and sign it with your own Certificate Authority when configuring identity connectivity with mTLS. In addition, certificates will now expire after two years instead of three. Both of these changes are reflected in the [Identity connectivity with mTLS](https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls) guide.

  #### Docs

  The following changes were made to the JWT claims list in the [Verifying webhook requests](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests) guide.

  * The JWT claim `aud` (audience/host name) was removed from the table because it is not a valid claim in the JWT token that Pismo provides.
  * The JWT claim `body-hash` was corrected to replace the incorrect format of “`body_hash`”.
  * The JWT claim `kid` is no longer marked “not always provided” as it is always part of the JWT.

  #### Docs

  The JSON request sample code in the [Authentication with OAuth2](https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2) guide was updated to indicate the recommended use of “data-urlencode” instead of “data”. Although the request works with “data”, “data-urlencode” is needed for some specific credentials when generated with special characters (such as `(  )`).

  ### Setup

  #### Docs

  In the [Create balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config-1) endpoint, the `global_config` parameter was added to documentation.

  #### Docs

  The [Update account limits (outdated)](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit)  endpoint was marked as outdated. Use the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limits)  endpoint instead, which also validates the account limit against the configured program global limit. The [Account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects)  guide was updated accordingly.
</summary>

<summary class="tabContent" id="Data">
  ### Events

  #### New

  The new [Cycle closing configuration created](https://developers.pismo.io/events/docs/account-balances-cycle-close-config-1) event is now available. The platform generates this event when a new account balance history configuration is created using organization, division, or program IDs.

  #### New

  The new [Account inactive\_since status updated](https://developers.pismo.io/events/docs/corporate-inactive-since-updated-1) event is now available to provide information how long a bank account has been inactive.

  #### New

  The [External payout processed](https://developers.pismo.io/events/docs/deposit-product-external-payout-1) event is now available. The platform generates this event when payouts are successfully processed and an external payout account was configured during product attachment.
</summary>

<summary class="tabContent" id="Banking">
  ### Integrated payments

  #### Updated

  The new `transaction_id` field is now available in the following endpoints. This is the ID that links the bank slip to the specific transaction performed in the payments API. It can be used for tracking, reconciliation, and reference purposes when managing bank slips and their associated transactions.

  * [Issue bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-issue) 
  * [List issued bank slips](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-bankslips-issue)
  * [Get issued bank slip](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-bankslips-issue-retrieve)

  ### Interest-bearing accounts

  #### Updated

  The `subsequent_withdrawals` field was added to the `penalties` object in the following endpoints. This field allows you to define a withdrawal window that applies a penalty to subsequent withdrawal events. 

  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products)

  #### Updated

  The corresponding fee IDs and penalty transaction flow were added to the following penalty types in the [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) endpoint.

  * `early_withdrawal_after_opening`
  * `grace_period`
  * `tiered_interest_forfeiture`
  * `withdrawal_fee`
  * `subsequent_withdrawals`

  #### Docs

  The new [Penalties for deposit products](https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts#penalties-for-deposit-products) section in the Interest-bearing accounts guide provides details on penalties, their corresponding fee IDs, and transaction flows.

  #### Docs

  The new `min_amount` field allows you to specify the minimum amount required for yield calculation. This field was added to the following endpoints.

  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products)

  #### Docs

  The "savings account" was renamed to "savings account product" in the documentation for the following endpoints.

  * [Create savings account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-savings-account-product)
  * [Get savings account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-savings-account-products)

  ### Transaction banking

  #### Updated

  The [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint now includes the following error codes.

  * `WEAM0016`: Invalid header account. Informs clients that the `x-account-id` header is invalid or malformed.
  * `WEAM0024`: The account cannot be credited. Credit function is not active. Returned when the account cannot receive credits, whether because it is inactive or for another related reason.

  #### Updated

  The [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint now includes the following error codes.

  * `WPMT0008`: Invalid processing code. Returned when the processing code is invalid.
  * `WPMT0014`: Account is closed. Returned when the account is closed.
  * `WPMT0019`: Cannot use same account for credit and debit. Returned when clients attempt to use the same account for both credit and debit in a transfer.
  * `WPMT0032`: Validation rules conflict with internal accounts program. Returned when validation rules conflict with the internal accounts program.
  * `WCAC0002`: Invalid header account. Indicates that the `x-account-id` header is invalid or malformed.
  * `WCAC0012`: Account not found. Returned when the account cannot be found.

  #### Updated

  The [Settle float payment](https://developers.pismo.io/pismo-docs/reference/patch-corporate-float-cash-in) endpoint now includes the following error codes.

  * `WCFC0022`: Transaction using this tracking\_id is in progress, please try again later. Returned when a transaction with the same tracking ID is already in progress.
  * `WCFC0023`: Operations blocked for account. Returned when an operations block is in place on the account.

  #### Updated

  The [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks) endpoint now includes the following error code.

  * `WCPT0014`: Invalid account currency code: 999. Returned when the client provides an invalid currency code.

  #### Updated

  The [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds) endpoint now includes the following error codes.

  * `WRFO0014`: Invalid restricted funds processing code. Returned when the client provides an invalid processing code for a restricted funds operation.
  * `WRFO0003`: Account is locked, please try again later. Returned when the account is locked because of concurrent operations.

  #### Updated

  The [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint now includes the following error code about division IDs being set with an invalid timezone.

  * `WPMT0002`: invalid timezone (invalid)

  #### Updated

  The [Upload bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file) endpoint now includes the following bulk header-related 400 error codes.

  * `WBUP0004`: Invalid request header
  * `WBUP0005`: Invalid JSON data in bulk header
  * `WBUP0006`: Authentication OrgID does not match Bulk Header
  * `WBUP0007`: BulkID in URL does not match Bulk Header
  * `WBUP0008`: Invalid operation\_type in Bulk Header
</summary>

<summary class="tabContent" id="Card issuing">
  ### Authorizations

  #### Docs

  The [Authorization configurations](https://developers.pismo.io/pismo-docs/docs/authorization-configurations-1) guide was updated to correctly indicate that the `always_call_ledger_rules` field is only required for Full balance and is not required for Zero balance.

  ### Card network integration

  #### Docs

  A new guide, [PAN encryption for 3DS authentication](https://developers.pismo.io/pismo-docs/docs/pan-encryption-for-3ds-authentication), was published to describe the PAN encryption process for use with the [Send pre-authentication info](https://developers.pismo.io/pismo-docs/reference/postpreauthenticate) endpoint.

  ### Cards

  #### Updated

  The `activation_date` field was removed from the [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event.

  ### Embossing

  #### Docs

  A new section was added to the Physical embossing guide—[Embossing flows](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing#embossing-flows)—that describes the endpoint/event flows for embossing nominal and noname cards.

  ### Statements

  #### Updated

  The following changes were made in the [Create installment advancement](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2) and [Create installment advancement (outdated)](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancement) endpoints.

  * The new option `REMOVE_ALL_INTEREST` was added to the `calculator` field and the field description was updated.
  * The endpoint descriptions were modified to clarify how to handle the interest on advanced installments.

  #### Updated

  The `x-program-id` header field was removed from the following endpoints.

  * [List program transaction categories](https://developers.pismo.io/pismo-docs/reference/listtransactioncategoryinterest) 
  * [Update program transaction category](https://developers.pismo.io/pismo-docs/reference/updatetransactioncategoryinterest)
  * [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory)
  * [List account transaction category rates](https://developers.pismo.io/pismo-docs/reference/getaccountstransactionsinterest_1) 
  * [List program transaction types](https://developers.pismo.io/pismo-docs/reference/gettransactiontypes_1)

  #### Updated

  The following change occurs in the [Payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) API.

  Starting March 30th, 2026, payment agreement transactions will be created using Payment methods. This change provides greater flexibility and includes the following enhancements: 

  * Support for processing codes. 
  * Use of the same authorization ID for payment agreement cancellation transactions. 
  * Support for creating additional transactions, such as insurance, when the agreement is created. 

  Rollout schedule: 

  * April 6 to 17: EXT
  * April 20: Other Prod environment (except Prod-MT and Itaú)
  * May 18: Prod-MT environment 
  * June 1: Itaú environment 

  This change does not affect current customer processes. 

  #### Docs

  The [Delinquency buckets](https://developers.pismo.io/pismo-docs/docs/delinquency-buckets) guide no longer applies only to India, because at least one other country is using delinquency buckets. So, “(India only)” was removed from the beginning of the guide. The second paragraph was also modified to remove the reference to India.

  #### Docs

  The [Credit card refinancing](https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt) guide was divided and some information was moved into the following new guides.

  * [Installment agreements](https://developers.pismo.io/pismo-docs/docs/installment-agreements)
  * [Statement agreements](https://developers.pismo.io/pismo-docs/docs/statement-agreements)
  * [Compulsory agreements](https://developers.pismo.io/pismo-docs/docs/compulsory-agreements)

  These 3 guides replace the following guides, which have been deleted.

  * Create an installment agreement
  * Create a statement agreement
  * Create a compulsory agreement

  The remaining text in the [Credit card refinancing](https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt) guide was updated to improve clarity.

  #### Docs

  The description of the [Change due date](https://developers.pismo.io/pismo-docs/reference/updatestatementsduedate) endpoint was updated to emphasize that the due date must be updated no later than two days before the cycle closes.

  #### Docs

  The text of the [Managing the charge order for debit transactions](https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions) guide was updated to improve clarity.

  #### Docs

  The following sections were added to the end of the Full balance credit program guide.

  * [Closing an account](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#closing-an-account)
  * [Definitive cancellation: Permanently stopping credit cycles](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#definitive-cancellation-permanently-stopping-credit-cycles)

  These features are not new but they haven’t been documented before.

  #### Docs

  The \[Accrual type rate structure]\(doc:configuring-accrual-rates#accrual-type-rate-structure section was updated for clarity. The callout in the [Validation for configuring accruals](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#validation-for-configuring-accruals) section was updated for the same reason.

  #### Docs

  The Installment management guide was replaced with the [Installment advancements](https://developers.pismo.io/pismo-docs/docs/installment-advancements-guide), since the original guide primarily covered installment advancements. Most of the material in the [Installment advancements](https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt#installment-advancements) section was moved into the new guide.

  #### Docs

  The [Accruals](https://developers.pismo.io/pismo-docs/docs/understanding-statements#accruals) section was updated to clarify how the MAD determines whether the Pismo platform considers the debits as paid, refinanced, or overdue.

  #### Docs

  The header names of the first two columns in the table in the [Update account collection status](https://developers.pismo.io/pismo-docs/reference/changeaccountcollectionstatus) endpoint documentation were switched because they were labeled in the wrong order. That is, the first column was incorrectly labeled “Account status”. It is now “Collection status”. The second column was incorrectly labeled “Collection status”. It is now “Account status”.

  #### Deprecated

  The **Accrual rate discount** program parameter was removed from the table in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide. This program parameter has been deprecated for some time and has now been decommissioned.
</summary>

<summary class="tabContent" id="Digital lending">
  ### Lending

  #### Updated

  The [List account loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2) page was updated to include the following new loan status options and their descriptions: SCHEDULED, PROCESSING, PAID, PARTIALLY\_PAID, PAST\_DUE, CANCELED, NOT\_PAID.
</summary>

<summary class="tabContent" id="Seller management">
  ### Marketplace

  #### New

  The new [List marketplaces](https://developers.pismo.io/pismo-docs/reference/getmarketplaces) is now available. This endpoint returns a paginated list of marketplaces with optional filtering and sorting capabilities.
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### Updated

  The [Interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center) guide was updated to reflect the enhanced Control Center experience, which makes it easier to configure how interest is calculated and applied across products, including:

  * **Interest thresholds**—Set minimum and maximum limits for interest rates
  * **Interest by tiers**—Apply different rates to different portions of a balance

  This feature is currently available in the PROD-US environment.

  #### Docs

  The [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters) guide was updated to clarify that you cannot remove transaction types from existing transaction categories for programs.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/protection-sources` (`post-protection-source`) | `api-specs/Banking_-_Funds_coverage.yaml` | no | KU-API-banking-funds-coverage--protection-sources |
| `PATCH /v1/protection-sources` (`update-protection-source`) | `api-specs/Banking_-_Funds_coverage.yaml` | no | KU-API-banking-funds-coverage--protection-sources |
| `GET /v1/protection-sources/accounts/{accountId}` (`get-protection-source`) | `api-specs/Banking_-_Funds_coverage.yaml` | no | KU-API-banking-funds-coverage--protection-sources |
| `POST /bank-statements/v2/account-balances/history/config` (`post-account-balance-history-configv2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v2/account-balances/history/config` (`list-account-balance-history-configv2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` (`get-account-balance-history-config-by-id-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` (`patch-account-balances-history-configv2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v2/account-balances/history/config/{targetType}/{targetId}` (`get-account-balance-history-config-by-target-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `POST /corporate/v2/corporate-accounts/register` (`post-corporate-v2-register-account`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--register-banking-account |
| `GET /v1/flex-controls` (`get-v1-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--program-flex-controls |
| `POST /v1/migrations/tokens` (`PostTokensV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--token-migration |
| `POST /v1/migrations/merchants` (`PostMerchantsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--merchant-migration |
| `POST /v1/migrations/recurring-charge-plans` (`PostRecurringChargePlansV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--recurring-charge-plan-migration |
| `POST /v1/pre-schedules` (`post-pre-schedules`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/transaction-types` (`PostSetupTransactionType`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `POST /v1/transaction-flow` (`PostTransactionFlow`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `PATCH /v1/accounts/{accountId}/limits` (`patch-v1-account-limit`) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `PATCH /v1/accounts/{accountId}/limits` (`patch-v1-account-limits`) | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--account-limits |
| `POST /v1/bankslips-issue` (`post-integrated-payments-api-v1-bankslips-issue`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `GET /v1/bankslips-issue` (`get-integrated-payments-api-v1-bankslips-issue`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `GET /v1/bankslips-issue/client-requests/{clientRequestId}` (`get-integrated-payments-api-v1-bankslips-issue-retrieve`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/deposits/{productId}` (`interest-bearing-v1-get-deposit-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/savings-accounts` (`interest-bearing-v1-create-savings-account-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/savings-accounts/{productId}` (`interest-bearing-v1-get-savings-account-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v1/checks` (`corporate-post-v1-checks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/restricted-funds` (`post-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `PUT /corporate/v1/bulk-payments/{bulkId}` (`corporate-put-bulk-file`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |
| `POST /v1/preauthenticate` (`postPreAuthenticate`) | `api-specs/Card_issuing_-_3DS_authentication.yaml` | no | KU-API-card-issuing-3ds-authentication--pre-authentication |
| `POST /v2/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancementV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `POST /v1/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancement`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | **yes** | KU-API-revolving-credit-installment-management--installment-advancements |
| `GET /statements-v2/v1/transactions-categories` (`listTransactionCategoryInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` (`updateTransactionCategoryInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `POST /statements-v2/v1/transactions-categories` (`createTransactionCategory`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `GET /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` (`getAccountsTransactionsInterest_1`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `GET /statements-v2/v1/programs-transactions-types` (`getTransactionTypes_1`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--transaction-types |
| `POST /statements/v4/accounts/{accountId}/installment-payments` (`InstallmentPaymentsv4`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `PUT /statements/v1/accounts/{accountId}/statements/due-date` (`UpdateStatementsDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `PATCH /statements-v2/v1/accounts/{accountId}` (`ChangeAccountCollectionStatus`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account |
| `GET /v2/accounts/{accountId}/loans` (`getLoansByAccountIdV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v3/marketplaces` (`getMarketplaces`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-v1-balances-config-1` | API; Balance configurations API; Create balance configuration; balance configuration | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `patch-corporate-float-cash-in` | Settle float payment | not found in the current OpenAPI specifications. Name-based inference: link text "Settle float payment" equals the endpoint name "Settle float payment" in the removed-endpoints list (row Transaction banking / Payments and Payment (Pismo account ID), date removed `8/12/2026`). This is a match on the endpoint name, not on an identifier. |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/3-april-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/3-april-2026 | `0b5ad08a2fec4a85…` | not stated |

## Related knowledge units

- `KU-API-banking-funds-coverage--protection-sources` — API reference: Banking - Funds coverage — Protection sources
- `KU-API-banking-integrated-payments--bank-slip-issuance` — API reference: Banking - Integrated payments — Bank slip issuance
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-banking-transaction-banking--bulk-payment-files` — API reference: Banking - Transaction banking — Bulk payment files
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--register-banking-account` — API reference: Banking - Transaction banking — Register banking account
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-card-issuing-3ds-authentication--pre-authentication` — API reference: Card issuing - 3DS authentication — Pre-authentication
- `KU-API-core-platform-balances-and-limits--account-limits` — API reference: Core platform - Balances and limits — Account limits
- `KU-API-core-platform-flex-controls--program-flex-controls` — API reference: Core platform - Flex controls — Program flex controls
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-core-platform-payment-scheduler-beta--schedules` — API reference: Core platform - Payment scheduler — Schedules
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-migrations--merchant-migration` — API reference: Migrations — Merchant migration
- `KU-API-migrations--recurring-charge-plan-migration` — API reference: Migrations — Recurring charge plan migration
- `KU-API-migrations--token-migration` — API reference: Migrations — Token migration
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-statements--account` — API reference: Revolving credit - Statements — Account
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-API-revolving-credit-statements--transaction-types` — API reference: Revolving credit - Statements — Transaction types
- `KU-API-seller-management-sellers--marketplace` — API reference: Seller management - Sellers — Marketplace
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
