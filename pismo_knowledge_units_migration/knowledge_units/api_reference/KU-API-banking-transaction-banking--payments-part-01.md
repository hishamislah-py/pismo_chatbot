---
ku_id: KU-API-banking-transaction-banking--payments-part-01
title: 'API reference: Banking - Transaction banking — Payments (part 1 of 3)'
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
- corporate-v2-post-payments
- corporate-v2-post-confirm-payments
- corporate-v2-post-cancel-payments
- corporate-v3-post-multileg-payments
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-account-balance-definitions-for-transaction-banking
- KU-BANK-calendars-and-holidays
- KU-BANK-dated-transactions
- KU-BANK-dormancy
- KU-BANK-get-started-demand-deposit-accounts
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-ERR-codes-weam
- KU-ERR-codes-wiac-to-wstm
- KU-ERR-codes-wmlp
- KU-ERR-codes-wpmt
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-corporate-banking-data-events
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
- KU-PAY-bulk-file-based-payment-processing
- KU-PAY-multi-leg-payments
- KU-PAY-payment-overview-and-instant-payments
- KU-PAY-scheduled-payments
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Payments (part 1 of 3)

**KU ID:** `KU-API-banking-transaction-banking--payments-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Payments` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Payment endpoints supporting external accounts

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /corporate/v2/payments` | `corporate-v2-post-payments` | Post payment | no |
| `POST /corporate/v2/payments/confirm` | `corporate-v2-post-confirm-payments` | Confirm payment | no |
| `POST /corporate/v2/payments/cancel` | `corporate-v2-post-cancel-payments` | Cancel payment | no |
| `POST /corporate/v3/payments/multileg` | `corporate-v3-post-multileg-payments` | Post multi-leg payment | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/payments operationId=corporate-v2-post-payments -->
### `POST /corporate/v2/payments` — Post payment

- **operationId:** `corporate-v2-post-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Enable users to submit a payment to the Pismo platform. It supports posting debits and credits to an account, as well as facilitating fund transfers between accounts.
>
> For details about payment operations, see [Payment overview](doc:payment-overview) and [Corporate Banking Launch Reference](doc:corporate-banking-launch-reference).
>
> <b>NOTES</b>:
>   - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
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

**Content type `application/json`** — schema: object (schema `PaymentV2Request`)

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
  "channel": "GCE",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244"
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
  "channel": "GCE",
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244"
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
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244"
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
  "tracking_id": "0a50c88a-ade8-4bcc-a639-9a0b0f11e244"
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
  }
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
  "force_post": true
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

400 Example `External account ID contains characters not permitted`:

