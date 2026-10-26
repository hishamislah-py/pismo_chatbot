---
ku_id: KU-API-seller-management-merchant-advance--merchant-advancement
title: 'API reference: Seller management - Merchant advancements — Merchant advancement'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- list-merchants-advancements
- merchants-advancements
- merchant-transaction-advancement
- merchants-advancements-data
related_kus:
- KU-ERR-codes-acq-to-esma
- KU-EVT-catalogue-merchants
- KU-EVT-merchant-advancements-data-events
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
- KU-SELL-seller-marketplace-implementation-steps
specification_version: 1.0.0
---

# API reference: Seller management - Merchant advancements — Merchant advancement

**KU ID:** `KU-API-seller-management-merchant-advance--merchant-advancement` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Merchant advancement` in `api-specs/Seller_management_-_Merchant_advance.yaml` (“Seller management - Merchant advancements”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for merchant advancements

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/merchants/{merchantId}/advancements` | `list-merchants-advancements` | List merchant advancement requests | no |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements` | `merchants-advancements` | Simulate merchant advancement | no |
| `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/transactions` | `merchant-transaction-advancement` | Simulate transaction advancement | no |
| `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/{advancementId}` | `merchants-advancements-data` | Get advancement | no |

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Merchant_advance.yaml method=GET path=/v2/merchants/{merchantId}/advancements operationId=list-merchants-advancements -->
### `GET /v2/merchants/{merchantId}/advancements` — List merchant advancement requests

- **operationId:** `list-merchants-advancements`
- **Specification:** `api-specs/Seller_management_-_Merchant_advance.yaml` (Seller management - Merchant advancements)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> List advancement requests for a merchant, with optional filters by status and date ranges, plus pagination and sorting.
>
> **Date filters.** `beginDateFrom`, `beginDateTo`, `requestDateFrom`, `requestDateTo` accept `YYYY-MM-DD`. The `*From` filters match advancements on or after the given date; the `*To` filters match advancements on or before it.
>
> **Pagination and sorting.** `page` defaults to 1 and `perPage` defaults to 10; `0` is treated as the default for both. `perPage` accepts up to 100. `order` accepts `asc` or `desc`. `orderBy` accepts `request_date`, `begin_date`, `end_date`, `status`, or `advancement_request_id`; any other value is treated as `request_date`. The default sort is `request_date DESC`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `merchantId` | path | yes | integer | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 20 |
| `status` | query | no | string | Filter advancement requests by exact status. Strict — any other value returns 400. | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PROCESSED" |
| `beginDateFrom` | query | no | string | Filters advancements with `begin_date` on or after this date. Format = `YYYY-MM-DD`.<br> | format: "date"; example: "2026-04-20" |
| `beginDateTo` | query | no | string | Filters advancements with `begin_date` on or before this date. Format = `YYYY-MM-DD`. Must be greater than or equal to `beginDateFrom` when both are provided.<br> | format: "date"; example: "2026-04-20" |
| `requestDateFrom` | query | no | string | Filters advancements with `request_date` on or after this date. Format = `YYYY-MM-DD`.<br> | format: "date"; example: "2026-04-15" |
| `requestDateTo` | query | no | string | Filters advancements with `request_date` on or before this date. Format = `YYYY-MM-DD`. Must be greater than or equal to `requestDateFrom` when both are provided.<br> | format: "date"; example: "2026-04-15" |
| `page` | query | no | integer | 1-based page number. Defaults to 1 when omitted or set to 0. | default: 1; format: "int32"; minimum: 1; example: 1 |
| `perPage` | query | no | integer | Number of items per page. Defaults to 10 when omitted or set to 0. | default: 10; format: "int32"; minimum: 1; maximum: 100; example: 10 |
| `order` | query | no | string | Sort order direction. Defaults to `desc` when omitted or set to empty string. | enum: ["asc", "desc"]; example: "desc" |
| `orderBy` | query | no | string | Column name to sort by. Unknown values fall back to the endpoint's default at the repository layer (no error). | example: "request_date" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AdvancementListResponse`) |
| 400 | BAD REQUEST — invalid `status`; invalid date filter (must be `YYYY-MM-DD`); inverted date range; `perPage > 100`; negative `page`/`perPage`; `order` outside `asc/desc`. | `application/json`: object (schema `DefaultErrorResponse`) |
| 404 | Merchant does not belong to the tenant. | `application/json`: object (schema `DefaultErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `page` | integer | yes | 1-based page number of the current response. | format: "int32"; example: 1 |
| `per_page` | integer | yes | Items per page applied to the current response. | format: "int32"; example: 10 |
| `has_next` | boolean | yes | True when at least one more page exists after this one. | example: false |
| `items` | array of object (schema `AdvancementListItem`) | yes | Advancement request items in the current page. May be empty. |  |

200 Example `advancement-list-response-success` (List Advancement Requests Success) — from `#/components/examples/AdvancementListResponseSuccess`:

```json
{
  "page": 1,
  "per_page": 10,
  "has_next": false,
  "items": [
    {
      "advancement_request_id": 5531,
      "begin_date": "2026-04-20",
      "end_date": "2026-07-20",
      "request_date": "2026-04-15",
      "status": "PROCESSED",
      "real_time_settlement": false,
      "interest_method": "COMPOUND",
      "advancement_gross_amount": 9876.5,
      "advancement_net_amount": 9756.05,
      "advancement_discount_amount": 120.45,
      "error_message": null,
      "currency_code": "BRL"
    },
    {
      "advancement_request_id": 5520,
      "begin_date": "2026-04-10",
      "end_date": null,
      "request_date": "2026-04-09",
      "status": "PENDING",
      "real_time_settlement": false,
      "interest_method": "SIMPLIFIED",
      "advancement_gross_amount": null,
      "advancement_net_amount": null,
      "advancement_discount_amount": null,
      "error_message": null,
      "currency_code": null
    }
  ]
}
```

##### Response 400

400 Example `advancement-list-bad-request` (Default Error Response) — from `#/components/examples/DefaultErrorResponse`:

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

404 Example `advancement-list-not-found` (Default Error Response) — from `#/components/examples/DefaultErrorResponse`:

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

<!-- op: spec=api-specs/Seller_management_-_Merchant_advance.yaml method=POST path=/v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements operationId=merchants-advancements -->
### `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements` — Simulate merchant advancement

- **operationId:** `merchants-advancements`
- **Specification:** `api-specs/Seller_management_-_Merchant_advance.yaml` (Seller management - Merchant advancements)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create or simulate a merchant advancement request.  To trigger a simulated advancement request, you must include `confirmAdvancement=false` in the query. If you specify `true`, the advancement request becomes an actual request, not a simulation.<br>
>
> The endpoint enables a merchant to simulate an advancement scenario in order to validate whether or not there is enough balance in the account, as well as how much tax is anticipated. Since a simulated advancement is not a real advancement, it is not processed.
>
> A merchant advancement is sometimes called a prepayment of receivables. You arrange to have a financial institution make regular deposits into your account equal to what you expect to receive in the future from credit card sales in installments or post-dated
> checks and bills. The financial institution deducts its fee before it puts the money in your account. You pay back each deposit when you receive
> payment from your customers. This is a way of covering business expenses in the short term. It's a cheaper alternative to a loan.<br>
>
> <b>Note</b>:
> - If the merchant is the head merchant (also called a centralizer), the advanced amount is given to the head merchant instead of individual branch merchants, this is designed for better manageability.
> - If the commercial establishment is not registered as a headquarter or a branch in the current marketplace, the advancement is for a single commercial establishment.
> - The merchant must have sufficient balance in the account for the specified date range of the advancement.
>
> This endpoint generates a [Merchant advancement request created](https://developers.pismo.io/events/docs/merchants-advancement-request-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>"; example: "<your_token>" |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `merchantId` | path | yes | integer | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 20 |
| `confirmAdvancement` | query | no | boolean | Flag that indicates whether this is an effective advancement or just a simulation. The default value is `false`. | default: false; example: false; example: false |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `MerchantsAdvancementsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `begin_date` | string | yes | Used for searching merchant advancement requests. This is the start date of your search range. | format: "date"; minLength: 10; maxLength: 10 |
| `request_date` | string | yes | Date for payment of the advancement (YYYY-MM-DD). Must be greater than or equal to today, where "today" is evaluated in the merchant program's resolved timezone. The organization's timezone is used as fallback. | format: "date"; minLength: 10; maxLength: 10 |
| `amount` | number | yes | Net amount to be paid in advance | format: "float"; minimum: 1; maximum: 4294967295 |
| `currency_code` | string (schema `CurrencyCode`) | no | Represents the currency with an ISO-4217 alphabetic or numeric (3 characters) string. For example, you represent Brazilian real with either BRL or 986.<br>If you don't provide this code, the system uses the currency from the merchant program.<br> | example: "986" |
| `real_time_settlement` | boolean | yes | If `true`, the transaction is settled real-time; that is, at the exact moment. Default is `false` | default: false |
| `end_date` | string | no | Used for searching merchant advancement requests. This is the end date of your search range | format: "date"; minLength: 10; maxLength: 10 |
| `campaign_advancement_fee` | number | no | Campaign advancement fee to be applied to the current advancement request. It replaces the advancement fee set for the merchant in the request | format: "float"; minimum: 1; maximum: 4294967295 |
| `campaign_discount_rate` | number | no | Campaign discount rate to be applied to all merchants in the current advancement request | format: "float"; minimum: 1; maximum: 4294967295 |
| `merchants` | array of object | no |  |  |
| `merchants[].merchant_id` | integer | no | Merchant ID of the advancement request. Must be the current merchant or a branch of the current merchant | format: "uint64"; minimum: 1; maximum: 18446744073709552000 |
| `merchants[].campaign_discount_rate` | number | no | Rate to be applied to a single merchant | format: "float"; minimum: 1; maximum: 4294967295 |

Example `merchant-advancements-request` (Registration Response Success Example) — from `#/components/examples/MerchantsAdvancementsRequest`:

```json
{
  "begin_date": "2023-08-01",
  "end_date": "2023-08-31",
  "request_date": "2023-08-10",
  "amount": 100,
  "currency_code": "BRL",
  "real_time_settlement": false,
  "campaign_advancement_fee": 5,
  "campaign_discount_rate": 1.024,
  "merchants": [
    {
      "merchant_id": 2,
      "campaign_discount_rate": 5
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `MerchantsAdvancementsResponse`) |
| 400 | BAD REQUEST | `application/json`: object (schema `DefaultErrorResponse`) |
| 404 | Marketplace or merchant does not belong to the tenant | `application/json`: object (schema `DefaultErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `simulation_id` | string | no | A unique UUID generated for the simulated advancement. This field is only returned if it is a simulation |  |
| `advancement_request_id` | integer | no | This field is returned only if it's an actual advancement request (`EFFECTIVE`) |  |
| `type` | string | no | Operation type, returns either `SIMULATION` or `EFFECTIVE` |  |
| `currency_code` | string (schema `CurrencyCodeResponse`) | no | ISO-4217 alphabetic (3 characters) currency code.<br> | example: "BRL" |
| `begin_date` | string | no | Used for searching merchant transactions. This is the start date of your search range | format: "date" |
| `end_date` | string | no | Used for searching merchant transactions. This is the end date of your search range | format: "date" |
| `request_date` | string | no | Advancement request date | format: "date" |

200 Example `merchant-advancement-response-success` (Registration Response Success Example) — from `#/components/examples/MerchantsAdvancementsResponseSuccess`:

```json
{
  "simulation_id": "a882e95e-5138-4e85-a89c-26778f2e4b14",
  "advancement_request_id": 1,
  "type": "SIMULATION",
  "currency_code": "BRL",
  "begin_date": "2023-08-01",
  "end_date": "2023-08-31",
  "request_date": "2023-08-10"
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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-advancement-request-1` | https://developers.pismo.io/events/docs/merchants-advancement-request-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-merchant-advancements-data-events`, `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`, `KU-SELL-seller-marketplace-implementation-steps`.

<!-- op: spec=api-specs/Seller_management_-_Merchant_advance.yaml method=POST path=/v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/transactions operationId=merchant-transaction-advancement -->
### `POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/transactions` — Simulate transaction advancement

- **operationId:** `merchant-transaction-advancement`
- **Specification:** `api-specs/Seller_management_-_Merchant_advance.yaml` (Seller management - Merchant advancements)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Create or simulate a merchant advancement request for specified transactions. You can select which transaction you want to advance by specifying a merchant transaction ID. To trigger a simulated advancement request, you must include `confirmAdvancement=false` in the query string. If you specify `true`, the advancement request becomes an actual request, not a simulation.<br>
>
> When a merchant advancement transaction is created, the endpoint produces [Merchant transaction created](https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1) and
> [Merchant advancement transaction created](https://developers.pismo.io/events/docs/merchants-advancement-transaction-create-1) events.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>"; example: "<your_token>" |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `merchantId` | path | yes | integer | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 20 |
| `confirmAdvancement` | query | no | boolean | Flag that indicates whether this is an effective advancement or just a simulation. The default value is `false`. | default: false; example: false; example: false |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `TransactionsAdvancementsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `request_date` | string | yes | Date for payment of the advancement (YYYY-MM-DD). Must be greater than or equal to today, where "today" is evaluated in the merchant program's resolved timezone. The organization's timezone is used as fallback. | format: "date"; minLength: 10; maxLength: 10 |
| `real_time_settlement` | boolean | yes | If `true`, the transaction is settled in realtime; that is, at the exact moment. The default is `false`. | default: false |
| `merchant_transaction_ids` | array of integer | yes | List of Merchant Transaction IDs |  |
| `campaign_advancement_fee` | number | no | Campaign advancement fee applied to the current advancement request. It replaces the advancement fee set for the merchant in the request. | format: "float"; minimum: 0; maximum: 999999.99 |
| `campaign_discount_rate` | number | no | Campaign discount rate applied to all merchants in the current advancement request. | format: "float"; minimum: 0; maximum: 1 |
| `merchants` | array of object | no |  |  |
| `merchants[].merchant_id` | integer | no | Merchant ID of the advancement request. Must be the current merchant or a branch of the current merchant. | format: "uint64"; minimum: 1; maximum: 18446744073709552000 |
| `merchants[].campaign_discount_rate` | number | no | Rate applied to a single merchant. | format: "float"; minimum: 0; maximum: 1 |
| `merchants[].merchant_transaction_ids` | array of integer | no | List of Merchant Transaction IDs |  |

Example `transactions-advancements-request` (Registration Response Success Example) — from `#/components/examples/TransactionsAdvancementsRequest`:

```json
{
  "request_date": "2025-03-10",
  "merchant_transaction_ids": [
    111,
    222,
    333
  ],
  "real_time_settlement": false,
  "campaign_advancement_fee": 5,
  "campaign_discount_rate": 0.036,
  "merchants": [
    {
      "merchant_id": 2,
      "campaign_discount_rate": 0.03,
      "merchant_transaction_ids": [
        444,
        555
      ]
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | ACCEPTED | `application/json`: object (schema `TransactionsAdvancementsResponse`) |
| 400 | BAD REQUEST | `application/json`: object (schema `DefaultErrorResponse`) |
| 404 | Marketplace or merchant does not belong to the tenant | `application/json`: object (schema `DefaultErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `simulation_id` | string | no | ID generated for the simulated advancement. This field is only returned if it is a simulation. |  |
| `advancement_request_id` | integer | no | This field is returned only if it's an actual advancement request (`EFFECTIVE`) |  |
| `type` | string | no | Operation type, returns either `SIMULATION` or `EFFECTIVE` |  |
| `request_date` | string | no | Advancement request date | format: "date" |
| `currency_code` | string (schema `CurrencyCodeResponse`) | no | ISO-4217 alphabetic (3 characters) currency code.<br> | example: "BRL" |

202 Example `transactions-advancement-response-success` (Registration response succeeded) — from `#/components/examples/TransactionsAdvancementsResponseSuccess`:

```json
{
  "simulation_id": "a882e95e-5138-4e85-a89c-26778f2e4b14",
  "advancement_request_id": 1,
  "type": "SIMULATION",
  "request_date": "2025-03-10",
  "currency_code": "BRL"
}
```

##### Response 400

400 Example `transactions-advancement-response-success` (Default Error Response) — from `#/components/examples/DefaultErrorResponse`:

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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-advancement-transaction-create-1` | https://developers.pismo.io/events/docs/merchants-advancement-transaction-create-1 |
| `merchants-merchant-transaction-created-1` | https://developers.pismo.io/events/docs/merchants-merchant-transaction-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;404`, has examples `True`, emits events `2`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchant_advance.yaml method=GET path=/v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/{advancementId} operationId=merchants-advancements-data -->
### `GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/{advancementId}` — Get advancement

- **operationId:** `merchants-advancements-data`
- **Specification:** `api-specs/Seller_management_-_Merchant_advance.yaml` (Seller management - Merchant advancements)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Return information about an existing advancement. It returns fields such as dates, values, or status. If the advancement is only simulated but not yet in effect, the endpoint does not return any information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token | example: "<your_token>"; example: "<your_token>" |
| `marketplaceId` | path | yes | integer | Marketplace ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 1 |
| `merchantId` | path | yes | integer | Merchant ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 20 |
| `advancementId` | path | yes | integer | Advancement request ID | format: "uint64"; minimum: 1; maximum: 18446744073709552000; example: 10000 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AdvancementDataResponse`) |
| 400 | BAD REQUEST | `application/json`: object (schema `DefaultErrorResponse`) |
| 404 | Marketplace or merchant does not belong to the tenant, or the advancement was not found for the given identifiers | `application/json`: object (schema `DefaultErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `begin_date` | string | no | Start date used to search merchant transactions | format: "date"; example: "2023-08-01" |
| `end_date` | anyOf: string, null | no | End date used to search merchant transactions; `null` when not provided | example: "2023-08-31" |
| `request_date` | string | no | Advancement request date | format: "date"; example: "2023-08-10" |
| `advancement_gross_amount` | anyOf: number, null | no | Gross amount of the merchant advancement, including all applicable rates; `null` when the advancement is not yet processed | example: 355 |
| `advancement_net_amount` | anyOf: number, null | no | Advancement net amount; `null` when the advancement is not yet processed | example: 300 |
| `advancement_discount_amount` | anyOf: number, null | no | Total amount of advancement discount; `null` when the advancement is not yet processed | example: 50 |
| `advancement_fee` | anyOf: number, null | no | Fixed advancement rate; `null` when a value is provided for `campaign_advancement_fee` instead | example: 5 |
| `campaign_advancement_fee` | anyOf: number, null | no | Fixed rate for requesting an advancement; `null` when the advancement uses the standard `advancement_fee` | example: null |
| `interest_method` | string | no | Type of interest. For example, compound or simple | enum: ["SIMPLE", "COMPOUND", "SIMPLIFIED"]; example: "SIMPLIFIED" |
| `status` | string | no | Advancement status | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PROCESSED" |
| `error_message` | anyOf: string, null | no | Error message; `null` when the status is either `PROCESSED` or `PENDING` | example: null |
| `metadata` | anyOf: object, null | no | Free-form metadata attached to the advancement; `null` when not provided | example: null |
| `currency_code` | anyOf: string, null (schema `OptionalCurrencyCode`) | no | ISO 4217 alphanumeric currency code. When you do not want to record a transaction's currency code, use `null`. | example: "BRL" |
| `details` | array of object | no | Per-merchant breakdown; empty array when the request is not processed or returns an error |  |
| `details[].merchant_id` | integer | no | Merchant ID used in the advancement request | example: 2 |
| `details[].merchant_name` | string | no | Merchant name | example: "Merchant Pismo 1" |
| `details[].advancement_gross_amount` | number | no | Total amount of advancement | format: "float"; example: 355 |
| `details[].advancement_net_amount` | number | no | Net amount of advancement | format: "float"; example: 300 |
| `details[].advancement_discount_amount` | number | no | Total discount amount | format: "float"; example: 50 |
| `details[].discount_rate` | anyOf: number, null | no | Merchant discount rate; `null` when the discount rate is a campaign rate (in which case `campaign_discount_rate` is populated) | example: 0.025 |
| `details[].campaign_discount_rate` | anyOf: number, null | no | Campaign discount rate; `null` when the discount rate is the standard merchant rate (in which case `discount_rate` is populated) | example: null |
| `details[].maximum_advancement_percentage` | anyOf: number, null | no | Maximum allowable percentage of the net amount for the advancement; `null` when not configured | example: 0.8 |
| `details[].transaction_ids` | array of integer | no | Transaction ID used by the merchant who makes the advancement request. This ID is generated by Pismo |  |

200 Example `advancement-data-response-success` (Registration Response Success Example) — from `#/components/examples/AdvancementDataResponseSuccess`:

```json
{
  "begin_date": "2023-08-01",
  "end_date": "2023-08-31",
  "request_date": "2023-08-10",
  "real_time_settlement": false,
  "advancement_gross_amount": 355,
  "advancement_net_amount": 300,
  "advancement_discount_amount": 50,
  "advancement_fee": 5,
  "campaign_advancement_fee": null,
  "interest_method": "SIMPLIFIED",
  "status": "PROCESSED",
  "error_message": null,
  "metadata": null,
  "currency_code": "BRL",
  "details": [
    {
      "merchant_id": 2,
      "merchant_name": "Merchant Pismo 1",
      "advancement_gross_amount": 355,
      "advancement_net_amount": 300,
      "advancement_discount_amount": 50,
      "discount_rate": 0.025,
      "campaign_discount_rate": null,
      "maximum_advancement_percentage": 0.8,
      "transaction_ids": [
        12312323,
        12312312312
      ]
    }
  ]
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

Guides that link to this operation: `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AdvancementListItem -->
### Schema `AdvancementListItem`

Pointer: `#/components/schemas/AdvancementListItem`. Type: object (schema `AdvancementListItem`).

> Single item in the paginated advancement requests history.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `advancement_request_id` | integer | yes | Advancement request identifier. | format: "int64"; example: 5531 |
| `begin_date` | string | yes | Start of the advancement period in ISO 8601 (UTC). Format = `YYYY-MM-DD`. | format: "date"; example: "2026-04-20" |
| `end_date` | anyOf: string, null | yes | End of the advancement period in ISO 8601 (UTC). Format = `YYYY-MM-DD`. When not provided, set to `null`. | example: "2026-07-20" |
| `request_date` | string | yes | Advancement request submission date in ISO 8601 (UTC). Format = `YYYY-MM-DD`. | format: "date"; example: "2026-04-15" |
| `status` | string | yes | Current advancement status. | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PROCESSED" |
| `real_time_settlement` | boolean | yes | Is the advancement settled in real time? | example: false |
| `interest_method` | string | yes | Interest calculation method applied to the advancement. | enum: ["SIMPLE", "COMPOUND", "SIMPLIFIED"]; example: "COMPOUND" |
| `advancement_gross_amount` | anyOf: number, null | yes | Gross amount of the advancement; `null` while the advancement is not yet processed. | example: 9876.5 |
| `advancement_net_amount` | anyOf: number, null | yes | Net amount of the advancement; `null` while the advancement is not yet processed. | example: 9756.05 |
| `advancement_discount_amount` | anyOf: number, null | yes | Total discount applied to the advancement; `null` while the advancement is not yet processed. | example: 120.45 |
| `error_message` | anyOf: string, null | yes | Error message; `null` when status is `PENDING` or `PROCESSED`. | example: null |
| `currency_code` | anyOf: string, null (schema `OptionalCurrencyCode`) | no | ISO 4217 alphanumeric currency code. When you do not want to record a transaction's currency code, use `null`. | example: "BRL" |

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

<!-- schema: #/components/schemas/OptionalCurrencyCode -->
### Schema `OptionalCurrencyCode`

Pointer: `#/components/schemas/OptionalCurrencyCode`. Type: anyOf: string, null (schema `OptionalCurrencyCode`).

> ISO 4217 alphanumeric currency code. When you do not want to record a transaction's currency code, use `null`.

anyOf: inline schema, inline schema

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Merchant_advance.yaml` | tag `Merchant advancement`: GET /v2/merchants/{merchantId}/advancements, POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements, POST /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/transactions, GET /v1/marketplaces/{marketplaceId}/merchants/{merchantId}/advancements/{advancementId} | https://github.com/PismoDevEx/pismo-api-specs | `73496f0c54253624…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
- `KU-EVT-merchant-advancements-data-events` — Seller management - Merchant advance
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
