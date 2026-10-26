---
ku_id: KU-API-revolving-credit-statements--program-transaction-categories
title: 'API reference: Revolving credit - Statements — Program transaction categories'
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
- listTransactionCategoryInterest
- createTransactionCategory
- updateTransactionCategoryInterest
related_kus:
- KU-CARD-transaction-categories
- KU-CORE-program-parameters-reference-table
- KU-CRED-calculating-interest-accruals
- KU-CRED-configuring-a-sellos-tax
- KU-CRED-full-balance-credit-program
- KU-CRED-managing-the-charge-order-for-debit-transactions
- KU-CRED-minimum-amount-due-calculation
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Program transaction categories

**KU ID:** `KU-API-revolving-credit-statements--program-transaction-categories` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Program transaction categories` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Program transaction category endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements-v2/v1/transactions-categories` | `listTransactionCategoryInterest` | List program transaction categories | no |
| `POST /statements-v2/v1/transactions-categories` | `createTransactionCategory` | Create program transaction category | no |
| `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` | `updateTransactionCategoryInterest` | Update program transaction category | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/transactions-categories operationId=listTransactionCategoryInterest -->
### `GET /statements-v2/v1/transactions-categories` — List program transaction categories

- **operationId:** `listTransactionCategoryInterest`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Program transaction categories`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List program transaction categories with filtering options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `program-id` | header | yes | string | Program ID | example: "1233" |
| `transactionCategoryId` | query | no | array of integer | One or more program transaction category ID's | example: [1, 2]; items.format: "int32" |
| `transactionCategoryDescription` | query | no | string | Transaction category description<br><br>If program transaction categories are defined for a program, you can view them in [Control Center](doc:get-started-with-control-center) by navigating to the <b>Program information</b> page (Configurations > Programs > Program information) and selecting the <b>Transaction categories</b> tab. The `transactionCategoryDescription` field corresponds to the <b>Transaction category name</b> column on that page.<br> | example: "Internal" |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `TransactionCategoryListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `TransactionCategoryResponse`) | no |  |  |
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

Guides that link to this operation: `KU-CARD-transaction-categories`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=POST path=/statements-v2/v1/transactions-categories operationId=createTransactionCategory -->
### `POST /statements-v2/v1/transactions-categories` — Create program transaction category

