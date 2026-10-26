---
ku_id: KU-CHG-9-january-2026
title: 'Changelog: 9 January 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/9-january-2026.md
  sha256: 0b960a1673d9d02d3b9b96c51ad25a7d4ff108a3dc12ae5e4c915a4d305f1058
  url: https://developers.pismo.io/pismo-docs/changelog/9-january-2026
  role: changelog_post
  updated_at: ''
operations:
- ChangeAccountCollectionStatus
- CreateInstallmentAdvancementV2
- CreateProgramCalendarStrategy
- CycleClosingRequest
- GetCreditorOperationById
- GetInstallmentAdvancementV2ById
- GetTransactionById
- ListTransactions
- cancelInstallmentAdvanceV2
- corporate-delete-v2-operation-block-id
- corporate-v2-post-cancel-payments
- corporate-v2-post-confirm-payments
- corporate-v2-post-payments
- corporate-v3-post-multileg-payments
- create-payment-agreement-simulation
- createRepaymentHierarchyV2
- delete-schedule
- get-all-schedules
- get-network-authorizations
- get-payment-agreement-simulation
- get-schedule
- get-schedule-executions
- get-v1-attribute-groups
- get-v1-attribute-groups-groupId
- get-v1-disputes-disputeId
- getByStatementId
- getInterestAccrualSummarization
- getLoanProductsV2
- getLoanV2
- getMarketplaceById
- getRepaymentHierarchyV2
- listAccountAccrualTypeRates
- patch-corporate-v2-earmarks-earmarkid
- patch-schedule
- patch-v2-pix-infraction
- post-acquisitions-v3-s2s-applications
- post-bulk-pre-schedules
- post-corporate-v1-restricted-funds
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-execute-pre-schedule
- post-generate-embossing-encrypted-noname
- post-generate-embossing-no-iv
- post-generate-embossing-noname
- post-pre-schedules
- post-v1-accounts-flex-controls
- post-v1-attribute-group-flex-controls
- post-v1-create-single-schedule
- post-v1-create-transfer-schedules
- post-v1-disputes-disputeId-forms
- postAccountAccrualTypesRates
- postAccrualTypesRates
- put-v1-interest-account
- registerRepaymentV2
- token_connet_push_multiple_accounts
- update-v1-attribute-groups
- updateMarketplace
- v4-get-account-reason
- v4-post-account-reason
related_kus:
- KU-API-banking-interest-engine--account-interest
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--operations-blocks
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-card-issuing-authorization--authorizations
- KU-API-card-issuing-cards--embossing-encrypted
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--disputes-part-02
- KU-API-card-issuing-disputes--supporting-forms
- KU-API-card-issuing-tokenization--mdes-token-connect-beta
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--statuses-and-reasons
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-flex-controls--attribute-groups
- KU-API-core-platform-payment-scheduler-beta--schedules
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-lending--repayment-hierarchy
- KU-API-lending--repayments
- KU-API-revolving-credit-calendar-management--close-account-cycle
- KU-API-revolving-credit-calendar-management--program-calendar-strategies
- KU-API-revolving-credit-configurations--account-accrual-rates
- KU-API-revolving-credit-configurations--program-accrual-rates
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation
- KU-API-revolving-credit-statements--account
- KU-API-revolving-credit-statements--accruals
- KU-API-revolving-credit-statements--statement
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-API-seller-management-sellers--marketplace
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 9 January 2026
coverage_window: 5 December 2025 and 9 January 2026
---

# Changelog: 9 January 2026

