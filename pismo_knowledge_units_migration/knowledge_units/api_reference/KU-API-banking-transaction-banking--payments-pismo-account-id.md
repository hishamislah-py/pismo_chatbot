---
ku_id: KU-API-banking-transaction-banking--payments-pismo-account-id
title: 'API reference: Banking - Transaction banking — Payments (Pismo account ID)'
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
- cash-management-v2-post-payments
- cash-management-v2-post-confirm-payments
- cash-management-v2-post-cancel-payments
- cash-management-v2-post-scheduled-payments
- cash-management-v2-get-scheduled-payment
related_kus:
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-ERR-codes-weam
- KU-ERR-codes-wiac-to-wstm
- KU-ERR-codes-wpmt
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Payments (Pismo account ID)

**KU ID:** `KU-API-banking-transaction-banking--payments-pismo-account-id` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Payments (Pismo account ID)` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Payment endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /cash-management/v2/payments` | `cash-management-v2-post-payments` | Post payment (Pismo account ID) | no |
| `POST /cash-management/v2/payments/confirm` | `cash-management-v2-post-confirm-payments` | Confirm payment (Pismo account ID) | no |
| `POST /cash-management/v2/payments/cancel` | `cash-management-v2-post-cancel-payments` | Cancel payment (Pismo account ID) | no |
| `POST /cash-management/v2/scheduled-payments` | `cash-management-v2-post-scheduled-payments` | Schedule payment (Pismo account ID) | no |
| `GET /cash-management/v2/scheduled-payments/{scheduledPaymentId}` | `cash-management-v2-get-scheduled-payment` | Get scheduled payment (Pismo account ID) | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/cash-management/v2/payments operationId=cash-management-v2-post-payments -->
### `POST /cash-management/v2/payments` — Post payment (Pismo account ID)

- **operationId:** `cash-management-v2-post-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments (Pismo account ID)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enable users to submit a payment to the Pismo platform. It supports posting debits and credits to an account, as well as facilitating fund transfers between accounts.
>
> For details about payment operations, see [Payment overview](doc:payment-overview) and [Corporate Banking Launch Reference](doc:corporate-banking-launch-reference).
>
> <b>NOTES</b>:
>   - This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
>   - To get the correct reason IDs, refer to the [List account status reasons](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts-status-reasons) endpoint.<br>
>
> Each payment operation created generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
> - [Account balance changed (Availables)](https://developers.pismo.io/events/docs/availables-change-available-1)
> - [Accounting entry created](https://developers.pismo.io/events/docs/accounting-entry-creation-1)
> - If flex controls are configured, a [Flex control evaluated](https://developers.pismo.io/events/docs/rules-evaluation-requested-1) event is triggered.
>
> See [Data and reporting](doc:data-reporting-overview) for more information on events and setting up event notifications.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `CoreAccountBasedPaymentV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | object (schema `Amount`) | yes | Amount |  |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `soft_descriptor` | string (schema `SoftDescriptorPayment`) | no | Brief description that helps to identify a particular transaction on the bank statement.<br><br><b>NOTES</b>:<br>- To be able to send different `soft_descriptor` information for each payment leg in transfer operations, the `soft_descriptor` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br> | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `credit` | object (schema `CoreAccountBasedCreditTransaction`) | no | Credit transaction. A credit transaction requires a credit object that includes a valid credit `processing_code` and a destination `account_id`.<br><br>To post a transfer, you must provide both credit and debit objects, with each representing the credit and debit legs of the operation respectively.<br> |  |
| `debit` | object (schema `CoreAccountBasedDebitTransaction`) | no | Debit transaction. To post a debit you must provide a `debit` object. If you provide an `earmark_id` value inside the `debit` object, the payment amount is withdrawn directly from the earmark balance. The earmark ID is generated by the [Create earmark](ref:post-corporate-v2-earmarks) endpoint.<br><br>To post a transfer, you must provide both `credit` and `debit` objects, with each representing the credit and debit legs of the operation respectively. If you provide an `earmark_id` value inside the `debit` object, the transferred amount is withdrawn directly from the earmark balance.<br> |  |
| `metadata` | object (schema `MetadataPayment`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><b>NOTES</b>:<br>- The `metadata` field includes a `corporate_metadata` object with the following fields:<br>    - `credit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the credit leg.<br>    - `debit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>    - `earmark_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>- The `corporate_metadata` attribute must be an object. A type mismatch results in an error as mapped in the responses section.<br>- To be able to send different `metadata` information for each payment leg in transfer operations, the `metadata` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"my-id": 2932} |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `force_post` | boolean (schema `ForcePostPayment`) | no | If `true`, the transaction is executed regardless of the accounts balance or state.<br><br>To post a forced transfer, you must specify both `credit` and `debit`, and set `force_post` to `true`.<br><br>Reason-based force payments:<br>  If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, it fails. The reasons that restrict force credit or debit operations are:<br>    - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>    - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credits and force credits are allowed.<br>    - `FORCE_CREDIT_ONLY`: Debits, credits, and force debits are not allowed.<br>    - `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>    - `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>    - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br><br><b>NOTE</b>: Forced transfers from an earmark balance are not supported when `credit`, `debit`, or `earmark_id` are specified.<br> | default: false; example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCode`) | no | Alphanumeric channel code identifier | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |

