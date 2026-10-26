---
ku_id: KU-CHG-7-july-2025
title: 'Changelog: 7 July 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/7-july-2025.md
  sha256: e6dfaeba8920201786e8b5da6975dbc3efcc5a15cfc4a18e0af648fc4207f55b
  url: https://developers.pismo.io/pismo-docs/changelog/7-july-2025
  role: changelog_post
  updated_at: ''
operations:
- CreateInstallmentAdvancement
- create-recurring-charge-plan
- get-account-balance-history
- get-account-balance-history-configuration
- get-account-balances
- get-accounts
- get-list-dict-refunds
- getByStatementId
- getDormancyConfig
- list-dormancy-configs
- patch-dormancy-config-v2
- patch-v1-accounts-flex-control
- patch-v1-customers-flex-control
- post-account-balance-history-configuration
- post-accounts-v1-accounts-accountId-addresses
- post-acquisitions-v3-s2s-applications
- post-create-recurrence
- post-create-recurrence-cob
- post-create-recurrence-cobv
- post-create-static
- post-dormancy-config-v2
- post-v1-accounts-flex-controls
- post-v1-card-reissue
- post-v1-customers-flex-controls
- postInterestAccruals
- put-v1-card-status
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-banking-transaction-banking--dormancy
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--card-status
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-accounts--addresses
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-flex-controls--customer-flex-controls-part-01
- KU-API-core-platform-flex-controls--customer-flex-controls-part-02
- KU-API-instant-payments-pix-management--refunds
- KU-API-instant-payments-qr-code--recurring-payment
- KU-API-revolving-credit-installment-management--installment-advancements
- KU-API-revolving-credit-interest-accruals--post-interest-accruals
- KU-API-revolving-credit-recurring-charges--recurring-charge-plans
- KU-API-revolving-credit-statements--statement
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 7 July 2025
coverage_window: 6 June and 7 July 2025
---

# Changelog: 7 July 2025

