---
ku_id: KU-API-revolving-credit-statements--statement-minimum-amount-due
title: 'API reference: Revolving credit - Statements — Statement minimum amount due'
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
- getStatementAmountDue
- createStatementAmountDue
- deleteStatementAmountDue
related_kus:
- KU-CRED-minimum-amount-due-calculation
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Statement minimum amount due

**KU ID:** `KU-API-revolving-credit-statements--statement-minimum-amount-due` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Statement minimum amount due` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Minimum amount due endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements-v2/v1/accounts/{accountId}/minimum-amount-due` | `getStatementAmountDue` | Get statement minimum amount due | no |
| `POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due` | `createStatementAmountDue` | Create or update statement minimum amount due | no |
| `DELETE /statements-v2/v1/accounts/{accountId}/minimum-amount-due` | `deleteStatementAmountDue` | Disable statement minimum amount due | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/accounts/{accountId}/minimum-amount-due operationId=getStatementAmountDue -->
### `GET /statements-v2/v1/accounts/{accountId}/minimum-amount-due` — Get statement minimum amount due

- **operationId:** `getStatementAmountDue`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement minimum amount due`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the statement minimum amount due by account ID and statement ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `statementId` | query | no | integer | Statement ID. When passed, the `accrualType`, `endDate` and `beginDate` filters are canceled. The other filters can be used concurrently.<br> | example: 30300 |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `StatementMinimumAmountDueResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `amount_type` | string (schema `AmountType`) | no | Amount type<br>- If you set `amount_type` to `FIXED_AMOUNT`, then the value you enter for `minimum_amount_due` should represent that fixed amount.<br><br>- If you set `amount_type` to `PERCENTAGE`, then `minimum_amount_due` should represent a percentage of the current balance. For example, if you set `minimum_amount_due` to 0.1, then the Pismo platform calculates the MAD as 10% of the current balance.<br> | enum: ["FIXED_AMOUNT", "PERCENTAGE"]; example: "FIXED_AMOUNT" |
| `cycle` | integer (schema `StatementCycle`) | no | Statement cycle | format: "int32"; example: 7 |
| `current_balance` | number (schema `CurrentBalance`) | no | Total amount you owe on the account right now. It updates as transactions post, so it can change many times during a billing cycle. `current_balance` = `previous_balance` + `debits` - `credits`. | example: 99.99 |
| `minimum_amount_due` | number (schema `MinimumAmountDue`) | no | Minimum amount due for the current statement cycle<br>- If `amount_type` is set to `FIXED_AMOUNT`, then `minimum_amount_due` represents that fixed amount.<br><br>- If `amount_type` is set to `PERCENTAGE`, then `minimum_amount_due` represents a percentage of the current balance. For example, 0.1 represents 10% of the current balance.<br> | format: "float"; example: 100.07 |
| `enabled` | boolean (schema `MinimumAmountDueEnabled`) | no | Is statement minimum amount due enabled? | example: true |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Settings not found`:

```json
{
  "code": "CE0001",
  "message": "No Statements Minimum Amount Due found for the provided Statement_ID and Account_ID."
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
| 404 | `CE0001` | No Statements Minimum Amount Due found for the provided Statement_ID and Account_ID. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=POST path=/statements-v2/v1/accounts/{accountId}/minimum-amount-due operationId=createStatementAmountDue -->
### `POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due` — Create or update statement minimum amount due

- **operationId:** `createStatementAmountDue`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement minimum amount due`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create statement minimum amount due (MAD) for the current cycle, or update it if it already exists. Using this endpoint bypasses the configured strategy for calculating the MAD. For more information, refer to [Minimum amount due calculation](doc:minimum-amount-due-calculation).
>
> **Notes:**
> - Running this endpoint bypasses the configured strategy only for the **current** cycle. The configured strategy, if it exists, still applies to future statements.
> - The following example demonstrates how the Pismo platform handles the request when you run this endpoint.<br>
>   Suppose the due date for Cycle A is March 10. The next cycle after Cycle A is Cycle B.<br>
>   - If the Pismo platform receives the "Create or update statement minimum amount due request" on March 9, it updates the MAD for Cycle A.<br>
>   - If it receives the request on March 10, and the platform has not finished closing Cycle A, the endpoint returns an error.<br>**Note:** This happens even if the platform hasn't started the process of closing Cycle A. The platform doesn't update the MAD for Cycle A on it's cycle closing date.<br>
>   - If it receives the request on March 10, and the platform has finished closing Cycle A, it updates the MAD for Cycle B.<br>
>   - If it receives the request on March 11, it updates the MAD for the next cycle (Cycle B).<br>
> - To use this endpoint, the **Allow overriding the minimum amount due for the current statement** program parameter must be set to `true`. Otherwise, the endpoint generates an error.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `StatementMinimumAmountDueRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount_type` | string (schema `AmountType`) | yes | Amount type<br>- If you set `amount_type` to `FIXED_AMOUNT`, then the value you enter for `minimum_amount_due` should represent that fixed amount.<br><br>- If you set `amount_type` to `PERCENTAGE`, then `minimum_amount_due` should represent a percentage of the current balance. For example, if you set `minimum_amount_due` to 0.1, then the Pismo platform calculates the MAD as 10% of the current balance.<br> | enum: ["FIXED_AMOUNT", "PERCENTAGE"]; example: "FIXED_AMOUNT" |
| `minimum_amount_due` | number (schema `MinimumAmountDue`) | yes | Minimum amount due for the current statement cycle<br>- If `amount_type` is set to `FIXED_AMOUNT`, then `minimum_amount_due` represents that fixed amount.<br><br>- If `amount_type` is set to `PERCENTAGE`, then `minimum_amount_due` represents a percentage of the current balance. For example, 0.1 represents 10% of the current balance.<br> | format: "float"; example: 100.07 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `StatementMinimumAmountDueResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_id` | integer (schema `StatementID`) | no | Statement ID | format: "int64"; example: 9497889 |
| `amount_type` | string (schema `AmountType`) | no | Amount type<br>- If you set `amount_type` to `FIXED_AMOUNT`, then the value you enter for `minimum_amount_due` should represent that fixed amount.<br><br>- If you set `amount_type` to `PERCENTAGE`, then `minimum_amount_due` should represent a percentage of the current balance. For example, if you set `minimum_amount_due` to 0.1, then the Pismo platform calculates the MAD as 10% of the current balance.<br> | enum: ["FIXED_AMOUNT", "PERCENTAGE"]; example: "FIXED_AMOUNT" |
| `cycle` | integer (schema `StatementCycle`) | no | Statement cycle | format: "int32"; example: 7 |
| `current_balance` | number (schema `CurrentBalance`) | no | Total amount you owe on the account right now. It updates as transactions post, so it can change many times during a billing cycle. `current_balance` = `previous_balance` + `debits` - `credits`. | example: 99.99 |
| `minimum_amount_due` | number (schema `MinimumAmountDue`) | no | Minimum amount due for the current statement cycle<br>- If `amount_type` is set to `FIXED_AMOUNT`, then `minimum_amount_due` represents that fixed amount.<br><br>- If `amount_type` is set to `PERCENTAGE`, then `minimum_amount_due` represents a percentage of the current balance. For example, 0.1 represents 10% of the current balance.<br> | format: "float"; example: 100.07 |
| `enabled` | boolean (schema `MinimumAmountDueEnabled`) | no | Is statement minimum amount due enabled? | example: true |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Current Statement not found`:

```json
{
  "code": "CE0001",
  "message": "No Current Statement found for the provided Account_ID."
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
| 404 | `CE0001` | No Current Statement found for the provided Account_ID. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-minimum-amount-due-calculation`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=DELETE path=/statements-v2/v1/accounts/{accountId}/minimum-amount-due operationId=deleteStatementAmountDue -->
### `DELETE /statements-v2/v1/accounts/{accountId}/minimum-amount-due` — Disable statement minimum amount due

- **operationId:** `deleteStatementAmountDue`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statement minimum amount due`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Disable the current statement minimum amount due.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Current Statement not found`:

```json
{
  "code": "CE0001",
  "message": "No Current Statement found for the provided Account_ID."
}
```

404 Example `Settings not found`:

```json
{
  "code": "CE0001",
  "message": "No Statements Minimum Amount Due found for the provided Statement_ID and Account_ID."
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
| 404 | `CE0001` | No Current Statement found for the provided Account_ID. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

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

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Statement minimum amount due`: GET /statements-v2/v1/accounts/{accountId}/minimum-amount-due, POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due, DELETE /statements-v2/v1/accounts/{accountId}/minimum-amount-due | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-minimum-amount-due-calculation` — Minimum amount due calculation
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
