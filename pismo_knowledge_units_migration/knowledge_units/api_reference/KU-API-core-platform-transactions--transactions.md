---
ku_id: KU-API-core-platform-transactions--transactions
title: 'API reference: Core platform - Transactions — Transactions'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Transactions.yaml
  sha256: 203c22b2f02c342bb5bfee34c8d991ae771dbff84a92772890e033042b03ce31
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
- GetTransactionById
- ListTransactions
- SearchTranscationMetaDataCount
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CORE-transactions-overview
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wtrc
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
specification_version: 1.0.0
---

# API reference: Core platform - Transactions — Transactions

**KU ID:** `KU-API-core-platform-transactions--transactions` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Transactions` in `api-specs/Core_platform_-_Transactions.yaml` (“Core platform - Transactions”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to retrieve transaction data.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/transactions/{transactionId}` | `GetTransactionById` | Get transaction | no |
| `GET /v2/transactions` | `ListTransactions` | List transactions | no |
| `GET /v2/transactions/total-items` | `SearchTranscationMetaDataCount` | Get transaction count (deprecated) | **yes** |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=GET path=/v2/transactions/{transactionId} operationId=GetTransactionById -->
### `GET /v2/transactions/{transactionId}` — Get transaction

- **operationId:** `GetTransactionById`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transactions`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a specific transaction by its ID. You can use the [List transactions](ref:searchtransactions) endpoint to search for a transaction and get its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `transactionId` | path | yes | integer | Transaction ID | format: "int64" |
| `includeMetadata` | query | no | boolean | Return transaction metadata flag. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `TransactionWithMetadata`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Transaction ID | format: "int64"; example: 1111 |
| `program_id` | integer | no | Program ID | format: "int64"; example: 2222 |
| `account_id` | integer | no | Account ID | format: "int64"; example: 1234 |
| `statement_id` | integer | no | Statement ID | format: "int64"; example: 2345 |
| `installment` | integer | no | Transaction installment number | example: 2 |
| `number_of_installments` | integer | no | Total number of installments | example: 20 |
| `soft_descriptor` | string | no | Soft descriptor of transaction. This is the description that shows on the customer's statement after it is authorized, but before it is settled. |  |
| `processing_code` | string | no | Processing code used to create the transaction. | example: "00" |
| `processing_description` | string | no | Processing code description | example: "Purchase" |
| `customer_id` | integer | no | Customer ID | format: "int64"; example: 8675309 |
| `user_category` | string | no | User category | example: "SERVICES" |
| `transaction_group` | string | no | Transaction group | deprecated: true; example: "EXPENSES" |
| `entry_mode` | string | no | Transaction Entry Mode | example: "POS" |
| `amount` | array of object (schema `Amount`) | no |  |  |
| `tax` | array of object (schema `Tax`) | no | Transaction taxes |  |
| `event_date` | string | no | Event timestamp in the UTC (zero-hour offset) ISO 8601 format (yyyy-MM-ddThh:mm:ssZ). | format: "date-time"; example: "2022-08-24T19:15:24.000Z" |
| `event_datetime` | string | no | Event timestamp in the UTC (zero-hour offset) RFC 3339 format, which includes milliseconds (yyyy-MM-ddThh:mm:ss.SSSZ). | format: "date-time"; example: "2022-08-24T19:15:24.000Z" |
| `payment_date` | string | no | Payment timestamp provided by the user in the ISO 8601 format (yyyy-MM-ddThh:mm:ssZ). | format: "date-time"; example: "2022-08-24T20:13:24.000Z" |
| `payment_datetime` | string | no | Payment timestamp provided by the user in the RFC 3339 format, which includes milliseconds (yyyy-MM-ddThh:mm:ss.SSSZ). | format: "date-time"; example: "2022-08-24T20:13:24.000Z" |
| `created_at` | string | no | Transaction creation date (ISO 8601) | format: "date-time"; example: "2022-08-24T19:05:24.000Z" |
| `transaction_type` | object (schema `TransactionType`) | no |  | example: {"id": 203, "description": "Credit voucher", "credit": true, "posted_transaction": true, "balance_impact_id": 4, "category": "PAYMENTS/CREDITS"} |
| `card` | object (schema `Card`) | no | Contains details about the card used in a transaction.<br>*  For transactions from card network operations, this object includes card information.<br>*  For platform operations, this object is empty.<br>Whether card information appears depends on what was provided during authorization, not on the transaction type.<br> |  |
| `authorization` | object (schema `Authorization`) | no |  |  |
| `merchant` | object (schema `Merchant`) | no |  |  |
| `metadata` | object | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. The Pismo platform does not perform any validation or processing on this field.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

##### Response 400

400 Example `invalidRequestHeaders` (Invalid request headers):

```json
{
  "message": "Invalid request headers",
  "error": "Invalid request headers",
  "code": "WTRC00002"
}
```

400 Example `invalidRequestParameter` (Invalid request parameters):

```json
{
  "message": "Invalid request parameters",
  "error": "Invalid request parameters",
  "code": "WTRC00003"
}
```

400 Example `transactionIdNotInformed` (Transaction ID not provided):

```json
{
  "message": "Transaction ID not provided",
  "error": "Transaction ID not provided",
  "code": "WTRC01003"
}
```

##### Response 404

404 Example `transactionNotFound` (Transaction not found):

```json
{
  "message": "Transaction not found",
  "error": "Transaction not found",
  "code": "WTRC01001"
}
```

##### Response 500

500 Example `internalProcessingError` (Internal processing error):

```json
{
  "message": "Internal processing error",
  "error": "Internal processing error",
  "code": "ETRC00001"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WTRC00002` | Invalid request headers |
| 400 | `WTRC00003` | Invalid request parameters |
| 400 | `WTRC01003` | Transaction ID not provided |
| 404 | `WTRC01001` | Transaction not found |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CORE-transactions-overview`.

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=GET path=/v2/transactions operationId=ListTransactions -->
### `GET /v2/transactions` — List transactions

- **operationId:** `ListTransactions`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transactions`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List transactions without their metadata. If you provide at least one of the following parameters, the `eventDateStart` parameter is optional.
> - `id`
> - `authorizationId`
> - `authorizationIds`
> - `statementId`
> - `authorizationTrackingId`
> - `numberOfLatestTransactions`
>
> If you don't provide any of the above parameters, you must include the `eventDateStart` parameter, and the maximum allowed query range is 90 days.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `statementId` | query | no | integer | Statement ID | format: "int64" |
| `customerId` | query | no | integer | Customer ID | format: "int64" |
| `transactionTypeId` | query | no | integer | Transaction type ID filter. | format: "int64"; example: 101010 |
| `processingCode` | query | no | string | Processing code |  |
| `credit` | query | no | boolean | Show only credit (`true`) or debit (`false`) transactions. |  |
| `statementPost` | query | no | boolean | Filter on `StatementPost` field. This field indicates whether a transaction should be posted to the statement. |  |
| `authorizationId` | query | no | integer | The authorization ID | format: "int64"; example: 1 |
| `authorizationType` | query | no | string | The authorization type | enum: ["NETWORK", "PLATFORM"] |
| `eventDateStart` | query | no | string | Event date period start in `date` (YYYY-MM-DD) or `date-time` (YYYY-MM-DDThh:mm:ssZ) format | example: "2021-06-26T12:03:04Z" |
| `order` | query | no | string | The order of the result set. The results are always ordered by transaction date. This param indicates whether the order is ascending or descending. | enum: ["asc", "desc"] |
| `eventDateEnd` | query | no | string | Event date period end in `date` (YYYY-MM-DD) or `date-time` (YYYY-MM-DDThh:mm:ssZ) format | example: "2021-06-26T12:03:04Z" |
| `numberOfLatestTransactions` | query | no | integer | Number of latest transactions. This filter gets the specified number of latest transactions, overwrites page filters, and doesn't allow any other filters with it. | format: "int64"; minimum: 1; maximum: 500 |
| `authorizationTrackingId` | query | no | string | Authorization tracking ID |  |
| `pageSize` | query | no | integer | Maximum number of transactions per page. If not provided, defaults to 100. Must be between 1 and 1000. | default: 100; minimum: 1; maximum: 1000 |
| `pageOffset` | query | no | integer | Page offset of transactions. Indicates which page to start with when returning the results. Defaults to 0. Must be between 0 and 5000. | default: 0; minimum: 0; maximum: 5000 |
| `ids` | query | no | array of integer | Array of transaction IDs | minItems: 1; maxItems: 100; items.format: "int64"; example: [10, 20, 30, 40, 50, 60] |
| `userCategory` | query | no | string | User category |  |
| `paymentMethodId` | query | no | string | Payment method ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Indicates whether there are more pages after the current page. |  |
| `items` | array of object | no | Items returned by the request |  |
| `items` | array of object (schema `Transaction`) | no |  |  |

##### Response 400

400 Example `invalidRequestHeaders` (Invalid request headers):

```json
{
  "message": "Invalid request headers",
  "error": "Invalid request headers",
  "code": "WTRC00002"
}
```

400 Example `invalidRequestParameter` (Invalid request parameters):

```json
{
  "message": "Invalid request parameters",
  "error": "Invalid request parameters",
  "code": "WTRC00003"
}
```

400 Example `invalidFilterValue` (Invalid filter value):

```json
{
  "message": "Invalid filter value",
  "error": "Invalid filter value",
  "code": "WTRC00001"
}
```

400 Example `invalidPageSizeExceedsMax` (Page size exceeds maximum):

```json
{
  "message": "pageSize must not exceed 1000",
  "error": "pageSize must not exceed 1000",
  "code": "WTRC00001"
}
```

400 Example `invalidPageSizeNotPositive` (Page size must be positive):

```json
{
  "message": "pageSize must be greater than 0",
  "error": "pageSize must be greater than 0",
  "code": "WTRC00001"
}
```

400 Example `invalidPageSizeNotInteger` (Page size not an integer):

```json
{
  "message": "pageSize should be an integer value",
  "error": "pageSize should be an integer value",
  "code": "WTRC00001"
}
```

400 Example `invalidPageOffsetNegative` (Page offset must not be negative):

```json
{
  "message": "pageOffset must not be negative",
  "error": "pageOffset must not be negative",
  "code": "WTRC00001"
}
```

400 Example `invalidPageOffsetNotInteger` (Page offset not an integer):

```json
{
  "message": "pageOffset should be an integer value",
  "error": "pageOffset should be an integer value",
  "code": "WTRC00001"
}
```

400 Example `invalidPageOffsetExceedsMax` (Page offset exceeds maximum):

```json
{
  "message": "pageOffset must not exceed 5000",
  "error": "pageOffset must not exceed 5000",
  "code": "WTRC00001"
}
```

400 Example `invalidNumberOfLatestTransactions` (Number of latest transactions should not have another filter):

```json
{
  "message": "numberOfLatestTransactions should not have another filters associate",
  "error": "numberOfLatestTransactions should not have another filters associate",
  "code": "WTRC00001"
}
```

400 Example `invalidNumberOfLatestTransactionsFilter` (Number of latest transactions should be an integer):

```json
{
  "message": "numberOfLatestTransactions should be an integer value",
  "error": "numberOfLatestTransactions should be an integer value",
  "code": "WTRC00001"
}
```

400 Example `invalidNumberOfLatestTransactionsRange` (Invalid range for number of latest transactions):

```json
{
  "message": "numberOfLatestTransactions should be between 1 and 500",
  "error": "numberOfLatestTransactions should be between 1 and 500",
  "code": "WTRC00001"
}
```

400 Example `invalidAuthorizationType` (Invalid authorization type):

```json
{
  "message": "authorization type should be PLATFORM or NETWORK",
  "error": "authorization type should be PLATFORM or NETWORK",
  "code": "WTRC00001"
}
```

400 Example `accountRequired` (Account is required when querying by card ID):

```json
{
  "message": "account is required when querying by cardId ",
  "error": "account is required when querying by cardId ",
  "code": "WTRC00001"
}
```

400 Example `eventDateStartRequired` (Event date start not provided):

```json
{
  "message": "eventDateStart not provided",
  "error": "eventDateStart not provided",
  "code": "WTRC00001"
}
```

400 Example `invalidEventDateStartFormat` (Invalid event date start format):

```json
{
  "message": "invalid eventDateStart format",
  "error": "invalid eventDateStart format",
  "code": "WTRC00001"
}
```

400 Example `invalidEventDateEndFormat` (Invalid event date end format):

```json
{
  "message": "invalid eventDateEnd format",
  "error": "invalid eventDateEnd format",
  "code": "WTRC00001"
}
```

400 Example `invalidTimeRange` (Invalid time range):

```json
{
  "message": "invalid time range: difference between eventDateStart and eventDateEnd cannot be greater than 90 days",
  "error": "invalid time range: difference between eventDateStart and eventDateEnd cannot be greater than 90 days",
  "code": "WTRC00001"
}
```

##### Response 500

500 Example `internalProcessingError` (Internal processing error):

```json
{
  "message": "Internal processing error",
  "error": "Internal processing error",
  "code": "ETRC00001"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WTRC00002` | Invalid request headers |
| 400 | `WTRC00003` | Invalid request parameters |
| 400 | `WTRC00001` | Invalid filter value |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CORE-transactions-overview`.

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=GET path=/v2/transactions/total-items operationId=SearchTranscationMetaDataCount -->
### `GET /v2/transactions/total-items` — Get transaction count (deprecated)

- **operationId:** `SearchTranscationMetaDataCount`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transactions`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> This endpoint is **deprecated**. There is no replacement endpoint as this functionality is no longer supported due to its lack of scalability.
>
> Returns the number of transactions that match the given search parameters.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `statementId` | query | no | integer | Statement ID | format: "int64" |
| `customerId` | query | no | integer | Customer ID | format: "int64" |
| `transactionTypeId` | query | no | integer | Transaction type ID filter. | format: "int64"; example: 101010 |
| `processingCode` | query | no | string | Processing code |  |
| `credit` | query | no | boolean | Count only credit (`true`) or debit (`false`). |  |
| `authorizationId` | query | no | integer | The authorization ID | format: "int64"; example: 1 |
| `authorizationType` | query | no | string | The authorization type | enum: ["NETWORK", "PLATFORM"] |
| `eventDateStart` | query | no | string | Event date period start in `date` (YYYY-MM-DD) or `date-time` (YYYY-MM-DDThh:mm:ssZ) format | example: "2021-06-26T12:03:04Z" |
| `eventDateEnd` | query | no | string | Event date period end in `date` (YYYY-MM-DD) or `date-time` (YYYY-MM-DDThh:mm:ssZ) format | example: "2021-06-26T12:03:04Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `TransactionsCount`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `total_items` | integer | no | Total transaction count |  |

##### Response 400

400 Example `invalidRequestHeaders` (Invalid request headers):

```json
{
  "message": "Invalid request headers",
  "error": "Invalid request headers",
  "code": "WTRC00002"
}
```

400 Example `invalidRequestParameter` (Invalid request parameters):

```json
{
  "message": "Invalid request parameters",
  "error": "Invalid request parameters",
  "code": "WTRC00003"
}
```

400 Example `invalidFilterValue` (Invalid filter value):

```json
{
  "message": "Invalid filter value",
  "error": "Invalid filter value",
  "code": "WTRC00001"
}
```

##### Response 500

500 Example `internalProcessingError` (Internal processing error):

```json
{
  "message": "Internal processing error",
  "error": "Internal processing error",
  "code": "ETRC00001"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WTRC00002` | Invalid request headers |
| 400 | `WTRC00003` | Invalid request parameters |
| 400 | `WTRC00001` | Invalid filter value |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CORE-transactions-overview`, `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Amount -->
### Schema `Amount`

Pointer: `#/components/schemas/Amount`. Type: object (schema `Amount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | no | Amount type<br>  - `PRINCIPAL`: Transaction amount in the customer’s account currency (already converted).<br>  - `LOCAL`: Transaction amount in the merchant’s local currency, where the purchase was made.<br>  - `SETTLEMENT`: Settlement amount that is typically defined by the issuer and usually matches the `PRINCIPAL` currency.<br> | enum: ["PRINCIPAL", "LOCAL", "SETTLEMENT"] |
| `currency` | string | no | ISO-4217 alphabetic code (3 characters) for transaction currency. | example: "USD" |
| `value` | number | no | Amount value | multipleOf: 0.01 |

<!-- schema: #/components/schemas/Tax -->
### Schema `Tax`

Pointer: `#/components/schemas/Tax`. Type: object (schema `Tax`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `currency` | string | no | ISO-4217 alphabetic code (3 characters) for transaction currency. | minLength: 0; maxLength: 3; example: "BRL" |
| `type` | string | no | Tax type | enum: ["IOF", "IOF_DAILY", "INTEREST"] |
| `value` | number | no | Tax value | multipleOf: 0.01 |

<!-- schema: #/components/schemas/TransactionType -->
### Schema `TransactionType`

Pointer: `#/components/schemas/TransactionType`. Type: object (schema `TransactionType`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Transaction type ID | format: "int64" |
| `description` | string | no | Transaction type description | maxLength: 30 |
| `credit` | boolean | no | Indicates if the transaction type is a credit or debit operation. |  |
| `posted_transaction` | boolean | no | Indicates whether transactions are posted on statements (`true`) or not (`false`). |  |
| `balance_impact_id` | integer | no | Balance impact ID | format: "int64" |
| `category` | string | no | Transaction type category |  |

<!-- schema: #/components/schemas/Card -->
### Schema `Card`

Pointer: `#/components/schemas/Card`. Type: object (schema `Card`).

> Contains details about the card used in a transaction.
> *  For transactions from card network operations, this object includes card information.
> *  For platform operations, this object is empty.
> Whether card information appears depends on what was provided during authorization, not on the transaction type.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Card ID |  |
| `name` | string | no | Card name |  |

<!-- schema: #/components/schemas/Authorization -->
### Schema `Authorization`

Pointer: `#/components/schemas/Authorization`. Type: object (schema `Authorization`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Authorization ID | format: "int64" |
| `type` | string | no | Authorization's type | enum: ["PLATFORM", "NETWORK"] |
| `code` | string | no | Authorization code or Network Approval Code |  |
| `payment_method_id` | string | no | Payment method |  |
| `network` | string | no | Visa or Mastercard network | enum: ["VISA", "MASTERCARD"] |
| `tracking_id` | string | no | Idempotency tracking ID |  |
| `correlated_authorization_id` | integer | no | Authorization ID generated by force or installment operations when the `original_authorization` field is provided. See the [Force operation](doc:force-operation) and [Installments payment](doc:installments-payment) guides for more information. | format: "int64" |
| `original_account_id` | integer | no | Original account ID. This field is used when the transaction is linked to a authorizaiton that was made on a different account than the one being queried. | format: "int64" |

<!-- schema: #/components/schemas/Merchant -->
### Schema `Merchant`

Pointer: `#/components/schemas/Merchant`. Type: object (schema `Merchant`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Merchant ID |  |
| `type` | string | no | Merchant type |  |
| `name` | string | no | Merchant name |  |
| `city` | string | no | Merchant city |  |
| `state` | string | no | Merchant's state. In some cases, for countries other than the U.S., it can indicate the country code of the merchant instead. |  |
| `category` | object (schema `MerchantCategory`) | no |  |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Error description. |  |
| `error` | string | no | Error description. |  |
| `code` | string | no | Code description. |  |

<!-- schema: #/components/schemas/Transaction -->
### Schema `Transaction`

Pointer: `#/components/schemas/Transaction`. Type: object (schema `Transaction`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Transaction ID | format: "int64"; example: 1111 |
| `program_id` | integer | no | Program ID | format: "int64"; example: 2222 |
| `account_id` | integer | no | Account ID | format: "int64"; example: 1234 |
| `statement_id` | integer | no | Statement ID | format: "int64"; example: 2345 |
| `installment` | integer | no | Transaction installment number | example: 2 |
| `number_of_installments` | integer | no | Total number of installments | example: 20 |
| `soft_descriptor` | string | no | Soft descriptor of transaction. This is the description that shows on the customer's statement after it is authorized, but before it is settled. |  |
| `processing_code` | string | no | Processing code used to create the transaction. | example: "00" |
| `processing_description` | string | no | Processing code description | example: "Purchase" |
| `customer_id` | integer | no | Customer ID | format: "int64"; example: 8675309 |
| `user_category` | string | no | User category | example: "SERVICES" |
| `transaction_group` | string | no | Transaction group | deprecated: true; example: "EXPENSES" |
| `entry_mode` | string | no | Transaction Entry Mode | example: "POS" |
| `amount` | array of object (schema `Amount`) | no |  |  |
| `tax` | array of object (schema `Tax`) | no | Transaction taxes |  |
| `event_date` | string | no | Event timestamp in the UTC (zero-hour offset) ISO 8601 format (yyyy-MM-ddThh:mm:ssZ). | format: "date-time"; example: "2022-08-24T19:15:24.000Z" |
| `event_datetime` | string | no | Event timestamp in the UTC (zero-hour offset) RFC 3339 format, which includes milliseconds (yyyy-MM-ddThh:mm:ss.SSSZ). | format: "date-time"; example: "2022-08-24T19:15:24.000Z" |
| `payment_date` | string | no | Payment timestamp provided by the user in the ISO 8601 format (yyyy-MM-ddThh:mm:ssZ). | format: "date-time"; example: "2022-08-24T20:13:24.000Z" |
| `payment_datetime` | string | no | Payment timestamp provided by the user in the RFC 3339 format, which includes milliseconds (yyyy-MM-ddThh:mm:ss.SSSZ). | format: "date-time"; example: "2022-08-24T20:13:24.000Z" |
| `created_at` | string | no | Transaction creation date (ISO 8601) | format: "date-time"; example: "2022-08-24T19:05:24.000Z" |
| `transaction_type` | object (schema `TransactionType`) | no |  | example: {"id": 203, "description": "Credit voucher", "credit": true, "posted_transaction": true, "balance_impact_id": 4, "category": "PAYMENTS/CREDITS"} |
| `card` | object (schema `Card`) | no | Contains details about the card used in a transaction.<br>*  For transactions from card network operations, this object includes card information.<br>*  For platform operations, this object is empty.<br>Whether card information appears depends on what was provided during authorization, not on the transaction type.<br> |  |
| `authorization` | object (schema `Authorization`) | no |  |  |
| `merchant` | object (schema `Merchant`) | no |  |  |

<!-- schema: #/components/schemas/MerchantCategory -->
### Schema `MerchantCategory`

Pointer: `#/components/schemas/MerchantCategory`. Type: object (schema `MerchantCategory`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Merchant category code (MCC). Provided by the network (Visa or Mastercard). |  |
| `description` | string | no | Merchant category description |  |
| `group_name` | string | no | Merchant category group name |  |
| `network_group` | string | no | Merchant category group name sent by network |  |

## Lifecycle status

- `GET /v2/transactions/total-items` (`SearchTranscationMetaDataCount`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Transactions.yaml` | tag `Transactions`: GET /v2/transactions/{transactionId}, GET /v2/transactions, GET /v2/transactions/total-items | https://github.com/PismoDevEx/pismo-api-specs | `203c22b2f02c342b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wtrc` — Error codes: WTRC
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
