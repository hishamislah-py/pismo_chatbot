---
ku_id: KU-API-lending--prepayment
title: 'API reference: Lending — Prepayment'
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
- simulatePrepaymentV2
- registerPrepaymentSimulationV2
- createPrepayment
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-ERR-codes-elnd
- KU-EVT-catalogue-lending
- KU-EVT-lending-data-events
specification_version: 1.0.0
---

# API reference: Lending — Prepayment

**KU ID:** `KU-API-lending--prepayment` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Prepayment` in `api-specs/Lending.yaml` (“Lending”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manages loan prepayment

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/loans/{loanId}/prepayment/simulate` | `simulatePrepaymentV2` | Simulate prepayment | no |
| `POST /v2/loans/{loanId}/prepayment/{simulationId}/register` | `registerPrepaymentSimulationV2` | Register prepayment simulation | no |
| `POST /v2/prepayments` | `createPrepayment` | Create prepayment record | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer"}

## Operation contracts

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{loanId}/prepayment/simulate operationId=simulatePrepaymentV2 -->
### `POST /v2/loans/{loanId}/prepayment/simulate` — Simulate prepayment

- **operationId:** `simulatePrepaymentV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Prepayment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Simulate a prepayment for a loan using the prepayment engine.
>
> The response includes the resulting balance breakdown, the new repayment
> schedule, and a `simulation_id` that can later be used to register the
> prepayment via `POST /v2/loans/{loanId}/prepayment/{simulationId}/register`.
>
> This endpoint generates a [Lending prepayment creation](https://developers.pismo.io/events/docs/lending-lending-prepayment-v2-creation-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `Idempotency-Key` | header | no | string | Optional UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PrepaymentSimulationV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount_paid` | object | yes |  |  |
| `reduce_option` | string (schema `ReduceOption`) | yes | Defines the way that the outstanding loan amount is reduced. | enum: ["INSTALLMENT", "TERM"]; example: "INSTALLMENT" |
| `reference_date` | string | no | Reference date used to compute the prepayment. When omitted, the Pismo platform sets the value to the current date. Format = YYYY-MM-DD. | format: "date"; example: "2026-05-15" |
| `waive_fee` | boolean | no | When omitted, the Pismo platform sets the value to `false`. Should the fees applied to this prepayment be waived? | example: false |

Example `Simulate a prepayment that reduces installments`:

