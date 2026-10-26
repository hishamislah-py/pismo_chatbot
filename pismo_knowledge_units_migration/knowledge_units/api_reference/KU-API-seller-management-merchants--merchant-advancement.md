---
ku_id: KU-API-seller-management-merchants--merchant-advancement
title: 'API reference: Seller management - Merchants — Merchant advancement'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Seller_management_-_Merchants.yaml
  sha256: ebc9f3fadda7001c7ad8d607cd3fe07461f96c39c6ca15baccef307dd27f67bb
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
- createAdvancementRequestForMerchant
- listAdvancementsForMerchant
- listAdvancementRequestsForMerchant
- getAdvancementRequest
related_kus:
- KU-EVT-catalogue-merchants
specification_version: 1.0.0
---

# API reference: Seller management - Merchants — Merchant advancement

**KU ID:** `KU-API-seller-management-merchants--merchant-advancement` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Merchant advancement` in `api-specs/Seller_management_-_Merchants.yaml` (“Seller management - Merchants”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for advancement operations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/merchants/{merchantId}/advancements` | `createAdvancementRequestForMerchant` | Create advancement request (outdated) | no |
| `GET /v1/merchants/{merchantId}/advancements` | `listAdvancementsForMerchant` | List advancements for merchant (outdated) | no |
| `GET /v1/merchants/{merchantId}/advancements/requests` | `listAdvancementRequestsForMerchant` | List advancement requests | no |
| `GET /v1/merchants/{merchantId}/advancements/requests/{advancementRequestId}` | `getAdvancementRequest` | Get advancement request (outdated) | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=POST path=/v2/merchants/{merchantId}/advancements operationId=createAdvancementRequestForMerchant -->
### `POST /v2/merchants/{merchantId}/advancements` — Create advancement request (outdated)

