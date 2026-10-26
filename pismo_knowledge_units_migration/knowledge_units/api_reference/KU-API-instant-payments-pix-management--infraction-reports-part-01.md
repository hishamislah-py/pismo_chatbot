---
ku_id: KU-API-instant-payments-pix-management--infraction-reports-part-01
title: 'API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_Pix_management.yaml
  sha256: 7d7fee078ccf55696a5fdd1a00ea559d88a6148a11b28529395dab8f2405a750
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
- get-v2-pix-account-infractions
- post-v2-pix-infraction-create
- post-v2-pix-infraction-close
- post-v2-pix-infraction-cancel
related_kus:
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-epda
- KU-ERR-codes-epdg
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-pix
- KU-EVT-pix-payments-data-events
- KU-PAY-pix-instant-payments
specification_version: 0.0.1
---

# API reference: Instant payments - Pix management — Infraction reports (part 1 of 2)

**KU ID:** `KU-API-instant-payments-pix-management--infraction-reports-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Infraction reports` in `api-specs/Instant_payments_-_Pix_management.yaml` (“Instant payments - Pix management”, version `0.0.1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage Pix transaction infraction reports endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/pix/infraction-reports` | `get-v2-pix-account-infractions` | List account infractions | no |
| `POST /v2/pix/infraction-reports` | `post-v2-pix-infraction-create` | Create infraction report (outdated) | no |
| `POST /v2/pix/infraction-reports/{id}/close` | `post-v2-pix-infraction-close` | Close infraction report | no |
| `POST /v2/pix/infraction-reports/{id}/cancel` | `post-v2-pix-infraction-cancel` | Cancel infraction report | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v2/pix/infraction-reports operationId=get-v2-pix-account-infractions -->
### `GET /v2/pix/infraction-reports` — List account infractions

- **operationId:** `get-v2-pix-account-infractions`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Infraction reports`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account infraction notifications.
>
> Notifications are sorted in ascending order by the `bacen_last_modified_datetime` response return field.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `funds_recovery_id` | query | no | string | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `is_reporter` | query | no | boolean | Return notifications where the participant is the creator? Default is `true`. | default: true |
| `is_counterparty` | query | no | boolean | Return notifications where the participant is a counterparty? Default is `true`. | default: true |
| `include_details` | query | no | boolean | Include details in response? Default is `false`. | default: false; example: false |
| `status` | query | no | string | Status filter, default is all (""). | enum: ["", "OPEN", "ACKNOWLEDGED", "CLOSED", "CANCELLED"]; default: "" |
| `modified_after` | query | no | string | Only return infractions modified at this datetime or after. Format = RFC 3339. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `modified_before` | query | no | string | Only return infractions modified at this datetime or before.  Format = RFC 3339.  For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2023-04-12T23:20:50.52Z" |
| `limit` | query | no | integer | Maximum results to return. Default is `20`. Maximum is `200`. | default: 20; maximum: 200; example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InfractionReportList`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 429 | Too many requests | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 503 | Service Unavailable | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_more_elements` | boolean | yes | Are there more items? | example: true |
| `items` | array of object (schema `InfractionReportResponse`) | yes |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `Tenant not found`:

```json
{
  "code": "EPDA0001",
  "message": "Missing x-tenant header."
}
```

400 Example `Invalid binding`:

```json
{
  "code": "EPDA0002",
  "message": "Failed to unmarshal request body"
}
```

400 Example `Validate errors`:

```json
{
  "code": "EPDA0003",
  "message": "There are invalid fields when trying to validate request body.",
  "details": {
    "payload": [
      {
        "field": "status",
        "message": "Field validation for 'status' failed on the 'oneof' tag"
      }
    ]
  }
}
```

##### Response 401

- Response header `x-cid`: Request tracking identifier. (string)
401 Example `Provider service error`:

```json
{
  "code": "EPDG0013",
  "message": "Unauthorized access to the provider service"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 429

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `Provider service communication error`:

```json
{
  "code": "EPDA0029",
  "message": "Internal errors while attempting to communicate with the provider service"
}
```

500 Example `Invalid client error`:

```json
{
  "code": "EPDG0005",
  "message": "Invalid Pix provider '{provider_name}'"
}
```

500 Example `Failed marshalling object`:

```json
{
  "code": "EPDG0006",
  "message": "Failed to marshal JSON object"
}
```

500 Example `Failed unmarshalling object`:

```json
{
  "code": "EPDG0007",
  "message": "Failed to unmarshal JSON object"
}
```

500 Example `Error reading response data`:

```json
{
  "code": "EPDG0010",
  "message": "I/O error while reading response data: '{details}'"
}
```

500 Example `Provider service error`:

```json
{
  "code": "EPDG0016",
  "message": "Provider service returned an internal error while trying to access the resource",
  "details": {
    "external": [
      {
        "code": "PBE315",
        "message": "Generic error"
      }
    ]
  }
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 503

- Response header `x-cid`: Request tracking identifier. (string)
503 Example `Provider service unavailable`:

```json
{
  "code": "EPDG0017",
  "message": "Provider service resource is unavailable"
}
```

503 Example `Provider authentication service unavailable`:

```json
{
  "code": "EPDG0021",
  "message": "Provider authentication service is unavailable"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0001` | Missing x-tenant header. |
| 400 | `EPDA0002` | Failed to unmarshal request body |
| 400 | `EPDA0003` | There are invalid fields when trying to validate request body. |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 500 | `EPDA0029` | Internal errors while attempting to communicate with the provider service |
| 500 | `EPDG0005` | Invalid Pix provider '{provider_name}' |
| 500 | `EPDG0006` | Failed to marshal JSON object |
| 500 | `EPDG0007` | Failed to unmarshal JSON object |
| 500 | `EPDG0010` | I/O error while reading response data: '{details}' |
| 500 | `EPDG0016` | Provider service returned an internal error while trying to access the resource |
| 500 | `PBE315` | Generic error |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 503 | `EPDG0017` | Provider service resource is unavailable |
| 503 | `EPDG0021` | Provider authentication service is unavailable |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;429;500;502;503;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/infraction-reports operationId=post-v2-pix-infraction-create -->
### `POST /v2/pix/infraction-reports` — Create infraction report (outdated)

- **operationId:** `post-v2-pix-infraction-create`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Infraction reports`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> This endpoint is outdated and no longer works. It is recommended you call [Create funds recovery](https://developers.pismo.io/pismo-docs/reference/post-create-funds-recovery) instead.
>
> Creates an infraction report. Both the debited participant and the credited participant can create an infraction report.
>
> For refund requests, the original transaction payer's payment service provider (PSP) **must** create the report. 
>
> Only the PSP or the original transaction's recipient can cancel a refund. 
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting a success or failure event.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1" >Pix infraction status changed</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: yes

> Infraction report

**Content type `*/*`** — schema: object (schema `InfractionCreationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | string (schema `InfractionTransactionID`) | yes | Original transaction's end to end ID. | example: "E9999901012341234123412345678900" |
| `situation_type` | string (schema `InfractionReportSituation`) | yes | What gave rise to the infraction notification | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"]; example: "SCAM" |
| `reason` | string (schema `InfractionReason`) | yes | Reason for opening infraction report | enum: ["REFUND_REQUEST", "REFUND_CANCELLED"]; example: "REFUND_REQUEST" |
| `details` | string (schema `InfractionDetails`) | no | Details that can help the receiving participant to analyze the suspected violation<br> | maxLength: 2000; example: "Details about infraction" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `CreateInfractionReportResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 429 | Too many requests | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 503 | Service Unavailable | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 201

- Response header `x-cid`: Request tracking identifier. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `InfractionReportID`) | yes | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `transaction_id` | string (schema `InfractionTransactionID`) | yes | Original transaction's end to end ID. | example: "E9999901012341234123412345678900" |
| `reason` | string (schema `InfractionReason`) | yes | Reason for opening infraction report | enum: ["REFUND_REQUEST", "REFUND_CANCELLED"]; example: "REFUND_REQUEST" |
| `situation_type` | string (schema `InfractionReportSituation`) | yes | What gave rise to the infraction notification | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"]; example: "SCAM" |
| `status` | string (schema `InfractionReportStatus`) | yes | Infraction report status | enum: ["OPEN", "ACKNOWLEDGED", "CLOSED", "CANCELLED"]; example: "OPEN" |
| `reporter_participant` | string (schema `InfractionReporterParticipant`) | yes | Transaction payer participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value.<br> | format: "number"; example: "78265328" |
| `counterparty_participant` | string (schema `InfractionCounterpartyParticipant`) | yes | Transaction recipient participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value.<br> | format: "number"; example: "78265328" |
| `bacen_creation_datetime` | string (schema `BacenCreationDateTime`) | yes | Date of infraction report creation. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `bacen_last_modified_datetime` | string (schema `BacenLastModifiedDateTime`) | yes | Date of infraction report modification. RFC 3339  date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `details` | string (schema `InfractionDetails`) | no | Details that can help the receiving participant to analyze the suspected violation<br> | maxLength: 2000; example: "Details about infraction" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

202 Example `Creation request accepted and will processed async`:

```json
{
  "code": "EPDA0148",
  "message": "Infraction registration will continue asynchronously"
}
```

202 Example `Cancellation request accepted and will processed async`:

```json
{
  "code": "EPDA0149",
  "message": "Infraction cancel will continue asynchronously"
}
```

202 Example `Close request accepted and will processed async`:

```json
{
  "code": "EPDA0149",
  "message": "Infraction close will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `Invalid binding`:

```json
{
  "code": "EPDA0002",
  "message": "Failed to unmarshal request body"
}
```

400 Example `Validate errors`:

```json
{
  "code": "EPDA0003",
  "message": "There are invalid fields when trying to validate request body",
  "details": {
    "payload": [
      {
        "field": "InfractionReportRequest.infraction_type",
        "message": "Field validation for 'infraction_type' failed on the 'oneof' tag"
      }
    ]
  }
}
```

##### Response 401

- Response header `x-cid`: Request tracking identifier. (string)
401 Example `Provider service error`:

```json
{
  "code": "EPDG0013",
  "message": "Unauthorized access to the provider service"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 429

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `Provider service communication error`:

```json
{
  "code": "EPDA0029",
  "message": "Internal errors while attempting to communicate with the provider service"
}
```

500 Example `Invalid client error`:

```json
{
  "code": "EPDG0005",
  "message": "Invalid Pix provider '{provider_name}'"
}
```

500 Example `Failed marshalling object`:

```json
{
  "code": "EPDG0006",
  "message": "Failed to marshal JSON object"
}
```

500 Example `Failed unmarshalling object`:

```json
{
  "code": "EPDG0007",
  "message": "Failed to unmarshal JSON object"
}
```

500 Example `Error reading response data`:

```json
{
  "code": "EPDG0010",
  "message": "I/O error while reading response data: '{details}'"
}
```

500 Example `Provider service error`:

```json
{
  "code": "EPDG0016",
  "message": "Provider service returned an internal error while trying to access the resource",
  "details": {
    "external": [
      {
        "code": "PBE315",
        "message": "Generic error"
      }
    ]
  }
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 503

- Response header `x-cid`: Request tracking identifier. (string)
503 Example `Provider service unavailable`:

```json
{
  "code": "EPDG0017",
  "message": "Provider service resource is unavailable"
}
```

503 Example `Provider authentication service unavailable`:

```json
{
  "code": "EPDG0021",
  "message": "Provider authentication service is unavailable"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0148` | Infraction registration will continue asynchronously |
| 202 | `EPDA0149` | Infraction cancel will continue asynchronously |
| 400 | `EPDA0002` | Failed to unmarshal request body |
| 400 | `EPDA0003` | There are invalid fields when trying to validate request body |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 500 | `EPDA0029` | Internal errors while attempting to communicate with the provider service |
| 500 | `EPDG0005` | Invalid Pix provider '{provider_name}' |
| 500 | `EPDG0006` | Failed to marshal JSON object |
| 500 | `EPDG0007` | Failed to unmarshal JSON object |
| 500 | `EPDG0010` | I/O error while reading response data: '{details}' |
| 500 | `EPDG0016` | Provider service returned an internal error while trying to access the resource |
| 500 | `PBE315` | Generic error |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 503 | `EPDG0017` | Provider service resource is unavailable |
| 503 | `EPDG0021` | Provider authentication service is unavailable |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-infraction-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;401;403;429;500;502;503;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/infraction-reports/{id}/close operationId=post-v2-pix-infraction-close -->
### `POST /v2/pix/infraction-reports/{id}/close` — Close infraction report

- **operationId:** `post-v2-pix-infraction-close`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Infraction reports`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Closes an infraction report.
>
> Only the counterparty participant can close an infraction report. 
>
> The operation is idempotent. If you try to close the report again with the same parameters, you will get the same response as the first time.
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting a success or failure event.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1" >Pix infraction status changed</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `id` | path | yes | string | Infraction report ID | format: "uuid" |

#### Request body

Required: yes

> Infraction report close

**Content type `application/json`** — schema: object (schema `InfractionCloseRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `analysis_result` | string (schema `InfractionAnalysisResult`) | yes | Infraction analysis result | enum: ["AGREED", "DISAGREED"]; example: "AGREED" |
| `fraud_type` | string (schema `InfractionFraudType`) | no | Verified fraud type. **REQUIRED** if `analysis_result` = `AGREED`. | enum: ["APPLICATION_FRAUD", "MULE_ACCOUNT", "SCAMMER_ACCOUNT", "OTHER"]; example: "APPLICATION_FRAUD" |
| `analysis_details` | string (schema `InfractionAnalysisDetails`) | no | Infraction's analysis details, which can guide the payer to next steps. | maxLength: 2000; example: "Details about infraction analysis" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.InfractionReportResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Resource Not Found | `application/json`: object (schema `message.Message`) |
| 429 | Too many requests | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 503 | Service Unavailable | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `creation_date` | string (schema `CreationDatetime`) | yes | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `credited_participant` | string (schema `CreditedParticipant`) | yes | Credited participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `debited_participant` | string (schema `DebitedParticipant`) | yes | Debited participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `end_to_end_id` | string (schema `EndToEndID`) | yes | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The end_to_end_id is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "132cca0f6a816dd5be409256b3662343" |
| `infraction_report_id` | string (schema `InfractionReportID`) | yes | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `infraction_type` | string (schema `infractionType`) | yes | Infraction type: <br>  * `FRAUD` - Payer or payee requested. <br>  * `REFUND_REQUEST` - Initiated only by payer's payment service provider (PSP). Used to mark a key as fraudulent and asks for a refund.<br>  * `REFUND_CANCELLED` - Initiated only by payee's PSP.   To indicate that a refund done thru an infraction process was a fraud and needs to be returned,<br> | enum: ["FRAUD", "REFUND_REQUEST", "REFUND_CANCELLED"]; example: "FRAUD" |
| `last_modified` | string (schema `LastModifiedDatetime`) | yes | Last modified datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `reported_by` | string (schema `InfractionReportedBy`) | yes | Who filed the infraction report | enum: ["DEBITED_PARTICIPANT", "CREDITED_PARTICIPANT"]; example: "DEBITED_PARTICIPANT" |
| `status` | string (schema `InfractionStatus`) | yes | Infraction status | enum: ["OPEN", "ACKNOWLEDGED", "CLOSED", "CANCELLED"]; example: "CLOSED" |
| `transaction_id` | string (schema `TransactionID`) | yes | Transaction ID | example: "E9999901012341234123412345678900" |
| `analysis_details` | string (schema `AnalysisDetails`) | no | Analysis details | maxLength: 2000; example: "Details about the analysis" |
| `analysis_result` | string (schema `AnalysisResult`) | no | Analysis results | enum: ["AGREED", "DISAGREED", "PARTIALLY_ACCEPTED", "TOTALLY_ACCEPTED", "REJECTED"]; example: "AGREED" |
| `bacen_response_time` | string (schema `BacenResponseTime`) | no | Banco Central do Brasil (Central Bank of Brazil) response datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `infraction_data` | object (schema `presenter.InfractionData`) | no |  |  |
| `report_details` | string (schema `ReportDetails`) | no | Details about report | maxLength: 2000; example: "Details that can help the receiving participant to analyze the suspected violation" |
| `transaction_result` | string (schema `TransactionResult`) | no | Transaction result | enum: ["SETTLED", "REJECTED_PAYEE", "REJECTED_PAYER"]; example: "SETTLED" |
| `transaction_type` | string (schema `TransactionType`) | no | Transaction type:<br>  * `SPI` -  Transaction was created in the Central Bank system. <br>  * `INTERNAL` - Transaction was created internally in the Pismo system.<br> | enum: ["SPI", "INTERNAL"]; example: "SPI" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

202 Example `Creation request accepted and will processed async`:

```json
{
  "code": "EPDA0148",
  "message": "Infraction registration will continue asynchronously"
}
```

202 Example `Cancellation request accepted and will processed async`:

```json
{
  "code": "EPDA0149",
  "message": "Infraction cancel will continue asynchronously"
}
```

202 Example `Close request accepted and will processed async`:

```json
{
  "code": "EPDA0149",
  "message": "Infraction close will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `Tenant not found`:

```json
{
  "code": "EPDA0001",
  "message": "Missing x-tenant header."
}
```

400 Example `Invalid request infractionId`:

```json
{
  "code": "EPDA0070",
  "message": "Invalid request infraction report id"
}
```

400 Example `Invalid binding`:

```json
{
  "code": "EPDA0002",
  "message": "Failed to unmarshal request body"
}
```

400 Example `Rest marshal error`:

```json
{
  "code": "ECM0005",
  "message": "Failed to marshal request"
}
```

400 Example `Validate errors`:

```json
{
  "code": "EPDA0003",
  "message": "There are invalid fields when trying to validate request body.",
  "details": {
    "payload": [
      {
        "field": "InfractionClose.analysis_result",
        "message": "Field validation for 'analysis_result' failed on the 'oneof' tag"
      }
    ]
  }
}
```

400 Example `Rest bad request`:

```json
{
  "code": "ECM0002",
  "message": "Bad request while accessing an external resource"
}
```

400 Example `Rest unknown response status`:

```json
{
  "code": "ECM0003",
  "message": "Received response status %d was not expected"
}
```

##### Response 401

- Response header `x-cid`: Request tracking identifier. (string)
401 Example `Provider service error`:

```json
{
  "code": "EPDG0013",
  "message": "Unauthorized access to the provider service"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `Infraction not found`:

```json
{
  "code": "EPDA0049",
  "message": "Infraction report not found"
}
```

##### Response 429

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `Provider service communication error`:

```json
{
  "code": "EPDA0029",
  "message": "Internal errors while attempting to communicate with the provider service"
}
```

500 Example `Invalid client error`:

```json
{
  "code": "EPDG0005",
  "message": "Invalid Pix provider '{provider_name}'"
}
```

500 Example `Failed marshalling object`:

```json
{
  "code": "EPDG0006",
  "message": "Failed to marshal JSON object"
}
```

500 Example `Failed unmarshalling object`:

```json
{
  "code": "EPDG0007",
  "message": "Failed to unmarshal JSON object"
}
```

500 Example `Error reading response data`:

```json
{
  "code": "EPDG0010",
  "message": "I/O error while reading response data: '{details}'"
}
```

500 Example `Provider service error`:

```json
{
  "code": "EPDG0016",
  "message": "Provider service returned an internal error while trying to access the resource",
  "details": {
    "external": [
      {
        "code": "PBE315",
        "message": "Generic error"
      }
    ]
  }
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 503

- Response header `x-cid`: Request tracking identifier. (string)
503 Example `Provider service unavailable`:

```json
{
  "code": "EPDG0017",
  "message": "Provider service resource is unavailable"
}
```

503 Example `Provider authentication service unavailable`:

```json
{
  "code": "EPDG0021",
  "message": "Provider authentication service is unavailable"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0148` | Infraction registration will continue asynchronously |
| 202 | `EPDA0149` | Infraction cancel will continue asynchronously |
| 400 | `EPDA0001` | Missing x-tenant header. |
| 400 | `EPDA0070` | Invalid request infraction report id |
| 400 | `EPDA0002` | Failed to unmarshal request body |
| 400 | `ECM0005` | Failed to marshal request |
| 400 | `EPDA0003` | There are invalid fields when trying to validate request body. |
| 400 | `ECM0002` | Bad request while accessing an external resource |
| 400 | `ECM0003` | Received response status %d was not expected |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 404 | `EPDA0049` | Infraction report not found |
| 500 | `EPDA0029` | Internal errors while attempting to communicate with the provider service |
| 500 | `EPDG0005` | Invalid Pix provider '{provider_name}' |
| 500 | `EPDG0006` | Failed to marshal JSON object |
| 500 | `EPDG0007` | Failed to unmarshal JSON object |
| 500 | `EPDG0010` | I/O error while reading response data: '{details}' |
| 500 | `EPDG0016` | Provider service returned an internal error while trying to access the resource |
| 500 | `PBE315` | Generic error |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 503 | `EPDG0017` | Provider service resource is unavailable |
| 503 | `EPDG0021` | Provider authentication service is unavailable |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-infraction-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;401;403;404;429;500;502;503;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/infraction-reports/{id}/cancel operationId=post-v2-pix-infraction-cancel -->
### `POST /v2/pix/infraction-reports/{id}/cancel` — Cancel infraction report

- **operationId:** `post-v2-pix-infraction-cancel`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Infraction reports`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel the infraction report. 
>
> Only the participant who created the report can cancel it and the report's status **must** be `OPEN` or `ACKNOWLEDGED`.
>
> The operation is idempotent. If you try to cancel the report again with the same parameters, you will get the same response as the first time.
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting a success or failure event.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1" >Pix infraction status changed</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `id` | path | yes | string | Infraction report ID | format: "uuid" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InfractionReportResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Resource Not Found | `application/json`: object (schema `message.Message`) |
| 429 | Too many requests | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 503 | Service Unavailable | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `InfractionReportID`) | yes | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `transaction_id` | string (schema `InfractionTransactionID`) | yes | Original transaction's end to end ID. | example: "E9999901012341234123412345678900" |
| `reason` | string (schema `InfractionReason`) | yes | Reason for opening infraction report | enum: ["REFUND_REQUEST", "REFUND_CANCELLED"]; example: "REFUND_REQUEST" |
| `situation_type` | string (schema `InfractionReportSituation`) | yes | What gave rise to the infraction notification | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"]; example: "SCAM" |
| `status` | string (schema `InfractionReportStatus`) | yes | Infraction report status | enum: ["OPEN", "ACKNOWLEDGED", "CLOSED", "CANCELLED"]; example: "OPEN" |
| `reporter_participant` | string (schema `InfractionReporterParticipant`) | yes | Transaction payer participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value.<br> | format: "number"; example: "78265328" |
| `counterparty_participant` | string (schema `InfractionCounterpartyParticipant`) | yes | Transaction recipient participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value.<br> | format: "number"; example: "78265328" |
| `bacen_creation_datetime` | string (schema `BacenCreationDateTime`) | yes | Date of infraction report creation. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `bacen_last_modified_datetime` | string (schema `BacenLastModifiedDateTime`) | yes | Date of infraction report modification. RFC 3339  date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `details` | string (schema `InfractionDetails`) | no | Details that can help the receiving participant to analyze the suspected violation<br> | maxLength: 2000; example: "Details about infraction" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `infraction_amount` | number (schema `InfractionAmount`) | no | Infraction Amount. | example: 1050.44 |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

202 Example `Creation request accepted and will processed async`:

```json
{
  "code": "EPDA0148",
  "message": "Infraction registration will continue asynchronously"
}
```

202 Example `Cancellation request accepted and will processed async`:

```json
{
  "code": "EPDA0149",
  "message": "Infraction cancel will continue asynchronously"
}
```

202 Example `Close request accepted and will processed async`:

```json
{
  "code": "EPDA0149",
  "message": "Infraction close will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `Tenant not found`:

```json
{
  "code": "EPDA0001",
  "message": "Missing x-tenant header."
}
```

400 Example `Invalid request infraction id`:

```json
{
  "code": "EPDA0070",
  "message": "Invalid request infraction report id"
}
```

400 Example `Error cancel infraction`:

```json
{
  "code": "EPDA0073",
  "message": "Infraction cannot be cancel it is possible to only close the infraction"
}
```

##### Response 401

- Response header `x-cid`: Request tracking identifier. (string)
401 Example `Provider service error`:

```json
{
  "code": "EPDG0013",
  "message": "Unauthorized access to the provider service"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EPDA0009` (Missing required header 'x-tenant'):

```json
{
  "code": "EPDA0009",
  "message": "Missing required header 'x-tenant'"
}
```

403 Example `EPDA0010` (Missing required header 'x-account-id'):

```json
{
  "code": "EPDA0010",
  "message": "Missing required header 'x-account-id'"
}
```

403 Example `EPDA0152` (Missing required param 'id'):

```json
{
  "code": "EPDA0152",
  "message": "Missing required param 'id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `Provider service error`:

```json
{
  "code": "EPDA0049",
  "message": "Infraction report not found"
}
```

##### Response 429

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `Provider service communication error`:

```json
{
  "code": "EPDA0029",
  "message": "Internal errors while attempting to communicate with the provider service"
}
```

500 Example `Invalid client error`:

```json
{
  "code": "EPDG0005",
  "message": "Invalid Pix provider '{provider_name}'"
}
```

500 Example `Failed marshalling object`:

```json
{
  "code": "EPDG0006",
  "message": "Failed to marshal JSON object"
}
```

500 Example `Failed unmarshalling object`:

```json
{
  "code": "EPDG0007",
  "message": "Failed to unmarshal JSON object"
}
```

500 Example `Error reading response data`:

```json
{
  "code": "EPDG0010",
  "message": "I/O error while reading response data: '{details}'"
}
```

500 Example `Provider service error`:

```json
{
  "code": "EPDG0016",
  "message": "Provider service returned an internal error while trying to access the resource",
  "details": {
    "external": [
      {
        "code": "PBE315",
        "message": "Generic error"
      }
    ]
  }
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
}
```

##### Response 503

- Response header `x-cid`: Request tracking identifier. (string)
503 Example `Provider service unavailable`:

```json
{
  "code": "EPDG0017",
  "message": "Provider service resource is unavailable"
}
```

503 Example `Provider authentication service unavailable`:

```json
{
  "code": "EPDG0021",
  "message": "Provider authentication service is unavailable"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```

504 Example `Provider timeout`:

```json
{
  "code": "EPDG0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `EPDA0148` | Infraction registration will continue asynchronously |
| 202 | `EPDA0149` | Infraction cancel will continue asynchronously |
| 400 | `EPDA0001` | Missing x-tenant header. |
| 400 | `EPDA0070` | Invalid request infraction report id |
| 400 | `EPDA0073` | Infraction cannot be cancel it is possible to only close the infraction |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 404 | `EPDA0049` | Infraction report not found |
| 500 | `EPDA0029` | Internal errors while attempting to communicate with the provider service |
| 500 | `EPDG0005` | Invalid Pix provider '{provider_name}' |
| 500 | `EPDG0006` | Failed to marshal JSON object |
| 500 | `EPDG0007` | Failed to unmarshal JSON object |
| 500 | `EPDG0010` | I/O error while reading response data: '{details}' |
| 500 | `EPDG0016` | Provider service returned an internal error while trying to access the resource |
| 500 | `PBE315` | Generic error |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 503 | `EPDG0017` | Provider service resource is unavailable |
| 503 | `EPDG0021` | Provider authentication service is unavailable |
| 504 | `EPDA0000` | Timeout while executing the request |
| 504 | `EPDG0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-infraction-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-infraction-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;401;403;404;429;500;502;503;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/InfractionReportResponse -->
### Schema `InfractionReportResponse`

Pointer: `#/components/schemas/InfractionReportResponse`. Type: object (schema `InfractionReportResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `InfractionReportID`) | yes | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `transaction_id` | string (schema `InfractionTransactionID`) | yes | Original transaction's end to end ID. | example: "E9999901012341234123412345678900" |
| `reason` | string (schema `InfractionReason`) | yes | Reason for opening infraction report | enum: ["REFUND_REQUEST", "REFUND_CANCELLED"]; example: "REFUND_REQUEST" |
| `situation_type` | string (schema `InfractionReportSituation`) | yes | What gave rise to the infraction notification | enum: ["SCAM", "ACCOUNT_TAKEOVER", "COERCION", "FRAUDULENT_ACCESS", "OTHER", "UNKNOWN"]; example: "SCAM" |
| `status` | string (schema `InfractionReportStatus`) | yes | Infraction report status | enum: ["OPEN", "ACKNOWLEDGED", "CLOSED", "CANCELLED"]; example: "OPEN" |
| `reporter_participant` | string (schema `InfractionReporterParticipant`) | yes | Transaction payer participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value.<br> | format: "number"; example: "78265328" |
| `counterparty_participant` | string (schema `InfractionCounterpartyParticipant`) | yes | Transaction recipient participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value.<br> | format: "number"; example: "78265328" |
| `bacen_creation_datetime` | string (schema `BacenCreationDateTime`) | yes | Date of infraction report creation. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `bacen_last_modified_datetime` | string (schema `BacenLastModifiedDateTime`) | yes | Date of infraction report modification. RFC 3339  date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `details` | string (schema `InfractionDetails`) | no | Details that can help the receiving participant to analyze the suspected violation<br> | maxLength: 2000; example: "Details about infraction" |
| `contact_information` | object (schema `ContactInformation`) | no |  |  |
| `funds_recovery_id` | string (schema `FundsRecoveryId`) | no | Funds recovery identifier. <br><br>Returned from the [Create funds recovery](ref:post-create-funds-recovery) endpoint.<br> | example: "53D0F66A-BAB0-49D7-B7DC-807B82AABD8D" |
| `infraction_amount` | number (schema `InfractionAmount`) | no | Infraction Amount. | example: 1050.44 |

<!-- schema: #/components/schemas/message.Message -->
### Schema `message.Message`

Pointer: `#/components/schemas/message.Message`. Type: object (schema `message.Message`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

<!-- schema: #/components/schemas/ContactInformation -->
### Schema `ContactInformation`

Pointer: `#/components/schemas/ContactInformation`. Type: object (schema `ContactInformation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `phone` | string | yes | Contact phone number | maxLength: 16; example: "551154874551" |
| `email` | string | yes | Contact email | maxLength: 77; example: "polly_ester@email.com" |

<!-- schema: #/components/schemas/message.DetailMessage -->
### Schema `message.DetailMessage`

Pointer: `#/components/schemas/message.DetailMessage`. Type: object (schema `message.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `message.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `message.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `message.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/presenter.InfractionData -->
### Schema `presenter.InfractionData`

Pointer: `#/components/schemas/presenter.InfractionData`. Type: object (schema `presenter.InfractionData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credited_participant` | string (schema `CreditedParticipant`) | yes | Credited participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `debited_participant` | string (schema `DebitedParticipant`) | yes | Debited participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `infracting_account_data` | object (schema `presenter.InfractingAccountData`) | yes |  |  |
| `reported_by` | string (schema `InfractionReportedBy`) | yes | Who filed the infraction report | enum: ["DEBITED_PARTICIPANT", "CREDITED_PARTICIPANT"]; example: "DEBITED_PARTICIPANT" |
| `tax_id_number` | string (schema `TaxIdNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits. | minLength: 11; maxLength: 14; example: "123412341234" |
| `transaction_date` | string | yes | Transaction date time. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-01-17T10:00:00Z" |
| `key` | string (schema `Key`) | no | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |

<!-- schema: #/components/schemas/message.ExternalMessage -->
### Schema `message.ExternalMessage`

Pointer: `#/components/schemas/message.ExternalMessage`. Type: object (schema `message.ExternalMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Error code | example: "PBE315" |
| `message` | string | yes | Error message | example: "Generic error" |

<!-- schema: #/components/schemas/message.ParameterMessage -->
### Schema `message.ParameterMessage`

Pointer: `#/components/schemas/message.ParameterMessage`. Type: object (schema `message.ParameterMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Parameter in error | example: "query parameter" |
| `message` | string | yes | Error message | example: "Generic error" |

<!-- schema: #/components/schemas/message.PayloadMessage -->
### Schema `message.PayloadMessage`

Pointer: `#/components/schemas/message.PayloadMessage`. Type: object (schema `message.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Field in error | example: "Entity.field" |
| `message` | string | yes | Error messsage | example: "Generic error" |

<!-- schema: #/components/schemas/presenter.InfractingAccountData -->
### Schema `presenter.InfractingAccountData`

Pointer: `#/components/schemas/presenter.InfractingAccountData`. Type: object (schema `presenter.InfractingAccountData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `branch` | string (schema `Branch`) | no | Bank-assigned branch ID or ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | example: "011" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_management.yaml` | tag `Infraction reports`: GET /v2/pix/infraction-reports, POST /v2/pix/infraction-reports, POST /v2/pix/infraction-reports/{id}/close, POST /v2/pix/infraction-reports/{id}/cancel | https://github.com/PismoDevEx/pismo-api-specs | `7d7fee078ccf5569…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-epda` — Error codes: EPDA
- `KU-ERR-codes-epdg` — Error codes: EPDG
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
