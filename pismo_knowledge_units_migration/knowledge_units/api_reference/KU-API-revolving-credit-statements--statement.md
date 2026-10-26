---
ku_id: KU-API-revolving-credit-statements--statement
title: 'API reference: Revolving credit - Statements — Statement'
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
- GetCurrentStatement
- GetStatementInfo
- getByStatementId
- getTotalDue
- getTransactionsBalance
- getMinimumPaymentCalculationMemory
- postRevolvingStatementSummary
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CORE-transactions-overview
- KU-CRED-agreements
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-EVT-catalogue-balance
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Statement

**KU ID:** `KU-API-revolving-credit-statements--statement` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Statement` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> General statement endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements/v1/accounts/{accountId}/next` | `GetCurrentStatement` | Get current statement | no |
| `GET /statements/v1/accounts/{accountId}/statements/{statementId}` | `GetStatementInfo` | Get statement | no |
| `GET /statements-v2/v3/accounts/{accountId}/statements` | `getByStatementId` | List statements | no |
| `GET /statements-v2/v2/accounts/{accountId}/total-due` | `getTotalDue` | Get account total due | no |
| `GET /statements-v2/v1/accounts/{accountId}/transactions-balance` | `getTransactionsBalance` | List transaction balances | no |
| `GET /statements-v2/v1/accounts/{accountId}/statements/{statementId}/min-payment-memory` | `getMinimumPaymentCalculationMemory` | Get minimum payout calculation memory | no |
| `POST /statements-v2/v1/accounts/{accountId}/revolving-statement-summary` | `postRevolvingStatementSummary` | Register revolving statement summary generation process | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements/v1/accounts/{accountId}/next operationId=GetCurrentStatement -->
### `GET /statements/v1/accounts/{accountId}/next` — Get current statement

- **operationId:** `GetCurrentStatement`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the current statement by account ID. For more information about statements, refer to [Understanding statements](doc:understanding-statements).
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.         

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: oneOf: object (schema `AccountNextResponse`) |
| 404 | Bad Request | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 404

404 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
}
```

404 Example `Invalid Account ID` — from `#/components/examples/InvalidAccountId`:

```json
{
  "message": "Invalid Long value for account_id parameter."
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
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements/v1/accounts/{accountId}/statements/{statementId} operationId=GetStatementInfo -->
### `GET /statements/v1/accounts/{accountId}/statements/{statementId}` — Get statement

- **operationId:** `GetStatementInfo`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a statement by account ID and statement ID. For more information about statements, refer to [Understanding statements](doc:understanding-statements).
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `statementId` | path | yes | integer | Statement ID | format: "int64"; example: 101 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: oneOf: object (schema `GetStatementV1ResponseSuccess`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `InvalidFieldErrorResponse`), object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
}
```

##### Response 404

404 Example `Statement not found` — from `#/components/examples/StatementNotFound`:

