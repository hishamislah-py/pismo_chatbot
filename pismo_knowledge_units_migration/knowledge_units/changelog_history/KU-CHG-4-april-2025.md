---
ku_id: KU-CHG-4-april-2025
title: 'Changelog: 4 April 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/4-april-2025.md
  sha256: 9e094fa042f17799d5e0264ae4af38522a398ec7fb780ae22df623e48b37b21c
  url: https://developers.pismo.io/pismo-docs/changelog/4-april-2025
  role: changelog_post
  updated_at: ''
operations:
- ChangeAccountCollectionStatus
- CreateProcessingCode
- CreateProgramBasedOnTemplate
- GetCurrentStatement
- GetInstallmentPayments
- GetTransactionById
- InstallmentPaymentsv4
- ListTransactions
- PostDisputeV1
- PostOnUsAuthorizationsV1
- PostSetupTransactionType
- SearchTranscationMetaDataCount
- cancel-bulk
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- corporate-v2-post-scheduled-payments
- create-recurring-charge-plan
- createProgramParameter
- createProgramTransactionType
- get-config-by-tenant
- getAccountAccrualsV3
- getByStatementId
- getInterestAccrualSummarization
- getMinimumPaymentCalculationMemory
- getProgramDueDates
- getTransactionsBalance
- interest-bearing-calculate-average-balance
- interest-bearing-get-average-balance
- list-division-v2
- list-dormancy-configs
- merchant-transaction-advancement
- merchants-advancements-data
- patch-corporate-v2-earmarks-earmarkid
- patch-division-v2
- patch-v1-account-limit
- post-acquisitions-v3-s2s-applications
- post-authorization
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-division-v2
- post-funds-transfer
- post-hierarchies
- post-list-cards
- post-passport-v2-s2s-access-token
- post-schedule-pix-payment
- post-v1-interest-plan
- post-validate-card-data
- saveAccountTransactionInterest
- setProgramParameters
- setProgramsParameters
- statementDueDate
- updateProgramDueDate
related_kus:
- KU-API-banking-interest-bearing-accounts--average-balance
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--hierarchies
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-card-issuing-cards--noname
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balance-watcher--limit-configurations
- KU-API-core-platform-ledger--account-limits
- KU-API-core-platform-payment-configurations--payment-method-configurations
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-core-platform-transactions--transaction-types
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-instant-payments-rupay-on-upi--upi
- KU-API-migrations--dispute-migration
- KU-API-migrations--on-us-authorization-migration
- KU-API-platform-authentication--authentication
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-API-platform-setup-programs--parameters
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-configurations--program-transaction-types
- KU-API-revolving-credit-recurring-charges--recurring-charge-plans
- KU-API-revolving-credit-statements--account
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--accruals
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--refinancing
- KU-API-revolving-credit-statements--statement
- KU-API-seller-management-merchant-advance--merchant-advancement
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 4 April 2025
coverage_window: 7 March and 4 April 2025
---

# Changelog: 4 April 2025

