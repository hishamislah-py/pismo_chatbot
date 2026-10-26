---
ku_id: KU-API-banking-funds-coverage--protection-sources
title: 'API reference: Banking - Funds coverage — Protection sources'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Funds_coverage.yaml
  sha256: 09dcec8171f881fe519823ee6b0bbb68cc3345827c3f20a3266ddc756e93d8b0
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
- post-protection-source
- update-protection-source
- get-protection-source
related_kus:
- KU-BANK-funds-coverage
- KU-ERR-codes-acq-to-esma
specification_version: 1.0.0
---

# API reference: Banking - Funds coverage — Protection sources

**KU ID:** `KU-API-banking-funds-coverage--protection-sources` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Protection sources` in `api-specs/Banking_-_Funds_coverage.yaml` (“Banking - Funds coverage”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that manage protection sources

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/protection-sources` | `post-protection-source` | Create protection source | no |
| `PATCH /v1/protection-sources` | `update-protection-source` | Update protection source | no |
| `GET /v1/protection-sources/accounts/{accountId}` | `get-protection-source` | Get protection source | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Funds_coverage.yaml method=POST path=/v1/protection-sources operationId=post-protection-source -->
### `POST /v1/protection-sources` — Create protection source

- **operationId:** `post-protection-source`
- **Specification:** `api-specs/Banking_-_Funds_coverage.yaml` (Banking - Funds coverage)
- **Server base URL(s):** `https://sandbox.pismolabs.io/funds-coverage`
- **Tags:** `Protection sources`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create new funds coverage protection source to cover insufficient funds.<br>
> The funds coverage service enables financial products—such as savings accounts, loans, and credit cards—to serve as coverage sources for other products when there is an insufficient balance or a payment failure. It supports overdraft coverage type, configurable fallback hierarchies, and is designed for future extensibility to accommodate additional product types. Refer to the [Funds coverage](doc:funds-coverage) guide for more details.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `AuthorizationToken` | header | yes | string | Account token. Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` error.<br> | example: "1234" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProtectionSourceParam`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `covered` | string | yes | The financial product you want to protect<br> | enum: ["overdraft", "credit_card"]; example: "overdraft" |
| `sources` | array of object (schema `Source`) | yes | The list of financial products that can act as coverage sources |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | No response body is returned when a protection source is created successfully |  |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Bad Request` (Bad Request) — from `#/components/examples/EFCA0001`:

```json
{
  "code": "EFCA0001",
  "message": "Bad Request"
}
```

400 Example `Validation error` (Validation error) — from `#/components/examples/EFCA0002`:

```json
{
  "code": "EFCA0002",
  "message": "Validation error"
}
```

400 Example `Organizations API 4xx error` (Organizations API 4xx error) — from `#/components/examples/EFCA0015`:

```json
{
  "code": "EFCA0015",
  "message": "Organization API 4xx error"
}
```

##### Response 404

404 Example `Organization API resource not found` (Organization API resource not found) — from `#/components/examples/EFCA0016`:

```json
{
  "code": "EFCA0016",
  "message": "Organizations API resource not found"
}
```

##### Response 409

409 Example `Resource already exists` (Resource already exists) — from `#/components/examples/EFCA0010`:

```json
{
  "code": "EFCA0010",
  "message": "Resource already exists"
}
```

##### Response 500

500 Example `Internal error` (Internal error) — from `#/components/examples/EFCA0006`:

```json
{
  "code": "EFCA0006",
  "message": "Internal error"
}
```

500 Example `HTTP request error` (HTTP request error) — from `#/components/examples/EFCA0007`:

```json
{
  "code": "EFCA0007",
  "message": "HTTP request error"
}
```

500 Example `Organization API request error` (Organization API request error) — from `#/components/examples/EFCA0011`:

```json
{
  "code": "EFCA0011",
  "message": "Organization API request error"
}
```

500 Example `Organization API unmarshal response error` (Organization API unmarshal response error) — from `#/components/examples/EFCA0012`:

```json
{
  "code": "EFCA0012",
  "message": "Organization API unmarshal response error"
}
```

500 Example `Organization API unmapped response code error` (Organization API unmapped response code error) — from `#/components/examples/EFCA0013`:

```json
{
  "code": "EFCA0013",
  "message": "Organization API unmapped response code error"
}
```

500 Example `Organization API 5xx error` (Organization API 5xx error) — from `#/components/examples/EFCA0014`:

```json
{
  "code": "EFCA0014",
  "message": "Organization API 5xx error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFCA0001` | Bad Request |
| 400 | `EFCA0002` | Validation error |
| 400 | `EFCA0015` | Organization API 4xx error |
| 404 | `EFCA0016` | Organizations API resource not found |
| 409 | `EFCA0010` | Resource already exists |
| 500 | `EFCA0006` | Internal error |
| 500 | `EFCA0007` | HTTP request error |
| 500 | `EFCA0011` | Organization API request error |
| 500 | `EFCA0012` | Organization API unmarshal response error |
| 500 | `EFCA0013` | Organization API unmapped response code error |
| 500 | `EFCA0014` | Organization API 5xx error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-funds-coverage`.

<!-- op: spec=api-specs/Banking_-_Funds_coverage.yaml method=PATCH path=/v1/protection-sources operationId=update-protection-source -->
### `PATCH /v1/protection-sources` — Update protection source

- **operationId:** `update-protection-source`
- **Specification:** `api-specs/Banking_-_Funds_coverage.yaml` (Banking - Funds coverage)
- **Server base URL(s):** `https://sandbox.pismolabs.io/funds-coverage`
- **Tags:** `Protection sources`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update protection source. If a source does not exist, the Pismo platform selects one from `sources.type`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `AuthorizationToken` | header | yes | string | Account token. Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` error.<br> | example: "1234" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProtectionSourceParam`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `covered` | string | yes | The financial product you want to protect<br> | enum: ["overdraft", "credit_card"]; example: "overdraft" |
| `sources` | array of object (schema `Source`) | yes | The list of financial products that can act as coverage sources |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | No response body is returned when a protection source is updated successfully |  |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Bad Request` (Bad Request) — from `#/components/examples/EFCA0001`:

```json
{
  "code": "EFCA0001",
  "message": "Bad Request"
}
```

400 Example `Validation error` (Validation error) — from `#/components/examples/EFCA0002`:

```json
{
  "code": "EFCA0002",
  "message": "Validation error"
}
```

400 Example `Organizations API 4xx error` (Organizations API 4xx error) — from `#/components/examples/EFCA0015`:

```json
{
  "code": "EFCA0015",
  "message": "Organization API 4xx error"
}
```

##### Response 404

404 Example `Organizations API resource not found` (Organization API resource not found) — from `#/components/examples/EFCA0016`:

```json
{
  "code": "EFCA0016",
  "message": "Organizations API resource not found"
}
```

##### Response 500

500 Example `Internal error` (Internal error) — from `#/components/examples/EFCA0006`:

```json
{
  "code": "EFCA0006",
  "message": "Internal error"
}
```

500 Example `HTTP request error` (HTTP request error) — from `#/components/examples/EFCA0007`:

```json
{
  "code": "EFCA0007",
  "message": "HTTP request error"
}
```

500 Example `Organizations API request error` (Organization API request error) — from `#/components/examples/EFCA0011`:

```json
{
  "code": "EFCA0011",
  "message": "Organization API request error"
}
```

500 Example `Organizations API unmarshal response error` (Organization API unmarshal response error) — from `#/components/examples/EFCA0012`:

```json
{
  "code": "EFCA0012",
  "message": "Organization API unmarshal response error"
}
```

500 Example `Organizations API unmapped response code error` (Organization API unmapped response code error) — from `#/components/examples/EFCA0013`:

```json
{
  "code": "EFCA0013",
  "message": "Organization API unmapped response code error"
}
```

