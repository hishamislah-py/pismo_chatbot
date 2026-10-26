---
ku_id: KU-API-core-platform-rule-models--model-list
title: 'API reference: Core platform - Rule models — Model list'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Rule_models.yaml
  sha256: 08f0ae12e1b26bff565e5754e6ddac7c269bb617a3f9f39f32e42f4a2bb806e3
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
- post-org-model-list
- get-model-list
- put-org-model-list
- patch-model-list
related_kus: []
specification_version: 1.37.0
---

# API reference: Core platform - Rule models — Model list

**KU ID:** `KU-API-core-platform-rule-models--model-list` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Model list` in `api-specs/Core_platform_-_Rule_models.yaml` (“Core platform - Rule models”, version `1.37.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for model list management.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/models/list` | `post-org-model-list` | Create model list | no |
| `GET /v1/models/list/{listId}` | `get-model-list` | Get model list | no |
| `PUT /v1/models/list/{listId}` | `put-org-model-list` | Replace model list | no |
| `PATCH /v1/models/list/{listId}` | `patch-model-list` | Update model list | no |

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=POST path=/v1/models/list operationId=post-org-model-list -->
### `POST /v1/models/list` — Create model list

- **operationId:** `post-org-model-list`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Model list`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create data for a rule model to evaluate.
>
> A model list contains values to evaluate in a rule model. To use the list, pass its ID as a `data` field's value in a `condition` when you [create a rule model](ref:post-org-rule-model).
>
> For example, you can create a model list to capture purchases made through designated merchants with the `MERCHANT_NAME_LIST` condition type. The list could look like this: `["APPLE", "MICROSOFT", "BEST BUY"]`, and be used like this:
> <pre>
> ...
>   {
>     "type": "MERCHANT_NAME_LIST",
>     "operator": "contains",
>     "data": "15bda43f-5f6d-4681-8c09-853de8b9479d"  ## Model list ID
>   }
> ...
> </pre>

#### Request body

Required: yes

> Parameters to create a new model list

