---
ku_id: KU-API-card-issuing-cards--mastercard-benefits
title: 'API reference: Card issuing - Cards — Mastercard benefits'
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
- post-v1-benefits-segments-assign
- post-v1-benefits-segments-replace
- post-v1-benefits-segments-cancel
- post-v1-benefits-cards-cancel
- post-v1-benefits-cards-freeze
related_kus:
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Mastercard benefits

**KU ID:** `KU-API-card-issuing-cards--mastercard-benefits` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Mastercard benefits` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card benefits endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /pcicards/v1/pcicards/benefits/segments/assign` | `post-v1-benefits-segments-assign` | Assign card segment | no |
| `PUT /pcicards/v1/pcicards/benefits/segments/replace` | `post-v1-benefits-segments-replace` | Replace card segment and benefits | no |
| `PUT /pcicards/v1/pcicards/benefits/segments/cancel` | `post-v1-benefits-segments-cancel` | Cancel card segment and benefits | no |
| `POST /pcicards/v1/pcicards/benefits/cards/replace` | `post-v1-benefits-cards-cancel` | Replace user card number | no |
| `PUT /pcicards/v1/pcicards/benefits/cards/freeze` | `post-v1-benefits-cards-freeze` | Allow freezing/unfreezing card benefits | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v1/pcicards/benefits/segments/assign operationId=post-v1-benefits-segments-assign -->
### `POST /pcicards/v1/pcicards/benefits/segments/assign` — Assign card segment

