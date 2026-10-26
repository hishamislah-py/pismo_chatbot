---
ku_id: KU-API-banking-transaction-banking--bulk-payment-files
title: 'API reference: Banking - Transaction banking — Bulk payment files'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Transaction_banking.yaml
  sha256: dec6c4900eb2db35c29c0f0380763da5ae0e1a18c4ad1e293216b2b6effdab56
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
- post-bulk-keys
- get-bulk-keys
- corporate-bulk-payments-put-aes-keys-jwe
- corporate-put-bulk-file
related_kus:
- KU-BANK-dormancy
- KU-BANK-file-based-processing
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-PAY-bulk-file-based-payment-processing
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Bulk payment files

**KU ID:** `KU-API-banking-transaction-banking--bulk-payment-files` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Bulk payment files` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Bulk payment file endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /corporate/v1/bulk-payments/keys` | `post-bulk-keys` | Upload public key | no |
| `GET /corporate/v1/bulk-payments/keys/{id}` | `get-bulk-keys` | Get public key | no |
| `PUT /corporate/v2/bulk-payments/encryption-keys/{bulkId}` | `corporate-bulk-payments-put-aes-keys-jwe` | Create AES key (encrypted response) | no |
| `PUT /corporate/v1/bulk-payments/{bulkId}` | `corporate-put-bulk-file` | Upload bulk file | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/bulk-payments/keys operationId=post-bulk-keys -->
### `POST /corporate/v1/bulk-payments/keys` — Upload public key

- **operationId:** `post-bulk-keys`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bulk payment files`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Upload a public key for validating signatures and sending signed bulk files. For detailed instructions on creating a public key, refer to the [Create public and private keys](doc:file-signature-and-encryption#creating-public-and-private-keys) section in <i>File signature and encryption</i>.
>
> To understand how bulk file payment processing works, refer to the [Bulk file-based payment processing](doc:bulk-file-based-payment-processing) guide.

#### Request body

Required: yes

> Upload public key request body

**Content type `application/json`** — schema: object (schema `UploadPublicKeyRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PublicKeyID`) | yes | ID of the public key. Only digits, letters, hyphens, and underscores are allowed, and cannot exceed 60 characters. | maxLength: 60; example: "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3" |
| `key_material` | string (schema `KeyMaterial`) | yes | Public-key encoded in DER and base64 formats | example: "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAsdRPlk9sW4I79X8hDarn82E9/6AZmEpHrG/IAdUkpaHHsQdvELnFySTAWtw5dNPIdBrYyn1jA6+Cf1dKuTjYxqt+TufMVsBbEbRobXHQezu8JajkkCgW9mzVweVP5qVpUFiryH3jHr3sPD8P8nDuKEzVe8Q83mmSt2YKyg95vkHl6iIrbM11whdZS5jy5VzV++P5BLTVvpPbrDFK/OStxStO7JjI0Lhz8zXqIDhopkOHtP9Ai/gFtdKZB3BefYFHTJFNifzyu8CGAZ00wLVfx61eRCi2cFBsW0HngTT+fLoELyvyxfpKmgkV+3eCMr8CkyEIxEpWNCxkOBxGk5LKMUHMka6YfurS0jXKNGi93wKJX3N1h93sPw4QHtRvqTm07zj8S9drSN6qa8B1u6kltWB+FckdOAqDWt2HBme0cy61xWK2REqXUPqywSrN1w2HitCoJOORUjf5zwUyzoGFMHjW9r7eChr8wsidu34DsMQNf6Lu9OzER2kCbhZlRMKZAgMBAAE=" |
| `expires_at` | string (schema `PublicKeyExpiresAt`) | no | Expiration date and time of the public key. If not provided, it is set to 6 months from the date of submission. | format: "date-time"; example: "2025-05-21T12:27:00Z" |

Example `New public key`:

```json
{
  "id": "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3",
  "key_material": "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAsdRPlk9sW4I79X8hDarn82E9/6AZmEpHrG/IAdUkpaHHsQdvELnFySTAWtw5dNPIdBrYyn1jA6+Cf1dKuTjYxqt+TufMVsBbEbRobXHQezu8JajkkCgW9mzVweVP5qVpUFiryH3jHr3sPD8P8nDuKEzVe8Q83mmSt2YKyg95vkHl6iIrbM11whdZS5jy5VzV++P5BLTVvpPbrDFK/OStxStO7JjI0Lhz8zXqIDhopkOHtP9Ai/gFtdKZB3BefYFHTJFNifzyu8CGAZ00wLVfx61eRCi2cFBsW0HngTT+fLoELyvyxfpKmgkV+3eCMr8CkyEIxEpWNCxkOBxGk5LKMUHMka6YfurS0jXKNGi93wKJX3N1h93sPw4QHtRvqTm07zj8S9drSN6qa8B1u6kltWB+FckdOAqDWt2HBme0cy61xWK2REqXUPqywSrN1w2HitCoJOORUjf5zwUyzoGFMHjW9r7eChr8wsidu34DsMQNf6Lu9OzER2kCbhZlRMKZAgMBAAE=",
  "expires_at": "2025-05-21T12:27:00Z"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `UploadPublicKeyResponse`) |
