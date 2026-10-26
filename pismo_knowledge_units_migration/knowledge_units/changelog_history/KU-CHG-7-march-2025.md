---
ku_id: KU-CHG-7-march-2025
title: 'Changelog: 7 March 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/7-march-2025.md
  sha256: 0b1dbcb9498dde657fc9d1059617a151cda1e78f4fb90f9e2eb6b80798c3c765
  url: https://developers.pismo.io/pismo-docs/changelog/7-march-2025
  role: changelog_post
  updated_at: ''
operations:
- CreateProcessingCode
- CreateProgramCalendarStrategy
- InstallmentPaymentsv4
- PostTransactionsV1
- UpdateStatementsDueDate
- corporate-v2-post-cancel-payments
- corporate-v2-post-confirm-payments
- corporate-v2-post-multileg-payments
- corporate-v2-post-payments
- createTransactionCategory
- delete-integrated-payments-api-v1-ebill-registration-accounts-accountId
- get-embossing-history
- get-integrated-payments-api-v1-ebill-registration-accounts-accountId
- get-v1-accounts-flex-control
- patch-corporate-v2-earmarks-earmarkid
- post-account
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-division-v2
- post-holiday
- post-integrated-payments-api-v1-ebill-registration-accounts-accountId
- post-payments-v1-installments-cancel
- post-payments-v1-payments
- post-v1-accounts-flex-controls
- post-v1-admin-division
- post-v2-admin-division
- updateTransactionCategoryInterest
related_kus:
- KU-API-banking-integrated-payments--ebill-registration
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-card-issuing-cards--embossing-data
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-payment-methods--installments-payments
- KU-API-core-platform-payment-methods--payments
- KU-API-migrations--transaction-migration
- KU-API-platform-setup-divisions--administrative-divisions-deprecated
- KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated
- KU-API-platform-setup-holidays--holidays-deprecated
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-API-revolving-credit-calendar-management--program-calendar-strategies
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-API-revolving-credit-statements--refinancing
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 7 March 2025
coverage_window: 7 February and 7 March 2025
---

# Changelog: 7 March 2025

