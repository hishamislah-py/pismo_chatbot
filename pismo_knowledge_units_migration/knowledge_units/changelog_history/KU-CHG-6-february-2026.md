---
ku_id: KU-CHG-6-february-2026
title: 'Changelog: 6 February 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/6-february-2026.md
  sha256: 87df813788c4da3c01389d1327dc913911252caf437329375c3ef274e6988af6
  url: https://developers.pismo.io/pismo-docs/changelog/6-february-2026
  role: changelog_post
  updated_at: ''
operations:
- CreateInstallmentAdvancementV2
- CycleClosingRequest
- GetInstallmentAdvancementV2ById
- ListTransactions
- PostCardsV1
- cancelAccountTransactionCategory
- cancelInstallmentAdvanceV2
- cancelLoanV2
- corporate-v3-post-multileg-payments
- createTransactionCategory
- deleteAccrualTypesConfigurations
- get-fps-in-transaction
- get-hierarchies
- get-list-dict-refunds
- get-overdraft-product
- get-v2-pix-account-infractions
- get-v2-pix-infraction
- get-v2-pix-infraction-search
- getProgramDueDates
- interest-bearing-v1-create-deposit-product
- listTransactionCategoryInterest
- post-attach-product-to-account
- post-authorization
- post-cancel-fps
- post-list-fraud-markers
- post-overdraft-product
- post-pix-out-transfer
- post-release-fps
- post-v1-accounts-flex-controls
- post-v1-interest-plan
- postAccrualTypesConfigurations
- postAccrualTypesRates
- saveAccountTransactionInterest
- updateTransactionCategoryInterest
related_kus:
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-overdraft--account
- KU-API-banking-overdraft--product
- KU-API-banking-transaction-banking--hierarchies
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-pix-management--anti-fraud
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-instant-payments-pix-management--refunds
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--pix-part-02
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-API-lending--loans
- KU-API-migrations--card-migration
- KU-API-revolving-credit-calendar-management--close-account-cycle
- KU-API-revolving-credit-configurations--additional-accrual-type-configurations
- KU-API-revolving-credit-configurations--program-accrual-rates
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 6 February 2026
coverage_window: 9 January and 6 February 2026
---

# Changelog: 6 February 2026

