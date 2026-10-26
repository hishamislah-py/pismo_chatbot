---
ku_id: KU-API-revolving-credit-statements--due-date
title: 'API reference: Revolving credit - Statements — Due date'
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
- getProgramDueDates
- saveProgramDueDate
- GetAvailableDueDates1
- statementDueDate
- updateProgramDueDate
- UpdateStatementsDueDate
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CORE-accounts-overview
- KU-CRED-calendar-management-strategies
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Due date

**KU ID:** `KU-API-revolving-credit-statements--due-date` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Due date` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Statement due date endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements-v2/v1/programs/{programId}/due-dates` | `getProgramDueDates` | List program due dates | no |
| `POST /statements-v2/v1/programs/{programId}/due-dates` | `saveProgramDueDate` | Save program due date | no |
| `GET /statements/v1/accounts/{accountId}/available-due-dates` | `GetAvailableDueDates1` | List available due dates | no |
| `PATCH /statements-v2/v2/due-date` | `statementDueDate` | Update statements calendar | no |
| `PATCH /statements-v2/v1/programs/{programId}/due-dates/{programDueDateId}` | `updateProgramDueDate` | Update program due date | no |
| `PUT /statements/v1/accounts/{accountId}/statements/due-date` | `UpdateStatementsDueDate` | Change due date | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/programs/{programId}/due-dates operationId=getProgramDueDates -->
### `GET /statements-v2/v1/programs/{programId}/due-dates` — List program due dates

- **operationId:** `getProgramDueDates`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Due date`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List a program's due dates with filtering options. If a value for the `programDueDateId` query parameter is provided, the request returns either a list with only one item or no items if there is no program due date with this ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programDueDateId` | query | no | integer | Program due date ID | format: "int64"; example: 2 |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 1122 |
| `day` | query | no | integer | Due day (day of the month) | format: "int32"; example: 2 |
| `gracePeriodDays` | query | no | integer | Number of grace period days. Maximum value is 20. This value overrides the value of the <b>Number of days before due date to set the closing date of the statement</b> program parameter for the specified account.<br> | format: "int64"; maximum: 20; example: 2 |
| `hasGracePeriod` | query | no | boolean | If `hasGracePeriod` is `true`, the request returns only program due dates that have a custom grace period configured. If `false`, it returns only those that don't. If `hasGracePeriod` is not provided, all program due dates are returned. | example: false |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `ProgramDueDateResponse2`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 503 | Service unavailable | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPage`) | no | Items per page | example: 50 |
| `total_items` | integer (schema `TotalItems`) | no | Number of items found | format: "int32"; example: 100 |
| `items_on_page` | integer (schema `ItemsOnPage`) | no | Number of items on this page | format: "int32"; example: 5 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int32"; example: 4 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Is this the last page? | example: true |
| `items` | array of object | no |  | example: [{"program_due_date_id": 8287, "program_id": 3002, "day": 1, "active": true, "grace_period_days": 0, "exists_account": true}, {"program_due_date_id": 8292, "program_id": 3002, "day": 2, "active": false, "grace_period_days": 0, "exists_account": false}] |
| `items[].program_due_date_id` | integer (schema `ProgramDueDateID`) | no | Program due date ID | format: "int64"; example: 3812 |
| `items[].program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `items[].day` | integer (schema `Day`) | no | Due date day index | format: "int32"; example: 1 |
| `items[].active` | boolean (schema `ProgramDueDateActive`) | no | Is program due date active?<br><br><b>Note:</b> If you set `active` from `true` to `false`, this just means that you are no longer able to assign the program due date to an account. Accounts that are already using the program due date continue to use it.<br> | example: true |
| `items[].exists_account` | boolean (schema `ExistsAccount`) | no | Does account exist? | example: false |
| `items[].grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of grace period days. This value overrides the value of the program parameter <b>Number of days before due date to set the closing date of the statement</b> for the specified account.<br><br>You can change the grace period days for a statement any time before its due date.<br> | format: "int32"; example: 5 |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 503