- **operationId:** `post-v1-benefits-segments-assign`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Mastercard benefits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Assigns segment to a card. An array of bundles are then assigned to the card. 
>
> A Mastercard card **segment** is a specific cardholder grouping (e.g., premium, business, or travel-focused) that issuers use to allocate tailored benefit bundles such as travel insurance, concierge services, or concierge access to particular cards. These segments allow for personalized, dynamic, and targeted rewards assigned to cardholders via API. 
>
> A Mastercard card segment **bundle** is a targeted package of benefits, rewards, or services assigned to specific carholder groups based on need.
>
> This endpoint generates a [Cards benefits allocation updated](https://developers.pismo.io/events/docs/cards-benefits-allocation-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Assign card segement request body

**Content type `application/json`** — schema: object (schema `Assign`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer (schema `CardID2`) | yes | Pismo card ID | example: 123456 |
| `segments` | array of object (schema `SegmentEffectiveDate`) (schema `AssignSegmentsEffectiveDate`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `BundlesResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bundles` | array of object (schema `Bundle`) (schema `Bundles`) | no | Bundle object array |  |
| `network_correlation_id` | string (schema `NetworkCorrelationId`) | no | Network correlation ID | example: "fe1bf855f651810629107cfbce5b09d2" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-benefits-allocation-1` | https://developers.pismo.io/events/docs/cards-benefits-allocation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/pcicards/v1/pcicards/benefits/segments/replace operationId=post-v1-benefits-segments-replace -->
### `PUT /pcicards/v1/pcicards/benefits/segments/replace` — Replace card segment and benefits

- **operationId:** `post-v1-benefits-segments-replace`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Mastercard benefits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Replaces the segment and existing benefits with a new benefit set assigned via a new segment code. The existing benefits are cancelled, and new benefits are assigned. An array of newly-assigned bundles is returned in the response. 
>
> This endpoint generates a [Cards benefits allocation updated](https://developers.pismo.io/events/docs/cards-benefits-allocation-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Replace card segment and updates request body

**Content type `application/json`** — schema: object (schema `ReplaceBenefit`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer (schema `CardID2`) | yes | Pismo card ID | example: 123456 |
| `old_segment_code` | string (schema `ReplaceOldCode`) | yes | Old segment code | example: "LAC_BBC" |
| `new_segment_code` | string (schema `ReplaceNewCode`) | yes | New segment code | example: "LAC_BBD" |
| `effective_date` | string (schema `EffectiveDate`) | yes | Card effective date. Format = yyyy-mm-dd | example: "2025-07-31" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `BundlesResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bundles` | array of object (schema `Bundle`) (schema `Bundles`) | no | Bundle object array |  |
| `network_correlation_id` | string (schema `NetworkCorrelationId`) | no | Network correlation ID | example: "fe1bf855f651810629107cfbce5b09d2" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-benefits-allocation-1` | https://developers.pismo.io/events/docs/cards-benefits-allocation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/pcicards/v1/pcicards/benefits/segments/cancel operationId=post-v1-benefits-segments-cancel -->
### `PUT /pcicards/v1/pcicards/benefits/segments/cancel` — Cancel card segment and benefits

- **operationId:** `post-v1-benefits-segments-cancel`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Mastercard benefits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancels a segment and the benefits associated to the card for the input segment. The canceled bundle array is returned.
>
> Exactly one input segment is supported at this time. It is defined as an array for future support.
>
> This endpoint generates a [Cards benefits allocation updated](https://developers.pismo.io/events/docs/cards-benefits-allocation-1) event. 
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Cancel card segment and benefits request body

**Content type `application/json`** — schema: object (schema `Cancel`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer (schema `CardID2`) | yes | Pismo card ID | example: 123456 |
| `code` | string (schema `Code`) | yes | Code | example: "LAC_BBC" |
| `expiry_date` | string (schema `ExpiryDate`) | yes | Card expiration date. Format = yyyy-dd-mm | example: "2026-01-20" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `BundlesResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bundles` | array of object (schema `Bundle`) (schema `Bundles`) | no | Bundle object array |  |
| `network_correlation_id` | string (schema `NetworkCorrelationId`) | no | Network correlation ID | example: "fe1bf855f651810629107cfbce5b09d2" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-benefits-allocation-1` | https://developers.pismo.io/events/docs/cards-benefits-allocation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v1/pcicards/benefits/cards/replace operationId=post-v1-benefits-cards-cancel -->
### `POST /pcicards/v1/pcicards/benefits/cards/replace` — Replace user card number

- **operationId:** `post-v1-benefits-cards-cancel`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Mastercard benefits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Replaces user card number associated. The old card benefits are cancelled, and the same benefit set is applied to the new card.
>
> This endpoint generates a [Cards benefits allocation updated](https://developers.pismo.io/events/docs/cards-benefits-allocation-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-customer-id` | header | yes | integer | Pismo customer ID | example: 125555 |

#### Request body

Required: yes

> Replace user card number request body

**Content type `application/json`** — schema: object (schema `ReplaceCard`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `old_card_id` | integer (schema `ReplaceOldCardID`) | yes | Pismo old card ID | example: 123456 |
| `new_card_id` | integer (schema `ReplaceNewCardID`) | yes | Pismo new card ID | example: 987654 |
| `effective_date` | string (schema `EffectiveDate`) | yes | Card effective date. Format = yyyy-mm-dd | example: "2025-07-31" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `BundlesResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bundles` | array of object (schema `Bundle`) (schema `Bundles`) | no | Bundle object array |  |
| `network_correlation_id` | string (schema `NetworkCorrelationId`) | no | Network correlation ID | example: "fe1bf855f651810629107cfbce5b09d2" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-benefits-allocation-1` | https://developers.pismo.io/events/docs/cards-benefits-allocation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/pcicards/v1/pcicards/benefits/cards/freeze operationId=post-v1-benefits-cards-freeze -->
### `PUT /pcicards/v1/pcicards/benefits/cards/freeze` — Allow freezing/unfreezing card benefits

- **operationId:** `post-v1-benefits-cards-freeze`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Mastercard benefits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Allows freezing or unfreezing a card for benefits.
>
> This endpoint generates a [Cards benefits allocation updated](https://developers.pismo.io/events/docs/cards-benefits-allocation-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Allow freezing/unfreezing card benefits request body

**Content type `application/json`** — schema: object (schema `Freeze`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | integer (schema `CardID2`) | yes | Pismo card ID | example: 123456 |
| `freezing_enabled` | boolean (schema `FreezingEnabled`) | yes | Is freezing enabled? | example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-benefits-allocation-1` | https://developers.pismo.io/events/docs/cards-benefits-allocation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SegmentEffectiveDate -->
### Schema `SegmentEffectiveDate`

Pointer: `#/components/schemas/SegmentEffectiveDate`. Type: object (schema `SegmentEffectiveDate`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `Code`) | no | Code | example: "LAC_BBC" |
| `effective_date` | string (schema `EffectiveDate`) | no | Card effective date. Format = yyyy-mm-dd | example: "2025-07-31" |

<!-- schema: #/components/schemas/Bundle -->
### Schema `Bundle`

Pointer: `#/components/schemas/Bundle`. Type: object (schema `Bundle`).

> Bundle object. A Mastercard card segment **bundle** is a targeted package of benefits, rewards, or services assigned to specific carholder groups based on need.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `Code`) | no | Code | example: "LAC_BBC" |
| `effective_date` | string (schema `EffectiveDate`) | no | Card effective date. Format = yyyy-mm-dd | example: "2025-07-31" |
| `expiry_date` | string (schema `ExpiryDate`) | no | Card expiration date. Format = yyyy-dd-mm | example: "2026-01-20" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Mastercard benefits`: POST /pcicards/v1/pcicards/benefits/segments/assign, PUT /pcicards/v1/pcicards/benefits/segments/replace, PUT /pcicards/v1/pcicards/benefits/segments/cancel, POST /pcicards/v1/pcicards/benefits/cards/replace, PUT /pcicards/v1/pcicards/benefits/cards/freeze | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-cards` — Event catalogue: cards
