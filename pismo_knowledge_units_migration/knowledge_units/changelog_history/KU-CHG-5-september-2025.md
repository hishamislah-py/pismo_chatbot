---
ku_id: KU-CHG-5-september-2025
title: 'Changelog: 5 September 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/5-september-2025.md
  sha256: 63cc8caf6c3126b3e4f6469e6ab7759b612e887c2b4d8c896f0648d7b932c5bd
  url: https://developers.pismo.io/pismo-docs/changelog/5-september-2025
  role: changelog_post
  updated_at: ''
operations:
- GetInstallmentPaymentByPaymentAgreementId
- GetInstallmentPayments
- InstallmentPaymentsv4
- PostAccountsV2
- PostCardsV1
- PostPciCardsV1
- cancelAccountTransactionCategory
- createAccrualTypePostConfig
- createStatementAmountDue
- deleteStatementAmountDue
- get-account-balance-history
- get-corporate-earmarks
- getAccountDischargeTracking
- getStatementAmountDue
- getTotalDue
- list-authorizations
- list-payment-orders
- list-recurrence-automatic
- patch-corporate-v2-earmarks-earmarkid
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-create-recurrence-cob
- post-overdraft-product
- post-v1-accounts-flex-controls
- postRevolvingStatementSummary
- saveAccountTransactionInterest
related_kus:
- KU-API-banking-overdraft--product
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-instant-payments-automatic-pix--automatic-pix-data
- KU-API-instant-payments-qr-code--recurring-payment
- KU-API-migrations--account-migration
- KU-API-migrations--card-migration
- KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--discharge-tracking
- KU-API-revolving-credit-statements--refinancing
- KU-API-revolving-credit-statements--statement
- KU-API-revolving-credit-statements--statement-minimum-amount-due
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 5 September 2025
coverage_window: 8 August and 5 September 2025
---

# Changelog: 5 September 2025

