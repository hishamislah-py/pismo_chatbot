---
ku_id: KU-API-seller-management-merchants--merchant-business-category
title: 'API reference: Seller management - Merchants — Merchant business category'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Merchants.yaml
  sha256: ebc9f3fadda7001c7ad8d607cd3fe07461f96c39c6ca15baccef307dd27f67bb
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
- listBusinessCategories
- getBusinessCategory
related_kus: []
specification_version: 1.0.0
---

# API reference: Seller management - Merchants — Merchant business category

**KU ID:** `KU-API-seller-management-merchants--merchant-business-category` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Merchant business category` in `api-specs/Seller_management_-_Merchants.yaml` (“Seller management - Merchants”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for business category

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/businesscategories` | `listBusinessCategories` | List business categories | no |
| `GET /v1/businesscategories/{externalCode}` | `getBusinessCategory` | Get business category | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/businesscategories operationId=listBusinessCategories -->
### `GET /v1/businesscategories` — List business categories

- **operationId:** `listBusinessCategories`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant business category`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieves the list of business categories for merchants.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `page` | query | no | integer | Current page number | default: 1; format: "int64"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |
| `externalCode` | query | yes | string | External code for business category. The category is the type of business. | maxLength: 128; example: "123-abc" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETBusinessCategoryResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean (schema `HasNext`) | no | Indicates whether there are more pages after the current one. | example: false |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page | format: "int64"; example: 20 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page number | default: 1; format: "int64"; example: 1 |
| `items` | array of object (schema `BusinessCategory`) | no | Items |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/businesscategories/{externalCode} operationId=getBusinessCategory -->
### `GET /v1/businesscategories/{externalCode}` — Get business category

- **operationId:** `getBusinessCategory`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant business category`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get business category using external code. The category is the type of business.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `externalCode` | path | yes | string | External code for business category. The category is the type of business. | maxLength: 128; example: "123-abc" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `BusinessCategory`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `business_category_id` | string (schema `BusinessCategoryID`) | no | Business category ID | example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |
| `external_code` | string (schema `ExternalCode`) | no | Code for merchant category. The category is the type of business. You can use the endpoint <a href="https://developers.pismo.io/pismo-docs/reference/get_v1-businesscategories">Retrieves business categories corresponding to query parameters</a> to get a list of business categories and their external codes.<br> | minLength: 1; maxLength: 128 |
| `category` | string (schema `BusinessCategoryName`) | no | Business category name | minLength: 1; maxLength: 128 |
| `description` | string (schema `BusinessCategoryDescription`) | no | Business category description | minLength: 1; maxLength: 128 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/BusinessCategory -->
### Schema `BusinessCategory`

Pointer: `#/components/schemas/BusinessCategory`. Type: object (schema `BusinessCategory`).

> Type of business

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID | example: "TN-f878e4a1-2879-48ba-be16-821e73ac98db" |
| `business_category_id` | string (schema `BusinessCategoryID`) | no | Business category ID | example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |
| `external_code` | string (schema `ExternalCode`) | no | Code for merchant category. The category is the type of business. You can use the endpoint <a href="https://developers.pismo.io/pismo-docs/reference/get_v1-businesscategories">Retrieves business categories corresponding to query parameters</a> to get a list of business categories and their external codes.<br> | minLength: 1; maxLength: 128 |
| `category` | string (schema `BusinessCategoryName`) | no | Business category name | minLength: 1; maxLength: 128 |
| `description` | string (schema `BusinessCategoryDescription`) | no | Business category description | minLength: 1; maxLength: 128 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Merchants.yaml` | tag `Merchant business category`: GET /v1/businesscategories, GET /v1/businesscategories/{externalCode} | https://github.com/PismoDevEx/pismo-api-specs | `ebc9f3fadda7001c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
