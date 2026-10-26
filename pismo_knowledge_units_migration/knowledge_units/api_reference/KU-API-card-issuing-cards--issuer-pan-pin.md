---
ku_id: KU-API-card-issuing-cards--issuer-pan-pin
title: 'API reference: Card issuing - Cards — Issuer PAN/PIN'
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
- put-v1-update-pan-nominal
- put-v1-update-pan-noname
related_kus:
- KU-CARD-cards-overview-1
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Issuer PAN/PIN

**KU ID:** `KU-API-card-issuing-cards--issuer-pan-pin` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Issuer PAN/PIN` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> For issuer-defined PIN and PIN endpoints.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PUT /pcicards/v1/pcicards/cards/{cardId}/pan` | `put-v1-update-pan-nominal` | Update nominal card PAN/PIN [beta] | no |
| `PUT /pcicards/v1/pcicards/cards/noname/{cardId}/pan` | `put-v1-update-pan-noname` | Update noname card PAN/PIN [beta] | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/pcicards/v1/pcicards/cards/{cardId}/pan operationId=put-v1-update-pan-nominal -->
### `PUT /pcicards/v1/pcicards/cards/{cardId}/pan` — Update nominal card PAN/PIN [beta]

- **operationId:** `put-v1-update-pan-nominal`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Issuer PAN/PIN`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a nominal `UNNUMBERED` card's Primary Account Number (PAN) and, optionally, Personal Identification Number (PIN). 
>
> `UNNUMBERED` cards are created without a Pismo platform-generated PAN and PIN.
>
> This endpoint uses AES256 with the GCM mode. AES-256 GCM is an authenticated encryption mode that uses the Advanced Encryption Standard (AES) with a 256-bit key in Galois/Counter Mode (GCM) to provide both confidentiality and integrity for data. In AES, an initialization vector (IV) is a fixed-size, non-secret randomized number used alongside the secret key to jumpstart the encryption process. The caller is responsible for generating the IV.  The Additional Authenticated Data (AAD) parameter used is the organization/tenant ID. AAD, in AES-GCM, is unencrypted data that is authenticated alongside the ciphertext to ensure the message's integrity and authenticity.
>
> **Notes:**
>
>  * To set up encryption for this endpoint, contact your Pismo representative.
>
>  * This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.
>
>  * This endpoint generates a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event with `operation_type` = `PAN_UPDATE`.
>
> For more information, refer to [Issuer-defined PAN/PIN](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#issuer-defined-panpin).
>

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdatePanBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pan` | object (schema `PanObjectUpdatePan`) | yes | PAN update object |  |
| `pin` | object (schema `PinObjectUpdatePan`) | no | PIN update object. If passed, either `pinblock` or `pin_length` is **REQUIRED**. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 406 | Not accepetable |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;406;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-cards-overview-1`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/pcicards/v1/pcicards/cards/noname/{cardId}/pan operationId=put-v1-update-pan-noname -->
### `PUT /pcicards/v1/pcicards/cards/noname/{cardId}/pan` — Update noname card PAN/PIN [beta]

- **operationId:** `put-v1-update-pan-noname`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Issuer PAN/PIN`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

>
> Update a noname `UNNUMBERED` card's Primary Account Number (PAN) and, optionally, Personal Identification Number (PIN). 
>
> `UNNUMBERED` cards are created without a Pismo platform-generated PAN and PIN.
>
> This endpoint uses AES256 with the GCM mode. AES-256 GCM is an authenticated encryption mode that uses the Advanced Encryption Standard (AES) with a 256-bit key in Galois/Counter Mode (GCM) to provide both confidentiality and integrity for data. In AES, an initialization vector (IV) is a fixed-size, non-secret randomized number used alongside the secret key to jumpstart the encryption process. The caller is responsible for generating the IV.  The Additional Authenticated Data (AAD) parameter used is the organization/tenant ID. AAD, in AES-GCM, is unencrypted data that is authenticated alongside the ciphertext to ensure the message's integrity and authenticity.
>
> To set up encryption for this endpoint, contact your Pismo representative.
>
> This endpoint generates a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event with `operation_type` = `PAN_UPDATE`.
>
> For more information, refer to [Issuer-defnined PAN/PIN](doc:cards-overview-1#issuer-defined-panpin).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdatePanBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pan` | object (schema `PanObjectUpdatePan`) | yes | PAN update object |  |
| `pin` | object (schema `PinObjectUpdatePan`) | no | PIN update object. If passed, either `pinblock` or `pin_length` is **REQUIRED**. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 406 | Not accepetable |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;406;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-cards-overview-1`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/PanObjectUpdatePan -->
### Schema `PanObjectUpdatePan`

Pointer: `#/components/schemas/PanObjectUpdatePan`. Type: object (schema `PanObjectUpdatePan`).

> PAN update object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bin` | string (schema `BIN`) | yes | Bank Identification Number (BIN). A 6 or 8 digit number identitying the card network, issuer, and product. | example: "87634277" |
| `data` | string (schema `PANencrypted`) | yes | Primary Account Number (PAN) encrypted with AES/GCM/NoPadding algorithm. The ciphertext (PAN encryption result) is **REQUIRED** to be base64 encoded.<br> | example: "/5yGTkBSoqGY+Ug5yJuHUSGk54VRMNoY0G5Ni2HSa64=" |
| `key_id` | string (schema `KeyID`) | yes | Key ID used for encryption. To obtain the `key_id`, the sender will generate a symmetric key (AES), encrypt this key with an asymmetric key (public_key) and send it via secure email to the security team. <br><br>To obtain the asymmetric key, you must open a Configuration item for the Cards squad. After the Pismo security team registers the symmetric key, the `key_id` is shared with the issuer.<br> | example: "5c09cda4-8153-11ed-a1eb-0242ac120002" |
| `iv` | string (schema `InitializationVector`) | yes | Array initialization vector, used as a initial state for the AES algorithm. This field is used on the requester side to encrypt the PAN. It must be an random array of 16 bytes of length encoded as base64<br> | example: "ZZ3cUcotvQeaGciyLZb1wA==" |

<!-- schema: #/components/schemas/PinObjectUpdatePan -->
### Schema `PinObjectUpdatePan`

Pointer: `#/components/schemas/PinObjectUpdatePan`. Type: object (schema `PinObjectUpdatePan`).

> PIN update object. If passed, either `pinblock` or `pin_length` is **REQUIRED**.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pinblock` | string (schema `PinBlock`) | no | PINBlocks are 64-bit strings that encode a PIN ready for encryption and secure transmission in banking networks. It contains both the PIN and additional data needed to encrypt it for transmission. The PIN block is typically encrypted using a secure cryptographic algorithm to prevent unauthorized access or tampering during transmission. <br> |  |
| `pin_length` | string (schema `PinLengthString`) | no | PIN length. <br><br>Either `pinblock` or `pin_length` is **REQUIRED**. If `pinblock` is not passed, Pismo will generate a random PIN. <br> | enum: ["4", "6"]; example: "4" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Issuer PAN/PIN`: PUT /pcicards/v1/pcicards/cards/{cardId}/pan, PUT /pcicards/v1/pcicards/cards/noname/{cardId}/pan | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-cards-overview-1` — Cards management
- `KU-EVT-catalogue-cards` — Event catalogue: cards