- **operationId:** `createTransactionCategory`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Program transaction categories`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a program transaction category. Program transaction categories are used to group transaction types and set properties for the group. Transaction types, in combination with processing codes, are used to define how financial operations are implemented on the Pismo platform. 
>
> For more information, refer to [Using configurable entities](doc:full-balance-credit-program#using-configurable-entities) and [Transaction category structure](doc:configuring-accrual-rates#transaction-category-structure).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `program-id` | header | yes | string | Program ID | example: "1233" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `TransactionCategoryRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `default_rate` | number (schema `DefaultRate`) | yes | Interest rate used for the accrual type `OVERDUE` when the statement is past the due date and the MAD has not been paid. (The account is overdue.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 1 |
| `fine_rate` | number (schema `FineRate`) | yes | Fine rate. Charged once per transaction when transaction is due. | format: "float"; example: 2 |
| `minimum_value` | number (schema `MinimumValue`) | yes | Minimum value to calculate the minimum amount due (MAD). This field is a percent, so 1.0 is 100%. Allowable values are between 0 and 1.<br> | format: "float"; example: 1 |
| `overdue_rate_after_due_date` | number (schema `OverdueRateAfterDueDate`) | yes | Interest rate used for the accrual type `REFINANCING` if the statement due date has passed and the MAD was not paid. <b>Note:</b> If this value is null, `refinancing_rate_after_due_date` is used instead.<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 17.99 |
| `refinancing_rate_after_due_date` | number (schema `RefinancingRateAfterDueDate`) | yes | Interest rate for the accrual type `REFINANCING` if the statement due date is past, but the account is not overdue. (That is, the MAD was paid.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 15.99 |
| `description` | string (schema `TransactionCategoryDescription`) | no | Transaction category description | maxLength: 50; example: "purchase" |
| `charge_order` | integer (schema `ChargeOrder`) | no | Indicates which transaction is discharged first. 1 is the highest in the hierarchy. | format: "int32"; example: 2 |
| `secondary_charge_order` | integer (schema `SecondaryChargeOrder`) | no | An alternative form of discharge priority for debit transactions. This field is only used if the `secondary_charge_order` parameter is active at the account level. In the discharge flow, the Pismo platform checks to see if `secondary_charge_order` is set for the account and is positive. If so, then the platform ignores the `charge_order` field and uses the `secondary_charge_order` field instead.<br><br>Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-update">Update account parameter</a> to set this parameter. The endpoint requires the ID of the parameter. Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-find">List account parameters</a> to find the ID. For example, if you want the `secondary_charge_order` field to be used for transactions on the account with account ID 1234, and the ID for the parameter is 108, then you should call the Update account parameter endpoint with `accountId` = `1234`, `parameterId` = 108, and `value` = 1.<br> | format: "int32"; example: 7 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `TransactionCategoryResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |
| `transaction_category_description` | string (schema `TransactionCategoryDescription`) | no | Transaction category description | maxLength: 50; example: "purchase" |
| `refinancing_rate_after_due_date` | number (schema `RefinancingRateAfterDueDate`) | no | Interest rate for the accrual type `REFINANCING` if the statement due date is past, but the account is not overdue. (That is, the MAD was paid.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 15.99 |
| `default_rate` | number (schema `DefaultRate`) | no | Interest rate used for the accrual type `OVERDUE` when the statement is past the due date and the MAD has not been paid. (The account is overdue.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 1 |
| `fine_rate` | number (schema `FineRate`) | no | Fine rate. Charged once per transaction when transaction is due. | format: "float"; example: 2 |
| `overdue_rate_after_due_date` | number (schema `OverdueRateAfterDueDate`) | no | Interest rate used for the accrual type `REFINANCING` if the statement due date has passed and the MAD was not paid. <b>Note:</b> If this value is null, `refinancing_rate_after_due_date` is used instead.<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 17.99 |
| `minimum_value` | number (schema `MinimumValue`) | no | Minimum value to calculate the minimum amount due (MAD). This field is a percent, so 1.0 is 100%. Allowable values are between 0 and 1.<br> | format: "float"; example: 1 |
| `charge_order` | integer (schema `ChargeOrder`) | no | Indicates which transaction is discharged first. 1 is the highest in the hierarchy. | format: "int32"; example: 2 |
| `secondary_charge_order` | integer (schema `SecondaryChargeOrder`) | no | An alternative form of discharge priority for debit transactions. This field is only used if the `secondary_charge_order` parameter is active at the account level. In the discharge flow, the Pismo platform checks to see if `secondary_charge_order` is set for the account and is positive. If so, then the platform ignores the `charge_order` field and uses the `secondary_charge_order` field instead.<br><br>Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-update">Update account parameter</a> to set this parameter. The endpoint requires the ID of the parameter. Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-find">List account parameters</a> to find the ID. For example, if you want the `secondary_charge_order` field to be used for transactions on the account with account ID 1234, and the ID for the parameter is 108, then you should call the Update account parameter endpoint with `accountId` = `1234`, `parameterId` = 108, and `value` = 1.<br> | format: "int32"; example: 7 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `programs` | array of integer (schema `Programs`) | no | Programs that use this transaction category in one or more transaction types | example: [1, 2]; items.format: "int32" |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-transaction-categories`, `KU-CORE-program-parameters-reference-table`, `KU-CRED-calculating-interest-accruals`, `KU-CRED-configuring-a-sellos-tax`, `KU-CRED-full-balance-credit-program`, `KU-CRED-managing-the-charge-order-for-debit-transactions`, `KU-CRED-minimum-amount-due-calculation`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PUT path=/statements-v2/v1/transactions-categories/{transactionCategoryId} operationId=updateTransactionCategoryInterest -->
### `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` — Update program transaction category

- **operationId:** `updateTransactionCategoryInterest`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Program transaction categories`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a program transaction category by ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `program-id` | header | yes | string | Program ID | example: "1233" |
| `transactionCategoryId` | path | yes | integer | Program transaction category ID | format: "int64"; example: 101 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `TransactionCategoryRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `default_rate` | number (schema `DefaultRate`) | yes | Interest rate used for the accrual type `OVERDUE` when the statement is past the due date and the MAD has not been paid. (The account is overdue.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 1 |
| `fine_rate` | number (schema `FineRate`) | yes | Fine rate. Charged once per transaction when transaction is due. | format: "float"; example: 2 |
| `minimum_value` | number (schema `MinimumValue`) | yes | Minimum value to calculate the minimum amount due (MAD). This field is a percent, so 1.0 is 100%. Allowable values are between 0 and 1.<br> | format: "float"; example: 1 |
| `overdue_rate_after_due_date` | number (schema `OverdueRateAfterDueDate`) | yes | Interest rate used for the accrual type `REFINANCING` if the statement due date has passed and the MAD was not paid. <b>Note:</b> If this value is null, `refinancing_rate_after_due_date` is used instead.<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 17.99 |
| `refinancing_rate_after_due_date` | number (schema `RefinancingRateAfterDueDate`) | yes | Interest rate for the accrual type `REFINANCING` if the statement due date is past, but the account is not overdue. (That is, the MAD was paid.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 15.99 |
| `description` | string (schema `TransactionCategoryDescription`) | no | Transaction category description | maxLength: 50; example: "purchase" |
| `charge_order` | integer (schema `ChargeOrder`) | no | Indicates which transaction is discharged first. 1 is the highest in the hierarchy. | format: "int32"; example: 2 |
| `secondary_charge_order` | integer (schema `SecondaryChargeOrder`) | no | An alternative form of discharge priority for debit transactions. This field is only used if the `secondary_charge_order` parameter is active at the account level. In the discharge flow, the Pismo platform checks to see if `secondary_charge_order` is set for the account and is positive. If so, then the platform ignores the `charge_order` field and uses the `secondary_charge_order` field instead.<br><br>Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-update">Update account parameter</a> to set this parameter. The endpoint requires the ID of the parameter. Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-find">List account parameters</a> to find the ID. For example, if you want the `secondary_charge_order` field to be used for transactions on the account with account ID 1234, and the ID for the parameter is 108, then you should call the Update account parameter endpoint with `accountId` = `1234`, `parameterId` = 108, and `value` = 1.<br> | format: "int32"; example: 7 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `TransactionCategoryResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |
| `transaction_category_description` | string (schema `TransactionCategoryDescription`) | no | Transaction category description | maxLength: 50; example: "purchase" |
| `refinancing_rate_after_due_date` | number (schema `RefinancingRateAfterDueDate`) | no | Interest rate for the accrual type `REFINANCING` if the statement due date is past, but the account is not overdue. (That is, the MAD was paid.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 15.99 |
| `default_rate` | number (schema `DefaultRate`) | no | Interest rate used for the accrual type `OVERDUE` when the statement is past the due date and the MAD has not been paid. (The account is overdue.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 1 |
| `fine_rate` | number (schema `FineRate`) | no | Fine rate. Charged once per transaction when transaction is due. | format: "float"; example: 2 |
| `overdue_rate_after_due_date` | number (schema `OverdueRateAfterDueDate`) | no | Interest rate used for the accrual type `REFINANCING` if the statement due date has passed and the MAD was not paid. <b>Note:</b> If this value is null, `refinancing_rate_after_due_date` is used instead.<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 17.99 |
| `minimum_value` | number (schema `MinimumValue`) | no | Minimum value to calculate the minimum amount due (MAD). This field is a percent, so 1.0 is 100%. Allowable values are between 0 and 1.<br> | format: "float"; example: 1 |
| `charge_order` | integer (schema `ChargeOrder`) | no | Indicates which transaction is discharged first. 1 is the highest in the hierarchy. | format: "int32"; example: 2 |
| `secondary_charge_order` | integer (schema `SecondaryChargeOrder`) | no | An alternative form of discharge priority for debit transactions. This field is only used if the `secondary_charge_order` parameter is active at the account level. In the discharge flow, the Pismo platform checks to see if `secondary_charge_order` is set for the account and is positive. If so, then the platform ignores the `charge_order` field and uses the `secondary_charge_order` field instead.<br><br>Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-update">Update account parameter</a> to set this parameter. The endpoint requires the ID of the parameter. Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-find">List account parameters</a> to find the ID. For example, if you want the `secondary_charge_order` field to be used for transactions on the account with account ID 1234, and the ID for the parameter is 108, then you should call the Update account parameter endpoint with `accountId` = `1234`, `parameterId` = 108, and `value` = 1.<br> | format: "int32"; example: 7 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `programs` | array of integer (schema `Programs`) | no | Programs that use this transaction category in one or more transaction types | example: [1, 2]; items.format: "int32" |

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

Guides that link to this operation: `KU-CARD-transaction-categories`, `KU-CRED-managing-the-charge-order-for-debit-transactions`, `KU-CRED-minimum-amount-due-calculation`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/TransactionCategoryResponse -->
### Schema `TransactionCategoryResponse`

Pointer: `#/components/schemas/TransactionCategoryResponse`. Type: object (schema `TransactionCategoryResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_category_id` | integer (schema `TransactionCategoryID`) | no | Transaction category ID | format: "int64"; example: 1 |
| `transaction_category_description` | string (schema `TransactionCategoryDescription`) | no | Transaction category description | maxLength: 50; example: "purchase" |
| `refinancing_rate_after_due_date` | number (schema `RefinancingRateAfterDueDate`) | no | Interest rate for the accrual type `REFINANCING` if the statement due date is past, but the account is not overdue. (That is, the MAD was paid.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 15.99 |
| `default_rate` | number (schema `DefaultRate`) | no | Interest rate used for the accrual type `OVERDUE` when the statement is past the due date and the MAD has not been paid. (The account is overdue.)<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 1 |
| `fine_rate` | number (schema `FineRate`) | no | Fine rate. Charged once per transaction when transaction is due. | format: "float"; example: 2 |
| `overdue_rate_after_due_date` | number (schema `OverdueRateAfterDueDate`) | no | Interest rate used for the accrual type `REFINANCING` if the statement due date has passed and the MAD was not paid. <b>Note:</b> If this value is null, `refinancing_rate_after_due_date` is used instead.<br><br>By default, this is a monthly rate, so the Pismo platform divides it by 30 before applying it on a daily basis. For more information, refer to [Changing the interest rate period](doc:configuring-accrual-rates#changing-the-interest-rate-period).<br> | format: "float"; example: 17.99 |
| `minimum_value` | number (schema `MinimumValue`) | no | Minimum value to calculate the minimum amount due (MAD). This field is a percent, so 1.0 is 100%. Allowable values are between 0 and 1.<br> | format: "float"; example: 1 |
| `charge_order` | integer (schema `ChargeOrder`) | no | Indicates which transaction is discharged first. 1 is the highest in the hierarchy. | format: "int32"; example: 2 |
| `secondary_charge_order` | integer (schema `SecondaryChargeOrder`) | no | An alternative form of discharge priority for debit transactions. This field is only used if the `secondary_charge_order` parameter is active at the account level. In the discharge flow, the Pismo platform checks to see if `secondary_charge_order` is set for the account and is positive. If so, then the platform ignores the `charge_order` field and uses the `secondary_charge_order` field instead.<br><br>Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-update">Update account parameter</a> to set this parameter. The endpoint requires the ID of the parameter. Use <a href="https://developers.pismo.io/pismo-docs/reference/account-parameters-find">List account parameters</a> to find the ID. For example, if you want the `secondary_charge_order` field to be used for transactions on the account with account ID 1234, and the ID for the parameter is 108, then you should call the Update account parameter endpoint with `accountId` = `1234`, `parameterId` = 108, and `value` = 1.<br> | format: "int32"; example: 7 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `programs` | array of integer (schema `Programs`) | no | Programs that use this transaction category in one or more transaction types | example: [1, 2]; items.format: "int32" |

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
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Program transaction categories`: GET /statements-v2/v1/transactions-categories, POST /statements-v2/v1/transactions-categories, PUT /statements-v2/v1/transactions-categories/{transactionCategoryId} | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-transaction-categories` — Transaction categories
- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-CRED-calculating-interest-accruals` — Calculating interest accruals
- `KU-CRED-configuring-a-sellos-tax` — Configuring a sellos tax
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-CRED-managing-the-charge-order-for-debit-transactions` — Managing the charge order for debit transactions
- `KU-CRED-minimum-amount-due-calculation` — Minimum amount due calculation
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
