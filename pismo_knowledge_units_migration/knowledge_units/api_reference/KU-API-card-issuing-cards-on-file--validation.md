---
ku_id: KU-API-card-issuing-cards-on-file--validation
title: 'API reference: Card issuing - Cards on file — Validation'
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
- list-all-validations-for-a-given-card
- create-a-new-validation-for-a-given-card
- get-a-specific-validation-for-a-given-card
- get-a-specific-validation-amount-for-a-given-card
- submit-a-validation-try
related_kus:
- KU-EVT-cards-data-events
- KU-EVT-catalogue-cardsonfile
specification_version: 2.0.0
---

# API reference: Card issuing - Cards on file — Validation

**KU ID:** `KU-API-card-issuing-cards-on-file--validation` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Validation` in `api-specs/Card_issuing_-_Cards_on_file.yaml` (“Card issuing - Cards on file”, version `2.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Cards on file validations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations` | `list-all-validations-for-a-given-card` | List card validations | no |
| `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations` | `create-a-new-validation-for-a-given-card` | Create card validation | no |
| `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}` | `get-a-specific-validation-for-a-given-card` | Get card validation | no |
| `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount` | `get-a-specific-validation-amount-for-a-given-card` | Get card validation amount | no |
| `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/tries` | `submit-a-validation-try` | Submit validation try | no |

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=GET path=/cardsonfile/v2/cardsonfile/cards/{uuid}/validations operationId=list-all-validations-for-a-given-card -->
### `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations` — List card validations

- **operationId:** `list-all-validations-for-a-given-card`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Validation`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get all validations for a card currently outstanding.
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `uuid` | path | yes | string | Card UUID (token) to validate. |  |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: array of object (schema `ValidationResponseModel`) |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=POST path=/cardsonfile/v2/cardsonfile/cards/{uuid}/validations operationId=create-a-new-validation-for-a-given-card -->
### `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations` — Create card validation

- **operationId:** `create-a-new-validation-for-a-given-card`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Validation`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create a new invoice validation for a given tokenized card. A random transacation amount between 1.00 and 5.00 (later chargebacked) is created for the cardholder to approve, which requires logging into an online banking account. The cardholder has up to 3 tries and 96 hours to input the correct amount. If the validation fails, the card is deleted from the wallet.<br>
>
> This endpoint generates a [Card on file validation result received](https://developers.pismo.io/events/docs/cardsonfile-verification-1) event. If the validation fails, it generates an [Card excluded](https://developers.pismo.io/events/docs/cardsonfile-exclusion-1) event.
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `uuid` | path | yes | string | Card UUID (token) to validate. |  |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `ValidationRequestModel`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `ValidationType`) | no | Validation type, currently only `INVOICE`. | enum: ["INVOICE"] |
| `expiration_hours` | number (schema `ValidationExpiration`) | no | When validation expires since creation in hours - 96 maximum. Default is 96. | minimum: 1; maximum: 96 |
| `remaining_tries` | number (schema `ValidationRemainingTries`) | no | Maximum card validation tries - 3 tries maximum. Default is 3. | minimum: 1; maximum: 3 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ValidationResponseModel`) |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `ValidationType`) | no | Validation type, currently only `INVOICE`. | enum: ["INVOICE"] |
| `expiration_hours` | number (schema `ValidationExpiration`) | no | When validation expires since creation in hours - 96 maximum. Default is 96. | minimum: 1; maximum: 96 |
| `remaining_tries` | number (schema `ValidationRemainingTries`) | no | Maximum card validation tries - 3 tries maximum. Default is 3. | minimum: 1; maximum: 3 |
| `uuid` | string | no | Unique validation ID |  |
| `type` | string | no | Validation type, currently, only `INVOICE`. |  |
| `status` | string | no | Validation status enum - `IN_PROGRESS`, `SUCCESS`, or `FAILED` | enum: ["IN_PROGRESS", "SUCCESS", "FAILED"] |
| `expiration_hours` | number | no | Validation expiration since creation in hours. Maximum is 96 | minimum: 1; maximum: 96 |
| `remaining_tries` | number | no | Maximum card validation tries. Maximum is 3. | minimum: 1; maximum: 3 |
| `inclusion_date` | string | no | Validation creation date in ISO 8601 format, i.e., 2019-09-04T19:09:53.881Z |  |
| `expiration_date` | string | no | Date validation expires if not validated yet in ISO 8601 format, i.e., 2019-09-08T19:09:53.881Z |  |
| `activation_date` | string | no | When validated date in ISO 8601 format, i.e., 2019-09-08T19:09:53.881Z |  |
| `cancellation_date` | string | no | Validation cancelled date, by expiration or out of remaining tries, in ISO 8601 format, i.e., 2019-09-08T19:09:53.881Z |  |
| `refunded_at` | string | no | When charge refunded in in ISO 8601 format, i.e., 2019-09-08T19:09:53.881Z |  |
| `refund_id` | string | no | Refund ID |  |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cardsonfile-exclusion-1` | https://developers.pismo.io/events/docs/cardsonfile-exclusion-1 |
| `cardsonfile-verification-1` | https://developers.pismo.io/events/docs/cardsonfile-verification-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-cards-data-events`.

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=GET path=/cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid} operationId=get-a-specific-validation-for-a-given-card -->
### `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}` — Get card validation

