---
ku_id: KU-API-card-issuing-cards--automatic-updater
title: 'API reference: Card issuing - Cards — Automatic updater'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Cards.yaml
  sha256: 687df76f123e41a762721ae0b3fe344c701d22f47bdd929d033b1ad2d14ca406
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
- post-vau-opt-in
- post-vau-opt-out
related_kus:
- KU-CARD-card-on-file-and-automatic-updater
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Automatic updater

**KU ID:** `KU-API-card-issuing-cards--automatic-updater` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Automatic updater` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for Visa's VAU and Mastercard's ABU

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /cards/v1/automatic-updater/{cardID}/opt-in` | `post-vau-opt-in` | Visa automatic updater opt-in | no |
| `POST /cards/v1/automatic-updater/{cardID}/opt-out` | `post-vau-opt-out` | Automatic updater opt-out | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/cards/v1/automatic-updater/{cardID}/opt-in operationId=post-vau-opt-in -->
### `POST /cards/v1/automatic-updater/{cardID}/opt-in` — Visa automatic updater opt-in

- **operationId:** `post-vau-opt-in`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Automatic updater`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Opt a card in to Visa Automatic Updater (VAU).
>
> This entry is processed during the next file generation window and be sent to the network. 
>
> This endpoint generates an [Automatic Updater notification file sent](https://developers.pismo.io/events/docs/cards-automatic-updater-1) event.
>
> For more information, refer to the [Automatic updater](doc:automatic-updater) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardID` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success or failure |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-automatic-updater-1` | https://developers.pismo.io/events/docs/cards-automatic-updater-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-on-file-and-automatic-updater`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/cards/v1/automatic-updater/{cardID}/opt-out operationId=post-vau-opt-out -->
### `POST /cards/v1/automatic-updater/{cardID}/opt-out` — Automatic updater opt-out

- **operationId:** `post-vau-opt-out`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Automatic updater`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Opt out of Visa Automatic Updater (VAU) or Mastercard's Automatic Billing Updater (ABU).
>
> This entry is processed during the next file generation window and be sent to the network. 
>
> This endpoint generates an [Automatic Updater notification file sent](https://developers.pismo.io/events/docs/cards-automatic-updater-1) event.
>
> For more information, refer to the [Automatic updater](doc:automatic-updater) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardID` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success or failure |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-automatic-updater-1` | https://developers.pismo.io/events/docs/cards-automatic-updater-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-on-file-and-automatic-updater`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Automatic updater`: POST /cards/v1/automatic-updater/{cardID}/opt-in, POST /cards/v1/automatic-updater/{cardID}/opt-out | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-card-on-file-and-automatic-updater` — Card-on-file and automatic updater
- `KU-EVT-catalogue-cards` — Event catalogue: cards
