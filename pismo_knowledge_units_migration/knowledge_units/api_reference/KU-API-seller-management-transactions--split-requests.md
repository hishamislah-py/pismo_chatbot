---
ku_id: KU-API-seller-management-transactions--split-requests
title: 'API reference: Seller management - Transactions — Split requests'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Transactions.yaml
  sha256: f064908196c8f7cdd21e34e27572c6f95f92f3503251232b87c3d12d769ca000
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- post-split-request
- cancel-split-request
- get-split-requests
- get-split-details
- get-sale-split-request-totals
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-merchants
- KU-SELL-managing-merchant-transactions
specification_version: 1.0.0
---

# API reference: Seller management - Transactions — Split requests

**KU ID:** `KU-API-seller-management-transactions--split-requests` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Split requests` in `api-specs/Seller_management_-_Transactions.yaml` (“Seller management - Transactions”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for managing split requests

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/transactions/{merchantTransactionId}/split` | `post-split-request` | Create split request | no |
| `POST /v1/transactions/{merchantTransactionId}/split/cancel` | `cancel-split-request` | Cancel split request | no |
| `GET /v1/marketplaces/{marketplaceId}/split-requests` | `get-split-requests` | List split requests | no |
| `GET /v1/marketplaces/{marketplaceId}/split-requests/{splitId}` | `get-split-details` | Get split request details | no |
| `GET /v1/marketplaces/{marketplaceId}/split-requests/{parentId}/totals` | `get-sale-split-request-totals` | Get split request totals | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Transactions.yaml method=POST path=/v1/transactions/{merchantTransactionId}/split operationId=post-split-request -->
### `POST /v1/transactions/{merchantTransactionId}/split` — Create split request

