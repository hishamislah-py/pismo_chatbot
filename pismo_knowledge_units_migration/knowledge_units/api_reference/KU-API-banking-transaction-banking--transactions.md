---
ku_id: KU-API-banking-transaction-banking--transactions
title: 'API reference: Banking - Transaction banking — Transactions'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Transaction_banking.yaml
  sha256: dec6c4900eb2db35c29c0f0380763da5ae0e1a18c4ad1e293216b2b6effdab56
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
- get-corporate-transactions
- get-corporate-transaction
- list-corporate-transaction-statuses
related_kus:
- KU-CRED-discharging-transactions
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-ERR-codes-wpmt
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Transactions

**KU ID:** `KU-API-banking-transaction-banking--transactions` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Transactions` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Transaction endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /corporate/v1/corporate-transactions` | `get-corporate-transactions` | List transactions (transaction banking) | no |
| `GET /corporate/v1/corporate-transactions/{transactionId}` | `get-corporate-transaction` | Get transaction (transaction banking) | no |
| `GET /corporate/v1/corporate-transactions/status/{trackingId}` | `list-corporate-transaction-statuses` | List transaction status details (transaction banking) | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/corporate-transactions operationId=get-corporate-transactions -->
### `GET /corporate/v1/corporate-transactions` — List transactions (transaction banking)

