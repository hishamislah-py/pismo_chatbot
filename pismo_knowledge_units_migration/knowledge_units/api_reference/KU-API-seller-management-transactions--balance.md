---
ku_id: KU-API-seller-management-transactions--balance
title: 'API reference: Seller management - Transactions — Balance'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Transactions.yaml
  sha256: f064908196c8f7cdd21e34e27572c6f95f92f3503251232b87c3d12d769ca000
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
- get-merchant-balance
related_kus:
- KU-ERR-codes-esmg-to-whis
specification_version: 1.0.0
---

# API reference: Seller management - Transactions — Balance

**KU ID:** `KU-API-seller-management-transactions--balance` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Balance` in `api-specs/Seller_management_-_Transactions.yaml` (“Seller management - Transactions”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Balance endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/balance` | `get-merchant-balance` | Get merchant balance | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Transactions.yaml method=GET path=/v1/marketplaces/{marketplaceId}/merchants/{merchantId}/balance operationId=get-merchant-balance -->
### `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/balance` — Get merchant balance

- **operationId:** `get-merchant-balance`
- **Specification:** `api-specs/Seller_management_-_Transactions.yaml` (Seller management - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/sellers`
- **Tags:** `Balance`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> The merchant balance endpoint provides an estimate of the available funds in the merchant account on a specified target date. It takes into account the scheduled merchant transactions in the specified marketplace to calculate the estimated values.
>
> `estimated_available_amount` represents the forecasted amount that might be available to the merchant on the target date, based on the current scheduled transactions. This estimate is subject to change due to cancellations, new transactions, and advancements made by the merchant until the target date arrives.
>
> If the merchant's scheduled balance is negative, the amount accumulates in the `scheduled_amount` field until it becomes positive and is available for settlement. Therefore, a negative `scheduled_amount` is not considered for settlement until it turns positive.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>" |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `merchantId` | path | yes | integer | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `date` | query | no | string | Target date to compose the balance amount. The date format used is ISO 8601.<br>minLength: 10<br>maxLength: 10<br><br>The date must be the current or a future date. If not provided, it defaults to the current date of the target merchant timezone.<br> | format: "date"; example: "2025-04-20T00:00:00.000Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successfully get merchant balance | `application/json`: object (schema `BalanceRequestGetResponse`) |
| 400 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 404 | Bad request | `application/json`: object (schema `DefaultErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `InternalServerErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date` | string (schema `TargetDate_date`) | no | Target date to estimate the merchant balance | format: "date" |
| `current_available_amount` | number (schema `CurrentAvailableAmount`) | no | Amount available in the merchant account. It is always the exact amount in that account, regardless of the target date | format: "float" |
| `estimated_available_amount` | number (schema `EstimatedAvailableAmount`) | no | Estimated available amount in the merchant account on the target date. This includes all scheduled amounts that are projected to be settled and available in the merchant account by that date. | format: "float" |
| `scheduled_amount` | number (schema `ScheduledAmount`) | no | Scheduled amount on the target date. The scheduled amount is the amount that is not yet available, but is scheduled to be settled on the target date. | format: "float" |
| `currency_code` | string (schema `OptionalCurrencyCodeResponse`) | no | ISO 4217 alphanumeric currency code. `null` when no currency is recorded. | nullable: true; example: "BRL" |

200 Example `Get merchant balance` (Get merchant balance response) — from `#/components/examples/BalanceRequestGetResponse`:

```json
{
  "date": "2025-03-01",
  "current_available_amount": 233.21,
  "estimated_available_amount": 300,
  "scheduled_amount": 203.1,
  "currency_code": "BRL"
}
```

##### Response 400

400 Example `400 Bad request` (Bad request response) — from `#/components/examples/DefaultErrorResponse`:

```json
{
  "code": "ESMT0001",
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

404 Example `Not found` (Not found response) — from `#/components/examples/DefaultNotFoundResponse`:

```json
{
  "code": "ESMT0003",
  "message": "Merchant not found"
}
```

##### Response 500

500 Example `Internal server error` (Internal Server Error Response) — from `#/components/examples/InternalServerErrorResponse`:

```json
{
  "message": "Internal Server Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ESMT0001` | Failed during validation of request payload |
| 404 | `ESMT0003` | Merchant not found |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/DefaultErrorResponse -->
### Schema `DefaultErrorResponse`

Pointer: `#/components/schemas/DefaultErrorResponse`. Type: object (schema `DefaultErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Pismo internal error code |  |
| `message` | string (schema `ErrorMessage`) | no | Error message |  |
| `details` | object (schema `ErrorDetails`) | no | If necessary, this field shows which fields failed validation |  |

<!-- schema: #/components/schemas/InternalServerErrorResponse -->
### Schema `InternalServerErrorResponse`

Pointer: `#/components/schemas/InternalServerErrorResponse`. Type: object (schema `InternalServerErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string (schema `InternalServerErrorMessage`) | no | Internal server error |  |

<!-- schema: #/components/schemas/ErrorDetails -->
### Schema `ErrorDetails`

Pointer: `#/components/schemas/ErrorDetails`. Type: object (schema `ErrorDetails`).

> If necessary, this field shows which fields failed validation

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payload` | array of object | no | Array of fields with error |  |
| `payload[].field` | string (schema `ErrorField`) | no | Name of field with error |  |
| `payload[].message` | string (schema `ErrorFieldMessage`) | no | Error Message referring to the field |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Transactions.yaml` | tag `Balance`: GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/balance | https://github.com/PismoDevEx/pismo-api-specs | `f064908196c8f7cd…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
