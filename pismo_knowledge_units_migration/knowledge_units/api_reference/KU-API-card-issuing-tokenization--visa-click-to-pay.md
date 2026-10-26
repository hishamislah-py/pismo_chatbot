---
ku_id: KU-API-card-issuing-tokenization--visa-click-to-pay
title: 'API reference: Card issuing - Tokenization — Visa Click to Pay'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Tokenization.yaml
  sha256: dd1e776cfe20b0d67cfcc866bc3663b044f224c72ea9b70658facb672666a03e
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
- post-v1-clicktopay-enroll_customer
- post-v1-clicktopay-enroll_card
- post-v1-clicktopay-get_data
- post-v1-clicktopay-manage_customer
- put-v1-clicktopay-manage_card
- post-v1-clicktopay-delete_customer
- post-v1-clicktopay-delete_card
related_kus:
- KU-CARD-digital-wallets
- KU-EVT-catalogue-cards
specification_version: 1.0.0
---

# API reference: Card issuing - Tokenization — Visa Click to Pay

**KU ID:** `KU-API-card-issuing-tokenization--visa-click-to-pay` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Visa Click to Pay` in `api-specs/Card_issuing_-_Tokenization.yaml` (“Card issuing - Tokenization”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Visa Click to Pay service endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/clicktopay/visa/enroll/customer` | `post-v1-clicktopay-enroll_customer` | Enroll customer and card in Visa CTP | no |
| `POST /v1/clicktopay/visa/enroll/card` | `post-v1-clicktopay-enroll_card` | Enroll card in Visa CTP | no |
| `GET /v1/clicktopay/visa/data` | `post-v1-clicktopay-get_data` | Get Visa CTP customer cards status | no |
| `PUT /v1/clicktopay/visa/manage/customer` | `post-v1-clicktopay-manage_customer` | Update Visa CTP customer | no |
| `PUT /v1/clicktopay/visa/manage/card` | `put-v1-clicktopay-manage_card` | Update Visa CTP customer billing address | no |
| `POST /v1/clicktopay/visa/delete/customer` | `post-v1-clicktopay-delete_customer` | Delete Visa CTP customer | no |
| `POST /v1/clicktopay/visa/delete/card` | `post-v1-clicktopay-delete_card` | Delete Visa CTP card | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a "**401 Unauthorized**" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/clicktopay/visa/enroll/customer operationId=post-v1-clicktopay-enroll_customer -->
### `POST /v1/clicktopay/visa/enroll/customer` — Enroll customer and card in Visa CTP

- **operationId:** `post-v1-clicktopay-enroll_customer`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Visa Click to Pay`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enroll a customer and card in <a href="https://usa.visa.com/products/click-to-pay/consumers.html" target="_blank">Visa's Click to Pay</a> service. Click to Pay is a secure, streamlined online checkout solution using tokenization.
>
>  For more information, refer to [Click to Pay](doc:click-to-pay).
>
>  This endpoint generates a [Click to Pay event generated](https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1) event.
>
> **Notes**:
>
> - The following fields are **mandatory** to enroll a customer/card into Visa's Click to Pay: `first_name`, `last_name`, `emails`, `phones` and `billing_address`. If not passed and not found internally, an error is returned.
>
> - The process is asynchronous, success or failure is indicated in the generated event.
>
> - This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
> - This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |
| `x-cid` | header | no | string | Request correlation ID used for tracking on Pismo platform. |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ClickToPayEnrollData`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `owner_bid` | string (schema `OwnerBid`) | yes | Owner business ID. Identifies the issuing entity creating or managing enrollment in Click to Pay.<br> | example: "1000052" |
| `card_information` | object (schema `ClickToPayCardInfo`) | yes |  |  |
| `customer_information` | object (schema `ClickToPayCustomerInfo`) | yes |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object (schema `ClickToPayBadRequest`) |
| 429 | Too Many Requests - Visa rate limit exceeded | `application/json`: object (schema `ClickToPayRateLimitError`) |
| 500 | Internal Server Error | `application/json`: object (schema `ClickToPayInternalServerError`) |

##### Response 400

400 Example `bad_request`:

```json
{
  "code": 400,
  "message": "bad request"
}
```

400 Example `bad_request_detailed`:

```json
{
  "code": 400,
  "message": "bad request",
  "details": [
    "AccountID: cannot be blank",
    "CustomerID: cannot be blank",
    "OrgID: cannot be blank.",
    "cardId: cannot be blank."
  ]
}
```