**KU ID:** `KU-CHG-7-july-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **7 July 2025** (changes between 6 June and 7 July 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated"; "Deprecated"; "Deprecated"; "Deprecated".

## Topics covered

Security guide; Seller management; Client webhooks; Flex controls; General; Payments; Programs; Security; Banking reports; Instant payments; Transaction banking; Card tokenization; Cards management; Disputes; Statements

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/7-july-2025

<!-- source:begin path=changelog/7-july-2025.md part=0-end -->

# 7 July 2025

Changes between 6 June and 7 July 2025

<div class="customTab" />

  <summary class="tabContent" id="New features">
    ### Control Center

#### New

We’re excited to announce that our redesigned menu is now live in EXT—making it easier than ever to find exactly what you need.

**What’s new?**

* **All configurations, organized clearly.** Find all configurations in one place, grouped by platform-wide settings, card issuing, and banking.
* **User and permission management, simplified.** Manage users and permissions from a single location.
* **Organization details, now easier to find.** We’ve moved them out of the menu and into the top organization selector, where they belong.

**Why the change?**

We’ve redesigned the menu to make navigation clearer and more intuitive now, while also making room for future features as Control Center grows.

**What do you need to do?**

Just one thing: **reset your favorites in EXT**. Your current favorites won’t carry over, so you’ll need to add them again.

### Security guide

#### Docs

A new [Security guide for Control Center](https://developers.pismo.io/pismo-docs/docs/security-guide-for-control-center) is available to help you understand the security options and protections available to you. The Control Center has a number of systems and policies in place to ensure and enforce security and privacy. This includes requirements and processes related to the creation, authentication, and authorization of users and defined practices for data retention and handling of personal identifiable information (PII). It also includes account and organization access.

### Seller management

#### Docs

If you are getting started with seller management, now you can read about onboarding with Pismo as well as how to get started including planning, governing, processing codes, testing, and monitoring seller marketplaces.

* [Get started with seller management](https://developers.pismo.io/pismo-docs/docs/seller-management-with-pismo)
* [Seller management onboarding](https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding)

  </summary>

  <summary class="tabContent" id="Core platform">
    ### Accounts

#### Updated

The `number` field in the address object for the [Create account application](https://developers.pismo.io/pismo-docs/reference/post-acquisitions-v3-s2s-applications) and [Create address](https://developers.pismo.io/pismo-docs/reference/post-accounts-v1-accounts-accountid-addresses) endpoints is no longer required.

### Client webhooks

#### Updated

Two new response address fields, `street` and `number`, were added to the [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook). The response fields table and the sample response were updated with these new fields.

### Flex controls

#### Updated

The following new attributes are now available to evaluate a flex control condition:

* `acquirer_country_code`
* `authentication_method`
* `is_cavv_present`
* `is_tra_exemption_requested`
* `is_token_present`
* `initiation_mode`

These attributes are available as options inside the `conditions.attribute` field in the following endpoints:

* [Create account flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls)
* [Update account flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-accounts-flex-control)
* [Create customer flex control](https://developers.pismo.io/pismo-docs/reference/post-v1-customers-flex-controls)
* [Update customer flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-customers-flex-control)

These attributes are also available as options inside the `conditions.attribute` field in the following events:

* [Evaluation requested](https://developers.pismo.io/events/docs/audit-evaluation-requested-1)
* [Customer flex control created](https://developers.pismo.io/events/docs/audit-customer-spending-limit-created-1)
* [Customer flex control updated](https://developers.pismo.io/events/docs/audit-customer-spending-limit-updated-1)
* [Flex control template created](https://developers.pismo.io/events/docs/audit-template-created-1)
* [Flex control template updated](https://developers.pismo.io/events/docs/audit-template-updated-1)

### General

#### Docs

The new [API endpoints removed](https://developers.pismo.io/pismo-docs/reference/api-endpoints-removed) guide lists when API endpoints were removed from Pismo’s public documentation.

### Payments

#### Updated

The following new [processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types#standard-processing-codes) and their reversal processing codes are now available:

* PSM039 (cashback) and PSM04 (cashback reversal)
* PSM018 (installment withdrawal TECBAN) and PSM019 (installment withdrawal TECBAN reversal)

### Programs

#### Deprecated

The deprecated endpoint **List due dates for all statements** was removed from public documentation.

### Security

#### Docs

The steps for [Server authentication](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid#server-authentication) in the Authentication with OpenID Connect guide were updated to reflect that you no longer need to send a public key to Pismo and instead you upload the public key directly to Control Center.

#### Docs

The JWT key descriptions in the [Authentication with OpenID Connect](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid#generate-your-jwt) guide were updated for clarification.

  </summary>

  <summary class="tabContent" id="Data and reporting">
    ### Events

#### Deprecated

The events in the **rules** domain that were previously listed on the [Events](https://developers.pismo.io/events/docs/event-base-main-event) tab under **Core platform > Flex controls** were removed as no longer applicable. Refer to the full list of [flex controls events](https://developers.pismo.io/pismo-docs/docs/flex-controls-data-events) in the **audit** domain.

  </summary>

  <summary class="tabContent" id="Core banking">
    ### Banking operations

#### Updated

The new field `change_available_datetime` is now available on the [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1) and [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1) events. This field records the exact date and time of impact to a balance in a ledger.

### Banking reports

#### Deprecated

The following endpoints were deprecated and decommissioned on 30 June 2025. Refer to [API endpoint deprecation and removal schedule](https://developers.pismo.io/pismo-docs/docs/deprecation-schedule) for a list of deprecated endpoints.

* Create transaction types
* Get account income report
* Get account annual fees report
* List transaction types

### Instant payments

#### New

A new enum value - `PIX_AUTOMATICO` - was added to the `refund_reason` enum field for [Pix refunds](https://developers.pismo.io/pismo-docs/reference/get-list-dict-refunds).  It indicates that a Pix refund was requested due to a failed Automatic Pix operation.

#### New

A new section was added to the QR Code API - **Recurring payment**. In this section, the following endpoints were added to generate QR Codes for recurring payments such as gym membership:

* [Create recurrent COB QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence-cob)
* [Create recurrent COBV QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence-cobv)
* [Create recurrent static QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-static)
* [Create recurrent compound QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence)

### Transaction banking

#### Updated

`division_id` in the [Division cycle closing completed](https://developers.pismo.io/events/docs/corporate-division-cycle-closing-1) event is now a required field.

#### Updated

The fields `future_dated_credits_balance` and `future_dated_debits_balance` were added to the 200 response payloads of the following endpoints. These fields add information about future-dated credit and debit balances in the response.

* [Get account balance](https://developers.pismo.io/pismo-docs/reference/get-account-balances)
* [Get account balance history](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history)
* [Get account info](https://developers.pismo.io/pismo-docs/reference/get-accounts)

#### Updated

The new field `check_timezone_origin` was added to the following endpoints and events. This field allows you to specify whether the dormancy check should use the timezone of the account’s program or division.

Endpoints:

* [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2)
* [List dormancy configuration](https://developers.pismo.io/pismo-docs/reference/list-dormancy-configs)
* [Get dormancy configuration](https://developers.pismo.io/pismo-docs/reference/getdormancyconfig)

Events:

* [Dormancy configuration created](https://developers.pismo.io/events/docs/corporate-dormancy-config-creation-1)
* [Dormancy configuration updated](https://developers.pismo.io/events/docs/corporate-dormancy-config-change-1)

In addition, the following "Invalid timezone origin" error message was added to the [Create dormancy configuration](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2) and [Update dormancy configuration](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2) endpoints.

```json
code: "WDOR0002"  
message: check_timezone_origin must be one of [DIVISION PROGRAM]
```

#### Updated

The `change_available_datetime` field is no longer a required field in the following events:

* [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
* [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1)

#### Updated

The following error messages were added to the [Create account balance history configuration](https://developers.pismo.io/pismo-docs/reference/post-account-balance-history-configuration) and [Get account balance history configuration](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history-configuration) endpoints in relation to the limit defined for `cycle_event_delay`. The limit is now set for 1439 minutes after `cycle_closing_time`.

* `WCFG0002: cycle_event_delay must be 1,439 or less`
* `WCFG0002: divisionCode is a required parameter`
* `WCFG0002: cycle_closing_time must be a maximum of 8 characters in length`
* `WCFG0002: cycle_closing_time has an invalid time format: {cycle_closing_time}`
* `WCFG0002: cycle_event_delay must be 5 or greater`
* `WCFG0002: cycle_closing_time or cycle_event_delay must be provided`

#### Docs

Two account balance definitions were added to the account balance definitions table in the [Account balance definitions for transaction banking](https://developers.pismo.io/pismo-docs/docs/account-balance-definitions-for-transaction-banking) guide:

* Future-dated credits balance
* Future-dated debits balance

In addition, this guide now includes a note that  `uncleared_funds` is calculated as `future_dated_credits_balance` - `future_dated_debits_balance`.

  </summary>

  <summary class="tabContent" id="Card issuing">
    ### Card network integration

#### Updated

A new REJECTED reason, `HSM_UNKNOWN_ERROR_RESPONSE`, was added to the [CVM validation](https://developers.pismo.io/pismo-docs/docs/rule-list#cvm-validation).

#### Docs

A note was added to the definition for the [validation code DCM](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#dcm---original-authorization-not-found-at-refund) (original authorization not found at refund) to clarify some differences in event responses for MTI `0420 `and `0400` refunds.

### Card tokenization

#### Deprecated

The public documentation for the deprecated endpoints **Get encrypted card data for wallet token** and **Get encrypted card data for Apple Pay** were removed.

### Cards management

#### Docs

Two new sections were added to the Cards API reference - [Card reissue](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue) (2 endpoints) and [Card status](https://developers.pismo.io/pismo-docs/reference/put-v1-card-status) (3 endpoints). The endpoints aren’t new, this was done to improve API organization and readability.

#### Docs

A new [Card reissuing](https://developers.pismo.io/pismo-docs/docs/card-reissuing) guide is now available. The content for this guide was previously contained in the [Cards lifecycle and statuses](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses) guide.

### Disputes

#### Updated

The following fields were removed from the Visa Collaboration Process Errors form under `dispute_due_to` = `D` (Duplicate) or `P` (Paid by other means):

* `arn`
* `transactionID`
* `rolTransactionId`
* `duplicateTranAmount`
* `duplicateTranId`
* `duplicateTranDate`

### Statements

#### Updated

The [Post interest accruals](https://developers.pismo.io/pismo-docs/reference/postinterestaccruals) endpoint now includes two new fields: `start_date` and `end_date`.

#### Updated

The following updates were made to the [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid) endpoint.

* The `showAmounts` query parameter was removed. Before this update, setting this parameter to `true` would cause some additional fields to be displayed in the 200 response. These fields are now displayed automatically if a statement is closed and if it was closed after 17 April 2025. This is because the behavior of these fields has changed, and if they were shown for statements that do not fit these criteria, they would not contain the expected information. The following fields were affected and their descriptions were modified.
  * `amount_due`
  * `amount_paid_until_due_date`
  * `amount_paid_after_due_date`
  * `other_credits_until_due_date`
  * `other_credits_after_due_date`
* A new enum field called `status` was added. It represents the status of the statement, and it has the following values: `CLOSED`, `CLOSED_NOT_DUE`, `OPEN`, `FUTURE`.

#### Updated

A new section [Configuring features based on account status](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#configuring-features-based-on-account-status) was added to the Full balance credit program guide. It explains the use of three new endpoints that have been added to the API.

#### Docs

A new guide [Limiting the number of days accruals can be charged](https://developers.pismo.io/pismo-docs/docs/limiting-the-number-of-days-accruals-can-be-charged) is now available.

#### Docs

The [Managing due date, cycle closing date, and additional grace periods](https://developers.pismo.io/pismo-docs/docs/managing-due-date-cycle-closing-date-and-additional-grace-periods) guide was updated to correct and clarify information about grace periods. Renamed the section “Defining a grace period” to [Defining an additional grace period](https://developers.pismo.io/pismo-docs/docs/managing-due-date-cycle-closing-date-and-additional-grace-periods#defining-an-additional-grace-period) and updated its contents.

#### Docs

A note was added to the description of the [Create recurring charge plan](https://developers.pismo.io/pismo-docs/reference/create-recurring-charge-plan)  endpoint explaining that the 504 - RECURRING\_CHARGE\_FINAL\_ACCOUNT\_STATUS program parameter must be set in order for the endpoint to work properly.

#### Docs

The new section [Configuring features based on account status](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#configuring-features-based-on-account-status) was added to the Full balance credit program guide.

#### Docs

The description and example for the reason field of [Close delinquent account](https://developers.pismo.io/pismo-docs/reference/delinquent-ccount-closure-post) was corrected.

#### Docs

The [Create installment advancement](https://developers.pismo.io/pismo-docs/reference/createinstallmentadvancement) endpoint description and the descriptions of the response body fields `old_amount`, `new_amount`, and `new_interest_amount` were updated.

#### Docs

The bullet point 3 in [Installment advancements](https://developers.pismo.io/pismo-docs/docs/installment-management#installment-advancements) was updated.

#### Docs

A new callout at the end of the “Payment hierarchy” section of [How the program discharges transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-discharges-transactions) explains an exception to the rules about how transactions are discharged.

#### Docs

The section [How to automate closing delinquent accounts](https://developers.pismo.io/pismo-docs/docs/credit-liquidation#how-to-automate-closing-delinquent-accounts) was updated.

#### Docs

The [Multivalue parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-parameters) guide was updated with additional columns and information and some corrected entries.

  </summary>

  <summary class="tabContent" id="Seller management">
    ### Merchants

#### New

Now you can link multiple merchants to a marketplace rather than one merchant to one marketplace. These newly released endpoints enable this feature:

* [Link merchant and marketplace](https://developers.pismo.io/pismo-docs/reference/postlinkmerchanttomarketplacev1)
* [List marketplace merchants](https://developers.pismo.io/pismo-docs/reference/getmerchantsbymarketplaceidv1)
* [Unlink marketplace and merchant](https://developers.pismo.io/pismo-docs/reference/deletelinkbetweenmerchantandmarketplacev1)

  </summary>

<details>
  <summary class="tabContent" id="Resources">
    ### Pismo Control Center

#### Fixed

An issue was fixed where network acceptance information was not being displayed for credit program exports.

#### Docs

The new [Cloned and exported program properties](https://developers.pismo.io/pismo-docs/docs/cc-cloned-and-exported-data) guide helps explain what program information is exported or copied, addressing issues with program status and manual configuration steps.

  </summary>
</details>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /acquisitions/v3/s2s/applications` (`post-acquisitions-v3-s2s-applications`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `POST /accounts/v1/accounts/{accountId}/addresses` (`post-accounts-v1-accounts-accountId-addresses`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--addresses |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `PATCH /v1/accounts/{accountId}/flex-controls/{flexControlId}` (`patch-v1-accounts-flex-control`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/customers/{customerId}/flex-controls` (`post-v1-customers-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-01, KU-API-core-platform-flex-controls--customer-flex-controls-part-02 |
| `PATCH /v1/customers/{customerId}/flex-controls/{flexControlId}` (`patch-v1-customers-flex-control`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-01, KU-API-core-platform-flex-controls--customer-flex-controls-part-02 |
| `GET /v2/pix/refunds` (`get-list-dict-refunds`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |
| `POST /v1/pix/qrcode/cob/recurrence` (`post-create-recurrence-cob`) | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /v1/pix/qrcode/cobv/recurrence` (`post-create-recurrence-cobv`) | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /v1/pix/qrcode/static/recurrence` (`post-create-static`) | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /v1/pix/qrcode/recurrence` (`post-create-recurrence`) | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `GET /bank-statements/v1/account-balances/{externalAccountId}` (`get-account-balances`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v1/account-balances/{externalAccountId}/history` (`get-account-balance-history`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /corporate/v1/corporate-accounts/{externalAccountId}` (`get-accounts`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v2/dormancy-config` (`post-dormancy-config-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `GET /corporate/v1/dormancy-config` (`list-dormancy-configs`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `GET /corporate/v1/dormancy-config/{dormancyConfigId}` (`getDormancyConfig`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` (`patch-dormancy-config-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `POST /bank-statements/v1/account-balances/history/config` (`post-account-balance-history-configuration`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /bank-statements/v1/account-balances/history/config/{divisionCode}` (`get-account-balance-history-configuration`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` (`post-v1-card-reissue`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `PUT /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/status` (`put-v1-card-status`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-status |
| `POST /v1/accounts/{accountId}/interest-accruals` (`postInterestAccruals`) | `api-specs/Revolving_credit_-_Interest_accruals.yaml` | no | KU-API-revolving-credit-interest-accruals--post-interest-accruals |
| `GET /statements-v2/v3/accounts/{accountId}/statements` (`getByStatementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /v1/recurring-charge-plans` (`create-recurring-charge-plan`) | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-charge-plans |
| `POST /v1/accounts/{accountId}/installment-advance` (`CreateInstallmentAdvancement`) | `api-specs/Revolving_credit_-_Installment_management.yaml` | **yes** | KU-API-revolving-credit-installment-management--installment-advancements |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `api-endpoints-removed` | API endpoints removed | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `delinquent-ccount-closure-post` | Close delinquent account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `postlinkmerchanttomarketplacev1` | Link merchant and marketplace; Link merchant to marketplace | not found in the current OpenAPI specifications. Name-based inference: link text "Link merchant and marketplace" equals the endpoint name "Link merchant and marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. |
| `getmerchantsbymarketplaceidv1` | List marketplace merchants | not found in the current OpenAPI specifications. Name-based inference: link text "List marketplace merchants" equals the endpoint name "List marketplace merchants" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. |
| `deletelinkbetweenmerchantandmarketplacev1` | Unlink marketplace and merchant | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/7-july-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/7-july-2025 | `e6dfaeba89202017…` | not stated |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--card-status` — API reference: Card issuing - Cards — Card status
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-accounts--addresses` — API reference: Core platform - Accounts — Addresses
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-01` — API reference: Core platform - Flex controls — Customer flex controls (part 1 of 2)
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-02` — API reference: Core platform - Flex controls — Customer flex controls (part 2 of 2)
- `KU-API-instant-payments-pix-management--refunds` — API reference: Instant payments - Pix management — Refunds
- `KU-API-instant-payments-qr-code--recurring-payment` — API reference: Instant payments - QR Code — Recurring payment
- `KU-API-revolving-credit-installment-management--installment-advancements` — API reference: Revolving credit - Installment management — Installment advancements
- `KU-API-revolving-credit-interest-accruals--post-interest-accruals` — API reference: Revolving credit - Interest accruals — Post interest accruals
- `KU-API-revolving-credit-recurring-charges--recurring-charge-plans` — API reference: Revolving credit - Recurring charges — Recurring charge plans
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
