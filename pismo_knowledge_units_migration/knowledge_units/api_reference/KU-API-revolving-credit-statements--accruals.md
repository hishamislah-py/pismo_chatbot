---
ku_id: KU-API-revolving-credit-statements--accruals
title: 'API reference: Revolving credit - Statements — Accruals'
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
- getInterestAccrualSummarization
- getAccountAccrualsV3
- getAccountsTransactionsInterest
- GetAccountAccrualsV2
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CRED-accrual-rate-types-and-limits
- KU-CRED-understanding-statements
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Accruals

**KU ID:** `KU-API-revolving-credit-statements--accruals` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Accruals` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Accrual endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals/summarization` | `getInterestAccrualSummarization` | Get interest accrual summary | no |
| `GET /statements-v2/v3/accounts/{accountId}/interest-accruals` | `getAccountAccrualsV3` | List account accruals v3 | no |
| `PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals` | `getAccountsTransactionsInterest` | Update interest accrual statuses | no |
| `GET /statements/v2/accounts/{accountId}/interest-accruals` | `GetAccountAccrualsV2` | List account accruals v2 | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v3/accounts/{accountId}/interest-accruals/summarization operationId=getInterestAccrualSummarization -->
### `GET /statements-v2/v3/accounts/{accountId}/interest-accruals/summarization` — Get interest accrual summary

- **operationId:** `getInterestAccrualSummarization`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accruals`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get an account interest accrual summary with filter options.
>
> Using the `beginDate` and `endDate` query parameters, you can specify a time period of up to 60 days. However, for the period between 31 and 60 days, the `interest_accruals_ids` field is omitted in the response. This is done because the list of IDs can get very large for a 60-day period. If you specify a period greater than 60 days, the endpoint returns an error.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `beginDate` | query | yes | string | Beginning date filter. Return statements that have opening date after or equal to this date. Default value is account creation date. Format = yyyy-mm-dd.<br> | format: "full-date"; example: "2020-06-18" |
| `endDate` | query | yes | string | End date filter. Return statements that have opening date before or equal to this date. Default value is today's date. Format = yyyy-mm-dd. | format: "full-date"; example: "2020-06-18" |
| `omitId` | query | no | string | Omit interest accrual IDs in the API response?<br><br>If the period specified using the `beginDate` and `endDate` query parameters is greater than 30 days, interest accrual IDs are automatically omitted. Setting `omitId` to `true` causes the API to omit interest accrual IDs even when the specified period is 30 days or less.<br>Using this parameter is recommended to improve performance.<br> | enum: ["true", "false"]; default: "false"; example: "true" |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `accrualType` | query | no | string | Interest accrual type. Possible values:<br>* `OVERDUE`:  Daily charge applied to an unpaid balance if the minimum amount due (MAD) has not been paid.<br>* `REFINANCING`: Daily charge applied to an unpaid balance if the MAD has been paid, but the total amount due has not.<br>* `IOF`: Brazilian tax<br>* `FINE`: One-time charge that's applied on the day an account becomes overdue.<br> | enum: ["OVERDUE", "REFINANCING", "IOF", "FINE"]; example: "OVERDUE" |
| `status` | query | yes | string | Status interest accrual filter. Possible values:<br>* `PENDING`: Accrual has been calculated but has not yet generated a transaction.<br>* `PROCESSED`: Accrual has been processed and a transaction has been generated.<br>* `STOP_ACCRUAL`: Due to a program parameter, the accrual has reached the maximum number of days to be posted as a transaction. For more information, refer to [Limiting the number of days accruals can be charged](doc:limiting-the-number-of-days-accruals-can-be-charged).<br>* `SETTLED`: Accrual transaction has been settled.<br> | enum: ["PENDING", "PROCESSED", "STOP_ACCRUAL", "SETTLED"]; example: "PENDING" |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `InterestAccrualSummarizationListResponse`) |
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
| `items[].accrual_type` | string (schema `AccrualType`) | no | Interest accrual type. Possible values:<br>* `OVERDUE`:  A daily charge applied to an unpaid balance if the minimum amount due (MAD) has not been paid.<br>* `REFINANCING`: A daily charge applied to an unpaid balance if the MAD has been paid, but the total amount due has not.<br>* `IOF`: A Brazilian tax<br>* `FINE`: A one-time charge that's applied on the day an account becomes overdue.<br> | enum: ["OVERDUE", "REFINANCING", "IOF", "FINE"]; example: "OVERDUE" |
| `items[].status` | string (schema `AccrualStatus`) | no | Interest accrual status.<br>* `PENDING`: Accrual has been calculated but has not yet generated a transaction.<br>* `PROCESSED`: Accrual has been processed and a transaction has been generated.<br>* `STOP_ACCRUAL`: Due to a program parameter, the accrual has reached the maximum number of days to be posted as a transaction. For more information, refer to [Limiting the number of days accruals can be charged](doc:limiting-the-number-of-days-accruals-can-be-charged).<br>* `SETTLED`: Accrual transaction has been settled.        <br> | enum: ["PENDING", "PROCESSED", "STOP_ACCRUAL", "SETTLED"]; example: "PENDING" |
| `items[].accrued_value` | number (schema `AccruedValue`) | no | Accrued value | format: "float"; example: 1.95 |
| `items[].interest_accrual_ids` | array of integer (schema `SummedInterestAccrualIDs`) | no | All ID's that are included in the summed interest accrual amount | example: [7, 8, 9, 10, 11]; items.format: "int64" |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-understanding-statements`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v3/accounts/{accountId}/interest-accruals operationId=getAccountAccrualsV3 -->
### `GET /statements-v2/v3/accounts/{accountId}/interest-accruals` — List account accruals v3

