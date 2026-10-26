---
ku_id: KU-CHG-5-june-2026
title: 'Changelog: 5 June 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/5-june-2026.md
  sha256: 5b46a69cf6487e092285caeefd737257192020ca7d3af8878e8cf83d6002de79
  url: https://developers.pismo.io/pismo-docs/changelog/5-june-2026
  role: changelog_post
  updated_at: ''
operations:
- CancelInstallmentsAdvanceV2
- CreateAccountingEntry
- GetInstallmentAdvancedSimulationV2
- GetInstallmentAdvancementV2ById
- GetInstallmentsAdvanceV2
- InstallmentAdvancedV2
- PostBalanceControlV1
- PostPciCardsV1
- UpdateProgramInfo
- cancelInstallmentAdvanceV2
- create-payment-agreement-simulation
- create-reissue-reason
- createLoanAdjustmentV2
- createLoanProductV2
- createPrepayment
- get-account-balances
- get-accounts
- get-accounts-v1-accounts
- get-reissue-reasons
- get-v1-card-reissue-reasons
- getLoanProductV2
- getLoanProductsV2
- getMerchantTransactionV2
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-update-payout-account
- interest-bearing-v1-get-account-attachment
- interest-bearing-v1-get-deposit-products
- interest-bearing-v1-savings-account-update-payout-account
- interest-bearing-v1-simulate-penalty
- list-recurrence-automatic
- patch-v1-orgs
- post-authorization
- post-cop-verification
- post-create-fps
- post-create-holiday-calendar
- post-passport-v1-oauth2-token
- post-recurrence-automatic
- post-return-fps
- post-reversal-bacs
- post-run-visa-device-lifecycle
- post-v1-accounts-flex-controls
- post-v1-disputes-fraud-report
- put-v1-disputes-fraud-report
- registerPrepaymentSimulationV2
- registerRepaymentV2
- resend-automatic-pix-payment-order
- update-reissue-reason
- update-scheduled-charge
- updateLoanProductV2
related_kus:
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--penalty
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-disputes--supporting-forms
- KU-API-card-issuing-tokenization--token-lifecycle
- KU-API-core-platform-accounting--accounting-entry
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-instant-payments-automatic-pix--automatic-pix
- KU-API-instant-payments-automatic-pix--automatic-pix-data
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-lending--prepayment
- KU-API-lending--repayments
- KU-API-migrations--balance-migration
- KU-API-migrations--card-migration
- KU-API-payment-rails-bacs-payments--bacs-direct-credit
- KU-API-platform-authentication--authentication
- KU-API-platform-setup-holidays--holiday-calendar
- KU-API-platform-setup-organizations--orgs
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges
- KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation
- KU-API-revolving-credit-statements--advancements
- KU-API-seller-management-merchants--merchant-transaction
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 5 June 2026
coverage_window: 1 May and 5 June 2026
---

# Changelog: 5 June 2026