- **operationId:** `get-a-specific-validation-for-a-given-card`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Validation`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Gets a specific validation for a card
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `uuid` | path | yes | string | Card UUID (token) to validate. |  |
| `validationid` | path | yes | string | Validation UUID. This is the `uuid` field returned from [Create card validation](https://developers.pismo.io/pismo-docs/reference/create-a-new-validation-for-a-given-card) |  |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `ValidationResponseWithTriesModel`) |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `ValidationType`) | no | Validation type, currently only `INVOICE`. | enum: ["INVOICE"] |
| `expiration_hours` | number (schema `ValidationExpiration`) | no | When validation expires since creation in hours - 96 maximum. Default is 96. | minimum: 1; maximum: 96 |
| `remaining_tries` | number (schema `ValidationRemainingTries`) | no | Maximum card validation tries - 3 tries maximum. Default is 3. | minimum: 1; maximum: 3 |
| `uuid` | string | no | Unique validation ID |  |
| `type` | string | no | Validation type, currently, only `INVOICE`. |  |
| `status` | string | no | Validation status enum - `IN_PROGRESS`, `SUCCESS`, or `FAILED` | enum: ["IN_PROGRESS", "SUCCESS", "FAILED"] |
| `expiration_hours` | number | no | Validation expiration since creation in hours. Maximum is 96 | minimum: 1; maximum: 96 |
| `remaining_tries` | number | no | Maximum card validation tries. Maximum is 3. | minimum: 1; maximum: 3 |
| `inclusion_date` | string | no | Validation creation date in ISO 8601 format, i.e., 2019-09-04T19:09:53.881Z |  |
| `expiration_date` | string | no | Date validation expires if not validated yet in ISO 8601 format, i.e., 2019-09-08T19:09:53.881Z |  |
| `activation_date` | string | no | When validated date in ISO 8601 format, i.e., 2019-09-08T19:09:53.881Z |  |
| `cancellation_date` | string | no | Validation cancelled date, by expiration or out of remaining tries, in ISO 8601 format, i.e., 2019-09-08T19:09:53.881Z |  |
| `refunded_at` | string | no | When charge refunded in in ISO 8601 format, i.e., 2019-09-08T19:09:53.881Z |  |
| `refund_id` | string | no | Refund ID |  |
| `tries` | array of object (schema `ValidationTriesModel`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=GET path=/cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount operationId=get-a-specific-validation-amount-for-a-given-card -->
### `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount` — Get card validation amount

- **operationId:** `get-a-specific-validation-amount-for-a-given-card`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Validation`
- **Deprecated in specification:** no
- **Security requirement:** not declared
- **Lifecycle note:** `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount` also appears in the removed-endpoints list (`docs/resources/api-endpoints-removed.md`). The current specification still contains it: conflicting sources (see ISSUES_AND_GAPS.md).

**Description (from the specification):**

> Gets the validation amount for a specific card validation
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `uuid` | path | yes | string | Card UUID (token) to validate. |  |
| `validationid` | path | yes | string | Validation UUID. This is the `uuid` field returned from [Create card validation](https://developers.pismo.io/pismo-docs/reference/create-a-new-validation-for-a-given-card) |  |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `ValidationAmountResponse`) |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `validation_amount` | number | no | Validation amount |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Cards_on_file.yaml method=POST path=/cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/tries operationId=submit-a-validation-try -->
### `POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/tries` — Submit validation try

- **operationId:** `submit-a-validation-try`
- **Specification:** `api-specs/Card_issuing_-_Cards_on_file.yaml` (Card issuing - Cards on file)
- **Server base URL(s):** `https://gw-pci.pismolabs.io`, `https://sandbox.pismolabs.io`
- **Tags:** `Validation`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Submit a validation try with amount.<br>
>
> This endpoint generates a [Card on file validation result received](https://developers.pismo.io/events/docs/cardsonfile-verification-1) event with `PENDING` status. If the verification/validation fails, a [Card excluded](https://developers.pismo.io/events/docs/cardsonfile-exclusion-1) event is generated and the card is deleted from the customer's wallet.
>
> **Note**: This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `uuid` | path | yes | string | Card UUID (token) to validate. |  |
| `validationid` | path | yes | string | Validation UUID. This is the `uuid` field returned from [Create card validation](https://developers.pismo.io/pismo-docs/reference/create-a-new-validation-for-a-given-card) |  |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.<br> |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `TryRequestModel`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Amount to be tried (1.00 - 5.00). | minimum: 1; maximum: 5 |
| `date` | string | no | Submission date. Format = dd/mm/yyyy. If not passed, the current datetime is used. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `CardsOnFileErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `CardsOnFileErrorResponse`) |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cardsonfile-exclusion-1` | https://developers.pismo.io/events/docs/cardsonfile-exclusion-1 |
| `cardsonfile-verification-1` | https://developers.pismo.io/events/docs/cardsonfile-verification-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;500`, has examples `False`, emits events `2`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/CardsOnFileErrorResponse -->
### Schema `CardsOnFileErrorResponse`

Pointer: `#/components/schemas/CardsOnFileErrorResponse`. Type: object (schema `CardsOnFileErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code |  |
| `message` | string | no | Error message |  |

<!-- schema: #/components/schemas/ValidationTriesModel -->
### Schema `ValidationTriesModel`

Pointer: `#/components/schemas/ValidationTriesModel`. Type: object (schema `ValidationTriesModel`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date` | string | no | Submission date. RFC3339 format. |  |
| `amount` | number | no | Tried amount. |  |

## Lifecycle status

- `GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount` also appears in the removed-endpoints list (`docs/resources/api-endpoints-removed.md`). The current specification still contains it: conflicting sources (see ISSUES_AND_GAPS.md).

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Cards_on_file.yaml` | tag `Validation`: GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations, POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations, GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}, GET /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/amount, POST /cardsonfile/v2/cardsonfile/cards/{uuid}/validations/{validationid}/tries | https://github.com/PismoDevEx/pismo-api-specs | `85cc36fbf4444718…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-cards-data-events` — Card issuing - Cards
- `KU-EVT-catalogue-cardsonfile` — Event catalogue: cardsonfile
