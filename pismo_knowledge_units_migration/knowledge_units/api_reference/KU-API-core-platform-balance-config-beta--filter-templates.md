---
ku_id: KU-API-core-platform-balance-config-beta--filter-templates
title: 'API reference: Core platform - Balance configurations — Filter templates'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Balance_config_Beta.yaml
  sha256: 76e234253e991b9887c9a5b3d0ca67692155b9edf0b8d4326bbfc54a742c0aef
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
- get-v1-filter-templates
- post-v1-filter-templates
- get-v1-filter-template-by-id
- put-v1-filter-template
related_kus:
- KU-CORE-balance-configurations
specification_version: 1.0.0
---

# API reference: Core platform - Balance configurations — Filter templates

**KU ID:** `KU-API-core-platform-balance-config-beta--filter-templates` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Filter templates` in `api-specs/Core_platform_-_Balance_config_Beta.yaml` (“Core platform - Balance configurations”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage filter templates.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/balances-config/filter-templates` | `get-v1-filter-templates` | List filter templates | no |
| `POST /v1/balances-config/filter-templates` | `post-v1-filter-templates` | Create filter template | no |
| `GET /v1/balances-config/filter-templates/{id}` | `get-v1-filter-template-by-id` | Get filter template | no |
| `PUT /v1/balances-config/filter-templates/{id}` | `put-v1-filter-template` | Update filter template | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Balance_config_Beta.yaml method=GET path=/v1/balances-config/filter-templates operationId=get-v1-filter-templates -->
### `GET /v1/balances-config/filter-templates` — List filter templates

- **operationId:** `get-v1-filter-templates`
- **Specification:** `api-specs/Core_platform_-_Balance_config_Beta.yaml` (Core platform - Balance configurations)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/balances-config`
- **Tags:** `Filter templates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List all filter templates available for the organization with pagination support.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `x-cid` | header | no | string | The Correlation Identifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated. | example: "12345" |
| `perPage` | query | no | integer | Maximum number of items to return (1-200) | default: 10; minimum: 1; maximum: 200 |
| `page` | query | no | integer | Page number (starting from 1) | default: 1; minimum: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FilterTemplateListResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorWithDetails`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `total_items` | integer | no | Total number of filter templates | example: 100 |
| `pages` | integer | no | Total number of pages | example: 10 |
| `current_page` | integer | no | Current page number | example: 1 |
| `per_page` | integer | no | Number of items per page | example: 10 |
| `items` | array of object (schema `FilterTemplate`) | no | Array of filter templates |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-balance-configurations`.

<!-- op: spec=api-specs/Core_platform_-_Balance_config_Beta.yaml method=POST path=/v1/balances-config/filter-templates operationId=post-v1-filter-templates -->
### `POST /v1/balances-config/filter-templates` — Create filter template

- **operationId:** `post-v1-filter-templates`
- **Specification:** `api-specs/Core_platform_-_Balance_config_Beta.yaml` (Core platform - Balance configurations)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/balances-config`
- **Tags:** `Filter templates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a reusable filter template that can be referenced in balance configurations. Filter templates allow you to define common filter criteria once and reuse them across multiple configurations.
>
> For more information, refer to the [Balance configurations filter templates](doc:filter-templates) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `x-cid` | header | no | string | The Correlation Identifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated. | example: "12345" |

#### Request body

Required: yes

> Filter template creation request

