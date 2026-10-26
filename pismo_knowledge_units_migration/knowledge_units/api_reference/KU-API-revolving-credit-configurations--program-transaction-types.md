---
ku_id: KU-API-revolving-credit-configurations--program-transaction-types
title: 'API reference: Revolving credit - Configurations — Program transaction types'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Configurations.yaml
  sha256: 5037a85683d87b9b20fa73777d80641130e25e59a6f3e80676d6996df9b88d15
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
- createProgramTransactionType
related_kus:
- KU-CARD-program-transaction-types
- KU-CARD-transaction-categories
- KU-CC-processing-codes
- KU-CRED-configuring-accrual-rates
- KU-CRED-full-balance-credit-program
- KU-CRED-managing-the-charge-order-for-debit-transactions
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Configurations — Program transaction types

**KU ID:** `KU-API-revolving-credit-configurations--program-transaction-types` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Program transaction types` in `api-specs/Revolving_credit_-_Configurations.yaml` (“Revolving credit - Configurations”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to associate debit transaction types with a program and a transaction category.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/programs/{programId}/program-transaction-types` | `createProgramTransactionType` | Create program transaction type | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=POST path=/v1/programs/{programId}/program-transaction-types operationId=createProgramTransactionType -->
### `POST /v1/programs/{programId}/program-transaction-types` — Create program transaction type

- **operationId:** `createProgramTransactionType`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Program transaction types`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> A program transaction type is used to associate a transaction type with a transaction category. It can also be used to set the charge order. For more information, refer to [Using configurable entities](doc:full-balance-credit-program#using-configurable-entities).
>
> **Note:** Only debit transactions and transactions that impact the statements can be used to create program transaction types. Use the [List transaction types](ref:searchtransactiontypes) endpoint to see if a transaction type is a debit (`credit` = `false`) and if it impacts the statement (`posted_transaction` = `true`).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 5689 |

#### Request body

Required: no

**Content type `application/json`** — schema: oneOf: object (schema `ProgramsTransactionsTypesRequest`)

_oneOf option 1: schema `ProgramsTransactionsTypesRequest`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeID`) | yes | Transaction type ID | example: 101 |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | yes | Transaction category ID | example: 1237456 |
| `charge_order` | integer (schema `ChargeOrder`) | no | Used to determine the priority order when discharging transaction balances. 1 is the highest priority. | example: 2 |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ProgramsTransactionsTypesResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_transaction_type_id` | integer (schema `ProgramTransactionTypeID`) | yes | Program transaction type ID | example: 156781 |
| `transaction_type_id` | integer (schema `TransactionTypeID`) | yes | Transaction type ID | example: 101 |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | yes | Transaction category ID | example: 1237456 |
| `charge_order` | integer (schema `ChargeOrder`) | no | Used to determine the priority order when discharging transaction balances. 1 is the highest priority. | example: 2 |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]."
}
```

##### Response 404

404 Example `Statement not found`:

```json
{
  "code": "EX0002",
  "message": "Program operationID does not exit."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0001` | Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]. |
| 404 | `EX0002` | Program operationID does not exit. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-program-transaction-types`, `KU-CARD-transaction-categories`, `KU-CC-processing-codes`, `KU-CRED-configuring-accrual-rates`, `KU-CRED-full-balance-credit-program`, `KU-CRED-managing-the-charge-order-for-debit-transactions`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Standard error code | example: "1020030" |
| `message` | string | no | Error message | example: "An error occurred when attempting to execute request." |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Configurations.yaml` | tag `Program transaction types`: POST /v1/programs/{programId}/program-transaction-types | https://github.com/PismoDevEx/pismo-api-specs | `5037a85683d87b9b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-program-transaction-types` — Program transaction types
- `KU-CARD-transaction-categories` — Transaction categories
- `KU-CC-processing-codes` — Control Center processing codes, transaction types and general ledger accounts
- `KU-CRED-configuring-accrual-rates` — Configuring accrual rates
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-CRED-managing-the-charge-order-for-debit-transactions` — Managing the charge order for debit transactions
- `KU-ERR-codes-ex` — Error codes: EX
