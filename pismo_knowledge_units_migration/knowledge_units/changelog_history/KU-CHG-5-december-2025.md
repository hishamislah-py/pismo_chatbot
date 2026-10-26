---
ku_id: KU-CHG-5-december-2025
title: 'Changelog: 5 December 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/5-december-2025.md
  sha256: 1c9177d03f1cf4f2875f2d7e96cdc9a6ec6a7c6adf13951a130fad67e539baa8
  url: https://developers.pismo.io/pismo-docs/changelog/5-december-2025
  role: changelog_post
  updated_at: ''
operations:
- CreateProgramCalendarStrategy
- PostOnUsAuthorizationsV1
- cancelAccountTransactionCategory
- createAccrualTypePostConfig
- deleteAccountAccrualTypesRate
- deleteAccrualTypesRates
- get-account-balance-history
- get-account-balances
- get-v1-cards
- get-v1-cards-by-account
- getDormancyConfig
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-create-savings-account-product
- interest-bearing-v1-list-products
- interest-bearing-v1-savings-account-attach-account
- interest-bearing-v1-savings-account-attach-program
- listProgramAccrualTypesRates
- patch-dormancy-config-v2
- patch-v1-interest-plan
- patch-v2-card
- post-accounts-accountId-close
- post-corporate-v1-restricted-funds
- post-create-funds-recovery
- post-dormancy-config-v2
- post-intl-bank-accounts-v1-bank-accounts-beneficiaries
- post-v1-cards-card-id-network-tokens-profile
- postAccountAccrualTypesRates
- postAccrualTypesRates
- post_v1-authorizations
- put-v1-card-status
- updateProgramDueDate
related_kus:
- KU-API-banking-bank-accounts--beneficiaries
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-bearing-accounts--program-attachment
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-card-issuing-authorization--authorizations
- KU-API-card-issuing-cards--card-status
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-tokenization--network-card-profile
- KU-API-instant-payments-pix-management--funds-recovery
- KU-API-migrations--on-us-authorization-migration
- KU-API-revolving-credit-calendar-management--program-calendar-strategies
- KU-API-revolving-credit-configurations--account-accrual-rates
- KU-API-revolving-credit-configurations--program-accrual-rates
- KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--due-date
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 5 December 2025
coverage_window: 7 November and 5 December 2025
---

# Changelog: 5 December 2025

