---
ku_id: KU-API-core-platform-accumulator--configuration
title: 'API reference: Core platform - Accumulator — Configuration'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Accumulator.yaml
  sha256: 98ada69002d4ea1e71c78acd676abe12b061257adb20b66877a451bc55382a55
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
- get-config-accumulators
- post-v1-accumulator-config
- get-v1-accumulator-config
- patch-v1-accumulator-config
related_kus:
- KU-CORE-fee-models-create-and-simulate
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
specification_version: 1.0.0
---

# API reference: Core platform - Accumulator — Configuration

**KU ID:** `KU-API-core-platform-accumulator--configuration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Configuration` in `api-specs/Core_platform_-_Accumulator.yaml` (“Core platform - Accumulator”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Accumulator configuration endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accumulator-configs` | `get-config-accumulators` | List accumulator configurations | no |
| `POST /v1/accumulator-configs` | `post-v1-accumulator-config` | Create accumulator configuration | no |
| `GET /v1/accumulator-configs/{accumulatorConfigId}` | `get-v1-accumulator-config` | Get accumulator configuration | no |
| `PATCH /v1/accumulator-configs/{accumulatorConfigId}` | `patch-v1-accumulator-config` | Update accumulator configuration | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "401 Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accumulator.yaml method=GET path=/v1/accumulator-configs operationId=get-config-accumulators -->
### `GET /v1/accumulator-configs` — List accumulator configurations

- **operationId:** `get-config-accumulators`
- **Specification:** `api-specs/Core_platform_-_Accumulator.yaml` (Core platform - Accumulator)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accumulator`
- **Tags:** `Configuration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get config accumulators

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | no | string | Organization/tenant ID | example: "TN-beaecb37-d149-4674-a485-af0d11e40d85" |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The CID can help the Pismo engineering team track everything related to a call. If not passed, a random one is generated. You can find the CID in the reponse header.<br> | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |
| `programId` | query | no | string | Pismo program ID | example: "2265" |
| `accountId` | query | no | string | Pismo account ID | example: "1000944" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccumulatorsConfigResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of oneOf: object (schema `AccumulatorConfig`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accumulator.yaml method=POST path=/v1/accumulator-configs operationId=post-v1-accumulator-config -->
### `POST /v1/accumulator-configs` — Create accumulator configuration

- **operationId:** `post-v1-accumulator-config`
- **Specification:** `api-specs/Core_platform_-_Accumulator.yaml` (Core platform - Accumulator)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accumulator`
- **Tags:** `Configuration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a new accumulator configuration, which keeps running totals for specified transaction types. Fees are applied to these totals based on an associated fee model.
>
> After you create an accumulator configuration, you need to:   
>
> 1. <a href='https://developers.pismo.io/pismo-docs/reference/postmodel' target="_blank">Create a fee model</a> referencing the accumulator configuration. 
> 2. Attach the fee model to a <a href='https://developers.pismo.io/pismo-docs/reference/attachmentbyprogram' target="_blank">program<a> or <a href='https://developers.pismo.io/pismo-docs/reference/attachmentbyaccount' target="_blank">account<a>.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | no | string | Organization/tenant ID | example: "TN-beaecb37-d149-4674-a485-af0d11e40d85" |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The CID can help the Pismo engineering team track everything related to a call. If not passed, a random one is generated. You can find the CID in the reponse header.<br> | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |

#### Request body

Required: yes

> Payload to create a new accumulator configuration.

**Content type `application/json`** — schema: object (schema `NewAccumulatorConfig`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `level` | string (schema `Level`) | yes | Configuration level - org/tenant or account | enum: ["tenant", "account"]; example: "account" |
| `account_id` | number (schema `AcctID`) | no | Pismo account ID | format: "int64"; example: 8675309 |
| `identifier` | string (schema `Identifier`) | yes | Client-assigned accumulator configuration identifier for client tracking purposes. This identifier is used to <a href="https://developers.pismo.io/pismo-docs/reference/postmodel" target="_blank">create an accumulator fee model</a>.<br> | example: "total_cashout_config" |
| `conditions` | object (schema `Conditions`) | yes |  |  |
| `increase_type` | string (schema `IncreaseType`) | yes | Type of increase the accumulator will use for accumulating.<br>`principal_amount` - The transaction amount without fees is accumulated.<br>`contract_amount` - The transaction amount including fees is accumulated.<br> | enum: ["principal_amount", "contract_amount"]; example: "principal_amount" |
| `reset_strategy` | object (schema `ResetStrategy`) | no | Configure when accumulator totals are reset to zero. |  |

Example `createAccumulatorConfigTenantLevel` — from `#/components/examples/createAccumulatorConfigTenantLevel`:

```json
{
  "level": "tenant",
  "identifier": "total_cashin",
  "conditions": {
    "processing_code": {
      "include": [
        "00",
        "01"
      ]
    }
  },
  "increase_type": "principal_amount",
  "reset_strategy": {
    "time_window": {
      "timezone": "America/Sao_paulo",
      "window": "daily",
      "month_day": 1
    }
  }
}
```

Example `createAccumulatorConfigAccountLevel` — from `#/components/examples/createAccumulatorConfigAccountLevel`:

```json
{
  "level": "account",
  "account_id": 1000099,
  "identifier": "total_cashin",
  "conditions": {
    "processing_code": {
      "exclude": [
        "99",
        "90"
      ]
    }
  },
  "increase_type": "principal_amount",
  "reset_strategy": {
    "time_window": {
      "timezone": "America/Sao_paulo",
      "window": "daily",
      "month_day": 1
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `AccumulatorConfig`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no |  | example: "3e6b3f44-1d1a-413c-8243-644618f53037" |
| `level` | string (schema `Level`) | yes | Configuration level - org/tenant or account | enum: ["tenant", "account"]; example: "account" |
| `account_id` | number (schema `AcctID`) | no | Pismo account ID | format: "int64"; example: 8675309 |
| `identifier` | string (schema `Identifier`) | yes | Client-assigned accumulator configuration identifier for client tracking purposes. This identifier is used to <a href="https://developers.pismo.io/pismo-docs/reference/postmodel" target="_blank">create an accumulator fee model</a>.<br> | example: "total_cashout_config" |
| `conditions` | object (schema `Conditions`) | yes |  |  |
| `increase_type` | string (schema `IncreaseType`) | yes | Type of increase the accumulator will use for accumulating.<br>`principal_amount` - The transaction amount without fees is accumulated.<br>`contract_amount` - The transaction amount including fees is accumulated.<br> | enum: ["principal_amount", "contract_amount"]; example: "principal_amount" |
| `reset_strategy` | object (schema `ResetStrategy`) | no | Configure when accumulator totals are reset to zero. |  |

##### Response 400

400 Example `invalidTypeError` — from `#/components/examples/invalidTypeError`:

```json
{
  "code": "WACM0001",
  "message": "error validating input",
  "details": [
    {
      "location": "payload.increase_type",
      "message": "expected type string but got number"
    }
  ]
}
```

400 Example `invalidLevelError` — from `#/components/examples/invalidLevelError`:

```json
{
  "code": "WACM0001",
  "message": "error validating input",
  "details": [
    {
      "location": "payload.level",
      "message": "level must be one of [tenant program account]"
    }
  ]
}
```

400 Example `invalidIncreaseTypeError` — from `#/components/examples/invalidIncreaseTypeError`:

```json
{
  "code": "WACM0001",
  "message": "Error validating input",
  "details": [
    {
      "location": "payload.increase_type",
      "message": "increase_type must be one of [`contract_amount`, `principal_amount``]"
    }
  ]
}
```

400 Example `invalidWindowError` — from `#/components/examples/invalidWindowError`:

