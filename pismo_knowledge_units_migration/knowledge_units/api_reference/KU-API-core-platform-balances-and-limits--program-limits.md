---
ku_id: KU-API-core-platform-balances-and-limits--program-limits
title: 'API reference: Core platform - Balances and limits — Program limits'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Balances_and_limits.yaml
  sha256: d7c0d6ed8ee05ff104a1b39a1ebfef06bc337f71776f0baf9b29633ffe36ca0a
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
- get-v1-global-configs
- post-v1-global-configs
- patch-v1-global-configs-program-programId
related_kus:
- KU-CORE-program-limits
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
specification_version: 1.0.0
---

# API reference: Core platform - Balances and limits — Program limits

**KU ID:** `KU-API-core-platform-balances-and-limits--program-limits` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Program limits` in `api-specs/Core_platform_-_Balances_and_limits.yaml` (“Core platform - Balances and limits”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage program limit configurations.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/global-configs` | `get-v1-global-configs` | Get program limits | no |
| `POST /v1/global-configs` | `post-v1-global-configs` | Configure program limit | no |
| `PATCH /v1/global-configs/program/{programId}` | `patch-v1-global-configs-program-programId` | Update program limit | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Balances_and_limits.yaml method=GET path=/v1/global-configs operationId=get-v1-global-configs -->
### `GET /v1/global-configs` — Get program limits

- **operationId:** `get-v1-global-configs`
- **Specification:** `api-specs/Core_platform_-_Balances_and_limits.yaml` (Core platform - Balances and limits)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balances-limits`
- **Tags:** `Program limits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a configured global limit granted for a program along with its current accumulated limit value. 
>
> Refer to the [Program limits](doc:program-limits) guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | query | no | integer | Program ID to retrieve configurations for | example: 123 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Program limits retrieved successfully | `application/json`: array of object (schema `GetGlobalConfigResponse`) |
| 400 | Bad request - validation error | `application/json`: object (schema `ErrorModel`) |
| 404 | Configuration not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `single config` (Single program limits configuration found):

```json
[
  {
    "level": "PROGRAM",
    "program_id": 1234,
    "limits": {
      "max_credit_limit": {
        "value": 10000,
        "is_active": true,
        "accumulated": 0
      }
    }
  }
]
```

##### Response 400

400 Example `validation error` — from `#/components/examples/globalConfigInvalidProgramIDError`:

```json
{
  "message": "Error validating input",
  "code": "WBLS0005",
  "details": [
    {
      "location": "query.programId",
      "message": "programId must be a positive integer"
    }
  ]
}
```

400 Example `header validation error` — from `#/components/examples/headerValidationError`:

```json
{
  "message": "Some required headers are missing",
  "code": "WBLS0001"
}
```

##### Response 404

404 Example `config not found`:

```json
{
  "message": "Configuration not found"
}
```

##### Response 500

500 Example `system error` — from `#/components/examples/genericSystemError`:

```json
{
  "message": "Internal error found, please contact the administrator",
  "code": "EBLS9999"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBLS0005` | Error validating input |
