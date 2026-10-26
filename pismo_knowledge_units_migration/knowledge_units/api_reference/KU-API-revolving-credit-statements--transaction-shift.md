---
ku_id: KU-API-revolving-credit-statements--transaction-shift
title: 'API reference: Revolving credit - Statements — Transaction shift'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- post-shift-transactions
- getTransactionShift
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-transaction-shifts
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-EVT-catalogue-balance
- KU-EVT-catalogue-transaction
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Transaction shift

**KU ID:** `KU-API-revolving-credit-statements--transaction-shift` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Transaction shift` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for transaction shifts. An installment can be moved between open statements in either direction in time. That is, it can be moved from a future 
> statement to an earlier open statement, or from a future statement to a statement farther in the future. Records can be retrieved for transaction shifts that 
> are already performed.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /statements-v2/v1/accounts/{accountId}/transactions/shifts` | `post-shift-transactions` | Shift transactions | no |
| `GET /statements-v2/v1/accounts/{accountId}/transactions/shifts/{transactionShiftId}` | `getTransactionShift` | Get transaction shift | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=POST path=/statements-v2/v1/accounts/{accountId}/transactions/shifts operationId=post-shift-transactions -->
### `POST /statements-v2/v1/accounts/{accountId}/transactions/shifts` — Shift transactions

- **operationId:** `post-shift-transactions`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transaction shift`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Shift one or more transactions between open statements. For example, a transaction can be moved from a future statement to an earlier open statement. A transaction can also be moved to a statement farther in the future. A maximum of 24 shifts are allowed per request.
>
> This endpoint generates an [Transaction updated](https://developers.pismo.io/events/docs/transaction-update-1) event for each transaction that is shifted. After all the transactions are successfully shifted, it generates a [Transactions shifted](https://developers.pismo.io/events/docs/balance-shift-transactions-1) event.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `TransactionShiftRequestBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `ShiftTrackingID`) | no | Tracking identifier. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. If a client <br>clicks the button more than once when sending the command to shift transactions, the Pismo platform could create duplicate <br>requests. The tracking identifier enables the platform to identify duplicates and ignore them.<br> | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `shifts` | array of object (schema `ShiftRequestItem`) (schema `RequestShifts`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and created the resource. | `application/json`: object (schema `TransactionShiftResponseBody`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | NOT FOUND - Some transactions were not found for the account ID and this organization. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_statement_shift_id` | integer (schema `TransactionStatementShiftID`) | no | ID of the shift operation performed | format: "int64"; example: 211452 |
| `desired_cycle_date` | string (schema `DesiredCycleDateInResponse`) | no | The desired cycle date. This is only present if the shift for the transaction is based on the cycle date. Format is yyyy-mm-dd. | format: "date"; example: "2023-12-25" |
| `tracking_id` | string (schema `ShiftTrackingID`) | no | Tracking identifier. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. If a client <br>clicks the button more than once when sending the command to shift transactions, the Pismo platform could create duplicate <br>requests. The tracking identifier enables the platform to identify duplicates and ignore them.<br> | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `shifts` | array of object (schema `ShiftResponseItem`) (schema `ResponseShifts`) | no |  |  |

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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-shift-transactions-1` | https://developers.pismo.io/events/docs/balance-shift-transactions-1 |
| `transaction-update-1` | https://developers.pismo.io/events/docs/transaction-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-transaction-shifts`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/accounts/{accountId}/transactions/shifts/{transactionShiftId} operationId=getTransactionShift -->
### `GET /statements-v2/v1/accounts/{accountId}/transactions/shifts/{transactionShiftId}` — Get transaction shift

- **operationId:** `getTransactionShift`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transaction shift`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the record for a performed shift. Includes the IDs for the source and destination statements.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `transactionShiftId` | path | yes | integer | Transaction shift ID | format: "int64"; example: 101 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and created the resource. | `application/json`: object (schema `TransactionShiftResponseBody`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | NOT FOUND - There is no transactions shift record with the requested ID for this organization. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_statement_shift_id` | integer (schema `TransactionStatementShiftID`) | no | ID of the shift operation performed | format: "int64"; example: 211452 |
| `desired_cycle_date` | string (schema `DesiredCycleDateInResponse`) | no | The desired cycle date. This is only present if the shift for the transaction is based on the cycle date. Format is yyyy-mm-dd. | format: "date"; example: "2023-12-25" |
| `tracking_id` | string (schema `ShiftTrackingID`) | no | Tracking identifier. Must consist of the characters [a-z,A-Z,0-9,-,:] with a range from 1 to 128. If a client <br>clicks the button more than once when sending the command to shift transactions, the Pismo platform could create duplicate <br>requests. The tracking identifier enables the platform to identify duplicates and ignore them.<br> | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `shifts` | array of object (schema `ShiftResponseItem`) (schema `ResponseShifts`) | no |  |  |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-transaction-shifts`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ShiftRequestItem -->
### Schema `ShiftRequestItem`

Pointer: `#/components/schemas/ShiftRequestItem`. Type: object (schema `ShiftRequestItem`).

> Resource that represents the shift for each transaction

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `new_statement_id` | integer (schema `NewStatementID`) | no | Indicates the ID of the statement to receive the transaction. This field cannot be present along with `desired_cycle_date`.<br> | format: "int64"; example: 124533 |
| `desired_cycle_date` | string (schema `DesiredCycleDateInRequest`) | no | Indicates the desired cycle date. Format is yyyy-mm-dd.<br><br>The statement to be used is the one with the closest cycle closing date (either the same date or the closest one in the future).<br>This field cannot be present along with `new_statement_id`.<br> | format: "date"; example: "2023-12-25" |

<!-- schema: #/components/schemas/ShiftResponseItem -->
### Schema `ShiftResponseItem`

Pointer: `#/components/schemas/ShiftResponseItem`. Type: object (schema `ShiftResponseItem`).

> Resource that represents the shift for each transaction

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `old_statement_id` | integer (schema `OldStatementID`) | no | ID of the source statement | format: "int64"; example: 124532 |
| `new_statement_id` | integer (schema `NewStatementID`) | no | Indicates the ID of the statement to receive the transaction. This field cannot be present along with `desired_cycle_date`.<br> | format: "int64"; example: 124533 |
| `desired_cycle_date` | string (schema `DesiredCycleDateInResponse`) | no | The desired cycle date. This is only present if the shift for the transaction is based on the cycle date. Format is yyyy-mm-dd. | format: "date"; example: "2023-12-25" |

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
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Transaction shift`: POST /statements-v2/v1/accounts/{accountId}/transactions/shifts, GET /statements-v2/v1/accounts/{accountId}/transactions/shifts/{transactionShiftId} | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-transaction-shifts` — Transaction shifts
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
