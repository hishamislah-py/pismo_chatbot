---
ku_id: KU-API-card-issuing-cards--card-validity
title: 'API reference: Card issuing - Cards — Card validity'
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
- patch-v2-card-validity-renew
- delete-v2-card-validity
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-cards-overview-1
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Card validity

**KU ID:** `KU-API-card-issuing-cards--card-validity` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Card validity` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage card validity period.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PATCH /wallet/v2/cards/{cardId}/validity/renew` | `patch-v2-card-validity-renew` | Renew card validity | no |
| `DELETE /wallet/v2/cards/{cardId}/validity` | `delete-v2-card-validity` | Delete card validity period | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/wallet/v2/cards/{cardId}/validity/renew operationId=patch-v2-card-validity-renew -->
### `PATCH /wallet/v2/cards/{cardId}/validity/renew` — Renew card validity

- **operationId:** `patch-v2-card-validity-renew`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card validity`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Renew a card's validity period in hours. 
>
> Renewal can be done for `VIRTUAL` cards and activated `PLASTIC` cards that were created or reissued with the `validity_period_hours` field set to a defined value greater than zero.
>
> When a card reaches its `valid_until` date, the card's status is set to `INOPERATIVE`. When this happens, a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event is generated.
>
> For existing cards that never had `validity_period_hours` defined, you can do it through this endpoint.
>
> When the card is renewed: 
>
>   * A new `valid_until` date is calculated and a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event is generated with `operation type` =  `CARD_VALIDITY_RENEWAL`.
>
>   * If the card's status is `INOPERATIVE`, the status changes to `NORMAL`.
>
>   * If the card's status is `NORMAL`, `REISSUED`, `BLOCKED`, `PENDING` or `WARNING`, the status remains the same. 
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error message. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `CardsValidityRenewBody`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `validity_period_hours` | integer (schema `ValidityPeriodHours2`) | yes | Sets a card's validity period in hours. Cannot exceed the card's `expiration_date`.<br><br><b>REQUIRED</b> for a `PLASTIC` or `VIRUTUAL` card.  <br> | minimum: 1; example: 48 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Card validity period was renewed | `application/json`: object (schema `CardsValidityRenewResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `CardID2`) | no | Pismo card ID | example: 123456 |
| `status` | string (schema `CardStatus`) | no | Card status enum. Refer to the [Card lifecycle and statuses](doc:card-lifecycle-and-statuses) guide for more information and a complete list.<br> | example: "NORMAL" |
| `validity_period_hours` | integer (schema `ValidityPeriodHours`) | no | How long, in hours, the card is valid. Cannot exceed the card's `expiration_date`. Once this period is exceeded, and the card has a  `NORMAL`, `BLOCKED`, `PENDING`, `WARNING` or `REISSUED` status, its status becomes `INOPERATIVE`. <br><br>This field is used to calculate the datetime value for `valid_until`.<br><br>For `VIRTUAL` and `PLASTIC` cards. Setting this field for `TEMPORARY` or `RECURRING` cards returns a **400 Bad request** error.  <br> | example: 240 |
| `valid_until` | string (schema `ValidUntil`) | no | Card validation date in UTC time (format:yyyy-MM-ddThh:mm:ssZ). For `TEMPORARY` virtual cards, which have a limited time frame, typically 24 hours (default), or according to the program parameter for this, which is why the date/time here is more granular than `expiration_date`.  <br><br>For more information, refer to [Configuring temporary cards](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#configuring-temporary-cards).<br> | example: "2021-07-03T17:23:18Z" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-cards-overview-1`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=DELETE path=/wallet/v2/cards/{cardId}/validity operationId=delete-v2-card-validity -->
### `DELETE /wallet/v2/cards/{cardId}/validity` — Delete card validity period

- **operationId:** `delete-v2-card-validity`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Card validity`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a card's previously scheduled validity period. 
>
> The card's validity period can be removed when a virtual or plastic card has a `valid_until` value in effect.
>
> If the card's status is `NORMAL`, `REISSUED`, `BLOCKED`, `PENDING`, or `WARNING`, the `valid_until` value is removed and the card's status remains the same.
>
> When authorizing a card with a `valid_until` value in effect, this date and the card's `expiration date` are both taken into account. Otherwise, only the `expiration_date` is taken into account.
>
> This endpoint generates a [Card updated](https://developers.pismo.io/events/docs/cards-update-1) event with `operation_type` = `CARD_VALIDITY_CANCEL`.
>
> **Notes:** 
>
>  * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No content. |  |
| 401 | Access token is missing or invalid |  |
| 403 | You don't have permission to access this resource |  |
| 500 | Internal server error |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-update-1` | https://developers.pismo.io/events/docs/cards-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;401;403;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-cards-overview-1`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Card validity`: PATCH /wallet/v2/cards/{cardId}/validity/renew, DELETE /wallet/v2/cards/{cardId}/validity | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-cards-overview-1` — Cards management
- `KU-EVT-catalogue-cards` — Event catalogue: cards