| 400 | `WBLS0001` | Some required headers are missing |
| 500 | `EBLS9999` | Internal error found, please contact the administrator |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-program-limits`.

<!-- op: spec=api-specs/Core_platform_-_Balances_and_limits.yaml method=POST path=/v1/global-configs operationId=post-v1-global-configs -->
### `POST /v1/global-configs` — Configure program limit

- **operationId:** `post-v1-global-configs`
- **Specification:** `api-specs/Core_platform_-_Balances_and_limits.yaml` (Core platform - Balances and limits)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balances-limits`
- **Tags:** `Program limits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Configure the maximum granted limit allowed for a program within an organization.
>
> Refer to the [Program limits](doc:program-limits) guide for more information.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CreateGlobalConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `level` | string | yes | Configuration level (currently only PROGRAM is supported) | enum: ["PROGRAM"]; example: "PROGRAM" |
| `program_id` | integer | yes | Program ID (required when level is PROGRAM, must be positive) | minimum: 1; example: 123 |
| `limits` | object (schema `GlobalConfigLimits`) | yes | Limits configuration |  |

Example `valid request with positive value` (Valid program limit config creation - is_active required when value > 0):

```json
{
  "level": "PROGRAM",
  "program_id": 123,
  "limits": {
    "max_credit_limit": {
      "value": 1000.5,
      "is_active": true
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Global configuration created successfully |  |
| 400 | Bad request - validation error | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict - configuration already exists | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 400

400 Example `header validation error` — from `#/components/examples/headerValidationError`:

```json
{
  "message": "Some required headers are missing",
  "code": "WBLS0001"
}
```

400 Example `validation error` — from `#/components/examples/globalConfigValidationError`:

```json
{
  "message": "Invalid input",
  "code": "WBLS0002",
  "details": [
    {
      "location": "payload.level",
      "message": "level 'INVALID' is not supported. Only 'PROGRAM' is currently allowed"
    }
  ]
}
```

400 Example `json syntax error` — from `#/components/examples/jsonSyntaxError`:

```json
{
  "message": "Invalid syntax input",
  "code": "WBLS0003"
}
```

##### Response 409

409 Example `duplicate config` — from `#/components/examples/globalConfigDuplicateError`:

```json
{
  "message": "Duplicate config",
  "code": "DUPLICATE_CONFIG"
}
```

##### Response 500

500 Example `system error` — from `#/components/examples/genericSystemError`:

```json
{
  "message": "Internal error found, please contact the administrator",
  "code": "EBLS9999"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBLS0001` | Some required headers are missing |
| 400 | `WBLS0002` | Invalid input |
| 400 | `WBLS0003` | Invalid syntax input |
| 500 | `EBLS9999` | Internal error found, please contact the administrator |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-program-limits`.

<!-- op: spec=api-specs/Core_platform_-_Balances_and_limits.yaml method=PATCH path=/v1/global-configs/program/{programId} operationId=patch-v1-global-configs-program-programId -->
### `PATCH /v1/global-configs/program/{programId}` — Update program limit

- **operationId:** `patch-v1-global-configs-program-programId`
- **Specification:** `api-specs/Core_platform_-_Balances_and_limits.yaml` (Core platform - Balances and limits)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balances-limits`
- **Tags:** `Program limits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the existing program limit.
>
> Refer to the [Program limits](doc:program-limits) guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 123 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `UpdateGlobalConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limits` | object (schema `GlobalConfigLimits`) | yes | Limits configuration |  |

Example `valid request with positive value` (Valid program limits update - is_active required when value > 0):

```json
{
  "limits": {
    "max_credit_limit": {
      "value": 1000.5,
      "is_active": true
    }
  }
}
```

Example `request with zero value and is_active` (Valid program limits update with zero value and explicit is_active):

```json
{
  "limits": {
    "max_credit_limit": {
      "value": 0,
      "is_active": false
    }
  }
}
```

Example `request with zero value without is_active` (Valid program limits update with zero value - is_active optional (defaults to false)):

```json
{
  "limits": {
    "max_credit_limit": {
      "value": 0,
      "is_active": true
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Program limits updated successfully |  |
| 400 | Bad request - validation error | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found - configuration does not exist | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 400

400 Example `header validation error` — from `#/components/examples/headerValidationError`:

```json
{
  "message": "Some required headers are missing",
  "code": "WBLS0001"
}
```

400 Example `validation error` — from `#/components/examples/globalConfigValidationError`:

```json
{
  "message": "Invalid input",
  "code": "WBLS0002",
  "details": [
    {
      "location": "payload.level",
      "message": "level 'INVALID' is not supported. Only 'PROGRAM' is currently allowed"
    }
  ]
}
```

400 Example `json syntax error` — from `#/components/examples/jsonSyntaxError`:

```json
{
  "message": "Invalid syntax input",
  "code": "WBLS0003"
}
```

##### Response 404

404 Example `config not found` — from `#/components/examples/globalConfigNotFoundError`:

```json
{
  "message": "Global configuration not found",
  "code": "WBLS0007"
}
```

##### Response 500

500 Example `system error` — from `#/components/examples/genericSystemError`:

```json
{
  "message": "Internal error found, please contact the administrator",
  "code": "EBLS9999"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBLS0001` | Some required headers are missing |
| 400 | `WBLS0002` | Invalid input |
| 400 | `WBLS0003` | Invalid syntax input |
| 404 | `WBLS0007` | Global configuration not found |
| 500 | `EBLS9999` | Internal error found, please contact the administrator |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-program-limits`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message that describes the error. | example: "An Internal Server Error found, please contact the administrator" |
| `code` | string | no | Code that identifies the error type. | example: "EBLS9999" |
| `details` | array of object (schema `ErrorDetails`) | no |  |  |

<!-- schema: #/components/schemas/GlobalConfigLimits -->
### Schema `GlobalConfigLimits`

Pointer: `#/components/schemas/GlobalConfigLimits`. Type: object (schema `GlobalConfigLimits`).

> Limits configuration

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `max_credit_limit` | object (schema `GlobalConfigLimit`) | yes | Limit configuration |  |

<!-- schema: #/components/schemas/ErrorDetails -->
### Schema `ErrorDetails`

Pointer: `#/components/schemas/ErrorDetails`. Type: object (schema `ErrorDetails`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `location` | string | no | Location describes the attribute when the error is present | example: "payload.attribute" |
| `message` | string | no | Message that describes the error detail | example: "attribute is null" |

<!-- schema: #/components/schemas/GlobalConfigLimit -->
### Schema `GlobalConfigLimit`

Pointer: `#/components/schemas/GlobalConfigLimit`. Type: object (schema `GlobalConfigLimit`).

> Limit configuration

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `value` | number | yes | Configured program limit value (must be a non-negative decimal number with high precision) | minimum: 0; example: 1000.5 |
| `is_active` | boolean | yes | Status of the configuration limit (`true` if active, `false` if inactive) | example: true |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Balances_and_limits.yaml` | tag `Program limits`: GET /v1/global-configs, POST /v1/global-configs, PATCH /v1/global-configs/program/{programId} | https://github.com/PismoDevEx/pismo-api-specs | `d7c0d6ed8ee05ff1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-program-limits` — Program limits
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