- **operationId:** `getAccountAccrualsV3`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accruals`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account accruals with filtering options. You must specify the period using `beginDate` and `endDate`, and this period must be less than or equal to 30 days. If you specify a period greater than this, the endpoint returns an error.
>
> The period is restricted to 30 days for performance reasons. A larger period could return a very large number of accruals.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `beginDate` | query | yes | string | Beginning date filter. Return statements that have opening date after or equal to this date. Default value is account creation date. Format = yyyy-mm-dd.<br> | format: "full-date"; example: "2020-06-18" |
| `endDate` | query | yes | string | End date filter. Return statements that have opening date before or equal to this date. Default value is today's date. Format = yyyy-mm-dd. | format: "full-date"; example: "2020-06-18" |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `accrualType` | query | no | string | Interest accrual type. Possible values:<br>* `OVERDUE`:  Daily charge applied to an unpaid balance if the minimum amount due (MAD) has not been paid.<br>* `REFINANCING`: Daily charge applied to an unpaid balance if the MAD has been paid, but the total amount due has not.<br>* `IOF`: Brazilian tax<br>* `FINE`: One-time charge that's applied on the day an account becomes overdue.<br> | enum: ["OVERDUE", "REFINANCING", "IOF", "FINE"]; example: "OVERDUE" |
| `status` | query | no | string | Status interest accrual filter. Possible values:<br>* `PENDING`: Accrual has been calculated but has not yet generated a transaction.<br>* `PROCESSED`: Accrual has been processed and a transaction has been generated.<br>* `STOP_ACCRUAL` Due to a program parameter, the accrual has reached the maximum number of days to be posted as a transaction. For more information, refer to [Limiting the number of days accruals can be charged](doc:limiting-the-number-of-days-accruals-can-be-charged).<br>* `SETTLED`: Accrual transaction has been settled.<br> | enum: ["PENDING", "PROCESSED", "STOP_ACCRUAL", "SETTLED"]; example: "PENDING" |
| `interestAccrualId` | query | no | integer | Interest accrual ID. Depending on `accrualType`, `endDate`, and `beginDate`, some filters might be ignored. The other filters can be used concurrently.<br> | format: "int64"; example: 10100 |
| `transactionId` | query | no | integer | Transaction ID. When passed, the `accrualType`, `endDate` and `beginDate` filters are canceled. The other filters can be used concurrently.<br> | format: "int64"; example: 20200 |
| `statementId` | query | no | integer | Statement ID | format: "int64"; example: 1 |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |
| `includeNegative` | query | no | boolean | If `false`, request does not return negative generated accruals. If `true`, both positive and negative generated accruals are returned.<br>A negative accrual occurs when the Pismo platform receives a payment retroactive to the due date and needs to reverse the positive accruals generated.<br>Default setting is `false`.<br> | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `InterestAccrualV3ListResponse`) |
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
| `items` | array of object (schema `InterestAccrualV3Response`) | no |  |  |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-understanding-statements`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PATCH path=/statements-v2/v3/accounts/{accountId}/interest-accruals operationId=getAccountsTransactionsInterest -->
### `PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals` — Update interest accrual statuses

