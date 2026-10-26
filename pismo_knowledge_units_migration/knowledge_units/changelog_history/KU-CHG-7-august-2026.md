---
ku_id: KU-CHG-7-august-2026
title: 'Changelog: 7 August 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/7-august-2026.md
  sha256: aef7c8860d509dca13aa13a8e6e54731b75c183c77875f8e133806e4e35c0d3e
  url: https://developers.pismo.io/pismo-docs/changelog/7-august-2026
  role: changelog_post
  updated_at: ''
operations:
- CreateProgramCalendarStrategy
- GetProgramCalendarStrategy
- GetStatementInfo
- ListProgramCalendarStrategies
- ListTransactions
- PostAccountsV2
- PostCardsV1
- PostGoLiveV1
- PostTokensV1
- UpdateProgramCalendarStrategy
- bookLoanV2
- corporate-put-bulk-file
- corporate-v2-get-multileg-payment
- corporate-v2-post-multileg-payments
- create-card-rules
- createLoanProductV2
- createPrepayment
- createRepaymentHierarchyV2
- createStatementAmountDue
- createTransactionCategory
- get-holiday-new
- get-transaction-e2e
- get-v1-benchmark-rate-b3
- get-v1-benchmark-rate-org-b3
- get-v1-interest-account
- get-v1-interest-account-b3
- get-v1-interest-plan
- get-v1-interest-plan-b3
- get-v1-interest-plans
- get-v2-pix-dict-participants
- get-v2-pix-statistics
- getAccountsTransactionsInterest_1
- getAdvancementsBySettlement
- getBusinessCategory
- getByStatementId
- getLoanProductV2
- getLoanProductsV2
- getLoanV2
- getLoansByAccountIdV2
- getRepaymentHierarchyV2
- getStatementAmountDue
- getTransactionTypes_1
- getTransactionsBalance
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-deposit-account-open
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-attach-program
- interest-bearing-v1-deposit-update-account-attachment
- interest-bearing-v1-deposit-update-program-attachment
- interest-bearing-v1-get-account-attachment
- interest-bearing-v1-get-deposit-products
- interest-bearing-v1-get-program-attachment
- interest-bearing-v1-list-products
- interest-bearing-v1-patch-deposit-product
- interest-bearing-v1-simulate-penalty
- listBusinessCategories
- listTransactionCategoryInterest
- merchants-transactions
- patch-corporate-v2-restricted-funds
- patch-v1-interest-plan
- post-acquisitions-v3-s2s-applications
- post-cancel-fps
- post-org-model-config
- post-pix-out-transfer
- post-release-fps
- post-transactions-search
- post-v1-benchmark-rate-b3
- post-v1-filter-templates
- post-v1-interest-plan
- post-v1-interest-plan-b3
- post-vau-opt-in
- post-vau-opt-out
- put-v1-interest-account
- put-v1-interest-account-b3
- retrievePaginatedLoans
- simulationConfigs
- statementDueDate
- updateLoanProductV2
- updateTransactionCategoryInterest
related_kus:
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--deposit-account-open
- KU-API-banking-interest-bearing-accounts--penalty
- KU-API-banking-interest-bearing-accounts--product
- KU-API-banking-interest-bearing-accounts--program-attachment
- KU-API-banking-interest-engine--account-interest
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-interest-management--account-interest
- KU-API-banking-interest-management--benchmark-rate
- KU-API-banking-interest-management--interest-plan
- KU-API-banking-transaction-banking--bulk-payment-files
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--restricted-funds
- KU-API-card-issuing-cards--automatic-updater
- KU-API-card-issuing-visa-flexible-credentials--rules
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balance-config-beta--filter-templates
- KU-API-core-platform-rule-models--apply
- KU-API-core-platform-transactions--transactions
- KU-API-instant-payments-pix-management--anti-fraud
- KU-API-instant-payments-pix-management--participants
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--pix-part-02
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-lending--prepayment
- KU-API-lending--repayment-hierarchy
- KU-API-migrations--account-migration
- KU-API-migrations--card-migration
- KU-API-migrations--token-migration
- KU-API-platform-setup-holidays--holiday-calendar-data
- KU-API-platform-setup-rates-and-fees--simulation
- KU-API-revolving-credit-calendar-management--program-calendar-strategies
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-API-revolving-credit-statements--statement
- KU-API-revolving-credit-statements--statement-minimum-amount-due
- KU-API-revolving-credit-statements--transaction-types
- KU-API-seller-management-merchant-advance--merchant-advancement-transaction
- KU-API-seller-management-merchants--merchant-business-category
- KU-API-seller-management-sellers--settlements
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 7 August 2026
coverage_window: 2 July and 7 August 2026
---

# Changelog: 7 August 2026