- **operationId:** `post-split-request`
- **Specification:** `api-specs/Seller_management_-_Transactions.yaml` (Seller management - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Split requests`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Create a new split request for a merchant transaction.<br>
> Managing financial transactions often requires dividing a single transaction into multiple parts for accurate record-keeping and reporting. The split transaction feature addresses this need by allowing you to split a transaction into different categories or assign portions to various accounts. This functionality is particularly useful for handling shared expenses, allocating costs across different budget categories, or separating business and personal expenses.
> When a split request is created, it's created with a `PENDING` status. Before you request a split, make sure the merchant transaction is already in the `WAITING_SPLIT` status.<br>
> This endpoint generates a [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>" |
| `merchantTransactionId` | path | yes | integer | Merchant transaction ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `SplitRequestPostSaleRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `event_date` | string (schema `EventDate`) | yes | Event datetime. The datetime format follows the ISO 8601 format (UTC). | format: "datetime"; example: "2023-01-01T12:00:00Z" |
| `installments` | integer (schema `Installments`) | yes | Number of installments | format: "int32"; minimum: 1; maximum: 2147483647; example: 1 |
| `processing_code` | string (schema `ProcessingCode`) | yes | Processing code.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "999999" |
| `definitions` | array of object (schema `SplitRequestPostSaleDefinitionsRequest`) | yes | Determines how the transaction amount is split among merchants and specifies the applicable taxes and discounts. `definitions` defines the number of merchants involved in the transaction, amount of tax or discount to apply, and the percentage or amount allocated to each merchant. <br> |  |

Example `split-request-post` (Split request post request) — from `#/components/examples/SplitRequestPostSaleRequest`:

```json
{
  "event_date": "2023-01-01T12:00:00Z",
  "installments": 1,
  "processing_code": "999999",
  "definitions": [
    {
      "merchant_id": 2,
      "amount_percentage": 0.25
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Successfully create split requests | `application/json`: object (schema `SplitRequestPostResponse`) |
| 400 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Marketplace ID | format: "uint64" |

202 Example `Create split request` (Split request post response) — from `#/components/examples/SplitRequestPostResponse`:

```json
{
  "id": 1
}
```

##### Response 400

400 Example `400 Bad request` (Bad request response) — from `#/components/examples/DefaultErrorResponse`:

```json
{
  "code": "ESMT0001",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `Internal server error` (Internal Server Error Response) — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMT0001` | Failed during validation of request payload |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-merchant-transaction-created-1` | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-SELL-managing-merchant-transactions`.

<!-- op: spec=api-specs/Seller_management_-_Transactions.yaml method=POST path=/v1/transactions/{merchantTransactionId}/split/cancel operationId=cancel-split-request -->
### `POST /v1/transactions/{merchantTransactionId}/split/cancel` — Cancel split request

- **operationId:** `cancel-split-request`
- **Specification:** `api-specs/Seller_management_-_Transactions.yaml` (Seller management - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Split requests`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Cancel a merchant transaction split request.<br>
> This endpoint generates a [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>" |
| `merchantTransactionId` | path | yes | integer | Merchant transaction ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `SplitRequestPostCancelRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `event_date` | string (schema `EventDate`) | yes | Event datetime. The datetime format follows the ISO 8601 format (UTC). | format: "datetime"; example: "2023-01-01T12:00:00Z" |
| `installments` | integer (schema `Installments`) | no | Number of installments | format: "int32"; minimum: 1; maximum: 2147483647; example: 1 |
| `processing_code` | string (schema `ProcessingCode`) | yes | Processing code.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "999999" |
| `definitions` | array of object (schema `SplitRequestPostCancelDefinitionsRequest`) | no | Determines how the transaction amount is split among merchants and specify the applicable taxes and discounts. `definitions` defines the number of merchants involved in the transaction, amount of tax or discount to apply, and the percentage or amount allocated to each merchant.<br><br>If you cancel a split request without specifying any values in the object, the amounts split among all merchants are canceled.<br> |  |

Example `split-request-post` (Split request cancel request) — from `#/components/examples/SplitRequestPostCancelRequest`:

```json
{
  "event_date": "2023-01-01T12:00:00Z",
  "installments": 1,
  "processing_code": "999999",
  "definitions": [
    {
      "merchant_id": 2,
      "amount": 100
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Successfully canceled split requests | `application/json`: object (schema `SplitRequestPostResponse`) |
| 400 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Marketplace ID | format: "uint64" |

202 Example `Cancel split request` (Split request post response) — from `#/components/examples/SplitRequestPostResponse`:

```json
{
  "id": 1
}
```

##### Response 400

400 Example `400 Bad request` (Bad request response) — from `#/components/examples/DefaultErrorResponse`:

```json
{
  "code": "ESMT0001",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `Internal server error` (Internal Server Error Response) — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMT0001` | Failed during validation of request payload |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-merchant-transaction-created-1` | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-SELL-managing-merchant-transactions`.

<!-- op: spec=api-specs/Seller_management_-_Transactions.yaml method=GET path=/v1/marketplaces/{marketplaceId}/split-requests operationId=get-split-requests -->
### `GET /v1/marketplaces/{marketplaceId}/split-requests` — List split requests

- **operationId:** `get-split-requests`
- **Specification:** `api-specs/Seller_management_-_Transactions.yaml` (Seller management - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Split requests`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> List split requests for a given marketplace.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>" |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `page` | query | no | integer | Page number of the returned split request list.<br>When this value is not provided, it defaults to 1.<br> | format: "int32"; minimum: 1; maximum: 2147483647; example: 1 |
| `perPage` | query | no | integer | Number of rows per page.<br>When this value is not provided, it defaults to 10.<br> | format: "int32"; minimum: 1; maximum: 2147483647; example: 1 |
| `startDate` | query | no | string | The start date of the split requests. Format is ISO 8601.<br>minLength: 10<br>maxLength: 10<br> | format: "date"; example: "2023-10-05T00:00:00.000Z" |
| `endDate` | query | no | string | The end date of the split requests. The date format used is ISO 8601.<br>minLength: 10<br>maxLength: 10<br> | format: "date"; example: "2023-10-30T00:00:00.000Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successfully list split requests | `application/json`: object (schema `SplitRequestListResponse`) |
| 400 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `SplitRequestListItemResponse`) | no |  |  |
| `page` | integer (schema `SplitRequestPageNumber`) | no | Page number | format: "int64" |
| `per_page` | integer (schema `SplitRequestPerPage`) | no | Number of items per page | format: "int64" |
| `has_next` | boolean (schema `SplitRequestHasNextPage`) | no | Is there a next page?<br> |  |

200 Example `List split request success` (Split request list response) — from `#/components/examples/SplitRequestListResponse`:

```json
{
  "items": [
    {
      "id": 1,
      "parent_id": null,
      "marketplace_id": 1,
      "merchant_transaction_id": 12345,
      "amount": 100,
      "currency_code": "BRL",
      "event_date": "2023-01-01T12:00:00Z",
      "processing_code": "999999",
      "type": "SALES",
      "status": "PENDING",
      "message": ""
    }
  ],
  "page": 1,
  "per_page": 10,
  "has_next": false
}
```

##### Response 400

400 Example `400 Bad request` (Bad request response) — from `#/components/examples/DefaultErrorResponse`:

```json
{
  "code": "ESMT0001",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `Internal server error` (Internal Server Error Response) — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMT0001` | Failed during validation of request payload |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Transactions.yaml method=GET path=/v1/marketplaces/{marketplaceId}/split-requests/{splitId} operationId=get-split-details -->
### `GET /v1/marketplaces/{marketplaceId}/split-requests/{splitId}` — Get split request details

- **operationId:** `get-split-details`
- **Specification:** `api-specs/Seller_management_-_Transactions.yaml` (Seller management - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Split requests`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get the details of a specific split request in a marketplace.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>" |
| `splitId` | path | yes | integer | Split request ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successfully get split request totals | `application/json`: object (schema `SplitRequestGetResponse`) |
| 400 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `SplitRequestId`) | no | Split request ID | format: "int64" |
| `event_date` | string (schema `EventDate`) | no | Event datetime. The datetime format follows the ISO 8601 format (UTC). | format: "datetime"; example: "2023-01-01T12:00:00Z" |
| `amount` | number (schema `SplitRequestAmount`) | no | Split request amount | format: "float" |
| `currency_code` | string (schema `CurrencyCodeResponse`) | no | ISO-4217 alphabetic (3 characters) currency code<br> | example: "BRL" |
| `installments` | integer (schema `Installments`) | no | Number of installments | format: "int32"; minimum: 1; maximum: 2147483647; example: 1 |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "999999" |
| `merchant_transaction_id` | integer (schema `MerchTransId`) | no | Merchant transaction identifier | format: "int64" |
| `marketplace_id` | integer (schema `MarketplaceId`) | no | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `parent_id` | integer (schema `ParentId`) | no | Parent ID assigned to the child split request<br> | format: "int64"; nullable: true |
| `type` | string (schema `SplitRequestType`) | no | Split request type | enum: ["SALES", "CANCELLATION"] |
| `status` | string (schema `SplitRequestStatus`) | no | Split request status | enum: ["PENDING", "PROCESSED", "ERROR"] |
| `message` | string (schema `SplitRequestMessage`) | no | Message associated with the split request | nullable: true |
| `definitions` | array of object (schema `SplitRequestGetDefinitionsResponse`) | no | Determines how the transaction amount is split among merchants and specifies the applicable taxes and discounts. `definitions` defines the number of merchants involved in the transaction, amount of tax or discount to apply, and the percentage or amount allocated to each merchant. |  |

200 Example `Get split request details` (Split request get response) — from `#/components/examples/SplitRequestGetResponse`:

```json
{
  "id": 1,
  "event_date": "2023-01-01T12:00:00Z",
  "amount": 100,
  "currency_code": "BRL",
  "installments": 1,
  "processing_code": "999999",
  "merchant_transaction_id": 12345,
  "marketplace_id": 1,
  "parent_id": null,
  "type": "SALES",
  "status": "PENDING",
  "message": "",
  "definitions": [
    {
      "merchant_id": 2,
      "transactions_status": "SCHEDULED",
      "processing_code": "999999",
      "total_amount": 100,
      "merchant_transactions_ids": [
        1,
        2,
        3
      ]
    }
  ]
}
```

##### Response 400

400 Example `400 Bad request` (Bad request response) — from `#/components/examples/DefaultErrorResponse`:

```json
{
  "code": "ESMT0001",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `Internal server error` (Internal Server Error Response) — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMT0001` | Failed during validation of request payload |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Transactions.yaml method=GET path=/v1/marketplaces/{marketplaceId}/split-requests/{parentId}/totals operationId=get-sale-split-request-totals -->
### `GET /v1/marketplaces/{marketplaceId}/split-requests/{parentId}/totals` — Get split request totals

- **operationId:** `get-sale-split-request-totals`
- **Specification:** `api-specs/Seller_management_-_Transactions.yaml` (Seller management - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Split requests`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Get the total amount for a specific split request in a marketplace.<br>
> This endpoint returns the gross amount for a specific parent split request with the `PROCESSED` status. It also return the gross amount for each participating merchant, as well as marketplace merchants.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>" |
| `parentId` | path | yes | integer | Parent split request ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successfully get split request totals | `application/json`: object (schema `SplitRequestGetTotalsResponse`) |
| 400 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `SplitRequestGetTotalGrossAmount`) | no | The gross amount of all split requests using `splitId` and `parentId` as reference | format: "float" |
| `currency_code` | string (schema `OptionalCurrencyCodeResponse`) | no | ISO 4217 alphanumeric currency code. `null` when no currency is recorded. | nullable: true; example: "BRL" |
| `marketplace_id` | integer (schema `MarketplaceId`) | no | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `definitions` | array of object (schema `SplitRequestGetTotalsDefinitionsResponse`) | no | Determines how the transaction amount is split among merchants and specify the applicable taxes and discounts. `definitions` defines the number of merchants involved in the transaction, amount of tax or discount to apply, and the percentage or amount allocated to each merchant. |  |

200 Example `Get split request totals` (Split request totals response) — from `#/components/examples/SplitRequestGetTotalsResponse`:

```json
{
  "amount": 100,
  "currency_code": "BRL",
  "marketplace_id": 2,
  "definitions": [
    {
      "merchant_id": 2,
      "amount": 100,
      "merchant_transactions_ids": [
        1,
        2,
        3
      ]
    }
  ]
}
```

##### Response 400

400 Example `400 Bad request` (Bad request response) — from `#/components/examples/DefaultErrorResponse`:

```json
{
  "code": "ESMT0001",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `Internal server error` (Internal Server Error Response) — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMT0001` | Failed during validation of request payload |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-SELL-managing-merchant-transactions`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SplitRequestPostSaleDefinitionsRequest -->
### Schema `SplitRequestPostSaleDefinitionsRequest`

Pointer: `#/components/schemas/SplitRequestPostSaleDefinitionsRequest`. Type: object (schema `SplitRequestPostSaleDefinitionsRequest`).

> Defines how a transaction is split for a merchant.
> Exactly one allocation method, `amount` or `amount_percentage`, must be provided.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `merchant_id` | integer (schema `MerchantId`) | yes | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `amount` | number (schema `SplitRequestPostSaleDefinitionsTotalAmount`) | no | Merchant's requested amount<br>If the sum of all defined amounts is less than the authorized amount, the difference is applied to the first merchant in the list.<br>Either `amount` or `amount_percentage` is **REQUIRED**.<br>Example:<br>  - Amount: 100.00<br>- Amounts: [ 10.00, 20.00, 30.00 ]<br>  - Adjusted Amounts: [ 50.00, 20.00, 30.00 ]<br> | format: "float"; example: 100 |
| `amount_percentage` | number (schema `SplitRequestPostSaleDefinitionsTotalAmountPercentage`) | no | Percentage of the gross amount of the merchant transactions. 10% is 0.10, 100% is 1.00<br>Either `amount` or `amount_percentage` is **REQUIRED**.<br> | format: "float"; example: 0.25 |
| `processing_code` | string (schema `MerchTransProcessingCode`) | no | Merchant transaction processing code | nullable: true; example: "999999" |
| `transaction_status` | string (schema `SplitMerchTransactionsStatus`) | no | Merchant transaction status | enum: ["PENDING", "SCHEDULED", "SETTLED", "CANCELED"]; nullable: true; example: "SCHEDULED" |

<!-- schema: #/components/schemas/DefaultErrorResponse -->
### Schema `DefaultErrorResponse`

Pointer: `#/components/schemas/DefaultErrorResponse`. Type: object (schema `DefaultErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Pismo internal error code |  |
| `message` | string (schema `ErrorMessage`) | no | Error message |  |
| `details` | object (schema `ErrorDetails`) | no | If necessary, this field shows which fields failed validation |  |

<!-- schema: #/components/schemas/InternalServerErrorResponse -->
### Schema `InternalServerErrorResponse`

Pointer: `#/components/schemas/InternalServerErrorResponse`. Type: object (schema `InternalServerErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string (schema `InternalServerErrorMessage`) | no | Internal server error |  |

<!-- schema: #/components/schemas/SplitRequestPostCancelDefinitionsRequest -->
### Schema `SplitRequestPostCancelDefinitionsRequest`

Pointer: `#/components/schemas/SplitRequestPostCancelDefinitionsRequest`. Type: object (schema `SplitRequestPostCancelDefinitionsRequest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `merchant_id` | integer (schema `MerchantId`) | yes | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `amount` | number | no | Requested amount of the merchant.<br>If the amount is null, the amount is calculated using the proportion of the amount from each merchant.<br> | format: "float"; nullable: true; example: 100 |
| `processing_code` | string (schema `MerchTransProcessingCode`) | no | Merchant transaction processing code | nullable: true; example: "999999" |

<!-- schema: #/components/schemas/SplitRequestListItemResponse -->
### Schema `SplitRequestListItemResponse`

Pointer: `#/components/schemas/SplitRequestListItemResponse`. Type: object (schema `SplitRequestListItemResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `SplitRequestId`) | no | Split request ID | format: "int64" |
| `parent_id` | integer (schema `ParentId`) | no | Parent ID assigned to the child split request<br> | format: "int64"; nullable: true |
| `marketplace_id` | integer (schema `MarketplaceId`) | no | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `merchant_transaction_id` | integer (schema `MerchTransId`) | no | Merchant transaction identifier | format: "int64" |
| `amount` | number (schema `SplitRequestAmount`) | no | Split request amount | format: "float" |
| `currency_code` | string (schema `CurrencyCodeResponse`) | no | ISO-4217 alphabetic (3 characters) currency code<br> | example: "BRL" |
| `event_date` | string (schema `EventDate`) | no | Event datetime. The datetime format follows the ISO 8601 format (UTC). | format: "datetime"; example: "2023-01-01T12:00:00Z" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "999999" |
| `type` | string (schema `SplitRequestType`) | no | Split request type | enum: ["SALES", "CANCELLATION"] |
| `status` | string (schema `SplitRequestStatus`) | no | Split request status | enum: ["PENDING", "PROCESSED", "ERROR"] |
| `message` | string (schema `SplitRequestMessage`) | no | Message associated with the split request | nullable: true |

<!-- schema: #/components/schemas/SplitRequestGetDefinitionsResponse -->
### Schema `SplitRequestGetDefinitionsResponse`

Pointer: `#/components/schemas/SplitRequestGetDefinitionsResponse`. Type: object (schema `SplitRequestGetDefinitionsResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `merchant_id` | integer (schema `MerchantId`) | no | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `transaction_status` | string (schema `SplitMerchTransactionsStatus`) | no | Merchant transaction status | enum: ["PENDING", "SCHEDULED", "SETTLED", "CANCELED"]; nullable: true; example: "SCHEDULED" |
| `processing_code` | string (schema `MerchTransProcessingCode`) | no | Merchant transaction processing code | nullable: true; example: "999999" |
| `total_amount` | number (schema `SplitRequestTotalAmount`) | no | Gross amount of the merchant transactions | format: "float" |
| `merchant_transactions_ids` | array of integer (schema `SplitRequestMerchTransId`) | no |  | items.format: "uint64" |

<!-- schema: #/components/schemas/SplitRequestGetTotalsDefinitionsResponse -->
### Schema `SplitRequestGetTotalsDefinitionsResponse`

Pointer: `#/components/schemas/SplitRequestGetTotalsDefinitionsResponse`. Type: object (schema `SplitRequestGetTotalsDefinitionsResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `merchant_id` | integer (schema `MerchantId`) | no | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `amount` | number (schema `SplitRequestGrossAmount`) | no | Gross amount of the merchant transaction | format: "float" |
| `merchant_transactions_ids` | array of integer (schema `SplitRequestMerchTransId`) | no |  | items.format: "uint64" |

<!-- schema: #/components/schemas/ErrorDetails -->
### Schema `ErrorDetails`

Pointer: `#/components/schemas/ErrorDetails`. Type: object (schema `ErrorDetails`).

> If necessary, this field shows which fields failed validation

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payload` | array of object | no | Array of fields with error |  |
| `payload[].field` | string (schema `ErrorField`) | no | Name of field with error |  |
| `payload[].message` | string (schema `ErrorFieldMessage`) | no | Error Message referring to the field |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Transactions.yaml` | tag `Split requests`: POST /v1/transactions/{merchantTransactionId}/split, POST /v1/transactions/{merchantTransactionId}/split/cancel, GET /v1/marketplaces/{marketplaceId}/split-requests, GET /v1/marketplaces/{marketplaceId}/split-requests/{splitId}, GET /v1/marketplaces/{marketplaceId}/split-requests/{parentId}/totals | https://github.com/PismoDevEx/pismo-api-specs | `f064908196c8f7cd…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
