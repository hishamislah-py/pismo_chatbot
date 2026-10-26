---
ku_id: KU-CHG-6-june-2025
title: 'Changelog: 6 June 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/6-june-2025.md
  sha256: d80ad16636ee551f95cf5a4e1b4a10db38d1f9eba292e3ec59100f81a702d8b4
  url: https://developers.pismo.io/pismo-docs/changelog/6-june-2025
  role: changelog_post
  updated_at: ''
operations:
- CreateProgramBasedOnTemplate
- CreateProgramBasedOnTemplateAsync
- CreateProgramCalendarStrategy
- DeleteInstallmentPaymentByPaymentAgreementId
- GetAccountAccrualsV2
- GetAvailableDueDates1
- GetInstallmentPaymentByPaymentAgreementId
- GetProgramCalendarStrategy
- ListProgramCalendarStrategies
- UpdateProgramCalendarStrategy
- UpdateStatementsDueDate
- accept-reject-authorization
- cancel-recurrence-automatic
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- corporate-v2-post-scheduled-payments
- createAccrualTypePostConfig
- createLoanProductV2
- createPrepayment
- enroll-card-enrollment
- get-corporate-transaction
- get-recurrence-automatic
- get-v1-card-satus-history
- getAccountAccrualsV3
- getAccountsTransactionsInterest_1
- getAccrualTypePostConfig
- getByStatementId
- getLoanProductV2
- getProgramDueDates
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-get-deposit-products
- interest-bearing-v1-list-products
- list-authorizations
- list-recurrence-automatic
- patch-division-v2
- post-config-by-tenant
- post-division-v2
- post-qr-code
- post-recurrence-automatic
- post-v1-accounts-flex-controls
- post-v1-card-reissue
- post-v1-networkauthorization-disputes
- retrievePaginatedLoans
- saveAccountTransactionInterest
- saveProgramDueDate
- statementDueDate
- updateAccrualTypePostConfig
- updateProgramDueDate
related_kus:
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--transactions
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--card-status
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--disputes-part-02
- KU-API-card-issuing-visa-flexible-credentials--enrollment
- KU-API-core-platform-balance-watcher--limit-configurations
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-payment-configurations--payment-method-configurations
- KU-API-instant-payments-automatic-pix--automatic-pix
- KU-API-instant-payments-automatic-pix--automatic-pix-data
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--pix-part-02
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-lending--prepayment
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-calendar-management--program-calendar-strategies
- KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--accruals
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--refinancing
- KU-API-revolving-credit-statements--statement
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 6 June 2025
coverage_window: 2 May and 6 June 2025
---

# Changelog: 6 June 2025