```json
{
  "amount_paid": 2000,
  "reference_date": "2026-05-15",
  "waive_fee": false,
  "reduce_option": "INSTALLMENT"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Prepayment simulated. | `application/json`: object (schema `PrepaymentSimulationV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Resource not found. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount_paid` | number (schema `AmountPaid`) | no | Prepayment amount | format: "double"; minimum: 0; example: 1000 |
| `balance_breakdown` | object (schema `PrepaymentBalanceBreakdownV2`) | no | Detailed description of the outstanding balance settled by this prepayment, shown by component |  |
| `created_at` | string | no | Date and time the simulation was created. ISO 8601 with millisecond precision and offset. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time"; example: "2026-09-03T17:59:36.550Z" |
| `insurance_amount_paid` | number | no | Insurance portion paid as part of the prepayment | format: "double"; example: 0 |
| `loan_id` | string | no | ID of the loan the simulation was run against | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `new_remaining_total` | number | no | Total remaining loan amount after applying this prepayment | format: "double"; example: 5000 |
| `new_repayment_schedule` | array of object (schema `PrepaymentRepaymentScheduleItemV2`) | no | List of resulting repayments in the schedule after applying this prepayment |  |
| `penalty_amount_paid` | number | no | Penalty portion paid as part of the prepayment | format: "double"; example: 50 |
| `reduce_option` | string (schema `ReduceOption`) | no | Defines the way that the outstanding loan amount is reduced. | enum: ["INSTALLMENT", "TERM"]; example: "INSTALLMENT" |
| `simulation_id` | string (schema `PrepaymentSimulationID`) | no | Prepayment simulation ID | format: "uuid"; example: "c04fd22b-7d9c-4099-aaf4-9ee002b5a6a7" |
| `tax_amount_paid` | number | no | Tax portion paid as part of the prepayment | format: "double"; example: 0 |

##### Response 400

400 Example `ELND0504`:

```json
{
  "code": "ELND0504",
  "message": "Field amount_paid not passed."
}
```

400 Example `ELND0512`:

```json
{
  "code": "ELND0512",
  "message": "Field reduce_option not passed."
}
```

400 Example `ELND0513`:

```json
{
  "code": "ELND0513",
  "message": "Loan product does not permit the reduce_option passed in the request."
}
```

400 Example `ELND0511`:

```json
{
  "code": "ELND0511",
  "message": "The calculated penalty would be greater than the amount being paid."
}
```

400 Example `ELND0514`:

```json
{
  "code": "ELND0514",
  "message": "Failed to calculate the new loan with the provided parameters."
}
```

400 Example `ELND0515`:

```json
{
  "code": "ELND0515",
  "message": "Simulation config not found."
}
```

##### Response 404

404 Example `ELND0005`:

```json
{
  "code": "ELND0005",
  "message": "{resource name} not found"
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
| 400 | `ELND0504` | Field amount_paid not passed. |
| 400 | `ELND0512` | Field reduce_option not passed. |
| 400 | `ELND0513` | Loan product does not permit the reduce_option passed in the request. |
| 400 | `ELND0511` | The calculated penalty would be greater than the amount being paid. |
| 400 | `ELND0514` | Failed to calculate the new loan with the provided parameters. |
| 400 | `ELND0515` | Simulation config not found. |
| 404 | `ELND0005` | {resource name} not found |
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-lending-prepayment-v2-creation-1` | https://developers.pismo.io/events/docs/lending-lending-prepayment-v2-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/loans/{loanId}/prepayment/{simulationId}/register operationId=registerPrepaymentSimulationV2 -->
### `POST /v2/loans/{loanId}/prepayment/{simulationId}/register` — Register prepayment simulation

- **operationId:** `registerPrepaymentSimulationV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Prepayment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Register a previously calculated prepayment simulation, applying it to
> the loan. The request body is optional and is only used to override the
> processing codes used to record the prepayment, penalty, and insurance
> movements in the prepayment workflow.
>
> This endpoint generates a [Lending prepayment status changed](https://developers.pismo.io/events/docs/lending-lending-prepayment-v2-status-changed-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `loanId` | path | yes | string | ID of the loan the operation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `simulationId` | path | yes | string | Prepayment simulation ID returned by the simulate endpoint | format: "uuid"; example: "c04fd22b-7d9c-4099-aaf4-9ee002b5a6a7" |
| `Idempotency-Key` | header | no | string | Optional UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `RegisterPrepaymentSimulationV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `insurance_processing_code` | string | no | Processing code used to register the insurance movement in the prepayment flow | minLength: 2; maxLength: 6; example: "INSR" |
| `penalty_processing_code` | string | no | Processing code used to register the penalty movement in the prepayment flow | minLength: 2; maxLength: 6; example: "PNLT" |
| `prepayment_processing_code` | string | no | Processing code used to register the prepayment movement in the prepayment flow. | minLength: 2; maxLength: 6; example: "PPMT" |

Example `Register with custom processing codes`:

```json
{
  "prepayment_processing_code": "PPMT",
  "penalty_processing_code": "PNLT",
  "insurance_processing_code": "INSR"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Prepayment registration accepted. | `application/json`: object (schema `RegisterPrepaymentSimulationV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Resource not found. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `loan_id` | string | no | ID of the loan the registered simulation applies to | format: "uuid"; example: "2717a296-124a-47cc-b2a1-91e80dc723eb" |
| `simulation_id` | string (schema `PrepaymentSimulationID`) | no | Prepayment simulation ID | format: "uuid"; example: "c04fd22b-7d9c-4099-aaf4-9ee002b5a6a7" |
| `status` | string | no | Current registration status of the simulation | example: "PROCESSING" |

##### Response 400

400 Example `ELND0500`:

```json
{
  "code": "ELND0500",
  "message": "simulationId must be an UUID"
}
```

400 Example `ELND0549`:

```json
{
  "code": "ELND0549",
  "message": "Prepayment processing code length must be between 2 and 6."
}
```

400 Example `ELND0550`:

```json
{
  "code": "ELND0550",
  "message": "Penalty processing code length must be between 2 and 6."
}
```

400 Example `ELND0551`:

```json
{
  "code": "ELND0551",
  "message": "Insurance processing code length must be between 2 and 6."
}
```

400 Example `ELND0509`:

```json
{
  "code": "ELND0509",
  "message": "This Prepayment simulation is no longer valid because the outstanding balance changed after the simulation was requested."
}
```

##### Response 404

404 Example `ELND0005`:

```json
{
  "code": "ELND0005",
  "message": "{resource name} not found"
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
| 400 | `ELND0500` | simulationId must be an UUID |
| 400 | `ELND0549` | Prepayment processing code length must be between 2 and 6. |
| 400 | `ELND0550` | Penalty processing code length must be between 2 and 6. |
| 400 | `ELND0551` | Insurance processing code length must be between 2 and 6. |
| 400 | `ELND0509` | This Prepayment simulation is no longer valid because the outstanding balance changed after the simulation was requested. |
| 404 | `ELND0005` | {resource name} not found |
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-lending-prepayment-v2-status-changed-1` | https://developers.pismo.io/events/docs/lending-lending-prepayment-v2-status-changed-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/prepayments operationId=createPrepayment -->
### `POST /v2/prepayments` — Create prepayment record

- **operationId:** `createPrepayment`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Prepayment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a prepayment record containing one or multiple repayments.
>
> This endpoint generates a [Prepayment created](https://developers.pismo.io/events/docs/lending-prepayment-creation-1) event.
>
> **Note**: This endpoint requires an [account-specific access token](ref:get-an-account-specific-token-basic-authentication).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | no | string | Optional UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PrepaymentV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `repayment_ids` | array of string (schema `PrepaymentRepaymentDetails`) | yes | List of repayments to be paid in the current prepayment | example: ["c04fd22b-7d9c-4099-aaf4-9ee002b5a6a7", "jdu55ks2-7d9c-4099-aaf4-9ee002tkl554"] |
| `expiration_date` | string (schema `ExpirationDate`) | no | Expiration date of the prepayment. Format = YYYY-MM-DD. | format: "date"; example: "2025-04-28" |
| `metadata` | object (map of string) (schema `PrepaymentMetadata`) | no | Additional prepayment information<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `reference_date` | string (schema `ReferenceDate`) | no | Reference date of the installment. Format = YYYY-MM-DD. | format: "date"; example: "2025-04-14" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Prepayment created. | `application/json`: object (schema `PrepaymentV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `allocation_summary` | array of object (schema `LoanAllocationSummary`) | no | List of summarized loan allocations with minimum total payment deltas, which represent the difference between the borrower's actual payment and the scheduled installment amount, applied as a principal reduction on the loan. | example: [{"loan_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890", "loan_start_date": "2025-01-15T00:00:00.000Z", "installment_amount": 156.54, "minimum_total_payment_delta": 43.46}, {"loan_id": "b2c3d4e5-f6a7-8901-bcde-f12345678901", "loan_start_date": "2025-03-01T00:00:00.000Z", "installment_amount": 200, "minimum_total_payment_delta": 0}] |
| `expected_amount` | number | no | Expected amount to be paid | format: "double"; example: 100 |
| `expiration_date` | string | no | Date after which the pending prepayment expires and its installments revert to their base status. Defaults to `reference_date` (or today when absent) plus 30 days. Format = YYYY-MM-DD. | format: "date"; example: "2026-08-31" |
| `insurance` | object | no | Insurance prepayment details (if applicable) |  |
| `insurance.expected_amount` | number | no | Expected insurance amount to be paid | format: "double" |
| `insurance.prepayment_id` | string | no | Insurance prepayment ID | format: "uuid" |
| `prepayment_id` | string | no | Pismo-generated UUID identifying the prepayment | format: "uuid"; example: "c04fd22b-7d9c-4099-aaf4-9ee002b5a6a7" |
| `reference_date` | string | no | Reference date applied to the prepayment (pricing base); `null` when not provided in the request. Format = YYYY-MM-DD. | format: "date"; example: "2026-08-01" |

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
| 500 | `ELND0001` | Unexpected error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `lending-prepayment-creation-1` | https://developers.pismo.io/events/docs/lending-prepayment-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-lending-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/PrepaymentBalanceBreakdownV2 -->
### Schema `PrepaymentBalanceBreakdownV2`

Pointer: `#/components/schemas/PrepaymentBalanceBreakdownV2`. Type: object (schema `PrepaymentBalanceBreakdownV2`).

> Detailed description of the outstanding balance settled by this prepayment, shown by component

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fee` | number | no |  | format: "double"; example: 0 |
| `interest` | number | no |  | format: "double"; example: 150 |
| `penalty` | number | no |  | format: "double"; example: 50 |
| `principal` | number | no |  | format: "double"; example: 1800 |
| `tax` | number | no |  | format: "double"; example: 0 |

<!-- schema: #/components/schemas/PrepaymentRepaymentScheduleItemV2 -->
### Schema `PrepaymentRepaymentScheduleItemV2`

Pointer: `#/components/schemas/PrepaymentRepaymentScheduleItemV2`. Type: object (schema `PrepaymentRepaymentScheduleItemV2`).

> A single installment in the resulting repayment schedule

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `due_date` | string | no | Installment due date. Format = YYYY-MM-DD. | format: "date"; example: "2026-06-15" |
| `fee_amount` | number | no |  | format: "double"; example: 0 |
| `installment_number` | integer | no | Installment sequence number, starting at 1 | example: 1 |
| `interest_amount` | number | no |  | format: "double"; example: 15 |
| `principal_amount` | number | no |  | format: "double"; example: 200 |
| `tax_amount` | number | no |  | format: "double"; example: 0 |
| `total_amount` | number | no |  | format: "double"; example: 215 |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |

<!-- schema: #/components/schemas/PrepaymentMetadata -->
### Schema `PrepaymentMetadata`

Pointer: `#/components/schemas/PrepaymentMetadata`. Type: object (map of string) (schema `PrepaymentMetadata`).

> Additional prepayment information
>
> **Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).

<!-- schema: #/components/schemas/LoanAllocationSummary -->
### Schema `LoanAllocationSummary`

Pointer: `#/components/schemas/LoanAllocationSummary`. Type: object (schema `LoanAllocationSummary`).

> Summary of a loan allocation within a group payment

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `installment_amount` | number | no | Installment amount allocated | format: "double" |
| `loan_id` | string | no | ID of the loan included in this allocation |  |
| `loan_start_date` | string | no | Date the loan started. Format = YYYY-MM-DDThh:mm:ss.SSSZ. | format: "date-time" |
| `minimum_total_payment_delta` | number (schema `MinimumTotalPaymentDelta`) | no | Additional amount added to the repayment to cover the minimum total payment requirement | format: "double"; minimum: 0; example: 43.46 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Lending.yaml` | tag `Prepayment`: POST /v2/loans/{loanId}/prepayment/simulate, POST /v2/loans/{loanId}/prepayment/{simulationId}/register, POST /v2/prepayments | https://github.com/PismoDevEx/pismo-api-specs | `6667602e6ada2f81…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-ERR-codes-elnd` — Error codes: ELND
- `KU-EVT-catalogue-lending` — Event catalogue: lending
- `KU-EVT-lending-data-events` — Lending events
