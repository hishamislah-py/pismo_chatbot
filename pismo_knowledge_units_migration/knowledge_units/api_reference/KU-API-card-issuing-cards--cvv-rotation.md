---
ku_id: KU-API-card-issuing-cards--cvv-rotation
title: 'API reference: Card issuing - Cards — CVV rotation'
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
- post-v2-reset-cvv
- patch-v2-card-change-rotation
- delete-v2-card-delete-rotation
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-cards-overview-1
- KU-EVT-cards-data-events
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — CVV rotation

**KU ID:** `KU-API-card-issuing-cards--cvv-rotation` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `CVV rotation` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> CVV rotation management

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /pcicards/v2/pcicards/cvv/{cardId}/reset` | `post-v2-reset-cvv` | Rotate virtual card CVV | no |
| `PATCH /pcicards/v2/pcicards/cvv/{cardId}/change-rotation` | `patch-v2-card-change-rotation` | Update CVV rotation interval | no |
| `DELETE /pcicards/v2/pcicards/cvv/{cardId}/delete-rotation` | `delete-v2-card-delete-rotation` | Delete CVV card rotation interval | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/pcicards/v2/pcicards/cvv/{cardId}/reset operationId=post-v2-reset-cvv -->
### `POST /pcicards/v2/pcicards/cvv/{cardId}/reset` — Rotate virtual card CVV

- **operationId:** `post-v2-reset-cvv`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `CVV rotation`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Force a virtual card's CVV (Card Verification Value) rotation.
>
> **CVV rotation rules:**
>
> Calling this endpoint can reset the CVV rotation schedule in the future. For example, if you call this endpoint at 3PM and the defined rotation interval is 24 hours, the next rotation will take place at 3PM the next day and subsequent days after.
>
> A 2-minute validation occurs between scheduling requests and, within this interval, no new scheduling takes place. This can lead to the following scenarios:
>
> * If a forced rotation occurs less than 2 minutes after an auto-rotation, the CVV is rotated and no new scheduling takes place.
> * If an auto-rotation occurs less than 2 minutes after a forced rotation, the CVV is rotated and no new scheduling takes place.
> * If more than one forced call occurs in less than 2 minutes, the CVV is rotated, but new scheduling only takes place for the first call.
>
> This endpoint generates a [Card CVV changed](https://developers.pismo.io/events/docs/cards-rotate-cvv-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: yes

> Rotate CVV request body

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `service_code` | string (schema `ServiceCode`) | no | A 3 digit value, not to be confused with the CVV. Each number in the service code has a well-defined meaning, known to the card networks and other components of the interchange networks. The service code's purpose is to tell merchant terminals and acquiring networks about usage restrictions the issuer has placed on the card.<br><br>If passed, a new random service code value is not generated, and the passed value is used instead.<br> | minLength: 3; maxLength: 3 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success CVV rotation response | `application/json`: object (schema `ResetCvvResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `success` | boolean | no | Was CVV rotated? |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-rotate-cvv-1` | https://developers.pismo.io/events/docs/cards-rotate-cvv-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-cards-overview-1`, `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/pcicards/v2/pcicards/cvv/{cardId}/change-rotation operationId=patch-v2-card-change-rotation -->
### `PATCH /pcicards/v2/pcicards/cvv/{cardId}/change-rotation` — Update CVV rotation interval

- **operationId:** `patch-v2-card-change-rotation`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `CVV rotation`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Allows to manage CVV rotation, for example:
>
>   * Set CVV rotation for cards without CVV rotation
>
>   * Increase/decrease CVV rotation interval
>
> A [Card CVV changed](https://developers.pismo.io/events/docs/cards-rotate-cvv-1) event is generated with `operation_type` = `CHANGE_CVV_ROTATION`
>
> **Notes**
>
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: yes

> Update CVV rotation interval request body

**Content type `application/json`** — schema: object (schema `CvvChangeRotationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cvv_rotation_interval_hours` | integer (schema `CvvRotationIntervalHours`) | yes | New CVV rotation interval in hours | minimum: 1; example: 4320 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. (The CVV rotation interval was changed) | `application/json`: object (schema `CvvChangeRotationResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `cvv_rotation_interval_hours` | integer (schema `CvvRotationIntervalHours`) | no | New CVV rotation interval in hours | minimum: 1; example: 4320 |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-rotate-cvv-1` | https://developers.pismo.io/events/docs/cards-rotate-cvv-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=DELETE path=/pcicards/v2/pcicards/cvv/{cardId}/delete-rotation operationId=delete-v2-card-delete-rotation -->
### `DELETE /pcicards/v2/pcicards/cvv/{cardId}/delete-rotation` — Delete CVV card rotation interval

- **operationId:** `delete-v2-card-delete-rotation`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `CVV rotation`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Deletes CVV rotation for cards with active rotation.
>
> A [Card CVV changed](https://developers.pismo.io/events/docs/cards-rotate-cvv-1) event is generated with `operation_type` = `DELETE_CVV_ROTATION`.
>
> **Notes**
> * This endpoint takes an account token - an access token encoded with a Pismo account ID.
> * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content (The CVV rotation was deleted) |  |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-rotate-cvv-1` | https://developers.pismo.io/events/docs/cards-rotate-cvv-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `False`, emits events `1`, deprecated `False`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `CVV rotation`: POST /pcicards/v2/pcicards/cvv/{cardId}/reset, PATCH /pcicards/v2/pcicards/cvv/{cardId}/change-rotation, DELETE /pcicards/v2/pcicards/cvv/{cardId}/delete-rotation | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-cards-overview-1` — Cards management
- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-catalogue-cards` — Event catalogue: cards
