---
ku_id: KU-API-banking-overdraft--program
title: 'API reference: Banking - Overdraft — Program'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Overdraft.yaml
  sha256: 957ed8db66676dab78bfaae5d72df3659a3ab7648f3ddcb6cd01235626375ff4
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
- post-attach-product-to-program
related_kus:
- KU-BANK-how-overdraft-works
- KU-ERR-codes-eovd
- KU-EVT-catalogue-overdraft
specification_version: 1.0.0
---

# API reference: Banking - Overdraft — Program

**KU ID:** `KU-API-banking-overdraft--program` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Program` in `api-specs/Banking_-_Overdraft.yaml` (“Banking - Overdraft”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/overdraft/programs/{programId}/attach` | `post-attach-product-to-program` | Attach overdraft product to program | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Overdraft.yaml method=POST path=/v1/overdraft/programs/{programId}/attach operationId=post-attach-product-to-program -->
### `POST /v1/overdraft/programs/{programId}/attach` — Attach overdraft product to program

- **operationId:** `post-attach-product-to-program`
- **Specification:** `api-specs/Banking_-_Overdraft.yaml` (Banking - Overdraft)
- **Server base URL(s):** `https://sandbox.pismolabs.io/overdraft`
- **Tags:** `Program`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Attach an overdraft product to a program.<br>
> This endpoint generates an [Overdraft program attached](https://developers.pismo.io/events/docs/overdraft-product-program-attach-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | string | Program ID | example: "123456" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ProductAttachRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | yes | Overdraft product ID | format: "uuid"; example: "876b2425-9778-4f02-8c50-67683e9a205e" |
| `metadata` | object | no | Additional details about the overdraft product. The information must be in `key:value` pair format. For example, `name:<your_name>`.<br><br>`minLength` = `0`<br>`maxLength` = `1024`<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | minLength: 0; maxLength: 1024; example: {"key": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Product attached successfully |  |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 403 | Forbidden | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Validation error` (Validation error) — from `#/components/examples/EOVD0008`:

```json
{
  "code": "EOVD0008",
  "message": "Validation error"
}
```

400 Example `Unmarshal error` (Unmarshal error) — from `#/components/examples/EOVD0012`:

```json
{
  "code": "EOVD0012",
  "message": "Unmarshal error"
}
```

400 Example `Ledger API 4xx error` (Ledger API 4xx error) — from `#/components/examples/EOVD0034`:

```json
{
  "code": "EOVD0034",
  "message": "Ledger API - Request returned error 4xx"
}
```

400 Example `Balance Watcher API 4xx error` (Balance Watcher API 4xx error) — from `#/components/examples/EOVD0040`:

```json
{
  "code": "EOVD0040",
  "message": "Balance Watcher API - Request returned error 4xx"
}
```

400 Example `Invalid account_id path parameter` (Invalid account_id path parameter) — from `#/components/examples/EOVD0043`:

```json
{
  "code": "EOVD0043",
  "message": "Invalid accountId path param"
}
```

400 Example `Account has attached product error` (Account has attached product error) — from `#/components/examples/EOVD0050`:

```json
{
  "code": "EOVD0050",
  "message": "The provided account already has an attached product"
}
```

400 Example `Accounts API 4xx error` (Accounts API 4xx error) — from `#/components/examples/EOVD0069`:

```json
{
  "code": "EOVD0069",
  "message": "Accounts API - Request returned error 4xx"
}
```

##### Response 403

403 Example `Overdraft limit not configured` (Overdraft limit not configured) — from `#/components/examples/EOVD0051`:

```json
{
  "code": "EOVD0051",
  "message": "Overdraft limit not configured"
}
```

##### Response 404

404 Example `Ledger API 404 error` (Ledger API 404 error) — from `#/components/examples/EOVD0035`:

```json
{
  "code": "EOVD0035",
  "message": "Ledger API - Request returned error 404"
}
```

404 Example `Balance Watcher API 404 error` (Balance Watcher API 404 error) — from `#/components/examples/EOVD0041`:

```json
{
  "code": "EOVD0041",
  "message": "Balance Watcher API - Request returned error 404"
}
```

404 Example `Product not found` (Product not found) — from `#/components/examples/EOVD0047`:

```json
{
  "code": "EOVD0047",
  "message": "Product not found"
}
```

404 Example `Accounts API 404 error` (Accounts API 404 error) — from `#/components/examples/EOVD0070`:

```json
{
  "code": "EOVD0070",
  "message": "Accounts API - Request returned error 404"
}
```

##### Response 409

409 Example `Product already attached` (Product already attached) — from `#/components/examples/EOVD0045`:

```json
{
  "code": "EOVD0045",
  "message": "The provided product ID is already attached"
}
```

##### Response 500

500 Example `Internal error` (Internal error) — from `#/components/examples/EOVD0007`:

```json
{
  "code": "EOVD0007",
  "message": "Internal error"
}
```

500 Example `Send event error` (Send event error) — from `#/components/examples/EOVD0029`:

```json
{
  "code": "EOVD0029",
  "message": "Error on sending event to topic"
}
```

500 Example `Ledger API request error` (Ledger API request error) — from `#/components/examples/EOVD0030`:

```json
{
  "code": "EOVD0030",
  "message": "Ledger API request error"
}
```

500 Example `Ledger API request timeout` (Ledger API request timeout) — from `#/components/examples/EOVD0031`:

```json
{
  "code": "EOVD0031",
  "message": "Ledger API  - Request timeout"
}
```

500 Example `Ledger API unmarshal response error` (Ledger API unmarshal response) — from `#/components/examples/EOVD0032`:

```json
{
  "code": "EOVD0032",
  "message": "Ledger API - Failed to unmarshal response body"
}
```

500 Example `Ledger API unmapped response code error` (Ledger API unmapped response code) — from `#/components/examples/EOVD0033`:

```json
{
  "code": "EOVD0033",
  "message": "Ledger API - Returned an unmapped response code"
}
```

500 Example `Ledger API 5xx error` (Ledger API 5xx error) — from `#/components/examples/EOVD0036`:

```json
{
  "code": "EOVD0036",
  "message": "Ledger API - Request returned error 5xx"
}
```

500 Example `Balance Watcher API unmarshal response` (Balance Watcher API unmarshal response) — from `#/components/examples/EOVD0038`:

```json
{
  "code": "EOVD0038",
  "message": "Balance Watcher API - Failed to unmarshal response body"
}
```

500 Example `Balance Watcher API unmapped response code error` (Balance Watcher API unmapped response code) — from `#/components/examples/EOVD0039`:

```json
{
  "code": "EOVD0039",
  "message": "Balance Watcher API - Returned an unmapped response code"
}
```

500 Example `Balance Watcher API 5xx error` (Balance Watcher API 5xx error) — from `#/components/examples/EOVD0042`:

```json
{
  "code": "EOVD0042",
  "message": "Balance Watcher API - Request returned error 5xx"
}
```

500 Example `Error getting product attachment` (Get product attachment error) — from `#/components/examples/EOVD0044`:

```json
{
  "code": "EOVD0044",
  "message": "Failed to get product attachment"
}
```

500 Example `Error getting product` (Get product error) — from `#/components/examples/EOVD0048`:

```json
{
  "code": "EOVD0048",
  "message": "Failed on get product"
}
```

500 Example `Error saving product attachment` (Save product attachment error) — from `#/components/examples/EOVD0052`:

```json
{
  "code": "EOVD0052",
  "message": "Failed to save product attachment"
}
```

500 Example `Accounts API request error` (Accounts API request error) — from `#/components/examples/EOVD0064`:

```json
{
  "code": "EOVD0064",
  "message": "Accounts API - Request error"
}
```

500 Example `Accounts API request timeout` (Accounts API request timeout) — from `#/components/examples/EOVD0065`:

```json
{
  "code": "EOVD0065",
  "message": "Accounts API - Request timeout"
}
```

500 Example `Accounts API unmarshal response error` (Accounts API unmarshal response) — from `#/components/examples/EOVD0066`:

```json
{
  "code": "EOVD0066",
  "message": "Accounts API - Failed to unmarshal response body"
}
```

500 Example `Accounts API unmapped response code error` (Accounts API unmapped response code) — from `#/components/examples/EOVD0067`:

```json
{
  "code": "EOVD0067",
  "message": "Accounts API - Returned an unmapped response code"
}
```

500 Example `Accounts API 5xx error` (Accounts API 5xx error) — from `#/components/examples/EOVD0068`:

```json
{
  "code": "EOVD0068",
  "message": "Accounts API - Request returned error 5xx"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOVD0008` | Validation error |
| 400 | `EOVD0012` | Unmarshal error |
| 400 | `EOVD0034` | Ledger API - Request returned error 4xx |
| 400 | `EOVD0040` | Balance Watcher API - Request returned error 4xx |
| 400 | `EOVD0043` | Invalid accountId path param |
| 400 | `EOVD0050` | The provided account already has an attached product |
| 400 | `EOVD0069` | Accounts API - Request returned error 4xx |
| 403 | `EOVD0051` | Overdraft limit not configured |
| 404 | `EOVD0035` | Ledger API - Request returned error 404 |
| 404 | `EOVD0041` | Balance Watcher API - Request returned error 404 |
| 404 | `EOVD0047` | Product not found |
| 404 | `EOVD0070` | Accounts API - Request returned error 404 |
| 409 | `EOVD0045` | The provided product ID is already attached |
| 500 | `EOVD0007` | Internal error |
| 500 | `EOVD0029` | Error on sending event to topic |
| 500 | `EOVD0030` | Ledger API request error |
| 500 | `EOVD0031` | Ledger API  - Request timeout |
| 500 | `EOVD0032` | Ledger API - Failed to unmarshal response body |
| 500 | `EOVD0033` | Ledger API - Returned an unmapped response code |
| 500 | `EOVD0036` | Ledger API - Request returned error 5xx |
| 500 | `EOVD0038` | Balance Watcher API - Failed to unmarshal response body |
| 500 | `EOVD0039` | Balance Watcher API - Returned an unmapped response code |
| 500 | `EOVD0042` | Balance Watcher API - Request returned error 5xx |
| 500 | `EOVD0044` | Failed to get product attachment |
| 500 | `EOVD0048` | Failed on get product |
| 500 | `EOVD0052` | Failed to save product attachment |
| 500 | `EOVD0064` | Accounts API - Request error |
| 500 | `EOVD0065` | Accounts API - Request timeout |
| 500 | `EOVD0066` | Accounts API - Failed to unmarshal response body |
| 500 | `EOVD0067` | Accounts API - Returned an unmapped response code |
| 500 | `EOVD0068` | Accounts API - Request returned error 5xx |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `overdraft-product-program-attach-1` | https://developers.pismo.io/events/docs/overdraft-product-program-attach-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;403;404;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-how-overdraft-works`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code | example: "EOVD0001" |
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
| `api-specs/Banking_-_Overdraft.yaml` | tag `Program`: POST /v1/overdraft/programs/{programId}/attach | https://github.com/PismoDevEx/pismo-api-specs | `957ed8db66676dab…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-how-overdraft-works` — How overdraft works
- `KU-ERR-codes-eovd` — Error codes: EOVD
- `KU-EVT-catalogue-overdraft` — Event catalogue: overdraft