| 400 | A Bad Request validation error | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PublicKeyID`) | no | ID of the public key. Only digits, letters, hyphens, and underscores are allowed, and cannot exceed 60 characters. | maxLength: 60; example: "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3" |

201 Example `Example hierarchy level structure`:

```json
{
  "id": "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3"
}
```

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WBPK0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `id required`:

```json
{
  "code": "WBPK0002",
  "message": "id is a required field"
}
```

400 Example `id exceed size`:

```json
{
  "code": "WBPK0002",
  "message": "name must be a maximum of 60 characters in length"
}
```

400 Example `key_material required`:

```json
{
  "code": "WBPK0002",
  "message": "key_material is a required field"
}
```

400 Example `key_material invalid`:

```json
{
  "code": "WBPK0002",
  "message": "key_material must be encoded in DER and a Base64 format string"
}
```

400 Example `expires_at invalid`:

```json
{
  "code": "WBPK0004",
  "message": "expires_at must not be in the past"
}
```

400 Example `id already registered`:

```json
{
  "code": "WBPK0005",
  "message": "Key with id {id} already registered"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBPK0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WBPK0002` | id is a required field |
| 400 | `WBPK0004` | expires_at must not be in the past |
| 400 | `WBPK0005` | Key with id {id} already registered |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-file-based-processing`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/bulk-payments/keys/{id} operationId=get-bulk-keys -->
### `GET /corporate/v1/bulk-payments/keys/{id}` — Get public key

- **operationId:** `get-bulk-keys`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bulk payment files`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a public key by its ID.<br>
>
> To understand how bulk file payment processing works, refer to the [Bulk file-based payment processing](doc:bulk-file-based-payment-processing) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `id` | path | yes | string | ID of the public key | example: "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get public key response | `application/json`: object (schema `GetPublicKeyResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `PublicKeyID`) | no | ID of the public key. Only digits, letters, hyphens, and underscores are allowed, and cannot exceed 60 characters. | maxLength: 60; example: "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3" |
| `key_material` | string (schema `KeyMaterial`) | no | Public-key encoded in DER and base64 formats | example: "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAsdRPlk9sW4I79X8hDarn82E9/6AZmEpHrG/IAdUkpaHHsQdvELnFySTAWtw5dNPIdBrYyn1jA6+Cf1dKuTjYxqt+TufMVsBbEbRobXHQezu8JajkkCgW9mzVweVP5qVpUFiryH3jHr3sPD8P8nDuKEzVe8Q83mmSt2YKyg95vkHl6iIrbM11whdZS5jy5VzV++P5BLTVvpPbrDFK/OStxStO7JjI0Lhz8zXqIDhopkOHtP9Ai/gFtdKZB3BefYFHTJFNifzyu8CGAZ00wLVfx61eRCi2cFBsW0HngTT+fLoELyvyxfpKmgkV+3eCMr8CkyEIxEpWNCxkOBxGk5LKMUHMka6YfurS0jXKNGi93wKJX3N1h93sPw4QHtRvqTm07zj8S9drSN6qa8B1u6kltWB+FckdOAqDWt2HBme0cy61xWK2REqXUPqywSrN1w2HitCoJOORUjf5zwUyzoGFMHjW9r7eChr8wsidu34DsMQNf6Lu9OzER2kCbhZlRMKZAgMBAAE=" |
| `expires_at` | string (schema `PublicKeyExpiresAt`) | no | Expiration date and time of the public key. If not provided, it is set to 6 months from the date of submission. | format: "date-time"; example: "2025-05-21T12:27:00Z" |

