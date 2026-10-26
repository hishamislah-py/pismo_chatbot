---
ku_id: KU-API-instant-payments-pix-management--anti-fraud
title: 'API reference: Instant payments - Pix management — Anti-fraud'
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
- post-v2-pix-fraud-marker-create
- get-v2-pix-fraud-marker
- post-v2-pix-fraud-marker-cancel
- post-v2-antifraud-statistics-key
- post-v2-antifraud-statistics-document-number
- post-list-fraud-markers
- get-v2-pix-statistics
related_kus:
- KU-ERR-codes-epda
- KU-ERR-codes-epdg
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-pix
specification_version: 0.0.1
---

# API reference: Instant payments - Pix management — Anti-fraud

**KU ID:** `KU-API-instant-payments-pix-management--anti-fraud` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Anti-fraud` in `api-specs/Instant_payments_-_Pix_management.yaml` (“Instant payments - Pix management”, version `0.0.1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage anti-fraud endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/pix/fraud-markers` | `post-v2-pix-fraud-marker-create` | Create fraud marker | no |
| `GET /v2/pix/fraud-markers/{id}` | `get-v2-pix-fraud-marker` | Get fraud marker | no |
| `POST /v2/pix/fraud-markers/{id}/cancel` | `post-v2-pix-fraud-marker-cancel` | Cancel fraud marker | no |
| `POST /v2/pix/statistics/keys` | `post-v2-antifraud-statistics-key` | Get anti-fraud statistics by key | no |
| `POST /v2/pix/statistics/persons` | `post-v2-antifraud-statistics-document-number` | Get anti-fraud statistics by document number | no |
| `POST /v2/pix/fraud-markers/list` | `post-list-fraud-markers` | List fraud markers | no |
| `GET /v2/pix/statistics` | `get-v2-pix-statistics` | Get PIX client statistics | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/fraud-markers operationId=post-v2-pix-fraud-marker-create -->
### `POST /v2/pix/fraud-markers` — Create fraud marker

- **operationId:** `post-v2-pix-fraud-marker-create`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Anti-fraud`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a fraud marker. 
>
> On PSP timeout, a `202 Accepted` response is returned with a fraud marker ID. The process continues asynchronously and, if it doesn't succeed, a failure event is emitted.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-fraud-marker-registration-1" >Fraud Marker registration event</a> or <a href="https://developers.pismo.io/events/docs/pix-dict-fraud-marker-registration-failure-1">failure event</a>.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: yes

> Fraud Marker

