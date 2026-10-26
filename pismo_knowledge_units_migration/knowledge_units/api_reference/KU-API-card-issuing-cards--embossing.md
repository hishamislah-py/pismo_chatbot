---
ku_id: KU-API-card-issuing-cards--embossing
title: 'API reference: Card issuing - Cards — Embossing'
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
- start-embossing
- patch-embossing-group
- patch-noname-embossing-group
- patch-embossing-address
- put-cards-embossing
- delete-cards-embossing
- start-reembossing
related_kus:
- KU-CARD-physical-card-embossing
- KU-EVT-catalogue-cards
specification_version: 1.4.6
---

# API reference: Card issuing - Cards — Embossing

**KU ID:** `KU-API-card-issuing-cards--embossing` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Embossing` in `api-specs/Card_issuing_-_Cards.yaml` (“Card issuing - Cards”, version `1.4.6`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card embossing endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /embossing/v1/triggers/embossing` | `start-embossing` | Start card embossing | no |
| `PATCH /embossing/v1/cards/{cardId}` | `patch-embossing-group` | Update nominal card embossing group | no |
| `PATCH /embossing/v1/cards/noname/{cardId}` | `patch-noname-embossing-group` | Update noname card embossing group | no |
| `PATCH /embossing/v1/cards/{cardId}/address` | `patch-embossing-address` | Update card embossing address | no |
| `PUT /embossing/v1/cards/{cardId}/embossing` | `put-cards-embossing` | Add card to next scheduled embossing | no |
| `DELETE /embossing/v1/cards/{cardId}/embossing` | `delete-cards-embossing` | Delete card from next scheduled embossing | no |
| `POST /embossing/v1/cards/reembossing` | `start-reembossing` | Resend cards for embossing | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/embossing/v1/triggers/embossing operationId=start-embossing -->
### `POST /embossing/v1/triggers/embossing` — Start card embossing

