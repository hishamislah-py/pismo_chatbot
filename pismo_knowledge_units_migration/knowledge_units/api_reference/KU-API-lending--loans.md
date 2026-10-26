---
ku_id: KU-API-lending--loans
title: 'API reference: Lending — Loans'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- getLoansByAccountIdV2
- cancelAllLoansByAccountV2
- createLoanAdjustmentV2
- retrievePaginatedLoans
- bookLoanV2
- getLoanV2
- cancelLoanV2
- restructureLoan
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CC-lending
- KU-ERR-codes-elnd
- KU-EVT-catalogue-lending
- KU-EVT-catalogue-other-domains
- KU-EVT-lending-data-events
- KU-LEND-book-a-loan
- KU-LEND-disburse-loan
- KU-LEND-manage-loan-repayment-and-settlement
specification_version: 1.0.0
---

# API reference: Lending — Loans

**KU ID:** `KU-API-lending--loans` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 8 operation(s) tagged `Loans` in `api-specs/Lending.yaml` (“Lending”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Creates the core loan management features

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/accounts/{accountId}/loans` | `getLoansByAccountIdV2` | List account loans | no |
| `POST /v2/accounts/{accountId}/loans/cancel` | `cancelAllLoansByAccountV2` | Cancel all loans by account | no |
| `POST /v2/loans/{loanId}/adjustment` | `createLoanAdjustmentV2` | Create loan adjustment | no |
| `GET /v2/loans` | `retrievePaginatedLoans` | List loans | no |
| `POST /v2/loans` | `bookLoanV2` | Book loan | no |
| `GET /v2/loans/{loanId}` | `getLoanV2` | Get loan | no |
| `POST /v2/loans/{loanId}/cancel` | `cancelLoanV2` | Cancel loan | no |
| `POST /v2/loans/{originalLoanId}/restructure` | `restructureLoan` | Restructure a loan | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer"}

## Operation contracts

<!-- op: spec=api-specs/Lending.yaml method=GET path=/v2/accounts/{accountId}/loans operationId=getLoansByAccountIdV2 -->
### `GET /v2/accounts/{accountId}/loans` — List account loans

- **operationId:** `getLoansByAccountIdV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve all loans associated with the specified account.
>
> **Note**: This endpoint requires an [account-specific access token](ref:get-an-account-specific-token-basic-authentication).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | ID of the account the loan belongs to | example: "514751581" |
| `nextCursor` | query | yes | string (schema `NextCursor`) | Next page cursor identifier | example: "NmI5NmNlYzUtZTg1Ni00MjY0LTlkNzctNGY5OGIzNTk4YWM1IzE3NDU5NDY2MTg3NTIjMjAyNS0wNC0yOVQxNzoxMDoxOC43MjY3MTY0Mlo"; example: "99999999-9999-9999-9999-999999999999" |
| `limit` | query | no | integer (schema `Limit`) | Maximum number of items to return per page | format: "int32"; maximum: 50; example: 10; example: 10 |
| `status` | query | no | string (schema `LoanStatus`) | Loan status filter | enum: ["PENDING", "BOOKED", "ACTIVE", "CANCELED", "SETTLED", "RENEGOTIATED"]; example: "ACTIVE"; example: "ACTIVE" |
| `expand` | query | no | boolean | Also retrieve disbursements and repayments? | default: false; example: true |
| `presentValue` | query | no | boolean (schema `BooleanValue`) | Retrieve the present value of the loan? | example: true; example: true |
| `referenceDate` | query | no | string (schema `DateValue`) | Reference date to calculate the present value of the loan | format: "date"; example: "2023-12-31"; example: "2024-06-01" |
| `fromCreatedDate` | query | no | string (schema `DateValue`) | Filter loans created on or after this date (inclusive). Format = YYYY-MM-DD. Invalid format returns 400 Bad Request. Can be used alone to get all loans created from this date onwards, or combined with `toCreatedDate` to filter within a specific date range. | format: "date"; example: "2023-12-31"; example: "2026-05-01" |
| `toCreatedDate` | query | no | string (schema `DateValue`) | Filter loans created on or before this date (inclusive). Format = YYYY-MM-DD. Invalid format returns 400 Bad Request. Can be used alone to get all loans created up to this date, or combined with `fromCreatedDate` to filter within a specific date range. | format: "date"; example: "2023-12-31"; example: "2026-05-31" |
| `fromStartDate` | query | no | string (schema `DateValue`) | Filter loans with start/activation date on or after this date (inclusive). Format = YYYY-MM-DD. Invalid format returns 400 Bad Request. Can be used alone to get all loans with start date from this date onwards, or combined with `toStartDate` to filter within a specific date range. | format: "date"; example: "2023-12-31"; example: "2026-05-01" |
| `toStartDate` | query | no | string (schema `DateValue`) | Filter loans with start/activation date on or before this date (inclusive). Format = YYYY-MM-DD. Invalid format returns 400 Bad Request. Can be used alone to get all loans with start date up to this date, or combined with `fromStartDate` to filter within a specific date range. | format: "date"; example: "2023-12-31"; example: "2026-05-31" |
| `summarizeLoans` | query | no | boolean | When true, returns an aggregated summary across all loans that match the provided filter parameters (pagination is ignored). The response contains only the `loan_summary` field. When absent or false, returns a standard paginated response (`has_next`, `next_cursor`, `items`).<br> | default: false; example: true |
| `includeInsuranceHistory` | query | no | boolean | Indicate `true` to get a response with the insurance history for loans in any state (`ACTIVE`, `CANCELED`, or `SETTLED`). When you use `true` for the query, each insured installment in `repayment_schedule` includes an `insurance_premium_state` field, and the response includes loan-level `insurance_summary` for loans that have an insurance policy. (The field is omitted entirely for uninsured loans). Also the response includes cancelled insurance and its installments. When absent or `false`, the response does not include these insurance-related fields. An invalid boolean value returns 400 with error code `ELND1807`. On the list endpoint, `summarizeLoans=true` takes precedence and this flag is ignored when `summarizeLoans=true`.<br> | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Loans retrieved | `application/json`: oneOf: object (schema `LoansV2PaginatedResponse`), object (schema `LoansV2SummaryResponse`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Paginated response` (Paginated list of loans (default, when summarizeLoans is omitted or false)):

```json
{
  "next_cursor": "NmI5NmNlYzUtZTg1Ni00MjY0LTlkNzctNGY5OGIzNTk4YWM1IzE3NDU5NDY2MTg3NTIjMjAyNS0wNC0yOVQxNzoxMDoxOC43MjY3MTY0Mlo",
  "has_next": true,
  "items": [
    {
      "loan_id": "MY_CUSTOM_LOAN_ID",
      "external_id": "my_external_id",
      "authorization_tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee",
      "status": "ACTIVE",
      "product_id": "2717a296-124a-47cc-b2a1-91e80dc723eb",
      "account_id": 514751582,
      "created_at": "2024-03-15T13:00:00.000+00:00",
      "updated_at": "2024-03-15T13:00:00.000+00:00",
      "start_date": "2022-06-28",
      "loan_amount": 2000,
      "loan_principal_amount": 1800,
      "total_expected_payment_amount": 2052,
      "grace_period_days": 7,
      "days_past_due": 12,
      "original_loan_id": "2717a296-124a-47cc-b2a1-91e80dc723eb",
      "restructure_loan_id": "2717a296-124a-47cc-b2a1-91e80dc723eb",
      "transactions_ids": [
        6354273849
      ],
      "rates": {
        "interest_rate": 12,
        "annual_interest_rate": 12,
        "effective_monthly_cost": 12.7,
        "effective_annual_cost": 319.98
      },
      "total_payable": {
        "principal": 1800,
        "interest": 200,
        "charge": 5,
        "tax": 10,
        "fee": 10,
        "penalty": 27,
        "total": 2052,
        "amount_due": {
          "principal": 1800,
          "interest": 200,
          "charge": 5,
          "tax": 10,
          "fee": 10,
          "penalty": 27,
          "total": 2052
        },
        "arrears": {
          "principal": 0,
          "interest": 0,
          "charge": 0,
          "tax": 0,
          "fee": 0,
          "penalty": 0,
          "total": 0
        }
      },
      "total_paid": {
        "amount_paid": {
          "principal": 0,
          "interest": 0,
          "charge": 0,
          "tax": 0,
          "fee": 0,
          "penalty": 0,
          "total": 0
        }
      },
      "prepayments": [
        {
          "prepayment_id": "73e45fd5-759f-4e04-a88a-7172fa948afa",
          "status": "REGISTERED",
          "settlement_date": "2026-06-15T10:00:00.000+00:00",
          "amount_paid": 1000,
          "penalty_amount_paid": 50,
          "insurance_amount_paid": 0,
          "tax_amount_paid": 0,
          "reduce_option": "INSTALLMENT",
          "new_remaining_total": 4000,
          "created_at": "2026-06-15T10:00:00.000+00:00",
          "updated_at": "2026-06-15T10:00:00.000+00:00"
        }
      ],
      "repayment_schedule": [
        {
          "repayment_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
          "transactions_ids": [
            6354273849
          ],
          "status": "SCHEDULED",
          "period": 1,
          "due_date": "2022-06-28",
          "real_due_date": "2025-06-28",
          "present_value_amount": 100,
          "present_value_discount": 100,
          "amount_due": {
            "principal": 1800,
            "interest": 200,
            "charge": 5,
            "tax": 10,
            "fee": 10,
            "penalty": 27,
            "total": 2052
          },
          "amount_paid": {
            "principal": 0,
            "interest": 0,
            "charge": 0,
            "tax": 0,
            "fee": 0,
            "penalty": 0,
            "total": 0
          },
          "initial_amount": {
            "principal": 1800,
            "interest": 200,
            "charge": 5,
            "tax": 10,
            "fee": 10,
            "penalty": 27,
            "total": 2052
          },
          "insurance": {
            "principal": 15,
            "interest": 2,
            "charge": 1,
            "tax": 1,
            "fee": 1,
            "penalty": 0,
            "total": 20
          },
          "insurance_premium_state": "PAID"
        }
      ],
      "disbursement": {
        "type": "SINGLE",
        "schedule": [
          {
            "id": "54efa995-66f1-4595-9934-5b92222faf37",
            "amount": 300,
            "date": "2025-11-13",
            "disbursement_account": {
              "account_type": "INTERNAL",
              "account_id": 317890964
            },
            "authorization_id": 2422410859,
            "tracking_id": "003b3de8-c321-464c-a3dd-6009b8698325",
            "status": "PAID",
            "transactions_ids": [
              6354273849
            ]
          }
        ]
      },
      "insurance_summary": {
        "insurance_ever_active": true,
        "last_covered_date": "2025-03-20",
        "installment_counts": {
          "paid": 2,
          "canceled": 2,
          "pending": 0
        }
      }
    }
  ]
}
```

200 Example `Summary response` (Aggregated loan summary (when summarizeLoans is true)):

```json
{
  "loan_summary": {
    "loan_count_by_status": {
      "ACTIVE": 3,
      "SETTLED": 2
    },
    "loan_value_by_status": {
      "ACTIVE": 8000,
      "SETTLED": 5000
    },
    "total_loan_count": 5,
    "total_loan_value": 13000,
    "total_outstanding": 8000,
    "total_paid": 5000,
    "total_principal": 10000
  }
}
```

##### Response 400

400 Example `ELND1802`:

```json
{
  "code": "ELND1802",
  "message": "Field fromCreatedDate must be before or equal to toCreatedDate."
}
```

400 Example `ELND1803`:

```json
{
  "code": "ELND1803",
  "message": "Field fromStartDate must be before or equal to toStartDate."
}
```

400 Example `ELND1804`:

```json
{
  "code": "ELND1804",
  "message": "summarizeLoans must be a valid boolean value."
}
```

400 Example `ELND1807`:

```json
{
  "code": "ELND1807",
  "message": "includeInsuranceHistory must be a valid boolean value."
}
```

400 Example `ELND1808`:

```json
{
  "code": "ELND1808",
  "message": "Field fromStartDate and toStartDate date range must not exceed 12 months."
}
```

400 Example `ELND1809`:

```json
{
  "code": "ELND1809",
  "message": "Field fromCreatedDate and toCreatedDate date range must not exceed 12 months."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ELND1802` | Field fromCreatedDate must be before or equal to toCreatedDate. |
| 400 | `ELND1803` | Field fromStartDate must be before or equal to toStartDate. |
| 400 | `ELND1804` | summarizeLoans must be a valid boolean value. |
| 400 | `ELND1807` | includeInsuranceHistory must be a valid boolean value. |
| 400 | `ELND1808` | Field fromStartDate and toStartDate date range must not exceed 12 months. |
| 400 | `ELND1809` | Field fromCreatedDate and toCreatedDate date range must not exceed 12 months. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-LEND-disburse-loan`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/accounts/{accountId}/loans/cancel operationId=cancelAllLoansByAccountV2 -->
### `POST /v2/accounts/{accountId}/loans/cancel` — Cancel all loans by account

- **operationId:** `cancelAllLoansByAccountV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancels all active loans for the specified account
>
> **Note**: This endpoint requires an [account-specific access token](ref:get-an-account-specific-token-basic-authentication).
>
> This endpoint generates [Loan updated](https://developers.pismo.io/events/docs/lending-lending-loan-update-1) events for each canceled loan.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | ID of the account the loan belongs to | example: "514751581" |
| `Idempotency-Key` | header | yes | string | Required UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

> Request body for canceling all loans of an account

**Content type `application/json`** — schema: object (schema `CancelAllLoansV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bring_to_present_value` | boolean | no | Calculate loan balances to present value before cancellation? When true, the system calculates interest and charges up to the cancellation date. | default: false; example: false |

Example `Cancel without present value`:

```json
{
  "bring_to_present_value": false
}
```

Example `Cancel with present value`:

```json
{
  "bring_to_present_value": true
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Cancellation accepted | `application/json`: object (schema `CancelAllLoansV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 403 | Unauthorized access — header account ID does not match path account ID. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `canceled_loans` | array of object (schema `CanceledLoanV2Summary`) | yes | List of canceled loan summaries |  |
| `total_to_be_canceled` | integer | yes | Total number of loans to be canceled | example: 2 |

202 Example `Success`:

```json
{
  "total_to_be_canceled": 2,
  "canceled_loans": [
    {
      "loan_id": "550e8400-e29b-41d4-a716-446655440000",
      "tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee"
    },
    {
      "loan_id": "550e8400-e29b-41d4-a716-446655440001",
      "tracking_id": "5ef098f4-9280-12fe-9310-07d8c133e2ff"
    }
  ]
}
```

##### Response 400

400 Example `ELND2107`:

```json
{
  "code": "ELND2107",
  "message": "Invalid account ID"
}
```

400 Example `ELND0010`:

```json
{
  "code": "ELND0010",
  "message": "Header idempotency-key not passed"
}
```

400 Example `ELND2106`:

```json
{
  "code": "ELND2106",
  "message": "No active loans found for the account."
}
```

##### Response 403

403 Example `ELND0002`:

```json
{
  "code": "ELND0002",
  "message": "Unauthorized access. Invalid credentials."
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
| 400 | `ELND2107` | Invalid account ID |
| 400 | `ELND0010` | Header idempotency-key not passed |
| 400 | `ELND2106` | No active loans found for the account. |
| 403 | `ELND0002` | Unauthorized access. Invalid credentials. |
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-lending-loan-update-1` | https://developers.pismo.io/events/docs/lending-lending-loan-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{loanId}/adjustment operationId=createLoanAdjustmentV2 -->
### `POST /v2/loans/{loanId}/adjustment` — Create loan adjustment

- **operationId:** `createLoanAdjustmentV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create loan adjustment

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `Idempotency-Key` | header | yes | string | Required UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: no

> Request body.

**Content type `application/json`** — schema: object (schema `CreateAdjustmentV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `adjustment_amount` | number (schema `AdjustmentAmount`) | yes | Amount of the adjustment | format: "double"; example: 1000 |
| `loan_balance_impact` | string (schema `LoanBalanceImpact`) | yes | Loan balance impact | enum: ["PRINCIPAL", "INTEREST", "TAX", "PENALTY", "FEE"]; example: "PRINCIPAL" |
| `processing_code` | string | yes | Processing code for the adjustment |  |
| `repayment_id` | string (schema `RepaymentID`) | yes | Repayment ID | format: "uuid"; example: "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Loan adjustment created. | `application/json`: object (schema `AdjustmentPostResponse`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | number (schema `AuthorizationId`) | yes | Authorization ID | format: "int64"; example: 123456789 |
| `idempotency_key` | string (schema `IdempotencyKey`) | yes | UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-EVT-lending-data-events`, `KU-LEND-manage-loan-repayment-and-settlement`.

<!-- op: spec=api-specs/Lending.yaml method=GET path=/v2/loans operationId=retrievePaginatedLoans -->
### `GET /v2/loans` — List loans

- **operationId:** `retrievePaginatedLoans`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List loans

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `nextCursor` | query | yes | string (schema `NextCursor`) | Next page cursor identifier | example: "NmI5NmNlYzUtZTg1Ni00MjY0LTlkNzctNGY5OGIzNTk4YWM1IzE3NDU5NDY2MTg3NTIjMjAyNS0wNC0yOVQxNzoxMDoxOC43MjY3MTY0Mlo"; example: "99999999-9999-9999-9999-999999999999" |
| `limit` | query | no | integer (schema `Limit`) | Maximum number of items to return per page | format: "int32"; maximum: 50; example: 10; example: 10 |
| `status` | query | no | string (schema `LoanStatus`) | Loan status filter | enum: ["PENDING", "BOOKED", "ACTIVE", "CANCELED", "SETTLED", "RENEGOTIATED"]; example: "ACTIVE"; example: "ACTIVE" |
| `loanProductId` | query | no | string (schema `LoanProductID`) | Loan product ID filter | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb"; example: "99999999-9999-9999-9999-999999999999" |
| `accountId` | query | no | string | Restricts results to loans belonging to this Pismo account | example: "514751581" |
| `expand` | query | no | boolean (schema `BooleanValue`) | Include information about scheduled repayments in the response? | example: true; example: true |
| `authorizationId` | query | no | number (schema `AuthorizationId`) | ID of the authorization that originated the loan | format: "int64"; example: 123456789; example: 123456789 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Loan retrieved. | `application/json`: object |
| 400 | Bad request. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean (schema `HasNext`) | no | Does the query have additional items to return? | example: true |
| `next_cursor` | string (schema `NextCursor`) | no | Opaque pagination cursor returned by the API. Pass back exactly as received to retrieve the next page; do not parse or modify it. | example: "NmI5NmNlYzUtZTg1Ni00MjY0LTlkNzctNGY5OGIzNTk4YWM1IzE3NDU5NDY2MTg3NTIjMjAyNS0wNC0yOVQxNzoxMDoxOC43MjY3MTY0Mlo" |
| `items` | array of object (schema `LendingLoanRepaymentResponse`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans operationId=bookLoanV2 -->
### `POST /v2/loans` — Book loan

- **operationId:** `bookLoanV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Books a loan with the configuration set up in the loan product.
>
> This endpoint generates a [Loan booked](https://developers.pismo.io/events/docs/lending-loan-booked-1) event and a [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `BookingV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 514751581 |
| `installment_plan_id` | string (schema `InstallmentPlanId`) | yes | ID of the installment plan | format: "uuid"; example: "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834" |
| `loan_product_id` | string (schema `LoanProductID`) | yes | Loan product ID. Accepts either a lowercase UUID (e.g., "2717a296-124a-47cc-b2a1-91e80dc723eb") or an uppercase alphanumeric string with underscores (e.g., "MY_LOAN_PRODUCT_001"). If not provided during creation, a UUID is auto-generated. | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `number_of_installments` | number (schema `NumberOfInstallments`) | yes | Number of installments | format: "int32" |
| `amount` | number (schema `BookingAmount`) | no | Booking amount | format: "double"; example: 1000 |
| `metadata` | object (map of string) (schema `V2Metadata`) | no | Additional information<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

Example `Book a loan using an installment plan`:

```json
{
  "amount": 2000,
  "account_id": 10483628,
  "loan_product_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "installment_plan_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "number_of_installments": 5,
  "metadata": {
    "external_id": "cf5687d4e834"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Loan booked. | `application/json`: object (schema `LoanIdResponse`) |
| 400 | A validation error occurred. | `application/json`: anyOf: object (schema `StandardErrorResponse`), object (schema `StandardAuthorizationErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `loan_id` | string (schema `LoanID`) | yes | Custom ID for the loan. Must consist of uppercase alphanumeric characters and underscores. | minLength: 0; maxLength: 36; example: "MY_CUSTOM_LOAN_ID" |

202 Example `Success Disbursement`:

```json
{
  "loan_id": "73e45fd5-759f-4e04-a88a-7172fa948afa"
}
```

##### Response 400

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
| 400 | `ELND0004` | Authorization failed |
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-loan-booked-1` | https://developers.pismo.io/events/docs/lending-loan-booked-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-CC-lending`, `KU-EVT-lending-data-events`, `KU-LEND-book-a-loan`.

<!-- op: spec=api-specs/Lending.yaml method=GET path=/v2/loans/{loanId} operationId=getLoanV2 -->
### `GET /v2/loans/{loanId}` — Get loan

- **operationId:** `getLoanV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a loan by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `presentValue` | query | no | boolean (schema `BooleanValue`) | Retrieve the present value of the loan? | example: true; example: true |
| `referenceDate` | query | no | string (schema `DateValue`) | Reference date to calculate the present value of the loan | format: "date"; example: "2023-12-31"; example: "2024-06-01" |
| `includeInsuranceHistory` | query | no | boolean | Indicate `true` to get a response with the insurance history for loans in any state (`ACTIVE`, `CANCELED`, or `SETTLED`). When you use `true` for the query, each insured installment in `repayment_schedule` includes an `insurance_premium_state` field, and the response includes loan-level `insurance_summary` for loans that have an insurance policy. (The field is omitted entirely for uninsured loans). Also the response includes cancelled insurance and its installments. When absent or `false`, the response does not include these insurance-related fields. An invalid boolean value returns 400 with error code `ELND1807`. On the list endpoint, `summarizeLoans=true` takes precedence and this flag is ignored when `summarizeLoans=true`.<br> | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Loan retrieved. | `application/json`: object (schema `LendingLoanRepaymentResponse`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 514751581 |
| `created_at` | string (schema `LoanCreatedAt`) | yes | Loan created date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ | format: "date-time"; example: "2026-09-03T17:58:35.520Z" |
| `loan_amount` | number (schema `LoanAmount`) | yes | Loan amount | format: "double"; example: 2000 |
| `loan_id` | string (schema `LoanID`) | yes | Custom ID for the loan. Must consist of uppercase alphanumeric characters and underscores. | minLength: 0; maxLength: 36; example: "MY_CUSTOM_LOAN_ID" |
| `product_id` | string (schema `LoanProductID`) | yes | Loan product ID. Accepts either a lowercase UUID (e.g., "2717a296-124a-47cc-b2a1-91e80dc723eb") or an uppercase alphanumeric string with underscores (e.g., "MY_LOAN_PRODUCT_001"). If not provided during creation, a UUID is auto-generated. | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `start_date` | string (schema `FirstActiveStartDate`) | yes | Date loan was first active. Format = YYYY-MM-DD. | format: "date"; example: "2022-06-28" |
| `status` | string (schema `LoanStatus`) | yes | Loan status<br><br>`PENDING`-The loan has been created but has not yet been booked. Terms may still be under review or awaiting confirmation.<br><br>`BOOKED`-The loan has been approved and booked. The payment schedule is confirmed and the loan is ready for disbursement.<br><br>`ACTIVE`-The loan is active and in progress. Funds have been disbursed and the borrower is expected to make repayments according to the agreed schedule.<br><br>`CANCELED`-A repayment is no longer expected to be paid.<br><br>`SETTLED`-The loan has been fully repaid and is closed. No further repayments are expected.<br><br>`RENEGOTIATED`-The original loan terms have been modified after booking, typically due to a change in repayment conditions or borrower circumstances.<br> | enum: ["PENDING", "BOOKED", "ACTIVE", "CANCELED", "SETTLED", "RENEGOTIATED"]; example: "ACTIVE" |
| `total_payable` | object (schema `TotalPayable`) | yes |  |  |
| `total_paid` | object (schema `TotalPaid`) | no | Consolidated loan-level amount that has already been paid across all repayments, aggregated server-side and broken down by component under `amount_paid`. Removes the need to total all repayment-level objects. Loan progress can be derived from `total_paid.amount_paid.total` versus `total_payable.total`. |  |
| `updated_at` | string (schema `LoanUpdatedAt`) | yes | Loan last updated date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2024-03-15T13:00:00.000+00:00" |
| `authorization_tracking_id` | string (schema `AuthorizationTrackingId`) | no | Authorization tracking ID | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |
| `days_past_due` | integer (schema `DaysPastDue`) | no | Number of calendar days elapsed since the real due date of the loan's most overdue repayment. Computed from repayments currently in a past due or overdue status. A value of `0` indicates the loan has no past due or overdue repayments. | format: "int32"; minimum: 0; example: 12 |
| `disbursement` | object (schema `LoanDisbursement`) | no | Disbursement details for the loan. The consolidated fields `total_disbursed_amount`, `remaining_to_disburse_amount` and `can_disburse_more` are present only for `MULTIPLE` disbursement loans and are omitted for `SINGLE` and `NONE`. |  |
| `external_id` | string (schema `ExternalID`) | no | External ID | maxLength: 50; example: "my_external_id" |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of calendar days after the installment due date during which late fees and delinquency are not applied. A value of `0` or omitted indicates no grace period. | format: "int32"; minimum: 0; maximum: 365; example: 7 |
| `insurance_summary` | object (schema `LoanInsuranceSummary`) | no | Loan-level insurance history summary. Returned only when `includeInsuranceHistory=true` and the loan has an insurance policy. It is omitted entirely for loans that were never insured. Per-installment `insurance_premium_state` values remain the source of truth.<br> |  |
| `loan_principal_amount` | number (schema `LoanPrincipalAmount`) | no | Principal portion of the loan amount, excluding interest, fees, taxes, and penalty | format: "double"; example: 1800 |
| `original_loan_id` | string (schema `OriginalLoanID`) | no | Original loan ID. When a loan is created from a restructure, this field contains the ID of the original loan that was restructured. | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `prepayments` | array of object (schema `PrepaymentSummaryV2Response`) | no | List of prepayments registered for this loan. Only populated when the loan aggregate is fully expanded (single GET, or paginated GET with `expand=true`). Only prepayments in `REGISTERED` status are returned. |  |
| `rates` | object (schema `LoansRates`) | no | Loan rates including annual interest rate and effective annual and monthly costs |  |
| `repayment_schedule` | array of object | no | Repayment schedule installments for this loan |  |
| `repayment_schedule[].repayment_id` | string (schema `RepaymentID`) | no | Repayment ID | format: "uuid"; example: "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834" |
| `repayment_schedule[].transactions_ids` | array of integer (schema `TransactionsIDs`) | no | List of transaction IDs | example: [6354273849, 982393773]; items.format: "int64" |
| `repayment_schedule[].status` | string (schema `InstallmentStatus`) | no | Current lifecycle status of a loan installment.<br><br>**Normal lifecycle:**<br>`SCHEDULED` → (due date passes) → `PAST_DUE` → (penalty accrual window closes) → `OVERDUE` → (payment received) → `PAID`<br><br>**Grace period lifecycle:**<br>`SCHEDULED` → `IN_GRACE_PERIOD` → (grace period expires) → `PAST_DUE` → `OVERDUE` → `PAID`<br>`SCHEDULED` → `IN_GRACE_PERIOD` → (payment within grace period) → `PAID_WITHIN_GRACE`<br><br>**Partial payment lifecycle:**<br>`PAST_DUE` → (partial payment made) → `PARTIALLY_PAID` → (due date passes) → `PAST_DUE_PARTIALLY_PAID` → (accrual window closes) → `OVERDUE_PARTIALLY_PAID` → (remaining balance paid) → `PAID`<br>`IN_GRACE_PERIOD` → (partial payment made) → `PARTIALLY_PAID_IN_GRACE_PERIOD` → (grace period expires) → `PARTIALLY_PAID`<br><br>**`PAST_DUE` vs `OVERDUE`:**<br>- `PAST_DUE`: the due date has passed and daily penalty charges are actively accruing.<br>- `OVERDUE`: the penalty accrual window has closed (configurable per loan product). No further charges accrue; the installment balance is frozen.<br><br>**`PAST_DUE_PARTIALLY_PAID` vs `OVERDUE_PARTIALLY_PAID`:**<br>- `PAST_DUE_PARTIALLY_PAID`: a partial payment has been received, the due date has passed, and daily penalty charges are still accruing on the remaining balance.<br>- `OVERDUE_PARTIALLY_PAID`: a partial payment has been received and the penalty accrual window has closed. No further charges accrue on the remaining balance.<br><br>**Pending payment suffixes (`*_PENDING_PAYMENT`):**<br>When a group payment or prepayment is initiated, the installment moves to a `*_PENDING_PAYMENT` variant<br>(for example, `PAST_DUE` → `PAST_DUE_PENDING_PAYMENT`). If the payment is confirmed the installment is settled;<br>if it expires the installment reverts to its base status. Penalty accrual follows the base status while a payment<br>is pending: `PAST_DUE_*` variants keep accruing on the remaining balance, `OVERDUE_*` variants do not.<br><br>Pending-payment variants of partially paid installments:<br>- `PARTIALLY_PAID_PENDING_PAYMENT`: a group payment is pending on a partially paid installment (outside the grace-period and past-due contexts).<br>- `PAST_DUE_PARTIALLY_PAID_PENDING_PAYMENT`: a group payment is pending on a `PAST_DUE_PARTIALLY_PAID` installment; penalty charges keep accruing until confirmation. Moves to `OVERDUE_PARTIALLY_PAID_PENDING_PAYMENT` when the accrual window closes, reverts to `PAST_DUE_PARTIALLY_PAID` if the payment expires, or settles to `PAID` once confirmed.<br>- `OVERDUE_PARTIALLY_PAID_PENDING_PAYMENT`: a group payment is pending on an `OVERDUE_PARTIALLY_PAID` installment; no further charges accrue. Reverts to `OVERDUE_PARTIALLY_PAID` if the payment expires, or settles to `PAID` once confirmed.<br>- `PARTIALLY_PAID_IN_GRACE_PERIOD_PENDING_PAYMENT`: a group payment is pending on a `PARTIALLY_PAID_IN_GRACE_PERIOD` installment. Moves to `PAST_DUE_PENDING_PAYMENT` when the grace period expires, or reverts to `PARTIALLY_PAID_IN_GRACE_PERIOD` if the payment expires.<br> | enum: ["PENDING", "PROCESSING", "SCHEDULED", "PAST_DUE", "PAID", "PARTIALLY_PAID", "CANCELED", "PENDING_PAYMENT", "PAST_DUE_PENDING_PAYMENT", "ACTIVE", "OVERDUE", "OVERDUE_PENDING_PAYMENT", "IN_GRACE_PERIOD", "IN_GRACE_PERIOD_PENDING_PAYMENT", "PARTIALLY_PAID_IN_GRACE_PERIOD", "PAID_WITHIN_GRACE", "PARTIALLY_PAID_PENDING_PAYMENT", "PAST_DUE_PARTIALLY_PAID", "OVERDUE_PARTIALLY_PAID", "PAST_DUE_PARTIALLY_PAID_PENDING_PAYMENT", "OVERDUE_PARTIALLY_PAID_PENDING_PAYMENT", "PARTIALLY_PAID_IN_GRACE_PERIOD_PENDING_PAYMENT"]; example: "SCHEDULED" |
| `repayment_schedule[].period` | integer (schema `Period`) | no | Period | format: "int32"; example: 1 |
| `repayment_schedule[].due_date` | string (schema `LoanPaymentDueDate`) | no | Loan payment due date. Format = YYYY-MM-DD. | format: "date"; example: "2022-06-28" |
| `repayment_schedule[].real_due_date` | string (schema `RealDueDate`) | no | Adjusted due date. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-28" |
| `repayment_schedule[].present_value_amount` | number (schema `PresentValueAmount`) | no | Amount of calculated loan present value | format: "double"; example: 100 |
| `repayment_schedule[].present_value_discount` | number (schema `PresentValueDiscount`) | no |  | format: "double"; example: 100 |
| `repayment_schedule[].amount_due` | object | no | Amount due for the repayment |  |
| `repayment_schedule[].amount_due.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `repayment_schedule[].amount_due.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `repayment_schedule[].amount_due.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `repayment_schedule[].amount_due.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `repayment_schedule[].amount_due.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `repayment_schedule[].amount_due.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `repayment_schedule[].amount_due.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `repayment_schedule[].amount_paid` | object | no | Amount paid for the repayment |  |
| `repayment_schedule[].amount_paid.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `repayment_schedule[].amount_paid.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `repayment_schedule[].amount_paid.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `repayment_schedule[].amount_paid.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `repayment_schedule[].amount_paid.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `repayment_schedule[].amount_paid.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `repayment_schedule[].amount_paid.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `repayment_schedule[].initial_amount` | object | no | Initial amount for the repayment |  |
| `repayment_schedule[].initial_amount.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `repayment_schedule[].initial_amount.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `repayment_schedule[].initial_amount.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `repayment_schedule[].initial_amount.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `repayment_schedule[].initial_amount.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `repayment_schedule[].initial_amount.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `repayment_schedule[].initial_amount.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `repayment_schedule[].insurance` | object | no | Insurance premium amount for the repayment. Present only for insured installments. |  |
| `repayment_schedule[].insurance.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `repayment_schedule[].insurance.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `repayment_schedule[].insurance.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `repayment_schedule[].insurance.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `repayment_schedule[].insurance.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `repayment_schedule[].insurance.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `repayment_schedule[].insurance.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `repayment_schedule[].insurance_premium_state` | string (schema `InsurancePremiumState`) | no | Derived state of an installment's insurance premium. Present only when `includeInsuranceHistory=true` and the installment belongs to an insured loan. The platform reads the information from the current installment status (it is not persisted). For uninsured loans and for installments with no linked insurance record you do not see this state.<br><br>`PAID` - The insurance premium was collected. The installment status is settled (`PAID` or `PAID_WITHIN_GRACE`).<br>`CANCELED` - The insurance was canceled and the premium was never collected (installment status `CANCELED`). Covers both cancellation before the first premium and mid-plan cancellation of later installments.<br>`PENDING` - The premium is still awaiting collection (includes the `*_PENDING_PAYMENT` statuses).<br> | enum: ["PAID", "CANCELED", "PENDING"]; example: "PAID" |
| `restructure_loan_id` | string (schema `RestructureLoanID`) | no | Restructure loan ID. When a loan has been restructured, this field contains the ID of the new loan created from the restructure. | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `total_expected_payment_amount` | number (schema `TotalExpectedPaymentAmount`) | no | Total expected payment amount for the loan including principal, interest, fees, and penalty (if applied) | format: "double"; example: 1100 |
| `transactions_ids` | array of integer (schema `TransactionsIDs`) | no | List of transaction IDs | example: [6354273849, 982393773]; items.format: "int64" |

200 Example `example`:

```json
{
  "loan_id": "a1b2c3d4-0004-0004-0004-000000000004",
  "external_id": "my_external_id",
  "authorization_tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee",
  "status": "CANCELED",
  "product_id": "2717a296-124a-47cc-b2a1-91e80dc723eb",
  "account_id": 514751584,
  "created_at": "2024-12-20T13:00:00.000+00:00",
  "updated_at": "2025-03-20T13:00:00.000+00:00",
  "start_date": "2024-12-20",
  "loan_amount": 2000,
  "loan_principal_amount": 1800,
  "total_expected_payment_amount": 2000,
  "grace_period_days": 7,
  "days_past_due": 0,
  "rates": {
    "interest_rate": 12,
    "annual_interest_rate": 12,
    "effective_monthly_cost": 12.7,
    "effective_annual_cost": 319.98
  },
  "total_payable": {
    "principal": 0,
    "interest": 0,
    "charge": 0,
    "tax": 0,
    "fee": 0,
    "penalty": 0,
    "total": 0,
    "amount_due": {
      "principal": 0,
      "interest": 0,
      "charge": 0,
      "tax": 0,
      "fee": 0,
      "penalty": 0,
      "total": 0
    },
    "arrears": {
      "principal": 0,
      "interest": 0,
      "charge": 0,
      "tax": 0,
      "fee": 0,
      "penalty": 0,
      "total": 0
    }
  },
  "transactions_ids": [
    6354273849,
    6354273905
  ],
  "repayment_schedule": [
    {
      "repayment_id": "49e5c088-8dc6-41d3-98a4-6930e066d41e",
      "period": 1,
      "status": "PAID",
      "due_date": "2025-01-10",
      "transactions_ids": [
        6354273850
      ],
      "real_due_date": "2025-01-10",
      "present_value_amount": 500,
      "present_value_discount": 0,
      "amount_due": {
        "principal": 0,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 0
      },
      "amount_paid": {
        "principal": 450,
        "interest": 50,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 500
      },
      "initial_amount": {
        "principal": 450,
        "interest": 50,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 500
      },
      "insurance": {
        "principal": 5,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 5
      },
      "insurance_premium_state": "PAID"
    },
    {
      "repayment_id": "92887f97-f3d6-488d-8d86-d4e201d25697",
      "period": 2,
      "status": "PAID",
      "due_date": "2025-02-10",
      "transactions_ids": [
        6354273851
      ],
      "real_due_date": "2025-02-10",
      "present_value_amount": 500,
      "present_value_discount": 0,
      "amount_due": {
        "principal": 0,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 0
      },
      "amount_paid": {
        "principal": 450,
        "interest": 50,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 500
      },
      "initial_amount": {
        "principal": 450,
        "interest": 50,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 500
      },
      "insurance": {
        "principal": 5,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 5
      },
      "insurance_premium_state": "PAID"
    },
    {
      "repayment_id": "7c8d6ceb-a678-4800-97bc-8977776ad942",
      "period": 3,
      "status": "CANCELED",
      "due_date": "2025-03-10",
      "transactions_ids": [
        6354273906
      ],
      "real_due_date": "2025-03-10",
      "present_value_amount": 500,
      "present_value_discount": 0,
      "amount_due": {
        "principal": 0,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 0
      },
      "amount_paid": {
        "principal": 0,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 0
      },
      "initial_amount": {
        "principal": 450,
        "interest": 50,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 500
      },
      "insurance": {
        "principal": 5,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 5
      },
      "insurance_premium_state": "CANCELED"
    },
    {
      "repayment_id": "3a4ebacd-5481-422e-81aa-a9b0aaded866",
      "period": 4,
      "status": "CANCELED",
      "due_date": "2025-04-10",
      "transactions_ids": [
        6354273907
      ],
      "real_due_date": "2025-04-10",
      "present_value_amount": 500,
      "present_value_discount": 0,
      "amount_due": {
        "principal": 0,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 0
      },
      "amount_paid": {
        "principal": 0,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 0
      },
      "initial_amount": {
        "principal": 450,
        "interest": 50,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 500
      },
      "insurance": {
        "principal": 5,
        "interest": 0,
        "charge": 0,
        "tax": 0,
        "fee": 0,
        "penalty": 0,
        "total": 5
      },
      "insurance_premium_state": "CANCELED"
    }
  ],
  "insurance_summary": {
    "insurance_ever_active": true,
    "last_covered_date": "2025-03-20",
    "installment_counts": {
      "paid": 2,
      "canceled": 2,
      "pending": 0
    }
  }
}
```

##### Response 400

400 Example `{header field} not passed`:

```json
{
  "code": "ELND0002",
  "message": "{header field} not passed"
}
```

400 Example `{path variable} not passed`:

```json
{
  "code": "ELND0002",
  "message": "{path variable} not passed"
}
```

400 Example `{body field} not passed`:

```json
{
  "code": "ELND0002",
  "message": "{body field} not passed"
}
```

400 Example `{related data} not found`:

```json
{
  "code": "ELND0005",
  "message": "{related data} not found"
}
```

400 Example `{body field} not valid`:

```json
{
  "code": "ELND0003",
  "message": "{body field} not valid"
}
```

400 Example `ELND1807`:

```json
{
  "code": "ELND1807",
  "message": "includeInsuranceHistory must be a valid boolean value"
}
```

##### Response 404

404 Example `ELND0005`:

```json
{
  "code": "ELND0005",
  "message": "Loan not found"
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
| 400 | `ELND0002` | {header field} not passed |
| 400 | `ELND0005` | {related data} not found |
| 400 | `ELND0003` | {body field} not valid |
| 400 | `ELND1807` | includeInsuranceHistory must be a valid boolean value |
| 404 | `ELND0005` | Loan not found |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LEND-book-a-loan`, `KU-LEND-disburse-loan`, `KU-LEND-manage-loan-repayment-and-settlement`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{loanId}/cancel operationId=cancelLoanV2 -->
### `POST /v2/loans/{loanId}/cancel` — Cancel loan

- **operationId:** `cancelLoanV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancels a loan.
>
> This endpoint generates a [Loan updated](https://developers.pismo.io/events/docs/lending-lending-loan-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `Idempotency-Key` | header | yes | string | Required UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

> Request body for loan cancellation.

**Content type `application/json`** — schema: object (schema `CancelLoanV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | Tracking ID | format: "uuid"; example: "003b3de8-c321-464c-a3dd-6009b8698325" |
| `metadata` | object (map of string) (schema `CancelLoanV2Metadata`) | no | Additional loan cancellation information<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `processing_code` | object (schema `LoanCancellationProcessingCodes`) | no | Define processing codes for each operation during the loan cancellation. |  |
| `refund_paid_repayments` | boolean (schema `RefundPaidRepayments`) | no | Refund paid repayments upon loan cancellation? | default: false; example: true |

Example `Cancels the loan`:

```json
{
  "tracking_id": "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834",
  "processing_code": {
    "booking": "7DJ8L",
    "repayment": "I1I7J",
    "penalty_waiver": "80Y39"
  },
  "metadata": {
    "cancellation_reason": "Write-off"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Cancellation accepted | `application/json`: object (schema `CancelLoanV2Response`) |
| 400 | A validation error occurred. | `application/json`: anyOf: object (schema `StandardErrorResponse`), object (schema `StandardAuthorizationErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `canceled_loan_id` | string (schema `LoanID`) | yes | Custom ID for the loan. Must consist of uppercase alphanumeric characters and underscores. | minLength: 0; maxLength: 36; example: "MY_CUSTOM_LOAN_ID" |
| `reversal_authorization_id` | number (schema `AuthorizationId`) | yes | Authorization ID | format: "int64"; example: 123456789 |
| `reversal_tracking_id` | string (schema `AuthorizationTrackingId`) | yes | Authorization tracking ID | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

202 Example `Success Cancellation`:

```json
{
  "canceled_loan_id": "73e45fd5-759f-4e04-a88a-7172fa948afa",
  "reversal_authorization_id": 123456789,
  "reversal_tracking_id": "4df987e3-8179-11ed-8209-06c7b022d1ee"
}
```

##### Response 400

400 Example `Validation exception`:

```json
{
  "code": "ELND0010",
  "message": "Header Idempotency-Key not passed"
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
| 400 | `ELND0010` | Header Idempotency-Key not passed |
| 400 | `ELND0004` | Authorization failed |
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-lending-loan-update-1` | https://developers.pismo.io/events/docs/lending-lending-loan-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-lending-data-events`, `KU-LEND-manage-loan-repayment-and-settlement`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{originalLoanId}/restructure operationId=restructureLoan -->
### `POST /v2/loans/{originalLoanId}/restructure` — Restructure a loan

- **operationId:** `restructureLoan`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Loans`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Restructures an existing loan based on provided details.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `originalLoanId` | path | yes | string | The ID of the original loan to restructure | format: "uuid" |
| `Idempotency-Key` | header | yes | string | Required UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `installment_plan_id` | string | yes | Installment plan ID |  |
| `loan_product_id` | string | yes | Loan product ID |  |
| `number_of_installments` | integer | yes | Number of installments |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Restructure request accepted. Processing is asynchronous, so the new loan is not returned. The original loan transitions to `RENEGOTIATED`; retrieve it and read its `restructure_loan_id` to obtain the new loan ID. | `application/json`: object |
| 400 | Invalid request. |  |
| 500 | Internal Server Error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string | no | Tracking ID for the asynchronous restructure processing. Matches the idempotency key sent in the request. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LEND-manage-loan-repayment-and-settlement`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |

<!-- schema: #/components/schemas/CanceledLoanV2Summary -->
### Schema `CanceledLoanV2Summary`

Pointer: `#/components/schemas/CanceledLoanV2Summary`. Type: object (schema `CanceledLoanV2Summary`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `loan_id` | string | yes | Loan ID | example: "550e8400-e29b-41d4-a716-446655440000" |
| `tracking_id` | string | yes | Authorization tracking ID for the cancellation | example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

<!-- schema: #/components/schemas/LendingLoanRepaymentResponse -->
### Schema `LendingLoanRepaymentResponse`

Pointer: `#/components/schemas/LendingLoanRepaymentResponse`. Type: object (schema `LendingLoanRepaymentResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 514751581 |
| `created_at` | string (schema `LoanCreatedAt`) | yes | Loan created date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ | format: "date-time"; example: "2026-09-03T17:58:35.520Z" |
| `loan_amount` | number (schema `LoanAmount`) | yes | Loan amount | format: "double"; example: 2000 |
| `loan_id` | string (schema `LoanID`) | yes | Custom ID for the loan. Must consist of uppercase alphanumeric characters and underscores. | minLength: 0; maxLength: 36; example: "MY_CUSTOM_LOAN_ID" |
| `product_id` | string (schema `LoanProductID`) | yes | Loan product ID. Accepts either a lowercase UUID (e.g., "2717a296-124a-47cc-b2a1-91e80dc723eb") or an uppercase alphanumeric string with underscores (e.g., "MY_LOAN_PRODUCT_001"). If not provided during creation, a UUID is auto-generated. | pattern: "^([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\|[A-Z0-9_]{1,80})$"; maxLength: 80; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `start_date` | string (schema `FirstActiveStartDate`) | yes | Date loan was first active. Format = YYYY-MM-DD. | format: "date"; example: "2022-06-28" |
| `status` | string (schema `LoanStatus`) | yes | Loan status<br><br>`PENDING`-The loan has been created but has not yet been booked. Terms may still be under review or awaiting confirmation.<br><br>`BOOKED`-The loan has been approved and booked. The payment schedule is confirmed and the loan is ready for disbursement.<br><br>`ACTIVE`-The loan is active and in progress. Funds have been disbursed and the borrower is expected to make repayments according to the agreed schedule.<br><br>`CANCELED`-A repayment is no longer expected to be paid.<br><br>`SETTLED`-The loan has been fully repaid and is closed. No further repayments are expected.<br><br>`RENEGOTIATED`-The original loan terms have been modified after booking, typically due to a change in repayment conditions or borrower circumstances.<br> | enum: ["PENDING", "BOOKED", "ACTIVE", "CANCELED", "SETTLED", "RENEGOTIATED"]; example: "ACTIVE" |
| `total_payable` | object (schema `TotalPayable`) | yes |  |  |
| `total_paid` | object (schema `TotalPaid`) | no | Consolidated loan-level amount that has already been paid across all repayments, aggregated server-side and broken down by component under `amount_paid`. Removes the need to total all repayment-level objects. Loan progress can be derived from `total_paid.amount_paid.total` versus `total_payable.total`. |  |
| `updated_at` | string (schema `LoanUpdatedAt`) | yes | Loan last updated date in UTC. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2024-03-15T13:00:00.000+00:00" |
| `authorization_tracking_id` | string (schema `AuthorizationTrackingId`) | no | Authorization tracking ID | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |
| `days_past_due` | integer (schema `DaysPastDue`) | no | Number of calendar days elapsed since the real due date of the loan's most overdue repayment. Computed from repayments currently in a past due or overdue status. A value of `0` indicates the loan has no past due or overdue repayments. | format: "int32"; minimum: 0; example: 12 |
| `disbursement` | object (schema `LoanDisbursement`) | no | Disbursement details for the loan. The consolidated fields `total_disbursed_amount`, `remaining_to_disburse_amount` and `can_disburse_more` are present only for `MULTIPLE` disbursement loans and are omitted for `SINGLE` and `NONE`. |  |
| `external_id` | string (schema `ExternalID`) | no | External ID | maxLength: 50; example: "my_external_id" |
| `grace_period_days` | integer (schema `GracePeriodDays`) | no | Number of calendar days after the installment due date during which late fees and delinquency are not applied. A value of `0` or omitted indicates no grace period. | format: "int32"; minimum: 0; maximum: 365; example: 7 |
| `insurance_summary` | object (schema `LoanInsuranceSummary`) | no | Loan-level insurance history summary. Returned only when `includeInsuranceHistory=true` and the loan has an insurance policy. It is omitted entirely for loans that were never insured. Per-installment `insurance_premium_state` values remain the source of truth.<br> |  |
| `loan_principal_amount` | number (schema `LoanPrincipalAmount`) | no | Principal portion of the loan amount, excluding interest, fees, taxes, and penalty | format: "double"; example: 1800 |
| `original_loan_id` | string (schema `OriginalLoanID`) | no | Original loan ID. When a loan is created from a restructure, this field contains the ID of the original loan that was restructured. | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `prepayments` | array of object (schema `PrepaymentSummaryV2Response`) | no | List of prepayments registered for this loan. Only populated when the loan aggregate is fully expanded (single GET, or paginated GET with `expand=true`). Only prepayments in `REGISTERED` status are returned. |  |
| `rates` | object (schema `LoansRates`) | no | Loan rates including annual interest rate and effective annual and monthly costs |  |
| `repayment_schedule` | array of object | no | Repayment schedule installments for this loan |  |
| `repayment_schedule[].repayment_id` | string (schema `RepaymentID`) | no | Repayment ID | format: "uuid"; example: "5c075cc6-8dc2-4fe6-9ed7-cf5687d4e834" |
| `repayment_schedule[].transactions_ids` | array of integer (schema `TransactionsIDs`) | no | List of transaction IDs | example: [6354273849, 982393773]; items.format: "int64" |
| `repayment_schedule[].status` | string (schema `InstallmentStatus`) | no | Current lifecycle status of a loan installment.<br><br>**Normal lifecycle:**<br>`SCHEDULED` → (due date passes) → `PAST_DUE` → (penalty accrual window closes) → `OVERDUE` → (payment received) → `PAID`<br><br>**Grace period lifecycle:**<br>`SCHEDULED` → `IN_GRACE_PERIOD` → (grace period expires) → `PAST_DUE` → `OVERDUE` → `PAID`<br>`SCHEDULED` → `IN_GRACE_PERIOD` → (payment within grace period) → `PAID_WITHIN_GRACE`<br><br>**Partial payment lifecycle:**<br>`PAST_DUE` → (partial payment made) → `PARTIALLY_PAID` → (due date passes) → `PAST_DUE_PARTIALLY_PAID` → (accrual window closes) → `OVERDUE_PARTIALLY_PAID` → (remaining balance paid) → `PAID`<br>`IN_GRACE_PERIOD` → (partial payment made) → `PARTIALLY_PAID_IN_GRACE_PERIOD` → (grace period expires) → `PARTIALLY_PAID`<br><br>**`PAST_DUE` vs `OVERDUE`:**<br>- `PAST_DUE`: the due date has passed and daily penalty charges are actively accruing.<br>- `OVERDUE`: the penalty accrual window has closed (configurable per loan product). No further charges accrue; the installment balance is frozen.<br><br>**`PAST_DUE_PARTIALLY_PAID` vs `OVERDUE_PARTIALLY_PAID`:**<br>- `PAST_DUE_PARTIALLY_PAID`: a partial payment has been received, the due date has passed, and daily penalty charges are still accruing on the remaining balance.<br>- `OVERDUE_PARTIALLY_PAID`: a partial payment has been received and the penalty accrual window has closed. No further charges accrue on the remaining balance.<br><br>**Pending payment suffixes (`*_PENDING_PAYMENT`):**<br>When a group payment or prepayment is initiated, the installment moves to a `*_PENDING_PAYMENT` variant<br>(for example, `PAST_DUE` → `PAST_DUE_PENDING_PAYMENT`). If the payment is confirmed the installment is settled;<br>if it expires the installment reverts to its base status. Penalty accrual follows the base status while a payment<br>is pending: `PAST_DUE_*` variants keep accruing on the remaining balance, `OVERDUE_*` variants do not.<br><br>Pending-payment variants of partially paid installments:<br>- `PARTIALLY_PAID_PENDING_PAYMENT`: a group payment is pending on a partially paid installment (outside the grace-period and past-due contexts).<br>- `PAST_DUE_PARTIALLY_PAID_PENDING_PAYMENT`: a group payment is pending on a `PAST_DUE_PARTIALLY_PAID` installment; penalty charges keep accruing until confirmation. Moves to `OVERDUE_PARTIALLY_PAID_PENDING_PAYMENT` when the accrual window closes, reverts to `PAST_DUE_PARTIALLY_PAID` if the payment expires, or settles to `PAID` once confirmed.<br>- `OVERDUE_PARTIALLY_PAID_PENDING_PAYMENT`: a group payment is pending on an `OVERDUE_PARTIALLY_PAID` installment; no further charges accrue. Reverts to `OVERDUE_PARTIALLY_PAID` if the payment expires, or settles to `PAID` once confirmed.<br>- `PARTIALLY_PAID_IN_GRACE_PERIOD_PENDING_PAYMENT`: a group payment is pending on a `PARTIALLY_PAID_IN_GRACE_PERIOD` installment. Moves to `PAST_DUE_PENDING_PAYMENT` when the grace period expires, or reverts to `PARTIALLY_PAID_IN_GRACE_PERIOD` if the payment expires.<br> | enum: ["PENDING", "PROCESSING", "SCHEDULED", "PAST_DUE", "PAID", "PARTIALLY_PAID", "CANCELED", "PENDING_PAYMENT", "PAST_DUE_PENDING_PAYMENT", "ACTIVE", "OVERDUE", "OVERDUE_PENDING_PAYMENT", "IN_GRACE_PERIOD", "IN_GRACE_PERIOD_PENDING_PAYMENT", "PARTIALLY_PAID_IN_GRACE_PERIOD", "PAID_WITHIN_GRACE", "PARTIALLY_PAID_PENDING_PAYMENT", "PAST_DUE_PARTIALLY_PAID", "OVERDUE_PARTIALLY_PAID", "PAST_DUE_PARTIALLY_PAID_PENDING_PAYMENT", "OVERDUE_PARTIALLY_PAID_PENDING_PAYMENT", "PARTIALLY_PAID_IN_GRACE_PERIOD_PENDING_PAYMENT"]; example: "SCHEDULED" |
| `repayment_schedule[].period` | integer (schema `Period`) | no | Period | format: "int32"; example: 1 |
| `repayment_schedule[].due_date` | string (schema `LoanPaymentDueDate`) | no | Loan payment due date. Format = YYYY-MM-DD. | format: "date"; example: "2022-06-28" |
| `repayment_schedule[].real_due_date` | string (schema `RealDueDate`) | no | Adjusted due date. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-28" |
| `repayment_schedule[].present_value_amount` | number (schema `PresentValueAmount`) | no | Amount of calculated loan present value | format: "double"; example: 100 |
| `repayment_schedule[].present_value_discount` | number (schema `PresentValueDiscount`) | no |  | format: "double"; example: 100 |
| `repayment_schedule[].amount_due` | object | no | Amount due for the repayment |  |
| `repayment_schedule[].amount_due.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `repayment_schedule[].amount_due.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `repayment_schedule[].amount_due.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `repayment_schedule[].amount_due.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `repayment_schedule[].amount_due.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `repayment_schedule[].amount_due.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `repayment_schedule[].amount_due.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `repayment_schedule[].amount_paid` | object | no | Amount paid for the repayment |  |
| `repayment_schedule[].amount_paid.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `repayment_schedule[].amount_paid.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `repayment_schedule[].amount_paid.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `repayment_schedule[].amount_paid.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `repayment_schedule[].amount_paid.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `repayment_schedule[].amount_paid.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `repayment_schedule[].amount_paid.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `repayment_schedule[].initial_amount` | object | no | Initial amount for the repayment |  |
| `repayment_schedule[].initial_amount.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `repayment_schedule[].initial_amount.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `repayment_schedule[].initial_amount.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `repayment_schedule[].initial_amount.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `repayment_schedule[].initial_amount.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `repayment_schedule[].initial_amount.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `repayment_schedule[].initial_amount.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `repayment_schedule[].insurance` | object | no | Insurance premium amount for the repayment. Present only for insured installments. |  |
| `repayment_schedule[].insurance.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `repayment_schedule[].insurance.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `repayment_schedule[].insurance.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `repayment_schedule[].insurance.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `repayment_schedule[].insurance.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `repayment_schedule[].insurance.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `repayment_schedule[].insurance.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `repayment_schedule[].insurance_premium_state` | string (schema `InsurancePremiumState`) | no | Derived state of an installment's insurance premium. Present only when `includeInsuranceHistory=true` and the installment belongs to an insured loan. The platform reads the information from the current installment status (it is not persisted). For uninsured loans and for installments with no linked insurance record you do not see this state.<br><br>`PAID` - The insurance premium was collected. The installment status is settled (`PAID` or `PAID_WITHIN_GRACE`).<br>`CANCELED` - The insurance was canceled and the premium was never collected (installment status `CANCELED`). Covers both cancellation before the first premium and mid-plan cancellation of later installments.<br>`PENDING` - The premium is still awaiting collection (includes the `*_PENDING_PAYMENT` statuses).<br> | enum: ["PAID", "CANCELED", "PENDING"]; example: "PAID" |
| `restructure_loan_id` | string (schema `RestructureLoanID`) | no | Restructure loan ID. When a loan has been restructured, this field contains the ID of the new loan created from the restructure. | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `total_expected_payment_amount` | number (schema `TotalExpectedPaymentAmount`) | no | Total expected payment amount for the loan including principal, interest, fees, and penalty (if applied) | format: "double"; example: 1100 |
| `transactions_ids` | array of integer (schema `TransactionsIDs`) | no | List of transaction IDs | example: [6354273849, 982393773]; items.format: "int64" |

<!-- schema: #/components/schemas/V2Metadata -->
### Schema `V2Metadata`

Pointer: `#/components/schemas/V2Metadata`. Type: object (map of string) (schema `V2Metadata`).

> Additional information
>
> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).

<!-- schema: #/components/schemas/StandardAuthorizationErrorResponse -->
### Schema `StandardAuthorizationErrorResponse`

Pointer: `#/components/schemas/StandardAuthorizationErrorResponse`. Type: object (schema `StandardAuthorizationErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `denial_code` | string (schema `AuthorizationDenialCode`) | no | Payment Methods - Denial Code | minLength: 3; maxLength: 5; example: "IAD" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |
| `response_code` | string (schema `AuthorizationResponseCode`) | no | Payment Methods - Response Code | minLength: 2; maxLength: 2; example: "62" |

<!-- schema: #/components/schemas/TotalPayable -->
### Schema `TotalPayable`

Pointer: `#/components/schemas/TotalPayable`. Type: object (schema `TotalPayable`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount_due` | object | no |  |  |
| `amount_due.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `amount_due.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `amount_due.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `amount_due.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `amount_due.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `amount_due.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `amount_due.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `arrears` | object | no | Outstanding amount owed across all installments currently in `PAST_DUE` or `OVERDUE` status, broken down by component. Offers the total in arrears at loan level<br>  without summing individual installments. Zero when no installment is `PAST_DUE` or `OVERDUE` status. |  |
| `arrears.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `arrears.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `arrears.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `arrears.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `arrears.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `arrears.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `arrears.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |
| `charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |

<!-- schema: #/components/schemas/TotalPaid -->
### Schema `TotalPaid`

Pointer: `#/components/schemas/TotalPaid`. Type: object (schema `TotalPaid`).

> Consolidated loan-level amount that has already been paid across all repayments, aggregated server-side and broken down by component under `amount_paid`. Removes the need to total all repayment-level objects. Loan progress can be derived from `total_paid.amount_paid.total` versus `total_payable.total`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount_paid` | object | no |  |  |
| `amount_paid.principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `amount_paid.interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `amount_paid.fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `amount_paid.tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |
| `amount_paid.charge` | number (schema `ChargeAmount`) | no | Charge amount | format: "double"; example: 5 |
| `amount_paid.penalty` | number (schema `PenaltyAmount`) | no | Penalty amount | format: "double"; example: 27 |
| `amount_paid.total` | number (schema `TotalAmount`) | no | Total amount | format: "double"; example: 2072 |

<!-- schema: #/components/schemas/LoanDisbursement -->
### Schema `LoanDisbursement`

Pointer: `#/components/schemas/LoanDisbursement`. Type: object (schema `LoanDisbursement`).

> Disbursement details for the loan. The consolidated fields `total_disbursed_amount`, `remaining_to_disburse_amount` and `can_disburse_more` are present only for `MULTIPLE` disbursement loans and are omitted for `SINGLE` and `NONE`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `can_disburse_more` | boolean | no | Does the loan still have remaining disbursement capacity? (Meaning, the `remaining_to_disburse_amount` is greater than 0.) Present only for `MULTIPLE` disbursement loans; omitted for `SINGLE` and `NONE`. | example: true |
| `remaining_to_disburse_amount` | number | no | Remaining amount available to disburse, computed as `loan_principal_amount` minus `total_disbursed_amount`, never goes below 0. Present only for `MULTIPLE` disbursement loans; omitted for `SINGLE` and `NONE`. | format: "double"; example: 700 |
| `schedule` | array of object (schema `DisbursementScheduleItem`) (schema `LoanDisbursementSchedule`) | no | List of disbursement schedules |  |
| `total_disbursed_amount` | number | no | Sum of the amounts of all active disbursements, excluding those that are `CANCELED` or `EXPIRED`. Present only for `MULTIPLE` disbursement loans; omitted for `SINGLE` and `NONE`. | format: "double"; example: 300 |
| `type` | string (schema `LoanDisbursementType`) | no | Disbursement type | enum: ["SINGLE", "MULTIPLE"]; example: "SINGLE" |

<!-- schema: #/components/schemas/LoanInsuranceSummary -->
### Schema `LoanInsuranceSummary`

Pointer: `#/components/schemas/LoanInsuranceSummary`. Type: object (schema `LoanInsuranceSummary`).

> Loan-level insurance history summary. Returned only when `includeInsuranceHistory=true` and the loan has an insurance policy. It is omitted entirely for loans that were never insured. Per-installment `insurance_premium_state` values remain the source of truth.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `installment_counts` | object | yes | Count of insured installments grouped by derived premium state. Paid + canceled + pending installments equals the total number of insured installments. |  |
| `installment_counts.canceled` | integer | yes | Number of installments whose premium was canceled and never collected (`insurance_premium_state = CANCELED`) | format: "int32"; example: 3 |
| `installment_counts.paid` | integer | yes | Number of installments whose premium was collected (`insurance_premium_state = PAID`) | format: "int32"; example: 3 |
| `installment_counts.pending` | integer | yes | Number of installments still awaiting premium collection (`insurance_premium_state = PENDING`) | format: "int32"; example: 0 |
| `insurance_ever_active` | boolean | yes | Was insurance ever collected in the history of the loan? Set to `true` when at least one insurance premium has been collected (at least one installment has `insurance_premium_state = PAID`); `false` when the loan has an insurance policy but no premium was ever collected. | example: true |
| `last_covered_date` | string (schema `DateValue`) | no | End of the insurance coverage period. For an active or settled policy it is the latest installment real/due date (the enrolled coverage term end, independent of how many premiums were collected). For a canceled policy it is the insurance cancellation date. Omitted when the system cannot determine the last covered date.<br> | format: "date"; example: "2023-12-31" |

<!-- schema: #/components/schemas/PrepaymentSummaryV2Response -->
### Schema `PrepaymentSummaryV2Response`

Pointer: `#/components/schemas/PrepaymentSummaryV2Response`. Type: object (schema `PrepaymentSummaryV2Response`).

> Summary of a registered prepayment associated with a loan

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount_paid` | number | no | Total prepayment amount paid by the customer | example: 1000 |
| `created_at` | string | no | When the prepayment record was created. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2026-06-15T10:00:00.000Z" |
| `insurance_amount_paid` | number | no | Insurance portion settled with the prepayment, if any | example: 0 |
| `new_remaining_total` | number | no | Outstanding total of the loan after this prepayment was applied | example: 4000 |
| `penalty_amount_paid` | number | no | Penalty amount charged on the prepayment, if any | example: 50 |
| `prepayment_id` | string | no | Identifier of the prepayment | format: "uuid"; example: "73e45fd5-759f-4e04-a88a-7172fa948afa" |
| `reduce_option` | string (schema `ReduceOption`) | no | Defines the way that the outstanding loan amount is reduced. | enum: ["INSTALLMENT", "TERM"]; example: "INSTALLMENT" |
| `settlement_date` | string | no | Settlement date of the prepayment. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2026-06-15T10:00:00.000Z" |
| `status` | string | no | Lifecycle status of the prepayment | enum: ["CREATED", "PROCESSING", "REGISTERED"]; example: "REGISTERED" |
| `tax_amount_paid` | number | no | Tax amount applied to the prepayment | example: 0 |
| `updated_at` | string | no | When the prepayment record was last updated. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2026-06-15T10:00:00.000Z" |

<!-- schema: #/components/schemas/LoansRates -->
### Schema `LoansRates`

Pointer: `#/components/schemas/LoansRates`. Type: object (schema `LoansRates`).

> Loan rates including annual interest rate and effective annual and monthly costs

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `annual_interest_rate` | number (schema `AnnualInterestRate`) | no | Annual interest rate | format: "double"; example: 12 |
| `effective_annual_cost` | number (schema `EffectiveAnnualCost`) | no | Effective annual cost of the loan in configured currency | format: "double"; example: 319.98 |
| `effective_monthly_cost` | number (schema `EffectiveMonthlyCost`) | no | Effective monthly cost of the loan in configured currency | format: "double"; example: 12.7 |
| `interest_rate` | number (schema `LoanInterestRate`) | no | Loan interest rate | format: "double"; example: 12 |

<!-- schema: #/components/schemas/CancelLoanV2Metadata -->
### Schema `CancelLoanV2Metadata`

Pointer: `#/components/schemas/CancelLoanV2Metadata`. Type: object (map of string) (schema `CancelLoanV2Metadata`).

> Additional loan cancellation information
>
> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).

<!-- schema: #/components/schemas/LoanCancellationProcessingCodes -->
### Schema `LoanCancellationProcessingCodes`

Pointer: `#/components/schemas/LoanCancellationProcessingCodes`. Type: object (schema `LoanCancellationProcessingCodes`).

> Define processing codes for each operation during the loan cancellation.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `booking` | string (schema `ProcessingCode`) | no | Booking processing code | minLength: 2; maxLength: 6; example: "000011" |
| `penalty_waiver` | string (schema `ProcessingCode`) | no | Penalty waiver processing code | minLength: 2; maxLength: 6; example: "000011" |
| `repayment` | string (schema `ProcessingCode`) | no | Repayment processing code | minLength: 2; maxLength: 6; example: "000011" |

<!-- schema: #/components/schemas/DisbursementScheduleItem -->
### Schema `DisbursementScheduleItem`

Pointer: `#/components/schemas/DisbursementScheduleItem`. Type: object (schema `DisbursementScheduleItem`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `LoanDisbursementAmount`) | no | Disbursement amount | format: "double"; example: 300 |
| `authorization_id` | integer (schema `LoanAuthorizationID`) | no | Authorization ID | format: "int64"; example: 2422410859 |
| `date` | string (schema `LoanDisbursementDate`) | no | Disbursement date. Format = YYYY-MM-DD. | format: "date"; example: "2025-11-13" |
| `disbursement_account` | object (schema `LoanDisbursementAccount`) | no |  |  |
| `id` | string (schema `LoanDisbursementID`) | no | Disbursement ID | format: "uuid"; example: "54efa995-66f1-4595-9934-5b92222faf37" |
| `status` | string (schema `LoanDisbursementStatus`) | no | Disbursement status | enum: ["SCHEDULED", "PROCESSING", "CANCELED", "EXPIRED", "PAID"]; example: "PAID" |
| `tracking_id` | string (schema `TrackingID`) | no | Tracking ID | format: "uuid"; example: "003b3de8-c321-464c-a3dd-6009b8698325" |
| `transactions_ids` | array of integer (schema `TransactionsIDs`) | no | List of transaction IDs | example: [6354273849, 982393773]; items.format: "int64" |

<!-- schema: #/components/schemas/LoanDisbursementAccount -->
### Schema `LoanDisbursementAccount`

Pointer: `#/components/schemas/LoanDisbursementAccount`. Type: object (schema `LoanDisbursementAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | ID of the account receiving the disbursed funds | format: "int64"; example: 317890964 |
| `account_type` | string | no | Whether funds are disbursed to an account inside Pismo (`INTERNAL`) or an external account (`EXTERNAL`) | enum: ["INTERNAL", "EXTERNAL"]; example: "INTERNAL" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Lending.yaml` | tag `Loans`: GET /v2/accounts/{accountId}/loans, POST /v2/accounts/{accountId}/loans/cancel, POST /v2/loans/{loanId}/adjustment, GET /v2/loans, POST /v2/loans, GET /v2/loans/{loanId}, POST /v2/loans/{loanId}/cancel, POST /v2/loans/{originalLoanId}/restructure | https://github.com/PismoDevEx/pismo-api-specs | `6667602e6ada2f81…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CC-lending` — Control Center lending: loan products and loan management
- `KU-ERR-codes-elnd` — Error codes: ELND
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-lending-data-events` — Lending events
- `KU-LEND-book-a-loan` — Book loans
- `KU-LEND-disburse-loan` — Disburse loans
- `KU-LEND-manage-loan-repayment-and-settlement` — Manage loan repayment and settlement