```json
{
  "code": "WPMT0018",
  "message": "external_account_id contains characters not permitted: [characters]"
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

400 Example `Unrecognized account ID type`:

```json
{
  "code": "WCAC0010",
  "message": "Token contains an unrecognized account ID type"
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
| 400 | `WCAC0010` | Token contains an unrecognized account ID type |
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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-account-balance-definitions-for-transaction-banking`, `KU-BANK-calendars-and-holidays`, `KU-BANK-dated-transactions`, `KU-BANK-dormancy`, `KU-BANK-get-started-demand-deposit-accounts`, `KU-EVT-corporate-banking-data-events`, `KU-PAY-bulk-file-based-payment-processing`, `KU-PAY-multi-leg-payments`, `KU-PAY-payment-overview-and-instant-payments`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/payments/confirm operationId=corporate-v2-post-confirm-payments -->
### `POST /corporate/v2/payments/confirm` — Confirm payment

- **operationId:** `corporate-v2-post-confirm-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Confirm an existing payment operation.
>
> NOTE:
> - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
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

Guides that link to this operation: `KU-BANK-calendars-and-holidays`, `KU-BANK-dated-transactions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/payments/cancel operationId=corporate-v2-post-cancel-payments -->
### `POST /corporate/v2/payments/cancel` — Cancel payment

- **operationId:** `corporate-v2-post-cancel-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel an existing payment operation.
>
> NOTE:
> - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
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

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v3/payments/multileg operationId=corporate-v3-post-multileg-payments -->
### `POST /corporate/v3/payments/multileg` — Post multi-leg payment

- **operationId:** `corporate-v3-post-multileg-payments`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Payments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Allow you to submit a payment with multiple legs to the platform. The payments are processed asynchronously and must contain at least two legs, but no more than 20.
> The payload contains `debits` and `credits` lists. These lists include legs that follow the requirements of `credit` and `debit` objects in the [Post payment](ref:corporate-v2-post-payments) endpoint.
> For information about multi-leg payments, refer to the [Multi-leg payments](doc:multi-leg-payments) guide.
> **NOTES**:
>   - To find the correct reason IDs, refer to the [List account status reasons](ref:get-accounts-v1-accounts-status-reasons) endpoint.
>   - This endpoint does not support forced transfers from an earmark balance.
>   - For error handling, see [Error handling mechanism](doc:payment-overview#error-handling-mechanism) in _Payment overview_.
>   - **Processing sequence**: Debit legs are always processed before credit legs. Within each group, the sequence is not guaranteed, and the order of execution among debits or among credits is non-deterministic.
>
> Each leg generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - If flex controls are configured, a [Flex control evaluated](https://developers.pismo.io/events/docs/rules-evaluation-requested-1) event is triggered.
> Additionally, the following events are generated for multi-leg payments:
> - [Multi-leg payment lifecycle created](https://developers.pismo.io/events/docs/corporate-multi-leg-creation-2)
> - [Multi-leg payment lifecycle status changed](https://developers.pismo.io/events/docs/corporate-multi-leg-status-change-2)
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `MultiLegPaymentV3Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `multileg_id` | string (schema `MultilegID`) | yes | A unique multileg payment identifier provided by the client. If an existing `multileg_id` already exists in the system, the API returns a `409` error.<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable — It can't be updated.<br>  - Not recyclable — You can't reuse a `multileg_id`.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e245" |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `debits` | array of object (schema `DebitLegV3Request`) | no |  |  |
| `credits` | array of object (schema `CreditLegV3Request`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `MultiLegPaymentV3Response`) |
| 400 | Bad request | `application/json`: object (schema `MultiLegPaymentV3ErrorResponse`) |
| 403 | The request has been lost |  |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `multileg_id` | string (schema `MultilegID`) | no | A unique multileg payment identifier provided by the client. If an existing `multileg_id` already exists in the system, the API returns a `409` error.<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable — It can't be updated.<br>  - Not recyclable — You can't reuse a `multileg_id`.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e245" |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `debits` | array of object (schema `DebitLegV3Response`) | no |  |  |
| `credits` | array of object (schema `CreditLegV3Response`) | no |  |  |

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WMLP0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Multileg ID exceed size`:

```json
{
  "code": "WMLP0002",
  "message": "multileg_id must be a maximum of 43 characters in length"
}
```

400 Example `Multileg ID required`:

```json
{
  "code": "WMLP0002",
  "message": "`multileg_id` is a required field"
}
```

400 Example `Metadata exceeded the maximum size`:

```json
{
  "code": "WMLP0002",
  "message": "metadata exceeded the maximum allowed size of 1024 bytes"
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

400 Example `Metadata primary and payment legs fields conflict`:

```json
{
  "code": "WMLP0008",
  "message": "Cannot use primary and payment legs metadata fields together"
}
```

400 Example `Program not found`:

```json
{
  "code": "WMLP1044",
  "message": "Program not found"
}
```

400 Example `Processing code exceed size`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `External Account ID exceed size`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `External Account ID required`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Amount value exceed`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `External account ID contains characters not permitted`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Currency required`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Validation rules errors`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "ee00de0f-a0ae-4136-95ca-e9d7f4d3f321",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Rates enforcement fee deduction model not supported`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "validation_rules": {
          "RATES": {
            "override": false
          }
        },
        "errors": [
          {
            "code": "WMLP1049",
            "message": "Rates enforcement is not supported for operations with a fee deduction model (deductFromTransactionValue)"
          }
        ]
      }
    ],
    "credits": []
  }
}
```

400 Example `Insufficient balance`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Invalid processing code`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Currency mismatch`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Amount has invalid decimal places for currency`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Invalid account status`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Account has not finished onboarding`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Earmark not active`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Earmark insufficient funds`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Weekend error`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Holiday error`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Account not found`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Earmark not found`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Processing code not found`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Tracking ID already exists`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Closed debit account`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Closed credit account`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Force debit restrictions`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Force credit restrictions`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Payment date cannot be earlier than account creation date`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Payment date cannot be earlier than account migration date`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Retroactive payment datetime not allowed`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Payment business date before earmark creation`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Back business dating disabled`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Operations blocked for account`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Invalid business date for the current business day cycle`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Invalid business date format`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Channel exceed size`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: One or more legs did not pass validation.",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
        "external_account_id": "289",
        "processing_code": "12345",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
        "channel": "Channel name is too long",
        "errors": [
          {
            "code": "WMLP0002",
            "message": "channel must be a maximum of 20 characters in length"
          }
        ]
      }
    ],
    "credits": [
      {
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Channel contains character not permitted`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: One or more legs did not pass validation.",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
        "external_account_id": "289",
        "processing_code": "12345",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
        "channel": "Channel name with invalid character: |",
        "errors": [
          {
            "code": "WMLP0002",
            "message": "channel contains character not permitted"
          }
        ]
      }
    ],
    "credits": [
      {
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Debit not allowed by status reason`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
    ],
    "credits": [
      {
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "errors": []
      }
    ]
  }
}
```

400 Example `Credit not allowed by status reason`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Future payment datetime above limit`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Tracking ID conflict within request payload`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "duplicated-tracking-id-123",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "currency": "USD",
        "earmark_id": "dadaab22-6e28-4746-8440-0caa030f0f3f",
        "errors": [
          {
            "code": "WMLP1040",
            "message": "Tracking ID already in use by another payment leg in the request"
          }
        ]
      }
    ],
    "credits": [
      {
        "tracking_id": "duplicated-tracking-id-123",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "payment_datetime": "2030-06-30T12:23:45.000Z",
        "currency": "USD",
        "errors": [
          {
            "code": "WMLP1040",
            "message": "Tracking ID already in use by another payment leg in the request"
          }
        ]
      }
    ]
  }
}
```

400 Example `Cannot post back value-dated for division`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Cannot post future value-dated for division`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
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
}
```

400 Example `Invalid account currency code`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: one or more legs did not pass validation",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "payment_datetime": "2030-06-30T12:23:45.000Z",
        "currency": "USD",
        "errors": [
          {
            "code": "WMLP1043",
            "message": "Invalid account currency code"
          }
        ]
      }
    ]
  }
}
```

400 Example `Channel not found`:

```json
{
  "code": "WMLP0005",
  "message": "Validation error: One or more legs did not pass validation.",
  "data": {
    "multileg_id": "b37a045b-8f84-4085-ac97-1d8684a4227b",
    "debits": [
      {
        "tracking_id": "7ebb12b9-98e1-469c-b57f-07aebbe12658",
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
        "tracking_id": "eb93fac3-548e-4a09-a577-1b678b4a9986",
        "external_account_id": "289",
        "processing_code": "220035",
        "soft_descriptor": "ACME Inc. - Invoice 2938",
        "amount": 1000.52,
        "payment_datetime": "2030-06-30T12:23:45.000Z",
        "currency": "USD",
        "business_date": "2025-05-30",
        "channel": "GCE",
        "errors": [
          {
            "code": "WMLP1046",
            "message": "Channel not found"
          }
        ]
      }
    ]
  }
}
```

##### Response 409

409 Example `Multileg ID is already in use`:

```json
{
  "code": "WMLP0009",
  "message": "multileg_id is already in use"
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
| 400 | `WMLP0002` | multileg_id must be a maximum of 43 characters in length |
| 400 | `WMLP0003` | Multi-leg payments must have up to 20 legs |
| 400 | `WMLP0004` | Multi-leg payments must have at least 2 legs |
| 400 | `WMLP0008` | Cannot use primary and payment legs metadata fields together |
| 400 | `WMLP1044` | Program not found |
| 400 | `WMLP0005` | Validation error: one or more legs did not pass validation |
| 400 | `WMLP1026` | Payment request with conflicting force parameters |
| 400 | `WMLP1028` | Invalid params for validation rule ACCOUNT_STATUS |
| 400 | `WMLP1027` | Invalid validation rule UNKNOWN |
| 400 | `WMLP1049` | Rates enforcement is not supported for operations with a fee deduction model (deductFromTransactionValue) |
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
| 400 | `WMLP1040` | Tracking ID already in use by another payment leg in the request |
| 400 | `WMLP1041` | Cannot post back value-dated transaction for this division |
| 400 | `WMLP1042` | Cannot post future value-dated transaction for this division |
| 400 | `WMLP1043` | Invalid account currency code |
| 400 | `WMLP1046` | Channel not found |
| 409 | `WMLP0009` | multileg_id is already in use |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `corporate-multi-leg-creation-2` | https://developers.pismo.io/events/docs/corporate-multi-leg-creation-2 |
| `corporate-multi-leg-status-change-2` | https://developers.pismo.io/events/docs/corporate-multi-leg-status-change-2 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |
| `rules-evaluation-requested-1` | https://developers.pismo.io/events/docs/rules-evaluation-requested-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;409;500`, has examples `True`, emits events `4`, deprecated `False`.

Guides that link to this operation: `KU-BANK-dormancy`, `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`, `KU-PAY-scheduled-payments`.

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

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/DebitLegV3Request -->
### Schema `DebitLegV3Request`

Pointer: `#/components/schemas/DebitLegV3Request`. Type: object (schema `DebitLegV3Request`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingIdMultiLegV3`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` already exists in the system, the API returns a `400` error.<br><br>For information about tracking IDs, see [Tracking ID requirement](https://developers.pismo.io/pismo-docs/docs/payment-overview#tracking-id-requirement).<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable: This field cannot be updated.<br>  - Not recyclable: `tracking_id` cannot be reused.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `amount` | number (schema `TransactionAmount`) | yes | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | yes | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `external_account_id` | string (schema `ExternalAccountId2`) | yes | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `force_post` | boolean (schema `ForcePostDebit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>The force operation fails if the account has any reason-based force payment restrictions, and the operation violates any of those restrictions. The reasons that restrict force credit or debit operations are:<br>  - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>  - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credit and force credit are allowed.<br>  - `FORCE_CREDIT_ONLY`: Debits, credits and force debit are not allowed.<br>  - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCode`) | no | Alphanumeric channel code identifier | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `earmark_id` | string (schema `EarmarkIdWithdrawal`) | no | ID of the earmark from which the amount is withdrawn. The earmark ID is generated by the [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint. | minLength: 1; maxLength: 60; example: "dadaab22-6e28-4746-8440-0caa030f0f3f" |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

<!-- schema: #/components/schemas/CreditLegV3Request -->
### Schema `CreditLegV3Request`

Pointer: `#/components/schemas/CreditLegV3Request`. Type: object (schema `CreditLegV3Request`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingIdMultiLegV3`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` already exists in the system, the API returns a `400` error.<br><br>For information about tracking IDs, see [Tracking ID requirement](https://developers.pismo.io/pismo-docs/docs/payment-overview#tracking-id-requirement).<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable: This field cannot be updated.<br>  - Not recyclable: `tracking_id` cannot be reused.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `amount` | number (schema `TransactionAmount`) | yes | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | yes | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `external_account_id` | string (schema `ExternalAccountId2`) | yes | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `force_post` | boolean (schema `ForcePostCredit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, the force operation fails. The reasons that restrict force credit or debit operations are:<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>- `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>- `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCode`) | no | Alphanumeric channel code identifier | pattern: "^[a-zA-Z0-9]+$"; minLength: 1; maxLength: 20; example: "GDP" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

<!-- schema: #/components/schemas/DebitLegV3Response -->
### Schema `DebitLegV3Response`

Pointer: `#/components/schemas/DebitLegV3Response`. Type: object (schema `DebitLegV3Response`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingIdMultiLegV3`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` already exists in the system, the API returns a `400` error.<br><br>For information about tracking IDs, see [Tracking ID requirement](https://developers.pismo.io/pismo-docs/docs/payment-overview#tracking-id-requirement).<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable: This field cannot be updated.<br>  - Not recyclable: `tracking_id` cannot be reused.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `force_post` | boolean (schema `ForcePostDebit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>The force operation fails if the account has any reason-based force payment restrictions, and the operation violates any of those restrictions. The reasons that restrict force credit or debit operations are:<br>  - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>  - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credit and force credit are allowed.<br>  - `FORCE_CREDIT_ONLY`: Debits, credits and force debit are not allowed.<br>  - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCodeResponse`) | no | Alphanumeric channel code | example: "GDP" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `earmark_id` | string (schema `EarmarkIdWithdrawal`) | no | ID of the earmark from which the amount is withdrawn. The earmark ID is generated by the [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint. | minLength: 1; maxLength: 60; example: "dadaab22-6e28-4746-8440-0caa030f0f3f" |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

<!-- schema: #/components/schemas/CreditLegV3Response -->
### Schema `CreditLegV3Response`

Pointer: `#/components/schemas/CreditLegV3Response`. Type: object (schema `CreditLegV3Response`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingIdMultiLegV3`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` already exists in the system, the API returns a `400` error.<br><br>For information about tracking IDs, see [Tracking ID requirement](https://developers.pismo.io/pismo-docs/docs/payment-overview#tracking-id-requirement).<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable: This field cannot be updated.<br>  - Not recyclable: `tracking_id` cannot be reused.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `force_post` | boolean (schema `ForcePostCredit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, the force operation fails. The reasons that restrict force credit or debit operations are:<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>- `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>- `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCodeResponse`) | no | Alphanumeric channel code | example: "GDP" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

<!-- schema: #/components/schemas/MultiLegPaymentV3ErrorResponse -->
### Schema `MultiLegPaymentV3ErrorResponse`

Pointer: `#/components/schemas/MultiLegPaymentV3ErrorResponse`. Type: object (schema `MultiLegPaymentV3ErrorResponse`).

Composition: includes the fields of schema `ErrorResponse` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |
| `data` | object | no |  |  |
| `data.multileg_id` | string (schema `MultilegID`) | no | A unique multileg payment identifier provided by the client. If an existing `multileg_id` already exists in the system, the API returns a `409` error.<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable — It can't be updated.<br>  - Not recyclable — You can't reuse a `multileg_id`.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e245" |
| `data.debits` | array of object (schema `DebitLegV3ErrorResponse`) | no |  |  |
| `data.credits` | array of object (schema `CreditLegV3ErrorResponse`) | no |  |  |

<!-- schema: #/components/schemas/DebitLegV3ErrorResponse -->
### Schema `DebitLegV3ErrorResponse`

Pointer: `#/components/schemas/DebitLegV3ErrorResponse`. Type: object (schema `DebitLegV3ErrorResponse`).

Composition: includes the fields of schema `DebitLegV3Response` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingIdMultiLegV3`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` already exists in the system, the API returns a `400` error.<br><br>For information about tracking IDs, see [Tracking ID requirement](https://developers.pismo.io/pismo-docs/docs/payment-overview#tracking-id-requirement).<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable: This field cannot be updated.<br>  - Not recyclable: `tracking_id` cannot be reused.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `force_post` | boolean (schema `ForcePostDebit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>The force operation fails if the account has any reason-based force payment restrictions, and the operation violates any of those restrictions. The reasons that restrict force credit or debit operations are:<br>  - `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>  - `CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED`: Only credit and force credit are allowed.<br>  - `FORCE_CREDIT_ONLY`: Debits, credits and force debit are not allowed.<br>  - `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCodeResponse`) | no | Alphanumeric channel code | example: "GDP" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `earmark_id` | string (schema `EarmarkIdWithdrawal`) | no | ID of the earmark from which the amount is withdrawn. The earmark ID is generated by the [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks) endpoint. | minLength: 1; maxLength: 60; example: "dadaab22-6e28-4746-8440-0caa030f0f3f" |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `errors` | array of object (schema `ErrorResponse`) | no |  | example: [] |

<!-- schema: #/components/schemas/CreditLegV3ErrorResponse -->
### Schema `CreditLegV3ErrorResponse`

Pointer: `#/components/schemas/CreditLegV3ErrorResponse`. Type: object (schema `CreditLegV3ErrorResponse`).

Composition: includes the fields of schema `CreditLegV3Response` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingIdMultiLegV3`) | no | A unique payment tracking number provided by the client. If an existing `tracking_id` already exists in the system, the API returns a `400` error.<br><br>For information about tracking IDs, see [Tracking ID requirement](https://developers.pismo.io/pismo-docs/docs/payment-overview#tracking-id-requirement).<br><br>This field is:<br>  - Unique within the Organization.<br>  - Immutable: This field cannot be updated.<br>  - Not recyclable: `tracking_id` cannot be reused.<br> | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `external_account_id` | string (schema `ExternalAccountId2`) | no | External ID of the account to which the transaction is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "289" |
| `amount` | number (schema `TransactionAmount`) | no | Transaction amount | format: "float"; minimum: 0.01; maximum: 100000000000000000; example: 1000.52 |
| `processing_code` | string (schema `ProcessingCode2`) | no | Processing code used for posting the transaction. The code must have a balance impact compatible with the operation type `debit` or `credit`. To list the organization processing codes, use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/get-processing-code-by-tenant) endpoint. | minLength: 1; maxLength: 6; example: "220035" |
| `soft_descriptor` | string (schema `SoftDescriptor`) | no | Brief description that helps to identify a particular transaction on the bank statement. | minLength: 0; maxLength: 100; example: "ACME Inc. - Invoice 2938" |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |
| `force_post` | boolean (schema `ForcePostCredit`) | no | If `true`, the operation is performed regardless of the account status, balance, or state, unless the account is closed.<br><br>If the account has any reason-based force payment restrictions, and the operation violates any of those restrictions, the force operation fails. The reasons that restrict force credit or debit operations are:<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `ALL_NO_FORCE_ALLOWED`: Debits and credits are permitted, but force operations are not allowed.<br>- `DEBIT_ONLY_NO_FORCE_CREDIT_ALLOWED`: Only debits and force debits are allowed.<br>- `FORCE_DEBIT_ONLY`: Debits, credits, and force credits are not allowed.<br>- `NONE_NO_FORCE_ALLOWED`: Debits, credits, force debits, and force credits are not allowed.<br> | example: false |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date and time of the payment. Specifying a `payment_datetime` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The payment datetime is in ISO 8601 format.<br>  - You can backdate payments a maximum of 390 calendar days. You can postdate payments a maximum of 10 calendar days.<br> | format: "date-time"; example: "2023-03-10T19:05:56.743Z" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `channel` | string (schema `ChannelCodeResponse`) | no | Alphanumeric channel code | example: "GDP" |
| `skip_account_date_validation` | boolean (schema `SkipAccountDateValidation`) | no | If `FALSE`, the `payment_datetime` is validated against the account creation date and time. If `TRUE`, the validation is skipped. | default: false; example: false |
| `instant_clearing` | boolean (schema `InstantClearing`) | no | Whether the funds are available when the payment is posted (`true`) or not (`false`). | example: false |
| `metadata` | object (schema `MultilegMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `errors` | array of object (schema `ErrorResponse`) | no |  | example: [] |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Payments`: POST /corporate/v2/payments, POST /corporate/v2/payments/confirm, POST /corporate/v2/payments/cancel, POST /corporate/v3/payments/multileg | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-account-balance-definitions-for-transaction-banking` — Account balance definitions for transaction banking
- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-BANK-dated-transactions` — Business-dated and value-dated transactions
- `KU-BANK-dormancy` — Dormancy and dormancy reactivation exceptions
- `KU-BANK-get-started-demand-deposit-accounts` — Get started with demand deposit accounts (DDAs)
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-ERR-codes-weam` — Error codes: WEAM
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-ERR-codes-wmlp` — Error codes: WMLP
- `KU-ERR-codes-wpmt` — Error codes: WPMT
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
- `KU-PAY-bulk-file-based-payment-processing` — Bulk file-based payment processing
- `KU-PAY-multi-leg-payments` — Multi-leg payments
- `KU-PAY-payment-overview-and-instant-payments` — Banking payment overview, instant payments and integrated payments
- `KU-PAY-scheduled-payments` — Schedule payment overview
