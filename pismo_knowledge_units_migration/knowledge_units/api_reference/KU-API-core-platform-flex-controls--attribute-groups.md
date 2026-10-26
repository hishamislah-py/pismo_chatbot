---
ku_id: KU-API-core-platform-flex-controls--attribute-groups
title: 'API reference: Core platform - Flex controls — Attribute groups'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Flex_controls.yaml
  sha256: af34d94f331c9b17178fc3eb93eae91bf3149e9f092fdef64d6b4e55ba9ef9a5
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
- get-v1-attribute-groups
- post-v1-attribute-group-flex-controls
- get-v1-attribute-groups-groupId
- update-v1-attribute-groups
related_kus:
- KU-CORE-attribute-groups
- KU-ERR-codes-erul
specification_version: 1.0.0
---

# API reference: Core platform - Flex controls — Attribute groups

**KU ID:** `KU-API-core-platform-flex-controls--attribute-groups` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Attribute groups` in `api-specs/Core_platform_-_Flex_controls.yaml` (“Core platform - Flex controls”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> API endpoints for managing attribute groups used in flex controls.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/attribute-groups` | `get-v1-attribute-groups` | List attribute groups | no |
| `POST /v1/attribute-groups` | `post-v1-attribute-group-flex-controls` | Create attribute group | no |
| `GET /v1/attribute-groups/{groupId}` | `get-v1-attribute-groups-groupId` | Get attribute group | no |
| `PATCH /v1/attribute-groups/{groupId}` | `update-v1-attribute-groups` | Update attribute group | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Flex_controls.yaml method=GET path=/v1/attribute-groups operationId=get-v1-attribute-groups -->
### `GET /v1/attribute-groups` — List attribute groups

