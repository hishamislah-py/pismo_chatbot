---
ku_id: KU-API-revolving-credit-calendar-management--program-calendar-strategies
title: 'API reference: Revolving credit - Calendar management — Program calendar strategies'
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
- ListProgramCalendarStrategies
- CreateProgramCalendarStrategy
- GetProgramCalendarStrategy
- UpdateProgramCalendarStrategy
related_kus:
- KU-CRED-calendar-management-strategies
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-EVT-catalogue-balance
specification_version: 1.0.0
---

# API reference: Revolving credit - Calendar management — Program calendar strategies

**KU ID:** `KU-API-revolving-credit-calendar-management--program-calendar-strategies` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Program calendar strategies` in `api-specs/Revolving_credit_-_Calendar_management.yaml` (“Revolving credit - Calendar management”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for program calendar strategies

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/programs/{programId}/calendar-strategies` | `ListProgramCalendarStrategies` | List program calendar strategies | no |
| `POST /v1/programs/{programId}/calendar-strategies` | `CreateProgramCalendarStrategy` | Create program calendar strategy | no |
| `GET /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` | `GetProgramCalendarStrategy` | Get program calendar strategy | no |
| `PATCH /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` | `UpdateProgramCalendarStrategy` | Update program calendar strategy | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Calendar_management.yaml method=GET path=/v1/programs/{programId}/calendar-strategies operationId=ListProgramCalendarStrategies -->
### `GET /v1/programs/{programId}/calendar-strategies` — List program calendar strategies