Example `Credit transaction`:

```json
{
  "credit": {
    "account_id": 102701621,
    "processing_code": "220035"
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "soft_descriptor": "Debit operation",
  "channel": "GCE",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244"
}
```

Example `Debit transaction`:

```json
{
  "debit": {
    "account_id": 102701621,
    "processing_code": "220037"
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "soft_descriptor": "Debit operation",
  "channel": "GCE",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244"
}
```

Example `Debit transaction with earmark`:

```json
{
  "debit": {
    "account_id": 102701621,
    "processing_code": "219251",
    "earmark_id": "632b378a-2248-11ee-be56-0242ac120002"
  },
  "amount": {
    "currency": "USD",
    "value": 100
  },
  "soft_descriptor": "Debit operation from earmark balance",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244"
}
```

Example `Transfer transaction`:

```json
{
  "credit": {
    "account_id": 102701621,
    "processing_code": "220035",
    "soft_descriptor": "Transfer - Credit leg",
    "metadata": {
      "invoice": 298
    }
  },
  "debit": {
    "account_id": 102701622,
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
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244"
}
```

Example `Transfer from earmark balance transaction`:

```json
{
  "credit": {
    "account_id": 102701621,
    "processing_code": "220035"
  },
  "debit": {
    "account_id": 102701622,
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
  }
}
```

Example `Force transfer transaction`:

```json
{
  "credit": {
    "account_id": 102701621,
    "processing_code": "220035",
    "soft_descriptor": "Force transfer - Credit leg",
    "metadata": {
      "invoice": 298
    }
  },
  "debit": {
    "account_id": 102701622,
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
  "force_post": true
}
```

Example `Transfer transaction with validation rules`:

```json
{
  "credit": {
    "account_id": 102701621,
    "processing_code": "220035"
  },
  "debit": {
    "account_id": 102701622,
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
    },
    "FLEX_CONTROLS": {
      "override": false
    },
    "RATES": {
      "override": false
    }
  },
  "metadata": {
    "invoice": 298
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `PaymentV2Response`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost |  |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `event_datetime` | string (schema `EventDatetime`) | no | Event date and time displayed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |

##### Response 400

400 Example `Operations blocked for account`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WPMT0017",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Corporate account not found`:

```json
{
  "code": "WPMT0011",
  "message": "Corporate account not found"
}
```

400 Example `Account has not finished onboarding`:

```json
{
  "code": "WPMT0053",
  "message": "Account has not finished onboarding"
}
```

400 Example `Processing code exceed size`:

```json
{
  "code": "WPMT0018",
  "message": "processing_code must be a maximum of 6 characters in length"
}
```

400 Example `Account ID required`:

```json
{
  "code": "WPMT0018",
  "message": "account_id is a required field"
}
```

400 Example `Amount value less than zero`:

```json
{
  "code": "WPMT0018",
  "message": "value must be 0 or greater"
}
```

400 Example `Amount value exceeded`:

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

400 Example `Channel contains character not permitted` (channel contains character not permitted):

```json
{
  "code": "WPMT0018",
  "message": "channel contains character not permitted"
}
```

400 Example `Channel exceed size` (channel exceeds maximum length):

```json
{
  "code": "WPMT0018",
  "message": "channel must be a maximum of 20 characters in length"
}
```

400 Example `Validation rules with force_post not allowed`:

```json
{
  "code": "WPMT0029",
  "message": "Payment request with conflicting force parameters"
}
```

400 Example `Invalid validation rule`:

```json
{
  "code": "WPMT0030",
  "message": "Invalid validation rule {validation rule}"
}
```

400 Example `Invalid params for validation rule`:

```json
{
  "code": "WPMT0031",
  "message": "Invalid params for validation rule {validation rule}"
}
```

400 Example `Flex controls denied`:

```json
{
  "code": "WPMT0062",
  "message": "Authorization failed flex control evaluation"
}
```

400 Example `Rates enforcement fee deduction model not supported`:

```json
{
  "code": "WPMT0063",
  "message": "Rates enforcement is not supported for operations with a fee deduction model (deductFromTransactionValue)"
}
```

400 Example `Payment date before account creation date`:

```json
{
  "code": "WPMT0001",
  "message": "The payment date cannot be earlier than the account creation date"
}
```

400 Example `Payment date before account migration date`:

```json
{
  "code": "WPMT0061",
  "message": "The payment date cannot be earlier than the account migration date"
}
```

400 Example `Invalid currency`:

```json
{
  "code": "WPMT0015",
  "message": "Invalid currency"
}
```

400 Example `Currency mismatch`:

```json
{
  "code": "WPMT0016",
  "message": "Cannot perform conversion between account currency and provided currency"
}
```

