---
ku_id: KU-API-seller-management-merchants--merchant-transaction
title: 'API reference: Seller management - Merchants — Merchant transaction'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Merchants.yaml
  sha256: ebc9f3fadda7001c7ad8d607cd3fe07461f96c39c6ca15baccef307dd27f67bb
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: openapi_specification
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/operations_catalog.csv
  sha256: b218bf75940b0c374ca9e3a48fe92fb615b559e3192f263aff99b738b50a71cf
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
- path: api-reference-data/request_response_examples.csv
  sha256: ac921f2e8d0d154511b4550462e609cf6bebe3e6ce05dada157e0ed645a80856
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- listMerchatTransactionsByOperationsV3
- listMerchantTransactionsV2
- listMerchantTransactionsV3
- getMerchantTransactionV2
- listMerchantTaxes
- getTransactionsSummary
- getTransactionsSummaryV2
- getReportForMerchantTransactionTypesV3
- getTransactionDetails
- updateTransactionStatus
related_kus:
- KU-SELL-managing-merchant-transactions
- KU-SELL-seller-marketplace-implementation-steps
specification_version: 1.0.0
---

# API reference: Seller management - Merchants — Merchant transaction

**KU ID:** `KU-API-seller-management-merchants--merchant-transaction` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 10 operation(s) tagged `Merchant transaction` in `api-specs/Seller_management_-_Merchants.yaml` (“Seller management - Merchants”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for transactions

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v3/merchants/{merchantId}/operations` | `listMerchatTransactionsByOperationsV3` | List merchant transactions by operations | no |
| `GET /v2/merchants/{merchantId}/transactions` | `listMerchantTransactionsV2` | List merchant transactions (V2) | no |
| `GET /v3/merchants/{merchantId}/transactions` | `listMerchantTransactionsV3` | List merchant transactions (V3) | no |
| `GET /v2/merchants/{merchantId}/transactions/{merchantTransactionId}` | `getMerchantTransactionV2` | Get merchant transaction | no |
| `GET /v1/merchants/{merchantId}/transactions/tax` | `listMerchantTaxes` | List merchant taxes | no |
| `GET /v1/merchants/{merchantId}/transactions-totals` | `getTransactionsSummary` | Get transactions summary | no |
| `GET /v2/merchants/{merchantId}/transactions-totals` | `getTransactionsSummaryV2` | Get transactions summary [beta] | no |
| `GET /v3/merchants/{merchantId}/transactions-types` | `getReportForMerchantTransactionTypesV3` | Get transaction types | no |
| `GET /v1/merchants/{merchantId}/transactions/{transactionId}` | `getTransactionDetails` | Get transaction details (deprecated) | **yes** |
| `PATCH /v1/merchants/{merchantId}/transactions/{transactionId}` | `updateTransactionStatus` | Update transaction status | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v3/merchants/{merchantId}/operations operationId=listMerchatTransactionsByOperationsV3 -->
### `GET /v3/merchants/{merchantId}/operations` — List merchant transactions by operations

- **operationId:** `listMerchatTransactionsByOperationsV3`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List merchant transactions grouped by Org operations. Returns one item for each Org operation that has transactions for the specified date.
> An item lists the amounts (gross, net, and discount) for that operation.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `marketplace` | query | no | integer | Marketplace ID | format: "int64"; example: 1 |
| `paymentDate` | query | no | string | Payment date. Format = yyyy-mm-dd. | format: "date"; example: "2018-03-29" |
| `transactionType` | query | no | string | Transaction type. Currently, SALES is the only value allowed.<br> | enum: ["SALES"]; example: "SALES" |
| `status` | query | no | string | Advancement request status | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PENDING" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `GETMerchantOperationsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v2/merchants/{merchantId}/transactions operationId=listMerchantTransactionsV2 -->
### `GET /v2/merchants/{merchantId}/transactions` — List merchant transactions (V2)

- **operationId:** `listMerchantTransactionsV2`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List merchants transactions filtered using query parameters.
>
> <b>NOTE</b>: By default, the endpoint returns only 60 days of merchant transactions. If you want a longer period (up to 365 days),
> you must provide the `saleAuthorizationId` parameter, and specify a desired date in both `startEventDate` and `endEventDate`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `originTransactionId` | query | no | integer | Merchant's original transaction ID. If it's a sale, then it's null; if it's a refund, then it refers to the transaction ID of a sale. | format: "int64"; example: 1 |
| `authorizationId` | query | no | integer | Authorization ID. Automatically generated unique identifier used in any flow where a transaction is created, whether sale, resale or cancellation.<br> | format: "int64"; example: 112345 |
| `saleAuthorizationId` | query | no | integer | Authorization ID of sale. This refers to the authorization ID of a transaction to which the current transaction is tied.<br>For example, when you cancel a transaction, `saleAuthorizationId` is the `authorizationId` of the transaction that you are cancelling.<br><br>Example of a sale: authorizationId: 101011<br><br>Cancelling this sale: authorizationId: 101012, saleAuthorizationId : 101011<br> | format: "int64"; example: 112345 |
| `orderId` | query | no | integer | Marketplace authorization (external or internal) ID | format: "int64"; example: 1 |
| `status` | query | no | string | Transaction status | enum: ["PENDING", "SCHEDULED", "BLOCKED", "SETTLED", "PAID", "ADVANCED", "CANCELED", "RETURNED"]; example: "SCHEDULED" |
| `startEventDate` | query | no | string | Date authorization is generated (and associated event emitted). Format is `yyyy-mm-dd`. | format: "date"; example: "2020-01-01" |
| `endEventDate` | query | no | string | End date of transaction event. Format is `yyyy-mm-dd`. | format: "date"; example: "2020-01-02" |
| `startPaymentDate` | query | no | string | Scheduled payment start date. Find scheduled payments between this date and `endPaymentDate`. Format = yyyy-mm-dd. | format: "date"; example: "2020-01-01" |
| `endPaymentDate` | query | no | string | Scheduled payment end date. Format = yyyy-mm-dd. Find scheduled payments between `startPaymentDate` and this date. | format: "date"; example: "2020-01-02" |
| `startReceiptDate` | query | no | string | Start date of merchant transaction settlement. Format is `yyyy-mm-dd`. | format: "date"; example: "2020-01-01" |
| `endReceiptDate` | query | no | string | End date of merchant transaction settlement. Format is `yyyy-mm-dd`. | format: "date"; example: "2020-01-02T00:00:00.000Z" |
| `operation` | query | no | integer | Transaction operation description | format: "int64"; example: 1; deprecated: true |
| `orgOperationId` | query | no | integer | Processing code. See <a href="https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types" target="_blank">Processing codes and transaction types</a>. | format: "int64"; example: 1 |
| `grossValue` | query | no | number | Gross amount of the transaction. `startEventDate` and `endEventDate` must be on the same date.<br>For example: grossValue: 100, startEventDate: 2023-03-01, endEventDate: 2023-03-01,<br> | format: "float"; example: 12.01 |
| `netValue` | query | no | number | Net amount of the transaction. `startEventDate` and `endEventDate` must be on the same date.<br>For example: netValue: 101, startEventDate: 2023-04-01, endEventDate: 2023-04-01<br> | format: "float"; example: 10.01 |
| `page` | query | no | integer | Page number. Default is 1. | format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `TransactionsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 408 | Request timeout |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int64"; example: 74 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page | format: "int64"; example: 20 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int64"; example: 10 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page number | default: 1; format: "int64"; example: 1 |
| `tax` | object (schema `RelatedFees`) | no | The related fees available to operation |  |
| `items` | array of object | no | Transactions for merchant |  |
| `items[].id` | integer (schema `MerchantTransactionID`) | no | Merchant transaction ID | format: "int64"; example: 1 |
| `items[].origin_transaction_id` | integer (schema `OriginTransactionID`) | no | ID of parent merchant transaction. If sale, this is null. If refund, this is the transaction ID of the sale. | format: "int64"; example: 1 |
| `items[].authorization_id` | string (schema `AuthorizationID`) | no | Authorization ID | example: "13387693" |
| `items[].sale_authorization_id` | string (schema `SaleAuthorizationID`) | no | ID of parent sale authorization | example: "13387693" |
| `items[].order_id` | integer (schema `MarketplaceAuthorizationID`) | no | Marketplace authorization ID (external or internal) | format: "int64"; example: 1 |
| `items[].type` | string (schema `MerchantTransactionType`) | no | Transaction type. Currently, SALES is the only value allowed.<br> | enum: ["SALES"]; example: "SALES" |
| `items[].number_of_installments` | integer (schema `NumberOfInstallments`) | no | Number of installments | format: "int64"; example: 3 |
| `items[].installment` | integer (schema `InstallmentNumber`) | no | Installment number of transaction | format: "int64"; example: 2 |
| `items[].gross_value` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `items[].net_value` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |
| `items[].discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `items[].advanced_amount` | number (schema `AdvancementAmount`) | no | Advancement amount | format: "float"; example: 988.9 |
| `items[].operation_type` | integer (schema `OperationType`) | no | Operation type ID | format: "int64"; example: 89 |
| `items[].operation` | string (schema `OperationName`) | no | Operation name | example: "Credit card without quotas" |
| `items[].event_date` | string (schema `TransactionEventDate`) | no | The transaction event date and time (sale or refund). UTC date/time - format: yyyy-MM-ddThh:mm:ssZ | format: "datetime"; example: "2020-07-14T00:41:29Z" |
| `items[].payment_date` | string (schema `ScheduledPaymentDate`) | no | Scheduled payment date. Format = yyyy-mm-dd. | format: "date"; example: "2020-04-20" |
| `items[].receipt_date` | string (schema `MerchantTransactionSettlementDate`) | no | Date of merchant transaction settlement. Format = yyyy-mm-dd. | format: "date"; example: "2020-07-16T00:00:00.000Z" |
| `items[].received_value` | number (schema `TransactionAmountSettled`) | no | Transaction amount settled | format: "float"; example: 0.1 |
| `items[].status` | string (schema `MerchantTransactionStatus`) | no | Merchant transaction status | enum: ["PENDING", "SCHEDULED", "BLOCKED", "SETTLED", "PAID", "ADVANCED", "CANCELED", "RETURNED", "WAITING_SPLIT", "SPLITTED"] |
| `items[].meta` | array of object (schema `TransactionMetadata`) | no | Metadata. The accepted parameters are `MarketplaceAuthorization` and `MarketplaceTransaction`. | example: [{"name": "MarketplaceAuthorization", "value": "ashga-jwjh-huahu-wquiqw"}, {"name": "MarketplaceTransaction", "value": "wquiqw-jwjh-huahu-ashga"}] |
| `items[].meta[].name` | string | no |  | example: "any value" |
| `items[].meta[].value` | string | no |  | example: "any value" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;408;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-SELL-managing-merchant-transactions`, `KU-SELL-seller-marketplace-implementation-steps`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v3/merchants/{merchantId}/transactions operationId=listMerchantTransactionsV3 -->
### `GET /v3/merchants/{merchantId}/transactions` — List merchant transactions (V3)

- **operationId:** `listMerchantTransactionsV3`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List merchant transactions filtered using query parameters.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `marketplaceId` | query | no | integer | Marketplace ID | format: "int64"; example: 1 |
| `status` | query | no | string | Transaction status | enum: ["PENDING", "SCHEDULED", "BLOCKED", "SETTLED", "PAID", "ADVANCED", "CANCELED", "RETURNED"]; example: "SCHEDULED" |
| `startPaymentDate` | query | no | string | Scheduled payment start date. Find scheduled payments between this date and `endPaymentDate`. Format = yyyy-mm-dd. | format: "date"; example: "2020-01-01" |
| `endPaymentDate` | query | no | string | Scheduled payment end date. Format = yyyy-mm-dd. Find scheduled payments between `startPaymentDate` and this date. | format: "date"; example: "2020-01-02" |
| `startEventDate` | query | no | string | Date authorization is generated (and associated event emitted). Format is `yyyy-mm-dd`. | format: "date"; example: "2020-01-01" |
| `endEventDate` | query | no | string | End date of transaction event. Format is `yyyy-mm-dd`. | format: "date"; example: "2020-01-02" |
| `startReceiptDate` | query | no | string | Start date of merchant transaction settlement. Format is `yyyy-mm-dd`. | format: "date"; example: "2020-01-01" |
| `endReceiptDate` | query | no | string | End date of merchant transaction settlement. Format is `yyyy-mm-dd`. | format: "date"; example: "2020-01-02T00:00:00.000Z" |
| `orgOperationId` | query | no | integer | Processing code. See <a href="https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types" target="_blank">Processing codes and transaction types</a>. | format: "int64"; example: 1 |
| `sortBy` | query | no | string | Sort field | example: "paymentDate" |
| `meta` | query | no | string | Metadata. The accepted parameters are `MarketplaceAuthorization` and `MarketplaceTransaction`. | minLength: 1; maxLength: 128; example: "MarketplaceTransaction:wquiqw-jwjh-huahu-ashga" |
| `page` | query | no | integer | Page number. Default is 1. | format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETTransactionsV3Response`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 408 | Request timeout |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int64"; example: 74 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page | format: "int64"; example: 20 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int64"; example: 10 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page number | default: 1; format: "int64"; example: 1 |
| `tax` | object (schema `RelatedFees`) | no | The related fees available to operation |  |
| `items` | array of object | no | Merchants transactions |  |
| `items[].id` | integer (schema `MerchantTransactionID`) | no | Merchant transaction ID | format: "int64"; example: 1 |
| `items[].type` | string | no | Transaction type | example: "SALES" |
| `items[].number_of_installments` | integer (schema `NumberOfInstallments`) | no | Number of installments | format: "int64"; example: 3 |
| `items[].installment` | integer (schema `InstallmentNumber`) | no | Installment number of transaction | format: "int64"; example: 2 |
| `items[].gross_value` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `items[].net_value` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |
| `items[].discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `items[].operation_type` | integer (schema `OperationType`) | no | Operation type ID | format: "int64"; example: 89 |
| `items[].operation` | string (schema `OperationName`) | no | Operation name | example: "Credit card without quotas" |
| `items[].event_date` | string (schema `TransactionEventDate`) | no | The transaction event date and time (sale or refund). UTC date/time - format: yyyy-MM-ddThh:mm:ssZ | format: "datetime"; example: "2020-07-14T00:41:29Z" |
| `items[].payment_date` | string (schema `ScheduledPaymentDate`) | no | Scheduled payment date. Format = yyyy-mm-dd. | format: "date"; example: "2020-04-20" |
| `items[].receipt_date` | string (schema `MerchantTransactionSettlementDate`) | no | Date of merchant transaction settlement. Format = yyyy-mm-dd. | format: "date"; example: "2020-07-16T00:00:00.000Z" |
| `items[].received_value` | number (schema `TransactionAmountSettled`) | no | Transaction amount settled | format: "float"; example: 0.1 |
| `items[].status` | string (schema `MerchantTransactionStatus`) | no | Merchant transaction status | enum: ["PENDING", "SCHEDULED", "BLOCKED", "SETTLED", "PAID", "ADVANCED", "CANCELED", "RETURNED", "WAITING_SPLIT", "SPLITTED"] |
| `items[].meta` | array of object (schema `TransactionMetadata`) | no | Metadata. The accepted parameters are `MarketplaceAuthorization` and `MarketplaceTransaction`. | example: [{"name": "MarketplaceAuthorization", "value": "ashga-jwjh-huahu-wquiqw"}, {"name": "MarketplaceTransaction", "value": "wquiqw-jwjh-huahu-ashga"}] |
| `items[].meta[].name` | string | no |  | example: "any value" |
| `items[].meta[].value` | string | no |  | example: "any value" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;408;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-SELL-seller-marketplace-implementation-steps`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v2/merchants/{merchantId}/transactions/{merchantTransactionId} operationId=getMerchantTransactionV2 -->
### `GET /v2/merchants/{merchantId}/transactions/{merchantTransactionId}` — Get merchant transaction

- **operationId:** `getMerchantTransactionV2`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get transaction details using merchant transaction ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `merchantTransactionId` | path | yes | integer | Merchant Transaction ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETMerchantTransactionResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 404 | The specified resource was not found |  |
| 408 | Request timeout |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MerchantTransactionID`) | no | Merchant transaction ID | format: "int64"; example: 1 |
| `authorization_id` | string (schema `AuthorizationID`) | no | Authorization ID | example: "13387693" |
| `parent_authorization_id` | string (schema `ParentAuthorizationID`) | no | Parent authorization ID | example: "13387682" |
| `type` | string (schema `TransactionType`) | no | Transaction type. Examples of transaction types include cash-in and cash-out.<br>See <a href="https://developers.pismo.io/pismo-docs/docs/transactions-overview#transaction-types">Transaction types</a> for the list of transaction types<br>on the Pismo platform.<br> | example: "SALES" |
| `status` | string (schema `TransactionStatus`) | no | Transaction status | enum: ["PENDING", "SCHEDULED", "BLOCKED", "SETTLED", "PAID", "ADVANCED", "CANCELED", "RETURNED"]; example: "SCHEDULED" |
| `merchant_id` | integer (schema `MerchantID`) | no | Merchant ID | format: "int64"; example: 1 |
| `org_operation_id` | integer (schema `OrgOperationID`) | no | Processing code. See <a href="https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types" target="_blank">Processing codes and transaction types</a>. | format: "int64"; example: 1 |
| `creditor_id` | integer (schema `CreditorID`) | no | Creditor ID | format: "int64"; example: 1 |
| `installment` | integer (schema `InstallmentNumber`) | no | Installment number of transaction | format: "int64"; example: 2 |
| `number_of_installments` | integer (schema `NumberOfInstallments`) | no | Number of installments | format: "int64"; example: 3 |
| `amount` | number (schema `TransactionTotalDouble`) | no | Transaction total (gross) amount | format: "double" |
| `mdr_amount` | number (schema `MDRamount`) | no | Merchant discount rate (MDR) amount | format: "double"; example: 5.5 |
| `mdr_tax` | number (schema `MDRtax`) | no | Merchant discount rate (MDR) tax amount | format: "double" |
| `transaction_fee` | number (schema `TransactionFee`) | no | Fixed transaction fee | format: "double"; example: 1 |
| `mdr_without_fee` | number (schema `MDRwithoutFee`) | no | Merchant discount rate (MDR) minus transaction fee | example: 1 |
| `advancement_discount` | number (schema `AdvancementDiscount`) | no | Advancement discount | format: "double" |
| `advanced_amount` | number (schema `AdvancementAmountDouble`) | no | Advanced amount | format: "double" |
| `event_date` | string (schema `TransactionEventDate`) | no | The transaction event date and time (sale or refund). UTC date/time - format: yyyy-MM-ddThh:mm:ssZ | format: "datetime"; example: "2020-07-14T00:41:29Z" |
| `scheduled_payment_date` | string (schema `ScheduledPaymentDate`) | no | Scheduled payment date. Format = yyyy-mm-dd. | format: "date"; example: "2020-04-20" |
| `origin_transaction_id` | integer (schema `OriginTransactionID`) | no | ID of parent merchant transaction. If sale, this is null. If refund, this is the transaction ID of the sale. | format: "int64"; example: 1 |
| `marketplace_id` | integer (schema `MarketplaceID`) | no | Marketplace ID | format: "int64"; example: 1 |
| `discount_amount` | number (schema `DiscountAmount`) | no | Total discount amount applied to the transaction | format: "double"; example: 1.99 |
| `discount_details` | array of object (schema `DiscountDetail`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;408;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants/{merchantId}/transactions/tax operationId=listMerchantTaxes -->
### `GET /v1/merchants/{merchantId}/transactions/tax` — List merchant taxes

- **operationId:** `listMerchantTaxes`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List taxes for merchant by merchant ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETTransactionTaxResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `mdr` | array of object (schema `MDRobject`) | no | Array of fees |  |
| `mdr[].description` | string (schema `OperationTypeDescription`) | no | Operation type description | example: "In one lump sum" |
| `mdr[].mdr` | number (schema `MDRnumber`) | no | Merchant discount rate (MDR) | format: "float"; example: 0.03 |
| `mdr[].days_to_payment` | integer (schema `DaysToPayment`) | no | Number of days before the first payment | format: "int64"; example: 30 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants/{merchantId}/transactions-totals operationId=getTransactionsSummary -->
### `GET /v1/merchants/{merchantId}/transactions-totals` — Get transactions summary

- **operationId:** `getTransactionsSummary`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a summary of a merchant's transactions.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `startPaymentDate` | query | no | string | Scheduled payment start date. Find scheduled payments between this date and `endPaymentDate`. Format = yyyy-mm-dd. | format: "date"; example: "2020-01-01" |
| `endPaymentDate` | query | no | string | Scheduled payment end date. Format = yyyy-mm-dd. Find scheduled payments between `startPaymentDate` and this date. | format: "date"; example: "2020-01-02" |
| `marketplace` | query | no | integer | Marketplace ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETTransactionsTotalsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pending` | object | no |  |  |
| `pending.gross` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `pending.discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `pending.net` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |
| `pending.unblocked` | object (schema `TotalAmountBlockedOrUnblocked`) | no |  |  |
| `pending.blocked` | object (schema `TotalAmountBlockedOrUnblocked`) | no |  |  |
| `scheduled` | object | no |  |  |
| `scheduled.gross` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `scheduled.discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `scheduled.net` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |
| `scheduled.unblocked` | object (schema `TotalAmountBlockedOrUnblocked`) | no |  |  |
| `scheduled.blocked` | object (schema `TotalAmountBlockedOrUnblocked`) | no |  |  |
| `settled` | object | no |  |  |
| `settled.gross` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `settled.discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `settled.net` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |
| `settled.unblocked` | object (schema `TotalAmountBlockedOrUnblocked`) | no |  |  |
| `settled.blocked` | object (schema `TotalAmountBlockedOrUnblocked`) | no |  |  |
| `all` | object | no |  |  |
| `all.gross` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `all.discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `all.net` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |
| `all.unblocked` | object (schema `TotalAmountBlockedOrUnblocked`) | no |  |  |
| `all.blocked` | object (schema `TotalAmountBlockedOrUnblocked`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v2/merchants/{merchantId}/transactions-totals operationId=getTransactionsSummaryV2 -->
### `GET /v2/merchants/{merchantId}/transactions-totals` — Get transactions summary [beta]

- **operationId:** `getTransactionsSummaryV2`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Returns the transactions totals summarized by status and/or date.
> When the `groupBy` is provided with the values `date` or `dateAndStatus` the date range between `startPaymentDate` and `endPaymentDate` must not exceed 30 days.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `startPaymentDate` | query | yes | string | Initial scheduled payment date used to filter the transactions. Format yyyy-mm-dd.<br>Finds scheduled payments between this date and `endPaymentDate`.<br> | format: "date"; example: "2020-01-01" |
| `endPaymentDate` | query | yes | string | Final scheduled payment date used to filter the transactions. Format yyyy-mm-dd.<br>Finds scheduled payments between `startPaymentDate` and this date.<br> | format: "date"; example: "2020-01-02" |
| `marketplaceId` | query | no | integer | Marketplace ID used as filter. When provided, it returns the values of the transactions belonging only to the marketplace.<br>When not provided, it returns the values of all transactions for the provided Merchant ID.<br> | format: "int64"; example: 12 |
| `status` | query | no | string | Transaction status used as a filter. When provided, it returns the values of the transactions matching this status. | example: "SCHEDULED" |
| `groupBy` | query | no | string | Group the returned entries by this criteria. The default value is `status`.<br>- For the `status` value, returns one item per different status in the response.<br>- For the `date` value, returns one item per day between the `startPaymentDate` and `endPaymentDate` that have transaction values for the filters. The response is ordered by day in ascending order.<br>- For the `dateAndStatus` value, returns one item per day and status. The response is ordered by day and status in ascending order.<br> | enum: ["status", "date", "dateAndStatus"]; example: "status" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETTransactionsTotalsV2Response`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object | no |  |  |
| `items[].gross_amount` | string | no | Gross amount | format: "float" |
| `items[].discount_amount` | string | no | Discount amount | format: "float" |
| `items[].net_amount` | string | no | Net amount (Gross amount - Discount amount) | format: "float" |
| `items[].status` | string | no | Transactions status. Returned only if the `groupBy` filter is `status` or `dateAndStatus`<br> |  |
| `items[].scheduled_payment_date` | string | no | Transactions scheduled payment date. Returned only if the `groupBy` filter is `date` or `dateAndStatus`. Format = yyyy-mm-dd.<br> | format: "date" |
| `totals` | object (schema `TransactionTotalAmountV2`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v3/merchants/{merchantId}/transactions-types operationId=getReportForMerchantTransactionTypesV3 -->
### `GET /v3/merchants/{merchantId}/transactions-types` — Get transaction types

- **operationId:** `getReportForMerchantTransactionTypesV3`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get transactions types.
>
> Examples of transaction types include cash-in and cash-out. See <a href="https://developers.pismo.io/pismo-docs/docs/transactions-overview#transaction-types">Transaction types</a> for the list of transaction types on the Pismo platform.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `paymentDate` | query | no | string | Payment date. Format = yyyy-mm-dd. | format: "date"; example: "2018-03-29" |
| `marketplace` | query | no | integer | Marketplace ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `GETTransactionTypesResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants/{merchantId}/transactions/{transactionId} operationId=getTransactionDetails -->
### `GET /v1/merchants/{merchantId}/transactions/{transactionId}` — Get transaction details (deprecated)

- **operationId:** `getTransactionDetails`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get details for specific transaction

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `transactionId` | path | yes | integer | Transaction ID | format: "int64"; example: 123 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETMerchantTransactionDetailsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_auth_id` | integer (schema `TransactionAuthorizationID`) | no | Transaction authorization ID | format: "int64"; example: 992009 |
| `card` | object (schema `Card`) | no |  |  |
| `total` | number (schema `TransactionTotalAmount`) | no | Transaction total amount | format: "int64"; example: 21480 |
| `date` | string (schema `TransactionAuthorizationDate`) | no | The date and time that a transaction is authorized. UTC date/time - format: yyyy-MM-ddThh:mm:ssZ | format: "datetime"; example: "2020-06-23T22:29:49Z" |
| `email` | string (schema `CustomerEmailAddress`) | no | Customer email | format: "email"; example: "johndoe@gmail.com" |
| `name` | string (schema `CustomerName`) | no | Customer name | example: "MARIA JOSE" |
| `installments` | integer (schema `NumberOfInstallments`) | no | Number of installments | format: "int64"; example: 3 |
| `authorization_code` | number (schema `AuthorizationCode`) | no | Authorization ID | example: 992009 |
| `account_id` | integer (schema `PismoAccountID`) | no | Pismo account ID | format: "int64"; example: 8675309 |
| `merchant` | object (schema `Merchant`) | no |  |  |
| `items` | array of object | no |  |  |
| `items[].id` | integer (schema `ItemID`) | no | Item ID | example: 10452 |
| `items[].code` | string (schema `ItemCode`) | no | Item Code | example: "40316017" |
| `items[].price` | number (schema `ItemPrice`) | no | Item Price | example: 49.5 |
| `items[].description` | string (schema `ItemDescription`) | no | Item description | example: "Widget number one" |
| `items[].amount` | integer (schema `ItemAmount`) | no | Number of items | format: "int64"; example: 5 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=PATCH path=/v1/merchants/{merchantId}/transactions/{transactionId} operationId=updateTransactionStatus -->
### `PATCH /v1/merchants/{merchantId}/transactions/{transactionId}` — Update transaction status

- **operationId:** `updateTransactionStatus`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant transaction`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update transaction status.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `transactionId` | path | yes | integer | Transaction ID | format: "int64"; example: 123 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `PATCHTransactionRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `TransactionStatus`) | no | Transaction status | enum: ["PENDING", "SCHEDULED", "BLOCKED", "SETTLED", "PAID", "ADVANCED", "CANCELED", "RETURNED"]; example: "SCHEDULED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/RelatedFees -->
### Schema `RelatedFees`

Pointer: `#/components/schemas/RelatedFees`. Type: object (schema `RelatedFees`).

> The related fees available to operation

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `mdr` | array of object (schema `MDRobject`) | no | Array of fees |  |
| `mdr[].description` | string (schema `OperationTypeDescription`) | no | Operation type description | example: "In one lump sum" |
| `mdr[].mdr` | number (schema `MDRnumber`) | no | Merchant discount rate (MDR) | format: "float"; example: 0.03 |
| `mdr[].days_to_payment` | integer (schema `DaysToPayment`) | no | Number of days before the first payment | format: "int64"; example: 30 |

<!-- schema: #/components/schemas/DiscountDetail -->
### Schema `DiscountDetail`

Pointer: `#/components/schemas/DiscountDetail`. Type: object (schema `DiscountDetail`).

> Discount description. The `amount` represents the fee applied—that is, the amount discounted before settlement.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | Discount name | example: "EMISSION_FEE" |
| `amount` | number | no | Total discount amount | format: "double"; example: 10 |

<!-- schema: #/components/schemas/TotalAmountBlockedOrUnblocked -->
### Schema `TotalAmountBlockedOrUnblocked`

Pointer: `#/components/schemas/TotalAmountBlockedOrUnblocked`. Type: object (schema `TotalAmountBlockedOrUnblocked`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `gross` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `net` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |

<!-- schema: #/components/schemas/TransactionTotalAmountV2 -->
### Schema `TransactionTotalAmountV2`

Pointer: `#/components/schemas/TransactionTotalAmountV2`. Type: object (schema `TransactionTotalAmountV2`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `gross_amount` | string | no | Gross amount | format: "float" |
| `discount_amount` | string | no | Discount amount | format: "float" |
| `net_amount` | string | no | Net amount (Gross amount - Discount amount) | format: "float" |

<!-- schema: #/components/schemas/Card -->
### Schema `Card`

Pointer: `#/components/schemas/Card`. Type: object (schema `Card`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `first_four_digits` | integer (schema `FirstFourDigitsOfCard`) | no | First four digits of credit card | format: "int64"; example: 1234 |
| `last_four_digits` | integer (schema `LastFourDigitsOfCard`) | no | Last four digits of credit card | format: "int64"; example: 6789 |

<!-- schema: #/components/schemas/Merchant -->
### Schema `Merchant`

Pointer: `#/components/schemas/Merchant`. Type: object (schema `Merchant`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `MerchantName`) | no | Merchant name | minLength: 1; maxLength: 100; example: "Acme Store" |
| `email` | string (schema `EmailAddress`) | no | Email address | example: "test@acmecorp.com" |

## Lifecycle status

- `GET /v1/merchants/{merchantId}/transactions/{transactionId}` (`getTransactionDetails`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Merchants.yaml` | tag `Merchant transaction`: GET /v3/merchants/{merchantId}/operations, GET /v2/merchants/{merchantId}/transactions, GET /v3/merchants/{merchantId}/transactions, GET /v2/merchants/{merchantId}/transactions/{merchantTransactionId}, GET /v1/merchants/{merchantId}/transactions/tax, GET /v1/merchants/{merchantId}/transactions-totals, GET /v2/merchants/{merchantId}/transactions-totals, GET /v3/merchants/{merchantId}/transactions-types, GET /v1/merchants/{merchantId}/transactions/{transactionId}, PATCH /v1/merchants/{merchantId}/transactions/{transactionId} | https://github.com/PismoDevEx/pismo-api-specs | `ebc9f3fadda7001c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
