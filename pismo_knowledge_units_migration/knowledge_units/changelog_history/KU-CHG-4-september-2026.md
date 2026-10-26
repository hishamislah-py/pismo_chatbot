---
ku_id: KU-CHG-4-september-2026
title: 'Changelog: 4 September 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/4-september-2026.md
  sha256: 89841fb5a3a18a5e8dcd136d23a12d7393c07bb83125fc59ead0dd000f5f6b24
  url: https://developers.pismo.io/pismo-docs/changelog/4-september-2026
  role: changelog_post
  updated_at: ''
operations:
- CancelInstallmentAdvancement
- CancelInstallmentsAdvanceV2
- CopyProgram
- CopyProgramAsync
- CreateInstallmentAdvancement
- CreateInstallmentAdvancementV2
- CreateProgramBasedOnTemplate
- CreateProgramBasedOnTemplateAsync
- GetAuthorizationConfigByAccount
- GetInstallmentAdvancedSimulationV2
- GetIntallmentAdvancementById
- InstallmentAdvancedV2
- ListTransactions
- PostAuthorizationsV1
- PostTransactionsV1
- SearchTransactionFlows
- SearchTransactionTypes
- SimulateInstallmentAdvancement
- UpdateProgramInfo
- cancel-recurrence-automatic
- cancelAllLoansByAccountV2
- cancelLoanV2
- cash-management-v2-post-cancel-payments
- cash-management-v2-post-confirm-payments
- cash-management-v2-post-payments
- corporate-post-v1-checks
- corporate-v2-post-cancel-payments
- corporate-v2-post-confirm-payments
- corporate-v2-post-payments
- createMarketplace
- createStatementAmountDue
- get-authorization-config-by-tenant
- get-corporate-v1-channels
- get-corporate-v1-channels-channel
- get-corporate-v1-restricted-funds
- get-program-v1
- get-v1-interest-account-b3
- get-v1-interest-plan-b3
- getLoanProductV2
- getLoanProductsV2
- getLoansByAccountIdV2
- getStatementAmountDue
- interest-bearing-get-average-balance
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-create-savings-account-product
- interest-bearing-v1-deposit-account-open
- interest-bearing-v1-deposit-update-account-attachment
- interest-bearing-v1-get-deposit-products
- interest-bearing-v1-list-products
- interest-bearing-v1-patch-deposit-product
- list-corporate-v1-restricted-funds
- list-merchants-advancements
- list-payment-orders
- patch-amend-mandate
- patch-cash-management-v2-earmarks-earmarkid
- patch-corporate-v1-channels-channel
- patch-corporate-v1-restricted-funds
- patch-corporate-v2-earmarks-earmarkid
- post-cancel-mandate
- post-cash-management-v2-earmarks
- post-cash-management-v2-earmarks-earmarkid-cancel
- post-cop-verification
- post-corporate-v1-checks-checkId-cancel
- post-corporate-v1-checks-release
- post-corporate-v1-restricted-funds
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-create-on-us-dispute
- post-v1-accounts-flex-controls
- post-v1-bulletin-setup
- post-v1-filter-templates
- post-v1-interest-account-cancellation
- post-v1-interest-accrual-setup
- post-v1-interest-balance
- post-v1-interest-deposit
- post-v1-interest-plan-b3
- post-v1-interest-withdrawal
- put-v1-filter-template
- put-v1-interest-account-b3
- restructureLoan
- simulateEarlyFinalSettlementV2
- updateProgramParamenter
related_kus:
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--average-balance
- KU-API-banking-interest-bearing-accounts--deposit-account-open
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-engine--interest-accrual
- KU-API-banking-interest-management--account-interest
- KU-API-banking-interest-management--interest-plan
- KU-API-banking-interest-operations--interest-engine
- KU-API-banking-transaction-banking--channels
- KU-API-banking-transaction-banking--check-posting
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--earmarking-pismo-account-id
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--payments-pismo-account-id
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01
- KU-API-card-issuing-authorization-configurations--authorization-configurations-part-02
- KU-API-card-issuing-disputes--on-us
- KU-API-card-issuing-protection-bulletin--rules
- KU-API-core-platform-balance-config-beta--filter-templates
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-transactions--transaction-flows
- KU-API-core-platform-transactions--transaction-types
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-automatic-pix--automatic-pix
- KU-API-instant-payments-automatic-pix--automatic-pix-data
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-API-lending--early-final-settlement
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-migrations--authorization-migration
- KU-API-migrations--transaction-migration
- KU-API-payment-rails-bacs-payments--bacs-direct-debit
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-installment-management--simulations
- KU-API-revolving-credit-statements--advancements
- KU-API-revolving-credit-statements--multivalue-program-parameters
- KU-API-revolving-credit-statements--statement-minimum-amount-due
- KU-API-seller-management-merchant-advance--merchant-advancement
- KU-API-seller-management-sellers--marketplace
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 4 September 2026
coverage_window: 7 August and 4 September 2026
---

# Changelog: 4 September 2026

