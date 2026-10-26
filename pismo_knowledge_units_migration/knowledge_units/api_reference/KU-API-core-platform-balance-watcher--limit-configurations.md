---
ku_id: KU-API-core-platform-balance-watcher--limit-configurations
title: 'API reference: Core platform - Balance watcher — Limit configurations'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Balance_watcher.yaml
  sha256: 6231d6e3b987333d48220541781dff1d14145d72a4911b57477e0c0fdfe35248
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
- get-config-by-tenant
- put-config-by-tenant
- post-config-by-tenant
- get-config-by-program
- put-config-by-program
- post-config-by-program
- get-config-by-account
- put-config-by-account
- post-config-by-account
related_kus:
- KU-CORE-commercial-cards
- KU-ERR-codes-acq-to-esma
- KU-PAY-configure-payment-methods
- KU-PAY-payment-configurations
- KU-PAY-payment-methods
specification_version: 1.0.0
---

# API reference: Core platform - Balance watcher — Limit configurations

**KU ID:** `KU-API-core-platform-balance-watcher--limit-configurations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 9 operation(s) tagged `Limit configurations` in `api-specs/Core_platform_-_Balance_watcher.yaml` (“Core platform - Balance watcher”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to support configuration operations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/config` | `get-config-by-tenant` | Get limit config by Org | no |
| `PUT /v1/config` | `put-config-by-tenant` | Update limit config by Org | no |
| `POST /v1/config` | `post-config-by-tenant` | Create limit config by Org | no |
| `GET /v1/config/program/{programId}` | `get-config-by-program` | Get limit config by program | no |
| `PUT /v1/config/program/{programId}` | `put-config-by-program` | Update limit config by program | no |
| `POST /v1/config/program/{programId}` | `post-config-by-program` | Create limit config by program | no |
| `GET /v1/config/account/{accountId}` | `get-config-by-account` | Get limit config by account | no |
| `PUT /v1/config/account/{accountId}` | `put-config-by-account` | Update limit config by account | no |
| `POST /v1/config/account/{accountId}` | `post-config-by-account` | Create limit config by account | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=GET path=/v1/config operationId=get-config-by-tenant -->
### `GET /v1/config` — Get limit config by Org

