---
ku_id: KU-API-core-platform-payment-methods--payments
title: 'API reference: Core platform - Payment methods — Payments'
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
- post-payments-v1-payments
- post-payments-v2-cancel
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-banking-as-a-service
- KU-CORE-platform-setup-holidays
- KU-CORE-transactiontypes
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-erul
- KU-ERR-codes-wiac-to-wstm
- KU-EVT-catalogue-other-domains
- KU-EVT-client-webhooks-part-01
- KU-EVT-payments-data-events
- KU-PAY-force-operation
- KU-PAY-payment-methods
- KU-PAY-payment-requests
- KU-PAY-payments
- KU-PAY-transfers-make-and-cancel
specification_version: 1.0.0
---

# API reference: Core platform - Payment methods — Payments

**KU ID:** `KU-API-core-platform-payment-methods--payments` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Payments` in `api-specs/Core_platform_-_Payment_methods.yaml` (“Core platform - Payment methods”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage payments and transfers.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /payments/v1/payments` | `post-payments-v1-payments` | Transfer funds | no |
| `POST /payments/v2/cancel` | `post-payments-v2-cancel` | Cancel transfer funds | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments operationId=post-payments-v1-payments -->
### `POST /payments/v1/payments` — Transfer funds

- **operationId:** `post-payments-v1-payments`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> **Note:** Enhanced features and improvements are available in the [Payment methods](doc:payment-methods) API, the new application interface for non-card network authorizations. This Transfer funds endpoint is still supported, but all new feature developments will be available only in the Payment methods API. For more information, contact your Pismo representative.
>
> -----
> Transfer funds between a source (`from`) and destination (`to`). 
>
> The `to` and `from` objects contain information about one of the following payment methods:
>
> 1. **`account`** - Platform merchant or customer account
> 2. **`card`** - Credit card stored in a digital wallet, known as a **card on file**
> 3. **`custom_info`** - Custom payment information, usually about an external account
> 4. **`merchant`** - Platform merchant
>
> ### Transfers
>
> You can use this endpoint to make the following types of transfers:
>
>   * Pismo platform account to Pismo platform account (P2P)
>   * Pismo platform account to merchant account (P2M)
>   * Card to platform account (P2P with card) 
>   * Pismo platform account to merchant account with card (P2M with card)
>   * Merchant account to merchant account (M2M)
>   * Cashin
>   * Cashin with card
>   * Cashout
>   * Cashout with card
>   * Payment, which requires token (code) from [creating payment request](ref:payment-requests)
>
> See the <b>Examples</b> drop-down menu for sample payloads for each of these transfer types. See the [Make transfer](doc:make-transfer) guide for more details on these transfer type use cases.
>
> This endpoint generates an [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event. 
>
> **Note:** This endpoint requires an account-specific access token. Getting an account token requires you to call the [Get OpenID access token](ref:post-passport-v1-oauth2-token) endpoint with an account ID. Tokens can expire quickly, which can result in an <b>Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Unique Org ID. | pattern: "TN\\\\-[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}"; minLength: 39; maxLength: 39; example: "TN-c0e4c660-9059-404c-ab22-761aa431766c" |
| `x-cid` | header | no | string | The correlation identifier field is used to link related API requests and events. <br>For example, if a user makes an authorization request with 10 installments, this generates 1 authorization event and 10 transaction events all containing the same correlation ID. <br>The x-cid can help the Pismo engineering team track everything related to a call.<br> | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |
| `x-account-id` | header | no | number | Optional account ID. For P2P, this should be the `from` account ID. | example: 1 |
| `x-skip-timeline` | header | no | string | Any value here results in an event **not** being generated in the customer timeline. | example: "true" |
| `x-alt-conflict` | header | no | string | If `true`, the HTTP response status code returned is 208 (already reported) and not 409 (conflict) | example: "true" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PaymentsModel`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `from` | array of oneOf: object (schema `PaymentMethodAccount`), object (schema `PaymentMethodCard`), object (schema `PaymentMethodExternal`), object (schema `PaymentMethodMerchant`) | yes | Source method to transfer funds. You must provide one item in this array. |  |
| `to` | array of oneOf: object (schema `PaymentMethodAccount`), object (schema `PaymentMethodExternal`), object (schema `PaymentMethodMerchant`) | yes | Destination method to transfer funds. You must provide one item in this array. |  |
| `tracking_id` | string | no | Unique tracking ID of the transaction. If you don't provide one, the Pismo platform generates it randomly. | minLength: 36; maxLength: 50; example: "1ff51e99-3a05-448a-bc19-7b5c05274174" |
| `entry_mode` | string | no | Payment entry mode. | example: "QRCODE" |
| `location` | object (schema `Location`) | no | Request latitude and longitude object. |  |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `token` | string | no | Validation token used for payment-requests transfers. | example: "e933dd73-ff1d-43af-935d-91891e926ed6" |
| `payment_datetime` | string | no | Value date (effective date) of the payment in UTC-0 (RFC3339) format. <br>Payments can be backdated but future dates are not allowed.<br>example: '2020-01-02T15:14:00.218Z'<br> | format: "date-time" |
| `descriptor` | string | no | Optional text that describes the created transaction. The platform supports only letters and numbers in this field and removes any special characters or emojis. | example: "eShop purchase" |
| `timeout` | integer | no | Maximum time (in seconds) a payment can take. Optional field forwarded to acquirers. | example: 10 |
| `point_of_sales_id` | integer | no | ID of POS device initiating request. This field is DEPRECATED - the ID should now be passed in the Merchant Payment Method.  Passing it here will cause it to **not** be stored, which could lead to cancellations referencing the wrong merchant.<br> | deprecated: true; example: 10 |
| `authorization_validations` | object | no | Object containing the authorization validation data. <br> |  |
| `authorization_validations.is_device_registered` | boolean | no | Indicates whether the device used for the operation is registered according to the financial institution's security policies. | example: true |

Example `P2P`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "account": {
        "id": 2417
      }
    }
  ],
  "to": [
    {
      "processing_code": "004000",
      "account": {
        "id": 2418
      }
    }
  ]
}
```

Example `P2P with card`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "card": {
        "id": "f45dbe01-4109-11ea-ab1d-3286e4ea7ade",
        "account_id": 2417
      }
    }
  ],
  "to": [
    {
      "processing_code": "004000",
      "account": {
        "id": 2418
      }
    }
  ]
}
```

Example `P2M`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "account": {
        "id": 2417
      }
    }
  ],
  "to": [
    {
      "processing_code": "004000",
      "merchant": {
        "id": 2418,
        "point_of_sales_id": 123
      }
    }
  ]
}
```

