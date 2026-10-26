---
ku_id: KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated
title: 'API reference: Platform setup - Divisions — Administrative divisions V2 (deprecated)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Divisions.yaml
  sha256: 96de390559b33b89009174f8f2d481cc5a03eac6b91eb93b61fcb7768cbb0289
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
- post-v2-admin-division
- get-v2-admin-division
- put-v2-admin-division
related_kus:
- KU-BANK-bank-statements-1
- KU-BANK-calendars-and-holidays
- KU-BANK-get-started-transaction-banking
- KU-CORE-platform-setup-holidays
specification_version: v1.0
---

# API reference: Platform setup - Divisions — Administrative divisions V2 (deprecated)

**KU ID:** `KU-API-platform-setup-divisions--administrative-divisions-v2-deprecated` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Administrative divisions V2 (deprecated)` in `api-specs/Platform_setup_-_Divisions.yaml` (“Platform setup - Divisions”, version `v1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> View and manage admin divisions for transaction banking

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /divisions-core/v2/administrative-division` | `post-v2-admin-division` | Create administrative division (deprecated) | **yes** |
| `GET /divisions-core/v2/administrative-division/{id}` | `get-v2-admin-division` | Get administrative division info (deprecated) | **yes** |
| `PUT /divisions-core/v2/administrative-division/{id}` | `put-v2-admin-division` | Update administrative division (deprecated) | **yes** |

## Authentication

- `S2SAuthentication`: {"type": "http", "scheme": "bearer"} — All requests must be previously authenticated with an account token.

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=POST path=/divisions-core/v2/administrative-division operationId=post-v2-admin-division -->
### `POST /divisions-core/v2/administrative-division` — Create administrative division (deprecated)

- **operationId:** `post-v2-admin-division`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions V2 (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [Create holiday calendar](ref:post-create-holiday-calendar) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Create an administrative division. 
>
> This is a v2 endpoint that offers more granular control over financial activities on non-business days. To understand the differences between v1 and v2 endpoints, refer to [Platform setup - Holidays and administrative divisions](doc:platform-setup-holidays#endpoints-for-transaction-banking).

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.v2CreateAdministrativeDivisionRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `AdminDivisionName`) | yes | Administrative division name | example: "Scotland" |
| `type` | string (schema `AdminDivisionType`) | yes | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |
| `parent_external_id` | string (schema `AdminDivisionParentExternalID`) | no | Parent external ID. Must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |
| `working_days` | array of integer (schema `WorkingDays`) | no | Week days that are working days where `0` = Sunday and `6` = Saturday. The default - [1,2,3,4,5] - corresponds to Monday through Friday.<br> | example: [1, 2, 3, 4, 5] |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in [https://json-schema.org/specification.html](https://json-schema.org/specification.html). Used to register the rules that are used to authorize the transaction.<br><br>This object uses [parameters](doc:posting-transactions-on-holidays#parameters) to specify business rules for holidays. For details, see [Posting Transactions on Holidays](doc:posting-transactions-on-holidays).<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `presenter.v2AdministrativeDivisionResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found. | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdminDivisionID`) | no | Admininistrative division ID | example: 84849 |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `working_days` | array of integer (schema `WorkingDays`) | no | Week days that are working days where `0` = Sunday and `6` = Saturday. The default - [1,2,3,4,5] - corresponds to Monday through Friday.<br> | example: [1, 2, 3, 4, 5] |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in [https://json-schema.org/specification.html](https://json-schema.org/specification.html). Used to register the rules that are used to authorize the transaction.<br><br>This object uses [parameters](doc:posting-transactions-on-holidays#parameters) to specify business rules for holidays. For details, see [Posting Transactions on Holidays](doc:posting-transactions-on-holidays).<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```

##### Response 404

404 Example `not-found-response` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target_name} not found"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-BANK-bank-statements-1`, `KU-BANK-calendars-and-holidays`, `KU-BANK-get-started-transaction-banking`, `KU-CORE-platform-setup-holidays`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=GET path=/divisions-core/v2/administrative-division/{id} operationId=get-v2-admin-division -->
### `GET /divisions-core/v2/administrative-division/{id}` — Get administrative division info (deprecated)

- **operationId:** `get-v2-admin-division`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions V2 (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [Get holiday calendar](ref:get-holiday-calendar) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Get administrative division detailed information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Administrative division ID. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Administrative division details. | `application/json`: object (schema `presenter.v2AdministrativeDivisionResponse`) |
| 400 | Bad request. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found. | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdminDivisionID`) | no | Admininistrative division ID | example: 84849 |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `working_days` | array of integer (schema `WorkingDays`) | no | Week days that are working days where `0` = Sunday and `6` = Saturday. The default - [1,2,3,4,5] - corresponds to Monday through Friday.<br> | example: [1, 2, 3, 4, 5] |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in [https://json-schema.org/specification.html](https://json-schema.org/specification.html). Used to register the rules that are used to authorize the transaction.<br><br>This object uses [parameters](doc:posting-transactions-on-holidays#parameters) to specify business rules for holidays. For details, see [Posting Transactions on Holidays](doc:posting-transactions-on-holidays).<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

200 Example `response-v1-administrative-division` — from `#/components/examples/GetV2AdministrativeDivisionResponse`:

```json
{
  "id": 1,
  "name": "Brazil",
  "type": "Country",
  "external_id": "BR",
  "working_days": [
    1,
    2,
    3,
    4,
    5
  ],
  "metadata": {
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

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```

##### Response 404

404 Example `not-found-response` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target_name} not found"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Platform_setup_-_Divisions.yaml method=PUT path=/divisions-core/v2/administrative-division/{id} operationId=put-v2-admin-division -->
### `PUT /divisions-core/v2/administrative-division/{id}` — Update administrative division (deprecated)

