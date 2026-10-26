---
ku_id: KU-API-seller-management-sellers--settlements
title: 'API reference: Seller management - Sellers — Settlements'
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
- getAdvancementsBySettlement
related_kus:
- KU-ERR-codes-esmg-to-whis
specification_version: 1.0.0
---

# API reference: Seller management - Sellers — Settlements

**KU ID:** `KU-API-seller-management-sellers--settlements` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Settlements` in `api-specs/Seller_management_-_Sellers.yaml` (“Seller management - Sellers”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for settlements

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/merchants/{merchantId}/settlements/advancements` | `getAdvancementsBySettlement` | List advancement requests settled | no |

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=GET path=/v1/merchants/{merchantId}/settlements/advancements operationId=getAdvancementsBySettlement -->
### `GET /v1/merchants/{merchantId}/settlements/advancements` — List advancement requests settled

- **operationId:** `getAdvancementsBySettlement`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Settlements`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> List advancement requests settled per merchant using a <strong>tracking_id</strong>.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 24175 |
| `tracking_id` | query | yes | string | Pismo-generated ID for tracking the settlement authorization | example: "9999" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `ListAdvancementRequestsResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `advancements` | array of object | no |  |  |
| `advancements[].id` | integer (schema `AdvancementId`) | no | Advancement request id | format: "int32"; example: 23 |
| `advancements[].request_date` | string (schema `AdvancementRequestDate`) | no | Request date of the advancement. (Format = YYYY-MM-DD) | format: "date"; example: "2024-11-23" |
| `advancements[].advanced_gross_amount` | string (schema `AdvancedGrossAmount`) | no | Gross amount requested | example: "200.00" |
| `advancements[].advanced_discount_amount` | string (schema `AdvancedDiscountAmount`) | no | Advancement discount amount | example: "3.50" |
| `advancements[].advancement_fee` | string (schema `AdvancementFee`) | no | Fixed advancement fee | example: "1.00" |
| `advancements[].discount_rate` | string (schema `AdvancementDiscountRate`) | no | Merchant discount rate applied to the advancement operation | example: "0.0125" |
| `advancements[].advanced_net_amount` | string (schema `AdvancedNetAmount`) | no | Advancement net amount | example: "196.5" |
| `advancements[].interest_method` | string (schema `InterestMethod`) | no | Type of interest | enum: ["SIMPLE", "COMPOUND", "SIMPLIFIED"]; example: "SIMPLIFIED" |
| `advancements[].currency_code` | anyOf: string, null (schema `AdvancementCurrencyCode`) | no | ISO 4217 alphanumeric currency code of the advancement request. `null` when no currency is recorded. | example: "BRL" |

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

##### Response 404

404 Example `generic-not-found-response` (Not Found Response) — from `#/components/examples/NotFoundResponse`:

```json
{
  "code": "ISMA1001",
  "message": "Not found.",
  "details": {
    "payload": [
      {
        "field": "field_name",
        "description": "not found message"
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
| 404 | `ISMA1001` | Not found. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AdvancementCurrencyCode -->
### Schema `AdvancementCurrencyCode`

Pointer: `#/components/schemas/AdvancementCurrencyCode`. Type: anyOf: string, null (schema `AdvancementCurrencyCode`).

> ISO 4217 alphanumeric currency code of the advancement request. `null` when no currency is recorded.

anyOf: inline schema, inline schema

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
| `api-specs/Seller_management_-_Sellers.yaml` | tag `Settlements`: GET /v1/merchants/{merchantId}/settlements/advancements | https://github.com/PismoDevEx/pismo-api-specs | `eb5d18c21f5848fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