- **operationId:** `ListProgramCalendarStrategies`
- **Specification:** `api-specs/Revolving_credit_-_Calendar_management.yaml` (Revolving credit - Calendar management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/calendar-management`
- **Tags:** `Program calendar strategies`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List program calendar strategies and their configurations.
>
> <b>Note:</b> This endpoint does not return information about a [fixed due date calendar](doc:fixed-due-date-calendars).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header of an API endpoint call.<br>If the x-cid value isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |
| `active` | query | no | boolean | Is the program calendar strategy active? | example: true |
| `strategy` | query | no | string | Strategy used to create calendars<br> | enum: ["FIXED_CYCLE_CLOSING", "MONTHLY_CYCLE_CLOSING", "MONTHLY_DUE_DATE", "WEEKLY_CYCLE_CLOSING", "WEEKLY_DUE_DATE", "DAILY_CYCLE_CLOSING", "DAILY_DUE_DATE"]; example: "FIXED_CYCLE_CLOSING" |
| `page` | query | no | integer | Page number | default: 1; format: "int64"; example: 1 |
| `perPage` | query | no | integer | Items per page | default: 10; format: "int64"; minimum: 1; maximum: 500; example: 15 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | OK | `application/json`: object (schema `GetListCalendarStrategyResponseDto`) |
| 400 | Invalid payload | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page number | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum number of items per page | default: 10; format: "int32"; minimum: 1; example: 15 |
| `pages` | integer (schema `NumberOfPages`) | no | Number of pages | format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 100 |
| `items` | array of oneOf: object (schema `FIXED_CYCLE_CLOSING_ListResponse`), object (schema `MONTHLY_CYCLE_CLOSING_ListResponse`), object (schema `MONTHLY_DUE_DATE_ListResponse`), object (schema `WEEKLY_CYCLE_CLOSING_ListResponse`), object (schema `WEEKLY_DUE_DATE_ListResponse`), object (schema `DAILY_CYCLE_CLOSING_ListResponse`), object (schema `DAILY_DUE_DATE_ListResponse`) | no |  |  |

##### Response 400

400 Example `Calendar with same config already exist`:

```json
{
  "code": "EX300",
  "message": "Another strategy has the same configuration."
}
```

400 Example `Calendar Strategy not found`:

```json
{
  "code": "EX301",
  "message": "Calendar strategy not found."
}
```

400 Example `Invalid configuration`:

```json
{
  "code": "EX302",
  "message": "Field configuration is invalid."
}
```

400 Example `Invalid field cycleClosing`:

```json
{
  "code": "EX303",
  "message": "Field cycle_closing_day must be between 1 and 28."
}
```

400 Example `Cycle closing day required`:

```json
{
  "code": "EX304",
  "message": "Field cycle_closing_day is required."
}
```

400 Example `Days between cycle closing and due date required`:

```json
{
  "code": "EX305",
  "message": "Field days_between_cycle_closing_and_due_date is required."
}
```

400 Example `Days between cycle closing and due date required range`:

```json
{
  "code": "EX307",
  "message": "Field days_between_cycle_closing_and_due_date must be between 1 and 100."
}
```

400 Example `None of the updatable attributes passed`:

```json
{
  "code": "EX308",
  "message": "To proceed with this operation, please provide either the configuration update, the active flag, or both."
}
```

400 Example `Every x months out of range`:

```json
{
  "code": "EX1101",
  "message": "Field every_x_months must be between 1 and 12."
}
```

400 Example `Cycle closing day and nth specific weekday mutually exclusive`:

```json
{
  "code": "EX1102",
  "message": "Fields cycle_closing_day and nth_specific_weekday are mutually exclusive."
}
```

400 Example `Cycle closing day or nth specific weekday required`:

```json
{
  "code": "EX1103",
  "message": "Either cycle_closing_day or nth_specific_weekday must be provided."
}
```

400 Example `Day of week required (nth weekday)`:

```json
{
  "code": "EX1104",
  "message": "Field day_of_week is required."
}
```

400 Example `Day of week invalid (nth weekday)`:

```json
{
  "code": "EX1105",
  "message": "Field day_of_week must be a valid day of the week."
}
```

400 Example `Week of month required`:

```json
{
  "code": "EX1106",
  "message": "Field week_of_month is required."
}
```

400 Example `Week of month out of range`:

```json
{
  "code": "EX1107",
  "message": "Field week_of_month must be between 1 and 5."
}
```

400 Example `Due day and nth specific weekday mutually exclusive`:

```json
{
  "code": "EX1108",
  "message": "Fields due_day and nth_specific_weekday are mutually exclusive."
}
```

400 Example `Due day or nth specific weekday required`:

```json
{
  "code": "EX1109",
  "message": "Either due_day or nth_specific_weekday must be provided."
}
```

400 Example `Due day out of range`:

```json
{
  "code": "EX1110",
  "message": "Field due_day must be between 1 and 28."
}
```

400 Example `Day of week required (weekly)`:

```json
{
  "code": "EX1200",
  "message": "Field day_of_week is required."
}
```

400 Example `Day of week invalid (weekly)`:

```json
{
  "code": "EX1201",
  "message": "Field day_of_week must be a valid day of the week (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)."
}
```

400 Example `Every x weeks out of range`:

```json
{
  "code": "EX1203",
  "message": "Field every_x_weeks must be between 1 and 52."
}
```

400 Example `Every x days out of range`:

```json
{
  "code": "EX1301",
  "message": "Field every_x_days must be between 1 and 365."
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
| 400 | `EX300` | Another strategy has the same configuration. |
| 400 | `EX301` | Calendar strategy not found. |
| 400 | `EX302` | Field configuration is invalid. |
| 400 | `EX303` | Field cycle_closing_day must be between 1 and 28. |
| 400 | `EX304` | Field cycle_closing_day is required. |
| 400 | `EX305` | Field days_between_cycle_closing_and_due_date is required. |
| 400 | `EX307` | Field days_between_cycle_closing_and_due_date must be between 1 and 100. |
| 400 | `EX308` | To proceed with this operation, please provide either the configuration update, the active flag, or both. |
| 400 | `EX1101` | Field every_x_months must be between 1 and 12. |
| 400 | `EX1102` | Fields cycle_closing_day and nth_specific_weekday are mutually exclusive. |
| 400 | `EX1103` | Either cycle_closing_day or nth_specific_weekday must be provided. |
| 400 | `EX1104` | Field day_of_week is required. |
| 400 | `EX1105` | Field day_of_week must be a valid day of the week. |
| 400 | `EX1106` | Field week_of_month is required. |
| 400 | `EX1107` | Field week_of_month must be between 1 and 5. |
| 400 | `EX1108` | Fields due_day and nth_specific_weekday are mutually exclusive. |
| 400 | `EX1109` | Either due_day or nth_specific_weekday must be provided. |
| 400 | `EX1110` | Field due_day must be between 1 and 28. |
| 400 | `EX1200` | Field day_of_week is required. |
| 400 | `EX1201` | Field day_of_week must be a valid day of the week (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY). |
| 400 | `EX1203` | Field every_x_weeks must be between 1 and 52. |
| 400 | `EX1301` | Field every_x_days must be between 1 and 365. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Calendar_management.yaml method=POST path=/v1/programs/{programId}/calendar-strategies operationId=CreateProgramCalendarStrategy -->
### `POST /v1/programs/{programId}/calendar-strategies` — Create program calendar strategy

- **operationId:** `CreateProgramCalendarStrategy`
- **Specification:** `api-specs/Revolving_credit_-_Calendar_management.yaml` (Revolving credit - Calendar management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/calendar-management`
- **Tags:** `Program calendar strategies`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a program calendar strategy.
>
> Program calendar strategies provide new methods of calendar creation. For example, in the `FIXED_CYCLE_CLOSING` strategy, the `cycle_closing_date` of the calendar is fixed, but the due date is dynamic. The due date is calculated from the values set in the `configuration` object.
>
> This endpoint generates a [Program calendar strategy created](https://developers.pismo.io/events/docs/balance-program-calendar-strategy-created-1) event.
>
> <b>Note:</b> This endpoint cannot be used to create a [fixed due date calendar](doc:fixed-due-date-calendars).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header of an API endpoint call.<br>If the x-cid value isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |

#### Request body

Required: yes

**Content type `application/json`** — schema: oneOf: object (schema `FIXED_CYCLE_CLOSING`), object (schema `MONTHLY_CYCLE_CLOSING`), object (schema `MONTHLY_DUE_DATE`), object (schema `WEEKLY_CYCLE_CLOSING`), object (schema `WEEKLY_DUE_DATE`), object (schema `DAILY_CYCLE_CLOSING`), object (schema `DAILY_DUE_DATE`) (schema `CreateOrPatchProgramCalendarStrategyRequestDto`)

_oneOf option 1: schema `FIXED_CYCLE_CLOSING`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["FIXED_CYCLE_CLOSING"] |
| `configuration` | object | yes |  |  |
| `configuration.cycle_closing_day` | integer (schema `CycleClosingDay`) | yes | Day of the month for the cycle closing. Must be in the range 1 to 28. | format: "int32"; example: 10 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 2: schema `MONTHLY_CYCLE_CLOSING`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["MONTHLY_CYCLE_CLOSING"] |
| `configuration` | object | yes |  | example: {"cycle_closing_day": 15, "every_x_months": 1, "days_between_cycle_closing_and_due_date": 10} |
| `configuration.cycle_closing_day` | integer (schema `CycleClosingDay`) | no | Day of the month for the cycle closing. Must be in the range 1 to 28. | format: "int32"; example: 10 |
| `configuration.nth_specific_weekday` | object (schema `NthSpecificWeekday`) | no | Nth specific weekday of the month (e.g. 3rd Friday). Mutually exclusive with fixed day fields. | example: {"day_of_week": "FRIDAY", "week_of_month": 3} |
| `configuration.every_x_months` | integer (schema `EveryXMonths`) | no | Interval in months between cycles. Must be between 1 and 12. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 12; example: 1 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 3: schema `MONTHLY_DUE_DATE`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["MONTHLY_DUE_DATE"] |
| `configuration` | object | yes |  | example: {"due_day": 20, "every_x_months": 2, "days_between_cycle_closing_and_due_date": 10} |
| `configuration.due_day` | integer (schema `DueDay`) | no | Day of the month for the due date. Must be in the range 1 to 28. | format: "int32"; minimum: 1; maximum: 28; example: 20 |
| `configuration.nth_specific_weekday` | object (schema `NthSpecificWeekday`) | no | Nth specific weekday of the month (e.g. 3rd Friday). Mutually exclusive with fixed day fields. | example: {"day_of_week": "FRIDAY", "week_of_month": 3} |
| `configuration.every_x_months` | integer (schema `EveryXMonths`) | no | Interval in months between cycles. Must be between 1 and 12. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 12; example: 1 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 4: schema `WEEKLY_CYCLE_CLOSING`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["WEEKLY_CYCLE_CLOSING"] |
| `configuration` | object | yes |  | example: {"day_of_week": "MONDAY", "every_x_weeks": 2, "days_between_cycle_closing_and_due_date": 5} |
| `configuration.day_of_week` | string (schema `DayOfWeek`) | yes | Day of the week. | enum: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]; example: "FRIDAY" |
| `configuration.every_x_weeks` | integer (schema `EveryXWeeks`) | no | Interval in weeks between cycles. Must be between 1 and 52. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 52; example: 2 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 5: schema `WEEKLY_DUE_DATE`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["WEEKLY_DUE_DATE"] |
| `configuration` | object | yes |  | example: {"day_of_week": "FRIDAY", "every_x_weeks": 2, "days_between_cycle_closing_and_due_date": 5} |
| `configuration.day_of_week` | string (schema `DayOfWeek`) | yes | Day of the week. | enum: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]; example: "FRIDAY" |
| `configuration.every_x_weeks` | integer (schema `EveryXWeeks`) | no | Interval in weeks between cycles. Must be between 1 and 52. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 52; example: 2 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 6: schema `DAILY_CYCLE_CLOSING`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["DAILY_CYCLE_CLOSING"] |
| `configuration` | object | yes |  | example: {"every_x_days": 7, "days_between_cycle_closing_and_due_date": 3} |
| `configuration.every_x_days` | integer (schema `EveryXDays`) | no | Interval in days between cycles. Must be between 1 and 365. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 365; example: 7 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 7: schema `DAILY_DUE_DATE`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["DAILY_DUE_DATE"] |
| `configuration` | object | yes |  | example: {"every_x_days": 7, "days_between_cycle_closing_and_due_date": 3} |
| `configuration.every_x_days` | integer (schema `EveryXDays`) | no | Interval in days between cycles. Must be between 1 and 365. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 365; example: 7 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | OK | `application/json`: oneOf: object (schema `FIXED_CYCLE_CLOSING_response`), object (schema `MONTHLY_CYCLE_CLOSING_response`), object (schema `MONTHLY_DUE_DATE_response`), object (schema `WEEKLY_CYCLE_CLOSING_response`), object (schema `WEEKLY_DUE_DATE_response`), object (schema `DAILY_CYCLE_CLOSING_response`), object (schema `DAILY_DUE_DATE_response`) (schema `CreateProgramOrPatchCalendarStrategyResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

_No fields declared in the schema._

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
| `balance-program-calendar-strategy-created-1` | https://developers.pismo.io/events/docs/balance-program-calendar-strategy-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CRED-calendar-management-strategies`.

<!-- op: spec=api-specs/Revolving_credit_-_Calendar_management.yaml method=GET path=/v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId} operationId=GetProgramCalendarStrategy -->
### `GET /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` — Get program calendar strategy

- **operationId:** `GetProgramCalendarStrategy`
- **Specification:** `api-specs/Revolving_credit_-_Calendar_management.yaml` (Revolving credit - Calendar management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/calendar-management`
- **Tags:** `Program calendar strategies`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a program calendar strategy by its ID.
>
> <b>Note:</b> This endpoint cannot be used to retrieve information about a [fixed due date calendar](doc:fixed-due-date-calendars).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 6912345 |
| `programCalendarStrategyId` | path | yes | integer | Program calendar strategy ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header of an API endpoint call.<br>If the x-cid value isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | OK | `application/json`: oneOf: object (schema `FIXED_CYCLE_CLOSING_response`), object (schema `MONTHLY_CYCLE_CLOSING_response`), object (schema `MONTHLY_DUE_DATE_response`), object (schema `WEEKLY_CYCLE_CLOSING_response`), object (schema `WEEKLY_DUE_DATE_response`), object (schema `DAILY_CYCLE_CLOSING_response`), object (schema `DAILY_DUE_DATE_response`) (schema `GetCalendarStrategyResponseDto`) |
| 400 | Invalid payload | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Calendar with same config already exist`:

```json
{
  "code": "EX300",
  "message": "Another strategy has the same configuration."
}
```

400 Example `Calendar Strategy not found`:

```json
{
  "code": "EX301",
  "message": "Calendar strategy not found."
}
```

400 Example `Invalid configuration`:

```json
{
  "code": "EX302",
  "message": "Field configuration is invalid."
}
```

400 Example `Invalid field cycleClosing`:

```json
{
  "code": "EX303",
  "message": "Field cycle_closing_day must be between 1 and 28."
}
```

400 Example `Cycle closing day required`:

```json
{
  "code": "EX304",
  "message": "Field cycle_closing_day is required."
}
```

400 Example `Days between cycle closing and due date required`:

```json
{
  "code": "EX305",
  "message": "Field days_between_cycle_closing_and_due_date is required."
}
```

400 Example `Days between cycle closing and due date required range`:

```json
{
  "code": "EX307",
  "message": "Field days_between_cycle_closing_and_due_date must be between 1 and 100."
}
```

400 Example `None of the updatable attributes passed`:

```json
{
  "code": "EX308",
  "message": "To proceed with this operation, please provide either the configuration update, the active flag, or both."
}
```

400 Example `Every x months out of range`:

```json
{
  "code": "EX1101",
  "message": "Field every_x_months must be between 1 and 12."
}
```

400 Example `Cycle closing day and nth specific weekday mutually exclusive`:

```json
{
  "code": "EX1102",
  "message": "Fields cycle_closing_day and nth_specific_weekday are mutually exclusive."
}
```

400 Example `Cycle closing day or nth specific weekday required`:

```json
{
  "code": "EX1103",
  "message": "Either cycle_closing_day or nth_specific_weekday must be provided."
}
```

400 Example `Day of week required (nth weekday)`:

```json
{
  "code": "EX1104",
  "message": "Field day_of_week is required."
}
```

400 Example `Day of week invalid (nth weekday)`:

```json
{
  "code": "EX1105",
  "message": "Field day_of_week must be a valid day of the week."
}
```

400 Example `Week of month required`:

```json
{
  "code": "EX1106",
  "message": "Field week_of_month is required."
}
```

400 Example `Week of month out of range`:

```json
{
  "code": "EX1107",
  "message": "Field week_of_month must be between 1 and 5."
}
```

400 Example `Due day and nth specific weekday mutually exclusive`:

```json
{
  "code": "EX1108",
  "message": "Fields due_day and nth_specific_weekday are mutually exclusive."
}
```

400 Example `Due day or nth specific weekday required`:

```json
{
  "code": "EX1109",
  "message": "Either due_day or nth_specific_weekday must be provided."
}
```

400 Example `Due day out of range`:

```json
{
  "code": "EX1110",
  "message": "Field due_day must be between 1 and 28."
}
```

400 Example `Day of week required (weekly)`:

```json
{
  "code": "EX1200",
  "message": "Field day_of_week is required."
}
```

400 Example `Day of week invalid (weekly)`:

```json
{
  "code": "EX1201",
  "message": "Field day_of_week must be a valid day of the week (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)."
}
```

400 Example `Every x weeks out of range`:

```json
{
  "code": "EX1203",
  "message": "Field every_x_weeks must be between 1 and 52."
}
```

400 Example `Every x days out of range`:

```json
{
  "code": "EX1301",
  "message": "Field every_x_days must be between 1 and 365."
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
| 400 | `EX300` | Another strategy has the same configuration. |
| 400 | `EX301` | Calendar strategy not found. |
| 400 | `EX302` | Field configuration is invalid. |
| 400 | `EX303` | Field cycle_closing_day must be between 1 and 28. |
| 400 | `EX304` | Field cycle_closing_day is required. |
| 400 | `EX305` | Field days_between_cycle_closing_and_due_date is required. |
| 400 | `EX307` | Field days_between_cycle_closing_and_due_date must be between 1 and 100. |
| 400 | `EX308` | To proceed with this operation, please provide either the configuration update, the active flag, or both. |
| 400 | `EX1101` | Field every_x_months must be between 1 and 12. |
| 400 | `EX1102` | Fields cycle_closing_day and nth_specific_weekday are mutually exclusive. |
| 400 | `EX1103` | Either cycle_closing_day or nth_specific_weekday must be provided. |
| 400 | `EX1104` | Field day_of_week is required. |
| 400 | `EX1105` | Field day_of_week must be a valid day of the week. |
| 400 | `EX1106` | Field week_of_month is required. |
| 400 | `EX1107` | Field week_of_month must be between 1 and 5. |
| 400 | `EX1108` | Fields due_day and nth_specific_weekday are mutually exclusive. |
| 400 | `EX1109` | Either due_day or nth_specific_weekday must be provided. |
| 400 | `EX1110` | Field due_day must be between 1 and 28. |
| 400 | `EX1200` | Field day_of_week is required. |
| 400 | `EX1201` | Field day_of_week must be a valid day of the week (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY). |
| 400 | `EX1203` | Field every_x_weeks must be between 1 and 52. |
| 400 | `EX1301` | Field every_x_days must be between 1 and 365. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Calendar_management.yaml method=PATCH path=/v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId} operationId=UpdateProgramCalendarStrategy -->
### `PATCH /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}` — Update program calendar strategy

- **operationId:** `UpdateProgramCalendarStrategy`
- **Specification:** `api-specs/Revolving_credit_-_Calendar_management.yaml` (Revolving credit - Calendar management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/calendar-management`
- **Tags:** `Program calendar strategies`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a program calendar strategy.
>
> This endpoint generates a [Program calendar strategy updated](https://developers.pismo.io/events/docs/balance-program-calendar-strategy-updated-1) event.
>
> <b>Note:</b> This endpoint cannot be used to update a [fixed due date calendar](doc:fixed-due-date-calendars).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 6912345 |
| `programCalendarStrategyId` | path | yes | integer | Program calendar strategy ID | format: "int64"; example: 6912345 |
| `x-cid` | header | no | string | The Correlation Identifier field is used to link related API requests and events. The x-cid can help the Pismo engineering team track everything related to a call. You can find the x-cid field in the response header of an API endpoint call.<br>If the x-cid value isn't passed, one is automatically generated.<br> | example: "5bb05174-4e80-11ea-b77f-2e728ce88125" |

#### Request body

Required: yes

**Content type `application/json`** — schema: oneOf: object (schema `FIXED_CYCLE_CLOSING`), object (schema `MONTHLY_CYCLE_CLOSING`), object (schema `MONTHLY_DUE_DATE`), object (schema `WEEKLY_CYCLE_CLOSING`), object (schema `WEEKLY_DUE_DATE`), object (schema `DAILY_CYCLE_CLOSING`), object (schema `DAILY_DUE_DATE`) (schema `CreateOrPatchProgramCalendarStrategyRequestDto`)

_oneOf option 1: schema `FIXED_CYCLE_CLOSING`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["FIXED_CYCLE_CLOSING"] |
| `configuration` | object | yes |  |  |
| `configuration.cycle_closing_day` | integer (schema `CycleClosingDay`) | yes | Day of the month for the cycle closing. Must be in the range 1 to 28. | format: "int32"; example: 10 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 2: schema `MONTHLY_CYCLE_CLOSING`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["MONTHLY_CYCLE_CLOSING"] |
| `configuration` | object | yes |  | example: {"cycle_closing_day": 15, "every_x_months": 1, "days_between_cycle_closing_and_due_date": 10} |
| `configuration.cycle_closing_day` | integer (schema `CycleClosingDay`) | no | Day of the month for the cycle closing. Must be in the range 1 to 28. | format: "int32"; example: 10 |
| `configuration.nth_specific_weekday` | object (schema `NthSpecificWeekday`) | no | Nth specific weekday of the month (e.g. 3rd Friday). Mutually exclusive with fixed day fields. | example: {"day_of_week": "FRIDAY", "week_of_month": 3} |
| `configuration.every_x_months` | integer (schema `EveryXMonths`) | no | Interval in months between cycles. Must be between 1 and 12. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 12; example: 1 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 3: schema `MONTHLY_DUE_DATE`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["MONTHLY_DUE_DATE"] |
| `configuration` | object | yes |  | example: {"due_day": 20, "every_x_months": 2, "days_between_cycle_closing_and_due_date": 10} |
| `configuration.due_day` | integer (schema `DueDay`) | no | Day of the month for the due date. Must be in the range 1 to 28. | format: "int32"; minimum: 1; maximum: 28; example: 20 |
| `configuration.nth_specific_weekday` | object (schema `NthSpecificWeekday`) | no | Nth specific weekday of the month (e.g. 3rd Friday). Mutually exclusive with fixed day fields. | example: {"day_of_week": "FRIDAY", "week_of_month": 3} |
| `configuration.every_x_months` | integer (schema `EveryXMonths`) | no | Interval in months between cycles. Must be between 1 and 12. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 12; example: 1 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 4: schema `WEEKLY_CYCLE_CLOSING`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["WEEKLY_CYCLE_CLOSING"] |
| `configuration` | object | yes |  | example: {"day_of_week": "MONDAY", "every_x_weeks": 2, "days_between_cycle_closing_and_due_date": 5} |
| `configuration.day_of_week` | string (schema `DayOfWeek`) | yes | Day of the week. | enum: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]; example: "FRIDAY" |
| `configuration.every_x_weeks` | integer (schema `EveryXWeeks`) | no | Interval in weeks between cycles. Must be between 1 and 52. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 52; example: 2 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 5: schema `WEEKLY_DUE_DATE`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["WEEKLY_DUE_DATE"] |
| `configuration` | object | yes |  | example: {"day_of_week": "FRIDAY", "every_x_weeks": 2, "days_between_cycle_closing_and_due_date": 5} |
| `configuration.day_of_week` | string (schema `DayOfWeek`) | yes | Day of the week. | enum: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]; example: "FRIDAY" |
| `configuration.every_x_weeks` | integer (schema `EveryXWeeks`) | no | Interval in weeks between cycles. Must be between 1 and 52. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 52; example: 2 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 6: schema `DAILY_CYCLE_CLOSING`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["DAILY_CYCLE_CLOSING"] |
| `configuration` | object | yes |  | example: {"every_x_days": 7, "days_between_cycle_closing_and_due_date": 3} |
| `configuration.every_x_days` | integer (schema `EveryXDays`) | no | Interval in days between cycles. Must be between 1 and 365. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 365; example: 7 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

_oneOf option 7: schema `DAILY_DUE_DATE`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `strategy` | string | no | Program calendar strategy | enum: ["DAILY_DUE_DATE"] |
| `configuration` | object | yes |  | example: {"every_x_days": 7, "days_between_cycle_closing_and_due_date": 3} |
| `configuration.every_x_days` | integer (schema `EveryXDays`) | no | Interval in days between cycles. Must be between 1 and 365. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 365; example: 7 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | yes | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |


#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | OK | `application/json`: oneOf: object (schema `FIXED_CYCLE_CLOSING_response`), object (schema `MONTHLY_CYCLE_CLOSING_response`), object (schema `MONTHLY_DUE_DATE_response`), object (schema `WEEKLY_CYCLE_CLOSING_response`), object (schema `WEEKLY_DUE_DATE_response`), object (schema `DAILY_CYCLE_CLOSING_response`), object (schema `DAILY_DUE_DATE_response`) (schema `CreateProgramOrPatchCalendarStrategyResponseDto`) |
| 400 | Invalid payload | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Calendar with same config already exist`:

```json
{
  "code": "EX300",
  "message": "Another strategy has the same configuration."
}
```

400 Example `Calendar Strategy not found`:

```json
{
  "code": "EX301",
  "message": "Calendar strategy not found."
}
```

400 Example `Invalid configuration`:

```json
{
  "code": "EX302",
  "message": "Field configuration is invalid."
}
```

400 Example `Invalid field cycleClosing`:

```json
{
  "code": "EX303",
  "message": "Field cycle_closing_day must be between 1 and 28."
}
```

400 Example `Cycle closing day required`:

```json
{
  "code": "EX304",
  "message": "Field cycle_closing_day is required."
}
```

400 Example `Days between cycle closing and due date required`:

```json
{
  "code": "EX305",
  "message": "Field days_between_cycle_closing_and_due_date is required."
}
```

400 Example `Days between cycle closing and due date required range`:

```json
{
  "code": "EX307",
  "message": "Field days_between_cycle_closing_and_due_date must be between 1 and 100."
}
```

400 Example `None of the updatable attributes passed`:

```json
{
  "code": "EX308",
  "message": "To proceed with this operation, please provide either the configuration update, the active flag, or both."
}
```

400 Example `Every x months out of range`:

```json
{
  "code": "EX1101",
  "message": "Field every_x_months must be between 1 and 12."
}
```

400 Example `Cycle closing day and nth specific weekday mutually exclusive`:

```json
{
  "code": "EX1102",
  "message": "Fields cycle_closing_day and nth_specific_weekday are mutually exclusive."
}
```

400 Example `Cycle closing day or nth specific weekday required`:

```json
{
  "code": "EX1103",
  "message": "Either cycle_closing_day or nth_specific_weekday must be provided."
}
```

400 Example `Day of week required (nth weekday)`:

```json
{
  "code": "EX1104",
  "message": "Field day_of_week is required."
}
```

400 Example `Day of week invalid (nth weekday)`:

```json
{
  "code": "EX1105",
  "message": "Field day_of_week must be a valid day of the week."
}
```

400 Example `Week of month required`:

```json
{
  "code": "EX1106",
  "message": "Field week_of_month is required."
}
```

400 Example `Week of month out of range`:

```json
{
  "code": "EX1107",
  "message": "Field week_of_month must be between 1 and 5."
}
```

400 Example `Due day and nth specific weekday mutually exclusive`:

```json
{
  "code": "EX1108",
  "message": "Fields due_day and nth_specific_weekday are mutually exclusive."
}
```

400 Example `Due day or nth specific weekday required`:

```json
{
  "code": "EX1109",
  "message": "Either due_day or nth_specific_weekday must be provided."
}
```

400 Example `Due day out of range`:

```json
{
  "code": "EX1110",
  "message": "Field due_day must be between 1 and 28."
}
```

400 Example `Day of week required (weekly)`:

```json
{
  "code": "EX1200",
  "message": "Field day_of_week is required."
}
```

400 Example `Day of week invalid (weekly)`:

```json
{
  "code": "EX1201",
  "message": "Field day_of_week must be a valid day of the week (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY)."
}
```

400 Example `Every x weeks out of range`:

```json
{
  "code": "EX1203",
  "message": "Field every_x_weeks must be between 1 and 52."
}
```

400 Example `Every x days out of range`:

```json
{
  "code": "EX1301",
  "message": "Field every_x_days must be between 1 and 365."
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
| 400 | `EX300` | Another strategy has the same configuration. |
| 400 | `EX301` | Calendar strategy not found. |
| 400 | `EX302` | Field configuration is invalid. |
| 400 | `EX303` | Field cycle_closing_day must be between 1 and 28. |
| 400 | `EX304` | Field cycle_closing_day is required. |
| 400 | `EX305` | Field days_between_cycle_closing_and_due_date is required. |
| 400 | `EX307` | Field days_between_cycle_closing_and_due_date must be between 1 and 100. |
| 400 | `EX308` | To proceed with this operation, please provide either the configuration update, the active flag, or both. |
| 400 | `EX1101` | Field every_x_months must be between 1 and 12. |
| 400 | `EX1102` | Fields cycle_closing_day and nth_specific_weekday are mutually exclusive. |
| 400 | `EX1103` | Either cycle_closing_day or nth_specific_weekday must be provided. |
| 400 | `EX1104` | Field day_of_week is required. |
| 400 | `EX1105` | Field day_of_week must be a valid day of the week. |
| 400 | `EX1106` | Field week_of_month is required. |
| 400 | `EX1107` | Field week_of_month must be between 1 and 5. |
| 400 | `EX1108` | Fields due_day and nth_specific_weekday are mutually exclusive. |
| 400 | `EX1109` | Either due_day or nth_specific_weekday must be provided. |
| 400 | `EX1110` | Field due_day must be between 1 and 28. |
| 400 | `EX1200` | Field day_of_week is required. |
| 400 | `EX1201` | Field day_of_week must be a valid day of the week (MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY). |
| 400 | `EX1203` | Field every_x_weeks must be between 1 and 52. |
| 400 | `EX1301` | Field every_x_days must be between 1 and 365. |
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-program-calendar-strategy-updated-1` | https://developers.pismo.io/events/docs/balance-program-calendar-strategy-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/FIXED_CYCLE_CLOSING_ListResponse -->
### Schema `FIXED_CYCLE_CLOSING_ListResponse`

Pointer: `#/components/schemas/FIXED_CYCLE_CLOSING_ListResponse`. Type: object (schema `FIXED_CYCLE_CLOSING_ListResponse`).

> Cycle closing date is fixed. Due date is dynamic.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 1122 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `strategy` | string (schema `FixedCycleClosingStrategy`) | no | Program calendar strategy | enum: ["FIXED_CYCLE_CLOSING"] |
| `configuration` | object | no |  |  |
| `configuration.cycle_closing_day` | integer (schema `CycleClosingDay`) | no | Day of the month for the cycle closing. Must be in the range 1 to 28. | format: "int32"; example: 10 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | no | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

<!-- schema: #/components/schemas/MONTHLY_CYCLE_CLOSING_ListResponse -->
### Schema `MONTHLY_CYCLE_CLOSING_ListResponse`

Pointer: `#/components/schemas/MONTHLY_CYCLE_CLOSING_ListResponse`. Type: object (schema `MONTHLY_CYCLE_CLOSING_ListResponse`).

> Cycle closes on a fixed day or Nth weekday each month.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 1122 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `strategy` | string | no | Program calendar strategy | enum: ["MONTHLY_CYCLE_CLOSING"] |
| `configuration` | object | no |  |  |
| `configuration.cycle_closing_day` | integer (schema `CycleClosingDay`) | no | Day of the month for the cycle closing. Must be in the range 1 to 28. | format: "int32"; example: 10 |
| `configuration.nth_specific_weekday` | object (schema `NthSpecificWeekday`) | no | Nth specific weekday of the month (e.g. 3rd Friday). Mutually exclusive with fixed day fields. | example: {"day_of_week": "FRIDAY", "week_of_month": 3} |
| `configuration.every_x_months` | integer (schema `EveryXMonths`) | no | Interval in months between cycles. Must be between 1 and 12. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 12; example: 1 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | no | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

<!-- schema: #/components/schemas/MONTHLY_DUE_DATE_ListResponse -->
### Schema `MONTHLY_DUE_DATE_ListResponse`

Pointer: `#/components/schemas/MONTHLY_DUE_DATE_ListResponse`. Type: object (schema `MONTHLY_DUE_DATE_ListResponse`).

> Due date falls on a fixed day or Nth weekday each month.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 1122 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `strategy` | string | no | Program calendar strategy | enum: ["MONTHLY_DUE_DATE"] |
| `configuration` | object | no |  |  |
| `configuration.due_day` | integer (schema `DueDay`) | no | Day of the month for the due date. Must be in the range 1 to 28. | format: "int32"; minimum: 1; maximum: 28; example: 20 |
| `configuration.nth_specific_weekday` | object (schema `NthSpecificWeekday`) | no | Nth specific weekday of the month (e.g. 3rd Friday). Mutually exclusive with fixed day fields. | example: {"day_of_week": "FRIDAY", "week_of_month": 3} |
| `configuration.every_x_months` | integer (schema `EveryXMonths`) | no | Interval in months between cycles. Must be between 1 and 12. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 12; example: 1 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | no | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

<!-- schema: #/components/schemas/WEEKLY_CYCLE_CLOSING_ListResponse -->
### Schema `WEEKLY_CYCLE_CLOSING_ListResponse`

Pointer: `#/components/schemas/WEEKLY_CYCLE_CLOSING_ListResponse`. Type: object (schema `WEEKLY_CYCLE_CLOSING_ListResponse`).

> Cycle closes on a specific weekday every N weeks.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 1122 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `strategy` | string | no | Program calendar strategy | enum: ["WEEKLY_CYCLE_CLOSING"] |
| `configuration` | object | no |  |  |
| `configuration.day_of_week` | string (schema `DayOfWeek`) | no | Day of the week. | enum: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]; example: "FRIDAY" |
| `configuration.every_x_weeks` | integer (schema `EveryXWeeks`) | no | Interval in weeks between cycles. Must be between 1 and 52. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 52; example: 2 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | no | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

<!-- schema: #/components/schemas/WEEKLY_DUE_DATE_ListResponse -->
### Schema `WEEKLY_DUE_DATE_ListResponse`

Pointer: `#/components/schemas/WEEKLY_DUE_DATE_ListResponse`. Type: object (schema `WEEKLY_DUE_DATE_ListResponse`).

> Due date falls on a specific weekday every N weeks.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 1122 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `strategy` | string | no | Program calendar strategy | enum: ["WEEKLY_DUE_DATE"] |
| `configuration` | object | no |  |  |
| `configuration.day_of_week` | string (schema `DayOfWeek`) | no | Day of the week. | enum: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]; example: "FRIDAY" |
| `configuration.every_x_weeks` | integer (schema `EveryXWeeks`) | no | Interval in weeks between cycles. Must be between 1 and 52. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 52; example: 2 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | no | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

