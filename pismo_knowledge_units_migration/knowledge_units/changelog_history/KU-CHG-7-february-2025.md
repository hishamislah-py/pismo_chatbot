---
ku_id: KU-CHG-7-february-2025
title: 'Changelog: 7 February 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/7-february-2025.md
  sha256: df76f47af644caa35e14e1b345fa66ccd702434bb9374a6bcbd43b44eefb2fbe
  url: https://developers.pismo.io/pismo-docs/changelog/7-february-2025
  role: changelog_post
  updated_at: ''
operations:
- CreateProgramBasedOnTemplate
- GetBucketsByAccount
- GetCurrentStatement
- GetTransactionById
- PostAccountsV2
- PostFeeModelV1
- PostMigrationProgram
- PostSetupTransactionType
- PostTransactionsV1
- cancel-pix-out-execution
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- customerV1patch
- customerV2Post
- get-pix-transaction
- getAccountsTransactionsInterest
- patch-dormancy-config-v2
- patch-v1-customers-flex-control
- post-acquisitions-v3-s2s-applications
- post-payments-v1-hold-funds-block
- post-payments-v1-installments
- post-pre-schedules
- post_v1-authorizations
- put-back-business-toggle
- put-v1-holiday
- saveProgramDueDate
- v1-search-business-day
- validate-v1-holiday
related_kus:
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-card-issuing-authorization--authorizations
- KU-API-core-platform-accounting--buckets
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--customers
- KU-API-core-platform-accounts--transfer-account
- KU-API-core-platform-flex-controls--customer-flex-controls-part-01
- KU-API-core-platform-flex-controls--customer-flex-controls-part-02
- KU-API-core-platform-payment-methods--hold-funds
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-payment-scheduler-beta--schedules
- KU-API-core-platform-transactions--transaction-types
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--pix-part-02
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-migrations--account-migration
- KU-API-migrations--fee-model-migration
- KU-API-migrations--transaction-migration
- KU-API-platform-setup-holidays--holidays-deprecated
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-statements--accruals
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--statement
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 7 February 2025
coverage_window: 3 January and 7 February 2025
---

# Changelog: 7 February 2025

