---
ku_id: KU-API-instant-payments-pix-management--keys-part-01
title: 'API reference: Instant payments - Pix management — Keys (part 1 of 2)'
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
- get-v2-pix-keys
- post-v2-pix-keys-create
- patch-v2-pix-keys
- post-v2-pix-keys-delete
related_kus:
- KU-BANK-banking-as-a-service
- KU-ERR-codes-epda
- KU-ERR-codes-epdg
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-pix
- KU-EVT-pix-payments-data-events
- KU-PAY-pix-instant-payments
specification_version: 0.0.1
---

# API reference: Instant payments - Pix management — Keys (part 1 of 2)

**KU ID:** `KU-API-instant-payments-pix-management--keys-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Keys` in `api-specs/Instant_payments_-_Pix_management.yaml` (“Instant payments - Pix management”, version `0.0.1`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage DICT keys endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/pix/keys` | `get-v2-pix-keys` | List user keys | no |
| `POST /v2/pix/keys` | `post-v2-pix-keys-create` | Create key entry | no |
| `PATCH /v2/pix/keys` | `patch-v2-pix-keys` | Update key entry | no |
| `POST /v2/pix/keys/delete` | `post-v2-pix-keys-delete` | Delete key | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=GET path=/v2/pix/keys operationId=get-v2-pix-keys -->
### `GET /v2/pix/keys` — List user keys

- **operationId:** `get-v2-pix-keys`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Keys`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a list of user keys based on the Pismo account ID, which is parsed from the account token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `key_type` | query | no | string | Type of user information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Brazil - Individual Taxpayer Registry) number. Similar to a Social Security number in the US<br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (Brazil - National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email address<br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br><br>If nothing is selected, all key data is returned.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.ListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 404 | Resource Not Found | `application/json`: object (schema `message.Message`) |
| 409 | Conflict | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `keys` | array of object (schema `presenter.KeyItemResponse`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `Invalid key type create` (Invalid Key Type):

```json
{
  "code": "EPDA0038",
  "message": "Invalid key type"
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

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `Account blocked cancelled create` (Account status blocked or cancelled):

```json
{
  "code": "EPDA0028",
  "message": "Account status blocked or cancelled"
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


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPDA0038` | Invalid key type |
| 404 | `EPDG0014` | Resource not found on the provider service |
| 404 | `PBE353` | Entity not found |
| 404 | `EPDA0024` | Account not found for ID {account_id} |
| 409 | `EPDA0028` | Account status blocked or cancelled |
| 500 | `EPDG0006` | Failed to marshal JSON object |
| 500 | `EPDG0007` | Failed to unmarshal JSON object |
| 500 | `EPDG0010` | I/O error while reading response data: '{details}' |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/keys operationId=post-v2-pix-keys-create -->
### `POST /v2/pix/keys` — Create key entry

- **operationId:** `post-v2-pix-keys-create`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Keys`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a new DICT key entry for the user.
>
> The Banco Central do Brazil (BCB) maintains Pix keys in the Diretório de Identificadores de Contas Transacionais (DICT), a national Pix key registry and database.
>
> On PSP timeout, a `202 Accepted` with a key status = `PROCESSING` reponse is returned  and the process continues asynchronously, eventually emitting a success or error event.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-key-status-change-1" >Pix key status changed</a> event. 
>
> For more information, refer to the [Pix instant payments](doc:pix-instant-payments) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: yes

> Create a new key

**Content type `application/json`** — schema: object (schema `presenter.CreationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `reason` | string (schema `EntryCreationReason`) | yes | Reason for entry creation | enum: ["USER_REQUESTED", "RECONCILIATION"]; example: "USER_REQUESTED" |
| `bank_account` | object (schema `presenter.CreationBankAccount`) | yes |  |  |
| `name_type` | string (schema `NameType`) | no | Name type: <br>  * `REGISTRATION_NAME` - Name assigned at birth <br>  * `SOCIAL_NAME` - Preferred name, not necessarily `REGISTRATION_NAME`<br> | enum: ["REGISTRATION_NAME", "SOCIAL_NAME"]; example: "SOCIAL_NAME" |

Example `Create Key`:

```json
{
  "bank_account": {
    "opening_datetime": "2020-08-13T13:49:03Z"
  },
  "key": "email@email.com",
  "key_type": "EMAIL",
  "reason": "USER_REQUESTED"
}
```

Example `Create Key EVP`:

```json
{
  "bank_account": {
    "opening_datetime": "2020-08-13T13:49:03Z"
  },
  "key": "8d33a43c-0d22-4974-9652-30c80f2d6b0e",
  "key_type": "EVP",
  "reason": "USER_REQUESTED"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `presenter.CreationResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
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

##### Response 201

- Response header `x-cid`: Request tracking identifier. (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bank_account` | object (schema `presenter.BankAccount`) | yes |  |  |
| `creation_datetime` | string (schema `CreationDatetime`) | yes | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `owner` | object (schema `presenter.Owner`) | yes |  |  |
| `reason` | string (schema `Reason`) | yes | Reason for request | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "BRANCH_TRANSFER", "RECONCILIATION", "FRAUD", "DEFAULT_OPERATION", "RFB_VALIDATION"]; example: "USER_REQUESTED" |
| `request_id` | string | no | Request ID | example: "8bfde840-bef5-42b7-bef2-350475ffb9e1" |
| `ownership_datetime` | string (schema `OwnershipDatetime`) | no | Ownership date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `bacen_processed_datetime` | string (schema `BacenProcessedDatetime`) | no | Banco Central do Brasil (Central Bank of Brazil) processed datetime.  A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `claim_requested_datetime` | string (schema `ClaimRequestedDatetime`) | no | Claim requested date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `account_id` | string (schema `AccountID`) | no | Pismo account ID | example: "8675309" |
| `status` | string (schema `KeyStatus`) | no | Key status: <br>  * `ACTIVE` - Key is active<br>  * `DELETED` - Key was removed<br>  * `PROCESSING` - An error occurred during the request to the PSP. The process continues asynchronously in this case.<br> | enum: ["ACTIVE", "DELETED", "PROCESSING"] |

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
        "field": "DeleteKeyRequest.reason",
        "message": "Field validation for 'reason' failed on the 'oneof' tag"
      }
    ]
  }
}
```

400 Example `Invalid key type create` (Invalid Key Type):

```json
{
  "code": "EPDA0038",
  "message": "Invalid Key Type"
}
```

400 Example `Invalid cpf create` (Invalid CPF):

```json
{
  "code": "EPDA0039",
  "message": "Invalid CPF"
}
```

400 Example `Invalid cnpj create` (Invalid CNPJ):

```json
{
  "code": "EPDA0040",
  "message": "Invalid CNPJ"
}
```

400 Example `Invalid phone create` (Invalid PHONE):

```json
{
  "code": "EPDA0041",
  "message": "Invalid PHONE"
}
```

400 Example `Invalid email create` (Invalid EMAIL):

```json
{
  "code": "EPDA0042",
  "message": "Invalid EMAIL"
}
```

400 Example `Invalid evp create` (Invalid EVP):

```json
{
  "code": "EPDA0043",
  "message": "Invalid EVP"
}
```

400 Example `Missing tenant header`:

```json
{
  "code": "EPDG0001",
  "message": "Missing x-tenant header"
}
```

400 Example `Provider service error request`:

```json
{
  "code": "EPDG0011",
  "message": "Bad request while accessing the provider service",
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

400 Example `Invalid provider service response`:

```json
{
  "code": "EPDG0018",
  "message": "Provider service returned a status {http_status} which was not expected"
}
```

400 Example `Provider authentication service error request`:

```json
{
  "code": "EPDG0019",
  "message": "Provider authentication service rejected request due to a client payload misconfiguration"
}
```

400 Example `Entry owned by different person` (Entry owned by different person):

```json
{
  "code": "EPDG0035",
  "message": "Entry owned by different person"
}
```

400 Example `Entry owned by same person but different participant` (Entry owned by same person, but with different participant):

```json
{
  "code": "EPDG0036",
  "message": "Entry owned by same person, but with different participant"
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
404 Example `Participant not found create` (Participant Not Found):

```json
{
  "code": "EPDA0023",
  "message": "Participant not found for org {orgId}"
}
```

404 Example `Account not found create` (Account Not Found):

```json
{
  "code": "EPDA0024",
  "message": "Account not found for ID {accountId}"
}
```

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

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `Key exists create` (Key already exists in database):

```json
{
  "code": "EPDA0025",
  "message": "Key already exists in database"
}
```

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
| 202 | `EPDA0169` | Request was accepted and gonna be processed asynchronously |
| 400 | `EPDA0002` | Failed to unmarshal request body |
| 400 | `EPDA0003` | There are invalid fields when trying to validate request body |
| 400 | `EPDA0038` | Invalid Key Type |
| 400 | `EPDA0039` | Invalid CPF |
| 400 | `EPDA0040` | Invalid CNPJ |
| 400 | `EPDA0041` | Invalid PHONE |
| 400 | `EPDA0042` | Invalid EMAIL |
| 400 | `EPDA0043` | Invalid EVP |
| 400 | `EPDG0001` | Missing x-tenant header |
| 400 | `EPDG0011` | Bad request while accessing the provider service |
| 400 | `PBE353` | Entity not found |
| 400 | `EPDG0018` | Provider service returned a status {http_status} which was not expected |
| 400 | `EPDG0019` | Provider authentication service rejected request due to a client payload misconfiguration |
| 400 | `EPDG0035` | Entry owned by different person |
| 400 | `EPDG0036` | Entry owned by same person, but with different participant |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 404 | `EPDA0023` | Participant not found for org {orgId} |
| 404 | `EPDA0024` | Account not found for ID {accountId} |
| 404 | `EPDG0014` | Resource not found on the provider service |
| 404 | `PBE353` | Entity not found |
| 409 | `EPDA0025` | Key already exists in database |
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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-key-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-key-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;401;403;404;409;429;500;502;503;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-as-a-service`, `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=PATCH path=/v2/pix/keys operationId=patch-v2-pix-keys -->
### `PATCH /v2/pix/keys` — Update key entry

- **operationId:** `patch-v2-pix-keys`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Keys`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the DICT key entry.
>
> On PSP timeout, a `202 Accepted` response with a key status =  `PROCESSING` is returned and the process continues asynchronously, eventually emitting a success or error event.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-key-status-change-1" >Pix key status changed</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: yes

> Update the key

**Content type `application/json`** — schema: object (schema `presenter.UpdateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `reason` | string (schema `EntryUpdateReason`) | yes | <br>Reason for request<br><br>* `USER_REQUESTED` - EVP keys are not supported<br> | enum: ["USER_REQUESTED", "BRANCH_TRANSFER", "RECONCILIATION", "RFB_VALIDATION"]; example: "USER_REQUESTED" |
| `bank_account` | object (schema `presenter.UpdateBankAccount`) | yes |  |  |
| `name_type` | string (schema `EntryUpdateNameType`) | no | Name type: <br>  * `REGISTRATION_NAME` - Name assigned at birth <br>  * `SOCIAL_NAME` - Preferred name, not necessarily `REGISTRATION_NAME` (not supported when key owner is a `LEGAL_PERSON`)<br> | enum: ["REGISTRATION_NAME", "SOCIAL_NAME"]; example: "SOCIAL_NAME" |

Example `Update Key`:

```json
{
  "bank_account": {
    "opening_datetime": "2020-08-13T13:49:03Z"
  },
  "key": "email@email.com",
  "key_type": "EMAIL",
  "reason": "USER_REQUESTED"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `presenter.UpdateResponse`) |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
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

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bank_account` | object (schema `presenter.BankAccount`) | yes |  |  |
| `creation_datetime` | string (schema `CreationDatetime`) | yes | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `owner` | object (schema `presenter.Owner`) | yes |  |  |
| `reason` | string (schema `Reason`) | yes | Reason for request | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "BRANCH_TRANSFER", "RECONCILIATION", "FRAUD", "DEFAULT_OPERATION", "RFB_VALIDATION"]; example: "USER_REQUESTED" |
| `open_claim_creation_datetime` | string (schema `OpenClaimCreationDatetime`) | no | Open claim creation date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `ownership_datetime` | string (schema `OwnershipDatetime`) | no | Ownership date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `account_id` | string (schema `AccountID`) | no | Pismo account ID | example: "8675309" |
| `content_id` | string (schema `ContentID`) | no | Content ID. This is a hashed value created from a number of key-related fields in the Pismo database. This is meant for you to store and send to Pismo in case there is any problem with the key.<br> | example: "4a46173b40f861f769ea00ef14aea3d3b7e12f730a7caba61c7fbbe437c1da65" |
| `correlation_id` | string (schema `CorrelationID`) | no | The correlation identifier is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header.<br> | format: "uuid"; example: "ea8bc045-9ff7-439f-a318-2e6f974707a5" |
| `status` | string (schema `KeyStatus`) | no | Key status: <br>  * `ACTIVE` - Key is active<br>  * `DELETED` - Key was removed<br>  * `PROCESSING` - An error occurred during the request to the PSP. The process continues asynchronously in this case.<br> | enum: ["ACTIVE", "DELETED", "PROCESSING"] |

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
        "field": "DeleteKeyRequest.reason",
        "message": "Field validation for 'reason' failed on the 'oneof' tag"
      }
    ]
  }
}
```

400 Example `Missing tenant header`:

```json
{
  "code": "EPDG0001",
  "message": "Missing x-tenant header"
}
```

400 Example `Provider service error request`:

```json
{
  "code": "EPDG0011",
  "message": "Bad request while accessing the provider service",
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

400 Example `Invalid provider service response`:

```json
{
  "code": "EPDG0018",
  "message": "Provider service returned a status {http_status} which was not expected"
}
```

400 Example `Provider authentication service error request`:

```json
{
  "code": "EPDG0019",
  "message": "Provider authentication service rejected request due to a client payload misconfiguration"
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
| 202 | `EPDA0169` | Request was accepted and gonna be processed asynchronously |
| 400 | `EPDA0002` | Failed to unmarshal request body |
| 400 | `EPDA0003` | There are invalid fields when trying to validate request body |
| 400 | `EPDG0001` | Missing x-tenant header |
| 400 | `EPDG0011` | Bad request while accessing the provider service |
| 400 | `PBE353` | Entity not found |
| 400 | `EPDG0018` | Provider service returned a status {http_status} which was not expected |
| 400 | `EPDG0019` | Provider authentication service rejected request due to a client payload misconfiguration |
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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-key-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-key-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;401;403;404;409;429;500;502;503;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-pix-payments-data-events`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_management.yaml method=POST path=/v2/pix/keys/delete operationId=post-v2-pix-keys-delete -->
### `POST /v2/pix/keys/delete` — Delete key

- **operationId:** `post-v2-pix-keys-delete`
- **Specification:** `api-specs/Instant_payments_-_Pix_management.yaml` (Instant payments - Pix management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/pix-dict`
- **Tags:** `Keys`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Deletes a user DICT key entry.
>
> On PSP timeout, a `202 Accepted` response is returned and the process continues asynchronously, eventually emitting a success or error event.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-dict-key-status-change-1" >Pix key status changed</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique UUID identifier to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "550e8400-e29b-41d4-a716-446655440000" |

#### Request body

Required: yes

> Delete the key.

**Content type `application/json`** — schema: object (schema `presenter.DeleteRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string (schema `Key`) | yes | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | yes | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `reason` | string (schema `DeleteReason`) | yes | Delete key reason for request. | enum: ["USER_REQUESTED", "ACCOUNT_CLOSURE", "RECONCILIATION", "FRAUD", "RFB_VALIDATION"]; example: "USER_REQUESTED" |

Example `CPF Key Exclusion`:

```json
{
  "key": "97361452043",
  "key_type": "CPF",
  "reason": "USER_REQUESTED"
}
```

Example `CNPJ Key Exclusion`:

```json
{
  "key": "73901114000186",
  "key_type": "CNPJ",
  "reason": "USER_REQUESTED"
}
```

Example `Email Key Exclusion`:

```json
{
  "key": "email@email.com",
  "key_type": "EMAIL",
  "reason": "USER_REQUESTED"
}
```

Example `Phone Key Exclusion`:

```json
{
  "key": "+5511987654321",
  "key_type": "PHONE",
  "reason": "USER_REQUESTED"
}
```

Example `EVP Key Exclusion`:

```json
{
  "key": "8d33a43c-0d22-4974-9652-30c80f2d6b0e",
  "key_type": "EVP",
  "reason": "USER_REQUESTED"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `message.Message`) |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `message.Message`) |
| 401 | Unauthorized | `application/json`: object (schema `message.Message`) |
| 403 | Forbidden | `application/json`: object (schema `message.Message`) |
| 404 | Not Found | `application/json`: object (schema `message.Message`) |
| 409 | Conflict | `application/json`: object (schema `message.Message`) |
| 429 | Too many requests | `application/json`: object (schema `message.Message`) |
| 500 | Internal Server Error | `application/json`: object (schema `message.Message`) |
| 502 | Bad Gateway | `application/json`: object (schema `message.Message`) |
| 503 | Service Unavailable | `application/json`: object (schema `message.Message`) |
| 504 | Gateway Timeout | `application/json`: object (schema `message.Message`) |

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

##### Response 204

- Response header `x-cid`: Request tracking identifier. (string)
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
        "field": "DeleteKeyRequest.reason",
        "message": "Field validation for 'reason' failed on the 'oneof' tag"
      }
    ]
  }
}
```

400 Example `Invalid key type`:

```json
{
  "code": "EPDA0038",
  "message": "Invalid key type"
}
```

400 Example `Invalid CPF Key`:

```json
{
  "code": "EPDA0039",
  "message": "Invalid CPF"
}
```

400 Example `Invalid CNPJ Key`:

```json
{
  "code": "EPDA0040",
  "message": "Invalid CNPJ"
}
```

400 Example `Invalid Email Key`:

```json
{
  "code": "EPDA0042",
  "message": "Invalid EMAIL"
}
```

400 Example `Invalid Phone Key`:

```json
{
  "code": "EPDA0041",
  "message": "Invalid PHONE"
}
```

400 Example `Invalid EVP Key`:

```json
{
  "code": "EPDA0043",
  "message": "Invalid EVP"
}
```

400 Example `Missing tenant header`:

```json
{
  "code": "EPDG0001",
  "message": "Missing x-tenant header"
}
```

400 Example `Provider service error request`:

```json
{
  "code": "EPDG0011",
  "message": "Bad request while accessing the provider service",
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

400 Example `Invalid provider service response`:

```json
{
  "code": "EPDG0018",
  "message": "Provider service returned a status {http_status} which was not expected"
}
```

400 Example `Provider authentication service error request`:

```json
{
  "code": "EPDG0019",
  "message": "Provider authentication service rejected request due to a client payload misconfiguration"
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

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `Key has open claim`:

```json
{
  "code": "EPDA0027",
  "message": "Key has open claim"
}
```

409 Example `Invalid account ID (User requested reason only)`:

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
| 202 | `EPDA0169` | Request was accepted and gonna be processed asynchronously |
| 400 | `EPDA0002` | Failed to unmarshal request body |
| 400 | `EPDA0003` | There are invalid fields when trying to validate request body |
| 400 | `EPDA0038` | Invalid key type |
| 400 | `EPDA0039` | Invalid CPF |
| 400 | `EPDA0040` | Invalid CNPJ |
| 400 | `EPDA0042` | Invalid EMAIL |
| 400 | `EPDA0041` | Invalid PHONE |
| 400 | `EPDA0043` | Invalid EVP |
| 400 | `EPDG0001` | Missing x-tenant header |
| 400 | `EPDG0011` | Bad request while accessing the provider service |
| 400 | `PBE353` | Entity not found |
| 400 | `EPDG0018` | Provider service returned a status {http_status} which was not expected |
| 400 | `EPDG0019` | Provider authentication service rejected request due to a client payload misconfiguration |
| 401 | `EPDG0013` | Unauthorized access to the provider service |
| 403 | `EPDA0009` | Missing required header 'x-tenant' |
| 403 | `EPDA0010` | Missing required header 'x-account-id' |
| 403 | `EPDA0152` | Missing required param 'id' |
| 404 | `EPDA0024` | Account not found for ID {account_id} |
| 404 | `EPDA0026` | Key not found |
| 404 | `EPDG0014` | Resource not found on the provider service |
| 404 | `PBE353` | Entity not found |
| 409 | `EPDA0027` | Key has open claim |
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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-dict-key-status-change-1` | https://developers.pismo.io/events/docs/pix-dict-key-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;204;400;401;403;404;409;429;500;502;503;504`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/presenter.KeyItemResponse -->
### Schema `presenter.KeyItemResponse`

Pointer: `#/components/schemas/presenter.KeyItemResponse`. Type: object (schema `presenter.KeyItemResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bank_account` | object (schema `presenter.BankAccount`) | no |  |  |
| `key` | string (schema `Key`) | no | Value, based on a key's type, used to encrypt Pix key. | maxLength: 77; example: "al_fresco@bourdain.com" |
| `key_type` | string (schema `KeyType`) | no | User information that can be used to create a Pix key:<br>* `CPF` - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number. Similar to a Social Security number in the US. <br>* `CNPJ` - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number. Unique ID for legal entities, such as companies and organizations, in Brazil<br>* `EMAIL` - Email <br>* `PHONE` - Phone number<br>* `EVP` - Endereco de pagamento virtual (virtual payment address). A randomly-generated UUID number.<br> | enum: ["CPF", "CNPJ", "PHONE", "EMAIL", "EVP"]; example: "EMAIL" |
| `creation_datetime` | string (schema `CreationDatetime`) | no | Creation datetime. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |
| `ownership_datetime` | string (schema `OwnershipDatetime`) | no | Ownership date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

<!-- schema: #/components/schemas/message.Message -->
### Schema `message.Message`

Pointer: `#/components/schemas/message.Message`. Type: object (schema `message.Message`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EPDA0001" |
| `details` | object (schema `message.DetailMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

<!-- schema: #/components/schemas/presenter.CreationBankAccount -->
### Schema `presenter.CreationBankAccount`

Pointer: `#/components/schemas/presenter.CreationBankAccount`. Type: object (schema `presenter.CreationBankAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `opening_datetime` | string (schema `OpeningDatetime`) | yes | Opening date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

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

<!-- schema: #/components/schemas/message.DetailMessage -->
### Schema `message.DetailMessage`

Pointer: `#/components/schemas/message.DetailMessage`. Type: object (schema `message.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `message.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `message.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `message.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/presenter.UpdateBankAccount -->
### Schema `presenter.UpdateBankAccount`

Pointer: `#/components/schemas/presenter.UpdateBankAccount`. Type: object (schema `presenter.UpdateBankAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `opening_datetime` | string (schema `OpeningDatetime`) | no | Opening date time. A RFC 3339 date-time value. For example -  `2023-04-12T23:20:50.52Z`. | format: "date-time"; example: "2020-08-13T13:49:03Z" |

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
| `api-specs/Instant_payments_-_Pix_management.yaml` | tag `Keys`: GET /v2/pix/keys, POST /v2/pix/keys, PATCH /v2/pix/keys, POST /v2/pix/keys/delete | https://github.com/PismoDevEx/pismo-api-specs | `7d7fee078ccf5569…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-banking-as-a-service` — Banking as a Service
- `KU-ERR-codes-epda` — Error codes: EPDA
- `KU-ERR-codes-epdg` — Error codes: EPDG
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
