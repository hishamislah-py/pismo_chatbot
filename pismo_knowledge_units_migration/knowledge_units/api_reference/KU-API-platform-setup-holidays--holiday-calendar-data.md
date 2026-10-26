---
ku_id: KU-API-platform-setup-holidays--holiday-calendar-data
title: 'API reference: Platform setup - Holidays — Holiday calendar data'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Holidays.yaml
  sha256: e7090515c96c54af9372c8860cc808a9c7bc3a33900bcc060fa294a7a5375882
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
- list-holiday-calendars
- get-holiday-calendar
- get-holiday-new
- post-search-business-day
- get-non-business-days
- get-holiday-calendar-by-external-id
related_kus:
- KU-ERR-codes-ehld
specification_version: v1.0
---

# API reference: Platform setup - Holidays — Holiday calendar data

**KU ID:** `KU-API-platform-setup-holidays--holiday-calendar-data` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Holiday calendar data` in `api-specs/Platform_setup_-_Holidays.yaml` (“Platform setup - Holidays”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/holiday-calendar` | `list-holiday-calendars` | List holiday calendars | no |
| `GET /v1/holiday-calendar/{holiday_calendar_id}` | `get-holiday-calendar` | Get holiday calendar | no |
| `GET /v1/holiday-calendar/{holiday_calendar_id}/holiday` | `get-holiday-new` | List holidays | no |
| `POST /v1/holiday-calendar/{holiday_calendar_id}/business-day` | `post-search-business-day` | Get business day | no |
| `GET /v1/holiday-calendar/{holiday_calendar_id}/non-business-days` | `get-non-business-days` | Get non-business days | no |
| `GET /v1/holiday-calendar/external-id/{external_id}` | `get-holiday-calendar-by-external-id` | Get calendar by external ID | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must pass an [account-specific token](https://developers.pismo.io/pismo-docs/docs/account-specific-access-tokens).<br>

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/v1/holiday-calendar operationId=list-holiday-calendars -->
### `GET /v1/holiday-calendar` — List holiday calendars

- **operationId:** `list-holiday-calendars`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar data`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> List holiday calendars for an Organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID |  |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `holiday_calendar_id` | query | no | integer | Holiday calendar ID filter |  |
| `name` | query | no | string | Holiday calendar name filter | maxLength: 80; example: "Independance Day" |
| `type` | query | no | string | Holiday calendar type filter |  |
| `external_id` | query | no | string | Client-created calendar holiday ID | maxLength: 36 |
| `parent_id` | query | no | integer | Holiday calendar parent ID filter | format: "int32"; minimum: 1; example: 5 |
| `sort_by` | query | no | string | Sort field - `name` or `type`. Default is `name`. | enum: ["name", "type"]; default: "name"; example: "name" |
| `sort_order` | query | no | string | Sort order - `asc` or `desc`. Default is `asc` | enum: ["asc", "desc"]; default: "asc" |
| `relation` | query | no | string | Calendar relationship type. Default is all Organization calendars. Either `external_id` or `holiday_calendar_id` is **REQUIRED** if this field is passed. | enum: ["parents", "children"] |
| `page` | query | no | integer | Page number.  Default = `1`. | format: "int32"; minimum: 1; example: 5 |
| `perPage` | query | no | integer | Items per page. Default =  `10`. Maximum = `100`. | format: "int32"; minimum: 1; maximum: 100; example: 30 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.ListHolidayCalendarResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current result page | example: 1 |
| `pages` | integer (schema `Pages`) | no | Total number of result pages. | example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum results per page | example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of result items | example: 11 |
| `items` | array of object (schema `presenter.GetHolidayCalendarResponse`) | no |  |  |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponseMissingHeader`:

```json
{
  "code": "EHLD0016",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-id-params` — from `#/components/examples/BadRequestResponseInvalidParams`:

```json
{
  "code": "400",
  "message": "Invalid parameter value: {parameter name}"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EHLD0001",
  "message": "Something went wrong - please try again"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EHLD0016` | Missing x-tenant header |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/v1/holiday-calendar/{holiday_calendar_id} operationId=get-holiday-calendar -->
### `GET /v1/holiday-calendar/{holiday_calendar_id}` — Get holiday calendar

- **operationId:** `get-holiday-calendar`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar data`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get a holiday calendar

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_calendar_id` | path | yes | string | Holiday calendar ID | example: "8675309" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.GetHolidayCalendarResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string (schema `ExternalId`) | no | Client-created external ID | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `holiday_calendar_id` | integer (schema `HolidayCalendarID`) | no | Holiday calendar ID | example: 8675309 |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `name` | string (schema `HolidayCalendarName`) | no | Holiday calendar name. Must be unique per organization. | minLength: 1; maxLength: 80; example: "Brazil holiday calendar" |
| `parent_id` | integer (schema `ParentId`) | no | Calendar parent ID.<br><br>Holiday calendars can have parent-child relationships, creating a hierarchy. Child calendars inherit holidays from their parent calendars.<br><br>Common use case: Country → State → City hierarchy<br><br>Example:<br> - Brazil (parent)<br>    - São Paulo (child of Brazil)<br>      - Campinas (child of São Paulo)<br><br>When you query holidays for Campinas, you automatically get:<br>  - Campinas city holidays<br>  - São Paulo state holidays<br>  - Brazil national holidays<br><br>You can reference the parent calendar using either:<br>  - `parent_id`: The internal parent calendar ID<br>  - `parent_external_id`: The parent calendar  `external_id`<br> | minimum: 1; example: 8675309 |
| `type` | string (schema `HolidayType`) | no | Type, free-form field. For example, `Country` or `Region`. | minLength: 1; maxLength: 15; example: "Country" |
| `working_days` | array of integer (schema `HolidayWorkingDays`) | no | Working days array<br><br>`1` = Monday, `6` = Saturday. Default = `[1, 2, 3, 4, 5]`.<br> | example: [1, 2, 3, 4, 5, 6]; items.enum: [1, 2, 3, 4, 5, 6] |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponseMissingHeader`:

```json
{
  "code": "EHLD0016",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-id-params` — from `#/components/examples/BadRequestResponseInvalidParams`:

```json
{
  "code": "400",
  "message": "Invalid parameter value: {parameter name}"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EHLD0001",
  "message": "Something went wrong - please try again"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EHLD0016` | Missing x-tenant header |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/v1/holiday-calendar/{holiday_calendar_id}/holiday operationId=get-holiday-new -->
### `GET /v1/holiday-calendar/{holiday_calendar_id}/holiday` — List holidays

- **operationId:** `get-holiday-new`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar data`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> List calendar holidays

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_calendar_id` | path | yes | string | Holiday calendar ID | example: "8675309" |
| `name` | query | no | string | Holiday calendar name filter | maxLength: 80; example: "Independance Day" |
| `beginDate` | query | no | string | Get results on or after this date. <br><br>This field indicates what part of the year to start searching for holidays, not when the holiday was created at Pismo.<br><br>Format = yyyy-mm-dd. Must be less than or equal to `endDate`.<br> | example: "2025-12-24" |
| `endDate` | query | no | string | Get holidays on or before this date. <br><br>This field indicates what part of the year to end searching for holidays, not when the holiday was created at Pismo.<br><br>Format: yyyy-mm-dd. Must be greater than or equal to `beginDate`."<br> | example: "2025-11-02" |
| `page` | query | no | integer | Page number.  Default = `1`. | format: "int32"; minimum: 1; example: 5 |
| `perPage` | query | no | integer | Items per page. Default =  `10`. Maximum = `100`. | format: "int32"; minimum: 1; maximum: 100; example: 30 |
| `order` | query | no | string | Sort order: `ASC` (ascending) or `DESC` (descending). Default = `ASC`.<br> | enum: ["ASC", "DESC"]; example: "ASC" |
| `orderBy` | query | no | string | Sort by `ID` or `NAME`. Default = `ID`. | enum: ["ID", "NAME"]; example: "ID" |
| `include_parent_holidays` | query | no | boolean | Should holidays from parent calendars be returned? Default is `false` | default: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.ListHolidayResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current result page | example: 1 |
| `pages` | integer (schema `Pages`) | no | Total number of result pages. | example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum results per page | example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of result items | example: 11 |
| `items` | array of object (schema `presenter.GetHolidayResponse`) | no |  |  |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponseMissingHeader`:

```json
{
  "code": "EHLD0016",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-id-params` — from `#/components/examples/BadRequestResponseInvalidParams`:

```json
{
  "code": "400",
  "message": "Invalid parameter value: {parameter name}"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EHLD0001",
  "message": "Something went wrong - please try again"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EHLD0016` | Missing x-tenant header |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=POST path=/v1/holiday-calendar/{holiday_calendar_id}/business-day operationId=post-search-business-day -->
### `POST /v1/holiday-calendar/{holiday_calendar_id}/business-day` — Get business day

- **operationId:** `post-search-business-day`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar data`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Searches for business day information for a specific date within a holiday calendar.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_calendar_id` | path | yes | string | Holiday calendar ID | example: "8675309" |

#### Request body

Required: no

> Business day search request body

**Content type `application/json`** — schema: object (schema `presenter.HolidayCalendarSearchBusinessDayRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_date` | string (schema `CurrentDate`) | yes | Current date. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.HolidayCalendarSearchBusinessDayResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_date` | string (schema `CurrentDate`) | no | Current date. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `holiday_calendar_id` | integer (schema `HolidayCalendarID`) | no | Holiday calendar ID | example: 8675309 |
| `holiday_calendar_metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `holiday_metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `is_holiday` | boolean (schema `IsHoliday`) | no | Is this a holiday? | example: true |
| `is_weekend` | boolean (schema `IsWeekend`) | no | Is this a weekend day? | example: true |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `next_business_date` | string (schema `NextBusinessDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `prior_business_date` | string (schema `PriorBusinessDate`) | no | Business day prior to holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponseMissingHeader`:

```json
{
  "code": "EHLD0016",
  "message": "Missing x-tenant header"
}
```

400 Example `missing-invalid-holiday-calendar-id` — from `#/components/examples/BadRequestResponseMissingRequiredFields`:

```json
{
  "code": "EHLD0050",
  "message": "Missing required fields"
}
```

400 Example `invalid-date-format` — from `#/components/examples/BadRequestResponseHolidayWrongFormat`:

```json
{
  "code": "EHLD0028",
  "message": "Holiday date with the wrong format"
}
```

400 Example `missing-current-date` — from `#/components/examples/BadRequestResponseMissingRequiredFields`:

```json
{
  "code": "EHLD0050",
  "message": "Missing required fields"
}
```

##### Response 404

404 Example `response-missing-tenant` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target name} not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EHLD0001",
  "message": "Something went wrong - please try again"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EHLD0016` | Missing x-tenant header |
| 400 | `EHLD0050` | Missing required fields |
| 400 | `EHLD0028` | Holiday date with the wrong format |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/v1/holiday-calendar/{holiday_calendar_id}/non-business-days operationId=get-non-business-days -->
### `GET /v1/holiday-calendar/{holiday_calendar_id}/non-business-days` — Get non-business days

- **operationId:** `get-non-business-days`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar data`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get non-business days (weekends and holidays) for a specific holiday calendar within a date range. Non-business days include weekends based on the holiday calendar's working days configuration and holidays associated with the group.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_calendar_id` | path | yes | string | Holiday calendar ID | example: "8675309" |
| `beginDate` | query | no | string | Get results on or after this date. <br><br>This field indicates what part of the year to start searching for holidays, not when the holiday was created at Pismo.<br><br>Format = yyyy-mm-dd. Must be less than or equal to `endDate`.<br> | example: "2025-12-24" |
| `endDate` | query | no | string | Get holidays on or before this date. <br><br>This field indicates what part of the year to end searching for holidays, not when the holiday was created at Pismo.<br><br>Format: yyyy-mm-dd. Must be greater than or equal to `beginDate`."<br> | example: "2025-11-02" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.HolidayCalendarNonBusinessDaysResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dates` | array of object (schema `presenter.NonBusinessDay`) | no |  |  |
| `holiday_calendar_metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponseMissingHeader`:

```json
{
  "code": "EHLD0016",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-id-params` — from `#/components/examples/BadRequestResponseInvalidParams`:

```json
{
  "code": "400",
  "message": "Invalid parameter value: {parameter name}"
}
```

##### Response 404

404 Example `response-missing-tenant` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target name} not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EHLD0001",
  "message": "Something went wrong - please try again"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EHLD0016` | Missing x-tenant header |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/v1/holiday-calendar/external-id/{external_id} operationId=get-holiday-calendar-by-external-id -->
### `GET /v1/holiday-calendar/external-id/{external_id}` — Get calendar by external ID

- **operationId:** `get-holiday-calendar-by-external-id`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar data`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Get a holiday calendar given its external ID in path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `external_id` | path | yes | string | Client-created calendar holiday ID | maxLength: 36 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.GetHolidayCalendarResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string (schema `ExternalId`) | no | Client-created external ID | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `holiday_calendar_id` | integer (schema `HolidayCalendarID`) | no | Holiday calendar ID | example: 8675309 |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `name` | string (schema `HolidayCalendarName`) | no | Holiday calendar name. Must be unique per organization. | minLength: 1; maxLength: 80; example: "Brazil holiday calendar" |
| `parent_id` | integer (schema `ParentId`) | no | Calendar parent ID.<br><br>Holiday calendars can have parent-child relationships, creating a hierarchy. Child calendars inherit holidays from their parent calendars.<br><br>Common use case: Country → State → City hierarchy<br><br>Example:<br> - Brazil (parent)<br>    - São Paulo (child of Brazil)<br>      - Campinas (child of São Paulo)<br><br>When you query holidays for Campinas, you automatically get:<br>  - Campinas city holidays<br>  - São Paulo state holidays<br>  - Brazil national holidays<br><br>You can reference the parent calendar using either:<br>  - `parent_id`: The internal parent calendar ID<br>  - `parent_external_id`: The parent calendar  `external_id`<br> | minimum: 1; example: 8675309 |
| `type` | string (schema `HolidayType`) | no | Type, free-form field. For example, `Country` or `Region`. | minLength: 1; maxLength: 15; example: "Country" |
| `working_days` | array of integer (schema `HolidayWorkingDays`) | no | Working days array<br><br>`1` = Monday, `6` = Saturday. Default = `[1, 2, 3, 4, 5]`.<br> | example: [1, 2, 3, 4, 5, 6]; items.enum: [1, 2, 3, 4, 5, 6] |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponseMissingHeader`:

```json
{
  "code": "EHLD0016",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-id-params` — from `#/components/examples/BadRequestResponseInvalidParams`:

```json
{
  "code": "400",
  "message": "Invalid parameter value: {parameter name}"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EHLD0001",
  "message": "Something went wrong - please try again"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EHLD0016` | Missing x-tenant header |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/presenter.GetHolidayCalendarResponse -->
### Schema `presenter.GetHolidayCalendarResponse`

Pointer: `#/components/schemas/presenter.GetHolidayCalendarResponse`. Type: object (schema `presenter.GetHolidayCalendarResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string (schema `ExternalId`) | no | Client-created external ID | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `holiday_calendar_id` | integer (schema `HolidayCalendarID`) | no | Holiday calendar ID | example: 8675309 |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `name` | string (schema `HolidayCalendarName`) | no | Holiday calendar name. Must be unique per organization. | minLength: 1; maxLength: 80; example: "Brazil holiday calendar" |
| `parent_id` | integer (schema `ParentId`) | no | Calendar parent ID.<br><br>Holiday calendars can have parent-child relationships, creating a hierarchy. Child calendars inherit holidays from their parent calendars.<br><br>Common use case: Country → State → City hierarchy<br><br>Example:<br> - Brazil (parent)<br>    - São Paulo (child of Brazil)<br>      - Campinas (child of São Paulo)<br><br>When you query holidays for Campinas, you automatically get:<br>  - Campinas city holidays<br>  - São Paulo state holidays<br>  - Brazil national holidays<br><br>You can reference the parent calendar using either:<br>  - `parent_id`: The internal parent calendar ID<br>  - `parent_external_id`: The parent calendar  `external_id`<br> | minimum: 1; example: 8675309 |
| `type` | string (schema `HolidayType`) | no | Type, free-form field. For example, `Country` or `Region`. | minLength: 1; maxLength: 15; example: "Country" |
| `working_days` | array of integer (schema `HolidayWorkingDays`) | no | Working days array<br><br>`1` = Monday, `6` = Saturday. Default = `[1, 2, 3, 4, 5]`.<br> | example: [1, 2, 3, 4, 5, 6]; items.enum: [1, 2, 3, 4, 5, 6] |

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

> Error

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

<!-- schema: #/components/schemas/presenter.GetHolidayResponse -->
### Schema `presenter.GetHolidayResponse`

Pointer: `#/components/schemas/presenter.GetHolidayResponse`. Type: object (schema `presenter.GetHolidayResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `created_at` | string (schema `CreatedAt`) | no | Date and time the holiday was created. Format = yyyy-mm-ddTHH:mm:ss. | format: "datetime"; example: "2024-04-30T17:24:03" |
| `deleted_at` | string (schema `DeletedAt`) | no | Date and time the holiday was deleted. Format = yyyy-mm-ddTHH:mm:ss. | format: "datetime"; example: "2024-04-30T17:24:03" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `holiday_calendar` | object (schema `HolidayCalendar`) | no |  |  |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `holiday_id` | integer (schema `HolidayID`) | no | Holiday ID | example: 8675309 |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `updated_at` | string (schema `UpdatedAt`) | no | Date and time the holiday was updated. Format = yyyy-mm-ddTHH:mm:ss. | format: "datetime"; example: "2024-04-30T17:24:03" |

<!-- schema: #/components/schemas/presenter.NonBusinessDay -->
### Schema `presenter.NonBusinessDay`

Pointer: `#/components/schemas/presenter.NonBusinessDay`. Type: object (schema `presenter.NonBusinessDay`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date` | string | no | Non-business day date. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-20" |
| `is_holiday` | boolean (schema `IsHoliday`) | no | Is this a holiday? | example: true |
| `is_weekend` | boolean (schema `IsWeekend`) | no | Is this a weekend day? | example: true |
| `holiday_metadata` | object (map of object) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used for transaction authorization.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

<!-- schema: #/components/schemas/HolidayCalendar -->
### Schema `HolidayCalendar`

Pointer: `#/components/schemas/HolidayCalendar`. Type: object (schema `HolidayCalendar`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `HolidayCalendarID`) | no | Holiday calendar ID | example: 8675309 |
| `name` | string (schema `HolidayCalendarName`) | no | Holiday calendar name. Must be unique per organization. | minLength: 1; maxLength: 80; example: "Brazil holiday calendar" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Holidays.yaml` | tag `Holiday calendar data`: GET /v1/holiday-calendar, GET /v1/holiday-calendar/{holiday_calendar_id}, GET /v1/holiday-calendar/{holiday_calendar_id}/holiday, POST /v1/holiday-calendar/{holiday_calendar_id}/business-day, GET /v1/holiday-calendar/{holiday_calendar_id}/non-business-days, GET /v1/holiday-calendar/external-id/{external_id} | https://github.com/PismoDevEx/pismo-api-specs | `e7090515c96c54af…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-ehld` — Error codes: EHLD
