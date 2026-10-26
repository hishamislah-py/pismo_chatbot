---
ku_id: KU-API-platform-setup-holidays--holidays-deprecated
title: 'API reference: Platform setup - Holidays — Holidays (deprecated)'
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
- get-v1-holidays
- post-holiday
- validate-v1-holiday
- put-v1-holiday
- delete-v1-holiday
- v1-search-business-day
- v1-get-non-business-days
- get-v1-holidays-with-administrative-divisions-ancestors
related_kus:
- KU-CORE-platform-setup-holidays
- KU-CRED-calendar-management-strategies
- KU-CRED-holidays-in-credit-card-accounts
- KU-ERR-codes-ehld
specification_version: v1.0
---

# API reference: Platform setup - Holidays — Holidays (deprecated)

**KU ID:** `KU-API-platform-setup-holidays--holidays-deprecated` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 8 operation(s) tagged `Holidays (deprecated)` in `api-specs/Platform_setup_-_Holidays.yaml` (“Platform setup - Holidays”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> View and manage business and non-business days configurations.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /holidays-core/v1/holiday` | `get-v1-holidays` | List holidays (deprecated) | **yes** |
| `POST /holidays-core/v1/holiday` | `post-holiday` | Create holiday (deprecated) | **yes** |
| `POST /holidays-core/v1/holiday/validate` | `validate-v1-holiday` | Get holiday (deprecated) | **yes** |
| `PUT /holidays-core/v1/holiday/{holiday_id}` | `put-v1-holiday` | Update holiday name (deprecated) | **yes** |
| `DELETE /holidays-core/v1/holiday/{holiday_id}` | `delete-v1-holiday` | Delete holiday (deprecated) | **yes** |
| `POST /holidays-core/v1/search-business-day` | `v1-search-business-day` | Check if business day (deprecated) | **yes** |
| `GET /holidays-core/v1/non-business-days` | `v1-get-non-business-days` | List non-business days (deprecated) | **yes** |
| `GET /holidays-core/v1/holiday/administrative-division/{administrative_division_id}/ancestors` | `get-v1-holidays-with-administrative-divisions-ancestors` | List holidays with administrative division ancestors (deprecated) | **yes** |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must pass an [account-specific token](https://developers.pismo.io/pismo-docs/docs/account-specific-access-tokens).<br>

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/holidays-core/v1/holiday operationId=get-v1-holidays -->
### `GET /holidays-core/v1/holiday` — List holidays (deprecated)

- **operationId:** `get-v1-holidays`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the Call the [List holiday calendars](ref:list-holiday-calendars) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Return a paginated list of holidays registered for an organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | integer | Page number.  Default = `1`. | format: "int32"; minimum: 1; example: 5 |
| `perPage` | query | no | integer | Items per page. Default =  `10`. Maximum = `100`. | format: "int32"; minimum: 1; maximum: 100; example: 30 |
| `order` | query | no | string | Sort order: `ASC` (ascending) or `DESC` (descending). Default = `ASC`.<br> | enum: ["ASC", "DESC"]; example: "ASC" |
| `orderBy` | query | no | string | Sort by `ID` or `NAME`. Default = `ID`. | enum: ["ID", "NAME"]; example: "ID" |
| `administrativeDivisionId` | query | yes | integer | Administrative Division ID filter | format: "int32" |
| `name` | query | no | string | Holiday calendar name filter | maxLength: 80; example: "Independance Day" |
| `holidayDate` | query | no | string | Holiday date filter. Format = yyyy-mm-dd. | example: "2023-01-01" |
| `beginDate` | query | no | string | Get results on or after this date. <br><br>This field indicates what part of the year to start searching for holidays, not when the holiday was created at Pismo.<br><br>Format = yyyy-mm-dd. Must be less than or equal to `endDate`.<br> | example: "2025-12-24" |
| `endDate` | query | no | string | Get holidays on or before this date. <br><br>This field indicates what part of the year to end searching for holidays, not when the holiday was created at Pismo.<br><br>Format: yyyy-mm-dd. Must be greater than or equal to `beginDate`."<br> | example: "2025-11-02" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `pagination.Pagination`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current result page | example: 1 |
| `items` | array of object (schema `presenter.HolidayResponse`) | no |  |  |
| `pages` | integer (schema `Pages`) | no | Total number of result pages. | example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum results per page | example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of result items | example: 11 |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponseMissingHeader`:

```json
{
  "code": "EHLD0016",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-order-query` — from `#/components/examples/BadRequestResponseInvalidOrder`:

```json
{
  "code": "EHLD0041",
  "message": "Invalid 'order' query param with value 'ascaa'. Order must be asc or desc."
}
```

400 Example `invalid-perpage-query` — from `#/components/examples/BadRequestResponseInvalidPerPage`:

```json
{
  "code": "EHLD0039",
  "message": "Invalid 'perPage' query param with value '10A'. PerPage must be > 0."
}
```

400 Example `end-date-before-begin-date` — from `#/components/examples/BadRequestResponseEndDateBeforeBeginDate`:

```json
{
  "code": "EHLD0046",
  "message": "End date before Begin date"
}
```

400 Example `end-date-wrong-format` — from `#/components/examples/BadRequestResponseEndDateWrongFormat`:

```json
{
  "code": "EHLD0048",
  "message": "End date with the wrong format"
}
```

400 Example `begin-date-wrong-format` — from `#/components/examples/BadRequestResponseBeginDateWrongFormat`:

```json
{
  "code": "EHLD0047",
  "message": "Begin date with the wrong format"
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
| 400 | `EHLD0041` | Invalid 'order' query param with value 'ascaa'. Order must be asc or desc. |
| 400 | `EHLD0039` | Invalid 'perPage' query param with value '10A'. PerPage must be > 0. |
| 400 | `EHLD0046` | End date before Begin date |
| 400 | `EHLD0048` | End date with the wrong format |
| 400 | `EHLD0047` | Begin date with the wrong format |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-CORE-platform-setup-holidays`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=POST path=/holidays-core/v1/holiday operationId=post-holiday -->
### `POST /holidays-core/v1/holiday` — Create holiday (deprecated)

- **operationId:** `post-holiday`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the [Add holiday](ref:post-add-holiday-to-calendar) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Create a holiday&mdash;a day on which your company's offices are closed for normal business activity though online financial transactions and other business activity could still be occurring.
>
> For more information, refer to <a href="https://developers.pismo.io/pismo-docs/docs/platform-setup-holidays">Platform setup - Holidays and administrative divisions</a>.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.CreateHolidayRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `HolidayName`) | yes | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `holiday_date` | string (schema `HolidayDate`) | yes | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `working_date` | string (schema `NextBusinessDate`) | yes | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `administrative_division_id` | integer (schema `AdminDivIdV1Only`) | no | Administrative division ID. <br><br>When passed as a parameter, either this or `external_id` is **REQUIRED**.<br> | example: 100100 |
| `external_id` | string (schema `ExternalIdV1Only`) | no | Existing ID value from another process or application.<br><br>When passed as a parameter, either this or `administrative_division_id` is **REQUIRED**.<br> | example: "38400-000" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Holidays response | `application/json`: object (schema `presenter.CreateHolidayResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `HolidayID`) | no | Holiday ID | example: 8675309 |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `working_date` | string (schema `NextBusinessDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `administrative_division_id` | integer (schema `AdminDivIdV1Only`) | no | Administrative division ID. <br><br>When passed as a parameter, either this or `external_id` is **REQUIRED**.<br> | example: 100100 |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;500`, has examples `False`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-CORE-platform-setup-holidays`, `KU-CRED-holidays-in-credit-card-accounts`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=POST path=/holidays-core/v1/holiday/validate operationId=validate-v1-holiday -->
### `POST /holidays-core/v1/holiday/validate` — Get holiday (deprecated)

- **operationId:** `validate-v1-holiday`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the [Get business day](ref:post-search-business-day) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Get information for an administrative division's holiday.
>
>  **Note:** The response could contain outdated information until at least one minute after an update is made to an administrative division.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.ValidateHolidayRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date` | string (schema `HolidayDate`) | yes | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `division_id` | integer | yes | Division ID | example: 100 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.HolidayResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `administrative_division` | object (schema `presenter.AdministrativeDivisionResponse`) | no |  |  |
| `id` | integer (schema `HolidayID`) | no | Holiday ID | example: 8675309 |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `next_business_date` | string (schema `NextBusinessDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `created_at` | string (schema `CreatedAt`) | no | Date and time the holiday was created. Format = yyyy-mm-ddTHH:mm:ss. | format: "datetime"; example: "2024-04-30T17:24:03" |

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

404 Example `holiday-calendar-not-found` — from `#/components/examples/BadRequestResponseHolidayCalendarNotFound`:

```json
{
  "code": "EHLD0052",
  "message": "Holiday calendar not found"
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
| 404 | `EHLD0052` | Holiday calendar not found |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-CRED-calendar-management-strategies`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=PUT path=/holidays-core/v1/holiday/{holiday_id} operationId=put-v1-holiday -->
### `PUT /holidays-core/v1/holiday/{holiday_id}` — Update holiday name (deprecated)

- **operationId:** `put-v1-holiday`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the [Update holiday](ref:update-holiday) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Update a holiday's name.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_id` | path | yes | string | Pismo-assigned holiday ID | example: "8675309" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.UpdateHolidayRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `HolidayName`) | yes | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated holiday name | `application/json`: object (schema `presenter.UpdateHolidayResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `HolidayID`) | no | Holiday ID | example: 8675309 |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=DELETE path=/holidays-core/v1/holiday/{holiday_id} operationId=delete-v1-holiday -->
### `DELETE /holidays-core/v1/holiday/{holiday_id}` — Delete holiday (deprecated)

- **operationId:** `delete-v1-holiday`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the new [Delete holiday](ref:delete-holiday) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Delete a holiday.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_id` | path | yes | string | Pismo-assigned holiday ID | example: "8675309" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No content |  |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;404;500`, has examples `False`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=POST path=/holidays-core/v1/search-business-day operationId=v1-search-business-day -->
### `POST /holidays-core/v1/search-business-day` — Check if business day (deprecated)

- **operationId:** `v1-search-business-day`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the [Get business day](ref:post-search-business-day) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Check if a specific date is a business day for an administrative division.
>
> **Note:** The response could contain outdated information until at least one minute after an administrative division update.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.SearchBusinessDayRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_date` | string (schema `HolidayDate`) | yes | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `division_id` | integer | yes | Division ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.SearchBusinessDayResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `division_id` | integer | no | Division ID | example: 100 |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `current_date` | string (schema `CurrentDate`) | no | Current date. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `next_business_date` | string (schema `NextBusinessDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `prior_business_date` | string (schema `PriorBusinessDate`) | no | Business day prior to holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `is_holiday` | boolean (schema `IsHoliday`) | no | Is this a holiday? | example: true |
| `is_weekend` | boolean (schema `IsWeekend`) | no | Is this a weekend day? | example: true |
| `holiday_metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `division_metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

200 Example `response-v1-search-business-day` — from `#/components/examples/SearchBusinessDayResponse`:

```json
{
  "division_id": 1,
  "name": "New Year's Day",
  "description": "New Year's Day",
  "current_date": "2023-01-01",
  "next_business_date": "2023-01-02",
  "prior_business_date": "2022-12-31",
  "is_holiday": true,
  "is_weekend": false,
  "holiday_metadata": {
    "accrue_interest": true,
    "check_dormancy": true,
    "create_account": false,
    "defer_statement_due_date": true,
    "defer_transactions": true,
    "post_interest": false,
    "post_transactions": false,
    "run_cycle_closing": false
  },
  "division_metadata": {
    "accrue_interest": true,
    "check_dormancy": true,
    "create_account": false,
    "defer_statement_due_date": true,
    "defer_transactions": true,
    "post_interest": false,
    "post_transactions": false,
    "run_cycle_closing": false
  }
}
```

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/holidays-core/v1/non-business-days operationId=v1-get-non-business-days -->
### `GET /holidays-core/v1/non-business-days` — List non-business days (deprecated)

- **operationId:** `v1-get-non-business-days`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the [Get non-business days](ref:get-non-business-days) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Return a list of non-business days.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID |  |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> |  |
| `administrativeDivisionId` | query | yes | integer | Administrative Division ID filter | format: "int32" |
| `beginDate` | query | no | string | Get results on or after this date. <br><br>This field indicates what part of the year to start searching for holidays, not when the holiday was created at Pismo.<br><br>Format = yyyy-mm-dd. Must be less than or equal to `endDate`.<br> | example: "2025-12-24" |
| `endDate` | query | no | string | Get holidays on or before this date. <br><br>This field indicates what part of the year to end searching for holidays, not when the holiday was created at Pismo.<br><br>Format: yyyy-mm-dd. Must be greater than or equal to `beginDate`."<br> | example: "2025-11-02" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.NonBusinessDaysResponse`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dates` | array of object (schema `presenter.NonBusinessDay`) | no |  |  |
| `division_metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

200 Example `response-v1-non-business-days` — from `#/components/examples/NonBusinessDaysResponse`:

```json
{
  "division_metadata": {
    "accrue_interest": true,
    "check_dormancy": true,
    "create_account": false,
    "defer_statement_due_date": true,
    "defer_transactions": true,
    "post_interest": false,
    "post_transactions": false,
    "run_cycle_closing": false
  },
  "holiday_metadata": {
    "accrue_interest": true,
    "check_dormancy": true,
    "create_account": false,
    "defer_statement_due_date": true,
    "defer_transactions": true,
    "post_interest": false,
    "post_transactions": false,
    "run_cycle_closing": false
  },
  "dates": [
    {
      "date": "2024-11-02",
      "is_holiday": true,
      "is_weekend": true
    },
    {
      "date": "2024-11-03",
      "is_holiday": false,
      "is_weekend": true
    },
    {
      "date": "2024-11-09",
      "is_holiday": false,
      "is_weekend": true
    }
  ]
}
```

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

400 Example `invalid-date-format` — from `#/components/examples/BadRequestResponseHolidayWrongFormat`:

```json
{
  "code": "EHLD0028",
  "message": "Holiday date with the wrong format"
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
| 404 | `EHLD0052` | Holiday calendar not found |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/holidays-core/v1/holiday/administrative-division/{administrative_division_id}/ancestors operationId=get-v1-holidays-with-administrative-divisions-ancestors -->
### `GET /holidays-core/v1/holiday/administrative-division/{administrative_division_id}/ancestors` — List holidays with administrative division ancestors (deprecated)

- **operationId:** `get-v1-holidays-with-administrative-divisions-ancestors`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the [List holiday calendars](ref:list-holiday-calendars) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Return a paginated list of holidays registered for an administrative division, including those inherited from a parent division.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `administrative_division_id` | path | yes | integer | Administrative Division ID | format: "int32" |
| `page` | query | no | integer | Page number.  Default = `1`. | format: "int32"; minimum: 1; example: 5 |
| `perPage` | query | no | integer | Items per page. Default =  `10`. Maximum = `100`. | format: "int32"; minimum: 1; maximum: 100; example: 30 |
| `order` | query | no | string | Sort order: `ASC` (ascending) or `DESC` (descending). Default = `ASC`.<br> | enum: ["ASC", "DESC"]; example: "ASC" |
| `orderBy` | query | no | string | Sort by `ID` or `NAME`. Default = `ID`. | enum: ["ID", "NAME"]; example: "ID" |
| `beginDate` | query | no | string | Get results on or after this date. <br><br>This field indicates what part of the year to start searching for holidays, not when the holiday was created at Pismo.<br><br>Format = yyyy-mm-dd. Must be less than or equal to `endDate`.<br> | example: "2025-12-24" |
| `endDate` | query | no | string | Get holidays on or before this date. <br><br>This field indicates what part of the year to end searching for holidays, not when the holiday was created at Pismo.<br><br>Format: yyyy-mm-dd. Must be greater than or equal to `beginDate`."<br> | example: "2025-11-02" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `pagination.Pagination`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current result page | example: 1 |
| `items` | array of object (schema `presenter.HolidayResponse`) | no |  |  |
| `pages` | integer (schema `Pages`) | no | Total number of result pages. | example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum results per page | example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of result items | example: 11 |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `True`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/presenter.HolidayResponse -->
### Schema `presenter.HolidayResponse`

Pointer: `#/components/schemas/presenter.HolidayResponse`. Type: object (schema `presenter.HolidayResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `administrative_division` | object (schema `presenter.AdministrativeDivisionResponse`) | no |  |  |
| `id` | integer (schema `HolidayID`) | no | Holiday ID | example: 8675309 |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `next_business_date` | string (schema `NextBusinessDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `created_at` | string (schema `CreatedAt`) | no | Date and time the holiday was created. Format = yyyy-mm-ddTHH:mm:ss. | format: "datetime"; example: "2024-04-30T17:24:03" |

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

> Error

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

<!-- schema: #/components/schemas/presenter.AdministrativeDivisionResponse -->
### Schema `presenter.AdministrativeDivisionResponse`

Pointer: `#/components/schemas/presenter.AdministrativeDivisionResponse`. Type: object (schema `presenter.AdministrativeDivisionResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Administrative division ID | example: 1111 |
| `name` | string | no | Administrative division name | example: "Brazil" |

<!-- schema: #/components/schemas/presenter.NonBusinessDay -->
### Schema `presenter.NonBusinessDay`

Pointer: `#/components/schemas/presenter.NonBusinessDay`. Type: object (schema `presenter.NonBusinessDay`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date` | string | no | Non-business day date. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-20" |
| `is_holiday` | boolean (schema `IsHoliday`) | no | Is this a holiday? | example: true |
| `is_weekend` | boolean (schema `IsWeekend`) | no | Is this a weekend day? | example: true |
| `holiday_metadata` | object (map of object) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used for transaction authorization.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

## Lifecycle status

- `GET /holidays-core/v1/holiday` (`get-v1-holidays`) is marked `deprecated: true` in the specification.
- `POST /holidays-core/v1/holiday` (`post-holiday`) is marked `deprecated: true` in the specification.
- `POST /holidays-core/v1/holiday/validate` (`validate-v1-holiday`) is marked `deprecated: true` in the specification.
- `PUT /holidays-core/v1/holiday/{holiday_id}` (`put-v1-holiday`) is marked `deprecated: true` in the specification.
- `DELETE /holidays-core/v1/holiday/{holiday_id}` (`delete-v1-holiday`) is marked `deprecated: true` in the specification.
- `POST /holidays-core/v1/search-business-day` (`v1-search-business-day`) is marked `deprecated: true` in the specification.
- `GET /holidays-core/v1/non-business-days` (`v1-get-non-business-days`) is marked `deprecated: true` in the specification.
- `GET /holidays-core/v1/holiday/administrative-division/{administrative_division_id}/ancestors` (`get-v1-holidays-with-administrative-divisions-ancestors`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Holidays.yaml` | tag `Holidays (deprecated)`: GET /holidays-core/v1/holiday, POST /holidays-core/v1/holiday, POST /holidays-core/v1/holiday/validate, PUT /holidays-core/v1/holiday/{holiday_id}, DELETE /holidays-core/v1/holiday/{holiday_id}, POST /holidays-core/v1/search-business-day, GET /holidays-core/v1/non-business-days, GET /holidays-core/v1/holiday/administrative-division/{administrative_division_id}/ancestors | https://github.com/PismoDevEx/pismo-api-specs | `e7090515c96c54af…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-platform-setup-holidays` — Platform setup - Holidays and administrative divisions
- `KU-CRED-calendar-management-strategies` — Calendar management strategies (cycle closing and due dates)
- `KU-CRED-holidays-in-credit-card-accounts` — Holidays in credit card accounts
- `KU-ERR-codes-ehld` — Error codes: EHLD
