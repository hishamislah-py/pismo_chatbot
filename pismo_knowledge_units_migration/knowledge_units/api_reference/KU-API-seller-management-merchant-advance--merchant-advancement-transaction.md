---
ku_id: KU-API-seller-management-merchant-advance--merchant-advancement-transaction
title: 'API reference: Seller management - Merchant advancements — Merchant advancement transaction'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Merchant_advance.yaml
  sha256: 73496f0c5425362468ba3bad070f5b51fa7d9f17ffe9ac6c43558a3ac3ee86ed
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
- merchants-transactions
related_kus:
- KU-ERR-codes-acq-to-esma
specification_version: 1.0.0
---

# API reference: Seller management - Merchant advancements — Merchant advancement transaction

**KU ID:** `KU-API-seller-management-merchant-advance--merchant-advancement-transaction` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Merchant advancement transaction` in `api-specs/Seller_management_-_Merchant_advance.yaml` (“Seller management - Merchant advancements”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for merchant advancement transactions

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` | `merchants-transactions` | List transactions | no |

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Merchant_advance.yaml method=GET path=/v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions operationId=merchants-transactions -->
### `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions` — List transactions

- **operationId:** `merchants-transactions`
- **Specification:** `api-specs/Seller_management_-_Merchant_advance.yaml` (Seller management - Merchant advancements)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement transaction`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Search for the balance of future schedules, consolidated by expected settlement date. In a head (centralizing) and branch (centralized) scenario, the transaction sum from all merchant branches is listed.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>"; example: "<your_token>" |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `merchantId` | path | yes | integer | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 20 |
| `startPaymentDate` | query | no | string | Date from which to search for a transaction | format: "date"; example: "2023-10-05T00:00:00.000Z" |
| `endPaymentDate` | query | no | string | End date for searching transactions | format: "date"; example: "2023-10-31T00:00:00.000Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `MerchantTransactionsResponse`) |
| 400 | BAD REQUEST | `application/json`: object (schema `DefaultErrorResponse`) |
| 404 | Marketplace or merchant does not belong to the tenant | `application/json`: object (schema `DefaultErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `currency_code` | string (schema `CurrencyCodeResponse`) | no | ISO-4217 alphabetic (3 characters) currency code.<br> | example: "BRL" |
| `items` | array of object | no |  |  |
| `items[].scheduled_payment_date` | string | no | Scheduling date for the next payment | format: "date"; example: "2023-10-29" |
| `items[].gross_value` | number | no | Merchant consolidated gross amount | format: "float"; example: 250 |
| `items[].discount` | number | no | Merchant consolidated discount amount | format: "float"; example: 8.25 |
| `items[].net_value` | number | no | Merchant consolidated net value | format: "float"; example: 241.75 |
| `items[].details` | array of object | no |  |  |
| `items[].details[].merchant_id` | integer | no | ID of the merchant who owns the transaction | example: 40305 |
| `items[].details[].merchant_name` | string | no | Name of the merchant who owns the transaction | example: "Merchant Name" |
| `items[].details[].gross_value` | number | no | Total transaction gross amount | format: "float"; example: 250 |
| `items[].details[].discount` | number | no | Total transaction discount amount | format: "float"; example: 8.25 |
| `items[].details[].net_value` | number | no | Total transaction net amount | format: "float"; example: 241.75 |
| `items[].details[].tax` | object | no | Taxes charged to the merchant |  |
| `items[].details[].tax.advancement_fee` | number | no | Fixed fee to be applied to the advancement request | format: "float"; example: 0 |
| `items[].details[].tax.discount_rate` | number | no | Discount rate used to calculate the discount over merchant advancements | format: "float"; example: 0.05 |
| `items[].details[].tax.maximum_advancement_percentage` | number | no | Maximum allowable percentage of the net amount for the advancement | format: "float"; example: 1 |
| `totals` | object | no |  |  |
| `totals.gross_value` | number | no | Total consolidated gross amount | format: "float"; example: 650 |
| `totals.discount` | number | no | Total consolidated discount amount | format: "float"; example: 8.25 |
| `totals.net_value` | number | no | Total consolidated net value | format: "float"; example: 641.75 |

200 Example `merchant-transactions-response-success` (Registration Response Success Example) — from `#/components/examples/MerchantTransactionsResponseSuccess`:

```json
{
  "currency_code": "BRL",
  "items": [
    {
      "scheduled_payment_date": "2023-10-29",
      "gross_value": 250,
      "discount": 8.25,
      "net_value": 241.75,
      "details": [
        {
          "merchant_id": 40305,
          "merchant_name": "Merchant Name",
          "gross_value": 250,
          "discount": 8.25,
          "net_value": 241.75,
          "tax": {
            "advancement_fee": 0,
            "discount_rate": 0.05,
            "maximum_advancement_percentage": 1
          }
        }
      ]
    }
  ],
  "totals": {
    "gross_value": 650,
    "discount": 8.25,
    "net_value": 641.75
  }
}
```

##### Response 400

400 Example `merchant-transactions-response-success` (Default Error Response) — from `#/components/examples/DefaultErrorResponse`:

```json
{
  "code": "EPT0303",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "MerchantID",
        "message": "Is not valid"
      },
      {
        "field": "MarketplaceID",
        "message": "Is not valid"
      }
    ]
  }
}
```

##### Response 404

404 Example `marketplace-not-found` (Default Error Response) — from `#/components/examples/DefaultErrorResponse`:

```json
{
  "code": "EPT0303",
  "message": "Failed during validation of request payload",
  "details": {
    "payload": [
      {
        "field": "MerchantID",
        "message": "Is not valid"
      },
      {
        "field": "MarketplaceID",
        "message": "Is not valid"
      }
    ]
  }
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPT0303` | Failed during validation of request payload |
| 404 | `EPT0303` | Failed during validation of request payload |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/DefaultErrorResponse -->
### Schema `DefaultErrorResponse`

Pointer: `#/components/schemas/DefaultErrorResponse`. Type: object (schema `DefaultErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Pismo internal error code |  |
| `message` | string | no | Error message |  |
| `details` | object | no | If necessary, this field shows which fields failed validation |  |
| `details.payload` | array of object | no | Array of fields with error |  |
| `details.payload[].field` | string | no | Name of field with error |  |
| `details.payload[].message` | string | no | Error Message referring to the field |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Merchant_advance.yaml` | tag `Merchant advancement transaction`: GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/transactions | https://github.com/PismoDevEx/pismo-api-specs | `73496f0c54253624…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
