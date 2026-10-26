---
ku_id: KU-CHG-3-january-2025
title: 'Changelog: 3 January 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/3-january-2025.md
  sha256: b2601955a852bfef1757043de21e45d4f0d8647617fdc659fd18619dc58d37b7
  url: https://developers.pismo.io/pismo-docs/changelog/3-january-2025
  role: changelog_post
  updated_at: ''
operations:
- CreateProgramBasedOnTemplate
- InstallmentPaymentsv4
- PostBalanceControlV1
- blockMerchantsForSettlement
- corporate-put-bulk-file
- corporate-v2-delete-scheduled-payment
- corporate-v2-get-multileg-payment
- corporate-v2-get-scheduled-payment
- corporate-v2-list-scheduled-payment
- corporate-v2-post-cancel-payments
- corporate-v2-post-confirm-payments
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- corporate-v2-post-scheduled-payments
- create-bulk
- customerV1patch
- customerV2Put
- get-account-balance-history-configuration
- get-corporate-transactions
- get-division-by-code-v2
- get-integrated-payments-api-v1-bankslips-receipts
- get-scheduled-charge
- get-scheduler-executions
- get-v1-card
- getAdvancementsBySettlement
- getBlockedMerchants
- list-division-v2
- list-scheduled-charges
- list-scheduled-transfers
- patch-accounts-accountId-status-rollback-v2
- patch-accounts-accountId-status-v2
- patch-corporate-v2-earmarks-earmarkid
- patch-division-v2
- patch-dormancy-config-v2
- patch-v1-accounts-flex-control
- patch-v2-card
- post-authorization
- post-close-dict-refund
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-division-v2
- post-dormancy-config-v2
- post-payments-cancel
- post-payments-v1-installments
- post-transfers-cancel
- post-v1-admin-division
- post-v1-card-reissue
- post-v2-card
- post-v2-pix-infraction-create
- post-v2-pix-keys-delete
- put-v1-disputes-disputeId
- runSettlement
- unblockMerchantsForSettlement
- updateProgramParamenter
related_kus:
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bank-statements-part-01
- KU-API-banking-transaction-banking--bank-statements-part-02
- KU-API-banking-transaction-banking--bulk-payment-files
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--dormancy
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-banking-transaction-banking--transactions
- KU-API-card-issuing-cards--card-reissue
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-cards--noname
- KU-API-card-issuing-disputes--disputes-part-01
- KU-API-card-issuing-disputes--disputes-part-02
- KU-API-core-platform-accounts--customers
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-instant-payments-pix-management--infraction-reports-part-01
- KU-API-instant-payments-pix-management--infraction-reports-part-02
- KU-API-instant-payments-pix-management--keys-part-01
- KU-API-instant-payments-pix-management--keys-part-02
- KU-API-instant-payments-pix-management--refunds
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-migrations--balance-migration
- KU-API-platform-setup-divisions--administrative-divisions-deprecated
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges
- KU-API-revolving-credit-statements--multivalue-program-parameters
- KU-API-revolving-credit-statements--refinancing
- KU-API-seller-management-sellers--settlement-actions
- KU-API-seller-management-sellers--settlements
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 3 January 2025
coverage_window: 6 December 2024 and 3 January 2025
---

# Changelog: 3 January 2025

