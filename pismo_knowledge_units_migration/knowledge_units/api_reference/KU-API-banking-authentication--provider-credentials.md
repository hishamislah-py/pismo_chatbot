---
ku_id: KU-API-banking-authentication--provider-credentials
title: 'API reference: Banking - Authentication — Provider credentials'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Authentication.yaml
  sha256: 202d9526dea064403280609936d318af60f20420f62c7999f9ff4e1c7498383e
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
- post-credentials
related_kus:
- KU-BANK-banking-as-a-service
- KU-BANK-get-started-core-banking
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-epix
specification_version: '1.0'
---

# API reference: Banking - Authentication — Provider credentials

**KU ID:** `KU-API-banking-authentication--provider-credentials` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Provider credentials` in `api-specs/Banking_-_Authentication.yaml` (“Banking - Authentication”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Banking authorization credentials

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /banking-auth/v1/credentials` | `post-credentials` | Create provider credential | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Authentication.yaml method=POST path=/banking-auth/v1/credentials operationId=post-credentials -->
### `POST /banking-auth/v1/credentials` — Create provider credential

- **operationId:** `post-credentials`
- **Specification:** `api-specs/Banking_-_Authentication.yaml` (Banking - Authentication)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Provider credentials`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Create or update your credentials with a third-party banking partner (provider). Banking as a Service clients need to partner with a provider such as Celcoin, BTG, or JD Consultores.
>
> When you call this endpoint with your authentication key and secret, Pismo saves and encrypts the information you provide, then uses it to obtain an access token from the provider.
>
> For more information, see [Banking as a Service overview](doc:banking-as-a-service)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account_token` | header | yes | string | Account token - access token encoded with a Pismo account ID. This is the token you get from Pismo. Tokens can expire quickly, which can result in a **401 Unauthorized** message.<br> | example: "Your account token" |
| `tracking_id` | header | no | string | Request tracking identifier, if you don't provide one, a random UUID is generated for you. | example: "1dd-dd84-cniidk-ioumjskd-87690" |

#### Request body

Required: no

> Request body

**Content type `application/json`** — schema: object (schema `PostCreateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string | yes | Authentication secret. Your third-party banking partner provides this to you. <br> | example: "Tc84Hi3CRyAHFBNIvbc8CuSuvHuGibjf" |
| `provider` | string | yes | Third-party banking service providers.<br> | enum: ["BTG", "CELCOIN", "JDPI"]; example: "BTG" |
| `type` | string | yes | Payment integration type.<br> | enum: ["PIX", "BAAS"]; example: "PIX" |
| `provider_data` | object (schema `ProviderData`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created |  |
| 400 | Bad Request | `application/json`: object (schema `DomainError`) |
| 500 | Internal Server Error | `application/json`: object (schema `DomainError`) |
| 502 | Bad Gateway | `application/json`: object (schema `DomainError`) |
| 504 | Gateway Timeout | `application/json`: object (schema `DomainError`) |

##### Response 400

400 Example `EBAA0004` (Invalid payload):

```json
{
  "code": "EBAA0004",
  "message": "Invalid payload"
}
```

400 Example `EBAA0005` (Invalid payload required fields):

```json
{
  "code": "BA00005",
  "message": "Invalid payload. Required fields: [fields]"
}
```

400 Example `EBAA0007` (Invalid payload required fields):

```json
{
  "code": "EBAA0007",
  "message": "Unsupported Type: (TYPE) and Provider (PROVIDER)"
}
```

##### Response 500

500 Example `EPIX0005` (Error unmarshalling object):

```json
{
  "code": "EPIX0005",
  "message": "Error unmarshalling object"
}
```

500 Example `EBAA0009` (Encrypted value error):

```json
{
  "code": "EBAA0009",
  "message": "Encrypted value error. Decrypt returned different value"
}
```

500 Example `EBAA0010` (Cryptography Decrypt error):

```json
{
  "code": "EBAA0010",
  "message": "Cryptography Decrypt error. Check logs for more details"
}
```

500 Example `EBAA0011` (Credential Repository Save config error):

```json
{
  "code": "EBAA0011",
  "message": "Credential Repository Save config error. Check logs for more details"
}
```

500 Example `EBAA0012` (Credential Repository Get config error):

```json
{
  "code": "EBAA0012",
  "message": "Credential Repository Get config error. Check logs for more details"
}
```

500 Example `EBAA0014` (BTG - API configuration not found):

```json
{
  "code": "EBAA0014",
  "message": "BTG - API configuration not found"
}
```

##### Response 502

502 Example `EBAA0002` (Bad Gateway Error):

```json
{
  "code": "EBAA0002",
  "message": "Bad Gateway Error"
}
```

##### Response 504

504 Example `EBAA0003` (Gateway Timeout):

```json
{
  "code": "EBAA0003",
  "message": "Gateway Timeout"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBAA0004` | Invalid payload |
| 400 | `BA00005` | Invalid payload. Required fields: [fields] |
| 400 | `EBAA0007` | Unsupported Type: (TYPE) and Provider (PROVIDER) |
| 500 | `EPIX0005` | Error unmarshalling object |
| 500 | `EBAA0009` | Encrypted value error. Decrypt returned different value |
| 500 | `EBAA0010` | Cryptography Decrypt error. Check logs for more details |
| 500 | `EBAA0011` | Credential Repository Save config error. Check logs for more details |
| 500 | `EBAA0012` | Credential Repository Get config error. Check logs for more details |
| 500 | `EBAA0014` | BTG - API configuration not found |
| 502 | `EBAA0002` | Bad Gateway Error |
| 504 | `EBAA0003` | Gateway Timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500;502;504`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-as-a-service`, `KU-BANK-get-started-core-banking`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ProviderData -->
### Schema `ProviderData`

Pointer: `#/components/schemas/ProviderData`. Type: object (schema `ProviderData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `client_id` | string | no | The client ID you used to obtain a provider access token. | example: "Your client ID" |

<!-- schema: #/components/schemas/DomainError -->
### Schema `DomainError`

Pointer: `#/components/schemas/DomainError`. Type: object (schema `DomainError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "BA00000" |
| `details` | string | no | Error details | example: "Error detail" |
| `message` | string | no | error message | example: "Error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Authentication.yaml` | tag `Provider credentials`: POST /banking-auth/v1/credentials | https://github.com/PismoDevEx/pismo-api-specs | `202d9526dea06440…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-banking-as-a-service` — Banking as a Service
- `KU-BANK-get-started-core-banking` — Get started with core banking
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-epix` — Error codes: EPIX
