---
ku_id: KU-API-seller-management-sellers--marketplace-merchants-links
title: 'API reference: Seller management - Sellers — Marketplace merchants links'
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
- listMarketplaceMerchantsLinked
- createMarketplaceMerchantsLink
- deleteMarketplaceMerchantLink
related_kus:
- KU-ERR-codes-esmg-to-whis
specification_version: 1.0.0
---

# API reference: Seller management - Sellers — Marketplace merchants links

**KU ID:** `KU-API-seller-management-sellers--marketplace-merchants-links` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Marketplace merchants links` in `api-specs/Seller_management_-_Sellers.yaml` (“Seller management - Sellers”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for managing marketplace relationships

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/marketplaces/{marketplaceId}/merchants` | `listMarketplaceMerchantsLinked` | List merchants linked to a marketplace | no |
| `POST /v1/marketplaces/{marketplaceId}/merchants` | `createMarketplaceMerchantsLink` | Link marketplace to merchants | no |
| `DELETE /v1/marketplaces/{marketplaceId}/merchants/{merchantId}` | `deleteMarketplaceMerchantLink` | Unlink marketplace and merchant | no |

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=GET path=/v1/marketplaces/{marketplaceId}/merchants operationId=listMarketplaceMerchantsLinked -->
### `GET /v1/marketplaces/{marketplaceId}/merchants` — List merchants linked to a marketplace

- **operationId:** `listMarketplaceMerchantsLinked`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Marketplace merchants links`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Returns information about the merchants linked to this marketplace

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 1654 |
| `page` | query | no | integer | Current page number | format: "int32"; minimum: 1; example: 1; example: 12 |
| `perPage` | query | no | integer | Number of items per page | format: "int32"; minimum: 1; example: 100 |
| `subnet` | query | no | string | Filter by merchant subnet. <br>Values are `individual`, `hq` (short for `Headquarters`), or `branch`. <br><br>A merchant is:<br>  * `hq` if it has branch merchants.<br>  * `branch` if it is another merchant's branch.<br>  * `individual` if it isn't a branch nor headquarters.<br><br>To create these relationships, use the [Link marketplace to merchants](https://developers.pismo.io/pismo-docs/reference/createmarketplacemerchantslink) endpoint.<br> | enum: ["individual", "hq", "branch"]; example: "hq" |
| `hqId` | query | no | integer | Filter by merchant headquarters ID | format: "int64"; minimum: 1; example: 8675409 |
| `branchId` | query | no | integer | Filter by merchant branch ID | format: "int64"; minimum: 1; example: 212121 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListMarketplaceMerchantsLinkResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | yes | Is a next page available? | example: true |
| `items` | array of object | yes |  |  |
| `items[].id` | integer (schema `MerchantId`) | no | Merchant ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 24175 |
| `items[].name` | string | no | Merchant name |  |
| `items[].document_number` | string | no | Merchant document number |  |
| `page` | integer | yes | Current page number (starts at 1) | format: "int32"; minimum: 1; example: 1 |
| `per_page` | integer | yes | Number of items per page | format: "int32"; minimum: 1; maximum: 100; example: 10 |

200 Example `marketplaces-merchants-link-list` (List linked merchants) — from `#/components/examples/ListMarketplaceMerchantsLink`:

```json
{
  "per_page": 100,
  "page": 1,
  "has_next": true,
  "items": [
    {
      "id": 1,
      "name": "Merchant 1",
      "document_number": "123"
    },
    {
      "id": 2,
      "name": "Merchant 2",
      "document_number": "456"
    },
    {
      "id": 3,
      "name": "Merchant 3",
      "document_number": "789"
    }
  ]
}
```

##### Response 500

500 Example `merchant-transactions-response-success` (Internal server error response) — from `#/components/examples/InternalServerErrorResponseExample`:

```json
{
  "message": "Internal Server Error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=POST path=/v1/marketplaces/{marketplaceId}/merchants operationId=createMarketplaceMerchantsLink -->
### `POST /v1/marketplaces/{marketplaceId}/merchants` — Link marketplace to merchants

- **operationId:** `createMarketplaceMerchantsLink`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Marketplace merchants links`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Link marketplace with a list of merchants.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 1654 |

#### Request body

Required: no

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `merchants` | array of integer | no | List of merchant IDs | example: [1, 2, 3]; items.format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Sellers.yaml method=DELETE path=/v1/marketplaces/{marketplaceId}/merchants/{merchantId} operationId=deleteMarketplaceMerchantLink -->
### `DELETE /v1/marketplaces/{marketplaceId}/merchants/{merchantId}` — Unlink marketplace and merchant

- **operationId:** `deleteMarketplaceMerchantLink`
- **Specification:** `api-specs/Seller_management_-_Sellers.yaml` (Seller management - Sellers)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Marketplace merchants links`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Delete link between marketplace and merchant.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 1654 |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 24175 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | `application/json`: object (schema `ErrorRequestResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorRequestResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorRequestResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

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

##### Response 409

409 Example `conflict-response` (Conflict response) — from `#/components/examples/ConflictResponse`:

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
| 404 | `ISMA1001` | Not found. |
| 409 | `ESMG0900` | Failed during validation of request payload |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/InternalServerErrorResponse -->
### Schema `InternalServerErrorResponse`

Pointer: `#/components/schemas/InternalServerErrorResponse`. Type: object (schema `InternalServerErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message |  |

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

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Sellers.yaml` | tag `Marketplace merchants links`: GET /v1/marketplaces/{marketplaceId}/merchants, POST /v1/marketplaces/{marketplaceId}/merchants, DELETE /v1/marketplaces/{marketplaceId}/merchants/{merchantId} | https://github.com/PismoDevEx/pismo-api-specs | `eb5d18c21f5848fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
