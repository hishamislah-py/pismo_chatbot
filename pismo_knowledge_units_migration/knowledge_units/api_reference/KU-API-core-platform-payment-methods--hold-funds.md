---
ku_id: KU-API-core-platform-payment-methods--hold-funds
title: 'API reference: Core platform - Payment methods — Hold funds'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- post-payments-v1-hold-funds-block
- post-payments-v1-hold-funds-unblock
- post-payments-v1-hold-funds-transfer
- post-payments-v1-hold-funds-transfer-cancel
related_kus:
- KU-BANK-banking-overview
- KU-CORE-working-with-limits-objects
- KU-EVT-catalogue-other-domains
- KU-PAY-hold-funds
specification_version: 1.0.0
---

# API reference: Core platform - Payment methods — Hold funds

**KU ID:** `KU-API-core-platform-payment-methods--hold-funds` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Hold funds` in `api-specs/Core_platform_-_Payment_methods.yaml` (“Core platform - Payment methods”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> APIs to manage hold funds.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /payments/v1/payments/hold-funds/block` | `post-payments-v1-hold-funds-block` | Block amount | no |
| `POST /payments/v1/payments/hold-funds/unblock` | `post-payments-v1-hold-funds-unblock` | Unblock held amount | no |
| `POST /payments/v1/payments/hold-funds/transfer` | `post-payments-v1-hold-funds-transfer` | Transfer held amount | no |
| `POST /payments/v1/payments/hold-funds/transfer/cancel` | `post-payments-v1-hold-funds-transfer-cancel` | Cancel transfer of held amount | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments/hold-funds/block operationId=post-payments-v1-hold-funds-block -->
### `POST /payments/v1/payments/hold-funds/block` — Block amount

- **operationId:** `post-payments-v1-hold-funds-block`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Hold funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Block amount in an account. This endpoint generates [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) and [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) events. See the [Hold funds](doc:hold-funds) guide for more details.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `HoldFundsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | yes | Unique identifier of the operation. | minLength: 1; maxLength: 36; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `account_id` | integer | yes | Unique identifier of an account in the Pismo platform. | minimum: 1; example: 101 |
| `amount` | number | yes | Credit or debit amount | format: "float"; minimum: 0.01; example: 12.13 |
| `processing_code` | string | yes | Unique 6-character processing code that identifies the credit or debit operation. | pattern: "^[0-9]{6}$"; maxLength: 6; example: "004000" |
| `description` | string | no | Optional text that describes this operation. The platform supports only letters and numbers in this field and removes any special characters or emojis. | example: "Blocked value" |
| `skip_balance_validation` | boolean | no | When set to `true`, the platform skips account balance validation and forces the operation. By default, the value is `false` and the platform performs account balance validation. | example: false |
| `skip_status_account_validation` | boolean | no | When set to `true`, the platform skips account status validation and forces the operation. By default, the value is `false` and the platform performs account status validation. | example: true |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `HoldFundsAuthorizationResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID | format: "int64"; example: 15301234 |
| `event_date` | string | no | Date and time of the authorization, in the UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique identifier for the operation. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code | deprecated: true; example: "EP2P0010" |
| `code` | string | no | Error code | example: "EP2P0010" |
| `message` | string | no | Message that the request is processing and will finish asynchronously. | example: "Request is processing and will finish asynchronously" |

##### Response 400

400 Example `Invalid payload`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Invalid payload"
}
```

400 Example `Limit of two decimal places`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Exceed amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits, including two decimals, is allowed for the amount field."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;404;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-overview`, `KU-CORE-working-with-limits-objects`, `KU-PAY-hold-funds`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments/hold-funds/unblock operationId=post-payments-v1-hold-funds-unblock -->
### `POST /payments/v1/payments/hold-funds/unblock` — Unblock held amount

- **operationId:** `post-payments-v1-hold-funds-unblock`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Hold funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Unblock held amount in an account. This endpoint generates [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) and [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) events. See the [Hold funds](doc:hold-funds) guide for more details.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `HoldFundsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | yes | Unique identifier of the operation. | minLength: 1; maxLength: 36; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `account_id` | integer | yes | Unique identifier of an account in the Pismo platform. | minimum: 1; example: 101 |
| `amount` | number | yes | Credit or debit amount | format: "float"; minimum: 0.01; example: 12.13 |
| `processing_code` | string | yes | Unique 6-character processing code that identifies the credit or debit operation. | pattern: "^[0-9]{6}$"; maxLength: 6; example: "004000" |
| `description` | string | no | Optional text that describes this operation. The platform supports only letters and numbers in this field and removes any special characters or emojis. | example: "Blocked value" |
| `skip_balance_validation` | boolean | no | When set to `true`, the platform skips account balance validation and forces the operation. By default, the value is `false` and the platform performs account balance validation. | example: false |
| `skip_status_account_validation` | boolean | no | When set to `true`, the platform skips account status validation and forces the operation. By default, the value is `false` and the platform performs account status validation. | example: true |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `HoldFundsAuthorizationResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID | format: "int64"; example: 15301234 |
| `event_date` | string | no | Date and time of the authorization, in the UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique identifier for the operation. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code | deprecated: true; example: "EP2P0010" |
| `code` | string | no | Error code | example: "EP2P0010" |
| `message` | string | no | Message that the request is processing and will finish asynchronously. | example: "Request is processing and will finish asynchronously" |

