---
ku_id: KU-CHG-2-july-2026
title: 'Changelog: 2 July 2026'
category: changelog_history
ku_type: changelog_history
lifecycle: historical
sources:
- path: changelog/2-july-2026.md
  sha256: 1a648c65786b1bccb0f52f4123d1f3c061a178da733450d615acc230d346a9ca
  url: https://developers.pismo.io/pismo-docs/changelog/2-july-2026
  role: changelog_post
  updated_at: ''
operations:
- corporate-v2-post-payments
- createLoanAdjustmentV2
- createStatementAmountDue
- delete-integrated-payments-api-v1-bankslips-issue
- delete-integrated-payments-api-v1-ebill-registration-accounts-accountId
- enroll-card-enrollment
- get-integrated-payments-api-v1-bankslips-issue-retrieve
- get-integrated-payments-api-v1-bankslips-receipts
- get-integrated-payments-api-v1-ebill-registration-accounts-accountId
- get-integrated-payments-api-v1-transfers
- get-v1-filter-template-by-id
- get-v1-filter-templates
- get-v1-interest-account
- get-v1-interest-plan
- get-v1-interest-plans
- getLoanProductV2
- getLoanProductsV2
- interest-bearing-v1-deposit-account-open
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-attach-program
- interest-bearing-v1-deposit-update-account-attachment
- interest-bearing-v1-deposit-update-program-attachment
- interest-bearing-v1-get-account-attachment
- interest-bearing-v1-get-program-attachment
- patch-v1-interest-plan
- post-account
- post-accounts-accountId-close
- post-accounts-accountId-force-close
- post-bacs-client-return
- post-create-recurrence-cob
- post-integrated-payments-api-v1-bankslips-cashout
- post-integrated-payments-api-v1-bankslips-issue
- post-integrated-payments-api-v1-bankslips-pay
- post-integrated-payments-api-v1-bankslips-validate
- post-integrated-payments-api-v1-ebill-registration-accounts-accountId
- post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil
- post-payments
- post-pix-out-transfer
- post-recurrence-automatic
- post-return-fps
- post-schedule-pix-payment
- post-transfers
- post-v1-benchmark-rate
- post-v1-filter-templates
- post-v1-interest-plan
- put-v1-filter-template
- put-v1-interest-account
- update-recurrence-automatic
related_kus:
- KU-API-banking-bank-accounts--bank-accounts-part-01
- KU-API-banking-bank-accounts--bank-accounts-part-02
- KU-API-banking-integrated-payments--bank-slip
- KU-API-banking-integrated-payments--bank-slip-issuance
- KU-API-banking-integrated-payments--ebill-registration
- KU-API-banking-integrated-payments--transfer
- KU-API-banking-interest-bearing-accounts--account-attachment
- KU-API-banking-interest-bearing-accounts--deposit-account-open
- KU-API-banking-interest-bearing-accounts--program-attachment
- KU-API-banking-interest-engine--account-interest
- KU-API-banking-interest-engine--benchmark-rate
- KU-API-banking-interest-engine--interest-engine
- KU-API-banking-transaction-banking--accounts
- KU-API-banking-transaction-banking--payments-part-01
- KU-API-banking-transaction-banking--payments-part-02
- KU-API-banking-transaction-banking--payments-part-03
- KU-API-card-issuing-visa-flexible-credentials--enrollment
- KU-API-core-platform-balance-config-beta--filter-templates
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-payment-methods--payment-methods-part-02
- KU-API-core-platform-payment-methods--payment-methods-part-03
- KU-API-instant-payments-automatic-pix--automatic-pix
- KU-API-instant-payments-pix-payments--pix-part-01
- KU-API-instant-payments-pix-payments--pix-part-02
- KU-API-instant-payments-pix-payments--scheduled-transfers-v2
- KU-API-instant-payments-qr-code--recurring-payment
- KU-API-instant-payments-uk-fps-beta--faster-payments
- KU-API-lending--loan-products
- KU-API-lending--loans
- KU-API-payment-rails-bacs-payments--bacs-direct-credit
- KU-API-revolving-credit-statements--statement-minimum-amount-due
- KU-LIFE-api-endpoints-removed
- KU-LIFE-marketplace-endpoint-removal
title_date: 2 July 2026
coverage_window: 5 June and 2 July 2026
---

# Changelog: 2 July 2026

**KU ID:** `KU-CHG-2-july-2026` · **Category:** Changelog history · **Type:** historical record

> **HISTORICAL RECORD.** This post records changes published by Pismo on **2 July 2026** (changes between 5 June and 2 July 2026). It describes what changed at that time. It is not, by itself, a description of current behaviour: check the current API-reference and guide KUs, and the removed-endpoints register, before relying on any statement here.

## Purpose and scope

Dated record of platform changes. The title date is the publication date of record (the RSS `pubDate` is not used). The post has no `updatedAt`.

Sections of this post about deprecations, removals or decommissioning: "Deprecated"; "Deprecated"; "Deprecated"; "Deprecated"; "Deprecated"; "Deprecated"; "Deprecated".

## Topics covered

General; Core banking; Card issuing - Statements; Control Center; General; Accounts; Client webhooks; Payments; Setup; Events; Reports; Banking operations; Integrated payments; Instant payments; Payment rails; Transaction banking; Card network integration; Statements; Visa Flexible Credentials; Lending; Control Center

## Change record (source content, verbatim)

Source URL: https://developers.pismo.io/pismo-docs/changelog/2-july-2026

<!-- source:begin path=changelog/2-july-2026.md part=0-end -->

