---
ku_id: KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations
title: 'API reference: Revolving credit - Interest accruals — Accrual type post configurations'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Interest_accruals.yaml
  sha256: c741d2a41ac47207d0bbbc8f40d9492a64f36e979006c8170c14a065a96978af
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
- getAccrualTypePostConfig
- createAccrualTypePostConfig
- updateAccrualTypePostConfig
related_kus:
- KU-CRED-projected-accruals
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Interest accruals — Accrual type post configurations

**KU ID:** `KU-API-revolving-credit-interest-accruals--accrual-type-post-configurations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Accrual type post configurations` in `api-specs/Revolving_credit_-_Interest_accruals.yaml` (“Revolving credit - Interest accruals”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Accrual type post configurations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/programs/{programId}/accrual-type-post-config` | `getAccrualTypePostConfig` | List accrual type post configurations | no |
| `POST /v1/programs/{programId}/accrual-type-post-config` | `createAccrualTypePostConfig` | Create accrual type post configuration | no |
| `PATCH /v1/programs/{programId}/accrual-type-post-config/{accrualTypePostConfigId}` | `updateAccrualTypePostConfig` | Update accrual type post configuration | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Interest_accruals.yaml method=GET path=/v1/programs/{programId}/accrual-type-post-config operationId=getAccrualTypePostConfig -->
### `GET /v1/programs/{programId}/accrual-type-post-config` — List accrual type post configurations

- **operationId:** `getAccrualTypePostConfig`
- **Specification:** `api-specs/Revolving_credit_-_Interest_accruals.yaml` (Revolving credit - Interest accruals)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-interest-accruals`
- **Tags:** `Accrual type post configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieves a list of accrual type post configurations for a program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64" |
| `accrualType` | query | no | string | Accrual type<br> | enum: ["REFINANCING", "OVERDUE", "WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX"]; example: "REFINANCING" |
| `page` | query | no | integer | Page number | default: 1; format: "int32" |
| `perPage` | query | no | integer | Number of items per page | default: 100; format: "int32" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of accrual type post configurations. | `application/json`: object |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page | format: "int32"; example: 20 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 955 |
| `items_on_page` | integer (schema `ItemsOnPage`) | no | Items on page. (This could be less than `per_page` if this is the last page.) | format: "int32"; example: 1 |
| `pages` | integer (schema `NumberOfPages`) | no | Number of pages | format: "int32"; example: 10 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Is this the last page? | example: false |
| `items` | array of object | no |  |  |
| `items[].accrual_type_post_config_id` | integer (schema `AccrualTypePostConfigId`) | no | Accrual type post configuration ID | format: "int64"; example: 1001 |
| `items[].program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 500 |
| `items[].accrual_type` | string (schema `AccrualType`) | no | Accrual type. Should be one of the following values:<br>  `REFINANCING`<br>  `OVERDUE`<br>  `WITHDRAWAL_INTEREST`<br>  `BILLPAYMENT_INTEREST`<br>  `OVERDRAFT_INTEREST`<br>  `FINANCIAL_TAX`<br> | maxLength: 20; example: "REFINANCING" |
| `items[].reversal_projection_processing_code` | string (schema `ReversalProjectionProcessingCode`) | no | Reversal projection processing code. This field is used if the `Enable accrual reversal to new accrual types` program parameter is set to `1` (true).<br> | example: "REV456" |
| `items[].processing_code` | string (schema `ProcessingCode`) | no | Processing code | example: "PROC123" |
| `items[].created_at` | string (schema `CreatedAt`) | no | Date created. Format = YYYY-MM-DDThh:mm:ss.sssz. | example: "2023-08-18T20:53:27.498Z" |
| `items[].updated_at` | string (schema `UpdatedAt`) | no | Timestamp of last update. Format = YYYY-MM-DDThh:mm:ssz. | format: "date-time"; example: "2025-05-16T12:30:00Z" |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EIAC0002",
  "message": "Request header is missing: x-tenant"
}
```

##### Response 404

404 Example `Program not found`:

```json
{
  "code": "EX0001",
  "message": "Program ID ${program_id} not found"
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
| 400 | `EIAC0002` | Request header is missing: x-tenant |
| 404 | `EX0001` | Program ID ${program_id} not found |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Interest_accruals.yaml method=POST path=/v1/programs/{programId}/accrual-type-post-config operationId=createAccrualTypePostConfig -->
### `POST /v1/programs/{programId}/accrual-type-post-config` — Create accrual type post configuration

- **operationId:** `createAccrualTypePostConfig`
- **Specification:** `api-specs/Revolving_credit_-_Interest_accruals.yaml` (Revolving credit - Interest accruals)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-interest-accruals`
- **Tags:** `Accrual type post configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a new accrual type post configuration for the specified program. This configuration is used in posting transactions for accruals to statements.
>
> When a cycle closes, the Pismo platform retrieves the accrual type post configuration for the specific program and accrual type and uses the specified processing code when posting the accrual transactions.
>
> The reversal projection processing code is used to reverse projected accruals when the customer's payment date is between `cycle-closing-date` and `due-date` (or the real due date, if different from `due_date`). The Pismo platform creates transactions to perform the reversals and posts them on the statement.
>
> **Note:** Payments can be backdated, but future dates are not allowed.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CreateNewAccrualTypePostConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_type` | string (schema `AccrualType`) | yes | Accrual type. Should be one of the following values:<br>  `REFINANCING`<br>  `OVERDUE`<br>  `WITHDRAWAL_INTEREST`<br>  `BILLPAYMENT_INTEREST`<br>  `OVERDRAFT_INTEREST`<br>  `FINANCIAL_TAX`<br> | maxLength: 20; example: "REFINANCING" |
| `processing_code` | string (schema `ProcessingCode`) | yes | Processing code | example: "PROC123" |
| `reversal_projection_processing_code` | string (schema `ReversalProjectionProcessingCode`) | no | Reversal projection processing code. This field is used if the `Enable accrual reversal to new accrual types` program parameter is set to `1` (true).<br> | example: "REV456" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Successfully created accrual type post config. | `application/json`: object |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `StandardErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_type_post_config_id` | integer (schema `AccrualTypePostConfigId`) | no | Accrual type post configuration ID | format: "int64"; example: 1001 |
| `accrual_type` | string (schema `AccrualType`) | no | Accrual type. Should be one of the following values:<br>  `REFINANCING`<br>  `OVERDUE`<br>  `WITHDRAWAL_INTEREST`<br>  `BILLPAYMENT_INTEREST`<br>  `OVERDRAFT_INTEREST`<br>  `FINANCIAL_TAX`<br> | maxLength: 20; example: "REFINANCING" |
| `program_id` | integer (schema `ProgramId`) | no | Program ID | format: "int64"; example: 500 |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code | example: "PROC123" |
| `reversal_projection_processing_code` | string (schema `ReversalProjectionProcessingCode`) | no | Reversal projection processing code. This field is used if the `Enable accrual reversal to new accrual types` program parameter is set to `1` (true).<br> | example: "REV456" |
| `created_at` | string (schema `CreatedAt`) | no | Date created. Format = YYYY-MM-DDThh:mm:ss.sssz. | example: "2023-08-18T20:53:27.498Z" |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EIAC0002",
  "message": "Request header is missing: x-tenant"
}
```

##### Response 404

404 Example `Program not found`:

```json
{
  "code": "EX0001",
  "message": "The program_id ${program_id} not found"
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
| 400 | `EIAC0002` | Request header is missing: x-tenant |
| 404 | `EX0001` | The program_id ${program_id} not found |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Interest_accruals.yaml method=PATCH path=/v1/programs/{programId}/accrual-type-post-config/{accrualTypePostConfigId} operationId=updateAccrualTypePostConfig -->
### `PATCH /v1/programs/{programId}/accrual-type-post-config/{accrualTypePostConfigId}` — Update accrual type post configuration

- **operationId:** `updateAccrualTypePostConfig`
- **Specification:** `api-specs/Revolving_credit_-_Interest_accruals.yaml` (Revolving credit - Interest accruals)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-interest-accruals`
- **Tags:** `Accrual type post configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update specific fields in an accrual type post configuration for a program.
>
> <b>Notes:</b>
> - If `reversal_projection_processing_code is omitted in request`, its value is updated to null.
> - If `processing_code` is omitted, its value remains unchanged.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64" |
| `accrualTypePostConfigId` | path | yes | integer | Accrual type post configuration ID | format: "int64" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `UpdateAccrualTypePostConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code | example: "PROC123" |
| `reversal_projection_processing_code` | string (schema `ReversalProjectionProcessingCode`) | no | Reversal projection processing code. This field is used if the `Enable accrual reversal to new accrual types` program parameter is set to `1` (true).<br> | example: "REV456" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successfully updated accrual type post config. | `application/json`: object |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_type_post_config_id` | integer (schema `AccrualTypePostConfigId`) | no | Accrual type post configuration ID | format: "int64"; example: 1001 |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code | example: "PROC123" |
| `reversal_projection_processing_code` | string (schema `ReversalProjectionProcessingCode`) | no | Reversal projection processing code. This field is used if the `Enable accrual reversal to new accrual types` program parameter is set to `1` (true).<br> | example: "REV456" |
| `updated_at` | string (schema `UpdatedAt`) | no | Timestamp of last update. Format = YYYY-MM-DDThh:mm:ssz. | format: "date-time"; example: "2025-05-16T12:30:00Z" |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EIAC0002",
  "message": "Request header is missing: x-tenant"
}
```

##### Response 404

404 Example `Program not found`:

```json
{
  "code": "EX0001",
  "message": "Program ID ${program_id} not found"
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
| 400 | `EIAC0002` | Request header is missing: x-tenant |
| 404 | `EX0001` | Program ID ${program_id} not found |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-projected-accruals`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Interest_accruals.yaml` | tag `Accrual type post configurations`: GET /v1/programs/{programId}/accrual-type-post-config, POST /v1/programs/{programId}/accrual-type-post-config, PATCH /v1/programs/{programId}/accrual-type-post-config/{accrualTypePostConfigId} | https://github.com/PismoDevEx/pismo-api-specs | `c741d2a41ac47207…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-projected-accruals` — Projected accruals
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
