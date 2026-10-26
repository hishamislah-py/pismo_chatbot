---
ku_id: KU-API-seller-management-transactions--merchant-transactions
title: 'API reference: Seller management - Transactions — Merchant transactions'
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
- post-merchant-transaction-sale
- post-merchant-transaction-cancel
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-merchants
- KU-SELL-managing-merchant-transactions
specification_version: 1.0.0
---

# API reference: Seller management - Transactions — Merchant transactions

**KU ID:** `KU-API-seller-management-transactions--merchant-transactions` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Merchant transactions` in `api-specs/Seller_management_-_Transactions.yaml` (“Seller management - Transactions”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoint for managing merchant transactions

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` | `post-merchant-transaction-sale` | Create merchant transaction | no |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel` | `post-merchant-transaction-cancel` | Cancel merchant transaction | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Transactions.yaml method=POST path=/v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions operationId=post-merchant-transaction-sale -->
### `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` — Create merchant transaction

- **operationId:** `post-merchant-transaction-sale`
- **Specification:** `api-specs/Seller_management_-_Transactions.yaml` (Seller management - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Merchant transactions`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Create a new merchant transaction (sale) for a specific merchant associated with a marketplace.
>
> This endpoint allows for the creation of merchant sale transactions with installment support, MDR calculations, and scheduled payment dates. The default status is `SCHEDULED`. However, if the merchant is a marketplace scheduler, the transaction will automatically be set to `WAITING_SPLIT` status.
>
> This endpoint generates a [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>" |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `merchantId` | path | yes | integer | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `MerchantTransactionSalePostRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `event_date` | string (schema `EventDate`) | yes | Event datetime. The datetime format follows the ISO 8601 format (UTC). | format: "datetime"; example: "2023-01-01T12:00:00Z" |
| `amount` | number (schema `MerchantTransactionAmount`) | yes | Merchant transaction amount | format: "float"; nullable: false |
| `installments` | integer (schema `Installments`) | yes | Number of installments | format: "int32"; minimum: 1; maximum: 2147483647; example: 1 |
| `processing_code` | string (schema `ProcessingCode`) | yes | Processing code.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "999999" |
| `currency_code` | string (schema `CurrencyCode`) | no | Represents the currency with an ISO-4217 alphabetic or numeric (3 characters) string. For example, you represent Brazilian real with either BRL or 986.<br>If you don't provide this code, the system uses the currency from the merchant program.<br> | examples: ["BRL", "986"] |
| `authorization_id` | number (schema `AuthorizationId`) | no | Authorization identifier | format: "int64"; nullable: true |
| `transaction_status` | string (schema `MerchTransactionRequestStatus`) | no | Defines the status of the merchant transaction request.<br><br>- The default value is `SCHEDULED` for merchant schedulers, or `WAITING_SPLIT` for marketplace schedulers.<br>- The `WAITING_SPLIT` status should only be used when the transaction needs to wait for split request processing,<br>and only if the `merchant_id` provided is the `schedule_id`.<br>- The `schedule_id` can be obtained through the [marketplace query API](https://developers.pismo.io/pismo-docs/reference/getmarketplacebyidv2).<br> | enum: ["PENDING", "SCHEDULED", "SETTLED", "CANCELED", "WAITING_SPLIT"]; nullable: true |

Example `merchant-transaction-sale-post` (Merchant transaction sale post request) — from `#/components/examples/MerchantTransactionSalePostRequest`:

```json
{
  "event_date": "2024-02-14T10:30:00Z",
  "amount": 1500,
  "installments": 12,
  "processing_code": "003000",
  "currency_code": "BRL",
  "authorization_id": 123456,
  "transaction_status": "SCHEDULED"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Successfully list merchant transactions | `application/json`: object (schema `MerchantTransactionsResponseList`) |
| 400 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `MerchantTransactionResponse`) | no |  |  |

201 Example `List merchant transactions success` (Merchant transaction response) — from `#/components/examples/MerchantTransactionListResponse`:

```json
{
  "items": [
    {
      "id": 789013,
      "merchant_id": 12345,
      "creditor_id": 67890,
      "authorization_id": 123456,
      "parent_authorization_id": 654321,
      "org_operation_id": 111,
      "amount": 1500,
      "mdr_amount": 30,
      "mdr_without_fee": 25,
      "mdr_tax": 5,
      "fee": 10,
      "installment": 1,
      "number_of_installments": 12,
      "event_date": "2024-02-14T10:30:00Z",
      "scheduled_payment_date": "2024-03-21",
      "status": "SCHEDULED",
      "advanced_amount": 0,
      "type": "SALES",
      "origin_merchant_transaction_id": null,
      "advancement_request_id": null,
      "marketplace_id": 98765,
      "currency_code": "BRL",
      "discount_amount": 40,
      "discount_details": [
        {
          "name": "MDR",
          "amount": 25
        },
        {
          "name": "TRANSACTION_FEE",
          "amount": 15
        }
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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-merchant-transaction-created-1` | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-SELL-managing-merchant-transactions`.

<!-- op: spec=api-specs/Seller_management_-_Transactions.yaml method=POST path=/v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel operationId=post-merchant-transaction-cancel -->
### `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel` — Cancel merchant transaction

- **operationId:** `post-merchant-transaction-cancel`
- **Specification:** `api-specs/Seller_management_-_Transactions.yaml` (Seller management - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Merchant transactions`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Cancel a previously created merchant transaction.
>
> This endpoint allows for the creation of cancellation transactions that reverse the financial impact of original sale transactions.
> Cancellation transactions maintain negative amounts of all financial values (amount, MDR, fees) and reference the original transaction via origin_merchant_transaction_id.
>
> When the original transaction was split, the cancellation status is automatically set to `WAITING_SPLIT`, otherwise it follows the default status (`SCHEDULED`).
>
> This endpoint generates a [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>" |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `merchantId` | path | yes | integer | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `MerchantTransactionCancelPostRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `event_date` | string (schema `EventDate`) | yes | Event datetime. The datetime format follows the ISO 8601 format (UTC). | format: "datetime"; example: "2023-01-01T12:00:00Z" |
| `amount` | number (schema `MerchantTransactionAmount`) | yes | Merchant transaction amount | format: "float"; nullable: false |
| `authorization` | object (schema `MerchantTransactionAuthorizationRequest`) | yes |  |  |
| `processing_code` | string (schema `ProcessingCode`) | yes | Processing code.<br><br>For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | example: "999999" |

Example `merchant-transaction-cancel-post` (Merchant transaction cancel post request) — from `#/components/examples/MerchantTransactionCancelPostRequest`:

```json
{
  "event_date": "2024-02-14T10:30:00Z",
  "amount": 1500,
  "authorization": {
    "id": 123456,
    "parent_id": 654321
  },
  "processing_code": "003001"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Successfully list merchant transactions | `application/json`: object (schema `MerchantTransactionsResponseList`) |
| 400 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `MerchantTransactionResponse`) | no |  |  |

201 Example `List merchant transactions success` (Merchant transaction response) — from `#/components/examples/MerchantTransactionListResponse`:

```json
{
  "items": [
    {
      "id": 789013,
      "merchant_id": 12345,
      "creditor_id": 67890,
      "authorization_id": 123456,
      "parent_authorization_id": 654321,
      "org_operation_id": 111,
      "amount": 1500,
      "mdr_amount": 30,
      "mdr_without_fee": 25,
      "mdr_tax": 5,
      "fee": 10,
      "installment": 1,
      "number_of_installments": 12,
      "event_date": "2024-02-14T10:30:00Z",
      "scheduled_payment_date": "2024-03-21",
      "status": "SCHEDULED",
      "advanced_amount": 0,
      "type": "SALES",
      "origin_merchant_transaction_id": null,
      "advancement_request_id": null,
      "marketplace_id": 98765,
      "currency_code": "BRL",
      "discount_amount": 40,
      "discount_details": [
        {
          "name": "MDR",
          "amount": 25
        },
        {
          "name": "TRANSACTION_FEE",
          "amount": 15
        }
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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-merchant-transaction-created-1` | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-SELL-managing-merchant-transactions`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/MerchantTransactionResponse -->
### Schema `MerchantTransactionResponse`

Pointer: `#/components/schemas/MerchantTransactionResponse`. Type: object (schema `MerchantTransactionResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MerchTransId`) | no | Merchant transaction identifier | format: "int64" |
| `merchant_id` | integer (schema `MerchantId`) | no | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `creditor_id` | integer (schema `CreditorId`) | no | Creditor identifier | format: "int64"; nullable: true |
| `authorization_id` | number (schema `AuthorizationId`) | no | Authorization identifier | format: "int64"; nullable: true |
| `parent_authorization_id` | number (schema `ParentAuthorizationId`) | no | Parent authorization identifier | format: "int64"; nullable: true |
| `org_operation_id` | number (schema `OrgOperationId`) | no | Org operation identifier | format: "int64"; nullable: true |
| `amount` | number (schema `MerchantTransactionAmount`) | no | Merchant transaction amount | format: "float"; nullable: false |
| `mdr_amount` | number (schema `MdrAmount`) | no | Merchant transaction MDR amount | format: "float" |
| `mdr_without_fee` | number (schema `MdrWithoutFee`) | no | Merchant transaction MDR amount without fee | format: "float" |
| `mdr_tax` | number (schema `MdrTax`) | no | Merchant transaction MDR amount of marketplace | format: "float" |
| `fee` | number (schema `Fee`) | no | Merchant transaction fee | format: "float" |
| `installment` | integer (schema `Installment`) | no | Current instalment | format: "int32"; minimum: 1; maximum: 2147483647; example: 1 |
| `number_of_installments` | integer (schema `NumberOfInstallments`) | no | Number of installments | format: "int32"; minimum: 1; maximum: 2147483647; example: 1 |
| `event_date` | string (schema `EventDate`) | no | Event datetime. The datetime format follows the ISO 8601 format (UTC). | format: "datetime"; example: "2023-01-01T12:00:00Z" |
| `scheduled_payment_date` | string (schema `ScheduledPaymentDate`) | no | The scheduled payment date for the transaction. The datetime format follows the ISO 8601 format (UTC). | format: "datetime"; example: "2023-01-02" |
| `status` | string (schema `MerchTransactionStatus`) | no | Merchant transaction status | nullable: false |
| `advanced_amount` | integer (schema `MerchTransId`) | no | Merchant transaction identifier | format: "int64" |
| `type` | string (schema `MerchTransactionType`) | no | Merchant transaction type | nullable: false |
| `origin_merchant_transaction_id` | integer (schema `OriginMerchTransId`) | no | Sale Merchant transaction identifier | format: "int64"; nullable: true |
| `advancement_request_id` | integer (schema `AdvancementRequestId`) | no | Advancement Requested id | format: "int64"; nullable: true |
| `marketplace_id` | integer (schema `MarketplaceId`) | no | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `currency_code` | string (schema `CurrencyCodeResponse`) | no | ISO-4217 alphabetic (3 characters) currency code<br> | example: "BRL" |
| `discount_amount` | number (schema `DiscountAmount`) | no | Total discount amount applied to the transaction | format: "float"; example: 1.99 |
| `discount_details` | array of object (schema `DiscountDetail`) | no |  |  |

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

<!-- schema: #/components/schemas/MerchantTransactionAuthorizationRequest -->
### Schema `MerchantTransactionAuthorizationRequest`

Pointer: `#/components/schemas/MerchantTransactionAuthorizationRequest`. Type: object (schema `MerchantTransactionAuthorizationRequest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | yes | Authorization identifier | format: "int64" |
| `parent_id` | integer | yes | Parent authorization identifier from the original transaction | format: "int64" |

<!-- schema: #/components/schemas/DiscountDetail -->
### Schema `DiscountDetail`

Pointer: `#/components/schemas/DiscountDetail`. Type: object (schema `DiscountDetail`).

> The `amount` represents the fee applied - that is, the amount discounted before settlement.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | Discount name | example: "EMISSION_FEE" |
| `amount` | number | no | Total discount amount | format: "float"; example: 10 |

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
| `api-specs/Seller_management_-_Transactions.yaml` | tag `Merchant transactions`: POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions, POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions/cancel | https://github.com/PismoDevEx/pismo-api-specs | `f064908196c8f7cd…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
