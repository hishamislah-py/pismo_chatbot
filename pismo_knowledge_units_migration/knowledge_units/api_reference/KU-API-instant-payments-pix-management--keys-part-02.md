---
ku_id: KU-API-instant-payments-pix-management--keys-part-02
title: 'API reference: Instant payments - Pix management — Keys (part 2 of 2)'
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
operations:
- post-v2-pix-keys-search
- post-v2-pix-keys-validate
- post-check-dict-keys
related_kus:
- KU-ERR-codes-epda
- KU-ERR-codes-epdg
- KU-ERR-codes-esmg-to-whis
specification_version: 0.0.1
---

# API reference: Instant payments - Pix management — Keys (part 2 of 2)

**KU ID:** `KU-API-instant-payments-pix-management--keys-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Keys` in `api-specs/Instant_payments_-_Pix_management.yaml` (“Instant payments - Pix management”, version `0.0.1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage DICT keys endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/pix/keys/search` | `post-v2-pix-keys-search` | Get key | no |
| `POST /v2/pix/keys/validate` | `post-v2-pix-keys-validate` | Validate key | no |
| `POST /v2/pix/keys/check` | `post-check-dict-keys` | Check DICT keys | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/keys/search operationId=post-v2-pix-keys-search -->
### `POST /v2/pix/keys/search` — Get key

- **operationId:** `post-v2-pix-keys-search`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Keys`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Searches for a DICT key entry returning the owner information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Search a key

**Content type `application/json`** — schema: object (schema `presenter.SearchRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |

Example `Searching by CPF key`:

```json
{
  "key": "97361452043"
}
```

Example `Searching by CNPJ Key`:

```json
{
  "key": "73901114000186"
}
```

Example `Searching by Email Key`:

```json
{
  "key": "email@email.com"
}
```

Example `Searching by Phone Key`:

```json
{
  "key": "+5511987654321"
}
```

Example `Searching by EVP Key`:

```json
{
  "key": "8d33a43c-0d22-4974-9652-30c80f2d6b0e"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.SearchResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Resource Not Found | `application/json`: object (schema `message.Message`) |
| 409 | Conflict | `application/json`: object (schema `message.Message`) |
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
| `org_id` | string (schema `OrgID`) | no | Organization/tenant ID. | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `account_id` | string (schema `AccountID`) | no | Pismo account ID | example: "8675309" |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `bank_account` | object (schema `presenter.BankAccount`) | yes |  |  |
| `owner` | object (schema `presenter.Owner`) | no |  |  |
| `creation_datetime` | string (schema `CreationDatetime`) | yes | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `ownership_datetime` | string (schema `OwnershipDatetime`) | no | Ownership date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `claim_requested_datetime` | string (schema `ClaimRequestedDatetime`) | no | Claim requested date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

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
  "code": "EPDG0014",
  "message": "Resource not found on the provider service",
  "details": {
    "external": [
      {
        "code": "PBE353",
        "message": "Entity not found"
      }
    ]
  }
}
```

404 Example `Account not found`:

```json
{
  "code": "EPDA0024",
  "message": "Account not found for ID {account_id}"
}
```

404 Example `Key not found`:

```json
{
  "code": "EPDA0026",
  "message": "Key not found"
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `Account blocked cancelled create` (Account status blocked or cancelled):

```json
{
  "code": "EPDA0028",
  "message": "Account status blocked or cancelled"
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
| 404 | `EPDG0014` | Resource not found on the provider service |
| 404 | `PBE353` | Entity not found |
| 404 | `EPDA0024` | Account not found for ID {account_id} |
| 404 | `EPDA0026` | Key not found |
| 409 | `EPDA0028` | Account status blocked or cancelled |
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;409;429;500;502;503;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/keys/validate operationId=post-v2-pix-keys-validate -->
### `POST /v2/pix/keys/validate` — Validate key

- **operationId:** `post-v2-pix-keys-validate`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Keys`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

>
> Validates a key locally (if Pismo holds the ownership of it) or directly in DICT (for external keys). It returns related information along with the `end_to_end_id` you are **required** to pass to start a Pix transaction with the [Perform pix-out transfer](ref:post-pix-out-transfer) endpoint.
>
> This call should only be used to initate a payment, it does not return key information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Validate Key

**Content type `application/json`** — schema: object (schema `presenter.ValidateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `include_statistics` | boolean | no | Include statistics |  |

Example `CPF Key Search`:

```json
{
  "key": "97361452043"
}
```

Example `CNPJ Key Search`:

```json
{
  "key": "73901114000186"
}
```

Example `Email Key Search`:

```json
{
  "key": "email@email.com"
}
```

Example `Phone Key Search`:

```json
{
  "key": "+5511987654321"
}
```

Example `EVP Key Search`:

```json
{
  "key": "8d33a43c-0d22-4974-9652-30c80f2d6b0e"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.ValidateResponse`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 409 | Conflict | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bank_account` | object (schema `presenter.BankAccount`) | yes |  |  |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `creation_datetime` | string (schema `CreationDatetime`) | no | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `key` | string (schema `Key`) | no | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_statistics` | object (schema `entry.KeyStatistics`) | no |  |  |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The end_to_end_id is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "132cca0f6a816dd5be409256b3662343" |
| `internal` | boolean | no | Is Pismo validating the key internally? | example: false |
| `owner` | object (schema `presenter.Owner`) | no |  |  |
| `ownership_datetime` | string (schema `OwnershipDatetime`) | no | Ownership date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `owner_statistics` | object (schema `entry.OwnerStatistics`) | no |  |  |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `claim_requested_datetime` | string (schema `ClaimRequestedDatetime`) | no | Claim requested date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EPDA0011` (Missing required header: 'x-account-id'):

```json
{
  "code": "EPDA0011",
  "message": "Missing required header: 'x-account-id'"
}
```

400 Example `EPDA0002` (Bad Request):

```json
{
  "code": "EPDA0002",
  "message": "Bad Request"
}
```

400 Example `EPDA0049` (Validation error):

```json
{
  "code": "EPDA0049",
  "message": "Validation error"
}
```

400 Example `EPDA0139` (Participant not found for organization):

```json
{
  "code": "EPDA0139",
  "message": "Participant not found for organization"
}
```

400 Example `EPDA01815` (Entity's account customer id is null):

```json
{
  "code": "EPDA01815",
  "message": "Entity's account customer id is null"
}
```

400 Example `ESPI00008` (Auth - API returned 4xx error):

```json
{
  "code": "ESPI00008",
  "message": "Auth - API returned 4xx error"
}
```

400 Example `ESPI00010` (Provider client error):

```json
{
  "code": "ESPI00010",
  "message": "Dict - API returned 4xx error",
  "details": {
    "external": [
      {
        "code": "PROVIDER_ERROR_CODE",
        "message": "Provider error message"
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

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EPDA0139` (Participant not found for organization):

```json
{
  "code": "EPDA0139",
  "message": "Participant not found for organization"
}
```

404 Example `ESPI00014` (Key not found on provider):

```json
{
  "code": "ESPI00014",
  "message": "Dict - API key not found"
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `EPDA0008` (Account blocked or cancelled):

```json
{
  "code": "EPDA0008",
  "message": "Account blocked or cancelled"
}
```

409 Example `ESPI00029` (Provider timeout):

```json
{
  "code": "ESPI00029",
  "message": "Provider timeout"
}
```

409 Example `ESPI00030` (Provider server error):

```json
{
  "code": "ESPI00030",
  "message": "Dict - API returned 5xx error",
  "details": {
    "external": [
      {
        "code": "PROVIDER_ERROR_CODE",
        "message": "Provider error message"
      }
    ]
  }
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EPDA0004` (Internal error):

```json
{
  "code": "EPDA0004",
  "message": "Internal error"
}
```

500 Example `ESPI00007` (Auth - API returned 5xx error):

```json
{
  "code": "ESPI00007",
  "message": "Auth - API returned 5xx error"
}
```

500 Example `ESPI00002` (Internal error):

```json
{
  "code": "ESPI00002",
  "message": "Internal error"
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `EPDA0018` (SPI Gateway - API returned error):

```json
{
  "code": "EPDA0018",
  "message": "SPI Gateway - API returned error"
}
```

502 Example `ESPI00005` (HTTP error):

```json
{
  "code": "ESPI00005",
  "message": "HTTP error"
}
```

502 Example `ESPI00009` (Provider bad gateway):

```json
{
  "code": "ESPI00009",
  "message": "Dict - API returned 5xx error"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `EPDA0030` (SPI Gateway - API returned a timeout error):

```json
{
  "code": "EPDA0030",
  "message": "SPI Gateway - API returned a timeout error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0011` | Missing required header: 'x-account-id' |
| 400 | `EPDA0002` | Bad Request |
| 400 | `EPDA0049` | Validation error |
| 400 | `EPDA0139` | Participant not found for organization |
| 400 | `EPDA01815` | Entity's account customer id is null |
| 400 | `ESPI00008` | Auth - API returned 4xx error |
| 400 | `ESPI00010` | Dict - API returned 4xx error |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 404 | `EPDA0139` | Participant not found for organization |
| 404 | `ESPI00014` | Dict - API key not found |
| 409 | `EPDA0008` | Account blocked or cancelled |
| 409 | `ESPI00029` | Provider timeout |
| 409 | `ESPI00030` | Dict - API returned 5xx error |
| 500 | `EPDA0004` | Internal error |
| 500 | `ESPI00007` | Auth - API returned 5xx error |
| 500 | `ESPI00002` | Internal error |
| 502 | `EPDA0018` | SPI Gateway - API returned error |
| 502 | `ESPI00005` | HTTP error |
| 502 | `ESPI00009` | Dict - API returned 5xx error |
| 504 | `EPDA0030` | SPI Gateway - API returned a timeout error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;409;500;502;504`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/keys/check operationId=post-check-dict-keys -->
### `POST /v2/pix/keys/check` — Check DICT keys

- **operationId:** `post-check-dict-keys`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Keys`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Check that a list of key(s) exist in DICT, a Brazilian national Pix registery and database. Keys can be generated from an email address, a mobile phone number, a Tax ID number, or an EVP (virtual payment address).     

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization/tenant ID | example: "TN-34778262-f4f0-464d-b4c6-a14e2dc6f4be" |
| `x-cid` | header | no | string | The Correlation IDentifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated.<br> | example: "B20220921145635222303062944CA66F" |
| `x-account-id` | header | no | string | Pismo account ID | example: "8675309" |

#### Request body

Required: yes

> CheckRequest Body

**Content type `application/json`** — schema: object (schema `entry.CheckRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `keys` | array of object (schema `entry.Key`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | CheckResponse Body | `application/json`: object (schema `entry.CheckResponse`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Resource Not Found | `application/json`: object (schema `message.Message`) |
| 409 | Conflict | `application/json`: object (schema `message.Message`) |
| 429 | Too many requests | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 503 | Service Unavailable | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `keys` | array of object (schema `entry.KeyResponse`) | no |  |  |

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
        "field": "ValidateKeyRequest.key",
        "message": "Field validation for 'key' failed on the 'oneof' tag"
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

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `Provider service error`:

```json
{
  "code": "EPDG0014",
  "message": "Resource not found on the provider service",
  "details": {
    "external": [
      {
        "code": "PBE353",
        "message": "Entry not found"
      }
    ]
  }
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `Account blocked cancelled create` (Account status blocked or cancelled):

```json
{
  "code": "EPDA0028",
  "message": "Account status blocked or cancelled"
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
| 404 | `EPDG0014` | Resource not found on the provider service |
| 404 | `PBE353` | Entry not found |
| 409 | `EPDA0028` | Account status blocked or cancelled |
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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;409;429;500;502;503;504`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/presenter.BankAccount -->
### Schema `presenter.BankAccount`

Pointer: `#/components/schemas/presenter.BankAccount`. Type: object (schema `presenter.BankAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `participant` | string (schema `Participant`) | yes | Participant's ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | maxLength: 8; example: "00115678" |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br>  `CACC` - Checking account<br>  `SVGS` - Savings account<br>  `TRAN` - Transactional account (Brazil only). Also known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking. <br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `branch` | string (schema `Branch`) | yes | Bank-assigned branch ID or ISPB (Identifcador do Sistema de Pagamento Brazil) number - the Brazilian Payment System identifier, an 8-digit value. | example: "011" |
| `opening_datetime` | string (schema `OpeningDatetime`) | yes | Opening date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

<!-- schema: #/components/schemas/presenter.Owner -->
### Schema `presenter.Owner`

Pointer: `#/components/schemas/presenter.Owner`. Type: object (schema `presenter.Owner`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 11; maxLength: 14; example: "123412341234" |
| `name` | string (schema `PersonName`) | yes | Person's name | maxLength: 100; example: "Jerry Atrick" |
| `type` | string (schema `PersonType`) | yes | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `trade_name` | string (schema `TradeName`) | no | Name under which the business operates. Not necessarily the same as the legal name. | maxLength: 100; example: "Acme Widgets" |

<!-- schema: #/components/schemas/message.Message -->
### Schema `message.Message`

Pointer: `#/components/schemas/message.Message`. Type: object (schema `message.Message`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

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

<!-- schema: #/components/schemas/entry.Key -->
### Schema `entry.Key`

Pointer: `#/components/schemas/entry.Key`. Type: object (schema `entry.Key`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string | yes |  | maxLength: 77; example: "mason.jarr@example.com" |

<!-- schema: #/components/schemas/entry.KeyResponse -->
### Schema `entry.KeyResponse`

Pointer: `#/components/schemas/entry.KeyResponse`. Type: object (schema `entry.KeyResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_entry` | boolean | no | Does key exist? |  |
| `key` | string | no | Key value | maxLength: 77; example: "nan_obyte@email.com" |

<!-- schema: #/components/schemas/message.DetailMessage -->
### Schema `message.DetailMessage`

Pointer: `#/components/schemas/message.DetailMessage`. Type: object (schema `message.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `message.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `message.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `message.PayloadMessage`) | no |  |  |

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
| `api-specs/Instant_payments_-_Pix_management.yaml` | tag `Keys`: POST /v2/pix/keys/search, POST /v2/pix/keys/validate, POST /v2/pix/keys/check | https://github.com/PismoDevEx/pismo-api-specs | `7d7fee078ccf5569…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-epda` — Error codes: EPDA
- `KU-ERR-codes-epdg` — Error codes: EPDG
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