```json
{
  "code": "WACM0001",
  "message": "error validating input",
  "details": [
    {
      "location": "payload.reset_strategy.time_window.window",
      "message": "window must follow iso8601 format"
    }
  ]
}
```

400 Example `invalidTimezoneError` — from `#/components/examples/invalidTimezoneError`:

```json
{
  "code": "WACM0001",
  "message": "error validating input",
  "details": [
    {
      "location": "payload.reset_strategy.time_window.timezone",
      "message": "timezone must follow iana time zone name"
    }
  ]
}
```

400 Example `invalidMonthDayError` — from `#/components/examples/invalidMonthDayError`:

```json
{
  "code": "WACM0001",
  "message": "error validating input",
  "details": [
    {
      "location": "payload.reset_strategy.time_window.month_day",
      "message": "month_day must be greater than 0"
    }
  ]
}
```

400 Example `MissingXTenantHeaderError` — from `#/components/examples/MissingXTenantHeaderError`:

```json
{
  "code": "WACM0001",
  "message": "error validating input",
  "details": [
    {
      "location": "headers.x-tenant",
      "message": "x-tenant is a required header"
    }
  ]
}
```

##### Response 409

409 Example `duplicatedIdentifierError` — from `#/components/examples/duplicatedIdentifierError`:

```json
{
  "code": "WACM0002",
  "message": "identifier gmf123 already exists"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WACM0001` | error validating input |
