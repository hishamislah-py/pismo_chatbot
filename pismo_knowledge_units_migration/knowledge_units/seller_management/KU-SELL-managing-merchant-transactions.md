---
ku_id: KU-SELL-managing-merchant-transactions
title: Managing merchant transactions
category: seller_management
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/seller-management/managing-merchant-transactions.md
  sha256: b4f8a0501fdd64eff39171a765e4a2f696478e6e02e21722168583450ed3c914
  url: https://developers.pismo.io/pismo-docs/docs/managing-merchant-transactions
  role: primary_guide
  updated_at: '2026-03-18T15:24:20.000Z'
operations:
- CreateProcessingCode
- GetCreditorOperationsByMerchantIDAndMarketplaceID
- GetMarketPlaceByIdV2
- PostCreditorsOperations
- PostSetupTransactionType
- cancel-split-request
- createMerchant
- get-sale-split-request-totals
- listMerchantTransactionsV2
- post-authorization
- post-merchant-transaction-cancel
- post-merchant-transaction-sale
- post-split-request
related_kus:
- KU-API-core-platform-payment-methods--payment-methods-part-01
- KU-API-core-platform-transactions--transaction-types
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-API-seller-management-marketplace--marketplace
- KU-API-seller-management-marketplace--marketplace-creditor-operations
- KU-API-seller-management-merchants--merchant
- KU-API-seller-management-merchants--merchant-transaction
- KU-API-seller-management-transactions--merchant-transactions
- KU-API-seller-management-transactions--split-requests
- KU-CORE-transactiontypes
- KU-EVT-catalogue-marketplace
- KU-EVT-catalogue-merchants
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-PAY-payment-methods
- KU-SELL-how-merchant-settlements-are-processed
- KU-SELL-seller-management-overview-and-onboarding
grouping_rationale: single source page
---

# Managing merchant transactions

**KU ID:** `KU-SELL-managing-merchant-transactions` · **Category:** Seller management · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/seller-management/managing-merchant-transactions.md`:

> Marketplace transactions represent sales where payments go to merchants affiliated with the marketplace. When creating a merchant transaction, you can include optional details such as installments, MDR (Merchant Discount Rate) calculations, and scheduled payment dates. It's also possible to split a transaction across multiple merchants or cancel an existing merchant transaction. You can cancel a request to split transactions also.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/seller-management/managing-merchant-transactions.md`: Managing merchant transactions; Prerequisites for merchant transactions; Create an authorization for merchant transactions; Create a transaction per merchant; Cancel a merchant transaction; Create transactions to split between merchants; Prerequisites for splitting a transaction; Pre-authorize the sale transaction; Create a split transaction; Cancel a split request; Request split totals

## Prerequisites and dependencies

- Prerequisites are described in `docs/seller-management/managing-merchant-transactions.md` section "Prerequisites for merchant transactions".
- Prerequisites are described in `docs/seller-management/managing-merchant-transactions.md` section "Prerequisites for splitting a transaction".
- Depends on 13 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/seller-management/managing-merchant-transactions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/managing-merchant-transactions · updatedAt: 2026-03-18T15:24:20.000Z

<!-- source:begin path=docs/seller-management/managing-merchant-transactions.md part=0-end -->

# Managing merchant transactions

Marketplace transactions represent sales where payments go to merchants affiliated with the marketplace. When creating a merchant transaction, you can include optional details such as installments, MDR (Merchant Discount Rate) calculations, and scheduled payment dates. It's also possible to split a transaction across multiple merchants or cancel an existing merchant transaction. You can cancel a request to split transactions also.