- **operationId:** `createAdvancementRequestForMerchant`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create advancement request for merchant. An advancement is the same as an anticipation of receivables or a prepayment of receivables. An example of a
> situation in which a seller might use advancements is if it has a deal with a large customer who it knows is going to take some time to pay its bills.
> To cover its business expenses in the meantime, the seller could make a deal with a bank to pay it for the goods sold at the time of sale. The seller later
> repays the bank when it gets paid by its customer. The bank profits because the seller pays a fee for each advancement.<br>
> This endpoint produces a [Merchant advancement request created](https://developers.pismo.io/events/docs/merchants-advancement-request-1) event.
>
> (<strong>Outdated:</strong> For an updated version of the advancement endpoint refer to [Advancement Request](https://developers.pismo.io/pismo-docs/reference/merchants-advancements).)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Content-Type` | header | no | string | Content type | example: "application/json" |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `POSTAdvancementRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `begin_date` | string (schema `BeginDate`) | yes | Begin date (DD/MM/YYYY) | example: "31/07/2021" |
| `amount` | number (schema `AdvancementAmount`) | yes | Advancement amount | format: "float"; example: 988.9 |
| `request_date` | string (schema `RequestDate`) | no | Request date (DD/MM/YYYY) | example: "07/07/2021" |
| `end_date` | string (schema `EndDate`) | no | End date (DD/MM/YYYY) | example: "02/05/2023" |
| `notify` | string (schema `Notify`) | no | URL that receives notification | deprecated: true; example: "pismo.io/notify" |
| `real_time_settlement` | boolean (schema `RealTimeSettlement`) | no | Indicates whether transaction is settled in real time. | example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `AdvancementRequestResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `advancement_request_id` | integer (schema `AdvancementRequestID`) | no | Advancement request ID | format: "int64"; example: 995 |
| `date_of_request` | string (schema `AdvancementDateOfRequest`) | no | The date and time the advancement is requested. Note that the date and time are displayed in UTC format `yyyy-MM-ddThh:mm:ssZ`. | format: "datetime" |
| `amount_requested` | string (schema `AdvancementAmountRequested`) | no | Amount requested | example: "346.99" |
| `begin_date` | string (schema `BeginDate`) | no | Begin date (DD/MM/YYYY) | example: "31/07/2021" |
| `end_date` | string (schema `EndDate`) | no | End date (DD/MM/YYYY) | example: "02/05/2023" |
| `advancement_fee` | string (schema `AdvancementFeeInRequest`) | no | Advancement fee for creditor.<br> | default: "10"; example: "30.00" |
| `discount_rate` | string (schema `CreditorDiscountRate`) | no | Advancement discount rate for creditor.<br> | default: "0.025"; example: "0.03" |
| `maximum_advancement_percentage` | string (schema `MaximumAdvancementPercentage`) | no | Maximum advancement percentage for creditor.<br> | default: "1"; example: "0.80" |
| `interest_method` | string (schema `AdvancementInterestMethod`) | no | Advancement interest mode | enum: ["SIMPLE", "COMPOUND", "SIMPLIFIED"]; example: "SIMPLE" |
| `schedule_payment_date_update_mode` | string (schema `AdvancementSchedulePaymentDateUpdateMode`) | no | Mode for updating advancement schedule payment date | enum: ["KEEP_FUTURE_DATES", "UPDATE_TO_NOW"]; example: "KEEP_FUTURE_DATES" |
| `status` | string (schema `AdvancementStatus`) | no | Advancement status | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PENDING" |
| `message` | string (schema `AdvancementFeedbackMessage`) | no | Feedback message for advancement request | example: "Advancement request successfully completed in 10 seconds." |
| `notify` | string (schema `Notify`) | no | URL that receives notification | deprecated: true; example: "pismo.io/notify" |
| `advanced_gross_amount` | number (schema `AdvancementGrossAmount`) | no | Gross amount advanced | example: 637.53 |
| `advanced_discount_amount` | number (schema `AdvancementDiscountAmount`) | no | AdvancementDiscountAmount | format: "float"; example: 1.09 |
| `advanced_net_amount` | number (schema `AdvancementNetAmount`) | no | Net amount advanced | example: 596.1 |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `merchants-advancement-request-1` | https://developers.pismo.io/events/docs/merchants-advancement-request-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants/{merchantId}/advancements operationId=listAdvancementsForMerchant -->
### `GET /v1/merchants/{merchantId}/advancements` — List advancements for merchant (outdated)

- **operationId:** `listAdvancementsForMerchant`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List advancements for merchant by merchant ID. A merchant advancement is sometimes called a prepayment of receivables. You arrange to have a financial
> institution make regular deposits into your account equal to what you expect to receive in the future from credit card sales in installments or post-dated
> checks and bills. The financial institution deducts its fee before it puts the money in your account. You pay back each deposit when you receive
> payment from your customers. This is a way of covering business expenses in the short term. It's a cheaper alternative to a loan.
>
> (<strong>Outdated:</strong> For an updated version of the future merchant schedule refer to [List Transactions](https://developers.pismo.io/pismo-docs/reference/merchants-transactions).)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `date` | query | no | string | Request date. Format is `yyyy-mm-dd`. | format: "date"; example: "2021-07-31" |
| `startPaymentDate` | query | no | string | Scheduled payment start date. Find scheduled payments between this date and `endPaymentDate`. Format = yyyy-mm-dd. | format: "date"; example: "2020-01-01" |
| `endPaymentDate` | query | no | string | Scheduled payment end date. Format = yyyy-mm-dd. Find scheduled payments between `startPaymentDate` and this date. | format: "date"; example: "2020-01-02" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETAdvancementResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object | no |  |  |
| `items[].payment_date` | string (schema `ScheduledPaymentDate`) | no | Scheduled payment date. Format = yyyy-mm-dd. | format: "date"; example: "2020-04-20" |
| `items[].gross_value` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `items[].discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `items[].net_value` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |
| `items[].max_advancement_amount` | number (schema `MaximumAdvancementAmount`) | no | Maximum advancement amount | format: "float"; example: 989.99 |
| `items[].advancement_discount_amount` | number (schema `AdvancementDiscountAmount`) | no | AdvancementDiscountAmount | format: "float"; example: 1.09 |
| `items[].advancement_amount` | number (schema `AdvancementAmount`) | no | Advancement amount | format: "float"; example: 988.9 |
| `totals` | object | no |  |  |
| `totals.gross_value` | number (schema `Gross`) | no | Gross amount | format: "float"; example: 1000.5 |
| `totals.discount` | number (schema `Discount`) | no | Discount amount | format: "float"; example: 0.5 |
| `totals.net_value` | number (schema `Net`) | no | Net amount | format: "float"; example: 1000 |
| `totals.max_advancement_amount` | number (schema `MaximumAdvancementAmount`) | no | Maximum advancement amount | format: "float"; example: 989.99 |
| `totals.advancement_discount_amount` | number (schema `AdvancementDiscountAmount`) | no | AdvancementDiscountAmount | format: "float"; example: 1.09 |
| `totals.advancement_amount` | number (schema `AdvancementAmount`) | no | Advancement amount | format: "float"; example: 988.9 |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants/{merchantId}/advancements/requests operationId=listAdvancementRequestsForMerchant -->
### `GET /v1/merchants/{merchantId}/advancements/requests` — List advancement requests

- **operationId:** `listAdvancementRequestsForMerchant`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List advancements requested by merchant. An advancement is the same as a receivable or a prepayment of a receivable. An example of a situation in which a seller might use advancements is if it has a deal with a large customer who it knows is going to take some time to pay its bills. To cover its business expenses in the meantime, the seller could make a deal with a bank to pay it for the goods sold at the time of sale. The seller later repays the bank when it gets paid by its customer. The bank profits because the seller pays a fee for each advancement.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `status` | query | no | string | Advancement request status | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PENDING" |
| `page` | query | no | integer | Page number. Default is 1. | format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETAdvancementRequestsResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int64"; example: 74 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page | format: "int64"; example: 20 |
| `pages` | integer (schema `Pages`) | no | Number of pages | format: "int64"; example: 10 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page number | default: 1; format: "int64"; example: 1 |
| `items` | array of object (schema `GETAdvancementRequestResponse`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Seller_management_-_Merchants.yaml method=GET path=/v1/merchants/{merchantId}/advancements/requests/{advancementRequestId} operationId=getAdvancementRequest -->
### `GET /v1/merchants/{merchantId}/advancements/requests/{advancementRequestId}` — Get advancement request (outdated)

- **operationId:** `getAdvancementRequest`
- **Specification:** `api-specs/Seller_management_-_Merchants.yaml` (Seller management - Merchants)
- **Server base URL(s):** `https://sandbox.pismolabs.io/merchants`
- **Tags:** `Merchant advancement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get an advancement request using an advancement request ID and a merchant ID. An advancement is the same as a receivable or a prepayment of a receivable. An example of a
> situation in which a seller might use advancements is if it has a deal with a large customer who it knows is going to take some time to pay its bills.
> To cover its business expenses in the meantime, the seller could make a deal with a bank to pay it for the goods sold at the time of sale. The seller later
> repays the bank when it gets paid by its customer. The bank profits because the seller pays a fee for each advancement.
>
> (<strong>Outdated:</strong> For an updated version of the get advancement request endpoint refer to [Get Advancement](https://developers.pismo.io/pismo-docs/reference/merchants-advancements-data).)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | no | string | Authorization token. This is a regular access token, which does not need to include an account ID. | example: "Bearer 1JI12J39182H39182JDIOAWJ%=" |
| `merchantId` | path | yes | integer | Merchant ID | format: "int64"; example: 1 |
| `advancementRequestId` | path | yes | integer | Advancement request ID | format: "int64"; example: 995 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GETAdvancementRequestResponse`) |
| 400 | Bad Request |  |
| 401 | Access token is missing or invalid |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `advancement_request_id` | integer (schema `AdvancementRequestID`) | no | Advancement request ID | format: "int64"; example: 995 |
| `date_of_request` | string (schema `AdvancementDateOfRequest`) | no | The date and time the advancement is requested. Note that the date and time are displayed in UTC format `yyyy-MM-ddThh:mm:ssZ`. | format: "datetime" |
| `amount_requested` | string (schema `AdvancementAmountRequested`) | no | Amount requested | example: "346.99" |
| `begin_date` | string (schema `BeginDate`) | no | Begin date (DD/MM/YYYY) | example: "31/07/2021" |
| `end_date` | string (schema `EndDate`) | no | End date (DD/MM/YYYY) | example: "02/05/2023" |
| `advancement_fee` | string (schema `AdvancementFeeInRequest`) | no | Advancement fee for creditor.<br> | default: "10"; example: "30.00" |
| `discount_rate` | string (schema `CreditorDiscountRate`) | no | Advancement discount rate for creditor.<br> | default: "0.025"; example: "0.03" |
| `maximum_advancement_percentage` | string (schema `MaximumAdvancementPercentage`) | no | Maximum advancement percentage for creditor.<br> | default: "1"; example: "0.80" |
| `interest_method` | string (schema `AdvancementInterestMethod`) | no | Advancement interest mode | enum: ["SIMPLE", "COMPOUND", "SIMPLIFIED"]; example: "SIMPLE" |
| `schedule_payment_date_update_mode` | string (schema `AdvancementSchedulePaymentDateUpdateMode`) | no | Mode for updating advancement schedule payment date | enum: ["KEEP_FUTURE_DATES", "UPDATE_TO_NOW"]; example: "KEEP_FUTURE_DATES" |
| `status` | string (schema `AdvancementStatus`) | no | Advancement status | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PENDING" |
| `message` | string (schema `AdvancementFeedbackMessage`) | no | Feedback message for advancement request | example: "Advancement request successfully completed in 10 seconds." |
| `notify` | string (schema `Notify`) | no | URL that receives notification | deprecated: true; example: "pismo.io/notify" |
| `advanced_gross_amount` | number (schema `AdvancementGrossAmount`) | no | Gross amount advanced | example: 637.53 |
| `advanced_discount_amount` | number (schema `AdvancementDiscountAmount`) | no | AdvancementDiscountAmount | format: "float"; example: 1.09 |
| `advanced_net_amount` | number (schema `AdvancementNetAmount`) | no | Net amount advanced | example: 596.1 |
| `group_transactions` | string (schema `AdvancementGroupTransactions`) | no | Advancement group transactions | enum: ["TOTAL", "NETWORK"]; example: "TOTAL" |
| `initial_transaction_status` | string (schema `AdvancementInitialTransactionStatus`) | no | Initial transaction status for advancement | enum: ["SCHEDULED", "SETTLED"]; example: "SCHEDULED" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/GETAdvancementRequestResponse -->
### Schema `GETAdvancementRequestResponse`

Pointer: `#/components/schemas/GETAdvancementRequestResponse`. Type: object (schema `GETAdvancementRequestResponse`).

Composition: includes the fields of schema `AdvancementRequestResponse` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `advancement_request_id` | integer (schema `AdvancementRequestID`) | no | Advancement request ID | format: "int64"; example: 995 |
| `date_of_request` | string (schema `AdvancementDateOfRequest`) | no | The date and time the advancement is requested. Note that the date and time are displayed in UTC format `yyyy-MM-ddThh:mm:ssZ`. | format: "datetime" |
| `amount_requested` | string (schema `AdvancementAmountRequested`) | no | Amount requested | example: "346.99" |
| `begin_date` | string (schema `BeginDate`) | no | Begin date (DD/MM/YYYY) | example: "31/07/2021" |
| `end_date` | string (schema `EndDate`) | no | End date (DD/MM/YYYY) | example: "02/05/2023" |
| `advancement_fee` | string (schema `AdvancementFeeInRequest`) | no | Advancement fee for creditor.<br> | default: "10"; example: "30.00" |
| `discount_rate` | string (schema `CreditorDiscountRate`) | no | Advancement discount rate for creditor.<br> | default: "0.025"; example: "0.03" |
| `maximum_advancement_percentage` | string (schema `MaximumAdvancementPercentage`) | no | Maximum advancement percentage for creditor.<br> | default: "1"; example: "0.80" |
| `interest_method` | string (schema `AdvancementInterestMethod`) | no | Advancement interest mode | enum: ["SIMPLE", "COMPOUND", "SIMPLIFIED"]; example: "SIMPLE" |
| `schedule_payment_date_update_mode` | string (schema `AdvancementSchedulePaymentDateUpdateMode`) | no | Mode for updating advancement schedule payment date | enum: ["KEEP_FUTURE_DATES", "UPDATE_TO_NOW"]; example: "KEEP_FUTURE_DATES" |
| `status` | string (schema `AdvancementStatus`) | no | Advancement status | enum: ["PENDING", "PROCESSED", "ERROR"]; example: "PENDING" |
| `message` | string (schema `AdvancementFeedbackMessage`) | no | Feedback message for advancement request | example: "Advancement request successfully completed in 10 seconds." |
| `notify` | string (schema `Notify`) | no | URL that receives notification | deprecated: true; example: "pismo.io/notify" |
| `advanced_gross_amount` | number (schema `AdvancementGrossAmount`) | no | Gross amount advanced | example: 637.53 |
| `advanced_discount_amount` | number (schema `AdvancementDiscountAmount`) | no | AdvancementDiscountAmount | format: "float"; example: 1.09 |
| `advanced_net_amount` | number (schema `AdvancementNetAmount`) | no | Net amount advanced | example: 596.1 |
| `group_transactions` | string (schema `AdvancementGroupTransactions`) | no | Advancement group transactions | enum: ["TOTAL", "NETWORK"]; example: "TOTAL" |
| `initial_transaction_status` | string (schema `AdvancementInitialTransactionStatus`) | no | Initial transaction status for advancement | enum: ["SCHEDULED", "SETTLED"]; example: "SCHEDULED" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Seller_management_-_Merchants.yaml` | tag `Merchant advancement`: POST /v2/merchants/{merchantId}/advancements, GET /v1/merchants/{merchantId}/advancements, GET /v1/merchants/{merchantId}/advancements/requests, GET /v1/merchants/{merchantId}/advancements/requests/{advancementRequestId} | https://github.com/PismoDevEx/pismo-api-specs | `ebc9f3fadda7001c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-merchants` — Event catalogue: merchants