**KU ID:** `KU-CHG-7-march-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **7 March 2025** (changes between 7 February and 7 March 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated".

## Topics covered

Core platform - Orgs operation; Integrated payments - eBill feature; Data and reporting - Regulatory scheduled reports; Resources - Control Center; Accounts; Authentication; Flexible transaction controls; Migrations; Payments; Security; Setup; Support; Files; Interest management; Transaction banking; Card network integration; Embossing; Network transactions; Statements; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/7-march-2025

<!-- source:begin path=changelog/7-march-2025.md part=0-end -->

# 7 March 2025

Changes between 7 February and 7 March 2025

<div class="customTab"></div>

<summary class="tabContent" id="New features">

### Core platform - Orgs operation

#### New

The new Platform setup - [Orgs operation](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) API is now available. This API introduces enhanced endpoints for creating and managing processing codes and reversal processing codes. Endpoints with the same name in the Core platform - [Payments configurations](https://developers.pismo.io/pismo-docs/reference/post-processing-code-by-tenant) API, Processing codes section, are now deprecated, as listed in the [deprecation schedule](https://developers.pismo.io/pismo-docs/docs/deprecation-schedule).

The new Orgs operation API simplifies internal automatic creation of transaction types through the created processing codes. The new processing code structure reduces the risk of financial penalties. Previous structure was very manual, and if a person incorrectly configured a balance impact, it generated a higher-level incident that could be subject to financial penalties.

### Integrated payments - eBill feature

#### New

The new [eBill feature](https://developers.pismo.io/pismo-docs/docs/banking-overview#ebill) is now available. This feature offers an electronic view of bank slips linked to the customer’s document number, simplifying bill payment process. Customers can pay bank slips via internet banking or a banking app. The following endpoints were created for this feature.

* [Register eBill](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-ebill-registration-accounts-accountid) for registering document number with the eBill service.
* [Get eBill registration](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-ebill-registration-accounts-accountid) for retrieving eBill registration information.
* [Delete eBill registration](https://developers.pismo.io/pismo-docs/reference/delete-integrated-payments-api-v1-ebill-registration-accounts-accountid) for deleting eBill registration if customers no longer wish to use this feature.

### Data and reporting - Regulatory scheduled reports

#### New

Pismo now has the capability to generate scheduled reports in a format required by regulatory entities such as central banks and government agencies. The new **Regulatory scheduled reports** section includes the following new guides.

* [Base scheduled reports](https://developers.pismo.io/pismo-docs/docs/base-scheduled-reports)
* [Regulatory scheduled reports](https://developers.pismo.io/pismo-docs/docs/regulatory-scheduled-reports)
* [Brazilian reports](https://developers.pismo.io/pismo-docs/docs/brazilian-reports)

The guides for the individual scheduled reports are now under the [Base scheduled reports](https://developers.pismo.io/pismo-docs/docs/base-scheduled-reports) section.

### Resources - Control Center

#### New

**Multi-account management**

The account management feature in Pismo Control Center was redesigned to improve the user experience.

* Account search results now show all accounts held or used by a customer. Select any account to easily switch among different customer accounts directly from anywhere in the feature.
* A breadcrumb trail helps you understand your current location within an account.
* New **Account configurations** and **Actions** menus provide access to customer information and account operations.

This feature is being introduced to all environments during March 2025.

**Notifications**

Control Center now has a **Notifications** icon at the top of all screens. Notifications keep you informed about asynchronous processes (such as program creation status updates), error messages, and other announcements.

</summary>

<summary class="tabContent" id="Core platform">

### Accounts

#### Deprecated

The `printed_name` field was deprecated in the Accounts API endpoints. This field can be set during card operations.

### Authentication

#### Docs

The [Endpoints that require an external account ID-specific token](https://developers.pismo.io/pismo-docs/docs/endpoints-that-require-an-external-id-token) guide was updated with the most current list and endpoint links.

### Flexible transaction controls

#### Docs

In the [Flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls) guide, introduction was updated to indicate that Pismo Control Center can be used for managing program-level flex controls.

#### Docs

In the [Flexible transaction controls](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) API, descriptions for the `max_limit` and `max_amount` fields were updated to correctly display calculations for the number of decimal places.

#### Docs

In the [Get account flex control](https://developers.pismo.io/pismo-docs/reference/get-v1-accounts-flex-control) endpoint, the `deny_code` response field was added.

### Migrations

#### Docs

In the [Migrate transactions](https://developers.pismo.io/pismo-docs/reference/posttransactionsv1) endpoint, documentation was added for the new `migration.type` request field. Also a link was added to the new [Instant payment transaction migration completed](https://developers.pismo.io/events/docs/migration-instant-payment-outgoing-1) event (generated when `migration.type` is `INSTANT_PAYMENT`).

### Payments

#### Updated

The new [Cancel installments payment](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-installments-cancel) endpoint is now available.

#### Docs

In the [Transfer funds](https://developers.pismo.io/pismo-docs/reference/post-payments-v1-payments) endpoint, added example code in the 400 response for "Flex controls evaluation results" .

#### Docs

In the [Hold funds](https://developers.pismo.io/pismo-docs/docs/hold-funds) guide, the event names were updated.

### Security

#### New

As a critical aspect of cybersecurity, the Control Center has implemented a strong list of password requirements. A new security guide was created to define and explain [Best practices for Control Center passwords](https://developers.pismo.io/pismo-docs/docs/cc-pw-best-practices).

#### Docs

The [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials) guide was updated to correctly reference the `server_secret` key instead of the previously incorrect reference to `secret_key`.

### Setup

#### Docs

The “Processing codes and transaction types” guide was rewritten and split into two guides:

* The [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) lists the standard processing codes and standard reversal processing codes that are granted to every new organization.
* The [Transaction types](https://developers.pismo.io/pismo-docs/reference/transactiontypes) lists the standard processing code to transaction types mapping for transaction flows.

#### Docs

The [Divisions](https://developers.pismo.io/pismo-docs/reference/post-v1-admin-division) API, which was previously undocumented, is now documented. A new header and section - [Admin divisions transaction banking](https://developers.pismo.io/pismo-docs/reference/post-v2-admin-division) - were added for V2 transaction banking endpoints.

#### Docs

In the [Create holiday](https://developers.pismo.io/pismo-docs/reference/post-holiday) endpoint, the `next_business_date parameter` was renamed to `working_date`.

#### Docs

Added "Percentage for calculating the minimum payment amount" program parameter to [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table). It was in the Pismo Control Center, but missing from the guide.

### Support

#### Docs

The new [Modify a service request](https://developers.pismo.io/pismo-docs/docs/modify-a-service-request) guide documents the following:

* A **Cancel** button displays on the portal so that clients can cancel a request at any time.
* After 30 minutes, for incident requests that are Unclassified or classified as P1 or P2, an **Escalate** button displays on the portal so that clients can escalate the ticket.
* In the [Incident resolution process](https://developers.pismo.io/pismo-docs/docs/incident-lifecycle#incident-resolution-processguide) section, the incident request status **In Dev** was changed to **In Progress**.

</summary>

<summary class="tabContent" id="Data and reporting">

### Files

#### Docs

The [AWS event file configuration tutorial](https://developers.pismo.io/pismo-docs/docs/aws-event-file-configuration-tutorial) was updated to include a sample code block for sharing the shell script **validate-s3-integration.sh**. This is a temporary solution until a permanent solution is developed in the future.

 </summary>

<summary class="tabContent" id="Core banking">

### Interest management

#### Docs

Updated many of the event descriptions for [Interest management](https://developers.pismo.io/events/docs/interest-management-interest-accrual-success-1) to correct some of them and improve others.

### Transaction banking

#### Updated

In the following endpoints, the 409​ conflict error was added to indicate that a duplicate tracking or earmark ID is already in use: "This error occurs when the client sends a duplicate tracking ID that is either already in use by another account, or by the same account with a different earmark ID than the one used in the original payment​."

* [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
* [Confirm payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-confirm-payments)
* [Cancel payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-cancel-payments)
* [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
* [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
* [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)

#### Updated

In the [Create transaction bank account](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint, the new `account_creation_datetime` field indicates when the account was created.

#### Updated

The "Operations blocked for account" error message was added to the following endpoints. This error is issued when an account involved in the transaction has an active operation block for the account's division, program, or org. For more details, refer to [Create operation block](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-operation-blocks).

* [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
* [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
* [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)
* [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-multileg-payments)

#### Docs

The [Manage account statuses](https://developers.pismo.io/pismo-docs/docs/managing-account-statuses) guide was updated with additional information on how dormancy configuration impacts transaction banking account statuses.

#### Docs

A supplementary note was added in the following documentation. The note states that if no timezone is specified for a division, the division inherits its timezone from its parent. However, if there is no timezone specified in the parent, Pismo defaults to using UTC for the division.

* In [Step 3 - Add divisions](https://developers.pismo.io/pismo-docs/docs/corporate-banking-launch-reference#step-3--add-divisions) in the Getting started with demand deposit accounts (DDAs) guide.
* In the `timezone` field of the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint.

</summary>

<summary class="tabContent" id="Card issuing">

### Card network integration

#### Updated

A change was made to field 126, subfield 10 of Visa's Authorization message. Previously, all data from field 126 was blocked. Now, subfield 10 presents as:

```json
"f126_visa_private_use_fields": {  
    sf10_cvv2_authorization_request_data: ""  
  }
