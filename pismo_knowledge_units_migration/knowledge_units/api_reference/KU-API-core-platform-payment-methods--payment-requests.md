---
ku_id: KU-API-core-platform-payment-methods--payment-requests
title: 'API reference: Core platform - Payment methods — Payment requests'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Payment_methods.yaml
  sha256: 9b02c87b6e39a1c803b8361362aa5beb50c098580d9549c8f58475df0d91a80e
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
- get-payments-v1-payment-requests
- post-payments-v1-payment-requests
related_kus:
- KU-PAY-payment-requests
specification_version: 1.0.0
---

# API reference: Core platform - Payment methods — Payment requests

**KU ID:** `KU-API-core-platform-payment-methods--payment-requests` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Payment requests` in `api-specs/Core_platform_-_Payment_methods.yaml` (“Core platform - Payment methods”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> APIs to manage payment requests.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /payments/v1/payment-requests` | `get-payments-v1-payment-requests` | List payment requests | no |
| `POST /payments/v1/payment-requests` | `post-payments-v1-payment-requests` | Create payment request | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=GET path=/payments/v1/payment-requests operationId=get-payments-v1-payment-requests -->
### `GET /payments/v1/payment-requests` — List payment requests

- **operationId:** `get-payments-v1-payment-requests`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment requests`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List previously created payment requests. Filter with either (but not both) account ID in `from` or `to`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `from` | query | no | string | Filter results with destination account ID |  |
| `to` | query | no | string | Filter results with source account ID |  |
| `x-tenant` | header | no | string | Unique Org ID. | pattern: "TN\\\\-[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}"; minLength: 39; maxLength: 39; example: "TN-c0e4c660-9059-404c-ab22-761aa431766c" |
| `x-cid` | header | no | string | Related correlation ID. If none is provided, a random one is generated. | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |
| `status` | query | no | string | Filter results with this payment request status |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `PaymentRequestItemResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `No account specified`:

```json
{
  "error_code": "WP2P0009",
  "code": "WP2P0009",
  "message": "No account specified in request."
}
```

400 Example `Only one account can be specified`:

```json
{
  "error_code": "WP2P0009",
  "code": "WP2P0009",
  "message": "Request can specify only one account."
}
```

##### Response 500

500 Example `Unable to proceed with request`:

```json
{
  "error_code": "EP2P9999",
  "code": "EP2P9999",
  "message": "Unable to proceed with request!"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0009` | No account specified in request. |
| 500 | `EP2P9999` | Unable to proceed with request! |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-payment-requests`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payment-requests operationId=post-payments-v1-payment-requests -->
### `POST /payments/v1/payment-requests` — Create payment request

- **operationId:** `post-payments-v1-payment-requests`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment requests`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new payment request. Once created, call the [Transfer funds](ref:post-payments-v1-payments) endpoint to execute the payment.
>
> For additional information, see the [Payment requests](doc:payment-requests) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Unique Org ID. | pattern: "TN\\\\-[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}"; minLength: 39; maxLength: 39; example: "TN-c0e4c660-9059-404c-ab22-761aa431766c" |
| `x-account-id` | header | no | string | Source account ID (optional). Can be ommited if `from` specifies the source account ID. |  |
| `x-cid` | header | no | string | Related correlation identifier. If none is provided, a random one is generated. | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `PaymentRequestModel`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `to` | object (schema `PaymentMethodAccount`) | yes | Payment method for Pismo account transfers. |  |
| `from` | object (schema `PaymentMethodAccount`) | no | Payment method for Pismo account transfers. |  |
| `amount` | number | yes | Payment request amount. | format: "float"; minimum: 0.01; example: 9.95 |
| `processing_code` | string | no | Payment request processing code. | example: "004000" |
| `expiration` | string | no | Payment request expiration date in UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-05-11T10:39:00.000Z" |
| `tracking_id` | string | no | Optional unique ID correlating the payment request's associated credit and debit authorizations. | example: "1ff51e99-3a05-448a-bc19-7b5c05274174" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `location` | object (schema `Location`) | no | Request latitude and longitude object. |  |

Example `Sample Payload`:

```json
{
  "amount": 10,
  "to": {
    "currency": "BRL",
    "account": {
      "id": 1234
    }
  },
  "expiration": "2021-12-31T10:00:00.000Z",
  "location": {
    "lat": 12.2,
    "lng": -12.2
  },
  "metadata": {
    "my-custom-key": "my-custom-value01"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `PaymentRequestResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | no | Payment request format type. | example: "TOKEN" |
| `code` | string | no | Payment request ID code. Token field for Transfer funds (`v1/payments`) | example: "a78f0809-7a22-4485-8e57-abf70168c5f0" |

##### Response 400

400 Example `Mandatory source error`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Source account is required"
}
```

400 Example `Mandatory destination error`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Destination account is required"
}
```

400 Example `Payment request already settled`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Payment request already settled"
}
```

400 Example `Invalid amount`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

##### Response 500

500 Example `Database connection error`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Database connection error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Source account is required |
| 500 | `WP2P0000` | Database connection error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-payment-requests`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

> API generic returned error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code. | deprecated: true |
| `code` | string | no | Error code. |  |
| `message` | string | no | Error description. |  |

<!-- schema: #/components/schemas/PaymentMethodAccount -->
### Schema `PaymentMethodAccount`

Pointer: `#/components/schemas/PaymentMethodAccount`. Type: object (schema `PaymentMethodAccount`).

> Payment method for Pismo account transfers.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account` | object | no |  |  |
| `account.id` | integer | yes | Pismo platform account ID. | example: 101 |
| `amount` | number | no | Credit or debit amount. | format: "float"; example: 12.13 |
| `processing_code` | string | no | Optional for use with private acceptance/acquiring merchant networks. <br>Can be used to define a different settlement condition (MDR, days to settle, and so on). <br>For details, see acquiring/marketplace documentation.<br> | pattern: "^[0-9]{6}$"; example: "004000" |
| `currency` | string (schema `Currency`) | no | ISO-4217 alphabetic or numeric (3 characters) operation currency code. For example, either BRL or 986 for Brazilian real. | example: "BRL" |
| `beneficiary_id` | string | no | Unique string identifier for the beneficiary associated with the account. | example: "2c298321-bc21-4039-9c45-780cc6d4ec46" |

<!-- schema: #/components/schemas/Location -->
### Schema `Location`

Pointer: `#/components/schemas/Location`. Type: object (schema `Location`).

> Request latitude and longitude object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `lat` | number | no | Request latitude. | format: "float"; example: 12.2 |
| `lng` | number | no | Request longitude. | format: "float"; example: -12.2 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_methods.yaml` | tag `Payment requests`: GET /payments/v1/payment-requests, POST /payments/v1/payment-requests | https://github.com/PismoDevEx/pismo-api-specs | `9b02c87b6e39a1c8…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-PAY-payment-requests` — Payment requests