500 Example `Organizations API 5xx error` (Organization API 5xx error) — from `#/components/examples/EFCA0014`:

```json
{
  "code": "EFCA0014",
  "message": "Organization API 5xx error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFCA0001` | Bad Request |
| 400 | `EFCA0002` | Validation error |
| 400 | `EFCA0015` | Organization API 4xx error |
| 404 | `EFCA0016` | Organizations API resource not found |
| 500 | `EFCA0006` | Internal error |
| 500 | `EFCA0007` | HTTP request error |
| 500 | `EFCA0011` | Organization API request error |
| 500 | `EFCA0012` | Organization API unmarshal response error |
| 500 | `EFCA0013` | Organization API unmapped response code error |
| 500 | `EFCA0014` | Organization API 5xx error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-funds-coverage`.

<!-- op: spec=api-specs/Banking_-_Funds_coverage.yaml method=GET path=/v1/protection-sources/accounts/{accountId} operationId=get-protection-source -->
### `GET /v1/protection-sources/accounts/{accountId}` — Get protection source

- **operationId:** `get-protection-source`
- **Specification:** `api-specs/Banking_-_Funds_coverage.yaml` (Banking - Funds coverage)
- **Server base URL(s):** `https://sandbox.pismolabs.io/funds-coverage`
- **Tags:** `Protection sources`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get funds coverage protection source using your account ID

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Pismo account ID | example: "78123456" |
| `AuthorizationToken` | header | yes | string | Account token. Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` error.<br> | example: "1234" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get protection sources successful | `application/json`: object (schema `ProtectionSourceParam`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `covered` | string | yes | The financial product you want to protect<br> | enum: ["overdraft", "credit_card"]; example: "overdraft" |
| `sources` | array of object (schema `Source`) | yes | The list of financial products that can act as coverage sources |  |

200 Example `Get protection sources successful` (Get protection sources successful) — from `#/components/examples/200GetProtectionSourcesExample`:

```json
{
  "covered": "overdraft",
  "sources": {
    "type": "savings_account",
    "id": "123",
    "hierarchy": 1,
    "is_active": true,
    "processing_code": "009797"
  }
}
```

##### Response 400

400 Example `Bad Request` (Bad Request) — from `#/components/examples/EFCA0001`:

```json
{
  "code": "EFCA0001",
  "message": "Bad Request"
}
```

##### Response 404

404 Example `Resource not found` (Resource not found) — from `#/components/examples/EFCA0009`:

```json
{
  "code": "EFCA0009",
  "message": "Resource not found"
}
```

##### Response 500

500 Example `Internal error` (Internal error) — from `#/components/examples/EFCA0006`:

```json
{
  "code": "EFCA0006",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFCA0001` | Bad Request |
| 404 | `EFCA0009` | Resource not found |
| 500 | `EFCA0006` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-funds-coverage`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Source -->
### Schema `Source`

Pointer: `#/components/schemas/Source`. Type: object (schema `Source`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | yes | Funds coverage source product type | enum: ["savings_account", "loan"]; example: "savings_account" |
| `hierarchy` | integer | yes | Funds coverage source hierarchy level. The funds coverage is selected according to its configured hierarchy level. Note that lower numbers have higher priority. | example: 1 |
| `processing_code` | string | yes | Processing code associated with the source, used to move funds | example: "009797" |
| `id` | string | no | ID representing the fund source. If you don't specify a value, the Pismo platform defaults to your account ID and `sources.type`. | example: "123" |
| `is_active` | boolean | no | Is the source active? | default: false; example: true |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EFCA0001" |
| `message` | string | no | Error message | example: "Error" |
| `details` | string | no | Details about the error | example: "Error details" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Funds_coverage.yaml` | tag `Protection sources`: POST /v1/protection-sources, PATCH /v1/protection-sources, GET /v1/protection-sources/accounts/{accountId} | https://github.com/PismoDevEx/pismo-api-specs | `09dcec8171f881fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-funds-coverage` — Funds coverage
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
