---
ku_id: KU-API-card-issuing-cards-on-file--metadata
title: 'API reference: Card issuing - Cards on file — Metadata'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Cards_on_file.yaml
  sha256: 85cc36fbf4444718a9f47cfc8ca9030639e42ef5a52184fd568fe4ed43d31681
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
- delete-a-metadata-field-for-a-given-card
related_kus:
- KU-EVT-catalogue-cardsonfile
specification_version: 2.0.0
---

# API reference: Card issuing - Cards on file — Metadata

**KU ID:** `KU-API-card-issuing-cards-on-file--metadata` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Metadata` in `api-specs/Card_issuing_-_Cards_on_file.yaml` (“Card issuing - Cards on file”, version `2.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Delete card on file metadata

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `DELETE /cardsonfile/v2/cardsonfile/cards/{uuid}/metadata` | `delete-a-metadata-field-for-a-given-card` | Delete card metadata | no |

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=DELETE path=/cardsonfile/v2/cardsonfile/cards/{uuid}/metadata operationId=delete-a-metadata-field-for-a-given-card -->
### `DELETE /cardsonfile/v2/cardsonfile/cards/{uuid}/metadata` — Delete card metadata

- **operationId:** `delete-a-metadata-field-for-a-given-card`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Metadata`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Deletes card metadata.
>
> This endpoint generates a [Card metadata deleted](https://developers.pismo.io/events/docs/cardsonfile-delete-metadata-1) event.
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `uuid` | path | yes | string | Card UUID (token) to validate. |  |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cardsonfile-delete-metadata-1` | https://developers.pismo.io/events/docs/cardsonfile-delete-metadata-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;500`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/CardsOnFileErrorResponse -->
### Schema `CardsOnFileErrorResponse`

Pointer: `#/components/schemas/CardsOnFileErrorResponse`. Type: object (schema `CardsOnFileErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards_on_file.yaml` | tag `Metadata`: DELETE /cardsonfile/v2/cardsonfile/cards/{uuid}/metadata | https://github.com/PismoDevEx/pismo-api-specs | `85cc36fbf4444718…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-cardsonfile` — Event catalogue: cardsonfile