```json
{
  "message": "Statement not found"
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
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v3/accounts/{accountId}/statements operationId=getByStatementId -->
### `GET /statements-v2/v3/accounts/{accountId}/statements` — List statements

- **operationId:** `getByStatementId`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account statements. For more information about statements, refer to [Understanding statements](doc:understanding-statements).
>
> The filter parameters have the following order of precedence:
> 1. `startFromCurrentCycle`
> 2. `presentToFront`
> 3. `presentToPast`
>
> That is, if `startFromCurrentCycle` is `true`, then `presentToFront` and `presentToPast` are ignored.
> If `startFromCurrentCycle` is `false` (or not set), and `presentToFront` is `true`, then `presentToPast` is ignored.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `statementId` | query | no | integer | Statement ID | format: "int64"; example: 1 |
| `startCycle` | query | no | integer | Cycle to start statements list. Only used when `startFromCurrentCycle` is `true`. | default: 1; format: "int32"; example: 12 |
| `startFromCurrentCycle` | query | no | boolean | If `startFromCurrentCycle` is `true` and `startCycle` is not set, the request lists all cycles starting from the current cycle. For example, if the current cycle is cycle 10, the endpoint returns the cycles in this order: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1.<br><br>If `startFromCurrentCycle` is `true` and `startCycle` is set, the request lists all cycles starting from `startCycle`. For example, if the current cycle is cycle 10, and `startCycle` is 5, the endpoint returns the cycles in this order: 5, 4, 3, 2, 1.<br> | default: false; example: true |
| `presentToFront` | query | no | boolean | List all statements starting from the current cycle?<br><b>Note:</b> This field is ignored if `startFromCurrentCycle` is set to `true`.<br> | default: false; example: false |
| `presentToPast` | query | no | boolean | Exclude future statements? If `true`, the endpoint returns only the current cycle and all previous cycles.<br><b>Note:</b> This field is ignored if `startFromCurrentCycle` or `presentToFront` are set to `true`.<br> | default: false; example: true |
| `beginDueDate` | query | no | string | Beginning due date. Don't return statements with a due date earlier than this.<br><br>If `beginDueDate` is provided, `endDueDate` must also be provided.<br> | format: "full-date"; example: "2025-02-01" |
| `endDueDate` | query | no | string | Ending due date. Don't return statements with a due date later than this.<br><br>If `endDueDate` is provided, `beginDueDate` must also be provided.<br> | format: "full-date"; example: "2025-06-01" |
| `maxClosedCycles` | query | no | integer | Maximum number of closed statements to return. For example, if a customer has 20 past statements, and `maxClosedCycles` = 5, the endpoint only returns the last 5 closed statements.<br> | format: "int32"; example: 2 |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `AccountStatementsListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `AccountStatementsResponse`) | no |  |  |
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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-agreements`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v2/accounts/{accountId}/total-due operationId=getTotalDue -->
### `GET /statements-v2/v2/accounts/{accountId}/total-due` — Get account total due

- **operationId:** `getTotalDue`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the total amount due for an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `TotalDueResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1010 |
| `current_cycle` | integer (schema `Currentycle`) | no | Current cycle | format: "int64"; example: 5 |
| `open_due_date` | string (schema `OpenDueDate`) | no | Open due date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |
| `collection_status` | string (schema `CollectionStatus`) | no | Collection status:<br>* NORMAL<br>* OVERDUE<br><br>If a customer fails to pay at least the minimum amount due on their credit account by a specified number of days after the due date, the account's `collection_status` is set to `OVERDUE`. In all other cases, it should be `NORMAL`. For more information, refer to [Credit liquidation](doc:credit-liquidation).<br> | enum: ["NORMAL", "OVERDUE"]; example: "OVERDUE" |
| `balance` | object (schema `BalanceObject`) | no |  |  |
| `pending_accruals` | array of object (schema `PendingAccrualResponse`) | no |  |  |

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

Guides that link to this operation: `KU-CRED-agreements`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/accounts/{accountId}/transactions-balance operationId=getTransactionsBalance -->
### `GET /statements-v2/v1/accounts/{accountId}/transactions-balance` — List transaction balances

