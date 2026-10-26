---
ku_id: KU-API-migrations--fee-model-migration
title: 'API reference: Migrations — Fee model migration'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Migrations.yaml
  sha256: 7478abcca92f0932e27157e9dc1cb8c0459b9c128cf72428de43092c903cd59a
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
- PostFeeModelV1
related_kus:
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Fee model migration

**KU ID:** `KU-API-migrations--fee-model-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Fee model migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Fee model migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/fee-model-account` | `PostFeeModelV1` | Migrate account fee models | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/fee-model-account operationId=PostFeeModelV1 -->
### `POST /v1/migrations/fee-model-account` — Migrate account fee models

- **operationId:** `PostFeeModelV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Fee model migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of **fee models** that are [linked to customer accounts](ref:attachmentbyaccount). (A [fee model](doc:fee-model) links a collection of fees to an account.)
>
> This endpoint generates the following events:
> - [Fee model account migration started](https://developers.pismo.io/events/docs/migration-fee-model-account-incoming-1)
> - [Fee model account migration completed](https://developers.pismo.io/events/docs/migration-fee-model-account-outgoing-1)

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `FeeModelAccountV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Migration information for the account fee model being migrated |  |
| `migration.id` | string | yes | Record ID for migration purposes. | pattern: "^[a-zA-Z0-9-._]+$"; maxLength: 255; example: "a-unique-migration-id" |
| `migration.account_ids` | array of string | yes | List of migration IDs for the accounts to which the fee model is attached (should be the same migration IDs used on account migration). | minItems: 1; maxItems: 512; items.pattern: "^[a-zA-Z0-9-._]+$"; items.maxLength: 255 |
| `fee_model_id` | string | yes | Fee model ID | format: "uuid"; example: "f47ac10b-58cc-4372-a567-0e02b2c3d479" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successful migration initiation | `application/json`: object |
| 400 | Invalid request | `application/json`: object |
| 500 | Internal server error | `application/json`: object |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string | no |  | example: "Migration initiated" |
| `migration_id` | string | no |  | example: "abc123" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `migration-fee-model-account-incoming-1` | https://developers.pismo.io/events/docs/migration-fee-model-account-incoming-1 |
| `migration-fee-model-account-outgoing-1` | https://developers.pismo.io/events/docs/migration-fee-model-account-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `2`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.


## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Migrations.yaml` | tag `Fee model migration`: POST /v1/migrations/fee-model-account | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-migration` — Event catalogue: migration
