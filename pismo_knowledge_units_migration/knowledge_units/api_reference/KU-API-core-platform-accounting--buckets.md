---
ku_id: KU-API-core-platform-accounting--buckets
title: 'API reference: Core platform - Accounting — Buckets'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Accounting.yaml
  sha256: f0272a891eaca0fedca4fa47cc760ff7fd676f50c94a22aa19ac665fa7017451
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
- GetBucketsByAccount
related_kus: []
specification_version: 1.0.0
---

# API reference: Core platform - Accounting — Buckets

**KU ID:** `KU-API-core-platform-accounting--buckets` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Buckets` in `api-specs/Core_platform_-_Accounting.yaml` (“Core platform - Accounting”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage account buckets.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/buckets` | `GetBucketsByAccount` | Get account buckets | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v1/buckets operationId=GetBucketsByAccount -->
### `GET /v1/buckets` — Get account buckets

- **operationId:** `GetBucketsByAccount`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Buckets`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get one or all buckets for a specific tenant. Buckets are accumulators that are related to an accounting script. Buckets can have their values changed with each related accounting entry.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `pageSize` | query | no | integer | Maximum number of accounting event types per page. |  |
| `pageOffset` | query | no | integer | Number to offset page resuts. For example, value `2` returns the third page. Defaults to `0`, which returns the first page. |  |
| `accountId` | query | no | integer | Account ID |  |
| `name` | query | no | string | Bucket name |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Indicates if there are more items to be retrieved. |  |
| `items` | array of object | no | Items retrieved from a given request. |  |
| `items` | array of object (schema `Bucket`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Bucket -->
### Schema `Bucket`

Pointer: `#/components/schemas/Bucket`. Type: object (schema `Bucket`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | Bucket name | example: "bacen_pre_2039" |
| `account` | integer | no | Account ID | format: "int64"; example: 123456 |
| `value` | number | no | Bucket value | example: 100 |
| `updated_at` | string | no | Bucket last updated date | format: "date"; example: "2021-06-26T00:00:00.000Z" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounting.yaml` | tag `Buckets`: GET /v1/buckets | https://github.com/PismoDevEx/pismo-api-specs | `f0272a891eaca0fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
