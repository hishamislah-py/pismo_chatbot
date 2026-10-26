---
ku_id: KU-API-revolving-credit-calendar-management--account-calendar-strategies
title: 'API reference: Revolving credit - Calendar management — Account calendar strategies'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- GetAcountCalendarStrategy
- UpdateAcountCalendarStrategy
related_kus:
- KU-CRED-calendar-management-strategies
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-EVT-catalogue-balance
specification_version: 1.0.0
---

# API reference: Revolving credit - Calendar management — Account calendar strategies

**KU ID:** `KU-API-revolving-credit-calendar-management--account-calendar-strategies` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Account calendar strategies` in `api-specs/Revolving_credit_-_Calendar_management.yaml` (“Revolving credit - Calendar management”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for account calendar strategies

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/calendar-strategies` | `GetAcountCalendarStrategy` | Get account calendar strategy | no |
| `PUT /v1/accounts/{accountId}/calendar-strategies` | `UpdateAcountCalendarStrategy` | Update account calendar strategy | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Calendar_management.yaml method=GET path=/v1/accounts/{accountId}/calendar-strategies operationId=GetAcountCalendarStrategy -->
### `GET /v1/accounts/{accountId}/calendar-strategies` — Get account calendar strategy

- **operationId:** `GetAcountCalendarStrategy`
- **Specification:** `api-specs/Revolving_credit_-_Calendar_management.yaml` (Revolving credit - Calendar management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/calendar-management`
- **Tags:** `Account calendar strategies`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the calendar strategy for an account.
>
> <b>Notes:</b>
> - A program calendar strategy is defined for a specific program. However, it can be associated with an account in that program, so you can search for accounts that are associated with a particular program calendar strategy.
> - This endpoint does not return information about a [fixed due date calendar](doc:fixed-due-date-calendars).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `x-tenant` | header | yes | string | Tenant ID |  |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header of an API endpoint call.<br>If the x-cid value isn't passed, one is automatically generated.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountCalendarStrategyGetResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |

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

<!-- op: spec=api-specs/Revolving_credit_-_Calendar_management.yaml method=PUT path=/v1/accounts/{accountId}/calendar-strategies operationId=UpdateAcountCalendarStrategy -->
### `PUT /v1/accounts/{accountId}/calendar-strategies` — Update account calendar strategy

- **operationId:** `UpdateAcountCalendarStrategy`
- **Specification:** `api-specs/Revolving_credit_-_Calendar_management.yaml` (Revolving credit - Calendar management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/calendar-management`
- **Tags:** `Account calendar strategies`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update an account calendar strategy. After a program calendar strategy is defined using [Create program calendar strategy](ref:createprogramcalendarstrategy), you must use this endpoint to assign the strategy to an account. If you have more than one program calendar strategy defined for a program, you can also use this endpoint to change the strategy assigned to an account.
>
> This endpoint generates a [Balance account changed](https://developers.pismo.io/events/docs/balance-balance-account-change-1) event.
>
> <b>Note:</b> This endpoint cannot be used to update a [fixed due date calendar](doc:fixed-due-date-calendars).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `x-tenant` | header | yes | string | Tenant ID |  |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header of an API endpoint call.<br>If the x-cid value isn't passed, one is automatically generated.<br> |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `AccountCalendarStrategyPutRequestDto`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | yes | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `apply_to_current_cycle` | boolean (schema `ApplyToCurrentCycle`) | no | Apply the strategy to the current cycle (`true`) or don't (`false`)? | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountCalendarStrategyPutResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |

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
| `balance-balance-account-change-1` | https://developers.pismo.io/events/docs/balance-balance-account-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CRED-calendar-management-strategies`.

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
| `api-specs/Revolving_credit_-_Calendar_management.yaml` | tag `Account calendar strategies`: GET /v1/accounts/{accountId}/calendar-strategies, PUT /v1/accounts/{accountId}/calendar-strategies | https://github.com/PismoDevEx/pismo-api-specs | `63fcebe8bc52b750…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-calendar-management-strategies` — Calendar management strategies (cycle closing and due dates)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-EVT-catalogue-balance` — Event catalogue: balance