Example `P2M with card`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "card": {
        "id": "f45dbe01-4109-11ea-ab1d-3286e4ea7ade",
        "account_id": 2417
      }
    }
  ],
  "to": [
    {
      "processing_code": "004000",
      "merchant": {
        "id": 2418,
        "point_of_sales_id": 123
      }
    }
  ]
}
```

Example `M2M`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "merchant": {
        "id": 2417
      }
    }
  ],
  "to": [
    {
      "processing_code": "004000",
      "merchant": {
        "id": 2418,
        "point_of_sales_id": 123
      }
    }
  ]
}
```

Example `Cashin`:

```json
{
  "from": [
    {
      "custom_info": {
        "type": "DEPOSIT"
      }
    }
  ],
  "to": [
    {
      "processing_code": "004000",
      "amount": 12.34,
      "account": {
        "id": 2417
      }
    }
  ]
}
```

Example `Cashin (card)`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "card": {
        "id": "f45dbe01-4109-11ea-ab1d-3286e4ea7ade",
        "account_id": 2417
      }
    }
  ],
  "to": [
    {
      "processing_code": "004000",
      "account": {
        "id": 2417
      }
    }
  ]
}
```

Example `Cashout`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "account": {
        "id": 2417
      }
    }
  ],
  "to": [
    {
      "custom_info": {
        "type": "WITHDRAWAL"
      },
      "beneficiary_id": "2c298321-bc21-4039-9c45-780cc6d4ec46"
    }
  ]
}
```

Example `Cash-out pre-authorization`:

```json
{
  "capture": false,
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "account": {
        "id": 2417
      }
    }
  ],
  "to": [
    {
      "custom_info": {
        "type": "WITHDRAWAL"
      },
      "beneficiary_id": "2c298321-bc21-4039-9c45-780cc6d4ec46"
    }
  ]
}
```

