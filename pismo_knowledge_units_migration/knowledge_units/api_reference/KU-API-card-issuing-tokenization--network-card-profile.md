---
ku_id: KU-API-card-issuing-tokenization--network-card-profile
title: 'API reference: Card issuing - Tokenization — Network card profile'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Tokenization.yaml
  sha256: dd1e776cfe20b0d67cfcc866bc3663b044f224c72ea9b70658facb672666a03e
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
- get-v1-cards-card-id-network-tokens-profile
- put-v1-cards-card-id-network-tokens-profile
- post-v1-cards-card-id-network-tokens-profile
related_kus:
- KU-CARD-card-tokenization-process-and-onboarding
- KU-CC-cards
- KU-ERR-codes-acq-to-esma
specification_version: 1.0.0
---

# API reference: Card issuing - Tokenization — Network card profile

**KU ID:** `KU-API-card-issuing-tokenization--network-card-profile` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Network card profile` in `api-specs/Card_issuing_-_Tokenization.yaml` (“Card issuing - Tokenization”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Network card profile endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/cards/{cardId}/network-tokens/profile` | `get-v1-cards-card-id-network-tokens-profile` | Get network card profile | no |
| `PUT /v1/cards/{cardId}/network-tokens/profile` | `put-v1-cards-card-id-network-tokens-profile` | Update network card profile | no |
| `POST /v1/cards/{cardId}/network-tokens/profile` | `post-v1-cards-card-id-network-tokens-profile` | Assign network card profile | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a "**401 Unauthorized**" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=GET path=/v1/cards/{cardId}/network-tokens/profile operationId=get-v1-cards-card-id-network-tokens-profile -->
### `GET /v1/cards/{cardId}/network-tokens/profile` — Get network card profile

- **operationId:** `get-v1-cards-card-id-network-tokens-profile`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Network card profile`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets the card's associated network card profile identifier.
>
> **Notes**:
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>  * This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `NetworkCardProfileObject`) |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_card_profile` | string (schema `NetworkCardProfile`) | yes | Network card profile that you, the issuer, have already configured with the card network. |  |
| `update_previous_tokens` | boolean | no | Should previously issued tokens on the network be updated?  **ONLY** for VISA and Mastercard. Default is `false`. | default: false |

200 Example `example-1`:

```json
{
  "network_card_profile": "XYZ-123"
}
```

##### Response 400

400 Example `example-1`:

```json
{
  "error_code": "ERR93836",
  "message": "Card profile can't be null"
}
```

##### Response 401

401 Example `example-1`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example-1`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR93836` | Card profile can't be null |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=PUT path=/v1/cards/{cardId}/network-tokens/profile operationId=put-v1-cards-card-id-network-tokens-profile -->
### `PUT /v1/cards/{cardId}/network-tokens/profile` — Update network card profile

- **operationId:** `put-v1-cards-card-id-network-tokens-profile`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Network card profile`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update an existing network card profile with a different one. This affects the display at the next tokenization (after deleting the token and creating another one).
>
> **Notes**:
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>  * This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `NetworkCardProfileObject`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_card_profile` | string (schema `NetworkCardProfile`) | yes | Network card profile that you, the issuer, have already configured with the card network. |  |
| `update_previous_tokens` | boolean | no | Should previously issued tokens on the network be updated?  **ONLY** for VISA and Mastercard. Default is `false`. | default: false |

Example `example-1`:

```json
{
  "network_card_profile": "XYZ-123"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 400

400 Example `example-1`:

```json
{
  "error_code": "ERR93836",
  "message": "Card profile can't be null"
}
```

##### Response 401

401 Example `example-1`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example-1`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR93836` | Card profile can't be null |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/cards/{cardId}/network-tokens/profile operationId=post-v1-cards-card-id-network-tokens-profile -->
### `POST /v1/cards/{cardId}/network-tokens/profile` — Assign network card profile

- **operationId:** `post-v1-cards-card-id-network-tokens-profile`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Network card profile`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Binds a network card profile to specified card. Pass the network profile identifier as a string. The network card profile determines such things as how the card is visually displayed in a mobile payment app. As the issuer, you need to configure network profiles with the card network.
>
> **Notes**:
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io/cards-tokenization environment.
>  * This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `NetworkCardProfileObject`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_card_profile` | string (schema `NetworkCardProfile`) | yes | Network card profile that you, the issuer, have already configured with the card network. |  |
| `update_previous_tokens` | boolean | no | Should previously issued tokens on the network be updated?  **ONLY** for VISA and Mastercard. Default is `false`. | default: false |

Example `example-1`:

```json
{
  "network_card_profile": "XYZ-123"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `ErrorObject`) |
| 401 | Access token is missing or invalid | `application/json`: object (schema `ErrorObject`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorObject`) |

##### Response 400

400 Example `example-1`:

```json
{
  "error_code": "ERR93836",
  "message": "Card profile can't be null"
}
```

##### Response 401

401 Example `example-1`:

```json
{
  "error_code": "ERR9786",
  "message": "Access token is missing or invalid"
}
```

##### Response 500

500 Example `example-1`:

```json
{
  "error_code": "ERR5446",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERR93836` | Card profile can't be null |
| 401 | `ERR9786` | Access token is missing or invalid |
| 500 | `ERR5446` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-card-tokenization-process-and-onboarding`, `KU-CC-cards`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorObject -->
### Schema `ErrorObject`

Pointer: `#/components/schemas/ErrorObject`. Type: object (schema `ErrorObject`).

> Standard error object

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
| `api-specs/Card_issuing_-_Tokenization.yaml` | tag `Network card profile`: GET /v1/cards/{cardId}/network-tokens/profile, PUT /v1/cards/{cardId}/network-tokens/profile, POST /v1/cards/{cardId}/network-tokens/profile | https://github.com/PismoDevEx/pismo-api-specs | `dd1e776cfe20b0d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-card-tokenization-process-and-onboarding` — Card tokenization process and onboarding
- `KU-CC-cards` — Control Center cards: card information and card network tokenization
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
