---
ku_id: KU-API-card-issuing-cards--modes
title: 'API reference: Card issuing - Cards — Modes'
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
operations:
- get-v1-card-mode
- post-v1-card-mode
- put-v1-card-mode-status
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-cards-overview-1
- KU-CORE-migrations-overview
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Modes

**KU ID:** `KU-API-card-issuing-cards--modes` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Modes` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card mode endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /wallet/v2/cards/{cardId}/modes` | `get-v1-card-mode` | Get card modes | no |
| `POST /wallet/v2/cards/{cardId}/modes` | `post-v1-card-mode` | Add card mode | no |
| `PUT /wallet/v2/cards/{cardId}/modes/{modeId}/status` | `put-v1-card-mode-status` | Change card mode status | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=GET path=/wallet/v2/cards/{cardId}/modes operationId=get-v1-card-mode -->
### `GET /wallet/v2/cards/{cardId}/modes` — Get card modes

- **operationId:** `get-v1-card-mode`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Modes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get card mode objects. A card can have both a credit and debit *mode*, meaning it can be used as both a credit or debit card. Each mode is associated with a credit or debit program and account. 
> For more information, refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Cards overview guide.
>
> NOTE: This endpoint requires an account-specific access token - a token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Cards relationship information | `application/json`: array of object (schema `GetCardModeResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 409 | You already have a card with this type and name active |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-cards-overview-1`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/wallet/v2/cards/{cardId}/modes operationId=post-v1-card-mode -->
### `POST /wallet/v2/cards/{cardId}/modes` — Add card mode

- **operationId:** `post-v1-card-mode`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Modes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Add mode to specified card to make it a combination card. A card can have both a credit and debit *mode*, meaning it can be used as both a credit or debit card. Each mode is associated with a credit or debit program and account. 
>
> The mode and program/account to be added is derived from the access token which **must** be an account-specific access token.
> For more information, refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Cards overview guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Add card mode success response | `application/json`: object (schema `AddCardModeResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 409 | You already have a card with this type and name active |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `mode_id` | integer | no | Mode ID | example: 128876 |
| `mode` | string | no |  | enum: ["DEBIT", "CREDIT"]; example: "CREDIT" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-cards-overview-1`, `KU-CORE-migrations-overview`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/wallet/v2/cards/{cardId}/modes/{modeId}/status operationId=put-v1-card-mode-status -->
### `PUT /wallet/v2/cards/{cardId}/modes/{modeId}/status` — Change card mode status

- **operationId:** `put-v1-card-mode-status`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Modes`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Change card mode status (active or suspended). A card can have both a credit and debit *mode*, meaning it can have both a credit and debit account. Each mode is associated with a credit or debit program and account.
>
> For more information, refer to the [mode documentation](doc:cards-overview-1#create-a-combination-card-with-card-modes) in the Cards overview guide.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `modeId` | path | yes | string | Card mode ID. For more information, refer to [Create a combination card with card modes](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#create-a-combination-card-with-card-modes).<br> | example: "348909874dfddf" |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |

#### Request body

Required: yes

> Change card mode request body

**Content type `application/json`** — schema: object (schema `UpdateCardModeStatusBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string | no | Status descriptions:<br> * `ACTIVE` - Status when card is created<br> * `SUSPENDED` - Cannot perform actions like authorization or tokenization flow<br> | enum: ["ACTIVE", "SUSPENDED"]; example: "SUSPENDED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Status updated |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 409 | You already have a card with this type and name active |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-cards-overview-1`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Modes`: GET /wallet/v2/cards/{cardId}/modes, POST /wallet/v2/cards/{cardId}/modes, PUT /wallet/v2/cards/{cardId}/modes/{modeId}/status | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-cards-overview-1` — Cards management
- `KU-CORE-migrations-overview` — Migrations