**KU ID:** `KU-CHG-4-september-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **4 September 2026** (changes between 7 August and 4 September 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated"; "Deprecated"; "Deprecated".

## Topics covered

Core platform - Accounting; Control Center; Card issuing - Disputes; Card issuing - Statements; Flexible transaction controls; Ledger; Migrations; Programs; Support; Transactions; Security; Setup; Events; Banking operations; Instant payments; Payment rails; Instant payments; Transaction banking; Authorization configuration; Card network integration; Cards; Protection Bulletin; Statements; Lending; Marketplace; Merchants; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/4-september-2026

<!-- source:begin path=changelog/4-september-2026.md part=0-end -->

# 4 September 2026

Changes between 7 August and 4 September 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### Core platform - Accounting

  #### Docs

  The [Create accounting scripts](https://developers.pismo.io/pismo-docs/docs/create-an-accounting-script) guide was rewritten to provide more information and payload examples and to explain new features introduced with accounting scripts v2.

  ### Control Center

  #### New

  [Copy configurations](https://developers.pismo.io/pismo-docs/docs/copy-configurations) feature is now available in Control Center. This feature helps you reuse existing configurations across Control Center environments, removing the need to recreate them manually. You can copy configurations between environments to:

  * Promote changes from sandbox to production
  * Keep environments aligned
  * Restore earlier versions when needed

  Copy configurations is currently available for holiday calendars, with support for more features planned.

  ### Card issuing - Disputes

  #### New

  There are new [endpoints](https://developers.pismo.io/pismo-docs/reference/post-create-on-us-dispute) and a [guide](https://developers.pismo.io/pismo-docs/docs/on-us-disputes) to handle on-us disputes. An on-us transaction is a payment, card purchase, or check where the issuing bank (the customer's bank) and the acquiring bank (the merchant's or receiver's bank) are the same financial institution. Because the payment stays inside a single bank, it does not need to go through outside card networks like Visa or Mastercard. Any on-us transaction dispute is resolved within that bank, without the need for card network involvement or extra fees.

  ### Card issuing - Statements

  #### Docs

  A new guide [Discharging transactions—Default process](https://developers.pismo.io/pismo-docs/docs/discharging-transactions-default-process) is now available. This guide explains the default discharge process, which is the only process currently in production. A link to this new guide was added to [Discharging transactions](https://developers.pismo.io/pismo-docs/docs/discharging-transactions).
</summary>

<summary class="tabContent" id="Core platform">
  ### Flexible transaction controls

  #### Updated

  The [Flex controls](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) API was updated in the following ways.

  * New response fields `available_amount` and `available_transactions` are now available in all account and customer flex controls endpoints. These fields track the remaining amount and number of transactions for `cumulative_limit` controls.
  * The list of attributes for conditions was expanded and clarified, specifying which are valid only for card network operations and adding detailed explanations for each. This includes new guidance on using `is_physical_card_present` and `is_token_present` together to distinguish digital wallet transactions.
  * Field descriptions for `max_limit` and `available_limit` were updated to clarify their meaning for different control types (`spending_limit`, `usage_limit`, and `cumulative_limit`).
  * The `reset_datetime` field was removed from the list of request parameters and its description was clarified to indicate that this is a response-only field and to explain how it's calculated.
  * Field descriptions for `currency_code`, `reset_strategy`, `customized`, `max_transactions`, `max_amount` were updated and clarified throughout.

  ### Ledger

  #### Docs

  The [Available ledger balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) event documentation was updated to reflect the correct placement of the  `impact_accounts` field and to clarify its description. This field is deprecated and scheduled to be removed. It is only populated in specific situations when there are associated accounts in the operation.

  ### Migrations

  #### Docs

  In the [Migrate authorizations](https://developers.pismo.io/pismo-docs/reference/postauthorizationsv1) endpoint, `merchant_city`, `merchant_name`, and `merchant_state_or_country` are now defined as optional fields (previously shown as required in error).

  #### Docs

  In the [Migrate transactions](https://developers.pismo.io/pismo-docs/reference/posttransactionsv1) endpoint, "INSTANT PAYMENT" references were removed from the `type` field description.

  #### Docs

  The [Statement organized migration completed](https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1) event can now be emitted after the organize-statement flow runs during a migration. This is useful for historical visibility, reconciliation, and financial validation.

  #### Docs

  The `merchant_state_or_country` field in the [Migrate authorizations](https://developers.pismo.io/pismo-docs/reference/postauthorizationsv1) endpoint was updated to indicate a `string` with `length ≤ 3`, described as "Merchant state or country using ISO 3166-1 alpha-2 or ISO 3166-1 alpha-3 country code," reflecting support for both 2- and 3-letter country codes.

  ### Programs

  #### New

  A new card network brand - `GPN` - was added to the brand parameter for the following endpoints.

  * [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate)
  * [Create program (async)](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplateasync)
  * [Copy program](https://developers.pismo.io/pismo-docs/reference/copyprogram)
  * [Copy program (async)](https://developers.pismo.io/pismo-docs/reference/copyprogramasync)

  #### Updated

  The `holiday_calendar_id` and `cycle_closing` fields were removed from the following “Platform setup - Programs” endpoints.

  * [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate)
  * [Create program (async)](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplateasync)
  * [Copy program](https://developers.pismo.io/pismo-docs/reference/copyprogram)
  * [Copy program (async)](https://developers.pismo.io/pismo-docs/reference/copyprogramasync)
  * [List programs](https://developers.pismo.io/pismo-docs/reference/programs-1)
  * [Get program V2](https://developers.pismo.io/pismo-docs/reference/program-2)
  * [Get program V1](https://developers.pismo.io/pismo-docs/reference/get-program-v1)
  * [Update program](https://developers.pismo.io/pismo-docs/reference/updateprograminfo)

  ### Support

  #### Docs

  The [Confluent event configuration tutorial](https://developers.pismo.io/pismo-docs/docs/confluent-event-config-tutorial) was enhanced in the following ways.

  * Added a Service Desk ticket template for Kafka topic provisioning, bootstrap server information, API key generation, and secure token file setup.
  * Documented Service Desk routing requirements.
  * Reorganized the Confluent event configuration tutorial into a quick-guide format to streamline onboarding and event configuration.

  ### Transactions

  #### Updated

  In the following endpoints, parameters `pageSize` and `pageOffset` were updated and field descriptions on each endpoint were updated accordingly.

  * [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions)
  * [List transactions type](https://developers.pismo.io/pismo-docs/reference/searchtransactiontypes)
  * [List transactions flows](https://developers.pismo.io/pismo-docs/reference/searchtransactionflows)

  `pageSize` is now allowed up to a maximum of 1000 records per page. If the `pageSize` parameter is not passed, the platform continues to consider `pageSize` = `100` as the default.

  `pageOffset` is now allowed up to a maximum of 5000 records per page. If the `pageOffset` parameter is not passed, the platform continues to consider `pageOffset` = `0` as the default.

  #### Docs

  In the [Transactions overview](https://developers.pismo.io/pismo-docs/docs/transactions-overview)  guide, the note about installment purchases was updated to clarify that this payment method is available for transactions only within Brazil.

  ### Security

  #### Updated

  The webhook lookup URL for retrieving public keys was updated in the [Verifying webhook requests](https://developers.pismo.io/pismo-docs/docs/verifying-webhook-requests#retrieving-a-list-of-public-keys) guide. You must use this updated URL to retrieve the current list of public keys from our JSON Web Key Set (JWKS) endpoint at the time of verification of the webhook requests sent by the Pismo platform. This ensures that your system always uses the correct key, even when scheduled rotation of the cryptographic keys used to sign webhook request tokens occur.   

  ### Setup

  #### Updated

  In the [Update filter template](https://developers.pismo.io/pismo-docs/reference/put-v1-filter-template) endpoint, the 204 response was changed to 200 response that returns the updated filter template.

  #### Docs

  The URL paths in the [balance configuration filter template](https://developers.pismo.io/pismo-docs/reference/post-v1-filter-templates) endpoints were corrected (`/balances-configs/` replaced with `/balances-config/`).
</summary>

<summary class="tabContent" id="Data">
  ### Events

  #### New

  The following new events that feature a required `external_account_id` are available in beta release.

  * [Account balance changed](https://developers.pismo.io/events/docs/apex-change-available-1)
  * [Accounting entry created](https://developers.pismo.io/events/docs/apex-entry-creation-1)
  * [Platform authorization created](https://developers.pismo.io/events/docs/apex-platform-authorization-1)
  * [Transaction created](https://developers.pismo.io/events/docs/apex-transaction-creation-1)
  * [Transaction updated](https://developers.pismo.io/events/docs/apex-transaction-update-1)

  #### Docs

  The **Corporate account created** event that was incorrectly documented in the **Core platform > Accounts** section was removed from documentation. In the [Banking - Transaction banking](https://developers.pismo.io/pismo-docs/docs/corporate-banking-data-events) guide, a reference to this non-existent event was updated to point to the correct [Corporate account created](https://developers.pismo.io/events/docs/corporate-corporate-account-creation-1) event.
</summary>

<summary class="tabContent" id="Core banking">
  ### Banking operations

  #### Updated

  The `grace_period_duration_days` and `accrue_during_grace_period` fields were added to the following endpoints. These two fields introduce the product‑level setting that determines whether interest accrual continues during the post‑maturity grace period.

  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products)
  * [Update deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-patch-deposit-product)

  #### Updated

  In the [Update deposit account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment) endpoint, the `maturity_period` object was added to the `deposit_configs` object. This field enables immediate term recalculation through `maturity_period`, updating the current cycle’s maturity date from a relative period or explicit date.

  #### Updated

  The `external_account_id` field was added to the 200 response for the following endpoints.

  * [Cancel account](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-account-cancellation)
  * [Create balance](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-balance)
  * [Deposit money](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-deposit)
  * [Withdraw money](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-withdrawal)
  * [Get average balance](https://developers.pismo.io/pismo-docs/reference/interest-bearing-get-average-balance)
    The string length for `external_account_id` was corrected and changed from 64 to 60 characters. This affects all the endpoints mentioned above in both their response and (when applicable) their request.

  #### Updated

  The `accrual_model` field was added to the 200 response for the [Get average balance](https://developers.pismo.io/pismo-docs/reference/interest-bearing-get-average-balance) and [Create savings account product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-savings-account-product) endpoints.

  #### Updated

  In the [Configure timing for accrual calculation](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-accrual-setup) endpoint, an additional time, `04:05`, was added to the list of times that are accepted by the `time_utc` field.

  #### Updated

  The incorrect and missing error codes were corrected in the [Open deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-account-open) endpoint. The following error codes were incorrect and were updated.

  400 errors:

  * `EIBACC0321` was updated to `EIBACC0330: Corporate API validation error` and a details‑field example was added showing that the underlying `WCAC` error code already appears there.
  * `EIBACC0407` was updated to `EIBACC0331: Provided account_id does not match the resolved external_account_id`.

  504 error:

  * `EIBACC0318` was updated to `EIBACC0329`.

  The following 400 errors were added to provide more details.

  * `EIBACC0018: Accounts API - Request returned error 4xx`
  * `EIBACC0065: Product Type is not valid`
  * `EIBACC0103: Programs API - Request returned error 4xx`
  * `EIBACC0107: Informed program or account already has an attached product`
  * `EIBACC0109: Maturity period is below the configured MinTerm of the product`
  * `EIBACC0110: Maturity period is above the configured MaxTerm of the product`
  * `EIBACC0236: Product cannot be attached before its start date`
  * `EIBACC0284: Payout account is configured but is invalid`
  * `EIBACC0298: Validation error` (details: Invalid `maturity_period` unit. Supported values: `DAYS`, `WEEKS`, `MONTHS`, `YEARS`)
  * `EIBACC0299: Validation error` (details: `maturity_period` value must be a positive integer (>= 1))
  * `EIBACC0303: New attachments are not allowed after the deposit product end_date`
  * `EIBACC0305: Validation error` (details: `calendar_maturity_date` must be in `YYYY-MM-DD` format)
  * `EIBACC0306: Validation error` (details: `calendar_maturity_date` must be a future date (after today))
  * `EIBACC0307: Validation error` (details: `maturity_period` accepts either `calendar_maturity_date` OR `unit` + \`value, not both)
  * `EIBACC0308: valid_until must be a future datetime`
  * `EIBACC0319: Effective date exceeds maximum backdating limit`
  * `EIBACC0320: Invalid effective date format. Expected YYYY-MM-DD`
  * `EIBACC0321: Effective date cannot be in the future`

  The following 422 errors were added:

  * `EIBACC0191: Account status is not NORMAL and it is unprocessable`
  * `EIBACC0297: Program is not valid for attachment. Program must be DEBIT type and ACTIVE status`

  Two missing 500‑level errors were added:

  * `EIBACC0328 : Corporate API request error`
  * `EIBACC0324 : Failed to unmarshal Corporate API response`

  #### Updated

  Interest bearing accounts now support two accrual models for submitting data to the interest engine.

  * `DEPOSIT_BASIS` uses the balance change model, where interest is computed from movement‑level changes and remains the default.
  * `BALANCE_BASIS` uses the closing balance model, submitting the account’s closing balance on each cycle\_closing event. Under balance basis, `balance_type` determines which balance is submitted:
  * `VALUE_DATED_BALANCE` provides the cleared, value‑dated balance (default)
  * `LEDGER_BALANCE` provides the raw ledger balance

  This update impacts the following endpoints.

  * [List products](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-list-products)
  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products)

  ### Instant payments

  #### Updated

  The `interval` and `type` parameters were removed from the List scheduled Pix transfers endpoint.

  #### Updated

  A new `sort_code_validation` object was added to the response from the [Confirmation of payee](https://developers.pismo.io/pismo-docs/reference/post-cop-verification) endpoint. This object returns the results of sort code and account validation.

  #### Updated

  A response object with 3 fields was added to the 200 return from the Pix Automatic’s [Cancel recurrence](https://developers.pismo.io/pismo-docs/reference/cancel-recurrence-automatic) endpoint. For example:

  ```json
  {
    "recurrence_id": "RN2199525620260901XIQf6272qzA",
    "reason_code": "SLDB",
    "cancelled_at": "2026-09-01T20:25:14.402Z"
  }
  ```

  ### Payment rails

  #### New

  The Payment rails - BACS payments API was reorganized into two sections - BACS direct credit and BACS direct debit. In addition, two new endpoints were added - [Amend BACS paper mandate](https://developers.pismo.io/pismo-docs/reference/patch-amend-mandate) and [Cancel BACS paper mandate](https://developers.pismo.io/pismo-docs/reference/post-cancel-mandate). A BACS paper mandate is a physical, signed authorization form that allows a UK organization to pull recurring or single direct debit payments directly from a customer's bank account.

  ### Instant payments

  #### Updated

  A `type` field was added to the response from the [List payment orders](https://developers.pismo.io/pismo-docs/reference/list-payment-orders) endpoint. This enum field identifies the payment order’s type.

  ### Transaction banking

  #### New

  The following new channel endpoints are now available.

  * [Get channel](https://developers.pismo.io/pismo-docs/reference/get-corporate-v1-channels-channel)
  * [Update channel](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v1-channels-channel)
  * [List channels](https://developers.pismo.io/pismo-docs/reference/get-corporate-v1-channels)

  #### Updated

  A new 400 error `WCPT0018: Account has not finished onboarding` was added to the following endpoints. This error is returned when a client attempts to create, release, or cancel a check while the external account is still undergoing onboarding.

  * [Create check posting](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-checks)
  * [Release check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-release)
  * [Cancel check](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-checks-checkid-cancel)

  #### Updated

  New fields `type` and `increase_datetime_limit` were added to the following endpoints, enabling regulatory and judicial reasons to be used when calling fund restriction endpoints.

  * [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds)
  * [List fund restrictions](https://developers.pismo.io/pismo-docs/reference/list-corporate-v1-restricted-funds)
  * [Get fund restriction](https://developers.pismo.io/pismo-docs/reference/get-corporate-v1-restricted-funds)
  * [Release restriction](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v1-restricted-funds)

  #### Updated

  A new hold method, `RECURRENT`, is introduced to the following endpoints, applying the restriction to each incoming credit until the target amount is reached or the `increase_datetime_limit` occurs.

  * [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds)
  * [List fund restrictions](https://developers.pismo.io/pismo-docs/reference/list-corporate-v1-restricted-funds)
  * [Get fund restriction](https://developers.pismo.io/pismo-docs/reference/get-corporate-v1-restricted-funds)

  #### Updated

  A 423 Locked error message, `Earmark locked by a concurrent operation`, was added to the following endpoints. This error is returned when another earmark or payment operation is already in progress.

  * [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
  * [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
  * [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)
  * [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
  * [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments)
  * [Cancel payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-cancel-payments)
  * [Post payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-payments)
  * [Confirm payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-confirm-payments)
  * [Cancel payment (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/cash-management-v2-post-cancel-payments)
  * [Create earmark (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/post-cash-management-v2-earmarks)
  * [Update earmark (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/patch-cash-management-v2-earmarks-earmarkid)
  * [Cancel earmark (Pismo account ID)](https://developers.pismo.io/pismo-docs/reference/post-cash-management-v2-earmarks-earmarkid-cancel)

  #### Deprecated

  The following endpoints were decommissioned on 6 August 2026 and removed from the Transaction banking API.

  * **Post float cash-in (Pismo account ID)**
  * **Settle float payment**
</summary>

<summary class="tabContent" id="Card issuing">
  ### Authorization configuration

  #### Docs

  The [Get authorization by organization](https://developers.pismo.io/pismo-docs/reference/get-authorization-config-by-tenant) and [Get authorization by account](https://developers.pismo.io/pismo-docs/reference/getauthorizationconfigbyaccount) endpoints are both now back on the Developers Portal after being mistakenly removed.

  ### Card network integration

  #### Updated

  The `network` field of the [Card network authorization return sent](https://developers.pismo.io/events/docs/networktransactions-network-message-1) event was updated to properly list the valid network options: `mastercard`, `visa`, `visa_vcc`, `tecban`, `rupay`, and `elo`.

  #### Docs

  The [Visa Consumer Authentication Service (VCAS)](https://developers.pismo.io/pismo-docs/docs/visa-consumer-authentication-service-vcas) guide was updated to properly distinguish the one-time password (OTP) as one option of the overall Step-up validation.

  #### Docs

  The Verify authorization decline reason for Zero balance transaction definition in the [Validation code definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions) guide was updated to reflect the correct field name as `custom_response_code` and not `CustomCode` as previously listed.

  ### Cards

  #### Deprecated

  The deprecated **Create combo card** endpoint was officially removed from the Developers Portal. An entry for the endpoint has been added to the [API endpoints removed](https://developers.pismo.io/pismo-docs/reference/api-endpoints-removed) page.

  ### Protection Bulletin

  The `bid` field used in [creating a Protection Bulletin rule](https://developers.pismo.io/pismo-docs/reference/post-v1-bulletin-setup) for Visa has had its length extended from 6 digits to 11 digits. The Business ID (BID) number - is a six to 11 digit account number through which Visa bills their clients.

  ### Statements

  #### Updated

  The following fields were added to the [Simulate installment advancement](https://developers.pismo.io/pismo-docs/reference/simulateinstallmentadvancement) endpoint.

  * `authorization_id` field in the response object
  * `id` field in the `installments` array in the response object
  * `interest_removal_end_date` field in body parameters and response object

  The `interest_removal_end_date` field was added to body parameters of the [Create installment advancement](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2).

  #### Docs

  A list of restrictions was added to the [Canceling an installment advancement](https://developers.pismo.io/pismo-docs/docs/installment-advancements-guide#canceling-an-installment-advancement) section of the Installment advancements guide.

  #### Docs

  A link to [Update multivalue program parameter values](https://developers.pismo.io/pismo-docs/reference/updateprogramparamenter) was added to the first paragraph of [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters).

  #### Docs

  In the [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements) guide, the following updates were made.

  * The “Statement management” callout at the end of the “Balances” section was deleted. It was replaced by the "Statement management" section near the beginning of the guide.
  * The “Accrual management” callout at the end of the “Accruals” section was deleted. It was replaced by the "Accrual management" section within the “Accruals” section. The new section provides a few more details than the callout.

  #### Docs

  In the first sentence of the [Credit card refinancing](https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt) guide, the word “payments” was changed to “billing periods”, which is more accurate. The following sentence was added to the end of the introductory section to clarify the purpose of the included figure: “If necessary, refer back to this figure when reading the guides linked to in the following sections.”

  #### Docs

  The field descriptions for `fixed_interest_rate`, `margin`, and `margin_rate` were updated in the following endpoints.

  * [Create interest plan (B3 only)](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan-b3)
  * [Get interest plan (B3 only)](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan-b3)
  * [Get account interest (B3 only)](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account-b3)
  * [Update account interest (B3 only)](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account-b3)

  #### Deprecated

  The following installment advancement endpoints are now deprecated.

  * [Create installment advancement (deprecated)](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancement)
  * [Create installment advancement (no cancellation event) (deprecated)](https://developers.pismo.io/pismo-docs/reference/installmentadvancedv2)
  * [Get installment advancement (deprecated)](https://developers.pismo.io/pismo-docs/reference/getintallmentadvancementbyid)
  * [Cancel installment advancement (deprecated)](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentadvancement)
  * [Cancel installments advancement (no cancellation event) (deprecated)](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentsadvancev2)
  * [Get simulation installment advancement (deprecated)](https://developers.pismo.io/pismo-docs/reference/getinstallmentadvancedsimulationv2)

  The [API endpoint deprecation and removal schedule](https://developers.pismo.io/pismo-docs/docs/api-endpoint-deprecation-and-removal-schedule) was updated accordingly.

  #### Docs

  The following updates were made for clarification.

  * [Create or update statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/createstatementamountdue): Updated the endpoint description and the field descriptions for `amount_type` and `minimum_amount_due` in the body parameters.
  * [Get statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/getstatementamountdue): Updated the field descriptions for `amount_type` and `minimum_amount_due` in the response.

  #### Docs

  The description for the `DELINQUENT_ACCOUNT_CLOSURE_DAYS` program parameter was updated in the [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters) guide.

  #### Docs

  The descriptions for the minimum payment calculation methods were clarified in the table in section [Minimum amount due calculation](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#mad-calculation-strategy).

  #### Docs

  The section header was renamed from “Full-amount transactions” to [Setting the transaction in a category to full-amount](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#setting-the-transactions-in-a-category-to-full-amount) and the text was updated for clarity.

  #### Docs

  The [Strategy 2 examples](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#strategy-2-examples) section was updated to correct some inaccuracies.
</summary>

<summary class="tabContent" id="Lending">
  ### Lending

  #### New

  The new [Cancel all loans by account](https://developers.pismo.io/pismo-docs/reference/cancelallloansbyaccountv2) endpoint is now available.

  #### Updated

  The [Simulate early final settlement](https://developers.pismo.io/pismo-docs/reference/simulateearlyfinalsettlementv2) endpoint was updated to remove the `Idempotency-Key` header.

  #### Updated

  The [Restructure a loan](https://developers.pismo.io/pismo-docs/reference/restructureloan) endpoint returns an asynchronous `tracking_id`, not a new `loan_id`, so the endpoint response body was updated accordingly.

  #### Updated

  The [List account loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2) endpoint now shows disbursement details for a loan that has MULTIPLE disbursements that include the following fields.

  * `can_disburse_more`—On a `MULTIPLE` disbursement loan, is the remaining amount to be disbursed greater than zero?
  * `remaining_to_disburse_amount`—On a `MULTIPLE` disbursement loan, the amount that remains to be disbursed. Calculated as `loan_principal_amount` minus `total_disbursed_amount`.
  * `total_disbursed_amount`—On a `MULTIPLE` disbursement loan, sum of all active disbursements, excluding any that are `CANCELED` or `EXPIRED`.

  #### Updated

  The [Cancel loan](https://developers.pismo.io/pismo-docs/reference/cancelloanv2) endpoint now shows `canceled_loans` and  `total_to_be_canceled` with summary information about the canceled loan or loans.

  #### Updated

  The [List account loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2) endpoint now shows `insurance_summary` information. When you set the `includeInsuranceHistory=true` query parameter, each insured installment in `repayment_schedule` includes an `insurance_premium_state` field, and the response includes loan-level `insurance_summary` for loans that have an insurance policy. Also the response includes cancelled insurance and its installments. (The field is omitted entirely for uninsured loans.) The `insurance_summary` includes the following information:

  * `insurance_ever_active`—Was insurance ever collected in the history of the loan?
  * `last_covered_date`—End of insurance coverage period, either the last installment due date or the insurance cancelation date for a canceled policy.

  #### Docs

  The [Lending prepayment or group payment created](https://developers.pismo.io/events/docs/lending-lending-prepayment-v2-creation-1) event was updated to indicate that the event is sent when a lending prepayment or group payment has been created. Previously the event indicated only “Lending prepayment created” in the title.

  #### Docs

  Multiple [Lending](https://developers.pismo.io/pismo-docs/reference/getloanproductv2) API request fields, headers, path parameters, and query parameters were updated with better descriptions of the meaning of the field.

  * `Idempotency-Key` headers
  * `loanId` path parameter
  * `accountId` path parameter and query parameter
  * `loan_id`
  * `loan_start_date`
  * `account_id`
  * `account_type`
  * `sortOrder` query parameter for [List loan products](https://developers.pismo.io/pismo-docs/reference/getloanproductsv2)
</summary>

<summary class="tabContent" id="Seller management">
  ### Marketplace

  #### Docs

  The `additional_phone_number` field description in the [Create marketplace V3](https://developers.pismo.io/pismo-docs/reference/createmarketplace) endpoint was updated to include that the additional phone number value should be of the E.164 format, which includes a max length of 15 characters.

  ### Merchants

  #### New

  The [List merchant advancement requests](https://developers.pismo.io/pismo-docs/reference/list-merchants-advancements) endpoint was moved from `/v1/merchants/{merchantId}/advancements` to `/v2/merchants/{merchantId}/advancements`. This avoids a routing collision with the still-active legacy /v1 endpoint served by the Merchants API, letting both versions run side-by-side during the migration window.
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### New

  The new [pending transactions](https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc#account-views) feature was added to Control Center. You can now view the list of pending transactions for an account and explore individual pending transactions in more detail.

  #### Updated

  The [audit](https://developers.pismo.io/pismo-docs/docs/view-user-activity-audit) feature in Control Center now supports exporting the audit logs. The guide was also updated to align with Pismo documentation and style standards.

  #### Updated

  The [transactions](https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc#account-views) feature was updated in Control Center. You can now view the list of pending transactions for an account and explore individual pending transactions in more detail.

  #### Updated

  The [Control Center Loan products](https://developers.pismo.io/pismo-docs/docs/loan-products-cc) and [Create loan products](https://developers.pismo.io/pismo-docs/docs/create-loan-products) guides were updated to:

  * Reflect support for creating both personal loans and Buy Now, Pay Later (BNPL) loans in Control Center. Previously, Control Center supported only BNPL loan creation.
  * Add more detailed information about creating processing codes, a prerequisite for creating loan products.

  #### Updated

  The Dual approval feature was transitioned from beta to full release. The following guides were also updated to reflect this.

  * [Users](https://developers.pismo.io/pismo-docs/docs/users)
  * [Security guide for Control Center](https://developers.pismo.io/pismo-docs/docs/security-guide-for-control-center)
  * [Edit programs](https://developers.pismo.io/pismo-docs/docs/cc-manage-program-details-and-parameters)
  * [Account actions](https://developers.pismo.io/pismo-docs/docs/account-actions)
  * [Card information](https://developers.pismo.io/pismo-docs/docs/card-information)
  * [Access keys](https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication)
  * [OpenID Connect](https://developers.pismo.io/pismo-docs/docs/openid-configurations)
  * [Manage loans in Control Center](https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center)

  In addition, the dual approval feature in Control Center was updated. You can now request Pismo to enable dual approval for issuing a refund.

  #### Docs

  The Control Center [Holidays](https://developers.pismo.io/pismo-docs/docs/holidays) guide was updated to align with Pismo documentation and style standards.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/on-us-dispute` (`post-create-on-us-dispute`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--on-us |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/migrations/authorizations` (`PostAuthorizationsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--authorization-migration |
| `POST /v1/migrations/transactions` (`PostTransactionsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--transaction-migration |
| `POST /programs/v1/programs/template` (`CreateProgramBasedOnTemplate`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v2/programs/template` (`CreateProgramBasedOnTemplateAsync`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v1/programs/copy` (`CopyProgram`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v2/programs/copy` (`CopyProgramAsync`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `GET /programs/v1/programs/{id}` (`get-program-v1`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `PATCH /programs/v1/programs/{id}` (`UpdateProgramInfo`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `GET /v2/transactions` (`ListTransactions`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `GET /v1/transaction-types` (`SearchTransactionTypes`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `GET /v1/transaction-flow` (`SearchTransactionFlows`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `PUT /v1/balances-config/filter-templates/{id}` (`put-v1-filter-template`) | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `POST /v1/balances-config/filter-templates` (`post-v1-filter-templates`) | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/deposits/{productId}` (`interest-bearing-v1-get-deposit-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `PATCH /v1/deposits/{productId}` (`interest-bearing-v1-patch-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `PATCH /v1/deposits/accounts/{accountId}/attachment` (`interest-bearing-v1-deposit-update-account-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/interest/account/cancellation` (`post-v1-interest-account-cancellation`) | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `POST /v1/interest/balance` (`post-v1-interest-balance`) | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `POST /v1/interest/deposit` (`post-v1-interest-deposit`) | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `POST /v1/interest/withdrawal` (`post-v1-interest-withdrawal`) | `api-specs/Banking_-_Interest_operations.yaml` | no | KU-API-banking-interest-operations--interest-engine |
| `GET /v1/accounts/{accountId}/average-balance` (`interest-bearing-get-average-balance`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--average-balance |
| `POST /v1/savings-accounts` (`interest-bearing-v1-create-savings-account-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/interest/accrual/setup` (`post-v1-interest-accrual-setup`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-accrual |
| `POST /v1/deposits/accounts/open` (`interest-bearing-v1-deposit-account-open`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--deposit-account-open |
| `GET /v1/products` (`interest-bearing-v1-list-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/payments/fps/cop` (`post-cop-verification`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /inst-pull-pay/v1/pix/automatic/cancel` (`cancel-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `PATCH /v1/payments/bacs/directdebit/mandates/{id}` (`patch-amend-mandate`) | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-debit |
| `POST /v1/payments/bacs/directdebit/mandates/{id}/cancel` (`post-cancel-mandate`) | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-debit |
| `GET /inst-pull-pay/v1/pix/automatic/payment/order` (`list-payment-orders`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix-data |
| `GET /corporate/v1/channels/{channel}` (`get-corporate-v1-channels-channel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--channels |
| `PATCH /corporate/v1/channels/{channel}` (`patch-corporate-v1-channels-channel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--channels |
| `GET /corporate/v1/channels` (`get-corporate-v1-channels`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--channels |
| `POST /corporate/v1/checks` (`corporate-post-v1-checks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/release` (`post-corporate-v1-checks-release`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/checks/{checkId}/cancel` (`post-corporate-v1-checks-checkId-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--check-posting |
| `POST /corporate/v1/restricted-funds` (`post-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v1/restricted-funds` (`list-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `GET /corporate/v1/restricted-funds/{restrictedFundsId}` (`get-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` (`patch-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/confirm` (`corporate-v2-post-confirm-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/cancel` (`corporate-v2-post-cancel-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /cash-management/v2/payments` (`cash-management-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `POST /cash-management/v2/payments/confirm` (`cash-management-v2-post-confirm-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `POST /cash-management/v2/payments/cancel` (`cash-management-v2-post-cancel-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-pismo-account-id |
| `POST /cash-management/v2/earmarks` (`post-cash-management-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `PATCH /cash-management/v2/earmarks/{earmarkId}` (`patch-cash-management-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `POST /cash-management/v2/earmarks/{earmarkId}/cancel` (`post-cash-management-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-pismo-account-id |
| `GET /v1/config` (`get-authorization-config-by-tenant`) | `api-specs/Card_issuing_-_Authorization_configurations.yaml` | no | KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01, KU-API-card-issuing-authorization-configurations--authorization-configurations-part-02 |
| `GET /v1/config/account/{accountId}` (`GetAuthorizationConfigByAccount`) | `api-specs/Card_issuing_-_Authorization_configurations.yaml` | no | KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01, KU-API-card-issuing-authorization-configurations--authorization-configurations-part-02 |
| `POST /v1/bulletin/setup` (`post-v1-bulletin-setup`) | `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | no | KU-API-card-issuing-protection-bulletin--rules |
| `GET /v1/accounts/{accountId}/installment-advance/simulations` (`SimulateInstallmentAdvancement`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--simulations |
| `POST /v2/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancementV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}` (`updateProgramParamenter`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--multivalue-program-parameters |
| `POST /v1/interest/plan` (`post-v1-interest-plan-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--interest-plan |
| `GET /v1/interest/plan/{interestPlanId}` (`get-v1-interest-plan-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--interest-plan |
| `GET /v1/interest/account/{accountId}` (`get-v1-interest-account-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--account-interest |
| `PUT /v1/interest/account/{accountId}` (`put-v1-interest-account-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--account-interest |
| `POST /v1/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancement`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | **yes** | KU-API-revolving-credit-installment-management--installment-advancements |
| `POST /statements/v2/accounts/{accountId}/installment-advance` (`InstallmentAdvancedV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `GET /v1/accounts/{accountId}/installment-advance/{advancementId}` (`GetIntallmentAdvancementById`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | **yes** | KU-API-revolving-credit-installment-management--installment-advancements |
| `DELETE /v1/accounts/{accountId}/installment-advance/{advancementId}` (`CancelInstallmentAdvancement`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | **yes** | KU-API-revolving-credit-installment-management--installment-advancements |
| `DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}` (`CancelInstallmentsAdvanceV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `GET /statements/v2/accounts/{accountId}/installment-advance` (`GetInstallmentAdvancedSimulationV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due` (`createStatementAmountDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |
| `GET /statements-v2/v1/accounts/{accountId}/minimum-amount-due` (`getStatementAmountDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |
| `POST /v2/accounts/{accountId}/loans/cancel` (`cancelAllLoansByAccountV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{loanId}/early-settlement/simulate` (`simulateEarlyFinalSettlementV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--early-final-settlement |
| `POST /v2/loans/{originalLoanId}/restructure` (`restructureLoan`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/accounts/{accountId}/loans` (`getLoansByAccountIdV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans/{loanId}/cancel` (`cancelLoanV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/loan-products/{productId}` (`getLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /v2/loan-products` (`getLoanProductsV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v3/marketplaces` (`createMarketplace`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace |
| `GET /v2/merchants/{merchantId}/advancements` (`list-merchants-advancements`) | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `programs-1` | List programs; Programs API | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `program-2` | Get program V2 | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `api-endpoints-removed` | API endpoints removed | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/4-september-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/4-september-2026 | `89841fb5a3a18a5e…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--average-balance` — API reference: Banking - Interest-bearing accounts — Average balance
- `KU-API-banking-interest-bearing-accounts--deposit-account-open` — API reference: Banking - Interest-bearing accounts — Deposit account open
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-engine--interest-accrual` — API reference: Banking - Interest engine — Interest accrual
- `KU-API-banking-interest-management--account-interest` — API reference: Banking - Interest management for B3-listed products — Account interest
- `KU-API-banking-interest-management--interest-plan` — API reference: Banking - Interest management for B3-listed products — Interest plan
- `KU-API-banking-interest-operations--interest-engine` — API reference: Banking - Interest operations — Interest engine
- `KU-API-banking-transaction-banking--channels` — API reference: Banking - Transaction banking — Channels
- `KU-API-banking-transaction-banking--check-posting` — API reference: Banking - Transaction banking — Check posting
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--earmarking-pismo-account-id` — API reference: Banking - Transaction banking — Earmarking (Pismo account ID)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--payments-pismo-account-id` — API reference: Banking - Transaction banking — Payments (Pismo account ID)
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01` — API reference: Card issuing - Authorization configurations — Authorization configurations (part 1 of 2)
- `KU-API-card-issuing-authorization-configurations--authorization-configurations-part-02` — API reference: Card issuing - Authorization configurations — Authorization configurations (part 2 of 2)
- `KU-API-card-issuing-disputes--on-us` — API reference: Card issuing - Disputes — On-Us
- `KU-API-card-issuing-protection-bulletin--rules` — API reference: Card issuing - Protection Bulletin — Rules
- `KU-API-core-platform-balance-config-beta--filter-templates` — API reference: Core platform - Balance configurations — Filter templates
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-automatic-pix--automatic-pix` — API reference: Instant payments - Automatic Pix — Automatic Pix
- `KU-API-instant-payments-automatic-pix--automatic-pix-data` — API reference: Instant payments - Automatic Pix — Automatic Pix data
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-API-lending--early-final-settlement` — API reference: Lending — Early final settlement
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-migrations--authorization-migration` — API reference: Migrations — Authorization migration
- `KU-API-migrations--transaction-migration` — API reference: Migrations — Transaction migration
- `KU-API-payment-rails-bacs-payments--bacs-direct-debit` — API reference: Payment rails - BACS payments — BACS direct debit
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-installment-management--simulations` — API reference: Revolving credit - Installment management — Simulations
- `KU-API-revolving-credit-statements--advancements` — API reference: Revolving credit - Statements — Advancements
- `KU-API-revolving-credit-statements--multivalue-program-parameters` — API reference: Revolving credit - Statements — Multivalue program parameters
- `KU-API-revolving-credit-statements--statement-minimum-amount-due` — API reference: Revolving credit - Statements — Statement minimum amount due
- `KU-API-seller-management-merchant-advance--merchant-advancement` — API reference: Seller management - Merchant advancements — Merchant advancement
- `KU-API-seller-management-sellers--marketplace` — API reference: Seller management - Sellers — Marketplace
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
