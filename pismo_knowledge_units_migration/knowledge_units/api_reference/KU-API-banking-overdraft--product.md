---
ku_id: KU-API-banking-overdraft--product
title: 'API reference: Banking - Overdraft — Product'
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
- post-overdraft-product
- get-overdraft-product
related_kus:
- KU-BANK-how-overdraft-works
- KU-ERR-codes-eovd
- KU-EVT-catalogue-overdraft
specification_version: 1.0.0
---

# API reference: Banking - Overdraft — Product

**KU ID:** `KU-API-banking-overdraft--product` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Product` in `api-specs/Banking_-_Overdraft.yaml` (“Banking - Overdraft”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that manage overdraft products

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/overdraft` | `post-overdraft-product` | Create overdraft product | no |
| `GET /v1/overdraft/{productId}` | `get-overdraft-product` | Get overdraft product | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Overdraft.yaml method=POST path=/v1/overdraft operationId=post-overdraft-product -->
### `POST /v1/overdraft` — Create overdraft product

- **operationId:** `post-overdraft-product`
- **Specification:** `api-specs/Banking_-_Overdraft.yaml` (Banking - Overdraft)
- **Server base URL(s):** `https://sandbox.pismolabs.io/overdraft`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new overdraft product.<br>
> The overdraft API enables a bank to set an overdraft limit for an account when the balance is insufficient. For details, refer to [How overdraft works](doc:how-overdraft-works).<br>
> This endpoint generates an [Overdraft product created](https://developers.pismo.io/events/docs/overdraft-product-creation-1) event.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CreateProductRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | Overdraft product name. This name is defined by the client. | example: "Overdraft Limit 1000" |
| `interest_plan_id` | string | yes | Interest plan ID generated during the plan's creation. Created via the [Create interest plan](ref:post-v1-interest-plan) endpoint. | format: "uuid"; example: "b935acaf-886c-4817-8f7c-c2cc3ce4d509" |
| `processing_code` | object (schema `ProcessingCode`) | yes |  |  |
| `grace_period` | integer | no | Grace period during which you can restore the balance without incurring any interest charges. The unit is measured in days. | example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Product created successfully | `application/json`: object (schema `Product`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | no | Product ID generated for an overdraft product. Once this ID is created, you must link it to your account ID. | format: "uuid" |
| `name` | string | no | Produt name | example: "Overdraft Limit 1000" |
| `interest_plan_id` | string | no | Interest plan ID generated during the plan's creation. Created via the [Create interest plan](ref:post-v1-interest-plan-1) endpoint. | format: "uuid" |
| `grace_period` | integer | no | Grace period during which you can restore the balance without incurring any interest charges. The unit is measured in days. |  |
| `processing_code` | object (schema `ProcessingCode`) | no |  |  |
| `status` | string | no | Overdraft product status.<br><br>* `CREATED`: When you successfully created an overdraft product.<br>* `ACTIVE`: When you attach your overdraft product to an account or a program ID. Once it's attached, the product becomes `ACTIVE`.<br> | enum: ["CREATED", "ACTIVE"]; format: "enum" |
| `created_at_datetime` | string | no | Product created datetime. Format: `YYYY-MM-DDThh:mm:ss.sss`.<br> | format: "date-time" |

201 Example `Product created successfully` (Product created successful) — from `#/components/examples/200201ProductCreatedSuccessfulExample`:

```json
{
  "product_id": "2c336e9d-d04f-4fd0-8f6e-25808f48d70c",
  "name": "Overdraft limit 1000",
  "interest_plan_id": "b935acaf-886c-4817-8f7c-c2cc3ce4d509",
  "grace_period": 10,
  "processing_code": {
    "interest_processing_code": "123456"
  },
  "status": "CREATED",
  "created_at_datetime": "2024-01-23T13:26:25"
}
```

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

400 Example `Interest plan API 4xx error` (Interest plan API 4xx error) — from `#/components/examples/EOVD0020`:

```json
{
  "code": "EOVD0020",
  "message": "Interest Plan API - Request returned error 4xx"
}
```

400 Example `Unicode escape sequence error` (Unicode escape sequence error) — from `#/components/examples/EOVD0076`:

```json
{
  "code": "EOVD0076",
  "message": "Request contains Unicode escape sequences, which are not allowed. Remove all Unicode escape sequences from the request."
}
```

##### Response 404

404 Example `Interest plan not found` (Interest plan not found) — from `#/components/examples/EOVD0021`:

```json
{
  "code": "EOVD0021",
  "message": "Interest plan API - Interest plan not found"
}
```

##### Response 422

422 Example `Payments API 4xx error` (Payments API 4xx error) — from `#/components/examples/EOVD0027`:

```json
{
  "code": "EOVD0027",
  "message": "Payments API - Request returned error 4xx"
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

500 Example `Interest plan API request error` (Interest plan API request error) — from `#/components/examples/EOVD0015`:

```json
{
  "code": "EOVD0015",
  "message": "Interest plan API - Request error"
}
```

500 Example `Interest plan API request timeout` (Interest plan API request timeout) — from `#/components/examples/EOVD0016`:

```json
{
  "code": "EOVD0016",
  "message": "Interest plan API - Request timeout"
}
```

500 Example `Interest plan API unmarshal response error` (Interest plan API unmarshal response) — from `#/components/examples/EOVD0017`:

```json
{
  "code": "EOVD0017",
  "message": "Interest plan API - Failed to unmarshal response body"
}
```

500 Example `Interest plan API unmapped response code error` (Interest plan API unmapped response code) — from `#/components/examples/EOVD0018`:

```json
{
  "code": "EOVD0018",
  "message": "Interest plan API - Returned an unmapped response code"
}
```

500 Example `Interest plan API 5xx error` (Interest plan API 5xx error) — from `#/components/examples/EOVD0019`:

```json
{
  "code": "EOVD0019",
  "message": "Interest plan API - Request returned error 5xx"
}
```

500 Example `Payments API request error` (Payments API request error) — from `#/components/examples/EOVD0022`:

```json
{
  "code": "EOVD0022",
  "message": "Payments API - Request error"
}
```

500 Example `Payments API request timeout` (Payments API request timeout) — from `#/components/examples/EOVD0023`:

```json
{
  "code": "EOVD0023",
  "message": "Payments API - Request timeout"
}
```

500 Example `Payments API unmarshal response error` (Payments API unmarshal response) — from `#/components/examples/EOVD0024`:

```json
{
  "code": "EOVD0024",
  "message": "Payments API - Failed to unmarshal response body"
}
```

500 Example `Payments API 5xx error` (Payments API 5xx error) — from `#/components/examples/EOVD0025`:

```json
{
  "code": "EOVD0025",
  "message": "Payments API - Request returned error 5xx"
}
```

500 Example `Payments API unmapped response code error` (Payments API unmapped response code) — from `#/components/examples/EOVD0026`:

```json
{
  "code": "EOVD0026",
  "message": "Payments API - Returned an unmapped response code"
}
```

500 Example `Save product error` (Save product error) — from `#/components/examples/EOVD0028`:

```json
{
  "code": "EOVD0028",
  "message": "Failed to save product"
}
```

500 Example `Send event error` (Send event error) — from `#/components/examples/EOVD0029`:

```json
{
  "code": "EOVD0029",
  "message": "Error on sending event to topic"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOVD0008` | Validation error |
| 400 | `EOVD0012` | Unmarshal error |
| 400 | `EOVD0020` | Interest Plan API - Request returned error 4xx |
| 400 | `EOVD0076` | Request contains Unicode escape sequences, which are not allowed. Remove all Unicode escape sequences from the request. |
| 404 | `EOVD0021` | Interest plan API - Interest plan not found |
| 422 | `EOVD0027` | Payments API - Request returned error 4xx |
| 500 | `EOVD0007` | Internal error |
| 500 | `EOVD0015` | Interest plan API - Request error |
| 500 | `EOVD0016` | Interest plan API - Request timeout |
| 500 | `EOVD0017` | Interest plan API - Failed to unmarshal response body |
| 500 | `EOVD0018` | Interest plan API - Returned an unmapped response code |
| 500 | `EOVD0019` | Interest plan API - Request returned error 5xx |
| 500 | `EOVD0022` | Payments API - Request error |
| 500 | `EOVD0023` | Payments API - Request timeout |
| 500 | `EOVD0024` | Payments API - Failed to unmarshal response body |
| 500 | `EOVD0025` | Payments API - Request returned error 5xx |
| 500 | `EOVD0026` | Payments API - Returned an unmapped response code |
| 500 | `EOVD0028` | Failed to save product |
| 500 | `EOVD0029` | Error on sending event to topic |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `overdraft-product-creation-1` | https://developers.pismo.io/events/docs/overdraft-product-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;422;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-how-overdraft-works`.

<!-- op: spec=api-specs/Banking_-_Overdraft.yaml method=GET path=/v1/overdraft/{productId} operationId=get-overdraft-product -->
### `GET /v1/overdraft/{productId}` — Get overdraft product

- **operationId:** `get-overdraft-product`
- **Specification:** `api-specs/Banking_-_Overdraft.yaml` (Banking - Overdraft)
- **Server base URL(s):** `https://sandbox.pismolabs.io/overdraft`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get details of a specific overdraft product.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | yes | string | Overdraft product ID | format: "uuid"; example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get product details successful | `application/json`: object (schema `Product`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | no | Product ID generated for an overdraft product. Once this ID is created, you must link it to your account ID. | format: "uuid" |
| `name` | string | no | Produt name | example: "Overdraft Limit 1000" |
| `interest_plan_id` | string | no | Interest plan ID generated during the plan's creation. Created via the [Create interest plan](ref:post-v1-interest-plan-1) endpoint. | format: "uuid" |
| `grace_period` | integer | no | Grace period during which you can restore the balance without incurring any interest charges. The unit is measured in days. |  |
| `processing_code` | object (schema `ProcessingCode`) | no |  |  |
| `status` | string | no | Overdraft product status.<br><br>* `CREATED`: When you successfully created an overdraft product.<br>* `ACTIVE`: When you attach your overdraft product to an account or a program ID. Once it's attached, the product becomes `ACTIVE`.<br> | enum: ["CREATED", "ACTIVE"]; format: "enum" |
| `created_at_datetime` | string | no | Product created datetime. Format: `YYYY-MM-DDThh:mm:ss.sss`.<br> | format: "date-time" |

200 Example `Get overdraft product successful` (Product created successful) — from `#/components/examples/200201ProductCreatedSuccessfulExample`:

```json
{
  "product_id": "2c336e9d-d04f-4fd0-8f6e-25808f48d70c",
  "name": "Overdraft limit 1000",
  "interest_plan_id": "b935acaf-886c-4817-8f7c-c2cc3ce4d509",
  "grace_period": 10,
  "processing_code": {
    "interest_processing_code": "123456"
  },
  "status": "CREATED",
  "created_at_datetime": "2024-01-23T13:26:25"
}
```

##### Response 400

400 Example `Invalid product_id path parameter` (Invalid product_id path parameter) — from `#/components/examples/EOVD0073`:

```json
{
  "code": "EOVD0073",
  "message": "Invalid product_id path param"
}
```

400 Example `Invalid product ID format` (Invalid product_id format) — from `#/components/examples/EOVD0074`:

```json
{
  "code": "EOVD0074",
  "message": "Product ID format is invalid. Expected a valid UUID"
}
```

400 Example `Metadata validation error` (Metadata validation error) — from `#/components/examples/EOVD0075`:

```json
{
  "code": "EOVD0075",
  "message": "Metadata validation failed. Keys must be strings, and values must be ASCII strings."
}
```

400 Example `Unicode escape sequence error` (Unicode escape sequence error) — from `#/components/examples/EOVD0076`:

```json
{
  "code": "EOVD0076",
  "message": "Request contains Unicode escape sequences, which are not allowed. Remove all Unicode escape sequences from the request."
}
```

##### Response 404

404 Example `Product not found` (Product not found) — from `#/components/examples/EOVD0047`:

```json
{
  "code": "EOVD0047",
  "message": "Product not found"
}
```

##### Response 500

500 Example `Failed to get product` (Get product error) — from `#/components/examples/EOVD0048`:

```json
{
  "code": "EOVD0048",
  "message": "Failed on get product"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EOVD0073` | Invalid product_id path param |
| 400 | `EOVD0074` | Product ID format is invalid. Expected a valid UUID |
| 400 | `EOVD0075` | Metadata validation failed. Keys must be strings, and values must be ASCII strings. |
| 400 | `EOVD0076` | Request contains Unicode escape sequences, which are not allowed. Remove all Unicode escape sequences from the request. |
| 404 | `EOVD0047` | Product not found |
| 500 | `EOVD0048` | Failed on get product |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-how-overdraft-works`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ProcessingCode -->
### Schema `ProcessingCode`

Pointer: `#/components/schemas/ProcessingCode`. Type: object (schema `ProcessingCode`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_processing_code` | string | yes | Processing code for interest calculation | example: "123456" |

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
| `api-specs/Banking_-_Overdraft.yaml` | tag `Product`: POST /v1/overdraft, GET /v1/overdraft/{productId} | https://github.com/PismoDevEx/pismo-api-specs | `957ed8db66676dab…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-how-overdraft-works` — How overdraft works
- `KU-ERR-codes-eovd` — Error codes: EOVD
- `KU-EVT-catalogue-overdraft` — Event catalogue: overdraft
