---
ku_id: KU-API-banking-transaction-banking--payments-part-02
title: 'API reference: Banking - Transaction banking — Payments (part 2 of 3)'
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
- corporate-v3-get-multileg-payment
- corporate-v2-list-scheduled-payment
- corporate-v2-post-scheduled-payments
- corporate-v2-get-scheduled-payment
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-get-started-demand-deposit-accounts
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-ERR-codes-wiac-to-wstm
- KU-ERR-codes-wmlp
- KU-ERR-codes-wpmt
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-corporate-banking-data-events
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
- KU-PAY-multi-leg-payments
- KU-PAY-scheduled-payments
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Payments (part 2 of 3)

**KU ID:** `KU-API-banking-transaction-banking--payments-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Payments` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Payment endpoints supporting external accounts

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /corporate/v3/payments/multileg/{multilegId}` | `corporate-v3-get-multileg-payment` | Get multi-leg payment status | no |
| `GET /corporate/v2/scheduled-payments` | `corporate-v2-list-scheduled-payment` | List scheduled payments | no |
| `POST /corporate/v2/scheduled-payments` | `corporate-v2-post-scheduled-payments` | Schedule payment | no |
| `GET /corporate/v2/scheduled-payments/{scheduledPaymentId}` | `corporate-v2-get-scheduled-payment` | Get scheduled payment | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v3/payments/multileg/{multilegId} operationId=corporate-v3-get-multileg-payment -->
### `GET /corporate/v3/payments/multileg/{multilegId}` — Get multi-leg payment status

- **operationId:** `corporate-v3-get-multileg-payment`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enables users to query the processing status of a multi-leg payment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `multilegId` | path | yes | string | Multileg ID provided when the multileg payment is created. | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e245" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successful response | `application/json`: object (schema `MultiLegV3Status`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `multileg_id` | string (schema `MultilegID`) | yes | A unique multileg payment identifier provided by the client. If an existing `multileg_id` already exists in the system, the API returns a `409` error.<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable — It can't be updated.<br>  - Not recyclable — You can't reuse a `multileg_id`.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e245" |
| `status` | string | yes | Status of the multi-leg processing.<br><br>* `CREATING`: The multileg payment request has been received and queued for execution.<br>* `EXECUTING`: Asynchronous processing of the multileg payment has started.<br>* `DEBITS_EXECUTED`: All debit legs have been successfully executed; credit leg processing is still in progress.<br>* `CREDITS_FAILED`: Used in v2 when one or more credit legs failed. This status is no longer used in v3, but remains in the API for queries on payments created via the V2 endpoint.<br>* `FINISHED`: All payment legs were processed successfully.<br>* `ROLLING_BACK`: One or more payment legs failed, and the rollback process has begun.<br>* `ROLLED_BACK`: One or more payment legs failed, and all successful legs were rolled back.<br>* `ROLLBACK_FAILED`: One or more payment legs failed, rollback was attempted, but the rollback of some legs was unsuccessful.<br>* `TIMED_OUT`: Processing did not complete because the multileg execution timed out.<br> | enum: ["CREATING", "EXECUTING", "DEBITS_EXECUTED", "CREDITS_FAILED", "FINISHED", "ROLLING_BACK", "ROLLED_BACK", "ROLLBACK_FAILED", "TIMED_OUT"]; example: "CREATING" |
| `debits` | array of object (schema `MultiLegItemV3Status`) | no |  |  |
| `credits` | array of object (schema `MultiLegItemV3Status`) | no |  |  |

200 Example `Successful payment`:

```json
{
  "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
  "status": "FINISHED",
  "debits": [
    {
      "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
      "external_account_id": "289",
      "status": "EXECUTED",
      "event_datetime": "2025-09-16T13:35:15.333Z"
    }
  ],
  "credits": [
    {
      "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
      "external_account_id": "289",
      "status": "EXECUTED",
      "event_datetime": "2025-09-16T13:35:15.333Z"
    }
  ]
}
```

200 Example `Rolled back`:

```json
{
  "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
  "status": "ROLLED_BACK",
  "debits": [
    {
      "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
      "external_account_id": "289",
      "status": "FAILED",
      "event_datetime": "2025-09-16T13:35:15.333Z",
      "error": {
        "status": 400,
        "code": "WPMT0010",
        "message": "Insufficient funds"
      }
    },
    {
      "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
      "external_account_id": "289",
      "status": "ROLLED_BACK",
      "event_datetime": "2025-09-16T13:35:15.333Z",
      "rollback": {
        "tracking_id": "63b7c177-cc70-456c-a2ff-5e2504d4bf3e",
        "event_datetime": "2025-09-16T13:35:16.333Z"
      }
    }
  ],
  "credits": [
    {
      "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
      "external_account_id": "289",
      "status": "PENDING"
    }
  ]
}
```

200 Example `Rollback failed`:

```json
{
  "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
  "status": "ROLLBACK_FAILED",
  "debits": [
    {
      "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
      "external_account_id": "289",
      "status": "ROLLBACK_FAILED",
      "event_datetime": "2025-09-16T13:35:15.333Z",
      "rollback": {
        "tracking_id": "8fa69f77-560e-49ab-b29f-7eadf36fb2e3",
        "event_datetime": "2025-09-16T13:35:16.333Z",
        "error": {
          "status": 400,
          "code": "WOBK0007",
          "message": "Operations blocked for account"
        }
      }
    },
    {
      "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
      "external_account_id": "289",
      "status": "ROLLED_BACK",
      "event_datetime": "2025-09-16T13:35:15.333Z",
      "rollback": {
        "tracking_id": "63b7c177-cc70-456c-a2ff-5e2504d4bf3e",
        "event_datetime": "2025-09-16T13:35:16.333Z"
      }
    }
  ],
  "credits": [
    {
      "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
      "external_account_id": "289",
      "status": "FAILED",
      "error": {
        "status": 400,
        "code": "WOBK0007",
        "message": "Operations blocked for account"
      }
    }
  ]
}
```

##### Response 404

404 Example `Multileg not found`:

```json
{
  "code": "WMLP0007",
  "message": "multi leg not found"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 200 | `WPMT0010` | Insufficient funds |
| 200 | `WOBK0007` | Operations blocked for account |
| 404 | `WMLP0007` | multi leg not found |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`, `KU-PAY-multi-leg-payments`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v2/scheduled-payments operationId=corporate-v2-list-scheduled-payment -->
### `GET /corporate/v2/scheduled-payments` — List scheduled payments

- **operationId:** `corporate-v2-list-scheduled-payment`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List all scheduled payments for an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `type` | query | no | string | Determines the type of operation for the listed scheduled payments. | enum: ["CREDIT", "DEBIT", "TRANSFER"]; default: "DEBIT"; example: "CREDIT" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListScheduledPaymentResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `scheduled_payments` | array of object | no | List of scheduled payments |  |
| `scheduled_payments[].id` | string (schema `ScheduledPaymentID`) | no | ID used to reference the scheduled payment for subsequent operations. | example: "d2644122-251b-41fa-b5b5-54cfad097afb" |
| `scheduled_payments[].status` | string (schema `ScheduledPaymentStatus`) | no | Status of scheduled payment | example: "ACTIVE" |
| `pagination` | object (schema `Pagination`) | no | Data related to list pagination using a cursor. |  |

##### Response 400

400 Example `Invalid type value`:

```json
{
  "code": "WPMT0018",
  "message": "The provided type {type} is invalid"
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
| 400 | `WPMT0018` | The provided type {type} is invalid |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/scheduled-payments operationId=corporate-v2-post-scheduled-payments -->
### `POST /corporate/v2/scheduled-payments` — Schedule payment

- **operationId:** `corporate-v2-post-scheduled-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Schedule payments for a specified future date (`schedule_datetime`). For more information, refer to [Schedule payment overview](https://developers.pismo.io/pismo-docs/docs/scheduled-payments).
>
> The payload for this request is similar to that of the [Post payment](ref:corporate-v2-post-payments) endpoint with the exception of the (`schedule_datetime`) property.
>
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.
>
> For more information on payments operations, see [Corporate Banking Launch Reference](doc:corporate-banking-launch-reference).
>
> NOTE:
> - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
> - For scheduled payments, validation of the transaction occurs only during the execution of the scheduled payment.
>
> This endpoint generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)
> - [Current scheduled payment status displayed](https://developers.pismo.io/events/docs/corporate-schedule-payment-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information about events and how to set up event notifications.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `ScheduledPaymentV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | object (schema `Amount`) | yes | Amount |  |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `soft_descriptor` | string (schema `SoftDescriptorPayment`) | no | Brief description that helps to identify a particular transaction on the bank statement.<br><br><b>NOTES</b>:<br>- To be able to send different `soft_descriptor` information for each payment leg in transfer operations, the `soft_descriptor` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br> | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `credit` | object (schema `RequiredCreditTransaction`) | no | Credit transaction. To post a credit, you must provide a `credit` object with a valid credit processing code (`processing_code`) and destination (`external_account_id`).<br><br>To post a transfer, you must provide both credit and debit objects, representing the credit and debit legs of the operation, respectively.<br> |  |
| `debit` | object (schema `RequiredDebitTransaction`) | no | Debit transaction. To post a debit you must provide a `debit` object. If you provide an `earmark_id` value inside the `debit` object, the payment amount is withdrawn directly from the earmark balance. The earmark ID is generated by the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint.<br><br>To post a transfer, you must provide both `credit` and `debit` objects, representing the credit and debit legs of the operation, respectively. If you provide an `earmark_id` value inside the `debit` object, the transferred amount is withdrawn directly from the earmark balance.<br> |  |
| `metadata` | object (schema `MetadataPayment`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><b>NOTES</b>:<br>- The `metadata` field includes a `corporate_metadata` object with the following fields:<br>    - `credit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the credit leg.<br>    - `debit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>    - `earmark_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>- The `corporate_metadata` attribute must be an object. A type mismatch results in an error as mapped in the responses section.<br>- To be able to send different `metadata` information for each payment leg in transfer operations, the `metadata` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"my-id": 2932} |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `force_post` | boolean (schema `ForcePostPayment`) | no | If `true`, the transaction is executed regardless of the accounts balance or state.<br><br>To post a forced transfer, you must specify both `credit` and `debit`, and set `force_post` to `true`.<br><br>Reason-based force payments:<br>  If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, it fails. The reasons that restrict force credit or debit operations are:<br>    - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>    - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credits and force credits are allowed.<br>    - `FORCE_CREDIT_ONLY`: Debits, credits, and force debits are not allowed.<br>    - `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>    - `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>    - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br><br><b>NOTE</b>: Forced transfers from an earmark balance are not supported when `credit`, `debit`, or `earmark_id` are specified.<br> | default: false; example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCode`) | no | Alphanumeric channel code identifier | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |
| `schedule_datetime` | string (schema `ScheduleDatetime`) | yes | The date and time when the transaction is scheduled to occur. Required for scheduled payments. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |

Example `Credit transaction`:

```json
{
  "credit": {
    "external_account_id": "289",
    "processing_code": "220035"
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "soft_descriptor": "Debit operation",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244",
  "schedule_datetime": "2023-03-10T19:05:56.743Z"
}
```

Example `Debit transaction`:

```json
{
  "debit": {
    "external_account_id": "289",
    "processing_code": "220037"
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "soft_descriptor": "Debit operation",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244",
  "schedule_datetime": "2023-03-10T19:05:56.743Z"
}
```

Example `Debit transaction with earmark`:

```json
{
  "debit": {
    "external_account_id": "289",
    "processing_code": "219251",
    "earmark_id": "632b378a-2248-11ee-be56-0242ac120002"
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "soft_descriptor": "Debit operation from earmark balance",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244",
  "schedule_datetime": "2023-03-10T19:05:56.743Z"
}
```

Example `Transfer transaction`:

```json
{
  "credit": {
    "external_account_id": "289",
    "processing_code": "220035",
    "soft_descriptor": "Transfer - Credit leg",
    "metadata": {
      "invoice": 298
    }
  },
  "debit": {
    "external_account_id": "289",
    "processing_code": "220037",
    "soft_descriptor": "Transfer - Debit leg",
    "metadata": {
      "invoice": 892
    }
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244",
  "schedule_datetime": "2023-03-10T19:05:56.743Z"
}
```

Example `Transfer from earmark balance transaction`:

```json
{
  "credit": {
    "external_account_id": "289",
    "processing_code": "220035"
  },
  "debit": {
    "external_account_id": "289",
    "processing_code": "220037",
    "earmark_id": "632b378a-2248-11ee-be56-0242ac120002"
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "soft_descriptor": "Transfer operation from earmark balance",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244",
  "metadata": {
    "invoice": 298
  },
  "schedule_datetime": "2023-03-10T19:05:56.743Z"
}
```

Example `Force transfer transaction`:

```json
{
  "credit": {
    "external_account_id": "289",
    "processing_code": "220035",
    "soft_descriptor": "Force transfer - Credit leg",
    "metadata": {
      "invoice": 298
    }
  },
  "debit": {
    "external_account_id": "289",
    "processing_code": "220037",
    "soft_descriptor": "Force transfer - Debit leg",
    "metadata": {
      "invoice": 892
    }
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244",
  "force_post": true,
  "schedule_datetime": "2023-03-10T19:05:56.743Z"
}
```

Example `Transfer transaction with validation rules`:

```json
{
  "credit": {
    "external_account_id": "289",
    "processing_code": "220035"
  },
  "debit": {
    "external_account_id": "289",
    "processing_code": "220037"
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "soft_descriptor": "Transfer operation with validation rules",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244",
  "validation_rules": {
    "ACCOUNT_STATUS": {
      "override": true
    },
    "LEDGER": {
      "force": true
    }
  },
  "metadata": {
    "invoice": 298
  },
  "schedule_datetime": "2023-03-10T19:05:56.743Z"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ScheduledPaymentResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `ScheduledPaymentID`) | no | ID used to reference the scheduled payment for subsequent operations. | example: "d2644122-251b-41fa-b5b5-54cfad097afb" |

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WPMT0017",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Processing code exceed size`:

```json
{
  "code": "WPMT0018",
  "message": "processing_code must be a maximum of 6 characters in length"
}
```

400 Example `External Account ID exceed size`:

```json
{
  "code": "WPMT0018",
  "message": "external_account_id must be a maximum of 60 characters in length"
}
```

400 Example `External Account ID required`:

```json
{
  "code": "WPMT0018",
  "message": "external_account_id is a required field"
}
```

400 Example `Amount value less than zero`:

```json
{
  "code": "WPMT0018",
  "message": "value must be 0 or greater"
}
```

400 Example `Amount value exceed`:

```json
{
  "code": "WPMT0018",
  "message": "amount must be 100,000,000,000,000,000 or less"
}
```

400 Example `Amount value required`:

```json
{
  "code": "WPMT0018",
  "message": "value is a required field"
}
```

400 Example `Tracking ID exceed size`:

```json
{
  "code": "WPMT0018",
  "message": "tracking_id must be a maximum of 43 characters in length"
}
```

400 Example `Primary and leg metadata conflict`:

```json
{
  "code": "WPMT0018",
  "message": "Cannot use primary and payment legs metadata fields together"
}
```

400 Example `Primary and leg soft descriptor conflict`:

```json
{
  "code": "WPMT0018",
  "message": "Cannot use primary and payment legs soft_descriptor fields together"
}
```

400 Example `Scheduled datetime in the past`:

```json
{
  "code": "WCMN0002",
  "message": "scheduleDatetime: The scheduled datetime earlier than the current datetime"
}
```

400 Example `Scheduled datetime too close to current datetime`:

```json
{
  "code": "WCMN0002",
  "message": "scheduleDatetime: The scheduled datetime is too close to the current datetime"
}
```

400 Example `Unrecognized account ID type`:

```json
{
  "code": "WCAC0010",
  "message": "Token contains an unrecognized account ID type"
}
```

400 Example `Invalid debit processing code`:

```json
{
  "code": "WPMT0005",
  "message": "Invalid debit processing code"
}
```

400 Example `Invalid credit processing code`:

```json
{
  "code": "WPMT0006",
  "message": "Invalid credit processing code"
}
```

400 Example `Action not permitted`:

```json
{
  "code": "WPMT0014",
  "message": "Action not permitted on a closed account"
}
```

400 Example `Tracking ID required`:

```json
{
  "code": "WPMT0018",
  "message": "tracking_id is a required field"
}
```

400 Example `Currency required`:

```json
{
  "code": "WPMT0018",
  "message": "currency is a required field"
}
```

400 Example `Account has not finished onboarding`:

```json
{
  "code": "WPMT0053",
  "message": "Account has not finished onboarding"
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
| 400 | `WPMT0017` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WPMT0018` | processing_code must be a maximum of 6 characters in length |
| 400 | `WCMN0002` | scheduleDatetime: The scheduled datetime earlier than the current datetime |
| 400 | `WCAC0010` | Token contains an unrecognized account ID type |
| 400 | `WPMT0005` | Invalid debit processing code |
| 400 | `WPMT0006` | Invalid credit processing code |
| 400 | `WPMT0014` | Action not permitted on a closed account |
| 400 | `WPMT0053` | Account has not finished onboarding |
| 401 | `WCAC0001` | Account not authorized |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `corporate-schedule-payment-1` | https://developers.pismo.io/events/docs/corporate-schedule-payment-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;500`, has examples `True`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-get-started-demand-deposit-accounts`, `KU-EVT-corporate-banking-data-events`, `KU-PAY-scheduled-payments`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v2/scheduled-payments/{scheduledPaymentId} operationId=corporate-v2-get-scheduled-payment -->
### `GET /corporate/v2/scheduled-payments/{scheduledPaymentId}` — Get scheduled payment

- **operationId:** `corporate-v2-get-scheduled-payment`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a scheduled payment by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `scheduledPaymentId` | path | yes | string | Scheduled payment ID | example: "1234" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get scheduled payment response | `application/json`: object (schema `ScheduledPaymentV2Item`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `ScheduledPaymentID`) | no | ID used to reference the scheduled payment for subsequent operations. | example: "d2644122-251b-41fa-b5b5-54cfad097afb" |
| `status` | string (schema `ScheduledPaymentStatus`) | no | Status of scheduled payment | example: "ACTIVE" |
| `payment` | object (schema `ScheduledPaymentV2Request`) | no |  |  |

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
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-scheduled-payments`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/MultiLegItemV3Status -->
### Schema `MultiLegItemV3Status`

Pointer: `#/components/schemas/MultiLegItemV3Status`. Type: object (schema `MultiLegItemV3Status`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `external_account_id` | string (schema `ExternalAccountId2`) | yes | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `status` | string (schema `LegProcessingStatus`) | yes | Status of the leg processing.<br><br>* `PENDING`: The payment leg is awaiting execution.<br>* `EXECUTED`: The payment leg was executed successfully.<br>* `FAILED`: The payment leg execution failed.<br>* `ROLLED_BACK`: The payment leg was executed successfully but was rolled back due to a failure in another leg.<br>* `ROLLBACK_FAILED`: The payment leg was executed successfully; another leg failed, triggering a rollback, but the rollback for this leg was unsuccessful.<br> | enum: ["PENDING", "EXECUTED", "FAILED", "ROLLED_BACK", "ROLLBACK_FAILED"]; example: "PENDING" |
| `event_datetime` | string (schema `EventDatetime`) | no | Event date and time displayed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `error` | object (schema `MultilegLegError`) | no |  |  |
| `rollback` | object | no |  |  |
| `rollback.tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `rollback.event_datetime` | string (schema `EventDatetime`) | no | Event date and time displayed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `rollback.error` | object (schema `MultilegLegError`) | no |  |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/Pagination -->
### Schema `Pagination`

Pointer: `#/components/schemas/Pagination`. Type: object (schema `Pagination`).

> Data related to list pagination using a cursor.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `cursor` | string (schema `Cursor`) | no | Cursor pointing to the next page of results | example: "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0=" |

<!-- schema: #/components/schemas/Amount -->
### Schema `Amount`

Pointer: `#/components/schemas/Amount`. Type: object (schema `Amount`).

> Amount

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `value` | number (schema `AmountValue`) | yes | Amount value | format: "float"; minimum: 0; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |

<!-- schema: #/components/schemas/RequiredCreditTransaction -->
### Schema `RequiredCreditTransaction`

Pointer: `#/components/schemas/RequiredCreditTransaction`. Type: object (schema `RequiredCreditTransaction`).

> Credit transaction. To post a credit, you must provide a `credit` object with a valid credit processing code (`processing_code`) and destination (`external_account_id`).<br>
> To post a transfer, you must provide both credit and debit objects, representing the credit and debit legs of the operation, respectively.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_account_id` | string (schema `ExternalAccountId2`) | yes | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `processing_code` | string (schema `CreditProcessingCode`) | no | Processing code for posting credit transactions. The code must have a credit balance impact. You can retrieve a list of the organization processing codes using [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant). | maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptorPayment`) | no | Brief description that helps to identify a particular transaction on the bank statement.<br><br><b>NOTES</b>:<br>- To be able to send different `soft_descriptor` information for each payment leg in transfer operations, the `soft_descriptor` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br> | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `metadata` | object (schema `MetadataPayment`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><b>NOTES</b>:<br>- The `metadata` field includes a `corporate_metadata` object with the following fields:<br>    - `credit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the credit leg.<br>    - `debit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>    - `earmark_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>- The `corporate_metadata` attribute must be an object. A type mismatch results in an error as mapped in the responses section.<br>- To be able to send different `metadata` information for each payment leg in transfer operations, the `metadata` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"my-id": 2932} |

<!-- schema: #/components/schemas/RequiredDebitTransaction -->
### Schema `RequiredDebitTransaction`

Pointer: `#/components/schemas/RequiredDebitTransaction`. Type: object (schema `RequiredDebitTransaction`).

> Debit transaction. To post a debit you must provide a `debit` object. If you provide an `earmark_id` value inside the `debit` object, the payment amount is withdrawn directly from the earmark balance. The earmark ID is generated by the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint.<br>
> To post a transfer, you must provide both `credit` and `debit` objects, representing the credit and debit legs of the operation, respectively. If you provide an `earmark_id` value inside the `debit` object, the transferred amount is withdrawn directly from the earmark balance.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_account_id` | string (schema `ExternalAccountId2`) | yes | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `processing_code` | string (schema `DebitProcessingCode`) | no | Processing code to be used for posting the debit transaction. List the organization processing codes in [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | maxLength: 6; example: "220037" |
| `earmark_id` | string (schema `EarmarkIdWithdrawal`) | no | ID of the earmark from which the amount is withdrawn. The earmark ID is generated by the [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint. | minLength: 1; maxLength: 60; example: "dadaab22-6e28-4746-8440-0caa030f0f3f" |
| `soft_descriptor` | string (schema `SoftDescriptorPayment`) | no | Brief description that helps to identify a particular transaction on the bank statement.<br><br><b>NOTES</b>:<br>- To be able to send different `soft_descriptor` information for each payment leg in transfer operations, the `soft_descriptor` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br> | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `metadata` | object (schema `MetadataPayment`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><b>NOTES</b>:<br>- The `metadata` field includes a `corporate_metadata` object with the following fields:<br>    - `credit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the credit leg.<br>    - `debit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>    - `earmark_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>- The `corporate_metadata` attribute must be an object. A type mismatch results in an error as mapped in the responses section.<br>- To be able to send different `metadata` information for each payment leg in transfer operations, the `metadata` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"my-id": 2932} |

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

<!-- schema: #/components/schemas/ScheduledPaymentV2Request -->
### Schema `ScheduledPaymentV2Request`

Pointer: `#/components/schemas/ScheduledPaymentV2Request`. Type: object (schema `ScheduledPaymentV2Request`).

Composition: includes the fields of schema `PaymentV2Request` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | object (schema `Amount`) | yes | Amount |  |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `soft_descriptor` | string (schema `SoftDescriptorPayment`) | no | Brief description that helps to identify a particular transaction on the bank statement.<br><br><b>NOTES</b>:<br>- To be able to send different `soft_descriptor` information for each payment leg in transfer operations, the `soft_descriptor` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br> | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `credit` | object (schema `RequiredCreditTransaction`) | no | Credit transaction. To post a credit, you must provide a `credit` object with a valid credit processing code (`processing_code`) and destination (`external_account_id`).<br><br>To post a transfer, you must provide both credit and debit objects, representing the credit and debit legs of the operation, respectively.<br> |  |
| `debit` | object (schema `RequiredDebitTransaction`) | no | Debit transaction. To post a debit you must provide a `debit` object. If you provide an `earmark_id` value inside the `debit` object, the payment amount is withdrawn directly from the earmark balance. The earmark ID is generated by the [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint.<br><br>To post a transfer, you must provide both `credit` and `debit` objects, representing the credit and debit legs of the operation, respectively. If you provide an `earmark_id` value inside the `debit` object, the transferred amount is withdrawn directly from the earmark balance.<br> |  |
| `metadata` | object (schema `MetadataPayment`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><b>NOTES</b>:<br>- The `metadata` field includes a `corporate_metadata` object with the following fields:<br>    - `credit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the credit leg.<br>    - `debit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>    - `earmark_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>- The `corporate_metadata` attribute must be an object. A type mismatch results in an error as mapped in the responses section.<br>- To be able to send different `metadata` information for each payment leg in transfer operations, the `metadata` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"my-id": 2932} |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `force_post` | boolean (schema `ForcePostPayment`) | no | If `true`, the transaction is executed regardless of the accounts balance or state.<br><br>To post a forced transfer, you must specify both `credit` and `debit`, and set `force_post` to `true`.<br><br>Reason-based force payments:<br>  If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, it fails. The reasons that restrict force credit or debit operations are:<br>    - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>    - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credits and force credits are allowed.<br>    - `FORCE_CREDIT_ONLY`: Debits, credits, and force debits are not allowed.<br>    - `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>    - `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>    - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br><br><b>NOTE</b>: Forced transfers from an earmark balance are not supported when `credit`, `debit`, or `earmark_id` are specified.<br> | default: false; example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCode`) | no | Alphanumeric channel code identifier | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |
| `schedule_datetime` | string (schema `ScheduleDatetime`) | yes | The date and time when the transaction is scheduled to occur. Required for scheduled payments. Format = yyyy-mm-dd:hr:mm:ss. | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |

<!-- schema: #/components/schemas/MultilegLegError -->
### Schema `MultilegLegError`

Pointer: `#/components/schemas/MultilegLegError`. Type: object (schema `MultilegLegError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | integer | no | HTTP Status code of the error | example: 400 |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Payments`: GET /corporate/v3/payments/multileg/{multilegId}, GET /corporate/v2/scheduled-payments, POST /corporate/v2/scheduled-payments, GET /corporate/v2/scheduled-payments/{scheduledPaymentId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-get-started-demand-deposit-accounts` — Get started with demand deposit accounts (DDAs)
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-ERR-codes-wmlp` — Error codes: WMLP
- `KU-ERR-codes-wpmt` — Error codes: WPMT
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
- `KU-PAY-multi-leg-payments` — Multi-leg payments
- `KU-PAY-scheduled-payments` — Schedule payment overview