- **operationId:** `getTransactionsBalance`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List transaction balances.
>
> Use this endpoint to retrieve the details for one or more transactions. This endpoint could be useful if your customer has a dispute or needs credit card refinancing.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `statementId` | query | no | integer | Statement ID | format: "int64"; example: 1 |
| `transactionIds` | query | no | array of integer | Transaction IDs | example: [1, 2]; items.format: "int64" |
| `transactionTypeId` | query | no | array of integer | One or more transaction type IDs | example: [101, 112]; items.format: "int64" |
| `hasBalance` | query | no | boolean | Should returned transactions have a positive balance?<br>`true`: Return only transactions with balance > 0.<br>`false`: Return only transactions with balance = 0.<br>Default is all transactions.<br> | example: true |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |
| `withStatements` | query | no | boolean | If `true`, a 200 response includes the following additional fields for each transaction.<br>- `statement_id`<br>- `cycle`<br>- `cycle_closing_date`        <br>- `due_date`<br>- `real_due_date`<br>- `previous_balance`<br>- `debits`<br>- `credits`<br>- `current_balance`<br>- `minimum_payment`<br>- `status`<br> | example: true |
| `balanceType` | query | no | string | Filter the results by balance type. Possible values:<br>- `OPEN`: Statement is open. This is the current statement, before cycle closing.<br>- `CLOSED`: Statement is closed, and the due date has already passed.<br>- `CLOSED_NOT_DUE`: Statement is closed, but the due date has not yet passed. In other words, the current date is between the statement's cycle closing date and due date.<br>- `FUTURE`: Future statement. That is, a statement that has not been opened yet. Statements with this status usually include installments from purchases that will be due in future billing cycles.<br><br><b>Note:</b> You can only filter by balance type if `with_statement` is set to `true`. If `with_statement` is not set or is set to `false`, the `balanceType` parameter is ignored.<br> | enum: ["OPEN", "CLOSED", "CLOSED_NOT_DUE", "FUTURE"]; example: "OPEN" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `TransactionsBalanceListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPageDefault10`) | no | Items per page | default: 10; format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Number of items found | format: "int32"; example: 100 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 4 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Is this the last page? | example: true |
| `items` | array of object (schema `TransactionsBalanceResponse`) | no |  |  |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CORE-transactions-overview`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/accounts/{accountId}/statements/{statementId}/min-payment-memory operationId=getMinimumPaymentCalculationMemory -->
### `GET /statements-v2/v1/accounts/{accountId}/statements/{statementId}/min-payment-memory` — Get minimum payout calculation memory

- **operationId:** `getMinimumPaymentCalculationMemory`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a minimum payment calculation memory for a specific account statement. The minimum payout calculation memory is the information used in the [calculation of the minimum amount due (MAD)](doc:minimum-amount-due-calculation) and the results of that calculation.
>
> This this information in a JSON file. For example, in the following sample result, the default calculation strategy was used, the resulting MAD was 150, and two transactions were used in the calculation.
> {
>   "id": 1,
>   "created_at": "2021-08-10T00:00:00",
>   "org_id": "TN-e7091464-aa1e-4c20-8c68-1e4c57741234",
>   "account_id": 1010,
>   "statement_id": 1,
>   "calc_strategy": "DEFAULT",
>   "minimum_amount": 150,
>   "calculation_memory": [
>     {
>       "type": "PREVIOUS_STATEMENT_TRANSACTION",
>       "cycle": 4,
>       "amount": 43.74,
>       "balance": 43.74,
>       "percentage": 1.0,           
>       "transaction_id": 77489
>     },
>     {
>       "type": "CURRENT_STATEMENT_TRANSACTION",
>       "cycle": 5,
>       "amount": 3.65,
>       "balance": 3.65,
>       "percentage": 1.0,
>       "transaction_id": 77542
>     }
>   ]
> }
>
> The `calc_strategy` field has three possible values: `DEFAULT`, `PERCENTAGE_ONLY`, and `FIXED_PERCENTAGE_WITH_OVERLIMIT_AND_OVERDUE_AMOUNT`. These values correspond to the three possible settings for the `Minimum payment calculation method` program parameter: 0, 1, and 2. That is, `DEFAULT` = 0, `PERCENTAGE_ONLY` = 1, and `FIXED_PERCENTAGE_WITH_OVERLIMIT_AND_OVERDUE_AMOUNT` = 2. For more information, refer to [Minimum amount due calculation](doc:minimum-amount-due-calculation#full-amount-transactions).
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `statementId` | path | yes | integer | Statement ID | format: "int64"; example: 101 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `MinimumPaymentCalculationMemoryResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `MinPaymentCalculationID`) | no | Minimum payment calculation memory ID | format: "int64"; example: 1 |
| `created_at` | string (schema `CreatedAt`) | no | Creation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-10T00:00:00" |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-e7091464-cd1e-4c20-8c68-1e4c5774d972" |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1010 |
| `statement_id` | integer (schema `ClosedStatementID`) | no | Statement that closed with this minimum payment. | format: "int64"; example: 1 |
| `calc_strategy` | string (schema `CalcStrategy`) | no | Strategy for caculating minimum payment. For more information, refer to <a href="https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation">Minimum amount due calculation</a>. | enum: ["DEFAULT", "PERCENTAGE_ONLY", "FIXED_PERCENTAGE_WITH_OVERLIMIT_AND_OVERDUE_AMOUNT"]; example: "DEFAULT" |
| `minimum_amount` | number (schema `MinPaymentCalculatedAmount`) | no | Minimum payment calculated amount | format: "float"; example: 150 |
| `calculation_memory` | array of object (schema `CalculationMemoryResponse`) (schema `CalculationMemory`) | no |  |  |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=POST path=/statements-v2/v1/accounts/{accountId}/revolving-statement-summary operationId=postRevolvingStatementSummary -->
### `POST /statements-v2/v1/accounts/{accountId}/revolving-statement-summary` — Register revolving statement summary generation process

