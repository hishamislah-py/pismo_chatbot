---
ku_id: KU-API-card-issuing-disputes--on-us
title: 'API reference: Card issuing - Disputes — On-Us'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Disputes.yaml
  sha256: 5c1d5513e1f3a4d1daa4d6bd654885c4edfeb5135eaa60b50f1a74d62031baad
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
- post-create-on-us-dispute
- post-update-on-us-dispute
related_kus:
- KU-CARD-disputes-setup-and-on-us
- KU-ERR-codes-acq-to-esma
- KU-EVT-catalogue-disputes
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — On-Us

**KU ID:** `KU-API-card-issuing-disputes--on-us` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `On-Us` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/on-us-dispute` | `post-create-on-us-dispute` | Create on-us dispute | no |
| `POST /v1/disputes-on-us/{disputeId}/event` | `post-update-on-us-dispute` | Update on-us dispute | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/on-us-dispute operationId=post-create-on-us-dispute -->
### `POST /v1/on-us-dispute` — Create on-us dispute

- **operationId:** `post-create-on-us-dispute`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `On-Us`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

>
> Create an on-us dispute. This allows issuers to create a dispute for a non-branded authorization or transaction performed with a Pismo-issued card. Disputes are initially created with a `PENDING` status. Once ready, the issuer must call [Update on-us dispute](ref:post-update-on-us-dispute) with the `OPEN` event to submit the dispute and move the dispute's status to `OPENED`. 
>
> For more information about on-us disputes and its state machine, refer to the [On-us disputes](https://developers.pismo.io/pismo-docs/docs/on-us-disputes) guide.
>
> This endpoint generates a [On-us dispute created](https://developers.pismo.io/events/docs/disputes-disputes-creation-1) event.
>
> **Notes:** 
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.
>   * The account ID, Org ID, and CID (correlation identifer) are parsed from the account token. 

#### Request body

Required: yes

> Create On-Us dispute request body

**Content type `application/json`** — schema: object (schema `CreateOnUsDisputeRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `source_identifier` | object (schema `SourceIdentifier`) | yes |  |  |
| `modality` | integer (schema `OnUsDisputeModality`) | yes | On-us issuer reason code:<br>  * `1` - Services not provided or product not received<br /><br>  * `2` - Defective product or not as described<br /><br>  * `3` - Nonexistent card number / Closed or nonexistent account<br /><br>  * `4` - Authorization denied / No authorization<br /><br>  * `5` - Fraud - Card present<br /><br>  * `6` - Fraud - Card not present<br /><br>  * `7` - Duplicate processing<br /><br>  * `8` - Processing error<br> | enum: [1, 2, 3, 4, 5, 6, 7, 8]; example: 2 |
| `is_partial` | boolean (schema `IsPartial`) | yes | Is partial amount chargeback? Default is `false`. | default: false; example: false |
| `disputed_amount` | number (schema `DisputedAmount`) | yes | Disputed amount. | example: 10 |
| `comment` | string (schema `Comment2`) | no | Client custom dispute comment.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `protocol` | string (schema `Protocol`) | no | Client custom protocol ID. This is primarily for you to internally identify a request. If not provided, Pismo creates a CID (correlation ID) field for this purpose.<br> | maxLength: 500; example: "20251128111532456" |
| `metadata` | object (schema `Metadata`) | no | Can be used for caller's dispute information and process. Objects and name-value pairs.<br><br> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"field1": "value", "field2": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Dispute Created | `application/json`: object (schema `CreateOnUsDisputeResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 504 | Gateway timeout | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_id` | number (schema `DisputeID`) | no | Dispute ID | example: 48670 |
| `dispute_status` | object (schema `OnUsDisputeStatusObject`) | no | On-Us dispute status information |  |
| `dispute_reason` | object (schema `DisputeReasonObject`) | no | Dispute reason information |  |
| `source` | object (schema `SourceIdentifier`) | no |  |  |
| `disputed_amount` | number (schema `DisputedAmount`) | no | Disputed amount. | example: 10 |
| `is_partial` | boolean (schema `IsPartial`) | no | Is partial amount chargeback? Default is `false`. | default: false; example: false |
| `account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 577830 |
| `comment` | string (schema `Comment2`) | no | Client custom dispute comment.<br> | maxLength: 5000; nullable: true; example: "Custom comment" |
| `protocol` | string (schema `Protocol`) | no | Client custom protocol ID. This is primarily for you to internally identify a request. If not provided, Pismo creates a CID (correlation ID) field for this purpose.<br> | maxLength: 500; example: "20251128111532456" |
| `metadata` | object (schema `Metadata`) | no | Can be used for caller's dispute information and process. Objects and name-value pairs.<br><br> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"field1": "value", "field2": "value"} |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `created_at_utc` | string (schema `CreatedAtUTC`) | no | Dispute created in UTC date/time. | format: "date-time"; example: "2021-02-21T22:51:43.000000000Z" |

##### Response 400

400 Example `EDPT0003 - Failed to parse request payload`:

```json
{
  "code": "EDPT0004",
  "message": "Failed to parse request payload",
  "http_status_code": 400
}
```

400 Example `EDPT0004 - Invalid param`:

```json
{
  "code": "EDPT0004",
  "message": "Invalid <nameOfParam> param",
  "http_status_code": 400
}
```

##### Response 401

401 Example `EDPT0005 - Missing or invalid Authorization header`:

```json
{
  "code": "EDPT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

##### Response 404

404 Example `EDPT0009 - TransactionById returned not found`:

```json
{
  "code": "EDPT0009",
  "message": "TransactionById returned [Not found] using ID: 1234567890",
  "http_status_code": 404
}
```

404 Example `BDPT0006 - Modality [123] not found`:

```json
{
  "code": "BDPT0006",
  "message": "Modality [123] not found",
  "http_status_code": 404
}
```

##### Response 422

422 Example `BDPT0001 - Error while validating fields`:

```json
{
  "code": "BDPT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "payload": [
      {
        "field": "transaction_id",
        "message": "This is field is required"
      },
      {
        "field": "report_type",
        "message": "This is an invalid value"
      }
    ]
  }
}
```

422 Example `BDPT0026 - Unable to retrieve program_id from account_id [1234]`:

```json
{
  "code": "BDPT0026",
  "message": "Unable to retrieve program_id from account_id [1234]",
  "http_status_code": 422
}
```

422 Example `BDPT0027 - Error while validating fields`:

```json
{
  "code": "BDPT0027",
  "message": "Program [1010] is not configured to create an On Us Dispute",
  "http_status_code": 422
}
```

##### Response 500

500 Example `EDPT9997 - Something went wrong when try to process a request in (entity) using ID`:

```json
{
  "code": "EDPT9997",
  "message": "Something went wrong when try to process a request in Authorizations using ID: 1234",
  "http_status_code": 500
}
```

500 Example `EDPT9998 - Something went wrong, please try again later`:

```json
{
  "code": "EDPT9998",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

500 Example `EDPT9999 - Something went wrong, please try again later`:

```json
{
  "code": "EDPT9999",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `EDPT0001 - Request timeout`:

```json
{
  "code": "EDPT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EDPT0004` | Failed to parse request payload |
| 401 | `EDPT0005` | Missing or invalid Authorization header |
| 404 | `EDPT0009` | TransactionById returned [Not found] using ID: 1234567890 |
| 404 | `BDPT0006` | Modality [123] not found |
| 422 | `BDPT0001` | Error while validating fields |
| 422 | `BDPT0026` | Unable to retrieve program_id from account_id [1234] |
| 422 | `BDPT0027` | Program [1010] is not configured to create an On Us Dispute |
| 500 | `EDPT9997` | Something went wrong when try to process a request in Authorizations using ID: 1234 |
| 500 | `EDPT9998` | Something went wrong, please try again later |
| 500 | `EDPT9999` | Something went wrong, please try again later |
| 504 | `EDPT0001` | Request timeout |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `disputes-disputes-creation-1` | https://developers.pismo.io/events/docs/disputes-disputes-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;422;500;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-setup-and-on-us`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v1/disputes-on-us/{disputeId}/event operationId=post-update-on-us-dispute -->
### `POST /v1/disputes-on-us/{disputeId}/event` — Update on-us dispute

- **operationId:** `post-update-on-us-dispute`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `On-Us`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

>
> Update on-us dispute. This endpoint updates a dispute for a non-branded authorization or transaction performed with a Pismo-issued card. Disputes are initially created with a `PENDING` status. Once ready, the issuer must call this endpoint with the `OPEN` event to submit the dispute and move the dispute status to `OPENED`. 
>
>  For more information about on-us disputes and its state machine, refer to the [On-us disputes](https://developers.pismo.io/pismo-docs/docs/on-us-disputes) guide.
>
> This endpoint generates a [Dispute status changed](https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1) event.
>
> **Notes:** 
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.
>   * The account ID, Org ID and cid (correlation identifier) are parsed from the account token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `disputeId` | path | yes | number | Dispute ID |  |

#### Request body

Required: yes

> Update On-Us dispute request body

**Content type `application/json`** — schema: object (schema `UpdateOnUsDisputeRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `event` | string (schema `OnUsEvents`) | yes | On-us dispute events | enum: ["OPEN", "CANCEL", "EXPIRE", "REJECTS", "REOPEN", "PENDING_DOCUMENTATION", "RESEND", "ISSUER_LOSS", "STORE_OWNER_LOSS", "CARDHOLDER_LOSS"]; example: "REOPEN" |
| `reason` | string (schema `OnUsReason`) | no | Reason for updating the on-us dispute | example: "Customer provided additional documentation" |
| `memo` | string (schema `OnUsMemo`) | no | Additional notes about on-us dispute endpoint |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Dispute updated | `application/json`: object (schema `UpdateOnUsDisputeResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorModel`) |
| 423 | Access not allowed | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 504 | Gateway timeout | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dispute_id` | number (schema `DisputeID`) | yes | Dispute ID | example: 48670 |
| `dispute_status` | string (schema `OnUsDisputeStatuses`) | yes | On-us dispute statuses | enum: ["OPENED", "CANCELED", "REJECTED", "PENDING", "PENDING_DOCUMENTATION", "ISSUER_LOSS", "STORE_OWNER_LOSS", "CARDHOLDER_LOSS", "EXPIRED"]; example: "OPENED" |

##### Response 400

400 Example `Invalid state machine event`:

```json
{
  "message": "Invalid state machine event",
  "http_status_code": 400
}
```

##### Response 401

401 Example `Missing or invalid Authorization header`:

```json
{
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

##### Response 404

404 Example `Could not find any account`:

```json
{
  "message": "Could not find any account",
  "http_status_code": 404
}
```

404 Example `Could not find any state machine`:

```json
{
  "message": "Could not find any state machine",
  "http_status_code": 404
}
```

404 Example `Dispute Not Found`:

```json
{
  "message": "Dispute Not Found",
  "http_status_code": 404
}
```

##### Response 422

422 Example `Event is required and cannot be empty`:

```json
{
  "message": "Event is required and cannot be empty.",
  "http_status_code": 422
}
```

422 Example `This endpoint accepts on-us disputes only.`:

```json
{
  "message": "This endpoint accepts on-us disputes only.",
  "http_status_code": 422
}
```

##### Response 423

423 Example `The dispute ID or dispute installment ID is already being used`:

```json
{
  "message": "The dispute ID or dispute installment ID is already being used",
  "http_status_code": 423
}
```

423 Example `Concurrent request detected - another request is already processing this Dispute`:

```json
{
  "message": "Concurrent request detected - another request is already processing this dispute",
  "http_status_code": 423
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `disputes-dispute-installment-status-change-1` | https://developers.pismo.io/events/docs/disputes-dispute-installment-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;422;423;500;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-disputes-setup-and-on-us`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SourceIdentifier -->
### Schema `SourceIdentifier`

Pointer: `#/components/schemas/SourceIdentifier`. Type: object (schema `SourceIdentifier`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | On-Us source ID - authorization or transaction ID depending on `type`. | maxLength: 255; example: "10001011169" |
| `type` | string | no | On-Us dispute type | enum: ["AUTHORIZATION", "TRANSACTION"]; example: "AUTHORIZATION" |

<!-- schema: #/components/schemas/OnUsDisputeStatusObject -->
### Schema `OnUsDisputeStatusObject`

Pointer: `#/components/schemas/OnUsDisputeStatusObject`. Type: object (schema `OnUsDisputeStatusObject`).

> On-Us dispute status information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | no | Description status - enums for a client's state machine, not to be implemented for anyone else at this point.<br> | example: "PENDING" |
| `type` | string | no | Type status ID. | enum: ["PRIMITIVE_ON_US"]; example: "PRIMITIVE_ON_US" |
| `group` | string (schema `DisputeGroupStatus`) | no | Group status enums<br> | enum: ["OPEN", "APPROVED", "DENIED", "CARDNETWORK_CHARGEBACK", "ANALYSING", "CARDNETWORK_SECOND_PRESENTMENT", "FAILED", "CARDNETWORK_PREARBITRATION", "RESEND", "LOSS", "WON", "REJECTED", "FAILED_PROCESSED"]; example: "OPEN" |

<!-- schema: #/components/schemas/DisputeReasonObject -->
### Schema `DisputeReasonObject`

Pointer: `#/components/schemas/DisputeReasonObject`. Type: object (schema `DisputeReasonObject`).

> Dispute reason information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | number | no | Dispute reason ID. | example: 58 |
| `description` | string | no | Dispute reason description | example: "Services not provided or product not received" |
| `reason_code` | integer (schema `OnUsDisputeModality`) | no | On-us issuer reason code:<br>  * `1` - Services not provided or product not received<br /><br>  * `2` - Defective product or not as described<br /><br>  * `3` - Nonexistent card number / Closed or nonexistent account<br /><br>  * `4` - Authorization denied / No authorization<br /><br>  * `5` - Fraud - Card present<br /><br>  * `6` - Fraud - Card not present<br /><br>  * `7` - Duplicate processing<br /><br>  * `8` - Processing error<br> | enum: [1, 2, 3, 4, 5, 6, 7, 8]; example: 2 |
| `type` | string | no | Dispute reason type | enum: ["ON_US"]; example: "ON_US" |

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

> API generic returned error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code. |  |
| `message` | string | no | Error description. |  |
| `http_status_code` | number | no | HTTP status code following RCF-9110 |  |
| `details` | object | no | Payload array returning all fields with problems on request validation. <br><br>These validations can be: <br><br>  * Invalid length <br><br>  * Invalid type <br><br>  * Invalid accepted <br><br><br>Values are explained in the message.<br><br> |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `On-Us`: POST /v1/on-us-dispute, POST /v1/disputes-on-us/{disputeId}/event | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-disputes-setup-and-on-us` — Disputes access setup and on-us disputes
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-EVT-catalogue-disputes` — Event catalogue: disputes