<!-- schema: #/components/schemas/DAILY_CYCLE_CLOSING_ListResponse -->
### Schema `DAILY_CYCLE_CLOSING_ListResponse`

Pointer: `#/components/schemas/DAILY_CYCLE_CLOSING_ListResponse`. Type: object (schema `DAILY_CYCLE_CLOSING_ListResponse`).

> Cycle closes every N days.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 1122 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `strategy` | string | no | Program calendar strategy | enum: ["DAILY_CYCLE_CLOSING"] |
| `configuration` | object | no |  |  |
| `configuration.every_x_days` | integer (schema `EveryXDays`) | no | Interval in days between cycles. Must be between 1 and 365. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 365; example: 7 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | no | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

<!-- schema: #/components/schemas/DAILY_DUE_DATE_ListResponse -->
### Schema `DAILY_DUE_DATE_ListResponse`

Pointer: `#/components/schemas/DAILY_DUE_DATE_ListResponse`. Type: object (schema `DAILY_DUE_DATE_ListResponse`).

> Due date falls every N days.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_calendar_strategy_id` | integer (schema `ProgramCalendarStrategyId`) | no | Program calendar strategy ID | format: "int64"; example: 67854322 |
| `program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 1122 |
| `created_at` | string (schema `CreatedAt`) | no | Datetime program calendar strategy was created. Format = YYYY-MM-DDTHH:MM:SS:MM. | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime program calendar strategy was updated. Format = YYYY-MM-DDTHH:MM:SS:MM | format: "date-time"; example: "2024-09-12T16:46:16.43663522" |
| `strategy` | string | no | Program calendar strategy | enum: ["DAILY_DUE_DATE"] |
| `configuration` | object | no |  |  |
| `configuration.every_x_days` | integer (schema `EveryXDays`) | no | Interval in days between cycles. Must be between 1 and 365. Defaults to 1. | default: 1; format: "int32"; minimum: 1; maximum: 365; example: 7 |
| `configuration.days_between_cycle_closing_and_due_date` | integer (schema `DaysBetweenCycleClosingAndDueDate`) | no | Number of days between cycle closing and due date | format: "int32"; example: 5 |
| `active` | boolean (schema `Active`) | no | Is the program calendar strategy active? | default: true; example: true |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code | example: "EX0001" |
| `message` | string | no | Error message | example: "Internal error" |

<!-- schema: #/components/schemas/NthSpecificWeekday -->
### Schema `NthSpecificWeekday`

Pointer: `#/components/schemas/NthSpecificWeekday`. Type: object (schema `NthSpecificWeekday`).

> Nth specific weekday of the month (e.g. 3rd Friday). Mutually exclusive with fixed day fields.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `day_of_week` | string (schema `DayOfWeek`) | yes | Day of the week. | enum: ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]; example: "FRIDAY" |
| `week_of_month` | integer (schema `WeekOfMonth`) | yes | Week of the month. 1 = first, 2 = second, 3 = third, 4 = fourth, 5 = last. | format: "int32"; minimum: 1; maximum: 5; example: 3 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Calendar_management.yaml` | tag `Program calendar strategies`: GET /v1/programs/{programId}/calendar-strategies, POST /v1/programs/{programId}/calendar-strategies, GET /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId}, PATCH /v1/programs/{programId}/calendar-strategies/{programCalendarStrategyId} | https://github.com/PismoDevEx/pismo-api-specs | `63fcebe8bc52b750…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-calendar-management-strategies` — Calendar management strategies (cycle closing and due dates)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-EVT-catalogue-balance` — Event catalogue: balance
