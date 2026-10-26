---
ku_id: KU-API-revolving-credit-configurations--program-accrual-rates
title: 'API reference: Revolving credit - Configurations — Program accrual rates'
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
- listProgramAccrualTypesRates
- postAccrualTypesRates
- deleteAccrualTypesRates
related_kus:
- KU-CRED-accrual-rate-types-and-limits
- KU-CRED-configuring-a-sellos-tax
- KU-CRED-configuring-accrual-rates
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Configurations — Program accrual rates

**KU ID:** `KU-API-revolving-credit-configurations--program-accrual-rates` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Program accrual rates` in `api-specs/Revolving_credit_-_Configurations.yaml` (“Revolving credit - Configurations”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to set up accrual rates at the program level.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/programs/{programId}/accrual-type-rates` | `listProgramAccrualTypesRates` | List program accrual rates | no |
| `POST /v1/programs/{programId}/accrual-type-rates` | `postAccrualTypesRates` | Configure program accrual rates | no |
| `DELETE /v1/programs/{programId}/accrual-type-rates` | `deleteAccrualTypesRates` | Delete program accrual rates | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=GET path=/v1/programs/{programId}/accrual-type-rates operationId=listProgramAccrualTypesRates -->
### `GET /v1/programs/{programId}/accrual-type-rates` — List program accrual rates