**KU ID:** `KU-CHG-7-august-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **7 August 2026** (changes between 2 July and 7 August 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated"; "Deprecated"; "Deprecated".

## Topics covered

Card issuing - Cards; Card issuing - Disputes; Card issuing - Statements; Control Center; Core platform - Balance configurations; Resources - Pismo API testing overview; General; Accounts; Client webhooks; Fee management; Holidays; Migrations; Rates and fees; Rule models; Security; Support; Transactions; Events; Banking operations; Instant payments; Payment rails; Transaction banking; Card network integration; Statements; Tokenization; Visa Flexible Credentials; Merchants; Transactions; Lending; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/7-august-2026

<!-- source:begin path=changelog/7-august-2026.md part=0-end -->

# 7 August 2026

Changes between 2 July and 7 August 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### Card issuing - Cards

  #### New

  You can now use Visa’s Automatic Updater (VAU) and Mastercard’s Automatic Billing Updater (ABU) as described in the new [Automatic updater](https://developers.pismo.io/pismo-docs/docs/automatic-updater) guide. The new API section **Card issuing - Cards > Automatic updater** includes the following two new endpoints.

  * [Automatic updater opt-out](https://developers.pismo.io/pismo-docs/reference/post-vau-opt-out) allows you to opt a card out of Visa’s Automatic Updater (VAU) or Mastercard’s Automatic Billing Updater (ABU).
  * [Visa automatic updater opt-in](https://developers.pismo.io/pismo-docs/reference/post-vau-opt-in) allows you to opt a card into VAU.

  ### Card issuing - Disputes

  #### New

  There is a new [Visa dispute use case](https://developers.pismo.io/pismo-docs/docs/visa-dispute-use-case) guide. It provides a detailed, real-world walkthrough of a Visa fraud dispute going through the full lifecycle on the Pismo platform, including every API call, state machine transition, and event generated.

  ### Card issuing - Statements

  #### New

  Five new program calendar strategies are available:

  * `MONTHLY_CYCLE_CLOSING`
  * `MONTHLY_DUE_DATE`
  * `WEEKLY_CYCLE_CLOSING`
  * `WEEKLY_DUE_DATEDAILY_CYCLE_CLOSING`
  * `DAILY_DUE_DATE`

  These strategies were added to the following endpoints:

  * [Create program calendar strategy](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) - The body params begin with a drop-down list that enables you to select the calendar strategy. Previously, `FIXED_CYCLE_CLOSING` was the only option. The new strategies were added to the list.
  * [List program calendar strategies](https://developers.pismo.io/pismo-docs/reference/listprogramcalendarstrategies) - The `strategy` body parameter includes new options.
  * [Get program calendar strategy](https://developers.pismo.io/pismo-docs/reference/getprogramcalendarstrategy) - Can return one of the new strategies.
  * [Update program calendar strategy](https://developers.pismo.io/pismo-docs/reference/updateprogramcalendarstrategy) - The body parameters begin with a drop-down list that enables you to select the calendar strategy. Previously, `FIXED_CYCLE_CLOSING` was the only option. The new strategies were added to the list.

  The following new guides have been published to address the new calendar strategies:

  * [Monthly cycle closing calendar management strategy](https://developers.pismo.io/pismo-docs/docs/monthly-cycle-closing-calendar-management-strategy)
  * [Montly due date calendar management strategy](https://developers.pismo.io/pismo-docs/docs/monthly-due-date-calendar-management-strategy)
  * [Weekly cycle closing calendar management strategy](https://developers.pismo.io/pismo-docs/docs/weekly-cycle-closing-calendar-management-strategy)
  * [Weekly due date calendar management strategy](https://developers.pismo.io/pismo-docs/docs/weekly-due-date-calendar-management-strategy)
  * [Daily cycle closing calendar management strategy](https://developers.pismo.io/pismo-docs/docs/daily-cycle-closing-calendar-management-strategy)
  * [Daily due date calendar management strategy](https://developers.pismo.io/pismo-docs/docs/daily-due-date-calendar-management-strategy)
  * [Reproducing the behavior of the fixed due date strategy](https://developers.pismo.io/pismo-docs/docs/reproducing-the-behavior-of-the-fixed-due-date-strategy)

  #### New

  You now have the option of customizing the discharge process as described in the new [Discharging transactions](https://developers.pismo.io/pismo-docs/docs/discharging-transactions) guide. The original discharge process is being maintained, insuring backward compatibility. The [Discharging transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#discharging-transactions) section of the Full balance credit program guide was updated accordingly.

  ### Control Center

  #### New

  [Card embossing](https://developers.pismo.io/pismo-docs/docs/embossing-in-control-center) is available in Control Center. With this new feature, you can:

  * Add existing embossing configurations to your programs
  * Adjust some settings, such as embossing schedules and aliases

  ### Core platform - Balance configurations

  #### New

  The new [Balance configuration filter templates](https://developers.pismo.io/pismo-docs/docs/filter-templates) guide provides step-by-step guidance how to create and manage filter templates via the new [filter templates](https://developers.pismo.io/pismo-docs/reference/post-v1-filter-templates) endpoints and use them in balance configurations. It also explains how to maintain and update filter logic efficiently.

  ### Resources - Pismo API testing overview

  #### New

  A new guide, [Access Pismo OpenAPI files on GitHub](https://developers.pismo.io/pismo-docs/docs/access-pismo-openapi-files-on-github) enables access to up-to-date OpenAPI specification files. In conjunction, the [Pismo API testing overview](https://developers.pismo.io/pismo-docs/docs/pismo-api-testing-overview) guide was updated and provides information about ways to test Pismo APIs, including OpenAPI and Postman. The [Access Pismo Postman collections](https://developers.pismo.io/pismo-docs/docs/access-pismo-postman-collections) was updated to accommodate the new Pismo API testing overview structure.
</summary>

<summary class="tabContent" id="Core platform">
  ### General

  #### Docs

  The descriptions of the `metadata` field were updated throughout the Developers Portal documentation to indicate that this field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information.

  #### Docs

  The supplementary UI icons were removed from the following guides to maintain style consistency and standards throughout the portal:

  * [Get started with Ask AI](https://developers.pismo.io/pismo-docs/docs/get-started-with-ask-ai)
  * [Interest plans](https://developers.pismo.io/pismo-docs/docs/interest-plans-in-control-center)

  ### Accounts

  #### Updated

  In the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) endpoint, the `is_centralizer` boolean field was removed from the main account application object and moved to the `account` object and renamed `centralizer`.  A centralizer account, within the account hierarchy, is the account responsible for invoice billing.

  ### Client webhooks

  #### New

  A new request field, `disableToken`, was added to the [Full balance anti-fraud webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook). This new field reflects the new token validation workflow within authorization processing and indicates when token validation has been bypassed. For the newly supported token types (Visa: `06` and Mastercard: `V`), Pismo will skip token validation as these tokens are not stored in the Pismo database.

  #### Docs

  The [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook) guide was updated to clarify the Zero balance validation webhook request field `amount_transaction` description and to properly indicate that the field is conditional and is only required when data is available.

  ### Fee management

  #### Docs

  The [Over-limit fees](https://developers.pismo.io/pismo-docs/docs/over-limit-fee) guide was updated to fix a couple of incorrect reference links.

  ### Holidays

  #### New

  The [List holidays](https://developers.pismo.io/pismo-docs/reference/get-holiday-new) endpoint has been updated with the following query parameters:

  * `name` - Holiday calendar name filter
  * `beginDate` - Return holiday calendars created after or on this date
  * `endDate` - Return holiday calendars created before or on this date
  * `page` - Return this page of data
  * `perPage` - Return this number of results per page
  * `order` - Return results in ascending or descending order
  * `orderBy` - Field to order returned results on
  * `include_parent_holidays` - Should holidays from parent calendars be returned?

  ### Migrations

  #### Updated

  The new `corporate_account` object was added to the [Migrate accounts](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint and includes fields like `status`, `account_status_reason_ext_id`, and `inactive_since`. This additional object is related to corporate banking accounts.

  #### Docs

  The Migrations > [Statements](https://developers.pismo.io/pismo-docs/docs/migrations-overview#statements) section was updated to relay statement moving window from 42 cycles to 120 cycles.

  #### Docs

  In the [Migrate cards](https://developers.pismo.io/pismo-docs/reference/postcardsv1) endpoint, the `status` body parameter was updated to show all possible enum values and to state that it is the card status at migration, not the card migration status.

  #### Docs

  In the [Migrate accounts](https://developers.pismo.io/pismo-docs/reference/postaccountsv2) endpoint, the `creation_date` body parameter was updated to show that it can accept either YYYY-MM-DD or YYYY-MM-DDTHH:DD:SSZ.

  #### Docs

  In the [Migrate tokens](https://developers.pismo.io/pismo-docs/reference/posttokensv1) endpoint, the `card_holder_name` field was updated to indicate that you pass `SKIP NETWORK CALL` to bypass network validation during sandbox testing.

  #### Docs

  In the [Migrate accounts Go-live](https://developers.pismo.io/pismo-docs/reference/postgolivev1) endpoint, the following updates were made.

  * The `status` field enum values were updated to not show a `MIGRATED` option because this endpoint is intended for accounts not yet migrated.
  * The `ACCOUNT` enum option was added to the `type` field.

  ### Rates and fees

  #### Docs

  The [Create simulation configuration](https://developers.pismo.io/pismo-docs/reference/simulationconfigs) endpoint was updated to include a more complete payload and to clarify the two options for the `day_count_method` field: `MONTH_30_YEAR_360` and `MONTH_ACTUAL_YEAR_365`.

  ### Rule models

  #### Docs

  In the [Apply](https://developers.pismo.io/pismo-docs/reference/post-org-model-config) endpoints, the model ID field was incorrectly listed as `modelId`. It was changed to `model_id`.

  ### Security

  #### Updated

  Creation of permission groups to control access to Pismo API endpoints for OIDC authentication can now be done directly through the Control Center. The [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid) guide was updated to reflect this change. In addition, the [Third-party authentication](https://developers.pismo.io/pismo-docs/docs/third-party-authentication-with-openid) guide (previously named Third-party authentication for OIDC) was rewritten to include instructions for third-party authentication for all three server authentication types.

  #### Updated

  The [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials) guide and the [Authentication with OAuth2](https://developers.pismo.io/pismo-docs/docs/authentication-with-oauth2) guide were updated to include a section on Third-party authentication.

  #### Docs

  The [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid) guide was updated with clarifying information and claims examples used when generating your JSON web token (JWT).

  ### Support

  #### Docs

  The [SFTP event file integration tutorial](https://developers.pismo.io/pismo-docs/docs/sftp-event-file-configuration-tutorial) was revised to introduce a quick-guide structure, add Service Desk routing instructions, and provide a copy-and-paste ticket template that includes required SSH public keys and IP addresses in CIDR /32 format.

  #### Docs

  The [GCP Pub/Sub tutorial](https://developers.pismo.io/pismo-docs/docs/gcp-event-configuration-tutorial) was updated to include a ticket template for Project ID and Topic Name, Service Desk routing guidance, and a streamlined quick-guide format.

  #### Docs

  The [AWS S3 file integration tutorial](https://developers.pismo.io/pismo-docs/docs/aws-event-file-configuration-tutorial) was updated to include a ticket template for Account ID, IAM Role ARN, and prerequisite checks, Service Desk routing guidance, and a streamlined quick-guide format.

  #### Docs

  The [AWS EventBridge tutorial](https://developers.pismo.io/pismo-docs/docs/aws-eventbridge-event-configuration-tutorial) was updated to include a ticket template for Account ID, EventBridge Bus ARN, and IAM Role ARN, Service Desk routing guidance, and a streamlined quick-guide format.

  #### Docs

  The [Azure Service Bus tutorial](https://developers.pismo.io/pismo-docs/docs/azure-event-configuration-tutorial) was updated to include a ticket template for Tenant ID and Topic URL, Service Desk routing guidance, and a streamlined quick-guide format.

  #### Docs

  The [GCP Cloud Storage file integration tutorial](https://developers.pismo.io/pismo-docs/docs/gcp-event-file-configuration-tutorial) was updated to include a ticket template for Project ID and Bucket Name, Service Desk routing guidance, and a streamlined quick-guide format.

  #### Docs

  The [Request a performance test tutorial](https://developers.pismo.io/pismo-docs/docs/requesting-a-performance-test) was updated to correct outdated Jira Service Desk navigation instructions and ensure the request workflow matches the current ticket categories.

  #### Docs

  The [Pismo data platform – HTTP integration guide (beta)](https://developers.pismo.io/pismo-docs/docs/pismo-data-platform-http-integration-guide-beta) was updated to add a ticket template and Service Desk routing guidance. The content was reorganized into a quick-guide format and documented the required request information: endpoint URL, certificate, certificate identifier, and maximum TPS.

  #### Docs

  The [Setting up an additional event subscriber](https://developers.pismo.io/pismo-docs/docs/setting-up-an-additional-subscriber) tutorial was updated to add a ticket template and Service Desk routing guidance. The content was reorganized into a quick-guide format and documented the required request information: source and destination organization IDs, delivery type, and cloud provider.

  #### Docs

  The [Setting up event filtering](https://developers.pismo.io/pismo-docs/docs/event-filtering) guide was updated to include a ticket template, Service Desk routing information, and a quick-start guide for configuring event filters.

  #### Docs

  The [Setting up real-time event delivery](https://developers.pismo.io/pismo-docs/docs/setting-up-real-time-event-delivery) guide was updated to include a ticket template for setup requests, Service Desk routing information, and a streamlined quick-start guide format.

  ### Transactions

  #### Updated

  In the [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) and [Transaction updated](https://developers.pismo.io/events/docs/transaction-update-1) events, the `rates.type` field max length was updated to be 40 instead of 30.

  #### Updated

  In the [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions) endpoint, the parameter `PageSize` is now allowed up to a maximum of 1000 records per page. If the `PageSize parameter` is not passed, the platform continues to consider `PageSize` = `100` as the default.
</summary>

<summary class="tabContent" id="Data">
  ### Events

  #### Docs

  The [Event data](https://developers.pismo.io/pismo-docs/docs/event-data) documentation was updated to better align with Pismo events behaviors and provide more clarity around how data events are validated. The new section [Event validation](https://developers.pismo.io/pismo-docs/docs/event-data#event-validation) was also added.
</summary>

<summary class="tabContent" id="Core banking">
  ### Banking operations

  #### New

  New fields were added to the following endpoints.

  * [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) - `capitalization_frequency` and `interest_base_model` was added to the request body parameters.
  * [List Org interest plans](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plans) - `capitalization_frequency` and `interest_base_model`  was added to the response.
  * [Get interest plan](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan) - `capitalization_frequency` and `interest_base_model`  was added to the response.
  * [Update account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account) - `capitalization_frequency` to  was added to the request body parameters.
  * [Get account interest](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account) - `capitalization_frequency` was added to the response.

  #### Updated

  The `interest_by_tiers` object was added to body parameters of the [Update account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account) endpoint.

  #### Updated

  The Interest‑bearing accounts API now includes `interest_capitalization_mode`, which allows you to specify whether capitalized interest should be paid out to the payout account (`PAYOUT`) or reinvested into principal (`REINVEST`). This explicit setting replaces inference‑based behavior and applies across the following endpoints.

  * [Get account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-account-attachment)
  * [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account)
  * [Update deposit account attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment)
  * [Get program attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-program-attachment)
  * [Attach deposit product to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-program)
  * [Update deposit program attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-program-attachment)

  #### Updated

  The [Open deposit account](https://developers.pismo.io/pismo-docs/reference/nterest-bearing-v1-deposit-account-open) endpoint introduced the `account_creation_datetime` field, which allows you to create accounts with an earlier effective date. This enables retroactive deposits and back‑dated interest calculation.

  #### Updated

  The following new fields were added to the 201 response payload of the [Open deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-account-open) endpoint. They provide additional detail about the status of the newly created deposit account.

  * `payout_account`
  * `maturity_instructions`
  * `penalties`

  #### Updated

  The following endpoints are no longer in beta release.

  * [Simulate penalty](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-simulate-penalty)
  * [Get account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-account-attachment)
  * [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account)
  * [Get program attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-program-attachment)
  * [Attach deposit product to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-program)
  * [Update deposit account attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment)
  * [Update deposit program attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-program-attachment)

  #### Updated

  The following endpoints now include or return a `notices` object. This object lets you know that you may renew, withdraw, or modify deposit terms before the maturity date.

  * [List products](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-list-products)
  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Update deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-patch-deposit-product)
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products)

  #### Updated

  The description of `grace_period_duration_days` in the following endpoints was updated to clarify that the grace‑period expiration is scheduled using the account’s division timezone. The Pismo platform applies the parent division’s timezone when available, and defaults to UTC when no division timezone is defined:

  * [List products](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-list-products)
  * [Create deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-create-deposit-product)
  * [Get deposit product](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-deposit-products)

  #### Deprecated

  The following endpoints were originally scheduled for decommission on 6 August 2026. Their decommission date for both test and production environments was updated to 6 November 2026. For details, refer to the [API endpoint deprecation and removal schedule](https://developers.pismo.io/pismo-docs/docs/api-endpoint-deprecation-and-removal-schedule).

  * [Post multi-leg payment v2](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments)
  * [Get multi-leg payment status v2](https://developers.pismo.io/pismo-docs/reference/corporate-v2-get-multileg-payment)

  #### Deprecated

  The following endpoints were decommissioned on 12 July 2026 and removed from the Interest-bearing accounts API.

  * `POST /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides`
  * `PATCH /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides`
  * `DELETE /v1/deposits/:productId/accounts/:accountId/maturity-instructions/overrides`
  * `GET /v1/deposits/accounts/:accountId/maturity-instructions/overrides`

  #### Docs

  The descriptions for the body parameters `fixed_interest_rate` and `margin_rate` in [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan-1) were updated and the following text was removed: “Otherwise, the field is required”.

  #### Docs

  The “Banking - Interest management” section of the guides was renamed to “Banking - Interest management (B3)”. This is meant to indicate that the endpoints in this section should only be used by Brazilian Stock Exchange (B3) customers.

  In addition “(B3 only)" was appended to the titles of the endpoints in that section (listed below), and a note was added to each endpoint description explaining that it should only be used by B3 customers.

  * [Create interest plan (B3 only)](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan-b3)
  * [Get interest plan (B3 only)](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan-b3)
  * [Get account interest (B3 only)](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account-b3)
  * [Update account interest (B3 only)](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account-b3)
  * [Configure benchmark rate (B3 only)](https://developers.pismo.io/pismo-docs/reference/post-v1-benchmark-rate-b3)
  * [Get Org benchmark rates (B3 only)](https://developers.pismo.io/pismo-docs/reference/get-v1-benchmark-rate-org-b3)
  * [Get specific benchmark rates (B3 only)](https://developers.pismo.io/pismo-docs/reference/get-v1-benchmark-rate-b3)

  #### Docs

  The field descriptions for `fixed_interest_rate` and `margin_rate` were updated. These fields appear in the following endpoints:

  * [Create interest plan (B3 only)](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan-b3) (in body params)
  * [Get interest plan (B3 only)](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan-b3) (in response)
  * [Get account interest (B3 only)](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account-b3) (in response)
  * [Update account interest (B3 only)](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account-b3) (in body params)
  * [Update account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account) (in body params)
  * [Get account interest](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account) (in response)
  * [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) (in body params)
  * [List org interest plans](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plans) (in response)
  * [Get interest plan](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan) (in response)
  * [Create interest plan version](https://developers.pismo.io/pismo-docs/reference/patch-v1-interest-plan) (in body params)

  #### Docs

  The field descriptions for `previous_balance` and `current_balance` were updated in the following endpoints:

  * [Get statement](https://developers.pismo.io/pismo-docs/reference/getstatementinfo) (in response)
  * [List statements](https://developers.pismo.io/pismo-docs/reference/getbystatementid) (in response)
  * [List transaction balances](https://developers.pismo.io/pismo-docs/reference/gettransactionsbalance) (in `statement` object of response)

  The description for `current_balance` was updated in the following endpoints:

  * [Create or update statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/createstatementamountdue) (in response)
  * [Get statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/getstatementamountdue) (in response)

  ### Instant payments

  #### New

  A new endpoint - [Get Pix client statistics](https://developers.pismo.io/pismo-docs/reference/get-v2-pix-statistics) - was added to the Pix management **Anti-fraud** section. This endpoint retrieves client account aggregated PIX statistics from BACEN DICT.

  #### New

  A new Pix endpoint - [Get Pix transaction by client request ID](https://developers.pismo.io/pismo-docs/reference/post-transactions-search) - was added to the Pix payments **Pix** section. The `client_request_id` is the value passed in the `Idempotency-Key` header when creating a cashin (Pix-in) or cashout (Pix-out) transaction. This endpoint is useful when a [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer) request times out and the client does not yet have the `end_to_end_id` needed to query the transaction through the [Get Pix transaction by end-to-end ID](https://developers.pismo.io/pismo-docs/reference/get-transaction-e2e) endpoint.

  #### New

  A new endpoint - [List Pix participants](https://developers.pismo.io/pismo-docs/reference/get-v2-pix-dict-participants) - and a new section - **Participants** - was added to the **Instant payments - Pix management** API. The endpoint returns the list of all Pix participants (institutions) registered in the BCB DICT, including each participant's ISPB, institution name, type and Pix participation modality.

  #### Updated

  Faster Payment Systems API endpoint error messages were updated:

  * EFPS009 - Transaction Not on Hold for Cancel was added to the 409 return from [Cancel FPS inbound transaction](https://developers.pismo.io/pismo-docs/reference/post-cancel-fps)
  * EFPS0094 - Transaction Not on Hold for Cancel was removed from the 400 return from [Release FPS inbound transaction](https://developers.pismo.io/pismo-docs/reference/post-release-fps)

  ### Payment rails

  #### Updated

  The “Reverse BACS direct credit outbound payment” endpoint was in beta and is now removed from production to rework the code.

  ### Transaction banking

  #### Updated

  The new [Update restriction](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-restricted-funds) endpoint is now available to enhance the restrict‑funds flow by allowing increase, release, and execution of restricted funds through a single request.

  #### Updated

  Two new 400 error messages are added to the [Update bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file) endpoint. They alert you when an invalid `bulkId` is used or when the number of bulk header lines exceeds the allowed range.

  * `WBUP0009: Invalid bulkId format`
  * `WBUP0010: Bulk header line exceeds maximum allowed length`
</summary>

<summary class="tabContent" id="Card issuing">
  ### Card network integration

  #### Updated

  Two new validation codes, `CAT` (Config API timeout) and `RAT` (Rates API timeout), were released and added to the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) guide. `CAT` indicates that authorization was denied because the Platform Config API did not respond within the configured timeout after all retries were exhausted. `RAT` indicates that authorization wad denied because the Rates API did not respond within the configured timeout after all retries were exhausted. Full definitions for these new validation codes were added to the [Validation code definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions) guide.

  #### Docs

  The definition for validation code `FRE` (Cryptogram data validation) was updated to clarify scenarios for this denial code. This update was made to the [Validation code definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions) guide.

  #### Docs

  The Consolidated file section of the [Clearing/Base II](https://developers.pismo.io/pismo-docs/docs/clearingbase#consolidated-file) guide was updated to include the paths of the generated consolidated clearing files.

  ### Statements

  #### Updated

  The following guides were updated to include the five new program calendar strategies:

  * [Calendar management strategies](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies)
  * [Fixed cycle closing calendar management strategy](https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy)

  #### Updated

  The `x-program-id` header was changed to `program-id` for the following endpoints.

  * [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory)
  * [List program transaction categories](https://developers.pismo.io/pismo-docs/reference/listtransactioncategoryinterest)
  * [Update program transaction category](https://developers.pismo.io/pismo-docs/reference/updatetransactioncategoryinterest)
  * [List account transaction category rates](https://developers.pismo.io/pismo-docs/reference/getaccountstransactionsinterest_1)
  * [List program transaction types](https://developers.pismo.io/pismo-docs/reference/gettransactiontypes_1)

  #### Updated

  The deprecated endpoint “List statements” (`GET /statements/v2/accounts/{accountId}/statements`) was decommissioned. The replacement endpoint “List statements v3” (`GET /statements-v2/v3/accounts/{accountId}/statements` was renamed [List statements](https://developers.pismo.io/pismo-docs/reference/getbystatementid).

  #### Docs

  The last paragraph of the [Credit card cycles (billing periods)](https://developers.pismo.io/pismo-docs/docs/understanding-statements#credit-card-cycles-billing-periods) section was updated to fix an error. Originally, it said that every new account has a moving window of 42 cycles - one current cycle and 41 future cycles. This was corrected to 43 cycles - one current cycle and 42 future cycles.

  #### Docs

  The [Credit liquidation](https://developers.pismo.io/pismo-docs/docs/credit-liquidation) guide was updated in the following ways.

  * Corrected Step 4 of [Closing delinquent accounts](https://developers.pismo.io/pismo-docs/docs/credit-liquidation#closing-delinquent-accounts). The final status does not necessarily have to be `CLOSED`.
  * Updated the final line of [How to manually close a delinquent account](https://developers.pismo.io/pismo-docs/docs/credit-liquidation#how-to-manually-close-a-delinquent-account) for the same reason.
  * Added a new section: [How to stop statement cycles for a canceled account](https://developers.pismo.io/pismo-docs/docs/credit-liquidation#how-to-stop-statement-cycles-for-a-canceled-account).

  #### Docs

  In the [Update statements calendar](https://developers.pismo.io/pismo-docs/reference/statementduedate) endpoint documentation, a note was added to the endpoint description and the description of the `account_default_program_due_date_id` body parameter was updated.

  #### Docs

  The last sentence of the introductory section of the [Credit liquidation](https://developers.pismo.io/pismo-docs/docs/credit-liquidation) guide was updated to: “An account that is overdue, meaning the MAD has not been paid by the due date, is called a delinquent account.” This was to clarify the meaning.

  #### Docs

  The description of the `DELINQUENT_ACCOUNT_CLOSURE_DAYS` parameter was updated in table in the [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters) guide.

  ### Tokenization

  #### Docs

  In the [Card tokenization flow and events](https://developers.pismo.io/pismo-docs/docs/card-tokenization-flow-and-events#visa-token-service-vts) guide, the VTS token create example was updated and a new VTS token status update example event was added.

  ### Visa Flexible Credentials

  #### New

  The enum values for `control_type` used in the [Create rules](https://developers.pismo.io/pismo-docs/reference/create-card-rules) endpoint was expanded to include the following values.

  * `TCT_GLOBAL` — Transaction control type (TCT) global
  * `TCT_ATM_WITHDRAW` — TCT ATM withdrawal
  * `TCT_AUTO_PAY` — TCT autopay
  * `TCT_BRICK_AND_MORTAR` — TCT brick and mortar
  * `TCT_CROSS_BORDER` — TCT cross border
  * `TCT_CONTACTLESS` — TCT contactless card
  * `MCT_ADULT_ENTERTAINMENT` — Merchant category type (MCT) adult entertainment
  * `MCT_AIRFARE` — MCT airfare
  * `MCT_ALCOHOL` — MCT alcohol
  * `MCT_APPAREL_AND_ACCESSORIES` — MCT apparel and accessories
  * `MCT_AUTOMOTIVE` — MCT automotive
  * `MCT_CAR_RENTAL` — MCT car rental
  * `MCT_ELECTRONICS` — MCT electronics
  * `MCT_SPORT_AND_RECREATION` — MCT sport and recreation
  * `MCT_GAMBLING` — MCT gambling
  * `MCT_GAS_AND_PETROLEUM` — MCT gas and petroleum
  * `MCT_GROCERY` — MCT grocery
  * `MCT_HOTEL_AND_LODGING` — MCT hotel and lodging
  * `MCT_HOUSEHOLD` — MCT household
  * `MCT_PERSONAL_CARE` — MCT personal car
  * `MCT_SMOKE_AND_TOBACCO` — MCT smoke and tobacco
  * `MCT_DINING` — MCT dining
</summary>

<summary class="tabContent" id="Seller management">
  ### Merchants

  #### New

  The following were added to the Merchant business category API.

  * [List business categories](https://developers.pismo.io/pismo-docs/reference/listbusinesscategories) allows you to retrieve a list of configured business categories.
  * [Get business category](https://developers.pismo.io/pismo-docs/reference/getbusinesscategory) allows you to get a business category using external codes.

  #### Updated

  The [List transactions](https://developers.pismo.io/pismo-docs/reference/merchants-transactions) endpoint was updated to return monetary fields as JSON numbers instead of strings.

  * Absent values now render as `null`.
  * The `advanced_*` fields were renamed to `advancement_*` throughout.

  #### Deprecated

  The following decommissioned endpoints were removed from the Developers Portal and added to the [API endpoints removed](https://developers.pismo.io/pismo-docs/docs/api-endpoints-removed) list.

  * `POST merchants/v1/merchants/{merchantId}/transactions`
  * `POST merchants/v1/merchants/{merchantId}/reversal-transactions`

  ### Transactions

  #### Updated

  The `currency_code` field was added to the response and the associated payload example in the [List advancement request settled](https://developers.pismo.io/pismo-docs/reference/getadvancementsbysettlement) endpoint.
</summary>

<summary class="tabContent" id="Lending">
  ### Lending

  #### Updated

  Restructured and rewrote all the guides in the [Lending](https://developers.pismo.io/pismo-docs/docs/lending-overview) section to document v2 endpoints, improve clarity, and help users better find the information they need.

  #### Updated

  All [Lending v2](https://developers.pismo.io/pismo-docs/reference/getloanproductv2) endpoints now have the “Beta” indicator removed.

  #### Updated

  Events related to Lending API v1 were removed from the Developers Portal.

  #### Updated

  You can now summarize loans using the summarizeLoans query parameter for the [List account loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2) endpoint. In the response, you get the corresponding aggregated `loan_summary` data.

  #### Docs

  The [Book loan](https://developers.pismo.io/pismo-docs/reference/bookloanv2) endpoint was updated to point to the event that is emitted, [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1).

  #### Docs

  Descriptions for arrays in the following Lending API endpoints were updated to start with “List of.”

  * [Get loan](https://developers.pismo.io/pismo-docs/reference/getloanv2)
  * [List account loans](https://developers.pismo.io/pismo-docs/reference/getloansbyaccountidv2)
  * [List loans](https://developers.pismo.io/pismo-docs/reference/retrievepaginatedloans)
  * [Get loan product](https://developers.pismo.io/pismo-docs/reference/getloanproductv2)
  * [List loan products](https://developers.pismo.io/pismo-docs/reference/getloanproductsv2)
  * [Create loan product](https://developers.pismo.io/pismo-docs/reference/createloanproductv2)
  * [Update loan product](https://developers.pismo.io/pismo-docs/reference/updateloanproductv2)
  * [Create prepayment record](https://developers.pismo.io/pismo-docs/reference/createprepayment)
  * [Create repayment hierarchy](https://developers.pismo.io/pismo-docs/reference/createrepaymenthierarchyv2)
  * [Get repayment hierarchy](https://developers.pismo.io/pismo-docs/reference/getrepaymenthierarchyv2)

  #### Docs

  The description of the `stop_accrual_number_of_days` field was updated across the [Lending](https://developers.pismo.io/pismo-docs/reference/getloanproductv2) API documentation to clarify how delinquency-related charges accrue after a payment becomes overdue and when new penalty charges stop posting.
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### Updated

  The [OpenID Connect](https://developers.pismo.io/pismo-docs/docs/openid-configurations) and [Permission groups](https://developers.pismo.io/pismo-docs/docs/cc-api-permission-groups) features were updated in Control Center.

  * All new OIDC authentication configurations must now have at least one permission group applied to them.
  * When creating a configuration, there is no longer a distinction between Standard and Third-Party configurations. You create a configuration and apply it to your specific use case.

  #### Updated

  The [dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval) feature was updated in Control Center. You can now request Pismo to enable dual approval for [editing card information](https://developers.pismo.io/pismo-docs/docs/card-information#view-and-edit-card-information) and [reissuing a card](https://developers.pismo.io/pismo-docs/docs/card-information#reissue-a-card).

  #### Docs

  The [Manage loans in Control Center](https://developers.pismo.io/pismo-docs/reference/manage-loans-in-control-center) guide was updated to align with Pismo documentation and style standards.

  #### Docs

  In Accounts overview > [Account views](https://developers.pismo.io/pismo-docs/docs/accounts-overview-cc#account-views), the **Loans** bullet was added to highlight the new lending functionality in Control Center.

  #### Docs

  The [Access keys](https://developers.pismo.io/pismo-docs/docs/access-keys-for-basic-authentication) guide title was updated to match the Control Center menu user interface.

  #### Docs

  The browser requirements were clarified in the [Sign on to Control Center](https://developers.pismo.io/pismo-docs/docs/get-access-and-sign-on) guide.

  #### Docs

  The [Card information](https://developers.pismo.io/pismo-docs/docs/card-information) guide was updated to maintain style consistency and standards throughout the portal.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /cards/v1/automatic-updater/{cardID}/opt-out` (`post-vau-opt-out`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--automatic-updater |
| `POST /cards/v1/automatic-updater/{cardID}/opt-in` (`post-vau-opt-in`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--automatic-updater |
| `POST /v1/programs/{programId}/calendar-strategies` (`CreateProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `GET /v1/programs/{programId}/calendar-strategies` (`ListProgramCalendarStrategies`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `GET /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` (`GetProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `PATCH /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` (`UpdateProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `POST /v1/balances-config/filter-templates` (`post-v1-filter-templates`) | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `POST /acquisitions/v3/s2s/applications` (`post-acquisitions-v3-s2s-applications`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `GET /v1/holiday-calendar/{holiday_calendar_id}/holiday` (`get-holiday-new`) | `api-specs/Platform_setup_-_Holidays.yaml` | no | KU-API-platform-setup-holidays--holiday-calendar-data |
| `POST /v2/migrations/accounts` (`PostAccountsV2`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--account-migration |
| `POST /v1/migrations/cards` (`PostCardsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--card-migration |
| `POST /v1/migrations/tokens` (`PostTokensV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--token-migration |
| `POST /v1/migrations/go-live` (`PostGoLiveV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--account-migration |
| `POST /v1/simulation/configs` (`simulationConfigs`) | `api-specs/Platform_setup_-_Rates_and_fees.yaml` | no | KU-API-platform-setup-rates-and-fees--simulation |
| `POST /v1/config` (`post-org-model-config`) | `api-specs/Core_platform_-_Rule_models.yaml` | no | KU-API-core-platform-rule-models--apply |
| `GET /v2/transactions` (`ListTransactions`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `POST /v1/interest/plan` (`post-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `GET /v1/interest/plan` (`get-v1-interest-plans`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `GET /v1/interest/plan/{interestPlanId}` (`get-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `PUT /v1/interest/account/{accountId}` (`put-v1-interest-account`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--account-interest |
| `GET /v1/interest/account/{accountId}` (`get-v1-interest-account`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--account-interest |
| `GET /v1/products/attachments/accounts/{accountId}` (`interest-bearing-v1-get-account-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits/accounts/{accountId}/attach` (`interest-bearing-v1-deposit-attach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/deposits/accounts/{accountId}/attachment` (`interest-bearing-v1-deposit-update-account-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `GET /v1/products/attachments/programs/{programId}` (`interest-bearing-v1-get-program-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `POST /v1/deposits/programs/{programId}/attach` (`interest-bearing-v1-deposit-attach-program`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `PATCH /v1/deposits/programs/{programId}/attachment` (`interest-bearing-v1-deposit-update-program-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `POST /v1/deposits/accounts/open` (`interest-bearing-v1-deposit-account-open`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--deposit-account-open |
| `POST /v1/deposits/accounts/{accountId}/penalty-simulation` (`interest-bearing-v1-simulate-penalty`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--penalty |
| `GET /v1/products` (`interest-bearing-v1-list-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /v1/deposits` (`interest-bearing-v1-create-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `PATCH /v1/deposits/{productId}` (`interest-bearing-v1-patch-deposit-product`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `GET /v1/deposits/{productId}` (`interest-bearing-v1-get-deposit-products`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--product |
| `POST /corporate/v2/payments/multileg` (`corporate-v2-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `GET /corporate/v2/payments/multileg/{trackingId}` (`corporate-v2-get-multileg-payment`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /v1/interest/plan` (`post-v1-interest-plan-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--interest-plan |
| `GET /v1/interest/plan/{interestPlanId}` (`get-v1-interest-plan-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--interest-plan |
| `GET /v1/interest/account/{accountId}` (`get-v1-interest-account-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--account-interest |
| `PUT /v1/interest/account/{accountId}` (`put-v1-interest-account-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--account-interest |
| `POST /v1/interest/benchmark-rate` (`post-v1-benchmark-rate-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--benchmark-rate |
| `GET /v1/interest/benchmark-rate` (`get-v1-benchmark-rate-org-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--benchmark-rate |
| `GET /v1/interest/benchmark-rate/{benchmark}` (`get-v1-benchmark-rate-b3`) | `api-specs/Banking_-_Interest_management.yaml` | no | KU-API-banking-interest-management--benchmark-rate |
| `PATCH /v1/interest/plan/{interestPlanId}` (`patch-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `GET /statements/v1/accounts/{accountId}/statements/{statementId}` (`GetStatementInfo`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `GET /statements-v2/v3/accounts/{accountId}/statements` (`getByStatementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `GET /statements-v2/v1/accounts/{accountId}/transactions-balance` (`getTransactionsBalance`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due` (`createStatementAmountDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |
| `GET /statements-v2/v1/accounts/{accountId}/minimum-amount-due` (`getStatementAmountDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |
| `GET /v2/pix/statistics` (`get-v2-pix-statistics`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--anti-fraud |
| `POST /pix/v1/pix/transactions/search` (`post-transactions-search`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01, KU-API-instant-payments-pix-payments--pix-part-02 |
| `POST /pix/v1/pix/out/transfer` (`post-pix-out-transfer`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01, KU-API-instant-payments-pix-payments--pix-part-02 |
| `GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction` (`get-transaction-e2e`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01, KU-API-instant-payments-pix-payments--pix-part-02 |
| `GET /v2/pix/dict/participants` (`get-v2-pix-dict-participants`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--participants |
| `POST /v1/payments/fps/cancel/{endToEndId}` (`post-cancel-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/fps/release/{endToEndId}` (`post-release-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `PATCH /corporate/v2/restricted-funds/{restrictedFundsId}` (`patch-corporate-v2-restricted-funds`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--restricted-funds |
| `PUT /corporate/v1/bulk-payments/{bulkId}` (`corporate-put-bulk-file`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |
| `POST /statements-v2/v1/transactions-categories` (`createTransactionCategory`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `GET /statements-v2/v1/transactions-categories` (`listTransactionCategoryInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` (`updateTransactionCategoryInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `GET /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` (`getAccountsTransactionsInterest_1`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `GET /statements-v2/v1/programs-transactions-types` (`getTransactionTypes_1`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--transaction-types |
| `PATCH /statements-v2/v2/due-date` (`statementDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /flex_credentials/v1/vfc/rules/cards/{cardId}` (`create-card-rules`) | `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` | no | KU-API-card-issuing-visa-flexible-credentials--rules |
| `GET /v1/businesscategories` (`listBusinessCategories`) | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant-business-category |
| `GET /v1/businesscategories/{externalCode}` (`getBusinessCategory`) | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant-business-category |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` (`merchants-transactions`) | `api-specs/Seller_management_-_Merchant_advance.yaml` | no | KU-API-seller-management-merchant-advance--merchant-advancement-transaction |
| `GET /v1/merchants/{merchantId}/settlements/advancements` (`getAdvancementsBySettlement`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--settlements |
| `GET /v2/loan-products/{productId}` (`getLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /v2/accounts/{accountId}/loans` (`getLoansByAccountIdV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `POST /v2/loans` (`bookLoanV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/loans/{loanId}` (`getLoanV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/loans` (`retrievePaginatedLoans`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |
| `GET /v2/loan-products` (`getLoanProductsV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v2/loan-products` (`createLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `PATCH /v2/loan-products/{productId}` (`updateLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v2/prepayments` (`createPrepayment`) | `api-specs/Lending.yaml` | no | KU-API-lending--prepayment |
| `POST /v2/repayment-hierarchies` (`createRepaymentHierarchyV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--repayment-hierarchy |
| `GET /v2/repayment-hierarchies/{hierarchyCode}` (`getRepaymentHierarchyV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--repayment-hierarchy |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `nterest-bearing-v1-deposit-account-open` | Open deposit account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `post-v1-interest-plan-1` | Create interest plan | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `manage-loans-in-control-center` | Manage loans in Control Center | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/7-august-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/7-august-2026 | `aef7c8860d509dca…` | not stated |

## Related knowledge units

- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--deposit-account-open` — API reference: Banking - Interest-bearing accounts — Deposit account open
- `KU-API-banking-interest-bearing-accounts--penalty` — API reference: Banking - Interest-bearing accounts — Penalty
- `KU-API-banking-interest-bearing-accounts--product` — API reference: Banking - Interest-bearing accounts — Product
- `KU-API-banking-interest-bearing-accounts--program-attachment` — API reference: Banking - Interest-bearing accounts — Program attachment
- `KU-API-banking-interest-engine--account-interest` — API reference: Banking - Interest engine — Account interest
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-interest-management--account-interest` — API reference: Banking - Interest management for B3-listed products — Account interest
- `KU-API-banking-interest-management--benchmark-rate` — API reference: Banking - Interest management for B3-listed products — Benchmark rate
- `KU-API-banking-interest-management--interest-plan` — API reference: Banking - Interest management for B3-listed products — Interest plan
- `KU-API-banking-transaction-banking--bulk-payment-files` — API reference: Banking - Transaction banking — Bulk payment files
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--restricted-funds` — API reference: Banking - Transaction banking — Restricted funds
- `KU-API-card-issuing-cards--automatic-updater` — API reference: Card issuing - Cards — Automatic updater
- `KU-API-card-issuing-visa-flexible-credentials--rules` — API reference: Card issuing - Visa Flexible Credentials [beta] — Rules
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balance-config-beta--filter-templates` — API reference: Core platform - Balance configurations — Filter templates
- `KU-API-core-platform-rule-models--apply` — API reference: Core platform - Rule models — Apply
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-instant-payments-pix-management--anti-fraud` — API reference: Instant payments - Pix management — Anti-fraud
- `KU-API-instant-payments-pix-management--participants` — API reference: Instant payments - Pix management — Participants
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-02` — API reference: Instant payments - Pix payments — Pix (part 2 of 2)
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-lending--prepayment` — API reference: Lending — Prepayment
- `KU-API-lending--repayment-hierarchy` — API reference: Lending — Repayment hierarchy
- `KU-API-migrations--account-migration` — API reference: Migrations — Account migration
- `KU-API-migrations--card-migration` — API reference: Migrations — Card migration
- `KU-API-migrations--token-migration` — API reference: Migrations — Token migration
- `KU-API-platform-setup-holidays--holiday-calendar-data` — API reference: Platform setup - Holidays — Holiday calendar data
- `KU-API-platform-setup-rates-and-fees--simulation` — API reference: Platform setup - Rates and fees — Simulation
- `KU-API-revolving-credit-calendar-management--program-calendar-strategies` — API reference: Revolving credit - Calendar management — Program calendar strategies
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-API-revolving-credit-statements--statement-minimum-amount-due` — API reference: Revolving credit - Statements — Statement minimum amount due
- `KU-API-revolving-credit-statements--transaction-types` — API reference: Revolving credit - Statements — Transaction types
- `KU-API-seller-management-merchant-advance--merchant-advancement-transaction` — API reference: Seller management - Merchant advancements — Merchant advancement transaction
- `KU-API-seller-management-merchants--merchant-business-category` — API reference: Seller management - Merchants — Merchant business category
- `KU-API-seller-management-sellers--settlements` — API reference: Seller management - Sellers — Settlements
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