# 2 July 2026

Changes between 5 June and 2 July 2026

<div class="customTab" />

<summary class="tabContent" id="New features">
  ### General

  #### Docs

  The **Get started** category was restructured to make it easier to explore the Pismo platform and products and start building. As part of the restructure, the following changes.

  * Introduced a [Start building](https://developers.pismo.io/pismo-docs/docs/start-building) category to centralize onboarding and get started guides. You can still access these guides within their features; for example, [Get started with card issuing](https://developers.pismo.io/pismo-docs/docs/get-started-building-card-issuing) is both part of the Start building category, and the Card issuing category.
  * Created a new [Learn about the Pismo platform](https://developers.pismo.io/pismo-docs/docs/pismo-platform-overview) category that helps customers understand the main building blocks of the platform, including **Main solutions**, **Core objects**, **Program types**, **Environments**, and **Data events**.
  * Renamed the **Pismo platform onboarding** to **Onboarding for new customers**.
  * Moved **Get started with Ask AI** under **Get started with the Pismo Developers Portal**.
  * Moved the following guides and sections to the **Resources** category:
    * [Support](https://developers.pismo.io/pismo-docs/docs/support) section
    * [API life cycle and deprecation strategy](https://developers.pismo.io/pismo-docs/docs/api-deprecation-strategy) guide
    * [Pismo changelog](https://developers.pismo.io/pismo-docs/docs/pismo-changelog) guide
  * The title of the [Rate limiting on the Pismo platform](https://developers.pismo.io/pismo-docs/docs/rate-limiting) guide was changed from **Rate limiting** and this guide was moved from the **Guides** area to the **APIs**, as part of the **Get started** category..

  ### Core banking

  #### New

  The new endpoint [Force close transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-accounts-accountid-force-close) allows you to initiate an asynchronous force‑closure of a transaction banking account by placing a closure instruction in the processing queue. This ensures all business rules, such as balance checks, earmark review, and status validation, are applied during asynchronous processing rather than at request time.

  #### Docs

  The new [Divisions](https://developers.pismo.io/pismo-docs/docs/divisions) guide is now available. It covers how divisions work, how to model them, and recommended best practices.

  ### Card issuing - Statements

  #### Docs

  The new [Creating payment agreements with custom transactions](https://developers.pismo.io/pismo-docs/docs/creating-payment-agreements-with-custom-transactions) guide is now available. This guide describes how you can use custom transactions to create a transaction flow for a payment agreement.

  ### Control Center

  #### New

  The [Loans](https://developers.pismo.io/pismo-docs/docs/manage-loans-in-control-center) feature was added to Control Center. This new feature adds support for viewing and managing customer loans, including:

  * Viewing the list of loans and individual loan details
  * Monitoring loan repayment progress
  * Making and tracking disbursements
  * Adjusting repayment installments
</summary>

<summary class="tabContent" id="Core platform">
  ### General

  #### Deprecated

  The CRM API and all of its endpoints (/crm/\*) was decommissioned and removed from the Developers Portal and added to the [API endpoints removed](https://developers.pismo.io/pismo-docs/reference/api-endpoints-removed) list.

  ### Accounts

  #### Deprecated

  The following decommissioned endpoints were removed from the Developers Portal and added to the [API endpoints removed](https://developers.pismo.io/pismo-docs/reference/api-endpoints-removed) list.

  * `GET /v2/accounts/:accountld/statements`
  * `GET /v1/accounts/:accountld/statements`
  * `POST /v2/customers/document-number`
  * `GET /v1/customers/:customerId/authorizations`
  * `PUT /v1/accounts/:accountld/duedate`
  * `GET /v1/accounts/:accountld/authorizations`

  ### Client webhooks

  #### Updated

  There is a new URL to access the Pismo’s public keys for Webhook requests: "`https://sandbox.pismolabs.io/v1/certs`". The old URL, "`https://sandbox.pismolabs.io/robot/v1/metadata/x509/pismolabs@dev-gke-7a65.iam.gserviceaccount.com`", will continue to work for existing clients but it will be phased out. All clients are encouraged to use the new URL. We will communicate in advance via a Pismo Bulletin when the old URL will be fully deprecated. This change is reflected in the Anti-fraud code sample (Go) section of the [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks) guide.

  #### Docs

  The following changes were made to the Zero balance validations webhook fields in the [Client webhooks](https://developers.pismo.io/pismo-docs/docs/client-webhooks) guide.

  * The following request fields were rewritten for clarity and usability: `processing_code`, `transaction_type`, and `transaction_timestamp`.
  * The `amount_transaction` field was updated to correctly indicate it is not a required field.

  ### Payments

  #### Updated

  The `beneficiary_id` field was added in the request body of the following endpoints.

  * [Create cash-in or cash-out](https://developers.pismo.io/pismo-docs/reference/post-payments)
  * [Create transfer](https://developers.pismo.io/pismo-docs/reference/post-transfers) in the `to` object

  ### Setup

  #### Updated

  Filter templates are now supported in balance configurations. The following new endpoints are available.

  * [Create filter template](https://developers.pismo.io/pismo-docs/reference/post-v1-filter-templates)
  * [List filter templates](https://developers.pismo.io/pismo-docs/reference/get-v1-filter-templates)
  * [Get filter template](https://developers.pismo.io/pismo-docs/reference/get-v1-filter-template-by-id)
  * [Update filter template](https://developers.pismo.io/pismo-docs/reference/put-v1-filter-template)

  The new `filter_template_id` field is available in the following events.

  * [Balance configuration created](https://developers.pismo.io/events/docs/balances-config-created-1)
  * [Balance configuration updated](https://developers.pismo.io/events/docs/balances-config-updated-1)
</summary>

<summary class="tabContent" id="Data and reporting">
  ### Events

  #### New

  The following events are generated when [Update deposit account attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment) and [Update deposit program attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-program-attachment) are called.

  * [Account attachment updated](https://developers.pismo.io/events/docs/deposit-product-account-attachment-updated-1)
  * [Program attachment updated](https://developers.pismo.io/events/docs/deposit-product-program-attachment-updated-1)

  #### Updated

  In the [Token migration completed](https://developers.pismo.io/events/docs/migration-token-outgoing-1) event, a third result, `ACCEPTED`, can be reported from the event generated when a card token migration finishes.

  #### Docs

  The [AWS SNS event integration tutorial](https://developers.pismo.io/pismo-docs/docs/aws-event-tutorial) was updated in the following ways: added a Service Desk ticket template, required AWS configuration fields, routing instructions, and a streamlined quick-guide structure to simplify setup.

  #### Deprecated

  The unused **Pre-authorization captured** event was removed.

  ### Reports

  #### Deprecated

  The deprecated **Account limits report** v1 was decommissioned and removed from the Developers Portal. It was replaced by the [Account limits report](https://developers.pismo.io/pismo-docs/docs/account-limits-report-files-v2) v2.
</summary>

<summary class="tabContent" id="Core banking">
  ### Banking operations

  #### New

  The new [Open deposit account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-account-open) endpoint allows you to create or locate a transaction banking account and attach a validated deposit product in a single request.

  #### New

  The following new interest-bearing endpoints are now available in beta release.

  * [Update deposit account attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-account-attachment)
  * [Update deposit program attachment overrides](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-update-program-attachment)

  #### Updated

  In the [Register Brazilian bank account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil) endpoint, the banking scheme now allows alphanumeric characters, previously it only supported numerics.

  #### Updated

  The field `effective_date` was introduced to indicate the date when the deposit product account attachment becomes valid. This field was added to the following endpoints.

  * In the 200 response payload of [Get account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-account-attachment)
  * In the body parameter section of [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account)

  In addition, another field `attached_at` was also added to these two endpoints to indicate when the product attachment API was last called.

  #### Updated

  The following endpoints were marked as \[beta].

  * [Get account attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-account-attachment)
  * [Attach deposit to account](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-account)
  * [Get program attachment](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-get-program-attachment)
  * [Attach deposit product to program](https://developers.pismo.io/pismo-docs/reference/interest-bearing-v1-deposit-attach-program)

  #### Updated

  The `fixed_interest_rate` field was added in the following endpoints.

  * [Get account interest](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account) - in response
  * [Update account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account) - in request and response
  * [Configure benchmark rate](https://developers.pismo.io/pismo-docs/reference/post-v1-benchmark-rate) - in response
  * [Create interest plan](https://developers.pismo.io/pismo-docs/reference/post-v1-interest-plan) - in request
  * [List Org interest plans](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plans) - in response
  * [Get interest plan](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-plan) - in response
  * [Create interest plan version](https://developers.pismo.io/pismo-docs/reference/patch-v1-interest-plan) - in request

  #### Docs

  Details were added to the error response documentation for all the endpoints under [Banking - Interest engine](https://developers.pismo.io/pismo-docs/reference/get-v1-interest-account), such as 400 Bad request, 401 Unauthorized, and so on.

  #### Docs

  In the [Update account interest](https://developers.pismo.io/pismo-docs/reference/put-v1-interest-account) endpoint, detailed instructions were added in the request body that certain rules apply when you choose either of the interest types: benchmark-indexed rate or fixed rate.

  #### Deprecated

  The following endpoints are now deprecated and scheduled to be removed.

  * Create maturity instruction override `POST /interest-bearing/v1/create-maturity-instruction-override`
  * Update maturity instruction override `PATCH /savings-products/v1/create-maturity-instruction-override`
  * Get maturity instruction override `GET /savings-products/v1/create-maturity-instruction-override` 
  * Delete maturity instruction override `DELETE /interest-bearing/v1/create-maturity-instruction-override` 

  ### Integrated payments

  #### Updated

  New error messages were introduced for the following endpoints to improve clarity and help diagnose issues more easily.

  In [Issue bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-issue):

  400:

  * `EIP0013: Accounts - API returned 4xx error`
  * `EIP0077: Address not found for this Account`

  403 :

  * `EIP0005: Missing required header: 'x-tenant'`
  * `EIP0006: Invalid account id header: 'x-account-id'`
  * `EIP0009: Missing required header: 'x-idempotency-key'`
  * `EIP0029: Account blocked or cancelled`

  409 :

  * `EIP0042: client request id already exists`
  * `EIP0065: BankingGatewayAPI - API returned 409 provider error`

  500 :

  * `EIP0070: BankingGateway API - Failed to unmarshal error response body`
  * `EIP0074: Bankslip issue database error`

  In [Get issued bank slip](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-bankslips-issue-retrieve):

  403:

  * `EIP0005: Missing required header {x-tenant}`
  * `EIP0006: Invalid account id header {x-account-id}`

  409: `EIP0065: BankingGatewayAPI - API returned 409 provider error`

  In [Delete issued bank slip](https://developers.pismo.io/pismo-docs/reference/delete-integrated-payments-api-v1-bankslips-issue):

  422: `EIP0076: Bankslips issue ExternalID invalid`

  500: `EIP0074: Bankslip issue database error`

  In [Pay bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-pay):

  400:

  * `EIP0005: Missing required header {x-tenant}`
  * `EIP0006: Missing account-id header {x-account-id}`
  * `EIP0020: P2p - API returned 4xx error`
  * `EIP0061: BankingGatewayAPI - Invalid bill for payment`

  403:

  * `EIP0005: Missing required header: 'x-tenant'`
  * `EIP0006: Invalid account id header: 'x-account-id'`
  * `EIP0009: Missing required header: 'x-idempotency-key'`
  * `EIP0030: Entity's account id does not match x-account-id header`

  404: `EIP0049: Convert barcode to digitable line failed`

  409:

  * `EIP0063: Bankslips is already in processing or paid`
  * `EIP0065: BankingGatewayAPI - API returned 409 provider error`

  500: `EIP0070: BankingGateway API - Failed to unmarshal error response body`

  502:

  * `EIP0018: IntlBankAccounts - API returned 5xx error`
  * `EIP0021: P2p - API returned 5xx error`

  In [Validate bank slip](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-validate):

  403:

  * `EIP0005: Missing required header: 'x-tenant'`
  * `EIP0006: Invalid account id header: 'x-account-id'`

  409: `EIP0065: BankingGatewayAPI - API returned 409 provider error`

  500: `EIP0070: BankingGateway API - Failed to unmarshal error response body`

  502: `EIP0024: BankingGatewayAPI - API returned 5xx error`

  In [List bank slip receipt](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-bankslips-receipts):

  403: `EIP0029: Account blocked or cancelled`

  500: `EIP0014: Accounts - API returned 5xx error`

  In [Perform cash-out](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-bankslips-cashout):

  403: `EIP0014: Accounts - API returned 5xx error`

  500:

  * `EIP0019: P2p - API timeout error`
  * `EIP0028: Transaction database error`
  * `EIP0053: Send integrity message error`
  * `EIP0069: P2P API - Failed to unmarshal error response body`
  * `EIP0070: BankingGateway API - Failed to unmarshal error response body`

  502:

  * `EIP0018: IntlBankAccounts - API returned 5xx error`
  * `EIP0021: P2p - API returned 5xx error`
  * `EIP0024: BankingGatewayAPI - API returned 5xx error`

  504: `EIP0002: API request timeout`

  In [List transfer](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-transfers):

  400:

  * `EIP0010: Unmarshal error`
  * `EIP0045: Invalid value for query param 'per_page'`
  * `EIP0046: Invalid value for datetime query parameter. RFC3339 format must be used`
  * `EIP0012: Account not found`
  * `EIP0013: Accounts - API returned 4xx error`
  * `EIP0047: Invalid value for query param 'authorization_id'`

  403:

  * `EIP0005: Missing required header: 'x-tenant'`
  * `EIP0006: Invalid account id header: 'x-account-id'`
  * `EIP0029: Account blocked or cancelled`

  500:

  * `EIP0004: HTTP request error`
  * `EIP0007: Internal error`
  * `EIP0011: Accounts API timeout error`
  * `EIP0014: Accounts - API returned 5xx error`
  * `EIP0028: Transaction database error`

  In [Register eBill](https://developers.pismo.io/pismo-docs/reference/post-integrated-payments-api-v1-ebill-registration-accounts-accountid):

  400:

  * `EIP0012: Account not found`
  * `EIP0013: Accounts - API returned 4xx error`
  * `EIP0023: BankingGatewayAPI - API returned 4xx error`

  409:

  * `EIP0065: BankingGatewayAPI - API returned 409 provider error`
  * `EIP0090: Ebill registration is already being processed`

  500:

  * `EIP0011: Accounts API timeout error`
  * `EIP0014: Accounts - API returned 5xx error`
  * `EIP0089: Ebill database error`
  * `EIP0070: BankingGateway API - Failed to unmarshal error response body`

  In [Get eBill registration](https://developers.pismo.io/pismo-docs/reference/get-integrated-payments-api-v1-ebill-registration-accounts-accountid):

  403:

  * `EIP0005: Missing required header: 'x-tenant'`
  * `EIP0006: Invalid account id header: 'x-account-id'`

  404: `EIP0088: Ebill registration not found`

  500: `EIP0089: Ebill database error`

  In [Delete eBill registration](https://developers.pismo.io/pismo-docs/reference/delete-integrated-payments-api-v1-ebill-registration-accounts-accountid):

  400:

  * `EIP0012: Account not found`
  * `EIP0013: Accounts - API returned 4xx error`
  * `EIP0091: Ebill registration is not deletable`

  403:

  * `EIP0005: Missing required header: 'x-tenant'`
  * `EIP0006: Invalid account id header: 'x-account-id'`

  404:

  * `EIP0088: Ebill registration not found`
  * `EIP0062: BankingGatewayAPI - Register data not found in provider`

  409: `EIP0065: BankingGatewayAPI - API returned 409 provider error`

  500:

  * `EIP0011: Accounts API timeout error`
  * `EIP0014: Accounts - API returned 5xx error`
  * `EIP0089: Ebill database error`

  ### Instant payments

  #### Updated

  The `taxes` object was added in the following endpoints. The new object is for Brazil specific taxes. Currently, it is only available for direct participants in the EXT environment.

  * QR codes [Create recurrent COB QR Code](https://developers.pismo.io/pismo-docs/reference/post-create-recurrence-cob) endpoint, inside the `recurrence` object
  * Automatic Pix [Create recurrence](https://developers.pismo.io/pismo-docs/reference/post-recurrence-automatic) and [Update recurrence](https://developers.pismo.io/pismo-docs/reference/update-recurrence-automatic) endpoints
  * Pix [Schedule transfers](https://developers.pismo.io/pismo-docs/reference/post-schedule-pix-payment) and [Pix-out transfer](https://developers.pismo.io/pismo-docs/reference/post-pix-out-transfer) endpoints

  #### Docs

  In the [Return FPS payment](https://developers.pismo.io/pismo-docs/reference/post-return-fps) endpoint, the description of the `amount` body parameter was updated and `EFPS0096` partial return error was added to the 400 Bad Request response.

  ### Payment rails

  #### New

  The new [Return BACS direct credit inbound payment](https://developers.pismo.io/pismo-docs/reference/post-bacs-client-return) endpoint is now available in beta release.

  ### Transaction banking

  #### Updated

  The `flex_controls` and `rates` options were added to the validation rules (`validation_rules`) in credit and debit validation in the following endpoints.

  * [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments)
  * [Post multi-leg payment](https://developers.pismo.io/pismo-docs/reference/corporate-v3-post-multileg-payments-1)
  * [Schedule payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-scheduled-payments-1)

  #### Updated

  The [Create transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-account) endpoint now returns HTTP 201 for successful account creation. It previously returned HTTP 200 in error.

  #### Updated

  In the [Close transaction banking account](https://developers.pismo.io/pismo-docs/reference/post-accounts-accountid-close) endpoint, the following 422 error was added that reminds clients that an account cannot be closed while the onboarding
  is in progress: `Account onboarding has not been completed yet. The
      account cannot be closed`.

  #### Deprecated

  The following decommissioned endpoints were removed from the Developers Portal and added to the [API endpoints removed](https://developers.pismo.io/pismo-docs/reference/api-endpoints-removed) list.

  * Create operation block `POST /corporate/v1/operations-blocks`
  * List operation block `GET /corporate/v1/operations-blocks`
  * Revoke operation block `DELETE /corporate/v1/operations-blocks/{operationsBlockId}`
</summary>

<summary class="tabContent" id="Card issuing">
  ### Card network integration

  #### Docs

  The [Processing codes](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) guide was updated to remove the statement that all processing codes must have a reversal as there are some legacy codes that do not have reversals.

  #### Docs

  The Network authorization event description in the [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events#network-authorization-event) guide was updated to clarify that balance inquiries or transactions do not generate a Network authorization event.

  The description of the [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event was updated to clarify that balance inquiries or transactions do not generate a Network authorization event. In addition, the event description now properly explains that this event is for both Full balance and Zero balance issuers.

  #### Docs

  To clarify that `airport_tax` is a lifecycle marker and not a data carrier, an Airport tax note was added to the Network authorization received event description in the [Authorization events](https://developers.pismo.io/pismo-docs/docs/authorization-events#network-authorization-event) guide.

  A new topic, “How to correctly read airport tax amounts across two categories”,  was added to the Linking authorization with confirmation events section of the [Linking authorizations](https://developers.pismo.io/pismo-docs/docs/linking-events-in-an-authorization-workflow#how-to-correctly-read-airport-tax-amounts-across-two-categories) guide.

  #### Docs

  The [Authorization validation rules for card network operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-card-network-operations#list-of-rules) guide and the [Rule list](https://developers.pismo.io/pismo-docs/docs/rule-list#account-number-inquiry-ani) guide were updated to explain that both The Account Number Inquiry (ANI) and the Address Verification Service (AVS) rules apply to both Full balance and Zero balance issuers, but in different ways.

  ### Statements

  #### Docs

  The new [Credit cycle dates and time periods](https://developers.pismo.io/pismo-docs/docs/statement-cycle-dates) guide is now available. It contains some information moved from the other guides. The following guides related to calendars were updated and reorganized.

  * **Managing due date, cycle closing date, and additional grace periods** guide was deleted and the information from it was moved into other guides.
  * [Calendar management strategies](https://developers.pismo.io/pismo-docs/docs/calendar-management-strategies) guide was rewritten.
  * [Fixed due date calendar management strategy](https://developers.pismo.io/pismo-docs/docs/fixed-due-date-calendars) guide was renamed from **Fixed due date calendars** and rewritten.
  * [Fixed cycle closing calendar management strategy](https://developers.pismo.io/pismo-docs/docs/fixed-cycle-closing-calendar-management-strategy) guide was rewritten.

  #### Docs

  The description was updated for the [Create or update statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/createstatementamountdue) endpoint.

  #### Docs

  The [Bypassing the MAD calculation strategy](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#bypassing-the-mad-calculation-strategy) section was added to the Minimum amount due calculation guide.

  #### Docs

  The [Account collection status](https://developers.pismo.io/pismo-docs/docs/account-collection-status) and [Credit liquidation](https://developers.pismo.io/pismo-docs/docs/credit-liquidation) guides were updated to clarify various points.

  #### Docs

  The first two descriptions in the table in [Minimum amount due calculation](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#mad-calculation-strategy) were updated to clarify how the calculations are done.

  #### Docs

  A warning callout was added to the [Update a scheduled charge](https://developers.pismo.io/pismo-docs/docs/recurring-charges#update-a-scheduled-charge) section in the Recurring charges guide.

  ### Visa Flexible Credentials

  #### Docs

  The endpoint paths for [Visa Flexible Credentials](https://developers.pismo.io/pismo-docs/reference/enroll-card-enrollment) in the documentation were missing a beginning “/flex\_credentials”. This was corrected.
</summary>

<summary class="tabContent" id="Lending">
  ### Lending

  #### Docs

  The `repayment_calculation_method` and `interest_plan_ids` fields were documented in the [Get loan product](https://developers.pismo.io/pismo-docs/reference/getloanproductv2) and [List loan products](https://developers.pismo.io/pismo-docs/reference/getloanproductsv2) guides.

  #### Docs

  The [Create loan adjustment](https://developers.pismo.io/pismo-docs/reference/createloanadjustmentv2) endpoint was marked as \[beta], the response code was changed from 201 to 202, and the response message was corrected from "Loan product created" to "Loan adjustment created".

  #### Docs

  Information about multiple disbursements was added to the [Disburse a loan](https://developers.pismo.io/pismo-docs/docs/disburse-loan) guide, including configuration requirements and behavior when not enabled.

  #### Deprecated

  The following endpoints were decommissioned and removed from the Developers Portal and added to the [API endpoints removed](https://developers.pismo.io/pismo-docs/reference/api-endpoints-removed) list.

  * Create loan product `POST /lending/v1/loan-products`
  * List loans `GET /lending/v1/loans`
  * List loan products `GET /lending/v1/loan-products`
  * Get loan product `GET /lending/v1/loan-products/{productId}`
  * Simulate loan booking `POST /lending/v1/simulations`
  * Create charge plan `POST /lending/v1/charge-plans`
  * Create loan booking `POST /lending/v1/loans`
  * Get loan details `GET /lending/v1/loans/{loanId}`
  * Disburse loan `POST /lending/v1/loans/{loanId}/disburse`
  * Register repayment `POST /lending/v1/loans/{loanId}/repayment`
  * Register simulation for EFS `POST /lending/v1/loans/{loanId}/early-settlement/simulate`
  * Apply EFS simulation `POST /lending/v1/loans/{loanId}/early-settlement/{efsId}/register`
  * Simulate prepayment `POST /lending/v1/loans/{loanId}/prepayment/simulate`
  * Apply prepayment simulation `POST /lending/v1/loans/{loanId}/prepayment/{prepaymentId}/register`
  * Create repayment hierarchy `POST /lending/v1/repayment-hierarchies`
  * List repayment hierarchies `GET /lending/v1/repayment-hierarchies`
  * Create penalty plan `POST /lending/v1/penalty-plans`
  * Get penalty plan `GET /lending/v1/penalty-plans`
  * Cancel loan `DELETE /lending/v1/loans/{loanId}`
  * Enable repayment hierarchy `PUT /lending/v1/repayment-hierarchies/{code}/enable`
  * Disable repayment hierarchy `PUT /lending/v1/repayment-hierarchies/{code}/disable`
  * Get repayment hierarchy `GET /lending/v1/repayment-hierarchies/{code}`
  * Delete repayment hierarchy `DELETE /lending/v1/repayment-hierarchies/{code}`
  * Get loan simulation `GET /lending/v1/simulations/{loanSimulationId}`
  * Enable charge plan `PUT /lending/v1/charge-plans/{code}/enable`
  * Disable charge plan `PUT /lending/v1/charge-plans/{code}/disable`
  * List charge plan `GET /lending/v1/charge-plans`
  * Get charge plan `GET /lending/v1/charge-plans/{code}`
  * Delete charge plan `DELETE /lending/v1/charge-plans/{code}`
  * Enable penalty plan `PUT /lending/v1/penalty-plans/{code}/enable`
  * Disable penalty plan `PUT /lending/v1/penalty-plans/{code}/disable`
  * List penalty plans `GET /lending/v1/penalty-plans`
  * Delete penalty plan `DELETE /lending/v1/penalty-plans/{code}`
  * Get program configuration `GET /lending/v1/program-configurations/{programId}`
  * Update program configuration `PUT /lending/v1/program-configurations/{programId}`
</summary>

<summary class="tabContent" id="Resources">
  ### Control Center

  #### Updated

  The [dual approval](https://developers.pismo.io/pismo-docs/docs/dual-approval) feature was updated in Control Center. You can now request Pismo to enable dual approval for [editing account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects).

  #### Docs

  An accompanying explainer video was added to the [Disputes](https://developers.pismo.io/pismo-docs/docs/disputes) guide. The video introduces the Disputes feature in Control Center and provides an overview of its functionality.

  #### Docs

  The [Get started with Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) guide was streamlined in the following ways.

  * The new dedicated sub-guide called [Sign on to Control Center](https://developers.pismo.io/pismo-docs/docs/get-access-and-sign-on) was created and the sign-on steps were simplified.
  * The [Navigate Control Center](https://developers.pismo.io/pismo-docs/docs/control-center-navigation) and [Control Center security](https://developers.pismo.io/pismo-docs/docs/security-for-control-center) guides under Get started with Control Center were moved as sub-guides.
</summary>
<!-- source:end -->

## Current status of operations mentioned in this post

Checked against the current OpenAPI specifications (snapshot in the corpus). Presence in the specifications means the operation is documented today; it does not confirm that a change described above is still in effect.

| Operation | Current specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- |
| `POST /corporate/v1/corporate-accounts/{externalAccountId}/force-close` (`post-accounts-accountId-force-close`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /payment-methods/v2/payments` (`post-payments`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /payment-methods/v2/transfers` (`post-transfers`) | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01, KU-API-core-platform-payment-methods--payment-methods-part-02, KU-API-core-platform-payment-methods--payment-methods-part-03 |
| `POST /v1/balances-config/filter-templates` (`post-v1-filter-templates`) | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `GET /v1/balances-config/filter-templates` (`get-v1-filter-templates`) | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `GET /v1/balances-config/filter-templates/{id}` (`get-v1-filter-template-by-id`) | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `PUT /v1/balances-config/filter-templates/{id}` (`put-v1-filter-template`) | `api-specs/Core_platform_-_Balance_config_Beta.yaml` | no | KU-API-core-platform-balance-config-beta--filter-templates |
| `PATCH /v1/deposits/accounts/{accountId}/attachment` (`interest-bearing-v1-deposit-update-account-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `PATCH /v1/deposits/programs/{programId}/attachment` (`interest-bearing-v1-deposit-update-program-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `POST /v1/deposits/accounts/open` (`interest-bearing-v1-deposit-account-open`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--deposit-account-open |
| `POST /v2/accounts/{accountId}/bank-accounts/brazil` (`post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-brazil`) | `api-specs/Banking_-_Bank_accounts.yaml` | no | KU-API-banking-bank-accounts--bank-accounts-part-01, KU-API-banking-bank-accounts--bank-accounts-part-02 |
| `GET /v1/products/attachments/accounts/{accountId}` (`interest-bearing-v1-get-account-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `POST /v1/deposits/accounts/{accountId}/attach` (`interest-bearing-v1-deposit-attach-account`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--account-attachment |
| `GET /v1/products/attachments/programs/{programId}` (`interest-bearing-v1-get-program-attachment`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `POST /v1/deposits/programs/{programId}/attach` (`interest-bearing-v1-deposit-attach-program`) | `api-specs/Banking_-_Interest-bearing_accounts.yaml` | no | KU-API-banking-interest-bearing-accounts--program-attachment |
| `GET /v1/interest/account/{accountId}` (`get-v1-interest-account`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--account-interest |
| `PUT /v1/interest/account/{accountId}` (`put-v1-interest-account`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--account-interest |
| `POST /v1/interest/benchmark-rate` (`post-v1-benchmark-rate`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--benchmark-rate |
| `POST /v1/interest/plan` (`post-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `GET /v1/interest/plan` (`get-v1-interest-plans`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `GET /v1/interest/plan/{interestPlanId}` (`get-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `PATCH /v1/interest/plan/{interestPlanId}` (`patch-v1-interest-plan`) | `api-specs/Banking_-_Interest_engine.yaml` | no | KU-API-banking-interest-engine--interest-engine |
| `POST /v1/bankslips-issue` (`post-integrated-payments-api-v1-bankslips-issue`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `GET /v1/bankslips-issue/client-requests/{clientRequestId}` (`get-integrated-payments-api-v1-bankslips-issue-retrieve`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `DELETE /v1/bankslips-issue/client-requests/{clientRequestId}` (`delete-integrated-payments-api-v1-bankslips-issue`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip-issuance |
| `POST /v1/bankslips/pay` (`post-integrated-payments-api-v1-bankslips-pay`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `POST /v1/bankslips/validate` (`post-integrated-payments-api-v1-bankslips-validate`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `GET /v1/bankslips/receipts` (`get-integrated-payments-api-v1-bankslips-receipts`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--bank-slip |
| `POST /v1/transfers/cashout` (`post-integrated-payments-api-v1-bankslips-cashout`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--transfer |
| `GET /v1/transfers` (`get-integrated-payments-api-v1-transfers`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--transfer |
| `POST /v1/ebill-registration/accounts/{accountId}` (`post-integrated-payments-api-v1-ebill-registration-accounts-accountId`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |
| `GET /v1/ebill-registration/accounts/{accountId}` (`get-integrated-payments-api-v1-ebill-registration-accounts-accountId`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |
| `DELETE /v1/ebill-registration/accounts/{accountId}` (`delete-integrated-payments-api-v1-ebill-registration-accounts-accountId`) | `api-specs/Banking_-_Integrated_payments.yaml` | no | KU-API-banking-integrated-payments--ebill-registration |
| `POST /v1/pix/qrcode/cob/recurrence` (`post-create-recurrence-cob`) | `api-specs/Instant_payments_-_QR_Code.yaml` | no | KU-API-instant-payments-qr-code--recurring-payment |
| `POST /inst-pull-pay/v1/pix/automatic` (`post-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `PATCH /inst-pull-pay/v1/pix/automatic/{recurrence_id}` (`update-recurrence-automatic`) | `api-specs/Instant_payments_-_Automatic_Pix.yaml` | no | KU-API-instant-payments-automatic-pix--automatic-pix |
| `POST /pix/v2/pix/out/scheduler` (`post-schedule-pix-payment`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--scheduled-transfers-v2 |
| `POST /pix/v1/pix/out/transfer` (`post-pix-out-transfer`) | `api-specs/Instant_payments_-_Pix_payments.yaml` | no | KU-API-instant-payments-pix-payments--pix-part-01, KU-API-instant-payments-pix-payments--pix-part-02 |
| `POST /v1/payments/fps/return/{endToEndId}` (`post-return-fps`) | `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | no | KU-API-instant-payments-uk-fps-beta--faster-payments |
| `POST /v1/payments/bacs/directcredit/return/{id}` (`post-bacs-client-return`) | `api-specs/Payment_rails_-_BACS_payments.yaml` | no | KU-API-payment-rails-bacs-payments--bacs-direct-credit |
| `POST /corporate/v2/payments` (`corporate-v2-post-payments`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--payments-part-01, KU-API-banking-transaction-banking--payments-part-02, KU-API-banking-transaction-banking--payments-part-03 |
| `POST /corporate/v1/corporate-accounts` (`post-account`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /corporate/v1/corporate-accounts/{externalAccountId}/close` (`post-accounts-accountId-close`) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--accounts |
| `POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due` (`createStatementAmountDue`) | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |
| `POST /flex_credentials/v1/vfc/enrollment/cards/{cardId}` (`enroll-card-enrollment`) | `api-specs/Card_issuing_-_Visa_Flexible_Credentials.yaml` | no | KU-API-card-issuing-visa-flexible-credentials--enrollment |
| `GET /v2/loan-products/{productId}` (`getLoanProductV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `GET /v2/loan-products` (`getLoanProductsV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loan-products |
| `POST /v2/loans/{loanId}/adjustment` (`createLoanAdjustmentV2`) | `api-specs/Lending.yaml` | no | KU-API-lending--loans |

| Link slug | Link text(s) | Status |
| --- | --- | --- |
| `api-endpoints-removed` | API endpoints removed | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `corporate-v3-post-multileg-payments-1` | Multi-leg payments feature; Post multi-leg payment | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |
| `corporate-v2-post-scheduled-payments-1` | Schedule payment | not found in the current OpenAPI specifications and not matched to any removed-endpoint entry; status unverified (possible rename, typo or undocumented removal) |

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `changelog/2-july-2026.md` | whole document | https://developers.pismo.io/pismo-docs/changelog/2-july-2026 | `1a648c65786b1bcc…` | not stated |

## Related knowledge units

- `KU-API-banking-bank-accounts--bank-accounts-part-01` — API reference: Banking - Bank accounts — Bank accounts (part 1 of 2)
- `KU-API-banking-bank-accounts--bank-accounts-part-02` — API reference: Banking - Bank accounts — Bank accounts (part 2 of 2)
- `KU-API-banking-integrated-payments--bank-slip` — API reference: Banking - Integrated payments — Bank slip
- `KU-API-banking-integrated-payments--bank-slip-issuance` — API reference: Banking - Integrated payments — Bank slip issuance
- `KU-API-banking-integrated-payments--ebill-registration` — API reference: Banking - Integrated payments — eBill registration
- `KU-API-banking-integrated-payments--transfer` — API reference: Banking - Integrated payments — Transfer
- `KU-API-banking-interest-bearing-accounts--account-attachment` — API reference: Banking - Interest-bearing accounts — Account attachment
- `KU-API-banking-interest-bearing-accounts--deposit-account-open` — API reference: Banking - Interest-bearing accounts — Deposit account open
- `KU-API-banking-interest-bearing-accounts--program-attachment` — API reference: Banking - Interest-bearing accounts — Program attachment
- `KU-API-banking-interest-engine--account-interest` — API reference: Banking - Interest engine — Account interest
- `KU-API-banking-interest-engine--benchmark-rate` — API reference: Banking - Interest engine — Benchmark rate
- `KU-API-banking-interest-engine--interest-engine` — API reference: Banking - Interest engine — Interest engine
- `KU-API-banking-transaction-banking--accounts` — API reference: Banking - Transaction banking — Accounts
- `KU-API-banking-transaction-banking--payments-part-01` — API reference: Banking - Transaction banking — Payments (part 1 of 3)
- `KU-API-banking-transaction-banking--payments-part-02` — API reference: Banking - Transaction banking — Payments (part 2 of 3)
- `KU-API-banking-transaction-banking--payments-part-03` — API reference: Banking - Transaction banking — Payments (part 3 of 3)
- `KU-API-card-issuing-visa-flexible-credentials--enrollment` — API reference: Card issuing - Visa Flexible Credentials [beta] — Enrollment
- `KU-API-core-platform-balance-config-beta--filter-templates` — API reference: Core platform - Balance configurations — Filter templates
- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-02` — API reference: Core platform - Payment methods — Payment methods (part 2 of 3)
- `KU-API-core-platform-payment-methods--payment-methods-part-03` — API reference: Core platform - Payment methods — Payment methods (part 3 of 3)
- `KU-API-instant-payments-automatic-pix--automatic-pix` — API reference: Instant payments - Automatic Pix — Automatic Pix
- `KU-API-instant-payments-pix-payments--pix-part-01` — API reference: Instant payments - Pix payments — Pix (part 1 of 2)
- `KU-API-instant-payments-pix-payments--pix-part-02` — API reference: Instant payments - Pix payments — Pix (part 2 of 2)
- `KU-API-instant-payments-pix-payments--scheduled-transfers-v2` — API reference: Instant payments - Pix payments — Scheduled transfers V2
- `KU-API-instant-payments-qr-code--recurring-payment` — API reference: Instant payments - QR Code — Recurring payment
- `KU-API-instant-payments-uk-fps-beta--faster-payments` — API reference: Instant payments - Faster payments — Faster payments
- `KU-API-lending--loan-products` — API reference: Lending — Loan products
- `KU-API-lending--loans` — API reference: Lending — Loans
- `KU-API-payment-rails-bacs-payments--bacs-direct-credit` — API reference: Payment rails - BACS payments — BACS direct credit
- `KU-API-revolving-credit-statements--statement-minimum-amount-due` — API reference: Revolving credit - Statements — Statement minimum amount due
- `KU-LIFE-api-endpoints-removed` — API endpoints removed
- `KU-LIFE-marketplace-endpoint-removal` — Marketplace endpoints removed on 10/6/26 and guides that still reference them
