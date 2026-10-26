---
ku_id: KU-API-banking-transaction-banking--payments-part-03
title: 'API reference: Banking - Transaction banking — Payments (part 3 of 3)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Transaction_banking.yaml
  sha256: dec6c4900eb2db35c29c0f0380763da5ae0e1a18c4ad1e293216b2b6effdab56
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
- corporate-v2-delete-scheduled-payment
- put-back-business-toggle
- corporate-v2-post-multileg-payments
- corporate-v2-get-multileg-payment
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-dated-transactions
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-ERR-codes-wmlp
- KU-ERR-codes-wpmt
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-corporate-banking-data-events
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Payments (part 3 of 3)

**KU ID:** `KU-API-banking-transaction-banking--payments-part-03` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Payments` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Payment endpoints supporting external accounts

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId}` | `corporate-v2-delete-scheduled-payment` | Cancel scheduled payment | no |
| `PUT /corporate/v1/feature/back-business/toggle` | `put-back-business-toggle` | Past business date toggle | no |
| `POST /corporate/v2/payments/multileg` | `corporate-v2-post-multileg-payments` | Post multi-leg payment (deprecated) | **yes** |
| `GET /corporate/v2/payments/multileg/{trackingId}` | `corporate-v2-get-multileg-payment` | Get multi-leg payment status (deprecated) | **yes** |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=DELETE path=/corporate/v2/scheduled-payments/{scheduledPaymentId} operationId=corporate-v2-delete-scheduled-payment -->
### `DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId}` — Cancel scheduled payment