Example `Cashout (card)`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 12.34,
      "card": {
        "id": "f45dbe01-4109-11ea-ab1d-3286e4ea7ade",
        "account_id": 2417
      }
    }
  ],
  "to": [
    {
      "custom_info": {
        "type": "WITHDRAWAL"
      },
      "beneficiary_id": "2c298321-bc21-4039-9c45-780cc6d4ec46"
    }
  ]
}
```

Example `Payment`:

```json
{
  "from": [
    {
      "processing_code": "002000",
      "amount": 10,
      "account": {
        "id": 2417
      }
    }
  ],
  "token": "test-token-1"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `PaymentsResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `TrackingIdAlreadyInUseResponse`), object (schema `ErrorModel`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 502 | Bad Gateway | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID, depending on operation type. <br>DEPRECATED for the `authorization_ids` object that can contain both credit and debit authorization IDs.<br> | deprecated: true |
| `authorization_ids` | object (schema `AuthorizationIDs`) | no | Credit and debit authorization IDs. |  |
| `event_date` | string | no | Transaction datetime in UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Transfer ID. If none provided in the request, a random one is generated. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |
| `available_credit_limit` | number | no | Available credit limit after transaction. | format: "float"; example: 99.5 |

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

400 Example `Tracking ID is longer than 50 characters`:

```json
{
  "error_code": "WP2P0019",
  "code": "WP2P0019",
  "message": "Tracking ID is longer than 50 characters."
}
```

400 Example `Payment request has been paid already`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Payment request already settled"
}
```

400 Example `Not possible to determine the type of payment operation`:

```json
{
  "error_code": "EP2P9999",
  "code": "EP2P9999",
  "message": "Unable to proceed with request!"
}
```

400 Example `Invalid debit processing code`:

```json
{
  "error_code": "WP2P0005",
  "code": "WP2P0005",
  "message": "Invalid debit processing code."
}
```

400 Example `Invalid credit processing code`:

```json
{
  "error_code": "WP2P0006",
  "code": "WP2P0006",
  "message": "Invalid credit processing code."
}
```

400 Example `Processing code not found`:

```json
{
  "error_code": "WP2P0003",
  "code": "WP2P0003",
  "message": "No Orgs Operation Found"
}
```

400 Example `Account has no credit status active`:

```json
{
  "error_code": "WP2P0002",
  "code": "WP2P0002",
  "message": "Account has no credit status active."
}
```

400 Example `Account has no debit status active`:

```json
{
  "error_code": "WP2P0002",
  "code": "WP2P0002",
  "message": "Account has no debit status active."
}
```

400 Example `Account not found`:

```json
{
  "error_code": "WLDG0019",
  "code": "WLDG0019",
  "message": "No Accounts authorization found."
}
```

400 Example `Currency sent is invalid`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The currency sent is invalid."
}
```

400 Example `Flex controls evaluation results`:

```json
{
  "evaluation_result": false,
  "message": "Restriction rule [max_value_authorized_device_unique_transaction] does not pass.",
  "error_code": "RULV10400",
  "deny_code": "DEVICE_LIMIT_DAILY_TRANSACTION",
  "code": "ERUL0404",
  "response_code": 57,
  "custom_code": "AA1",
  "evaluated_controls": [
    {
      "id": "max_value_authorized_device_unique_transaction",
      "name": "max_value_authorized_device_unique_transaction",
      "evaluation_result": false,
      "message": "Restriction rule [max_value_authorized_device_unique_transaction] does not pass.",
      "deny_code": "DEVICE_LIMIT_DAILY_TRANSACTION",
      "max_limit": 0,
      "accumulated_limit": 0,
      "available_limit": 0
    },
    {
      "id": "max_value_authorized_device_daily",
      "name": "max_value_authorized_device_daily",
      "evaluation_result": true,
      "message": "",
      "deny_code": "DEVICE_LIMIT_DAILY",
      "max_limit": 100000,
      "accumulated_limit": 30000,
      "available_limit": 70000
    }
  ]
}
```

400 Example `Acquirer credential code sent is invalid`:

```json
{
  "error_code": "WP2P0020",
  "code": "WP2P0020",
  "message": "The credential code should be a valid uuid"
}
```

400 Example `Parameter OPTIN SAVING ACCOUNT is off for this account`:

```json
{
  "error_code": "WP2P0013",
  "code": "WP2P0013",
  "message": "Operation not allowed. Parameter OPTIN SAVING ACCOUNT is off."
}
```

400 Example `No limit available`:

```json
{
  "error_code": "WLDG0006",
  "code": "WLDG0006",
  "message": "No AvailableCreditLimit to complete the transaction - amount: 10, availableCreditLimit: 5.00"
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

##### Response 409

409 Example `Tracking id is already in use by an ongoing request`:

```json
{
  "error_code": "WP2P0010",
  "code": "WP2P0010",
  "message": "Tracking id is already in use."
}
```

409 Example `Tracking id has been already used`:

```json
{
  "error_code": "WP2P0010",
  "code": "WP2P0010",
  "message": "Tracking id is already in use.",
  "authorizations": [
    {
      "authorization_id": 16397984,
      "response_code": "00",
      "amount": 12.13,
      "date": "2020-01-02T15:14:00.218Z"
    }
  ]
}
```

##### Response 422

422 Example `Authorized account is different from request`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Authorized account is different from the request"
}
```

##### Response 500

500 Example `Unexpected Error`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Unexpected Error"
}
```

500 Example `Internal server error`:

```json
{
  "error_code": "ELDG500",
  "code": "ELDG500",
  "message": "Internal server error"
}
```

500 Example `Internal server error getting Payment Configuration`:

```json
{
  "error_code": "EPCG501",
  "code": "EPCG501",
  "message": "Internal server error"
}
```

500 Example `Unmarshal error`:

```json
{
  "error_code": "ELDG500",
  "code": "ELDG500",
  "message": "Unmarshal error"
}
```

500 Example `Unable to proceed with request`:

```json
{
  "error_code": "EP2P9999",
  "code": "EP2P9999",
  "message": "Unable to proceed with request!"
}
```

500 Example `Unable to connect to acquirer gateway`:

```json
{
  "error_code": "EP2P0001",
  "code": "EP2P0001",
  "message": "Unable to connect to acquirer gateway"
}
```

##### Response 502

502 Example `Acquirer gateway bad response`:

