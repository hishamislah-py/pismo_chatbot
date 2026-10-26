---
ku_id: KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat
title: 'API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)'
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
- get-v2-holidays
- post-v2-holiday
- put-v2-holiday
related_kus:
- KU-BANK-bank-statements-1
- KU-BANK-calendars-and-holidays
- KU-BANK-get-started-transaction-banking
- KU-CORE-platform-setup-holidays
- KU-CRED-statement-cycle-dates
- KU-ERR-codes-ehld
specification_version: v1.0
---

# API reference: Platform setup - Holidays — Holidays v2 - Transaction banking (deprecated)

**KU ID:** `KU-API-platform-setup-holidays--holidays-v2-transaction-banking-deprecat` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Holidays v2 - Transaction banking (deprecated)` in `api-specs/Platform_setup_-_Holidays.yaml` (“Platform setup - Holidays”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> View and manage business and non-business days configurations (for Transaction banking only)

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /holidays-core/v2/holiday` | `get-v2-holidays` | List holidays (deprecated) | **yes** |
| `POST /holidays-core/v2/holiday` | `post-v2-holiday` | Create holiday (deprecated) | **yes** |
| `PUT /holidays-core/v2/holiday/{holiday_id}` | `put-v2-holiday` | Update holiday (deprecated) | **yes** |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must pass an [account-specific token](https://developers.pismo.io/pismo-docs/docs/account-specific-access-tokens).<br>

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=GET path=/holidays-core/v2/holiday operationId=get-v2-holidays -->
### `GET /holidays-core/v2/holiday` — List holidays (deprecated)

- **operationId:** `get-v2-holidays`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays v2 - Transaction banking (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the new [List holidays](ref:get-holiday-new) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Return a paginated list of holidays registered for an organization. 
>
> **Note:** This endpoint is designed for transaction banking. For more information, refer to [Calendars and holidays in transaction banking](doc:calendars-and-holidays-in-transaction-banking).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | no | integer | Page number.  Default = `1`. | format: "int32"; minimum: 1; example: 5 |
| `perPage` | query | no | integer | Items per page. Default =  `10`. Maximum = `100`. | format: "int32"; minimum: 1; maximum: 100; example: 30 |
| `order` | query | no | string | Sort order: `ASC` (ascending) or `DESC` (descending). Default = `ASC`.<br> | enum: ["ASC", "DESC"]; example: "ASC" |
| `orderBy` | query | no | string | Sort by `ID` or `NAME`. Default = `ID`. | enum: ["ID", "NAME"]; example: "ID" |
| `administrativeDivisionId` | query | yes | integer | Administrative Division ID filter | format: "int32" |
| `name` | query | no | string | Holiday name filter | maxLength: 80; example: "New Year's Day" |
| `holidayDate` | query | no | string | Holiday date filter. Format = yyyy-mm-dd. | example: "2023-01-01" |
| `beginDate` | query | no | string | Get results on or after this date. <br><br>This field indicates what part of the year to start searching for holidays, not when the holiday was created at Pismo.<br><br>Format = yyyy-mm-dd. Must be less than or equal to `endDate`.<br> | example: "2025-12-24" |
| `endDate` | query | no | string | Get holidays on or before this date. <br><br>This field indicates what part of the year to end searching for holidays, not when the holiday was created at Pismo.<br><br>Format: yyyy-mm-dd. Must be greater than or equal to `beginDate`."<br> | example: "2025-11-02" |
| `deleted` | query | no | boolean | Deleted holidays filter. This field is for internal use only, deleted holidays are not returned, |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `pagination.v2.Pagination`) |
| 400 | Bad request | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token missing or invalid |  |
| 404 | Not found | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current result page | example: 1 |
| `items` | array of object (schema `presenter.HolidayV2Response`) | no |  |  |
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

Guides that link to this operation: `KU-CRED-statement-cycle-dates`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=POST path=/holidays-core/v2/holiday operationId=post-v2-holiday -->
### `POST /holidays-core/v2/holiday` — Create holiday (deprecated)

- **operationId:** `post-v2-holiday`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays v2 - Transaction banking (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the [Add holiday](ref:post-add-holiday-to-calendar) endpoint instead.
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Create a holiday&mdash;a day on which your company's offices are closed for normal business activity though online financial transactions and other business activity could still be occurring. 
>
> **Note:** This endpoint is designed for transaction banking. For more information, refer to [Calendars and holidays in transaction banking](doc:calendars-and-holidays-in-transaction-banking).

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.CreateHolidayRequestV2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `HolidayName`) | yes | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `holiday_date` | string (schema `HolidayDate`) | yes | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `administrative_division_id` | integer (schema `AdminDivIdV2Only`) | no | Administrative division ID. <br><br>When passed as a parameter, either this or `external_id` is **REQUIRED**.<br><br>**Note:** <br>Holiday metadata always takes precedence over the administrative division settings. If a holiday is not specifically configured using the [transaction banking parameters](doc:posting-transactions-on-holidays#parameters), the platform defaults to the settings in the administrative division's `metadata` object when processing transactions.<br> | example: 100100 |
| `external_id` | string (schema `ExternalIdV1Only`) | no | Existing ID value from another process or application.<br><br>When passed as a parameter, either this or `administrative_division_id` is **REQUIRED**.<br> | example: "38400-000" |
| `metadata` | object (schema `MetadataV2`) | no | A valid JSON schema, as specified in https://json-schema.org/specification.html. Used to register the rules that are used to authorize the transaction.<br><br>You can use metadata <a href="https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays#parameters">parameters</a> to specify holiday business rules. For details, refer to <a href="https://developers.pismo.io/pismo-docs/docs/posting-transactions-on-holidays">Posting Transactions on Holidays</a>.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Holidays response | `application/json`: object (schema `presenter.CreateHolidayResponseV2`) |
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
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `next_business_date` | string (schema `NextBusinessDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `administrative_division_id` | integer (schema `AdminDivIdV1Only`) | no | Administrative division ID. <br><br>When passed as a parameter, either this or `external_id` is **REQUIRED**.<br> | example: 100100 |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

201 Example `response-create-holidays-v2` — from `#/components/examples/CreateHolidayResponseV2`:

```json
{
  "id": 1,
  "name": "New Year's Day",
  "description": "New Year's Day",
  "holiday_date": "2023-01-01",
  "administrative_division_id": 1,
  "metadata": {
    "accrue_interest": true,
    "check_dormancy": true,
    "create_account": false,
    "defer_statement_due_date": true,
    "defer_transactions": true,
    "post_interest": false,
    "post_transactions": false,
    "run_cycle_closing": false,
    "any_value": "any_value"
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

400 Example `working-date-less-than-current-date` — from `#/components/examples/BadRequestResponseDatesWrong`:

```json
{
  "code": "EHLD0031",
  "message": "Working date less than the current date"
}
```

400 Example `holiday-already-exists` — from `#/components/examples/BadRequestResponseAlreadyExists`:

```json
{
  "code": "EHLD0027",
  "message": "Holiday calendar already exists"
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
| 400 | `EHLD0028` | Holiday date with the wrong format |
| 400 | `EHLD0030` | Working date with the wrong format |
| 400 | `EHLD0031` | Working date less than the current date |
| 400 | `EHLD0027` | Holiday calendar already exists |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-BANK-bank-statements-1`, `KU-BANK-calendars-and-holidays`, `KU-BANK-get-started-transaction-banking`, `KU-CORE-platform-setup-holidays`.

<!-- op: spec=api-specs/Platform_setup_-_Holidays.yaml method=PUT path=/holidays-core/v2/holiday/{holiday_id} operationId=put-v2-holiday -->
### `PUT /holidays-core/v2/holiday/{holiday_id}` — Update holiday (deprecated)

- **operationId:** `put-v2-holiday`
- **Specification:** `api-specs/Platform_setup_-_Holidays.yaml` (Platform setup - Holidays)
- **Server base URL(s):** `https://sandbox.pismolabs.io/holidays-core`
- **Tags:** `Holidays v2 - Transaction banking (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the new [Update holiday](ref:update-holiday) endpoint instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Update some holiday information. Only parameters that are passed are updated.
>
> **Note:** This endpoint is designed for transaction banking. For more information, refer to [Calendars and holidays in transaction banking](doc:calendars-and-holidays-in-transaction-banking).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `holiday_id` | path | yes | string | Pismo-assigned holiday ID | example: "8675309" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.UpdateHolidayV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `HolidayName`) | yes | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated holiday | `application/json`: object (schema `presenter.UpdateHolidayV2Response`) |
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
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

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

400 Example `holiday-not-found` — from `#/components/examples/BadRequestResponseNotFound`:

```json
{
  "code": "EHLD0034",
  "message": "Holiday not found"
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
| 400 | `EHLD0034` | Holiday not found |
| 500 | `EHLD0001` | Something went wrong - please try again |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `True`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/presenter.HolidayV2Response -->
### Schema `presenter.HolidayV2Response`

Pointer: `#/components/schemas/presenter.HolidayV2Response`. Type: object (schema `presenter.HolidayV2Response`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `administrative_division` | object (schema `presenter.AdministrativeDivisionResponse`) | no |  |  |
| `id` | integer (schema `HolidayID`) | no | Holiday ID | example: 8675309 |
| `name` | string (schema `HolidayName`) | no | Holiday name | minLength: 1; maxLength: 80; example: "New Year's Day" |
| `description` | string (schema `HolidayDescription`) | no | Holiday description | maxLength: 500; example: "Day to party like it's 1999" |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2023-12-01" |
| `working_date` | string (schema `WorkingDate`) | no | Next work day following the holiday. Format = yyyy-mm-dd. | format: "date"; example: "2023-01-02" |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in https://json-schema.org/specification.html. Used to register rules used to authorize the transaction.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
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

## Lifecycle status

- `GET /holidays-core/v2/holiday` (`get-v2-holidays`) is marked `deprecated: true` in the specification.
- `POST /holidays-core/v2/holiday` (`post-v2-holiday`) is marked `deprecated: true` in the specification.
- `PUT /holidays-core/v2/holiday/{holiday_id}` (`put-v2-holiday`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Holidays.yaml` | tag `Holidays v2 - Transaction banking (deprecated)`: GET /holidays-core/v2/holiday, POST /holidays-core/v2/holiday, PUT /holidays-core/v2/holiday/{holiday_id} | https://github.com/PismoDevEx/pismo-api-specs | `e7090515c96c54af…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-bank-statements-1` — Bank statements
- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-BANK-get-started-transaction-banking` — Get started with transaction banking
- `KU-CORE-platform-setup-holidays` — Platform setup - Holidays and administrative divisions
- `KU-CRED-statement-cycle-dates` — Credit cycle dates and time periods
- `KU-ERR-codes-ehld` — Error codes: EHLD