**Content type `application/json`** — schema: object (schema `CreateFilterTemplate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | yes | Optional custom ID for the filter template. If not provided, an ID will be auto-generated. | maxLength: 36; example: "filter-template-123" |
| `description` | string | no | Filter template description | maxLength: 50; example: "Standard retail transactions filter" |
| `filters` | object (schema `FilterTemplateFilters`) | yes | Filter criteria for the template |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object |
| 400 | Bad request | `application/json`: object (schema `ErrorWithDetails`) |
| 409 | Conflict - Filter template ID already exists | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `filter_template_id` | string | no | Filter template ID | example: "filter-template-123" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-balance-configurations`.

<!-- op: spec=api-specs/Core_platform_-_Balance_config_Beta.yaml method=GET path=/v1/balances-config/filter-templates/{id} operationId=get-v1-filter-template-by-id -->
### `GET /v1/balances-config/filter-templates/{id}` — Get filter template

- **operationId:** `get-v1-filter-template-by-id`
- **Specification:** `api-specs/Core_platform_-_Balance_config_Beta.yaml` (Core platform - Balance configurations)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/balances-config`
- **Tags:** `Filter templates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a specific filter template by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Filter template ID | example: "filter-template-123" |
| `x-tenant` | header | yes | string | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `x-cid` | header | no | string | The Correlation Identifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated. | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FilterTemplate`) |
| 404 | Filter template not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Filter template ID | maxLength: 36; example: "filter-template-123" |
| `org_id` | string | no | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `description` | string | no | Filter template description | maxLength: 50; example: "Standard retail transactions filter" |
| `filters` | object (schema `FilterTemplateFilters`) | no | Filter criteria for the template |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-balance-configurations`.

<!-- op: spec=api-specs/Core_platform_-_Balance_config_Beta.yaml method=PUT path=/v1/balances-config/filter-templates/{id} operationId=put-v1-filter-template -->
### `PUT /v1/balances-config/filter-templates/{id}` — Update filter template

- **operationId:** `put-v1-filter-template`
- **Specification:** `api-specs/Core_platform_-_Balance_config_Beta.yaml` (Core platform - Balance configurations)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/balances-config`
- **Tags:** `Filter templates`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update filter template. Each update will version the filter template, allowing you to track changes over time.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | Filter template ID | example: "filter-template-123" |
| `x-tenant` | header | yes | string | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `x-cid` | header | no | string | The Correlation Identifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated. | example: "12345" |

#### Request body

Required: yes

> Filter template update request

**Content type `application/json`** — schema: object (schema `UpdateFilterTemplate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | no | Filter template description | maxLength: 50; example: "Updated retail transactions filter" |
| `filters` | object (schema `FilterTemplateFilters`) | yes | Filter criteria for the template |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK - Returns the updated filter template | `application/json`: object (schema `FilterTemplate`) |
| 400 | Bad request | `application/json`: object (schema `ErrorWithDetails`) |
| 404 | Filter template not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Filter template ID | maxLength: 36; example: "filter-template-123" |
| `org_id` | string | no | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `description` | string | no | Filter template description | maxLength: 50; example: "Standard retail transactions filter" |
| `filters` | object (schema `FilterTemplateFilters`) | no | Filter criteria for the template |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-balance-configurations`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/FilterTemplate -->
### Schema `FilterTemplate`

Pointer: `#/components/schemas/FilterTemplate`. Type: object (schema `FilterTemplate`).

> Filter template response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Filter template ID | maxLength: 36; example: "filter-template-123" |
| `org_id` | string | no | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `description` | string | no | Filter template description | maxLength: 50; example: "Standard retail transactions filter" |
| `filters` | object (schema `FilterTemplateFilters`) | no | Filter criteria for the template |  |

<!-- schema: #/components/schemas/ErrorWithDetails -->
### Schema `ErrorWithDetails`

Pointer: `#/components/schemas/ErrorWithDetails`. Type: object (schema `ErrorWithDetails`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message that describes the error. | example: "An Internal Server Error found, please contact the administrator" |
| `code` | string | no | Code that identifies the error type. | example: "EBLC9999" |
| `details` | array of object (schema `ErrorDetails`) | no |  |  |

<!-- schema: #/components/schemas/Error -->
### Schema `Error`

Pointer: `#/components/schemas/Error`. Type: object (schema `Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message that describes the error. | example: "An Internal Server Error found, please contact the administrator" |
| `code` | string | no | Code that identifies the error type. | example: "EBLC9999" |

<!-- schema: #/components/schemas/FilterTemplateFilters -->
### Schema `FilterTemplateFilters`

Pointer: `#/components/schemas/FilterTemplateFilters`. Type: object (schema `FilterTemplateFilters`).

> Filter criteria for the template

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_codes` | array of string | yes | Array of processing codes | minItems: 1; example: ["0000", "0001", "0100"] |
| `min_installments` | integer | no | Minimum number of installments | minimum: 0; example: 1 |
| `max_installments` | integer | no | Maximum number of installments | minimum: 0; maximum: 99; example: 12 |
| `mcc` | array of string | no | Merchant Category Codes | example: ["5411", "5912"] |
| `account_type` | string (schema `AccountType`) | no | Account type that impacts limit or different account.<br>Account types:<br>"00" = Non-specified account<br>"10" = Savings account<br>"20" = Checking account<br>"30" = Credit card account<br> | enum: ["00", "10", "20", "30"]; example: "00" |
| `currency_code` | string (schema `CurrencyCode`) | no | Alphanumeric ISO 4217 standard currency code that impacts different limits or accounts. | example: "USD" |

<!-- schema: #/components/schemas/ErrorDetails -->
### Schema `ErrorDetails`

Pointer: `#/components/schemas/ErrorDetails`. Type: object (schema `ErrorDetails`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `location` | string | no | Location describes the attribute when the error is present. | example: "payload.attribute" |
| `message` | string | no | Message that describes the error detail. | example: "attribute is null" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Balance_config_Beta.yaml` | tag `Filter templates`: GET /v1/balances-config/filter-templates, POST /v1/balances-config/filter-templates, GET /v1/balances-config/filter-templates/{id}, PUT /v1/balances-config/filter-templates/{id} | https://github.com/PismoDevEx/pismo-api-specs | `76e234253e991b98…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-balance-configurations` — Balance configurations and filter templates