```json
{
  "error_code": "EP2P0002",
  "code": "EP2P0002",
  "message": "Acquirer gateway bad response"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |
| 400 | `WP2P0019` | Tracking ID is longer than 50 characters. |
| 400 | `EP2P9999` | Unable to proceed with request! |
| 400 | `WP2P0005` | Invalid debit processing code. |
| 400 | `WP2P0006` | Invalid credit processing code. |
| 400 | `WP2P0003` | No Orgs Operation Found |
| 400 | `WP2P0002` | Account has no credit status active. |
| 400 | `WLDG0019` | No Accounts authorization found. |
| 400 | `ERUL0404` | Restriction rule [max_value_authorized_device_unique_transaction] does not pass. |
| 400 | `RULV10400` | Restriction rule [max_value_authorized_device_unique_transaction] does not pass. |
| 400 | `WP2P0020` | The credential code should be a valid uuid |
| 400 | `WP2P0013` | Operation not allowed. Parameter OPTIN SAVING ACCOUNT is off. |
| 400 | `WLDG0006` | No AvailableCreditLimit to complete the transaction - amount: 10, availableCreditLimit: 5.00 |
| 409 | `WP2P0010` | Tracking id is already in use. |
| 422 | `WP2P0000` | Authorized account is different from the request |
| 500 | `WP2P0000` | Unexpected Error |
| 500 | `ELDG500` | Internal server error |
| 500 | `EPCG501` | Internal server error |
| 500 | `EP2P9999` | Unable to proceed with request! |
| 500 | `EP2P0001` | Unable to connect to acquirer gateway |
| 502 | `EP2P0002` | Acquirer gateway bad response |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;409;422;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-banking-as-a-service`, `KU-CORE-platform-setup-holidays`, `KU-CORE-transactiontypes`, `KU-EVT-client-webhooks-part-01`, `KU-EVT-payments-data-events`, `KU-PAY-force-operation`, `KU-PAY-payment-methods`, `KU-PAY-payment-requests`, `KU-PAY-payments`, `KU-PAY-transfers-make-and-cancel`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v2/cancel operationId=post-payments-v2-cancel -->
### `POST /payments/v2/cancel` — Cancel transfer funds