| 409 | `WACM0002` | identifier gmf123 already exists |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-fee-models-create-and-simulate`.

<!-- op: spec=api-specs/Core_platform_-_Accumulator.yaml method=GET path=/v1/accumulator-configs/{accumulatorConfigId} operationId=get-v1-accumulator-config -->
### `GET /v1/accumulator-configs/{accumulatorConfigId}` — Get accumulator configuration

- **operationId:** `get-v1-accumulator-config`
- **Specification:** `api-specs/Core_platform_-_Accumulator.yaml` (Core platform - Accumulator)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accumulator`
- **Tags:** `Configuration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets the accumulator configuration
>
> You can get accumulator configuration IDs with the [List accumulator configuration](ref:get-config-accumulators) endpoint.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accumulatorConfigId` | path | yes | string | Accumulator ID | example: "x88900-0009xx" |
| `x-tenant` | header | no | string | Organization/tenant ID | example: "TN-beaecb37-d149-4674-a485-af0d11e40d85" |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The CID can help the Pismo engineering team track everything related to a call. If not passed, a random one is generated. You can find the CID in the reponse header.<br> | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccumulatorConfig`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no |  | example: "3e6b3f44-1d1a-413c-8243-644618f53037" |
| `level` | string (schema `Level`) | yes | Configuration level - org/tenant or account | enum: ["tenant", "account"]; example: "account" |
| `account_id` | number (schema `AcctID`) | no | Pismo account ID | format: "int64"; example: 8675309 |
| `identifier` | string (schema `Identifier`) | yes | Client-assigned accumulator configuration identifier for client tracking purposes. This identifier is used to <a href="https://developers.pismo.io/pismo-docs/reference/postmodel" target="_blank">create an accumulator fee model</a>.<br> | example: "total_cashout_config" |
| `conditions` | object (schema `Conditions`) | yes |  |  |
| `increase_type` | string (schema `IncreaseType`) | yes | Type of increase the accumulator will use for accumulating.<br>`principal_amount` - The transaction amount without fees is accumulated.<br>`contract_amount` - The transaction amount including fees is accumulated.<br> | enum: ["principal_amount", "contract_amount"]; example: "principal_amount" |
| `reset_strategy` | object (schema `ResetStrategy`) | no | Configure when accumulator totals are reset to zero. |  |

##### Response 404

404 Example `accumulatorConfigNotFoundError` — from `#/components/examples/accumulatorConfigNotFoundError`:

```json
{
  "code": "EACM0003",
  "message": "Configuration not found"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 404 | `EACM0003` | Configuration not found |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accumulator.yaml method=PATCH path=/v1/accumulator-configs/{accumulatorConfigId} operationId=patch-v1-accumulator-config -->
### `PATCH /v1/accumulator-configs/{accumulatorConfigId}` — Update accumulator configuration

- **operationId:** `patch-v1-accumulator-config`
- **Specification:** `api-specs/Core_platform_-_Accumulator.yaml` (Core platform - Accumulator)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accumulator`
- **Tags:** `Configuration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update accumulator configuration

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accumulatorConfigId` | path | yes | string | Accumulator ID | example: "x88900-0009xx" |
| `x-tenant` | header | no | string | Organization/tenant ID | example: "TN-beaecb37-d149-4674-a485-af0d11e40d85" |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The CID can help the Pismo engineering team track everything related to a call. If not passed, a random one is generated. You can find the CID in the reponse header.<br> | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |

#### Request body

Required: yes

> Response to updated accumulator configuration creation.