**KU ID:** `KU-CHG-5-june-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **5 June 2026** (changes between 1 May and 5 June 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated".

## Topics covered

General; Control Center; Core banking; Instant payments; Accounting; Accounts; Authentication; Client webhooks; Flex controls; General; Migrations; Payments; Programs; Rates and fees; Security; Setup; Support; Events; Banking operations; Instant payments; Payment rails; Transaction banking; Card network integration; Cards; Cards on file; Disputes; Statements; Tokenization; Lending; Merchants; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/5-june-2026

<!-- source:begin path=changelog/5-june-2026.md part=0-end -->

# 5 June 2026

Changes between 1 May and 5 June 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### General

  #### New

  An [llms.txt](https://developers.pismo.io/llms.txt) file was added to the Pismo Developers Portal to help large language models (LLMs) parse and understand Pismo documentation. The file provides a machine‑readable, Markdown‑based index of all portal content, stays in sync with documentation updates, and offers direct access to Markdown versions of all site pages. For more information, refer to [Using LLMs with the Pismo Developers Portal](https://developers.pismo.io/pismo-docs/docs/using-llms).

  #### Docs

  The **Pismo API reference overview** guide was moved to the new **Get started** section on the **APIs** tab, and was renamed to [Get started with Pismo APIs](https://developers.pismo.io/pismo-docs/docs/get-started-with-pismo-apis).

  ### Control Center

  #### Docs

  The [Holidays](https://developers.pismo.io/pismo-docs/docs/holidays) guide is now available with instructions for managing bank holiday calendars in Control Center, including calendar creation, hierarchy, import/export, and holiday configuration.

  ### Core banking

  #### Docs

  The new [Bankers Automated Clearing System (BACS)](https://developers.pismo.io/pismo-docs/docs/banking-automated-clearing-system) guide is now available to accompany the new [BACS API](https://developers.pismo.io/pismo-docs/reference/post-create-bacs-1) endpoints.

  ### Instant payments

  #### New

  The new [Return FPS payment \[beta\]](ref:post-return-fps) endpoint is now available in beta release.
</summary>

<summary class="tabContent" id="Core platform">
  ### Accounting

  #### Docs

  In the [Create accounting entry](https://developers.pismo.io/pismo-docs/reference/createaccountingentry) endpoint, the example for the `event_date` field was updated to be in the correct YYYY-MM-DD format and the description of the `tracking_id` field was updated to clarify its format as UUID and to include a generator link.

  ### Accounts

  #### Docs

  In the [Account status](https://developers.pismo.io/pismo-docs/docs/accounts-overview#account-status) table, the **CANCELLED** row was updated to explicitly state that you can change the status in Control Center.

  #### Docs

  In the [Get account](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts) endpoint, the `show_children` field description was updated to indicate that the response lists up to 3 levels of descendant account numbers (children, grandchildren, and great-grandchildren) in the `children` array.

  ### Authentication

  #### Docs

  The description for [Get OpenID access token](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token) endpoint was updated to clearly explain the role of the JSON Web Token (JWT) and to include a link to the [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid) guide.

  ### Client webhooks

  #### Docs

  The [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) section of the Client webhooks guide was updated to address the following.

  * The requirement descriptions for request fields `authorization_code` and `incoming_authorization_code` were updated for clarification.
  * The `partial_approval_info` object and its fields `local_amount`, `settlement_amount`, and `cardholder_amount`, were added to the response fields list to address insufficient fund declines at point-of-sale when the available Visa card or account balance is not sufficient to approve a transaction in full.
  * The `original_network_data` object is now properly marked as required for both Zero balance and Full balance.

  ### Flex controls

  #### Updated

  In the [Flex controls](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) API, the `currency_code` value was removed from the list of options in the `conditions.attributes` field.

  ### General

  #### Docs

  The [Get started with Ask AI](https://developers.pismo.io/pismo-docs/docs/get-started-with-ask-ai) guide was moved to the **Resources** section.

  #### Docs

  The following note was added to the description of the `metadata` field in the Transaction banking, Overdraft, Lending, and Statements APIs.

  **Note:** This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](https://developers.pismo.io/pismo-docs/reference/get-started-with-pismo-apis).\`

  ### Migrations

  #### Docs

  [Balance control](https://developers.pismo.io/pismo-docs/docs/migrations-overview#balance-control) and [Accruals](https://developers.pismo.io/pismo-docs/docs/migrations-overview#accruals) sections were added to the Migrations guide. These sections detail how to ensure account balances are established correctly, as well as ensure interest and other accrued charges are transferred correctly on to the Pismo platform during the migration process.

  #### Docs

  In the [Migrate PCI cards](https://developers.pismo.io/pismo-docs/reference/postpcicardsv1) endpoint, `pin_type` and `pin_validation_data` field descriptions were updated to reflect accepted enum values. The `encrypted_pin` field was also revised for clarity and adherence to Pismo platform standards.

  #### Docs

  The summary for the [Migrate balances](https://developers.pismo.io/pismo-docs/reference/postbalancecontrolv1) endpoint was updated to explicitly state the configuration requirements when migrating balances.

  ### Payments

  #### Updated

  In the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) endpoint, the `validation_rules` field is now available. You can set `validation_rules` to control the rules in this flow, such as disabling a rule, changing the response code and denial code, and forcing a rule. The [Define validation rules](https://developers.pismo.io/pismo-docs/docs/configure-payment-methods#define-validation-rules) of the Configure payment methods guide was updated accordingly also.

  ### Programs

  #### Docs

  The unused and incorrect field, `currency_numeric_code`, was removed from the [Update program](https://developers.pismo.io/pismo-docs/reference/updateprograminfo) endpoint. The currency defined for a program was never intended to be modifiable, as it could cause problems with the program.

  ### Rates and fees

  #### Docs

  The [Exchange rates](https://developers.pismo.io/pismo-docs/docs/exchange-rate) guide was updated to better explain exchange rate configuration and retention behavior and to include a description of rates behavior in a multi-currency setup (MCS).

  #### Docs

  The sample for [Bulk upload of exchange rates](https://developers.pismo.io/pismo-docs/docs/exchange-rates#bulk-upload-exchange-rates) in the Exchange rates in Control Center guide was updated to clarify that both periods and commas work for exchange rates and fees, regardless of the specified currency codes.

  ### Security

  #### Docs

  The [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid) guide was updated with the following clarifying edits.

  * A reference and link to the [Get OpenID access token](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token) endpoint was added to the initial guide summary.
  * The definition for the claim `tenant_id` was updated to clarify that the `tenant_id` claim is different than the Org ID.
  * The definition and example for the claim `pismo` was updated to indicate that you can add more than one permission group at a time.

  #### Docs

  The [Important security details](https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls#important-security-details) section of the Identity connectivity with mTLS guide was rewritten for clarification of security for API communications.

  #### Docs

  The Request parameter list for Grant type in the [Authentication with OAuth2](https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2) guide was updated to list the parameter `client_secret` (it was previously incorrectly listed as `client_secret_string`).

  ### Setup

  #### New

  New sections and endpoints were added to [Platform setup - Holidays](https://developers.pismo.io/pismo-docs/reference/post-create-holiday-calendar): **Holiday calendar** and **Holiday calendar data**. The endpoints in these sections are a replacement for endpoints in two sections in the same API: Holidays and Holidays V2 - transaction banking. These two sections and their endpoints are now deprecated. Endpoints under Holidays (found under [Platform setup – Organizations](https://developers.pismo.io/pismo-docs/reference/patch-v1-orgs)) were also deprecated and replaced with endpoints in the two new sections.

  #### Docs

  A new section for **Holidays and admin divisions** was added to the [API endpoint deprecation and removal schedule](https://developers.pismo.io/pismo-docs/docs/api-endpoint-deprecation-and-removal-schedule) to detail deprecated endpoints and their replacements.

  #### Docs

  The table in [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) was updated to use an advanced format. Some of the new features and changes include:

  * The table can now be sorted by any column.
  * The filter textbox enables you to search for a text value anywhere in the table.
  * Pagination is enabled with page size set to 30 rows.
  * You can export the table to a CSV file.
  * The column header “Required?” has been changed to “Constraints”. This is meant to better reflect the purpose of the column, which is to indicate how the program type constrains the use of the parameters.
  * Other minor changes have been made to the table and the rest of the page.

  #### Docs

  The table in [Account parameters](https://developers.pismo.io/pismo-docs/docs/account-parameters-reference-table) was updated to use an advanced format. Some of the new features and changes include:

  * The table can now be sorted by any column.
  * The filter textbox enables you to search for a text value anywhere in the table.
  * You can export the table to a CSV file.
  * The column header “Required?” has been changed to “Constraints”. This is meant to better reflect the purpose of the column, which is to indicate how the program type constrains the use of the parameters.
  * Other minor changes have been made to the table and the rest of the page.

  ### Support

  #### Docs

  The **Comments** column of the [Request types and common fields](https://developers.pismo.io/pismo-docs/docs/request-types) guide was updated to remove the reference that did not link to any additional content and caused confusion. The column now presents the information without unnecessary or misleading text.

  #### Docs

  The "Sandbox" request type was updated to "Non-production environment" across the following guides.

  * [Request types and common fields](https://developers.pismo.io/pismo-docs/docs/request-types)
  * [Open a service request](https://developers.pismo.io/pismo-docs/docs/opening-a-service-desk-ticket)
  * [Describe the issue](https://developers.pismo.io/pismo-docs/docs/describing-an-issue)
  * [Non-incident lifecycle](https://developers.pismo.io/pismo-docs/docs/non-incident-lifecycle)
</summary>

<summary class="tabContent" id="Data">
  ### Events

  #### Updated

  The new `maturity_period` and `detach_datetime` fields were added to the following events to provide additional details about account and product attachments.

  * [Account attached](https://developers.pismo.io/events/docs/deposit-product-account-attach-1)
  * [Program attached](https://developers.pismo.io/events/docs/deposit-product-program-attach-1)

  #### Updated

  The description of the [Installment advanced](https://developers.pismo.io/events/docs/balance-installment-advancement-1) event was updated to list the endpoints that generate it.

  #### Updated

  References to the `cycle` field were removed from the [Statement migration started](https://developers.pismo.io/events/docs/migration-statement-incoming-1) and [Statement migration completed](https://developers.pismo.io/events/docs/migration-account-balance-statement-update-outgoing-1) events. These events are only a receipt/acknowledgement and do not define the invoice cycle, and therefore were  removed to avoid misinterpretation of the event.

  #### Updated

  The `status` field was added as a required field to the [Account migration started](https://developers.pismo.io/events/docs/migration-account-incoming-2) and [Account migration completed](https://developers.pismo.io/events/docs/migration-account-outgoing-2) events. This update was to address the mandatory field missing from the payload.
</summary>

<summary class="tabContent" id="Core banking">
  ### Banking operations

  #### New

  Two new endpoints are introduced to enable clients to update payout accounts for deposit and savings accounts.

  * [Update payout account for deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-payout-account)
  * [Update payout account for savings account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-update-payout-account)

  #### Updated

  In the `deposit_configs` field of the [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account) endpoint request payload and [Get account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-account-attachment) response payload, the following fields were replaced by `maturity_period`.

  * `maturity_date_days`
  * `calendar_maturity_date`

  #### Updated

  The `end_date` field is introduced to the deposit product and is used as a validation point for rollover rules. The deposit product creation endpoint currently supports configuring maturity and rollover behavior but does not enforce any boundary tied to an end date. This new field is added to the following endpoints.

  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product), in the request payload
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products), in the response payload

  #### Updated

  The new `legal_holds` field was added to the response payload of the following endpoints to indicate the portion of an account balance under legal holds and unavailable for transactions.

  * [Get transaction banking account information](https://developers.pismo.io/pismo-docs/reference/get-accounts)
  * [Get transaction banking account balance](https://developers.pismo.io/pismo-docs/reference/get-account-balances)

  #### Updated

  In the `maturity_instructions` object of the [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product) and [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products) endpoints, the `NO_ACTION` attribute of the `principal` object in the 200 response payloads is now replaced by `PAY`, which indicates the principal amount paid to the payout account.

  ### Instant payments

  #### New

  The new [Confirmation of payee](https://developers.pismo.io/pismo-docs/reference/post-cop-verification) (CoP) endpoint was added to the Faster Payments API. CoP allows payers to check that the name they have for the intended recipient matches the actual name on the recipient's account, reducing the risk of fraud and misdirected payments. This endpoint must be called before calling [Send Faster Payment](https://developers.pismo.io/pismo-docs/reference/post-create-fps). The new [Confirmation of payee](https://developers.pismo.io/pismo-docs/docs/faster-payment-system#confirmation-of-payee) section was also added to the Faster Payments guide. The two [CoP](https://developers.pismo.io/events/docs/fps-cop-name-verification-submissions-1) events were edited for clarity and standards.

  #### New

  The new [Resend payment order](https://developers.pismo.io/pismo-docs/reference/resend-automatic-pix-payment-order) endpoint is now available in the Automatic Pix API. You can use this endpoint when:

  * The payer's PSP did not accept the payment order and the status is `REJECTED` or `EXPIRED`,
  * When the payment order was accepted, but the Pix transaction was not found by the due date, with status `CANCELLING`.

  In these cases, the payment order can be resent to trigger a new attempt to process the payment.

  #### Updated

  In the [Automatic Pix](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic) API, the `reason_code` has a new cancellation reason code: `OTHS`. This reason indicates that the cancellation was requested by either the payer’s participant or the receiver’s participant for other reasons not specified in the previous categories.

  #### Docs

  The “Instant payments - Automatic Pix” API has been divided into two sections - Automatic Pix and [Automatic Pix data](https://developers.pismo.io/pismo-docs/reference/list-recurrence-automatic). In the CRUD (Create, Read, Update, Delete) scheme of things, the first section contains all the CUD (POST, PUT, PATCH, DELETE) endpoints and the data section contains all the R (GET) endpoints.

  ### Payment rails

  #### New

  The new [Reverse BACS direct credit outbound payment](https://developers.pismo.io/pismo-docs/reference/post-reversal-bacs) endpoint is now available in the Bankers' Automated Clearing System (BACS) API. This endpoint can be called to reverse a BACS direct credit outbound payment that is on hold.

  #### Updated

  The URL path was updated in the [Release BACS inbound transaction \[beta\]](ref:post-release-bacs-1) and [Cancel BACS inbound transaction \[beta\]](ref:post-cancel-bacs-1) endpoints.

  ### Transaction banking

  #### New

  The new [Simulate penalty](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-simulate-penalty) endpoint is now available. This endpoint lets clients simulate the penalty applied to a specified withdrawal on a given date.

  #### Docs

  The [Account balance definitions for transaction banking](https://developers.pismo.io/pismo-docs/docs/account-balance-definitions-for-transaction-banking) previously listed the book balance formula as `credit_balance` - `debit_balance` + `earmark_balance`. This was now corrected to `credit_balance` - `debit_balance`.
</summary>

<summary class="tabContent" id="Card issuing">
  ### Card network integration

  #### Updated

  The Visa denial code for custom code RED (operation\_not\_allowed\_by\_rules) was changed from `78`to `9G`. This change is reflected in the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) guide.

  #### Docs

  The [Consolidated file and events](https://developers.pismo.io/pismo-docs/docs/clearingbase#consolidated-file-and-events) section of the Clearing/Base II guide was updated to better explain that all settlement-related information is delivered through clearing events and there are no actual settlement events.

  ### Cards

  #### New

  The following new card reissue endpoints are now available.

  * [List reissue reasons](https://developers.pismo.io/pismo-docs/reference/get-reissue-reasons)
  * [Update reissue reason](https://developers.pismo.io/pismo-docs/reference/update-reissue-reason)
  * [Create reissue reason](https://developers.pismo.io/pismo-docs/reference/create-reissue-reason)
    The [Get card reissue reasons](https://developers.pismo.io/pismo-docs/reference/get-v1-card-reissue-reasons) endpoint is outdated and is soon to be deprecated.

  ### Cards on file

  #### Updated

  The unused **Get card validation amount** endpoint was removed.

  ### Disputes

  #### Updated

  The names of version 1 of the Create fraud report and Update fraud report endpoints were changed to [Create dispute fraud report](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-fraud-report) and [Update dispute fraud report](https://developers.pismo.io/pismo-docs/reference/put-v1-disputes-fraud-report), respectively. These name changes resolve duplicate endpoint names within the Disputes API.

  ### Statements

  #### Updated

  The 423 - Account Locked HTTP status code response was added to the [Create payment agreement simulation](https://developers.pismo.io/pismo-docs/reference/create-payment-agreement-simulation) endpoint.

  #### Docs

  The description for the [Update scheduled charge](https://developers.pismo.io/pismo-docs/reference/update-scheduled-charge) endpoint was updated.

  #### Docs

  The **Configuring accrual rates** guide was broken up into:

  * [Configuring accrual rates](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates)
  * [Transaction categories](https://developers.pismo.io/pismo-docs/docs/transaction-category-structure)
  * [Accrual type rates](https://developers.pismo.io/pismo-docs/docs/accrual-type-rate-structures)
  * [Program transaction types](https://developers.pismo.io/pismo-docs/docs/program-transaction-types)

  The [Using configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#using-configurable-entities) section of the Full balance credit program guide was rewritten and shortened using links to the new guides.

  #### Docs

  The following endpoints were renamed and their descriptions were updated. The original names were confusing and did not clearly differentiate the endpoints from other endpoints with similar functionality.

  * Create installment advance without interest → [Create installment advancement (no cancellation event)](https://developers.pismo.io/pismo-docs/reference/installmentadvancedv2)
  * Get simulation installment advance without interest → [Get simulation installment advancement](https://developers.pismo.io/pismo-docs/reference/getinstallmentadvancedsimulationv2)
  * Get installment advance without interest → [Get installment advancement (no cancellation event)](https://developers.pismo.io/pismo-docs/reference/getinstallmentsadvancev2)
  * Cancel installment advance without interest → [Cancel installments advancement (no cancellation event)](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentsadvancev2)

  #### Docs

  The path parameter `PaymentAgreementId` was changed to `advancementId` for the following endpoints. The original parameter was incorrect.

  * [Get installment advancement](https://developers.pismo.io/pismo-docs/reference/getinstallmentadvancementv2byid)
  * [Cancel installment advancement](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentadvancev2)

  #### Docs

  The table in the [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters) guide was updated to use an advanced format.

  * The table can now be sorted by any column.
  * The filter textbox enables you to search for a text value anywhere in the table.
  * You can export the table to a CSV file.
  * The “Applies to” column has been moved to the right of the “Name” column.

  #### Docs

  The 423 - Account Locked HTTP status code response was added to the [Create payment agreement simulation](https://developers.pismo.io/pismo-docs/reference/create-payment-agreement-simulation) endpoint.

  #### Deprecated

  The deprecated endpoint **Get program future calendars** (GET /statements-v2/v1/calendars) was decommissioned and removed from the API reference. An entry for it was added to [API endpoints removed](https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed).

  ### Tokenization

  #### New

  The new tokenization endpoint [Bind Visa device and token](https://developers.pismo.io/pismo-docs/reference/post-run-visa-device-lifecycle) is now available. Device binding establishes that a specific device belongs to a specific cardholder. Once bound, the device can be trusted more in future transactions. An issuer can use this endpoint to update the status of a specific device linked to a token.
</summary>

<summary class="tabContent" id="Lending">
  ### Lending

  #### New

  The following endpoints are now available in beta release for lending to enable prepayment simulation and prepayment records.

  * [Create prepayment record \[beta\]](ref:createprepayment)
  * [Register prepayment simulation \[beta\]](ref:registerprepaymentsimulationv2)
  * \[Simulate prepayment \[beta]]Register repaymen(ref:simulateprepaymentv2)

  #### Updated

  The following endpoints were updated to remove `program_id` from any loan adjustment information to avoid confusion and mismatched program configuration IDs.

  * [Create loan product \[beta\]](ref:createloanproductv2)
  * [Get loan product \[beta\]](ref:getloanproductv2)
  * [List loan products \[beta\]](ref:getloanproductsv2)
  * [Create loan adjustment](https://developers.pismo.io/pismo-docs/reference/createloanadjustmentv2)

  #### Updated

  The following endpoints were updated to enable you to set or get a grace period with the `grace_period_days` field. When set, the loan installment status goes to `IN_GRACE_PERIOD` instead of `PAST_DUE` when the deadline has passed for repayment.

  * [Create loan product \[beta\]](ref:createloanproductv2)
  * [Get loan product \[beta\]](ref:getloanproductv2)
  * [List loan products \[beta\]](ref:getloanproductsv2)

  #### Updated

  You can now set, update, or remove a minimum total payment with `minimum_total_payment` on the following endpoints.

  * [Create loan product \[beta\]](ref:createloanproductv2)
  * [Update loan product \[beta\]](ref:updateloanproductv2)

  #### Updated

  You can now indicate the minimum total payment difference with `minimum_total_payment_delta` on the [Register repayment \[beta\]](ref:registerrepaymentv2) endpoint.
</summary>

<summary class="tabContent" id="Seller management">
  ### Merchants

  #### Updated

  The following new fields were added to the [Get merchant transaction](https://developers.pismo.io/pismo-docs/reference/getmerchanttransactionv2) endpoint. These new fields allow you to see total discount and itemized discount breakdowns within the Seller management - Merchants API.

  * `discount_amount`
  * `discount_details`
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### Docs

  In the [Change account status](https://developers.pismo.io/pismo-docs/docs/account-actions#change-account-status) section:

  * An info notice was added, stating that you can reactivate a canceled account by changing its status back to **Active**.
  * The link at the bottom of the section was updated to point to the [Accounts](https://developers.pismo.io/pismo-docs/docs/accounts-overview) guide.

  #### Docs

  The [OpenId Connect authentication](https://developers.pismo.io/pismo-docs/docs/openid-configurations) guide for Control Center was updated to clearly indicate that Admin access is needed to view and edit OpenID authentication configurations.

  #### Docs

  Documentation was clarified that Pismo does not create and manage Control Center users. Rather, the customer’s Control Center administrators are responsible for these tasks. The following guides were updated:

  * [Pismo platform onboarding](https://developers.pismo.io/pismo-docs/docs/pismo-platform-onboarding)—Clarified that when defining an organization, the email contact is also assigned the Control Center administrator role initially.
  * [Create and edit users](https://developers.pismo.io/pismo-docs/docs/add-a-user)

  #### Docs

  The Exchange rates for Control Center guide was updated to include a note in the [Bulk upload exchange rates](https://developers.pismo.io/pismo-docs/docs/exchange-rates#bulk-upload-exchange-rates) section that it essential to include identity pairs when your setup is multi-currency.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/payments/fps/return/{endToEndId}` (`post-return-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/accounting-entries` (`CreateAccountingEntry`) | `api-specs/Core_platform_-_Accounting.yaml` | no | KU-API-core-platform-accounting--accounting-entry |
| `GET /accounts/v1/accounts/{accountId}` (`get-accounts-v1-accounts`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v1/oauth2/token` (`post-passport-v1-oauth2-token`) | `api-specs/Platform_authentication.yaml` | no | KU-API-platform-authentication--authentication |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/migrations/cards-pci` (`PostPciCardsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /v1/migrations/balance-control` (`PostBalanceControlV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--balance-migration |
| `POST /payment-methods/v1/authorization` (`post-authorization`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `PATCH /programs/v1/programs/{id}` (`UpdateProgramInfo`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /v1/holiday-calendar` (`post-create-holiday-calendar`) | `api-specs/Platform_setup_-_Holidays.yaml` | no | KU-API-platform-setup-holidays--holiday-calendar |
| `PATCH /orgs-core/v1/orgs` (`patch-v1-orgs`) | `api-specs/Platform_setup_-_Organizations.yaml` | no | KU-API-platform-setup-organizations--orgs |
| `PATCH /v1/deposits/accounts/{accountId}` (`interest-bearing-v1-deposit-update-payout-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/savings-accounts/accounts/{accountId}` (`interest-bearing-v1-savings-account-update-payout-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits/accounts/{accountId}/attach` (`interest-bearing-v1-deposit-attach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `GET /v1/products/attachments/accounts/{accountId}` (`interest-bearing-v1-get-account-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/deposits/{productId}` (`interest-bearing-v1-get-deposit-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /corporate/v1/corporate-accounts/{externalAccountId}` (`get-accounts`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `GET /bank-statements/v1/account-balances/{externalAccountId}` (`get-account-balances`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `POST /v1/payments/fps/cop` (`post-cop-verification`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/fps/out` (`post-create-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /inst-pull-pay/v1/pix/automatic/payment/order/{end_to_end_id}/resend` (`resend-automatic-pix-payment-order`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /inst-pull-pay/v1/pix/automatic` (`post-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `GET /inst-pull-pay/v1/pix/automatic` (`list-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix-data |
| `POST /v1/payments/bacs/directcredit/{id}/reversal` (`post-reversal-bacs`) | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `POST /v1/deposits/accounts/{accountId}/penalty-simulation` (`interest-bearing-v1-simulate-penalty`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--penalty |
| `GET /cards/v1/reissue/reasons` (`get-reissue-reasons`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `PATCH /cards/v1/reissue/reasons/{id}` (`update-reissue-reason`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `POST /cards/v1/reissue/reasons` (`create-reissue-reason`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `GET /wallet/v1/cards/reissue/reasons` (`get-v1-card-reissue-reasons`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `POST /v1/disputes/{disputeId}/fraud-report` (`post-v1-disputes-fraud-report`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--supporting-forms |
| `PUT /v1/disputes/{fraudReportId}/fraud-report` (`put-v1-disputes-fraud-report`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--supporting-forms |
| `POST /v1/accounts/{accountId}/payment-agreement-simulations` (`create-payment-agreement-simulation`) | `api-specs/Revolving_credit_-_Statement_refinancing_API.yaml` | no | KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation |
| `PATCH /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}` (`update-scheduled-charge`) | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges |
| `POST /statements/v2/accounts/{accountId}/installment-advance` (`InstallmentAdvancedV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `GET /statements/v2/accounts/{accountId}/installment-advance` (`GetInstallmentAdvancedSimulationV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `GET /statements/v2/accounts/{accountId}/installment-advance/{id}` (`GetInstallmentsAdvanceV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `DELETE /statements/v2/accounts/{accountId}/installment-advance/{id}` (`CancelInstallmentsAdvanceV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | **yes** | KU-API-revolving-credit-statements--advancements |
| `GET /v2/accounts/{accountId}/installment-advance/{advancementId}` (`GetInstallmentAdvancementV2ById`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}` (`cancelInstallmentAdvanceV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `POST /v1/cards/{cardId}/network-tokens/{tokenId}/devices/{deviceId}/binding` (`post-run-visa-device-lifecycle`) | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--token-lifecycle |
| `POST /v2/prepayments` (`createPrepayment`) | `api-specs/Lending.yaml` | no | KU-API-lending--prepayment |
| `POST /v2/loans/{loanId}/prepayment/{simulationId}/register` (`registerPrepaymentSimulationV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--prepayment |
| `POST /v2/loan-products` (`createLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /v2/loan-products/{productId}` (`getLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /v2/loan-products` (`getLoanProductsV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v2/loans/{loanId}/adjustment` (`createLoanAdjustmentV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `PATCH /v2/loan-products/{productId}` (`updateLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v2/loans/{loanId}/repayment` (`registerRepaymentV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--repayments |
| `GET /v2/merchants/{merchantId}/transactions/{merchantTransactionId}` (`getMerchantTransactionV2`) | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant-transaction |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-create-bacs-1` | BACS API; Payment rails - BACS payments | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `get-started-with-pismo-apis` | Get started with Pismo APIs | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-release-bacs-1` | Release BACS inbound transaction \\[beta\\] | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-cancel-bacs-1` | Cancel BACS inbound transaction \\[beta\\] | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/5-june-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/5-june-2026 | `5b46a69cf6487e09…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--penalty` — API reference: Banking - Interest-bearing accounts — Penalty
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-disputes--supporting-forms` — API reference: Card issuing - Disputes — Supporting forms
- `KU-API-card-issuing-tokenization--token-lifecycle` — API reference: Card issuing - Tokenization — Token lifecycle
- `KU-API-core-platform-accounting--accounting-entry` — API reference: Core platform - Accounting — Accounting entry
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-instant-payments-automatic-pix--automatic-pix` — API reference: Instant payments - Automatic Pix — Automatic Pix
- `KU-API-instant-payments-automatic-pix--automatic-pix-data` — API reference: Instant payments - Automatic Pix — Automatic Pix data
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-lending--prepayment` — API reference: Lending — Prepayment
- `KU-API-lending--repayments` — API reference: Lending — Repayments
- `KU-API-migrations--balance-migration` — API reference: Migrations — Balance migration
- `KU-API-migrations--card-migration` — API reference: Migrations — Card migration
- `KU-API-payment-rails-bacs-payments--bacs-direct-credit` — API reference: Payment rails - BACS payments — BACS direct credit
- `KU-API-platform-authentication--authentication` — API reference: Platform authentication — Authentication
- `KU-API-platform-setup-holidays--holiday-calendar` — API reference: Platform setup - Holidays — Holiday calendar
- `KU-API-platform-setup-organizations--orgs` — API reference: Platform setup - Organizations — Orgs
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges` — API reference: Revolving credit - Recurring charges — Recurring scheduled charges
- `KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation` — API reference: Revolving credit - Statement refinancing — Payment agreement simulation
- `KU-API-revolving-credit-statements--advancements` — API reference: Revolving credit - Statements — Advancements
- `KU-API-seller-management-merchants--merchant-transaction` — API reference: Seller management - Merchants — Merchant transaction
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