- **operationId:** `get-corporate-transactions`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transactions`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Lists transactions of your transaction banking account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `offset` | query | no | integer | Starting point for the results list. Default is `0` | default: 0; format: "int32"; minimum: 0; example: 1 |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `10` | default: 10; format: "int32"; maximum: 100; example: 100 |
| `statementId` | query | no | integer | Statement ID | format: "int64"; example: 1234 |
| `customerId` | query | no | integer | Customer ID | format: "int64"; example: 4321 |
| `transactionTypeId` | query | no | integer | Transaction type ID | format: "int64"; example: 5678 |
| `processingCode` | query | no | string | Processing code used to create the transaction | example: "219248" |
| `credit` | query | no | boolean | Show only credit (`true`) or debit (`false`) transactions. | example: true |
| `statementPost` | query | no | boolean | Filter transactions posted to the statement. | example: true |
| `authorizationId` | query | no | integer | Authorization ID | format: "int64"; example: 78; deprecated: true |
| `authorizationType` | query | no | string | Authorization type | enum: ["PLATFORM", "NETWORK"]; example: "PLATFORM" |
| `eventDateStart` | query | no | string | Start of event date period. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2023-04-27T12:00:00Z" |
| `eventDateEnd` | query | no | string | End of event date period. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2023-04-27T13:00:00Z" |
| `order` | query | no | string | Order of the result list. The results are always ordered by transaction date. This param indicates whether the order is ascending ('asc') or descending ('desc'). | enum: ["asc", "desc"]; example: "asc" |
| `authorizationTrackingId` | query | no | string | Authorization tracking ID | example: "68ea7e26-e506-11ed-b5ea-0242ac120002" |
| `ids` | query | no | array of integer | Array of transaction IDs | minItems: 1; maxItems: 100; items.format: "int64"; example: [1, 2, 3, 4, 5, 6] |
| `userCategory` | query | no | string | User category | example: "RETAIL" |
| `paymentMethodId` | query | no | string | Payment method ID | example: "MASTERCARD" |
| `numberOfLatestTransactions` | query | no | integer | Number of latest transactions. Get the latest transactions based on the date specified in the `event_date` field. Note that this filter overwrites page filters and doesn't allow any other filters. | format: "int64"; minimum: 1; maximum: 500; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListTransactionsResponse`) |
| 400 | A Bad Request validation error | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized. | `application/json`: object (schema `ErrorResponse`) |
| 403 | Forbidden | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transactions` | array of object (schema `TransactionResponse`) | no | List of transactions |  |
| `pagination` | object (schema `OffsetPagination`) | no | Data related to list pagination using an offset parameter |  |

200 Example `Example transactions list`:

```json
{
  "transactions": [
    {
      "id": 1111,
      "program_id": 2222,
      "account_id": 1234,
      "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
      "soft_descriptor": "Purchase",
      "processing_code": "219248",
      "processing_description": "Hold Funds",
      "amount": {
        "currency": "USD",
        "value": 1000.52
      },
      "event_date": "2023-04-27T12:01:24Z",
      "payment_date": "2023-04-27T12:01:24Z",
      "created_at": "2023-04-27T12:01:24Z",
      "transaction_type": {
        "id": 2345,
        "description": "Purchase",
        "credit": false,
        "posted_transaction": true
      },
      "authorization": {
        "id": 5678,
        "type": "PLATFORM",
        "code": "1234"
      },
      "metadata": {
        "invoice": 2938
      }
    },
    {
      "id": 1112,
      "program_id": 2222,
      "account_id": 1234,
      "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdac",
      "soft_descriptor": "Purchase",
      "processing_code": "219248",
      "processing_description": "Hold Funds",
      "amount": {
        "currency": "USD",
        "value": 1000.52
      },
      "event_date": "2023-04-27T12:02:24Z",
      "payment_date": "2023-04-27T12:02:24Z",
      "created_at": "2023-04-27T12:02:24Z",
      "transaction_type": {
        "id": 2345,
        "description": "Purchase",
        "credit": false,
        "posted_transaction": true
      },
      "authorization": {
        "id": 5679,
        "type": "PLATFORM",
        "code": "1234"
      },
      "metadata": {
        "invoice": 2938
      }
    }
  ],
  "pagination": {
    "has_next": false,
    "limit": 10,
    "offset": 0
  }
}
```

##### Response 400

400 Example `Invalid filter boolean value`:

```json
{
  "code": "WCTR0003",
  "message": "param_name is not a valid boolean value"
}
```

400 Example `Invalid authorization type value`:

```json
{
  "code": "WCTR0003",
  "message": "authorization type should be PLATFORM or NETWORK"
}
```

400 Example `Invalid order type`:

```json
{
  "code": "WCTR0003",
  "message": "invalid order type"
}
```

400 Example `Invalid request parameters`:

```json
{
  "code": "WCTR0004",
  "message": "Invalid request parameters"
}
```

##### Response 401

401 Example `Account not authorized`:

```json
{
  "code": "WCAC0001",
  "message": "Account not authorized"
}
```

##### Response 403

403 Example `Forbidden request`:

```json
{
  "message": "access denied"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCTR0003` | param_name is not a valid boolean value |
| 400 | `WCTR0004` | Invalid request parameters |
| 401 | `WCAC0001` | Account not authorized |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/corporate-transactions/{transactionId} operationId=get-corporate-transaction -->
### `GET /corporate/v1/corporate-transactions/{transactionId}` — Get transaction (transaction banking)

- **operationId:** `get-corporate-transaction`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transactions`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets transaction using transaction ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `transactionId` | path | yes | integer | Transaction ID | example: 313123 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `TransactionResponse`) |
| 400 | A Bad Request validation error | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized. | `application/json`: object (schema `ErrorResponse`) |
| 403 | Forbidden | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 1111 |
| `program_id` | integer (schema `ProgramID3`) | no | Program ID. This is a client-provided ID. | format: "int64"; example: 2222 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1234 |
| `external_account_id` | string (schema `ExternalAccountID`) | no | Custom account ID. Used as the key for all operations (manage accounts, transactions, etc.) on the corporate layer.<br><br>This field is:<br>- Unique within the Organization<br>- Immutable: The field cannot be updated.<br>- Not recyclable: You can't reuse an external account ID, even if the account that was using it has been canceled.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code used to create the underlying transaction. Each internal operation type uses a default processing code.<br><br>`minLength: 1`<br>`maxLength: 6`<br> | minLength: 1; maxLength: 6; example: "219248" |
| `processing_description` | string (schema `ProcessingCodeDescription`) | no | Processing code description | example: "Hold Funds" |
| `amount` | object (schema `Amount`) | no | Amount |  |
| `event_date` | string (schema `EventDate`) | no | Event date in format ISO 8601. | format: "date-time"; example: "2023-04-27T12:01:24Z" |
| `payment_date` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `created_at` | string (schema `TransactionCreatedAt`) | no | Transaction creation date in format ISO 8601 | format: "date-time"; example: "2023-04-27T12:01:24Z" |
| `transaction_type` | object (schema `TransactionType`) | no | Transaction type |  |
| `authorization` | object (schema `Authorization`) | no | Authorization |  |
| `metadata` | object (schema `Metadata`) | no | Key-value pairs that contain data intended for storage on the Pismo platform.<br><br><br>**Note**: The `metadata` field includes a `corporate_metadata` object with the following attributes:<br><br>  * `credit_external_account_id`: present when supplied in the credit leg.<br><br>  * `debit_external_account_id`: present when supplied in the debit leg.<br><br>  * `earmark_id`: present when supplied in the debit leg.<br><br>  The `corporate_metadata` attribute must be an object. A type mismatch results in an error as described in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"my-id": 2932} |