- **operationId:** `post-payments-v2-cancel`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> **Note:** Enhanced features and improvements are available in the [Payment methods](doc:payment-methods) API, the new application interface for non-card network authorizations. This Cancel transfer funds endpoint is still supported, but all new feature developments will be available only in the Payment methods API. For more information, contact your Pismo representative.
>
> -----
> Cancel a previously authorized transfer made with the [Transfer funds](ref:post-payments-v1-payments) endpoint. 
> Pass one of two parameters (but not both) returned from the Transfer funds endpoint to identify the transfer to be canceled:
> - The `tracking_id` (pass as `original_tracking_id`)
> - The credit or debit authorization ID (pass as `authorization_id`). 
>
> For an external operation, the acquirer response is returned in the `metadata` field.
> If no processing codes are specified, the original authorization's reversal processing codes are used.
>
> This endpoint generates an [Authorization cancelled](https://developers.pismo.io/events/docs/authorization-authorization-cancellation-event-1) event.
>
> For additional information, see the [Cancel transfer](doc:cancel-transfer) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Unique Org ID. | pattern: "TN\\\\-[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}"; minLength: 39; maxLength: 39; example: "TN-c0e4c660-9059-404c-ab22-761aa431766c" |
| `x-cid` | header | no | string | Related correlation ID. If none is provided, a random one is generated. | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `CancelModel`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Credit or debit authorization ID (`authorization_ids.credit` or `authorization_ids.debit`) returned in the response of the original transfer from the [Transfer funds](ref:post-payments-v1-payments) endpoint. <br><br>Either this field or the `original_tracking_id` field is **REQUIRED** to identify the original transfer that needs to be canceled with this request.<br> | format: "int64"; minimum: 1; example: 15301234 |
| `tracking_id` | string | no | Unique tracking ID of the pending cancellation. If you don't provide one, the Pismo platform generates it randomly. This field is useful for tracking and searching transaction information. <br><br>This field needs to be sent to guarantee the idempotence of the request. Requests that use the same tracking_id are considered the same. If tracking_id is not received, each request is treated as a new one.<br> | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; minLength: 36; maxLength: 65; example: "1ff51e99-3a05-448a-bc19-7b5c05274174" |
| `original_tracking_id` | string | no | Unique tracking ID of the original operation to be cancelled, which is returned from the [Transfer funds](ref:post-payments-v1-payments) endpoint as `tracking_id`.<br><br>Either this field or the `authorization_id` field is **REQUIRED** to identify the original transfer that needs to be cancelled with this request.<br> | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; example: "0d240226-d03e-47eb-ab3f-6d57c7d5feeb" |
| `amount` | number | yes | Full or partial amount to cancel, which cannot be more than the original transaction amount. Maximum of two decimal places.<br> | format: "float"; minimum: 0.01; example: 9.95 |
| `cancel_fees` | boolean | no | Indicates whether to cancel associated fees when canceling a transfer operation. When set to `true`, if a total or partial cancellation of an operation with a fee occurs, the platform automatically cancels the associated fee also.<br>When this flag is not provided:<br>- if a total cancellation of an operation with a fee occurs, the platform automatically cancels the fee also.<br>- if a partial cancellation of an operation with a fee occurs, the platform does not cancel the fee.<br> | example: false |
| `processing_code` | object | no | This optional field identifies the processing codes to be used in the cancellation operation. Depending on the type of transaction you want to cancel, this object can contain only one subfield of string type: `credit` or `debit`. <br><br>If no processing codes are specified, the platform uses the processing codes that correspond to the reversal of original authorization.<br><br>Do not use a reversal processing code in this field since the endpoint processes a reversal operation, automatically gathering the reversal processing code.<br> |  |
| `processing_code.credit` | string | no | Credit operation processing code. | pattern: "^[0-9]{6}$"; example: "002000" |
| `processing_code.debit` | string | no | Debit operation processing code. | pattern: "^[0-9]{6}$"; example: "004000" |
| `acquirer` | object (schema `AcquirerCredential`) | no |  |  |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `descriptor` | string | no | This field allows you to provide an optional cancellation description. <br><br>The Pismo platform passes this field to the acquirer in transactions involving calls to the acquirer.<br> | example: "eShop purchase cancellation" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `CancelResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 208 | Already reported | `application/json`: object (schema `ErrorModel`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not Found | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `TrackingIdHasAlreadyInUsedResponse`), object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 502 | Bad Gateway | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | yes | Provided `tracking_id` or the identifier automatically generated by the Pismo platform. | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `authorization_datetime` | string | no | Authorization timestamp in the UTC-0 (RFC3339) format. | example: "2006-01-02T15:04:05.000Z" |
| `authorization_ids` | object (schema `AuthorizationIDs`) | yes | Credit and debit authorization IDs. |  |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code | deprecated: true; example: "EP2P0010" |
| `code` | string | no | Error code | example: "EP2P0010" |
| `message` | string | no | Message that the request is processing and will finish asynchronously. | example: "Request is processing and will finish asynchronously" |

##### Response 208

**208 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code. | deprecated: true |
| `code` | string | no | Error code. |  |
| `message` | string | no | Error description. |  |

208 Example `Authorization already cancelled`:

```json
{
  "error_code": "AMON0004",
  "code": "AMON0004",
  "message": "Authorization was already refunded/reversed."
}
```

208 Example `Duplicated Correlation ID`:

```json
{
  "error_code": "WP2P0009",
  "code": "WP2P0009",
  "message": "Duplicated correlation ID."
}
```

208 Example `Payment denied`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Payment was previously denied and can't be cancelled."
}
```

##### Response 400

400 Example `Refund amount error`:

```json
{
  "error_code": "AMON0000",
  "code": "AMON0000",
  "message": "The amount passed 51 is greater than the current balance 50"
}
```

400 Example `Invalid payload`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Invalid payload"
}
```

400 Example `Amount cannot be negative`:

```json
{
  "error_code": "WP2P1005",
  "code": "WP2P1005",
  "message": "The amount cannot be negative or zero"
}
```

400 Example `The amount is greater than`:

```json
{
  "error_code": "EP2P0005",
  "code": "EP2P0005",
  "message": "The amount passed 1000 is greater than the current balance 800.00"
}
```

400 Example `Not possible to change limit`:

```json
{
  "error_code": "WP2P1111",
  "code": "WP2P1111",
  "message": "Not possible to change limit."
}
```

400 Example `Unable to cancel a Force authorization`:

```json
{
  "error_code": "EP2P0011",
  "code": "EP2P0011",
  "message": "Unable to cancel a Force authorization"
}
```

400 Example `Unable to cancel an Installment authorization`:

```json
{
  "error_code": "EP2P0013",
  "code": "EP2P0013",
  "message": "Unable to cancel an Installment authorization"
}
```

400 Example `Only one processing code`:

```json
{
  "error_code": "EP2P0005",
  "code": "EP2P0005",
  "message": "Only one processing code can be provided for external cancels"
}
```

400 Example `No Orgs Operation Found`:

```json
{
  "error_code": "WP2P0003",
  "code": "WP2P0003",
  "message": "No Orgs Operation Found"
}
```

400 Example `More than one org operation found`:

```json
{
  "error_code": "WP2P0003",
  "code": "WP2P0003",
  "message": "More than one org operation found"
}
```

400 Example `Unable to proceed with request`:

```json
{
  "error_code": "EP2P9999",
  "code": "EP2P9999",
  "message": "Unable to proceed with request!"
}
```

400 Example `Merchant or Merchant parameters not found`:

```json
{
  "error_code": "WP2P3003",
  "code": "WP2P3003",
  "message": "No Merchant or Merchant parameters found. Check for a valid merchant or configured merchant operations"
}
```

400 Example `Authorization process is still ongoing`:

```json
{
  "error_code": "WP2P0033",
  "code": "WP2P0033",
  "message": "Authorization process is still ongoing."
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

##### Response 404

404 Example `Authorization not found`:

```json
{
  "error_code": "WP2P0008",
  "code": "WP2P0008",
  "message": "Authorization not found."
}
```

404 Example `Reversal Processing Code not Found`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "No Reversal Processing Code Found"
}
```

404 Example `Account not found`:

```json
{
  "error_code": "WLDG0019",
  "code": "WLDG0019",
  "message": "No Accounts authorization found."
}
```

404 Example `No AvailableIntegrity found`:

```json
{
  "error_code": "WLDG0004",
  "code": "WLDG0004",
  "message": "No AvailableIntegrity found"
}
```

404 Example `No limit available`:

```json
{
  "error_code": "WLDG0006",
  "code": "WLDG0006",
  "message": "No AvailableCreditLimit to complete the transaction - amount: 15, availableCreditLimit: -121.07"
}
```

404 Example `Insufficient funds`:

```json
{
  "error_code": "WLDG0005",
  "code": "WLDG0005",
  "message": "No Available Entries found"
}
```

##### Response 409

409 Example `Tracking id is being used in an ongoing request`:

```json
{
  "error_code": "WP2P0010",
  "code": "WP2P0010",
  "message": "Tracking id is already in use."
}
```

409 Example `Authorization already cancelled`:

```json
{
  "error_code": "AMON0004",
  "code": "AMON0004",
  "message": "Authorization already refunded/reversed"
}
```

409 Example `Duplicated Correlation ID`:

```json
{
  "error_code": "WP2P0009",
  "code": "WP2P0009",
  "message": "Duplicated correlation ID."
}
```

409 Example `Payment denied`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Payment was previously denied and can't be cancelled."
}
```

