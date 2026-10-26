---
ku_id: KU-API-core-platform-payment-methods--installments-payments
title: 'API reference: Core platform - Payment methods — Installments payments'
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
- post-payments-v1-installments
- post-payments-v1-installments-cancel
related_kus:
- KU-ERR-codes-erul
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wiac-to-wstm
- KU-EVT-catalogue-other-domains
- KU-EVT-client-webhooks-part-01
- KU-PAY-installments-payment
specification_version: 1.0.0
---

# API reference: Core platform - Payment methods — Installments payments

**KU ID:** `KU-API-core-platform-payment-methods--installments-payments` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Installments payments` in `api-specs/Core_platform_-_Payment_methods.yaml` (“Core platform - Payment methods”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> APIs to manage installments payments.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /payments/v1/payments/installments` | `post-payments-v1-installments` | Create installments payment | no |
| `POST /payments/v1/payments/installments/cancel` | `post-payments-v1-installments-cancel` | Cancel installments payment | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments/installments operationId=post-payments-v1-installments -->
### `POST /payments/v1/payments/installments` — Create installments payment

- **operationId:** `post-payments-v1-installments`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Installments payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new installments payment. 
>
> This endpoint generates the [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Unique Org ID. | pattern: "TN\\\\-[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}"; minLength: 39; maxLength: 39; example: "TN-c0e4c660-9059-404c-ab22-761aa431766c" |
| `x-account-id` | header | no | string | Optional account identifier. |  |
| `x-skip-timeline` | header | no | string | If set to `true`, this will prevent the generation of timeline events in the customer timeline. | example: "true" |
| `x-cid` | header | no | string | Related correlation identifier. If none is provided, a random one is generated. | example: "c737895c-8159-4c0c-a92a-a4f8600bff37" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `InstallmentsPaymentRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | no | Unique tracking ID of the installments operation. If you don't provide one, the Pismo platform generates it randomly. | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; minLength: 36; maxLength: 50; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `account_id` | integer | yes | Unique identifier of an account in the Pismo platform. | example: 101 |
| `charging_amount` | number | yes | Total amount to be charged. | format: "float"; example: 12.13 |
| `processing_code` | string | yes | Unique 6-character processing code that identifies the debit operation. | pattern: "^[0-9]{6}$"; example: "004000" |
| `descriptor` | string | no | Optional text that describes the created operation. The platform supports only letters and numbers in this field and removes any special characters or emojis. | example: "Installments payment" |
| `skip_balance_validation` | boolean | no | When set to `true`, the platform skips account balance validation and forces the operation. By default, the value is `false` and the platform performs account balance validation. | example: true |
| `skip_account_status_validation` | boolean | no | When set to `true`, the platform skips account status validation and forces the operation. By default, the value is `false` and the platform performs account status validation. | example: true |
| `financed_charge` | object | no | Informative optional object that allows financed charges in the `principal_amount` to be described and posted only in accounting. All fields within the financed charge object must have the suffix `_amount`. For example, `iof_amount`, `iva_amount`, `other_tax_amount`.  In the `name_amount` field example, `name` indicates a dynamic value. To define a new financed charge type field, you must contact a Pismo representative.<br>When the `financed_charge` object is used, the `tax_amout` field cannot be used simultaneously, since this object is used only for cases of charges financed in the `principal_amount`.<br> |  |
| `financed_charge.name_amount` | number | no | Amount of the financed charge type to send to accounting. | format: "float"; example: 12.13 |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `first_installment_date` | string | no | Date that the first installment should be posted on the invoice. Format = YYYY-MM-DD. | format: "date"; pattern: "([0-9]{4})-(?:[0-9]{2})-([0-9]{2})"; example: "2023-12-31" |
| `installments` | array of object (schema `InstallmentDetails`) | yes | Non-empty collection of installments to be used to implement the agreement. |  |
| `original_authorization` | object | no | This optional field identifies the original authorization. <br>When this field is provided, all your fields needs be filled.<br> |  |
| `original_authorization.id` | number | yes | Unique identifier of original authorization in the Pismo plataform. | example: 101 |
| `original_authorization.type` | string | yes | Type of original authorization. | enum: ["NETWORK", "PLATFORM"]; example: "NETWORK" |

Example `post-v1-payments-installments-example`:

```text
{
	"charging_amount": 22.30,
	"processing_code": "005000",
	"descriptor": "Installments payment",
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37",
  "metadata": {
      "my-custom-key": "my-custom-info"
  },
  "original_authorization": {
    "id": 1234,
    "type": "NETWORK"
  },
	"installments": [
		{
			"installment_number": 1,
			"total_amount": 11.15,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10,
			"tax_amount": 0.15
		},
		{
			"installment_number": 2,
			"total_amount": 11.15,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10,
			"tax_amount": 0.15
		}
	]
}
```

Example `post-v1-payments-installments-with-financed-charge-example`:

```text
{
	"charging_amount": 22.00,
	"processing_code": "005000",
	"descriptor": "Installments payment",
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37",
  "financed_charge": {
    "iof_amount": 1
  },
	"installments": [
		{
			"installment_number": 1,
			"total_amount": 11.00,
			"principal_amount": 10.00,
			"interest_amount": 1.00
		},
		{
			"installment_number": 2,
			"total_amount": 11.00,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10
		}
	]
}
```

Example `post-v1-payments-installments-with-skip-balance-validation`:

```text
{
	"charging_amount": 22.30,
	"processing_code": "005000",
	"descriptor": "Installments payment",
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37", 
  "skip_balance_validation": true,
	"installments": [
		{
			"installment_number": 1,
			"total_amount": 11.15,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10,
			"tax_amount": 0.15
		},
		{
			"installment_number": 2,
			"total_amount": 11.15,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10,
			"tax_amount": 0.15
		}
	]
}
```

Example `post-v1-payments-installments-with-skip-account-status-validation`:

```text
{
	"charging_amount": 22.30,
	"processing_code": "005000",
	"descriptor": "Installments payment",
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37", 
  "skip_account_status_validation": true,
	"installments": [
		{
			"installment_number": 1,
			"total_amount": 11.15,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10,
			"tax_amount": 0.15
		},
		{
			"installment_number": 2,
			"total_amount": 11.15,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10,
			"tax_amount": 0.15
		}
	]
}
```

Example `post-v1-payments-installments-with-first-installment-date`:

```text
{
	"charging_amount": 22.30,
	"processing_code": "005000",
	"descriptor": "Installments payment",
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37", 
  "first_installment_date": "2023-12-31",
	"installments": [
		{
			"installment_number": 1,
			"total_amount": 11.15,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10,
			"tax_amount": 0.15
		},
		{
			"installment_number": 2,
			"total_amount": 11.15,
			"principal_amount": 10.00,
			"interest_amount": 1.00,
			"interest_rate": 0.10,
			"tax_amount": 0.15
		}
	]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `InstallmentsPaymentResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `TrackingIdAlreadyInUseResponse`), object (schema `InstallmentsPaymentResponseTrackingIdAlreadyInUseResponse`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID. | format: "int64"; example: 15301234 |
| `event_date` | string | no | Date and time of the authorization, in UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique 36-character identifier for the installments payment. If you didn't provide an identifier, then the Pismo platform automatically generates and includes one in the response. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

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

400 Example `Invalid amount`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Invalid installment number`:

```json
{
  "error_code": "WP2P0024",
  "code": "WP2P0024",
  "message": "Invalid installment number. Installment number should be sequential, starting with 1."
}
```

400 Example `Invalid account program type`:

```json
{
  "error_code": "WP2P0025",
  "code": "WP2P0025",
  "message": "Debit program accounts are invalid for installments payments."
}
```

400 Example `Invalid total amount`:

```json
{
  "error_code": "WP2P0026",
  "code": "WP2P0026",
  "message": "Total amount is not equal to the others amounts added"
}
```

400 Example `Invalid charging amount`:

```json
{
  "error_code": "WP2P0027",
  "code": "WP2P0027",
  "message": "Charging amount is not equal to the sum of all installments total_amount"
}
```

400 Example `Installments tax amount not allowed`:

```json
{
  "error_code": "WP2P0028",
  "code": "WP2P0028",
  "message": "Installments tax_amount not allowed for financed charge operations"
}
```

400 Example `Invalid financed charge amount`:

```json
{
  "error_code": "WP2P0029",
  "code": "WP2P0029",
  "message": "All fields within the financed charge amount must be greater than zero"
}
```

400 Example `Invalid financed charge amount suffix`:

```json
{
  "error_code": "WP2P0030",
  "code": "WP2P0030",
  "message": "All fields within the financed charge must have the suffix _amount"
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

400 Example `Processing code not found`:

```json
{
  "error_code": "WP2P0003",
  "code": "WP2P0003",
  "message": "No Orgs Operation Found"
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

400 Example `Account authorization not found`:

```json
{
  "error_code": "WLDG0019",
  "code": "WLDG0019",
  "message": "No Accounts authorization found."
}
```

400 Example `Invalid rules when evaluating`:

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

400 Example `No limit available`:

```json
{
  "error_code": "WLDG0006",
  "code": "WLDG0006",
  "message": "No AvailableCreditLimit to complete the transaction - amount: 10, availableCreditLimit: 5.00"
}
```

400 Example `Original authorization id was not provided`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Original authorization id was not provided."
}
```

400 Example `Original authorization type was not provided`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "Original authorization type was not provided."
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

400 Example `Exceed charging_amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits including two decimals is allowed for field charging_amount"
}
```

400 Example `Exceed total_amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits including two decimals is allowed for field total_amount"
}
```

400 Example `Exceed principal_amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits including two decimals is allowed for field principal_amount"
}
```

400 Example `Exceed interest_amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits including two decimals is allowed for field interest_amount"
}
```

400 Example `Exceed interest_rate limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits including two decimals is allowed for field interest_rate"
}
```

400 Example `Exceed tax_amount limit`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "A maximum of 20 digits including two decimals is allowed for field tax_amount"
}
```