- **operationId:** `get-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the limit configuration for authorizations on the Org level.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 404 | Not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 404

404 Example `example`:

```json
{
  "code": "BW0001",
  "message": "No configuration was found."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 404 | `BW0001` | No configuration was found. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=PUT path=/v1/config operationId=put-config-by-tenant -->
### `PUT /v1/config` — Update limit config by Org

- **operationId:** `put-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the limit configuration for authorizations on the Org level. This endpoint updates the entire configuration, so you must send all fields to avoid data loss.

#### Request body

Required: yes

> Update configuration request body

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 404 | Not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 404

404 Example `example`:

```json
{
  "code": "BW0001",
  "message": "No configuration was found."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 404 | `BW0001` | No configuration was found. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=POST path=/v1/config operationId=post-config-by-tenant -->
### `POST /v1/config` — Create limit config by Org

- **operationId:** `post-config-by-tenant`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a limit configuration for authorizations on the organization (Org) level. 
>
> This level can be used as a default configuration for all programs and accounts in this Org. There can be only one configuration by Org. New creation attempts for the same Org get a conflict response.
>
> This configuration currently supports only the over-limit feature. See the [Over-limit fee](doc:over-limit-fee) guide for more information.

#### Request body

Required: yes

> Create configuration request body

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 409 | Conflict | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 409

409 Example `example`:

```json
{
  "code": "BW0032",
  "message": "Config already exists."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 409 | `BW0032` | Config already exists. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-commercial-cards`, `KU-PAY-configure-payment-methods`, `KU-PAY-payment-configurations`, `KU-PAY-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=GET path=/v1/config/program/{programId} operationId=get-config-by-program -->
### `GET /v1/config/program/{programId}` — Get limit config by program

- **operationId:** `get-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the limit configuration for authorizations on the program level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID for this configuration. | example: 7126354 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 404 | Not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 404

404 Example `example`:

```json
{
  "code": "BW0001",
  "message": "No configuration was found."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 404 | `BW0001` | No configuration was found. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=PUT path=/v1/config/program/{programId} operationId=put-config-by-program -->
### `PUT /v1/config/program/{programId}` — Update limit config by program

- **operationId:** `put-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the limit configuration for authorizations on the program level. This endpoint updates the entire configuration, so you must send all fields to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID for this configuration. | example: 7126354 |

#### Request body

Required: yes

> Update configuration request body

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 404 | Not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 404

404 Example `example`:

```json
{
  "code": "BW0001",
  "message": "No configuration was found."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 404 | `BW0001` | No configuration was found. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=POST path=/v1/config/program/{programId} operationId=post-config-by-program -->
### `POST /v1/config/program/{programId}` — Create limit config by program

- **operationId:** `post-config-by-program`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a limit configuration for authorizations on the program level. 
>
> This level is a more granular level than Org and can be used as a default configuration for all accounts in this program. There can be only one configuration by program. New creation attempts for the same program get a conflict response.
>
> This configuration currently supports only the over-limit feature. See the [Over-limit fee](doc:over-limit-fee) guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID for this configuration. | example: 7126354 |

#### Request body

Required: yes

> Create configuration request body

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 409 | Conflict | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 409

409 Example `example`:

```json
{
  "code": "BW0032",
  "message": "Config already exists."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 409 | `BW0032` | Config already exists. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=GET path=/v1/config/account/{accountId} operationId=get-config-by-account -->
### `GET /v1/config/account/{accountId}` — Get limit config by account

- **operationId:** `get-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the limit configuration for authorizations on the account level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID for this configuration. | example: 11935782 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 404 | Not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 404

404 Example `example`:

```json
{
  "code": "BW0001",
  "message": "No configuration was found."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 404 | `BW0001` | No configuration was found. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=PUT path=/v1/config/account/{accountId} operationId=put-config-by-account -->
### `PUT /v1/config/account/{accountId}` — Update limit config by account

- **operationId:** `put-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the limit configuration for authorizations on the account level. This endpoint updates the entire configuration, so you must send all fields to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID for this configuration. | example: 11935782 |

#### Request body

Required: yes

> Update configuration request body

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 404 | Not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 404

404 Example `example`:

```json
{
  "code": "BW0001",
  "message": "No configuration was found."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 404 | `BW0001` | No configuration was found. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Balance_watcher.yaml method=POST path=/v1/config/account/{accountId} operationId=post-config-by-account -->
### `POST /v1/config/account/{accountId}` — Create limit config by account

- **operationId:** `post-config-by-account`
- **Specification:** `api-specs/Core_platform_-_Balance_watcher.yaml` (Core platform - Balance watcher)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balance-watcher`
- **Tags:** `Limit configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a limit configuration for authorizations on the account level. 
>
> This is the most granular level allowed and can be used to customize a specific account. There can be only one configuration by account. New creation attempts for the same account get a conflict response.
>
> This configuration currently supports only the over-limit feature. See the [Over-limit fee](doc:over-limit-fee) guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID for this configuration. | example: 11935782 |

#### Request body

Required: yes

> Create configuration request body

**Content type `application/json`** — schema: object (schema `ConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 401 | Unauthorized | `application/json`: object (schema `Error`) |
| 409 | Conflict | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `over_limit` | object (schema `Overlimit`) | no | Group of configurations related to the over-limit flow |  |
| `limit_refund` | object (schema `LimitRefund`) | no | Group of configurations related to the limit refund flow |  |

##### Response 400

400 Example `example`:

```json
{
  "code": "BW0008",
  "message": "Invalid request."
}
```

##### Response 401

401 Example `example`:

```json
{
  "code": "BW0031",
  "message": "Config creation by account unauthorized."
}
```

##### Response 409

409 Example `example`:

```json
{
  "code": "BW0032",
  "message": "Config already exists."
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "BW0007",
  "message": "An unexpected error happened."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `BW0008` | Invalid request. |
| 401 | `BW0031` | Config creation by account unauthorized. |
| 409 | `BW0032` | Config already exists. |
| 500 | `BW0007` | An unexpected error happened. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-configure-payment-methods`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Overlimit -->
### Schema `Overlimit`

Pointer: `#/components/schemas/Overlimit`. Type: object (schema `Overlimit`).

> Group of configurations related to the over-limit flow

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `enable` | boolean | yes | Flag to enable the over-limit feature. | example: true |

<!-- schema: #/components/schemas/LimitRefund -->
### Schema `LimitRefund`

Pointer: `#/components/schemas/LimitRefund`. Type: object (schema `LimitRefund`).

> Group of configurations related to the limit refund flow

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `enable` | boolean | yes | Flag to enable the limit refund feature. | example: true |

<!-- schema: #/components/schemas/Error -->
### Schema `Error`

Pointer: `#/components/schemas/Error`. Type: object (schema `Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code. | example: "RCAPI-DOMAIN-VIOLATION" |
| `message` | string | no | Error description. | example: "RCAPI domain violation." |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Balance_watcher.yaml` | tag `Limit configurations`: GET /v1/config, PUT /v1/config, POST /v1/config, GET /v1/config/program/{programId}, PUT /v1/config/program/{programId}, POST /v1/config/program/{programId}, GET /v1/config/account/{accountId}, PUT /v1/config/account/{accountId}, POST /v1/config/account/{accountId} | https://github.com/PismoDevEx/pismo-api-specs | `6231d6e3b987333d…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-commercial-cards` — Commercial cards programs
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-PAY-configure-payment-methods` — Configure payment methods
- `KU-PAY-payment-configurations` — Payment methods configurations overview
- `KU-PAY-payment-methods` — Payment methods