- **operationId:** `put-v2-admin-division`
- **Specification:** `api-specs/Platform_setup_-_Divisions.yaml` (Platform setup - Divisions)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Administrative divisions V2 (deprecated)`
- **Deprecated in specification:** **yes**
- **Security requirement:** `S2SAuthentication`

**Description (from the specification):**

> **DEPRECATED**. Call [Update holiday calendar](ref:update-holiday-calendar) instead. 
>
> This endpoint is deprecated starting April 30, 2026, and final removal from both test (EXT) and production environments on October 30, 2026.
>
> Update an administrative division.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | integer | Administrative division ID. |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `presenter.v2UpdateAdministrativeDivisionRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |
| `working_days` | array of integer (schema `WorkingDays`) | no | Week days that are working days where `0` = Sunday and `6` = Saturday. The default - [1,2,3,4,5] - corresponds to Monday through Friday.<br> | example: [1, 2, 3, 4, 5] |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in [https://json-schema.org/specification.html](https://json-schema.org/specification.html). Used to register the rules that are used to authorize the transaction.<br><br>This object uses [parameters](doc:posting-transactions-on-holidays#parameters) to specify business rules for holidays. For details, see [Posting Transactions on Holidays](doc:posting-transactions-on-holidays).<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated | `application/json`: object (schema `presenter.v2AdministrativeDivisionResponse`) |
| 400 | Bad request error. | `application/json`: object (schema `handler.HTTPError`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `handler.HTTPError`) |
| 404 | Not found error. | `application/json`: object (schema `handler.HTTPError`) |
| 500 | Internal server error | `application/json`: object (schema `handler.HTTPError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `AdminDivisionID`) | no | Admininistrative division ID | example: 84849 |
| `external_id` | string (schema `AdminDivisionExternalID`) | no | Client-supplied external ID. It must comply with the rule `^[a-zA-Z0-9-]+$`. | example: "8675309" |
| `name` | string (schema `AdminDivisionName`) | no | Administrative division name | example: "Scotland" |
| `parent_id` | integer (schema `AdminDivisionParentID`) | no | Parent ID |  |
| `type` | string (schema `AdminDivisionType`) | no | Admin division type | enum: ["City", "State", "Country"]; example: "State" |
| `working_days` | array of integer (schema `WorkingDays`) | no | Week days that are working days where `0` = Sunday and `6` = Saturday. The default - [1,2,3,4,5] - corresponds to Monday through Friday.<br> | example: [1, 2, 3, 4, 5] |
| `metadata` | object (schema `Metadata`) | no | A valid JSON schema as specified in [https://json-schema.org/specification.html](https://json-schema.org/specification.html). Used to register the rules that are used to authorize the transaction.<br><br>This object uses [parameters](doc:posting-transactions-on-holidays#parameters) to specify business rules for holidays. For details, see [Posting Transactions on Holidays](doc:posting-transactions-on-holidays).<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |

##### Response 400

400 Example `response-missing-tenant` — from `#/components/examples/MissingTenantResponse`:

```json
{
  "code": "400",
  "message": "Missing x-tenant header"
}
```

400 Example `invalid-params-response` — from `#/components/examples/InvalidParamsResponse`:

```json
{
  "code": "400",
  "message": "Invalid {parameter_name} parameter value"
}
```

400 Example `hierarchyLoopResponse` — from `#/components/examples/HierarchyLoopResponse`:

```json
{
  "code": "400",
  "message": "The parent_id {parent_id} causes a circular hierarchy loop with the administrative_division id {id}."
}
```

##### Response 404

404 Example `not-found-response` — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "404",
  "message": "{target_name} not found"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `True`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/handler.HTTPError -->
### Schema `handler.HTTPError`

Pointer: `#/components/schemas/handler.HTTPError`. Type: object (schema `handler.HTTPError`).

> Code and error message.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

## Lifecycle status

- `POST /divisions-core/v2/administrative-division` (`post-v2-admin-division`) is marked `deprecated: true` in the specification.
- `GET /divisions-core/v2/administrative-division/{id}` (`get-v2-admin-division`) is marked `deprecated: true` in the specification.
- `PUT /divisions-core/v2/administrative-division/{id}` (`put-v2-admin-division`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Divisions.yaml` | tag `Administrative divisions V2 (deprecated)`: POST /divisions-core/v2/administrative-division, GET /divisions-core/v2/administrative-division/{id}, PUT /divisions-core/v2/administrative-division/{id} | https://github.com/PismoDevEx/pismo-api-specs | `96de390559b33b89…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-bank-statements-1` — Bank statements
- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-BANK-get-started-transaction-banking` — Get started with transaction banking
- `KU-CORE-platform-setup-holidays` — Platform setup - Holidays and administrative divisions
