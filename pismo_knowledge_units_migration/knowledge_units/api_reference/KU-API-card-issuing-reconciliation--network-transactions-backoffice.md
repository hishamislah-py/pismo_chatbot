---
ku_id: KU-API-card-issuing-reconciliation--network-transactions-backoffice
title: 'API reference: Card issuing - Reconciliation — Network transactions backoffice'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Reconciliation.yaml
  sha256: 757d9f2502ab0b648b88b28e40a22f94faf673610eb8e2dc13a3423563a2566d
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
- performClearingReconciliation
related_kus:
- KU-CARD-authorization-events
- KU-CARD-clearing
specification_version: 1.0.0
---

# API reference: Card issuing - Reconciliation — Network transactions backoffice

**KU ID:** `KU-API-card-issuing-reconciliation--network-transactions-backoffice` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Network transactions backoffice` in `api-specs/Card_issuing_-_Reconciliation.yaml` (“Card issuing - Reconciliation”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Network transactions backoffice related endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/clearing-reconciliation` | `performClearingReconciliation` | Perform clearing reconciliation | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Reconciliation.yaml method=POST path=/v1/clearing-reconciliation operationId=performClearingReconciliation -->
### `POST /v1/clearing-reconciliation` — Perform clearing reconciliation

- **operationId:** `performClearingReconciliation`
- **Specification:** `api-specs/Card_issuing_-_Reconciliation.yaml` (Card issuing - Reconciliation)
- **Server base URL(s):** `https://sandbox.pismolabs.io/network-transactions-backoffice-api`
- **Tags:** `Network transactions backoffice`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Perform clearing reconciliation using the provided clearing message. The clearing message must be pending to enable reprocessing.

#### Request body

Required: yes

> Clearing reconciliation request

**Content type `application/json`** — schema: object (schema `ReconciliationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_network` | string | yes | Card network | example: "valid card network" |
| `card_hash` | string | yes | Card hash | example: "valid card hash" |
| `reconciliation_reason` | string | yes | Reason for reconciliation | example: "valid reason" |
| `adjustments` | array of object | no |  |  |
| `adjustments[].field` | string | no | Field to be adjusted | example: "valid field" |
| `adjustments[].new_value` | string | no | New value for the field | example: "valid field value" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Reconciliation response | `application/json`: object (schema `ReconciliationResponse`) |
| 400 | The request is not acceptable, the syntax is malformed, for example, some type number parameter with a text content. | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost | `application/json`: object (schema `ErrorResponse`) |
| 404 | The specified resource was not found. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error. | `application/json`: object (schema `ErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Success message | example: "The message has been received and is being processed." |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-authorization-events`, `KU-CARD-clearing`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Error code | example: "BTN0000" |
| `message` | string | yes | Error message | example: "Validation error: Test message" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Reconciliation.yaml` | tag `Network transactions backoffice`: POST /v1/clearing-reconciliation | https://github.com/PismoDevEx/pismo-api-specs | `757d9f2502ab0b64…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-authorization-events` — Authorization events
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
