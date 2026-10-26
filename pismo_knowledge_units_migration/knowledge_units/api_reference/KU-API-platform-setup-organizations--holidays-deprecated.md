---
ku_id: KU-API-platform-setup-organizations--holidays-deprecated
title: 'API reference: Platform setup - Organizations — Holidays (deprecated)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Organizations.yaml
  sha256: a1a72a2b080121e0dbaa5b67c207e5a4c60bf8106801fc485804a437c1acff0a
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
- get-v1-orgs-holidays
- post-v1-orgs-holidays
- put-v1-orgs-holidays
- delete-v1-orgs-holidays
related_kus:
- KU-ERR-codes-eoa
specification_version: v1.0
---

# API reference: Platform setup - Organizations — Holidays (deprecated)

**KU ID:** `KU-API-platform-setup-organizations--holidays-deprecated` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Holidays (deprecated)` in `api-specs/Platform_setup_-_Organizations.yaml` (“Platform setup - Organizations”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> View and manage some general holidays configurations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /orgs-core/v1/orgs/holidays` | `get-v1-orgs-holidays` | List holidays (deprecated) | **yes** |
| `POST /orgs-core/v1/orgs/holidays` | `post-v1-orgs-holidays` | Create holiday (deprecated) | **yes** |
| `PUT /orgs-core/v1/orgs/holidays/{id}` | `put-v1-orgs-holidays` | Update holiday (deprecated) | **yes** |
| `DELETE /orgs-core/v1/orgs/holidays/{id}` | `delete-v1-orgs-holidays` | Delete holiday (deprecated) | **yes** |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — All requests must be previously authenticated with an account-specific token.

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Organizations.yaml method=GET path=/orgs-core/v1/orgs/holidays operationId=get-v1-orgs-holidays -->
### `GET /orgs-core/v1/orgs/holidays` — List holidays (deprecated)