400 Example `customer_already_on_click_to_pay`:

```json
{
  "code": 400,
  "message": "customer already on click to pay"
}
```

400 Example `click_to_pay_not_enabled_to_tenant`:

```json
{
  "code": 400,
  "message": "click to pay is not enabled to tenant"
}
```

##### Response 429

429 Example `rate_limit_exceeded`:

```json
{
  "code": 429,
  "message": "Rate limit exceeded",
  "details": [
    "rate limit exceeded"
  ]
}
```

##### Response 500

500 Example `internal_server_error`:

```json
{
  "code": 500,
  "message": "internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-tokenization-click-to-pay-1` | https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;429;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-digital-wallets`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/clicktopay/visa/enroll/card operationId=post-v1-clicktopay-enroll_card -->
### `POST /v1/clicktopay/visa/enroll/card` — Enroll card in Visa CTP

- **operationId:** `post-v1-clicktopay-enroll_card`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Visa Click to Pay`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enroll a customer card in Visa Click to Pay.
>
> This endpoint generates a [Click to Pay event generated](https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1) event.
>
>  **Notes**:
>
> - If `billing_address` is not passed,  it is looked for internally. If not found, an error is returned.
>
> - This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
> - The process is asynchronous, success or failure is indicated in the generated event.
>
> - This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |
| `x-cid` | header | no | string | Request correlation ID used for tracking on Pismo platform. |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ClickToPayEnrollCardRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `owner_bid` | string (schema `OwnerBid`) | yes | Owner business ID. Identifies the issuing entity creating or managing enrollment in Click to Pay.<br> | example: "1000052" |
| `card_id` | number (schema `CardID`) | yes | Card ID | example: 6743052 |
| `billing_address` | object (schema `ClickToPayAddress`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object (schema `ClickToPayBadRequest`) |
| 429 | Too Many Requests - Visa rate limit exceeded | `application/json`: object (schema `ClickToPayRateLimitError`) |
| 500 | Internal Server Error | `application/json`: object (schema `ClickToPayInternalServerError`) |

##### Response 400

400 Example `bad_request`:

```json
{
  "code": 400,
  "message": "bad request"
}
```

400 Example `invalid_network`:

```json
{
  "code": 400,
  "message": "invalid network"
}
```

400 Example `bad_request_detailed`:

```json
{
  "code": 400,
  "message": "bad request",
  "details": [
    "AccountID: cannot be blank",
    "CustomerID: cannot be blank",
    "OrgID: cannot be blank."
  ]
}
```

400 Example `customer_not_in_click_to_pay`:

```json
{
  "code": 400,
  "message": "customer not enabled to click to pay"
}
```

400 Example `click_to_pay_not_enabled_to_tenant`:

```json
{
  "code": 400,
  "message": "click to pay is not enabled to tenant"
}
```

##### Response 429

429 Example `rate_limit_exceeded`:

```json
{
  "code": 429,
  "message": "Rate limit exceeded",
  "details": [
    "rate limit exceeded"
  ]
}
```

##### Response 500

500 Example `internal_server_error`:

```json
{
  "code": 500,
  "message": "internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-tokenization-click-to-pay-1` | https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;429;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-digital-wallets`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=GET path=/v1/clicktopay/visa/data operationId=post-v1-clicktopay-get_data -->
### `GET /v1/clicktopay/visa/data` — Get Visa CTP customer cards status

- **operationId:** `post-v1-clicktopay-get_data`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Visa Click to Pay`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Returns customer's cards statuses (active or inactive) in the Visa Click to Pay service.
>
> **Notes**:
>
> - This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
> - This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |
| `x-owner-bid` | header | yes | string | Owner business ID. Identifies the issuing entity creating or managing enrollment in Click to Pay.<br> |  |
| `x-cid` | header | no | string | Request correlation ID used for tracking on Pismo platform. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | ok | `application/json`: object (schema `ClickToPayGetCustomerCardStatusResponse`) |
| 204 | No Content | `application/json`: object |
| 400 | Bad Request | `application/json`: object (schema `ClickToPayBadRequest`) |
| 429 | Too Many Requests - Visa rate limit exceeded | `application/json`: object (schema `ClickToPayRateLimitError`) |
| 500 | Internal Server Error | `application/json`: object (schema `ClickToPayInternalServerError`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `customer_id` | number (schema `CustomerId`) | no | Customer ID | example: 6743052 |
| `cards_status` | array of object | no |  |  |
| `cards_status[].card_id` | number (schema `CardID`) | no | Card ID | example: 6743052 |
| `cards_status[].status` | string | no | Manage Consumer Status | enum: ["ACTIVE", "DISABLED"]; example: "ACTIVE" |

##### Response 204

**204 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `Code` | number | no | HTTP response code | example: 204 |
| `message` | string | no | response message | example: "no content" |

##### Response 400

400 Example `bad_request`:

```json
{
  "code": 400,
  "message": "bad request"
}
```

400 Example `invalid_network`:

```json
{
  "code": 400,
  "message": "invalid network"
}
```

400 Example `customer_not_in_click_to_pay`:

```json
{
  "code": 400,
  "message": "customer not enabled to click to pay"
}
```

400 Example `click_to_pay_not_enabled_to_tenant`:

```json
{
  "code": 400,
  "message": "click to pay is not enabled to tenant"
}
```

##### Response 429

429 Example `rate_limit_exceeded`:

```json
{
  "code": 429,
  "message": "Rate limit exceeded",
  "details": [
    "rate limit exceeded"
  ]
}
```

##### Response 500

500 Example `internal_server_error`:

```json
{
  "code": 500,
  "message": "internal server error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;204;400;429;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=PUT path=/v1/clicktopay/visa/manage/customer operationId=post-v1-clicktopay-manage_customer -->
### `PUT /v1/clicktopay/visa/manage/customer` — Update Visa CTP customer

- **operationId:** `post-v1-clicktopay-manage_customer`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Visa Click to Pay`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update customer data in the Visa Click to Pay service.
>
> This endpoint generates a [Click to Pay event generated](https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1) event.
>
> **Notes**:
>
> - Any field not passed is not updated.
>
> - This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
> - The process is asynchronous, success or failure is indicated in the generated event.
>
> - This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |
| `x-cid` | header | no | string | Request correlation ID used for tracking on Pismo platform. |  |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `ClickToPayUpdateCustomerRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `owner_bid` | string (schema `OwnerBid`) | yes | Owner business ID. Identifies the issuing entity creating or managing enrollment in Click to Pay.<br> | example: "1000052" |
| `customer_information` | object (schema `ClickToPayCustomerInfo`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object (schema `ClickToPayBadRequest`) |
| 429 | Too Many Requests - Visa rate limit exceeded | `application/json`: object (schema `ClickToPayRateLimitError`) |
| 500 | Internal Server Error | `application/json`: object (schema `ClickToPayInternalServerError`) |

##### Response 400

400 Example `bad_request`:

```json
{
  "code": 400,
  "message": "bad request"
}
```

400 Example `invalid_network`:

```json
{
  "code": 400,
  "message": "invalid network"
}
```

400 Example `bad_request_detailed`:

```json
{
  "code": 400,
  "message": "bad request",
  "details": [
    "AccountID: cannot be blank",
    "CustomerID: cannot be blank",
    "OrgID: cannot be blank."
  ]
}
```

400 Example `customer_not_in_click_to_pay`:

```json
{
  "code": 400,
  "message": "customer not enabled to click to pay"
}
```

400 Example `click_to_pay_not_enabled_to_tenant`:

```json
{
  "code": 400,
  "message": "click to pay is not enabled to tenant"
}
```

##### Response 429

429 Example `rate_limit_exceeded`:

```json
{
  "code": 429,
  "message": "Rate limit exceeded",
  "details": [
    "rate limit exceeded"
  ]
}
```

##### Response 500

500 Example `internal_server_error`:

```json
{
  "code": 500,
  "message": "internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-tokenization-click-to-pay-1` | https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;429;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=PUT path=/v1/clicktopay/visa/manage/card operationId=put-v1-clicktopay-manage_card -->
### `PUT /v1/clicktopay/visa/manage/card` — Update Visa CTP customer billing address

- **operationId:** `put-v1-clicktopay-manage_card`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Visa Click to Pay`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the billing address for customer cards in Visa Click to Pay.
>
> This endpoint generates a [Click to Pay event generated](https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1) event.
>
>  **Notes**:
>
> - If billing address information is not passed, it is looked for internally. If not found, an error is returned.
>
> - The process is asynchronous, success or failure is indicated in the generated event.
>
> - This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
> - This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |
| `x-cid` | header | no | string | Request correlation ID used for tracking on Pismo platform. |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ClickToPayUpdateCustomerBillingRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cards` | array of object | yes |  |  |
| `cards[].owner_bid` | string (schema `OwnerBid`) | yes | Owner business ID. Identifies the issuing entity creating or managing enrollment in Click to Pay.<br> | example: "1000052" |
| `cards[].card_id` | number (schema `CardID`) | yes | Card ID | example: 6743052 |
| `cards[].billing_address` | object (schema `ClickToPayAddress`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object (schema `ClickToPayBadRequest`) |
| 429 | Too Many Requests - Visa rate limit exceeded | `application/json`: object (schema `ClickToPayRateLimitError`) |
| 500 | Internal Server Error | `application/json`: object (schema `ClickToPayInternalServerError`) |

##### Response 400

400 Example `bad_request`:

```json
{
  "code": 400,
  "message": "bad request"
}
```

400 Example `invalid_network`:

```json
{
  "code": 400,
  "message": "invalid network"
}
```

400 Example `bad_request_detailed`:

```json
{
  "code": 400,
  "message": "bad request",
  "details": [
    "AccountID: cannot be blank",
    "CustomerID: cannot be blank",
    "OrgID: cannot be blank.",
    "CardI: cannot be blank."
  ]
}
```

400 Example `customer_not_in_click_to_pay`:

```json
{
  "code": 400,
  "message": "customer not enabled to click to pay"
}
```

400 Example `click_to_pay_not_enabled_to_tenant`:

```json
{
  "code": 400,
  "message": "click to pay is not enabled to tenant"
}
```

400 Example `cards_not_found`:

```json
{
  "code": 400,
  "message": "cards not found"
}
```

##### Response 429

429 Example `rate_limit_exceeded`:

```json
{
  "code": 429,
  "message": "Rate limit exceeded",
  "details": [
    "rate limit exceeded"
  ]
}
```

##### Response 500

500 Example `internal_server_error`:

```json
{
  "code": 500,
  "message": "internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-tokenization-click-to-pay-1` | https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;429;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/clicktopay/visa/delete/customer operationId=post-v1-clicktopay-delete_customer -->
### `POST /v1/clicktopay/visa/delete/customer` — Delete Visa CTP customer

- **operationId:** `post-v1-clicktopay-delete_customer`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Visa Click to Pay`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete the customer and all their cards from the Visa Click to Pay service,
>
> This endpoint generates a [Click to Pay event generated](https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1) event.
>
> **Notes**:
>
> - This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
> - The process is asynchronous, success or failure is indicated in the generated event.
>
> - This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |
| `x-cid` | header | no | string | Request correlation ID used for tracking on Pismo platform. |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ClickToPayDeleteCustomerRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `owner_bid` | string (schema `OwnerBid`) | yes | Owner business ID. Identifies the issuing entity creating or managing enrollment in Click to Pay.<br> | example: "1000052" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object (schema `ClickToPayBadRequest`) |
| 429 | Too Many Requests - Visa rate limit exceeded | `application/json`: object (schema `ClickToPayRateLimitError`) |
| 500 | Internal Server Error | `application/json`: object (schema `ClickToPayInternalServerError`) |

##### Response 400

400 Example `bad_request`:

```json
{
  "code": 400,
  "message": "bad request"
}
```

400 Example `invalid_network`:

```json
{
  "code": 400,
  "message": "invalid network"
}
```

400 Example `bad_request_detailed`:

```json
{
  "code": 400,
  "message": "bad request",
  "details": [
    "AccountID: cannot be blank",
    "CustomerID: cannot be blank",
    "OrgID: cannot be blank."
  ]
}
```

400 Example `customer_not_in_click_to_pay`:

```json
{
  "code": 400,
  "message": "customer not enabled to click to pay"
}
```

400 Example `click_to_pay_not_enabled_to_tenant`:

```json
{
  "code": 400,
  "message": "click to pay is not enabled to tenant"
}
```

##### Response 429

429 Example `rate_limit_exceeded`:

```json
{
  "code": 429,
  "message": "Rate limit exceeded",
  "details": [
    "rate limit exceeded"
  ]
}
```

##### Response 500

500 Example `internal_server_error`:

```json
{
  "code": 500,
  "message": "internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-tokenization-click-to-pay-1` | https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;429;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Tokenization.yaml method=POST path=/v1/clicktopay/visa/delete/card operationId=post-v1-clicktopay-delete_card -->
### `POST /v1/clicktopay/visa/delete/card` — Delete Visa CTP card

- **operationId:** `post-v1-clicktopay-delete_card`
- **Specification:** `api-specs/Card_issuing_-_Tokenization.yaml` (Card issuing - Tokenization)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/cards-tokenization`, `https://pci.pismolabs.io/cards-tokenization`
- **Tags:** `Visa Click to Pay`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Remove a customer's card from Visa Click to Pay service.
>
> This endpoint generates a [Click to Pay event generated](https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1) event.
>
>  **Notes**:
>
> - This endpoint takes an account token - an access token encoded with a Pismo account ID.
>
> - The process is asynchronous, success or failure is indicated in the generated event.
>
> - This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Pismo organization/tenant ID |  |
| `x-customer-id` | header | yes | integer | Customer ID |  |
| `x-cid` | header | no | string | Request correlation ID used for tracking on Pismo platform. |  |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `ClickToPayDeleteCardRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `owner_bid` | string (schema `OwnerBid`) | yes | Owner business ID. Identifies the issuing entity creating or managing enrollment in Click to Pay.<br> | example: "1000052" |
| `card_id` | number (schema `CardID`) | yes | Card ID | example: 6743052 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad Request | `application/json`: object (schema `ClickToPayBadRequest`) |
| 429 | Too Many Requests - Visa rate limit exceeded | `application/json`: object (schema `ClickToPayRateLimitError`) |
| 500 | Internal Server Error | `application/json`: object (schema `ClickToPayInternalServerError`) |

##### Response 400

400 Example `bad_request`:

```json
{
  "code": 400,
  "message": "bad request"
}
```

400 Example `invalid_network`:

```json
{
  "code": 400,
  "message": "invalid network"
}
```

400 Example `bad_request_detailed`:

```json
{
  "code": 400,
  "message": "bad request",
  "details": [
    "AccountID: cannot be blank",
    "CustomerID: cannot be blank",
    "OrgID: cannot be blank.",
    "CardI: cannot be blank."
  ]
}
```

400 Example `customer_not_in_click_to_pay`:

```json
{
  "code": 400,
  "message": "customer not enabled to click to pay"
}
```

400 Example `click_to_pay_not_enabled_to_tenant`:

```json
{
  "code": 400,
  "message": "click to pay is not enabled to tenant"
}
```

400 Example `cards_not_found`:

```json
{
  "code": 400,
  "message": "cards not found"
}
```

##### Response 429

429 Example `rate_limit_exceeded`:

```json
{
  "code": 429,
  "message": "Rate limit exceeded",
  "details": [
    "rate limit exceeded"
  ]
}
```

##### Response 500

500 Example `internal_server_error`:

```json
{
  "code": 500,
  "message": "internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cards-tokenization-click-to-pay-1` | https://developers.pismo.io/events/docs/cards-tokenization-click-to-pay-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;429;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ClickToPayCardInfo -->
### Schema `ClickToPayCardInfo`

Pointer: `#/components/schemas/ClickToPayCardInfo`. Type: object (schema `ClickToPayCardInfo`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number (schema `CardID`) | yes | Card ID | example: 6743052 |
| `billing_address` | object (schema `ClickToPayAddress`) | no |  |  |

<!-- schema: #/components/schemas/ClickToPayCustomerInfo -->
### Schema `ClickToPayCustomerInfo`

Pointer: `#/components/schemas/ClickToPayCustomerInfo`. Type: object (schema `ClickToPayCustomerInfo`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `locale` | string (schema `Locale`) | yes | Consumer preferred locale (language and country).<br><br>**Format**: two-letter ISO-639-1 language in lowercase + underscore ("_") + two-letter ISO 3166-1 country code in uppercase.<br> | example: "en_US" |
| `first_name` | string | no | Customer first name | minLength: 1; maxLength: 35; example: "Alex" |
| `middle_name` | string | no | Customer middle name | minLength: 1; maxLength: 35; example: "Robert" |
| `last_name` | string | no | Customer last name | minLength: 1; maxLength: 35; example: "Miller" |
| `country_code` | string | no | Country code&mdash;3-character ISO 3166 (Alpha 3) format | format: "ISO 3166-1-alpha3"; minLength: 1; maxLength: 3; example: "USA" |
| `emails` | array of string | no | Customer emails | minLength: 1; maxLength: 5; items.format: "email" |
| `phones` | array of string | no | Customer phones | minLength: 1; maxLength: 5 |
| `national_identifiers` | array of object | no | Customer national identifiers | minLength: 1; maxLength: 5 |
| `national_identifiers[].type` | string | yes | Identification type | enum: ["PASSPORT", "DRIVING_LICENSE", "NATIONAL_IDENTITY"]; example: "NATIONAL_IDENTITY" |
| `national_identifiers[].value` | string | yes | Identification type value | minLength: 1; maxLength: 24; example: "A123456" |
| `consent` | object (schema `ClickToPayConsent`) | no | Consent details |  |

<!-- schema: #/components/schemas/ClickToPayBadRequest -->
### Schema `ClickToPayBadRequest`

Pointer: `#/components/schemas/ClickToPayBadRequest`. Type: object (schema `ClickToPayBadRequest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | number | no | HTTP response code | example: 400 |
| `message` | string | no | Error description |  |
| `details` | array of string | no | Error details |  |

<!-- schema: #/components/schemas/ClickToPayRateLimitError -->
### Schema `ClickToPayRateLimitError`

Pointer: `#/components/schemas/ClickToPayRateLimitError`. Type: object (schema `ClickToPayRateLimitError`).

> Click to Pay rate limit error - Visa API throttling

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | number | no | HTTP response code | example: 429 |
| `message` | string | no | Error description | example: "Rate limit exceeded" |
| `details` | array of string | no | Error details from Visa |  |

<!-- schema: #/components/schemas/ClickToPayInternalServerError -->
### Schema `ClickToPayInternalServerError`

Pointer: `#/components/schemas/ClickToPayInternalServerError`. Type: object (schema `ClickToPayInternalServerError`).

> Click to Pay internal server error

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | number | no | HTTP response code | example: 500 |
| `message` | string | no | Error description | example: "Internal server error" |

<!-- schema: #/components/schemas/ClickToPayAddress -->
### Schema `ClickToPayAddress`

Pointer: `#/components/schemas/ClickToPayAddress`. Type: object (schema `ClickToPayAddress`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `city` | string | no | City | minLength: 1; maxLength: 32; example: "San Francisco" |
| `state` | string | no | State - ISO 3166-2 code format. For example - `RJ` (Rio de Janiero, Brazil) | format: "ISO 3166-2"; minLength: 1; maxLength: 3; example: "RJ" |
| `postal_code` | string | no | Postal code | minLength: 1; maxLength: 9; example: "94105" |
| `country_code` | string | no | Country code - 3-character ISO 3166 (Alpha 3) format | format: "ISO 3166-1-alpha3,"; minLength: 1; maxLength: 3; example: "USA" |
| `address_line1` | string | no | Address line one | minLength: 1; maxLength: 64; example: "1000 Market Street" |
| `address_line2` | string | no | Address line two | minLength: 1; maxLength: 64; example: "Building 56" |
| `address_line3` | string | no | Address line three | minLength: 1; maxLength: 64; example: "Suite 101" |

<!-- schema: #/components/schemas/ClickToPayConsent -->
### Schema `ClickToPayConsent`

Pointer: `#/components/schemas/ClickToPayConsent`. Type: object (schema `ClickToPayConsent`).

> Consent details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `time_of_consent` | string | yes | Date/time when consent becomes valid, in ISO UTC format YYYY-MM-DDThh:mm:ss.000Z. Only accepts present and past dates.<br> | pattern: "\\\\d\\\\d\\\\d\\\\d-\\\\d\\\\d-\\\\d\\\\dT\\\\d\\\\d:\\\\d\\\\d:\\\\d\\\\d\\\\.000Z"; example: "2020-05-05T12:12:12.000Z" |
| `version` | string | no | Terms and conditions version that the customer accepted. | minLength: 1; maxLength: 9; example: "1.0" |
| `presenter` | string | no | Text identifying consent presenter. | minLength: 1; maxLength: 30; example: "Acme Bank" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Tokenization.yaml` | tag `Visa Click to Pay`: POST /v1/clicktopay/visa/enroll/customer, POST /v1/clicktopay/visa/enroll/card, GET /v1/clicktopay/visa/data, PUT /v1/clicktopay/visa/manage/customer, PUT /v1/clicktopay/visa/manage/card, POST /v1/clicktopay/visa/delete/customer, POST /v1/clicktopay/visa/delete/card | https://github.com/PismoDevEx/pismo-api-specs | `dd1e776cfe20b0d6…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-digital-wallets` — Digital wallets, MDES Token Connect and Click to Pay
- `KU-EVT-catalogue-cards` — Event catalogue: cards