**KU ID:** `KU-CHG-5-december-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **5 December 2025** (changes between 7 November and 5 December 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated"; "Deprecated".

## Topics covered

Control Center - Access keys; Core banking; Core banking - Instant payments; Core platform - Security; Migrations; Payments; Reports; Banking operations; Transaction banking; Cards; Card network integration; Statements; Tokenization; Marketplace; Control Center; Postman

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/5-december-2025

<!-- source:begin path=changelog/5-december-2025.md part=0-end -->

# 5 December 2025

Changes between 7 November and 5 December 2025

<div class="customTab"></div>

<summary class="tabContent" id="New features">

### Control Center - Access keys

#### New

In addition to creating [access keys](https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication), you can now deactivate them in Control Center. You must be cautious when deactivating keys—it is a permanent action that cannot be reversed and you must create a new key if it is needed again.

### Core banking

#### Docs

The [Get started with core banking](https://developers.pismo.io/pismo-docs/docs/get-started-with-core-banking) guide is now available to assist you with initial core banking setup.

### Core banking - Instant payments

#### New

A new funds recovery process now exists for Pix instant payments. This includes new Pix [endpoints](https://developers.pismo.io/pismo-docs/reference/post-create-funds-recovery), new events—[Pix funds recovery status changed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-status-change-1) and [Pix funds recovery operation failed](https://developers.pismo.io/events/docs/pix-dict-funds-recoveries-operation-failed-1)—and a new [Pix funds recovery](https://developers.pismo.io/pismo-docs/docs/pix-funds-recovery) guide. For its initial launch, this process is in beta release.

### Core platform - Security

#### Docs

The new [Security guide for APIs](https://developers.pismo.io/pismo-docs/docs/security-guide-for-apis) is now available. This guide offers a high-level understanding of the security Pismo provides in regard to our APIs. This includes topics such as API access control, encryption management, security incident management, security certifications and compliance, and more. The guide also gives you an introduction to the Pismo security teams.

</summary>

<summary class="tabContent" id="Core platform">

### Migrations

#### Docs

The [Migrate on-us authorizations](https://developers.pismo.io/pismo-docs/reference/postonusauthorizationsv1) endpoint descriptions were updated to provide more detailed information, accurate data types, and information about maximum length.

### Payments

#### Deprecated

The deprecated Adjustments API was removed from Pismo's public documentation and added to the list of [API endpoints removed](https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed).

#### Updated

The tables in [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations) were updated for readability and with the following changes.

In [Original authorization retrieval](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations#original-authorization-retrieval), the response code for `ORIGINAL_AUTHORIZATION_ERROR` was changed to `96`. Also, the denial code was changed to `POA` and response code was changed to `57` for the following reasons:

* `ORIGINAL_AUTHORIZATION_IS_NOT_PENDING`
* `ORIGINAL_AUTHORIZATION_DIFFERENT_PROCESSING_CODE`
* `ORIGINAL_AUTHORIZATION_DIFFERENT_CLEARING_TYPE`
* `ORIGINAL_AUTHORIZATION_DIFFERENT_CURRENCY`
* `ORIGINAL_AUTHORIZATION_DIFFERENT_NUMBER_OF_INSTALLMENTS`
* `ORIGINAL_AUTHORIZATION_WITH_EXTERNAL_CALCULATION`
* `INCREMENTAL_AUTHORIZATION_WITH_EXTERNAL_CALCULATION`
* `MULTIPLE_CONFIRMATION_WITH_EXTERNAL_CALCULATION`
* `MULTIPLE_CONFIRMATION_ORIGINAL_AUTHORIZATION_WITH_EXTERNAL_CALCULATION`
* `MULTIPLE_CONFIRMATION_ORIGINAL_AUTHORIZATION_DIFFERENT_NUMBER_OF_INSTALLMENTS`

In [Processing code type validation](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations#processing-code-type-validation), the following new reasons are now available:

* `REVERSAL_PROCESSING_CODE_INVALID_BALANCE_IMPACT`
* `PROCESSING_CODE_TYPE_NOT_PERMITTED`

In [Processing code validation](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations#processing-code-validation), the following new reason is now available:

* `PROCESSING_CODE_STATUS_NOT_PERMITTED`

</summary>

<summary class="tabContent" id="Data and reporting">

### Reports

#### New

The new version of the [Account limits report](https://developers.pismo.io/pismo-docs/docs/account-limits-report-files-v2) is now available and includes the following improvements:

* Enhanced data accuracy with updated field types (for example, decimal(38,10))
* Inclusion of key fields that were missing in the previous version
* A more flexible time zone configuration for the reference date, enabling global scalability
* Improved compatibility with future platform features

The [outdated version of this report](https://developers.pismo.io/pismo-docs/docs/account-limits-report-files) is scheduled to be deprecated on 30 June 2025.

#### Updated

The following report file guides, located under “Base scheduled reports”, were legacy files and were no longer up-to-date, so they have been deleted. Information related to these reports can now be found in the table in [Reports for Brazil](https://developers.pismo.io/pismo-docs/docs/brazilian-reports).

* CADOC 3040 report files
* CADOC 3050 report files
* DECRED report files
* DOC 5816 report files

</summary>

<summary class="tabContent" id="Core banking">

### Banking operations

#### New

The new [Create interest plan version](https://developers.pismo.io/pismo-docs/reference/patch-v1-interest-plan) endpoint is now available.

#### Updated

In the [Interest-bearing accounts](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-list-products) API, the following error codes were changed:

* `400` error code for `Validation error [(Field 'Order' is invalid)]` was changed from `EIBA0008` to `EIBACC0008`. This change impacts every endpoint in the Interest-bearing accounts API that produces `400` errors.
* `404` error code for `Product not found` was changed from `EIBA0078` to `EIBACC0078`. This change impacts every endpoint that produces `404` errors.
* `409` error code for `Product is already detached` was changed from `EIBA0128` to `EIBACC0128`. This change impacts every endpoint that produces `409` errors.
* Another `409` error code for `The product ID provided is already attached` was changed from `EIBA0120` to `EIBACC0120`. This change impacts every endpoint that produces this error.
* `500` error code for `Internal error` was changed from `EIBA0007` to `EIBACC0007`. This change impacts every endpoint that produces 500 errors.

Also, the `savings_account_configs` object was removed from the following endpoints:

* [Attach savings account to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-account)
* [Attach savings accounts to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-program)

#### Docs

The description of the `interest_id_plan` field in the request body was updated to “Interest rate plan ID” instead of “Fee plan.” This update affects the following endpoints:

* [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
* [Create savings account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-savings-account-product)

#### Docs

In the [Register beneficiary](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v1-bank-accounts-beneficiaries) endpoint, the following `account_type` descriptions were updated:

* `CACC` - Checking/current account. Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.
* `SVGS` - Savings account.
* `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.
* `SLRY` - Salary account. Employer deposits a fixed amount every month.