**KU ID:** `KU-CHG-4-april-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **4 April 2025** (changes between 7 March and 4 April 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated".

## Topics covered

Core platform - Client webhooks; Core banking - Banking operations; Core banking - Rule models; Seller management - Merchants; Resources - Control Center; Accounts; Authentication; Client webhooks; Flexible transaction controls; Ledger; Migrations; Payments; Security; Setup; Transactions; Events; Instant payments; Interest management; Transaction banking; Card network integration; Disputes; Noname; Statements; Tokenization; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/4-april-2025

<!-- source:begin path=changelog/4-april-2025.md part=0-end -->

# 4 April 2025

Changes between 7 March and 4 April 2025

<div class="customTab"></div>

<summary class="tabContent" id="New features">

### Core platform - Client webhooks

#### New

In compliance with the regulatory order of BACEN (Central Bank of Brazil), article 30 of circular 3978/2020, which enters into force on 11 April 2025, the document number and the name of the account holder must be sent in messages between the issuer and the card network, for example, messages 0110 and 0210. This regulatory order is applicable to all card networks.

Pismo will handle the fulfillment of this data for accounts and cards that have this kind of information in Pismo database and are full balance. However, you can override the information using the [Full balance anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook). In cases where the issuer has "noname" cards, the issuer is responsible to send this information in the webhook.

For zero balance issuers, Pismo will expect this data in the webhook so the platform can build the message with the data provided by the issuer. The [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) was updated to support this.

#### New

In compliance with the VISA release 1.3: Requirements to Support Account Name Inquiry Functionality in Account Verification Messages, changes were made to both [Full balance anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook) and the [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook).

For full balance customers, Pismo will handle the matching result or the sending of the cardholder’s name. However, using the anti-fraud webhook, issuers can override the data and send the information themselves.

### Core banking - Banking operations

#### New

The Interest-bearing accounts API now includes two new endpoints that allow you to calculate average balance for an account according to the datetime range specified.

* [Calculate average balance](https://developers.pismo.io/pismo-docs/reference/interest-bearing-calculate-average-balance) calculates an average balance for an account by specifying a datetime range.
* [Get average balance](https://developers.pismo.io/pismo-docs/reference/interest-bearing-get-average-balance) retrieves an already calculated average balance for an account.

### Core banking - Rule models

#### Updated

The "Core platform - Processing codes management” API was renamed to [Core platform - Rule models](https://developers.pismo.io/pismo-docs/reference/post-org-rule-model-1) to more accurately reflect its functionality. Rule models allow you to change a processing code during authorization.  The API has been rewritten, reorganized and edited with additional text. To accompany this, a [Changing processing codes during authorization with rule models](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types#changing-processing-codes-during-authorization-with-rule-models) section was added to the Processing codes guide.

### Seller management - Merchants

#### New

The Merchant advancement API now includes two new endpoints that allow you to create or simulate a merchant advancement request for specific transactions by specifying a merchant transaction ID.

* [Simulate transaction advancement](https://developers.pismo.io/pismo-docs/reference/merchant-transaction-advancement) allows you to select which merchant transactions you want to advance.
* [Get advancement](https://developers.pismo.io/pismo-docs/reference/merchants-advancements-data) returns information about an existing merchant transaction advancement request.

### Resources - Control Center

#### New

**Security and organization**

Pismo Control Center is being updated in all test and production environments over the next few months, starting in April 2025. The new version includes security enhancements that impact user accounts, such as two-step identity verification and stricter password requirements. During the update period, depending on the environment, you will use either the updated version or the legacy version. For details, refer to the [Get started](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) guide for Control Center.

Security improvements to Pismo Control Center have changed how new users register their accounts. Instead of a link, they receive two separate emails. User administrators are now able to resend these emails to any user who has not responded. In addition, the requirements for creating a Control Center password are more robust.

The organization name that displays on all Control Center screens now enables you to quickly access any of the other organizations you belong to, without having to sign off and then back on again with a different user ID. Select the organization name and choose one of the available organizations.

**General ledger accounts**

Control Center now supports viewing and adding [General ledger accounts](https://developers.pismo.io/pismo-docs/docs/cc-general-ledger-accounts).

</summary>

<summary class="tabContent" id="Core platform">

### Accounts

#### Deprecated

The following accounts endpoints were deprecated and will be removed on 1 September 2025:

* GET /v2/accounts/:accountld/statements/:statementld/transactions
* GET /v1/accounts/:accountld/transactions
* GET /v2/accounts/:accountld/statements
* GET /v1/accounts/:accountld/statements
* POST /v2/customers/document-number
* GET /v1/customers/:customerId/authorizations
* PUT /v1/accounts/:accountld/duedate
* GET /v1/accounts/:accountld/authorizations

Please use the following endpoints instead:

* [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions)
* [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid)
* [Update statements due date](https://developers.pismo.io/pismo-docs/reference/updateprogramduedate)
* [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)

#### Docs

The new account status - `DEBIT_ONLY` - is now documented in the [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview#account-status) guide. This is the default status for accounts created after July, 2024.

This status indicates the account is active and allows cash-out but not cash-in. Accounts created before July, 2024 have `NORMAL` as their default status.

### Authentication

#### Updated

The `external_acount_id` parameter was removed from the [Get basic authentication access token](https://developers.pismo.io/pismo-docs/reference/post-passport-v2-s2s-access-token) endpoint of the Platform authentication API.

### Client webhooks

#### Docs

The `atc_database` request field was updated for both the [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) and the [Full balance anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook) in the Client webhooks guide to correctly identify the field as a string, with an example in the definition. Both sample requests were updated accordingly.

### Flexible transaction controls

#### Updated

In the [Evaluation requested](https://developers.pismo.io/events/docs/audit-evaluation-requested-1) event, removed `currency_code` from the `accounts.from` object.

#### Docs

In the [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls) and Control Center [Flex controls](https://developers.pismo.io/pismo-docs/docs/cc-flex-controls) guides, the introductions were updated for clarity.

#### Docs

In the [Create flex control per transaction type](https://developers.pismo.io/pismo-docs/docs/flex-controls#create-flex-control-per-transaction-type) example, the withdrawal processing code was corrected to be `01`.

### Ledger

#### Docs

In the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint documentation, the event name and field descriptions were updated.

### Migrations

#### New

The Migrations API now includes the new [Migrate disputes](https://developers.pismo.io/pismo-docs/reference/postdisputev1) endpoint.

#### Updated

The [Migrate on-us authorizations](https://developers.pismo.io/pismo-docs/reference/postonusauthorizationsv1) endpoint now includes the new `InstallmentsDetails` object.

### Payments

#### Updated

In the [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) endpoint, the new `tags` field was added to the processing codes object. This is an array of enum strings with the following possible values: `GLOBAL`, `BRAZIL`, `ARGENTINA`, `INDIA`, `NETWORK`, `VISA`, `MASTERCARD`, `ELO`, `RUPAY`, `TECBAN`, `UPI`, `PIX`, `BNPL`, `DEPRECATED`.

#### Updated

The [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization)  endpoint now includes idempotency logic that returns status code 200 with the original authorization data for duplicate `tracking_id` requests.

#### Updated

In the [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event, the `authorization_validations` field is now available.

#### Updated

In the [Anti-fraud integration](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations#anti-fraud-integration) validation, the `override_type` field was added to `additional_data`.

#### Docs

In the [Create adjustment (deprecated)](https://developers.pismo.io/pismo-docs/reference/post-adjustments-v1-adjustments) endpoint documentation, the event name was updated.

#### Docs

The [Get configuration by Org](https://developers.pismo.io/pismo-docs/reference/get-config-by-tenant) endpoint in the Payment configurations API was updated to include a note clarifying that the organization and account information is pulled from the access token.

### Security

#### Docs

The [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid) guide was updated to give clarification regarding the Pismo-provided claims (keys) when generating your JSON Web Token (JWT). The values for the four keys, `iss`, `sub`, `aud`, and `tenant_id`, are provided by Pismo and are automatically generated by Control Center when a user creates a new credential.

#### Docs

The instructions for [Checking message integrity](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests#checking-message-integrity) in the Verifying webhook requests guide were rewritten for clarification.

### Setup

#### Docs

The [Programs](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) API was comprehensively edited and rewritten for clarity. Additional text about export/import steps, program type IDs, and program types was added. Endpoint descriptions were significantly rewritten. The following endpoints were renamed:

* Create program parameter > [Link parameter to program](https://developers.pismo.io/pismo-docs/reference/createprogramparameter) (This endpoint links an optional parameter to a program.)
* Set program parameter for one of more programs > [Update program(s) parameter](https://developers.pismo.io/pismo-docs/reference/setprogramsparameters)
* Set one or more program parameters for program > [Update program parameter(s)](https://developers.pismo.io/pismo-docs/reference/setprogramparameters)

#### Docs

A note was added to the [Program types](https://developers.pismo.io/pismo-docs/docs/program-types) guide about program implementation and how long it takes for a program to be operational once created. Pismo has a 90 hour service level agreement to do the back-end configurations needed before a program can be used.

### Transactions

#### Docs

The `x-account-id` header parameter was removed on the following transactions endpoints.

* [Get transaction](https://developers.pismo.io/pismo-docs/reference/gettransactionbyid)
* [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions)
* [Get transaction count](https://developers.pismo.io/pismo-docs/reference/searchtranscationmetadatacount)

#### Docs

In the [Create transaction type](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) endpoint documentation, the event name was updated.

</summary>

<summary class="tabContent" id="Data and reporting">

### Events

#### Docs

In the [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1) event documentation, all of the `trigger_reason` types now include detailed descriptions.

</summary>

<summary class="tabContent" id="Core banking">

### Instant payments

#### Updated

The new `flex_controls` parameter was added to the Pix [Schedule transfer(s) V2](https://developers.pismo.io/pismo-docs/reference/post-schedule-pix-payment) endpoint . This parameter applies a flex control to a Pix scheduled transfer.

#### Docs

More information was added to the [RuPay and UPI instant payments](https://developers.pismo.io/pismo-docs/docs/united-payments-interface) guide about initial connection with the Pismo platform. Text was added to the [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-funds-transfer) endpoint about `account_reference_number` and the need to call [List cards](https://developers.pismo.io/pismo-docs/reference/post-list-cards) and [Validate card data](https://developers.pismo.io/pismo-docs/reference/post-validate-card-data) before calling Transfer funds.

### Interest management

#### Docs

The [Interest management](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) API was updated to conform with Pismo standards: some endpoints were renamed,  descriptions updated, and so on.

### Transaction banking

#### Updated

Previously, in the following endpoints, the error message was `value must be 999,999,999,999.99 or less`. It is now updated to `value must be 100,000,000,000,000,000 or less`.

* In [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments), for the 400 error `amount value exceeded`.
* In [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments), for error WMPL0002.
* In [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments), for error WPMT0018.

#### Updated

In the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint, the following errors were added to inform a duplicate earmark or tracking ID has already been used:

409:

* `WEAM0001: earmark_id [{earmark_id}] is already in use.`
* `WEAM0025: Tracking ID is already in use.`

423:

* `WEAM0033: transaction using this tracking_id is in progress, please try again later.`

#### Updated

In the [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel) endpoint, the 403 error was added to indicate a duplicate tracking ID is already in use: `WEAM0025: Tracking ID is already in use.`

#### Updated

The new 400 error `WCMN0004 : Invalid cursor` was added to the following endpoints to allow the return of a more specific invalid cursor error instead of a generic 500 `Internal server error`:

* [List division](https://developers.pismo.io/pismo-docs/reference/list-division-v2)
* [List dormancy configurations](https://developers.pismo.io/pismo-docs/reference/list-dormancy-configs)

#### Updated

The new 400 error `WDIV0018: Invalid hierarchy` was added to the following endpoints. This error occurs while creating a division with an organization ID whose hierarchy belongs to a different organization.

* [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2)
* [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2)

#### Updated

The new 400 error message `WHIE0007: levels should have at least 1 item` is issued when a request to [Create hierarchy](https://developers.pismo.io/pismo-docs/reference/post-hierarchies) is made with the levels field left empty. Although this field is a required field, it does not force customers to add values to the child fields, thereby causing an error such as: levels: \[]. The addition of this new error is part of a validation mechanism to examine whether the required field and subfield index have values in them.

#### Updated

The new 400 error `Amount has invalid decimal places for currency` was added to the following endpoints. This error is generated when the amount submitted has incorrect decimal places; for example, for USD, the maximum allowed decimal place is two, while JPY (Japanese Yen) does not allow any decimal places. The decimal places for currency follow the ISO 4217 standard.

* [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
* [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
* [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
* [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments)

#### Docs

The new section **Custom processing codes** was added to advise customers that an error would occur if they use their own custom processing codes in a transaction without first informing Pismo, as using client’s own custom processing codes requires special configuration from Pismo. This section was added to the following guides:

* [Earmarks](https://developers.pismo.io/pismo-docs/docs/earmarks#custom-processing-codes)
* [Future-business-dated transactions](https://developers.pismo.io/pismo-docs/docs/future-biz-dated-txns#custom-processing-codes)

#### Docs

The following error was removed from the [Common error messages](https://developers.pismo.io/pismo-docs/docs/bulk-file-based-payment-processing#common-error-messages) section in Bulk file-based payment processing:

`WBLK1008:  Invalid signature: Org ID or bulk ID is not the same for signature and original files.`

</summary>

<summary class="tabContent" id="Card issuing">

### Card network integration

#### Updated

The [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list) guide was updated to include previously undocumented rules and a number of rules were updated or corrected.

The following rules were added to the guide:

* [Fetch program](https://developers.pismo.io/pismo-docs/docs/rule-list#fetch-program)
* [DCC validation](https://developers.pismo.io/pismo-docs/docs/rule-list#dcc-validation)
* [Installments validation](https://developers.pismo.io/pismo-docs/docs/rule-list#installments-validation)
* [Message format validation](https://developers.pismo.io/pismo-docs/docs/rule-list#message-format-validation)
* [Max installments number validation](https://developers.pismo.io/pismo-docs/docs/rule-list#max-installments-number-validation)

The following rules were updated to include `additional_data` field information:

* [Valid card token validation](https://developers.pismo.io/pismo-docs/docs/rule-list#valid-card-token-validation)
* [Account type validation](https://developers.pismo.io/pismo-docs/docs/rule-list#account-type-validation)
* [Token status validation](https://developers.pismo.io/pismo-docs/docs/rule-list#token-status-validation)
* [Card mode status validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-mode-status-validation)
* [Card status validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-status-validation)
* [Account status validation](https://developers.pismo.io/pismo-docs/docs/rule-list#account-status-validation)
* [Unexpected errors](https://developers.pismo.io/pismo-docs/docs/rule-list#unexpected-errors)

The following rules were updated with corrections or clarifications:

* [Card inputted expiration date validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-inputted-expiration-date-validation)—a more detailed description was added, the custom code list was corrected, and a new payload example was added
* [Card expiration date validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-expiration-date-validation)—a more detailed description was added
* [Available limits validation](https://developers.pismo.io/pismo-docs/docs/rule-list#available-limits-validation)—more `additional_field` information was added and the payload examples were updated to include the new fields
* [Flex controls validation](https://developers.pismo.io/pismo-docs/docs/rule-list#flex-controls-validation)—more `additional_field` information was added and the payload example was updated to include the new fields
* [Processing code definition](https://developers.pismo.io/pismo-docs/docs/rule-list#processing-code-definition)—`APPROVED` status was added
* [Valid card token validation](https://developers.pismo.io/pismo-docs/docs/rule-list#valid-card-token-validation)—updated to include the `custom_code` additional data field

#### Updated

A new Visa response code was added for custom code IMF (invalid message format) due to a mandate from the latest Visa release. This new code, `5C`, is for card not present transactions, such as e-commerce transactions. This new response code is shown in the Authorization validations table in the Validation codes for authorization events guide.

The Visa response codes for MPC (program configuration not found) and PGE (program configuration generic error) were changed from `14` to `N0`.

#### Docs

The [Clearing event examples](https://developers.pismo.io/pismo-docs/docs/authorization-events#clearing-event-examples) section of the Authorization events guide was updated to include an ELO settlement file example.

### Disputes

#### Updated

The following fields were removed from the [Consumer disputes](https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire#consumer-disputes-reason-13) and the [Processing errors](https://developers.pismo.io/pismo-docs/docs/visa-colloboration-questionaire#processing-errors-reason-12) tables:

* `AccountStatus` in dispute\_due\_to = Late Presentment (processing errors table)
* `MerchandiseIdentifiedAsCounterfeit` in dispute\_due\_to = Counterfeit Merchandise (consumer disputes table)
* `InfoMerchandiseToBeCounterfeit` in dispute\_due\_to = Counterfeit Merchandise (consumer disputes table)

### Noname

#### New

The new [Cancel noname bulk operation](https://developers.pismo.io/pismo-docs/reference/cancel-bulk) endpoint is now available. Noname cards are batch-generated and not initially associated with customers, which occurs later.

### Statements

#### New

The [Get interest accrual summary](https://developers.pismo.io/pismo-docs/reference/getinterestaccrualsummarization) endpoint now allows requests with periods of up to 60 days. However, for periods between 31 and 60 days, the `interest_accrual_ids` field is omitted in the response. The endpoint description was updated to explain this.

#### New

The new program parameter **Enable accrual reversal for new accrual types** was added to the table in the [Program parameters](https://developers.pismo.io/pismo-docs/reference/program-parameters-reference-table) guide.

#### Docs

The endpoint name was changed from “Update account overdue status” to [Update account collection status](https://developers.pismo.io/pismo-docs/reference/changeaccountcollectionstatus), and the endpoint description was updated to use the term “collection status” instead of “overdue status”.

#### Docs

Updated the last paragraph of the [Credit card cycles (billing periods)](https://developers.pismo.io/pismo-docs/docs/understanding-statements#credit-card-cycles-billing-periods) section to correct a couple of mistakes. The original version said that a new account is created with a moving window of 30 cycles. It’s actually created with a moving window of 42 cycles. It also said that the account would always have 30 future cycles. It actually always has one current cycle and 41 future cycles.

#### Docs

The `credit_transaction` field was removed from the sample 201 response of the [List payment agreements](https://developers.pismo.io/pismo-docs/reference/getinstallmentpayments) endpoint.

#### Docs

In the [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) endpoint, the `compulsory` and `split_iof` fields were added to the sample 201 response. The `installments` field was removed from the 201 response body and the sample 201 response.

#### Docs

The description of the **Stop accrual # of days** program parameter was updated in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) table to reference the specific endpoint that can be used to post the accruals.

#### Docs

Clarified the description of the `cycle` field, which is returned by the following endpoints.

* [Get minimum payout calculation memory](https://developers.pismo.io/pismo-docs/reference/getminimumpaymentcalculationmemory)
* [Get current statement](https://developers.pismo.io/pismo-docs/reference/getcurrentstatement)
* [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid)
* List statements v2
* [Save account interest rate](https://developers.pismo.io/pismo-docs/reference/saveaccounttransactioninterest)
* [Update statements calendar](https://developers.pismo.io/pismo-docs/reference/statementduedate)

#### Docs

Descriptions were updated for the following endpoints:

* [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid)
* List statements v2
* [List transaction balances](https://developers.pismo.io/pismo-docs/reference/gettransactionsbalance)

#### Docs

Descriptions were corrected for the following parameters:

* `gracePeriodDays` query parameter in [List program due dates](https://developers.pismo.io/pismo-docs/reference/getprogramduedates)
* `grace_period_days` body parameter in [Update program due date](https://developers.pismo.io/pismo-docs/reference/updateprogramduedate)

#### Docs

* Description for “Statement events messaging” was updated in [Cycle closing routine](https://developers.pismo.io/pismo-docs/docs/understanding-statements#cycle-closing-routine).
* The **Indicates whether the cycle opening event should be sent to the first cycle** program parameter was added to the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) table.
* Description was updated for the [Statement cycle opened](https://developers.pismo.io/events/docs/statements-cycle-opening-1) event.

#### Docs

Documentation was updated in the following sections:

* "Payment hierarchy" section of [How the program discharges transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-discharges-transactions)
* Last part of section [How a Full balance credit program manages credit accounts](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-a-full-balance-credit-program-manages-credit-accounts)

#### Docs

In the [Full balance credit program](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program) guide, replaced the term “written off” with the terms “paid in full” or “paid off”, which are more accurate.

#### Docs

In [Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview), the `collections_status` in the Account object was incorrectly documented. It needed to be  renamed `collection_status`, and the possible values were changed to `NORMAL` and `OVERDUE`.

#### Docs

The documentation was corrected to make the `beginDate` and `endDate` query parameters required in the following endpoints:

* [List account accruals v3](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv3)
* [Get interest accrual summary](https://developers.pismo.io/pismo-docs/reference/getinterestaccrualsummarization)

#### Docs

In the [Close delinquent account](https://developers.pismo.io/pismo-docs/reference/delinquent-ccount-closure-post) endpoint and the [Recurring charges](https://developers.pismo.io/pismo-docs/reference/create-recurring-charge-plan) API, the links to the events were updated to use the event names in the link text.

#### Docs

In the [Save account interest rate](https://developers.pismo.io/pismo-docs/reference/saveaccounttransactioninterest) endpoint, the description for the `overdue_rate_after_due_date_multiplier_percent` field was updated to clarify that the value entered should be a decimal value, not a percentage.

#### Docs

The description of the [Create program transaction type](https://developers.pismo.io/pismo-docs/reference/createprogramtransactiontype) endpoint was updated to clarify what kinds of transactions can be used to create program transaction types.

### Tokenization

#### Updated

The `migrated_tokens` field was removed from the [PAN updated](https://developers.pismo.io/events/docs/cards-tokenization-pan-update-1) event.

</summary>

<summary class="tabContent" id="Resources">

### Control Center

#### New

Pismo Control Center now has a Report log feature. When a Control Center request fails, Control Center displays a popup message. The message includes a session log with details about your current login session. There is also a **Copy report log** button that copies the error report details for use in creating a Service Desk request.

</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/accounts/{accountId}/average-balance` (`interest-bearing-calculate-average-balance`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--average-balance |
| `GET /v1/accounts/{accountId}/average-balance` (`interest-bearing-get-average-balance`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--average-balance |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/transactions` (`merchant-transaction-advancement`) | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/{advancementId}` (`merchants-advancements-data`) | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |
| `GET /v2/transactions` (`ListTransactions`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `GET /statements-v2/v3/accounts/{accountId}/statements` (`getByStatementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `PATCH /statements-v2/v1/programs/{programId}/due-dates/{programDueDateId}` (`updateProgramDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /acquisitions/v3/s2s/applications` (`post-acquisitions-v3-s2s-applications`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v2/s2s/access-token` (`post-passport-v2-s2s-access-token`) | `api-specs/Platform_authentication.yaml` | no | KU-API-platform-authentication--authentication |
| `PATCH /v1/accounts/{accountId}/limits` (`patch-v1-account-limit`) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `POST /v1/migrations/disputes` (`PostDisputeV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--dispute-migration |
| `POST /v1/migrations/on-us-authorizations` (`PostOnUsAuthorizationsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--on-us-authorization-migration |
| `POST /orgs-operation/v1/processing-codes` (`CreateProcessingCode`) | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /payment-methods/v1/authorization` (`post-authorization`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `GET /v1/config` (`get-config-by-tenant`) | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `GET /payment-methods-configs/v1/configs` (`get-config-by-tenant`) | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /programs/v1/programs/template` (`CreateProgramBasedOnTemplate`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v1/programs/{program_id}/parameters` (`createProgramParameter`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /programs/v1/programs/parameters/batch` (`setProgramsParameters`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /programs/v1/programs/{id}/parameters/batch` (`setProgramParameters`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `GET /v2/transactions/{transactionId}` (`GetTransactionById`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `GET /v2/transactions/total-items` (`SearchTranscationMetaDataCount`) | `api-specs/Core_platform_-_Transactions.yaml` | **yes** | KU-API-core-platform-transactions--transactions |
| `POST /v1/transaction-types` (`PostSetupTransactionType`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `POST /pix/v2/pix/out/scheduler` (`post-schedule-pix-payment`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `POST /v1/cards/transfer` (`post-funds-transfer`) | `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` | no | KU-API-instant-payments-rupay-on-upi--upi |
| `POST /v1/cards/list` (`post-list-cards`) | `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` | no | KU-API-instant-payments-rupay-on-upi--upi |
| `POST /v1/cards/validate` (`post-validate-card-data`) | `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` | no | KU-API-instant-payments-rupay-on-upi--upi |
| `POST /v1/interest/plan` (`post-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/multileg` (`corporate-v2-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/scheduled-payments` (`corporate-v2-post-scheduled-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `GET /corporate/v2/divisions` (`list-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v1/dormancy-config` (`list-dormancy-configs`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `POST /corporate/v2/divisions` (`post-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PATCH /corporate/v2/divisions/{divisionCode}` (`patch-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /corporate/v1/hierarchies` (`post-hierarchies`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /cards/v1/bulks/{bulkID}/cancel` (`cancel-bulk`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals/summarization` (`getInterestAccrualSummarization`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `PATCH /statements-v2/v1/accounts/{accountId}` (`ChangeAccountCollectionStatus`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account |
| `GET /statements/v4/accounts/{accountId}/installment-payments` (`GetInstallmentPayments`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `POST /statements/v4/accounts/{accountId}/installment-payments` (`InstallmentPaymentsv4`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /statements-v2/v1/accounts/{accountId}/statements/{statementId}/min-payment-memory` (`getMinimumPaymentCalculationMemory`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `GET /statements/v1/accounts/{accountId}/next` (`GetCurrentStatement`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` (`saveAccountTransactionInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `PATCH /statements-v2/v2/due-date` (`statementDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `GET /statements-v2/v1/accounts/{accountId}/transactions-balance` (`getTransactionsBalance`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `GET /statements-v2/v1/programs/{programId}/due-dates` (`getProgramDueDates`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals` (`getAccountAccrualsV3`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `POST /v1/recurring-charge-plans` (`create-recurring-charge-plan`) | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `POST /v1/programs/{programId}/program-transaction-types` (`createProgramTransactionType`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-transaction-types |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-org-rule-model-1` | Core platform - Rule models | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-adjustments-v1-adjustments` | Create adjustment (deprecated) | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `program-parameters-reference-table` | Program parameters; program parameters | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `delinquent-ccount-closure-post` | Close delinquent account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/4-april-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/4-april-2025 | `9e094fa042f17799…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--average-balance` — API reference: Banking - Interest-bearing accounts — Average balance
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balance-watcher--limit-configurations` — API reference: Core platform - Balance watcher — Limit configurations
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-core-platform-payment-configurations--payment-method-configurations` — API reference: Core platform - Payment configurations — Payment method configurations
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-instant-payments-rupay-on-upi--upi` — API reference: Instant payments - RuPay on UPI — UPI
- `KU-API-migrations--dispute-migration` — API reference: Migrations — Dispute migration
- `KU-API-migrations--on-us-authorization-migration` — API reference: Migrations — On-us authorization migration
- `KU-API-platform-authentication--authentication` — API reference: Platform authentication — Authentication
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-API-platform-setup-programs--parameters` — API reference: Platform setup - Programs — Parameters
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-configurations--program-transaction-types` — API reference: Revolving credit - Configurations — Program transaction types
- `KU-API-revolving-credit-recurring-charges--recurring-charge-plans` — API reference: Revolving credit - Recurring charges — Recurring charge plans
- `KU-API-revolving-credit-statements--account` — API reference: Revolving credit - Statements — Account
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-API-seller-management-merchant-advance--merchant-advancement` — API reference: Seller management - Merchant advancements — Merchant advancement
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