##### Response 404

404 Example `Account not found`:

```json
{
  "error_code": "WP2P0023",
  "code": "WP2P0023",
  "message": "Accounts not found"
}
```

404 Example `Program not found`:

```json
{
  "error_code": "WP2P0022",
  "code": "WP2P0022",
  "message": "Program not found"
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
  "authorization_id": 16397984,
  "date": "2020-01-02T15:14:00.218Z",
  "tracking_id": "82766158-514c-42f0-87e2-1bb3250c6dee",
  "message": "Tracking id has been already used"
}
```

409 Example `Evaluation already exists for CID`:

```json
{
  "error_code": "RULVAL0409",
  "code": "RULVAL0409",
  "message": "Evaluation already exists for CID."
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


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |
| 400 | `WP2P0024` | Invalid installment number. Installment number should be sequential, starting with 1. |
| 400 | `WP2P0025` | Debit program accounts are invalid for installments payments. |
| 400 | `WP2P0026` | Total amount is not equal to the others amounts added |
| 400 | `WP2P0027` | Charging amount is not equal to the sum of all installments total_amount |
| 400 | `WP2P0028` | Installments tax_amount not allowed for financed charge operations |
| 400 | `WP2P0029` | All fields within the financed charge amount must be greater than zero |
| 400 | `WP2P0030` | All fields within the financed charge must have the suffix _amount |
| 400 | `WP2P0005` | Invalid debit processing code. |
| 400 | `WP2P0003` | No Orgs Operation Found |
| 400 | `WP2P0002` | Account has no debit status active. |
| 400 | `WLDG0019` | No Accounts authorization found. |
| 400 | `ERUL0404` | Restriction rule [max_value_authorized_device_unique_transaction] does not pass. |
| 400 | `RULV10400` | Restriction rule [max_value_authorized_device_unique_transaction] does not pass. |
| 400 | `WLDG0006` | No AvailableCreditLimit to complete the transaction - amount: 10, availableCreditLimit: 5.00 |
| 404 | `WP2P0023` | Accounts not found |
| 404 | `WP2P0022` | Program not found |
| 409 | `WP2P0010` | Tracking id is already in use. |
| 409 | `RULVAL0409` | Evaluation already exists for CID. |
| 422 | `WP2P0000` | Authorized account is different from the request |
| 500 | `WP2P0000` | Unexpected Error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;404;409;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-client-webhooks-part-01`, `KU-PAY-installments-payment`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payments/v1/payments/installments/cancel operationId=post-payments-v1-installments-cancel -->
### `POST /payments/v1/payments/installments/cancel` — Cancel installments payment