200 Example `Example transaction`:

```json
{
  "id": 1111,
  "program_id": 2222,
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "soft_descriptor": "Purchase",
  "processing_code": "219248",
  "processing_description": "Hold Funds",
  "amount": {
    "currency": "USD",
    "value": 1000.52
  },
  "event_date": "2023-04-27T12:01:24Z",
  "payment_date": "2023-04-27T12:01:24Z",
  "created_at": "2023-04-27T12:01:24Z",
  "transaction_type": {
    "id": 2345,
    "description": "Purchase",
    "credit": false,
    "posted_transaction": true
  },
  "authorization": {
    "id": 5678,
    "type": "PLATFORM",
    "code": "1234"
  },
  "metadata": {
    "invoice": 2938
  }
}
```

##### Response 400

400 Example `transactionId is invalid`:

```json
{
  "code": "WCTR0005",
  "message": "transactionId is invalid"
}
```

##### Response 401

401 Example `Account not authorized`:

```json
{
  "code": "WCAC0001",
  "message": "Account not authorized"
}
```

##### Response 403

403 Example `Forbidden request`:

```json
{
  "message": "access denied"
}
```

##### Response 404

404 Example `Transaction not found`:

```json
{
  "code": "WCTR0006",
  "message": "Transaction not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCTR0005` | transactionId is invalid |
| 401 | `WCAC0001` | Account not authorized |
| 404 | `WCTR0006` | Transaction not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-discharging-transactions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/corporate-transactions/status/{trackingId} operationId=list-corporate-transaction-statuses -->
### `GET /corporate/v1/corporate-transactions/status/{trackingId}` — List transaction status details (transaction banking)

- **operationId:** `list-corporate-transaction-statuses`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transactions`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Returns a list of transactions mapped to a tracking ID. For each transaction, the request returns the approval status (approved or declined), as well as details such as amount, currency, and metadata. Multiple transactions can be associated with a single tracking ID; for example in transfers where both debit and credit legs are present. Additionally, if there are multiple attempts using the same tracking ID, all failed (declined) attempts are also included in the response.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `trackingId` | path | yes | string | Original tracking ID provided when the ID is created. | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e245" |
| `cursor` | query | no | string | Cursor to the next page of results. If no value is specified, it fetches the first page. | example: "1234" |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `10` | default: 10; format: "int32"; example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListTransactionStatusResponse`) |
| 401 | Unauthorized. | `application/json`: object (schema `ErrorResponse`) |
| 403 | Forbidden | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `TransactionStatusResponse`) | no | List of transactions statuses |  |
| `pagination` | object (schema `Pagination`) | no | Data related to list pagination using a cursor. |  |

200 Example `Example transactions list`:

```json
{
  "items": [
    {
      "authorizations_status": "DECLINED",
      "amount": 1000,
      "currency": "USD",
      "processing_code": "220035",
      "tracking_id": "f216e914-7e72-4253-a386-d2215048af00",
      "metadata": {
        "invoice": 2938
      },
      "event_datetime": "2023-04-27T12:01:24Z",
      "error": {
        "code": "WPMT0010",
        "message": "Insufficient funds"
      }
    },
    {
      "authorizations_status": "APPROVED",
      "amount": 1000,
      "currency": "USD",
      "processing_code": "220035",
      "tracking_id": "f216e914-7e72-4253-a386-d2215048af00",
      "metadata": {
        "invoice": 2938
      },
      "event_datetime": "2023-04-27T13:01:24Z"
    }
  ],
  "pagination": {
    "cursor": "eyJvZmZzZXQiOiA0MDAwfQ==",
    "limit": 10
  }
}
```

##### Response 401

401 Example `Account not authorized`:

```json
{
  "code": "WCAC0001",
  "message": "Account not authorized"
}
```

##### Response 403

403 Example `Forbidden request`:

```json
{
  "message": "access denied"
}
```

##### Response 404

404 Example `Transaction not found`:

```json
{
  "code": "WCTR0006",
  "message": "Transaction not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 200 | `WPMT0010` | Insufficient funds |
| 401 | `WCAC0001` | Account not authorized |
| 404 | `WCTR0006` | Transaction not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/TransactionResponse -->
### Schema `TransactionResponse`

Pointer: `#/components/schemas/TransactionResponse`. Type: object (schema `TransactionResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 1111 |
| `program_id` | integer (schema `ProgramID3`) | no | Program ID. This is a client-provided ID. | format: "int64"; example: 2222 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1234 |
| `external_account_id` | string (schema `ExternalAccountID`) | no | Custom account ID. Used as the key for all operations (manage accounts, transactions, etc.) on the corporate layer.<br><br>This field is:<br>- Unique within the Organization<br>- Immutable: The field cannot be updated.<br>- Not recyclable: You can't reuse an external account ID, even if the account that was using it has been canceled.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code used to create the underlying transaction. Each internal operation type uses a default processing code.<br><br>`minLength: 1`<br>`maxLength: 6`<br> | minLength: 1; maxLength: 6; example: "219248" |
| `processing_description` | string (schema `ProcessingCodeDescription`) | no | Processing code description | example: "Hold Funds" |
| `amount` | object (schema `Amount`) | no | Amount |  |
| `event_date` | string (schema `EventDate`) | no | Event date in format ISO 8601. | format: "date-time"; example: "2023-04-27T12:01:24Z" |
| `payment_date` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `created_at` | string (schema `TransactionCreatedAt`) | no | Transaction creation date in format ISO 8601 | format: "date-time"; example: "2023-04-27T12:01:24Z" |
| `transaction_type` | object (schema `TransactionType`) | no | Transaction type |  |
| `authorization` | object (schema `Authorization`) | no | Authorization |  |
| `metadata` | object (schema `Metadata`) | no | Key-value pairs that contain data intended for storage on the Pismo platform.<br><br><br>**Note**: The `metadata` field includes a `corporate_metadata` object with the following attributes:<br><br>  * `credit_external_account_id`: present when supplied in the credit leg.<br><br>  * `debit_external_account_id`: present when supplied in the debit leg.<br><br>  * `earmark_id`: present when supplied in the debit leg.<br><br>  The `corporate_metadata` attribute must be an object. A type mismatch results in an error as described in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"my-id": 2932} |

<!-- schema: #/components/schemas/OffsetPagination -->
### Schema `OffsetPagination`

Pointer: `#/components/schemas/OffsetPagination`. Type: object (schema `OffsetPagination`).