**Content type `application/json`** — schema: object (schema `PatchAccumulatorConfig`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `conditions` | object (schema `Conditions`) | no |  |  |
| `increase_type` | string (schema `IncreaseType`) | no | Type of increase the accumulator will use for accumulating.<br>`principal_amount` - The transaction amount without fees is accumulated.<br>`contract_amount` - The transaction amount including fees is accumulated.<br> | enum: ["principal_amount", "contract_amount"]; example: "principal_amount" |
| `reset_strategy` | object (schema `ResetStrategy`) | no | Configure when accumulator totals are reset to zero. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Not content success. |  |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 400

400 Example `accumulatorConfigValidationError` — from `#/components/examples/accumulatorConfigValidationError`:

```json
{
  "code": "WACM0001",
  "message": "validation error",
  "details": [
    {
      "location": "payload.increase_type",
      "message": "increase_type invalid"
    }
  ]
}
```

##### Response 404

404 Example `accumulatorConfigNotFoundError` — from `#/components/examples/accumulatorConfigNotFoundError`:

```json
{
  "code": "EACM0003",
  "message": "Configuration not found"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WACM0001` | validation error |
| 404 | `EACM0003` | Configuration not found |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccumulatorConfig -->
### Schema `AccumulatorConfig`

Pointer: `#/components/schemas/AccumulatorConfig`. Type: object (schema `AccumulatorConfig`).

Composition: includes the fields of schema `NewAccumulatorConfig` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no |  | example: "3e6b3f44-1d1a-413c-8243-644618f53037" |
| `level` | string (schema `Level`) | yes | Configuration level - org/tenant or account | enum: ["tenant", "account"]; example: "account" |
| `account_id` | number (schema `AcctID`) | no | Pismo account ID | format: "int64"; example: 8675309 |
| `identifier` | string (schema `Identifier`) | yes | Client-assigned accumulator configuration identifier for client tracking purposes. This identifier is used to <a href="https://developers.pismo.io/pismo-docs/reference/postmodel" target="_blank">create an accumulator fee model</a>.<br> | example: "total_cashout_config" |
| `conditions` | object (schema `Conditions`) | yes |  |  |
| `increase_type` | string (schema `IncreaseType`) | yes | Type of increase the accumulator will use for accumulating.<br>`principal_amount` - The transaction amount without fees is accumulated.<br>`contract_amount` - The transaction amount including fees is accumulated.<br> | enum: ["principal_amount", "contract_amount"]; example: "principal_amount" |
| `reset_strategy` | object (schema `ResetStrategy`) | no | Configure when accumulator totals are reset to zero. |  |

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Code the error internal | example: "EACM9999" |
| `message` | string | no | Message that describes the error. | example: "An Internal Server Error found, please contact the administrator" |

<!-- schema: #/components/schemas/Conditions -->
### Schema `Conditions`

Pointer: `#/components/schemas/Conditions`. Type: object (schema `Conditions`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | object (schema `ListCondition`) | no | Add processing codes representing transaction types to either include or exclude - enter one or the other, but not both. If processing codes are "include"d, then only those transactionss of those type(s) are accumulated. If processing codes are "excluded"d, then only non-excluded types are accumulated.<br> |  |

<!-- schema: #/components/schemas/ResetStrategy -->
### Schema `ResetStrategy`

Pointer: `#/components/schemas/ResetStrategy`. Type: object (schema `ResetStrategy`).

> Configure when accumulator totals are reset to zero.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `time_window` | object (schema `TimeWindow`) | no |  |  |

<!-- schema: #/components/schemas/ListCondition -->
### Schema `ListCondition`

Pointer: `#/components/schemas/ListCondition`. Type: object (schema `ListCondition`).

> Add processing codes representing transaction types to either include or exclude - enter one or the other, but not both. If processing codes are "include"d, then only those transactionss of those type(s) are accumulated. If processing codes are "excluded"d, then only non-excluded types are accumulated.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `include` | array of string | no | Include these transaction types for accumulation | example: ["00", "01"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 2; items.maxLength: 6 |
| `exclude` | array of string | no | Exclude these transaction types for accumulation | example: ["99", "90"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 2; items.maxLength: 6 |

<!-- schema: #/components/schemas/TimeWindow -->
### Schema `TimeWindow`

Pointer: `#/components/schemas/TimeWindow`. Type: object (schema `TimeWindow`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `timezone` | string (schema `Timezone`) | no | The <a href='https://en.wikipedia.org/wiki/List_of_tz_database_time_zones' target='_blank'>IANA Time Zone database</a>, such as "America/New_York". <br>This attribute will be used to evaluate the desired time zone for the time reset window.<br>If `time_zone` is not passed, the default is current UTC time zone.<br> | default: "UTC"; example: "America/Sao_Paulo" |
| `window` | string (schema `Window`) | yes | Window duration for the accumulator reset. | enum: ["daily", "weekly", "monthly", "lifetime", "once"]; example: "daily" |
| `month_day` | number (schema `MonthDay`) | no | Month day to reset. Can only be used when `window` is monthly. | format: "int32"; minimum: 1; maximum: 28; example: 1 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accumulator.yaml` | tag `Configuration`: GET /v1/accumulator-configs, POST /v1/accumulator-configs, GET /v1/accumulator-configs/{accumulatorConfigId}, PATCH /v1/accumulator-configs/{accumulatorConfigId} | https://github.com/PismoDevEx/pismo-api-specs | `98ada69002d4ea1e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-fee-models-create-and-simulate` — Creating, applying and simulating fee models
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