400 Example `Holiday error`:

```json
{
  "code": "WPMT0003",
  "message": "Cannot post transaction on holidays"
}
```

400 Example `Weekend error`:

```json
{
  "code": "WPMT0004",
  "message": "Cannot post transaction on weekends"
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

400 Example `Invalid account status`:

```json
{
  "code": "WPMT0009",
  "message": "Invalid account status"
}
```

400 Example `Insufficient funds`:

```json
{
  "code": "WPMT0010",
  "message": "Insufficient funds"
}
```

400 Example `Invalid debit earmark processing code`:

```json
{
  "code": "WPMT0021",
  "message": "Invalid debit earmark processing code"
}
```

400 Example `Earmark not active`:

```json
{
  "code": "WEAM0008",
  "message": "Earmark ID `earmark_id` not active"
}
```

400 Example `Earmark insufficient balance`:

```json
{
  "code": "WEAM0006",
  "message": "Earmark does not have sufficient balance to complete this operation. Balance: `earmark_balance`"
}
```

400 Example `Payment business date before earmark creation`:

```json
{
  "code": "WPMT0050",
  "message": "Payment business date cannot be earlier than the earmark creation date"
}
```

400 Example `Orgs operation not found or parameterized`:

```json
{
  "code": "WEAM0017",
  "message": "Orgs operations not found or parameters are incorrect or invalid"
}
```

400 Example `Invalid account program type`:

```json
{
  "code": "WEAM0019",
  "message": "The account's program type is invalid"
}
```

400 Example `Target account cannot be credited`:

```json
{
  "code": "WPMT0022",
  "message": "The account cannot be credited, credit earmark function is not active"
}
```

400 Example `Sender account cannot be debited`:

```json
{
  "code": "WPMT0023",
  "message": "The account cannot be debited. Debit earmark function is not active"
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

400 Example `Force operation not allowed`:

```json
{
  "code": "WPMT0024",
  "message": "Force operation not allowed by reason: {reason_description}"
}
```

400 Example `Debit not permitted`:

```json
{
  "code": "WPMT0025",
  "message": "Debit not permitted on a closed account"
}
```

400 Example `Credit not permitted`:

```json
{
  "code": "WPMT0026",
  "message": "Credit not permitted on a closed account"
}
```

400 Example `Amount has invalid decimal places for currency`:

```json
{
  "code": "WPMT0018",
  "message": "The number of decimal places is not compatible with the specified currency"
}
```

400 Example `Corporate Metadata must be an object`:

```json
{
  "code": "WCMN0002",
  "message": "corporate_metadata is reserved and must be an object"
}
```

400 Example `Invalid business date for the current business day cycle`:

```json
{
  "code": "WPMT0028",
  "message": "Invalid business date for the current business day cycle"
}
```

400 Example `Invalid business date format`:

```json
{
  "code": "WPMT0018",
  "message": "business_date 24-05-2024 should be formatted as yyyy-mm-dd and be a valid date"
}
```

400 Example `Misconfigured administrative division`:

```json
{
  "code": "WPMT0045",
  "message": "Administrative division is misconfigured"
}
```

400 Example `Transfer must be sent by debit account`:

```json
{
  "code": "WPMT0049",
  "message": "Transfer operations must be sent by the debit account"
}
```

400 Example `Future dated earmark payments are not allowed`:

```json
{
  "code": "WPMT0036",
  "message": "Future dated earmark payments are not allowed"
}
```

400 Example `Future dated payments only supports default debit processing code`:

```json
{
  "code": "WPMT0005",
  "message": "Future dated payments only supports default debit processing code"
}
```

400 Example `Future dated payments only supports default credit processing code`:

```json
{
  "code": "WPMT0006",
  "message": "Future dated payments only supports default credit processing code"
}
```

400 Example `Back business dating disabled`:

```json
{
  "code": "WPMT0044",
  "message": "Back business dating is disabled"
}
```

400 Example `Operation not allowed by reason`:

```json
{
  "code": "WPMT0051",
  "message": "Operation not allowed by reason: <reason>"
}
```

400 Example `Future payment datetime above limit`:

```json
{
  "code": "WPMT0035",
  "message": "Future dated payment datetime must be before date limit"
}
```

400 Example `Back payment datetime above limit`:

```json
{
  "code": "WPMT0046",
  "message": "The maximum retroactive payment datetime allowed is <days_limit> days"
}
```

400 Example `Cannot post back value-dated for division`:

```json
{
  "code": "WPMT0054",
  "message": "Cannot post back value-dated transaction for this division"
}
```

400 Example `Cannot post future value-dated for division`:

```json
{
  "code": "WPMT0055",
  "message": "Cannot post future value-dated transaction for this division"
}
```

400 Example `Invalid account currency code`:

```json
{
  "code": "WPMT0056",
  "message": "Invalid account currency code: 999"
}
```

400 Example `Channel not found` (Channel not found):

```json
{
  "code": "WPMT0058",
  "message": "Channel not found"
}
```

400 Example `Invalid processing code`:

```json
{
  "code": "WPMT0008",
  "message": "Invalid processing code"
}
```

400 Example `Account closed error`:

```json
{
  "code": "WPMT0014",
  "message": "Account is closed"
}
```

400 Example `Same account credit debit`:

```json
{
  "code": "WPMT0019",
  "message": "Cannot use same account for credit and debit"
}
```

400 Example `Invalid header account`:

```json
{
  "code": "WCAC0002",
  "message": "Invalid header account"
}
```

400 Example `Account not found`:

```json
{
  "code": "WCAC0012",
  "message": "Account not found"
}
```

400 Example `Invalid time zone`:

```json
{
  "code": "WPMT0002",
  "message": "Invalid timezone {invalid}"
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

##### Response 404

404 Example `Earmark not found`:

```json
{
  "code": "WEAM0007",
  "message": "Earmark with ID `earmark_id` not found"
}
```

##### Response 409

409 Example `Tracking ID already in use`:

```json
{
  "code": "WPMT0007",
  "message": "tracking_id is already in use",
  "data": {
    "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
    "event_datetime": "2025-02-05T21:46:06Z"
  }
}
```

409 Example `Tracking ID already in use by another account`:

```json
{
  "code": "WPMT0052",
  "message": "tracking_id is already in use"
}
```

409 Example `Earmark was concurrently modified`:

```json
{
  "code": "WEAM0049",
  "message": "Earmark was concurrently modified"
}
```

##### Response 423

423 Example `Transaction using this tracking ID in progress`:

```json
{
  "code": "WPMT0047",
  "message": "transaction using this tracking_id is in progress, please try again later"
}
```

423 Example `Earmark locked by a concurrent operation`:

```json
{
  "code": "WEAM0048",
  "message": "Earmark locked by a concurrent operation"
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
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WPMT0017` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WPMT0011` | Corporate account not found |
| 400 | `WPMT0053` | Account has not finished onboarding |
| 400 | `WPMT0018` | processing_code must be a maximum of 6 characters in length |
| 400 | `WPMT0029` | Payment request with conflicting force parameters |
| 400 | `WPMT0030` | Invalid validation rule {validation rule} |
| 400 | `WPMT0031` | Invalid params for validation rule {validation rule} |
| 400 | `WPMT0062` | Authorization failed flex control evaluation |
| 400 | `WPMT0063` | Rates enforcement is not supported for operations with a fee deduction model (deductFromTransactionValue) |
| 400 | `WPMT0001` | The payment date cannot be earlier than the account creation date |
| 400 | `WPMT0061` | The payment date cannot be earlier than the account migration date |
| 400 | `WPMT0015` | Invalid currency |
| 400 | `WPMT0016` | Cannot perform conversion between account currency and provided currency |
| 400 | `WPMT0003` | Cannot post transaction on holidays |
| 400 | `WPMT0004` | Cannot post transaction on weekends |
| 400 | `WPMT0005` | Invalid debit processing code |
| 400 | `WPMT0006` | Invalid credit processing code |
| 400 | `WPMT0009` | Invalid account status |
| 400 | `WPMT0010` | Insufficient funds |
| 400 | `WPMT0021` | Invalid debit earmark processing code |
| 400 | `WEAM0008` | Earmark ID `earmark_id` not active |
| 400 | `WEAM0006` | Earmark does not have sufficient balance to complete this operation. Balance: `earmark_balance` |
| 400 | `WPMT0050` | Payment business date cannot be earlier than the earmark creation date |
| 400 | `WEAM0017` | Orgs operations not found or parameters are incorrect or invalid |
| 400 | `WEAM0019` | The account's program type is invalid |
| 400 | `WPMT0022` | The account cannot be credited, credit earmark function is not active |
| 400 | `WPMT0023` | The account cannot be debited. Debit earmark function is not active |
| 400 | `WPMT0024` | Force operation not allowed by reason: {reason_description} |
| 400 | `WPMT0025` | Debit not permitted on a closed account |
| 400 | `WPMT0026` | Credit not permitted on a closed account |
| 400 | `WCMN0002` | corporate_metadata is reserved and must be an object |
| 400 | `WPMT0028` | Invalid business date for the current business day cycle |
| 400 | `WPMT0045` | Administrative division is misconfigured |
| 400 | `WPMT0049` | Transfer operations must be sent by the debit account |
| 400 | `WPMT0036` | Future dated earmark payments are not allowed |
| 400 | `WPMT0044` | Back business dating is disabled |
| 400 | `WPMT0051` | Operation not allowed by reason: <reason> |
| 400 | `WPMT0035` | Future dated payment datetime must be before date limit |
| 400 | `WPMT0046` | The maximum retroactive payment datetime allowed is <days_limit> days |
| 400 | `WPMT0054` | Cannot post back value-dated transaction for this division |
| 400 | `WPMT0055` | Cannot post future value-dated transaction for this division |
| 400 | `WPMT0056` | Invalid account currency code: 999 |
| 400 | `WPMT0058` | Channel not found |
| 400 | `WPMT0008` | Invalid processing code |
| 400 | `WPMT0014` | Account is closed |
| 400 | `WPMT0019` | Cannot use same account for credit and debit |
| 400 | `WCAC0002` | Invalid header account |
| 400 | `WCAC0012` | Account not found |
| 400 | `WPMT0002` | Invalid timezone {invalid} |
| 401 | `WCAC0001` | Account not authorized |
| 404 | `WEAM0007` | Earmark with ID `earmark_id` not found |
| 409 | `WPMT0007` | tracking_id is already in use |
| 409 | `WPMT0052` | tracking_id is already in use |
| 409 | `WEAM0049` | Earmark was concurrently modified |
| 423 | `WPMT0047` | transaction using this tracking_id is in progress, please try again later |
| 423 | `WEAM0048` | Earmark locked by a concurrent operation |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `accounting-entry-creation-1` | https://developers.pismo.io/events/docs/accounting-entry-creation-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |
| `rules-evaluation-requested-1` | https://developers.pismo.io/events/docs/rules-evaluation-requested-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;404;409;423;500`, has examples `True`, emits events `5`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/cash-management/v2/payments/confirm operationId=cash-management-v2-post-confirm-payments -->
### `POST /cash-management/v2/payments/confirm` — Confirm payment (Pismo account ID)

- **operationId:** `cash-management-v2-post-confirm-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments (Pismo account ID)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Confirm an existing payment operation.
>
> NOTE:
> - This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
> This endpoint generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
> - [Account balance changed (Availables)](https://developers.pismo.io/events/docs/availables-change-available-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information on events and setting up event notifications.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `PaymentSettlementV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `original_tracking_id` | string (schema `OriginalTrackingID`) | yes | Tracking ID for the original operation. | maxLength: 43; example: "249fbd1c-cfcd-48aa-8bcb-1ffe3a5f7978" |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `metadata` | object (schema `ConfirmPaymentMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `SettlementV2Response`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost |  |
| 404 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Errors | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `original_tracking_id` | string (schema `OriginalTrackingID`) | no | Tracking ID for the original operation. | maxLength: 43; example: "249fbd1c-cfcd-48aa-8bcb-1ffe3a5f7978" |
| `tracking_id` | string (schema `TrackingID`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `event_datetime` | string (schema `EventDatetime`) | no | Event date and time displayed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |

##### Response 400

400 Example `Operations blocked for account`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WPMT0017",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Tracking ID exceed size`:

```json
{
  "code": "WPMT0018",
  "message": "tracking_id must be a maximum of 43 characters in length"
}
```

400 Example `Original Tracking ID exceed size`:

```json
{
  "code": "WPMT0018",
  "message": "original_tracking_id must be a maximum of 43 characters in length"
}
```

400 Example `Tracking ID required`:

```json
{
  "code": "WPMT0018",
  "message": "tracking_id is a required field"
}
```

400 Example `Original Tracking ID required`:

```json
{
  "code": "WPMT0018",
  "message": "original_tracking_id is a required field"
}
```

400 Example `Payment date before account creation date`:

```json
{
  "code": "WPMT0001",
  "message": "The payment date cannot be earlier than the account creation date"
}
```

400 Example `Payment date before account migration date`:

```json
{
  "code": "WPMT0061",
  "message": "The payment date cannot be earlier than the account migration date"
}
```

400 Example `Holiday error`:

```json
{
  "code": "WPMT0003",
  "message": "Cannot post transaction on holidays"
}
```

400 Example `Weekend error`:

```json
{
  "code": "WPMT0004",
  "message": "Cannot post transaction on weekends"
}
```

400 Example `Invalid business date for the current business day cycle`:

```json
{
  "code": "WPMT0028",
  "message": "Invalid business date for the current business day cycle"
}
```

400 Example `Transaction owned by another account`:

```json
{
  "code": "WPMT0038",
  "message": "transaction is owned by another account"
}
```

400 Example `Transaction cannot be confirmed`:

```json
{
  "code": "WPMT0039",
  "message": "transaction cannot be confirmed"
}
```

400 Example `Back business dating disabled`:

```json
{
  "code": "WPMT0044",
  "message": "Back business dating is disabled"
}
```

400 Example `Transfer must be sent by debit account`:

```json
{
  "code": "WPMT0049",
  "message": "Transfer operations must be sent by the debit account"
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

##### Response 404

404 Example `Original Tracking ID not found`:

```json
{
  "code": "WPMT0037",
  "message": "original_tracking_id not found"
}
```

##### Response 409

409 Example `Tracking ID already in use`:

```json
{
  "code": "WPMT0007",
  "message": "tracking_id is already in use",
  "data": {
    "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
    "event_datetime": "2025-02-05T21:46:06Z"
  }
}
```

409 Example `Tracking ID already in use by another account`:

```json
{
  "code": "WPMT0052",
  "message": "tracking_id is already in use"
}
```

##### Response 423

423 Example `Transaction using this tracking ID in progress`:

```json
{
  "code": "WPMT0047",
  "message": "transaction using this tracking_id is in progress, please try again later"
}
```

423 Example `Transaction using this original tracking ID in progress`:

```json
{
  "code": "WPMT0048",
  "message": "transaction using this original_tracking_id is in progress, please try again later"
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
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WPMT0017` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WPMT0018` | tracking_id must be a maximum of 43 characters in length |
| 400 | `WPMT0001` | The payment date cannot be earlier than the account creation date |
| 400 | `WPMT0061` | The payment date cannot be earlier than the account migration date |
| 400 | `WPMT0003` | Cannot post transaction on holidays |
| 400 | `WPMT0004` | Cannot post transaction on weekends |
| 400 | `WPMT0028` | Invalid business date for the current business day cycle |
| 400 | `WPMT0038` | transaction is owned by another account |
| 400 | `WPMT0039` | transaction cannot be confirmed |
| 400 | `WPMT0044` | Back business dating is disabled |
| 400 | `WPMT0049` | Transfer operations must be sent by the debit account |
| 401 | `WCAC0001` | Account not authorized |
| 404 | `WPMT0037` | original_tracking_id not found |
| 409 | `WPMT0007` | tracking_id is already in use |
| 409 | `WPMT0052` | tracking_id is already in use |
| 423 | `WPMT0047` | transaction using this tracking_id is in progress, please try again later |
| 423 | `WPMT0048` | transaction using this original_tracking_id is in progress, please try again later |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;404;409;423;500`, has examples `True`, emits events `3`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/cash-management/v2/payments/cancel operationId=cash-management-v2-post-cancel-payments -->
### `POST /cash-management/v2/payments/cancel` — Cancel payment (Pismo account ID)

- **operationId:** `cash-management-v2-post-cancel-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments (Pismo account ID)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel an existing payment operation.
>
> NOTE:
> - This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
>
> This endpoint generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
> - [Account balance changed (Availables)](https://developers.pismo.io/events/docs/availables-change-available-1)
>
> Refer to [Data and reporting](doc:data-reporting-overview) for more information on events and setting up event notifications.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `CancelPaymentV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `original_tracking_id` | string (schema `OriginalTrackingID`) | yes | Tracking ID for the original operation. | maxLength: 43; example: "249fbd1c-cfcd-48aa-8bcb-1ffe3a5f7978" |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `cancellation_method` | string (schema `CancellationMethod`) | no | Define the cancellation method used to determine which dates the cancellation will impact the account balance.<br><br>* `INSTANT` (default): Cancels the payment using the current business date.<br>* `ORIGINAL_DATES`: Cancels the payment using the original payment dates.<br> | enum: ["INSTANT", "ORIGINAL_DATES"]; default: "INSTANT"; example: "INSTANT" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `metadata` | object (schema `ConfirmPaymentMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `SettlementV2Response`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost |  |
| 404 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `original_tracking_id` | string (schema `OriginalTrackingID`) | no | Tracking ID for the original operation. | maxLength: 43; example: "249fbd1c-cfcd-48aa-8bcb-1ffe3a5f7978" |
| `tracking_id` | string (schema `TrackingID`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `event_datetime` | string (schema `EventDatetime`) | no | Event date and time displayed in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |

##### Response 400

400 Example `Operations blocked for account`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WPMT0017",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Tracking ID exceed size`:

```json
{
  "code": "WPMT0018",
  "message": "tracking_id must be a maximum of 43 characters in length"
}
```

400 Example `Original Tracking ID exceed size`:

```json
{
  "code": "WPMT0018",
  "message": "original_tracking_id must be a maximum of 43 characters in length"
}
```

400 Example `Tracking ID required`:

```json
{
  "code": "WPMT0018",
  "message": "tracking_id is a required field"
}
```

400 Example `Original Tracking ID required`:

```json
{
  "code": "WPMT0018",
  "message": "original_tracking_id is a required field"
}
```

400 Example `Payment date before account creation date`:

```json
{
  "code": "WPMT0001",
  "message": "The payment date cannot be earlier than the account creation date"
}
```

400 Example `Payment date before account migration date`:

```json
{
  "code": "WPMT0061",
  "message": "The payment date cannot be earlier than the account migration date"
}
```

400 Example `Holiday error`:

```json
{
  "code": "WPMT0003",
  "message": "Cannot post transaction on holidays"
}
```

400 Example `Weekend error`:

```json
{
  "code": "WPMT0004",
  "message": "Cannot post transaction on weekends"
}
```

400 Example `Invalid business date for the current business day cycle`:

```json
{
  "code": "WPMT0028",
  "message": "Invalid business date for the current business day cycle"
}
```

400 Example `Transaction owned by another account`:

```json
{
  "code": "WPMT0038",
  "message": "transaction is owned by another account"
}
```

400 Example `Transaction cannot be confirmed`:

```json
{
  "code": "WPMT0039",
  "message": "transaction cannot be confirmed"
}
```

400 Example `Transaction cannot be cancelled`:

```json
{
  "code": "WPMT0040",
  "message": "transaction cannot be canceled"
}
```

400 Example `Earmark internal operation cannot be cancelled`:

```json
{
  "code": "WPMT0041",
  "message": "earmark internal_operation cannot be canceled"
}
```

400 Example `Back business dating disabled`:

```json
{
  "code": "WPMT0044",
  "message": "Back business dating is disabled"
}
```

400 Example `Back payment datetime above limit`:

```json
{
  "code": "WPMT0046",
  "message": "The maximum retroactive payment datetime allowed is <days_limit> days"
}
```

400 Example `Transfer must be sent by debit account`:

```json
{
  "code": "WPMT0049",
  "message": "Transfer operations must be sent by the debit account"
}
```

400 Example `Cannot instantly cancel when original business date is after the current date`:

```json
{
  "code": "WPMT0057",
  "message": "Cannot instantly cancel when original business date is after the current date"
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

##### Response 404

404 Example `Original Tracking ID not found`:

```json
{
  "code": "WPMT0037",
  "message": "original_tracking_id not found"
}
```

##### Response 409

409 Example `Tracking ID already in use`:

```json
{
  "code": "WPMT0007",
  "message": "tracking_id is already in use",
  "data": {
    "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
    "event_datetime": "2025-02-05T21:46:06Z"
  }
}
```

409 Example `Tracking ID already in use by another account`:

```json
{
  "code": "WPMT0052",
  "message": "tracking_id is already in use"
}
```

##### Response 423

423 Example `Transaction using this tracking ID in progress`:

```json
{
  "code": "WPMT0047",
  "message": "transaction using this tracking_id is in progress, please try again later"
}
```

423 Example `Transaction using this original tracking ID in progress`:

```json
{
  "code": "WPMT0048",
  "message": "transaction using this original_tracking_id is in progress, please try again later"
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
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WPMT0017` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WPMT0018` | tracking_id must be a maximum of 43 characters in length |
| 400 | `WPMT0001` | The payment date cannot be earlier than the account creation date |
| 400 | `WPMT0061` | The payment date cannot be earlier than the account migration date |
| 400 | `WPMT0003` | Cannot post transaction on holidays |
| 400 | `WPMT0004` | Cannot post transaction on weekends |
| 400 | `WPMT0028` | Invalid business date for the current business day cycle |
| 400 | `WPMT0038` | transaction is owned by another account |
| 400 | `WPMT0039` | transaction cannot be confirmed |
| 400 | `WPMT0040` | transaction cannot be canceled |
| 400 | `WPMT0041` | earmark internal_operation cannot be canceled |
| 400 | `WPMT0044` | Back business dating is disabled |
| 400 | `WPMT0046` | The maximum retroactive payment datetime allowed is <days_limit> days |
| 400 | `WPMT0049` | Transfer operations must be sent by the debit account |
| 400 | `WPMT0057` | Cannot instantly cancel when original business date is after the current date |
| 401 | `WCAC0001` | Account not authorized |
| 404 | `WPMT0037` | original_tracking_id not found |
| 409 | `WPMT0007` | tracking_id is already in use |
| 409 | `WPMT0052` | tracking_id is already in use |
| 423 | `WPMT0047` | transaction using this tracking_id is in progress, please try again later |
| 423 | `WPMT0048` | transaction using this original_tracking_id is in progress, please try again later |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;404;409;423;500`, has examples `True`, emits events `3`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/cash-management/v2/scheduled-payments operationId=cash-management-v2-post-scheduled-payments -->
### `POST /cash-management/v2/scheduled-payments` — Schedule payment (Pismo account ID)

- **operationId:** `cash-management-v2-post-scheduled-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments (Pismo account ID)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Schedule payments for a specified future date (`schedule_datetime`). For more information, refer to [Schedule payment overview](https://developers.pismo.io/pismo-docs/docs/scheduled-payments).
>
> The payload for this request is similar to that of the [Post payment](ref:cash-management-v2-post-payments) endpoint with the exception of the (`schedule_datetime`) property.
>
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.
>
> For more information on payments operations, see [Corporate Banking Launch Reference](doc:corporate-banking-launch-reference).
>
> NOTE:
> - This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
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

**Content type `application/json`** — schema: object (schema `CoreAccountBasedScheduledPaymentV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | object (schema `Amount`) | yes | Amount |  |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `soft_descriptor` | string (schema `SoftDescriptorPayment`) | no | Brief description that helps to identify a particular transaction on the bank statement.<br><br><b>NOTES</b>:<br>- To be able to send different `soft_descriptor` information for each payment leg in transfer operations, the `soft_descriptor` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br> | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `credit` | object (schema `CoreAccountBasedCreditTransaction`) | no | Credit transaction. A credit transaction requires a credit object that includes a valid credit `processing_code` and a destination `account_id`.<br><br>To post a transfer, you must provide both credit and debit objects, with each representing the credit and debit legs of the operation respectively.<br> |  |
| `debit` | object (schema `CoreAccountBasedDebitTransaction`) | no | Debit transaction. To post a debit you must provide a `debit` object. If you provide an `earmark_id` value inside the `debit` object, the payment amount is withdrawn directly from the earmark balance. The earmark ID is generated by the [Create earmark](ref:post-corporate-v2-earmarks) endpoint.<br><br>To post a transfer, you must provide both `credit` and `debit` objects, with each representing the credit and debit legs of the operation respectively. If you provide an `earmark_id` value inside the `debit` object, the transferred amount is withdrawn directly from the earmark balance.<br> |  |
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
    "account_id": 102701621,
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
    "account_id": 102701621,
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

Example `Transfer transaction`:

```json
{
  "credit": {
    "account_id": 102701621,
    "processing_code": "220035",
    "soft_descriptor": "Transfer - Credit leg",
    "metadata": {
      "invoice": 298
    }
  },
  "debit": {
    "account_id": 102701622,
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

400 Example `Account ID required`:

```json
{
  "code": "WPMT0018",
  "message": "account_id is a required field"
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

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/cash-management/v2/scheduled-payments/{scheduledPaymentId} operationId=cash-management-v2-get-scheduled-payment -->
### `GET /cash-management/v2/scheduled-payments/{scheduledPaymentId}` — Get scheduled payment (Pismo account ID)

- **operationId:** `cash-management-v2-get-scheduled-payment`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments (Pismo account ID)`
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

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Amount -->
### Schema `Amount`

Pointer: `#/components/schemas/Amount`. Type: object (schema `Amount`).

> Amount

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `value` | number (schema `AmountValue`) | yes | Amount value | format: "float"; minimum: 0; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |

<!-- schema: #/components/schemas/CoreAccountBasedCreditTransaction -->
### Schema `CoreAccountBasedCreditTransaction`

Pointer: `#/components/schemas/CoreAccountBasedCreditTransaction`. Type: object (schema `CoreAccountBasedCreditTransaction`).

> Credit transaction. A credit transaction requires a credit object that includes a valid credit `processing_code` and a destination `account_id`.<br>
> To post a transfer, you must provide both credit and debit objects, with each representing the credit and debit legs of the operation respectively.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID4`) | yes | Account ID generated by [Create account application](ref:post-acquisitions-v3-s2s-applications).<br><br>`minimum: 1`<br> | format: "int64"; example: 102701621 |
| `processing_code` | string (schema `CreditProcessingCode`) | no | Processing code for posting credit transactions. The code must have a credit balance impact. You can retrieve a list of the organization processing codes using [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant). | maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptorPayment`) | no | Brief description that helps to identify a particular transaction on the bank statement.<br><br><b>NOTES</b>:<br>- To be able to send different `soft_descriptor` information for each payment leg in transfer operations, the `soft_descriptor` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br> | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `metadata` | object (schema `MetadataPayment`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><b>NOTES</b>:<br>- The `metadata` field includes a `corporate_metadata` object with the following fields:<br>    - `credit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the credit leg.<br>    - `debit_external_account_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>    - `earmark_id`: Included in the `corporate_metadata` field when it's provided in the debit leg.<br>- The `corporate_metadata` attribute must be an object. A type mismatch results in an error as mapped in the responses section.<br>- To be able to send different `metadata` information for each payment leg in transfer operations, the `metadata` can be included in the primary or leg field. A conflict between the primary and a leg field results in an error as mapped in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"my-id": 2932} |

<!-- schema: #/components/schemas/CoreAccountBasedDebitTransaction -->
### Schema `CoreAccountBasedDebitTransaction`

Pointer: `#/components/schemas/CoreAccountBasedDebitTransaction`. Type: object (schema `CoreAccountBasedDebitTransaction`).

> Debit transaction. To post a debit you must provide a `debit` object. If you provide an `earmark_id` value inside the `debit` object, the payment amount is withdrawn directly from the earmark balance. The earmark ID is generated by the [Create earmark](ref:post-corporate-v2-earmarks) endpoint.<br>
> To post a transfer, you must provide both `credit` and `debit` objects, with each representing the credit and debit legs of the operation respectively. If you provide an `earmark_id` value inside the `debit` object, the transferred amount is withdrawn directly from the earmark balance.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID4`) | yes | Account ID generated by [Create account application](ref:post-acquisitions-v3-s2s-applications).<br><br>`minimum: 1`<br> | format: "int64"; example: 102701621 |
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

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

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

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Payments (Pismo account ID)`: POST /cash-management/v2/payments, POST /cash-management/v2/payments/confirm, POST /cash-management/v2/payments/cancel, POST /cash-management/v2/scheduled-payments, GET /cash-management/v2/scheduled-payments/{scheduledPaymentId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-ERR-codes-weam` — Error codes: WEAM
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-ERR-codes-wpmt` — Error codes: WPMT
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