- **operationId:** `start-embossing`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Starts card embossing for a specific embossing configuration. Within that configuration, you can emboss cards for a specific program or card(s).
>
> * If only `config_id` is passed in the request, then all cards in all programs are added to the embossing file.
> * If `config_id` and  program ID(s) are passed in the request, then all cards in those programs are added to the embossing file.
> * If `config_id` and card ID(s) are passed in the request, then only those cards are added to the embossing file.
>
> You can call the [List embossing files](ref:get-embossing-file-info) endpoint to get embossing configuration IDs.
>
> The file generation is asynchronous and not in real-time for any option described above.
>
> Only available in the EXT environment. For more information, refer to [Embossing flows](doc:physical-card-embossing#embossing-flow).
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string (schema `ConfigID`) | yes | Embosser configuration/group ID. <br><br>You can call [Get nominal card embossing info](https://developers.pismo.io/pismo-docs/reference/get-embossing-info)  to get a card's embossing group.<br><br>You can also call [Get org embosser info](https://developers.pismo.io/pismo-docs/reference/get-embossing-configurations-info) to get an embossing group's configuration ID. <br> | format: "uuid"; example: "acde070d-8c4c-4f0d-9d8a-162843c10333" |
| `programs` | array of integer | no | Program ID array |  |
| `cards` | array of integer | no | Card ID array |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Embossing trigger as Accepted |  |
| 400 | Bad Request | `application/json`: object |

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "Field config_id is required",
  "error": "bad_request",
  "status": 400
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/embossing/v1/cards/{cardId} operationId=patch-embossing-group -->
### `PATCH /embossing/v1/cards/{cardId}` — Update nominal card embossing group

- **operationId:** `patch-embossing-group`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a nominal card's embossing group.<br>
>
> As a card issuer, you can set up your own embossing configuration in the Pismo platform, which can have multiple embossing groups. Each embossing group can have its own configured schedule and embosser. Assigning a card to a different embossing group effectively changes its schedule and embosser.
>
> Contact your Pismo representative to set up your embossing configuration and process. For more information on embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `embossing_group` | string | no | Embossing group name. If not passed, the default embossing group is used. |  |

Example `example-1`:

```json
{
  "embossing_group": "key_embossing_group"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object |
| 404 | Not Found | `application/json`: object |
| 409 | Conflict | `application/json`: object |

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "The field embossing_group is required",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

##### Response 404

404 Example `example-card-not-found`:

```json
{
  "message": "Card not found",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```

404 Example `example-config-not-found`:

```json
{
  "message": "Config invalid",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```

##### Response 409

409 Example `example-conflict`:

```json
{
  "message": "Card has already been embossed",
  "error": "conflict",
  "status": 409,
  "error_code": ""
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;409`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/embossing/v1/cards/noname/{cardId} operationId=patch-noname-embossing-group -->
### `PATCH /embossing/v1/cards/noname/{cardId}` — Update noname card embossing group

- **operationId:** `patch-noname-embossing-group`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the embossing group for noname cards.<br>
>
> Noname cards are batch-generated and not initially associated with customers, which occurs later.
>
> As a card issuer, you can set up your own embossing configuration in the Pismo platform, which can have multiple embossing groups. Each embossing group can have its own configured schedule and embosser. Assigning a card to a different embossing group effectively changes its schedule and embosser.
>
> Contact your Pismo representative to set up your embossing configuration and process. For more information on embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide.
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

#### Request body

Required: yes

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `embossing_group` | string | no | Embossing group name. If not passed, the default embossing group is used. |  |

Example `example-1`:

```json
{
  "embossing_group": "key_embossing_group"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object |
| 404 | Not Found | `application/json`: object |
| 409 | Conflict | `application/json`: object |

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "the field embossing_group is required",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

##### Response 404

404 Example `example-card-not-found`:

```json
{
  "message": "card not found",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```

404 Example `example-config-not-found`:

```json
{
  "message": "config invalid",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```

##### Response 409

409 Example `example-conflict`:

```json
{
  "message": "patch not allowed because card has already been embossed",
  "error": "conflict",
  "status": 409,
  "error_code": ""
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;409`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PATCH path=/embossing/v1/cards/{cardId}/address operationId=patch-embossing-address -->
### `PATCH /embossing/v1/cards/{cardId}/address` — Update card embossing address

- **operationId:** `patch-embossing-address`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Updates the embossing address. Currently, the embossing process uses the address of the customer linked to the account. However, you can use this endpoint to send the embossed card to an address other than the mailing address. For example, a customer is traveling and loses their card. They request a duplicate and want it delivered to their hotel. With this endpoint, it is possible to have it sent to another address without changing their default mailing address.
>
> You can call the [Create new address](ref:post-accounts-v1-accounts-accountid-addresses) endpoint to create an address object and get an address ID.
>
> For more information about embossing, refer to the [Physical card embossing](doc:physical-card-embossing) guide. 
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

#### Request body

Required: yes

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `address_id` | string | yes | Address object ID |  |

Example `example-1`:

```json
{
  "address_id": "123"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok address updated. |  |
| 400 | Bad request | `application/json`: object |
| 406 | Not acceptable | `application/json`: object |

##### Response 400

400 Example `example-address-not-found`:

```json
{
  "message": "Address not found",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

400 Example `example-invalid-payload`:

```json
{
  "message": "Invalid payload",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

##### Response 406

406 Example `example-not-acceptable`:

```json
{
  "message": "Address setting for embossed card not allowed",
  "error": "not_acceptable",
  "status": 406,
  "error_code": ""
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;406`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=PUT path=/embossing/v1/cards/{cardId}/embossing operationId=put-cards-embossing -->
### `PUT /embossing/v1/cards/{cardId}/embossing` — Add card to next scheduled embossing

- **operationId:** `put-cards-embossing`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

>
> Add card to next scheduled embossing. 
>
> You can use this endpoint for On Demand embossing. For more information, refer to [Embossing rules](doc:physical-card-embossing#embossing-rules) > On Demand embossing and [Embossing flows](doc:physical-card-embossing#embossing-flow).
>
> **IMPORTANT**: 
>   * You should only call this endpoint **AFTER** the [Card can be added to next scheduled embossing](https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1) event is received. This event is generated when a card is created and all necessary asynchronous PCI configuration is done.
>   * This endpoint does **NOT** generate an event.
>
> **Notes:**
>   * To use this endpoint, request it with a [Jira ticket](doc:opening-a-service-desk-ticket) with type = Settings and ask to use *ondemand* embossing.
>   * If you call this endpoint, the [Change card password](ref:put-v2-card-password) endpoint will no longer add the card for embossing.
>   * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>   * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object |
| 401 | Access token is missing or invalid |  |
| 404 | Not Found | `application/json`: object |
| 406 | StatusNotAcceptable | `application/json`: object |
| 500 | Internal server error |  |

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "the field card_id is required",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

##### Response 404

404 Example `example-card-not-found`:

```json
{
  "message": "card not found",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```

##### Response 406

406 Example `example-card-not-found`:

```json
{
  "message": "Card already embossed",
  "error": "StatusNotAcceptable",
  "status": 406,
  "error_code": ""
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-embossing-card-ingress-1` | https://developers.pismo.io/events/docs/cards-embossing-card-ingress-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;404;406;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=DELETE path=/embossing/v1/cards/{cardId}/embossing operationId=delete-cards-embossing -->
### `DELETE /embossing/v1/cards/{cardId}/embossing` — Delete card from next scheduled embossing

- **operationId:** `delete-cards-embossing`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete card from next scheduled embossing. This endpoint only works in conjunction with the [Add card to next scheduled embossing](ref:put-cards-embossing) endpoint.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cardId` | path | yes | string | Pismo card ID | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted. |  |
| 400 | Bad Request | `application/json`: object |
| 401 | Access token is missing or invalid |  |
| 404 | Not Found | `application/json`: object |
| 406 | StatusNotAcceptable | `application/json`: object |
| 500 | Internal server error |  |

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "The field card_id is required",
  "error": "bad_request",
  "status": 400,
  "error_code": ""
}
```

##### Response 404

404 Example `example-card-not-found`:

```json
{
  "message": "Card not found",
  "error": "not_found",
  "status": 404,
  "error_code": ""
}
```

##### Response 406

406 Example `example-card-not-found`:

```json
{
  "message": "Card already embossed",
  "error": "StatusNotAcceptable",
  "status": 406,
  "error_code": ""
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;404;406;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

<!-- op: spec=api-specs/Card_issuing_-_Cards.yaml method=POST path=/embossing/v1/cards/reembossing operationId=start-reembossing -->
### `POST /embossing/v1/cards/reembossing` — Resend cards for embossing

- **operationId:** `start-reembossing`
- **Specification:** `api-specs/Card_issuing_-_Cards.yaml` (Card issuing - Cards)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Embossing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enables cards to be sent again to the embosser at the next scheduled time. Cards to be resent must meet the prerequisites. For more information, refer to the [Physical card embossing guide](doc:physical-card-embossing).
>
> This endpoint is available to on-demand customers. On-demand customers can emboss cards with `NORMAL`, `BLOCKED`, `PENDING`, and `WARNING` statuses, in addition to `CREATED`.
>
> This endpoint generates a [Card reembossing notification received](https://developers.pismo.io/events/docs/cards-reembossing-1) event. 
>
> **Notes:** 
>
>  * This endpoint requires an account token - an access token encoded with a Pismo account ID. 
>
>  * This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cards` | array of integer | yes | Card IDs to resend for embossing |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Rembossing accepted |  |
| 400 | Bad Request | `application/json`: object |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 400

400 Example `example-bad-request`:

```json
{
  "message": "Invalid payload to reembossing, cards is required",
  "error": "bad_request",
  "status": 40
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-reembossing-1` | https://developers.pismo.io/events/docs/cards-reembossing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-physical-card-embossing`.

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
| `api-specs/Card_issuing_-_Cards.yaml` | tag `Embossing`: POST /embossing/v1/triggers/embossing, PATCH /embossing/v1/cards/{cardId}, PATCH /embossing/v1/cards/noname/{cardId}, PATCH /embossing/v1/cards/{cardId}/address, PUT /embossing/v1/cards/{cardId}/embossing, DELETE /embossing/v1/cards/{cardId}/embossing, POST /embossing/v1/cards/reembossing | https://github.com/PismoDevEx/pismo-api-specs | `687df76f123e41a7…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-physical-card-embossing` — Physical card embossing
- `KU-EVT-catalogue-cards` — Event catalogue: cards