- **operationId:** `getAccountsTransactionsInterest`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accruals`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the statuses of one or more interest accruals. 
>
> You can use accrual type and accrual IDs to filter interest accruals. 
>
> You can change an interest accrual's status to  PENDING, STOP_ACCRUAL, or SETTLED. If the current status is PROCESSED, it cannot be changed.
> As a result, this endpoint could return two lists, one for updated accruals and one for not updated accruals.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `AccrualsToUpdateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accruals` | array of object (schema `AccrualsIdsToUpdateStatusRequest`) (schema `AccrualsToUpdate`) | yes | Interest accruals to update. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `AccountInterestAccrualStatusUpdatedResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `updated_ids` | array of integer (schema `UpdatedIDs`) | no | ID's of interest accruals that have been updated. | example: [1, 2, 3]; items.format: "int64" |
| `not_updated_ids` | array of integer (schema `NotUpdatedIDs`) | no | ID's of interest accruals that have not been updated, because, for example, the status cannot be changed if it is already PROCESSED. | example: [5, 6]; items.format: "int64" |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-accrual-rate-types-and-limits`, `KU-CRED-understanding-statements`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements/v2/accounts/{accountId}/interest-accruals operationId=GetAccountAccrualsV2 -->
### `GET /statements/v2/accounts/{accountId}/interest-accruals` — List account accruals v2

