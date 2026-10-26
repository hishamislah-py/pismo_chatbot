---
ku_id: KU-API-core-platform-transactions--transaction-types
title: 'API reference: Core platform - Transactions — Transaction types'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- SearchTransactionTypes
- PostSetupTransactionType
- GetTransactionTypeById
- PatchTransactionType
- PatchProgramTransactionType
related_kus:
- KU-BANK-penalties-for-cd-accounts
- KU-CORE-transactions-overview
- KU-CORE-transactiontypes
- KU-CRED-full-balance-credit-program
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wtrc
- KU-EVT-catalogue-transaction
- KU-EVT-transactions-data-events
- KU-PAY-installments-payment
- KU-PAY-payments-configurations
- KU-SELL-managing-merchant-transactions
specification_version: 1.0.0
---

# API reference: Core platform - Transactions — Transaction types

**KU ID:** `KU-API-core-platform-transactions--transaction-types` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Transaction types` in `api-specs/Core_platform_-_Transactions.yaml` (“Core platform - Transactions”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage transaction types

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/transaction-types` | `SearchTransactionTypes` | List transaction types | no |
| `POST /v1/transaction-types` | `PostSetupTransactionType` | Create transaction type | no |
| `GET /v1/transaction-type/{transactionTypeId}` | `GetTransactionTypeById` | Get transaction type | no |
| `PATCH /v1/transaction-types/{transactionTypeId}` | `PatchTransactionType` | Update transaction type | no |
| `PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId}` | `PatchProgramTransactionType` | Update program transaction type description | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=GET path=/v1/transaction-types operationId=SearchTransactionTypes -->
### `GET /v1/transaction-types` — List transaction types

- **operationId:** `SearchTransactionTypes`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List transaction types that match the search parameters. If no search parameters are given, then all transaction types are returned.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `transactionTypeId` | query | no | integer | Transaction type ID filter. | format: "int64"; example: 101010 |
| `description` | query | no | string | Wildcard filter used to search transaction types by description. | minLength: 3 |
| `credit` | query | no | boolean | Filters transaction types by credit (`true`) or debit (`false`). |  |
| `pageSize` | query | no | integer | Maximum number of items per page. If not provided, defaults to 100. Must be between 1 and 1000. | default: 100; minimum: 1; maximum: 1000 |
| `orderBy` | query | no | string | Transaction type sort parameter | enum: ["transactionId", "description"]; default: "transactionId" |
| `pageOffset` | query | no | integer | Page offset. Indicates which page to start with when returning the results. For example, value `2` returns the third page. Defaults to `0`, which returns the first page. Must be between 0 and 5000. | default: 0; minimum: 0; maximum: 5000 |

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
| `has_next` | boolean | no | Indicates whether there are more pages after the current page |  |
| `items` | array of array of object (schema `ListTransactionTypes`) | no |  |  |

##### Response 400

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

##### Response 500

500 Example `failedToFetch` (Failed to get transaction type):