200 Example `Division response`:

```json
{
  "id": "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3",
  "key_material": "MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAsdRPlk9sW4I79X8hDarn82E9/6AZmEpHrG/IAdUkpaHHsQdvELnFySTAWtw5dNPIdBrYyn1jA6+Cf1dKuTjYxqt+TufMVsBbEbRobXHQezu8JajkkCgW9mzVweVP5qVpUFiryH3jHr3sPD8P8nDuKEzVe8Q83mmSt2YKyg95vkHl6iIrbM11whdZS5jy5VzV++P5BLTVvpPbrDFK/OStxStO7JjI0Lhz8zXqIDhopkOHtP9Ai/gFtdKZB3BefYFHTJFNifzyu8CGAZ00wLVfx61eRCi2cFBsW0HngTT+fLoELyvyxfpKmgkV+3eCMr8CkyEIxEpWNCxkOBxGk5LKMUHMka6YfurS0jXKNGi93wKJX3N1h93sPw4QHtRvqTm07zj8S9drSN6qa8B1u6kltWB+FckdOAqDWt2HBme0cy61xWK2REqXUPqywSrN1w2HitCoJOORUjf5zwUyzoGFMHjW9r7eChr8wsidu34DsMQNf6Lu9OzER2kCbhZlRMKZAgMBAAE=",
  "expires_at": "2025-05-21T12:27:00Z"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-file-based-processing`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PUT path=/corporate/v2/bulk-payments/encryption-keys/{bulkId} operationId=corporate-bulk-payments-put-aes-keys-jwe -->
### `PUT /corporate/v2/bulk-payments/encryption-keys/{bulkId}` — Create AES key (encrypted response)

- **operationId:** `corporate-bulk-payments-put-aes-keys-jwe`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bulk payment files`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an Advanced Encryption Standard (AES) key using bulk ID.<br>
>
> This endpoint uses JSON Web Encryption (JWE) to encrypt the response body at the message level. It takes a `public_key_id`, which refers to the public key you have already uploaded to the Pismo platform. Pismo uses this key to encrypt the response payload in accordance with the standard JWE protocol. To decrypt the response, you must use the corresponding private key.
> For information about file encryption and AES keys, refer to the [File encryption](doc:file-signature-and-encryption#file-encryption) section in <i>File signature and encryption</i>.
>
> The decrypted plaintext is a JSON object with fields:
> ```json
> {
>   "aes_key": "245ca959580cae6317c8f8215cbae42c8b98bbf30d9f222b92db30df81a06f91"
>   "iv": "7b75d3b5a25e9651e69245fa844cf3ec"
> }
> ```
>
> To understand how bulk file payment processing works, refer to the [bulk file-based payment processing](doc:bulk-file-based-payment-processing) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bulkId` | path | yes | string | ID of the existing bulk payment file. This ID is client-generated. | example: "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3" |

#### Request body

Required: yes

> Create AES key request body

