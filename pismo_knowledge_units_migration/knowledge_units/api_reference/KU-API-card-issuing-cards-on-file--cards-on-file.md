---
ku_id: KU-API-card-issuing-cards-on-file--cards-on-file
title: 'API reference: Card issuing - Cards on file — Cards on file'
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
- list-all-cardsonfile-registries
- create-a-cardsonfile
- updates-a-cardsonfile
- list-cardonfile
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-card-on-file-and-automatic-updater
- KU-EVT-cards-data-events
- KU-EVT-catalogue-cardsonfile
specification_version: 2.0.0
---

# API reference: Card issuing - Cards on file — Cards on file

**KU ID:** `KU-API-card-issuing-cards-on-file--cards-on-file` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Cards on file` in `api-specs/Card_issuing_-_Cards_on_file.yaml` (“Card issuing - Cards on file”, version `2.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Cards on file management

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /cardsonfile/v2/cardsonfile/cards` | `list-all-cardsonfile-registries` | Get account cards on file | no |
| `POST /cardsonfile/v2/cardsonfile/cards` | `create-a-cardsonfile` | Create card on file | no |
| `PATCH /cardsonfile/v2/cardsonfile/cards` | `updates-a-cardsonfile` | Update card on file | no |
| `GET /cardsonfile/v2/cardsonfile/cards/{cardid}` | `list-cardonfile` | Get card on file | no |

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=GET path=/cardsonfile/v2/cardsonfile/cards operationId=list-all-cardsonfile-registries -->
### `GET /cardsonfile/v2/cardsonfile/cards` — Get account cards on file

- **operationId:** `list-all-cardsonfile-registries`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Cards on file`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get  all cards on file for a specific account, which is derived from the access token.
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |
| `status` | query | no | string | Card status - `ACTIVE`, `SUSPENDED` or `PENDING`. To filter more than one status, separate with a comma (,)<br> |  |
| `type` | query | no | string | Card type - `PLASTIC`, `VIRTUAL`, `TEMPORARY` or `RECURRING`. To filter more than one type, separate with a comma (,)<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 |  | `application/json`: array of object (schema `CardsOnFileGetResponseModel`) |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=POST path=/cardsonfile/v2/cardsonfile/cards operationId=create-a-cardsonfile -->
### `POST /cardsonfile/v2/cardsonfile/cards` — Create card on file

- **operationId:** `create-a-cardsonfile`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Cards on file`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create a *card on file* - an existing card that has been tokenized and stored in a digital wallet. The token is then used for payment transactions to avoid exposing sensitive data like the card's PAN and CVV.<br>
> The card can be a Pismo-issued card or an external card. The card is added to the customer's digital wallet.<br>
>
> This endpoint generates a [Card on file created](https://developers.pismo.io/events/docs/cardsonfile-provision-1) event.
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `skip_validation` | query | no | boolean | Skip acquirer and anti-fraud validation? Default is `false`. |  |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `CardsOnFileCreate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_name` | string (schema `CardName`) | yes | Card alias name. No limit. | example: "Vacation card" |
| `cvv` | string (schema `CVV`) | yes | Card Verification Code (CVV) (the three numbers behind the card). | example: "564" |
| `expiration_date` | string (schema `CardExpirationDate`) | yes | Card expiration date (mmyy) | example: "1214" |
| `name` | string (schema `CardholderName`) | yes | Cardholder printed name. No limit. | example: "Mabel Syrup" |
| `pan` | string (schema `Pan`) | yes | Primary Account Number (PAN) to store. The PAN shown here is a fictional example used for documentation purposes. It does not represent a real card number.<br> | minLength: 12; maxLength: 19; example: "123456******7890" |
| `acquirer` | string (schema `AcquirerID`) | no | Acquirer ID. | maxLength: 50; example: "289900" |
| `card_profile` | string (schema `CardProfile`) | no | Network card profile identifier or HEX color. A profile or HEX color determines a card's appearance in a mobile payment app or payment system. Issuers are responsible for configuring card profiles with the card network.<br> | example: "0XFFFFFF" |
| `card_stored_uuid` | string (schema `CardStoredUuid`) | no | API-generated card token from registration. This is NOT a field you can change, but it must be passed to identify the card.<br> | example: "uuid-a-1ffff" |
| `default_card` | boolean (schema `DefaultCard`) | no | Is this card the default card? Default is `false`. | example: true |
| `document_number` | string (schema `DocumentNumber`) | no | Cardholder government document number. This can be from any document that identifies the cardholder such as a Tax ID, State ID, or driver's license.<br> | example: "7777888hh" |
| `issuer_card` | boolean (schema `IssuerCard`) | no | Is this the issuer's card? Default is `false`. | example: false |
| `verified` | boolean (schema `Verified`) | no | Is card verified? Default is `false`. | example: false |
| `metadata` | string (schema `Metadata`) | no | Any data object with key/value pairs. No limit on length.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: "{ \\"key\\": \\"value\\"}" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `CardsOnFileRegisterResponse`) |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_stored_uuid` | string (schema `CardStoredUuid`) | no | API-generated card token from registration. This is NOT a field you can change, but it must be passed to identify the card.<br> | example: "uuid-a-1ffff" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cardsonfile-provision-1` | https://developers.pismo.io/events/docs/cardsonfile-provision-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-card-on-file-and-automatic-updater`.

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=PATCH path=/cardsonfile/v2/cardsonfile/cards operationId=updates-a-cardsonfile -->
### `PATCH /cardsonfile/v2/cardsonfile/cards` — Update card on file

