---
ku_id: KU-CHG-8-august-2025
title: 'Changelog: 8 August 2025'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/8-august-2025.md
  sha256: 55f7fc342811e92ab67702cf8e42b867947194459343ff69838ae335414c1330
  url: https://developers.pismo.io/pismo-docs/changelog/8-august-2025
  role: changelog_post
  updated_at: ''
operations:
- CreateProgramBasedOnTemplate
- GetCurrentStatement
- GetStatementInfo
- advance-pix-out-execution
- cancel-network-authorizations
- card-token-operation
- getByStatementId
- patch-accounts-accountId-status-v2
- patch-corporate-v2-earmarks-earmarkid
- patch-v1-account-limit
- patch-v1-orgs
- post-accounts-accountId-close
- post-bulk-settlement
- post-corporate-v2-earmarks
- post-corporate-v2-earmarks-earmarkid-cancel
- post-create-cob
- post-merchant-transaction-cancel
- post-merchant-transaction-sale
- post-schedule-pix-payment
- post-v1-accounts-flex-controls
- post-v1-clicktopay-enroll_customer
- post-v1-clicktopay-get_data
- post-v2-card
- postFeaturesByAccountStatus
- put-back-business-toggle
- saveAccountTransactionInterest
- statementDueDate
related_kus:
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--bulk-settlement
- KU-API-banking-transaction-banking--earmarking-external-accounts
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-card-issuing-authorization--authorizations
- KU-API-card-issuing-cards--cards
- KU-API-card-issuing-tokenization--card-lifecycle
- KU-API-card-issuing-tokenization--visa-click-to-pay
- KU-API-core-platform-flex-controls--account-flex-controls
- KU-API-core-platform-ledger--account-limits
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-instant-payments-qr-code--qr-code
- KU-API-platform-setup-organizations--orgs
- KU-API-platform-setup-programs--programs-part-01
- KU-API-platform-setup-programs--programs-part-02
- KU-API-revolving-credit-configurations--features-by-account-status
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--due-date
- KU-API-revolving-credit-statements--statement
- KU-API-seller-management-transactions--merchant-transactions
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 8 August 2025
coverage_window: 7 July and 8 August 2025
---

# Changelog: 8 August 2025

**KU ID:** `KU-CHG-8-august-2025` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **8 August 2025** (changes between 7 July and 8 August 2025). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated"; "Deprecated".

## Topics covered

Click to Pay; Balance configurations; Client webhooks; Flex controls; Ledger; Organizations; Payments; Programs; Security; Setup; Instant payments; Transaction banking; Authorization; Card network integration; Card tokenization; Cards; Embossing; Statements; Merchants; Transactions; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/8-august-2025

<!-- source:begin path=changelog/8-august-2025.md part=0-end -->

# 8 August 2025

Changes between 7 July and 8 August 2025

<div class="customTab"></div>

<summary class="tabContent" id="New features">

### Click to Pay

#### New

Pismo now supports Click to Pay, a new secure, streamlined online checkout solution using tokenization. Most major card networks now have a Click to Pay service. Initially, Pismo supports Visa’s Click to Pay service. Support for Mastercard’s service is now in development. More card networks' Click to Pay services will be supported in the future. There is a new [Click to Pay](https://developers.pismo.io/pismo-docs/docs/click-to-pay) guide, a new [Visa Click to Pay](https://developers.pismo.io/pismo-docs/reference/post-v1-clicktopay-enroll_customer) API, and a new [Click to Pay](https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1) event.

This feature is in beta, giving you early access to explore its capabilities and share feedback. Note that the functionality and API contracts might change before the production release. For more information or to join the beta program, contact your Pismo representative.

</summary>

<summary class="tabContent" id="Core platform">

### Balance configurations

#### Docs

