---
ku_id: KU-API-seller-management-merchants--merchant-creditor
title: 'API reference: Seller management - Merchants — Merchant creditor'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- listCreditors
- getCreditor
- updateCreditor
related_kus:
- KU-EVT-catalogue-marketplace
specification_version: 1.0.0
---

# API reference: Seller management - Merchants — Merchant creditor

**KU ID:** `KU-API-seller-management-merchants--merchant-creditor` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Merchant creditor` in `api-specs/Seller_management_-_Merchants.yaml` (“Seller management - Merchants”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for creditor operations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/creditors` | `listCreditors` | List creditors | no |
| `GET /v1/creditors/{creditorId}` | `getCreditor` | Get creditor | no |
| `PUT /v1/creditors/{creditorId}` | `updateCreditor` | Update creditor | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/creditors operationId=listCreditors -->
### `GET /v1/creditors` — List creditors

- **operationId:** `listCreditors`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant creditor`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List creditors using query parameters.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `name` | query | no | string | Creditor name | minLength: 1; maxLength: 128 |
| `page` | query | no | integer | Page number. Default is 1. | format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETCreditorsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int64"; example: 74 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page | format: "int64"; example: 20 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int64"; example: 10 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page number | default: 1; format: "int64"; example: 1 |
| `items` | array of object (schema `CreditorResponse`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/creditors/{creditorId} operationId=getCreditor -->
### `GET /v1/creditors/{creditorId}` — Get creditor

- **operationId:** `getCreditor`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant creditor`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get creditor by ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `creditorId` | path | yes | integer | Creditor ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `CreditorResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CreditorID`) | no | Creditor ID | format: "int64"; example: 1 |
| `name` | string (schema `CreditorName`) | no | Creditor name | minLength: 1; maxLength: 100; example: "Acme Corporation" |
| `crediting_method` | string (schema `CreditingMethod`) | no | Crediting method. Must be set to `ACCOUNT`.<br> | enum: ["ACCOUNT"]; example: "ACCOUNT" |
| `account` | object | no | Pismo platform account |  |
| `account.id` | integer (schema `PismoAccountID`) | no | Pismo account ID | format: "int64"; example: 8675309 |
| `advancement_fee` | string (schema `AdvancementFeeInRequest`) | no | Advancement fee for creditor.<br> | default: "10"; example: "30.00" |
| `discount_rate` | string (schema `CreditorDiscountRate`) | no | Advancement discount rate for creditor.<br> | default: "0.025"; example: "0.03" |
| `maximum_advancement_percentage` | string (schema `MaximumAdvancementPercentage`) | no | Maximum advancement percentage for creditor.<br> | default: "1"; example: "0.80" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=PUT path=/v1/creditors/{creditorId} operationId=updateCreditor -->
### `PUT /v1/creditors/{creditorId}` — Update creditor

- **operationId:** `updateCreditor`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant creditor`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update creditor using its ID.
>
> This endpoint generates a [Marketplace creditor operation updated](https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `creditorId` | path | yes | integer | Creditor ID | format: "int64"; example: 1 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `POSTCreditorRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `CreditorName`) | yes | Creditor name | minLength: 1; maxLength: 100; example: "Acme Corporation" |
| `crediting_method` | string (schema `CreditingMethod`) | no | Crediting method. Must be set to `ACCOUNT`.<br> | enum: ["ACCOUNT"]; example: "ACCOUNT" |
| `advancement_fee` | string (schema `AdvancementFeeInRequest`) | no | Advancement fee for creditor.<br> | default: "10"; example: "30.00" |
| `discount_rate` | string (schema `CreditorDiscountRate`) | no | Advancement discount rate for creditor.<br> | default: "0.025"; example: "0.03" |
| `maximum_advancement_percentage` | string (schema `MaximumAdvancementPercentage`) | no | Maximum advancement percentage for creditor.<br> | default: "1"; example: "0.80" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `marketplace-marketplace-creditor-operation-updated-1` | https://developers.pismo.io/events/docs/marketplace-marketplace-creditor-operation-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/CreditorResponse -->
### Schema `CreditorResponse`

Pointer: `#/components/schemas/CreditorResponse`. Type: object (schema `CreditorResponse`).

> Response from merchant creditor. This is the entity from which the merchant receives money when a transaction is settled.
> It can be an external bank account or a Pismo account.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CreditorID`) | no | Creditor ID | format: "int64"; example: 1 |
| `name` | string (schema `CreditorName`) | no | Creditor name | minLength: 1; maxLength: 100; example: "Acme Corporation" |
| `crediting_method` | string (schema `CreditingMethod`) | no | Crediting method. Must be set to `ACCOUNT`.<br> | enum: ["ACCOUNT"]; example: "ACCOUNT" |
| `account` | object | no | Pismo platform account |  |
| `account.id` | integer (schema `PismoAccountID`) | no | Pismo account ID | format: "int64"; example: 8675309 |
| `advancement_fee` | string (schema `AdvancementFeeInRequest`) | no | Advancement fee for creditor.<br> | default: "10"; example: "30.00" |
| `discount_rate` | string (schema `CreditorDiscountRate`) | no | Advancement discount rate for creditor.<br> | default: "0.025"; example: "0.03" |
| `maximum_advancement_percentage` | string (schema `MaximumAdvancementPercentage`) | no | Maximum advancement percentage for creditor.<br> | default: "1"; example: "0.80" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Merchants.yaml` | tag `Merchant creditor`: GET /v1/creditors, GET /v1/creditors/{creditorId}, PUT /v1/creditors/{creditorId} | https://github.com/PismoDevEx/pismo-api-specs | `ebc9f3fadda7001c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-marketplace` — Event catalogue: marketplace