**KU ID:** `KU-CHG-6-february-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **6 February 2026** (changes between 9 January and 6 February 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

## Topics covered

Control Center; Lending; Core banking - Transaction banking; Client webhooks; Flexible transaction controls; Migrations; Payments; Programs; Rates and fees; Transactions; Support; Events; Reports; Banking operations; Instant payments; Interest management; Transaction banking; Authorizations; Network authorizations; Statements; Merchants

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/6-february-2026

<!-- source:begin path=changelog/6-february-2026.md part=0-end -->

# 6 February 2026

Changes between 9 January and 6 February 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### Control Center

  #### New

  The [dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval) feature was updated in Control Center. You can now request Pismo to enable dual approval for creating or deactivating access keys and creating, editing, or deactivating OpenID authentication configurations.

  ### Lending

  #### New

  The new [Cancel loan V2](https://developers.pismo.io/pismo-docs/reference/cancelloanv2) endpoint is now available in beta release. The endpoint introduces loan cancellation functionality with the following enhanced features.

  * New request/response schemas with support for configurable processing codes and metadata
  * Comprehensive error handling
  * Supporting schemas for loan cancellation processing codes and refund options

  ### Core banking - Transaction banking

  #### New

  The [Dormancy reactivation exception](https://developers.pismo.io/pismo-docs/docs/dormancy-reactivation-exception) guide is now available. It describes the enhanced feature that allows you to use the `reactivation_exceptions_config` object to specify values that bypass the standard dormancy reactivation logic.
</summary>

<summary class="tabContent" id="Core platform">
  ### Client webhooks

  #### Docs

  The response field `merchant_denial_code` was added to the [Full balance anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook) section of the Client webhooks guide. This previously missing field was added to the **Response fields** list and to the **Sample response**.

  #### Docs

  A duplicate request field, `cardholder_postal_code`, was removed from the [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) section of the Client webhooks guide. This duplicate field was removed from the **Request fields** list and from the **Sample request**.

  ### Flexible transaction controls

  #### Updated

  In the [flex controls](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) endpoints, in the `conditions` object, the `attribute` enum field now has a new value - `avr` - which indicates that the transaction is a card network Account Verification Request (AVR) transaction. The `avr` field is now also available in the [Evaluation requested](https://developers.pismo.io/events/docs/audit-evaluation-requested-1) event, `object.request` field.

  ### Migrations

  #### Docs

  The [Migrate cards](https://developers.pismo.io/pismo-docs/reference/postcardsv1) endpoint documentation was updated to remove incorrect fields within the `migration` object.

  ### Payments

  #### Updated

  The requirements for the following fields in the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) endpoint were impacted and their field descriptions were updated accordingly.

  * `amount`
  * `original_authorization_id`
  * `original_tracking_id`
  * `processing_code`

  This impact occurs if the `mti` is equal to `0202` (confirmation request) or `0402` (confirmation of cancellation request) and the force original authorization is enabled in the payment method configuration or acceptance as follows.

  ```json
  "ORIGINAL_AUTHORIZATION": {  
          "force": true  
        }
  ```

  #### Updated

  The new [Payment methods multiple transfers completed](https://developers.pismo.io/events/docs/payment-methods-multiple-transfers-1) event is now available. It occurs when the Pismo platform completes a multiple transfer process which moves funds between multiple accounts. This event was also added to the [Payment scheduler](https://developers.pismo.io/pismo-docs/docs/payment-scheduler) guide and the [guide](https://developers.pismo.io/pismo-docs/docs/payments-data-events) that lists payments data events.

  #### Docs

  Documentation for the [payments scheduler](https://developers.pismo.io/events/docs/scheduler-payments-scheduled-payments-1) events was updated to remove \[beta] tags, update field descriptions, and remove internal events. Additionally, the [guide](https://developers.pismo.io/pismo-docs/docs/payments-data-events) that lists payments data events was updated with the list of payment scheduler events.

  ### Programs

  #### Docs

  Information about [programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-programs) and [creating programs from a template](https://developers.pismo.io/pismo-docs/docs/add-a-program-from-a-template) in Control Center was reorganized and clarified.

  ### Rates and fees

  The [Fee models](https://developers.pismo.io/pismo-docs/docs/fee-model) guide was reorganized and updated. The “Fee models methods” section was renamed to “Creating a fee model” and updated with additional information. The “Processing codes” section was moved after the “Creating a fee model” section.

  ### Transactions

  #### Updated

  In the [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions) endpoint, if you provide at least one of the following parameters, the `eventDateStart` parameter is now optional.

  * `id`
  * `authorizationId`
  * `authorizationIds`
  * `statementId`
  * `authorizationTrackingId`
  * `numberOfLatestTransactions`

  If you don't provide any of the above parameters, you must include the `eventDateStart` parameter, and the maximum allowed query range is 90 days.

  #### Docs

  Documentation for the [transaction types ](https://developers.pismo.io/events/docs/transaction-types-creation-1) events was corrected to remove duplicate and internal events.

  #### Docs

  The [Transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes) guide was updated for documentation standards.

  ### Support

  #### Docs

  The [Pismo platform sub-processors](https://developers.pismo.io/pismo-docs/docs/pismo-platform-sub-processors) page was updated to include support for AWS Australia.
</summary>

<summary class="tabContent" id="Data and reporting">
  ### Events

  #### New

  The new [Bank statement cycle closing completed](https://developers.pismo.io/events/docs/bank-statements-cycle-closing-1) event is now available. This event indicates that a bank statement cycle closing has been completed for a specific target, such as an organization, program, or division.

  ### Reports

  #### Docs

  The [Regulatory scheduled reports](https://developers.pismo.io/pismo-docs/docs/regulatory-scheduled-reports) guide was updated according to standards.

  #### Docs

  The **Notes** column was added to the table in [Reports for Brazil](https://developers.pismo.io/pismo-docs/docs/brazilian-reports).
</summary>

<summary class="tabContent" id="Core banking">
  ### Banking operations

  #### Updated

  In the [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) endpoint, a new enum value `FIXED` was added to the `withdrawal_fee` object.

  #### Updated

  The `AuthorizationToken` account‑token parameter was removed from the following affected endpoints, as these endpoints support only bearer‑token authentication.

  * [Create overdraft product](https://developers.pismo.io/pismo-docs/reference/post-overdraft-product)
  * [Get overdraft product](https://developers.pismo.io/pismo-docs/reference/get-overdraft-product)
  * [Attach product to account](https://developers.pismo.io/pismo-docs/reference/post-attach-product-to-account)

  #### Docs

  The [Interest-bearing accounts](https://developers.pismo.io/pismo-docs/docs/interest-bearing-accounts) guide was updated to reflect the latest information.

  #### Docs

  The **Prospect creation service** was renamed to **Prospect management service** in the [Banking overview](https://developers.pismo.io/pismo-docs/docs/banking-overview#prospect-management-service) guide to reflect its expanded functionality, which now includes updating and deleting accounts.

  ### Instant payments

  #### New

  The new Instant payments - Pix management > Anti-fraud > [List fraud markers](https://developers.pismo.io/pismo-docs/reference/post-list-fraud-markers) endpoint is now available in beta release.

  #### New

  The following new endpoints are now available in beta release in the Instant payments - Faster Payments (UK) API.

  * [Get FPS transaction](https://developers.pismo.io/pismo-docs/reference/get-fps-in-transaction)
  * [Cancel FPS inbound transaction](https://developers.pismo.io/pismo-docs/reference/post-cancel-fps)
  * [Release FPS inbound transaction](https://developers.pismo.io/pismo-docs/reference/post-release-fps)

  #### Updated

  The new `psp_account` object was added to the [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer) endpoint. This field is required if `transaction_type` = `REFUND`.  It provides information about the Payment Service Provider’s (PSP) account.

  #### Updated

  The new `funds_recovery_id` query parameter was added to the following Instant payments - Pix management endpoints:

  * Infraction reports > [List infraction reports](https://developers.pismo.io/pismo-docs/reference/get-v2-pix-infraction-search)
  * Refunds > [List refunds](https://developers.pismo.io/pismo-docs/reference/get-list-dict-refunds)
  * Infraction reports > [List account infractions](https://developers.pismo.io/pismo-docs/reference/get-v2-pix-account-infractions)

  The same parameter was removed from the [Get infraction report](https://developers.pismo.io/pismo-docs/reference/get-v2-pix-infraction) endpoint.

  #### Docs

  The [Pix Automatic](https://developers.pismo.io/pismo-docs/docs/pix-automatic) guide was updated with more information about journeys, payment orders, and recurrence use cases.

  ### Interest management

  #### Updated

  The `x-program-id` header is no longer required in the [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) endpoint.

  ### Transaction banking

  #### Updated

  The following error code was added to the [List hierarchies](https://developers.pismo.io/pismo-docs/reference/get-hierarchies) endpoint to set a maximum cursor value for results that the endpoint can return.

  * `WCMN0006: Limit must be less than or equal to 100`

  #### Docs

  The following note about processing sequence was added to the [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments) endpoint documentation.

  > Processing sequence: Debit legs are always processed before credit legs. Within each group, the sequence is not guaranteed, and the order of execution among debits or among credits is non‑deterministic.

  #### Docs

  Two balance types were added to [Account balance definitions for transaction banking](https://developers.pismo.io/pismo-docs/docs/account-balance-definitions-for-transaction-banking).

  * Accrued remunerative interest (`remunerative_interest_accrued`): This is the total interest amount that has accrued but has not yet been capitalized.
  * Held checks balance (`held_checks_balance`): This is the balance from checks that the bank considers available but temporarily holds in order to earn interest.
</summary>

<summary class="tabContent" id="Card issuing">
  ### Authorizations

  #### Updated

  The obsolete parameter `use_anti_fraud_api` was removed from the following endpoints.

  * [Create configuration by org](https://developers.pismo.io/pismo-docs/reference/post-config-by-tenant-1)
  * [Get configuration by org](https://developers.pismo.io/pismo-docs/reference/get-config-by-tenant-1)
  * [Update configuration by org](https://developers.pismo.io/pismo-docs/reference/put-config-by-tenant-1)
  * [Create configuration by program](https://developers.pismo.io/pismo-docs/reference/post-config-by-program-1)
  * [Get configuration by program](https://developers.pismo.io/pismo-docs/reference/get-config-by-program-1)
  * [Update configuration by program](https://developers.pismo.io/pismo-docs/reference/put-config-by-program-1)
  * [Create configuration by account](https://developers.pismo.io/pismo-docs/reference/post-config-by-account-1)
  * [Get configuration by account](https://developers.pismo.io/pismo-docs/reference/get-config-by-account-1)
  * [Update configuration by account](https://developers.pismo.io/pismo-docs/reference/put-config-by-account-1)

  ### Network authorizations

  #### Docs

  The [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event was updated to correctly reflect the title for the Token information ID as “Pismo-created token ID”.

  ### Statements

  #### Updated

  The following endpoints that were previously available in beta release are now available in production.

  * [Create installment advancement (v2)](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2)
  * [Get installment advancement (v2)](https://developers.pismo.io/pismo-docs/reference/getinstallmentadvancementv2byid)
  * [Cancel installment advancement (v2)](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentadvancev2)
  * [Close account cycle](https://developers.pismo.io/pismo-docs/reference/cycleclosingrequest)

  #### Updated

  The word “informed” was replaced with “provided” in some of the 4xx error messages for the following endpoints.

  * [Enable additional configurations on accrual types](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesconfigurations)
  * [Disable additional configuration on accrual types](https://developers.pismo.io/pismo-docs/reference/deleteaccrualtypesconfigurations)

  #### Updated

  In the  [List program due dates](https://developers.pismo.io/pismo-docs/reference/getprogramduedates) endpoint, the query parameter `dueDay` was renamed to `day` The original name was incorrect.

  #### Updated

  The following parameters were added to [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters). Note that they are in beta release and are not yet available on the public server.

  * 512 - PAYMENT\_AGREEMENT\_SIMULATION\_INTEREST\_CAP\_ENABLED
  * 513 - PAYMENT\_AGREEMENT\_SIMULATION\_FIRST\_INSTALLMENT\_AS\_DOWNPAYMENT
  * 514 - PAYMENT\_AGREEMENT\_SIMULATION\_ENABLED

  Additionally, the following parameter that was previously missing was now added to the guide.

  * 501 - DELINQUENT\_ACCOUNT\_CLOSURE\_PROCESSING\_CODE

  #### Docs

  The `contract_condition` field was added to the `contracts` array in the body params for [Create installment advancement (V2)](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2). This field was missing in the original documentation. Also, the **REQUIRED** label was removed from the `number_of_installments` field in the `contracts` array. This field is only required if `contract_condition` is set to `SPECIFIC_NUMBER_OF_INSTALLMENTS`.

  #### Docs

  The following guides were updated for standards.

  * [Credit card refinancing](https://developers.pismo.io/pismo-docs/reference/negotiating-credit-card-debt)
  * [Transaction shifts](https://developers.pismo.io/pismo-docs/reference/transaction-shifts)
  * [Full balance credit program](https://developers.pismo.io/pismo-docs/reference/full-balance-credit-program)

  In addition, [Creating and configuring a Full balance credit program](https://developers.pismo.io/pismo-docs/reference/creating-and-configuring-a-full-balance-credit-program) was moved into a separate guide.

  #### Docs

  The body parameters `default_rate` and `rate_if_overdue` in the [Configure program accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates) were incorrectly listed as required. One or the other is required, but not both. The documentation was updated to reflect this.

  #### Docs

  The “transaction category” was renamed to “program transaction category” and their descriptions were updated to avoid confusion with “account transaction category”  in the following endpoints.

  * [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory)
  * [List program transaction categories](https://developers.pismo.io/pismo-docs/reference/listtransactioncategoryinterest)
  * [Update program transaction category](https://developers.pismo.io/pismo-docs/reference/updatetransactioncategoryinterest)

  The “Interest rates” menu section was renamed to “Account transaction categories” and the following endpoints in that section were renamed and their descriptions updated.

  * [Create or update account transaction category](https://developers.pismo.io/pismo-docs/reference/saveaccounttransactioninterest)
  * [Cancel account transaction category](https://developers.pismo.io/pismo-docs/reference/cancelaccounttransactioncategory)

  The text of the following guides was renamed to use “program transaction category” and “program transaction categories”.

  * [Full balance credit program](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program)
  * [Minimum amount due calculation](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation)
  * [Payments configurations](https://developers.pismo.io/pismo-docs/docs/payments-configurations)
  * [Managing the charge order for debit transactions](https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions)
  * [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals)
  * [Configuring accrual rates](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates)
  * [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters)
  * [How payments are applied to accruals](https://developers.pismo.io/pismo-docs/docs/how-payments-are-applied-to-accruals)
  * [Program types](https://developers.pismo.io/pismo-docs/docs/program-types)
  * [Migrations](https://developers.pismo.io/pismo-docs/docs/migrations-overview)
  * [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements)
</summary>

<summary class="tabContent" id="Seller management">
  ### Merchants

  #### Docs

  The [How merchant settlements and installments are processed](https://developers.pismo.io/pismo-docs/docs/how-merchant-settlements-are-processed) guide was updated for standards and clarity.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v2/loans/{loanId}/cancel` (`cancelLoanV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/migrations/cards` (`PostCardsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /payment-methods/v1/authorization` (`post-authorization`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `GET /v2/transactions` (`ListTransactions`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/overdraft` (`post-overdraft-product`) | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--product |
| `GET /v1/overdraft/{productId}` (`get-overdraft-product`) | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--product |
| `POST /v1/overdraft/accounts/{accountId}/attach` (`post-attach-product-to-account`) | `api-specs/Banking_-_Overdraft.yaml` | no | KU-API-banking-overdraft--account |
| `POST /v2/pix/fraud-markers/list` (`post-list-fraud-markers`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--anti-fraud |
| `GET /v1/payments/fps/{endToEndId}` (`get-fps-in-transaction`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/fps/cancel/{endToEndId}` (`post-cancel-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/fps/release/{endToEndId}` (`post-release-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /pix/v1/pix/out/transfer` (`post-pix-out-transfer`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01, KU-API-instant-payments-pix-payments--pix-part-02 |
| `GET /v2/pix/infraction-reports/search` (`get-v2-pix-infraction-search`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01, KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `GET /v2/pix/refunds` (`get-list-dict-refunds`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |
| `GET /v2/pix/infraction-reports` (`get-v2-pix-account-infractions`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01, KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `GET /v2/pix/infraction-reports/{id}` (`get-v2-pix-infraction`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01, KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `POST /v1/interest/plan` (`post-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `GET /corporate/v1/hierarchies` (`get-hierarchies`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--hierarchies |
| `POST /corporate/v3/payments/multileg` (`corporate-v3-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /v2/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancementV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `GET /v2/accounts/{accountId}/installment-advance/{advancementId}` (`GetInstallmentAdvancementV2ById`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}` (`cancelInstallmentAdvanceV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `POST /v1/accounts/{accountId}/statement-close` (`CycleClosingRequest`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--close-account-cycle |
| `POST /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` (`postAccrualTypesConfigurations`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--additional-accrual-type-configurations |
| `DELETE /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` (`deleteAccrualTypesConfigurations`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--additional-accrual-type-configurations |
| `GET /statements-v2/v1/programs/{programId}/due-dates` (`getProgramDueDates`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /v1/programs/{programId}/accrual-type-rates` (`postAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `POST /statements-v2/v1/transactions-categories` (`createTransactionCategory`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `GET /statements-v2/v1/transactions-categories` (`listTransactionCategoryInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` (`updateTransactionCategoryInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` (`saveAccountTransactionInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `DELETE /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId}` (`cancelAccountTransactionCategory`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-config-by-tenant-1` | Authorization configurations; Balance watcher; Create configuration by org; Limit configurations | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `get-config-by-tenant-1` | Get configuration by org | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `put-config-by-tenant-1` | Update configuration by org | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-config-by-program-1` | Create configuration by program | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `get-config-by-program-1` | Get configuration by program | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `put-config-by-program-1` | Update configuration by program | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-config-by-account-1` | Create configuration by account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `get-config-by-account-1` | Get configuration by account; Get limit config by account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `put-config-by-account-1` | Update configuration by account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `negotiating-credit-card-debt` | Credit card refinancing | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `transaction-shifts` | Transaction shifts | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `full-balance-credit-program` | Full balance credit program | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `creating-and-configuring-a-full-balance-credit-program` | Creating and configuring a Full balance credit program | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/6-february-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/6-february-2026 | `87df813788c4da3c…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-overdraft--account` — API reference: Banking - Overdraft — Account
- `KU-API-banking-overdraft--product` — API reference: Banking - Overdraft — Product
- `KU-API-banking-transaction-banking--hierarchies` — API reference: Banking - Transaction banking — Hierarchies
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-pix-management--anti-fraud` — API reference: Instant payments - Pix management — Anti-fraud
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-instant-payments-pix-management--refunds` — API reference: Instant payments - Pix management — Refunds
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-02` — API reference: Instant payments - Pix payments — Pix (part 2 of 2)
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-migrations--card-migration` — API reference: Migrations — Card migration
- `KU-API-revolving-credit-calendar-management--close-account-cycle` — API reference: Revolving credit - Calendar management — Close account cycle
- `KU-API-revolving-credit-configurations--additional-accrual-type-configurations` — API reference: Revolving credit - Configurations — Additional accrual type configurations
- `KU-API-revolving-credit-configurations--program-accrual-rates` — API reference: Revolving credit - Configurations — Program accrual rates
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