409 Example `Authorization_ID is being used in an ongoing request`:

```json
{
  "error_code": "WP2P0009",
  "code": "WP2P0009",
  "message": "Parent ID is already in use."
}
```

409 Example `Tracking id has been already used`:

```json
{
  "tracking_id": "d24729c0-0c2b-4ee4-b599-8c2fcebf0280",
  "authorizations_ids": {
    "debit": 33636662,
    "credit": 0
  }
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

500 Example `Acquirer communication error`:

```json
{
  "error_code": "ACQ0001",
  "code": "ACQ0001",
  "message": "Internal server error"
}
```

500 Example `Error with acquirer`:

```json
{
  "error_code": "ACQ0000",
  "code": "ACQ0000",
  "message": "Unknown error"
}
```

500 Example `Error with other apis`:

```json
{
  "error_code": "EP2P9999",
  "code": "EP2P9999",
  "message": "Unable to proceed with request!"
}
```

500 Example `Unmarshal error`:

```json
{
  "error_code": "ELDG500",
  "code": "ELDG500",
  "message": "Unmarshal error"
}
```

500 Example `Unexpected Error`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Unexpected Error"
}
```

##### Response 502

502 Example `Unable to connect to acquirer gateway`:

```json
{
  "error_code": "EP2P0001",
  "code": "EP2P0001",
  "message": "Unable to connect to acquirer gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 208 | `AMON0004` | Authorization was already refunded/reversed. |
| 208 | `WP2P0009` | Duplicated correlation ID. |
| 208 | `WP2P0000` | Payment was previously denied and can't be cancelled. |
| 400 | `AMON0000` | The amount passed 51 is greater than the current balance 50 |
| 400 | `WP2P0000` | Invalid payload |
| 400 | `WP2P1005` | The amount cannot be negative or zero |
| 400 | `EP2P0005` | The amount passed 1000 is greater than the current balance 800.00 |
| 400 | `WP2P1111` | Not possible to change limit. |
| 400 | `EP2P0011` | Unable to cancel a Force authorization |
| 400 | `EP2P0013` | Unable to cancel an Installment authorization |
| 400 | `WP2P0003` | No Orgs Operation Found |
| 400 | `EP2P9999` | Unable to proceed with request! |
| 400 | `WP2P3003` | No Merchant or Merchant parameters found. Check for a valid merchant or configured merchant operations |
| 400 | `WP2P0033` | Authorization process is still ongoing. |
| 404 | `WP2P0008` | Authorization not found. |
| 404 | `WP2P0000` | No Reversal Processing Code Found |
| 404 | `WLDG0019` | No Accounts authorization found. |
| 404 | `WLDG0004` | No AvailableIntegrity found |
| 404 | `WLDG0006` | No AvailableCreditLimit to complete the transaction - amount: 15, availableCreditLimit: -121.07 |
| 404 | `WLDG0005` | No Available Entries found |
| 409 | `WP2P0010` | Tracking id is already in use. |
| 409 | `AMON0004` | Authorization already refunded/reversed |
| 409 | `WP2P0009` | Duplicated correlation ID. |
| 409 | `WP2P0000` | Payment was previously denied and can't be cancelled. |
| 500 | `WP2P0000` | Database connection error |
| 500 | `ACQ0001` | Internal server error |
| 500 | `ACQ0000` | Unknown error |
| 500 | `EP2P9999` | Unable to proceed with request! |
| 500 | `ELDG500` | Unmarshal error |
| 502 | `EP2P0001` | Unable to connect to acquirer gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-cancellation-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-cancellation-event-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;208;400;404;409;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-payments-data-events`, `KU-PAY-payment-methods`, `KU-PAY-payments`, `KU-PAY-transfers-make-and-cancel`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

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

