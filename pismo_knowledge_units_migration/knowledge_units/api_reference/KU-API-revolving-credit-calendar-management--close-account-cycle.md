---
ku_id: KU-API-revolving-credit-calendar-management--close-account-cycle
title: 'API reference: Revolving credit - Calendar management — Close account cycle'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Calendar_management.yaml
  sha256: 63fcebe8bc52b750ae3659d979a4f71e06445faaa31cdcd0566754ee3b9de3c9
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
- CycleClosingRequest
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 1.0.0
---

# API reference: Revolving credit - Calendar management — Close account cycle

**KU ID:** `KU-API-revolving-credit-calendar-management--close-account-cycle` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Close account cycle` in `api-specs/Revolving_credit_-_Calendar_management.yaml` (“Revolving credit - Calendar management”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoint to close cycle for a specific account

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/accounts/{accountId}/statement-close` | `CycleClosingRequest` | Close account cycle | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Calendar_management.yaml method=POST path=/v1/accounts/{accountId}/statement-close operationId=CycleClosingRequest -->
### `POST /v1/accounts/{accountId}/statement-close` — Close account cycle

- **operationId:** `CycleClosingRequest`
- **Specification:** `api-specs/Revolving_credit_-_Calendar_management.yaml` (Revolving credit - Calendar management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/calendar-management`
- **Tags:** `Close account cycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Close cycle for a specific account.
>
> **Note:** This endpoint does not change the account's due date or real due date. It only updates the cycle closing date to the date the endpoint is executed.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `x-tenant` | header | yes | string | Tenant ID |  |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header of an API endpoint call.<br>If the x-cid value isn't passed, one is automatically generated.<br> |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CycleClosingRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | Customer created tracking ID. Must consist of alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and colons (:), with a length from 1 to 128. The Pismo platform uses this field to implement idempotency and prevent duplicates.<br> | minLength: 1; maxLength: 128; example: "3368328d-e4c6-4c75-99a9-9d59f3501d8c" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `CycleClosingResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cycle_closing_request_id` | integer (schema `CycleClosingRequestIdResponse`) | no | ID generated for the request by the Pismo platform | format: "int64"; example: 365 |
| `account_id` | integer (schema `AccountIdResponse`) | no | Account ID | format: "int64"; example: 6912345 |
| `current_statement_id` | integer (schema `CurrentStatementId`) | no | ID of current statement | format: "int64"; example: 325632587 |
| `tracking_id` | string (schema `TrackingID`) | no | Customer created tracking ID. Must consist of alphanumeric characters (a-z, A-Z, 0-9), hyphens (-), and colons (:), with a length from 1 to 128. The Pismo platform uses this field to implement idempotency and prevent duplicates.<br> | minLength: 1; maxLength: 128; example: "3368328d-e4c6-4c75-99a9-9d59f3501d8c" |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `status` | string (schema `StatusCycleClosingRequest`) | no | Online cycle closing status. Possible values are [`PENDING`, `CYCLE_CLOSING_REQUESTED`, `ERROR`]. | enum: ["PENDING", "CYCLE_CLOSING_REQUESTED", "ERROR"]; example: "PENDING" |

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

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code | example: "EX0001" |
| `message` | string | no | Error message | example: "Internal error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Calendar_management.yaml` | tag `Close account cycle`: POST /v1/accounts/{accountId}/statement-close | https://github.com/PismoDevEx/pismo-api-specs | `63fcebe8bc52b750…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
