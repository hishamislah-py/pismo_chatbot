---
ku_id: KU-CHG-2-may-2025
title: 'Changelog: 2 May 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/2-may-2025.md
  sha256: 83210e936ef3dff0dddf14fee5f00161d785940d94ba1ce5082630f2153a31f3
  url: https://developers.pismo.io/pismo-docs/changelog/2-may-2025
  role: changelog_post
  updated_at: ''
operations:
- GetAccountAccrualsV2
- PatchTransactionFlow
- PostDisputeV1
- PostOnUsAuthorizationsV1
- PostTransactionFlow
- cancel-split-request
- corporate-put-bulk-file
- corporate-v2-post-scheduled-payments
- get-accounts-v1-accounts
- get-merchant-balance
- get-sale-split-request-totals
- get-split-details
- get-split-requests
- get-v1-account-balance
- get-v1-account-limit
- get-v1-accounts-limits-related-accounts
- getAccountAccrualsV3
- getFeaturesByAccountStatus
- list-division-v2
- patch-corporate-v2-earmarks-earmarkid
- patch-v1-accounts-flex-control
- patch-v1-customers-flex-control
- patchFeaturesByAccountStatus
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-division-v2
- post-split-request
- post-v1-bulletin
- post-v1-bulletin-setup
- post-v2-holiday
- postFeaturesByAccountStatus
related_kus:
- KU-API-banking-transaction-banking--bulk-payment-files
- KU-API-banking-transaction-banking--divisions
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-card-issuing-protection-bulletin--bulletin
- KU-API-card-issuing-protection-bulletin--rules
- KU-API-core-platform-accounts--accounts
- KU-API-core-platform-balances-and-limits--account-balances
- KU-API-core-platform-balances-and-limits--related-accounts
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-flex-controls--customer-flex-controls-part-01
- KU-API-core-platform-flex-controls--customer-flex-controls-part-02
- KU-API-core-platform-ledger--account-limits
- KU-API-core-platform-transactions--transaction-flows
- KU-API-migrations--dispute-migration
- KU-API-migrations--on-us-authorization-migration
- KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat
- KU-API-revolving-credit-configurations--features-by-account-status
- KU-API-revolving-credit-statements--accruals
- KU-API-seller-management-transactions--balance
- KU-API-seller-management-transactions--split-requests
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 2 May 2025
coverage_window: 4 April and 2 May 2025
---

# Changelog: 2 May 2025