- **operationId:** `listProgramAccrualTypesRates`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Program accrual rates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieves a list of accrual rates configured at the program level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 5689 |
| `perPage` | query | no | integer | Number of items per page | default: 100; example: 100 |
| `page` | query | no | integer | Current page | default: 1; example: 1 |
| `transactionCategoryId` | query | no | integer | Program transaction category ID | example: 2 |
| `accrualType` | query | no | string | Accrual type | enum: ["WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX", "REFINANCING", "OVERDUE", "FINE"]; example: "WITHDRAWAL_INTEREST" |
| `periodToCalculate` | query | no | string | Period to calculate the accruals | enum: ["UNTIL_DUE_DATE", "AFTER_DUE_DATE"]; example: "UNTIL_DUE_DATE" |
| `validityToCalculate` | query | no | string | When the rate is used to calculate the accrual. The possible values are:<br>- IMMEDIATE — The rate is used to calculate the next generated accruals.<br>- DUEDATE — The rate is used to calculate accruals only after the next due date.<br> | enum: ["IMMEDIATE", "DUEDATE"]; example: "IMMEDIATE" |
| `isDeleted` | query | no | boolean | Filter by status | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `GetAllProgramAccrualTypesRatesResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPageNumber`) | yes | Current page number | default: 1; example: 1 |
| `per_page` | integer (schema `ItemsPerPage`) | yes | Number of items per page | default: 1; minLength: 1; example: 10 |
| `total_items` | integer (schema `NumberOfItems`) | yes | Number of items | example: 50 |
| `items_on_page` | integer (schema `ItemsOnCurrentPage`) | yes | Number of items on the current page | example: 10 |
| `pages` | integer (schema `NumberOfPages`) | yes | Number of pages | example: 5 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Indicates if the current page is the last page | example: false |
| `items` | array of object (schema `AccountAccrualTypesRatesResponse`) (schema `ArrayOfInterestRateObjects`) | no | Array of interest rate objects |  |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0001` | Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=POST path=/v1/programs/{programId}/accrual-type-rates operationId=postAccrualTypesRates -->
### `POST /v1/programs/{programId}/accrual-type-rates` — Configure program accrual rates

- **operationId:** `postAccrualTypesRates`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Program accrual rates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Configure accrual rates at the program level. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 5689 |

#### Request body

Required: no

**Content type `application/json`** — schema: oneOf: object (schema `ProgramAccrualTypesRatesRequest`)

_oneOf option 1: schema `ProgramAccrualTypesRatesRequest`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | yes | Transaction category ID | example: 1237456 |
| `accrual_type` | string (schema `ProgramAccrualType`) | yes | Accrual type. The possible values at the program level are:<br>- `WITHDRAWAL_INTEREST` — Interest on a withdrawal<br>- `BILLPAYMENT_INTEREST` — Interest on a bill payment<br>- `OVERDRAFT_INTEREST` — Interest on an overdraft<br>- `FINANCIAL_TAX` — Financial tax<br>- `REFINANCING` — Refinancing charge<br>- `OVERDUE` — Overdue charge<br>- `FINE` — Overdue fine<br> | enum: ["WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX", "REFINANCING", "OVERDUE", "FINE"]; example: "WITHDRAWAL_INTEREST" |
| `period_to_calculate` | string (schema `PeriodToCalculate`) | yes | Period to calculate the accrual<br><br>`UNTIL_DUE_DATE`—The period extends from the transaction date plus one day to the due date.<br>`AFTER_DUE_DATE`—The period extends from the due date plus one day to the current date.<br><br>**Note:** If an accrual needs to start at the transaction date and continue past the due date, then two accrual rates need to be created—one with `UNTIL_DUE_DATE` and another with `AFTER_DUE_DATE`.      <br> |  |
| `default_rate` | number (schema `DefaultAccrualRate`) | no | Rate used to calculate the accrual when the account is not overdue.<br><br>**Notes:**<br>- If you don't provide a value for this field, you must provide a value for `rate_if_overdue`.<br>- If you provide a value for `default_rate`, but not `rate_if_overdue`, then the Pismo platform only calculates the interest if the account <i>is not</i> overdue. If you provide a value for `rate_if_overdue`, but not `default_rate`, then the platform only calculates the interest when the account <i>is</i> overdue. If you want the platform to calculate the interest in both cases, you must provide values for both fields.<br> | format: "double"; example: 2 |
| `rate_if_overdue` | number (schema `AccrualRateIfOverdue`) | no | Rate used to calculate the accrual when the account is overdue.<br><br>**Notes:**<br>- If you don't provide a value for this field, you must provide a value for `default_rate`.<br>- If you provide a value for `default_rate`, but not `rate_if_overdue`, then the Pismo platform only calculates the interest if the account <i>is not</i> overdue. If you provide a value for `rate_if_overdue`, but not `default_rate`, then the platform only calculates the interest when the account <i>is</i> overdue. If you want the platform to calculate the interest in both cases, you must provide values for both fields.<br> | format: "double"; example: 3 |
| `validity_to_calculate` | string (schema `ValidityToCalculate`) | yes | When the rate is used to calculate the accrual. The possible values are:<br>- `IMMEDIATE` — The rate is used to calculate the next generated accruals.<br>- `DUEDATE` — The rate is used to calculate accruals only after the next due date.<br> | enum: ["IMMEDIATE", "DUEDATE"]; example: "IMMEDIATE" |
| `ranges` | array of object (schema `AccrualRateRange`) (schema `AccrualRateRanges`) | no | List of accrual rate ranges. Which range applies depends on a comparison of the last amount due with `amount_due_lower_limit`. For example, suppose you execute the endpoint with the following parameter values.<br><pre><br>{<br>  'transaction_category_id': 107178,<br>  'accrual_type': 'WITHDRAWAL_INTEREST',<br>  'period_to_calculate: 'AFTER_DUE_DATE',<br>  'default_rate': 10.70,<br>  'rate_if_overdue': 12.70,<br>  'validity_to_calculate': 'IMMEDIATE',<br>  'ranges': [<br>      {<br>          'amount_due_lower_limit': 1000,<br>          'default_rate': 10.00,<br>          'rate_if_overdue': 8.123456<br>      },<br>      {<br>          'amount_due_lower_limit': 3000,<br>          'default_rate': 9.25,<br>          'rate_if_overdue': 7.351451<br>      }<br>  ]<br>}<br></pre><br><br>If the last amount due is 4000, then both of above ranges are valid, but the `amount_due_lower_limit` with 3000 is the closest, so the values for `default_rate` and `rate_if_overdue` in the second range are used to calculate accruals.<br><br>**Notes:**<br><br>- Either `default_rate`, `rate_if_overdue`, or both must be provided in each range.<br><br>- The rate division by total days is not affected by whether or not ranges are defined.<br><br>- The **Overdue strategy start** program parameter also impacts the amount due. For more information, refer to the entry for that parameter in [Program parameters](doc:program-parameters-reference-table).<br> |  |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `ProgramAccrualTypesRatesResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 409 | The specified resource status conflicts with the current request. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | yes | Transaction category ID | example: 1237456 |
| `accrual_type` | string (schema `ProgramAccrualType`) | yes | Accrual type. The possible values at the program level are:<br>- `WITHDRAWAL_INTEREST` — Interest on a withdrawal<br>- `BILLPAYMENT_INTEREST` — Interest on a bill payment<br>- `OVERDRAFT_INTEREST` — Interest on an overdraft<br>- `FINANCIAL_TAX` — Financial tax<br>- `REFINANCING` — Refinancing charge<br>- `OVERDUE` — Overdue charge<br>- `FINE` — Overdue fine<br> | enum: ["WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX", "REFINANCING", "OVERDUE", "FINE"]; example: "WITHDRAWAL_INTEREST" |
| `period_to_calculate` | string (schema `PeriodToCalculate`) | yes | Period to calculate the accrual<br><br>`UNTIL_DUE_DATE`—The period extends from the transaction date plus one day to the due date.<br>`AFTER_DUE_DATE`—The period extends from the due date plus one day to the current date.<br><br>**Note:** If an accrual needs to start at the transaction date and continue past the due date, then two accrual rates need to be created—one with `UNTIL_DUE_DATE` and another with `AFTER_DUE_DATE`.      <br> |  |
| `validity_to_calculate` | string (schema `ValidityToCalculate`) | yes | When the rate is used to calculate the accrual. The possible values are:<br>- `IMMEDIATE` — The rate is used to calculate the next generated accruals.<br>- `DUEDATE` — The rate is used to calculate accruals only after the next due date.<br> | enum: ["IMMEDIATE", "DUEDATE"]; example: "IMMEDIATE" |
| `default_rate` | number (schema `DefaultAccrualRate`) | no | Rate used to calculate the accrual when the account is not overdue.<br><br>**Notes:**<br>- If you don't provide a value for this field, you must provide a value for `rate_if_overdue`.<br>- If you provide a value for `default_rate`, but not `rate_if_overdue`, then the Pismo platform only calculates the interest if the account <i>is not</i> overdue. If you provide a value for `rate_if_overdue`, but not `default_rate`, then the platform only calculates the interest when the account <i>is</i> overdue. If you want the platform to calculate the interest in both cases, you must provide values for both fields.<br> | format: "double"; example: 2 |
| `rate_if_overdue` | number (schema `AccrualRateIfOverdue`) | no | Rate used to calculate the accrual when the account is overdue.<br><br>**Notes:**<br>- If you don't provide a value for this field, you must provide a value for `default_rate`.<br>- If you provide a value for `default_rate`, but not `rate_if_overdue`, then the Pismo platform only calculates the interest if the account <i>is not</i> overdue. If you provide a value for `rate_if_overdue`, but not `default_rate`, then the platform only calculates the interest when the account <i>is</i> overdue. If you want the platform to calculate the interest in both cases, you must provide values for both fields.<br> | format: "double"; example: 3 |
| `ranges` | array of object (schema `AccrualRateRange`) (schema `AccrualRateRanges`) | no | List of accrual rate ranges. Which range applies depends on a comparison of the last amount due with `amount_due_lower_limit`. For example, suppose you execute the endpoint with the following parameter values.<br><pre><br>{<br>  'transaction_category_id': 107178,<br>  'accrual_type': 'WITHDRAWAL_INTEREST',<br>  'period_to_calculate: 'AFTER_DUE_DATE',<br>  'default_rate': 10.70,<br>  'rate_if_overdue': 12.70,<br>  'validity_to_calculate': 'IMMEDIATE',<br>  'ranges': [<br>      {<br>          'amount_due_lower_limit': 1000,<br>          'default_rate': 10.00,<br>          'rate_if_overdue': 8.123456<br>      },<br>      {<br>          'amount_due_lower_limit': 3000,<br>          'default_rate': 9.25,<br>          'rate_if_overdue': 7.351451<br>      }<br>  ]<br>}<br></pre><br><br>If the last amount due is 4000, then both of above ranges are valid, but the `amount_due_lower_limit` with 3000 is the closest, so the values for `default_rate` and `rate_if_overdue` in the second range are used to calculate accruals.<br><br>**Notes:**<br><br>- Either `default_rate`, `rate_if_overdue`, or both must be provided in each range.<br><br>- The rate division by total days is not affected by whether or not ranges are defined.<br><br>- The **Overdue strategy start** program parameter also impacts the amount due. For more information, refer to the entry for that parameter in [Program parameters](doc:program-parameters-reference-table).<br> |  |
| `created_at` | string (schema `CreatedAt`) | yes | Date created, format = yyyy-mm-ddThh:mm:ssZ | example: "2023-08-18T20:53:27.498Z" |
| `deleted_at` | string (schema `DeletedAt`) | no | Date deleted, format = yyyy-mm-ddThh:mm:ssZ | example: "2023-10-10T10:50:18.212Z" |
| `accrual_type_rate_id` | integer (schema `AccrualTypeRateID`) | no | Account accrual type rate ID | example: 1237456 |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0001` | Validation Error. Details: Can't find [BalanceAccount] with params: [AccountID: XXXXXX, OrgID: TN-XXXXXXXXXXX-XXXX-XXXX-XXXXXXXXXX]. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-accrual-rate-types-and-limits`, `KU-CRED-configuring-a-sellos-tax`, `KU-CRED-configuring-accrual-rates`.

<!-- op: spec=api-specs/Revolving_credit_-_Configurations.yaml method=DELETE path=/v1/programs/{programId}/accrual-type-rates operationId=deleteAccrualTypesRates -->
### `DELETE /v1/programs/{programId}/accrual-type-rates` — Delete program accrual rates

- **operationId:** `deleteAccrualTypesRates`
- **Specification:** `api-specs/Revolving_credit_-_Configurations.yaml` (Revolving credit - Configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-configurations`
- **Tags:** `Program accrual rates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Deletes an accrual rate that's configured for a program.
> If only `programId` is provided, all program accrual rates are deleted for that program.
> You can use the optional parameters `transactionCategoryId`, `accrualType`, and `periodToCalculate` to specify a subset of the program accrual rates that you want to delete.
> For example, if you provide values for `transactionCategoryId`, `accrualType`, and `periodToCalculate`, then all program accrual rates configured for the specified program, transaction category, accrual type, and period to calculate are deleted.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 5689 |
| `transactionCategoryId` | query | no | integer | Program transaction category ID | example: 2 |
| `accrualType` | query | no | string | Accrual type | enum: ["WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX", "REFINANCING", "OVERDUE", "FINE"]; example: "WITHDRAWAL_INTEREST" |
| `periodToCalculate` | query | no | string | Period to calculate the accruals | enum: ["UNTIL_DUE_DATE", "AFTER_DUE_DATE"]; example: "UNTIL_DUE_DATE" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountAccrualTypesRatesResponse -->
### Schema `AccountAccrualTypesRatesResponse`

Pointer: `#/components/schemas/AccountAccrualTypesRatesResponse`. Type: object (schema `AccountAccrualTypesRatesResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | yes | Transaction category ID | example: 1237456 |
| `accrual_type` | string (schema `AccountAccrualType`) | yes | Accrual type at the account level. The most commonly used values are:<br>- `WITHDRAWAL_INTEREST`—Interest on a withdrawal<br>- `BILLPAYMENT_INTEREST`—Interest on a bill payment<br>- `OVERDRAFT_INTEREST`—Interest on an overdraft<br>- `FINANCIAL_TAX`—Financial tax<br> | example: "WITHDRAWAL_INTEREST" |
| `period_to_calculate` | string (schema `PeriodToCalculate`) | yes | Period to calculate the accrual<br><br>`UNTIL_DUE_DATE`—The period extends from the transaction date plus one day to the due date.<br>`AFTER_DUE_DATE`—The period extends from the due date plus one day to the current date.<br><br>**Note:** If an accrual needs to start at the transaction date and continue past the due date, then two accrual rates need to be created—one with `UNTIL_DUE_DATE` and another with `AFTER_DUE_DATE`.      <br> |  |
| `default_rate` | number (schema `DefaultAccrualRate`) | no | Rate used to calculate the accrual when the account is not overdue.<br><br>**Notes:**<br>- If you don't provide a value for this field, you must provide a value for `rate_if_overdue`.<br>- If you provide a value for `default_rate`, but not `rate_if_overdue`, then the Pismo platform only calculates the interest if the account <i>is not</i> overdue. If you provide a value for `rate_if_overdue`, but not `default_rate`, then the platform only calculates the interest when the account <i>is</i> overdue. If you want the platform to calculate the interest in both cases, you must provide values for both fields.<br> | format: "double"; example: 2 |
| `rate_if_overdue` | number (schema `AccrualRateIfOverdue`) | no | Rate used to calculate the accrual when the account is overdue.<br><br>**Notes:**<br>- If you don't provide a value for this field, you must provide a value for `default_rate`.<br>- If you provide a value for `default_rate`, but not `rate_if_overdue`, then the Pismo platform only calculates the interest if the account <i>is not</i> overdue. If you provide a value for `rate_if_overdue`, but not `default_rate`, then the platform only calculates the interest when the account <i>is</i> overdue. If you want the platform to calculate the interest in both cases, you must provide values for both fields.<br> | format: "double"; example: 3 |
| `ranges` | array of object (schema `AccrualRateRange`) (schema `AccrualRateRanges`) | no | List of accrual rate ranges. Which range applies depends on a comparison of the last amount due with `amount_due_lower_limit`. For example, suppose you execute the endpoint with the following parameter values.<br><pre><br>{<br>  'transaction_category_id': 107178,<br>  'accrual_type': 'WITHDRAWAL_INTEREST',<br>  'period_to_calculate: 'AFTER_DUE_DATE',<br>  'default_rate': 10.70,<br>  'rate_if_overdue': 12.70,<br>  'validity_to_calculate': 'IMMEDIATE',<br>  'ranges': [<br>      {<br>          'amount_due_lower_limit': 1000,<br>          'default_rate': 10.00,<br>          'rate_if_overdue': 8.123456<br>      },<br>      {<br>          'amount_due_lower_limit': 3000,<br>          'default_rate': 9.25,<br>          'rate_if_overdue': 7.351451<br>      }<br>  ]<br>}<br></pre><br><br>If the last amount due is 4000, then both of above ranges are valid, but the `amount_due_lower_limit` with 3000 is the closest, so the values for `default_rate` and `rate_if_overdue` in the second range are used to calculate accruals.<br><br>**Notes:**<br><br>- Either `default_rate`, `rate_if_overdue`, or both must be provided in each range.<br><br>- The rate division by total days is not affected by whether or not ranges are defined.<br><br>- The **Overdue strategy start** program parameter also impacts the amount due. For more information, refer to the entry for that parameter in [Program parameters](doc:program-parameters-reference-table).<br> |  |
| `validity_to_calculate` | string (schema `ValidityToCalculate`) | yes | When the rate is used to calculate the accrual. The possible values are:<br>- `IMMEDIATE` — The rate is used to calculate the next generated accruals.<br>- `DUEDATE` — The rate is used to calculate accruals only after the next due date.<br> | enum: ["IMMEDIATE", "DUEDATE"]; example: "IMMEDIATE" |
| `account_accrual_type_rate_id` | integer (schema `AccrualTypeRateID`) | no | Account accrual type rate ID | example: 1237456 |
| `account_id` | integer (schema `AccountID`) | no | Account  ID | example: 1237456 |
| `created_at` | string (schema `CreatedAt`) | no | Date created, format = yyyy-mm-ddThh:mm:ssZ | example: "2023-08-18T20:53:27.498Z" |
| `deleted_at` | string (schema `DeletedAt`) | no | Date deleted, format = yyyy-mm-ddThh:mm:ssZ | example: "2023-10-10T10:50:18.212Z" |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Standard error code | example: "1020030" |
| `message` | string | no | Error message | example: "An error occurred when attempting to execute request." |

<!-- schema: #/components/schemas/AccrualRateRange -->
### Schema `AccrualRateRange`

Pointer: `#/components/schemas/AccrualRateRange`. Type: object (schema `AccrualRateRange`).

> Accrual rate ranges

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount_due_lower_limit` | number (schema `AmountDueLowerLimit`) | yes | Lower limit for the range. Must be greater than zero. If the amount due is greater than or equal to this amount, `default_rate` and `rate_if_overdue` apply. | format: "double"; example: 4000 |
| `default_rate` | number (schema `DefaultAccrualRate`) | no | Rate used to calculate the accrual when the account is not overdue.<br><br>**Notes:**<br>- If you don't provide a value for this field, you must provide a value for `rate_if_overdue`.<br>- If you provide a value for `default_rate`, but not `rate_if_overdue`, then the Pismo platform only calculates the interest if the account <i>is not</i> overdue. If you provide a value for `rate_if_overdue`, but not `default_rate`, then the platform only calculates the interest when the account <i>is</i> overdue. If you want the platform to calculate the interest in both cases, you must provide values for both fields.<br> | format: "double"; example: 2 |
| `rate_if_overdue` | number (schema `AccrualRateIfOverdue`) | no | Rate used to calculate the accrual when the account is overdue.<br><br>**Notes:**<br>- If you don't provide a value for this field, you must provide a value for `default_rate`.<br>- If you provide a value for `default_rate`, but not `rate_if_overdue`, then the Pismo platform only calculates the interest if the account <i>is not</i> overdue. If you provide a value for `rate_if_overdue`, but not `default_rate`, then the platform only calculates the interest when the account <i>is</i> overdue. If you want the platform to calculate the interest in both cases, you must provide values for both fields.<br> | format: "double"; example: 3 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Configurations.yaml` | tag `Program accrual rates`: GET /v1/programs/{programId}/accrual-type-rates, POST /v1/programs/{programId}/accrual-type-rates, DELETE /v1/programs/{programId}/accrual-type-rates | https://github.com/PismoDevEx/pismo-api-specs | `5037a85683d87b9b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-accrual-rate-types-and-limits` — Accrual rate types, accrual-free transaction types and accrual-day limits
- `KU-CRED-configuring-a-sellos-tax` — Configuring a sellos tax
- `KU-CRED-configuring-accrual-rates` — Configuring accrual rates
- `KU-ERR-codes-ex` — Error codes: EX
