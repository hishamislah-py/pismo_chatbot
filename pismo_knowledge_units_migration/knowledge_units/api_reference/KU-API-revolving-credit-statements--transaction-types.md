---
ku_id: KU-API-revolving-credit-statements--transaction-types
title: 'API reference: Revolving credit - Statements — Transaction types'
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
- updateProgramTransactionType
- getTransactionTypes_1
- getTransactionTypes
related_kus:
- KU-CORE-transactions-overview
- KU-CRED-configuring-a-sellos-tax
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Transaction types

**KU ID:** `KU-API-revolving-credit-statements--transaction-types` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Transaction types` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Transaction type endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PATCH /statements-v2/v1/programs-transactions-types/{programTransactionTypeId}` | `updateProgramTransactionType` | Update program transaction type | no |
| `GET /statements-v2/v1/programs-transactions-types` | `getTransactionTypes_1` | List program transaction types | no |
| `GET /statements-v2/v1/transactions-types` | `getTransactionTypes` | List transaction types<br> | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PATCH path=/statements-v2/v1/programs-transactions-types/{programTransactionTypeId} operationId=updateProgramTransactionType -->
### `PATCH /statements-v2/v1/programs-transactions-types/{programTransactionTypeId}` — Update program transaction type

- **operationId:** `updateProgramTransactionType`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a program transaction type.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programTransactionTypeId` | path | yes | integer | ID of program transaction type to update. | format: "int64"; example: 2 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProgramTransactionTypeUpdateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |
| `charge_order` | integer (schema `ChargeOrder`) | no | Indicates which transaction is discharged first. 1 is the highest in the hierarchy. | format: "int32"; example: 2 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramTransactionTypeUpdatedResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_transaction_type_id` | integer (schema `ProgramTransactionTypeID`) | no | Program transaction type ID | format: "int64"; example: 5 |
| `charge_order` | integer (schema `ChargeOrder`) | no | Indicates which transaction is discharged first. 1 is the highest in the hierarchy. | format: "int32"; example: 2 |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |

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

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/programs-transactions-types operationId=getTransactionTypes_1 -->
### `GET /statements-v2/v1/programs-transactions-types` — List program transaction types

- **operationId:** `getTransactionTypes_1`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List a program's transaction types with filtering options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program-id` | header | yes | string | Program ID | example: "1233" |
| `transactionTypeId` | query | no | array of integer | One or more transaction type IDs | example: [101, 112]; items.format: "int64" |
| `transactionCategoryId` | query | no | array of integer | One or more program transaction category ID's | example: [1, 2]; items.format: "int32" |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `ProgramTransactionTypeListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pagination` | object (schema `PaginationListResponseProgramTransactionTypeResponse`) | no |  |  |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Program not found`:

```json
{
  "code": "EX0001",
  "message": "There is no program with the informed program_id: ${program_id}"
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
| 404 | `EX0001` | There is no program with the informed program_id: ${program_id} |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-transactions-overview`, `KU-CRED-configuring-a-sellos-tax`, `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/transactions-types operationId=getTransactionTypes -->
### `GET /statements-v2/v1/transactions-types` — List transaction types


- **operationId:** `getTransactionTypes`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List transaction types.
>
> This endpoint will be **DEPRECATED**. Use [List program transaction types](ref:gettransactiontypes_1) instead.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-program-id` | header | yes | integer | Program ID | format: "int64"; example: 1122 |
| `transactionTypeId` | query | no | array of integer | One or more transaction type IDs | example: [101, 112]; items.format: "int64" |
| `transactionCategoryId` | query | no | array of integer | One or more program transaction category ID's | example: [1, 2]; items.format: "int32" |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `TransactionTypeListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `TransactionTypeResponse`) | no |  |  |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPageDefault10`) | no | Items per page | default: 10; format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Number of items found | format: "int32"; example: 100 |
| `items_on_page` | integer (schema `ItemsOnPage`) | no | Number of items on this page | format: "int32"; example: 5 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 4 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Is this the last page? | example: true |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Program not found`:

```json
{
  "code": "EX0001",
  "message": "There is no program with the informed program_id: ${program_id}"
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
| 404 | `EX0001` | There is no program with the informed program_id: ${program_id} |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

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

<!-- schema: #/components/schemas/PaginationListResponseProgramTransactionTypeResponse -->
### Schema `PaginationListResponseProgramTransactionTypeResponse`

Pointer: `#/components/schemas/PaginationListResponseProgramTransactionTypeResponse`. Type: object (schema `PaginationListResponseProgramTransactionTypeResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPageDefault10`) | no | Items per page | default: 10; format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Number of items found | format: "int32"; example: 100 |
| `items_on_page` | integer (schema `ItemsOnPage`) | no | Number of items on this page | format: "int32"; example: 5 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 4 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Is this the last page? | example: true |
| `items` | array of object (schema `ProgramTransactionTypeResponse`) | no |  |  |

<!-- schema: #/components/schemas/TransactionTypeResponse -->
### Schema `TransactionTypeResponse`

Pointer: `#/components/schemas/TransactionTypeResponse`. Type: object (schema `TransactionTypeResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeID`) | no | Transaction type ID | format: "int32"; example: 342 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |
| `transaction_type_description` | string (schema `TransactionTypeDescription`) | no | Transaction type description | example: "purchase" |

<!-- schema: #/components/schemas/ProgramTransactionTypeResponse -->
### Schema `ProgramTransactionTypeResponse`

Pointer: `#/components/schemas/ProgramTransactionTypeResponse`. Type: object (schema `ProgramTransactionTypeResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeID`) | no | Transaction type ID | format: "int32"; example: 342 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |
| `transaction_type_description` | string (schema `TransactionTypeDescription`) | no | Transaction type description | example: "purchase" |
| `program_transaction_type_id` | integer (schema `ProgramTransactionTypeID`) | no | Program transaction type ID | format: "int64"; example: 5 |
| `charge_order` | integer (schema `ChargeOrder`) | no | Indicates which transaction is discharged first. 1 is the highest in the hierarchy. | format: "int32"; example: 2 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Transaction types`: PATCH /statements-v2/v1/programs-transactions-types/{programTransactionTypeId}, GET /statements-v2/v1/programs-transactions-types, GET /statements-v2/v1/transactions-types | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-transactions-overview` — Transactions overview
- `KU-CRED-configuring-a-sellos-tax` — Configuring a sellos tax
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
