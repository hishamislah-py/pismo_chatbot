---
ku_id: KU-API-revolving-credit-installment-management--simulations
title: 'API reference: Revolving credit - Installment management — Simulations'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Installment_management.yaml
  sha256: 1a735b324f2927f966984801891fd29894e1fe67abeeebc38d0bb02eb465ab9c
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
- SimulateInstallmentAdvancement
related_kus:
- KU-CRED-installment-advancements-guide
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-EVT-catalogue-balance
- KU-LIFE-api-endpoint-deprecation-and-removal-schedule
specification_version: 1.0.0
---

# API reference: Revolving credit - Installment management — Simulations

**KU ID:** `KU-API-revolving-credit-installment-management--simulations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Simulations` in `api-specs/Revolving_credit_-_Installment_management.yaml` (“Revolving credit - Installment management”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage installment simulations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/installment-advance/simulations` | `SimulateInstallmentAdvancement` | Simulate installment advancement | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Installment_management.yaml method=GET path=/v1/accounts/{accountId}/installment-advance/simulations operationId=SimulateInstallmentAdvancement -->
### `GET /v1/accounts/{accountId}/installment-advance/simulations` — Simulate installment advancement

- **operationId:** `SimulateInstallmentAdvancement`
- **Specification:** `api-specs/Revolving_credit_-_Installment_management.yaml` (Revolving credit - Installment management)
- **Server base URL(s):** `https://sandbox.pismolabs.io/installment-management`
- **Tags:** `Simulations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Simulate an installment advancement for an account. That is, it simulates advancing one or more installments from a future cycle to the current cycle.
>
> To simulate advancing installments for a specific installment agreement (contract), set the `condition` query parameter to `SINGLE_CONTRACT`, and set the `transaction_id` query parameter to the transaction ID of any of the installments in the installment agreement. Specify the number of installments to advance in the simulation in the `number_of_installments_to_advance` query parameter. Installments are advanced starting with the last scheduled installment in the agreement and working backwards from there.
>
> To simulate advancing <b>all</b> future installments for <b>all</b> installment agreements in the account, set the `condition` field to `ALL_CONTRACTS`. (In this case, the `number_of_installments_to_advance` field is ignored.)
>
> When you simulate advancing installments, you must specify what to do with the interest. You have three options:
> - To simulate removing 100% of the interest on the advanced installment(s), set the `remove_interest_from_current` query parameter to `true` and the `calculator` query parameter to `NONE`.
> - To simulate advancing 100% of the interest on the advanced installment(s), set `remove_interest_from_current` to `false` and set `calculator` to `NONE`.
> - To simulate recalculating the interest applied to the advanced installments(s), set `calculator` to `PRESENT_VALUE`. The `remove_interest_from_current` parameter can be set to either `true` or `false`. If `true`, the interest on installments that were already in the current cycle (and did not need to be advanced) is recalculated in the simulation. Otherwise, interest on those installments is unchanged.
>
> For more information, see <a href='https://developers.pismo.io/pismo-docs/docs/installment-management#installment-advancements'>Installment advancements</a>.
>
> This endpoint generates an <a href='https://developers.pismo.io/events/docs/balance-installment-advancement-1'>Installment advanced</a> event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; example: 6912345 |
| `transactionId` | query | no | integer | Transaction ID | format: "int64"; example: 98457355 |
| `condition` | query | yes | string | Indicates if all installments should be advanced (`ALL_CONTRACTS`) or just a single installment (`SINGLE_CONTRACT`). | enum: ["ALL_CONTRACTS", "SINGLE_CONTRACT"]; example: "ALL_CONTRACTS" |
| `removeInterestFromCurrent` | query | no | boolean | Indicates whether interest should be removed when an installment is advanced to the current statement. Default is `false`. | default: false; example: false |
| `calculator` | query | no | string | Specifies the type of calculation to be applied for interest reduction when an installment is advanced to the current cycle. To recalculate the interest on advancements, set `calculator` to `PRESENT_VALUE`. Default is `NONE`. | enum: ["PRESENT_VALUE", "NONE"] |
| `reschedule` | query | yes | string | Indicates the type of rescheduling to apply. Must be set to `ADVANCEMENT`. | enum: ["ADVANCEMENT"] |
| `numberOfInstallmentsToAdvance` | query | no | integer | Define the number of installments to be brought to the current statement. | example: 2 |
| `interestRemovalEndDate` | query | no | string | Optional cutoff date for interest removal when `calculator` is set to `PRESENT_VALUE`.<br>Installments with a due date on or before this date will have interest recalculated using this date as the reference instead of the original due date.<br>If omitted, the installment's original due date is used.<br> | format: "date"; example: "2025-06-30" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `SimulateInstallmentAdvancedResponseDto`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 67854328 |
| `authorization_id` | integer (schema `AuthorizationIdForFirstInstallment`) | no | Authorization ID for the first installment | format: "int64"; example: 200 |
| `condition` | string (schema `Condition`) | no | Installments should be advanced for all the contracts for an account (`ALL_CONTRACTS`) or for a specific contract (`SINGLE_CONTRACT`).<br>If `condition` is set to `SINGLE_CONTRACT`, then the `transaction_id` field must be set to the transaction ID of the specific contract.<br> | enum: ["SINGLE_CONTRACT", "ALL_CONTRACTS"]; example: "SINGLE_CONTRACT" |
| `calculator` | string (schema `Calculator`) | no | Type of calculation to apply. Default is `NONE`.<br> | enum: ["PRESENT_VALUE", "REMOVE_ALL_INTEREST", "NONE"]; example: "PRESENT_VALUE" |
| `reschedule` | string (schema `Reschedule`) | no | Reschedule mode to apply. Must be `ADVANCEMENT`.<br> | enum: ["ADVANCEMENT"]; example: "ADVANCEMENT" |
| `interest_removal_end_date` | string (schema `InterestRemovalEndDate`) | no | Cutoff date used for interest recalculation when `calculator` is `PRESENT_VALUE`.<br>Reflects the value passed in the request. `null` if not passed. Format = yyyy-mm-dd.<br> | format: "date"; example: "2021-04-14" |
| `installments` | array of object (schema `InstallmentResponseDto`) | no |  |  |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 409

409 Example `Account conflict`:

```json
{
  "message": "Installment advance already exists with this Account_ID and Tracking_ID."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-installment-advancement-1` | https://developers.pismo.io/events/docs/balance-installment-advancement-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CRED-installment-advancements-guide`, `KU-LIFE-api-endpoint-deprecation-and-removal-schedule`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/InstallmentResponseDto -->
### Schema `InstallmentResponseDto`

Pointer: `#/components/schemas/InstallmentResponseDto`. Type: object (schema `InstallmentResponseDto`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `TransactionIdOfInstallment`) | no | Transaction ID of the installment | format: "int64"; example: 98457355 |
| `new_amount` | number (schema `NewAmount`) | no | Full installment amount after applying any discount, including principal and interest charges<br> | format: "double"; example: 99.9 |
| `old_amount` | number (schema `OldAmount`) | no | Full installment amount before applying any discount, including principal and interest charges<br> | format: "double"; example: 102.9 |
| `new_interest_amount` | number (schema `NewInterestAmount`) | no | Full interest amount of installment after applying any discount<br> | format: "double"; example: 9.9 |
| `old_interest_amount` | number (schema `OldInterestAmount`) | no | The full interest amount of an installment before applying any discount.<br> | format: "double"; example: 11.9 |
| `new_statement_id` | number (schema `NewStatementId`) | no | ID of the current statement<br> | format: "integer"; example: 1 |
| `old_statement_id` | number (schema `OldStatementId`) | no | ID of the old statement. This is the ID of the statement on which the installment was scheduled to appear before it was advanced. For installments that are not advanced, `old_statement_id` and `new_statement_id` should contain the same values.<br> | format: "integer"; example: 10 |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code | example: "EX0001" |
| `message` | string | no | Error message | example: "Internal error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Installment_management.yaml` | tag `Simulations`: GET /v1/accounts/{accountId}/installment-advance/simulations | https://github.com/PismoDevEx/pismo-api-specs | `1a735b324f2927f9…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CRED-installment-advancements-guide` — Installment advancements
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-LIFE-api-endpoint-deprecation-and-removal-schedule` — API endpoint deprecation and removal schedule