**Content type `application/json`** — schema: object (schema `CreateAESKeyRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `public_key_id` | string (schema `PublicKeyID`) | yes | ID of the public key. Only digits, letters, hyphens, and underscores are allowed, and cannot exceed 60 characters. | maxLength: 60; example: "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3" |

Example `Public key`:

```json
{
  "public_key_id": "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Create AES key response | `application/jose`: string (schema `CreateAESKeyResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/jose` body fields:**

_No fields declared in the schema._

200 Example `AES key response`:

```text
eyJhbGciOiJSU0.cG8IjDbOwrNmuFuu.cG8IjDbOwrNmuFuu.hRmQ0dLFA.Uo3S0eDP0GLkQW6LJVNi5
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-file-based-processing`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PUT path=/corporate/v1/bulk-payments/{bulkId} operationId=corporate-put-bulk-file -->
### `PUT /corporate/v1/bulk-payments/{bulkId}` — Upload bulk file

- **operationId:** `corporate-put-bulk-file`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bulk payment files`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> This endpoint enables you to manage the upload of bulk files along with their corresponding signature data in the request header.
>
> <b>Detailed flow:</b>
> 1. The client sends a request with the bulk file as the body and signature in the
>    `Signature` header. The signature header is formatted as `keyId="{key_id}",signature="{signature_base64}"`. The parameters `key_id` and `signature_base64` are specified in the `parameters` section.
> 2. The server processes the request and responds with a `200 OK` status, indicating the file upload request is complete.
>
> For detailed instructions, refer to [File signature and encryption](doc:file-signature-and-encryption).
>
> To understand how bulk file payment processing works, refer to the [bulk file-based payment processing](doc:bulk-file-based-payment-processing) guide.
>
> <b>Note</b>: Pismo reserves the right to offer this endpoint only for single-tenant clients, reach out to your Pismo representative for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `bulkId` | path | yes | string | ID of the bulk payment file. This ID is client-generated. | example: "b6cdccc4-f6bf-4218-9e5e-7fb8f66008e3" |
| `signature` | header | yes | string | The `Signature` header includes two fields: `keyId` and `signature`. The `keyId` represents the public key ID used to verify the request, while `signature` contains the the base64-encoded cryptographic signature of the request body, created using the private key associated with the `keyId`. | example: "keyId=\\"abcd1234\\", signature=\\"c2lnbmF0dXJlLWRhdGE=\\"" |

#### Request body

Required: yes

> Bulk file data.

**Content type `application/octet-stream`** — schema: string

_No fields declared in the schema._

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: string (schema `PutUploadBulkFile`) |
| 400 | A Bad Request validation error | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `keyId is required`:

```json
{
  "code": "WBUP0001",
  "message": "'keyId' header: attribute is required"
}
```

400 Example `signature is required`:

```json
{
  "code": "WBUP0001",
  "message": "'signature' header: attribute is required"
}
```

400 Example `signature is not a valid base64-encoded string`:

```json
{
  "code": "WBUP0001",
  "message": "'signature' header: attribute must be a valid base64 encoded string"
}
```

400 Example `signature is malformed`:

```json
{
  "code": "WBUP0001",
  "message": "'signature' header: header is malformed"
}
```

400 Example `invalid request header`:

```json
{
  "code": "WBUP0004",
  "message": "Invalid request header"
}
```

400 Example `invalid JSON data in bulk header`:

```json
{
  "code": "WBUP0005",
  "message": "Invalid JSON data in bulk header"
}
```

400 Example `authentication OrgID does not match bulk header`:

```json
{
  "code": "WBUP0006",
  "message": "Authentication OrgID does not match Bulk Header"
}
```

400 Example `BulkID in URL does not match bulk header`:

```json
{
  "code": "WBUP0007",
  "message": "BulkID in URL does not match Bulk Header"
}
```

400 Example `invalid operation type in bulk header`:

```json
{
  "code": "WBUP0008",
  "message": "Invalid operation_type in Bulk Header"
}
```

400 Example `invalid bulkId format`:

```json
{
  "code": "WBUP0009",
  "message": "Invalid bulkId format"
}
```

400 Example `bulk header line too long`:

```json
{
  "code": "WBUP0010",
  "message": "Bulk header line exceeds maximum allowed length"
}
```

##### Response 409

409 Example `duplicate bulk file uploaded`:

```json
{
  "code": "WBUP0003",
  "message": "Duplicate bulk file uploaded"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBUP0001` | 'keyId' header: attribute is required |
| 400 | `WBUP0004` | Invalid request header |
| 400 | `WBUP0005` | Invalid JSON data in bulk header |
| 400 | `WBUP0006` | Authentication OrgID does not match Bulk Header |
| 400 | `WBUP0007` | BulkID in URL does not match Bulk Header |
| 400 | `WBUP0008` | Invalid operation_type in Bulk Header |
| 400 | `WBUP0009` | Invalid bulkId format |
| 400 | `WBUP0010` | Bulk header line exceeds maximum allowed length |
| 409 | `WBUP0003` | Duplicate bulk file uploaded |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-dormancy`, `KU-BANK-file-based-processing`, `KU-PAY-bulk-file-based-payment-processing`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Bulk payment files`: POST /corporate/v1/bulk-payments/keys, GET /corporate/v1/bulk-payments/keys/{id}, PUT /corporate/v2/bulk-payments/encryption-keys/{bulkId}, PUT /corporate/v1/bulk-payments/{bulkId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-dormancy` — Dormancy and dormancy reactivation exceptions
- `KU-BANK-file-based-processing` — File-based processing, file signature and encryption
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-PAY-bulk-file-based-payment-processing` — Bulk file-based payment processing