> Data related to list pagination using an offset parameter

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean (schema `HasNext`) | no | Whether there are more pages after the current page (`true`) or not (`false`). | example: true |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `offset` | integer (schema `Offset`) | no | Starting index of the result list. Default is 0. | format: "int32"; example: 10 |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/Amount -->
### Schema `Amount`

Pointer: `#/components/schemas/Amount`. Type: object (schema `Amount`).

> Amount

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `value` | number (schema `AmountValue`) | yes | Amount value | format: "float"; minimum: 0; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |

<!-- schema: #/components/schemas/TransactionType -->
### Schema `TransactionType`

Pointer: `#/components/schemas/TransactionType`. Type: object (schema `TransactionType`).

> Transaction type

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `TransactionTypeID`) | no | Transaction type ID | format: "int64"; example: 2345 |
| `description` | string (schema `TransactionTypeDescription`) | no | Transaction type description | maxLength: 30; example: "Purchase" |
| `credit` | boolean (schema `IsCredit`) | no | Is the transaction a credit (`true`) or debit (`false`)? | example: true |
| `posted_transaction` | boolean (schema `PostedTransaction`) | no | Are transactions posted on statements? | example: false |

<!-- schema: #/components/schemas/Authorization -->
### Schema `Authorization`

Pointer: `#/components/schemas/Authorization`. Type: object (schema `Authorization`).

> Authorization

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AuthorizationID`) | no | Authorization ID | format: "int64"; example: 5678 |
| `type` | string (schema `AuthorizationType`) | no | Authorization type | enum: ["PLATFORM", "NETWORK"]; example: "PLATFORM" |
| `code` | string (schema `AuthorizationCode`) | no | Authorization code or network approval code | example: "1234" |
| `payment_method_id` | string (schema `PaymentMethod`) | no | Payment method | example: "MASTERCARD" |
| `tracking_id` | string (schema `TrackingID`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |

<!-- schema: #/components/schemas/TransactionStatusResponse -->
### Schema `TransactionStatusResponse`

Pointer: `#/components/schemas/TransactionStatusResponse`. Type: object (schema `TransactionStatusResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorizations_status` | string (schema `AuthorizationStatus`) | no | Authorization status | enum: ["APPROVED", "DECLINED"]; example: "DECLINED" |
| `amount` | number (schema `AmountValue`) | no | Amount value | format: "float"; minimum: 0; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code used to create the underlying transaction. Each internal operation type uses a default processing code.<br><br>`minLength: 1`<br>`maxLength: 6`<br> | minLength: 1; maxLength: 6; example: "219248" |
| `tracking_id` | string (schema `TrackingID`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `metadata` | object (schema `Metadata`) | no | Key-value pairs that contain data intended for storage on the Pismo platform.<br><br><br>**Note**: The `metadata` field includes a `corporate_metadata` object with the following attributes:<br><br>  * `credit_external_account_id`: present when supplied in the credit leg.<br><br>  * `debit_external_account_id`: present when supplied in the debit leg.<br><br>  * `earmark_id`: present when supplied in the debit leg.<br><br>  The `corporate_metadata` attribute must be an object. A type mismatch results in an error as described in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"my-id": 2932} |
| `event_datetime` | string (schema `EventDate`) | no | Event date in format ISO 8601. | format: "date-time"; example: "2023-04-27T12:01:24Z" |
| `error` | object (schema `ErrorResponse`) | no |  |  |

<!-- schema: #/components/schemas/Pagination -->
### Schema `Pagination`

Pointer: `#/components/schemas/Pagination`. Type: object (schema `Pagination`).

> Data related to list pagination using a cursor.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `cursor` | string (schema `Cursor`) | no | Cursor pointing to the next page of results | example: "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0=" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Transactions`: GET /corporate/v1/corporate-transactions, GET /corporate/v1/corporate-transactions/{transactionId}, GET /corporate/v1/corporate-transactions/status/{trackingId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-discharging-transactions` — Discharging transactions and the default discharge process
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-ERR-codes-wpmt` — Error codes: WPMT