```json
{
  "message": "Failed to get transaction type",
  "error": "Failed to get transaction type",
  "code": "ETRC05001"
}
```

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
| 400 | `WTRC00001` | Invalid filter value |
| 500 | `ETRC05001` | Failed to get transaction type |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-transactions-overview`, `KU-CORE-transactiontypes`.

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=POST path=/v1/transaction-types operationId=PostSetupTransactionType -->
### `POST /v1/transaction-types` — Create transaction type

- **operationId:** `PostSetupTransactionType`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new transaction type. Examples of transaction types include cash-in and cash-out. For the list of transaction types on the Pismo platform, refer to [Standard processing codes](doc:processing-codes-and-transaction-types#standard-processing-codes).
>
> This endpoint generates the [Transaction type created](https://developers.pismo.io/events/docs/transaction-types-creation-1) event.
>
> For information on creating and managing processing codes and transaction types, refer to [Processing codes and transaction types](doc:processing-codes-and-transaction-types) and [Payments configurations](doc:payments-configurations).

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `TransactionTypeResult`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeId`) | yes | Transaction type ID. Certain IDs are reserved by the platform and cannot be used. | format: "int64"; minimum: 1 |
| `description` | string | yes | Transaction type description | maxLength: 30 |
| `credit` | boolean | yes | Indicates whether the transaction type is credit (`true`) or debit (`false`). |  |
| `posted_transaction` | boolean | yes | Indicates whether transactions are posted on statements (`true`) or not (`false`). Set to `false` for zero balance integrations. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `TransactionTypeResult`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeId`) | yes | Transaction type ID. Certain IDs are reserved by the platform and cannot be used. | format: "int64"; minimum: 1 |
| `description` | string | yes | Transaction type description | maxLength: 30 |
| `credit` | boolean | yes | Indicates whether the transaction type is credit (`true`) or debit (`false`). |  |
| `posted_transaction` | boolean | yes | Indicates whether transactions are posted on statements (`true`) or not (`false`). Set to `false` for zero balance integrations. |  |

##### Response 400

400 Example `invalidRequestBody` (Invalid request body):

```json
{
  "message": "Invalid request body",
  "error": "Invalid request body",
  "code": "WTRC00005"
}
```

##### Response 409

409 Example `ttDoesntMatch` (Transaction type ID already exists):

```json
{
  "message": "Transaction type ID already exists",
  "error": "Transaction type ID already exists",
  "code": "WTRC05001"
}
```

409 Example `ttReservedByPlatform` (Transaction type ID is reserved by platform):

```json
{
  "message": "The provided transaction_type_id is reserved by the platform and cannot be used",
  "error": "The provided transaction_type_id is reserved by the platform and cannot be used",
  "code": "WTRC08001"
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
| 400 | `WTRC00005` | Invalid request body |
| 409 | `WTRC05001` | Transaction type ID already exists |
| 409 | `WTRC08001` | The provided transaction_type_id is reserved by the platform and cannot be used |
| 500 | `ETRC00001` | Internal processing error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `transaction-types-creation-1` | https://developers.pismo.io/events/docs/transaction-types-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-penalties-for-cd-accounts`, `KU-CORE-transactiontypes`, `KU-CRED-full-balance-credit-program`, `KU-EVT-transactions-data-events`, `KU-PAY-installments-payment`, `KU-PAY-payments-configurations`, `KU-SELL-managing-merchant-transactions`.

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=GET path=/v1/transaction-type/{transactionTypeId} operationId=GetTransactionTypeById -->
### `GET /v1/transaction-type/{transactionTypeId}` — Get transaction type

- **operationId:** `GetTransactionTypeById`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a transaction type, given the transaction type ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `transactionTypeId` | path | yes | integer | Transaction type ID. | format: "int64"; example: 101010 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `TransactionType`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Transaction type ID | format: "int64" |
| `description` | string | no | Transaction type description | maxLength: 30 |
| `credit` | boolean | no | Indicates if the transaction type is a credit or debit operation. |  |
| `posted_transaction` | boolean | no | Indicates whether transactions are posted on statements (`true`) or not (`false`). |  |
| `balance_impact_id` | integer | no | Balance impact ID | format: "int64" |
| `category` | string | no | Transaction type category |  |

##### Response 400

400 Example `ttIdNotInformed` (Transaction type ID not provided):

```json
{
  "message": "Transaction type ID not provided",
  "error": "Transaction type ID not provided",
  "code": "WTRC05004"
}
```

##### Response 404

404 Example `ttNotFound` (Transaction type not found):

```json
{
  "message": "Transaction type not found",
  "error": "Transaction type not found",
  "code": "WTRC05005"
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
| 400 | `WTRC05004` | Transaction type ID not provided |
| 404 | `WTRC05005` | Transaction type not found |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-transactions-overview`.

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=PATCH path=/v1/transaction-types/{transactionTypeId} operationId=PatchTransactionType -->
### `PATCH /v1/transaction-types/{transactionTypeId}` — Update transaction type

- **operationId:** `PatchTransactionType`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Updates a transaction type description, given the transaction type ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `transactionTypeId` | path | yes | integer | Transaction type ID. | format: "int64"; example: 101010 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `TransactionTypePatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | yes | Transaction type description. | maxLength: 30 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `TransactionTypeResult`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeId`) | yes | Transaction type ID. Certain IDs are reserved by the platform and cannot be used. | format: "int64"; minimum: 1 |
| `description` | string | yes | Transaction type description | maxLength: 30 |
| `credit` | boolean | yes | Indicates whether the transaction type is credit (`true`) or debit (`false`). |  |
| `posted_transaction` | boolean | yes | Indicates whether transactions are posted on statements (`true`) or not (`false`). Set to `false` for zero balance integrations. |  |