### Transaction banking

#### Updated

A new object `reactivation_exceptions_config` was added to the following endpoints. This object allows you to specify configuration rules that allow certain transactions to bypass dormancy reactivation. This object includes two fields: `field` and `values`.

* [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2)
* [Update dormancy configuration](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2)
* [Get dormancy configuration](https://developers.pismo.io/pismo-docs/reference/getdormancyconfig) (in the `200` response payload)

#### Updated

The following new error message was added to the [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds) endpoint. This error explains that you should not apply restrictions while the account is still in the onboarding state.

`WRFO0012 : Account has not finished onboarding`

#### Updated

The following fields were added to the 200 response of the [Get account balance](https://developers.pismo.io/pismo-docs/reference/get-account-balances) and [Get account balance history](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history) endpoints to provide details on held funds and accrued remunerative interest.

* `held_funds` - Funds that are temporarily restricted due to regulatory or operational requirements, unavailable for transactions, and representing the total amount of earmarked or otherwise restricted balances.
* `held_checks_balance` - The balance from checks that the bank considers available but holds to earn interest. It increases when check holds are applied and decreases when those holds are released or canceled.
* `remunerative_interest_accrued` - This balance reflects the total interest pending capitalization. It increases as interest accrues and decreases when the accrued interest is added to the principal balance.

#### Updated

A new error code was added to the [Close transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-accounts-accountid-close) endpoint. This error is returned when a client attempts to close an account within five minutes of its creation, preventing premature closure while the account might still be processing or holding a balance.

`WCAC0040: Account balance is still being created. Please try again in a few minutes.`

</summary>

<summary class="tabContent" id="Card issuing">

### Cards

#### Updated

In the EXT environment, the `stage` field was removed from the following endpoint responses:

* [Update card status](https://developers.pismo.io/pismo-docs/reference/put-v1-card-status)
* [Get cards for customer and account](https://developers.pismo.io/pismo-docs/reference/get-v1-cards)
* [Get account cards](https://developers.pismo.io/pismo-docs/reference/get-v1-cards-by-account)
* [Update card information](https://developers.pismo.io/pismo-docs/reference/patch-v2-card)

### Card network integration

#### Docs

A note was added to the [Simulate authorizations](https://developers.pismo.io/pismo-docs/docs/simulate-authorizations) guide to clarify that the [Simulate authorization](https://developers.pismo.io/pismo-docs/reference/post_v1-authorizations) endpoint does not issue a Clearing event. Instead, when you use the endpoint for simulation with `MTI Clearing (1240)`, it generates a [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event with the category `CONFIRMATION`, which represents the clearing.

### Statements

#### Updated

In the [Create an accrual type post configuration](https://developers.pismo.io/pismo-docs/reference/createaccrualtypepostconfig) endpoint, the following updates were made.

* The `additional_configurations` object was added to body parameters.
* New possible values were added to the `accrual_type` body parameter.

#### Updated

The [Delinquency buckets](https://developers.pismo.io/pismo-docs/docs/delinquency-buckets) guide was updated to correct some information that is no longer valid. The original documentation stated that every 7253 transaction type will discharge buckets. This has changed. The program parameter `DELINQUENCY_BUCKETS_PAYMENTS_TRANSACTIONS_TYPES` can now be used to specify which transaction types will discharge buckets.

#### Docs

The [Cancel account transaction category](https://developers.pismo.io/pismo-docs/reference/cancelaccounttransactioncategory) endpoint documentation was moved from “Transaction categories” to “Interest rate” in the API reference menu. “Transaction categories” was wrong because that heading groups the program-level transaction category endpoints. The account-level endpoints belong in “Interest rate”.

#### Docs

In the [Update program due date](https://developers.pismo.io/pismo-docs/reference/updateprogramduedate) endpoint, the descriptions for the `active` and `grace_period_days` body parameters were updated.

#### Docs

A note was added to the description for all the [endpoints](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) under the “Revolving credit - Calendar management” menu header. The note explains that the endpoints don’t handle fixed due date calendars.

#### Docs

Renamed the “Calendars and holidays in credit card accounts” guide to [Holidays in credit card accounts](https://developers.pismo.io/pismo-docs/docs/holidays-in-credit-card-accounts), and rewrote the guide to remove all reference to calendars, since the concept of calendars is not needed to explain holidays in credit card accounts.

#### Docs

The following new guides are now available.

* [Calendar management strategies](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies)
* [Fixed cycle closing calendar management strategy](https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy)

The following guides were updated to better explain calendars and calendar management strategies.

* [Understanding statements | Calendars](https://developers.pismo.io/pismo-docs/docs/understanding-statements#calendars): Moved most of the information that was in this section was moved into a separate guide and the section was shortened accordingly.
* [Managing grace period | Calculating the real due date](https://developers.pismo.io/pismo-docs/docs/managing-grace-period#calculating-the-real-due-date): This section was updated to clarify the material.
* [Fixed due date calendars](https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars): The text was updated to clarify the material.

#### Docs

The following endpoints were renamed for consistency with the header names and with other references to accruals in the documentation. The endpoint descriptions were also updated to replace “interest” with “accrual”.

* Configure account interest rates → [Configure account accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates)
* Delete account interest rates -> [Delete account accrual rates](https://developers.pismo.io/pismo-docs/reference/deleteaccountaccrualtypesrate)
* Configure program interest rates → [Configure program accrual rate](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates)
* List program interest rates → [List program accrual rates](https://developers.pismo.io/pismo-docs/reference/listprogramaccrualtypesrates)
* Delete program interest rates → [Delete program accrual rates](https://developers.pismo.io/pismo-docs/reference/deleteaccrualtypesrates)

#### Docs

The `period-to-calculate` body parameter in the [Configure program accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates) endpoint incorrectly listed `UNTIL_DUE_DATE` as the only possible value. The `AFTER_DUE_DATE` was added as another possible value.

#### Docs

The Cancel account transaction category was moved from “Transaction categories” to “Interest rate” in the API Reference menu. “Transaction categories” was wrong because that heading groups the program-level transaction category endpoints. The account-level endpoints belong in “Interest rate”.

### Tokenization

#### Updated

The new `update_previous_tokens` field is now available in the [Assign network card profile](https://developers.pismo.io/pismo-docs/reference/post-v1-cards-card-id-network-tokens-profile) endpoint. This field enables you to assign a new network card profile to all previous card tokens.

</summary>

<summary class="tabContent" id="Seller management">

### Marketplace

#### Updated

The [Marketplace created](https://developers.pismo.io/events/docs/marketplace-marketplace-created-1) and [Marketplace updated](https://developers.pismo.io/events/docs/marketplace-marketplace-updated-1) events now have a version 2 of each. In version 2, these fields are removed:

* `days_to_payment`
* `acquirer_mdr`
* `incremental_mdr`
* `bank_account` (and sub fields)
* `cedente_id`
* `financial_email`
* `chargeback_management`
* `org_as_sub_acquirer`

</summary>

<summary class="tabContent" id="Resources">

### Control Center

#### Deprecated

The following deprecated program parameters were removed from the Control Center:

* Annuity fee amount
* Annuity installments

They were removed from the table in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide also.

#### Updated

The `CONTA CORRENTE` account type was removed from the **Required?** column of the table in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide.

#### Docs

A sentence was added to the last bullet point in the [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals) guide.

### Postman

#### Docs

The new [Postman Pismo cards collection walkthrough](https://developers.pismo.io/pismo-docs/docs/pismo-cards-postman-collection-walkthrough) provides step-by-step instructions for creating and managing cards using Pismo API endpoints.

</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/pix/funds-recoveries` (`post-create-funds-recovery`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--funds-recovery |
| `POST /v1/migrations/on-us-authorizations` (`PostOnUsAuthorizationsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--on-us-authorization-migration |
| `PATCH /v1/interest/plan/{interestPlanId}` (`patch-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `GET /v1/products` (`interest-bearing-v1-list-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/savings-accounts/accounts/{accountId}/attach` (`interest-bearing-v1-savings-account-attach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/savings-accounts/programs/{programId}/attach` (`interest-bearing-v1-savings-account-attach-program`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/savings-accounts` (`interest-bearing-v1-create-savings-account-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/beneficiaries` (`post-intl-bank-accounts-v1-bank-accounts-beneficiaries`) | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--beneficiaries |
| `POST /corporate/v2/dormancy-config` (`post-dormancy-config-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` (`patch-dormancy-config-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `GET /corporate/v1/dormancy-config/{dormancyConfigId}` (`getDormancyConfig`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `POST /corporate/v1/restricted-funds` (`post-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /bank-statements/v1/account-balances/{externalAccountId}` (`get-account-balances`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v1/account-balances/{externalAccountId}/history` (`get-account-balance-history`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `POST /corporate/v1/corporate-accounts/{externalAccountId}/close` (`post-accounts-accountId-close`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status` (`put-v1-card-status`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-status |
| `GET /wallet/v1/customers/{customerId}/accounts/{accountId}/cards` (`get-v1-cards`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `GET /wallet/v1/cards` (`get-v1-cards-by-account`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `PATCH /wallet/v2/cards/{cardId}` (`patch-v2-card`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /networktransactions/v1/authorizations` (`post_v1-authorizations`) | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `POST /v1/programs/{programId}/accrual-type-post-config` (`createAccrualTypePostConfig`) | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations |
| `DELETE /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId}` (`cancelAccountTransactionCategory`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `PATCH /statements-v2/v1/programs/{programId}/due-dates/{programDueDateId}` (`updateProgramDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /v1/programs/{programId}/calendar-strategies` (`CreateProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `POST /v1/accounts/{accountId}/accrual-type-rates` (`postAccountAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `DELETE /v1/accounts/{accountId}/accrual-type-rates` (`deleteAccountAccrualTypesRate`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `POST /v1/programs/{programId}/accrual-type-rates` (`postAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `GET /v1/programs/{programId}/accrual-type-rates` (`listProgramAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `DELETE /v1/programs/{programId}/accrual-type-rates` (`deleteAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `POST /v1/cards/{cardId}/network-tokens/profile` (`post-v1-cards-card-id-network-tokens-profile`) | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--network-card-profile |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/5-december-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/5-december-2025 | `1c9177d03f1cf4f2…` | not stated |

## Related knowledge units

- `KU-API-banking-bank-accounts--beneficiaries` — API reference: Banking - Bank accounts — Beneficiaries
- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-bearing-accounts--program-attachment` — API reference: Banking - Interest-bearing accounts — Program attachment
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-card-issuing-cards--card-status` — API reference: Card issuing - Cards — Card status
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-tokenization--network-card-profile` — API reference: Card issuing - Tokenization — Network card profile
- `KU-API-instant-payments-pix-management--funds-recovery` — API reference: Instant payments - Pix management — Funds recovery
- `KU-API-migrations--on-us-authorization-migration` — API reference: Migrations — On-us authorization migration
- `KU-API-revolving-credit-calendar-management--program-calendar-strategies` — API reference: Revolving credit - Calendar management — Program calendar strategies
- `KU-API-revolving-credit-configurations--account-accrual-rates` — API reference: Revolving credit - Configurations — Account accrual rates
- `KU-API-revolving-credit-configurations--program-accrual-rates` — API reference: Revolving credit - Configurations — Program accrual rates
- `KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations` — API reference: Revolving credit - Interest accruals — Accrual type post configurations
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