References to [balance configurations](https://developers.pismo.io/pismo-docs/docs/balances-configurations-overview) were updated throughout the guide and API reference documentation.

### Client webhooks

#### Updated

The [Zero balance validations webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#zero-balance-validations-webhook) was updated with the following:

* Three new request fields were added to the Request fields list and the Sample request: `match_address`, `match_postal_code`, and `no_address_data`. These three field values override Pismo’s matching results when informed, so they have been marked as not required in the Response fields list and removed from the Sample response.
* Pismo now validates the account owner name and sends the result in the Zero Balance request payload. The client can return the same values/result received in the request or they can return different values/result based on their business case. The response from the client overrides Pismo's result. As a result, the following fields were also added to the Request fields list and the Sample request:
  * `account_owner_data`
    * `account_owner_type`
    * `account_owner_name_first`
    * `account_owner_name_middle`
    * `account_owner_name_last`
    * `additional_service_result_data`
      * `account_name_request_result`
      * `full_name_account_match_decision`
      * `last_name_account_match_decision`
      * `middle_name_account_match_decision`
      * `first_name_account_match_decision`
  * `additional_service_request_data`
    * `account_name_request`
* The `additional_service_request_data` field and the `account_name_request `field have been removed from the Response field and the Sample response.

#### Updated

The `referral` field has been removed and is no longer required in the anti-fraud  [Full balance webhook](https://developers.pismo.io/pismo-docs/docs/client-webhooks#full-balance-anti-fraud--webhook) response. The example response in the [Anti-fraud integration](https://developers.pismo.io/pismo-docs/docs/anti-fraud-integration) guide has also been updated to reflect this change.

### Flex controls

#### Docs

The `country_code` and `acquirer_country_code` field descriptions in the [flex controls](https://developers.pismo.io/pismo-docs/reference/post-v1-accounts-flex-controls) endpoint documentation were improved to provide additional explanations.

### Ledger

#### Updated

In the [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint, all amount limit field descriptions were updated to state that the ledger stores and reports the amount using the same number of decimal places as supplied in the request payload. Previously, the documentation incorrectly stated that the number of decimal places was two.

#### Updated

The [Update account limits](https://developers.pismo.io/pismo-docs/reference/patch-v1-account-limit) endpoint now includes the following new validations.

* The `max_credit_limit` field now includes validation that this value must not be less than the `total_credit_limit` or the program’s minimum credit limit parameter, and must not exceed the program’s maximum credit limit parameter.
* The `total_installment_credit_limit` field now includes validation that this value must not exceed the program’s maximum credit limit parameter.

### Organizations

#### Updated

The [Update Org](https://developers.pismo.io/pismo-docs/reference/patch-v1-orgs) endpoint now includes two new fields: `document_number` and `legal_proxy_name`.

### Payments

#### Fixed

In the [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments-1) endpoint, the `currency` field name was corrected to be `currency_code`.

### Programs

#### New

A new card-issuing [program type](https://developers.pismo.io/pismo-docs/reference/createprogrambasedontemplate) for prepaid voucher meal/food cards has been added: `VOUCHER`.

#### Docs

The Program types guide now includes a new [Sample credit program JSON](https://developers.pismo.io/pismo-docs/docs/program-types#sample-credit-program) section. Internally, the Pismo platform keeps a JSON file for each program. This sample shows what a typical credit program might look like, with the processing codes, transaction types, transaction categories, network acceptances, and program parameters given to a credit program upon creation.

### Security

#### Docs

The [Generate your JWT](https://developers.pismo.io/pismo-docs/docs/authentication-with-openid#generate-your-jwt) instructions in the Authentication with OpenID Connect guide were updated to clarify that you can use any trusted helper library that is compatible with your stack when generating your JSON web token.

### Setup

#### New

The new program parameter **Revolving statement summary at cycle closing**  is now available and is listed in the [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide.

#### Docs

The [Program parameters](https://developers.pismo.io/pismo-docs/docs/program-parameters-reference-table) guide was updated in the following ways.

* There was a duplicated display name: “Interest projection reversal “. The first instance of this name was changed to “Accruals reversal strategy”, which is the correct name for that parameter. Since the table is in alphabetical order, the row for this parameter was moved up.
* The duplicate row for “Maximum credit limit” was removed.

</summary>

<summary class="tabContent" id="Core banking">

### Instant payments

#### New

There is a new Pix instant payments API endpoint - [Execute scheduled Pix-out transfer in advance](https://developers.pismo.io/pismo-docs/reference/advance-pix-out-execution). The endpoint performs a scheduled Pix-out transfer execution in advance. A scheduled transfer can have many executions if, for example, it is recurring.

#### Updated

A new required header field, `Idempotency-Key`, was added to the Instant payments - Pix payments > [Scheduled transfers V2](https://developers.pismo.io/pismo-docs/reference/post-schedule-pix-payment) endpoint.

#### Updated

Two new objects were added to the Instant payments - QR Code > [Create dynamic COBV QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-cob) endpoint:  `withdraw` and `change`. These objects can be used to make a cash withdrawal or cashback transaction.

#### Docs

The new [Pix and QR Codes](https://developers.pismo.io/pismo-docs/docs/pix-and-qr-codes) guide is now available. A Quick Response (QR) Code is a type of barcode that digital devices can scan and read. Pix uses QR Codes—specifically the Brazilian BR Code format adhering to Europay Mastercard Visa (EMV) standards—to embed payment details such as recipient account, Pix key, and in the case of dynamic codes, transaction amount and metadata. QR Codes can be used for immediate payments as well as scheduled and automatically-recurring payments.

### Transaction banking

#### New

A new endpoint [Get AES key](https://developers.pismo.io/pismo-docs/reference/corporate-bulk-payments-get-aes-keys) is now available to enhance communication security using AES keys. This endpoint encrypts the response payload using a public key you have previously uploaded. Before this release, only files could be encrypted, not the response messages

#### Updated

The following error messages were added to the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks), [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid), and [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel) endpoints:

* `WEAM0039: Invalid business date for current business day cycle` - This error occurs when clients submit a business date that is excessively old. There is a restriction on how far back a financial operation can be backdated.
* `WEAM0041: Business date cannot be earlier than earmark creation date` - This error occurs when clients try to update or cancel an earmark using a business date earlier than its creation date.
* `WEAM0042: Future dated earmark operations are not allowed` - This error occurs when clients use a future business date. Unlike payments, earmark operations don’t support future-dated transactions.
* `WEAM0043: Cannot post transaction on holidays` - This error occurs when transactions are posted on holidays.
* `WEAM0044: Cannot post transaction on weekends` - This error occurs when transactions are posted on weekends.

#### Updated

The [Create operation block](https://developers.pismo.io/pismo-docs/reference/corporate-post-v1-operation-blocks) endpoint now includes a missing field `created_at` and an example to the 201 response payload.

#### Updated

In the [Close transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-accounts-accountid-close) and [Update transaction banking account status](https://developers.pismo.io/pismo-docs/reference/patch-accounts-accountid-status-v2) endpoints, the following error message was added to notify clients who attempt to update an account that is already in its final status such as CLOSED:

* `WCAC0035: Account is currently in the final status`

#### Updated

The following validation errors were added to the [Request bulk settlement](https://developers.pismo.io/pismo-docs/reference/post-bulk-settlement) endpoint:

* `WSTM0010: Bulk settlement for the current date is allowed only after {hour}:{minute}, according to the division’s time zone`
* `WSTM0011: Administrative division is misconfigured`

#### Updated

The error `WPMT0045: Back business dating is disabled ` was introduced to inform clients that backdated earmark requests are not allowed when [Past business date toggle](https://developers.pismo.io/pismo-docs/reference/put-back-business-toggle) is disabled. This error was added to the following endpoints:

* [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks)
* [Update earmark](https://developers.pismo.io/pismo-docs/reference/patch-corporate-v2-earmarks-earmarkid)
* [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel)

</summary>

<summary class="tabContent" id="Card issuing">

### Authorization

#### Docs

The description of the [Cancel authorization](https://developers.pismo.io/pismo-docs/reference/cancel-network-authorizations) endpoint now points to its generated event, Network authorization received.

### Card network integration

#### Updated

Due to a new release implemented by the card networks, the following validation codes were updated for [CNC - Account cancelled](https://developers.pismo.io/pismo-docs/docs/validation-codes-for-authorization-events#authorization-validations).

|                  | Old code | New code |
| :--------------- | :------- | :------- |
| VDC (Visa)       | 62       | 46       |
| MDC (Mastercard) | 57       | 62       |
| EDC (ELO)        | 57       | 46       |

### Card tokenization

#### New

A new tokenization endpoint is now available - [Card token operation](https://developers.pismo.io/pismo-docs/reference/card-token-operation). This endpoint performs a token operation for a specific card.

#### New

The Card issuing - Tokenization > Visa Click to Pay > [Get Visa CTP customer cards status](https://developers.pismo.io/pismo-docs/reference/post-v1-clicktopay-get_data) endpoint now takes the Owner business ID (identifies the issuing entity creating or managing enrollment in Click to Pay) as a required header (`x-owner-bid`) parameter and not in the path. The Visa Click to Pay service API is currently in `beta`.

### Cards

#### Updated

Pismo cards now support 6-digit Primary Identification Numbers (PINs) in addition to 4-digit PINs (or passwords). In the [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card) endpoint, there is now a new `pin_length` field, which you can set to 4 or 6.

#### Updated

In the [Create card](https://developers.pismo.io/pismo-docs/reference/post-v2-card) endpoint, there is now a new `generate_pvv` boolean field (should a PIN Verification Value (PVV) be generated and inserted into the card tracks during embossing?) This is for physical cards. This is necessary for Visa's PVS service. Default is `false`.

### Embossing

#### Docs

New sections about [Embossing layouts](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing#embossing-layouts) and [Embossing upload times](https://developers.pismo.io/pismo-docs/docs/physical-card-embossing#embossing-file-upload-times) were added to the Physical card embossing guide.

### Statements

#### Updated

The body parameter `cancel_at_start_date` was added to the [Configure account transaction category rates](https://developers.pismo.io/pismo-docs/reference/saveaccounttransactioninterest) endpoint.

#### Updated

The header field `x-account-id` was removed from the [Update statements calendar](https://developers.pismo.io/pismo-docs/reference/statementduedate) endpoint. It’s not needed, since the account ID is retrieved from the access token. Also, a note was added to the endpoint description explaining that the endpoint requires an account token.

#### Updated

The new `create-accruals` field was added to the [Configure features by account status](https://developers.pismo.io/pismo-docs/reference/postfeaturesbyaccountstatus) endpoint.

#### Updated

Two new fields, `final_account_status` and `excluded_steps` were added to the body parameters of the [Close delinquent account](https://developers.pismo.io/pismo-docs/reference/delinquent-ccount-closure-post) endpoint.

#### Updated

The \[optional] tag was removed from step 11 in [Add a floating interest rate plan](https://developers.pismo.io/pismo-docs/docs/add-interest-plans#add-a-floating-interest-rate-plan). This step is not optional if the benchmark index is provided (step 10). Since step 10 is required, this means that step 11 is also required.

#### Updated

In the table in the [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-program-parameters) guide, the description for the PAYMENTS\_TTS parameter was corrected. The line “By default, the platform considers the following transaction types as payments: 282, 320, 342, 701, 711, 721, 2224” was changed to “By default, the platform considers the following transaction types as payments: 201, 244, 255, 276, 282, 320, 342, 701, 711, 721, 2224”.

#### Docs

The table in the [Multivalue program parameters](https://developers.pismo.io/pismo-docs/docs/multivalue-parameters) guide was updated and some information was added to the opening text.

#### Docs

A link to the [Understanding statements](https://developers.pismo.io/pismo-docs/docs/understanding-statements) guide was added in the descriptions of the following endpoints:

* [Get current statement](https://developers.pismo.io/pismo-docs/reference/getcurrentstatement)
* [Get statement](https://developers.pismo.io/pismo-docs/reference/getstatementinfo)
* [List statements v3](https://developers.pismo.io/pismo-docs/reference/getbystatementid)

#### Docs

[How to manually close a delinquent account](https://developers.pismo.io/pismo-docs/docs/credit-liquidation#how-to-manually-close-a-delinquent-account) instructions were updated to remove irrelevant information and specify which multivalue program parameter to use.

</summary>

<summary class="tabContent" id="Seller management">

### Merchants

#### Updated

The [Create merchant transaction](https://developers.pismo.io/pismo-docs/reference/createmerchantusingmerchantid)  and [Create reversal transaction](https://developers.pismo.io/pismo-docs/reference/createreversaltransaction) endpoints now include  `processing_code` and `currency_code` fields in the response body.

#### Updated

In the [Create merchant transaction](https://developers.pismo.io/pismo-docs/reference/createmerchantusingmerchantid) endpoint, you can now send a `currency_code` within the `authorization ` object and a `status` within the  `acceptance` object.

#### Deprecated

The following two endpoints have now passed the deprecation date and are no longer available:

* GET /v1/merchants/scheduler
* POST /v1/creditors

#### Deprecated

The merchant terminals endpoints, events, and related documentation were removed as they were not being used.

### Transactions

#### New

The following new transaction endpoints for split transactions are now available.

* [Create merchant transaction](https://developers.pismo.io/pismo-docs/reference/post-merchant-transaction-sale)
* [Cancel merchant transaction](https://developers.pismo.io/pismo-docs/reference/post-merchant-transaction-cancel)

</summary>

<summary class="tabContent" id="Resources">

### Control Center

#### Docs

The [Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) documentation was updated to reflect the redesigned menu structure, making it easier to find what you need. The Get Started pages have also been refined to emphasize key features, guide you through navigation, and simplify access, login, and security topics.

</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /v1/clicktopay/visa/enroll/customer` (`post-v1-clicktopay-enroll_customer`) | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `POST /v1/accounts/{accountId}/flex-controls` (`post-v1-accounts-flex-controls`) | `api-specs/Core_platform_-_Flex_controls.yaml` | no | KU-API-core-platform-flex-controls--account-flex-controls |
| `PATCH /v1/accounts/{accountId}/limits` (`patch-v1-account-limit`) | `api-specs/Core_platform_-_Ledger.yaml` | no | KU-API-core-platform-ledger--account-limits |
| `PATCH /orgs-core/v1/orgs` (`patch-v1-orgs`) | `api-specs/Platform_setup_-_Organizations.yaml` | no | KU-API-platform-setup-organizations--orgs |
| `POST /programs/v1/programs/template` (`CreateProgramBasedOnTemplate`) | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--programs-part-01, KU-API-platform-setup-programs--programs-part-02 |
| `POST /pix/v2/pix/out/scheduler/{scheduler_id}/execution/{execution_id}/advance` (`advance-pix-out-execution`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `POST /pix/v2/pix/out/scheduler` (`post-schedule-pix-payment`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `POST /v1/pix/qrcode/cob` (`post-create-cob`) | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--qr-code |
| `POST /corporate/v2/earmarks` (`post-corporate-v2-earmarks`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `PATCH /corporate/v2/earmarks/{earmarkId}` (`patch-corporate-v2-earmarks-earmarkid`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` (`post-corporate-v2-earmarks-earmarkid-cancel`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--earmarking-external-accounts |
| `POST /corporate/v1/corporate-accounts/{externalAccountId}/close` (`post-accounts-accountId-close`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `PATCH /corporate/v2/corporate-accounts/{externalAccountId}/status` (`patch-accounts-accountId-status-v2`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v1/bulk-settlement` (`post-bulk-settlement`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--bulk-settlement |
| `PUT /corporate/v1/feature/back-business/toggle` (`put-back-business-toggle`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /direct-network-transactions/v1/cancellation` (`cancel-network-authorizations`) | `api-specs/Card_issuing_-_Authorization.yaml` | no | KU-API-card-issuing-authorization--authorizations |
| `POST /v1/cards/{card_id}` (`card-token-operation`) | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--card-lifecycle |
| `GET /v1/clicktopay/visa/data` (`post-v1-clicktopay-get_data`) | `api-specs/Card_issuing_-_Tokenization.yaml` | no | KU-API-card-issuing-tokenization--visa-click-to-pay |
| `POST /wallet/v2/cards` (`post-v2-card`) | `api-specs/Card_issuing_-_Cards.yaml` | no | KU-API-card-issuing-cards--cards |
| `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` (`saveAccountTransactionInterest`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `PATCH /statements-v2/v2/due-date` (`statementDueDate`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--due-date |
| `POST /v1/features-by-account-status` (`postFeaturesByAccountStatus`) | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--features-by-account-status |
| `GET /statements/v1/accounts/{accountId}/next` (`GetCurrentStatement`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `GET /statements/v1/accounts/{accountId}/statements/{statementId}` (`GetStatementInfo`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `GET /statements-v2/v3/accounts/{accountId}/statements` (`getByStatementId`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` (`post-merchant-transaction-sale`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--merchant-transactions |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel` (`post-merchant-transaction-cancel`) | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--merchant-transactions |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `post-payments-1` | Create cash-in or cash-out | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `corporate-bulk-payments-get-aes-keys` | Get AES key | not found in the current OpenAPI specifications. Name-based inference: link text "Get AES key" equals the endpoint name "Get AES key" in the removed-endpoints list (row Banking / Transaction banking, date removed `2/20/2026`). This is a match on the endpoint name, not on an identifier. |
| `corporate-post-v1-operation-blocks` | Create operation block | not found in the current OpenAPI specifications. Name-based inference: link text "Create operation block" equals the endpoint name "Create operation block" in the removed-endpoints list (row Banking / Transaction banking, date removed `2/20/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`corporate-post-v2-operation-blocks` (POST /corporate/v2/operations-blocks)); no source states that it replaces the removed endpoint. |
| `delinquent-ccount-closure-post` | Close delinquent account | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `createmerchantusingmerchantid` | Create merchant transaction; Create merchant transactions | not found in the current OpenAPI specifications. Name-based inference: link text "Create merchant transaction" equals the endpoint name "Create merchant transaction" in the removed-endpoints list (row Seller Management / Merchant transactions, date removed `7/24/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`post-merchant-transaction-sale` (POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions)); no source states that it replaces the removed endpoint. |
| `createreversaltransaction` | Create a reversal transaction; Create reversal transaction | not found in the current OpenAPI specifications. Name-based inference: link text "Create reversal transaction" equals the endpoint name "Create reversal transaction" in the removed-endpoints list (row Seller Management / Merchant transactions, date removed `7/24/2026`). This is a match on the endpoint name, not on an identifier. |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/8-august-2025.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/8-august-2025 | `55f7fc342811e92a…` | not stated |

## Related knowledge units

- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--bulk-settlement` — API reference: Banking - Transaction banking — Bulk settlement
- `KU-API-banking-transaction-banking--earmarking-external-accounts` — API reference: Banking - Transaction banking — Earmarking (external accounts)
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-card-issuing-authorization--authorizations` — API reference: Card issuing - Authorization — Authorizations
- `KU-API-card-issuing-cards--cards` — API reference: Card issuing - Cards — Cards
- `KU-API-card-issuing-tokenization--card-lifecycle` — API reference: Card issuing - Tokenization — Card lifecycle
- `KU-API-card-issuing-tokenization--visa-click-to-pay` — API reference: Card issuing - Tokenization — Visa Click to Pay
- `KU-API-core-platform-flex-controls--account-flex-controls` — API reference: Core platform - Flex controls — Account flex controls
- `KU-API-core-platform-ledger--account-limits` — API reference: Core platform - Ledger — Account limits
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-instant-payments-qr-code--qr-code` — API reference: Instant payments - QR Code — QR Code
- `KU-API-platform-setup-organizations--orgs` — API reference: Platform setup - Organizations — Orgs
- `KU-API-platform-setup-programs--programs-part-01` — API reference: Platform setup - Programs — Programs (part 1 of 2)
- `KU-API-platform-setup-programs--programs-part-02` — API reference: Platform setup - Programs — Programs (part 2 of 2)
- `KU-API-revolving-credit-configurations--features-by-account-status` — API reference: Revolving credit - Configurations — Features by account status
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--due-date` — API reference: Revolving credit - Statements — Due date
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-API-seller-management-transactions--merchant-transactions` — API reference: Seller management - Transactions — Merchant transactions
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