- **operationId:** `post-payments-v1-installments-cancel`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Installments payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel an existing installments payment. 
>
> This endpoint generates the [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Unique Org ID. | pattern: "TN\\\\-[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}"; minLength: 39; maxLength: 39; example: "TN-c0e4c660-9059-404c-ab22-761aa431766c" |
| `x-account-id` | header | no | string | Optional account ID. |  |
| `x-skip-timeline` | header | no | string | If set to `true`, this will prevent the generation of timeline events in the customer timeline. | example: "true" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `CancelInstallmentsPaymentPayload`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | no | Unique tracking ID of the installments operation. If you don't provide one, the Pismo platform generates it randomly. | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; minLength: 36; maxLength: 50; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `original_tracking_id` | string | no | Unique tracking ID of the original installments operation. You have to provide either `original_tracking_id` or `original_authorization_id` to execute this request. | pattern: "^[0-9a-fA-F]{8}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{4}\\\\b-[0-9a-fA-F]{12}$"; minLength: 36; maxLength: 50; example: "be68db6e-8da0-4761-8632-6a51857bd123" |
| `original_authorization_id` | integer | no | Authorization ID of the original installments operation. You have to provide either `original_authorization_id` or `original_tracking_id` to execute this request. | format: "int64"; example: 15301234 |
| `account_id` | integer | yes | Pismo account ID. | example: 101 |
| `amount` | number | no | Total amount to be cancelled. | format: "float"; example: 12.13 |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

Example `post-v1-payments-cancel-installments-example`:

```text
{
	"amount": 22.30,
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37",
  "metadata": {
      "my-custom-key": "my-custom-info"
  },
  "original_tracking_id": "4bffde04-81f1-42ba-bb00-519daa88d2e6"
}
```

Example `post-v1-payments-cancel-installments-authorization-id-example`:

```text
{
	"amount": 22.30,
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37",
  "metadata": {
      "my-custom-key": "my-custom-info"
  },
  "original_authorization_id": 15301234
}
```

Example `post-v1-payments-cancel-installments-partial-cancellation-example`:

```text
{
	"amount": 10.30,
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37",
  "metadata": {
      "my-custom-key": "my-custom-info"
  },
  "original_tracking_id": "cdde684c-824d-4234-9d00-7a47e41b67cd"
}
```

Example `post-v1-payments-cancel-installments-without-amount-cancellation-example`:

```text
{
	"account_id": 1,
	"tracking_id": "c737895c-8159-4c0c-a92a-a4f8600bff37",
  "metadata": {
      "my-custom-key": "my-custom-info"
  },
  "original_tracking_id": "cdde684c-824d-4234-9d00-7a47e41b67cd"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `InstallmentsPaymentResponse`) |
| 202 | Accepted | `application/json`: object (schema `AcceptedResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `TrackingIdAlreadyInUseResponse`), object (schema `InstallmentsPaymentResponseTrackingIdAlreadyInUseResponse`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID. | format: "int64"; example: 15301234 |
| `event_date` | string | no | Date and time of the authorization, in UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique 36-character identifier for the installments payment. If you didn't provide an identifier, then the Pismo platform automatically generates and includes one in the response. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

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

400 Example `Invalid amount`:

```json
{
  "error_code": "WP2P0000",
  "code": "WP2P0000",
  "message": "The amount must have a maximum of two decimal places."
}
```

400 Example `Invalid account program type`:

```json
{
  "error_code": "WP2P0025",
  "code": "WP2P0025",
  "message": "Debit program accounts are invalid for installments payments."
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

400 Example `OriginalAuthorizationID or OriginalTrackingID missing`:

```json
{
  "error_code": "WP2P0080",
  "code": "WP2P0080",
  "message": "Either the Original Authorization ID or Original Tracking ID is required."
}
```

400 Example `Cancellation amount exceeds original amount`:

```json
{
  "error_code": "EP2P0005",
  "code": "EP2P0005",
  "message": "The amount passed {{.amount}} is greater than the current balance 0.00."
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

404 Example `Account not found`:

```json
{
  "error_code": "WP2P0023",
  "code": "WP2P0023",
  "message": "Accounts not found"
}
```

##### Response 409

409 Example `Tracking ID is already in use by an ongoing request`:

```json
{
  "error_code": "WP2P0010",
  "code": "WP2P0010",
  "message": "Tracking ID is already in use."
}
```

409 Example `Tracking ID has been already used`:

```json
{
  "authorization_id": 16397984,
  "date": "2020-01-02T15:14:00.218Z",
  "tracking_id": "82766158-514c-42f0-87e2-1bb3250c6dee"
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
  "message": "Unexpected error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WP2P0000` | Invalid payload |
| 400 | `WP2P0025` | Debit program accounts are invalid for installments payments. |
| 400 | `WP2P0006` | Invalid credit processing code. |
| 400 | `WP2P0080` | Either the Original Authorization ID or Original Tracking ID is required. |
| 400 | `EP2P0005` | The amount passed {{.amount}} is greater than the current balance 0.00. |
| 404 | `WP2P0023` | Accounts not found |
| 409 | `WP2P0010` | Tracking ID is already in use. |
| 422 | `WP2P0000` | Authorized account is different from the request |
| 500 | `WP2P0000` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;404;409;422;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/InstallmentDetails -->
### Schema `InstallmentDetails`

Pointer: `#/components/schemas/InstallmentDetails`. Type: object (schema `InstallmentDetails`).

> Installment details object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `installment_number` | integer | no | Sequential number that represents the order of the installment. The ordering starts with 1. | example: 1 |
| `total_amount` | number | yes | Total amount of the financed installment, including interest and fees. | format: "float"; example: 1.15 |
| `principal_amount` | number | yes | Principal amount of the financed installment, excluding interest and fees. | format: "float"; example: 10 |
| `interest_amount` | number | no | Total amount of interest applied to this installment. | format: "float"; example: 1 |
| `interest_rate` | number | no | Interest rate applied to the installment. | format: "float"; example: 0.1 |
| `tax_amount` | number | no | Total amount of fixed tax applied to the financing for this installment. | format: "float"; example: 0.05 |

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

<!-- schema: #/components/schemas/InstallmentsPaymentResponseTrackingIdAlreadyInUseResponse -->
### Schema `InstallmentsPaymentResponseTrackingIdAlreadyInUseResponse`

Pointer: `#/components/schemas/InstallmentsPaymentResponseTrackingIdAlreadyInUseResponse`. Type: object (schema `InstallmentsPaymentResponseTrackingIdAlreadyInUseResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer | no | Generated authorization ID. | example: 15301234 |
| `event_date` | string | no | Date and time of the authorization, in UTC-0 (RFC3339) format. | format: "date-time"; example: "2020-01-02T15:14:00.218Z" |
| `tracking_id` | string | no | Unique 36-character identifier for the installments payment. If you didn't provide an identifier, then the Pismo platform automatically generates and includes one in the response. | example: "82766158-514c-42f0-87e2-1bb3250c6dee" |

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
| `api-specs/Core_platform_-_Payment_methods.yaml` | tag `Installments payments`: POST /payments/v1/payments/installments, POST /payments/v1/payments/installments/cancel | https://github.com/PismoDevEx/pismo-api-specs | `9b02c87b6e39a1c8…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-erul` — Error codes: ERUL
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-PAY-installments-payment` — Installments payment