**Content type `*/*`** — schema: object (schema `FraudMarkerCreationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string | yes | User's tax ID number (CPF or CNPJ) associated with the fraud marker. |  |
| `fraud_type` | string | yes | Type of fraud. For fraud marking coming from infraction reports closed in API V1, the value `UNKNOWN` will appear. | enum: ["APPLICATION_FRAUD", "MULE_ACCOUNT", "SCAMMER_ACCOUNT", "OTHER", "UNKNOWN"]; example: "APPLICATION_FRAUD" |
| `key` | string | no | Key associated with fraud marker. It must be reported, if known | maxLength: 77 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `FraudMarkerResponse`) |
| 202 | Accepted. The process will be processed asynchronous and will send a event via SNS when OK | `application/json`: object (schema `FraudMarkerAcceptedResponse`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 409 | Conflict | `application/json`: object (schema `message.Message`) |
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
| `id` | string (schema `FraudMarkerID`) | yes | Fraud marker ID | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `fraud_type` | string (schema `FraudMarkerFraudType`) | yes | Verified fraud type | enum: ["APPLICATION_FRAUD", "MULE_ACCOUNT", "SCAMMER_ACCOUNT", "OTHER", "UNKNOWN"]; example: "APPLICATION_FRAUD" |
| `status` | string (schema `InfractionFraudMarkerStatus`) | yes | Fraud marker status | enum: ["REGISTERED", "CANCELLED"]; example: "REGISTERED" |
| `key` | string (schema `FraudMarkerKey`) | no | Key to which the fraud marker will be associated. It must be reported, if known | maxLength: 77 |
| `bacen_creation_datetime` | string (schema `BacenCreationDateTime`) | yes | Date of infraction report creation. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `bacen_last_modified_datetime` | string (schema `BacenLastModifiedDateTime`) | yes | Date of infraction report modification. RFC 3339  date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `FraudMarkerID`) | yes | Fraud marker ID | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |

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
        "field": "FraudMarkerCreationRequest.fraud_type",
        "message": "Field validation for 'fraud_type' failed on the 'oneof' tag"
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

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `Fraud marker already registered` (Fraud marker already registered with different value):

```json
{
  "code": "EPDA0166",
  "message": "Fraud marker already registered with different values for the idempotency key"
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
| 400 | `EPDA0002` | Failed to unmarshal request body |
| 400 | `EPDA0003` | There are invalid fields when trying to validate request body |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 409 | `EPDA0166` | Fraud marker already registered with different values for the idempotency key |
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
| `pix-dict-fraud-marker-registration-1` | https://developers.pismo.io/events/docs/pix-dict-fraud-marker-registration-1 |
| `pix-dict-fraud-marker-registration-failure-1` | https://developers.pismo.io/events/docs/pix-dict-fraud-marker-registration-failure-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;401;403;409;429;500;502;503;504`, has examples `True`, emits events `2`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v2/pix/fraud-markers/{id} operationId=get-v2-pix-fraud-marker -->
### `GET /v2/pix/fraud-markers/{id}` — Get fraud marker

- **operationId:** `get-v2-pix-fraud-marker`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Anti-fraud`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get fraud marker details

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `id` | path | yes | string | Fraud marker ID generated for a suspected fraudelent transaction. | format: "uuid" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FraudMarkerResponse`) |
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
| `id` | string (schema `FraudMarkerID`) | yes | Fraud marker ID | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `fraud_type` | string (schema `FraudMarkerFraudType`) | yes | Verified fraud type | enum: ["APPLICATION_FRAUD", "MULE_ACCOUNT", "SCAMMER_ACCOUNT", "OTHER", "UNKNOWN"]; example: "APPLICATION_FRAUD" |
| `status` | string (schema `InfractionFraudMarkerStatus`) | yes | Fraud marker status | enum: ["REGISTERED", "CANCELLED"]; example: "REGISTERED" |
| `key` | string (schema `FraudMarkerKey`) | no | Key to which the fraud marker will be associated. It must be reported, if known | maxLength: 77 |
| `bacen_creation_datetime` | string (schema `BacenCreationDateTime`) | yes | Date of infraction report creation. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `bacen_last_modified_datetime` | string (schema `BacenLastModifiedDateTime`) | yes | Date of infraction report modification. RFC 3339  date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |

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
  "code": "EPDA0167",
  "message": "Fraud marker not found"
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
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 404 | `EPDA0167` | Fraud marker not found |
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;429;500;502;503;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/fraud-markers/{id}/cancel operationId=post-v2-pix-fraud-marker-cancel -->
### `POST /v2/pix/fraud-markers/{id}/cancel` — Cancel fraud marker

- **operationId:** `post-v2-pix-fraud-marker-cancel`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Anti-fraud`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> The participant who created the fraud marker can call this endpoint. In the case of a fraud marker created as a result of closing an infraction report, the participant who created it can cancel it, in addition to the participant who closed the notification.
>
> On PSP timeout, a `202 Accepted` response with a fraud marker ID is returned. The process continues asynchronously and, if it doesn't succeed, a failure event is emitted.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-fraud-marker-status-change-1" >Fraud Marker registration event</a> or <a href="https://developers.pismo.io/events/docs/pix-dict-fraud-marker-status-change-failure-1">failure event</a>.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `id` | path | yes | string | Fraud marker ID generated for a suspected fraudelent transaction. | format: "uuid" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FraudMarkerResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
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
| `id` | string (schema `FraudMarkerID`) | yes | Fraud marker ID | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `fraud_type` | string (schema `FraudMarkerFraudType`) | yes | Verified fraud type | enum: ["APPLICATION_FRAUD", "MULE_ACCOUNT", "SCAMMER_ACCOUNT", "OTHER", "UNKNOWN"]; example: "APPLICATION_FRAUD" |
| `status` | string (schema `InfractionFraudMarkerStatus`) | yes | Fraud marker status | enum: ["REGISTERED", "CANCELLED"]; example: "REGISTERED" |
| `key` | string (schema `FraudMarkerKey`) | no | Key to which the fraud marker will be associated. It must be reported, if known | maxLength: 77 |
| `bacen_creation_datetime` | string (schema `BacenCreationDateTime`) | yes | Date of infraction report creation. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `bacen_last_modified_datetime` | string (schema `BacenLastModifiedDateTime`) | yes | Date of infraction report modification. RFC 3339  date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

202 Example `Request accepted and will processed async`:

```json
{
  "code": "EPDA0169",
  "message": "Request was accepted and gonna be processed asynchronously"
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
  "code": "EPDA0167",
  "message": "Fraud marker not found"
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
| 202 | `EPDA0169` | Request was accepted and gonna be processed asynchronously |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 404 | `EPDA0167` | Fraud marker not found |
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
| `pix-dict-fraud-marker-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-fraud-marker-status-change-1 |
| `pix-dict-fraud-marker-status-change-failure-1` | https://developers.pismo.io/events/docs/pix-dict-fraud-marker-status-change-failure-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;401;403;404;429;500;502;503;504`, has examples `True`, emits events `2`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/statistics/keys operationId=post-v2-antifraud-statistics-key -->
### `POST /v2/pix/statistics/keys` — Get anti-fraud statistics by key

- **operationId:** `post-v2-antifraud-statistics-key`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Anti-fraud`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets anti fraud statistics based on key.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Get anti-fraud statistics by key request body

**Content type `application/json`** — schema: object (schema `antifraud.StatisticsSearchByKeyRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string (schema `Key`) | no | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `antifraud.StatisticsSearchByKey`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `key_statistics` | object (schema `entry.KeyStatistics`) | no |  |  |
| `owner_statistics` | object (schema `entry.OwnerStatistics`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `Invalid key`:

```json
{
  "code": "EPDA0075",
  "message": "Invalid key"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
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

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0075` | Invalid key |
| 500 | `EPDG0006` | Failed to marshal JSON object |
| 500 | `EPDG0007` | Failed to unmarshal JSON object |
| 500 | `EPDG0010` | I/O error while reading response data: '{details}' |
| 504 | `EPDA0000` | Timeout while executing the request |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/statistics/persons operationId=post-v2-antifraud-statistics-document-number -->
### `POST /v2/pix/statistics/persons` — Get anti-fraud statistics by document number

- **operationId:** `post-v2-antifraud-statistics-document-number`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Anti-fraud`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Gets anti fraud statistics based on document number.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Get anti-fraud statistics request body

**Content type `application/json`** — schema: object (schema `antifraud.StatisticsSearchByDocumentNumberRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `antifraud.StatisticsSearchByDocumentNumber`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `person_statistics` | object (schema `entry.OwnerStatistics`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `Invalid key`:

```json
{
  "code": "EPDA0075",
  "message": "Invalid document number"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
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

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `Service timeout`:

```json
{
  "code": "EPDA0000",
  "message": "Timeout while executing the request"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0075` | Invalid document number |
| 500 | `EPDG0006` | Failed to marshal JSON object |
| 500 | `EPDG0007` | Failed to unmarshal JSON object |
| 500 | `EPDG0010` | I/O error while reading response data: '{details}' |
| 504 | `EPDA0000` | Timeout while executing the request |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/fraud-markers/list operationId=post-list-fraud-markers -->
### `POST /v2/pix/fraud-markers/list` — List fraud markers

- **operationId:** `post-list-fraud-markers`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Anti-fraud`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List fraud markers

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `useProvider` | query | no | string | Search fraud marker in provider? Default is `true`. | example: "true" |

#### Request body

Required: yes

> List fraud markers request

**Content type `*/*`** — schema: object (schema `ListFraudMarkersRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `key` | string (schema `Key`) | no | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `date_time_start` | string (schema `CreationDatetime`) | no | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `date_time_end` | string | no | Creation end date time. RFC 3339 date-time value. Must be greater than or equal to `date_time_start`.<br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `limit` | integer (schema `Limit`) | no | Maximum results to return. Default is `20`. Maximum is `200`. | default: 20; maximum: 200; example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListFraudMarkersResponse`) |
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
| `infraction_id` | string (schema `InfractionReportID`) | no | Infraction report ID (UUID) | format: "uuid"; maxLength: 36; example: "cfdff46e-5d58-45b8-b7aa-591a65f74444" |
| `response_date_time` | string (schema `ResponseDateTime`) | no | Response date time. RFC 3339 date-time value. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `has_more_elements` | boolean (schema `HasMoreElements`) | no | Are there more items? | example: true |
| `fraud_markers` | array of object (schema `ListFraudMarkersObject`) | no |  |  |

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
  "code": "EPDA0167",
  "message": "Fraud marker not found"
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
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 404 | `EPDA0167` | Fraud marker not found |
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;429;500;502;503;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v2/pix/statistics operationId=get-v2-pix-statistics -->
### `GET /v2/pix/statistics` — Get PIX client statistics

- **operationId:** `get-v2-pix-statistics`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Anti-fraud`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve client account aggregated PIX statistics from BACEN DICT. 
>
> **Statistics include:**
>
> - **SPI settlements**: count of settlements over the last 90 days, 12 months, and 60 months
> - **Fraud markers**: categorized fraud report counts (application frauds, mule accounts, scammer accounts, etc.)
> - **Infraction reports**: open reports, distinct reporters, and rejected reports counts
> - **Entries**: number of registered accounts linked to the client
>
> Statistics are pre-computed and cached. Use `force_update=true` to trigger a fresh
> computation from BACEN DICT.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `force_update` | query | no | boolean | Force a fresh computation of BACEN DICT statistics instead of returning cached results? Default is `false`. | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `statistic.GetClientStatisticsResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 429 | Too many requests | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `person_statistics` | object (schema `entry.OwnerStatistics`) | no |  |  |

200 Example `example`:

```json
{
  "person_statistics": {
    "spi": {
      "settlements": {
        "d90": 5,
        "m12": 62,
        "m60": 310
      },
      "watermark": "2024-01-01T00:00:00Z"
    },
    "fraud_markers": {
      "application_frauds": {
        "d90": 0,
        "m12": 1,
        "m60": 2
      },
      "mule_accounts": {
        "d90": 0,
        "m12": 0,
        "m60": 0
      },
      "scammer_accounts": {
        "d90": 0,
        "m12": 0,
        "m60": 0
      },
      "other_frauds": {
        "d90": 0,
        "m12": 0,
        "m60": 0
      },
      "unknown_frauds": {
        "d90": 0,
        "m12": 0,
        "m60": 0
      },
      "total_fraud_transaction_amount": {
        "d90": 0,
        "m12": 0,
        "m60": 0
      },
      "distinct_fraud_reporters": {
        "d90": 0,
        "m12": 0,
        "m60": 0
      },
      "watermark": "2024-01-01T00:00:00Z"
    },
    "infraction_reports": {
      "open_reports": 0,
      "open_reports_distinct_reporters": 0,
      "rejected_reports": {
        "d90": 0,
        "m12": 0,
        "m60": 0
      },
      "watermark": "2024-01-01T00:00:00Z"
    },
    "entries": {
      "registered_accounts": 3,
      "watermark": "2024-01-01T00:00:00Z"
    }
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
500 Example `EPDA0004` (Internal error):

```json
{
  "code": "EPDA0004",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 500 | `EPDA0004` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;429;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/message.Message -->
### Schema `message.Message`

Pointer: `#/components/schemas/message.Message`. Type: object (schema `message.Message`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

<!-- schema: #/components/schemas/message.DetailMessage -->
### Schema `message.DetailMessage`

Pointer: `#/components/schemas/message.DetailMessage`. Type: object (schema `message.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `message.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `message.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `message.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/entry.KeyStatistics -->
### Schema `entry.KeyStatistics`

Pointer: `#/components/schemas/entry.KeyStatistics`. Type: object (schema `entry.KeyStatistics`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `entries` | object (schema `entry.EntriesKey`) | no |  |  |
| `fraud_markers` | object (schema `entry.FraudMarkersKey`) | no |  |  |
| `infraction_reports` | object (schema `entry.InfractionReportsKey`) | no |  |  |
| `spi` | object (schema `entry.Spi`) | no | Data on settlements |  |

<!-- schema: #/components/schemas/entry.OwnerStatistics -->
### Schema `entry.OwnerStatistics`

Pointer: `#/components/schemas/entry.OwnerStatistics`. Type: object (schema `entry.OwnerStatistics`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `entries` | object (schema `entry.EntriesOwner`) | no |  |  |
| `fraud_markers` | object (schema `entry.FraudMarkersOwner`) | no |  |  |
| `infraction_reports` | object (schema `entry.InfractionReportsOwner`) | no |  |  |
| `spi` | object (schema `entry.Spi`) | no | Data on settlements |  |

<!-- schema: #/components/schemas/ListFraudMarkersObject -->
### Schema `ListFraudMarkersObject`

Pointer: `#/components/schemas/ListFraudMarkersObject`. Type: object (schema `ListFraudMarkersObject`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `FraudMarkerID`) | yes | Fraud marker ID | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `fraud_type` | string (schema `FraudMarkerFraudType`) | yes | Verified fraud type | enum: ["APPLICATION_FRAUD", "MULE_ACCOUNT", "SCAMMER_ACCOUNT", "OTHER", "UNKNOWN"]; example: "APPLICATION_FRAUD" |
| `status` | string (schema `InfractionFraudMarkerStatus`) | yes | Fraud marker status | enum: ["REGISTERED", "CANCELLED"]; example: "REGISTERED" |
| `key` | string (schema `FraudMarkerKey`) | no | Key to which the fraud marker will be associated. It must be reported, if known | maxLength: 77 |
| `creation_datetime` | string (schema `BacenCreationDateTime`) | no | Date of infraction report creation. RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `last_modified_datetime` | string (schema `BacenLastModifiedDateTime`) | no | Date of infraction report modification. RFC 3339  date-time value. For example -  `2023-04-12T23:20:50.52Z`. <br> | format: "date-time"; example: "2020-08-13T13:49:03Z" |

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

<!-- schema: #/components/schemas/entry.EntriesKey -->
### Schema `entry.EntriesKey`

Pointer: `#/components/schemas/entry.EntriesKey`. Type: object (schema `entry.EntriesKey`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `distinct_accounts` | object (schema `entry.Details`) | no | Event counters. |  |
| `watermark` | string (schema `Watermark`) | no | Last anti-fraud event's date and time. RFC 3339 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |

<!-- schema: #/components/schemas/entry.FraudMarkersKey -->
### Schema `entry.FraudMarkersKey`

Pointer: `#/components/schemas/entry.FraudMarkersKey`. Type: object (schema `entry.FraudMarkersKey`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application_frauds` | object (schema `entry.Details`) | no | Event counters. |  |
| `distinct_fraud_reporters` | object (schema `entry.Details`) | no | Event counters. |  |
| `mule_accounts` | object (schema `entry.Details`) | no | Event counters. |  |
| `other_frauds` | object (schema `entry.Details`) | no | Event counters. |  |
| `scammer_accounts` | object (schema `entry.Details`) | no | Event counters. |  |
| `total_fraud_transaction_amount` | object (schema `entry.Details`) | no | Event counters. |  |
| `unknown_frauds` | object (schema `entry.Details`) | no | Event counters. |  |
| `watermark` | string (schema `Watermark`) | no | Last anti-fraud event's date and time. RFC 3339 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |

<!-- schema: #/components/schemas/entry.InfractionReportsKey -->
### Schema `entry.InfractionReportsKey`

Pointer: `#/components/schemas/entry.InfractionReportsKey`. Type: object (schema `entry.InfractionReportsKey`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `rejected_reports` | object (schema `entry.Details`) | no | Event counters. |  |
| `open_reports` | integer (schema `OpenReports`) | no | Number of infringement notifications not yet completed or cancelled. | example: 45 |
| `open_reports_distinct_reporters` | integer (schema `OpenReportsDistinctReporters`) | no | Number of distinct participants creating infringement notifications that have not yet been completed or cancelled. | example: 34 |
| `watermark` | string (schema `Watermark`) | no | Last anti-fraud event's date and time. RFC 3339 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |

<!-- schema: #/components/schemas/entry.Spi -->
### Schema `entry.Spi`

Pointer: `#/components/schemas/entry.Spi`. Type: object (schema `entry.Spi`).

> Data on settlements

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `settlements` | object (schema `entry.Details`) | no | Event counters. |  |
| `watermark` | string (schema `Watermark`) | no | Last anti-fraud event's date and time. RFC 3339 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |

<!-- schema: #/components/schemas/entry.EntriesOwner -->
### Schema `entry.EntriesOwner`

Pointer: `#/components/schemas/entry.EntriesOwner`. Type: object (schema `entry.EntriesOwner`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `registered_accounts` | integer | no | Number of owner's accounts associated with currently registered keys. |  |
| `watermark` | string (schema `Watermark`) | no | Last anti-fraud event's date and time. RFC 3339 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |

<!-- schema: #/components/schemas/entry.FraudMarkersOwner -->
### Schema `entry.FraudMarkersOwner`

Pointer: `#/components/schemas/entry.FraudMarkersOwner`. Type: object (schema `entry.FraudMarkersOwner`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `application_frauds` | object (schema `entry.Details`) | no | Event counters. |  |
| `distinct_fraud_reporters` | object (schema `entry.Details`) | no | Event counters. |  |
| `mule_accounts` | object (schema `entry.Details`) | no | Event counters. |  |
| `other_frauds` | object (schema `entry.Details`) | no | Event counters. |  |
| `scammer_accounts` | object (schema `entry.Details`) | no | Event counters. |  |
| `total_fraud_transaction_amount` | object (schema `entry.Details`) | no | Event counters. |  |
| `unknown_frauds` | object (schema `entry.Details`) | no | Event counters. |  |
| `watermark` | string (schema `Watermark`) | no | Last anti-fraud event's date and time. RFC 3339 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |

<!-- schema: #/components/schemas/entry.InfractionReportsOwner -->
### Schema `entry.InfractionReportsOwner`

Pointer: `#/components/schemas/entry.InfractionReportsOwner`. Type: object (schema `entry.InfractionReportsOwner`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `open_reports` | integer (schema `OpenReports`) | no | Number of infringement notifications not yet completed or cancelled. | example: 45 |
| `open_reports_distinct_reporters` | integer (schema `OpenReportsDistinctReporters`) | no | Number of distinct participants creating infringement notifications that have not yet been completed or cancelled. | example: 34 |
| `rejected_reports` | object (schema `entry.Details`) | no | Event counters. |  |
| `watermark` | string (schema `Watermark`) | no | Last anti-fraud event's date and time. RFC 3339 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |

<!-- schema: #/components/schemas/entry.Details -->
### Schema `entry.Details`

Pointer: `#/components/schemas/entry.Details`. Type: object (schema `entry.Details`).

> Event counters.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `d90` | integer | no | Events occurring in last 90 days counter. | example: 86 |
| `m12` | integer | no | Events occurring in last 12 months counter. | example: 23 |
| `m60` | integer | no | Events occurring in last 60 months counter. | example: 12 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_management.yaml` | tag `Anti-fraud`: POST /v2/pix/fraud-markers, GET /v2/pix/fraud-markers/{id}, POST /v2/pix/fraud-markers/{id}/cancel, POST /v2/pix/statistics/keys, POST /v2/pix/statistics/persons, POST /v2/pix/fraud-markers/list, GET /v2/pix/statistics | https://github.com/PismoDevEx/pismo-api-specs | `7d7fee078ccf5569…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-epda` — Error codes: EPDA
- `KU-ERR-codes-epdg` — Error codes: EPDG
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
