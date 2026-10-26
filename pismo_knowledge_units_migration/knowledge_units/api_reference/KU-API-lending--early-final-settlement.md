---
ku_id: KU-API-lending--early-final-settlement
title: 'API reference: Lending — Early final settlement'
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
- simulateEarlyFinalSettlementV2
- registerEarlyFinalSettlementV2
related_kus:
- KU-ERR-codes-elnd
- KU-LEND-manage-loan-repayment-and-settlement
specification_version: 1.0.0
---

# API reference: Lending — Early final settlement

**KU ID:** `KU-API-lending--early-final-settlement` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Early final settlement` in `api-specs/Lending.yaml` (“Lending”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Creates early final settlement management features

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/loans/{loanId}/early-settlement/simulate` | `simulateEarlyFinalSettlementV2` | Simulate early final settlement | no |
| `POST /v2/loans/{loanId}/early-settlement/{efsId}/register` | `registerEarlyFinalSettlementV2` | Register early final settlement | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer"}

## Operation contracts

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{loanId}/early-settlement/simulate operationId=simulateEarlyFinalSettlementV2 -->
### `POST /v2/loans/{loanId}/early-settlement/simulate` — Simulate early final settlement

- **operationId:** `simulateEarlyFinalSettlementV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Early final settlement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Simulate an early final settlement (EFS) for a loan. Optionally calculate present value with a future reference date

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |

#### Request body

Required: no

> Optional request body for simulation parameters

**Content type `application/json`** — schema: object (schema `EarlyFinalSettlementV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reference_date` | string (schema `ReferenceDate`) | no | Reference date of the installment. Format = YYYY-MM-DD. | format: "date"; example: "2025-04-14" |
| `waive_penalty` | boolean | no | Waive the penalty for early settlement? | default: false; example: false |

Example `Simulate EFS without reference date`:

```json
{}
```

Example `Simulate EFS with reference date`:

```json
{
  "reference_date": "2025-04-14",
  "waive_penalty": false
}
```

Example `Simulate EFS with waived penalty`:

```json
{
  "waive_penalty": true
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Simulation created | `application/json`: object (schema `EarlyFinalSettlementV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Resource not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `early_settlement_id` | string | yes | Early settlement simulation ID | format: "uuid"; example: "72852338-5764-4c7e-b503-10dcee1cdb7e" |
| `outstanding` | object (schema `OutstandingResponse`) | yes | Outstanding amount of a loan |  |
| `settlement_total` | number | yes | Total amount to settle the loan | format: "double"; example: 1584 |

201 Example `Simulation created`:

```json
{
  "early_settlement_id": "72852338-5764-4c7e-b503-10dcee1cdb7e",
  "settlement_total": 1584,
  "outstanding": {
    "principal": 800,
    "interest": 80,
    "charge": 0,
    "tax": 0,
    "fee": 0,
    "installments": 8,
    "penalty": 704
  }
}
```

##### Response 400

400 Example `ELND0400`:

```json
{
  "code": "ELND0400",
  "message": "Loan must be active to perform this action"
}
```

400 Example `ELND0401`:

```json
{
  "code": "ELND0401",
  "message": "Loan product does not support early final settlement."
}
```

400 Example `ELND0402`:

```json
{
  "code": "ELND0402",
  "message": "Lock In period defined in the current loan product did not meet the number of installments paid."
}
```

400 Example `ELND0405`:

```json
{
  "code": "ELND0405",
  "message": "Field reference_date must be equal to or greater than today."
}
```

400 Example `ELND0406`:

```json
{
  "code": "ELND0406",
  "message": "Field waive_penalty is true but no penalty is configured for this product."
}
```

##### Response 404

404 Example `ELND2000`:

```json
{
  "code": "ELND2000",
  "message": "Loan not found"
}
```

404 Example `ELND3000`:

```json
{
  "code": "ELND3000",
  "message": "Loan product not found."
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
| 400 | `ELND0400` | Loan must be active to perform this action |
| 400 | `ELND0401` | Loan product does not support early final settlement. |
| 400 | `ELND0402` | Lock In period defined in the current loan product did not meet the number of installments paid. |
| 400 | `ELND0405` | Field reference_date must be equal to or greater than today. |
| 400 | `ELND0406` | Field waive_penalty is true but no penalty is configured for this product. |
| 404 | `ELND2000` | Loan not found |
| 404 | `ELND3000` | Loan product not found. |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LEND-manage-loan-repayment-and-settlement`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{loanId}/early-settlement/{efsId}/register operationId=registerEarlyFinalSettlementV2 -->
### `POST /v2/loans/{loanId}/early-settlement/{efsId}/register` — Register early final settlement

- **operationId:** `registerEarlyFinalSettlementV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Early final settlement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register an early final settlement (EFS) for a loan using a previously simulated EFS ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `efsId` | path | yes | string | Early final settlement simulation ID | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `Idempotency-Key` | header | no | string | Optional UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Early final settlement registration accepted | `application/json`: object (schema `RegisterEarlyFinalSettlementV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Resource not found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `early_settle_id` | string | yes | Early settlement ID | format: "uuid"; example: "72852338-5764-4c7e-b503-10dcee1cdb7e" |
| `outstanding` | object (schema `OutstandingResponse`) | yes | Outstanding amount of a loan |  |
| `total_settled` | number | yes | Total amount settled for the loan | format: "double"; example: 1584 |

202 Example `Success response`:

```json
{
  "early_settle_id": "72852338-5764-4c7e-b503-10dcee1cdb7e",
  "total_settled": 1584,
  "outstanding": {
    "principal": 800,
    "interest": 80,
    "charge": 0,
    "tax": 0,
    "fee": 0,
    "installments": 8,
    "penalty": 704
  }
}
```

##### Response 400

400 Example `ELND0400`:

```json
{
  "code": "ELND0400",
  "message": "Loan must be active to perform this action."
}
```

400 Example `ELND0403`:

```json
{
  "code": "ELND0403",
  "message": "Early final settlement ID must be a UUID"
}
```

400 Example `ELND0404`:

```json
{
  "code": "ELND0404",
  "message": "This EFS simulation is not valid anymore because the outstanding balance changed after the simulation was requested."
}
```

##### Response 404

404 Example `ELND2000`:

```json
{
  "code": "ELND2000",
  "message": "Loan not found"
}
```

404 Example `ELND0005`:

```json
{
  "code": "ELND0005",
  "message": "EFS simulation not found"
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
| 400 | `ELND0400` | Loan must be active to perform this action. |
| 400 | `ELND0403` | Early final settlement ID must be a UUID |
| 400 | `ELND0404` | This EFS simulation is not valid anymore because the outstanding balance changed after the simulation was requested. |
| 404 | `ELND2000` | Loan not found |
| 404 | `ELND0005` | EFS simulation not found |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LEND-manage-loan-repayment-and-settlement`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/OutstandingResponse -->
### Schema `OutstandingResponse`

Pointer: `#/components/schemas/OutstandingResponse`. Type: object (schema `OutstandingResponse`).

> Outstanding amount of a loan

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `charge` | number (schema `OutstandingCharge`) | no | Outstanding charge | format: "double"; example: 10 |
| `fee` | number (schema `FeeAmount`) | no | Fee amount | format: "double"; example: 10 |
| `installments` | integer (schema `OutstandingInstallments`) | no | Number of outstanding installments | format: "int32"; example: 5 |
| `interest` | number (schema `InterestAmount`) | no | Interest amount | format: "double"; example: 20 |
| `penalty` | number (schema `CalculationPenalty`) | no | Calculation penalty early settlement | format: "double"; example: 100 |
| `principal` | number (schema `PrincipalAmount`) | no | Principal amount | format: "double"; example: 2000 |
| `tax` | number (schema `TaxAmount`) | no | Tax amount | format: "double"; example: 10 |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Lending.yaml` | tag `Early final settlement`: POST /v2/loans/{loanId}/early-settlement/simulate, POST /v2/loans/{loanId}/early-settlement/{efsId}/register | https://github.com/PismoDevEx/pismo-api-specs | `6667602e6ada2f81…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-elnd` — Error codes: ELND
- `KU-LEND-manage-loan-repayment-and-settlement` — Manage loan repayment and settlement
