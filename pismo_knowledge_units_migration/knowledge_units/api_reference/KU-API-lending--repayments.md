---
ku_id: KU-API-lending--repayments
title: 'API reference: Lending — Repayments'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Lending.yaml
  sha256: 6667602e6ada2f8177fdb087e70904d04ae7ac8a59867d0cc5e4e6a12cd74b97
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
- registerRepaymentV2
related_kus:
- KU-ERR-codes-elnd
specification_version: 1.0.0
---

# API reference: Lending — Repayments

**KU ID:** `KU-API-lending--repayments` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Repayments` in `api-specs/Lending.yaml` (“Lending”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Creates repayment management features

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/loans/{loanId}/repayment` | `registerRepaymentV2` | Register repayment | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer"}

## Operation contracts

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{loanId}/repayment operationId=registerRepaymentV2 -->
### `POST /v2/loans/{loanId}/repayment` — Register repayment

- **operationId:** `registerRepaymentV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Repayments`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Registers a repayment for the specified loan ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `Idempotency-Key` | header | yes | string | Required UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

> Request body.

**Content type `application/json`** — schema: object (schema `RepayV2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `repayment_id` | string (schema `RepaymentID`) | yes | Repayment ID | format: "uuid"; example: "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834" |
| `metadata` | object (map of string) (schema `RepaymentMetadata`) | no | Additional repayment information<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `reference_date` | string (schema `ReferenceDate`) | no | Reference date of the installment. Format = YYYY-MM-DD. | format: "date"; example: "2025-04-14" |
| `repayment_amount` | number (schema `RepaymentAmount`) | no | Repayment amount | format: "double"; example: 100 |
| `repayment_date` | string (schema `RepaymentDate`) | no | Repayment date. Format = YYYY-MM-DD. When earlier than the date the payment is processed, it is treated as a backdated payment: the product must have `backdating_enabled`, the date must be within `max_backdating_window_days`, and a `backdating_reason` is required. On success the arrears penalty charged for the days after this date is given back.<br> | format: "date"; example: "2022-06-30" |
| `backdating_reason` | string (schema `BackdatingReason`) | no | Reason a payment is being backdated. Required only when `repayment_date` is a genuine backdate (earlier than the processing date). Case-insensitive. An invalid value returns `ELND2304`.<br><br>The reason is a governance/audit label, not a verified fact — pick the value that best matches the situation, and use `OTHER` when none fits.<br><br>- `RAIL_DELAY`: Payment was made on time, but the payment rail or bank file reporting it reached Pismo later.<br>- `SYSTEM_ERROR`: A technical failure or outage delayed recording a payment that was actually made earlier.<br>- `OPS_CORRECTION`: An operations team is correcting the recorded date of a payment (back-office correction).<br>- `RETRY_WINDOW`: Payment was originally initiated within the expected timeframe but was temporarily unsuccessful (e.g., transient bank, network, or processing failure) and subsequently reprocessed. The payment is backdated to reflect the original intended payment date.<br>- `REINSTATEMENT`: A previously reversed, cancelled, returned, or otherwise invalidated payment is being reinstated and recorded using its original effective payment date to restore the loan to the correct historical state.<br>- `MISAPPLIED_PAYMENT_CORRECTION`: A payment applied to the wrong loan or installment is being corrected and re-applied using its true effective payment date.<br>- `OTHER`: Generic catch-all for a legitimate backdating reason not covered by the specific values above.<br> | enum: ["RAIL_DELAY", "SYSTEM_ERROR", "OPS_CORRECTION", "RETRY_WINDOW", "REINSTATEMENT", "MISAPPLIED_PAYMENT_CORRECTION", "OTHER"]; example: "RAIL_DELAY" |

Example `Register repayment with full amount`:

```json
{
  "repayment_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "repayment_date": "2025-10-24T00:00:00.000Z",
  "repayment_amount": 1000,
  "metadata": {
    "payment_reference": "ref-987654321",
    "additional_information": "Full repayment"
  }
}
```

Example `Register partial repayment`:

```json
{
  "repayment_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "repayment_date": "2025-10-24T00:00:00.000Z",
  "repayment_amount": 500,
  "metadata": {
    "payment_reference": "ref-123456789",
    "additional_information": "Partial repayment"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Repayment registered successfully. | `application/json`: object (schema `RepayV2Result`) |
| 400 | A validation error occurred. | `application/json`: anyOf: object (schema `StandardErrorResponse`), object (schema `StandardAuthorizationErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | number (schema `AuthorizationId`) | no | Authorization ID | format: "int64"; example: 123456789 |
| `installment_amount` | object (schema `InstallmentAmount`) | no | Installment amount |  |
| `minimum_total_payment_delta` | number (schema `MinimumTotalPaymentDelta`) | no | Additional amount added to the repayment to cover the minimum total payment requirement | format: "double"; minimum: 0; example: 43.46 |
| `repaid_amount` | number (schema `RepaidAmount`) | no | Repaid amount | format: "double"; example: 100 |

202 Example `Success Repayment`:

```json
{
  "loan_id": "73e45fd5-759f-4e04-a88a-7172fa948afa",
  "repayment_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "repayment_amount": 1000
}
```

##### Response 400

400 Example `Validation exception`:

```json
{
  "code": "ELND0003",
  "message": "repayment_amount not valid"
}
```

400 Example `Authorization failed`:

```json
{
  "code": "ELND0004",
  "message": "Authorization failed",
  "response_code": "62",
  "denial_code": "IAD"
}
```

400 Example `ELND2300`:

```json
{
  "code": "ELND2300",
  "message": "repayment_date must be less than or equal to current date."
}
```

400 Example `ELND2301`:

```json
{
  "code": "ELND2301",
  "message": "Backdating is not enabled for this product."
}
```

400 Example `ELND2302`:

```json
{
  "code": "ELND2302",
  "message": "repayment_date is older than the maximum backdating window."
}
```

400 Example `ELND2303`:

```json
{
  "code": "ELND2303",
  "message": "Backdating reason is required when the operation is backdated."
}
```

400 Example `ELND2304`:

```json
{
  "code": "ELND2304",
  "message": "Invalid backdating reason."
}
```

400 Example `ELND2305`:

```json
{
  "code": "ELND2305",
  "message": "repayment_date must not be before the loan creation date."
}
```

##### Response 500

500 Example `ELND0001`:

```json
{
  "code": "ELND0001",
  "message": "Unexpected error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ELND0003` | repayment_amount not valid |
| 400 | `ELND0004` | Authorization failed |
| 400 | `ELND2300` | repayment_date must be less than or equal to current date. |
| 400 | `ELND2301` | Backdating is not enabled for this product. |
| 400 | `ELND2302` | repayment_date is older than the maximum backdating window. |
| 400 | `ELND2303` | Backdating reason is required when the operation is backdated. |
| 400 | `ELND2304` | Invalid backdating reason. |
| 400 | `ELND2305` | repayment_date must not be before the loan creation date. |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/RepaymentMetadata -->
### Schema `RepaymentMetadata`

Pointer: `#/components/schemas/RepaymentMetadata`. Type: object (map of string) (schema `RepaymentMetadata`).

> Additional repayment information
>
> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).

<!-- schema: #/components/schemas/InstallmentAmount -->
### Schema `InstallmentAmount`

Pointer: `#/components/schemas/InstallmentAmount`. Type: object (schema `InstallmentAmount`).

> Installment amount

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `max` | integer (schema `MaxValue`) | no | Maximum value | format: "int32"; example: 100 |
| `min` | integer (schema `MinValue`) | no | Minimum value | format: "int32"; example: 10 |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |

<!-- schema: #/components/schemas/StandardAuthorizationErrorResponse -->
### Schema `StandardAuthorizationErrorResponse`

Pointer: `#/components/schemas/StandardAuthorizationErrorResponse`. Type: object (schema `StandardAuthorizationErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `denial_code` | string (schema `AuthorizationDenialCode`) | no | Payment Methods - Denial Code | minLength: 3; maxLength: 5; example: "IAD" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |
| `response_code` | string (schema `AuthorizationResponseCode`) | no | Payment Methods - Response Code | minLength: 2; maxLength: 2; example: "62" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Lending.yaml` | tag `Repayments`: POST /v2/loans/{loanId}/repayment | https://github.com/PismoDevEx/pismo-api-specs | `6667602e6ada2f81…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-elnd` — Error codes: ELND