**Content type `application/json`** — schema: object (schema `ModelListCreationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `data` | array of string (schema `ModelListData`) | yes | List of values used to evaluate the rule condition. | example: ["MERCHANT 1", "MERCHANT 2"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ModelListResponse`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | The ID generated for the new model list. | example: "b3f53d8f-6812-4869-b17a-874d78750cc6" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=GET path=/v1/models/list/{listId} operationId=get-model-list -->
### `GET /v1/models/list/{listId}` — Get model list

- **operationId:** `get-model-list`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Model list`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get the model list identified in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `listId` | path | yes | string | List ID | example: "30db80ce-ca5e-41ed-b9b0-4a2ee5e02c7a" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ModelListPayload`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Not found | `application/json`: object (schema `NotFoundError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `ModelListType`) | no | List types and data formats allowed:<br /><br>    - `INSTALLMENT_NUMBER` - Integer values<br /><br>    - `PROCESSING_CODE` - Alphanumeric strings<br /><br>    - `ACCOUNT_TYPE` - Alphanumeric strings<br /><br>    - `ORIGIN`- Alphanumeric strings<br /><br>    - `DCC`-  Boolean values<br /><br>    - `DOMESTIC`-  Boolean values<br /><br>    - `MERCHANT_NAME_LIST` - Alphanumeric strings<br /><br>    - `INSTALLMENT_PLAN` - Alphanumeric strings<br /><br>    - `AMOUNT` - Numbers with or without decimal places<br /><br>    - `MERCHANT_CATEGORY_CODE` - Alphanumeric strings<br /><br>    - `REVERSAL_INDICATOR` - Boolean values<br /><br>    - `AUTHORIZATION_FLOW` - Either `PAYMENTS` or `NETWORK`<br /><br>    - `ORIGINAL_PROCESSING_CODE`- Original processing code or persisted authorization processing code<br /><br>    - `MTI` - Message Type Indicator (MTI) - a four-digit numeric field - ISO 8583 standard<br /><br> | enum: ["INSTALLMENT_NUMBER", "PROCESSING_CODE", "ACCOUNT_TYPE", "ORIGIN", "DCC", "DOMESTIC", "MERCHANT_NAME_LIST", "INSTALLMENT_PLAN", "AMOUNT", "MERCHANT_CATEGORY_CODE", "REVERSAL_INDICATOR", "AUTHORIZATION_FLOW", "ORIGINAL_PROCESSING_CODE", "MTI"]; example: "MERCHANT_NAME_LIST" |
| `data` | array of string (schema `ModelListData`) | no | List of values used to evaluate the rule condition. | example: ["MERCHANT 1", "MERCHANT 2"] |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=PUT path=/v1/models/list/{listId} operationId=put-org-model-list -->
### `PUT /v1/models/list/{listId}` — Replace model list

- **operationId:** `put-org-model-list`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Model list`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Replace a model list to evaluate a rule that the platform applies at the organization level, overriding the old list with the list being sent on this request.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `listId` | path | yes | string | List ID | example: "30db80ce-ca5e-41ed-b9b0-4a2ee5e02c7a" |

#### Request body

Required: yes

> Parameters to replace a model list.

**Content type `application/json`** — schema: object (schema `ModelListCreationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `data` | array of string (schema `ModelListData`) | yes | List of values used to evaluate the rule condition. | example: ["MERCHANT 1", "MERCHANT 2"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ModelListResponse`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | The ID generated for the new model list. | example: "b3f53d8f-6812-4869-b17a-874d78750cc6" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=PATCH path=/v1/models/list/{listId} operationId=patch-model-list -->
### `PATCH /v1/models/list/{listId}` — Update model list

- **operationId:** `patch-model-list`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Model list`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Update the model list identified in the path, either adding new values or deleting values. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `listId` | path | yes | string | List ID | example: "30db80ce-ca5e-41ed-b9b0-4a2ee5e02c7a" |

#### Request body

Required: yes

> Parameters to update a given model list

**Content type `application/json`** — schema: object (schema `ModelListReplaceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `append` | array of string | no | Values to add to the model list. | example: ["VALUE 1", "VALUE 2"] |
| `delete` | array of string | no | Values to remove from the model list. | example: ["VALUE 3", "VALUE 4"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ModelListPayload`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Not found | `application/json`: object (schema `NotFoundError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `ModelListType`) | no | List types and data formats allowed:<br /><br>    - `INSTALLMENT_NUMBER` - Integer values<br /><br>    - `PROCESSING_CODE` - Alphanumeric strings<br /><br>    - `ACCOUNT_TYPE` - Alphanumeric strings<br /><br>    - `ORIGIN`- Alphanumeric strings<br /><br>    - `DCC`-  Boolean values<br /><br>    - `DOMESTIC`-  Boolean values<br /><br>    - `MERCHANT_NAME_LIST` - Alphanumeric strings<br /><br>    - `INSTALLMENT_PLAN` - Alphanumeric strings<br /><br>    - `AMOUNT` - Numbers with or without decimal places<br /><br>    - `MERCHANT_CATEGORY_CODE` - Alphanumeric strings<br /><br>    - `REVERSAL_INDICATOR` - Boolean values<br /><br>    - `AUTHORIZATION_FLOW` - Either `PAYMENTS` or `NETWORK`<br /><br>    - `ORIGINAL_PROCESSING_CODE`- Original processing code or persisted authorization processing code<br /><br>    - `MTI` - Message Type Indicator (MTI) - a four-digit numeric field - ISO 8583 standard<br /><br> | enum: ["INSTALLMENT_NUMBER", "PROCESSING_CODE", "ACCOUNT_TYPE", "ORIGIN", "DCC", "DOMESTIC", "MERCHANT_NAME_LIST", "INSTALLMENT_PLAN", "AMOUNT", "MERCHANT_CATEGORY_CODE", "REVERSAL_INDICATOR", "AUTHORIZATION_FLOW", "ORIGINAL_PROCESSING_CODE", "MTI"]; example: "MERCHANT_NAME_LIST" |
| `data` | array of string (schema `ModelListData`) | no | List of values used to evaluate the rule condition. | example: ["MERCHANT 1", "MERCHANT 2"] |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/BadRequestError -->
### Schema `BadRequestError`

Pointer: `#/components/schemas/BadRequestError`. Type: object (schema `BadRequestError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "PC0001" |
| `message` | string | no | Error message | example: "Invalid request payload" |

<!-- schema: #/components/schemas/InternalServerError -->
### Schema `InternalServerError`

Pointer: `#/components/schemas/InternalServerError`. Type: object (schema `InternalServerError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "PC0002" |
| `message` | string | no | Error message | example: "An unexpected error happened." |

<!-- schema: #/components/schemas/NotFoundError -->
### Schema `NotFoundError`

Pointer: `#/components/schemas/NotFoundError`. Type: object (schema `NotFoundError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "PC0004" |
| `message` | string | no | Error message | example: "Validation error: Item not found." |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Rule_models.yaml` | tag `Model list`: POST /v1/models/list, GET /v1/models/list/{listId}, PUT /v1/models/list/{listId}, PATCH /v1/models/list/{listId} | https://github.com/PismoDevEx/pismo-api-specs | `08f0ae12e1b26bff…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