**KU ID:** `KU-CHG-6-june-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **6 June 2025** (changes between 2 May and 6 June 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated".

## Topics covered

AI-powered search; Card issuing - Visa Flexible Credentials; Core banking - Instant payments; Client webhooks; Flexible transaction controls; Migrations; Payments; Setup; Events; Reports; Banking as a Service; Banking operations; Instant payments; Transaction banking; Card network integration; Cards management; Disputes; Statements; Lending; Pismo Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/6-june-2025

<!-- source:begin path=changelog/6-june-2025.md part=0-end -->

# 6 June 2025

Changes between 2 May and 6 June 2025

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### AI-powered search

#### New

Introducing the new [AI-powered search](https://developers.pismo.io/pismo-docs/docs/get-started-with-ai-powered-search)—faster, smarter, and with deeper insights. Our more comprehensive search delivers instant responses plus direct links to related content. Need code? Copy snippets straight from the results with a single click.

### Card issuing - Visa Flexible Credentials

#### New

Pismo now offers Visa Flexible Credentials, which allows a single card to access multiple funding sources as backup during transactions. A new [VFC](https://developers.pismo.io/pismo-docs/reference/enroll-card-enrollment) API and [guide](https://developers.pismo.io/pismo-docs/docs/visa-flexible-credentials) were published to support this feature.

This feature is currently in beta release to give you a chance to check out its functionality and provide feedback. Its functionality might change before being released to production. Contact your Pismo representative for more information or to participate in the beta program.

### Core banking - Instant payments

#### New

Pismo now supports [Pix Automatic](https://developers.pismo.io/pismo-docs/docs/pix-automatic), a Pix feature designed for recurring payments, such as gym memberships and rent. This includes new Pix Automatic endpoints for [creating a recurring transaction](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic), [getting a recurring transaction](https://developers.pismo.io/pismo-docs/reference/get-recurrence-automatic), [listing recurring transactions](https://developers.pismo.io/pismo-docs/reference/list-recurrence-automatic), [cancel a recurring transaction](https://developers.pismo.io/pismo-docs/reference/cancel-recurrence-automatic) and [authorize or reject a recurring transaction](https://developers.pismo.io/pismo-docs/reference/accept-reject-authorization).

This feature is currently in beta release to give you a chance to check out its functionality and provide feedback. Its functionality might change before being released to production. Contact your Pismo representative for more information or to participate in the beta program.

</summary>

<summary class="tabContent" id="Core platform">
  ### Client webhooks

#### Updated

A new request field, `card_metadata`, was added to the [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook). Both the request fields table and the sample request were updated with this new field.

### Flexible transaction controls

#### Docs

On the [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) page, the `limit_duration` field is not longer marked as required.

### Migrations

#### Docs

The [Migrations](https://developers.pismo.io/pismo-docs/docs/migrations-overview) overview guide was expanded and revised with more details about migrating different platform entity types.

### Payments

#### Updated

In the [Payment configurations](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant) API, the new fields `confirmation_verification_mtls` and `confirmation_verification_mtls_prefix` are now available.

#### Docs

In the [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event, most fields were updated with the minimum and maximum length values and the description of the `validation_results` field was updated with the link to the corresponding guide that lists all possible validations.

#### Docs

In the [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-1) endpoint, the links for the endpoint to create processing codes were updated.

#### Docs

In the [Payment scheduler \[beta\]](doc:payment-scheduler) guide, information about creating a pre-schedule was corrected. Instructions to contact Pismo representative were removed and instructions to set the `Post the pre-scheduled transactions when the cycle closes` program parameter were added.

### Setup

#### Updated

The new program parameter `Overdue strategy start`  was added to the table in [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table).

#### Docs

The endpoint descriptions for [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) and [Create program (async)](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplateasync) were updated to clarify that neither endpoint generates an event.

#### Docs

* The description for the [Change due date](https://developers.pismo.io/pismo-docs/reference/updatestatementsduedate) endpoint was updated. A note was added that the due date must be updated no later than two days before the cycle closes, otherwise it will not function properly.
* A similar note was added to the description of the [Update statements calendar](https://developers.pismo.io/pismo-docs/reference/statementduedate) endpoint, explaining that the calendar must be updated no later than two days before the cycle closes to function properly.

#### Docs

A callout in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide was corrected. It originally stated that you could look up program parameter IDs in Control Center. This was not correct. You have to use an endpoint.

</summary>

<summary class="tabContent" id="Data and reporting">
  ### Events

#### New

Under **Core banking**, the new section **Credit rights** now includes the following new events.

* [Contract digital receivable supplement created](https://developers.pismo.io/events/docs/credit-rights-contract-digital-receivable-supplement-create-success-1)
* [Contract digital receivable supplement creation failed](https://developers.pismo.io/events/docs/credit-rights-contract-digital-receivable-supplement-create-failure-1)
* [Digital receivable create succeeded](https://developers.pismo.io/events/docs/credit-rights-digital-receivable-create-success-1)
* [Digital receivable create failed](https://developers.pismo.io/events/docs/credit-rights-digital-receivable-create-failure-1)
* [Contract create success](https://developers.pismo.io/events/docs/credit-rights-contract-create-success-1)
* [Contract create failure](https://developers.pismo.io/events/docs/credit-rights-contract-create-failure-1)
* [Digital receivable unit contract create success](https://developers.pismo.io/events/docs/credit-rights-contract-digital-receivable-unit-create-success-1)
* [Digital receivable unit contract creation failed](https://developers.pismo.io/events/docs/credit-rights-contract-digital-receivable-unit-create-failure-1)

#### New

The following new events are now available.

* [Balance configuration created](https://developers.pismo.io/events/docs/balances-config-created-1)
* [Balance configuration updated](https://developers.pismo.io/events/docs/balances-config-updated-1)

### Reports

#### Updated

[Brazilian reports](https://developers.pismo.io/pismo-docs/docs/brazilian-reports) were updated to put reports in alphabetical order by name in the **Report** column. Two new reports were added:

* APIX 001 - 1201
* COSIF 4111

The “National Transactions 6308 Report“ report was renamed to “6308 Payment Card Report”.

The entry for “SVR (Sistema de Valores a Receber / System of Receivables): \[9800] and \[9805]” originally covered two reports: 9800 and 9805. These have been separated into 2 entries in the table: “SVR 9800 (Sistema de Valores a Receber / System of Receivables)” and “SVR 9805 (Sistema de Valores a Receber / System of Receivables)”

</summary>

<summary class="tabContent" id="Core banking">
  ### Banking as a Service

#### Updated

The new Prospect creation service feature is now available. This feature enables banks to automate the account opening process. For details, refer to the [Prospect creation service](https://developers.pismo.io/pismo-docs/docs/banking-overview#prospect-creation-service) section of the Banking overview guide.

### Banking operations

#### Updated

To comply with U.S. Regulation D, the Deposit product creation process has been enhanced by expanding the capabilities for configuring early withdrawal penalties on invested amounts. This was done by adding a `penalties` object field to the following endpoints:

* [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) - in the request body and 201 response
* [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products) - in the 200 response
* [List product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-list-products) - in the 200 response

### Instant payments

#### New

The following new Pix endpoints are now available:

* [List recurrence authorizations \[beta\]](ref:list-authorizations)
* [Cancel recurrence \[beta\]](ref:cancel-recurrence-automatic)

#### Updated

In the [Create recurrence \[beta\]](ref:post-recurrence-automatic) endpoint, `reason_code` values for cancellation were updated in the response.

#### Updated

In the [Accept/reject recurrence authorization \[beta\]](ref:accept-reject-authorization)  endpoint, the `payment_date_time` and `transaction_identification` fields are now available in the request body.

#### Updated

The Pix endpoint [Validate QR code](https://developers.pismo.io/pismo-docs/reference/post-qr-code) can now validate a QR code for a Pix Automatic recurring payment. For this, the endpoint now returns a `recurrence` object.

### Transaction banking

#### Docs

In the 400 error messages for [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) and [Update division](https://developers.pismo.io/pismo-docs/reference/patch-division-v2) endpoints, the new error explanation “Administrative division is misconfigured” was added.

#### Docs

The description of the `payment_datetime` field was clarified. It appears in the following places:

* [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) - in the request body
* [Get transaction](https://developers.pismo.io/pismo-docs/reference/get-corporate-transaction) - in the 200 response
* [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments) - in debits and credits array objects of request body and 200 response
* [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments) - in the request body

#### Docs

The following, formerly missing, 400 errors were added to [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) and [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments):

* 400 - Future payment datetime above limit
* 400 - Back payment datetime above limit

</summary>

<summary class="tabContent" id="Card issuing">
  ### Card network integration

#### Updated

A new custom code was added for the network transactions. This new code, **OON** (Org operation not found), is returned when the operation related to the `Transaction Type` subfield of the Processing Code (DE3) present in the body of the authorization message is not configured in the program of the card used. This new custom code was added to the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) guide and its definition was added to the [Validation codes definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#oon---org-operation-not-found) guide.

#### Docs

The Rule list guide content for the [Flex controls validation](https://developers.pismo.io/pismo-docs/docs/rule-list#flex-controls-validation) rule and the [Available limits validation](https://developers.pismo.io/pismo-docs/docs/rule-list#available-limits-validation) rule for Ledger were updated for clarity and now have updated payload examples.

### Cards management

#### Updated

The [List card status history](https://developers.pismo.io/pismo-docs/reference/get-v1-card-satus-history) endpoint now returns an `operation` enum field, indicating the operation that caused the status change.

#### Docs

The new [Card PIN, PAN,  and tokens when a card is reissued](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses#card-pin-pan--and-tokens-when-a-card-is-reissued) section has been added to the Cards management guide. This section makes clear what happens to a card’s PIN, PAN, and tokens when a card is reissued. The same information has also been added to the [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue) endpoint documentation.

### Disputes

#### Updated

In the [Disputes](https://developers.pismo.io/pismo-docs/reference/post-v1-networkauthorization-disputes) API, the `x-account-id` parameter was removed and authorization header was included in all impacted endpoints.

### Statements

#### Updated

In the response object of the List statements v2 endpoint , `bar_code` was marked as deprecated and `cycle_number` field was added to the `cycle` object.

#### Updated

The [Projected accruals](https://developers.pismo.io/pismo-docs/docs/projected-accruals#reversing-projected-accruals) guide was updated. Formerly, projected accruals could only be reversed for refinancing and overdue transactions. Now, you can configure reversal for other types of transactions using the new [Update accrual type post configuration](https://developers.pismo.io/pismo-docs/reference/updateaccrualtypepostconfig) endpoint.

#### Updated

The `stop_accrual_reason` field was removed from the `additional_info` object in 200 response for the following endpoints:

* [List account accruals v2](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv2)
* [List account accruals v3](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv3)

#### Docs

The following calendar management endpoints were updated to correct the request and response parameters:

* [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy)
* [List program calendar strategies](https://developers.pismo.io/pismo-docs/reference/listprogramcalendarstrategies)
* [Get program calendar strategy](https://developers.pismo.io/pismo-docs/reference/getprogramcalendarstrategy)
* [Update program calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateprogramcalendarstrategy)

#### Docs

The following updates were made in the Statements documentation.

* The endpoint “Save account interest rate” was renamed to [Configure account transaction category rates](https://developers.pismo.io/pismo-docs/reference/saveaccounttransactioninterest) and the endpoint description was updated.
* The endpoint “List account interest rates” was renamed to [List account transaction category rates](https://developers.pismo.io/pismo-docs/reference/getaccountstransactionsinterest_1) and the endpoint description was updated.
* The corresponding endpoint names were updated in [Configuring accrual rates](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#validation-for-configuring-accruals) and  [Endpoints that require an account-specific token](https://developers.pismo.io/pismo-docs/reference/endpoints-that-require-an-account-specific-token).

#### Docs

The [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid) endpoint includes a new query parameter called `showAmounts`. If this parameter is set to `true`, the following additional fields will be returned in the endpoint response:

* `amount_due`
* `amount_paid_until_due_date`
* `amount_paid_after_due_date`
* `other_credits_until_due_date`
* `other_credits_after_due_date`
* `evolve_to_delinquency`

#### Docs

In the first paragraph of the [Credit liquidation](https://developers.pismo.io/pismo-docs/docs/credit-liquidation) guide, a correction was made to the explanation of what happens if you don’t set the program parameter `Number of days to block the account for unpaid statement`.

#### Docs

A new section **Accrual type post configurations** was added with the following new endpoints:

* [Create an accrual type post configuration](https://developers.pismo.io/pismo-docs/reference/createaccrualtypepostconfig)
* [List accrual type post configurations](https://developers.pismo.io/pismo-docs/reference/getaccrualtypepostconfig)
* [Update accrual type post configuration](https://developers.pismo.io/pismo-docs/reference/updateaccrualtypepostconfig)

#### Docs

The names of the following endpoints were changed.

* “Cancel installment payment” was changed to [Cancel payment agreement](https://developers.pismo.io/pismo-docs/reference/deleteinstallmentpaymentbypaymentagreementid).
* “Get installment payment” was changed to [Get payment agreement](https://developers.pismo.io/pismo-docs/reference/getinstallmentpaymentbypaymentagreementid).

#### Docs

Description of the `grace_period_days` field was corrected for the following endpoints:

* [List available due dates](https://developers.pismo.io/pismo-docs/reference/getavailableduedates1): 200 response
* [Save program due date](https://developers.pismo.io/pismo-docs/reference/saveprogramduedate): 201 response
* [List program due dates](https://developers.pismo.io/pismo-docs/reference/getprogramduedates): 200 response
* [Save program due date](https://developers.pismo.io/pismo-docs/reference/saveprogramduedate): in request
* [Update program due date](https://developers.pismo.io/pismo-docs/reference/updateprogramduedate): in request
* [List program due dates](https://developers.pismo.io/pismo-docs/reference/getprogramduedates): query parameter

#### Docs

Made the following changes to the [Installment advancements](https://developers.pismo.io/pismo-docs/docs/installment-management#installment-advancements) guide.

* Updated bullet point #3 in the first section of the guide.
* Updated the example in the [Creating an installment advancement](https://developers.pismo.io/pismo-docs/docs/installment-management#creating-an-installment-advancement) section.

</summary>

<summary class="tabContent" id="Digital lending">
  ### Lending

#### New

The following new endpoints are now available in the Lending API.

* [Create prepayment record \[beta\]](ref:createprepayment) enables you to create a prepayment record containing one or multiple repayments so you can implement Buy Now Pay Later (BNPL) programs.
* [Create loan product \[beta\]](ref:createloanproductv2) defaults to BNPL for the `product_type`.
* [Get loan product \[beta\] ](ref:getloanproductv2) gets a loan product by its ID.
* [List loans \[beta\]](ref:retrievepaginatedloans) filters loans by account ID, authorization ID, or loan product ID and provides information about scheduled repayments in the response.

#### Deprecated

The following endpoints were deprecated.

* [Create loan product](https://developers.pismo.io/pismo-docs/reference/createloanproduct)
* [Get loan product](https://developers.pismo.io/pismo-docs/reference/getloanproduct)
* [List loans](https://developers.pismo.io/pismo-docs/reference/listloans)

#### New

The [Loan updated](https://developers.pismo.io/events/docs/lending-lending-loan-update-1) event now includes a `repayment_schedule` object that includes the repayment, installment, amount, and due date information.

#### New

The new [Prepayment created](https://developers.pismo.io/events/docs/lending-prepayment-creation-1) event signals when a prepayment has been created or changes status.

#### Docs

[Lending events](https://developers.pismo.io/events/docs/lending-loan-repayment-status-change-1) were rewritten and edited for clarity and standards.

</summary>

<summary class="tabContent" id="Resources">
  ### Pismo Control Center

#### Updated

Accounts management in Pismo Control Center now supports [two types of searches](https://developers.pismo.io/pismo-docs/docs/find-an-account):

* Search by customer using a document, account, email or name. When using this type of search, you will select a customer and access all related accounts in the Accounts overview page.
* Search by specific account using the account number. When using this type of search, you can select the specific account and go directly to the overview page.

</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /flex_credentials/v1/vfc/enrollment/cards/{cardId}` (`enroll-card-enrollment`) | `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` | no | KU-API-card-issuing-visa-flexible-credentials--enrollment |
| `POST /inst-pull-pay/v1/pix/automatic` (`post-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `GET /inst-pull-pay/v1/pix/automatic/{recurrence_id}` (`get-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix-data |
| `GET /inst-pull-pay/v1/pix/automatic` (`list-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix-data |
| `POST /inst-pull-pay/v1/pix/automatic/cancel` (`cancel-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /inst-pull-pay/v1/pix/automatic/payer/authorization` (`accept-reject-authorization`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/config` (`post-config-by-tenant`) | `api-specs/Core_platform_-_Balance_watcher.yaml` | no | KU-API-core-platform-balance-watcher--limit-configurations |
| `POST /payment-methods-configs/v1/configs` (`post-config-by-tenant`) | `api-specs/Core_platform_-_Payment_configurations.yaml` | no | KU-API-core-platform-payment-configurations--payment-method-configurations |
| `POST /programs/v1/programs/template` (`CreateProgramBasedOnTemplate`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v2/programs/template` (`CreateProgramBasedOnTemplateAsync`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `PUT /statements/v1/accounts/{accountId}/statements/due-date` (`UpdateStatementsDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `PATCH /statements-v2/v2/due-date` (`statementDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/deposits/{productId}` (`interest-bearing-v1-get-deposit-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/products` (`interest-bearing-v1-list-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /inst-pull-pay/v1/pix/automatic/authorizations` (`list-authorizations`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix-data |
| `POST /pix/v1/pix/qrcode/validate` (`post-qr-code`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01, KU-API-instant-payments-pix-payments--pix-part-02 |
| `POST /corporate/v2/divisions` (`post-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PATCH /corporate/v2/divisions/{divisionCode}` (`patch-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `GET /corporate/v1/corporate-transactions/{transactionId}` (`get-corporate-transaction`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |
| `POST /corporate/v2/payments/multileg` (`corporate-v2-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/scheduled-payments` (`corporate-v2-post-scheduled-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `GET /wallet/v1/cards/{cardId}/status-history` (`get-v1-card-satus-history`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-status |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` (`post-v1-card-reissue`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `POST /v1/networkauthorization-disputes` (`post-v1-networkauthorization-disputes`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01, KU-API-card-issuing-disputes--disputes-part-02 |
| `PATCH /v1/programs/{programId}/accrual-type-post-config/{accrualTypePostConfigId}` (`updateAccrualTypePostConfig`) | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations |
| `GET /statements/v2/accounts/{accountId}/interest-accruals` (`GetAccountAccrualsV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals` (`getAccountAccrualsV3`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `POST /v1/programs/{programId}/calendar-strategies` (`CreateProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `GET /v1/programs/{programId}/calendar-strategies` (`ListProgramCalendarStrategies`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `GET /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` (`GetProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `PATCH /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` (`UpdateProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` (`saveAccountTransactionInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `GET /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` (`getAccountsTransactionsInterest_1`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `GET /statements-v2/v3/accounts/{accountId}/statements` (`getByStatementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /v1/programs/{programId}/accrual-type-post-config` (`createAccrualTypePostConfig`) | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations |
| `GET /v1/programs/{programId}/accrual-type-post-config` (`getAccrualTypePostConfig`) | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations |
| `DELETE /statements/v4/accounts/{accountId}/installment-payments/{id}` (`DeleteInstallmentPaymentByPaymentAgreementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /statements/v4/accounts/{accountId}/installment-payments/{id}` (`GetInstallmentPaymentByPaymentAgreementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /statements/v1/accounts/{accountId}/available-due-dates` (`GetAvailableDueDates1`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /statements-v2/v1/programs/{programId}/due-dates` (`saveProgramDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `GET /statements-v2/v1/programs/{programId}/due-dates` (`getProgramDueDates`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `PATCH /statements-v2/v1/programs/{programId}/due-dates/{programDueDateId}` (`updateProgramDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /v2/prepayments` (`createPrepayment`) | `api-specs/Lending.yaml` | no | KU-API-lending--prepayment |
| `POST /v2/loan-products` (`createLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /v2/loan-products/{productId}` (`getLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /v2/loans` (`retrievePaginatedLoans`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-payments-1` | Create cash-in or cash-out | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `endpoints-that-require-an-account-specific-token` | Endpoints that require an account-specific token | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `createloanproduct` | Create loan product | not found in the current OpenAPI specifications. Name-based inference: link text "Create loan product" equals the endpoint name "Create loan product" in the removed-endpoints list (row Lending v1 / Create, simulate, manage loans, date removed `7/1/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`createLoanProductV2` (POST /v2/loan-products)); no source states that it replaces the removed endpoint. |
| `getloanproduct` | Get loan product | not found in the current OpenAPI specifications. Name-based inference: link text "Get loan product" equals the endpoint name "Get loan product" in the removed-endpoints list (row Lending v1 / Create, simulate, manage loans, date removed `7/1/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`getLoanProductV2` (GET /v2/loan-products/{productId})); no source states that it replaces the removed endpoint. |
| `listloans` | List loans | not found in the current OpenAPI specifications. Name-based inference: link text "List loans" equals the endpoint name "List loans" in the removed-endpoints list (row Lending v1 / Create, simulate, manage loans, date removed `7/1/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`retrievePaginatedLoans` (GET /v2/loans)); no source states that it replaces the removed endpoint. |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/6-june-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/6-june-2025 | `d80ad16636ee551f…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--transactions` — API reference: Banking - Transaction banking — Transactions
- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--card-status` — API reference: Card issuing - Cards — Card status
- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--disputes-part-02` — API reference: Card issuing - Disputes — Disputes (part 2 of 2)
- `KU-API-card-issuing-visa-flexible-credentials--enrollment` — API reference: Card issuing - Visa Flexible Credentials [beta] — Enrollment
- `KU-API-core-platform-balance-watcher--limit-configurations` — API reference: Core platform - Balance watcher — Limit configurations
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-payment-configurations--payment-method-configurations` — API reference: Core platform - Payment configurations — Payment method configurations
- `KU-API-instant-payments-automatic-pix--automatic-pix` — API reference: Instant payments - Automatic Pix — Automatic Pix
- `KU-API-instant-payments-automatic-pix--automatic-pix-data` — API reference: Instant payments - Automatic Pix — Automatic Pix data
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-02` — API reference: Instant payments - Pix payments — Pix (part 2 of 2)
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-lending--prepayment` — API reference: Lending — Prepayment
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-calendar-management--program-calendar-strategies` — API reference: Revolving credit - Calendar management — Program calendar strategies
- `KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations` — API reference: Revolving credit - Interest accruals — Accrual type post configurations
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
