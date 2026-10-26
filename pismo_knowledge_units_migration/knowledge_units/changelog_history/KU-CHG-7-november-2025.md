---
ku_id: KU-CHG-7-november-2025
title: 'Changelog: 7 November 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/7-november-2025.md
  sha256: 5d1b719ddf8be28d2a01f5b55221e175e25af78d91b080588bc5067ff02ee6b5
  url: https://developers.pismo.io/pismo-docs/changelog/7-november-2025
  role: changelog_post
  updated_at: ''
operations:
- CopyProgram
- CopyProgramAsync
- CreateProcessingCode
- CreateProgramBasedOnTemplate
- CreateProgramBasedOnTemplateAsync
- CreateProgramCalendarStrategy
- ListTransactions
- PostAccountsV2
- PostCardsV1
- PostCustomersV1
- PostPciCardsV1
- UpdateProgramInfo
- UpdateStatementsDueDate
- corporate-v2-post-payments
- corporate-v3-post-multileg-payments
- create-recurring-charge-plan
- deleteAccrualTypesConfigurations
- disburseLoanV2
- get-v1-org
- get-v2-pix-infraction-search
- getAccountAccrualsV3
- getAccountsTransactionsInterest
- getLoansByAccountIdV2
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-attach-program
- interest-bearing-v1-patch-deposit-product
- interest-bearing-v1-savings-account-attach-account
- interest-bearing-v1-savings-account-attach-program
- listAccountAccrualTypeRates
- listTransactionCategoryInterest
- patch-accounts-v1-accounts
- patch-v1-orgs
- post-acquisitions-v3-s2s-applications
- post-authorization
- post-create-fps
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban
- post-pix-out-transfer
- post-v1-card-reissue
- post-v1-interest-accrual-setup
- post-v1-simulation
- post-v2-card
- postAccrualTypesConfigurations
- put-v1-update-pan-nominal
- put-v1-update-pan-noname
related_kus:
- KU-API-banking-bank-accounts--bank-accounts-part-01
- KU-API-banking-bank-accounts--bank-accounts-part-02
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-bearing-accounts--program-attachment
- KU-API-banking-interest-engine--interest-accrual
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--issuer-pan-pin
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-core-platform-payment-methods-admin--simulation
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--pix-part-02
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-API-lending--disbursements
- KU-API-lending--loans
- KU-API-migrations--account-migration
- KU-API-migrations--card-migration
- KU-API-migrations--customer-migration
- KU-API-platform-setup-organizations--orgs
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-calendar-management--program-calendar-strategies
- KU-API-revolving-credit-configurations--account-accrual-rates
- KU-API-revolving-credit-configurations--additional-accrual-type-configurations
- KU-API-revolving-credit-recurring-charges--recurring-charge-plans
- KU-API-revolving-credit-statements--accruals
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 7 November 2025
coverage_window: 3 October and 7 November 2025
---

# Changelog: 7 November 2025