- **operationId:** `updates-a-cardsonfile`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Cards on file`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Updates a card on file - change the card name, status, or profile. You must pass the card uuid token as a body parameter to identify the card.
>
> Fields that are not passed are not updated.
>
> This endpoint generates a [Card on file updated](https://developers.pismo.io/events/docs/cardsonfile-patch-cards-1) event. If the card status is being changed to `SUSPENDED`, it also generates a [Card excluded](https://developers.pismo.io/events/docs/cardsonfile-exclusion-1) event.
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `CardsOnFilePatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_stored_uuid` | string (schema `CardStoredUuid`) | yes | API-generated card token from registration. This is NOT a field you can change, but it must be passed to identify the card.<br> | example: "uuid-a-1ffff" |
| `card_name` | string (schema `CardName`) | no | Card alias name. No limit. | example: "Vacation card" |
| `card_profile` | string (schema `CardProfile`) | no | Network card profile identifier or HEX color. A profile or HEX color determines a card's appearance in a mobile payment app or payment system. Issuers are responsible for configuring card profiles with the card network.<br> | example: "0XFFFFFF" |
| `metadata` | string (schema `Metadata`) | no | Any data object with key/value pairs. No limit on length.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: "{ \\"key\\": \\"value\\"}" |
| `status` | string | no | Card-on-file token status - `ACTIVE` or `SUSPENDED`. | enum: ["", "ACTIVE", "SUSPENDED"]; example: "SUSPENDED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | SUCCESS |  |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cardsonfile-exclusion-1` | https://developers.pismo.io/events/docs/cardsonfile-exclusion-1 |
| `cardsonfile-patch-cards-1` | https://developers.pismo.io/events/docs/cardsonfile-patch-cards-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=GET path=/cardsonfile/v2/cardsonfile/cards/{cardid} operationId=list-cardonfile -->
### `GET /cardsonfile/v2/cardsonfile/cards/{cardid}` — Get card on file

- **operationId:** `list-cardonfile`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Cards on file`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get card on file
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardid` | path | yes | string | Card ID |  |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 |  | `application/json`: array of object (schema `CardOnFileResponse`) |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

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
| `api-specs/Card_issuing_-_Cards_on_file.yaml` | tag `Cards on file`: GET /cardsonfile/v2/cardsonfile/cards, POST /cardsonfile/v2/cardsonfile/cards, PATCH /cardsonfile/v2/cardsonfile/cards, GET /cardsonfile/v2/cardsonfile/cards/{cardid} | https://github.com/PismoDevEx/pismo-api-specs | `85cc36fbf4444718…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-card-on-file-and-automatic-updater` — Card-on-file and automatic updater
- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-catalogue-cardsonfile` — Event catalogue: cardsonfile