**KU ID:** `KU-CHG-7-february-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **7 February 2025** (changes between 3 January and 7 February 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

## Topics covered

Accounting; Accounts; Client webhooks; Flexible transaction controls; Migrations; Payments; Security; Setup; Support; Transactions; Events; Banking as a Service; Instant payments; Transaction banking; Authorization; Card network integration; Embossing; Network transactions; Statements; Pismo Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/7-february-2025

<!-- source:begin path=changelog/7-february-2025.md part=0-end -->

# 7 February 2025

Changes between 3 January and 7 February 2025

<div class="customTab"></div>

<details>
  <summary class="tabContent" id="Core platform">

### Accounting

#### Updated

The new [Get account buckets](https://developers.pismo.io/pismo-docs/reference/getbucketsbyaccount) endpoint is now available.

### Accounts

#### Docs

In the [Transfer account to different program](https://developers.pismo.io/pismo-docs/reference/postmigrationprogram) endpoint, introduction was updated to clarify that the account keeps the flex controls of the original program.

#### Docs

In the [Account status](https://developers.pismo.io/pismo-docs/docs/accounts-overview#account-status) guide, instructions about rolling back an account status were streamlined.

#### Docs

The date format of the `birth_date` field was corrected in the following endpoints.

* [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications)
* [Create customer](https://developers.pismo.io/pismo-docs/reference/customerv2post)
* [Update customer information](https://developers.pismo.io/pismo-docs/reference/customerv1patch)

#### Docs

The [Accounts](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) API reference documentation was updated for standards such as updated event names.

#### Docs

In the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint, the descriptions for `account`, `personal`, and `company` were updated to correctly represent the entity’s external ID.

### Client webhooks

#### Updated

The following changes were made in the anti-fraud payload for full balance clients only.

* The two new required request fields `card_mode_type` and `pin_validated` were added.
* The options list for request field `card_status` was updated to include more options.
* The new optional response field `merchant_denial_code` was added.

The new request and response fields are defined in the [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook) guide.

### Flexible transaction controls

#### Docs

In the [Update customer flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-customers-flex-control) endpoint, documentation was updated to note that the `current_spend_limit` field is internal.

#### Docs

The [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls) guide was updated for clarity.

### Migrations

#### New

The new [Migrate accounts (v2)](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint is now available. It relocates the address and phone fields to outside the applicant.personal object. The [Migrate accounts (v1)](https://developers.pismo.io/pismo-docs/reference/postaccountsv1) endpoint remains available to support existing implementations.

#### New

The new [Fee model migration](https://developers.pismo.io/pismo-docs/reference/postfeemodelv1) endpoint is now available. This endpoint generates two new events: [Fee model account migration started](https://developers.pismo.io/events/docs/migration-fee-model-account-incoming-1) and [Fee Model account migration completed]().

#### Updated

The [Authorization migration completed](https://developers.pismo.io/events/docs/migration-authorization-outgoing-1) event was updated to include a number of missing fields.

#### Updated

The [Migrate transaction](https://developers.pismo.io/pismo-docs/reference/posttransactionsv1) endpoint was updated to add the field `instant_payment_data.internal_transaction`. This is a boolean that, if true, means the credit and debit transactions for an instant payment both happened within the same organization.

### Payments

#### Updated

In the [Block amount](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-hold-funds-block) endpoint, the new `skip_status_account_validation` field is now available.

#### Updated

In the [Create pre-schedule \[beta\]](ref:post-pre-schedules) endpoint, the error 409 was replaced with error 200.

#### Docs

In the [Create installments payment](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-installments) endpoint,  the pattern for `first_installment_date` was added to the field’s description.

### Security

#### Docs

The [Generate your JSON Web Token (JWT)](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid#generate-your-jwt) section of the Authentication with OpenID guide was updated to indicate where users can find the list of valid groups. A reference and link to the View API permission groups was also added for clarification.

#### Docs

The [Identity connectivity with mTLS](https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls) guide was updated to include a list of details that need to be provided to Pismo before mTLS can be issued.

#### Docs

Due to Postman warning issues, token examples were removed from the [Get OpenID access token](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token-1) endpoint documentation.

### Setup

#### Docs

The new [Program types](https://developers.pismo.io/pismo-docs/docs/program-types)  guide is now available.

#### Docs

In the [Programs](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) API reference documentation, the explanation of `due_dates` was improved to explain that this is an array defined in the program configuration. The accounts in the program specify the ID of which available due date to use.

#### Docs

The Holidays API reference documentation was rewritten and updated for clarity. The following endpoints were renamed to better reflect their functionality.

* Validate holiday > [Get holiday](https://developers.pismo.io/pismo-docs/reference/validate-v1-holiday)
* Search for business day > [Check if business day](https://developers.pismo.io/pismo-docs/reference/v1-search-business-day)
* Update holiday > [Update holiday name](https://developers.pismo.io/pismo-docs/reference/put-v1-holiday)

### Support

The [Pismo operations status](https://developers.pismo.io/pismo-docs/docs/pismo-operations-status) guide was updated. Customers now must request access to the Operations Status page from their Pismo representative.

### Transactions

#### New

To meet ISO 4217 standards, every instance of the `currency` field description was updated and new `currency` field was added to the `tax` object in the [Transactions](https://developers.pismo.io/pismo-docs/reference/gettransactionbyid) API.

#### Docs

The [Create transaction type](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) endpoint documentation now links to [Standard processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types#standard-processing-codes).

  </summary>
</details>

<details>
  <summary class="tabContent" id="Data and reporting">

### Events

#### Docs

In the [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) event, the fields `currency_code` and `currency_numeric_code`  were added.

#### Docs

The Interest plan creation succeeded event is now [Interest plan created](https://developers.pismo.io/events/docs/interest-management-interest-plan-creation-success-1).

#### Docs

The [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) event and the links in [Core platform - Transactions](https://developers.pismo.io/pismo-docs/docs/transactions-data-events) were standardized.

  </summary>
</details>

<details>
  <summary class="tabContent" id="Core banking">

### Banking as a Service

#### Docs

A legal disclaimer was added to both the [Banking as a Service (BaaS)](https://developers.pismo.io/pismo-docs/docs/banking-overview#banking-as-a-service-baas) section in the Banking overview and the [Banking as a Service](https://developers.pismo.io/pismo-docs/docs/banking-as-a-service) guide. This disclaimer clarifies that Pismo only provides the technology and collaborates with partners to provide BaaS services to customers.

### Instant payments

#### New

The following new endpoints are now available in the Pix payments API.

* [Cancel Pix-out scheduled execution](https://developers.pismo.io/pismo-docs/reference/cancel-pix-out-execution)
* [Get transaction from provider](https://developers.pismo.io/pismo-docs/reference/get-pix-transaction) can be used to verify that both provider and Pismo have the same information.

### Transaction banking

#### Updated

In the [Update dormancy configuration](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2) endpoint, the path parameter `externalAccountId` was changed to `dormancyConfigId`.

#### Updated

In the [Post payment ](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint, the following changes were made.

* New 400 error codes were added:
  * `WPMT0044: Back business dating is disabled.` This error occurs when the back business payment feature is disabled through the [Past business date toggle](https://developers.pismo.io/pismo-docs/reference/put-back-business-toggle) endpoint.
  * `WPMT0051: Operation not allowed by reason: <reason>.` This error indicates the post payment is not allowed by the status reason provided.
* The status reasons for `force_post` in the request and response payloads were updated. Previously, the status reasons in the request and response bodies were:
  * `CREDIT ONLY` — No force debit allowed
  * `DEBIT ONLY `— No force credit allowed
  * `ANY` — No force allowed
  * `MANUAL` — No force allowed
* The new status reasons are:
  * `ALL_NO_FORCE_ALLOWED`
  * `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`
  * `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`
  * `FORCE_DEBIT_ONLY`
  * `FORCE_CREDIT_ONLY`
  * `NONE_NO_FORCE_ALLOWED`

#### Updated

In the [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments) endpoint, the following changes were made.

* New 400 errors were added:
  * `WMLP0005: Validation error: one or more legs did not pass validation.` This error is related to back business dating.
  * `WMLP1037: Debit not allowed by reason - <reason>.` This error occurs when the debit transaction is not allowed by the status reason clients provided.
  * `WMLP1038: Credit not allowed by reason - <reason>.` This error occurs when the credit transaction is not allowed by the status reason clients provided.
* The status reasons for force\_post for the debit object in the request and response payloads were updated. Previously, the status reasons in the request and response bodies were:
  * `CREDIT ONLY` — No force debit allowed
  * `DEBIT ONLY` — No force credit allowed
  * `ANY` — No force allowed
  * `MANUAL` — No force allowed
* The new status reasons are:
  * `ALL_NO_FORCE_ALLOWED`
  * `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`
  * `FORCE_CREDIT_ONLY`
  * `NONE_NO_FORCE_ALLOWED`
* For `force_post` in the `credit` object, the status reasons used to be:
  * `CREDIT ONLY` — No force debit allowed
  * `DEBIT ONLY` — No force credit allowed
  * `ANY` — No force allowed
  * `MANUAL` — No force allowed
* Now they are:
  * `ALL_NO_FORCE_ALLOWED`
  * `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`
  * `FORCE_DEBIT_ONLY`
  * `NONE_NO_FORCE_ALLOWED`

#### Docs

The following guides are now available.

* [Business-dated transactions](https://developers.pismo.io/pismo-docs/docs/biz-dated-txns)
* [Back-business-dated transactions](https://developers.pismo.io/pismo-docs/docs/back-biz-dated-txns)
* [Future-business-dated transactions](https://developers.pismo.io/pismo-docs/docs/future-biz-dated-txns)

#### Docs

The [Bulk file-based payment processing](https://developers.pismo.io/pismo-docs/docs/bulk-file-based-payment-processing#common-error-messages) guide now includes a table of common error messages output by the response file.

  </summary>
</details>

<details>
  <summary class="tabContent" id="Card issuing">

### Authorization

#### Updated

The [Authorization configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant-1) API was updated to include DELETE endpoints.

#### Docs

Two new guides are available for working with the Authorization configurations API. The new guide [Authorization configurations](https://developers.pismo.io/pismo-docs/docs/authorization-configurations-1) gives details on the required parameters for Full balance and Zero balance. The new guide [Run the configuration requests](https://developers.pismo.io/pismo-docs/docs/run-the-configuration-requests) provides sample code and examples of how to use the various API requests.

#### Docs

Field descriptions in the [Authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) API reference documentation were updated for clarity and completeness and to include default values for all boolean fields.

#### Docs

The [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint was updated to properly indicate all required parameter fields.

#### Docs

The API reference guide for Card issuing - Authorizations (network-transactions-api) was updated to include default values for all Boolean fields and to include revised descriptions for clarity.

### Card network integration

#### Updated

The custom authorization validation code for `UBN` (NFC disabled) was changed from `57` to `78` for Visa and from `FM` to `78` for ELO. This change, and all validation codes, can be found in the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events#authorization-validations) guide.

#### Docs

The [Simulate authorizations](https://developers.pismo.io/pismo-docs/docs/simulate-authorizations) guide was updated to include a note for considerations when using processing codes.

#### Docs

Definitions for custom validation codes `BII` (Balance inquiry internal error), `IZA` (Zero amount not allowed), and `ZBD` (Zero balance client declined) were added to the [Validation codes definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions) guide.

#### Docs

Custom validation codes for ELO were added to all validation tables in the Rule list guide. In addition, corrections were made to the following codes in the [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list) guide to ensure accuracy: `988` (Visa), `BNW` (Visa), `FRE` (RuPay), `FRN` (Visa), `LAE` (Visa), `OP1` (Visa), `PCE` (Visa), `TSM` (TecBan), and `UBT` (Visa and Mastercard).

#### Docs

The authorization validation rules Account number inquiry (`ANI`) and Address verification service (`AVS`) were added to the [Authorization validation rules for card network operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations) guide and to the [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list#account-number-inquiry-ani) guide.

### Embossing

#### New

Customers who work with ondemand embossing can now emboss cards with NORMAL, BLOCKED, PENDING, WARNING status, in addition to CREATED.

### Network transactions

#### Docs

The description for the  `cvv_present` field in the [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event was updated for clarification to specify that the field is looking at the CVV2 code. This change clarifies that the boolean flag only considers CVV2 validation. To validate the presence of CVV1 using this endpoint, consider using the `track1_present` and `track2_present` attributes.

### Statements

#### Docs

The following new guides are now available.

* [Calendars and holidays in credit card accounts](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-credit-card-accounts)
* [Create an installment agreement](https://developers.pismo.io/pismo-docs/docs/create-an-installment-agreement)
* [Configuring a sellos tax](https://developers.pismo.io/pismo-docs/docs/configuring-a-sellos-tax) explains the sellos tax. While the sellos tax itself is not a new feature, the capability of setting a minimum amount for it is new. How to do this is explained in the guide.

#### Docs

The description of the [Save program due date](https://developers.pismo.io/pismo-docs/reference/saveprogramduedate) endpoint was updated to clarify its behavior.

#### Docs

Made various changes to the [Statements](https://developers.pismo.io/pismo-docs/reference/getcurrentstatement) API to bring it up to Pismo standards, such as specifying the default values for parameters and clarifying parameter descriptions. Updated some endpoint descriptions. Moved endpoints dealing with transaction categories into their own section called “Transaction categories”. Similarly, moved endpoints for transaction types into “Transaction types”.

#### Docs

In the [Create a statement agreement](https://developers.pismo.io/pismo-docs/docs/create-a-statement-agreement#create-a-new-statement-agreement) guide, items 6 and 7 were added to the numbered bullet point list.

#### Docs

In the [Update interest accrual statuses](https://developers.pismo.io/pismo-docs/reference/getaccountstransactionsinterest) endpoint, `SETTLED`  was added to the list of possible values for the `new_status` field, which is a property of the objects in the accruals array in the body of the request.

#### Docs

A diagram was added to the [Calendars and holidays in credit card accounts](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-credit-card-accounts) guide and the paragraph above the diagram was updated to refer to it.

#### Docs

In the [Minimum amount due calculation](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation) guide, corrected `Over-limit amount` in **Strategy 2 examples > Second example > Cycle 3 statement**. It used to be $322.50. The correct value is $304.50.

  </summary>
</details>

<details>
  <summary class="tabContent" id="Resources">

### Pismo Control Center

#### Docs

In Control Center, the program creation flow was redesigned to provide better user experience.

#### Updated

Notification emails from Pismo now come from the domains **@notify.pismo.io** and **@notify.pismolabs.io**. Please take any necessary steps to ensure proper email receipt.

  </summary>
</details>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `GET /v1/buckets` (`GetBucketsByAccount`) | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--buckets |
| `POST /accounts/v1/accounts/programs/migration` (`PostMigrationProgram`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--transfer-account |
| `POST /acquisitions/v3/s2s/applications` (`post-acquisitions-v3-s2s-applications`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /accounts/v2/customers` (`customerV2Post`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail` (`customerV1patch`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `PATCH /v1/customers/{customerId}/flex-controls/{flexControlId}` (`patch-v1-customers-flex-control`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-01, KU-API-core-platform-flex-controls--customer-flex-controls-part-02 |
| `POST /v2/migrations/accounts` (`PostAccountsV2`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--account-migration |
| `POST /v1/migrations/fee-model-account` (`PostFeeModelV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--fee-model-migration |
| `POST /v1/migrations/transactions` (`PostTransactionsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--transaction-migration |
| `POST /payments/v1/payments/hold-funds/block` (`post-payments-v1-hold-funds-block`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--hold-funds |
| `POST /v1/pre-schedules` (`post-pre-schedules`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /payments/v1/payments/installments` (`post-payments-v1-installments`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--installments-payments |
| `POST /programs/v1/programs/template` (`CreateProgramBasedOnTemplate`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /holidays-core/v1/holiday/validate` (`validate-v1-holiday`) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-deprecated |
| `POST /holidays-core/v1/search-business-day` (`v1-search-business-day`) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-deprecated |
| `PUT /holidays-core/v1/holiday/{holiday_id}` (`put-v1-holiday`) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-deprecated |
| `GET /v2/transactions/{transactionId}` (`GetTransactionById`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `POST /v1/transaction-types` (`PostSetupTransactionType`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `DELETE /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}` (`cancel-pix-out-execution`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `GET /pix/v1/pix/provider/transaction/type/{type}/end-to-end/{end_to_end_id}` (`get-pix-transaction`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01, KU-API-instant-payments-pix-payments--pix-part-02 |
| `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` (`patch-dormancy-config-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `PUT /corporate/v1/feature/back-business/toggle` (`put-back-business-toggle`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/multileg` (`corporate-v2-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /networktransactions/v1/authorizations` (`post_v1-authorizations`) | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `POST /statements-v2/v1/programs/{programId}/due-dates` (`saveProgramDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `GET /statements/v1/accounts/{accountId}/next` (`GetCurrentStatement`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals` (`getAccountsTransactionsInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `postaccountsv1` | Migrate accounts (v1); Migrations API | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-passport-v1-oauth2-token-1` | Get OpenID access token; Passport API endpoint | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-config-by-tenant-1` | Authorization configurations; Balance watcher; Create configuration by org; Limit configurations | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/7-february-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/7-february-2025 | `df76f47af644caa3…` | not stated |

## Related knowledge units

- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-core-platform-accounting--buckets` — API reference: Core platform - Accounting — Buckets
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-core-platform-accounts--transfer-account` — API reference: Core platform - Accounts — Transfer account
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-01` — API reference: Core platform - Flex controls — Customer flex controls (part 1 of 2)
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-02` — API reference: Core platform - Flex controls — Customer flex controls (part 2 of 2)
- `KU-API-core-platform-payment-methods--hold-funds` — API reference: Core platform - Payment methods — Hold funds
- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-payment-scheduler-beta--schedules` — API reference: Core platform - Payment scheduler — Schedules
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-02` — API reference: Instant payments - Pix payments — Pix (part 2 of 2)
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-migrations--account-migration` — API reference: Migrations — Account migration
- `KU-API-migrations--fee-model-migration` — API reference: Migrations — Fee model migration
- `KU-API-migrations--transaction-migration` — API reference: Migrations — Transaction migration
- `KU-API-platform-setup-holidays--holidays-deprecated` — API reference: Platform setup - Holidays — Holidays (deprecated)
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
