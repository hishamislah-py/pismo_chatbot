---
ku_id: KU-API-revolving-credit-statements--account-transaction-categories
title: 'API reference: Revolving credit - Statements — Account transaction categories'
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
- getAccountsTransactionsInterest_1
- saveAccountTransactionInterest
- cancelAccountTransactionCategory
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-transaction-categories
- KU-CRED-configuring-accrual-rates
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Account transaction categories

**KU ID:** `KU-API-revolving-credit-statements--account-transaction-categories` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Account transaction categories` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Account transaction category endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` | `getAccountsTransactionsInterest_1` | List account transaction category rates | no |
| `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` | `saveAccountTransactionInterest` | Create or update account transaction category | no |
| `DELETE /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId}` | `cancelAccountTransactionCategory` | Cancel account transaction category | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/accounts/{accountId}/accounts-transactions-categories operationId=getAccountsTransactionsInterest_1 -->
### `GET /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` — List account transaction category rates

- **operationId:** `getAccountsTransactionsInterest_1`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Account transaction categories`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List all account transaction category rates, canceled or active. 
> An active rate has the attribute `cancelled_at` set to `null`. 
> Since there can be more than one account transaction category per account, there might be more than one active rate.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `program-id` | header | yes | string | Program ID | example: "1233" |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `AccountTransactionCategoryListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `AccountTransactionCategoryResponse`) | no |  |  |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-transaction-categories`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=POST path=/statements-v2/v1/accounts/{accountId}/accounts-transactions-categories operationId=saveAccountTransactionInterest -->
### `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` — Create or update account transaction category

- **operationId:** `saveAccountTransactionInterest`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Account transaction categories`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create or update a account transaction category.
>
> If an existing account transaction category is found (same `account_id` and `transaction_category_id`), it is updated. Otherwise, a new one is created.
>
> For an interest rate, for example `fine_rate`, the field `fine_rate` or `fine_rate_multiplier_percent` **must** be passed. You can pass one or the other but not both. This rule applies to all interest rate fields.  However, you can combine fixed amounts and multipliers for different interest rates. Note that zero (0) is considered a valid value. 
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `AccountTransactionCategorySaveRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_category_id` | integer (schema `TransactionCategoryIDForSave`) | yes | Transaction category ID. **Must** be associated with the passed `program_id` and `org_id`. | format: "int64"; example: 1 |
| `description` | string (schema `TransactionCategoryDescription`) | no | Transaction category description | maxLength: 50; example: "purchase" |
| `refinancing_rate_after_due_date` | number (schema `RefinancingRateAfterDueDate`) | no | Interest rate for the accrual type `REFINANCING` if the statement due date is past, but the account is not overdue. (That is, the MAD was paid.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 15.99 |
| `default_rate` | number (schema `DefaultRate`) | no | Interest rate used for the accrual type `OVERDUE` when the statement is past the due date and the MAD has not been paid. (The account is overdue.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 1 |
| `fine_rate` | number (schema `FineRate`) | no | Fine rate. Charged once per transaction when transaction is due. | format: "float"; example: 2 |
| `overdue_rate_after_due_date` | number (schema `OverdueRateAfterDueDate`) | no | Interest rate used for the accrual type `REFINANCING` if the statement due date has passed and the MAD was not paid. <b>Note:</b> If this value is null, `refinancing_rate_after_due_date` is used instead.<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 17.99 |
| `refinancing_rate_after_due_date_multiplier_percent` | number (schema `RefinancingRateAfterDueDateMultiplierPercent`) | no | Percentage multiplier applied to transaction category refinancing rate after due date. 1.5 = 150% of the refinancing rate. | format: "float"; example: 1.5 |
| `default_rate_multiplier_percent` | number (schema `DefaultRateMultiplierPercent`) | no | Percentage multiplier applied to transaction category default rate. 1.7 = 170% of the default rate. | example: 1.7 |
| `fine_rate_multiplier_percent` | number (schema `FineRateMultiplierPercent`) | no | Percentage multiplier applied to transaction category fine rate. For example, 2 = 200% of the fine rate. | format: "float"; example: 2 |
| `overdue_rate_after_due_date_multiplier_percent` | number (schema `OverdueRateAfterDueDateMultiplierPercent`) | no | Multiplier applied to transaction category overdue rate after due date. 0.7 = 70% of the overdue rate. | format: "float"; example: 0.7 |
| `start_cycle` | integer (schema `StartCycleInRequest`) | no | Account cycle in which this interest rate should start being applied. **Must** be greater than or equal to the current account cycle. Enter either this field or `start_date`, but not both. Format = yyyy-mm-dd.<br> | format: "int64"; example: 4 |
| `start_date` | string (schema `StartDateInRequest`) | no | When this interest rate should start being applied. Enter either this field or `start_cylce` but not both. Date **must** be greater than current date. Format = yyyy-mm-dd.<br> | format: "date"; example: "2021-08-20" |
| `cancel_at_start_date` | boolean (schema `CancelAtStartDate`) | no | Cancel at start date?<br><br>If `false`, the behavior of the endpoint is not affected.<br><br>If `true`, the endpoint presents the following behavior.<br>* If a value is provided for `start_date`, the `cancelled_at` field is set to the day before `start_date`, and the configuration is canceled on that date.<br>* If a value is provided for `start_cycle`, `cancel_at_start_date` is ignored. The account transaction category is immediately canceled (that is, `cancelled_at` is set to null), and the `cancelled_at` field is updated with today's date (the date of the request), just as it would be if `cancel_at_start_date` were `false`.       <br><br>**Note:** You must provide a value for either `start_date` or `start_cycle`, but not both.<br><br>Executing this endpoint multiple times with `cancel_at_start_date` set to `true`, but with different values for `rate` and `start_date` enables you to define a schedule for when the different rates should be applied. For example, suppose you have an existing account transaction category with the following settings.<br>`account_transaction_category_id` = 2301<br>`account_id` = 1<br>`transaction_category_id` = 1001<br>`rate` = 10.0<br>`start_date` = 2025-07-01 <br><br>Now suppose you execute this endpoint with the following settings. (Assume 2025-07-15 is the current date or a date in the near future.) You do not have to pass an `account_transaction_category_id`. The Pismo platform generates a new ID and returns it in the endpoint response. Note, however, that you're passing the same value (1001) for `transaction_category_id` as in the existing category.<br>`account_id` = 1<br>`transaction_category_id` = 1001<br>`rate` = 12.0<br>`start_date` = 2025-07-15<br><br>The new account transaction category is created with ID 2302 (for example), and the account transaction category with ID 2301 is canceled on 2025-07-14.<br><br>Suppose the client executes the endpoint again, using the following values.<br>`account_id`: 1<br>`transaction_category_id`: 1001<br>`rate`: 14.0<br>`start_date`: 2025-07-25<br><br>The new account transaction category is created with ID 2303 (for example) and the account transaction category with ID 2302 is canceled on 2025-07-24.<br>In the last request, if a value is provided for `start_cycle`, instead of `start_date`, the platform immediately cancels all of the existing account transactions categories, just as it would have done if `cancel_at_start_date` were `false`.<br> | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | CREATED | `application/json`: object (schema `AccountTransactionCategoryResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_transaction_category_id` | integer (schema `AccountTransactionCategoryID`) | no | Account transaction category ID | format: "int64"; example: 1 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1010 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-e7091464-cd1e-4c20-8c68-1e4c5774d972" |
| `description` | string (schema `TransactionDescription`) | no | Transaction description | example: "purchase" |
| `refinancing_rate_after_due_date` | number (schema `RefinancingRateAfterDueDate`) | no | Interest rate for the accrual type `REFINANCING` if the statement due date is past, but the account is not overdue. (That is, the MAD was paid.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 15.99 |
| `default_rate` | number (schema `DefaultRate`) | no | Interest rate used for the accrual type `OVERDUE` when the statement is past the due date and the MAD has not been paid. (The account is overdue.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 1 |
| `fine_rate` | number (schema `FineRate`) | no | Fine rate. Charged once per transaction when transaction is due. | format: "float"; example: 2 |
| `overdue_rate_after_due_date` | number (schema `OverdueRateAfterDueDate`) | no | Interest rate used for the accrual type `REFINANCING` if the statement due date has passed and the MAD was not paid. <b>Note:</b> If this value is null, `refinancing_rate_after_due_date` is used instead.<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 17.99 |
| `refinancing_rate_after_due_date_multiplier_percent` | number (schema `RefinancingRateAfterDueDateMultiplierPercent`) | no | Percentage multiplier applied to transaction category refinancing rate after due date. 1.5 = 150% of the refinancing rate. | format: "float"; example: 1.5 |
| `default_rate_multiplier_percent` | number (schema `DefaultRateMultiplierPercent`) | no | Percentage multiplier applied to transaction category default rate. 1.7 = 170% of the default rate. | example: 1.7 |
| `fine_rate_multiplier_percent` | number (schema `FineRateMultiplierPercent`) | no | Percentage multiplier applied to transaction category fine rate. For example, 2 = 200% of the fine rate. | format: "float"; example: 2 |
| `overdue_rate_after_due_date_multiplier_percent` | number (schema `OverdueRateAfterDueDateMultiplierPercent`) | no | Multiplier applied to transaction category overdue rate after due date. 0.7 = 70% of the overdue rate. | format: "float"; example: 0.7 |
| `start_cycle` | integer (schema `StartCycleInResponse`) | no | Account cycle in which this interest rate should start being applied. | format: "int64"; example: 4 |
| `start_date` | string (schema `StartDateInResponse`) | no | When this interest rate should start being applied. Format = yyyy-mm-dd. | format: "date"; example: "2021-08-20" |
| `updated_at` | string (schema `UpdatedAt`) | no | When this interest rate was updated. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-20T00:00:00" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Cancellation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-20T00:00:00" |
| `created_at` | string (schema `CreatedAt`) | no | Creation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-10T00:00:00" |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 423

423 Example `Account Locked`:

```json
{
  "message": "The operation could not be completed because another process is manipulating the account (the account lock could not be obtained). Try again in a moment."
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;423;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-transaction-categories`, `KU-CRED-configuring-accrual-rates`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=DELETE path=/statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId} operationId=cancelAccountTransactionCategory -->
### `DELETE /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId}` — Cancel account transaction category

- **operationId:** `cancelAccountTransactionCategory`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Account transaction categories`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel an account transaction category. If the passed account transaction category is already canceled, an exception is raised.
>
> When you cancel an account transaction category, the account reverts back to using the rates defined in the program-level transaction category. For more information about program transaction categories, refer to [Transaction category structure](doc:configuring-accrual-rates#transaction-category-structure).
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountTransactionCategoryId` | path | yes | integer | ID of account transaction category | format: "int64"; example: 101 |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Indicates that the server accepted the request and created the resource. | `application/json`: object (schema `TransactionShiftResponseBody`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-transaction-categories`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountTransactionCategoryResponse -->
### Schema `AccountTransactionCategoryResponse`

Pointer: `#/components/schemas/AccountTransactionCategoryResponse`. Type: object (schema `AccountTransactionCategoryResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_transaction_category_id` | integer (schema `AccountTransactionCategoryID`) | no | Account transaction category ID | format: "int64"; example: 1 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1010 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-e7091464-cd1e-4c20-8c68-1e4c5774d972" |
| `description` | string (schema `TransactionDescription`) | no | Transaction description | example: "purchase" |
| `refinancing_rate_after_due_date` | number (schema `RefinancingRateAfterDueDate`) | no | Interest rate for the accrual type `REFINANCING` if the statement due date is past, but the account is not overdue. (That is, the MAD was paid.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 15.99 |
| `default_rate` | number (schema `DefaultRate`) | no | Interest rate used for the accrual type `OVERDUE` when the statement is past the due date and the MAD has not been paid. (The account is overdue.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 1 |
| `fine_rate` | number (schema `FineRate`) | no | Fine rate. Charged once per transaction when transaction is due. | format: "float"; example: 2 |
| `overdue_rate_after_due_date` | number (schema `OverdueRateAfterDueDate`) | no | Interest rate used for the accrual type `REFINANCING` if the statement due date has passed and the MAD was not paid. <b>Note:</b> If this value is null, `refinancing_rate_after_due_date` is used instead.<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 17.99 |
| `refinancing_rate_after_due_date_multiplier_percent` | number (schema `RefinancingRateAfterDueDateMultiplierPercent`) | no | Percentage multiplier applied to transaction category refinancing rate after due date. 1.5 = 150% of the refinancing rate. | format: "float"; example: 1.5 |
| `default_rate_multiplier_percent` | number (schema `DefaultRateMultiplierPercent`) | no | Percentage multiplier applied to transaction category default rate. 1.7 = 170% of the default rate. | example: 1.7 |
| `fine_rate_multiplier_percent` | number (schema `FineRateMultiplierPercent`) | no | Percentage multiplier applied to transaction category fine rate. For example, 2 = 200% of the fine rate. | format: "float"; example: 2 |
| `overdue_rate_after_due_date_multiplier_percent` | number (schema `OverdueRateAfterDueDateMultiplierPercent`) | no | Multiplier applied to transaction category overdue rate after due date. 0.7 = 70% of the overdue rate. | format: "float"; example: 0.7 |
| `start_cycle` | integer (schema `StartCycleInResponse`) | no | Account cycle in which this interest rate should start being applied. | format: "int64"; example: 4 |
| `start_date` | string (schema `StartDateInResponse`) | no | When this interest rate should start being applied. Format = yyyy-mm-dd. | format: "date"; example: "2021-08-20" |
| `updated_at` | string (schema `UpdatedAt`) | no | When this interest rate was updated. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-20T00:00:00" |
| `cancelled_at` | string (schema `CanceledAt`) | no | Cancellation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-20T00:00:00" |
| `created_at` | string (schema `CreatedAt`) | no | Creation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-10T00:00:00" |

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

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Account transaction categories`: GET /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories, POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories, DELETE /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId} | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-transaction-categories` — Transaction categories
- `KU-CRED-configuring-accrual-rates` — Configuring accrual rates
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