##### Response 400

400 Example `Invalid payload`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Invalid payload"
}
```

400 Example `Limit of two decimal places`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Exceed amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits, including two decimals, is allowed for the amount field."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;404;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-PAY-hold-funds`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments/hold-funds/transfer operationId=post-payments-v1-hold-funds-transfer -->
### `POST /payments/v1/payments/hold-funds/transfer` — Transfer held amount

- **operationId:** `post-payments-v1-hold-funds-transfer`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Hold funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Transfer a previously held amount from an account. This endpoint generates the [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) and [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) events. See the [Hold funds](doc:hold-funds) guide for more details.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `HoldFundsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | yes | Unique identifier of the operation. | minLength: 1; maxLength: 36; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `account_id` | integer | yes | Unique identifier of an account in the Pismo platform. | minimum: 1; example: 101 |
| `amount` | number | yes | Credit or debit amount | format: "float"; minimum: 0.01; example: 12.13 |
| `processing_code` | string | yes | Unique 6-character processing code that identifies the credit or debit operation. | pattern: "^[0-9]{6}$"; maxLength: 6; example: "004000" |
| `description` | string | no | Optional text that describes this operation. The platform supports only letters and numbers in this field and removes any special characters or emojis. | example: "Blocked value" |
| `skip_balance_validation` | boolean | no | When set to `true`, the platform skips account balance validation and forces the operation. By default, the value is `false` and the platform performs account balance validation. | example: false |
| `skip_status_account_validation` | boolean | no | When set to `true`, the platform skips account status validation and forces the operation. By default, the value is `false` and the platform performs account status validation. | example: true |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `HoldFundsAuthorizationResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID | format: "int64"; example: 15301234 |
| `event_date` | string | no | Date and time of the authorization, in the UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique identifier for the operation. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code | deprecated: true; example: "EP2P0010" |
| `code` | string | no | Error code | example: "EP2P0010" |
| `message` | string | no | Message that the request is processing and will finish asynchronously. | example: "Request is processing and will finish asynchronously" |

##### Response 400

400 Example `Invalid payload`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Invalid payload"
}
```

400 Example `Limit of two decimal places`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Exceed amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits, including two decimals, is allowed for the amount field."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;404;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-PAY-hold-funds`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments/hold-funds/transfer/cancel operationId=post-payments-v1-hold-funds-transfer-cancel -->
### `POST /payments/v1/payments/hold-funds/transfer/cancel` — Cancel transfer of held amount

- **operationId:** `post-payments-v1-hold-funds-transfer-cancel`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Hold funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel transfer of a previously held amount from an account. This endpoint generates the [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) and [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1) events. See the [Hold funds](doc:hold-funds) guide for more details.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CancelTransferRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | yes | Unique identifier of the operation. | minLength: 1; maxLength: 50; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `original_tracking_id` | string | yes | Unique identifier that references the original transfer. | minLength: 1; maxLength: 50; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `account_id` | integer | yes | Unique identifier of an account in the Pismo platform. | minimum: 1; example: 101 |
| `amount` | number | yes | Credit or debit amount. | format: "float"; minimum: 0.01; example: 12.13 |
| `processing_code` | string | yes | Unique 6-character processing code that identifies the credit or debit operation. | pattern: "^[0-9]{6}$"; maxLength: 6; example: "004000" |
| `description` | string | no | Optional text that describes this operation. The platform supports only letters and numbers in this field and removes any special characters or emojis. | example: "Blocked value" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `HoldFundsAuthorizationResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID | format: "int64"; example: 15301234 |
| `event_date` | string | no | Date and time of the authorization, in the UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique identifier for the operation. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code | deprecated: true; example: "EP2P0010" |
| `code` | string | no | Error code | example: "EP2P0010" |
| `message` | string | no | Message that the request is processing and will finish asynchronously. | example: "Request is processing and will finish asynchronously" |

##### Response 400

400 Example `Invalid payload`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Invalid payload"
}
```

400 Example `Limit of two decimal places`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Exceed amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits, including two decimals, is allowed for the amount field."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;404;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-PAY-hold-funds`.

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

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_methods.yaml` | tag `Hold funds`: POST /payments/v1/payments/hold-funds/block, POST /payments/v1/payments/hold-funds/unblock, POST /payments/v1/payments/hold-funds/transfer, POST /payments/v1/payments/hold-funds/transfer/cancel | https://github.com/PismoDevEx/pismo-api-specs | `9b02c87b6e39a1c8…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-banking-overview` — Banking overview
- `KU-CORE-working-with-limits-objects` — Account limits
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-hold-funds` — Hold funds