**KU ID:** `KU-CHG-9-january-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **9 January 2026** (changes between 5 December 2025 and 9 January 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

## Topics covered

Core platform - Flex controls; Core platform - Payments; Core platform - Security; Data and reporting; Card issuing - Card tokenization; Card issuing - Statements; Control Center; Core banking; Seller management; Accounts; Flexible transaction controls; General; Migrations; Payments; Security; Setup; Support; Transactions; Events; Banking operations; Integrated payments; Instant payments; Transaction banking; Authorizations; Card network integration; Disputes; Embossing; Instant payments; Statements; Lending; Migrations; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/9-january-2026

<!-- source:begin path=changelog/9-january-2026.md part=0-end -->

# 9 January 2026

Changes between 5 December 2025 and 9 January 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### Core platform - Flex controls

  #### New

  Flexible transaction controls now support attribute groups, which allow you to define sets of values, such as merchant IDs or Merchant Category Codes (MCCs), that can be shared across multiple controls within the same organization. This feature simplifies control configuration and significantly improves maintainability.

  The following new endpoints are available:

  * [Create attribute group](https://developers.pismo.io/pismo-docs/reference/post-v1-attribute-group-flex-controls)
  * [List attribute groups](https://developers.pismo.io/pismo-docs/reference/get-v1-attribute-groups)
  * [Get attribute group](https://developers.pismo.io/pismo-docs/reference/get-v1-attribute-groups-groupid)
  * [Update attribute group](https://developers.pismo.io/pismo-docs/reference/update-v1-attribute-groups)

  For more information, refer to the [Attribute groups](https://developers.pismo.io/pismo-docs/docs/attribute-groups) guide.

  ### Core platform - Payments

  #### New

  The payment scheduler functionality is now available in general release and with additional endpoints and features. In addition to the [creating](https://developers.pismo.io/pismo-docs/reference/post-pre-schedules) and [executing](https://developers.pismo.io/pismo-docs/reference/post-execute-pre-schedule) a **pre-schedule**, which was previously supported in beta release, you can now also [create bulk pre-schedules](https://developers.pismo.io/pismo-docs/reference/post-bulk-pre-schedules). In addition, the following endpoints are now available and support schedules of **single** and **transfer** type.

  * [Create single schedule](https://developers.pismo.io/pismo-docs/reference/post-v1-create-single-schedule)
  * [Create transfer schedule](https://developers.pismo.io/pismo-docs/reference/post-v1-create-transfer-schedules)
  * [List account schedules](https://developers.pismo.io/pismo-docs/reference/get-all-schedules)
  * [Get schedule](https://developers.pismo.io/pismo-docs/reference/get-schedule)
  * [List schedule executions](https://developers.pismo.io/pismo-docs/reference/get-schedule-executions)
  * [Update schedule](https://developers.pismo.io/pismo-docs/reference/patch-schedule)
  * [Cancel schedule](https://developers.pismo.io/pismo-docs/reference/delete-schedule)

  For more information, refer to the [Payment scheduler](https://developers.pismo.io/pismo-docs/docs/payment-scheduler) guide.

  ### Core platform - Security

  #### New

  New security guides are now available: [Pismo platform security guide](https://developers.pismo.io/pismo-docs/docs/pismo-platform-security-guide) and two sub-guides [Security audit, testing, and incident response](https://developers.pismo.io/pismo-docs/docs/security-audit-testing-and-incident-response) and [Compliance, certifications, and security teams](https://developers.pismo.io/pismo-docs/docs/certifications-compliance-and-security-teams). These guides offer a high-level understanding of the security Pismo provides for the Pismo platform. This includes topics such as access management, data and information management, backup and recovery, and much more.

  ### Data and reporting

  #### New

  Regulatory scheduled reports are now available for the United States. A new guide, [Reports for the United States](https://developers.pismo.io/pismo-docs/docs/reports-for-the-united-states), lists and describes them.

  ### Card issuing - Card tokenization

  #### New

  There is a new [MDES Token Connect](https://developers.pismo.io/pismo-docs/reference/token_connet_push_multiple_accounts) API and [guide](https://developers.pismo.io/pismo-docs/docs/mdes-token-connect) to support Mastercard’s [Token Connect](https://developer.mastercard.com/mdes-token-connect/documentation/#overview) service. Pismo acts as a pass-through proxy for this service and Pismo’s API endpoints mirror Mastercard’s endpoints. Token Connect is a framework within Mastercards’s Digital Enablement Service that allows issuers (card-issuing banks) to directly push a tokenized version of a customer's card (for example, their debit or credit card) to digital wallets and merchant platforms.

  ### Card issuing - Statements

  #### New

  The new installment advancement functionality is now available in beta release, giving you early access to explore its capabilities and share feedback. This functionality supports two new modes:

  * ALL\_CONTRACTS: Advances all future installments for all installment agreements in the account.
  * MULTIPLE\_CONTRACTS: Advances installments for specific contracts with individual configurations.

  The following endpoints are available in beta release:

  * [Create installment advancement (v2)](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancementv2)
  * [Get installment advancement (v2)](https://developers.pismo.io/pismo-docs/reference/getinstallmentadvancementv2byid)
  * [Cancel installment advancement (v2)](https://developers.pismo.io/pismo-docs/reference/cancelinstallmentadvancev2)

  #### New

  The new “Revolving credit - Statement refinancing” section with subsection “Payment agreement simulation” is now available. It contains the following endpoints:

  * [Create payment agreement simulation](https://developers.pismo.io/pismo-docs/reference/create-payment-agreement-simulation)
  * [Get payment agreement simulation](https://developers.pismo.io/pismo-docs/reference/get-payment-agreement-simulation)

  #### New

  The new [Close account cycle](https://developers.pismo.io/pismo-docs/reference/cycleclosingrequest) endpoint is now available in beta release.

  ### Control Center

  #### New

  The Control Center homepage was redesigned to keep the essentials front and center.

  **What’s changed?**

  * What’s new section—gives you quick insight into upcoming features, key changes, and any pending actions (like requests and approvals).
  * Refined design—makes scanning simpler and helps you stay focused on what matters most.
  * Direct access to the Pismo Developers Portal— provides deeper technical resources.

  **What hasn’t changed?**

  The key features you rely on remain the same:

  * Your program data
  * Your favorites
  * Navigation: the main menu, organization menu, and header

  Read more about these changes in [Navigating Control Center](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#homepage).

  #### New

  There is now a quick and easy way to unblock cards without waiting for timeouts directly from the Pismo Control Center. When a cardholder enters the wrong PIN too many times, their card gets temporarily blocked. With this new feature, you can reset the PIN try count and instantly unblock the card—right from the Accounts -> cards section in Control Center. This feature supports dual approval: one person initiates the request, and another reviews and approves it. With dual approval, the change only takes effect after approval, ensuring full control and compliance. Learn more about this feature in the [Card information](https://developers.pismo.io/pismo-docs/docs/card-information#unblock-card-when-pin-try-count-has-been-exceeded) guide and the [Dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval) guide.

  ### Core banking

  #### Docs

  The [Bank statements](https://developers.pismo.io/pismo-docs/docs/bank-statements-1) guide is now available. This guide explains how the Pismo platform generates and manages bank statements through cycle closing—its continuous, configurable process for capturing daily account balances, producing balance history, and supporting accurate reporting across business and non‑business days.

  ### Seller management

  #### New

  The Seller management, Marketplace API has three new endpoints. These new endpoints allows you to create a new marketplace, retrieve marketplace information by its ID, and update marketplace information.

  * [Create marketplace](https://developers.pismo.io/pismo-docs/docs/createmarketplace)
  * [Get marketplace](https://developers.pismo.io/pismo-docs/reference/getmarketplacebyid)
  * [Update marketplace](https://developers.pismo.io/pismo-docs/reference/updatemarketplace)
</summary>

<summary class="tabContent" id="Core platform">
  ### Accounts

  #### Updated

  A `currency_numeric_code` field was added to the `account` object in the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint. This is the ISO 4217 code for the account's currency. If not defined, the Pismo platform uses the program currency code. If not defined at the program level, the platform uses the currency code defined at the organization level.

  An `allowed_operations` enum field was added to the [Create status reason](https://developers.pismo.io/pismo-docs/reference/v4-post-account-reason) endpoint. It is now also now returned from the [List status reasons](https://developers.pismo.io/pismo-docs/reference/v4-get-account-reason) endpoint. This field is used to determine what operations an account is allowed to do given its status.

  ### Flexible transaction controls

  #### Docs

  The description of the `entry_mode` field description on the [flex controls](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) endpoints was updated to provide  details about the Visa and Mastercard field and code specifications.

  ### General

  #### Docs

  The [Welcome to Pismo](https://developers.pismo.io/pismo-docs/docs/welcome) page was updated to include Control Center and link to more developer guides.

  #### Docs

  BIN descriptions were updated throughout [documentation](https://developers.pismo.io/pismo-docs/docs/setup-overview#program) to indicate that it refers to the first six to eight numbers on a payment card.

  ### Migrations

  #### Docs

  The **Accruals** and **Balance** sections in the [Migrations](https://developers.pismo.io/pismo-docs/docs/migrations-overview) guide were removed.

  ### Payments

  #### Docs

  The [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations) guide was updated to correct a typographical error and display in tables.

  ### Security

  #### Docs

  The link to Generating a JWT in the `token` field of the [Get OpenID access token](https://developers.pismo.io/pismo-docs/reference/post-passport-v1-oauth2-token-1) endpoint was fixed.

  ### Setup

  #### Updated

  A new program parameter **Allow overriding the minimum amount due for the current statement** was added to the table in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide.

  #### Docs

  A line was added to the description for the **Interest rate period** program parameter in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) table.

  ### Support

  #### Docs

  The [Incident lifecycle](https://developers.pismo.io/pismo-docs/docs/incident-lifecycle) guide was updated to include a diagram of the incident lifecycle workflow.

  #### Docs

  The [Pismo operations status](https://developers.pismo.io/pismo-docs/docs/pismo-operations-status) guide was updated to include the timelines for sending out scheduled and emergency status messages.

  ### Transactions

  #### Docs

  The description of the `card` object in the response of the [Get transaction](https://developers.pismo.io/pismo-docs/reference/gettransactionbyid) and [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions) endpoints was updated with clarifications how the field is populated for different types of transactions.

  #### Docs

  In the [Transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes) guide, the descriptions of the 604 and 512 transaction types and 0001 processing code were standardized.
</summary>

<summary class="tabContent" id="Data">
  ### Events

  #### Updated

  Two new values were added to the `trigger_reason` field of the [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1) event:

  * `INTEREST_POSTED`: Triggered when interest is posted to the account
  * `INTEREST_ACCRUED`: Emitted when interest is accrued on the account

  #### Docs

  A note was added to the description of the [Delinquent account closed](https://developers.pismo.io/events/docs/delinquent-account-delinquent-account-1) event.

  #### Docs

  The [Setting up an additional event subscriber](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery) section within Data and Reporting was revised to align with the GRC policy. External systems or organizations outside Pismo are not allowed as additional subscribers. This avoids misconfigurations and non-compliant solution designs.
</summary>

<summary class="tabContent" id="Banking">
  ### Banking operations

  #### Updated

  Two new body parameters were added to the [Update account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account) endpoint: `taxes_exemption` and `fee_processing_code`.

  ### Integrated payments

  #### Fixed

  The **Perform cash-in** endpoint is removed from the Integrated payments API reference, as it was intended for internal use only.

  ### Instant payments

  #### New

  Pix payments has a new endpoint - [Update infraction report](https://developers.pismo.io/pismo-docs/reference/patch-v2-pix-infraction) - that allows the caller to update some fields in an infraction report.

  #### New

  There is a new event - [Pix internal transaction reported](https://developers.pismo.io/events/docs/pix-pix-internal-transaction-report-1) - generated when a Pix internal transaction occurs and is reported. You can use this event to track internal Pix transaction progress, completion, or failure.

  ### Transaction banking

  #### Updated

  A new error code, `WEAM0046 (Invalid account currency code)`, is now available. This error is returned when a client provides a literal currency code instead of a numeric one—for example, entering `USD` instead of `840`. This code was added to the following endpoints: 

  * [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
  * [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
  * [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)

  #### Updated

  A second error code, `WPMT0056 (Invalid account currency code: 999)`, was added for the same validation in the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint.

  #### Updated

  For the [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments) endpoint, two additional error codes were introduced to handle credit and debit legs separately:

  * `WMLP1043` for credit legs
  * `WMLP0005` for debit legs

  #### Updated

  The [Create fund restriction](https://developers.pismo.io/pismo-docs/reference/post-corporate-v1-restricted-funds) endpoint now includes the error code `WRFO0013` to enforce the same rule.

  #### Updated

  The new optional `business_date` field was added to the [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments) endpoint, consistent with the field of the same name in the payments API.

  Key behavior:

  * Defaults to the current business date.
  * Allows the client to submit a business date to confirm a future‑dated payment pre‑authorization.
  * Accepts dates within the range D‑1 to D+1.

  #### Updated

  The [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments) and [Cancel payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-cancel-payments) endpoints now include the same business‑date validation errors used in the payments API, with one exception:

  * `WPMT0057 : Cannot instantly cancel when original business date is after the current date`

  This is a new error specific to [Cancel payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-cancel-payments). It occurs when you attempt to cancel a future‑dated payment using `cancellation_method=INSTANT`.

  #### Updated

  The new optional `cancellation_method` field was added to the [Cancel payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-cancel-payments) endpoint. It supports the following values:

  * `instant` (default): Reverts the payment and updates balances using the current business date.
  * `original_dates`: Reverts the payment and updates balances using the payment’s original dates (`business_date` and `payment_datetime`).

  #### Updated

  For the [Revoke operation block](https://developers.pismo.io/pismo-docs/reference/corporate-delete-v2-operation-block-id) endpoint, the following error was introduced to indicated that the operation block you are attempting to deactivate is already inactive:

  * `WOBK0009: Operation block is not active`
</summary>

<summary class="tabContent" id="Card issuing">
  ### Authorizations

  #### Updated

  The [List account authorizations](https://developers.pismo.io/pismo-docs/reference/get-network-authorizations) endpoint has two new fields, `merchant_category_id` and `processing_code`, returned with network authorization query results.

  ### Card network integration

  #### Docs

  The [Full balance versus Zero balance integration](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance) guide was updated in the following ways.

  * Included support for flexible transaction controls in Zero balance integration.
  * Corrected link to and added clarifying details in the [Accounting management](https://developers.pismo.io/pismo-docs/docs/full-balance-versus-zero-balance#accounting-management) section.

  #### Docs

  The [Simulate authorizations](https://developers.pismo.io/pismo-docs/docs/simulate-authorizations) guide was updated to include entry mode information with a link to the Validation code definitions guide with full details of the possible entry mode codes.

  #### Docs

  The [FRH-POS (point-of-sale) entry mode validation](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#frh---pos-point-of-sale-entry-mode-validation) description in the Validation code definitions guide was updated to correctly reflect that the entry mode field for Visa is field 22.

  #### Docs

  The [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events) guide was updated to correctly reflect that the Network authorization ISO8583 message event and the Network authorization received event are sent to both Full and Zero balance issuers. The same correction was made to the [Authorization/Base I workflow](https://developers.pismo.io/pismo-docs/docs/full-and-zero-balance-workflows#authorizationbase-i) in the Full and Zero balance transaction workflows guide.

  ### Disputes

  #### Updated

  For the [Get dispute](https://developers.pismo.io/pismo-docs/reference/get-v1-disputes-disputeid) endpoint, the `form` field in the response is a string but was incorrectly listed as an object. This string contains many objects and properties though. In the [Create dispute form](https://developers.pismo.io/pismo-docs/reference/post-v1-disputes-disputeid-forms) endpoint, the `form` field is an object and you can view its objects and properties to see what is returned as a string in [Get dispute](https://developers.pismo.io/pismo-docs/reference/get-v1-disputes-disputeid).

  ### Embossing

  #### New

  The “Cards issuing - Cards > Embossing” section is now 3 sections - **Embossing**, **Embossing data**, and **Embossing encrypted**.

  Three new endpoints were added to the **Embossing encrypted** section:

  * [Get nominal encrypted card data for embossing V2](https://developers.pismo.io/pismo-docs/reference/post-generate-embossing-no-iv)
  * [Get noname encrypted card data for embossing](https://developers.pismo.io/pismo-docs/reference/post-generate-embossing-encrypted-noname)
  * [Get noname encrypted card data for embossing V2](https://developers.pismo.io/pismo-docs/reference/post-generate-embossing-noname)

  The **Embossing encrypted** endpoints are for issuers who want to do their own embossing and need a card’s encrypted data as per regulations. For the V2 endpoints, the initial vector (iv) field is not passed but is Pismo-generated and returned in the response.

  #### Docs

  A section about IPK certificates has been added to the [Physical card embossing](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing) guide. An [Issuer Public Key](https://en.wikipedia.org/wiki/Public_key_certificate) (IPK) Certificate is a digital certificate used in financial transactions, especially with Visa contactless cards, containing an issuer's public key. Pismo does not provide the IPK; the issuer or network, likely the issuer, is responsible for it. Providing this certificate falls outside Pismo's scope.

  ### Instant payments

  #### Docs

  There is a new [Faster Payments System](https://developers.pismo.io/pismo-docs/docs/faster-payment-system) (FPS) guide. FPS is an instant payments service in the United Kingdom. This guide documents Pismo services for FPS integration in the UK, their architectural approach, its major transaction flows, and the end-to-end process for connecting to FPS using the Pismo platform.

  ### Statements

  #### Updated

  The new `ranges` property was added to the body parameters and 200 responses in the following endpoints.

  * [Configure program accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccrualtypesrates)
  * [Configure account accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates)

  #### Updated

  The new query parameters `beginDueDate`, `endDueDate`, and `maxClosedCycles` were added to the [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid) endpoint.

  #### Docs

  Description of the [Update account collection status](https://developers.pismo.io/pismo-docs/reference/changeaccountcollectionstatus) endpoint was updated.

  #### Docs

  The first two paragraphs of the [Credit liquidation](https://developers.pismo.io/pismo-docs/docs/credit-liquidation) guide were updated to remove duplicated information.

  #### Docs

  The description for the [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) endpoint was updated.

  #### Docs

  The first bullet point in [How the program discharges transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-discharges-transactions) was updated to clarify information.

  #### Docs

  A note was added to the descriptions of `default_rate` and `rate_if_overdue` in the body parameters and 200 response of the [Configure account accrual rates](https://developers.pismo.io/pismo-docs/reference/postaccountaccrualtypesrates) endpoint and in the 200 response of the [List account accrual rates](https://developers.pismo.io/pismo-docs/reference/listaccountaccrualtyperates) endpoint.

  #### Docs

  The items field in the 200 response for the [Get interest accrual summary](https://developers.pismo.io/pismo-docs/reference/getinterestaccrualsummarization) endpoint was incorrectly documented as an object. It should be an array of objects. The documentation was updated accordingly.
</summary>

<summary class="tabContent" id="Digital lending">
  ### Lending

  #### New

  The following new v2 endpoints are now available in beta release. They will eventually replace the v1 endpoints.

  * [Register repayment](https://developers.pismo.io/pismo-docs/reference/registerrepaymentv2)
  * [Get repayment hierarchy](https://developers.pismo.io/pismo-docs/reference/getrepaymenthierarchyv2)
  * [Create repayment hierarchy](https://developers.pismo.io/pismo-docs/reference/createrepaymenthierarchyv2)
  * [Get loan](https://developers.pismo.io/pismo-docs/reference/getloanv2)
  * [List loan products](https://developers.pismo.io/pismo-docs/reference/getloanproductsv2)
</summary>

<summary class="tabContent" id="Seller management">
  ### Migrations

  #### Updated

  The new `fees` field was added to the [Get creditor operation](https://developers.pismo.io/pismo-docs/reference/getcreditoroperationbyid) endpoint.
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### New

  The [Export user list](https://developers.pismo.io/pismo-docs/docs/export-user-list) functionality was added to Control Center. If you have the Admin or User manager role, you can export the list of an organization’s users as a CSV file. The exported user list contains information useful for auditing and reporting purposes.

  #### Docs

  The [Card network tokenization](https://developers.pismo.io/pismo-docs/docs/card-network-tokenization#create-a-card-network-tokenization-configuration) guide for Control Center was updated to note that a Service Desk request is necessary to configure anti-fraud webhooks within Control Center.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/attribute-groups` (`post-v1-attribute-group-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--attribute-groups |
| `GET /v1/attribute-groups` (`get-v1-attribute-groups`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--attribute-groups |
| `GET /v1/attribute-groups/{groupId}` (`get-v1-attribute-groups-groupId`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--attribute-groups |
| `PATCH /v1/attribute-groups/{groupId}` (`update-v1-attribute-groups`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--attribute-groups |
| `POST /v1/pre-schedules` (`post-pre-schedules`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/accounts/{accountId}/pre-schedules/{scheduleId}/execute` (`post-execute-pre-schedule`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/pre-schedules/bulk` (`post-bulk-pre-schedules`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/schedules` (`post-v1-create-single-schedule`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/transfers` (`post-v1-create-transfer-schedules`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `GET /v1/accounts/{accountId}/schedules` (`get-all-schedules`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `GET /v1/accounts/{accountId}/schedules/{scheduleId}` (`get-schedule`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `GET /v1/accounts/{accountId}/schedules/{scheduleId}/executions` (`get-schedule-executions`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `PATCH /v1/accounts/{accountId}/schedules/{scheduleId}` (`patch-schedule`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `DELETE /v1/accounts/{accountId}/schedules/{scheduleId}` (`delete-schedule`) | `api-specs/Core_platform_-_Payment_scheduler_beta.yaml` | no | KU-API-core-platform-payment-scheduler-beta--schedules |
| `POST /v1/token-connect/push-multiple-accounts` (`token_connet_push_multiple_accounts`) | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--mdes-token-connect-beta |
| `POST /v2/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancementV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `GET /v2/accounts/{accountId}/installment-advance/{advancementId}` (`GetInstallmentAdvancementV2ById`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `DELETE /v2/accounts/{accountId}/installment-advance/{advancementId}` (`cancelInstallmentAdvanceV2`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | no | KU-API-revolving-credit-installment-management--installment-advancements |
| `POST /v1/accounts/{accountId}/payment-agreement-simulations` (`create-payment-agreement-simulation`) | `api-specs/Revolving_credit_-_Statement_refinancing_API.yaml` | no | KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation |
| `GET /v1/accounts/{accountId}/payment-agreement-simulations/{paymentAgreementSimulationId}` (`get-payment-agreement-simulation`) | `api-specs/Revolving_credit_-_Statement_refinancing_API.yaml` | no | KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation |
| `POST /v1/accounts/{accountId}/statement-close` (`CycleClosingRequest`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--close-account-cycle |
| `GET /v3/marketplaces/{marketplaceId}` (`getMarketplaceById`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace |
| `PATCH /v1/marketplaces/{marketplaceId}` (`updateMarketplace`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--marketplace |
| `POST /acquisitions/v3/s2s/applications` (`post-acquisitions-v3-s2s-applications`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /accounts/v4/reasons` (`v4-post-account-reason`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `GET /accounts/v4/reasons` (`v4-get-account-reason`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--statuses-and-reasons |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `GET /v2/transactions/{transactionId}` (`GetTransactionById`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `GET /v2/transactions` (`ListTransactions`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `PUT /v1/interest/account/{accountId}` (`put-v1-interest-account`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--account-interest |
| `PATCH /v2/pix/infraction-reports/{id}` (`patch-v2-pix-infraction`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01, KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v3/payments/multileg` (`corporate-v3-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v1/restricted-funds` (`post-corporate-v1-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `POST /corporate/v2/payments/confirm` (`corporate-v2-post-confirm-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/cancel` (`corporate-v2-post-cancel-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `DELETE /corporate/v2/operations-blocks/{operationsBlockId}` (`corporate-delete-v2-operation-block-id`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--operations-blocks |
| `GET /direct-network-transactions/v1/authorizations/desc` (`get-network-authorizations`) | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `GET /v1/disputes/{disputeId}` (`get-v1-disputes-disputeId`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01, KU-API-card-issuing-disputes--disputes-part-02 |
| `POST /v1/disputes/{disputeId}/forms` (`post-v1-disputes-disputeId-forms`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--supporting-forms |
| `POST /embossing/v2/cards/generate-embossing` (`post-generate-embossing-no-iv`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-encrypted |
| `POST /embossing/v1/cards/generate-embossing/noname` (`post-generate-embossing-encrypted-noname`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-encrypted |
| `POST /embossing/v2/cards/generate-embossing/noname` (`post-generate-embossing-noname`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-encrypted |
| `POST /v1/programs/{programId}/accrual-type-rates` (`postAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-accrual-rates |
| `POST /v1/accounts/{accountId}/accrual-type-rates` (`postAccountAccrualTypesRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `GET /statements-v2/v3/accounts/{accountId}/statements` (`getByStatementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `PATCH /statements-v2/v1/accounts/{accountId}` (`ChangeAccountCollectionStatus`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account |
| `POST /v1/programs/{programId}/calendar-strategies` (`CreateProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `GET /v1/accounts/{accountId}/accrual-type-rates` (`listAccountAccrualTypeRates`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--account-accrual-rates |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals/summarization` (`getInterestAccrualSummarization`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `POST /v2/loans/{loanId}/repayment` (`registerRepaymentV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--repayments |
| `GET /v2/repayment-hierarchies/{hierarchyCode}` (`getRepaymentHierarchyV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--repayment-hierarchy |
| `POST /v2/repayment-hierarchies` (`createRepaymentHierarchyV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--repayment-hierarchy |
| `GET /v2/loans/{loanId}` (`getLoanV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/loan-products` (`getLoanProductsV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /marketplaces/{marketplaceId}/creditors-operations/{creditorOperationId}` (`GetCreditorOperationById`) | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-passport-v1-oauth2-token-1` | Get OpenID access token; Passport API endpoint | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/9-january-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/9-january-2026 | `0b960a1673d9d02d…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-engine--account-interest` — API reference: Banking - Interest engine — Account interest
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--operations-blocks` — API reference: Banking - Transaction banking — Operations blocks
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-card-issuing-cards--embossing-encrypted` — API reference: Card issuing - Cards — Embossing encrypted
- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--disputes-part-02` — API reference: Card issuing - Disputes — Disputes (part 2 of 2)
- `KU-API-card-issuing-disputes--supporting-forms` — API reference: Card issuing - Disputes — Supporting forms
- `KU-API-card-issuing-tokenization--mdes-token-connect-beta` — API reference: Card issuing - Tokenization — MDES Token Connect [Beta]
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--statuses-and-reasons` — API reference: Core platform - Accounts — Statuses and reasons
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-flex-controls--attribute-groups` — API reference: Core platform - Flex controls — Attribute groups
- `KU-API-core-platform-payment-scheduler-beta--schedules` — API reference: Core platform - Payment scheduler — Schedules
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-lending--repayment-hierarchy` — API reference: Lending — Repayment hierarchy
- `KU-API-lending--repayments` — API reference: Lending — Repayments
- `KU-API-revolving-credit-calendar-management--close-account-cycle` — API reference: Revolving credit - Calendar management — Close account cycle
- `KU-API-revolving-credit-calendar-management--program-calendar-strategies` — API reference: Revolving credit - Calendar management — Program calendar strategies
- `KU-API-revolving-credit-configurations--account-accrual-rates` — API reference: Revolving credit - Configurations — Account accrual rates
- `KU-API-revolving-credit-configurations--program-accrual-rates` — API reference: Revolving credit - Configurations — Program accrual rates
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-statement-refinancing-api--payment-agreement-simulation` — API reference: Revolving credit - Statement refinancing — Payment agreement simulation
- `KU-API-revolving-credit-statements--account` — API reference: Revolving credit - Statements — Account
- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-API-seller-management-sellers--marketplace` — API reference: Seller management - Sellers — Marketplace
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
