---
ku_id: KU-API-revolving-credit-statements--discharge-tracking
title: 'API reference: Revolving credit - Statements — Discharge tracking'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Statements.yaml
  sha256: 2ffe392a0e56ae3b5bf71474f241d08b9b078bb852ffaeff142b4dd32d278fd1
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
- getAccountDischargeTracking
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Discharge tracking

**KU ID:** `KU-API-revolving-credit-statements--discharge-tracking` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Discharge tracking` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Discharge tracking endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements-v2/v1/accounts/{accountId}/discharges-tracking` | `getAccountDischargeTracking` | List discharges | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/accounts/{accountId}/discharges-tracking operationId=getAccountDischargeTracking -->
### `GET /statements-v2/v1/accounts/{accountId}/discharges-tracking` — List discharges

- **operationId:** `getAccountDischargeTracking`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Discharge tracking`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Track discharges for an account. A discharge occurs when a credit transaction is used to reduce the balance of a debit transaction.
> This endpoint returns a list of credit transactions along with the debit transactions that they were used to discharge.
> You can filter the list by `creditTransactionId`, `CreditTransactionBeginDate`, and `CreditTransactionEndDate`.
>
> If an invalid value is entered for `creditTransactionBeginDate` or `creditTransactionEndDate`, the endpoint returns `400 - Bad Request`. An example of an invalid value would be if `creditTransactionEndDate` is an earlier date than `creditTransactionBeginDate` or if `creditTransactionBeginDate` is more than 184 days in the past.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `creditTransactionId` | query | no | integer | Credit transaction ID | format: "int64"; example: 1 |
| `creditTransactionBeginDate` | query | no | string | Start date to filter credit transactions. If not provided, it defaults to today's date minus 184 days. Format = yyyy-mm-dd.<br><br>This endpoint returns no credit transactions older than 184 days, so `creditTransactionBeginDate` must be greater than the current date minus 185 days.<br> | format: "date"; example: "2023-01-01" |
| `creditTransactionEndDate` | query | no | string | End date to filter credit transactions. If not provided, it defaults to `creditTransactionBeginDate` plus 184 days. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-01" |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `DischargeTrackingListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPageDefault10`) | no | Items per page | default: 10; format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Number of items found | format: "int32"; example: 100 |
| `items_on_page` | integer (schema `ItemsOnPage`) | no | Number of items on this page | format: "int32"; example: 5 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 4 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Is this the last page? | example: true |
| `items` | array of object | no |  |  |
| `items[].transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `items[].statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `items[].transaction_amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; example: 150 |
| `items[].transaction_type_id` | integer (schema `TransactionTypeID`) | no | Transaction type ID | format: "int32"; example: 342 |
| `items[].customer_id` | integer (schema `CustomerID`) | no | Customer ID | format: "int64"; example: 12456721 |
| `items[].account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1010 |
| `items[].program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `items[].program_type_id` | integer (schema `ProgramTypeID`) | no | Program type ID | format: "int64"; example: 1 |
| `items[].event_datetime` | string (schema `EventDatetime`) | no | Event datetime. Format = yyyy-mm-dd:hr:mm:ss. | format: "full-date-time"; example: "2023-02-22T15:17:05" |
| `items[].payment_datetime` | string (schema `PaymentDatetime`) | no | Date/time of the down payment. Format = YYYY-MM-DDThr:mm:ss.<br><br>This field may represent the payment date for the down payment. When provided, this date is used as the transaction event date for credit and installments.<br> | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `items[].target` | array of object | no |  |  |
| `items[].target[].transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `items[].target[].statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `items[].target[].transaction_type_id` | integer (schema `TransactionTypeID`) | no | Transaction type ID | format: "int32"; example: 342 |
| `items[].target[].customer_id` | integer (schema `CustomerID`) | no | Customer ID | format: "int64"; example: 12456721 |
| `items[].target[].account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1010 |
| `items[].target[].event_datetime` | string (schema `EventDatetime`) | no | Event datetime. Format = yyyy-mm-dd:hr:mm:ss. | format: "full-date-time"; example: "2023-02-22T15:17:05" |
| `items[].target[].discharge_datetime` | string (schema `DischargeDatetime`) | no | Discharge datetime. Format is yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2023-02-22T15:17:05" |
| `items[].target[].transaction_amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; example: 150 |
| `items[].target[].discharge_amount` | number (schema `DischargeAmount`) | no | Discharged amount | format: "float"; example: 600 |
| `items[].target[].previous_balance` | number (schema `PreviousBalance`) | no | Amount you owed on the account when the previous statement closed. | format: "float"; example: 99.99 |
| `items[].target[].final_balance` | number (schema `FinalBalance`) | no | Final balance. The final balance is the remaining balance of a debit transaction after it is discharged. | format: "float" |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Internal error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Discharge tracking`: GET /statements-v2/v1/accounts/{accountId}/discharges-tracking | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