- **operationId:** `get-v1-attribute-groups`
- **Specification:** `api-specs/Core_platform_-_Flex_controls.yaml` (Core platform - Flex controls)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rules`
- **Tags:** `Attribute groups`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List all available attribute groups in the organization. You can optionally provide the `limit` query parameter to specify the maximum number of groups to return per page.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `limit` | query | no | number | Maximum number of attribute groups to return | example: 100 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. Attribute groups for the account were found. | `application/json`: object (schema `AttributeListGroupResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `AttributeGroupObject`) | no | List of attribute groups |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-attribute-groups`.

<!-- op: spec=api-specs/Core_platform_-_Flex_controls.yaml method=POST path=/v1/attribute-groups operationId=post-v1-attribute-group-flex-controls -->
### `POST /v1/attribute-groups` — Create attribute group

- **operationId:** `post-v1-attribute-group-flex-controls`
- **Specification:** `api-specs/Core_platform_-_Flex_controls.yaml` (Core platform - Flex controls)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rules`
- **Tags:** `Attribute groups`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an attribute group, which is a set of values that can be shared across multiple flex controls within the organization. Once you create an attribute group, you reference it in flex controls in the `conditions` field in the [Create account flex control](ref:post-v1-accounts-flex-controls) or [Create customer flex control](ref:post-v1-customers-flex-controls) endpoint.
>
> For more information, refer to the [Attribute groups](doc:attribute-groups) guide.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `AttributeGroupObject`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `AttributeGroupID`) | yes | Attribute group ID, unique within the organization | minLength: 1; maxLength: 36; example: "non-trusted-merchants" |
| `description` | string (schema `AttributeGroupDescription`) | yes | Short description of the attribute group | minLength: 1; maxLength: 50; example: "High-risk merchant IDs" |
| `type` | string (schema `AttributeGroupType`) | yes | Flex control scope<br>  * `merchant_category_code`:  Merchant category code (MCC) is a four-digit number assigned to a business by credit card companies. It is used to classify the business by the type of goods or services it provides.<br>  * `merchant_id`: Unique ID assigned to a merchant by the payment processor.<br> | enum: ["merchant_id", "merchant_category_code"] |
| `values` | array of string (schema `AttributeGroupValues`) | yes | Attribute group values<br>- Each value must be unique within the array<br>- Maximum of 20,000 items<br>- Each item must not exceed 15 characters<br> | minLength: 1; maxLength: 25000; example: ["0123", "2224", "3876"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 1; items.maxLength: 15 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK. Successful attribute group creation. | `application/json`: object (schema `AttributeGroupObject`) |
| 400 | Bad request. Validation error on request. | `application/json`: object (schema `ErrorAttributeTypeDetail`) |
| 409 | Conflict. | `application/json`: object (schema `ErrorResponseWithDetails`) |
| 500 | Internal server error. | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `AttributeGroupID`) | yes | Attribute group ID, unique within the organization | minLength: 1; maxLength: 36; example: "non-trusted-merchants" |
| `description` | string (schema `AttributeGroupDescription`) | yes | Short description of the attribute group | minLength: 1; maxLength: 50; example: "High-risk merchant IDs" |
| `type` | string (schema `AttributeGroupType`) | yes | Flex control scope<br>  * `merchant_category_code`:  Merchant category code (MCC) is a four-digit number assigned to a business by credit card companies. It is used to classify the business by the type of goods or services it provides.<br>  * `merchant_id`: Unique ID assigned to a merchant by the payment processor.<br> | enum: ["merchant_id", "merchant_category_code"] |
| `values` | array of string (schema `AttributeGroupValues`) | yes | Attribute group values<br>- Each value must be unique within the array<br>- Maximum of 20,000 items<br>- Each item must not exceed 15 characters<br> | minLength: 1; maxLength: 25000; example: ["0123", "2224", "3876"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 1; items.maxLength: 15 |

##### Response 409

409 Example `Attribute group already exists` — from `#/components/examples/ERUL0707`:

```json
{
  "message": "Attribute group already exists",
  "error_code": "RULVAL0400",
  "code": "ERUL0707"
}
```

##### Response 500

500 Example `Internal server error` — from `#/components/examples/ERUL0001`:

```json
{
  "message": "internal server error",
  "error_code": "RULREP0500",
  "code": "ERUL0001"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 409 | `ERUL0707` | Attribute group already exists |
| 409 | `RULVAL0400` | Attribute group already exists |
| 500 | `ERUL0001` | internal server error |
| 500 | `RULREP0500` | internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-attribute-groups`.

<!-- op: spec=api-specs/Core_platform_-_Flex_controls.yaml method=GET path=/v1/attribute-groups/{groupId} operationId=get-v1-attribute-groups-groupId -->
### `GET /v1/attribute-groups/{groupId}` — Get attribute group

- **operationId:** `get-v1-attribute-groups-groupId`
- **Specification:** `api-specs/Core_platform_-_Flex_controls.yaml` (Core platform - Flex controls)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rules`
- **Tags:** `Attribute groups`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a specific attribute group by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `groupId` | path | yes | string | Attribute group ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. Attribute group was found. | `application/json`: object (schema `AttributeGroupObject`) |
| 404 | Not found. The attribute group was not found. | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `AttributeGroupID`) | yes | Attribute group ID, unique within the organization | minLength: 1; maxLength: 36; example: "non-trusted-merchants" |
| `description` | string (schema `AttributeGroupDescription`) | yes | Short description of the attribute group | minLength: 1; maxLength: 50; example: "High-risk merchant IDs" |
| `type` | string (schema `AttributeGroupType`) | yes | Flex control scope<br>  * `merchant_category_code`:  Merchant category code (MCC) is a four-digit number assigned to a business by credit card companies. It is used to classify the business by the type of goods or services it provides.<br>  * `merchant_id`: Unique ID assigned to a merchant by the payment processor.<br> | enum: ["merchant_id", "merchant_category_code"] |
| `values` | array of string (schema `AttributeGroupValues`) | yes | Attribute group values<br>- Each value must be unique within the array<br>- Maximum of 20,000 items<br>- Each item must not exceed 15 characters<br> | minLength: 1; maxLength: 25000; example: ["0123", "2224", "3876"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 1; items.maxLength: 15 |

##### Response 404

404 Example `attribute group not found` — from `#/components/examples/ERUL0805`:

```json
{
  "message": "attribute group not found",
  "error_code": "RULVAL0400",
  "code": "ERUL0805"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 404 | `ERUL0805` | attribute group not found |
| 404 | `RULVAL0400` | attribute group not found |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-attribute-groups`.

<!-- op: spec=api-specs/Core_platform_-_Flex_controls.yaml method=PATCH path=/v1/attribute-groups/{groupId} operationId=update-v1-attribute-groups -->
### `PATCH /v1/attribute-groups/{groupId}` — Update attribute group

- **operationId:** `update-v1-attribute-groups`
- **Specification:** `api-specs/Core_platform_-_Flex_controls.yaml` (Core platform - Flex controls)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rules`
- **Tags:** `Attribute groups`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the `values` field in an attribute group. All other attribute group fields are immutable.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `groupId` | path | yes | string | Attribute group ID |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `values` | array of string (schema `AttributeGroupValues`) | yes | Attribute group values<br>- Each value must be unique within the array<br>- Maximum of 20,000 items<br>- Each item must not exceed 15 characters<br> | minLength: 1; maxLength: 25000; example: ["0123", "2224", "3876"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 1; items.maxLength: 15 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No content |  |
| 400 | Bad request. Validation error on request. | `application/json`: object (schema `ErrorResponseWithDetails`) |
| 404 | Not found. The attribute group was not found. | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `attribute group not found` — from `#/components/examples/ERUL0806`:

```json
{
  "message": "The 'value' field is the only one that can be updated.",
  "error_code": "RULVAL0400",
  "code": "ERUL0806"
}
```

##### Response 404

404 Example `attribute group not found` — from `#/components/examples/ERUL0805`:

```json
{
  "message": "attribute group not found",
  "error_code": "RULVAL0400",
  "code": "ERUL0805"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERUL0806` | The 'value' field is the only one that can be updated. |
| 400 | `RULVAL0400` | The 'value' field is the only one that can be updated. |
| 404 | `ERUL0805` | attribute group not found |
| 404 | `RULVAL0400` | attribute group not found |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-attribute-groups`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AttributeGroupObject -->
### Schema `AttributeGroupObject`

Pointer: `#/components/schemas/AttributeGroupObject`. Type: object (schema `AttributeGroupObject`).

> Attribute group object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `AttributeGroupID`) | yes | Attribute group ID, unique within the organization | minLength: 1; maxLength: 36; example: "non-trusted-merchants" |
| `description` | string (schema `AttributeGroupDescription`) | yes | Short description of the attribute group | minLength: 1; maxLength: 50; example: "High-risk merchant IDs" |
| `type` | string (schema `AttributeGroupType`) | yes | Flex control scope<br>  * `merchant_category_code`:  Merchant category code (MCC) is a four-digit number assigned to a business by credit card companies. It is used to classify the business by the type of goods or services it provides.<br>  * `merchant_id`: Unique ID assigned to a merchant by the payment processor.<br> | enum: ["merchant_id", "merchant_category_code"] |
| `values` | array of string (schema `AttributeGroupValues`) | yes | Attribute group values<br>- Each value must be unique within the array<br>- Maximum of 20,000 items<br>- Each item must not exceed 15 characters<br> | minLength: 1; maxLength: 25000; example: ["0123", "2224", "3876"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 1; items.maxLength: 15 |

<!-- schema: #/components/schemas/ErrorAttributeTypeDetail -->
### Schema `ErrorAttributeTypeDetail`

Pointer: `#/components/schemas/ErrorAttributeTypeDetail`. Type: object (schema `ErrorAttributeTypeDetail`).

> Error detail.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `location` | string | no | Location where the request is causing an error | example: "payload.type" |
| `message` | string | no | Error description | example: "`type` should be `merchant_category_code` or `merchant_id`" |

<!-- schema: #/components/schemas/ErrorResponseWithDetails -->
### Schema `ErrorResponseWithDetails`

Pointer: `#/components/schemas/ErrorResponseWithDetails`. Type: object (schema `ErrorResponseWithDetails`).

> Error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Error description |  |
| `details` | array of object (schema `ErrorDetail`) | no | Provides more information about the error message. |  |
| `error_code` | string | no | Error code ID | deprecated: true |
| `code` | string | no | Error code ID |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Error description |  |
| `error_code` | string | no | Error code ID | deprecated: true |
| `code` | string | no | Error code ID |  |

<!-- schema: #/components/schemas/ErrorDetail -->
### Schema `ErrorDetail`

Pointer: `#/components/schemas/ErrorDetail`. Type: object (schema `ErrorDetail`).

> Error detail.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `location` | string | no | Identifies where the request is causing an error. | example: "payload.entity_type" |
| `message` | string | no | Description of error | example: "`entity_type` should be `legal_person` or `natural_person`" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Flex_controls.yaml` | tag `Attribute groups`: GET /v1/attribute-groups, POST /v1/attribute-groups, GET /v1/attribute-groups/{groupId}, PATCH /v1/attribute-groups/{groupId} | https://github.com/PismoDevEx/pismo-api-specs | `af34d94f331c9b17…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-attribute-groups` — Attribute groups
- `KU-ERR-codes-erul` — Error codes: ERUL