- **operationId:** `corporate-v2-delete-scheduled-payment`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel a scheduled payment by its ID. For more information on payments operations, refer to the [Corporate Banking Launch Reference](doc:corporate-banking-launch-reference) guide.
>
> This endpoint generates a [Current scheduled payment status displayed](https://developers.pismo.io/events/docs/corporate-schedule-payment-1) event.
> See the [Data and reporting](doc:data-reporting-overview) guide for more information on events and setting up event notifications.
>
> **NOTE**: This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `scheduledPaymentId` | path | yes | string | Scheduled payment ID | example: "1234" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost |  |
| 500 | Internal Errors | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Unrecognized account ID type`:

```json
{
  "code": "WCAC0010",
  "message": "Token contains an unrecognized account ID type"
}
```

400 Example `Scheduled payment not found`:

```json
{
  "code": "WPMT0012",
  "message": "Scheduled payment not found"
}
```

400 Example `Scheduled payment not active`:

```json
{
  "code": "WPMT0013",
  "message": "Scheduled payment not active"
}
```

##### Response 401

401 Example `Unauthorized account`:

```json
{
  "code": "WCAC0001",
  "message": "Account not authorized"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0010` | Token contains an unrecognized account ID type |
| 400 | `WPMT0012` | Scheduled payment not found |
| 400 | `WPMT0013` | Scheduled payment not active |
| 401 | `WCAC0001` | Account not authorized |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `corporate-schedule-payment-1` | https://developers.pismo.io/events/docs/corporate-schedule-payment-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PUT path=/corporate/v1/feature/back-business/toggle operationId=put-back-business-toggle -->
### `PUT /corporate/v1/feature/back-business/toggle` — Past business date toggle

- **operationId:** `put-back-business-toggle`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> This endpoint enables you to enable or disable the back business payment feature for a specific division, as well as `business_date` in the payments and multileg payments endpoint. For `business_date`, see [Post payment](ref:corporate-v2-post-payments) and [Post multileg payment](ref:corporate-v2-post-multileg-payments) for details.
>
> NOTE:
> - Only transactions for a business date are blocked. If you want to block transactions for more than one business date, you must call this endpoint to disable transactions for each business date.
> - It is not allowed to set a business date that falls within the current or a future business cycle.
> - The channel codes configured in this toggle act as an allowlist, so any payment submitted through one of those channels bypasses the back-business-dated restriction for the relevant division and business date.
> - For transfers, which involve both a debit account and a credit account, the toggle applies independently to each account’s administrative division. Both divisions must allow the back-business-dated operation; if either division rejects it, the system rejects the entire payment.
>
> This endpoint does not generate events.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `BackBusinessToggleRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `division_code` | string | yes | The division code registered in the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint for which payments are enabled or disabled. It must comply with the rule `^[a-zA-Z0-9-]+$`. | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 36; example: "my-division-code" |
| `business_date` | string | yes | The business date on which payments will be disabled or enabled.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - Users are restricted to specifying a `business_date` that is within a past business cycle.<br>  - Setting a `business_date` that falls within the current or a future business cycle returns a `400` error.<br> | format: "date"; example: "2023-03-09" |
| `enabled` | boolean | yes | Indicates whether the payments are enabled or disabled. When set to `true`, payments within a division and business date are allowed. When set to `false`, payment requests are not allowed. | example: true |
| `channels` | array of string (schema `ChannelCode`) | no | List of channels that may bypass the cutoff when `enabled=false` | example: ["GCE", "GDP"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 1; items.maxLength: 20 |

Example `Disable with channels`:

```json
{
  "enabled": false,
  "division_code": "CN6",
  "business_date": "2026-02-23",
  "channels": [
    "GCE",
    "GDP"
  ]
}
```

Example `Disable without channels`:

```json
{
  "enabled": false,
  "division_code": "CN6",
  "business_date": "2026-02-23"
}
```

Example `Enable`:

```json
{
  "enabled": true,
  "division_code": "CN6",
  "business_date": "2026-02-23"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `BackBusinessToggleRequest`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 500 | Internal Errors | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `division_code` | string | yes | The division code registered in the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint for which payments are enabled or disabled. It must comply with the rule `^[a-zA-Z0-9-]+$`. | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 36; example: "my-division-code" |
| `business_date` | string | yes | The business date on which payments will be disabled or enabled.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - Users are restricted to specifying a `business_date` that is within a past business cycle.<br>  - Setting a `business_date` that falls within the current or a future business cycle returns a `400` error.<br> | format: "date"; example: "2023-03-09" |
| `enabled` | boolean | yes | Indicates whether the payments are enabled or disabled. When set to `true`, payments within a division and business date are allowed. When set to `false`, payment requests are not allowed. | example: true |
| `channels` | array of string (schema `ChannelCode`) | no | List of channels that may bypass the cutoff when `enabled=false` | example: ["GCE", "GDP"]; items.pattern: "^[a-zA-Z0-9]+$"; items.minLength: 1; items.maxLength: 20 |

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WBBT0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Enabled required`:

```json
{
  "code": "WBBT0002",
  "message": "enabled is a required field"
}
```

400 Example `Division code required`:

```json
{
  "code": "WBBT0002",
  "message": "division_code is a required field"
}
```

400 Example `Division code exceeds size`:

```json
{
  "code": "WBBT0002",
  "message": "division_code must be a maximum of 36 characters in length"
}
```

400 Example `Business date invalid format`:

```json
{
  "code": "WBBT0002",
  "message": "business_date {business_date} should be formatted as yyyy-mm-dd and be a valid date"
}
```

400 Example `Business date required`:

```json
{
  "code": "WBBT0002",
  "message": "business_date is a required field"
}
```

400 Example `Business date fall within future cycle`:

```json
{
  "code": "WBBT0003",
  "message": "Business date must fall within a past business cycle"
}
```

400 Example `Division not found`:

```json
{
  "code": "WBBT0004",
  "message": "Division not found"
}
```

400 Example `Channel not found` (Channel not found):

```json
{
  "code": "WBBT0005",
  "message": "Channel '{channel}' not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBBT0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WBBT0002` | enabled is a required field |
| 400 | `WBBT0003` | Business date must fall within a past business cycle |
| 400 | `WBBT0004` | Division not found |
| 400 | `WBBT0005` | Channel '{channel}' not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/payments/multileg operationId=corporate-v2-post-multileg-payments -->
### `POST /corporate/v2/payments/multileg` — Post multi-leg payment (deprecated)

- **operationId:** `corporate-v2-post-multileg-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enable users to submit a payment with multiple legs to the platform. The payments are processed asynchronously and must contain at least two legs, but no more than twenty.
>
> The payload contains `debits` and `credits` lists. These lists include legs that follow the requirements of `credit` and `debit` objects in the [Post payment](https://developers.pismo.io/pismo-docs/reference/corporate-v2-post-payments) endpoint.
>
> For information about multi-leg payments, see the [Post multi-leg payment](https://developers.pismo.io/pismo-docs/docs/payment-overview#post-multi-leg-payment) section in _Payment overview_.
>
> <b>NOTES</b>:
>   - To find the correct reason IDs, refer to the [List account status reasons](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts-status-reasons) endpoint.
>   - This endpoint does not support forced transfers from an earmark balance.
>   - For error handling, see [Error handling mechanism](https://developers.pismo.io/pismo-docs/docs/payment-overview#error-handling-mechanism) in _Payment overview_.
>
> Each leg generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
> - [Account balance changed (Availables)](https://developers.pismo.io/events/docs/availables-change-available-1)
> - [Accounting entry created](https://developers.pismo.io/events/docs/accounting-entry-creation-1)
> - If flex controls are configured, a [Flex control evaluated](https://developers.pismo.io/events/docs/rules-evaluation-requested-1) event is triggered.
>
> Additionally, the following events are generated for multi-leg payments:
> - [Multi-leg payment lifecycle created](https://developers.pismo.io/events/docs/corporate-multi-leg-creation-1)
> - [Multi-leg payment lifecycle status changed](https://developers.pismo.io/events/docs/corporate-multi-leg-status-change-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `MultiLegPaymentV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingIdMultiLeg`) | yes | A unique payment tracking number. In the case of multi-leg payments, this ID is used to generate distinct child tracking IDs for each leg. If any of these child tracking IDs matches an existing tracking ID within the platform, a 400 error is returned.<br><br>A single tracking ID must be provided. This is referred to as the `original tracking ID`. For information about tracking IDs, see [Tracking ID requirement](https://developers.pismo.io/pismo-docs/docs/payment-overview#tracking-id-requirement).<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable: This field cannot be updated.<br>  - Not recyclable: `tracking_id` cannot be reused.<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `debits` | array of object (schema `DebitLegV2Request`) | no |  |  |
| `credits` | array of object (schema `CreditLegV2Request`) | no |  |  |
| `instant_clearing` | boolean (schema `MultiLegInstantClearing`) | no | Whether funds are available when payment is posted.<br> | example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `MultiLegPaymentV2Response`) |
| 400 | Bad request | `application/json`: object (schema `MultiLegPaymentV2ErrorResponse`) |
| 403 | The request has been lost |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `debits` | array of object (schema `DebitLegV2Response`) | no |  |  |
| `credits` | array of object (schema `CreditLegV2Response`) | no |  |  |

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WMLP0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Tracking ID exceed size`:

```json
{
  "code": "WMLP0002",
  "message": "tracking_id must be a maximum of 43 characters in length"
}
```

400 Example `Tracking ID required`:

```json
{
  "code": "WMLP0002",
  "message": "`tracking_id` is a required field"
}
```

400 Example `Payment with more than 20 legs`:

```json
{
  "code": "WMLP0003",
  "message": "Multi-leg payments must have up to 20 legs"
}
```

400 Example `Payment with less than 2 legs`:

```json
{
  "code": "WMLP0004",
  "message": "Multi-leg payments must have at least 2 legs"
}
```

400 Example `Multi-leg payments don't allow single transfers`:

```json
{
  "code": "WMLP0006",
  "message": "Multi-leg payments don't allow single transfers"
}
```

400 Example `Processing code exceed size`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "12345",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP0002",
          "message": "processing_code must be a maximum of 6 characters in length"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `External Account ID exceed size`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "abcdefghijklmnopqrstuvwxyz012345689abcdefghijklmno",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP0002",
          "message": "external_account_id must be a maximum of 60 characters in length"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `External Account ID required`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP0002",
          "message": "external_account_id is a required field"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Amount value exceed`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 100000000000000000,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP0002",
          "message": "amount must be 100,000,000,000,000,000 or less"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `External account ID contains characters not permitted`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "288",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP0002",
          "message": "external_account_id contains characters not permitted: [characters]"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Currency required`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP0002",
          "message": "currency is a required field"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Validation rules errors`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "force_post": true,
      "validation_rules": {
        "ACCOUNT_STATUS": {
          "override": true
        },
        "LEDGER": {
          "force": true
        }
      },
      "errors": [
        {
          "code": "WMLP1026",
          "message": "Payment request with conflicting force parameters"
        }
      ]
    },
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "force_post": false,
      "validation_rules": {
        "ACCOUNT_STATUS": {
          "force": true
        }
      },
      "errors": [
        {
          "code": "WMLP1028",
          "message": "Invalid params for validation rule ACCOUNT_STATUS"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "force_post": false,
      "validation_rules": {
        "UNKNOWN": {
          "override": true
        }
      },
      "errors": [
        {
          "code": "WMLP1027",
          "message": "Invalid validation rule UNKNOWN"
        }
      ]
    }
  ]
}
```

400 Example `Insufficient balance`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1002",
          "message": "Insufficient balance"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Invalid processing code`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1003",
          "message": "Invalid processing code"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Currency mismatch`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1004",
          "message": "Cannot perform conversion between account currency and provided currency"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Amount has invalid decimal places for currency`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.523,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP0002",
          "message": "The number of decimal places is not compatible with the specified currency"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Invalid account status`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1005",
          "message": "Invalid account status"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Account has not finished onboarding`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1039",
          "message": "Account has not finished onboarding"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Earmark not active`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1006",
          "message": "Earmark is not active"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Earmark insufficient funds`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1022",
          "message": "There is insufficient balance in the earmark to complete this operation"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Weekend error`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1007",
          "message": "Cannot post transaction on weekends"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Holiday error`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1008",
          "message": "Cannot post transaction on holidays"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Account not found`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1009",
          "message": "Account not found"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Earmark not found`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1010",
          "message": "Earmark not found"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Processing code not found`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1011",
          "message": "Processing code not found"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Tracking ID already exists`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1013",
          "message": "Tracking ID already exists"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Closed debit account`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1014",
          "message": "Debit not permitted on a closed account"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Closed credit account`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": []
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP1015",
          "message": "Credit not permitted on a closed account"
        }
      ]
    }
  ]
}
```

400 Example `Force debit restrictions`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": [
        {
          "code": "WMLP1016",
          "message": "Force debit not allowed by reason - Credit Only - No Force Debit Allowed"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Force credit restrictions`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "errors": []
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP1017",
          "message": "Force credit not allowed by reason - {Reason}"
        }
      ]
    }
  ]
}
```

400 Example `Payment date cannot be earlier than account creation date`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "payment_datetime": "2033-10-24T12:00:00Z",
      "errors": [
        {
          "code": "WMLP1019",
          "message": "The payment date cannot be earlier than the account creation date"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Payment date cannot be earlier than account migration date`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "payment_datetime": "2033-10-24T12:00:00Z",
      "errors": [
        {
          "code": "WMLP1048",
          "message": "The payment date cannot be earlier than the account migration date"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Retroactive payment datetime not allowed`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "payment_datetime": "2033-10-24T12:00:00Z",
      "errors": [
        {
          "code": "WMLP1023",
          "message": "The maximum retroactive payment datetime allowed is [n] days"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Payment business date before earmark creation`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "business_date": "2024-12-15",
      "errors": [
        {
          "code": "WMLP1036",
          "message": "Payment business date cannot be earlier than the earmark creation date"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Back business dating disabled`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "business_date": "2024-12-15",
      "errors": [
        {
          "code": "WMLP1034",
          "message": "Back business dating is disabled"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Operations blocked for account`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
      "business_date": "2024-12-15",
      "errors": [
        {
          "code": "WMLP1035",
          "message": "Operations blocked for account"
        }
      ]
    }
  ],
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": []
    }
  ]
}
```

400 Example `Invalid business date for the current business day cycle`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "business_date": "2030-06-30",
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP1024",
          "message": "Invalid business date for the current business day cycle"
        }
      ]
    }
  ]
}
```

400 Example `Invalid business date format`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "business_date": "2025-05-30",
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP0002",
          "message": "business_date 2025-05-32 should be formatted as yyyy-mm-dd and be a valid date"
        }
      ]
    }
  ]
}
```

400 Example `Debit not allowed by status reason`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "debits": [
    {
      "external_account_id": "289",
      "processing_code": "220037",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP1037",
          "message": "Debit not allowed by reason - <reason>"
        }
      ]
    }
  ]
}
```

400 Example `Credit not allowed by status reason`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP1038",
          "message": "Credit not allowed by reason - <reason>"
        }
      ]
    }
  ]
}
```

400 Example `Future payment datetime above limit`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "payment_datetime": "2030-06-30T12:23:45.000Z",
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP1030",
          "message": "Future dated payment datetime must be before date limit"
        }
      ]
    }
  ]
}
```

400 Example `Cannot post back value-dated for division`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "payment_datetime": "2030-06-30T12:23:45.000Z",
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP1041",
          "message": "Cannot post back value-dated transaction for this division"
        }
      ]
    }
  ]
}
```