> 📘
>
> The Pismo platform handles merchant transactions separately from the general [transaction types](https://developers.pismo.io/pismo-docs/docs/transactiontypes) listed via the [List transaction types](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) endpoint. To retrieve merchant transactions, use the [List merchant transactions (V2)](https://developers.pismo.io/pismo-docs/reference/listmerchanttransactionsv2) endpoint instead.

## Prerequisites for merchant transactions

You should be onboarded for Seller management as a prerequisite to offering merchant transactions or splitting transactions between merchants. See  [Seller management onboarding](https://developers.pismo.io/pismo-docs/docs/seller-management-onboarding) for requirements to meet during onboarding.

You need to have [processing codes](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) for your organization, [creditor operations](https://developers.pismo.io/pismo-docs/reference/postcreditorsoperations), and [merchants](https://developers.pismo.io/pismo-docs/reference/createmerchant) in the [marketplace](https://developers.pismo.io/pismo-docs/reference/postmarketplacesv2) prior to creating a merchant transaction (per merchant or split among multiple merchants).

Optionally, you can take in transactions in a flow from the [Payment methods API](https://developers.pismo.io/pismo-docs/docs/payment-methods). The Pismo platform automatically creates a merchant transaction when it sees a marketplace ID and merchant ID in the payment information. The `mti` or Message Type Identifier makes this connection with authorization requests with the `mti` value `0100`(clearing type offline). Then the client sends a confirmation request with `mti` value `0202` (clearing type online) to confirm the transaction in this flow.

## Create an authorization for merchant transactions

Use this workflow for authorization and to automatically create a merchant transaction. When using the Payment methods API, any transactions containing the marketplace ID and merchant ID creates a merchant transaction automatically with `transaction_status` set to `SCHEDULED`.

1. Request authorization using the PCI endpoint, [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization). You get an authorization ID in the response.
2. Use the authorization ID when creating the merchant transaction in the request body like this example:
   ```json
   {
     "event_date": "2025-02-14T10:30:00Z",
     "amount": 1500.00,
     "installments": 12,
     "authorization_id": 123456,
     "processing_code": "000700",
     "transaction_status": "SCHEDULED"
   }
   ```

See the [Payment methods](https://developers.pismo.io/pismo-docs/docs/payment-methods) guide for details on authorizations.

If you want to cancel a merchant transaction later, you use this `authorization_id` as the `parent_id`, representing the parent authorization identifier from the original transaction. You'll have a separate authorization identifier for the cancellation.

## Create a transaction per merchant

To create a single merchant transaction, you need the following information:

* Marketplace ID
* Merchant ID
* Date you want the transaction event to take place
* Amount
* Number of installments
* Processing code
* (optional) Authorization ID

You can optionally provide an authorization ID obtained with a [Request authorization](https://developers.pismo.io/pismo-docs/reference/post-authorization) workflow and the Payment methods API endpoints to manage cash-in, cash-out, and transfer operations. Walk through that workflow in [Create an authorization for merchant transactions](https://developers.pismo.io/pismo-docs/docs/managing-merchant-transactions#create-an-authorization-for-merchant-transactions).

Create a new transaction for a single merchant using the [Create merchant transaction ](https://developers.pismo.io/pismo-docs/reference/post-merchant-transaction-sale)endpoint (without optional authorization) with a request body like this example:

```json
{
  "event_date": "2025-08-14T10:30:00Z",
  "amount": 1000.00,
  "installments": 12,
  "processing_code": "000700",
  "transaction_status": "SCHEDULED"
}
```

This endpoint responds with HTTP 201 (Created) status code, a response body, and generates a [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) event. The Pismo platform considers time zone, MDR taxes, and marketplace creditor operations when creating the transaction.

## Cancel a merchant transaction

Example for canceling a merchant transaction with the [Create reversal transaction](https://developers.pismo.io/pismo-docs/reference/post-merchant-transaction-cancel) endpoint. Notice that the `authorization` requires both a new identifier and the `parent_id` which is the original authorization ID.

```json
{
  "event_date": "2025-02-18T11:35:00Z",
  "amount": 1500.00,
  "authorization": {
    "id": 123456,
    "parent_id": 654321
  },
  "processing_code": "000701"
}
```

This endpoint generates a [Merchant transaction settled](https://developers.pismo.io/events/docs/merchants-merchant-transaction-settled-1) event.

## Create transactions to split between merchants

In a marketplace with multiple vendors, you can split transactions between merchants for accurate account crediting. The transaction split ensures that each merchant receives their share of a transaction, based on defined amounts or percentages. It's particularly useful when a transaction involves multiple merchants, such as in a marketplace selling products from various vendors. For example, in an art-selling marketplace, a single checkout might include items from different artists. By splitting transactions, the marketplace can automate settlements, reduce administrative overhead, and provide a single purchase point for a buyer. This method also supports commissions or fees, ensuring appropriate compensation for all merchants.

Managing split transactions involves configuring, creating, and processing split requests among merchants in a marketplace with a scheduler entity. You also can cancel a split request if needed. This guide outlines the necessary API calls and steps to handle these marketplace management tasks.

The Pismo platform uses the concept of a "marketplace scheduler" to handle these split transactions. Each marketplace created with the v2 [Create marketplace](https://developers.pismo.io/pismo-docs/reference/postmarketplacesv2) endpoint has a "schedule ID" assigned that serves as a marketplace scheduler. By creating the split transaction with the scheduler as the initial merchant, you put the transaction through the proper status changes from WAITING\_SPLIT to PROCESSED.

## Prerequisites for splitting a transaction

You can determine which merchants belong to the marketplace using the  [List marketplace merchants](https://developers.pismo.io/pismo-docs/reference/getmerchantsbymarketplaceidv2) endpoint. You can use the [List creditor operations for marketplace and merchant](https://developers.pismo.io/pismo-docs/reference/getcreditoroperationsbymerchantidandmarketplaceid) endpoint to view the rules applied for each. All merchants involved in the split must have their fee registration configured in the platform and they must be linked to the marketplace. The marketplace must have a valid `schedule_id` and in turn that merchant must have a valid `creditor_id`. This requirement means that you must create the marketplace with the v2  [Create marketplace](https://developers.pismo.io/pismo-docs/reference/postmarketplacesv2) endpoint.

The data required for any split transaction includes:

* Merchant transaction ID
* Marketplace schedule ID (in the v2 [Get marketplace](https://developers.pismo.io/pismo-docs/reference/getmarketplacebyidv2) response body you find the `schedule_id`)
* Event date for when the split should occur
* Processing code

You indicate all the merchants involved in the split transaction in a later API call.

## Pre-authorize the sale transaction

First, use the [Create merchant transaction](https://developers.pismo.io/pismo-docs/reference/createmerchantusingmerchantid) endpoint and create a merchant transaction, specifying a merchant that is a marketplace scheduler. When you create a merchant transaction with the Marketplace's `schedule_id`, you get a transaction ID with a `WAITING_SPLIT` status.

In this example, the `marketplace_id` is `2625`. This marketplace has a scheduler assigned to it, which you use in the next section.

Create a merchant transaction with this example request body:

```json

{
  "authorization": {
    "principal_amount": 1000,
    "number_of_installments": 1,
    "installment_amount": 1000,
    "event_date_hour": "2025-04-20T18:14:56Z"
  },
  "acceptance": {
    "matched_mdr": false,
    "matched_settlement": false,
    "mdr": 0.03,
    "transaction_fee": 1,
  },
  "operation": {
    "org_operation_id": 1125
  },
  "additional_info": {
    "account_id": 8675309
  },
  "marketplace_id": 2625
}
```

Authorization applies to the full amount prior to splitting the amount per merchant. There's no split for authorization, only one authorization for the total amount. The authorization amount does not exceed the sum of split amounts.

## Create a split transaction

Next, you provide the merchant authorization ID to the [Create split request](https://developers.pismo.io/pismo-docs/reference/post-split-request) endpoint. This endpoint generates a [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) event.

```json
{
  "event_date": "2025-04-20T18:15:56Z",
  "installments": 1,
  "processing_code": "0120",
  "definitions": [
    {
      "merchant_id": 20445, # represents the scheduler_id for the marketplace
      "amount": 100,
      "amount_percentage": 0.35
    }
  ]
}
```

When you create a split transaction request, you specify either the `amount` or `amount_percentage` that defines the split, however you cannot combine fees and percentages, you must use one or the other. The total split cannot exceed the authorized transaction amount. Also, when using `amount_percentage`, the sum of each must total 1.0.

Specify a merchant that is a marketplace scheduler in the request by using the `schedule_id` that matches up with the marketplace. You must have a merchant transaction already created using the [Create merchant transaction](https://developers.pismo.io/pismo-docs/reference/createmerchantusingmerchantid) endpoint.

Here is an example request body for a split transaction. This example shows a split request sale request between two merchants with a percentage indicated. For percentage, the value is a decimal value where 0.7 represents 70%, 0.3 represents 30%, and 1.0 represents 100%. The total percentages must equal 1.0.

```json
{
  "event_date": "2024-12-18T08:07:07Z",
  "installments": 1,
  "processing_code": "003000",
  "definitions": [
    {
      "merchant_id": 46729,
      "amount_percentage": 0.7
    },
    {
      "merchant_id": 49558,
      "amount_percentage": 0.3
    }
  ]
}
```

The endpoint responds with HTTP 202 (Accepted) status code and generates a [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) event.

After processing the transaction, settlement occurs so that the system debits the customer's account, credits each merchant's account according to the defined splits (amount or percentage), then sets the transaction to `PROCESSED`. See [How merchant settlements are processed](https://developers.pismo.io/pismo-docs/docs/how-merchant-settlements-are-processed) for details.

## Cancel a split request

You can cancel the split transaction using the [Cancel split request](https://developers.pismo.io/pismo-docs/reference/cancel-split-request) endpoint. You must have the transaction ID of the original merchant transaction that was split. The body of the request contains the details such as event date, processing code, marketplace, and which merchants were included in the original split request.

```json
{
  "event_date": "2023-12-19T20:23:55Z",
  "installments": 1,
  "processing_code": "009900",
  "marketplace": {
    "id": 1,
  },
  "definitions": [
    {
      "merchant_id": 46729,
      "amount": 100,
    },
    {
      "merchant_id": 47187,
    }
  ]
}
```

## Request split totals

When you want to know the totals from a specific parent split request with the PROCESSED status, use the [Get split request totals](https://developers.pismo.io/pismo-docs/reference/get-sale-split-request-totals) endpoint. It returns the gross amount for each participating merchant, as well as the marketplace schedule ID.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/transaction-types` | `PostSetupTransactionType` | Create transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `GET /v2/merchants/{merchantId}/transactions` | `listMerchantTransactionsV2` | List merchant transactions (V2) | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant-transaction |
| `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | Create processing code | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /marketplaces/{marketplaceId}/creditors-operations` | `PostCreditorsOperations` | Create creditor operation | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `POST /v1/merchants` | `createMerchant` | Create merchant | `api-specs/Seller_management_-_Merchants.yaml` | no | KU-API-seller-management-merchants--merchant |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | `api-specs/Core_platform_-_Payment_methods.yaml` | no | KU-API-core-platform-payment-methods--payment-methods-part-01 |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` | `post-merchant-transaction-sale` | Create merchant transaction | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--merchant-transactions |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel` | `post-merchant-transaction-cancel` | Cancel merchant transaction | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--merchant-transactions |
| `GET /marketplaces/{marketplaceId}/merchants/{merchantId}/creditors-operations` | `GetCreditorOperationsByMerchantIDAndMarketplaceID` | List creditor operations for marketplace and merchant | `api-specs/Seller_management_-_Marketplace.yaml` | no | KU-API-seller-management-marketplace--marketplace-creditor-operations |
| `GET /v2/marketplaces/{marketplaceId}` | `GetMarketPlaceByIdV2` | Get marketplace V2 (deprecated) | `api-specs/Seller_management_-_Marketplace.yaml` | **yes** | KU-API-seller-management-marketplace--marketplace |
| `POST /v1/transactions/{merchantTransactionId}/split` | `post-split-request` | Create split request | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `POST /v1/transactions/{merchantTransactionId}/split/cancel` | `cancel-split-request` | Cancel split request | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |
| `GET /v1/marketplaces/{marketplaceId}/split-requests/{parentId}/totals` | `get-sale-split-request-totals` | Get split request totals | `api-specs/Seller_management_-_Transactions.yaml` | no | KU-API-seller-management-transactions--split-requests |

### Operation essentials

- **`POST /v1/transaction-types`** (`PostSetupTransactionType`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `description`, `credit`, `posted_transaction`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05001`, `WTRC08001`, `ETRC00001`; events `transaction-types-creation-1`.
- **`GET /v2/merchants/{merchantId}/transactions`** (`listMerchantTransactionsV2`): security `BearerAuth`; required parameters `merchantId` (path); required body fields none declared; response statuses 200, 400, 401, 404, 408, 500; error codes in examples none; events none listed.
- **`POST /orgs-operation/v1/processing-codes`** (`CreateProcessingCode`): security `S2SAuthentication`; required parameters none declared; required body fields `processing_code`, `balance_impact`, `description`, `reversal_processing_code`; response statuses 201, 400; error codes in examples none; events `orgs-operation-create-1`.
- **`POST /marketplaces/{marketplaceId}/creditors-operations`** (`PostCreditorsOperations`): security `BearerAuth`; required parameters `marketplaceId` (path); required body fields `creditor_id`, `first_installment_days_to_payment`, `installments`, `n_installment_days_to_payment`; response statuses 200, 400, 401, 500; error codes in examples none; events `marketplace-marketplace-creditor-operation-created-1`.
- **`POST /v1/merchants`** (`createMerchant`): security `BearerAuth`; required parameters none declared; required body fields `document_number`, `name`, `email`; response statuses 201, 400, 401, 500; error codes in examples none; events `merchants-merchant-created-1`.
- **`POST /payment-methods/v1/authorization`** (`post-authorization`): security `BearerAuth`; required parameters none declared; required body fields `currency_code`, `mti`, `network`; response statuses 200, 201, 400, 401, 403, 422, 500; error codes in examples `WONA0001`, `WONA0004`, `WONA0005`, `WONA0006`, `WONA0011`, `WONA0012`, `WONA0013`, `WONA0015`, `WONA0016`, `WONA0018`, `WONA0019`, `WONA0020`, `WONA0032`, `WONA0033`, `WONA0036`, `WONA039`, `WONA040`, `WONA041`, `WONA042`, `WONA043`, `EINS0004`, `EINS0005`, `EINS0006`, `EINS0010`, `EINS0011`, `EINS0012`, `EINS0015`, `EINS0016`, `EPAE0004`, `EPAE0001`, `EPAE0002`; events `payment-methods-authorization-1`, `platform-authorization-platform-authorization-1`.
- **`POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions`** (`post-merchant-transaction-sale`): security `bearerAuth`; required parameters `Authorization` (header), `marketplaceId` (path), `merchantId` (path); required body fields `event_date`, `amount`, `installments`, `processing_code`; response statuses 201, 400, 500; error codes in examples `ESMT0001`; events `merchants-merchant-transaction-created-1`.
- **`POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel`** (`post-merchant-transaction-cancel`): security `bearerAuth`; required parameters `Authorization` (header), `marketplaceId` (path), `merchantId` (path); required body fields `event_date`, `amount`, `authorization`, `processing_code`; response statuses 201, 400, 500; error codes in examples `ESMT0001`; events `merchants-merchant-transaction-created-1`.
- **`GET /marketplaces/{marketplaceId}/merchants/{merchantId}/creditors-operations`** (`GetCreditorOperationsByMerchantIDAndMarketplaceID`): security `BearerAuth`; required parameters `marketplaceId` (path), `merchantId` (path); required body fields none declared; response statuses 200, 400, 401, 500; error codes in examples none; events none listed.
- **`GET /v2/marketplaces/{marketplaceId}`** (`GetMarketPlaceByIdV2`): security `BearerAuth`; required parameters `marketplaceId` (path); required body fields none declared; response statuses 200, 400, 401, 500, 502; error codes in examples none; events none listed.
- **`POST /v1/transactions/{merchantTransactionId}/split`** (`post-split-request`): security `bearerAuth`; required parameters `Authorization` (header), `merchantTransactionId` (path); required body fields `event_date`, `installments`, `processing_code`, `definitions`; response statuses 202, 400, 500; error codes in examples `ESMT0001`; events `merchants-merchant-transaction-created-1`.
- **`POST /v1/transactions/{merchantTransactionId}/split/cancel`** (`cancel-split-request`): security `bearerAuth`; required parameters `Authorization` (header), `merchantTransactionId` (path); required body fields `event_date`, `processing_code`; response statuses 202, 400, 500; error codes in examples `ESMT0001`; events `merchants-merchant-transaction-created-1`.
- **`GET /v1/marketplaces/{marketplaceId}/split-requests/{parentId}/totals`** (`get-sale-split-request-totals`): security `bearerAuth`; required parameters `Authorization` (header), `parentId` (path), `marketplaceId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `ESMT0001`; events none listed.

### Operation links that do not resolve to a current specification

| Link slug | Link text(s) in source | Status |
| --- | --- | --- |
| `postmarketplacesv2` | Create marketplace; Create your marketplace; marketplace | not found in the current OpenAPI specifications. Name-based inference: link text "Create marketplace" equals the endpoint name "Create marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. |
| `getmerchantsbymarketplaceidv2` | List marketplace merchants | not found in the current OpenAPI specifications. Name-based inference: link text "List marketplace merchants" equals the endpoint name "List marketplace merchants" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier. |
| `createmerchantusingmerchantid` | Create merchant transaction; Create merchant transactions | not found in the current OpenAPI specifications. Name-based inference: link text "Create merchant transaction" equals the endpoint name "Create merchant transaction" in the removed-endpoints list (row Seller Management / Merchant transactions, date removed `7/24/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`post-merchant-transaction-sale` (POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions)); no source states that it replaces the removed endpoint. |

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `PostCreditorsOperations` | `marketplace-marketplace-creditor-operation-created-1` |
| `createMerchant` | `merchants-merchant-created-1` |
| `cancel-split-request` | `merchants-merchant-transaction-created-1` |
| `post-merchant-transaction-cancel` | `merchants-merchant-transaction-created-1` |
| `post-merchant-transaction-sale` | `merchants-merchant-transaction-created-1` |
| `post-split-request` | `merchants-merchant-transaction-created-1` |
| `CreateProcessingCode` | `orgs-operation-create-1` |
| `post-authorization` | `payment-methods-authorization-1` |
| `post-authorization` | `platform-authorization-platform-authorization-1` |
| `PostSetupTransactionType` | `transaction-types-creation-1` |

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `merchants-merchant-transaction-created-1` | merchants | 1 | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 | 5 | KU-EVT-catalogue-merchants |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/seller-management/managing-merchant-transactions.md`: updatedAt 2026-03-18T15:24:20.000Z.
- Links to `GetMarketPlaceByIdV2`, which is marked `deprecated: true` in `api-specs/Seller_management_-_Marketplace.yaml`.
- Links to `postmarketplacesv2`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Create marketplace" equals the endpoint name "Create marketplace" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier.
- Links to `getmerchantsbymarketplaceidv2`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "List marketplace merchants" equals the endpoint name "List marketplace merchants" in the removed-endpoints list (row Marketplace / Seller Management - Marketplace, date removed `10/6/26`). This is a match on the endpoint name, not on an identifier.
- Links to `createmerchantusingmerchantid`, which is not in the current specifications; not found in the current OpenAPI specifications. Name-based inference: link text "Create merchant transaction" equals the endpoint name "Create merchant transaction" in the removed-endpoints list (row Seller Management / Merchant transactions, date removed `7/24/2026`). This is a match on the endpoint name, not on an identifier. A current operation has the same summary (`post-merchant-transaction-sale` (POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions)); no source states that it replaces the removed endpoint.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/seller-management/managing-merchant-transactions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/managing-merchant-transactions | `b4f8a0501fdd64ef…` | 2026-03-18T15:24:20.000Z |

## Related knowledge units

- `KU-API-core-platform-payment-methods--payment-methods-part-01` — API reference: Core platform - Payment methods — Payment methods (part 1 of 3)
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-API-seller-management-marketplace--marketplace` — API reference: Seller management - Marketplace — Marketplace
- `KU-API-seller-management-marketplace--marketplace-creditor-operations` — API reference: Seller management - Marketplace — Marketplace creditor operations
- `KU-API-seller-management-merchants--merchant` — API reference: Seller management - Merchants — Merchant
- `KU-API-seller-management-merchants--merchant-transaction` — API reference: Seller management - Merchants — Merchant transaction
- `KU-API-seller-management-transactions--merchant-transactions` — API reference: Seller management - Transactions — Merchant transactions
- `KU-API-seller-management-transactions--split-requests` — API reference: Seller management - Transactions — Split requests
- `KU-CORE-transactiontypes` — Transaction types
- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-PAY-payment-methods` — Payment methods
- `KU-SELL-how-merchant-settlements-are-processed` — How merchant settlements and installments are processed
- `KU-SELL-seller-management-overview-and-onboarding` — Seller management overview and onboarding