- **operationId:** `GetAccountAccrualsV2`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Accruals`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account accruals with filtering options.
>
> <b>Note:</b> This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.      

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `status` | query | no | string | Interest accrual status.<br>* `PENDING`: Accrual has been calculated but has not yet generated a transaction.<br>* `PROCESSED`: Accrual has been processed and a transaction has been generated.<br>* `STOP_ACCRUAL`: Due to a program parameter, the accrual has reached the maximum number of days to be posted as a transaction. For more information, refer to [Limiting the number of days accruals can be charged](doc:limiting-the-number-of-days-accruals-can-be-charged).<br> | enum: ["PENDING", "PROCESSED", "STOP_ACCRUAL"]; default: "STOP_ACCRUAL"; example: "STOP_ACCRUAL" |
| `accrualType` | query | no | string | Interest accrual type.<br>* `REFINANCING`: When payment is greater than the minimum and less than the total balance amount.<br>* `OVERDUE`: When a payment is received that is less than the minimum amount required, the account enters overdue state, and refinancing of that type is calculated.<br> | enum: ["REFINANCING", "OVERDUE"]; default: "REFINANCING"; example: "REFINANCING" |
| `interestAccrualId` | query | no | integer | Interest accrual ID. Depending on `accrualType`, `endDate`, and `beginDate`, some filters might be ignored. The other filters can be used concurrently.<br> | format: "int64"; example: 10100 |
| `transactionId` | query | no | integer | Transaction ID. When passed, the `accrualType`, `endDate` and `beginDate` filters are canceled. The other filters can be used concurrently.<br> | format: "int64"; example: 20200 |
| `statementId` | query | no | integer | Statement ID. When passed, the `accrualType`, `endDate` and `beginDate` filters are canceled. The other filters can be used concurrently.<br> | example: 30300 |
| `beginDate` | query | no | string | Beginning date filter. Return statements that have opening date after or equal to this date. Default value is account creation date. Format = yyyy-mm-dd.<br> | format: "full-date"; example: "2020-06-18" |
| `endDate` | query | no | string | End date filter. Return statements that have opening date before or equal to this date. Default value is today's date. Format = yyyy-mm-dd. | format: "full-date"; example: "2020-06-18" |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `GetInterestAccrualsV2ResponseSuccess`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 4 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPage`) | no | Items per page | example: 50 |
| `total_items` | integer (schema `TotalItems`) | no | Number of items found | format: "int32"; example: 100 |
| `items` | array of object | no |  |  |
| `items[].interest_accrual_id` | integer (schema `InterestAccrualID`) | no | Interest accrual ID | format: "int64"; example: 564 |
| `items[].created_at` | string (schema `CreatedAt`) | no | Creation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-10T00:00:00" |
| `items[].transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `items[].statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `items[].transaction_balance` | number (schema `TransactionBalance`) | no | Value of interest accrual transaction | format: "float"; example: 101.99 |
| `items[].accrual_date` | string (schema `AccrualDate`) | no | Accrual date. Format = yyyy-mm-dd. | format: "date"; example: "2021-01-01" |
| `items[].accrual_type` | string (schema `AccrualType2`) | no | Interest accrual type.<br>* `REFINANCING`: When payment is greater than the minimum and less than the total balance amount.<br>* `OVERDUE`:  When a customer pays less than the minimum amount on the balance, he enters an overdue state, and refinancing of that type is calculated.<br> | enum: ["REFINANCING", "OVERDUE"]; example: "REFINANCING" |
| `items[].interest_rate` | number (schema `AccrualInterestRate`) | no | Interest rate | format: "float"; example: 0.1 |
| `items[].accrued_amount` | number (schema `AccruedValue`) | no | Accrued value | format: "float"; example: 1.95 |
| `items[].iof_amount` | number (schema `IofAmount`) | no | IOF (Brazilian tax) amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 1.35 |
| `items[].fixed_iof_amount` | number (schema `FixedIofAmount`) | no | Fixed IOF (Brazilian tax) Amount | format: "float"; example: 1.15 |
| `items[].status` | string (schema `InterestAccrualStatus`) | no | Interest accrual status | enum: ["PENDING", "PROCESSED", "STOP_ACCRUAL"]; example: "PENDING" |
| `items[].additional_info` | object (schema `AdditionalInfo`) | no |  |  |

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
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-understanding-statements`.

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

<!-- schema: #/components/schemas/InterestAccrualV3Response -->
### Schema `InterestAccrualV3Response`

Pointer: `#/components/schemas/InterestAccrualV3Response`. Type: object (schema `InterestAccrualV3Response`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_accrual_id` | integer (schema `InterestAccrualID`) | no | Interest accrual ID | format: "int64"; example: 564 |
| `created_at` | string (schema `CreatedAt`) | no | Creation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-10T00:00:00" |
| `transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `transaction_balance` | number (schema `TransactionBalance`) | no | Value of interest accrual transaction | format: "float"; example: 101.99 |
| `accrual_date` | string (schema `AccrualDate`) | no | Accrual date. Format = yyyy-mm-dd. | format: "date"; example: "2021-01-01" |
| `accrual_type` | string (schema `AccrualType`) | no | Interest accrual type. Possible values:<br>* `OVERDUE`:  A daily charge applied to an unpaid balance if the minimum amount due (MAD) has not been paid.<br>* `REFINANCING`: A daily charge applied to an unpaid balance if the MAD has been paid, but the total amount due has not.<br>* `IOF`: A Brazilian tax<br>* `FINE`: A one-time charge that's applied on the day an account becomes overdue.<br> | enum: ["OVERDUE", "REFINANCING", "IOF", "FINE"]; example: "OVERDUE" |
| `accrued_value` | number (schema `AccruedValue`) | no | Accrued value | format: "float"; example: 1.95 |
| `status` | string (schema `AccrualStatus`) | no | Interest accrual status.<br>* `PENDING`: Accrual has been calculated but has not yet generated a transaction.<br>* `PROCESSED`: Accrual has been processed and a transaction has been generated.<br>* `STOP_ACCRUAL`: Due to a program parameter, the accrual has reached the maximum number of days to be posted as a transaction. For more information, refer to [Limiting the number of days accruals can be charged](doc:limiting-the-number-of-days-accruals-can-be-charged).<br>* `SETTLED`: Accrual transaction has been settled.        <br> | enum: ["PENDING", "PROCESSED", "STOP_ACCRUAL", "SETTLED"]; example: "PENDING" |
| `interest_rate` | number (schema `TransactionInterestRate`) | no | Transaction interest rate. | format: "float"; example: 15.99 |
| `additional_info` | object (schema `AdditionalInfo`) | no |  |  |

<!-- schema: #/components/schemas/AccrualsIdsToUpdateStatusRequest -->
### Schema `AccrualsIdsToUpdateStatusRequest`

Pointer: `#/components/schemas/AccrualsIdsToUpdateStatusRequest`. Type: object (schema `AccrualsIdsToUpdateStatusRequest`).