400 Example `Cannot post future value-dated for division`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "credits": [
    {
      "external_account_id": "289",
      "processing_code": "220035",
      "soft_descriptor": "ACME Inc. - Invoice 2938",
      "amount": 1000.52,
      "payment_datetime": "2030-06-30T12:23:45.000Z",
      "currency": "USD",
      "errors": [
        {
          "code": "WMLP1042",
          "message": "Cannot post future value-dated transaction for this division"
        }
      ]
    }
  ]
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WMLP0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WMLP0002` | tracking_id must be a maximum of 43 characters in length |
| 400 | `WMLP0003` | Multi-leg payments must have up to 20 legs |
| 400 | `WMLP0004` | Multi-leg payments must have at least 2 legs |
| 400 | `WMLP0006` | Multi-leg payments don't allow single transfers |
| 400 | `WMLP0005` | Validation error: one or more legs did not pass validation |
| 400 | `WMLP1026` | Payment request with conflicting force parameters |
| 400 | `WMLP1028` | Invalid params for validation rule ACCOUNT_STATUS |
| 400 | `WMLP1027` | Invalid validation rule UNKNOWN |
| 400 | `WMLP1002` | Insufficient balance |
| 400 | `WMLP1003` | Invalid processing code |
| 400 | `WMLP1004` | Cannot perform conversion between account currency and provided currency |
| 400 | `WMLP1005` | Invalid account status |
| 400 | `WMLP1039` | Account has not finished onboarding |
| 400 | `WMLP1006` | Earmark is not active |
| 400 | `WMLP1022` | There is insufficient balance in the earmark to complete this operation |
| 400 | `WMLP1007` | Cannot post transaction on weekends |
| 400 | `WMLP1008` | Cannot post transaction on holidays |
| 400 | `WMLP1009` | Account not found |
| 400 | `WMLP1010` | Earmark not found |
| 400 | `WMLP1011` | Processing code not found |
| 400 | `WMLP1013` | Tracking ID already exists |
| 400 | `WMLP1014` | Debit not permitted on a closed account |
| 400 | `WMLP1015` | Credit not permitted on a closed account |
| 400 | `WMLP1016` | Force debit not allowed by reason - Credit Only - No Force Debit Allowed |
| 400 | `WMLP1017` | Force credit not allowed by reason - {Reason} |
| 400 | `WMLP1019` | The payment date cannot be earlier than the account creation date |
| 400 | `WMLP1048` | The payment date cannot be earlier than the account migration date |
| 400 | `WMLP1023` | The maximum retroactive payment datetime allowed is [n] days |
| 400 | `WMLP1036` | Payment business date cannot be earlier than the earmark creation date |
| 400 | `WMLP1034` | Back business dating is disabled |
| 400 | `WMLP1035` | Operations blocked for account |
| 400 | `WMLP1024` | Invalid business date for the current business day cycle |
| 400 | `WMLP1037` | Debit not allowed by reason - <reason> |
| 400 | `WMLP1038` | Credit not allowed by reason - <reason> |
| 400 | `WMLP1030` | Future dated payment datetime must be before date limit |
| 400 | `WMLP1041` | Cannot post back value-dated transaction for this division |
| 400 | `WMLP1042` | Cannot post future value-dated transaction for this division |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `accounting-entry-creation-1` | https://developers.pismo.io/events/docs/accounting-entry-creation-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `corporate-multi-leg-creation-1` | https://developers.pismo.io/events/docs/corporate-multi-leg-creation-1 |
| `corporate-multi-leg-status-change-1` | https://developers.pismo.io/events/docs/corporate-multi-leg-status-change-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |
| `rules-evaluation-requested-1` | https://developers.pismo.io/events/docs/rules-evaluation-requested-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;500`, has examples `True`, emits events `7`, deprecated `True`.

