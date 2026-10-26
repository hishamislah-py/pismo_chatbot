---
ku_id: KU-API-card-issuing-cards--migration
title: 'API reference: Card issuing - Cards — Migration'
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
- patch-migrate-card
- patch-migrate-card-mode
related_kus:
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Migration

**KU ID:** `KU-API-card-issuing-cards--migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Migration` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Migrate card and card modes

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PATCH /wallet/v2/cards/{cardId}/program-migration` | `patch-migrate-card` | Migrate card to different program [beta] | no |
| `PATCH /wallet/v2/cards/{cardId}/mode/{modeId}/program-migration` | `patch-migrate-card-mode` | Migrate card mode [beta] | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/wallet/v2/cards/{cardId}/program-migration operationId=patch-migrate-card -->
### `PATCH /wallet/v2/cards/{cardId}/program-migration` — Migrate card to different program [beta]

- **operationId:** `patch-migrate-card`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Migration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Migrate a card to a different program. It is possible to migrate from a Zero balance program to a Full balance program and vice-versa.
>
> This endpoint generates two events:
>
>   * [Card can be added to next scheduled embossing](https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1) event containing the field `operation_type` = `CARD_PROGRAM_MIGRATION` if the card has not yet been embossed.
>
>   * [Card migrated](https://developers.pismo.io/events/docs/cards-migration-1) event. 
>
> **Notes:** 
>
>    * This endpoint **REQUIRES** an account token - an access token encoded with a Pismo account ID.
>
>    * For combination cards, this endpoint migrates the [card mode](doc:cards-overview-1#create-a-combination-card-with-card-modes) the card was originally created with. To migrate the secondary mode, call the [Migrate card mode](ref:patch-migrate-card-mode) endpoint.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `MigrateCardToProgramRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `new_program_id` | integer (schema `ProgramID`) | yes | Pismo program ID | example: 7654 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success |  |
| 400 | Bad Request, missing customer ID or program ID |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 406 | Not accepetable |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-embossing-card-ingress-1` | https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1 |
| `cards-migration-1` | https://developers.pismo.io/events/docs/cards-migration-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;406;500`, has examples `False`, emits events `2`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/wallet/v2/cards/{cardId}/mode/{modeId}/program-migration operationId=patch-migrate-card-mode -->
### `PATCH /wallet/v2/cards/{cardId}/mode/{modeId}/program-migration` — Migrate card mode [beta]

- **operationId:** `patch-migrate-card-mode`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Migration`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Migrate a [card's mode](doc:cards-overview-1#create-a-combination-card-with-card-modes) to a different program.
>
> Migrate a card's secondary mode (debit or credit) to a new program. If a combination card is initially created with a credit account (has a `CREDIT` mode), it gets migrated when the [Migrate card to different program](ref:patch-migrate-card) endpoint is called. However, if you wish to migrate the debit (secondary) mode, you need to call this endpoint. 
>
> This endpoint generates a [Card migrated](https://developers.pismo.io/events/docs/cards-migration-1) event. 
>
> **Note:** This endpoint **REQUIRES** an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `modeId` | path | yes | string | Card mode ID. For more information, refer to [Create a combination card with card modes](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#create-a-combination-card-with-card-modes).<br> | example: "348909874dfddf" |

#### Request body

Required: yes

> Migrate card mode request body

**Content type `application/json`** — schema: object (schema `MigrateCardToProgramRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `new_program_id` | integer (schema `ProgramID`) | yes | Pismo program ID | example: 7654 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Success |  |
| 400 | Bad Request, missing customer ID or program ID |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 406 | Not accepetable |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-migration-1` | https://developers.pismo.io/events/docs/cards-migration-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;406;500`, has examples `False`, emits events `1`, deprecated `False`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Migration`: PATCH /wallet/v2/cards/{cardId}/program-migration, PATCH /wallet/v2/cards/{cardId}/mode/{modeId}/program-migration | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-cards` — Event catalogue: cards