```

Considering only position 1 of this field, the only possible values are  0, 1, 2, 3, 4, or 9 per the VisaNet Authorization-Only Online Messages guide, page 737. This change is reflected in the Visa [iso8583 message event example](https://developers.pismo.io/pismo-docs/docs/authorization-events#iso8583-message-event-examples) in the Authorization events guide.

#### Updated

The denial code for ELO for Account blocked (CND) was changed from 57 to 62. This change is reflected in the [Validation codes for authorization events](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events) guide and in the [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list#account-status-validation) guide.

### Embossing

#### Docs

There is a new [Troubleshooting embossing errors](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing#troubleshooting-embossing-errors) section in the Physical card embossing guide.

#### Docs

The [Get card embossing history](https://developers.pismo.io/pismo-docs/reference/get-embossing-history) endpoint documentation was updated to include a  “204 - No content. Card has no embossing history” HTTP response.

### Network transactions

#### Docs

The example for the `replacement_amount` parameter within the [Card network authorization return sent](https://developers.pismo.io/events/docs/networktransactions-network-message-1) event was updated to reflect a correct example.

### Statements

#### New

The new Revolving credit - [Calendar management](https://developers.pismo.io/pismo-docs/reference/createprogramcalendarstrategy) API is now available. Currently, only one calendar management strategy is available: `FIXED_CYCLE_CLOSING`.

#### New

The following new program parameters are now available and documented in the [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-parameters) guide.

* `CHARGE_IOF_INDEPENDENTLY`
* `CHARGE_FINE_INDEPENDENTLY`
* `EXCLUDE_TXN_CATEGORY_CHARGE_IOF_INDEPENDENTLY`
* `EXCLUDE_TXN_CATEGORY_CHARGE_FINE_INDEPENDENTLY`

Note that the first two are actually single value parameters, but they are used in conjunction with the two multivalue parameters, so they are documented on the Multivalue program parameter page for convenience.

#### Docs

The [Credit liquidation](https://developers.pismo.io/pismo-docs/docs/credit-liquidation) guide was updated to correctly reflect the default for the `Number of days to block the account for unpaid statement` parameter is “10”.

#### Docs

The description of [Accruals](https://developers.pismo.io/pismo-docs/docs/understanding-statements#accruals) in the Understanding statements guide was updated for clarity and the second diagram in this section was updated to correct a few mistakes in the legend.

#### Docs

The [Calendars and holidays in credit card accounts](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-credit-card-accounts) guide was moved from **Core banking** to **Card issuing > Understanding statements**.

#### Docs

The [Setting up holidays within administrative divisions](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-credit-card-accounts#setting-up-holidays-within-administrative-divisions) and [Linking administrative divisions](https://developers.pismo.io/pismo-docs/docs/calendars-and-holidays-in-credit-card-accounts#linking-administrative-divisions) section now include a warning note about associating the account with the division.

#### Docs

The descriptions of the following fields in the [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) endpoint were updated to indicate that no more than 2 digits should follow the decimal point.

* `total_amount`
* `principal_amount`
* `interest_amount`
* `iof_amount`
* `daily_iof_amount`

#### Docs

In [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table), the description for `Due date exchange control` was updated. The line “Valid only if STANDARD CALENDAR SELECTION = false” was removed, because the STANDARD CALENDAR SELECTION is no longer used.

#### Docs

In the [Create payment agreement](https://developers.pismo.io/pismo-docs/reference/installmentpaymentsv4) endpoint documentation, a note was added to the definition of the `installments` body parameter.

#### Docs

The description of the [Change due date](https://developers.pismo.io/pismo-docs/reference/updatestatementsduedate) endpoint was updated.

#### Docs

The [Calculating interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals#configuring-transactions-not-used-when-calculating-interest-accruals) guide was updated to introduce the topic, remove duplicate information, and link to [Setting transaction types to block accrual charges](https://developers.pismo.io/pismo-docs/docs/configuring-transaction-types-to-not-accrue-charges) for more details and some additional information.

#### Docs

The [Managing due date, cycle closing date, and grace period](https://developers.pismo.io/pismo-docs/docs/managing-grace-period#customizing-the-grace-period-for-a-due-date) guide was rewritten to correct some errors and improve the clarity.

#### Docs

The following updates were made in statements documentation.

* Changed guide title from “Configuring transaction types to not accrue charges” to [Setting transaction types to block accrual charges](https://developers.pismo.io/pismo-docs/docs/configuring-transaction-types-to-not-accrue-charges), which more accurately describes the contents, and updated text for clarity.
* Changed section title from “Configuring transactions not used when calculating interest accruals” to [Setting transaction types to block accrual charges](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals#setting-transaction-types-to-block-accrual-charges) and updated the label of the link in that section.
* Changed section title from “Balance program parameters” to [Additional program parameters for interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals#additional-program-parameters-for-interest-accruals) and modified the introductory text.
* In the table in [Additional program parameters for interest accruals](https://developers.pismo.io/pismo-docs/docs/calculating-interest-accruals#additional-program-parameters-for-interest-accruals), removed the “Minimo boleto” entry, since it is explained in an earlier section, and updated the "Stop accrual # of days" program parameter with the correct name (it was previously listed incorrectly as "Stop accrual (days)").

#### Docs

In [How the program discharges transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-discharges-transactions), the “Payment hierarchy” section was updated.

#### Docs

The [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements) was updated to say "minimum amount due (MAD)" or "MAD" instead of "minimum amount".

#### Docs

Description of the `minimum_value` field was updated in [Create transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) and [Update transaction category interest](https://developers.pismo.io/pismo-docs/reference/updatetransactioncategoryinterest) endpoints.

#### Docs

Several new examples were added to the “Examples” section of [Overdue tolerance](https://developers.pismo.io/pismo-docs/docs/overdue-tolerance).

</summary>

<summary class="tabContent" id="Resources">

### Control Center

#### Updated

In Control Center, the program creation flow was redesigned to provide an improved user experience.

* Importing and exporting programs is now consolidated in the Programs area.
* Program download is now available on the exported program’s details page.
* Added new option to clone a program within the current environment.

#### Updated

When `SEND_RULES_AUTHORIZATION_PARAMETER` is disabled for a program, Control Center now displays an indicator on the list of flex controls and on the flex control details screen.

#### Updated

Two new fields are now available for setting up flex controls: `response_code` and `custom_code`. These enable you to have customized information for denied authorizations. To configure these fields, you must open a service request.

#### Docs

The [Access profiles and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles) guide was updated to replace outdated information and to add the **Collections analyst** role.

<br />

</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /orgs-operation/v1/processing-codes` (`CreateProcessingCode`) | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /v1/ebill-registration/accounts/{accountId}` (`post-integrated-payments-api-v1-ebill-registration-accounts-accountId`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |
| `GET /v1/ebill-registration/accounts/{accountId}` (`get-integrated-payments-api-v1-ebill-registration-accounts-accountId`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |
| `DELETE /v1/ebill-registration/accounts/{accountId}` (`delete-integrated-payments-api-v1-ebill-registration-accounts-accountId`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `GET /v1/accounts/{accountId}/flex-controls/{flexControlId}` (`get-v1-accounts-flex-control`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `POST /v1/migrations/transactions` (`PostTransactionsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--transaction-migration |
| `POST /payments/v1/payments/installments/cancel` (`post-payments-v1-installments-cancel`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--installments-payments |
| `POST /payments/v1/payments` (`post-payments-v1-payments`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payments |
| `POST /divisions-core/v1/administrative-division` (`post-v1-admin-division`) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-deprecated |
| `POST /divisions-core/v2/administrative-division` (`post-v2-admin-division`) | `api-specs/Platform_setup_-_Divisions.yaml` | **yes** | KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated |
| `POST /holidays-core/v1/holiday` (`post-holiday`) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-deprecated |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/confirm` (`corporate-v2-post-confirm-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/payments/cancel` (`corporate-v2-post-cancel-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v1/corporate-accounts` (`post-account`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v2/payments/multileg` (`corporate-v2-post-multileg-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | **yes** | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/divisions` (`post-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /embossing/v1/cards/{cardId}/history` (`get-embossing-history`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--embossing-data |
| `POST /v1/programs/{programId}/calendar-strategies` (`CreateProgramCalendarStrategy`) | `api-specs/Revolving_credit_-_Calendar_management.yaml` | no | KU-API-revolving-credit-calendar-management--program-calendar-strategies |
| `POST /statements/v4/accounts/{accountId}/installment-payments` (`InstallmentPaymentsv4`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--refinancing |
| `PUT /statements/v1/accounts/{accountId}/statements/due-date` (`UpdateStatementsDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /statements-v2/v1/transactions-categories` (`createTransactionCategory`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` (`updateTransactionCategoryInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-processing-code-by-tenant` | Payments configurations; creating a processing code | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `transactiontypes` | Transaction types; transaction type | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `corporate-post-v1-operation-blocks` | Create operation block | not found in the current OpenAPI specifications. Name-based inference: link text "Create operation block" equals the endpoint name "Create operation block" in the removed-endpoints list (row Banking / Transaction banking, date removed `2/20/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`corporate-post-v2-operation-blocks` (POST /corporate/v2/operations-blocks)); no source states that it replaces the removed endpoint. |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/7-march-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/7-march-2025 | `0b1dbcb9498dde65…` | not stated |

## Related knowledge units

- `KU-API-banking-integrated-payments--ebill-registration` — API reference: Banking - Integrated payments — eBill registration
- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-card-issuing-cards--embossing-data` — API reference: Card issuing - Cards — Embossing data
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-payment-methods--installments-payments` — API reference: Core platform - Payment methods — Installments payments
- `KU-API-core-platform-payment-methods--payments` — API reference: Core platform - Payment methods — Payments
- `KU-API-migrations--transaction-migration` — API reference: Migrations — Transaction migration
- `KU-API-platform-setup-divisions--administrative-divisions-deprecated` — API reference: Platform setup - Divisions — Administrative divisions (deprecated)
- `KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated` — API reference: Platform setup - Divisions — Administrative divisions V2 (deprecated)
- `KU-API-platform-setup-holidays--holidays-deprecated` — API reference: Platform setup - Holidays — Holidays (deprecated)
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-API-revolving-credit-calendar-management--program-calendar-strategies` — API reference: Revolving credit - Calendar management — Program calendar strategies
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-API-revolving-credit-statements--refinancing` — API reference: Revolving credit - Statements — Refinancing
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
