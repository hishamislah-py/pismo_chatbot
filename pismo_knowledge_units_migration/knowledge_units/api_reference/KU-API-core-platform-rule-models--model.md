---
ku_id: KU-API-core-platform-rule-models--model
title: 'API reference: Core platform - Rule models — Model'
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
- post-org-rule-model
- get-rule-model
- put-rule-model
related_kus:
- KU-CORE-processing-codes-and-transaction-types
specification_version: 1.37.0
---

# API reference: Core platform - Rule models — Model

**KU ID:** `KU-API-core-platform-rule-models--model` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Model` in `api-specs/Core_platform_-_Rule_models.yaml` (“Core platform - Rule models”, version `1.37.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for rule model management.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/models` | `post-org-rule-model` | Create org rule model | no |
| `GET /v1/models/{modelId}` | `get-rule-model` | Get rule model | no |
| `PUT /v1/models/{modelId}` | `put-rule-model` | Replace rule model | no |

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=POST path=/v1/models operationId=post-org-rule-model -->
### `POST /v1/models` — Create org rule model

- **operationId:** `post-org-rule-model`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Model`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create a rule model at the organizational level for a processing code. A rule model swaps one processing code for another if certain conditions are met. For example, you may want to use a custom processing code if the merchant is Apple. 
>
> Rule models cannot be shared between organizations.
>
> Refer to [Processing codes](doc:processing-codes-and-transaction-types) for more information on processing codes and rule models.
>
> Call the following to attach a rule model to an organization, program, or account.
>
> - [Apply rule model to org](ref:post-org-model-config)
> - [Apply rule model to program](ref:post-program-model-config)
> - [Apply rule model to account](ref:post-account-model-config)

#### Request body

Required: yes

> Parameters to create a new rule model

