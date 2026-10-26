---
ku_id: KU-API-platform-setup-holidays--holiday-calendar
title: 'API reference: Platform setup - Holidays — Holiday calendar'
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
- post-create-holiday-calendar
- delete-holiday-calendar
- update-holiday-calendar
- post-add-holiday-to-calendar
- delete-holiday
- update-holiday
related_kus:
- KU-BANK-divisions-and-hierarchies
- KU-ERR-codes-ehld
specification_version: v1.0
---

# API reference: Platform setup - Holidays — Holiday calendar

**KU ID:** `KU-API-platform-setup-holidays--holiday-calendar` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Holiday calendar` in `api-specs/Platform_setup_-_Holidays.yaml` (“Platform setup - Holidays”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/holiday-calendar` | `post-create-holiday-calendar` | Create holiday calendar | no |
| `DELETE /v1/holiday-calendar/{holiday_calendar_id}` | `delete-holiday-calendar` | Delete holiday calendar | no |
| `PATCH /v1/holiday-calendar/{holiday_calendar_id}` | `update-holiday-calendar` | Update holiday calendar | no |
| `POST /v1/holiday-calendar/holiday` | `post-add-holiday-to-calendar` | Add holiday | no |
| `DELETE /v1/holiday-calendar/{holiday_calendar_id}/holiday/{holiday_id}` | `delete-holiday` | Delete holiday | no |
| `PATCH /v1/holiday-calendar/{holiday_calendar_id}/holiday/{holiday_id}` | `update-holiday` | Update holiday | no |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must pass an [account-specific token](https://developers.pismo.io/pismo-docs/docs/account-specific-access-tokens).<br>

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=POST path=/v1/holiday-calendar operationId=post-create-holiday-calendar -->
### `POST /v1/holiday-calendar` — Create holiday calendar

- **operationId:** `post-create-holiday-calendar`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Creates a new holiday calendar with associated holidays. 
>
> This endpoint does not generate an event.

#### Request body

Required: no

> Create holiday calendar request body

**Content type `application/json`** — schema: object (schema `presenter.CreateHolidayCalendarRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `HolidayCalendarName`) | yes | Holiday calendar name. Must be unique per organization. | minLength: 1; maxLength: 80; example: "Brazil holiday calendar" |
| `type` | string (schema `HolidayType`) | yes | Type, free-form field. For example, `Country` or `Region`. | minLength: 1; maxLength: 15; example: "Country" |
| `external_id` | string (schema `ExternalId`) | no | Client-created external ID | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `holidays` | array of object (schema `presenter.CreateNewHolidayRequest2`) | no | Holidays array |  |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `parent_external_id` | string (schema `ExternalIdParent`) | no | Client-created external ID for parent calendar. <br>Refer to `parent_id` parameter for more information.<br> | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `parent_id` | integer (schema `ParentId`) | no | Calendar parent ID.<br><br>Holiday calendars can have parent-child relationships, creating a hierarchy. Child calendars inherit holidays from their parent calendars.<br><br>Common use case: Country → State → City hierarchy<br><br>Example:<br> - Brazil (parent)<br>    - São Paulo (child of Brazil)<br>      - Campinas (child of São Paulo)<br><br>When you query holidays for Campinas, you automatically get:<br>  - Campinas city holidays<br>  - São Paulo state holidays<br>  - Brazil national holidays<br><br>You can reference the parent calendar using either:<br>  - `parent_id`: The internal parent calendar ID<br>  - `parent_external_id`: The parent calendar  `external_id`<br> | minimum: 1; example: 8675309 |
| `working_days` | array of integer (schema `HolidayWorkingDays`) | no | Working days array<br><br>`1` = Monday, `6` = Saturday. Default = `[1, 2, 3, 4, 5]`.<br> | example: [1, 2, 3, 4, 5, 6]; items.enum: [1, 2, 3, 4, 5, 6] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `presenter.CreateHolidayCalendarResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 409 | Conflict | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string (schema `ExternalId`) | no | Client-created external ID | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `holiday_calendar_id` | integer (schema `HolidayCalendarID`) | no | Holiday calendar ID | example: 8675309 |
| `holidays` | array of object (schema `presenter.CreateNewHolidayResponse`) | no |  |  |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `parent_external_id` | string (schema `ExternalIdParent`) | no | Client-created external ID for parent calendar. <br>Refer to `parent_id` parameter for more information.<br> | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
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

400 Example `missing-required-fields` — from `#/components/examples/BadRequestResponseMissingRequiredFields`:

```json
{
  "code": "EHLD0050",
  "message": "Missing required fields"
}
```

400 Example `holiday-date-wrong-format` — from `#/components/examples/BadRequestResponseHolidayWrongFormat`:

```json
{
  "code": "EHLD0028",
  "message": "Holiday date with the wrong format"
}
```

400 Example `working-date-wrong-format` — from `#/components/examples/BadRequestResponseWorkingDateWrongFormat`:

```json
{
  "code": "EHLD0030",
  "message": "Working date with the wrong format"
}
```

400 Example `invalid-metadata` — from `#/components/examples/BadRequestResponseInvalidMetadata`:

```json
{
  "code": "EHLD0049",
  "message": "Invalid metadata"
}
```

##### Response 404

404 Example `holiday-calendar-not-found` — from `#/components/examples/BadRequestResponseHolidayCalendarNotFound`:

```json
{
  "code": "EHLD0052",
  "message": "Holiday calendar not found"
}
```

##### Response 409

409 Example `holiday-calendar-already-exists` — from `#/components/examples/BadRequestResponseAlreadyExists`:

```json
{
  "code": "EHLD0027",
  "message": "Holiday calendar already exists"
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
| 400 | `EHLD0030` | Working date with the wrong format |
| 400 | `EHLD0049` | Invalid metadata |
| 404 | `EHLD0052` | Holiday calendar not found |
| 409 | `EHLD0027` | Holiday calendar already exists |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-divisions-and-hierarchies`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=DELETE path=/v1/holiday-calendar/{holiday_calendar_id} operationId=delete-holiday-calendar -->
### `DELETE /v1/holiday-calendar/{holiday_calendar_id}` — Delete holiday calendar

- **operationId:** `delete-holiday-calendar`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Delete a holiday calendar

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_calendar_id` | path | yes | string | Holiday calendar ID | example: "8675309" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=PATCH path=/v1/holiday-calendar/{holiday_calendar_id} operationId=update-holiday-calendar -->
### `PATCH /v1/holiday-calendar/{holiday_calendar_id}` — Update holiday calendar

- **operationId:** `update-holiday-calendar`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Update a holiday calendar. Fields not passed are not updated.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_calendar_id` | path | yes | string | Holiday calendar ID | example: "8675309" |

#### Request body

Required: no

> Business day search request body

**Content type `application/json`** — schema: object (schema `presenter.UpdateHolidayCalendarRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `Type`) | no | Holiday calendar type | example: "Country" |
| `parent_id` | integer (schema `ParentId`) | no | Calendar parent ID.<br><br>Holiday calendars can have parent-child relationships, creating a hierarchy. Child calendars inherit holidays from their parent calendars.<br><br>Common use case: Country → State → City hierarchy<br><br>Example:<br> - Brazil (parent)<br>    - São Paulo (child of Brazil)<br>      - Campinas (child of São Paulo)<br><br>When you query holidays for Campinas, you automatically get:<br>  - Campinas city holidays<br>  - São Paulo state holidays<br>  - Brazil national holidays<br><br>You can reference the parent calendar using either:<br>  - `parent_id`: The internal parent calendar ID<br>  - `parent_external_id`: The parent calendar  `external_id`<br> | minimum: 1; example: 8675309 |
| `external_id` | string (schema `ExternalId`) | no | Client-created external ID | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `working_days` | array of integer (schema `HolidayWorkingDays`) | no | Working days array<br><br>`1` = Monday, `6` = Saturday. Default = `[1, 2, 3, 4, 5]`.<br> | example: [1, 2, 3, 4, 5, 6]; items.enum: [1, 2, 3, 4, 5, 6] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=POST path=/v1/holiday-calendar/holiday operationId=post-add-holiday-to-calendar -->
### `POST /v1/holiday-calendar/holiday` — Add holiday

- **operationId:** `post-add-holiday-to-calendar`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Add a new holiday to an existing holiday calendar. 
>
> This endpoint generates a _______ event.

#### Request body

Required: no

> Holiday creation request data

**Content type `application/json`** — schema: object (schema `presenter.AddHolidayToCalendarRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `holiday_date` | string (schema `HolidayDate`) | yes | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `name` | string (schema `HolidayName`) | yes | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `external_id` | string (schema `ExternalId2`) | no | Client-created external ID. <br><br>Either this field or `holiday_calendar_id` is **REQUIRED**. Pass one or the other but not both.<br> | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `holiday_calendar_id` | integer (schema `HolidayCalendarID2`) | no | Holiday calendar ID. <br><br>Either this field or `external_id` is **REQUIRED**. Pass one or the other but not both.<br> | example: 8675309 |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `presenter.AddHolidayToCalendarResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 409 | Conflict | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `created_at` | string (schema `CreatedAt`) | no | Date and time the holiday was created. Format = yyyy-mm-ddTHH:mm:ss. | format: "datetime"; example: "2024-04-30T17:24:03" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `external_id` | string (schema `ExternalId`) | no | Client-created external ID | minLength: 1; maxLength: 36; example: "f89urqljnahosluiefku" |
| `holiday_calendar_id` | integer (schema `HolidayCalendarID`) | no | Holiday calendar ID | example: 8675309 |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `holiday_id` | integer (schema `HolidayID`) | no | Holiday ID | example: 8675309 |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `working_date` | string (schema `WorkingDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponseMissingHeader`:

```json
{
  "code": "EHLD0016",
  "message": "Missing x-tenant header"
}
```

400 Example `missing-required-fields` — from `#/components/examples/BadRequestResponseMissingRequiredFields`:

```json
{
  "code": "EHLD0050",
  "message": "Missing required fields"
}
```

400 Example `holiday-date-wrong-format` — from `#/components/examples/BadRequestResponseHolidayWrongFormat`:

```json
{
  "code": "EHLD0028",
  "message": "Holiday date with the wrong format"
}
```

400 Example `working-date-wrong-format` — from `#/components/examples/BadRequestResponseHolidayWrongFormat`:

```json
{
  "code": "EHLD0028",
  "message": "Holiday date with the wrong format"
}
```

400 Example `working-date-before-holiday-date` — from `#/components/examples/BadRequestResponseWorkingDateBeforeHolidayDate`:

```json
{
  "code": "EHLD0032",
  "message": "Working date before holiday date"
}
```

400 Example `invalid-metadata` — from `#/components/examples/BadRequestResponseInvalidMetadata`:

```json
{
  "code": "EHLD0049",
  "message": "Invalid metadata"
}
```

##### Response 404

404 Example `holiday-calendar-not-found` — from `#/components/examples/BadRequestResponseHolidayCalendarNotFound`:

```json
{
  "code": "EHLD0052",
  "message": "Holiday calendar not found"
}
```

404 Example `administrative-division-not-found` — from `#/components/examples/BadRequestResponseAdminDivisionNotFound`:

```json
{
  "code": "EHLD0026",
  "message": "Administrative division not found"
}
```

##### Response 409

409 Example `holiday-exists-in-group` — from `#/components/examples/BadRequestResponseAlreadyExists`:

```json
{
  "code": "EHLD0027",
  "message": "Holiday calendar already exists"
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
| 400 | `EHLD0032` | Working date before holiday date |
| 400 | `EHLD0049` | Invalid metadata |
| 404 | `EHLD0052` | Holiday calendar not found |
| 404 | `EHLD0026` | Administrative division not found |
| 409 | `EHLD0027` | Holiday calendar already exists |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=DELETE path=/v1/holiday-calendar/{holiday_calendar_id}/holiday/{holiday_id} operationId=delete-holiday -->
### `DELETE /v1/holiday-calendar/{holiday_calendar_id}/holiday/{holiday_id}` — Delete holiday

- **operationId:** `delete-holiday`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Delete a calendar holiday

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_calendar_id` | path | yes | string | Holiday calendar ID | example: "8675309" |
| `holiday_id` | path | yes | string | Pismo-assigned holiday ID | example: "8675309" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=PATCH path=/v1/holiday-calendar/{holiday_calendar_id}/holiday/{holiday_id} operationId=update-holiday -->
### `PATCH /v1/holiday-calendar/{holiday_calendar_id}/holiday/{holiday_id}` — Update holiday

- **operationId:** `update-holiday`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holiday calendar`
- **Deprecated in specification:** no
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> Update a holiday in a holiday calendar.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_calendar_id` | path | yes | string | Holiday calendar ID | example: "8675309" |
| `holiday_id` | path | yes | string | Pismo-assigned holiday ID | example: "8675309" |

#### Request body

Required: no

> Holiday update data

**Content type `application/json`** — schema: object (schema `presenter.UpdateHolidayInGroupRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/presenter.CreateNewHolidayRequest2 -->
### Schema `presenter.CreateNewHolidayRequest2`

Pointer: `#/components/schemas/presenter.CreateNewHolidayRequest2`. Type: object (schema `presenter.CreateNewHolidayRequest2`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `HolidayName`) | yes | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `holiday_date` | string (schema `HolidayDate`) | yes | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

<!-- schema: #/components/schemas/presenter.CreateNewHolidayResponse -->
### Schema `presenter.CreateNewHolidayResponse`

Pointer: `#/components/schemas/presenter.CreateNewHolidayResponse`. Type: object (schema `presenter.CreateNewHolidayResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `holiday_id` | integer (schema `HolidayID`) | no | Holiday ID | example: 8675309 |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `working_date` | string (schema `WorkingDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

> Error

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Holidays.yaml` | tag `Holiday calendar`: POST /v1/holiday-calendar, DELETE /v1/holiday-calendar/{holiday_calendar_id}, PATCH /v1/holiday-calendar/{holiday_calendar_id}, POST /v1/holiday-calendar/holiday, DELETE /v1/holiday-calendar/{holiday_calendar_id}/holiday/{holiday_id}, PATCH /v1/holiday-calendar/{holiday_calendar_id}/holiday/{holiday_id} | https://github.com/PismoDevEx/pismo-api-specs | `e7090515c96c54af…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-divisions-and-hierarchies` — Divisions and hierarchies
- `KU-ERR-codes-ehld` — Error codes: EHLD
