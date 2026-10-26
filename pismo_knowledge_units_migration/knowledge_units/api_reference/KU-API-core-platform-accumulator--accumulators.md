---
ku_id: KU-API-core-platform-accumulator--accumulators
title: 'API reference: Core platform - Accumulator — Accumulators'
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
- search-account-accumulators
related_kus: []
specification_version: 1.0.0
---

# API reference: Core platform - Accumulator — Accumulators

**KU ID:** `KU-API-core-platform-accumulator--accumulators` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Accumulators` in `api-specs/Core_platform_-_Accumulator.yaml` (“Core platform - Accumulator”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Account accumulator endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/accumulators` | `search-account-accumulators` | List account accumulators | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "401 Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accumulator.yaml method=GET path=/v1/accounts/{accountId}/accumulators operationId=search-account-accumulators -->
### `GET /v1/accounts/{accountId}/accumulators` — List account accumulators

- **operationId:** `search-account-accumulators`
- **Specification:** `api-specs/Core_platform_-_Accumulator.yaml` (Core platform - Accumulator)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accumulator`
- **Tags:** `Accumulators`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account accumulators. 
>
> *NOTE*: This endpoint requires an account-specific access token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Pismo account ID | example: "100094" |
| `x-tenant` | header | no | string | Organization/tenant ID | example: "TN-beaecb37-d149-4674-a485-af0d11e40d85" |
| `x-cid` | header | no | string | The Correlation IDentifier field is used to link related API requests and events.  The CID can help the Pismo engineering team track everything related to a call. If not passed, a random one is generated. You can find the CID in the reponse header.<br> | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccumulatorsResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of oneOf: object (schema `Accumulator`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Accumulator -->
### Schema `Accumulator`

Pointer: `#/components/schemas/Accumulator`. Type: object (schema `Accumulator`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `identifier` | string (schema `Identifier`) | no | Client-assigned accumulator configuration identifier for client tracking purposes. This identifier is used to <a href="https://developers.pismo.io/pismo-docs/reference/postmodel" target="_blank">create an accumulator fee model</a>.<br> | example: "total_cashout_config" |
| `accumulated_amount` | number (schema `AccumulatedAmount`) | no | Current accumulator amount | format: "float"; example: 1490.9 |
| `accumulated_quantity` | number (schema `AccumulatedQuantity`) | no | Current accumulator quantity | format: "int64"; example: 190 |

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Code the error internal | example: "EACM9999" |
| `message` | string | no | Message that describes the error. | example: "An Internal Server Error found, please contact the administrator" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accumulator.yaml` | tag `Accumulators`: GET /v1/accounts/{accountId}/accumulators | https://github.com/PismoDevEx/pismo-api-specs | `98ada69002d4ea1e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