**KU ID:** `KU-CHG-5-september-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **5 September 2025** (changes between 8 August and 5 September 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

## Topics covered

Banking; Control Center - Balance configurations; Control Center - Dual approval; Client webhooks; Flexible transaction controls; Merchants; Transactions; Security; Setup; Events; Instant payments; Transaction banking; Authorization configurations; Card network integration; Disputes; Statements; Merchants; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/5-september-2025

<!-- source:begin path=changelog/5-september-2025.md part=0-end -->

# 5 September 2025

Changes between 8 August and 5 September 2025

<div class="customTab"></div>

<details>
  <summary class="tabContent" id="New features">

### Banking

#### New

The [Overdraft](https://developers.pismo.io/pismo-docs/reference/post-overdraft-product) API is now live. This API allows a bank to authorize a bank account for an allowable overdrawn limit to cover its debit transactions when the balance is insufficient.

The new [How overdraft works](https://developers.pismo.io/pismo-docs/docs/how-overdraft-works) guide explains this functionality.

### Control Center - Balance configurations

#### New

We’re pleased to offer you program-level balance configurations in Control Center. Balance configurations are a flexible set of rules that define how account balances and limits are impacted based on transaction activity. Use balance configurations to proactively manage risk, encourage responsible spending, and deliver personalized experiences to your customers. Refer to these new guides to learn more:

* [Balance configurations overview](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview)
* [Balance configurations in Control Center](https://developers.pismo.io/pismo-docs/docs/balance-configurations-in-control-center)
* [Balance configuration use cases](https://developers.pismo.io/pismo-docs/docs/balance-configuration-use-cases)

### Control Center - Dual approval

#### New

We’re excited to announce that dual approval is available in Control Center (beta release), adding a layer of oversight to critical processes. Dual approval is a security and governance feature that requires two separate individuals to review and approve a critical action or data change before it's finalized. One person initiates the request and a second person reviews and approves it. This process helps to prevent errors and unauthorized changes and reduce fraud.

Your company must opt-in to use dual approval. It's available for these Control Center processes:

* Edit a program parameter
* Make a single adjustment to an account

To learn more about dual approval, refer to [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval). To join the beta program, contact your Pismo representative.

</summary>
</details>

<details>
  <summary class="tabContent" id="Core platform">

### Client webhooks

#### Updated

The following changes were made to the request fields in the [Full balance anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook).

* A new field, `additional_data`, was added under the `validation_results` object. This optional field contains important additional information related to the validation.
* The unused field `id_last_referral_unlock_date` was removed.

#### Docs

The following updates were made to the request fields in the [Full balance anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook).

* An incorrect duplicate of the `cvv_data` field was removed.
* The `unlock_date` field is now correctly defined as a string.

The following update was made to the results fields in the [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook).

* The description for `available_credit_limit` was updated to indicate that the result is for either Balance limit for processing code 30 (balance inquiry) or for Voucher authorizations - account\_type 70.

### Flexible transaction controls

#### Updated

The description for the `week_day` attribute in the [flex controls](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) endpoints was updated to specify that this is a day of the week when the operation occurs and that the valid values use the full lowercase weekday name: `sunday`, `monday`, `tuesday`, `wednesday`, `thursday`, `friday`, `saturday`.

### Merchants

#### Docs

The descriptions of the following endpoints were updated to more accurately reflect the attributes and indicate which fields are required:

* [Migrate PCI Card](https://developers.pismo.io/pismo-docs/reference/postpcicardsv1)
* [Migrate cards](https://developers.pismo.io/pismo-docs/reference/postcardsv1)
* [Migrate accounts (v2)](https://developers.pismo.io/pismo-docs/reference/postaccountsv2)

### Transactions

#### Updated

The [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) and [Transaction updated](https://developers.pismo.io/events/docs/transaction-update-1) events now include the `created_at` field.

### Security

#### Docs

A note indicating the access token expiration time of 10 minutes was added to the [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials) guide for clarity.

#### Docs

A new security guide has been created for [Authentication with OAuth2](https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2). The Pismo platform supports OAuth2 authentication using stored credentials. This new guide explains how to obtain access tokens using the Client Credentials grant type.

#### Docs

Guidelines on how to request mTLS support for webhook requests were added in the [Verifying webhook requests](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests#request-mtls-support-for-webhook-requests) guide.

### Setup

#### Updated

The display name of the program parameter “Indicates whether the cycle opening event should be sent to the first cycle” was changed to “Send cycle opening event when first cycle is created” in both Control Center and the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide.

#### Docs

The \[beta] tag was removed from the balance configurations documentation. The new [Balance configurations data events](https://developers.pismo.io/pismo-docs/docs/balance-configurations-data-events) guide lists balance configurations data events.

#### Docs

The description of the "Accrual calculation strategy" program parameter was updated in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) and [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals) guides.

</summary>
</details>

<details>
  <summary class="tabContent" id="Data and reporting">

### Events

#### Updated

The unused field `anti_fraud_url` was removed from the [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event.

</summary>
</details>

<details>
  <summary class="tabContent" id="Core banking">

### Instant payments

#### Updated

There is a new field - `type` - returned in the Instant payments - Pix payments > Automatic Pix > [List payment orders](https://developers.pismo.io/pismo-docs/reference/list-payment-orders) endpoint response. This is the payment order’s type as a translation of the type coming from Brazil’s Instant Payments System (SPI).

#### Updated

* The `perPage` parameter is no longer required for Instant payments - Pix payments > Automatic Pix > [List recurrences](https://developers.pismo.io/pismo-docs/reference/list-recurrence-automatic).
* The `status` and `perPage` parameters are no longer required for Instant-payments > Pix payments > Automatic Pix > [List recurrence authorizations](https://developers.pismo.io/pismo-docs/reference/list-authorizations).
* The `recurrenceId` and `perPage` parameters are no longer required for Instant payments - Pix payments > Automatic Pix > [List payment orders](https://developers.pismo.io/pismo-docs/reference/list-payment-orders).

#### Updated

For the Instant payments - QR Code > [Recurring payment](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence-cob) endpoints, the `retry` boolean field in the recurrence object has been renamed to `allow_attempts_after_expiration`. Its functionality, indicating whether to allow transaction retries after failure, remains the same.

### Transaction banking

#### Updated

A new validation error message: `WEAM0040: The payment date cannot be earlier than the account creation date` was added to the following endpoints. This validation error occurs when you specify an earmark payment date that is earlier than the account creation date.

* [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
* [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
* [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)

#### Updated

Three new fields are now available in the [Get account balance history](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history) endpoint. The purpose of these fields is to enable accurate interest accrual on accounts with positive balances, the balance history logic is updated to track daily net changes in balance.

* `credit_movement`: Represents the total of all credits processed during the business day. Always expressed as a positive value.
* `debit_movement`: Represents the total of all debits processed during the business day. Always expressed as a positive value.
* `net_movement`: Is the change in an account’s balance between two consecutive business dates.

#### Updated

The following new query parameters are now available the [List earmarks](https://developers.pismo.io/pismo-docs/reference/get-corporate-earmarks) endpoint. These parameters allow you to query earmarks whose balances are greater than, less than, or equal to the specified amount.

* `balanceGt`: Filters earmarks whose balance exceeds the specified amount.
* `balanceGe`: Filters earmarks with a balance greater than the specified amount.
* `balanceLt`: Filters earmarks with a balance less than the specified amount.
* `balanceLe`: Filters earmarks with a balance less than or equal to the specified amount.

</summary>
</details>

<details>
  <summary class="tabContent" id="Card issuing">

### Authorization configurations

#### Updated

The `use_anti_fraud_api` field was removed from the Authorization configurations API because it is no longer necessary to send this field. The parameter list in the [Authorization configurations](https://developers.pismo.io/pismo-docs/docs/authorization-configurations-1) guide was updated and the field was replaced with `disable_dcc` in the code samples in the [Run the configuration requests](https://developers.pismo.io/pismo-docs/docs/run-the-configuration-requests) guide.

#### Docs

The following updates were made to the [Authorization configurations](https://developers.pismo.io/pismo-docs/docs/authorization-configurations-1) guide:

* The `bypass_card_status_canceled` field was removed from the parameter list because it was a temporary field that was unused.
* The four previously undocumented fields were added to the parameter list: `days_to_cancel_pre_authorization`, `days_to_cancel_pre_authorization_migration`, `days_to_cancel_authorization_migration`, and `always_call_ledger_rules`.

### Card network integration

#### Updated

A new custom code, 91 - Authorization system or issuer system inoperative, was added to the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) guide. Validation code 91 is returned when the authorizations or route is not available, such as when the issuer host is unavailable, unexpected disconnection, or any unforeseen/platform-mapped error. The new validation code was also added to the [Validation code definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions) guide.

#### Docs

The new [Card network mandates](https://developers.pismo.io/pismo-docs/docs/card-network-mandates) guide is now available. Card network mandates are rules, requirements, and deadlines that govern how banks, merchants, processors, and service providers must operate in their payment ecosystems. This guide provides a general overview about these mandates with a FAQ about how they are handled on the Pismo platform.

### Disputes

#### Updated

The [Card issuing - Disputes > ELO](https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed) section has been removed. It contained 3 endpoints: Create authorization fraud report, List authorization fraud reports, and Count authorization fraud reports.

### Statements

#### New

The following new endpoints are now available.

* [Get account total due](https://developers.pismo.io/pismo-docs/reference/gettotaldue)
* [Create or update statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/createstatementamountdue)
* [Get statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/getstatementamountdue)
* [Disable statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/deletestatementamountdue)
* [Register revolving statement summary generation process](https://developers.pismo.io/pismo-docs/reference/postrevolvingstatementsummary)

#### Docs

Two values in two of the tables in [Delinquency buckets](https://developers.pismo.io/pismo-docs/docs/delinquency-buckets) were corrected. $54.97 was changed to $54.96. 2, and $113.99 was changed to $113.98.

#### Docs

The `transaction_category_id` body parameter was marked as required in the [Configure account transaction category rates](https://developers.pismo.io/pismo-docs/reference/saveaccounttransactioninterest) endpoint documentation. It was already a required parameter—the documentation was updated to reflect that.

#### Docs

The description for the [Cancel account transaction category](https://developers.pismo.io/pismo-docs/reference/cancelaccounttransactioncategory) endpoint was updated to clarify what happens to the rates when an account transaction category is canceled.

#### Docs

Many details in the [Minimum amount due calculation](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation) guide were clarified.

#### Docs

The description of the body parameter `reversal_projection_processing_code` in the [Create an accrual type post configuration](https://developers.pismo.io/pismo-docs/reference/createaccrualtypepostconfig) endpoint was updated to clarify when it’s used.

#### Docs

The description of the `split_iof body` parameter of the [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) endpoint was updated.

#### Docs

The “Transaction categories” section of [How the program uses configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-uses-configurable-entities) was updated.

#### Docs

The last sentence in [Transaction categories](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters#transaction-categories) was changed to link to a different guide.

#### Docs

The definition of “account transaction category” in [Transaction category structure](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#transaction-category-structure) was modified.

#### Docs

The description of `open_due_date` in [Account](https://developers.pismo.io/pismo-docs/docs/setup-overview#account) was updated to clarify how it differs from the statement due date.

#### Docs

The description of the `type` field in the table in the [Accounts balances report files](https://developers.pismo.io/pismo-docs/docs/accounts-balances-report-files) guide was updated and definitions for the possible values were added.

#### Docs

The description of the `payment_datetime` field was updated in the following endpoints:

* [List discharges](https://developers.pismo.io/pismo-docs/reference/getaccountdischargetracking) (returned in items objects of 200 response)
* [List payment agreements](https://developers.pismo.io/pismo-docs/reference/getinstallmentpayments) (returned in items objects of 200 response)
* [Get payment agreement](https://developers.pismo.io/pismo-docs/reference/getinstallmentpaymentbypaymentagreementid) (returned in 200 response)
* [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) (body parameter)

</summary>
</details>

<details>
  <summary class="tabContent" id="Seller management">

### Merchants

#### Docs

The [Managing merchant transactions](https://developers.pismo.io/pismo-docs/docs/managing-merchant-transactions) guide is now available. This guide describes how to create, cancel, retrieve transactions for a single merchant, and how to split transactions across multiple merchants.

</summary>
</details>

<details>
  <summary class="tabContent" id="Resources">

### Control Center

#### Docs

The [Get started with Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) was updated to include directions for users logging in with single-sign on. Also, troubleshooting guidance was added for users who don’t get the login emails.

#### Docs

The new section [Resend login emails](https://developers.pismo.io/pismo-docs/docs/add-a-user#resend-login-emails) was added to the Create and edit users guide.

</summary>
</details>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/overdraft` (`post-overdraft-product`) | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--product |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/migrations/cards-pci` (`PostPciCardsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /v1/migrations/cards` (`PostCardsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /v2/migrations/accounts` (`PostAccountsV2`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--account-migration |
| `GET /inst-pull-pay/v1/pix/automatic/payment/order` (`list-payment-orders`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix-data |
| `GET /inst-pull-pay/v1/pix/automatic` (`list-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix-data |
| `GET /inst-pull-pay/v1/pix/automatic/authorizations` (`list-authorizations`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix-data |
| `POST /v1/pix/qrcode/cob/recurrence` (`post-create-recurrence-cob`) | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `GET /bank-statements/v1/account-balances/{externalAccountId}/history` (`get-account-balance-history`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /corporate/v1/earmarks` (`get-corporate-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `GET /statements-v2/v2/accounts/{accountId}/total-due` (`getTotalDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due` (`createStatementAmountDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |
| `GET /statements-v2/v1/accounts/{accountId}/minimum-amount-due` (`getStatementAmountDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |
| `DELETE /statements-v2/v1/accounts/{accountId}/minimum-amount-due` (`deleteStatementAmountDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |
| `POST /statements-v2/v1/accounts/{accountId}/revolving-statement-summary` (`postRevolvingStatementSummary`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` (`saveAccountTransactionInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `DELETE /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId}` (`cancelAccountTransactionCategory`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `POST /v1/programs/{programId}/accrual-type-post-config` (`createAccrualTypePostConfig`) | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations |
| `POST /statements/v4/accounts/{accountId}/installment-payments` (`InstallmentPaymentsv4`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /statements-v2/v1/accounts/{accountId}/discharges-tracking` (`getAccountDischargeTracking`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--discharge-tracking |
| `GET /statements/v4/accounts/{accountId}/installment-payments` (`GetInstallmentPayments`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /statements/v4/accounts/{accountId}/installment-payments/{id}` (`GetInstallmentPaymentByPaymentAgreementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/5-september-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/5-september-2025 | `63cc8caf6c3126b3…` | not stated |

## Related knowledge units

- `KU-API-banking-overdraft--product` — API reference: Banking - Overdraft — Product
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-instant-payments-automatic-pix--automatic-pix-data` — API reference: Instant payments - Automatic Pix — Automatic Pix data
- `KU-API-instant-payments-qr-code--recurring-payment` — API reference: Instant payments - QR Code — Recurring payment
- `KU-API-migrations--account-migration` — API reference: Migrations — Account migration
- `KU-API-migrations--card-migration` — API reference: Migrations — Card migration
- `KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations` — API reference: Revolving credit - Interest accruals — Accrual type post configurations
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--discharge-tracking` — API reference: Revolving credit - Statements — Discharge tracking
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-API-revolving-credit-statements--statement-minimum-amount-due` — API reference: Revolving credit - Statements — Statement minimum amount due
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
