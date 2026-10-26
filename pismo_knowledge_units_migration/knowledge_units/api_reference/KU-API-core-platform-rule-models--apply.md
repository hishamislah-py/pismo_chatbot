---
ku_id: KU-API-core-platform-rule-models--apply
title: 'API reference: Core platform - Rule models — Apply'
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
- get-org-model-config
- put-org-model-config
- post-org-model-config
- get-program-model-config
- put-program-model-config
- post-program-model-config
- get-account-model-config
- put-account-model-config
- post-account-model-config
related_kus: []
specification_version: 1.37.0
---

# API reference: Core platform - Rule models — Apply

**KU ID:** `KU-API-core-platform-rule-models--apply` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 9 operation(s) tagged `Apply` in `api-specs/Core_platform_-_Rule_models.yaml` (“Core platform - Rule models”, version `1.37.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to apply a rule model.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/config` | `get-org-model-config` | Get org rule model | no |
| `PUT /v1/config` | `put-org-model-config` | Replace org rule model | no |
| `POST /v1/config` | `post-org-model-config` | Apply rule model to  org | no |
| `GET /v1/config/program/{programId}` | `get-program-model-config` | Get program rule model | no |
| `PUT /v1/config/program/{programId}` | `put-program-model-config` | Replace program rule model | no |
| `POST /v1/config/program/{programId}` | `post-program-model-config` | Apply rule model to program | no |
| `GET /v1/config/account/{accountId}` | `get-account-model-config` | Get account rule model | no |
| `PUT /v1/config/account/{accountId}` | `put-account-model-config` | Replace account rule model | no |
| `POST /v1/config/account/{accountId}` | `post-account-model-config` | Apply rule model to account | no |

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=GET path=/v1/config operationId=get-org-model-config -->
### `GET /v1/config` — Get org rule model

- **operationId:** `get-org-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get an organization's rule model

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `Config`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | no | Model ID configured for this organization, program, or account. | example: "b3f53d8f-6812-4869-b17a-874d78750cc6" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=PUT path=/v1/config operationId=put-org-model-config -->
### `PUT /v1/config` — Replace org rule model

- **operationId:** `put-org-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Replace the organization rule model

#### Request body

Required: yes

> Parameters to create the configuration

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigRequest`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=POST path=/v1/config operationId=post-org-model-config -->
### `POST /v1/config` — Apply rule model to  org

- **operationId:** `post-org-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Apply rule model to an organization.

#### Request body

Required: yes

> Parameters to apply the rule model

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigRequest`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=GET path=/v1/config/program/{programId} operationId=get-program-model-config -->
### `GET /v1/config/program/{programId}` — Get program rule model

- **operationId:** `get-program-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get a program rule model

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | string | Program ID | example: "86754" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `Config`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | no | Model ID configured for this organization, program, or account. | example: "b3f53d8f-6812-4869-b17a-874d78750cc6" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=PUT path=/v1/config/program/{programId} operationId=put-program-model-config -->
### `PUT /v1/config/program/{programId}` — Replace program rule model

- **operationId:** `put-program-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Replace the program rule model

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | string | Program ID | example: "86754" |

#### Request body

Required: yes

> Parameters to create the configuration.

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigRequest`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=POST path=/v1/config/program/{programId} operationId=post-program-model-config -->
### `POST /v1/config/program/{programId}` — Apply rule model to program

- **operationId:** `post-program-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Apply a rule model to a specified program.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | string | Program ID | example: "86754" |

#### Request body

Required: yes

> Parameters to apply the rule model.

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigRequest`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=GET path=/v1/config/account/{accountId} operationId=get-account-model-config -->
### `GET /v1/config/account/{accountId}` — Get account rule model

- **operationId:** `get-account-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get account rule model

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID | example: "30db80ce-ca5e-41ed-b9b0-4a2ee5e02c7a" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `Config`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | no | Model ID configured for this organization, program, or account. | example: "b3f53d8f-6812-4869-b17a-874d78750cc6" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=PUT path=/v1/config/account/{accountId} operationId=put-account-model-config -->
### `PUT /v1/config/account/{accountId}` — Replace account rule model

- **operationId:** `put-account-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Replace an account rule model

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID | example: "30db80ce-ca5e-41ed-b9b0-4a2ee5e02c7a" |

#### Request body

Required: yes

> Parameters to create the configuration.

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigRequest`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Rule_models.yaml method=POST path=/v1/config/account/{accountId} operationId=post-account-model-config -->
### `POST /v1/config/account/{accountId}` — Apply rule model to account

- **operationId:** `post-account-model-config`
- **Specification:** `api-specs/Core_platform_-_Rule_models.yaml` (Core platform - Rule models)
- **Server base URL(s):** `https://sandbox.pismolabs.io/processing-code`
- **Tags:** `Apply`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Apply rule model to an account

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID | example: "30db80ce-ca5e-41ed-b9b0-4a2ee5e02c7a" |

#### Request body

Required: yes

> Parameters to create the configuration.

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigRequest`) |
| 400 | Bad request | `application/json`: object (schema `BadRequestError`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerError`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `model_id` | string | yes | Model ID | example: "a9995aba-c2c0-41f9-84e9-f245665e0159" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `0`, deprecated `False`.

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

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Rule_models.yaml` | tag `Apply`: GET /v1/config, PUT /v1/config, POST /v1/config, GET /v1/config/program/{programId}, PUT /v1/config/program/{programId}, POST /v1/config/program/{programId}, GET /v1/config/account/{accountId}, PUT /v1/config/account/{accountId}, POST /v1/config/account/{accountId} | https://github.com/PismoDevEx/pismo-api-specs | `08f0ae12e1b26bff…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
