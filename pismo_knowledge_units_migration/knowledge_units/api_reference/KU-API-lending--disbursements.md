---
ku_id: KU-API-lending--disbursements
title: 'API reference: Lending — Disbursements'
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
- disburseLoanV2
related_kus:
- KU-ERR-codes-elnd
- KU-EVT-lending-data-events
- KU-LEND-disburse-loan
specification_version: 1.0.0
---

# API reference: Lending — Disbursements

**KU ID:** `KU-API-lending--disbursements` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Disbursements` in `api-specs/Lending.yaml` (“Lending”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Creates the disbursement management features

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/loans/{loanId}/disburse` | `disburseLoanV2` | Disburse loan | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer"}

## Operation contracts

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{loanId}/disburse operationId=disburseLoanV2 -->
### `POST /v2/loans/{loanId}/disburse` — Disburse loan

- **operationId:** `disburseLoanV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Disbursements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Disburse a loan.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `Idempotency-Key` | header | yes | string | Required UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

> Request body.

**Content type `application/json`** — schema: object (schema `DisbursementV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `disbursement_account` | anyOf: object (schema `InternalDisburseAccountV2`), object (schema `ExternalDisburseAccountV2`) | yes |  |  |
| `disbursement_amount` | number (schema `DisbursementAmount`) | no | Disbursement amount | format: "double"; example: 1000 |
| `disbursement_date` | string (schema `DisbursementDate`) | no | Disbursement date. Format = YYYY-MM-DD. | format: "date"; example: "2022-06-30" |
| `disbursement_id` | string (schema `DisbursementID`) | no | Disbursement ID. Required if the number of loan disbursements is greater than 1. | format: "uuid"; example: "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834" |
| `metadata` | object (map of string) (schema `DisbursementV2Metadata`) | no | Additional disbursement information<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

Example `Disburses the loan to an internal Pismo account`:

```json
{
  "disbursement_account": {
    "account_type": "INTERNAL",
    "account_id": 784165
  },
  "disbursement_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "disbursement_date": "2024-10-15T00:00:00.000Z",
  "disbursement_amount": 1000,
  "metadata": {
    "payment_order_id": "po-123456789",
    "payment_order_reference": "ref-987654321"
  }
}
```

Example `Disburses the loan to an external account`:

```json
{
  "disbursement_account": {
    "account_type": "EXTERNAL"
  },
  "disbursement_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "disbursement_date": "2024-10-15T00:00:00.000Z",
  "disbursement_amount": 1000,
  "metadata": {
    "bank_id": "785",
    "bank_account": "123456",
    "additional_information": "Additional information"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Disburse accepted. | `application/json`: object (schema `DisbursementV2Response`) |
| 400 | A validation error occurred. | `application/json`: anyOf: object (schema `StandardErrorResponse`), object (schema `StandardAuthorizationErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | number (schema `AuthorizationId`) | yes | Authorization ID | format: "int64"; example: 123456789 |
| `authorization_tracking_id` | string (schema `AuthorizationTrackingId`) | no | Authorization tracking ID | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |
| `disbursement_amount` | number (schema `DisbursementAmount`) | no | Disbursement amount | format: "double"; example: 1000 |
| `disbursement_id` | string (schema `DisbursementID`) | no | Disbursement ID. Required if the number of loan disbursements is greater than 1. | format: "uuid"; example: "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834" |
| `loan_id` | string (schema `LoanID`) | no | Custom ID for the loan. Must consist of uppercase alphanumeric characters and underscores. | minLength: 0; maxLength: 36; example: "MY_CUSTOM_LOAN_ID" |

202 Example `Success Disbursement`:

```json
{
  "loan_id": "73e45fd5-759f-4e04-a88a-7172fa948afa",
  "authorization_id": 123456789,
  "authorization_tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee",
  "disbursement_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "disbursement_amount": 1000
}
```

##### Response 400

400 Example `Validation exception`:

```json
{
  "code": "ELND0003",
  "message": "disbursement_account.account_type not valid"
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
| 400 | `ELND0003` | disbursement_account.account_type not valid |
| 400 | `ELND0004` | Authorization failed |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-EVT-lending-data-events`, `KU-LEND-disburse-loan`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/InternalDisburseAccountV2 -->
### Schema `InternalDisburseAccountV2`

Pointer: `#/components/schemas/InternalDisburseAccountV2`. Type: object (schema `InternalDisburseAccountV2`).

> Describes disbursement data for internal accounts, where the lender and beneficiary have accounts with the same entity

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 514751581 |
| `account_type` | string (schema `InternalAccountType`) | yes | Account type | enum: ["INTERNAL"]; example: "INTERNAL" |

<!-- schema: #/components/schemas/ExternalDisburseAccountV2 -->
### Schema `ExternalDisburseAccountV2`

Pointer: `#/components/schemas/ExternalDisburseAccountV2`. Type: object (schema `ExternalDisburseAccountV2`).

> Describes disbursement data for external accounts, where the disbursement will be made to an account at a different entity than the lender

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_type` | string (schema `ExternalAccountType`) | yes | External account type | enum: ["EXTERNAL"]; example: "EXTERNAL" |

<!-- schema: #/components/schemas/DisbursementV2Metadata -->
### Schema `DisbursementV2Metadata`

Pointer: `#/components/schemas/DisbursementV2Metadata`. Type: object (map of string) (schema `DisbursementV2Metadata`).

> Additional disbursement information
>
> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).

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
| `api-specs/Lending.yaml` | tag `Disbursements`: POST /v2/loans/{loanId}/disburse | https://github.com/PismoDevEx/pismo-api-specs | `6667602e6ada2f81…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-elnd` — Error codes: ELND
- `KU-EVT-lending-data-events` — Lending events
- `KU-LEND-disburse-loan` — Disburse loans
