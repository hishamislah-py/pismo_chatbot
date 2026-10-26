---
ku_id: KU-API-instant-payments-pix-management--claims
title: 'API reference: Instant payments - Pix management — Claims'
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
- get-dict-key-claims
- post-dict-key-claim
- post-confirm-dict-claim
- post-cancel-dict-claim
- post-complete-dict-claim
related_kus:
- KU-ERR-codes-epda
- KU-ERR-codes-epdg
- KU-EVT-catalogue-pix
- KU-EVT-pix-payments-data-events
- KU-PAY-pix-instant-payments
specification_version: 0.0.1
---

# API reference: Instant payments - Pix management — Claims

**KU ID:** `KU-API-instant-payments-pix-management--claims` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Claims` in `api-specs/Instant_payments_-_Pix_management.yaml` (“Instant payments - Pix management”, version `0.0.1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage key ownership and key portability endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/pix/claims` | `get-dict-key-claims` | List key claims | no |
| `POST /v2/pix/claims` | `post-dict-key-claim` | Create key claim | no |
| `POST /v2/pix/claims/confirm` | `post-confirm-dict-claim` | Confirm key claim | no |
| `POST /v2/pix/claims/cancel` | `post-cancel-dict-claim` | Cancel key claim | no |
| `POST /v2/pix/claims/complete` | `post-complete-dict-claim` | Complete key claim | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v2/pix/claims operationId=get-dict-key-claims -->
### `GET /v2/pix/claims` — List key claims

- **operationId:** `get-dict-key-claims`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Claims`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List key DICT claims

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `type` | query | no | string | Key claim type filter:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |
| `status` | query | no | string | Claim status filter | enum: ["OPEN", "WAITING_RESOLUTION", "CONFIRMED", "CANCELLED", "COMPLETED"]; example: "OPEN" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | List claims | `application/json`: object (schema `claim.ListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `claims` | array of object (schema `claim.ListItemResponse`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
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
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
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
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500;502;504`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/claims operationId=post-dict-key-claim -->
### `POST /v2/pix/claims` — Create key claim

- **operationId:** `post-dict-key-claim`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Claims`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a DICT claim for a key. 
>
> The Brazil Central Bank maintains Pix keys in the Diretório de Identificadores de Contas Transacionais (DICT), a national Pix key registry and database.
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronous, eventually emitting a claim successful creation event.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1" >Pix key claim status changed</a> event.
>
> For more information, refer to [Pix key transfer (key claim)](doc:pix-instant-payments#pix-key-transfer-key-claim).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: no

> Register DICT key request body

**Content type `application/json`** — schema: object (schema `claim.RegisterClaimRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `claimer_account` | object (schema `claim.Account`) | yes |  |  |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `type` | string (schema `ClaimType`) | yes | Key claim type:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |
| `name_type` | string (schema `NameType`) | no | Name type: <br>  * `REGISTRATION_NAME` - Name assigned at birth <br>  * `SOCIAL_NAME` - Preferred name, not necessarily `REGISTRATION_NAME`<br> | enum: ["REGISTRATION_NAME", "SOCIAL_NAME"]; example: "SOCIAL_NAME" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Claim registered | `application/json`: object (schema `claim.RegisterClaimResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bacen_response_time` | string (schema `BacenResponseTime`) | no | Banco Central do Brasil (Central Bank of Brazil) response datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `claim_id` | string (schema `ClaimID`) | no | Claim ID for key transfer. The Create key claim or Create DICT key claim endpoint returns this field. | example: "123e4567-e89b-12d3-a456-426655440000" |
| `claimer` | object (schema `claim.Owner`) | no |  |  |
| `claimer_account` | object (schema `claim.Account`) | no |  |  |
| `completion_period_end_datetime` | string (schema `CompletionPeriodEndDatetime`) | no | Completion period end for claim. Present for claim type `OWNERSHIP`. ISO 8601 format. | format: "date-time"; example: "2020-01-24T10:00:00Z" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `donor_participant` | string (schema `DonorParticipant`) | no | Donor participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `key` | string (schema `Key`) | no | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | no | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `last_modified_datetime` | string (schema `LastModifiedDatetime`) | no | Last modified datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `resolution_period_end_datetime` | string (schema `ResolutionPeriodEndDatetime`) | no | Resolution period end for claim. ISO 8601 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |
| `status` | string (schema `ClaimStatus`) | no | Claim status | enum: ["OPEN", "WAITING_RESOLUTION", "CONFIRMED", "CANCELLED", "COMPLETED"]; example: "OPEN" |
| `type` | string (schema `ClaimType`) | no | Key claim type:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |

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
  "code": "EPDA0180",
  "message": "Claim creation will continue asynchronously"
}
```

202 Example `Confirm request accepted and will processed async`:

```json
{
  "code": "EPDA0162",
  "message": "Claim confirmation will continue asynchronously"
}
```

202 Example `Cancel request accepted and will processed async`:

```json
{
  "code": "EPDA0160",
  "message": "Claim cancel will continue asynchronously"
}
```

202 Example `Complete request accepted and will processed async`:

```json
{
  "code": "EPDA0161",
  "message": "Claim complete will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
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
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
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
| 202 | `EPDA0180` | Claim creation will continue asynchronously |
| 202 | `EPDA0162` | Claim confirmation will continue asynchronously |
| 202 | `EPDA0160` | Claim cancel will continue asynchronously |
| 202 | `EPDA0161` | Claim complete will continue asynchronously |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-claim-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;401;403;404;500;502;504`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/claims/confirm operationId=post-confirm-dict-claim -->
### `POST /v2/pix/claims/confirm` — Confirm key claim

- **operationId:** `post-confirm-dict-claim`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Claims`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Confirm a DICT claim for a key.
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously and, when successful,  emits an event.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1" >Pix key claim status changed</a> event.
>
> For more information, refer to [Pix key transfer (key claim)](doc:pix-instant-payments#pix-key-transfer-key-claim).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: no

> Confirm DICT key request body

**Content type `application/json`** — schema: object (schema `claim.ConfirmClaimRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `claim_id` | string (schema `ClaimID`) | yes | Claim ID for key transfer. The Create key claim or Create DICT key claim endpoint returns this field. | example: "123e4567-e89b-12d3-a456-426655440000" |
| `reason` | string (schema `Reason`) | yes | Reason for request | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "BRANCH_TRANSFER", "RECONCILIATION", "FRAUD", "DEFAULT_OPERATION", "RFB_VALIDATION"]; example: "USER_REQUESTED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Claim confirmed | `application/json`: object (schema `claim.ConfirmClaimResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cancel_reason` | string (schema `ConfirmReason`) | yes | Confirm reason | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "FRAUD", "DEFAULT_OPERATION"]; example: "USER_REQUESTED" |
| `claim_id` | string (schema `ClaimID`) | yes | Claim ID for key transfer. The Create key claim or Create DICT key claim endpoint returns this field. | example: "123e4567-e89b-12d3-a456-426655440000" |
| `completion_period_end_datetime` | string (schema `CompletionPeriodEndDatetime`) | yes | Completion period end for claim. Present for claim type `OWNERSHIP`. ISO 8601 format. | format: "date-time"; example: "2020-01-24T10:00:00Z" |
| `confirm_reason` | string (schema `ConfirmReason`) | yes | Confirm reason | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "FRAUD", "DEFAULT_OPERATION"]; example: "USER_REQUESTED" |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `last_modified_datetime` | string (schema `LastModifiedDatetime`) | yes | Last modified datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `resolution_period_end_datetime` | string (schema `ResolutionPeriodEndDatetime`) | yes | Resolution period end for claim. ISO 8601 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |
| `status` | string (schema `ClaimStatus`) | yes | Claim status | enum: ["OPEN", "WAITING_RESOLUTION", "CONFIRMED", "CANCELLED", "COMPLETED"]; example: "OPEN" |
| `type` | string (schema `ClaimType`) | yes | Key claim type:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |
| `claimer` | object (schema `claim.ClaimerData`) | no |  |  |
| `claimer_account` | object (schema `claim.ClaimerAccountData`) | no |  |  |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `donor_participant` | string (schema `DonorParticipant`) | no | Donor participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `bacen_response_time` | string (schema `BacenResponseTime`) | no | Banco Central do Brasil (Central Bank of Brazil) response datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

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
  "code": "EPDA0180",
  "message": "Claim creation will continue asynchronously"
}
```

202 Example `Confirm request accepted and will processed async`:

```json
{
  "code": "EPDA0162",
  "message": "Claim confirmation will continue asynchronously"
}
```

202 Example `Cancel request accepted and will processed async`:

```json
{
  "code": "EPDA0160",
  "message": "Claim cancel will continue asynchronously"
}
```

202 Example `Complete request accepted and will processed async`:

```json
{
  "code": "EPDA0161",
  "message": "Claim complete will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
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
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
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
| 202 | `EPDA0180` | Claim creation will continue asynchronously |
| 202 | `EPDA0162` | Claim confirmation will continue asynchronously |
| 202 | `EPDA0160` | Claim cancel will continue asynchronously |
| 202 | `EPDA0161` | Claim complete will continue asynchronously |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-claim-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;403;404;500;502;504`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/claims/cancel operationId=post-cancel-dict-claim -->
### `POST /v2/pix/claims/cancel` — Cancel key claim

- **operationId:** `post-cancel-dict-claim`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Claims`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel a key's DICT claim. 
>
> The table below defines, depending on the reason and type, who can cancel. 
>
> For more information, refer to <a href="https://developers.pismo.io/pismo-docs/docs/pix-instant-payments#pix-key-transfer-key-claim" >Pix key transfer (key claim)</a>
>
> * `OWNERSHIP` - Transfer key ownership between users in the same or another bank. 
>
> * `PORTABILITY` - Transfer key ownership for the same user to another bank.
>
>
> <table border="1">
> <tr>
> <th> </th>
> <th colspan="2"> OWNERSHIP </th>
> <th colspan="3"> PORTABILITY </th>
> </tr>
> <tr>
> <th> Reason </th>
> <th> Donor </th>
> <th> Claimer </th>
> <th> Donor </th>
> <th colspan="2"> Claimer </th>
> </tr>
> <tr>
> <th colspan=4>&nbsp</td>
> <th>WAITING_RESOLUTION</th>
> <th>CONFIRMED</th>
> <tr bgcolor="#FFFAFA">
> <td>USER_REQUESTED</td>
> <td></td>
> <td align="center">√</td>
> <td align="center">√</td>
> <td align="center">√</td>
> <td aligm="center">&nbsp;</td>
> </tr>
> <tr>
> <td>ACCOUNT_CLOSURE</td>
> <td align="center">√</td>
> <td align="center">√</td>
> <td align="center"></td>
> <td align="center">√</td>
> </tr>
> <tr bgcolor="#FFFAFA">
> <td>FRAUD</td>
> <td align="center">√</td>
> <td align="center">√</td>
> <td align="center">√</td>
> <td align="center">√</td>
> <td align="center">√</td>
> </tr>
> <tr>
> <td>DEFAULT_OPERATION</td>
> <td align="center"></td>
> <td align="center">√</td>
> <td align="center">√</td>
> <td align="center"></td>
> </tr>
> <tr bgcolor="#FFFAFA">
> <td>RECONCILIATION</td>
> <td align="center"></td>
> <td align="center"></td>
> <td align="center"></td>
> <td align="center">√</td>
>  <td align="center">√</td>
> </tr>
> </table>
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting an event if it succeeds.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1" >Pix key claim status changed</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: no

> Register DICT key request body

**Content type `application/json`** — schema: object (schema `claim.CancelClaimRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `claim_id` | string (schema `ClaimID`) | yes | Claim ID for key transfer. The Create key claim or Create DICT key claim endpoint returns this field. | example: "123e4567-e89b-12d3-a456-426655440000" |
| `reason` | string (schema `Reason`) | yes | Reason for request | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "BRANCH_TRANSFER", "RECONCILIATION", "FRAUD", "DEFAULT_OPERATION", "RFB_VALIDATION"]; example: "USER_REQUESTED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Claim cancelled | `application/json`: object (schema `claim.CancelClaimResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cancel_reason` | string (schema `Reason`) | yes | Reason for request | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "BRANCH_TRANSFER", "RECONCILIATION", "FRAUD", "DEFAULT_OPERATION", "RFB_VALIDATION"]; example: "USER_REQUESTED" |
| `confirm_reason` | string (schema `Reason`) | yes | Reason for request | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "BRANCH_TRANSFER", "RECONCILIATION", "FRAUD", "DEFAULT_OPERATION", "RFB_VALIDATION"]; example: "USER_REQUESTED" |
| `bacen_response_time` | string (schema `BacenResponseTime`) | no | Banco Central do Brasil (Central Bank of Brazil) response datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `claim_id` | string (schema `ClaimID`) | no | Claim ID for key transfer. The Create key claim or Create DICT key claim endpoint returns this field. | example: "123e4567-e89b-12d3-a456-426655440000" |
| `claimer` | object (schema `claim.ClaimerData`) | no |  |  |
| `claimer_account` | object (schema `claim.ClaimerAccountData`) | no |  |  |
| `completion_period_end_datetime` | string (schema `CompletionPeriodEndDatetime`) | no | Completion period end for claim. Present for claim type `OWNERSHIP`. ISO 8601 format. | format: "date-time"; example: "2020-01-24T10:00:00Z" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `donor_participant` | string (schema `DonorParticipant`) | no | Donor participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "99999011" |
| `key` | string (schema `Key`) | no | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | no | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `last_modified_datetime` | string (schema `LastModifiedDatetime`) | no | Last modified datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `resolution_period_end_datetime` | string (schema `ResolutionPeriodEndDatetime`) | no | Resolution period end for claim. ISO 8601 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |
| `status` | string (schema `ClaimStatus`) | no | Claim status | enum: ["OPEN", "WAITING_RESOLUTION", "CONFIRMED", "CANCELLED", "COMPLETED"]; example: "OPEN" |
| `type` | string (schema `ClaimType`) | no | Key claim type:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |

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
  "code": "EPDA0180",
  "message": "Claim creation will continue asynchronously"
}
```

202 Example `Confirm request accepted and will processed async`:

```json
{
  "code": "EPDA0162",
  "message": "Claim confirmation will continue asynchronously"
}
```

202 Example `Cancel request accepted and will processed async`:

```json
{
  "code": "EPDA0160",
  "message": "Claim cancel will continue asynchronously"
}
```

202 Example `Complete request accepted and will processed async`:

```json
{
  "code": "EPDA0161",
  "message": "Claim complete will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
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
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
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
| 202 | `EPDA0180` | Claim creation will continue asynchronously |
| 202 | `EPDA0162` | Claim confirmation will continue asynchronously |
| 202 | `EPDA0160` | Claim cancel will continue asynchronously |
| 202 | `EPDA0161` | Claim complete will continue asynchronously |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-claim-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;403;404;500;502;504`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/claims/complete operationId=post-complete-dict-claim -->
### `POST /v2/pix/claims/complete` — Complete key claim

- **operationId:** `post-complete-dict-claim`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Claims`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Complete a DICT claim for a key.  
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting an event if it succeeds.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1" >Pix key claim status changed</a> event.
>
> For more information, refer to [Pix key transfer (key claim)](doc:pix-instant-payments#pix-key-transfer-key-claim).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: no

> Register DICT key request body

**Content type `application/json`** — schema: object (schema `claim.CompleteClaimRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `claim_id` | string (schema `ClaimID`) | yes | Claim ID for key transfer. The Create key claim or Create DICT key claim endpoint returns this field. | example: "123e4567-e89b-12d3-a456-426655440000" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Claim completed | `application/json`: object (schema `claim.CompleteClaimResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 500 | Internal server errpr | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `claim_id` | string (schema `ClaimID`) | yes | Claim ID for key transfer. The Create key claim or Create DICT key claim endpoint returns this field. | example: "123e4567-e89b-12d3-a456-426655440000" |
| `completion_period_end_datetime` | string (schema `CompletionPeriodEndDatetime`) | yes | Completion period end for claim. Present for claim type `OWNERSHIP`. ISO 8601 format. | format: "date-time"; example: "2020-01-24T10:00:00Z" |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `creation_datetime` | string (schema `CreationDatetime`) | yes | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `confirm_reason` | string (schema `ConfirmReason`) | yes | Confirm reason | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "FRAUD", "DEFAULT_OPERATION"]; example: "USER_REQUESTED" |
| `last_modified_datetime` | string (schema `LastModifiedDatetime`) | yes | Last modified datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `resolution_period_end_datetime` | string (schema `ResolutionPeriodEndDatetime`) | yes | Resolution period end for claim. ISO 8601 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |
| `status` | string (schema `ClaimStatus`) | yes | Claim status | enum: ["OPEN", "WAITING_RESOLUTION", "CONFIRMED", "CANCELLED", "COMPLETED"]; example: "OPEN" |
| `type` | string (schema `ClaimType`) | yes | Key claim type:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |
| `claimer` | object (schema `claim.ClaimerData`) | no |  |  |
| `claimer_account` | object (schema `claim.ClaimerAccountData`) | no |  |  |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `donor_participant` | string (schema `Participant`) | no | Participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "00115678" |
| `bacen_response_time` | string (schema `BacenResponseTime`) | no | Banco Central do Brasil (Central Bank of Brazil) response datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

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
  "code": "EPDA0180",
  "message": "Claim creation will continue asynchronously"
}
```

202 Example `Confirm request accepted and will processed async`:

```json
{
  "code": "EPDA0162",
  "message": "Claim confirmation will continue asynchronously"
}
```

202 Example `Cancel request accepted and will processed async`:

```json
{
  "code": "EPDA0160",
  "message": "Claim cancel will continue asynchronously"
}
```

202 Example `Complete request accepted and will processed async`:

```json
{
  "code": "EPDA0161",
  "message": "Claim complete will continue asynchronously"
}
```

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
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
##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `Provider authentication service error`:

```json
{
  "code": "EPDG0020",
  "message": "Provider authentication service is unable to complete the request"
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
| 202 | `EPDA0180` | Claim creation will continue asynchronously |
| 202 | `EPDA0162` | Claim confirmation will continue asynchronously |
| 202 | `EPDA0160` | Claim cancel will continue asynchronously |
| 202 | `EPDA0161` | Claim complete will continue asynchronously |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 502 | `EPDG0020` | Provider authentication service is unable to complete the request |
| 504 | `EPDA0000` | Timeout while executing the request |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-claim-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-claim-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;403;404;500;502;504`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/claim.ListItemResponse -->
### Schema `claim.ListItemResponse`

Pointer: `#/components/schemas/claim.ListItemResponse`. Type: object (schema `claim.ListItemResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | string (schema `AccountID`) | yes | Pismo account ID | example: "8675309" |
| `claim_id` | string (schema `ClaimID`) | yes | Claim ID for key transfer. The Create key claim or Create DICT key claim endpoint returns this field. | example: "123e4567-e89b-12d3-a456-426655440000" |
| `claim_type` | string (schema `ClaimType`) | yes | Key claim type:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |
| `claimer` | object (schema `claim.Claimer`) | yes |  |  |
| `claimer_account` | object (schema `claim.ClaimerAccount`) | yes |  |  |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `last_modified` | string (schema `LastModifiedDatetime`) | yes | Last modified datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `status` | string (schema `ClaimStatus`) | yes | Claim status | enum: ["OPEN", "WAITING_RESOLUTION", "CONFIRMED", "CANCELLED", "COMPLETED"]; example: "OPEN" |
| `creation_datetime` | string (schema `CreationDatetime`) | yes | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `resolution_period_end` | string (schema `ResolutionPeriodEndDatetime`) | yes | Resolution period end for claim. ISO 8601 format. | format: "date-time"; example: "2020-01-17T10:00:00Z" |
| `reason` | string (schema `Reason`) | no | Reason for request | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "BRANCH_TRANSFER", "RECONCILIATION", "FRAUD", "DEFAULT_OPERATION", "RFB_VALIDATION"]; example: "USER_REQUESTED" |
| `completion_period_end` | string (schema `CompletionPeriodEndDatetime`) | no | Completion period end for claim. Present for claim type `OWNERSHIP`. ISO 8601 format. | format: "date-time"; example: "2020-01-24T10:00:00Z" |

<!-- schema: #/components/schemas/message.Message -->
### Schema `message.Message`

Pointer: `#/components/schemas/message.Message`. Type: object (schema `message.Message`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

<!-- schema: #/components/schemas/claim.Account -->
### Schema `claim.Account`

Pointer: `#/components/schemas/claim.Account`. Type: object (schema `claim.Account`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br>  `CACC` - Checking account<br>  `SVGS` - Savings account<br>  `TRAN` - Transactional account (Brazil only). Also known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking. <br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `branch` | string (schema `Branch`) | yes | Bank-assigned branch ID or ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | example: "011" |
| `participant` | string (schema `Participant`) | no | Participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "00115678" |
| `opening_datetime` | string (schema `OpeningDatetime`) | yes | Opening date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

<!-- schema: #/components/schemas/claim.Owner -->
### Schema `claim.Owner`

Pointer: `#/components/schemas/claim.Owner`. Type: object (schema `claim.Owner`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `name` | string (schema `PersonName`) | yes | Person's name | maxLength: 100; example: "Jerry Atrick" |
| `type` | string (schema `ClaimType`) | yes | Key claim type:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |
| `trade_name` | string (schema `TradeName`) | no | Name under which the business operates. Not necessarily the same as the legal name. | maxLength: 100; example: "Acme Widgets" |

<!-- schema: #/components/schemas/message.DetailMessage -->
### Schema `message.DetailMessage`

Pointer: `#/components/schemas/message.DetailMessage`. Type: object (schema `message.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `message.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `message.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `message.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/claim.ClaimerData -->
### Schema `claim.ClaimerData`

Pointer: `#/components/schemas/claim.ClaimerData`. Type: object (schema `claim.ClaimerData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `name` | string (schema `PersonName`) | yes | Person's name | maxLength: 100; example: "Jerry Atrick" |
| `type` | string (schema `PersonType`) | yes | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `trade_name` | string (schema `TradeName`) | no | Name under which the business operates. Not necessarily the same as the legal name. | maxLength: 100; example: "Acme Widgets" |

<!-- schema: #/components/schemas/claim.ClaimerAccountData -->
### Schema `claim.ClaimerAccountData`

Pointer: `#/components/schemas/claim.ClaimerAccountData`. Type: object (schema `claim.ClaimerAccountData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br>  `CACC` - Checking account<br>  `SVGS` - Savings account<br>  `TRAN` - Transactional account (Brazil only). Also known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking. <br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `opening_datetime` | string (schema `OpeningDatetime`) | yes | Opening date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `branch` | string (schema `Branch`) | no | Bank-assigned branch ID or ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | example: "011" |
| `participant` | string (schema `Participant`) | no | Participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "00115678" |

<!-- schema: #/components/schemas/claim.Claimer -->
### Schema `claim.Claimer`

Pointer: `#/components/schemas/claim.Claimer`. Type: object (schema `claim.Claimer`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `name` | string (schema `PersonName`) | yes | Person's name | maxLength: 100; example: "Jerry Atrick" |
| `trade_name` | string (schema `TradeName`) | no | Name under which the business operates. Not necessarily the same as the legal name. | maxLength: 100; example: "Acme Widgets" |
| `type` | string (schema `ClaimType`) | no | Key claim type:<br><br>* `OWNERSHIP` - Transfers key ownership between individuals in the same or another bank.<br>* `PORTABILITY`- Transfers key ownership for the same individual to another bank.<br> | enum: ["OWNERSHIP", "PORTABILITY"]; example: "OWNERSHIP" |

<!-- schema: #/components/schemas/claim.ClaimerAccount -->
### Schema `claim.ClaimerAccount`

Pointer: `#/components/schemas/claim.ClaimerAccount`. Type: object (schema `claim.ClaimerAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br>  `CACC` - Checking account<br>  `SVGS` - Savings account<br>  `TRAN` - Transactional account (Brazil only). Also known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking. <br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `opening_datetime` | string (schema `OpeningDatetime`) | yes | Opening date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `participant` | string (schema `Participant`) | yes | Participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "00115678" |
| `branch` | string (schema `Branch`) | no | Bank-assigned branch ID or ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | example: "011" |

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

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_management.yaml` | tag `Claims`: GET /v2/pix/claims, POST /v2/pix/claims, POST /v2/pix/claims/confirm, POST /v2/pix/claims/cancel, POST /v2/pix/claims/complete | https://github.com/PismoDevEx/pismo-api-specs | `7d7fee078ccf5569…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-epda` — Error codes: EPDA
- `KU-ERR-codes-epdg` — Error codes: EPDG
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