Guides that link to this operation: `KU-BANK-dated-transactions`, `KU-EVT-corporate-banking-data-events`, `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v2/payments/multileg/{trackingId} operationId=corporate-v2-get-multileg-payment -->
### `GET /corporate/v2/payments/multileg/{trackingId}` — Get multi-leg payment status (deprecated)

- **operationId:** `corporate-v2-get-multileg-payment`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enables users to query the processing status of a multi-leg payment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `trackingId` | path | yes | string | Original tracking ID provided when the ID is created. | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e245" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get multi-leg payment status | `application/json`: object (schema `MultiLegStatus`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `status` | string | no | Status of the multi-leg processing. | enum: ["CREATING", "EXECUTING", "DEBITS_EXECUTED", "CREDITS_FAILED", "FINISHED", "ROLLING_BACK", "ROLLED_BACK", "ROLLBACK_FAILED", "TIMED_OUT"]; example: "CREATING" |
| `debits` | array of object (schema `MultiLegItemStatus`) | no |  |  |
| `credits` | array of object (schema `MultiLegItemStatus`) | no |  |  |

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WMLP0007",
  "message": "multi leg not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WMLP0007` | multi leg not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `True`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/DebitLegV2Request -->
### Schema `DebitLegV2Request`

Pointer: `#/components/schemas/DebitLegV2Request`. Type: object (schema `DebitLegV2Request`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `TransactionAmount`) | yes | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | yes | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `external_account_id` | string (schema `ExternalAccountId2`) | yes | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `force_post` | boolean (schema `ForcePostDebit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>The force operation fails if the account has any reason-based force payment restrictions, and the operation violates any of those restrictions. The reasons that restrict force credit or debit operations are:<br>  - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>  - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credit and force credit are allowed.<br>  - `FORCE_CREDIT_ONLY`: Debits, credits and force debit are not allowed.<br>  - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `earmark_id` | string (schema `EarmarkIdWithdrawal`) | no | ID of the earmark from which the amount is withdrawn. The earmark ID is generated by the [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint. | minLength: 1; maxLength: 60; example: "dadaab22-6e28-4746-8440-0caa030f0f3f" |

<!-- schema: #/components/schemas/CreditLegV2Request -->
### Schema `CreditLegV2Request`

Pointer: `#/components/schemas/CreditLegV2Request`. Type: object (schema `CreditLegV2Request`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `TransactionAmount`) | yes | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | yes | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `external_account_id` | string (schema `ExternalAccountId2`) | yes | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `force_post` | boolean (schema `ForcePostCredit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, the force operation fails. The reasons that restrict force credit or debit operations are:<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>- `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>- `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |

<!-- schema: #/components/schemas/DebitLegV2Response -->
### Schema `DebitLegV2Response`

Pointer: `#/components/schemas/DebitLegV2Response`. Type: object (schema `DebitLegV2Response`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `force_post` | boolean (schema `ForcePostDebit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>The force operation fails if the account has any reason-based force payment restrictions, and the operation violates any of those restrictions. The reasons that restrict force credit or debit operations are:<br>  - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>  - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credit and force credit are allowed.<br>  - `FORCE_CREDIT_ONLY`: Debits, credits and force debit are not allowed.<br>  - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `earmark_id` | string (schema `EarmarkIdWithdrawal`) | no | ID of the earmark from which the amount is withdrawn. The earmark ID is generated by the [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint. | minLength: 1; maxLength: 60; example: "dadaab22-6e28-4746-8440-0caa030f0f3f" |

<!-- schema: #/components/schemas/CreditLegV2Response -->
### Schema `CreditLegV2Response`

Pointer: `#/components/schemas/CreditLegV2Response`. Type: object (schema `CreditLegV2Response`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `force_post` | boolean (schema `ForcePostCredit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, the force operation fails. The reasons that restrict force credit or debit operations are:<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>- `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>- `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |

<!-- schema: #/components/schemas/MultiLegPaymentV2ErrorResponse -->
### Schema `MultiLegPaymentV2ErrorResponse`

Pointer: `#/components/schemas/MultiLegPaymentV2ErrorResponse`. Type: object (schema `MultiLegPaymentV2ErrorResponse`).

Composition: includes the fields of schema `ErrorResponse` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |
| `debits` | array of object (schema `DebitLegV2ErrorResponse`) | no |  |  |
| `credits` | array of object (schema `CreditLegV2ErrorResponse`) | no |  |  |

<!-- schema: #/components/schemas/MultiLegItemStatus -->
### Schema `MultiLegItemStatus`

Pointer: `#/components/schemas/MultiLegItemStatus`. Type: object (schema `MultiLegItemStatus`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `status` | string (schema `LegProcessingStatus`) | no | Status of the leg processing.<br><br>* `PENDING`: The payment leg is awaiting execution.<br>* `EXECUTED`: The payment leg was executed successfully.<br>* `FAILED`: The payment leg execution failed.<br>* `ROLLED_BACK`: The payment leg was executed successfully but was rolled back due to a failure in another leg.<br>* `ROLLBACK_FAILED`: The payment leg was executed successfully; another leg failed, triggering a rollback, but the rollback for this leg was unsuccessful.<br> | enum: ["PENDING", "EXECUTED", "FAILED", "ROLLED_BACK", "ROLLBACK_FAILED"]; example: "PENDING" |

<!-- schema: #/components/schemas/ValidationRules -->
### Schema `ValidationRules`

Pointer: `#/components/schemas/ValidationRules`. Type: object (map of object (schema `ValidationRule`)) (schema `ValidationRules`).

> Rules that determine which validations are executed during the payment process.<br>
> Available validation rules:
>   - `LEDGER`
>   - `ACCOUNT_STATUS`
>   - `FLEX_CONTROLS`
>   - `RATES`<br>
>
> `force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.

<!-- schema: #/components/schemas/DebitLegV2ErrorResponse -->
### Schema `DebitLegV2ErrorResponse`

Pointer: `#/components/schemas/DebitLegV2ErrorResponse`. Type: object (schema `DebitLegV2ErrorResponse`).

Composition: includes the fields of schema `DebitLegV2Response` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `force_post` | boolean (schema `ForcePostDebit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>The force operation fails if the account has any reason-based force payment restrictions, and the operation violates any of those restrictions. The reasons that restrict force credit or debit operations are:<br>  - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>  - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credit and force credit are allowed.<br>  - `FORCE_CREDIT_ONLY`: Debits, credits and force debit are not allowed.<br>  - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `earmark_id` | string (schema `EarmarkIdWithdrawal`) | no | ID of the earmark from which the amount is withdrawn. The earmark ID is generated by the [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint. | minLength: 1; maxLength: 60; example: "dadaab22-6e28-4746-8440-0caa030f0f3f" |
| `errors` | array of object (schema `ErrorResponse`) | no |  | example: [] |

<!-- schema: #/components/schemas/CreditLegV2ErrorResponse -->
### Schema `CreditLegV2ErrorResponse`

Pointer: `#/components/schemas/CreditLegV2ErrorResponse`. Type: object (schema `CreditLegV2ErrorResponse`).

Composition: includes the fields of schema `CreditLegV2Response` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `force_post` | boolean (schema `ForcePostCredit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, the force operation fails. The reasons that restrict force credit or debit operations are:<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>- `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>- `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `errors` | array of object (schema `ErrorResponse`) | no |  | example: [] |

## Lifecycle status

- `POST /corporate/v2/payments/multileg` (`corporate-v2-post-multileg-payments`) is marked `deprecated: true` in the specification.
- `GET /corporate/v2/payments/multileg/{trackingId}` (`corporate-v2-get-multileg-payment`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Payments`: DELETE /corporate/v2/scheduled-payments/{scheduledPaymentId}, PUT /corporate/v1/feature/back-business/toggle, POST /corporate/v2/payments/multileg, GET /corporate/v2/payments/multileg/{trackingId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-dated-transactions` — Business-dated and value-dated transactions
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-ERR-codes-wmlp` — Error codes: WMLP
- `KU-ERR-codes-wpmt` — Error codes: WPMT
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