**KU ID:** `KU-CHG-2-may-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **2 May 2025** (changes between 4 April and 2 May 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

## Topics covered

Card issuing - Get started with card issuing; Card issuing - Card network integrations; Seller management - Marketplace; Accounts; Balance configurations; Flexible transaction controls; Ledger; Migrations; Setup; Transactions; Transaction banking; Card network integrations; Direct network transactions; Statements; Protection Bulletin; Lending; Merchants; Pismo Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/2-may-2025

<!-- source:begin path=changelog/2-may-2025.md part=0-end -->

# 2 May 2025

Changes between 4 April and 2 May 2025

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### Card issuing - Get started with card issuing

#### Docs

Your ultimate resource for card issuing is here! Dive into the latest detailed guide [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-with-card-issuing), meticulously crafted to provide you with everything you need to know about setting up card issuing on the Pismo platform.

This comprehensive guide offers clear step-by-step instructions for launching your card issuing program. It outlines the seven steps you take to get your card issuing program up and running.

* [1: Plan](https://developers.pismo.io/pismo-docs/docs/step-1-plan): Identify the integration decisions to consider.
* [2: Establish a framework](https://developers.pismo.io/pismo-docs/docs/step-2-establish-a-framework): Build the foundational processes and permissions for your program.
* [3: Create your programs](https://developers.pismo.io/pismo-docs/docs/step-3-create-your-programs): Design your card issuing program.
* [4: Create accounts and customers](https://developers.pismo.io/pismo-docs/docs/step-4-create-accounts-and-customers): Add accounts and customers to use your card issuing program.
* [5: Create cards](https://developers.pismo.io/pismo-docs/docs/step-5-create-cards): Create your customized cards.
* [6: Test](https://developers.pismo.io/pismo-docs/docs/step-5-test): Ensure your program works correctly before launching it.
* [7: Monitor](https://developers.pismo.io/pismo-docs/docs/step-6-monitor): Continuously monitor your program’s performance and provide ongoing customer support.

### Card issuing - Card network integrations

#### New

A new option was added to the [available limits validation](https://developers.pismo.io/pismo-docs/docs/rule-list#available-limits-validation) in ledger to allow customers to perform a dry run validation. In this case, the ledger validations are performed as a simulation to check if the account balance would be impacted, with no actual impact to the account balance. Dry run results are returned in the validation\_results field in the anti-fraud payload. The dry run can be performed for `SKIPPED` and `REJECTED` statuses, for specific reasons. Details are included in the [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list#available-limits-validation) guide.

### Seller management - Marketplace

#### New

The new Split transactions feature is now live. This feature allows for dividing a single transaction into different categories or assign portions to various accounts. This is particularly useful for handling shared expenses, allocating costs across different budget categories, or separating business and personal expenses. This new feature includes the following endpoints:

* [Create split request](https://developers.pismo.io/pismo-docs/reference/post-split-request)
* [Cancel split request](https://developers.pismo.io/pismo-docs/reference/cancel-split-request)
* [List split requests](https://developers.pismo.io/pismo-docs/reference/get-split-requests)
* [Get split request details](https://developers.pismo.io/pismo-docs/reference/get-split-details)
* [Get split request totals](https://developers.pismo.io/pismo-docs/reference/get-sale-split-request-totals)
* [Get merchant balance](https://developers.pismo.io/pismo-docs/reference/get-merchant-balance)

</summary>

<summary class="tabContent" id="Core platform">
  ### Accounts

#### Updated

For the [Get account](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts) endpoint response, the `blocked_amount` field is always going to be null. To get this information, you can call [List account limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-limit) and look at the `held_funds` field.

### Balance configurations

#### Updated

In the [balance configuration](https://developers.pismo.io/pismo-docs/reference/post-v1-balances-config-1) endpoints, the enum values for the `amount` field in the `configs.scenarios.result` object were updated (the `principal_amount` option was removed).

### Flexible transaction controls

#### Updated

In the [Evaluation requested](https://developers.pismo.io/events/docs/audit-evaluation-requested-1) event, the `custom_code` and `evaluated_controls` fields were added to the `object.result` object.

#### Updated

In the [Account flex control created](https://developers.pismo.io/events/docs/audit-account-spending-limit-created-1) and [Account flex control updated](https://developers.pismo.io/events/docs/audit-account-spending-limit-updated-1) events, `object` field, the `account_id` field is now available.

#### Docs

The `time_zone` field now correctly shows up in documentation for the following endpoints:

* [Update account flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-accounts-flex-control)
* [Update customer flex control](https://developers.pismo.io/pismo-docs/reference/patch-v1-customers-flex-control)

### Ledger

#### Updated

The `currency_code` and `currency_numeric_code` fields are now available in the [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) event and in the following endpoints:

* [Get daily account balance limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-balance)
* [List account limits](https://developers.pismo.io/pismo-docs/reference/get-v1-account-limit)
* [Get related accounts](https://developers.pismo.io/pismo-docs/reference/get-v1-accounts-limits-related-accounts)

### Migrations

#### Updated

Documentation for the [Migrate on-us authorizations](https://developers.pismo.io/pismo-docs/reference/postonusauthorizationsv1) endpoint was updated with the new object `InstallmentsDetails`.

#### Updated

The object `PostDisputeV1Request`  was added to the [Migrate disputes](https://developers.pismo.io/pismo-docs/reference/postdisputev1) endpoint.

#### Updated

The error message sent by the [Migrate disputes](https://developers.pismo.io/pismo-docs/reference/postdisputev1) endpoint was improved. This message is sent when the endpoint requires information about the clearing file that was previously provided by client.

#### Docs

The [Migrations](https://developers.pismo.io/pismo-docs/docs/migrations-overview) guide was updated with information about migrating balance controls and accruals.

### Setup

#### Docs

The [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide was updated with additional information and corrections.

### Transactions

#### Updated

The following error code was added to the [Create transaction flow](https://developers.pismo.io/pismo-docs/reference/posttransactionflow)  and [Update transaction flow](https://developers.pismo.io/pismo-docs/reference/patchtransactionflow) endpoints:

* ETRC04003: The provided amount type is already configured for the processing code

The following error codes were added to the [Create transaction flow](https://developers.pismo.io/pismo-docs/reference/posttransactionflow) endpoint:

* ETRC04004: The provided transaction type is already configured for the processing code
* ETRC04005: The provided amount type conflicts with an existing configured amount type for the processing code

</summary>

<summary class="tabContent" id="Core banking">
  ### Transaction banking

#### Updated

The new 400 error message "Misconfigured administrative division" was added to the following endpoints. This error occurs when customers send the wrong data type in the `metadata` field from the [Create holiday](https://developers.pismo.io/pismo-docs/reference/post-v2-holiday) endpoint.

* [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
* [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
* [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)

#### Updated

The error message "Account has not finished onboarding" was added to the following endpoints. This validation error occurs when an account is not yet fully onboarded but begins to accept payments.

* [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
* [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments)

#### Updated

The `division_id` field was added to the 200 and 201 response payloads of the following endpoints:

* [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2)
* [List division](https://developers.pismo.io/pismo-docs/reference/list-division-v2)

#### Docs

In the [Upload bulk file](https://developers.pismo.io/pismo-docs/reference/corporate-put-bulk-file) endpoint, step 2 in the **Detailed flow** in the description is now changed to “The server processes the request and responds with a 200 OK status, indicating that the file upload request is complete.“ Previously, it was “The server processes the request and responds with 307 Temporary Redirect instructing the client to forward the request to a pre-signed URL provided in the Location header.“

#### Docs

The following guides are now available:

* [Back-value-dated transactions](https://developers.pismo.io/pismo-docs/docs/back-value-dated-txns)
* [Future-value-dated-transactions](https://developers.pismo.io/pismo-docs/docs/future-value-dated-txns)

#### Docs

Additional information is now available in the File signature and encryption guide.

In the [Before you begin](https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption#before-you-begin) section:

* When sending a bulk file, both the original file and the signature file must be included.
* The original file refers to the input bulk file.
* The original file must be encrypted using an AES key after it has been signed. You can request an AES key by calling the Get AES key endpoint.
* The original and signature files should have the extensions `.original` and `.sign`, respectively.

In the [Signature file format](https://developers.pismo.io/pismo-docs/docs/file-signature-and-encryption#signature-file-format) section, the signature file is a text file containing a JSON object with the signature data, the JSON object contains the following fields:

* `org_id`: Tenant identification.
* `signing_key_id`: ID of the public key corresponding to the private key used to sign the file.
* `bulk_id`: ID of the bulk as specified in the original file.
* `signature`: Signature encoded in base64.

</summary>

<summary class="tabContent" id="Card issuing">
  ### Card network integrations

#### Docs

The custom code for [card inputted expiration date validation](https://developers.pismo.io/pismo-docs/docs/rule-list#card-inputted-expiration-date-validation) in the Rule list guide was updated to reflect the correct code of CED.

#### Docs

The Validation results example for [Validation results data](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations#validation-results-data) has been updated to represent a situation where flex controls are enabled. This is part of the Authorization validation rules for card network operations guide.

### Direct network transactions

#### Fixed

The **List authorizations** endpoint was removed from the Authorizations API reference documentation as it is for internal Pismo use only.

### Statements

#### New

The new section in the API reference - **Features by account status** - contains 3 new endpoints:

* [Configure features by account status](https://developers.pismo.io/pismo-docs/reference/postfeaturesbyaccountstatus)
* [List features by account status](https://developers.pismo.io/pismo-docs/reference/getfeaturesbyaccountstatus)
* [Update features by account status](https://developers.pismo.io/pismo-docs/reference/patchfeaturesbyaccountstatus)

#### Updated

In the 200 response payload of the [List account accruals v3](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv3) and [List account accruals v2](https://developers.pismo.io/pismo-docs/reference/getaccountaccrualsv2) endpoints, the new  `stop_accrual_reason` field was added to the `additional_info` object.

### Protection Bulletin

#### New

Protection Bulletin (PB) endpoints - [Register card for Protection Bulletin](https://developers.pismo.io/pismo-docs/reference/post-v1-bulletin) and [Create Protection Bulletin rule](https://developers.pismo.io/pismo-docs/reference/post-v1-bulletin-setup) - were redesigned with specific objects for each network Pismo’s PB supports - ELO, Mastercard, and Visa. The [Protection Bulletin](https://developers.pismo.io/pismo-docs/docs/protection-bulletin) guide was updated and moved to the Cards management section.

</summary>

<summary class="tabContent" id="Digital lending">
  ### Lending

#### Docs

In the [Loan repayment updated](https://developers.pismo.io/events/docs/lending-repayment-update-1) event, the required `account_id` is now documented correctly.

</summary>

<summary class="tabContent" id="Seller management">
  ### Merchants

#### Updated

The new [Get merchant balance](https://developers.pismo.io/pismo-docs/reference/get-merchant-balance) endpoint is now available in the Seller management - Transactions API. This endpoint provides an estimate of the available funds in the merchant account on a specified target date. It takes into account the scheduled merchant transactions in the specified marketplace to calculate the estimated values.

</summary>

<summary class="tabContent" id="Resources">
  ### Pismo Control Center

#### New

Pismo Control Center now enables you to view, add, edit, and deactivate [general ledger accounts](https://developers.pismo.io/pismo-docs/docs/cc-general-ledger-accounts).

#### New

[Notifications](https://developers.pismo.io/pismo-docs/docs/control-center-navigation#notifications) in Control Center now support announcements. This type of notification communicates application updates, new features, or similar changes.

#### New

When a Control Center request fails, the error is reported in a popup message. The message includes a Report log with technical details that users may copy to include when making a service request.

#### Docs

The role descriptions table in the [Access profiles and roles](https://developers.pismo.io/pismo-docs/docs/control-center-access-profiles-and-roles) guide for Control Center was simplified for clarity.

#### Docs

The [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/cc-manage-processing-codes-and-transaction-types) guide for Control Center was combined into one and updated.

</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/transactions/{merchantTransactionId}/split` (`post-split-request`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `POST /v1/transactions/{merchantTransactionId}/split/cancel` (`cancel-split-request`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `GET /v1/marketplaces/{marketplaceId}/split-requests` (`get-split-requests`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `GET /v1/marketplaces/{marketplaceId}/split-requests/{splitId}` (`get-split-details`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `GET /v1/marketplaces/{marketplaceId}/split-requests/{parentId}/totals` (`get-sale-split-request-totals`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/balance` (`get-merchant-balance`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--balance |
| `GET /accounts/v1/accounts/{accountId}` (`get-accounts-v1-accounts`) | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--accounts |
| `GET /v1/accounts/{accountId}/limits` (`get-v1-account-limit`) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `PATCH /v1/accounts/{accountId}/flex-controls/{flexControlId}` (`patch-v1-accounts-flex-control`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `PATCH /v1/customers/{customerId}/flex-controls/{flexControlId}` (`patch-v1-customers-flex-control`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--customer-flex-controls-part-01, KU-API-core-platform-flex-controls--customer-flex-controls-part-02 |
| `GET /v1/accounts/{accountId}/daily-balances` (`get-v1-account-balance`) | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--account-balances |
| `GET /v1/accounts/{accountId}/related-accounts-limits` (`get-v1-accounts-limits-related-accounts`) | `api-specs/Core_platform_-_Balances_and_limits.yaml` | no | KU-API-core-platform-balances-and-limits--related-accounts |
| `POST /v1/migrations/on-us-authorizations` (`PostOnUsAuthorizationsV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--on-us-authorization-migration |
| `POST /v1/migrations/disputes` (`PostDisputeV1`) | `api-specs/Migrations.yaml` | no | KU-API-migrations--dispute-migration |
| `POST /v1/transaction-flow` (`PostTransactionFlow`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId}` (`PatchTransactionFlow`) | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `POST /holidays-core/v2/holiday` (`post-v2-holiday`) | `api-specs/Platform_setup_-_Holidays.yaml` | **yes** | KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/scheduled-payments` (`corporate-v2-post-scheduled-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v2/divisions` (`post-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `GET /corporate/v2/divisions` (`list-division-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--divisions |
| `PUT /corporate/v1/bulk-payments/{bulkId}` (`corporate-put-bulk-file`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-payment-files |
| `POST /v1/features-by-account-status` (`postFeaturesByAccountStatus`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--features-by-account-status |
| `GET /v1/features-by-account-status` (`getFeaturesByAccountStatus`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--features-by-account-status |
| `PATCH /v1/features-by-account-status` (`patchFeaturesByAccountStatus`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--features-by-account-status |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals` (`getAccountAccrualsV3`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `GET /statements/v2/accounts/{accountId}/interest-accruals` (`GetAccountAccrualsV2`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--accruals |
| `POST /v1/bulletin` (`post-v1-bulletin`) | `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | no | KU-API-card-issuing-protection-bulletin--bulletin |
| `POST /v1/bulletin/setup` (`post-v1-bulletin-setup`) | `api-specs/Card_issuing_-_Protection_Bulletin.yaml` | no | KU-API-card-issuing-protection-bulletin--rules |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-v1-balances-config-1` | API; Balance configurations API; Create balance configuration; balance configuration | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/2-may-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/2-may-2025 | `83210e936ef3dff0…` | not stated |

## Related knowledge units

- `KU-API-banking-transaction-banking--bulk-payment-files` — API reference: Banking - Transaction banking — Bulk payment files
- `KU-API-banking-transaction-banking--divisions` — API reference: Banking - Transaction banking — Divisions
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-card-issuing-protection-bulletin--bulletin` — API reference: Card issuing - Protection Bulletin — Bulletin
- `KU-API-card-issuing-protection-bulletin--rules` — API reference: Card issuing - Protection Bulletin — Rules
- `KU-API-core-platform-accounts--accounts` — API reference: Core platform - Accounts — Accounts
- `KU-API-core-platform-balances-and-limits--account-balances` — API reference: Core platform - Balances and limits — Account balances
- `KU-API-core-platform-balances-and-limits--related-accounts` — API reference: Core platform - Balances and limits — Related accounts
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-01` — API reference: Core platform - Flex controls — Customer flex controls (part 1 of 2)
- `KU-API-core-platform-flex-controls--customer-flex-controls-part-02` — API reference: Core platform - Flex controls — Customer flex controls (part 2 of 2)
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-migrations--dispute-migration` — API reference: Migrations — Dispute migration
- `KU-API-migrations--on-us-authorization-migration` — API reference: Migrations — On-us authorization migration
- `KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat` — API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)
- `KU-API-revolving-credit-configurations--features-by-account-status` — API reference: Revolving credit - Configurations — Features by account status
- `KU-API-revolving-credit-statements--accruals` — API reference: Revolving credit - Statements — Accruals
- `KU-API-seller-management-transactions--balance` — API reference: Seller management - Transactions — Balance
- `KU-API-seller-management-transactions--split-requests` — API reference: Seller management - Transactions — Split requests
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