##### Response 400

400 Example `invalidRequestBody` (Invalid request body):

```json
{
  "message": "Invalid request body",
  "error": "Invalid request body",
  "code": "WTRC00005"
}
```

##### Response 409

409 Example `ttIdAlreadyExist` (Transaction type ID already exists):

```json
{
  "message": "Transaction type ID already exists",
  "error": "Transaction type ID already exists",
  "code": "WTRC05001"
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
| 400 | `WTRC00005` | Invalid request body |
| 409 | `WTRC05001` | Transaction type ID already exists |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-transactions-overview`.

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=PATCH path=/v1/programs/{programId}/transaction-types/{transactionTypeId} operationId=PatchProgramTransactionType -->
### `PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId}` — Update program transaction type description

- **operationId:** `PatchProgramTransactionType`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the description of a transaction type for a specific program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64" |
| `transactionTypeId` | path | yes | integer | Transaction type ID. | format: "int64"; example: 101010 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `ProgramTransactionTypePatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | yes | Transaction type description | maxLength: 30 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 400

400 Example `invalidRequestParameters` (Invalid request parameters):

```json
{
  "message": "Invalid request parameters",
  "error": "Invalid request parameters",
  "code": "WTRC00003"
}
```

400 Example `invalidRequestBody` (Invalid request body):

```json
{
  "message": "Invalid request body",
  "error": "Invalid request body",
  "code": "WTRC00005"
}
```

##### Response 404

404 Example `pttNotFound` (Program transaction type not found):

```json
{
  "message": "Program transaction type not found",
  "error": "Program transaction type not found",
  "code": "WTRC03001"
}
```

##### Response 500

500 Example `pttNotFound` (Could not perform program transaction type operation):

```json
{
  "message": "Could not perform program transaction type operation",
  "error": "Could not perform program transaction type operation",
  "code": "ETRC03002"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WTRC00003` | Invalid request parameters |
| 400 | `WTRC00005` | Invalid request body |
| 404 | `WTRC03001` | Program transaction type not found |
| 500 | `ETRC03002` | Could not perform program transaction type operation |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-transactions-overview`, `KU-CRED-full-balance-credit-program`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Error description. |  |
| `error` | string | no | Error description. |  |
| `code` | string | no | Code description. |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Transactions.yaml` | tag `Transaction types`: GET /v1/transaction-types, POST /v1/transaction-types, GET /v1/transaction-type/{transactionTypeId}, PATCH /v1/transaction-types/{transactionTypeId}, PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId} | https://github.com/PismoDevEx/pismo-api-specs | `203c22b2f02c342b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-penalties-for-cd-accounts` — Penalties and taxes for CD accounts
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-CORE-transactiontypes` — Transaction types
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wtrc` — Error codes: WTRC
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-EVT-transactions-data-events` — Core platform - Transactions
- `KU-PAY-installments-payment` — Installments payment
- `KU-PAY-payments-configurations` — Payments configurations
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