- **operationId:** `postRevolvingStatementSummary`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Registers a record with `PENDING` status to start the revolving statement summary generation process. When the process completes, it generates a [Revolving statement summary](https://developers.pismo.io/events/docs/balance-revolving-statement-summary-1) event containing the summary.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `RevolvingStatementSummaryResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `revolving_statements_summary_id` | integer (schema `RevolvingStatementsSummaryId`) | no | Revolving statement summary ID | format: "int64"; example: 1 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1010 |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-e7091464-cd1e-4c20-8c68-1e4c5774d972" |
| `cid` | string (schema `CID`) | no | Correlation ID used to link related API requests and events. | example: "3ea22692-a209-11eb-89a2-f73e179dcbc2" |
| `status` | string (schema `ImportedStatementStatusInSummaryResponse`) | no | Statement status. This is used to check if this endpoint has already registered a `PENDING` record. If not, the endpoint creates a new pending record. If it has, then it does nothing, since there is alread a record in progress.<br>  * PENDING<br>  * PROCESSED | enum: ["PENDING", "PROCESSED"]; example: "PENDING" |
| `created_at` | string | no | Date and time the summary was created. Format = YYYY-MM-DDThh:mm:ss. | example: "2021-08-10T00:00:00" |

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
| `balance-revolving-statement-summary-1` | https://developers.pismo.io/events/docs/balance-revolving-statement-summary-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Internal error" |

<!-- schema: #/components/schemas/InvalidFieldErrorResponse -->
### Schema `InvalidFieldErrorResponse`

Pointer: `#/components/schemas/InvalidFieldErrorResponse`. Type: object (schema `InvalidFieldErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Amount must not be empty." |
| `field` | string | yes | Field where error occurred. | example: "amount" |

<!-- schema: #/components/schemas/AccountStatementsResponse -->
### Schema `AccountStatementsResponse`

Pointer: `#/components/schemas/AccountStatementsResponse`. Type: object (schema `AccountStatementsResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `status` | string (schema `StatementStatus`) | no | Statement status. The possible values are:<br>* `CLOSED`: Statement is closed, and the due date has already passed.<br>* `CLOSED_NOT_DUE`: Statement is closed, but the due date has not yet passed. In other words, the current date is between the statement's cycle closing date and due date.<br>* `OPEN`: Statement is open. This is the current statement, before cycle closing.<br>* `FUTURE`: Future statement. That is, a statement that has not been opened yet. Statements with this status usually include installments from purchases that will be due in future billing cycles.<br> | example: "CLOSED" |
| `cycle` | integer (schema `CycleNumber`) | no | Cycle number. When an account is created, its first cycle is cycle number 1. This number is incremented for each successive cycle. | format: "int32"; example: 1 |
| `previous_balance` | number (schema `PreviousBalance`) | no | Amount you owed on the account when the previous statement closed. | format: "float"; example: 99.99 |
| `debits` | number (schema `Debits`) | no | Total debits for current cycle | format: "float"; example: 42.5 |
| `credits` | number (schema `Credits`) | no | Total credits for current cycle | format: "float"; example: 20 |
| `current_balance` | number (schema `CurrentBalance`) | no | Total amount you owe on the account right now. It updates as transactions post, so it can change many times during a billing cycle. `current_balance` = `previous_balance` + `debits` - `credits`. | example: 99.99 |
| `posted_date` | string (schema `PostedDate`) | no | Date posted. Format = yyyy-mm-dd. | format: "date"; example: "2022-02-11" |
| `minimum_payment` | number (schema `MinimumPayment`) | no | Statement minimum payment | format: "float"; example: 10.35 |
| `amount_due` | number (schema `AmountDue`) | no | Amount due. Must be less than or equal to `current_balance` and greater than zero. It should be equal to `current_balance` at cycle closing.<br>**Note:** This field only appears in closed statements and only if they were closed after 17 April 2025.<br> | format: "float"; example: 705 |
| `amount_paid_until_due_date` | number (schema `AmountPaidUntilDueDate`) | no | Amount discharged on or before real due date by credit transactions that <i>are</i> considered payments transactions.<br><b>Notes:</b><br>- If you do not use the program parameter [PAYMENTS_TTS](doc:multivalue-parameters) to configure the payments transactions, the Pismo platform uses the following transaction types as defaults: [201, 244, 255, 276, 282, 320, 342, 701, 711, 721, 2224]<br><br>- This field only appears in closed statements and only if they were closed after 17 April 2025.<br> | format: "float"; example: 300 |
| `amount_paid_after_due_date` | number (schema `AmountPaidAfterDueDate`) | no | Amount discharged after real due date by credit transactions that <i>are</i> considered payments transactions.<br><b>Notes:</b><br>- If you do not use the program parameter [PAYMENTS_TTS](doc:multivalue-parameters) to configure the payments transactions, the Pismo platform uses the following transaction types as defaults: [201, 244, 255, 276, 282, 320, 342, 701, 711, 721, 2224]<br><br>- This field only appears in closed statements and only if they were closed after 17 April 2025.<br> | format: "float"; example: 0 |
| `other_credits_until_due_date` | number (schema `OtherCreditsUntilDueDate`) | no | Amount discharged on or before real due date by credit transactions that <i>are not</i> considered payment transactions.<br><b>Notes:</b><br>- If you do not use the program parameter [PAYMENTS_TTS](doc:multivalue-parameters) to configure the payments transactions, the Pismo platform uses the following transaction types as defaults: [201, 244, 255, 276, 282, 320, 342, 701, 711, 721, 2224]<br><br>- This field only appears in closed statements and only if they were closed after 17 April 2025.<br> | format: "float"; example: 0 |
| `other_credits_after_due_date` | number (schema `OtherCreditsAfterDueDate`) | no | Amount discharged after real due date by credit transactions that <i>are not</i> considered payment transactions.<br><b>Notes:</b><br>- If you do not use the program parameter [PAYMENTS_TTS](doc:multivalue-parameters) to configure the payments transactions, the Pismo platform uses the following transaction types as defaults: [201, 244, 255, 276, 282, 320, 342, 701, 711, 721, 2224]<br><br>- This field only appears in closed statements and only if they were closed after 17 April 2025.<br> | format: "float"; example: 0 |
| `calendar` | object (schema `CalendarStatementsResponse`) | no |  |  |
| `evolve_to_delinquency` | boolean (schema `EvolveToDelinquency`) | no | Evolve to delinquency? If `false`, the account won't be updated to `OVERDUE`, and accruals won't be calculated.<br><br>For some features like [Minimo Boleto](doc:calculating-interest-accruals#minimum-amount) and [transactions configured to not evolve delinquency](doc:configuring-transaction-types-to-not-accrue-charges), `OpenDueDate` is not filled at cycle closing with the next due date. So, even if he cardholder does not pay, the account's collection status is not changed to `OVERDUE`. In this case, the account is said to be set to "not evolve to delinquency".<br> | example: true |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

<!-- schema: #/components/schemas/BalanceObject -->
### Schema `BalanceObject`

Pointer: `#/components/schemas/BalanceObject`. Type: object (schema `BalanceObject`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `closed_due` | number (schema `ClosedDue`) | no | Unpaid amount for the previous statement that is already closed, and the due date has passed. If the due date for the previous statement has passed, then `closed_due` is the unpaid amount from the previous statement, and `closed_not_due` is zero. | format: "float"; example: 150 |
| `closed_not_due` | number (schema `ClosedNotDue`) | no | Unpaid amount for the previous statement that is already closed, but the due date has not been passed. If the due date for the previous statement has not yet passed, then `closed_not_due` is the unpaid amount from the previous statement, and `closed_due` is zero. | format: "float"; example: 0 |
| `open` | number (schema `CurrentOpen`) | no | Total amount due for the current statement | format: "float"; example: 150 |
| `future` | number (schema `DueInFuture`) | no | Total amount for future installments | format: "float"; example: 200 |

<!-- schema: #/components/schemas/PendingAccrualResponse -->
### Schema `PendingAccrualResponse`

Pointer: `#/components/schemas/PendingAccrualResponse`. Type: object (schema `PendingAccrualResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_type` | string | no | Interest accrual type | example: "REFINANCING" |
| `amount` | number (schema `InterestAccrualAmount`) | no | Interest accrual amount | format: "float"; example: 2.5 |

<!-- schema: #/components/schemas/TransactionsBalanceResponse -->
### Schema `TransactionsBalanceResponse`

Pointer: `#/components/schemas/TransactionsBalanceResponse`. Type: object (schema `TransactionsBalanceResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; example: 150 |
| `tax_amount` | number (schema `TaxAmount`) | no | Tax amount | format: "float"; example: 7.99 |
| `interest_rate` | number (schema `TransactionInterestRate`) | no | Transaction interest rate. | format: "float"; example: 15.99 |
| `interest_amount` | number (schema `InterestAmount`) | no | Interest amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 12.35 |
| `balance_amount` | number (schema `BalanceAmount`) | no | Transaction balance. Unpaid balance for this transaction. | format: "float"; example: 43 |
| `event_datetime` | string (schema `EventDatetime`) | no | Event datetime. Format = yyyy-mm-dd:hr:mm:ss. | format: "full-date-time"; example: "2023-02-22T15:17:05" |
| `installment_number` | integer (schema `InstallmentNumber`) | no | Installment number | format: "int32"; minimum: 1; maximum: 36; example: 1 |
| `number_of_installments` | integer (schema `NumberOfInstallments`) | no | Number of installments | format: "int32"; example: 8 |
| `transaction_type_id` | integer (schema `TransactionTypeID`) | no | Transaction type ID | format: "int32"; example: 342 |
| `statement` | object (schema `StatementObject`) | no |  |  |

<!-- schema: #/components/schemas/CalculationMemoryResponse -->
### Schema `CalculationMemoryResponse`

Pointer: `#/components/schemas/CalculationMemoryResponse`. Type: object (schema `CalculationMemoryResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `CalculationMemoryType`) | no | Calculation memory type | enum: ["PREVIOUS_STATEMENT_TRANSACTION", "CURRENT_STATEMENT_TRANSACTION"]; example: "PREVIOUS_STATEMENT_TRANSACTION" |
| `transaction_id` | integer (schema `TransactionID`) | no | Transaction ID | format: "int64"; example: 77489 |
| `balance` | number (schema `MinPaymentTransactionBalance`) | no | Transaction balance when calculating the minimum payment | format: "float"; example: 100 |
| `percentage` | number (schema `MinPaymentPercentageOfTransactionsBalance`) | no | Minimum payment's percentage of transaction balance | format: "float"; example: 10 |
| `amount` | number (schema `MinPaymentCalculatedAmount`) | no | Minimum payment calculated amount | format: "float"; example: 150 |
| `cycle` | integer (schema `CycleNumber`) | no | Cycle number. When an account is created, its first cycle is cycle number 1. This number is incremented for each successive cycle. | format: "int32"; example: 1 |

<!-- schema: #/components/schemas/CalendarStatementsResponse -->
### Schema `CalendarStatementsResponse`

Pointer: `#/components/schemas/CalendarStatementsResponse`. Type: object (schema `CalendarStatementsResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calendar_id` | integer (schema `CalendarID`) | no | Calendar ID | format: "int64"; example: 57868 |
| `program_due_date_id` | integer (schema `ProgramDueDateID`) | no | Program due date ID | format: "int64"; example: 3812 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `cycle_closing_date` | string (schema `CycleClosingDate`) | no | Cycle closing date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-14" |
| `due_date` | string (schema `DueDate`) | no | Due date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |
| `real_due_date` | string (schema `RealDueDate`) | no | Real due date. The regular due date does not take holidays into account. The real due date does, so it might be a later date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |

<!-- schema: #/components/schemas/StatementObject -->
### Schema `StatementObject`

Pointer: `#/components/schemas/StatementObject`. Type: object (schema `StatementObject`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `cycle` | integer (schema `CycleNumber`) | no | Cycle number. When an account is created, its first cycle is cycle number 1. This number is incremented for each successive cycle. | format: "int32"; example: 1 |
| `cycle_closing_date` | string (schema `CycleClosingDate`) | no | Cycle closing date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-14" |
| `due_date` | string (schema `DueDate`) | no | Due date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |
| `real_due_date` | string (schema `RealDueDate`) | no | Real due date. The regular due date does not take holidays into account. The real due date does, so it might be a later date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |
| `previous_balance` | number (schema `PreviousBalance`) | no | Amount you owed on the account when the previous statement closed. | format: "float"; example: 99.99 |
| `debits` | number (schema `Debits`) | no | Total debits for current cycle | format: "float"; example: 42.5 |
| `credits` | number (schema `Credits`) | no | Total credits for current cycle | format: "float"; example: 20 |
| `current_balance` | number (schema `CurrentBalance`) | no | Total amount you owe on the account right now. It updates as transactions post, so it can change many times during a billing cycle. `current_balance` = `previous_balance` + `debits` - `credits`. | example: 99.99 |
| `minimum_payment` | number (schema `MinimumPayment`) | no | Statement minimum payment | format: "float"; example: 10.35 |
| `status` | string (schema `StatementStatus`) | no | Statement status. The possible values are:<br>* `CLOSED`: Statement is closed, and the due date has already passed.<br>* `CLOSED_NOT_DUE`: Statement is closed, but the due date has not yet passed. In other words, the current date is between the statement's cycle closing date and due date.<br>* `OPEN`: Statement is open. This is the current statement, before cycle closing.<br>* `FUTURE`: Future statement. That is, a statement that has not been opened yet. Statements with this status usually include installments from purchases that will be due in future billing cycles.<br> | example: "CLOSED" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Statement`: GET /statements/v1/accounts/{accountId}/next, GET /statements/v1/accounts/{accountId}/statements/{statementId}, GET /statements-v2/v3/accounts/{accountId}/statements, GET /statements-v2/v2/accounts/{accountId}/total-due, GET /statements-v2/v1/accounts/{accountId}/transactions-balance, GET /statements-v2/v1/accounts/{accountId}/statements/{statementId}/min-payment-memory, POST /statements-v2/v1/accounts/{accountId}/revolving-statement-summary | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CORE-transactions-overview` — Transactions overview
- `KU-CRED-agreements` — Agreements: compulsory, statement, installment and payment agreements
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-EVT-catalogue-balance` — Event catalogue: balance