> List of interest accrual data for update.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_accrual_ids` | array of integer (schema `InterestAccrualIDs`) | yes | IDs of interest accruals to update. | example: [1, 2, 3, 4]; items.format: "int64" |
| `accrual_type` | string (schema `AccrualType`) | yes | Interest accrual type. Possible values:<br>* `OVERDUE`:  A daily charge applied to an unpaid balance if the minimum amount due (MAD) has not been paid.<br>* `REFINANCING`: A daily charge applied to an unpaid balance if the MAD has been paid, but the total amount due has not.<br>* `IOF`: A Brazilian tax<br>* `FINE`: A one-time charge that's applied on the day an account becomes overdue.<br> | enum: ["OVERDUE", "REFINANCING", "IOF", "FINE"]; example: "OVERDUE" |
| `new_status` | string (schema `NewStatus`) | yes | New status for updated interest accruals. You can change an interest accrual's status to `PENDING`, `STOP_ACCRUAL`, or `SETTLED`. If the current status is `PROCESSED`, it cannot be changed.<br>* `PENDING`: Accrual has been calculated but has not yet generated a transaction.<br>* `PROCESSED`: Accrual has been processed and a transaction has been generated.<br>* `STOP_ACCRUAL`: Due to a program parameter, the accrual has reached the maximum number of days to be posted as a transaction. For more information, refer to [Limiting the number of days accruals can be charged](doc:limiting-the-number-of-days-accruals-can-be-charged).<br>* `SETTLED`: Accrual transaction has been settled.   <br> | enum: ["PENDING", "STOP_ACCRUAL", "SETTLED"]; example: "SETTLED" |

<!-- schema: #/components/schemas/AdditionalInfo -->
### Schema `AdditionalInfo`

Pointer: `#/components/schemas/AdditionalInfo`. Type: object (schema `AdditionalInfo`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_financial_classification` | integer (schema `AccountFinancialClassification`) | no | Customer-defined number representing the financial classification of the account. | format: "int32"; example: 2 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Accruals`: GET /statements-v2/v3/accounts/{accountId}/interest-accruals/summarization, GET /statements-v2/v3/accounts/{accountId}/interest-accruals, PATCH /statements-v2/v3/accounts/{accountId}/interest-accruals, GET /statements/v2/accounts/{accountId}/interest-accruals | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CRED-accrual-rate-types-and-limits` — Accrual rate types, accrual-free transaction types and accrual-day limits
- `KU-CRED-understanding-statements` — Understanding statements
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