- **operationId:** `get-v1-orgs-holidays`
- **Specification:** `api-specs/Platform_setup_-_Organizations.yaml` (Platform setup - Organizations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the new [List holidays](https://developers.pismo.io/pismo-docs/reference/get-holiday-new) endpoint instead.
>
> Retrieve a paginated list of holidays.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `page` | query | no | integer | Current page. Must be greater than 0. Default is `1`. | format: "int32"; example: 2 |
| `perPage` | query | no | integer | Maximum number of items per page. Must be greater than 0. Default is `10`. | format: "int32"; example: 20 |
| `order` | query | no | string | Sort order.  Default = `ASC`. | enum: ["ASC", "DESC"]; example: "DESC" |
| `orderBy` | query | no | string | Sort order. Default = `ID`. | enum: ["ID", "name", "holidayYear", "holidayDate"]; example: "name" |
| `name` | query | no | string | Holiday name filter | maxLength: 255; example: "Christmas" |
| `holidayYear` | query | no | string | Holiday year filter | example: "2024" |
| `holidayDate` | query | no | string | Holiday date filter. Format = yyyy-mm-dd. | example: "2024-02-24" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Holidays page | `application/json`: object (schema `HolidaysPageResponse`) |
| 400 | Bad Request | `application/json`: object (schema `HTTPError`) |
| 401 | Unauthorized |  |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | default: 1; format: "int32"; example: 1 |
| `items` | array of object (schema `HolidayDetails`) | no |  |  |
| `pages` | integer (schema `Pages`) | no | Total number of pages | default: 1; format: "int32"; example: 2 |
| `per_page` | integer (schema `PerPage`) | no | Maximum number of items per page | default: 10; format: "int32"; example: 10 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 21 |

200 Example `response-v1-orgs` — from `#/components/examples/GetV1HolidaysResponse`:

```json
{
  "pages": 1,
  "current_page": 1,
  "per_page": 10,
  "total_items": 4,
  "items": [
    {
      "id": 1,
      "name": "Carnival",
      "holiday_date": "2023-02-20",
      "working_date": "2023-02-22"
    },
    {
      "id": 2,
      "name": "Corpus Christi",
      "holiday_date": "2023-05-01",
      "working_date": "2023-05-02"
    },
    {
      "id": 3,
      "name": "Independence Day",
      "holiday_date": "2023-09-07",
      "working_date": "2023-09-08"
    },
    {
      "id": 4,
      "holiday_date": "2023-11-02",
      "working_date": "2023-11-03"
    }
  ]
}
```

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "EOA0030",
  "message": "Missing x-tenant header"
}
```

400 Example `tenant-not-found` — from `#/components/examples/TenantNotFoundResponse`:

```json
{
  "code": "EOA0100",
  "message": "Org TN-00000000000001 was not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EOA0001",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOA0030` | Missing x-tenant header |
| 400 | `EOA0100` | Org TN-00000000000001 was not found |
| 500 | `EOA0001` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Organizations.yaml method=POST path=/orgs-core/v1/orgs/holidays operationId=post-v1-orgs-holidays -->
### `POST /orgs-core/v1/orgs/holidays` — Create holiday (deprecated)

- **operationId:** `post-v1-orgs-holidays`
- **Specification:** `api-specs/Platform_setup_-_Organizations.yaml` (Platform setup - Organizations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the [Add holiday](https://developers.pismo.io/pismo-docs/reference/post-add-holiday-to-calendar) endpoint instead.
>
> Create a holiday. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `HolidayRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2024-02-24" |
| `name` | string (schema `HolidayName`) | no | Holiday name | example: "Festivus" |
| `working_date` | string (schema `WorkingDate`) | no | Working date. The first normal business day after the holiday. Format = yyyy-mm-dd. | example: "2023-02-22" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Holidays response | `application/json`: object (schema `HolidayDetails`) |
| 400 | Bad Request | `application/json`: object (schema `HTTPError`) |
| 401 | Unauthorized |  |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2024-02-24" |
| `id` | integer (schema `HolidayID`) | no | Holiday ID | format: "int64"; example: 1 |
| `name` | string (schema `HolidayName`) | no | Holiday name | example: "Festivus" |
| `working_date` | string (schema `WorkingDate`) | no | Working date. The first normal business day after the holiday. Format = yyyy-mm-dd. | example: "2023-02-22" |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "EOA0030",
  "message": "Missing x-tenant header"
}
```

400 Example `tenant-not-found` — from `#/components/examples/TenantNotFoundResponse`:

```json
{
  "code": "EOA0100",
  "message": "Org TN-00000000000001 was not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EOA0001",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOA0030` | Missing x-tenant header |
| 400 | `EOA0100` | Org TN-00000000000001 was not found |
| 500 | `EOA0001` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Organizations.yaml method=PUT path=/orgs-core/v1/orgs/holidays/{id} operationId=put-v1-orgs-holidays -->
### `PUT /orgs-core/v1/orgs/holidays/{id}` — Update holiday (deprecated)

- **operationId:** `put-v1-orgs-holidays`
- **Specification:** `api-specs/Platform_setup_-_Organizations.yaml` (Platform setup - Organizations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the new [Uodate holiday](https://developers.pismo.io/pismo-docs/reference/update-holiday) endpoint instead.
>
> Update a holiday. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Holiday ID | example: "12345" |
| `x-tenant` | header | yes | string | Pismo organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `HolidayRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2024-02-24" |
| `name` | string (schema `HolidayName`) | no | Holiday name | example: "Festivus" |
| `working_date` | string (schema `WorkingDate`) | no | Working date. The first normal business day after the holiday. Format = yyyy-mm-dd. | example: "2023-02-22" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Holidays response | `application/json`: object (schema `HolidayDetails`) |
| 400 | Bad Request | `application/json`: object (schema `HTTPError`) |
| 401 | Unauthorized |  |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2024-02-24" |
| `id` | integer (schema `HolidayID`) | no | Holiday ID | format: "int64"; example: 1 |
| `name` | string (schema `HolidayName`) | no | Holiday name | example: "Festivus" |
| `working_date` | string (schema `WorkingDate`) | no | Working date. The first normal business day after the holiday. Format = yyyy-mm-dd. | example: "2023-02-22" |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "EOA0030",
  "message": "Missing x-tenant header"
}
```

400 Example `tenant-not-found` — from `#/components/examples/TenantNotFoundResponse`:

```json
{
  "code": "EOA0100",
  "message": "Org TN-00000000000001 was not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EOA0001",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOA0030` | Missing x-tenant header |
| 400 | `EOA0100` | Org TN-00000000000001 was not found |
| 500 | `EOA0001` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Organizations.yaml method=DELETE path=/orgs-core/v1/orgs/holidays/{id} operationId=delete-v1-orgs-holidays -->
### `DELETE /orgs-core/v1/orgs/holidays/{id}` — Delete holiday (deprecated)

- **operationId:** `delete-v1-orgs-holidays`
- **Specification:** `api-specs/Platform_setup_-_Organizations.yaml` (Platform setup - Organizations)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Holidays (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call the new [Delete holiday](https://developers.pismo.io/pismo-docs/reference/delete-holiday) instead.
>
> Delete a holiday. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Holiday ID | example: "12345" |
| `x-tenant` | header | yes | string | Pismo organization ID | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Holidays response. |  |
| 400 | Bad Request | `application/json`: object (schema `HTTPError`) |
| 401 | Unauthorized |  |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `HTTPError`) |

##### Response 400

400 Example `missing-x-tenant-header` — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "EOA0030",
  "message": "Missing x-tenant header"
}
```

400 Example `tenant-not-found` — from `#/components/examples/TenantNotFoundResponse`:

```json
{
  "code": "EOA0100",
  "message": "Org TN-00000000000001 was not found"
}
```

##### Response 500

500 Example `generic-internal-error` — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "code": "EOA0001",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOA0030` | Missing x-tenant header |
| 400 | `EOA0100` | Org TN-00000000000001 was not found |
| 500 | `EOA0001` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/HolidayDetails -->
### Schema `HolidayDetails`

Pointer: `#/components/schemas/HolidayDetails`. Type: object (schema `HolidayDetails`).

> Holiday details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `holiday_date` | string (schema `HolidayDate`) | no | Holiday date. Format = yyyy-mm-dd. | example: "2024-02-24" |
| `id` | integer (schema `HolidayID`) | no | Holiday ID | format: "int64"; example: 1 |
| `name` | string (schema `HolidayName`) | no | Holiday name | example: "Festivus" |
| `working_date` | string (schema `WorkingDate`) | no | Working date. The first normal business day after the holiday. Format = yyyy-mm-dd. | example: "2023-02-22" |

<!-- schema: #/components/schemas/HTTPError -->
### Schema `HTTPError`

Pointer: `#/components/schemas/HTTPError`. Type: object (schema `HTTPError`).

> Error

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no |  |  |

## Lifecycle status

- `GET /orgs-core/v1/orgs/holidays` (`get-v1-orgs-holidays`) is marked `deprecated: true` in the specification.
- `POST /orgs-core/v1/orgs/holidays` (`post-v1-orgs-holidays`) is marked `deprecated: true` in the specification.
- `PUT /orgs-core/v1/orgs/holidays/{id}` (`put-v1-orgs-holidays`) is marked `deprecated: true` in the specification.
- `DELETE /orgs-core/v1/orgs/holidays/{id}` (`delete-v1-orgs-holidays`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Organizations.yaml` | tag `Holidays (deprecated)`: GET /orgs-core/v1/orgs/holidays, POST /orgs-core/v1/orgs/holidays, PUT /orgs-core/v1/orgs/holidays/{id}, DELETE /orgs-core/v1/orgs/holidays/{id} | https://github.com/PismoDevEx/pismo-api-specs | `a1a72a2b080121e0…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-eoa` — Error codes: EOA
