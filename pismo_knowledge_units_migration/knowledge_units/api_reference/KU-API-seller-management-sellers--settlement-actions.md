---
ku_id: KU-API-seller-management-sellers--settlement-actions
title: 'API reference: Seller management - Sellers — Settlement actions'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Sellers.yaml
  sha256: eb5d18c21f5848fe7db87917b88dfe2d23206e9b68f8382dc8c41745d518c00d
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
- blockMerchantsForSettlement
- unblockMerchantsForSettlement
- getBlockedMerchants
- runSettlement
related_kus:
- KU-ERR-codes-esmg-to-whis
specification_version: 1.0.0
---

# API reference: Seller management - Sellers — Settlement actions

**KU ID:** `KU-API-seller-management-sellers--settlement-actions` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Settlement actions` in `api-specs/Seller_management_-_Sellers.yaml` (“Seller management - Sellers”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for settlement actions

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/settlements/actions/block` | `blockMerchantsForSettlement` | Block merchants for settlement | no |
| `POST /v1/settlements/actions/unblock` | `unblockMerchantsForSettlement` | Unblock merchants for settlement | no |
| `GET /v1/settlements/merchants/blocked` | `getBlockedMerchants` | Get blocked merchants | no |
| `POST /v1/settlements/actions/run` | `runSettlement` | Run settlement | no |

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=POST path=/v1/settlements/actions/block operationId=blockMerchantsForSettlement -->
### `POST /v1/settlements/actions/block` — Block merchants for settlement

- **operationId:** `blockMerchantsForSettlement`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Settlement actions`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Block merchants for settlement.
>
> Designates merchants that should be skipped in the settlement process.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `SettlementMerchantsPayload`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `marketplace_id` | integer (schema `MarketplaceId`) | yes | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 51148 |
| `merchant_ids` | array of integer (schema `MerchantId`) (schema `MerchantIds`) | yes |  | items.format: "int64" |

Example `merchant-transactions-response-success` (Block Merchants Payload) — from `#/components/examples/SettlementMerchantsPayloadExample`:

```json
{
  "marketplace_id": 1,
  "merchant_ids": [
    1
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreatedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Pismo internal code |  |
| `message` | string | no | Message |  |

201 Example `merchant-transactions-response-success` (Created response) — from `#/components/examples/CreatedResponseExample`:

```json
{
  "code": "ISMG0001",
  "message": "Success."
}
```

##### Response 400

400 Example `merchant-transactions-response-success` (Bad request response) — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "ESMG0900",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 201 | `ISMG0001` | Success. |
| 400 | `ESMG0900` | Failed during validation of request payload |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=POST path=/v1/settlements/actions/unblock operationId=unblockMerchantsForSettlement -->
### `POST /v1/settlements/actions/unblock` — Unblock merchants for settlement

- **operationId:** `unblockMerchantsForSettlement`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Settlement actions`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Unblock merchants that were previously blocked using the [Block merchants for settlement](ref:blockmerchantsforsettlement) endpoint. Unblocked merchants are no longer skipped in the settlement process.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `SettlementMerchantsPayload`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `marketplace_id` | integer (schema `MarketplaceId`) | yes | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 51148 |
| `merchant_ids` | array of integer (schema `MerchantId`) (schema `MerchantIds`) | yes |  | items.format: "int64" |

Example `merchant-transactions-response-success` (Block Merchants Payload) — from `#/components/examples/SettlementMerchantsPayloadExample`:

```json
{
  "marketplace_id": 1,
  "merchant_ids": [
    1
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: array of object (schema `GetBlockedMerchantsResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `merchant-transactions-response-success` (Get blocked merchants response) — from `#/components/examples/GetBlockedMerchantsResponseExample`:

```json
[
  {
    "marketplace_id": 1,
    "merchant_ids": [
      1,
      2
    ]
  },
  {
    "marketplace_id": 2,
    "merchant_ids": [
      3
    ]
  }
]
```

##### Response 400

400 Example `merchant-transactions-response-success` (Bad request response) — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "ESMG0900",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMG0900` | Failed during validation of request payload |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=GET path=/v1/settlements/merchants/blocked operationId=getBlockedMerchants -->
### `GET /v1/settlements/merchants/blocked` — Get blocked merchants

- **operationId:** `getBlockedMerchants`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Settlement actions`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Retrieve merchants that were previously blocked using the [Block merchants for settlement](ref:blockmerchantsforsettlement) endpoint.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: array of object (schema `GetBlockedMerchantsResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `merchant-transactions-response-success` (Get blocked merchants response) — from `#/components/examples/GetBlockedMerchantsResponseExample`:

```json
[
  {
    "marketplace_id": 1,
    "merchant_ids": [
      1,
      2
    ]
  },
  {
    "marketplace_id": 2,
    "merchant_ids": [
      3
    ]
  }
]
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=POST path=/v1/settlements/actions/run operationId=runSettlement -->
### `POST /v1/settlements/actions/run` — Run settlement

- **operationId:** `runSettlement`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Settlement actions`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Start the settlement process for a specified merchant.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `RunSettlementPayload`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `marketplace_id` | integer (schema `MarketplaceId`) | yes | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 51148 |
| `merchant_id` | integer (schema `MerchantId`) | yes | Merchant ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 24175 |

Example `merchant-transactions-response-success` (Run Settlement Payload) — from `#/components/examples/RunSettlementPayload`:

```json
{
  "marketplace_id": 1,
  "merchant_id": 1
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `CreatedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Pismo internal code |  |
| `message` | string | no | Message |  |

202 Example `merchant-transactions-response-success` (Created response) — from `#/components/examples/CreatedResponseExample`:

```json
{
  "code": "ISMG0001",
  "message": "Success."
}
```

##### Response 400

400 Example `merchant-transactions-response-success` (Bad request response) — from `#/components/examples/BadRequestResponse`:

```json
{
  "code": "ESMG0900",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "message": "validation message"
      }
    ]
  }
}
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 202 | `ISMG0001` | Success. |
| 400 | `ESMG0900` | Failed during validation of request payload |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorRequestResponse -->
### Schema `ErrorRequestResponse`

Pointer: `#/components/schemas/ErrorRequestResponse`. Type: object (schema `ErrorRequestResponse`).

> Error payload returned by the API

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Pismo internal error code |  |
| `message` | string | no | Error message |  |
| `details` | object | no | If necessary, this field shows which fields failed validation |  |
| `details.payload` | array of object | no | Array of fields with error |  |
| `details.payload[].field` | string | no | Name of field with error |  |
| `details.payload[].message` | string | no | Error message referring to the field |  |

<!-- schema: #/components/schemas/InternalServerErrorResponse -->
### Schema `InternalServerErrorResponse`

Pointer: `#/components/schemas/InternalServerErrorResponse`. Type: object (schema `InternalServerErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Sellers.yaml` | tag `Settlement actions`: POST /v1/settlements/actions/block, POST /v1/settlements/actions/unblock, GET /v1/settlements/merchants/blocked, POST /v1/settlements/actions/run | https://github.com/PismoDevEx/pismo-api-specs | `eb5d18c21f5848fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