503 Example `Internal Server Error`:

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
| 503 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;503`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=POST path=/statements-v2/v1/programs/{programId}/due-dates operationId=saveProgramDueDate -->
### `POST /statements-v2/v1/programs/{programId}/due-dates` — Save program due date

- **operationId:** `saveProgramDueDate`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Due date`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Save a program due date. Day **must** be between 1 and 28.
> (**Note:** Due date is *required* for credit full-balance program types.)
>
> When you execute this endpoint, the Pismo platform first checks to see if the specified due date already exists. If it finds an existing due date with the same values for `day` and `grace_period_days`, it considers this a match and determines that the specified due date <b>already exists</b>. In this case, there are two possibilities.
> - If `active` has the same value in both the existing due date and the request, the request does nothing.
> - If `active` has a different value in the request, the value of `active` in the existing due date is updated accordingly. In other words, you can use this endpoint to activate or deactivate an existing due date. <b>Note:</b>The preferred way of updating existing due dates is to use the [Update program due date](ref:updateprogramduedate) endpoint.
>
> If the platform <b>does not</b> find a match, then it creates a new due date. (Note: This means that you could end up with two due dates that have the same value for `day`, 
> but different values for `grace_period_days`.)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 1122 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProgramDueDateSaveRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `day` | integer (schema `Day`) | yes | Due date day index | format: "int32"; example: 1 |
| `active` | boolean (schema `ProgramDueDateActive`) | yes | Is program due date active?<br><br><b>Note:</b> If you set `active` from `true` to `false`, this just means that you are no longer able to assign the program due date to an account. Accounts that are already using the program due date continue to use it.<br> | example: true |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of grace period days. This value overrides the value of the program parameter <b>Number of days before due date to set the closing date of the statement</b> for the specified account.<br><br>You can change the grace period days for a statement any time before its due date.<br> | format: "int32"; example: 5 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | CREATED | `application/json`: object (schema `ProgramDueDateResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_due_date_id` | integer (schema `ProgramDueDateID`) | no | Program due date ID | format: "int64"; example: 3812 |
| `program_id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 1052 |
| `day` | integer (schema `Day`) | no | Due date day index | format: "int32"; example: 1 |
| `active` | boolean (schema `ProgramDueDateActive`) | no | Is program due date active?<br><br><b>Note:</b> If you set `active` from `true` to `false`, this just means that you are no longer able to assign the program due date to an account. Accounts that are already using the program due date continue to use it.<br> | example: true |
| `exists_account` | boolean (schema `ExistsAccount`) | no | Does account exist? | example: false |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of grace period days. This value overrides the value of the program parameter <b>Number of days before due date to set the closing date of the statement</b> for the specified account.<br><br>You can change the grace period days for a statement any time before its due date.<br> | format: "int32"; example: 5 |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-calendar-management-strategies`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements/v1/accounts/{accountId}/available-due-dates operationId=GetAvailableDueDates1 -->
### `GET /statements/v1/accounts/{accountId}/available-due-dates` — List available due dates

- **operationId:** `GetAvailableDueDates1`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Due date`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List available due dates with filtering options.
>
> **Note: This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `hasGracePeriod` | query | no | boolean | If `hasGracePeriod` is `true`, the request returns only program due dates that have a custom grace period configured. If `false`, it returns only those that don't. If `hasGracePeriod` is not provided, all program due dates are returned. | example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: oneOf: object (schema `GetAvailableDueDatesV1ResponseSuccess`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `InvalidFieldErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Program Type`:

```json
{
  "message": "Account is not from a credit program"
}
```

##### Response 404

404 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
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

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PATCH path=/statements-v2/v2/due-date operationId=statementDueDate -->
### `PATCH /statements-v2/v2/due-date` — Update statements calendar

- **operationId:** `statementDueDate`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Due date`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the calendar for one or more statements.
>
> **Notes:** 
> - To function properly, the calendar must be updated no later than two days before the cycle closes.
> - The endpoint only works for [fixed due date calendars](doc:fixed-due-date-calendars). For other types of calendars, refer to the [Calendar management strategies](doc:calendar-management-strategies) guide.
> - This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `StatementDueDateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_default_program_due_date_id` | integer (schema `ProgramDueDateIdForUpdateCalendar`) | yes | Program due date ID. This field defines the new program due date for future statements for this account. After each cycle closure, the Pismo platform generates a statement that uses the program due date defined in this request.<br> | format: "int64"; example: 3812 |
| `statements` | array of object (schema `StatementRequest`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `StatementDueDateResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `StandardErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 503 | Service unavailable | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_default_program_due_date_id` | integer (schema `ProgramDueDateID`) | no | Program due date ID | format: "int64"; example: 3812 |
| `statements` | array of object (schema `StatementCalendarResponse`) | no |  |  |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

400 Example `Not found account_default_program_due_date_id`:

```json
{
  "code": "CE0001",
  "message": "Invalid request body"
}
```

400 Example `Unexpected response`:

```json
{
  "code": "CE0001",
  "message": "Unexpected response. Code: 400, Body: {}"
}
```

##### Response 404

404 Example `Not found statement_id`:

```json
{
  "code": "CE0001",
  "message": "Information not found for statement_id (value = 1)"
}
```

404 Example `Not found calendar_id`:

```json
{
  "code": "CE0001",
  "message": "Information not found for calendar_id (value = 1)"
}
```

404 Example `Resource not found`:

```json
{
  "code": "CE0001",
  "message": "Resource account not found"
}
```

404 Example `Unexpected response`:

```json
{
  "code": "CE0001",
  "message": "Unexpected response. Code: 404, Body: {}"
}
```

##### Response 409

409 Example `Invalid account_default_program_due_date_id`:

```json
{
  "code": "CE0001",
  "message": "account_default_program_due_date_id is invalid for this account"
}
```

409 Example `Invalid calendar_id`:

```json
{
  "code": "CE0001",
  "message": "Selected calendar_id is invalid"
}
```

409 Example `statement_id from different account`:

```json
{
  "code": "CE0001",
  "message": "Selected statement_id (value = 1) is from a different account"
}
```

409 Example `statement_id from closed statement`:

```json
{
  "code": "CE0001",
  "message": "Selected statement_id (value = 1) is a closed statement"
}
```

409 Example `Disordered statement_id`:

```json
{
  "code": "CE0001",
  "message": "Selected statement_id (value = 1) is disordered"
}
```

409 Example `Past calendar_id`:

```json
{
  "code": "CE0001",
  "message": "Selected calendar_id (value = 1) has a past cycle closing date"
}
```

409 Example `calendar_id from different program`:

```json
{
  "code": "CE0001",
  "message": "Selected calendar_id (value = 1) is from a different program"
}
```

409 Example `Disordered calendar_id`:

```json
{
  "code": "CE0001",
  "message": "Selected calendar_id (value = 1) is disordered"
}
```

409 Example `Unexpected response`:

```json
{
  "code": "CE0001",
  "message": "Unexpected response. Code: 409, Body: {}"
}
```

##### Response 423

423 Example `Account Locked`:

```json
{
  "message": "The operation could not be completed because another process is manipulating the account (the account lock could not be obtained). Try again in a moment."
}
```

##### Response 503

503 Example `Internal Server Error`:

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
| 400 | `CE0001` | Invalid request body |
| 404 | `CE0001` | Information not found for statement_id (value = 1) |
| 409 | `CE0001` | account_default_program_due_date_id is invalid for this account |
| 503 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;423;503`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PATCH path=/statements-v2/v1/programs/{programId}/due-dates/{programDueDateId} operationId=updateProgramDueDate -->
### `PATCH /statements-v2/v1/programs/{programId}/due-dates/{programDueDateId}` — Update program due date

- **operationId:** `updateProgramDueDate`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Due date`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a program due date.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 1122 |
| `programDueDateId` | path | yes | integer | Program due date ID | format: "int64"; example: 2 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProgramDueDateUpdateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `active` | boolean (schema `ProgramDueDateActive`) | yes | Is program due date active?<br><br><b>Note:</b> If you set `active` from `true` to `false`, this just means that you are no longer able to assign the program due date to an account. Accounts that are already using the program due date continue to use it.<br> | example: true |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of grace period days. This value overrides the value of the program parameter <b>Number of days before due date to set the closing date of the statement</b> for the specified account.<br><br>You can change the grace period days for a statement any time before its due date.<br> | format: "int32"; example: 5 |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-calendar-management-strategies`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PUT path=/statements/v1/accounts/{accountId}/statements/due-date operationId=UpdateStatementsDueDate -->
### `PUT /statements/v1/accounts/{accountId}/statements/due-date` — Change due date

- **operationId:** `UpdateStatementsDueDate`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Due date`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the due date for all subsequent account statements.
>
> To avoid inconsistencies in the platform:
> - The new due date must always be greater than the current due date.
> - The new due date must always be greater than the current cycle closing date. 
>
> **Important:** The due date must be updated no later than two days before the cycle closes. If you try to update the due date within a day of the cycle closing date, the endpoint generates an error. This behavior is necessary to ensure accuracy on cycle closing and data consistency.
>
> By default, you can only update the due date once per credit cycle. If you update the due date, and then try to update it again before the end of the same cycle, the endpoint returns an error. This behavior can be disabled by setting the [Due date exchange control](doc:program-parameters-reference-table) program parameter to `false`.
>
> **Notes:**
> - Due date is *required* for credit full balance program types.
>
> - This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized message**.        

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `UpdateStatementsDueDateV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | yes | ID of desired program due date | format: "int32"; minimum: 1; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `UpdateStatementsDueDateV1ResponseSuccess`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `success` | boolean | yes | `true` if update operation was successful. `false` otherwise. | example: true |

##### Response 400

400 Example `Invalid due date`:

```json
{
  "message": "Invalid due date ID"
}
```

##### Response 404

404 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
}
```

##### Response 409

409 Example `Same due date id`:

```json
{
  "message": "Due date is the same already configured"
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CORE-accounts-overview`, `KU-CRED-calendar-management-strategies`.

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

<!-- schema: #/components/schemas/InvalidFieldErrorResponse -->
### Schema `InvalidFieldErrorResponse`

Pointer: `#/components/schemas/InvalidFieldErrorResponse`. Type: object (schema `InvalidFieldErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Amount must not be empty." |
| `field` | string | yes | Field where error occurred. | example: "amount" |

<!-- schema: #/components/schemas/StatementRequest -->
### Schema `StatementRequest`

Pointer: `#/components/schemas/StatementRequest`. Type: object (schema `StatementRequest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `calendar_id` | integer (schema `CalendarID`) | no | Calendar ID | format: "int64"; example: 57868 |

<!-- schema: #/components/schemas/StatementCalendarResponse -->
### Schema `StatementCalendarResponse`

Pointer: `#/components/schemas/StatementCalendarResponse`. Type: object (schema `StatementCalendarResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `cycle` | integer (schema `CycleNumber`) | no | Cycle number. When an account is created, its first cycle is cycle number 1. This number is incremented for each successive cycle. | format: "int32"; example: 1 |
| `calendar_id` | integer (schema `CalendarID`) | no | Calendar ID | format: "int64"; example: 57868 |
| `cycle_closing_date` | string (schema `CycleClosingDate`) | no | Cycle closing date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-14" |
| `due_date` | string (schema `DueDate`) | no | Due date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |
| `real_due_date` | string (schema `RealDueDate`) | no | Real due date. The regular due date does not take holidays into account. The real due date does, so it might be a later date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |
| `program_due_date_id` | integer (schema `ProgramDueDateID`) | no | Program due date ID | format: "int64"; example: 3812 |

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
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Due date`: GET /statements-v2/v1/programs/{programId}/due-dates, POST /statements-v2/v1/programs/{programId}/due-dates, GET /statements/v1/accounts/{accountId}/available-due-dates, PATCH /statements-v2/v2/due-date, PATCH /statements-v2/v1/programs/{programId}/due-dates/{programDueDateId}, PUT /statements/v1/accounts/{accountId}/statements/due-date | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CORE-accounts-overview` — Accounts
- `KU-CRED-calendar-management-strategies` — Calendar management strategies (cycle closing and due dates)
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
