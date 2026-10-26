---
ku_id: KU-API-revolving-credit-configurations--additional-accrual-type-configurations
title: 'API reference: Revolving credit - Configurations — Additional accrual type configurations'
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
- postAccrualTypesConfigurations
- deleteAccrualTypesConfigurations
related_kus:
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Configurations — Additional accrual type configurations

**KU ID:** `KU-API-revolving-credit-configurations--additional-accrual-type-configurations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Additional accrual type configurations` in `api-specs/Revolving_credit_-_Configurations.yaml` (“Revolving credit - Configurations”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to enable additional accrual type configurations at program level

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` | `postAccrualTypesConfigurations` | Enable additional configurations on accrual types | no |
| `DELETE /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` | `deleteAccrualTypesConfigurations` | Disable additional configuration on accrual types | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=POST path=/v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations operationId=postAccrualTypesConfigurations -->
### `POST /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` — Enable additional configurations on accrual types

- **operationId:** `postAccrualTypesConfigurations`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Additional accrual type configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enable additional configurations on accrual types. Any additional configuration that you enable modifies the default accrual behavior.
>
> Specify configurations to enable by listing them as an array in the `configurations` body parameter. The following configuration is available.
> - `ONCE_AFTER_TRANSACTION_DUE_DATE`: By default, accruals on transactions with this transaction category occur on a daily basis. If this additional configuration is enabled, then, for each transaction, the accrual is calculated only once on the transaction due date.
>
> **Note:** Unlike other rates that you define using transaction categories or accrual type rates, when you enable the `ONCE_AFTER_TRANSACTION_DUE_DATE` configuration on an accrual type, the rate you define for that type is <i>not</i> divided by the interest rate period before it's applied.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 5689 |
| `transactionCategoryId` | path | yes | integer | Program transaction category ID | example: 2 |
| `accrualType` | path | yes | string | Accrual type | enum: ["WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX", "REFINANCING", "OVERDUE", "FINE"]; example: "WITHDRAWAL_INTEREST" |
| `periodToCalculate` | path | yes | string | Period to calculate the accruals | enum: ["UNTIL_DUE_DATE", "AFTER_DUE_DATE"]; example: "UNTIL_DUE_DATE" |

#### Request body

Required: no

**Content type `application/json`** — schema: oneOf: object (schema `PostAccrualTypeConfigurationsRequest`)

_oneOf option 1: schema `PostAccrualTypeConfigurationsRequest`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `configurations` | array of string (schema `AccrualTypesConfigurations`) | yes | Array of additional accrual type configurations | items.enum: ["ONCE_AFTER_TRANSACTION_DUE_DATE"] |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `PostAccrualTypeConfigurationsResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 409 | The specified resource status conflicts with the current request. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `configurations` | array of string (schema `AccrualTypesConfigurations`) | yes | Array of additional accrual type configurations | items.enum: ["ONCE_AFTER_TRANSACTION_DUE_DATE"] |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]."
}
```

##### Response 404

404 Example `Invalid accrual type configuration passed`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The Accrual type configuration provided (MY_INVALID_CONFIGURATION) does not exist"
}
```

404 Example `Program not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The program ID XXXXXXXX in the path not found"
}
```

404 Example `Transaction category not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The transaction category XXXXXXXX does not exist or does not belong to the provided program."
}
```

404 Example `Accrual type not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The accrual type XXXXXXXX does not exist or does not belong to the provided program."
}
```

404 Example `Period to calculate not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The periodToCalculate (XXXXXXXX) not found"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0001` | Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]. |
| 404 | `EX0004` | Validation Error: The Accrual type configuration provided (MY_INVALID_CONFIGURATION) does not exist |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=DELETE path=/v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations operationId=deleteAccrualTypesConfigurations -->
### `DELETE /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations` — Disable additional configuration on accrual types

- **operationId:** `deleteAccrualTypesConfigurations`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Additional accrual type configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Disable additional configurations on accrual types. Any additional configuration that you disable modifies the default accrual behavior.
> Specify configurations to be disabled by listing them as an array in the `configurations` body parameter. The following configurations are available.
> - `ONCE_AFTER_TRANSACTION_DUE_DATE`: If this additional configuration is disabled, accruals on transactions with this transaction category occur on a daily basis.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 5689 |
| `transactionCategoryId` | path | yes | integer | Program transaction category ID | example: 2 |
| `accrualType` | path | yes | string | Accrual type | enum: ["WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX", "REFINANCING", "OVERDUE", "FINE"]; example: "WITHDRAWAL_INTEREST" |
| `periodToCalculate` | path | yes | string | Period to calculate the accruals | enum: ["UNTIL_DUE_DATE", "AFTER_DUE_DATE"]; example: "UNTIL_DUE_DATE" |

#### Request body

Required: no

**Content type `application/json`** — schema: oneOf: object (schema `PostAccrualTypeConfigurationsRequest`)

_oneOf option 1: schema `PostAccrualTypeConfigurationsRequest`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `configurations` | array of string (schema `AccrualTypesConfigurations`) | yes | Array of additional accrual type configurations | items.enum: ["ONCE_AFTER_TRANSACTION_DUE_DATE"] |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 409 | The specified resource status conflicts with the current request. |  |
| 500 | Internal server error |  |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]."
}
```

##### Response 404

404 Example `No configurations to be deleted`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: There are no active TransactionsCategoriesAccrualTypesConfigurations with the data provided."
}
```

404 Example `Invalid accrual type configuration passed`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The Accrual type configuration provided (XXXXXXXX) does not exist"
}
```

404 Example `Program not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The program ID XXXXXXXX in the path was not found"
}
```

404 Example `Transaction category not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The transaction category XXXXXXXX does not exist or does not belong to the provided program."
}
```

404 Example `Accrual type not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The accrual type XXXXXXXX does not exist or does not belong to the provided program."
}
```

404 Example `Period to calculate not found`:

```json
{
  "code": "EX0004",
  "message": "Validation Error: The periodToCalculate (XXXXXXXX) not found"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0001` | Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]. |
| 404 | `EX0004` | Validation Error: There are no active TransactionsCategoriesAccrualTypesConfigurations with the data provided. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;409;500`, has examples `True`, emits events `0`, deprecated `False`.

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
| `api-specs/Revolving_credit_-_Configurations.yaml` | tag `Additional accrual type configurations`: POST /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations, DELETE /v1/programs/{programId}/transaction-category-id/{transactionCategoryId}/accrual-type/{accrualType}/period-to-calculate/{periodToCalculate}/configurations | https://github.com/PismoDevEx/pismo-api-specs | `5037a85683d87b9b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-ex` — Error codes: EX