**Content type `application/json`** — schema: object (schema `ModelPayload`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `rules` | array of object (schema `Rule`) | yes | Processing code rules configuration array. |  |
| `name` | string | no | Model name | example: "Model name" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ModelPostResponse`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `RulesModelID`) | no | Model ID | example: "b3f53d8f-6812-4869-b17a-874d78750cc6" |
| `name` | string (schema `RulesGroupName`) | no | Rules group name | example: "Model name" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-processing-codes-and-transaction-types`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=GET path=/v1/models/{modelId} operationId=get-rule-model -->
### `GET /v1/models/{modelId}` — Get rule model

- **operationId:** `get-rule-model`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Model`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get the rule model identified in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `modelId` | path | yes | string | Model ID | example: "b3f53d8f-6812-4869-b17a-874d78750cc6" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ModelPayload`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Not found | `application/json`: object (schema `NotFoundError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `rules` | array of object (schema `Rule`) | yes | Processing code rules configuration array. |  |
| `name` | string | no | Model name | example: "Model name" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=PUT path=/v1/models/{modelId} operationId=put-rule-model -->
### `PUT /v1/models/{modelId}` — Replace rule model

- **operationId:** `put-rule-model`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Model`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Replace the rule model identified in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `modelId` | path | yes | string | Model ID | example: "b3f53d8f-6812-4869-b17a-874d78750cc6" |

#### Request body

Required: yes

> Parameters to replace a given rule model

**Content type `application/json`** — schema: object (schema `ModelPayload`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `rules` | array of object (schema `Rule`) | yes | Processing code rules configuration array. |  |
| `name` | string | no | Model name | example: "Model name" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | No content |  |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 404 | Not found | `application/json`: object (schema `NotFoundError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Rule -->
### Schema `Rule`

Pointer: `#/components/schemas/Rule`. Type: object (schema `Rule`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | yes | Processing code to use when the rule condition is met and it is a domestic transaction.<br> | example: "00" |
| `order` | integer (schema `RuleOrder`) | yes | Rule evaluation order, `1` being the highest. | example: 1 |
| `conditions` | array of object (schema `Condition`) | yes | Conditions that need to be `true` to assign the processing code. |  |
| `name` | string (schema `RuleName`) | no | Rule name | example: "Rule name example" |
| `international_processing_code` | string | no | Processing code to use when the rule condition is met and it is an international transaction. If this is an international transaction and this field is not passed, the `processing_code` field is used instead.<br> | example: "003100" |

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

<!-- schema: #/components/schemas/Condition -->
### Schema `Condition`

Pointer: `#/components/schemas/Condition`. Type: object (schema `Condition`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `ModelListType`) | yes | List types and data formats allowed:<br /><br>    - `INSTALLMENT_NUMBER` - Integer values<br /><br>    - `PROCESSING_CODE` - Alphanumeric strings<br /><br>    - `ACCOUNT_TYPE` - Alphanumeric strings<br /><br>    - `ORIGIN`- Alphanumeric strings<br /><br>    - `DCC`-  Boolean values<br /><br>    - `DOMESTIC`-  Boolean values<br /><br>    - `MERCHANT_NAME_LIST` - Alphanumeric strings<br /><br>    - `INSTALLMENT_PLAN` - Alphanumeric strings<br /><br>    - `AMOUNT` - Numbers with or without decimal places<br /><br>    - `MERCHANT_CATEGORY_CODE` - Alphanumeric strings<br /><br>    - `REVERSAL_INDICATOR` - Boolean values<br /><br>    - `AUTHORIZATION_FLOW` - Either `PAYMENTS` or `NETWORK`<br /><br>    - `ORIGINAL_PROCESSING_CODE`- Original processing code or persisted authorization processing code<br /><br>    - `MTI` - Message Type Indicator (MTI) - a four-digit numeric field - ISO 8583 standard<br /><br> | enum: ["INSTALLMENT_NUMBER", "PROCESSING_CODE", "ACCOUNT_TYPE", "ORIGIN", "DCC", "DOMESTIC", "MERCHANT_NAME_LIST", "INSTALLMENT_PLAN", "AMOUNT", "MERCHANT_CATEGORY_CODE", "REVERSAL_INDICATOR", "AUTHORIZATION_FLOW", "ORIGINAL_PROCESSING_CODE", "MTI"]; example: "MERCHANT_NAME_LIST" |
| `operator` | string | yes | Operator that will be used on this rule evaluation<br>- `eq`: Equals operator, allowed with rules that evaluate data containing strings, numbers, and booleans.<br>- `neq`: Not equals operator, allowed with rules that evaluate data containing strings, numbers, and booleans.<br>- `gt`: Greater than operator, allowed with rules that evaluate data containing numbers.<br>- `gte`: Greater than or equal operator, allowed with rules that evaluate data containing numbers.<br>- `lt`: Less than operator, allowed with rules that evaluate data containing numbers.<br>- `lte`: Less than or equal operator, allowed with rules that evaluate data containing numbers.<br>- `in`: In operator, allowed with rules that use model list as data. Compares if the data is in the configured list.<br>- `contains`: Contains operator, allowed with rules that use model list as data. Compares if the data is part of any string in the configured list.<br>- `starts_with`: Starts with operator, allowed with rules that use model list as data. Verifies whether any string in the list starts with the data value.<br>- `ends_with`: Ends with operator, allowed with rules that use model list as data. Verifies whether any string in the list ends with the data value.<br> | enum: ["eq", "neq", "gt", "gte", "lt", "lte", "in", "contains", "starts_with", "ends_with"]; example: "eq" |
| `data` | string | yes | Data used to evaluate this rule against the operator and the information received in the request.<br><br>This field must be in the format as indicated in `type` and `operator`.<br><br>**Note:** This field's value can be a model list ID returned from [Create model list](ref:post-org-model-list). A model list contains a list of values for evaluation. <br> | example: "10" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Rule_models.yaml` | tag `Model`: POST /v1/models, GET /v1/models/{modelId}, PUT /v1/models/{modelId} | https://github.com/PismoDevEx/pismo-api-specs | `08f0ae12e1b26bff…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