<!-- schema: #/components/schemas/PaymentMethodCard -->
### Schema `PaymentMethodCard`

Pointer: `#/components/schemas/PaymentMethodCard`. Type: object (schema `PaymentMethodCard`).

> Cards on file payment method.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card` | object | no |  |  |
| `card.id` | string | yes | Card on file (in digital wallet) ID. | example: "b3777333-7a7e-4ae6-8d23-950c5d984e68" |
| `card.account_id` | integer | yes | Card on file's account ID. | example: 101 |
| `card.acquirer_id` | string | no | Acquirer ID for operation validation. | example: "8518835f-b24f-4473-87b7-fe41e7cd60e8" |
| `card.installments` | object | no | Installments information for acquirer. |  |
| `card.installments.number` | integer | yes | Number of installments. | minimum: 1; example: 1 |
| `card.installments.deferred_months` | integer | no | Number of months before first installment. | minimum: 0; example: 3 |
| `card.acquirer` | object | no | Information sent to specific acquirers. |  |
| `card.acquirer.business_application_identifier` | string | no | Business application type ID (for REDE acquirer ONLY). | example: "01" |
| `card.acquirer.sub_merchant` | object | no |  |  |
| `card.acquirer.sub_merchant.merchant_category_code` | string | no | 4-digit merchant category code (ISO 18245) based on goods or services the merchant sells the most (for REDE acquirer ONLY). | example: "6051" |
| `card.acquirer.wallet` | object | no |  |  |
| `card.acquirer.wallet.id` | string | no | Card's wallet ID (for REDE acquirer ONLY). | example: "1234567890" |
| `card.acquirer.wallet.sender_tax_identification` | string | no | Document number of wallet owner (for REDE acquirer ONLY). | example: "09365523959" |
| `card.acquirer.wallet.first_name` | string | no | First name of the wallet owner (for REDE acquirer ONLY). | example: "jose" |
| `card.acquirer.wallet.last_name` | string | no | Last name of the wallet owner (for REDE acquirer ONLY). | example: "souza" |
| `card.acquirer.wallet.processing_type` | integer | no | Identifies the type of the operation (for REDE acquirer ONLY). | example: 1 |
| `card.acquirer.capture` | boolean | no | Should authorization be auto-captured flag. Default is `true`. (For REDE acquirer ONLY.) | example: true |
| `card.acquirer.credential` | object | no |  |  |
| `card.acquirer.credential.code` | string | no | UUID key REDE acquirer uses to get authentication information. Only validated if passed. | example: "5f1c280e-ffde-4081-a126-5f2f10a96c2f" |
| `amount` | number | no | Credited or debited amount. | format: "float"; example: 12.13 |
| `processing_code` | string | no | Optional for use with private acceptance/acquiring merchant networks. <br>Can be used to define a different settlement condition (MDR, days to settle, etc). <br>For details, see acquiring/marketplace documentation.<br> | pattern: "^[0-9]{6}$"; example: "004000" |
| `currency` | string (schema `Currency`) | no | ISO-4217 alphabetic or numeric (3 characters) operation currency code. For example, either BRL or 986 for Brazilian real. | example: "BRL" |

<!-- schema: #/components/schemas/PaymentMethodExternal -->
### Schema `PaymentMethodExternal`

Pointer: `#/components/schemas/PaymentMethodExternal`. Type: object (schema `PaymentMethodExternal`).

> External entity payment method object. 
> Not related to a Pismo account, can take any form - an external checking account, a bankslip, and so on. 
> The information here is persisted for future reference.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `custom_info` | object | no |  |  |
| `custom_info.external_id` | string | yes | Custom information ID | example: "my-external-id-abc123" |
| `custom_info.type` | string | yes | Custom information type | example: "CASHIN" |
| `custom_info.name` | string | no | Custom information name. | example: "CASHIN-TEF" |
| `custom_info.description` | string | no | Custom information description. | example: "CASHIN from online bank transfer" |
| `custom_info.origin` | string | no | Origin used in migrations. | example: "STRIKER" |
| `custom_info.accounting_date` | string | no | Accounting date used in migrations. | example: "2021-10-25" |
| `amount` | number | no | Credit or debit amount. | format: "float"; example: 12.13 |
| `processing_code` | string | no | Optional for use with private acceptance/acquiring merchant networks. <br>Can be used to define a different settlement condition (MDR, days to settle, etc). <br>For more details, see acquiring/marketplace documentation.<br> | pattern: "^[0-9]{6}$"; example: "004000" |
| `currency` | string (schema `Currency`) | no | ISO-4217 alphabetic or numeric (3 characters) operation currency code. For example, either BRL or 986 for Brazilian real. | example: "BRL" |