**KU ID:** `KU-CHG-7-november-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **7 November 2025** (changes between 3 October and 7 November 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated".

## Topics covered

Cards; Control Center; Accounts; Flexible transaction controls; General; Migrations; Organizations; Payments; Processing codes; Programs; Security; Support; Transactions; Events; Reports; Banking as a Service; Banking operations; Transaction banking; Card network integration; Instant payments; Statements; Lending; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/7-november-2025

<!-- source:begin path=changelog/7-november-2025.md part=0-end -->

# 7 November 2025

Changes between 3 October and 7 November 2025

<div class="customTab"></div>

<summary class="tabContent" id="New features">

### Cards

#### New

Issuers can now create or reissue cards without PCI data (PAN/PIN) that they can define themselves at some future date. A new [card status](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses) - `UNNUMBERED` - was created to support this. Two new fields - `status` and `brand` - were added to the [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card) and [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue) endpoints. Two new endpoints in a new API section (Card issuing - Cards > Issuer PAN/PIN) were added - [Update nominal card PAN/PIN](https://developers.pismo.io/pismo-docs/reference/put-v1-update-pan-nominal) and [Update noname card PAN/PIN](https://developers.pismo.io/pismo-docs/reference/put-v1-update-pan-noname). These endpoints are currently in beta release. A new [Issuer-defined PAN/PIN](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#issuer-defined-panpin) section was added to the Cards management guide.  A `PAN_UPDATE` enum was added to the `operation_type` field for the [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event.

### Control Center

#### New

The [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval) and [Account actions](https://developers.pismo.io/pismo-docs/docs/account-actions#change-account-status) guides were updated to reflect that users with dual approval capability can now change an account status in Control Center with the dual approval process. The dual approval guide was also updated to make navigation easier, improve clarity, and include more answers to frequently asked questions.

</summary>

<summary class="tabContent" id="Core platform">

### Accounts

#### New

A new `program_calendar_strategy_id` field was added to the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint. This field determines how program calendars are created. For more information, refer to the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint.

#### Updated

The `external_id` field was added to the [Update account](https://developers.pismo.io/pismo-docs/reference/patch-accounts-v1-accounts) endpoint. This field is customer-provided, and is for customer tracking and monitoring.

### Flexible transaction controls

#### Docs

In the [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls) guide, the note was added to specify limits on the number of flex controls you can create.

### General

#### Docs

[Core objects](https://developers.pismo.io/pismo-docs/docs/setup-overview) documentation was updated to adhere to documentation standards.

### Migrations

#### Deprecated

The Migrate accounts (v1) endpoint was deprecated, removed, and replaced with the [Migrate accounts (v2)](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint. Documentation was updated accordingly throughout.

#### Docs

In the [Migrate PCI cards](https://developers.pismo.io/pismo-docs/reference/postpcicardsv1) endpoint documentation, fictional PAN example was updated and a disclaimer was added.

#### Docs

In the [Migrate accounts (v2)](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint, field description for `available_credit_limit` was updated to indicate debit cards can also use this field.

#### Docs

The `account_id` field description in the [Migrate cards](https://developers.pismo.io/pismo-docs/reference/postcardsv1) endpoint was updated to explicitly mention that this field must match the `applicant.migration.id` from the [Migrate accounts](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint.

#### Docs

The following field descriptions in the [Migrate cards](https://developers.pismo.io/pismo-docs/reference/postcardsv1) endpoint were updated to adhere to documentation standards

* `combo_account_id`
* `account_id`

#### Docs

The [Migrate customers](https://developers.pismo.io/pismo-docs/reference/postcustomersv1) endpoint introductory sentence was revised to adhere to documentation standards.

### Organizations

#### Updated

New fields were added to the [Update organization](https://developers.pismo.io/pismo-docs/reference/patch-v1-orgs) endpoint request and response: `official_name`, `org_name`, `language`, `cycle_closing`, `holiday_calendar_id`, and `responsible`. Refer to the endpoint documentation for field descriptions.

#### Updated

Two new tags, `TRANSACTION_BANKING` and `FPS`, were added to the `tags` field in the [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) endpoint.

#### Docs

The following updates were made in the Organizations API reference documentation.

* **Core platform - Orgs** was renamed to **Core platform - Organizations**
* Get Org was renamed to [Get organization](https://developers.pismo.io/pismo-docs/reference/get-v1-org)
* Update Org was renamed to [Update organization](https://developers.pismo.io/pismo-docs/reference/patch-v1-orgs)

### Payments

#### Updated

In the [Create simulation](https://developers.pismo.io/pismo-docs/reference/post-v1-simulation) endpoint, the `custom_filters` and `payment_agreement` fields are now available.

#### Updated

In the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) endpoint, the following existing error messages are now documented.

* WONA0004 - MTI required
* WONA0013 - Amount can't be negative
* WONA0015 - Initiator ID required
* WONA0016 - Network required
* WONA0018 - Invalid MTI
* WONA0019 - Invalid entry mode
* WONA0032 - Amount must be greater than zero
* WONA0033 - Beneficiary ID must be UUID
* WONA0036 - Invalid clearing type
* WONA039 - Max amount exceeded
* WONA040 - Invalid amount decimal places
* WONA041 - Invalid tracking ID size
* WONA042 - Invalid authorization date time format
* WONA043 - Invalid posting date format
* EINS0004 - External calculation invalid contract amount
* EINS0005 - External calculation invalid principal amount
* EINS0006 - External calculation principal greater than contract amount
* EINS0010 - External calculation invalid installment number
* EINS0011 - External calculation invalid installment info size
* EINS0012 - External calculation invalid installment amounts
* EINS0015 - External calculation invalid sum installment
* EINS0016 - External calculation invalid first payment date

#### Updated

The following new rejection reasons were added to the [Original authorization retrieval](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations#original-authorization-retrieval) validation rule.

* `ORIGINAL_AUTHORIZATION_IS_NOT_PENDING`&#x9;
* `ORIGINAL_AUTHORIZATION_DIFFERENT_PROCESSING_CODE`
* `ORIGINAL_AUTHORIZATION_DIFFERENT_CLEARING_TYPE`
* `ORIGINAL_AUTHORIZATION_DIFFERENT_CURRENCY`
* `ORIGINAL_AUTHORIZATION_DIFFERENT_NUMBER_OF_INSTALLMENTS`
* `ORIGINAL_AUTHORIZATION_WITH_EXTERNAL_CALCULATION`
* `INCREMENTAL_AUTHORIZATION_WITH_EXTERNAL_CALCULATION`
* `MULTIPlE_CONFIRMATION_WITH_EXTERNAL_CALCULATION`
* `MULTIPlE_CONFIRMATION_ORIGINAL_AUTHORIZATION_WITH_EXTERNAL_CALCULATION`
* `MULTIPlE_CONFIRMATION_ORIGINAL_AUTHORIZATION_DIFFERENT_NUMBER_OF_INSTALLMENTS`

#### Updated

In the [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event, the new `related_accounts` array is now available.

#### Docs

In the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) endpoint documentation, in the `amount` field description, the erroneous provision that the amount can't be 0 was removed. The platform supports a zero amount authorization model where you can validate the flow without causing any financial impact.

### Processing codes

#### Docs

Date in the New authorization system info box in [Custom processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types#custom-processing-codes) was updated to explicitly clarify date reference to January 2, 2025.

### Programs

#### Updated

New program events were added: [Program created](https://developers.pismo.io/events/docs/programs-creation-1) and [Program updated](https://developers.pismo.io/events/docs/programs-update-1). The following endpoints generate and link to Program created: [Create program](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate), [Create program (async)](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplateasync), [Copy program](https://developers.pismo.io/pismo-docs/reference/copyprogram), and [Copy program (async)](https://developers.pismo.io/pismo-docs/reference/copyprogramasync). The following endpoint generates and links to Program updated: [Update program](https://developers.pismo.io/pismo-docs/reference/updateprograminfo).

### Security

#### Docs

The [Identity connectivity with mTLS](https://developers.pismo.io/pismo-docs/docs/identity-connectivity-with-mtls) guide was updated to remove the requirement for customers to provide a risk letter when using certificates from a signing authority other than Cloudflare.

### Support

#### Docs

Pismo [Service Desk](https://developers.pismo.io/pismo-docs/docs/service-desk) documentation was updated to adhere to documentation standards.

### Transactions

#### Docs

In the [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions) endpoint, the description of the response `amount.type` field was updated to explain each available amount type.

</summary>

<summary class="tabContent" id="Data and reporting">

### Events

#### Updated

The [Timeline events](https://developers.pismo.io/pismo-docs/docs/timeline-overview) table, the following events were added.

For **Confirmation** type:

* `AUTHORIZE` – Operation was authorized.
* `CANCELLATION` – Operation was cancelled.
* `REPLACEMENT`– Operation was replaced.
* `REFUSAL` – Transaction was not authorized and was refused.

For **Transaction** type:

* `CANCELLATION_REFUSAL` – Cancellation was not authorized and was refused.
* `CANCELLATION_REVERSAL` – Cancellation was reversed.
* `PARTIAL_CANCELLATION` – Operation was partially cancelled.
* `INCREMENTAL` – Incremental amount was added to the transaction.
* `REFERRAL` – Operation was referred.
* `REPLACEMENT` – Operation was replaced.

#### Docs

Descriptions related to transaction banking were removed from the following events to maintain data consistency. The removed text will be migrated to the relevant guide.

* `metadata` field in [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
* `details` field in [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)

### Reports

#### Updated

The table in [Reports for Brazil](https://developers.pismo.io/pismo-docs/docs/brazilian-reports) was updated in the following ways.

* Two new reports, CADOC-3050 and CCS - JD CABINE CCS, were added.
* The names of some of the existing reports were simplified.
* Each report description was updated to explain which databases were used to prepare the report.

</summary>

<summary class="tabContent" id="Core banking">

### Banking as a Service

#### Docs

The [Banking as a Service](https://developers.pismo.io/pismo-docs/docs/banking-as-a-service) guide was updated according to documentation standards and the steps were rearranged to reflect that setting up organization, programs, accounts, and customers should be the first step. In addition, the guide was revised to state that Celcoin is Pismo’s BaaS partner.

### Banking operations

#### New

The following endpoints are now available to handle maturity instruction overrides. A maturity instruction override is when a client changes or updates the original instructions for what should happen to a financial product when it reaches its maturity date. This process is most common with fixed-term investments like certificates of deposit (CDs), fixed deposits, and bonds.

* [Create maturity instruction override](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-maturity-instruction-override)
* [Get maturity instruction override](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-maturity-instruction-override)
* [Update maturity instruction override](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-update-maturity-instruction-override)
* [Delete maturity instruction override](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-delete-maturity-instruction-override)

#### Updated

The [Configure timing for accrual calculation](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-accrual-setup) endpoint was updated in the following ways.

* The endpoint name was changed from “Configure timing for division accrual calculation” to “Configure timing for accrual calculation”.
* `division_id` is no longer required.
* The endpoint description was updated.

#### Updated

A new banking scheme CLABE is now available in the [Bank accounts](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban) API. A Clave Bancaria Estandarizada (CLABE) is an 18-digit standardized banking code used in Mexico for domestic electronic fund transfers. This update adds the following endpoint: [Register CLABE account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe).

#### Updated

In the [Change due date](https://developers.pismo.io/pismo-docs/reference/updatestatementsduedate) endpoint, the description of the `id` body parameter was updated.

#### Updated

A new field, `deposit_configs`,  was added to the following endpoints. It includes two child fields— `maturity_date_days` and `calendar_maturity_date`—that allow you to specify either the maturity period in days or the exact calendar maturity date.

* [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account)
* [Attach deposit product to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-program)

Similarly, a `savings_account_configs` field is added to the following endpoint to serve the same purposes as `deposit_configs`:

* [Attach savings account to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-account)
* [Attach savings accounts to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-savings-account-attach-program)

#### Docs

In the [Update deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-patch-deposit-product) endpoint documentation, changed the description in `AuthorizationToken` to say “Generic token“ instead of “Account token.“

### Transaction banking

#### Updated

New error codes and messages are now available to prevent posting back value-dated and future value-dated transactions across the entire division. This feature enables you to block such postings as needed.

In the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint:

`WPMT0054: Cannot post back value-dated transaction for this division`

In the [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments) endpoint:

`WMLP0005: Validation error: one or more legs did not pass validation`

</summary>

<summary class="tabContent" id="Card issuing">

### Card network integration

#### Updated

The following updates were made to the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) guide and the [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list) guide.

* The Visa response code was changed to 5C for the following custom codes: ANF, BII, BNM, CMD, CV3, DCC, DIC, DIY, IAT, ISE, NCV, OON, PIC, RAD, Z22, Z23, Z24, Z26, Z27, Z29, Z30.
* The following custom codes had Merchant denial code changed from 03 to 02: 998, ANF, AUD, CED, CTE, DCC, FR6, FR7, FRO, IAT, NCV, OON, VEV, VNM.
* The Visa response code for RED (Rules do not honor) was changed from 57 to 78.
* The Merchant denial code for RED (Operation not permitted - credit voucher) was changed from blank to 02.
* Two new custom codes were added: TNP (Token not provisioned), MDC (Multi-currency not allowed for DCC authorization, and OP1 (PIN translation failed).

#### Docs

Updates were made to the denial codes for the following custom codes: CVV1 or CVC1 validation (FR1), CVV2 or CVC2 validation (FR2), and transaction made with magnetic stripe in a country where it’s not allowed to be used (FR5). The changes are reflected in the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) guide.

#### Docs

[Card issuing](https://developers.pismo.io/pismo-docs/docs/card-issuing-basics) reference documentation was updated to adhere to documentation standards.

#### Docs

[Full and Zero balance transaction workflows](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows) documentation was updated to adhere to documentation standards.

#### Docs

The [Validation code definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions) guide now includes instructions for verifying the actual reason for declined authorizations. The method for determining the reason is based on the authorization model you are working with and instructions for Full balance and Zero balance are provided.

#### Docs

The [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events#authorization-discard-process) guide was updated to include the authorization discard time of 35 days for international authorizations.

### Instant payments

#### New

A new endpoint [List infraction reports](https://developers.pismo.io/pismo-docs/reference/get-v2-pix-infraction-search) is now available.

#### Updated

A new `signature_info` field was added to the [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer) endpoint. This field is used to encrypt the request according to [Product Security and Telecommunications Infrastructure](https://www.legislation.gov.uk/ukpga/2022/46/contents) (PSTI) standards. It guarantees the request's integrity and authenticity and the transaction messaging non-repudiation (assurance that a party involved in a transaction cannot later deny their involvement) from customer to PSTI. Pismo acts as a pass-through entity in this process.

#### Docs

The “Instant payments - Faster payments” API was renamed to “Instant payments - UK FPS”. Its one endpoint, “Send Faster Payment”, was renamed to [FPS out-transfer](https://developers.pismo.io/pismo-docs/reference/post-create-fps). The FPS functionality continues to remain in beta release.

### Statements

#### New

The following new endpoints are now available under Revolving credit - Configurations:

* [Enable additional configurations on accrual types](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesconfigurations)
* [Disable additional configuration on accrual types](https://developers.pismo.io/pismo-docs/reference/deleteaccrualtypesconfigurations)

#### Updated

In the [List account interest rates](https://developers.pismo.io/pismo-docs/reference/listaccountaccrualtyperates) endpoint, the list of enum values was corrected for the `accrualType` query parameter. Only three different accrual types can be defined at the account level.

#### Updated

The descriptions of the accrual type rates listed in the [Configure accrual rates](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#transaction-category-structure) guide were updated to clarify when they are applied.

#### Docs

In the  [List transaction categories](https://developers.pismo.io/pismo-docs/reference/listtransactioncategoryinterest) endpoint, the description of the `transactionCategoryDescription` query parameter was updated.

#### Docs

In the [Create recurring charge plan](https://developers.pismo.io/pismo-docs/reference/create-recurring-charge-plan) endpoint, the descriptions of the `processing_code` and `number_of_cycles` body parameters were updated.

#### Docs

A new multivalue program parameter, `DISCHARGE_PRIORITIZED_TTS_MIGRATION`, was added to the table in [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters).

#### Docs

In the [Limiting the number of days accruals can be charged](https://developers.pismo.io/pismo-docs/docs/limiting-the-number-of-days-accruals-can-be-charged) guide, a note was added explaining that reaching the `STOP_ACCRUAL` limit does not automatically advance future installments.

#### Docs

A note was added to the end of [How a Full balance credit program manages credit accounts](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-a-full-balance-credit-program-manages-credit-accounts).

#### Docs

[How the program handles overdue transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-handles-overdue-transactions) was updated to clarify some points.

#### Docs

In the [Update interest accrual statuses](https://developers.pismo.io/pismo-docs/reference/getaccountstransactionsinterest) endpoint, a link was added in the description of the `new_status` field of the `accruals` body parameter to [Limiting the number of days accruals can be charged](https://developers.pismo.io/pismo-docs/docs/limiting-the-number-of-days-accruals-can-be-charged).

#### Docs

The [List account accruals v3](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv3) endpoint description was modified and a link was added in the description of the `STOP_ACCRUAL` enum of the `status` query parameter to [Limiting the number of days accruals can be charged](https://developers.pismo.io/pismo-docs/docs/limiting-the-number-of-days-accruals-can-be-charged).

#### Docs

All diagrams in the [Accrual status changed event flows](https://developers.pismo.io/pismo-docs/docs/accrual-status-changed-event-flows) guide were updated.

#### Docs

The text and the diagram in the [Over-limit fees - Example](https://developers.pismo.io/pismo-docs/docs/over-limit-fee#example) section were updated to correct some errors.

</summary>

<summary class="tabContent" id="Digital lending">

### Lending

#### New

The new [Disburse loan V2](https://developers.pismo.io/pismo-docs/reference/disburseloanv2) endpoint is now available in beta release.

#### Docs

The lending loan repayment response for the [List account loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2) endpoint was updated to include loan rates that have annual interest rate and effective annual and monthly costs.

#### Docs

A typographical error was corrected on the [Get loan details](https://developers.pismo.io/pismo-docs/reference/getloandetails) endpoint documentation.

</summary>

<summary class="tabContent" id="Resources">

### Control Center

#### Docs

All references to legacy sign on procedures were removed as all users have been migrated to use the new sign on procedures.

* [Get started with Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center)
* [Navigating Control Center](https://developers.pismo.io/pismo-docs/docs/control-center-navigation)
* [Reset your password](https://developers.pismo.io/pismo-docs/docs/password-self-reset-control-center)
* [Create and edit users](https://developers.pismo.io/pismo-docs/docs/add-a-user)

</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /wallet/v2/cards` (`post-v2-card`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` (`post-v1-card-reissue`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `PUT /pcicards/v1/pcicards/cards/{cardId}/pan` (`put-v1-update-pan-nominal`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--issuer-pan-pin |
| `PUT /pcicards/v1/pcicards/cards/noname/{cardId}/pan` (`put-v1-update-pan-noname`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--issuer-pan-pin |
| `POST /acquisitions/v3/s2s/applications` (`post-acquisitions-v3-s2s-applications`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v1/programs/{programId}/calendar-strategies` (`CreateProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `PATCH /accounts/v1/accounts/{accountId}` (`patch-accounts-v1-accounts`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /v2/migrations/accounts` (`PostAccountsV2`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--account-migration |
| `POST /v1/migrations/cards-pci` (`PostPciCardsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /v1/migrations/cards` (`PostCardsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /v1/migrations/customers` (`PostCustomersV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--customer-migration |
| `PATCH /orgs-core/v1/orgs` (`patch-v1-orgs`) | `api-specs/Platform_setup_-_Organizations.yaml` | no | KU-API-platform-setup-organizations--orgs |
| `POST /orgs-operation/v1/processing-codes` (`CreateProcessingCode`) | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `GET /orgs-core/v1/orgs/{id}` (`get-v1-org`) | `api-specs/Platform_setup_-_Organizations.yaml` | no | KU-API-platform-setup-organizations--orgs |
| `POST /v1/simulations` (`post-v1-simulation`) | `api-specs/Core_platform_-_Payment_methods_admin.yaml` | no | KU-API-core-platform-payment-methods-admin--simulation |
| `POST /payment-methods/v1/authorization` (`post-authorization`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /programs/v1/programs/template` (`CreateProgramBasedOnTemplate`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v2/programs/template` (`CreateProgramBasedOnTemplateAsync`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v1/programs/copy` (`CopyProgram`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /programs/v2/programs/copy` (`CopyProgramAsync`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `PATCH /programs/v1/programs/{id}` (`UpdateProgramInfo`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `GET /v2/transactions` (`ListTransactions`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `POST /v1/interest/accrual/setup` (`post-v1-interest-accrual-setup`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-accrual |
| `POST /v2/accounts/{accountId}/bank-accounts/iban` (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-iban`) | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01, KU-API-banking-bank-accounts--bank-accounts-part-02 |
| `POST /v2/accounts/{accountId}/bank-accounts/clabe` (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-clabe`) | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01, KU-API-banking-bank-accounts--bank-accounts-part-02 |
| `PUT /statements/v1/accounts/{accountId}/statements/due-date` (`UpdateStatementsDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /v1/deposits/accounts/{accountId}/attach` (`interest-bearing-v1-deposit-attach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits/programs/{programId}/attach` (`interest-bearing-v1-deposit-attach-program`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `POST /v1/savings-accounts/accounts/{accountId}/attach` (`interest-bearing-v1-savings-account-attach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/savings-accounts/programs/{programId}/attach` (`interest-bearing-v1-savings-account-attach-program`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `PATCH /v1/deposits/{productId}` (`interest-bearing-v1-patch-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v3/payments/multileg` (`corporate-v3-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `GET /v2/pix/infraction-reports/search` (`get-v2-pix-infraction-search`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01, KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `POST /pix/v1/pix/out/transfer` (`post-pix-out-transfer`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01, KU-API-instant-payments-pix-payments--pix-part-02 |
| `POST /v1/payments/fps/out` (`post-create-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` (`postAccrualTypesConfigurations`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--additional-accrual-type-configurations |
| `DELETE /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` (`deleteAccrualTypesConfigurations`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--additional-accrual-type-configurations |
| `GET /v1/accounts/{accountId}/accrual-type-rates` (`listAccountAccrualTypeRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `GET /statements-v2/v1/transactions-categories` (`listTransactionCategoryInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `POST /v1/recurring-charge-plans` (`create-recurring-charge-plan`) | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals` (`getAccountsTransactionsInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals` (`getAccountAccrualsV3`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `POST /v2/loans/{loanId}/disburse` (`disburseLoanV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--disbursements |
| `GET /v2/accounts/{accountId}/loans` (`getLoansByAccountIdV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `interest-bearing-v1-create-maturity-instruction-override` | Create maturity instruction override | not found in the current OpenAPI specifications. Name-based inference: link text "Create maturity instruction override" equals the endpoint name "Create maturity instruction override" in the removed-endpoints list (row Banking / Interest-bearing accounts, date removed `7/12/2026`). This is a match on the endpoint name, not on an identifier. |
| `interest-bearing-v1-get-maturity-instruction-override` | Get maturity instruction override | not found in the current OpenAPI specifications. Name-based inference: link text "Get maturity instruction override" equals the endpoint name "Get maturity instruction override" in the removed-endpoints list (row Banking / Interest-bearing accounts, date removed `7/12/2026`). This is a match on the endpoint name, not on an identifier. |
| `interest-bearing-v1-update-maturity-instruction-override` | Update maturity instruction override | not found in the current OpenAPI specifications. Name-based inference: link text "Update maturity instruction override" equals the endpoint name "Update maturity instruction override" in the removed-endpoints list (row Banking / Interest-bearing accounts, date removed `7/12/2026`). This is a match on the endpoint name, not on an identifier. |
| `interest-bearing-v1-delete-maturity-instruction-override` | Delete maturity instruction override | not found in the current OpenAPI specifications. Name-based inference: link text "Delete maturity instruction override" equals the endpoint name "Delete maturity instruction override" in the removed-endpoints list (row Banking / Interest-bearing accounts, date removed `7/12/2026`). This is a match on the endpoint name, not on an identifier. |
| `getloandetails` | Get loan details | not found in the current OpenAPI specifications. Name-based inference: link text "Get loan details" equals the endpoint name "Get loan details" in the removed-endpoints list (row Lending v1 / Create, simulate, manage loans, date removed `7/1/2026`). This is a match on the endpoint name, not on an identifier. |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/7-november-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/7-november-2025 | `5d1b719ddf8be28d…` | not stated |

## Related knowledge units

- `KU-API-banking-bank-accounts--bank-accounts-part-01` — API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)
- `KU-API-banking-bank-accounts--bank-accounts-part-02` — API reference: Banking - Bank accounts — Bank accounts (part 2 of 2)
- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-bearing-accounts--program-attachment` — API reference: Banking - Interest-bearing accounts — Program attachment
- `KU-API-banking-interest-engine--interest-accrual` — API reference: Banking - Interest engine — Interest accrual
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--issuer-pan-pin` — API reference: Card issuing - Cards — Issuer PAN/PIN
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-core-platform-payment-methods-admin--simulation` — API reference: Core platform - Payment methods admin — Simulation
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-02` — API reference: Instant payments - Pix payments — Pix (part 2 of 2)
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-API-lending--disbursements` — API reference: Lending — Disbursements
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-migrations--account-migration` — API reference: Migrations — Account migration
- `KU-API-migrations--card-migration` — API reference: Migrations — Card migration
- `KU-API-migrations--customer-migration` — API reference: Migrations — Customer migration
- `KU-API-platform-setup-organizations--orgs` — API reference: Platform setup - Organizations — Orgs
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-calendar-management--program-calendar-strategies` — API reference: Revolving credit - Calendar management — Program calendar strategies
- `KU-API-revolving-credit-configurations--account-accrual-rates` — API reference: Revolving credit - Configurations — Account accrual rates
- `KU-API-revolving-credit-configurations--additional-accrual-type-configurations` — API reference: Revolving credit - Configurations — Additional accrual type configurations
- `KU-API-revolving-credit-recurring-charges--recurring-charge-plans` — API reference: Revolving credit - Recurring charges — Recurring charge plans
- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
