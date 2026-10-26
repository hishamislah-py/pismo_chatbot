---
ku_id: KU-API-revolving-credit-calendar-management--list-calendars
title: 'API reference: Revolving credit - Calendar management — List calendars'
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
- ListCalendars
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 1.0.0
---

# API reference: Revolving credit - Calendar management — List calendars

**KU ID:** `KU-API-revolving-credit-calendar-management--list-calendars` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `List calendars` in `api-specs/Revolving_credit_-_Calendar_management.yaml` (“Revolving credit - Calendar management”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoint to list calendars

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/programs/{programId}/calendars` | `ListCalendars` | List calendars | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Calendar_management.yaml method=GET path=/v1/programs/{programId}/calendars operationId=ListCalendars -->
### `GET /v1/programs/{programId}/calendars` — List calendars

- **operationId:** `ListCalendars`
- **Specification:** `api-specs/Revolving_credit_-_Calendar_management.yaml` (Revolving credit - Calendar management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/calendar-management`
- **Tags:** `List calendars`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List calendars for a program.
>
> You can use the following fields to filter the results. At most one of these fields should be filled.
> - `dueDay`
> - `programCalendarStrategyId`
> - `divisionId`

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header of an API endpoint call.<br>If the x-cid value isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `dueDay` | query | no | integer | Due day of the calendar | format: "int32"; example: 15 |
| `programDueDateId` | query | no | integer | Program due date ID | format: "int64"; example: 123 |
| `programCalendarStrategyId` | query | no | integer | Program calendar strategy ID | format: "int64"; example: 5 |
| `includeDivisionCalendars` | query | no | boolean | Include division calendars? | example: true |
| `divisionId` | query | no | integer | Division ID | format: "int64"; example: 10 |
| `perPage` | query | no | integer | Items per page | default: 10; format: "int64"; minimum: 1; maximum: 500; example: 15 |
| `nextCursor` | query | no | integer | Cursor for pagination | format: "int64"; example: 30 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetCalendarsResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Is there is a next page? | example: true |
| `next_cursor` | integer | no | Cursor for the next page | format: "int64" |
| `calendars` | array of object (schema `CalendarDto`) | no | List of calendars |  |

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

<!-- schema: #/components/schemas/CalendarDto -->
### Schema `CalendarDto`

Pointer: `#/components/schemas/CalendarDto`. Type: object (schema `CalendarDto`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `calendar_id` | integer (schema `CalendarID`) | no | Calendar ID | format: "int64"; example: 57868 |
| `cycle_closing_date` | string (schema `CycleClosingDate`) | no | Cycle closing date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |
| `due_date` | string (schema `DueDate`) | no | Due date. Format = yyyy-mm-dd. | format: "date"; example: "2021-05-24" |
| `real_due_date` | string | no | Real due date | format: "date"; example: "2024-09-18" |
| `program_due_date_id` | integer | no | Program due date ID | format: "int64"; example: 1 |
| `program_calendar_strategy_id` | integer | no | Program calendar strategy ID | format: "int64"; example: 5 |
| `division_id` | integer | no | Division ID | format: "int64"; example: 10 |

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
| `api-specs/Revolving_credit_-_Calendar_management.yaml` | tag `List calendars`: GET /v1/programs/{programId}/calendars | https://github.com/PismoDevEx/pismo-api-specs | `63fcebe8bc52b750…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