<!-- schema: #/components/schemas/PaymentMethodMerchant -->
### Schema `PaymentMethodMerchant`

Pointer: `#/components/schemas/PaymentMethodMerchant`. Type: object (schema `PaymentMethodMerchant`).

> Payment transfer method for Pismo merchant accounts.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `merchant` | object | no |  |  |
| `merchant.id` | integer | yes | Pismo platform merchant account ID. | example: 103 |
| `merchant.point_of_sales_id` | integer | no | Marketplace identification for P2M and M2M transactions. A merchant can be linked to more than one marketplace. Provide this value in the `to` field to ensure that the correct fees are applied according to the contract between merchant and marketplace.<br> | example: 123 |

<!-- schema: #/components/schemas/Location -->
### Schema `Location`

Pointer: `#/components/schemas/Location`. Type: object (schema `Location`).

> Request latitude and longitude object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `lat` | number | no | Request latitude. | format: "float"; example: 12.2 |
| `lng` | number | no | Request longitude. | format: "float"; example: -12.2 |

<!-- schema: #/components/schemas/AuthorizationIDs -->
### Schema `AuthorizationIDs`

Pointer: `#/components/schemas/AuthorizationIDs`. Type: object (schema `AuthorizationIDs`).

> Credit and debit authorization IDs.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credit` | integer | no | Credit authorization ID. | format: "int64"; example: 15301234 |
| `debit` | integer | no | Debit authorization ID. | format: "int64"; example: 15301235 |

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

> API generic returned error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code. | deprecated: true |
| `code` | string | no | Error code. |  |
| `message` | string | no | Error description. |  |

<!-- schema: #/components/schemas/TrackingIdAlreadyInUseResponse -->
### Schema `TrackingIdAlreadyInUseResponse`

Pointer: `#/components/schemas/TrackingIdAlreadyInUseResponse`. Type: object (schema `TrackingIdAlreadyInUseResponse`).

> Tracking ID already in use error object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code. | deprecated: true; example: "WP2P0010" |
| `code` | string | no | Error code. | example: "WP2P0010" |
| `message` | string | no | Error description. | example: "Tracking ID already in use" |
| `authorizations` | array of object (schema `Authorization`) | no |  |  |

<!-- schema: #/components/schemas/AcquirerCredential -->
### Schema `AcquirerCredential`

Pointer: `#/components/schemas/AcquirerCredential`. Type: object (schema `AcquirerCredential`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credential` | object | no | Information used to authenticate with custom credentials at the acquirer |  |
| `credential.code` | string | no | UUID key used to obtain authentication information used at the acquirer. This field will only be validated when present on the payload, and it is currently forwarded only to REDE acquirer. | example: "5f1c280e-ffde-4081-a126-5f2f10a96c2f" |

<!-- schema: #/components/schemas/TrackingIdHasAlreadyInUsedResponse -->
### Schema `TrackingIdHasAlreadyInUsedResponse`

Pointer: `#/components/schemas/TrackingIdHasAlreadyInUsedResponse`. Type: object (schema `TrackingIdHasAlreadyInUsedResponse`).

> Tracking ID has already in use error object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_ids` | object (schema `AuthorizationIDs`) | no | Credit and debit authorization IDs. |  |
| `tracking_id` | string | no | Same transaction ID filled on request. | example: "e12df252-2133-4689-8598-3a157adcfb3a" |

<!-- schema: #/components/schemas/Authorization -->
### Schema `Authorization`

Pointer: `#/components/schemas/Authorization`. Type: object (schema `Authorization`).

> Authorization object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID. | format: "int64"; example: 16397984 |
| `response_code` | string | no | Operation status code. | example: "00" |
| `amount` | number | no | Credited or debited amount. | format: "float"; example: 12.13 |
| `date` | string | no | Authorization date/time in UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_methods.yaml` | tag `Payments`: POST /payments/v1/payments, POST /payments/v2/cancel | https://github.com/PismoDevEx/pismo-api-specs | `9b02c87b6e39a1c8…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-banking-as-a-service` — Banking as a Service
- `KU-CORE-platform-setup-holidays` — Platform setup - Holidays and administrative divisions
- `KU-CORE-transactiontypes` — Transaction types
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-erul` — Error codes: ERUL
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-payments-data-events` — Core platform - Payments
- `KU-PAY-force-operation` — Force operation
- `KU-PAY-payment-methods` — Payment methods
- `KU-PAY-payment-requests` — Payment requests
- `KU-PAY-payments` — Payments and transfers
- `KU-PAY-transfers-make-and-cancel` — Transfers: making and cancelling transfers