**KU ID:** `KU-CHG-3-january-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **3 January 2025** (changes between 6 December 2024 and 3 January 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated"; "Deprecated".

## Topics covered

Accounts; Client webhooks; Flex controls; Migrations; Payments; Setup; Transactions; Events; Reports; Integrated payments; Instant payments; Transaction banking; Cards; Card network integration; Disputes; Statements; Sellers; Pismo Control Center; Postman

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/3-january-2025

<!-- source:begin path=changelog/3-january-2025.md part=0-end -->

# 3 January 2025

Changes between 6 December 2024 and 3 January 2025

<div class="customTab"></div>

<summary class="tabContent" id="Core platform">

### Accounts

#### Docs

In the [Overwrite customer information](https://developers.pismo.io/pismo-docs/reference/customerv2put) and [Update customer information](https://developers.pismo.io/pismo-docs/reference/customerv1patch) endpoints, the field descriptions have been updated to clarify if the endpoint updates the fields even if a field value isn't passed.

### Client webhooks

#### Updated

New request and response fields have been added to the [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook). The new fields support Visa’s Address Verification Service (AVS) and Account Name Inquiries (ANI) as part of name matching validations. The new fields are listed in the Request fields and Response fields tables and are also included in the Sample request code and the Sample response code provided in the [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks) guide.

### Flex controls

#### Updated

In the [Update account flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-accounts-flex-control) endpoint, the  `available_limit` field has been added to limit the total available spending.

### Migrations

#### Docs

Updated the description for the [Start migration of balances](https://developers.pismo.io/pismo-docs/reference/postbalancecontrolv1) endpoint to clarify that the correct balance amount to pass in the request depends on when during the statement cycle the account is being migrated.

### Payments

#### Updated

The following updates have been made to standardize currency fields for ISO 4217.

* In the [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) endpoint, the `currency_code` field was updated to support both alphabetic and numeric 3-character codes.
* In the [Payment methods authorization created](https://developers.pismo.io/events/docs/payment-methods-authorization-1) event, the `currency_num_code` field has been added and the description of the `currency_code` field has been updated.
* In the [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event, the `account_currency_num_code` and `local_currency_num_code` fields have been added.

#### Updated

In [Create installments payment](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-installments), the `first_installment_date` field has been added to specify the date that the first installment should be posted on the invoice.

#### Docs

In the [Cancel cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-cancel) and [Cancel transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers-cancel) endpoints, the example for the `tracking_id` has been updated to distinguish it from the `original_tracking_id`.

### Setup

#### Docs

The Balances configuration [guide](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview) and [API](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config-1) have been updated for clarity and standardization.

#### Docs

The [Platform setup - Divisions](https://developers.pismo.io/pismo-docs/reference/post-v1-admin-division) and [Platform setup - Programs](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) APIs have been updated for documentation standards, including various changes to endpoint descriptions, parameter descriptions, attributes, and other minor changes.

### Transactions

#### Docs

In the [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) and [Transactions overview](https://developers.pismo.io/pismo-docs/docs/transactions-overview) guides, the transaction type description has been updated.

</summary>

<summary class="tabContent" id="Data and reporting">

### Events

#### Docs

The [SFTP event file configuration tutorial](https://developers.pismo.io/pismo-docs/docs/sftp-event-file-configuration-tutorial) has been updated to indicate that a direct IP address or list of IP addresses in /32 subnet mask format must be included in the request for SFTP access.

### Reports

#### Docs

The [Scheduled reports](https://developers.pismo.io/pismo-docs/docs/scheduled-reports) guide has been updated to clarify that reports run on independent schedules and frequencies (not on demand).

</summary>

<summary class="tabContent" id="Core banking">

### Integrated payments

#### Docs

In the [List bank slip receipt](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-bankslips-receipts) endpoint, the new `additional_info` field has been added under the `items` object in the 200 response payload. This field stores managed data that banking providers send to Pismo.

### Instant payments

#### New

The following new endpoints are now available in the Pix management API.

* [List scheduled transfers](https://developers.pismo.io/pismo-docs/reference/list-scheduled-transfers) returns a list scheduled Pix transfers.
* [List Pix scheduler executions](https://developers.pismo.io/pismo-docs/reference/get-scheduler-executions) returns a list of scheduled Pix transactions that have run and are complete.

#### Updated

In the Pix management API, the following changes have been made.

* In the [Close refund](https://developers.pismo.io/pismo-docs/reference/post-close-dict-refund) endpoint, the new `INVALID_REQUEST` enum has been added to the `refund_rejection_reason` field.
* In the [Delete key](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-delete) endpoint, `RFB_VIOLATION` has been added to the `reason` field.
* In the [Create infraction report](https://developers.pismo.io/pismo-docs/reference/post-v2-pix-infraction-create) endpoint, the `contact_information` object containing `phone` and `email` fields has been added.

#### Docs

Banking overview now includes information about [STR protocol](https://developers.pismo.io/pismo-docs/docs/banking-overview#str-protocol).

### Transaction banking

#### Deprecated

The following transaction banking endpoints were deprecated and removed on 20 December 2024.

<details>

<summary>Transaction banking API</summary>

| Deprecated endpoint                               | New endpoint                                                                                         |
| :------------------------------------------------ | :--------------------------------------------------------------------------------------------------- |
| Post payment (v1)                                 | [Post payment (v2)](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)                                                  |
| Post multi-leg payment (v1)                       | [Post multi-leg payment (v2)](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments)                               |
| Get multi-payment status (v1)                     | [Get multi-leg payment status (v2)](https://developers.pismo.io/pismo-docs/reference/corporate-v2-get-multileg-payment)                           |
| Schedule payment (v1)                             | [Schedule payment (v2)](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments)                                    |
| List scheduled payments                           | [List scheduled payment (v2)](https://developers.pismo.io/pismo-docs/reference/corporate-v2-list-scheduled-payment)                               |
| Get scheduled payment by ID                       | [Get scheduled payment by ID (v2)](https://developers.pismo.io/pismo-docs/reference/corporate-v2-get-scheduled-payment)                           |
| Cancel scheduled payment                          | [Cancel scheduled payment (v2)](https://developers.pismo.io/pismo-docs/reference/corporate-v2-delete-scheduled-payment)                           |
| Create division (v1)                              | [Create division (v2)](https://developers.pismo.io/pismo-docs/reference/post-division-v2)                                                         |
| List division (v1)                                | [List division (v2)](https://developers.pismo.io/pismo-docs/reference/list-division-v2)                                                           |
| Get division by code (v1)                         | [Get division by code (v2)](https://developers.pismo.io/pismo-docs/reference/get-division-by-code-v2)                                             |
| Patch division (v1)                               | [Patch division (v2)](https://developers.pismo.io/pismo-docs/reference/patch-division-v2)                                                         |
| Create earmark (v1)                               | [Create earmark (v2)](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)                                                |
| Update earmark (v1)                               | [Update earmark (v2)](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)                                     |
| Cancel earmark (v1)                               | [Cancel earmark (v2)](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)                               |
| Create dormancy configuration (v1)                | [Create dormancy configuration (v2)](https://developers.pismo.io/pismo-docs/reference/post-dormancy-config-v2)                                    |
| Update dormancy configuration (v1)                | [Update dormancy configuration (v2)](https://developers.pismo.io/pismo-docs/reference/patch-dormancy-config-v2)                                   |
| Update transaction banking account status (v1)    | [Update transaction banking account status (v2)](https://developers.pismo.io/pismo-docs/reference/patch-accounts-accountid-status-v2)             |
| Roll back transaction banking account status (v1) | [Roll back transaction banking account status (v2)](https://developers.pismo.io/pismo-docs/reference/patch-accounts-accountid-status-rollback-v2) |

</details>

#### Updated

In the [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1) event, the following new fields have been added to `trigger_reason`. These new fields provide more details about future-business-dated operations than what was previously available.

* `FUTURE_BUSINESS_DATED_OPERATION`
* `FUTURE_BUSINESS_DATED_OPERATION_CURRENT_DATE`

#### Updated

The new 400 message `Transfer must be sent by debit account` and examples have been added to the following endpoints. The error indicates that transfer requests cannot originate from a credit account.

* [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
* [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments)
* [Cancel payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-cancel-payments)

#### Updated

In the [Upload bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file) endpoint, the new 400 message `Duplicate bulk file uploaded` has been added.

#### Updated

In the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint, the following 400 error examples have been added.

* `WPMT0005: Future dated payments only supports default debit processing code`
* `WPMT0006: Future dated payments only supports default credit processing code`
* `WPMT0036 : Future dated earmark payments are not allowed`
* `WPMT0050: Payment business date cannot be earlier than earmark creation date`

#### Updated

In the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint, the following error examples have been corrected.

* For `WPMT0025`, the error message used to be `Debit earmark not permitted on a closed account`, and now it’s corrected to `Debit not permitted on a closed account`.
* For `WPMT0026`,  the error message used to be `Credit earmark not permitted on a closed account`, and now it’s corrected to `Credit not permitted on a closed account`.

#### Updated

In the [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments) endpoint, the following 400 error has been added.

* `WMLP0005: Validation error: one or more legs did not pass validation`

#### Updated

In the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint, the following 400 error example had been corrected.

* It used to be: `WEAM0015: release_datetime cannot be in the past`, but it is now corrected to: `schedule_release_datetime cannot be in the past`.

#### Updated

In the [List transactions](https://developers.pismo.io/pismo-docs/reference/get-corporate-transactions) endpoint, the new `numberOfLatestTransactionsQuery` query parameter has been added to list latest transactions based on the date specified in the `event_date` field.

#### Updated

Removed the following 400 error messages as they no longer apply.

* In [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments), removed error `WEAM0021: Earmark transaction collision detected. OrgID: org_id, EarmarkID: earmark_id, TrackingID: tracking_id`.
* In [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments), removed error `WMLP0005: Validation error: one or more legs did not pass validation`.

#### Updated

In the [Get account balance history configuration](https://developers.pismo.io/pismo-docs/reference/get-account-balance-history-configuration) endpoint, the new `end` field has been added to `previous` > `cycle_config_validity` of the 200 response payload to indicate when the balance history configuration ends.

#### Docs

The text in the information box in [Payment overview](https://developers.pismo.io/pismo-docs/docs/payment-overview#post-multi-leg-payment) has been updated to state that “You cannot use [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments) to transfer credit and debit leg payments to **different accounts** for identical amounts. For such situations, send [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) requests instead.“ Previously, the statement said “same account“ instead of “different accounts.”

</summary>

<summary class="tabContent" id="Card issuing">

### Cards

#### Updated

The [Get non-PCI card information](https://developers.pismo.io/pismo-docs/reference/get-v1-card) endpoint now requires the `x-account-id` header.

#### Updated

The `abu_enabled` field for the [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card), [Reissue card](https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue), and [Create noname card bulk](https://developers.pismo.io/pismo-docs/reference/create-bulk) endpoints has been deprecated. This field, indicating if the card should be enabled for Mastercard’s Automatic Billing Update service, is now enabled during setup. You can opt out of this service, if enabled, using the [Update card information](https://developers.pismo.io/pismo-docs/reference/patch-v2-card) endpoint.

### Card network integration

#### New

There is a new custom validation code for authorization events: Credit limit impact not found (CLF). When the authorization gets an error while trying to retrieve information from the Credit Limit Impact, the card network is notified that there is an internal error and a message is generated for this authorization. This new custom code is documented in the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events#authorization-validations) and [Validation code definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions#clf---credit-limit-impact-not-found) guides.

#### Updated

The CED (Invalid expiration date provided) response code for RuPay has been changed from 14 to 54. This update is reflected in the [Authorization validations](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events#authorization-validations) table of the Validation codes for authorization events guide and in the [CVM validation](https://developers.pismo.io/pismo-docs/docs/rule-list#cvm-validation) table of the Rule list guide. The CVM validation description has also been updated for clarification.

#### Docs

The new [Authorization discard process](https://developers.pismo.io/pismo-docs/docs/authorization-events#authorization-discard-process) section has been added to the Authorization events guide. This new section details the purchaser cancellation process and documents the authorization discard timing when a purchase does not receive confirmation via Base II and does not receive a cancellation (online or via Base II).

#### Docs

The [Validation code definitions](https://developers.pismo.io/pismo-docs/docs/validation-code-definitions) guide has been updated to display the codes definitions in alphabetical order for ease of use and many definitions have been updated for clarity.

### Disputes

#### Updated

There are new fields you can update with the [Update dispute](https://developers.pismo.io/pismo-docs/reference/put-v1-disputes-disputeid) endpoint: `disputed_amount`, `comment`, and `first_installment_amount`.

### Statements

#### Updated

The `cycle` field has been added to the 200 response for [Get scheduled charge](https://developers.pismo.io/pismo-docs/reference/get-scheduled-charge) and [List scheduled charges](https://developers.pismo.io/pismo-docs/reference/list-scheduled-charges).

#### Docs

The endpoint description for [Get program future calendars](https://developers.pismo.io/pismo-docs/reference/getcalendarlist) has been updated to explain the use of the query parameters `showCustomCalendars`, `divisionId`, and `programCalendarStrategyId`.

#### Docs

The description of the [Update multivalue program parameter values](https://developers.pismo.io/pismo-docs/reference/updateprogramparamenter) endpoint has been updated.

#### Docs

Some inaccuracies in [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals#configuring-transactions-not-used-when-calculating-interest-accruals) have been corrected.

#### Docs

In the request payload of [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4),  the `payment_datetime` field was incorrectly documented as a property of the installments array. It's now documented as a separate parameter.

</summary>

<summary class="tabContent" id="Seller management">

### Sellers

#### New

The new [List advancement requests settled](https://developers.pismo.io/pismo-docs/reference/getadvancementsbysettlement) endpoint is now available in the new “Settlements” subsection under “Seller management - Sellers”.

#### Updated

The title of “Seller management - Settlements” has been changed to "Seller management - Sellers" API and the URLs for all the endpoints in this section have been changed as follows.

* For [Block merchants for settlement](https://developers.pismo.io/pismo-docs/reference/blockmerchantsforsettlement), the URL changed from\
  `POST /settlements/actions/block` to\
  `POST /sellers/v1/settlements/actions/block`
* For [Unblock merchants for settlement](https://developers.pismo.io/pismo-docs/reference/unblockmerchantsforsettlement), the URL changed from\
  `POST /settlements/actions/unblock` to\
  `POST /sellers/v1/settlements/actions/unblock`
* For  [Get blocked merchants](https://developers.pismo.io/pismo-docs/reference/getblockedmerchants), the URL changed from\
  `GET /settlements/merchants/blocked` to\
  `GET /sellers/v1/settlements/merchants/blocked`
* For [Run settlement](https://developers.pismo.io/pismo-docs/reference/runsettlement), the URL changed from\
  `POST /settlements/actions/run` to\
  `POST /sellers/v1/settlements/actions/run`

#### Deprecated

The Create creditor endpoint is now deprecated and scheduled for removal on 30 June 2025.

</summary>

<summary class="tabContent" id="Resources">

### Pismo Control Center

#### Updated

The new "Device Registered" condition is now available in Flex Controls within the Control Center. This enables you to create a set of controls to mitigate potential fraudulent actions by individuals using non-registered devices.

### Postman

#### Docs

The [Testing Pismo API endpoints with Postman](https://developers.pismo.io/pismo-docs/docs/testing-pismo-api-endpoints-with-postman) guide has been updated for clarity and to adhere to the Pismo style guide.

</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `PUT /accounts/v2/customers/{customerId}` (`customerV2Put`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `PATCH /accounts/v1/accounts/{accountId}/customers/{customerId}/detail` (`customerV1patch`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--customers |
| `PATCH /v1/accounts/{accountId}/flex-controls/{flexControlId}` (`patch-v1-accounts-flex-control`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/migrations/balance-control` (`PostBalanceControlV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--balance-migration |
| `POST /payment-methods/v1/authorization` (`post-authorization`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payments/v1/payments/installments` (`post-payments-v1-installments`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--installments-payments |
| `POST /payment-methods/v2/payments/cancel` (`post-payments-cancel`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payment-methods/v2/transfers/cancel` (`post-transfers-cancel`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /divisions-core/v1/administrative-division` (`post-v1-admin-division`) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-deprecated |
| `POST /programs/v1/programs/template` (`CreateProgramBasedOnTemplate`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `GET /v1/bankslips/receipts` (`get-integrated-payments-api-v1-bankslips-receipts`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `GET /pix/v2/pix/out/scheduler` (`list-scheduled-transfers`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `GET /pix/v2/pix/out/scheduler/:scheduler_id/executions` (`get-scheduler-executions`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `POST /v2/pix/refunds/{refundId}/close` (`post-close-dict-refund`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--refunds |
| `POST /v2/pix/keys/delete` (`post-v2-pix-keys-delete`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--keys-part-01, KU-API-instant-payments-pix-management--keys-part-02 |
| `POST /v2/pix/infraction-reports` (`post-v2-pix-infraction-create`) | `api-specs/Instant_payments_-_Pix_management.yaml` | no | KU-API-instant-payments-pix-management--infraction-reports-part-01, KU-API-instant-payments-pix-management--infraction-reports-part-02 |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/multileg` (`corporate-v2-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `GET /corporate/v2/payments/multileg/{trackingId}` (`corporate-v2-get-multileg-payment`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/scheduled-payments` (`corporate-v2-post-scheduled-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `GET /corporate/v2/scheduled-payments` (`corporate-v2-list-scheduled-payment`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `GET /corporate/v2/scheduled-payments/{scheduledPaymentId}` (`corporate-v2-get-scheduled-payment`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId}` (`corporate-v2-delete-scheduled-payment`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/divisions` (`post-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v2/divisions` (`list-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v2/divisions/{divisionCode}` (`get-division-by-code-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PATCH /corporate/v2/divisions/{divisionCode}` (`patch-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/dormancy-config` (`post-dormancy-config-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` (`patch-dormancy-config-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--dormancy |
| `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status` (`patch-accounts-accountId-status-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status/rollback` (`patch-accounts-accountId-status-rollback-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v2/payments/confirm` (`corporate-v2-post-confirm-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/cancel` (`corporate-v2-post-cancel-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `PUT /corporate/v1/bulk-payments/{bulkId}` (`corporate-put-bulk-file`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |
| `GET /corporate/v1/corporate-transactions` (`get-corporate-transactions`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |
| `GET /bank-statements/v1/account-balances/history/config/{divisionCode}` (`get-account-balance-history-configuration`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bank-statements-part-01, KU-API-banking-transaction-banking--bank-statements-part-02 |
| `GET /wallet/v1/cards/{cardId}` (`get-v1-card`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /wallet/v2/cards` (`post-v2-card`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /wallet/v1/customers/{customerId}/accounts/{accountId}/cards/{cardId}/reissue` (`post-v1-card-reissue`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--card-reissue |
| `POST /cards/v1/bulks` (`create-bulk`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--noname |
| `PATCH /wallet/v2/cards/{cardId}` (`patch-v2-card`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `PUT /v1/disputes/{disputeId}` (`put-v1-disputes-disputeId`) | `api-specs/Card_issuing_-_Disputes.yaml` | no | KU-API-card-issuing-disputes--disputes-part-01, KU-API-card-issuing-disputes--disputes-part-02 |
| `GET /v1/accounts/{account_id}/scheduled-charges/{recurring_scheduled_charge_id}` (`get-scheduled-charge`) | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges |
| `GET /v1/accounts/{account_id}/scheduled-charges` (`list-scheduled-charges`) | `api-specs/Revolving_credit_-_Recurring_charges.yaml` | no | KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges |
| `PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}` (`updateProgramParamenter`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--multivalue-program-parameters |
| `POST /statements/v4/accounts/{accountId}/installment-payments` (`InstallmentPaymentsv4`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `GET /v1/merchants/{merchantId}/settlements/advancements` (`getAdvancementsBySettlement`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--settlements |
| `POST /v1/settlements/actions/block` (`blockMerchantsForSettlement`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--settlement-actions |
| `POST /v1/settlements/actions/unblock` (`unblockMerchantsForSettlement`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--settlement-actions |
| `GET /v1/settlements/merchants/blocked` (`getBlockedMerchants`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--settlement-actions |
| `POST /v1/settlements/actions/run` (`runSettlement`) | `api-specs/Seller_management_-_Sellers.yaml` | no | KU-API-seller-management-sellers--settlement-actions |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-v1-balances-config-1` | API; Balance configurations API; Create balance configuration; balance configuration | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `getcalendarlist` | Get program future calendars | not found in the current OpenAPI specifications. Name-based inference: link text "Get program future calendars" equals the endpoint name "Get program future calendars" in the removed-endpoints list (row Revolving / Statements, date removed `5/4/2026`). This is a match on the endpoint name, not on an identifier. |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/3-january-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/3-january-2025 | `b2601955a852bfef…` | not stated |

## Related knowledge units

- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bank-statements-part-01` — API reference: Banking - Transaction banking — Bank statements (part 1 of 2)
- `KU-API-banking-transaction-banking--bank-statements-part-02` — API reference: Banking - Transaction banking — Bank statements (part 2 of 2)
- `KU-API-banking-transaction-banking--bulk-payment-files` — API reference: Banking - Transaction banking — Bulk payment files
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--dormancy` — API reference: Banking - Transaction banking — Dormancy
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-banking-transaction-banking--transactions` — API reference: Banking - Transaction banking — Transactions
- `KU-API-card-issuing-cards--card-reissue` — API reference: Card issuing - Cards — Card reissue
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-cards--noname` — API reference: Card issuing - Cards — Noname
- `KU-API-card-issuing-disputes--disputes-part-01` — API reference: Card issuing - Disputes — Disputes (part 1 of 2)
- `KU-API-card-issuing-disputes--disputes-part-02` — API reference: Card issuing - Disputes — Disputes (part 2 of 2)
- `KU-API-core-platform-accounts--customers` — API reference: Core platform - Accounts — Customers
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-instant-payments-pix-management--infraction-reports-part-01` — API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)
- `KU-API-instant-payments-pix-management--infraction-reports-part-02` — API reference: Instant payments - Pix management — Infraction reports (part 2 of 2)
- `KU-API-instant-payments-pix-management--keys-part-01` — API reference: Instant payments - Pix management — Keys (part 1 of 2)
- `KU-API-instant-payments-pix-management--keys-part-02` — API reference: Instant payments - Pix management — Keys (part 2 of 2)
- `KU-API-instant-payments-pix-management--refunds` — API reference: Instant payments - Pix management — Refunds
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-migrations--balance-migration` — API reference: Migrations — Balance migration
- `KU-API-platform-setup-divisions--administrative-divisions-deprecated` — API reference: Platform setup - Divisions — Administrative divisions (deprecated)
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-recurring-charges--recurring-scheduled-charges` — API reference: Revolving credit - Recurring charges — Recurring scheduled charges
- `KU-API-revolving-credit-statements--multivalue-program-parameters` — API reference: Revolving credit - Statements — Multivalue program parameters
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-API-seller-management-sellers--settlement-actions` — API reference: Seller management - Sellers — Settlement actions
- `KU-API-seller-management-sellers--settlements` — API reference: Seller management - Sellers — Settlements
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
