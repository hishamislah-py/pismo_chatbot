---
ku_id: KU-API-banking-interest-engine--interest-engine
title: 'API reference: Banking - Interest engine — Interest engine'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Interest_engine.yaml
  sha256: 93ec981c793eff612b56fb2c5044f8aebbc05f8aa4557c9e68bf99417212bdff
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
- get-v1-interest-plans
- post-v1-interest-plan
- get-v1-interest-plan
- patch-v1-interest-plan
related_kus:
- KU-BANK-how-overdraft-works
- KU-BANK-interest-bearing-accounts
- KU-BANK-penalties-for-cd-accounts
- KU-EVT-catalogue-interest
- KU-EVT-interest-management-data-events
- KU-LEND-loan-products
specification_version: 1.0.0
---

# API reference: Banking - Interest engine — Interest engine

**KU ID:** `KU-API-banking-interest-engine--interest-engine` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Interest engine` in `api-specs/Banking_-_Interest_engine.yaml` (“Banking - Interest engine”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage interest plans

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/interest/plan` | `get-v1-interest-plans` | List Org interest plans | no |
| `POST /v1/interest/plan` | `post-v1-interest-plan` | Create interest plan | no |
| `GET /v1/interest/plan/{interestPlanId}` | `get-v1-interest-plan` | Get interest plan | no |
| `PATCH /v1/interest/plan/{interestPlanId}` | `patch-v1-interest-plan` | Create interest plan version | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest_engine.yaml method=GET path=/v1/interest/plan operationId=get-v1-interest-plans -->
### `GET /v1/interest/plan` — List Org interest plans

- **operationId:** `get-v1-interest-plans`
- **Specification:** `api-specs/Banking_-_Interest_engine.yaml` (Banking - Interest engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/interest-engine`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Interest engine`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List all interest plans for a given Org.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `page` | query | yes | integer | Page number. Default is `1`. | format: "int32"; example: 1 |
| `perPage` | query | yes | integer | Number of items per page. Default is `10`. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InterestPlansResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized. The response body is produced by the upstream authentication gateway and is not defined by this service. |  |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page. Default is `10`. | format: "Int32"; example: 1 |
| `pages` | integer (schema `Pages`) | no | Total number of pages. Default is `1`. | format: "Int32"; example: 1 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 1 |
| `items` | array of object | no |  |  |
| `items[].interest_plan_id` | string (schema `InterestPlanId`) | no | Interest plan ID generated during the plan's creation. Must be an alphanumeric UUID with the alphabetical characters in lowercase. | format: "UUID"; example: "07d84f79-3027-47bd-b628-65528ccc8fb2" |
| `items[].org_id` | string (schema `OrgId`) | no | Organization ID generated in the onboarding process | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `items[].description` | string (schema `Description`) | no | Interest plan name | example: "Banking plan" |
| `items[].currency_code` | string (schema `CurrencyCode`) | no | Numeric currency code in ISO 4217 standard. Only the following codes are accepted: 986 (BRL), 826 (GBP), 356 (INR), 840 (USD), 978 (EUR), 604 (PEN), 036 (AUD), 484 (MXN), 764 (THB), 208 (DKK), 752 (SEK), 578 (NOK). | enum: ["986", "826", "356", "840", "978", "604", "036", "484", "764", "208", "752", "578"]; format: "number"; example: "986" |
| `items[].benchmark` | string (schema `BenchmarkResponse`) | no | Market index returned in responses.<br>  - `BOE`: Bank of England, UK<br>  - `DI`: Interbank Deposit Contract, Brazil<br>  - `FED`: Federal Reserve System, USA<br>  - `FIXED`: Fixed interest rate, no market index<br>  - `RBA`: Reserve Bank of Australia<br>  - `RBI`: Reserve Bank of India<br>  - `TO`: Overnight Interbank Target Rate (Tasa Objetivo), Mexico<br> | enum: ["BOE", "DI", "FED", "FIXED", "RBA", "RBI", "TO"]; example: "FIXED" |
| `items[].fixed_interest_rate` | number (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "float"; example: 0.1 |
| `items[].margin_rate` | number \\\| null (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you don't pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `items[].margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `items[].tax_withholding` | object (schema `TaxWithholding`) | no | Tax withholding configuration. Replaces the standalone `fee_processing_code` field.<br>Conditional rules enforced at creation/update time:<br>- `ACCRUAL`: `fee_processing_code` is required; `tax_rules` must be omitted.<br>- `CAPITALIZATION`: `tax_rules` is required; `fee_processing_code` must be omitted.<br>- Omitted `withholding_moment`: both `fee_processing_code` and `tax_rules` must be omitted.<br>In GET responses, legacy plans that predate this field may return `fee_processing_code` with a null `withholding_moment`.<br> |  |
| `items[].accrual_basis` | string (schema `AccrualBasis`) | no | Method used to calculate interest accrual.<br>  * `BD/252`: Calculates daily interest using a 252-day year and the actual number of business days in each time period.<br>  * `ACTUAL/360`: Calculates daily interest using a 360-day year and the actual number of days in each time period.<br>  * `ACTUAL/365`: Calculates daily interest using a 365-day year and the actual number of days in each time period.<br>  * `ACTUAL/ACTUAL`: Calculates daily interest using the actual number of days in the year (which in the leap year is 366) and the actual number of days in each time period.<br> | enum: ["BD/252", "ACTUAL/360", "ACTUAL/365", "ACTUAL/ACTUAL"]; example: "ACTUAL/365" |
| `items[].interest_type` | string (schema `InterestType`) | no | Interest calculation type<br>- `SIMPLE`: Calculated on the original deposit or investment value.<br>- `COMPOUND`: Calculated on the original value plus the last accumulated interest.<br> | enum: ["SIMPLE", "COMPOUND"]; example: "SIMPLE" |
| `items[].capitalization_frequency` | string (schema `CapitalizationFrequency`) | no | Interest payout frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |
| `items[].accrual_frequency` | string (schema `AccrualFrequency`) | no | Interest accrual frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |
| `items[].status` | string (schema `Status`) | no | Interest plan status. Must be set to `ACTIVE`. | enum: ["ACTIVE"]; example: "ACTIVE" |
| `items[].operation_type` | string (schema `OperationType`) | no | Operation type.<br>- `DEBIT`: Interest plan for debit type operations<br>- `CREDIT`: Interest plan for credit type operations<br> | enum: ["DEBIT", "CREDIT"]; example: "DEBIT" |
| `items[].start_date` | string (schema `StartDate`) | no | Date to start applying the benchmark rate in the accrual process. Format = YYYY-MM-DD. | format: "date"; example: "2024-09-10" |
| `items[].interest_by_tiers` | object (schema `InterestByTiers`) | no | Interest by tiers configuration | example: {"type": "TERM", "tier_calculation": "RETROACTIVE", "tiers": [{"days": 30, "amount": 1000, "margin_rate": 1, "fixed_interest_rate": 1.2}, {"days": 60, "amount": 2000, "margin_rate": 1, "fixed_interest_rate": 1.3}]} |
| `items[].interest_thresholds` | object (schema `InterestThresholds`) | no | Cap and floor thresholds for the interest plan | example: {"cap_threshold": 1.1, "cap_effective_rate": 1.2, "floor_threshold": 2.2, "floor_effective_rate": 2.1} |
| `items[].division_id` | string (schema `DivisionId`) | no | Division ID attached to the interest plan for accrual by division | example: "d9b2c9e1-4633-4a10-841b-270f7f1493cd" |
| `items[].interest_base_model` | string (schema `InterestBaseModel`) | no | Interest calculation model. `CLOSING-BALANCE` calculates interest on a single end-of-day balance snapshot. `BALANCE-CHANGE` calculates interest on each intraday balance movement (for example, credits and debits) as it occurs, so interest accrues on the balance held during each interval between consecutive movements rather than on one end-of-day figure. Defaults to `CLOSING-BALANCE`. | enum: ["CLOSING-BALANCE", "BALANCE-CHANGE"]; default: "CLOSING-BALANCE"; example: "CLOSING-BALANCE" |

##### Response 400

400 Example `validation` (Bean validation or binding errors):

```json
{
  "message": [
    "fixed_interest_rate must be informed",
    "margin_rate must be positive"
  ]
}
```

400 Example `requestBody` (invalid or missing request value):

```json
{
  "message": "Failed to process your request. Validate the fields in your request."
}
```

400 Example `tenantHeader` (Tenant header missing or malformed):

```json
{
  "message": "x-tenant header is missing or malformed"
}
```

400 Example `unknownField` (Unknown field in request body):

```json
{
  "error": "Invalid field in request",
  "message": "Field 'foo' is not allowed. Only the following fields can be updated: start_date, description, fixed_interest_rate, margin_rate, margin, interest_by_tiers, interest_thresholds",
  "field": "foo",
  "status": 400
}
```

400 Example `invalidJson` (Invalid JSON body):

```json
{
  "error": "Invalid JSON format",
  "message": "Request contains invalid JSON structure or field types",
  "status": 400
}
```

400 Example `taxWithholdingAccrualFeeRequired` (ACCRUAL withholding without fee_processing_code):

```json
{
  "message": [
    "fee_processing_code is required when tax_withholding.withholding_moment is ACCRUAL."
  ]
}
```

400 Example `taxWithholdingAccrualTaxRulesNotAllowed` (ACCRUAL withholding with tax_rules present):

```json
{
  "message": [
    "tax_rules must be null when tax_withholding.withholding_moment is ACCRUAL."
  ]
}
```

400 Example `taxWithholdingCapitalizationFeeNotAllowed` (CAPITALIZATION withholding with fee_processing_code present):

```json
{
  "message": [
    "fee_processing_code must be null when tax_withholding.withholding_moment is CAPITALIZATION."
  ]
}
```

400 Example `taxWithholdingCapitalizationTaxRulesRequired` (CAPITALIZATION withholding without tax_rules):

```json
{
  "message": [
    "tax_rules is required when tax_withholding.withholding_moment is CAPITALIZATION."
  ]
}
```

400 Example `taxWithholdingNoneFieldsNotAllowed` (NULL withholding_moment with fee_processing_code or tax_rules present):

```json
{
  "message": [
    "fee_processing_code and tax_rules must be null when tax_withholding.withholding_moment is NULL."
  ]
}
```

400 Example `taxWithholdingNotAllowedWhenTaxesExemption` (taxes_exemption is true with tax_withholding present):

```json
{
  "message": [
    "tax_withholding must be null when taxes_exemption is true."
  ]
}
```

##### Response 404

404 Example `interestAccountNotFound` (Interest account not found):

```json
{
  "message": "interest account not found"
}
```

404 Example `interestPlanNotFound` (Interest plan not found):

```json
{
  "message": "interest plan not found"
}
```

404 Example `benchmarkNotFound` (Benchmark not found):

```json
{
  "message": "benchmark not found"
}
```

##### Response 500

500 Example `example`:

```json
{
  "message": "Failed to process your request"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Interest_engine.yaml method=POST path=/v1/interest/plan operationId=post-v1-interest-plan -->
### `POST /v1/interest/plan` — Create interest plan

- **operationId:** `post-v1-interest-plan`
- **Specification:** `api-specs/Banking_-_Interest_engine.yaml` (Banking - Interest engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/interest-engine`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Interest engine`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates an interest plan configuration that defines how the platform calculates interest accrual. After it's created, you can apply the interest plan to a specific product or account. For example, you can provide the `interest_plan_id` when creating a [deposit product](ref:interest-bearing-v1-create-deposit-product), when creating a [savings account](ref:interest-bearing-v1-create-savings-account-product), or when [depositing money](ref:post-v1-interest-deposit) into an account.
>
> This endpoint generates an [Interest plan creation succeeded](https://developers.pismo.io/events/docs/interest-engine-interest-plan-creation-success-1) event.
>
> For more information, refer to the [Interest-bearing accounts](doc:interest-bearing-accounts) guide.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `InterestPlanRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_basis` | string (schema `AccrualBasis`) | yes | Method used to calculate interest accrual.<br>  * `BD/252`: Calculates daily interest using a 252-day year and the actual number of business days in each time period.<br>  * `ACTUAL/360`: Calculates daily interest using a 360-day year and the actual number of days in each time period.<br>  * `ACTUAL/365`: Calculates daily interest using a 365-day year and the actual number of days in each time period.<br>  * `ACTUAL/ACTUAL`: Calculates daily interest using the actual number of days in the year (which in the leap year is 366) and the actual number of days in each time period.<br> | enum: ["BD/252", "ACTUAL/360", "ACTUAL/365", "ACTUAL/ACTUAL"]; example: "ACTUAL/365" |
| `accrual_frequency` | string (schema `AccrualFrequency`) | yes | Interest accrual frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |
| `capitalization_frequency` | string (schema `CapitalizationFrequency`) | yes | Interest payout frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |
| `currency_code` | string (schema `CurrencyCode`) | yes | Numeric currency code in ISO 4217 standard. Only the following codes are accepted: 986 (BRL), 826 (GBP), 356 (INR), 840 (USD), 978 (EUR), 604 (PEN), 036 (AUD), 484 (MXN), 764 (THB), 208 (DKK), 752 (SEK), 578 (NOK). | enum: ["986", "826", "356", "840", "978", "604", "036", "484", "764", "208", "752", "578"]; format: "number"; example: "986" |
| `description` | string (schema `Description`) | yes | Interest plan name | example: "Banking plan" |
| `interest_type` | string (schema `InterestType`) | yes | Interest calculation type<br>- `SIMPLE`: Calculated on the original deposit or investment value.<br>- `COMPOUND`: Calculated on the original value plus the last accumulated interest.<br> | enum: ["SIMPLE", "COMPOUND"]; example: "SIMPLE" |
| `operation_type` | string (schema `OperationType`) | no | Operation type.<br>- `DEBIT`: Interest plan for debit type operations<br>- `CREDIT`: Interest plan for credit type operations<br> | enum: ["DEBIT", "CREDIT"]; example: "DEBIT" |
| `benchmark` | string (schema `Benchmark`) | no | Market index used to measure interest value over time. For fixed interest, this field must be null.<br>  - `BOE`: Bank of England, UK<br>  - `DI`: Interbank Deposit Contract, Brazil<br>  - `FED`: Federal Reserve System, USA<br>  - `RBA`: Reserve Bank of Australia<br>  - `RBI`: Reserve Bank of India<br>  - `TO`: Overnight Interbank Target Rate (Tasa Objetivo), Mexico<br> | enum: ["BOE", "DI", "FED", "RBA", "RBI", "TO"]; example: "FED" |
| `tax_withholding` | object (schema `TaxWithholding`) | no | Tax withholding configuration. Replaces the standalone `fee_processing_code` field.<br>Conditional rules enforced at creation/update time:<br>- `ACCRUAL`: `fee_processing_code` is required; `tax_rules` must be omitted.<br>- `CAPITALIZATION`: `tax_rules` is required; `fee_processing_code` must be omitted.<br>- Omitted `withholding_moment`: both `fee_processing_code` and `tax_rules` must be omitted.<br>In GET responses, legacy plans that predate this field may return `fee_processing_code` with a null `withholding_moment`.<br> |  |
| `fixed_interest_rate` | number (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "float"; example: 0.1 |
| `margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `margin_rate` | number \\\| null (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you don't pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `start_date` | string (schema `PlanStartDate`) | yes | Date to start applying the interest plan. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-17" |
| `division_id` | string (schema `DivisionId`) | no | Division ID attached to the interest plan for accrual by division | example: "d9b2c9e1-4633-4a10-841b-270f7f1493cd" |
| `interest_by_tiers` | object (schema `InterestByTiers`) | no | Interest by tiers configuration | example: {"type": "TERM", "tier_calculation": "RETROACTIVE", "tiers": [{"days": 30, "amount": 1000, "margin_rate": 1, "fixed_interest_rate": 1.2}, {"days": 60, "amount": 2000, "margin_rate": 1, "fixed_interest_rate": 1.3}]} |
| `interest_thresholds` | object (schema `InterestThresholds`) | no | Cap and floor thresholds for the interest plan | example: {"cap_threshold": 1.1, "cap_effective_rate": 1.2, "floor_threshold": 2.2, "floor_effective_rate": 2.1} |
| `interest_base_model` | string (schema `InterestBaseModel`) | no | Interest calculation model. `CLOSING-BALANCE` calculates interest on a single end-of-day balance snapshot. `BALANCE-CHANGE` calculates interest on each intraday balance movement (for example, credits and debits) as it occurs, so interest accrues on the balance held during each interval between consecutive movements rather than on one end-of-day figure. Defaults to `CLOSING-BALANCE`. | enum: ["CLOSING-BALANCE", "BALANCE-CHANGE"]; default: "CLOSING-BALANCE"; example: "CLOSING-BALANCE" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InterestPlanResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized. The response body is produced by the upstream authentication gateway and is not defined by this service. |  |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_plan_id` | string (schema `InterestPlanId`) | no | Interest plan ID generated during the plan's creation. Must be an alphanumeric UUID with the alphabetical characters in lowercase. | format: "UUID"; example: "07d84f79-3027-47bd-b628-65528ccc8fb2" |

##### Response 400

400 Example `validation` (Bean validation or binding errors):

```json
{
  "message": [
    "fixed_interest_rate must be informed",
    "margin_rate must be positive"
  ]
}
```

400 Example `requestBody` (invalid or missing request value):

```json
{
  "message": "Failed to process your request. Validate the fields in your request."
}
```

400 Example `tenantHeader` (Tenant header missing or malformed):

```json
{
  "message": "x-tenant header is missing or malformed"
}
```

400 Example `unknownField` (Unknown field in request body):

```json
{
  "error": "Invalid field in request",
  "message": "Field 'foo' is not allowed. Only the following fields can be updated: start_date, description, fixed_interest_rate, margin_rate, margin, interest_by_tiers, interest_thresholds",
  "field": "foo",
  "status": 400
}
```

400 Example `invalidJson` (Invalid JSON body):

```json
{
  "error": "Invalid JSON format",
  "message": "Request contains invalid JSON structure or field types",
  "status": 400
}
```

400 Example `taxWithholdingAccrualFeeRequired` (ACCRUAL withholding without fee_processing_code):

```json
{
  "message": [
    "fee_processing_code is required when tax_withholding.withholding_moment is ACCRUAL."
  ]
}
```

400 Example `taxWithholdingAccrualTaxRulesNotAllowed` (ACCRUAL withholding with tax_rules present):

```json
{
  "message": [
    "tax_rules must be null when tax_withholding.withholding_moment is ACCRUAL."
  ]
}
```

400 Example `taxWithholdingCapitalizationFeeNotAllowed` (CAPITALIZATION withholding with fee_processing_code present):

```json
{
  "message": [
    "fee_processing_code must be null when tax_withholding.withholding_moment is CAPITALIZATION."
  ]
}
```

400 Example `taxWithholdingCapitalizationTaxRulesRequired` (CAPITALIZATION withholding without tax_rules):

```json
{
  "message": [
    "tax_rules is required when tax_withholding.withholding_moment is CAPITALIZATION."
  ]
}
```

400 Example `taxWithholdingNoneFieldsNotAllowed` (NULL withholding_moment with fee_processing_code or tax_rules present):

```json
{
  "message": [
    "fee_processing_code and tax_rules must be null when tax_withholding.withholding_moment is NULL."
  ]
}
```

400 Example `taxWithholdingNotAllowedWhenTaxesExemption` (taxes_exemption is true with tax_withholding present):

```json
{
  "message": [
    "tax_withholding must be null when taxes_exemption is true."
  ]
}
```

##### Response 404

404 Example `interestAccountNotFound` (Interest account not found):

```json
{
  "message": "interest account not found"
}
```

404 Example `interestPlanNotFound` (Interest plan not found):

```json
{
  "message": "interest plan not found"
}
```

404 Example `benchmarkNotFound` (Benchmark not found):

```json
{
  "message": "benchmark not found"
}
```

##### Response 500

500 Example `example`:

```json
{
  "message": "Failed to process your request"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `interest-engine-interest-plan-creation-success-1` | https://developers.pismo.io/events/docs/interest-engine-interest-plan-creation-success-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-how-overdraft-works`, `KU-BANK-interest-bearing-accounts`, `KU-BANK-penalties-for-cd-accounts`, `KU-EVT-interest-management-data-events`, `KU-LEND-loan-products`.

<!-- op: spec=api-specs/Banking_-_Interest_engine.yaml method=GET path=/v1/interest/plan/{interestPlanId} operationId=get-v1-interest-plan -->
### `GET /v1/interest/plan/{interestPlanId}` — Get interest plan

- **operationId:** `get-v1-interest-plan`
- **Specification:** `api-specs/Banking_-_Interest_engine.yaml` (Banking - Interest engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/interest-engine`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Interest engine`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get interest plan details. By default, returns the latest version of the interest plan.
> You can optionally specify a `version_date` query parameter to retrieve the version that was active on a specific date.
> If a `version_date` is provided, the endpoint returns the latest version with a start date less than or equal to the specified date.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `interestPlanId` | path | yes | string | Interest plan ID generated during the plan's creation. Must be an alphanumeric UUID with the alphabetical characters in lowercase. | example: "d9b2c9e1-4633-4a10-841b-270f7f1493cd" |
| `version_date` | query | no | string | Optional date to retrieve a specific version of the interest plan. If not provided, returns the latest version. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-17" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetInterestPlanResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized. The response body is produced by the upstream authentication gateway and is not defined by this service. |  |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_plan_id` | string (schema `InterestPlanId`) | no | Interest plan ID generated during the plan's creation. Must be an alphanumeric UUID with the alphabetical characters in lowercase. | format: "UUID"; example: "07d84f79-3027-47bd-b628-65528ccc8fb2" |
| `org_id` | string (schema `OrgId`) | no | Organization ID generated in the onboarding process | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `description` | string (schema `Description`) | no | Interest plan name | example: "Banking plan" |
| `currency_code` | string (schema `CurrencyCode`) | no | Numeric currency code in ISO 4217 standard. Only the following codes are accepted: 986 (BRL), 826 (GBP), 356 (INR), 840 (USD), 978 (EUR), 604 (PEN), 036 (AUD), 484 (MXN), 764 (THB), 208 (DKK), 752 (SEK), 578 (NOK). | enum: ["986", "826", "356", "840", "978", "604", "036", "484", "764", "208", "752", "578"]; format: "number"; example: "986" |
| `benchmark` | string (schema `BenchmarkResponse`) | no | Market index returned in responses.<br>  - `BOE`: Bank of England, UK<br>  - `DI`: Interbank Deposit Contract, Brazil<br>  - `FED`: Federal Reserve System, USA<br>  - `FIXED`: Fixed interest rate, no market index<br>  - `RBA`: Reserve Bank of Australia<br>  - `RBI`: Reserve Bank of India<br>  - `TO`: Overnight Interbank Target Rate (Tasa Objetivo), Mexico<br> | enum: ["BOE", "DI", "FED", "FIXED", "RBA", "RBI", "TO"]; example: "FIXED" |
| `fixed_interest_rate` | number (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "float"; example: 0.1 |
| `margin_rate` | number \\\| null (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you don't pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `tax_withholding` | object (schema `TaxWithholding`) | no | Tax withholding configuration. Replaces the standalone `fee_processing_code` field.<br>Conditional rules enforced at creation/update time:<br>- `ACCRUAL`: `fee_processing_code` is required; `tax_rules` must be omitted.<br>- `CAPITALIZATION`: `tax_rules` is required; `fee_processing_code` must be omitted.<br>- Omitted `withholding_moment`: both `fee_processing_code` and `tax_rules` must be omitted.<br>In GET responses, legacy plans that predate this field may return `fee_processing_code` with a null `withholding_moment`.<br> |  |
| `accrual_basis` | string (schema `AccrualBasis`) | no | Method used to calculate interest accrual.<br>  * `BD/252`: Calculates daily interest using a 252-day year and the actual number of business days in each time period.<br>  * `ACTUAL/360`: Calculates daily interest using a 360-day year and the actual number of days in each time period.<br>  * `ACTUAL/365`: Calculates daily interest using a 365-day year and the actual number of days in each time period.<br>  * `ACTUAL/ACTUAL`: Calculates daily interest using the actual number of days in the year (which in the leap year is 366) and the actual number of days in each time period.<br> | enum: ["BD/252", "ACTUAL/360", "ACTUAL/365", "ACTUAL/ACTUAL"]; example: "ACTUAL/365" |
| `interest_type` | string (schema `InterestType`) | no | Interest calculation type<br>- `SIMPLE`: Calculated on the original deposit or investment value.<br>- `COMPOUND`: Calculated on the original value plus the last accumulated interest.<br> | enum: ["SIMPLE", "COMPOUND"]; example: "SIMPLE" |
| `operation_type` | string (schema `OperationType`) | no | Operation type.<br>- `DEBIT`: Interest plan for debit type operations<br>- `CREDIT`: Interest plan for credit type operations<br> | enum: ["DEBIT", "CREDIT"]; example: "DEBIT" |
| `status` | string (schema `Status`) | no | Interest plan status. Must be set to `ACTIVE`. | enum: ["ACTIVE"]; example: "ACTIVE" |
| `start_date` | string (schema `PlanStartDate`) | no | Date to start applying the interest plan. Format = YYYY-MM-DD. | format: "date"; example: "2025-06-17" |
| `capitalization_frequency` | string (schema `CapitalizationFrequency`) | no | Interest payout frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |
| `accrual_frequency` | string (schema `AccrualFrequency`) | no | Interest accrual frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |
| `interest_by_tiers` | object (schema `InterestByTiers`) | no | Interest by tiers configuration | example: {"type": "TERM", "tier_calculation": "RETROACTIVE", "tiers": [{"days": 30, "amount": 1000, "margin_rate": 1, "fixed_interest_rate": 1.2}, {"days": 60, "amount": 2000, "margin_rate": 1, "fixed_interest_rate": 1.3}]} |
| `interest_thresholds` | object (schema `InterestThresholds`) | no | Cap and floor thresholds for the interest plan | example: {"cap_threshold": 1.1, "cap_effective_rate": 1.2, "floor_threshold": 2.2, "floor_effective_rate": 2.1} |
| `interest_base_model` | string (schema `InterestBaseModel`) | no | Interest calculation model. `CLOSING-BALANCE` calculates interest on a single end-of-day balance snapshot. `BALANCE-CHANGE` calculates interest on each intraday balance movement (for example, credits and debits) as it occurs, so interest accrues on the balance held during each interval between consecutive movements rather than on one end-of-day figure. Defaults to `CLOSING-BALANCE`. | enum: ["CLOSING-BALANCE", "BALANCE-CHANGE"]; default: "CLOSING-BALANCE"; example: "CLOSING-BALANCE" |

##### Response 400

400 Example `validation` (Bean validation or binding errors):

```json
{
  "message": [
    "fixed_interest_rate must be informed",
    "margin_rate must be positive"
  ]
}
```

400 Example `requestBody` (invalid or missing request value):

```json
{
  "message": "Failed to process your request. Validate the fields in your request."
}
```

400 Example `tenantHeader` (Tenant header missing or malformed):

```json
{
  "message": "x-tenant header is missing or malformed"
}
```

400 Example `unknownField` (Unknown field in request body):

```json
{
  "error": "Invalid field in request",
  "message": "Field 'foo' is not allowed. Only the following fields can be updated: start_date, description, fixed_interest_rate, margin_rate, margin, interest_by_tiers, interest_thresholds",
  "field": "foo",
  "status": 400
}
```

400 Example `invalidJson` (Invalid JSON body):

```json
{
  "error": "Invalid JSON format",
  "message": "Request contains invalid JSON structure or field types",
  "status": 400
}
```

400 Example `taxWithholdingAccrualFeeRequired` (ACCRUAL withholding without fee_processing_code):

```json
{
  "message": [
    "fee_processing_code is required when tax_withholding.withholding_moment is ACCRUAL."
  ]
}
```

400 Example `taxWithholdingAccrualTaxRulesNotAllowed` (ACCRUAL withholding with tax_rules present):

```json
{
  "message": [
    "tax_rules must be null when tax_withholding.withholding_moment is ACCRUAL."
  ]
}
```

400 Example `taxWithholdingCapitalizationFeeNotAllowed` (CAPITALIZATION withholding with fee_processing_code present):

```json
{
  "message": [
    "fee_processing_code must be null when tax_withholding.withholding_moment is CAPITALIZATION."
  ]
}
```

400 Example `taxWithholdingCapitalizationTaxRulesRequired` (CAPITALIZATION withholding without tax_rules):

```json
{
  "message": [
    "tax_rules is required when tax_withholding.withholding_moment is CAPITALIZATION."
  ]
}
```

400 Example `taxWithholdingNoneFieldsNotAllowed` (NULL withholding_moment with fee_processing_code or tax_rules present):

```json
{
  "message": [
    "fee_processing_code and tax_rules must be null when tax_withholding.withholding_moment is NULL."
  ]
}
```

400 Example `taxWithholdingNotAllowedWhenTaxesExemption` (taxes_exemption is true with tax_withholding present):

```json
{
  "message": [
    "tax_withholding must be null when taxes_exemption is true."
  ]
}
```

##### Response 404

404 Example `interestAccountNotFound` (Interest account not found):

```json
{
  "message": "interest account not found"
}
```

404 Example `interestPlanNotFound` (Interest plan not found):

```json
{
  "message": "interest plan not found"
}
```

404 Example `benchmarkNotFound` (Benchmark not found):

```json
{
  "message": "benchmark not found"
}
```

##### Response 500

500 Example `example`:

```json
{
  "message": "Failed to process your request"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Interest_engine.yaml method=PATCH path=/v1/interest/plan/{interestPlanId} operationId=patch-v1-interest-plan -->
### `PATCH /v1/interest/plan/{interestPlanId}` — Create interest plan version

- **operationId:** `patch-v1-interest-plan`
- **Specification:** `api-specs/Banking_-_Interest_engine.yaml` (Banking - Interest engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/interest-engine`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Interest engine`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a new version of an existing interest plan. This endpoint allows you to update specific fields while preserving others from the previous version.
>
> Key features:
> - Creates a new version with the specified `start_date`.
> - Updates only the provided fields—any field not specified inherits the value from the previous version.
> - Validates that the new `start_date` is after the `start_date` of the previous version.
> - Maintains immutable fields like `interest_type` and `tier_calculation`.
> - Preserves existing tiers when updating `interest_by_tiers`—only specified tiers are updated.
>
> This endpoint generates an [Interest plan created](https://developers.pismo.io/events/docs/interest-engine-interest-plan-creation-success-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `interestPlanId` | path | yes | string | Interest plan ID generated during the plan's creation. Must be an alphanumeric UUID with the alphabetical characters in lowercase. | example: "d9b2c9e1-4633-4a10-841b-270f7f1493cd" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `InterestPlanVersionRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `start_date` | string (schema `StartDateForNewVersion`) | yes | Date to start applying the new interest plan version. Format = YYYY-MM-DD. Must be greater than or equal to current date. | format: "date"; example: "2025-06-17" |
| `description` | string (schema `Description`) | no | Interest plan name | example: "Banking plan" |
| `fixed_interest_rate` | number (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "float"; example: 0.1 |
| `margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `margin_rate` | number \\\| null (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you don't pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `interest_by_tiers` | object (schema `InterestByTiers`) | no | Interest by tiers configuration | example: {"type": "TERM", "tier_calculation": "RETROACTIVE", "tiers": [{"days": 30, "amount": 1000, "margin_rate": 1, "fixed_interest_rate": 1.2}, {"days": 60, "amount": 2000, "margin_rate": 1, "fixed_interest_rate": 1.3}]} |
| `interest_thresholds` | object (schema `InterestThresholds`) | no | Cap and floor thresholds for the interest plan | example: {"cap_threshold": 1.1, "cap_effective_rate": 1.2, "floor_threshold": 2.2, "floor_effective_rate": 2.1} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InterestPlanVersionResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized. The response body is produced by the upstream authentication gateway and is not defined by this service. |  |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict: A version with this start date already exists | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_plan_id` | string (schema `InterestPlanId`) | no | Interest plan ID generated during the plan's creation. Must be an alphanumeric UUID with the alphabetical characters in lowercase. | format: "UUID"; example: "07d84f79-3027-47bd-b628-65528ccc8fb2" |
| `version` | string | no | ID for the new interest plan version | example: "2025-06-17" |

##### Response 400

400 Example `validation` (Bean validation or binding errors):

```json
{
  "message": [
    "fixed_interest_rate must be informed",
    "margin_rate must be positive"
  ]
}
```

400 Example `requestBody` (invalid or missing request value):

```json
{
  "message": "Failed to process your request. Validate the fields in your request."
}
```

400 Example `tenantHeader` (Tenant header missing or malformed):

```json
{
  "message": "x-tenant header is missing or malformed"
}
```

400 Example `unknownField` (Unknown field in request body):

```json
{
  "error": "Invalid field in request",
  "message": "Field 'foo' is not allowed. Only the following fields can be updated: start_date, description, fixed_interest_rate, margin_rate, margin, interest_by_tiers, interest_thresholds",
  "field": "foo",
  "status": 400
}
```

400 Example `invalidJson` (Invalid JSON body):

```json
{
  "error": "Invalid JSON format",
  "message": "Request contains invalid JSON structure or field types",
  "status": 400
}
```

400 Example `taxWithholdingAccrualFeeRequired` (ACCRUAL withholding without fee_processing_code):

```json
{
  "message": [
    "fee_processing_code is required when tax_withholding.withholding_moment is ACCRUAL."
  ]
}
```

400 Example `taxWithholdingAccrualTaxRulesNotAllowed` (ACCRUAL withholding with tax_rules present):

```json
{
  "message": [
    "tax_rules must be null when tax_withholding.withholding_moment is ACCRUAL."
  ]
}
```

400 Example `taxWithholdingCapitalizationFeeNotAllowed` (CAPITALIZATION withholding with fee_processing_code present):

```json
{
  "message": [
    "fee_processing_code must be null when tax_withholding.withholding_moment is CAPITALIZATION."
  ]
}
```

400 Example `taxWithholdingCapitalizationTaxRulesRequired` (CAPITALIZATION withholding without tax_rules):

```json
{
  "message": [
    "tax_rules is required when tax_withholding.withholding_moment is CAPITALIZATION."
  ]
}
```

400 Example `taxWithholdingNoneFieldsNotAllowed` (NULL withholding_moment with fee_processing_code or tax_rules present):

```json
{
  "message": [
    "fee_processing_code and tax_rules must be null when tax_withholding.withholding_moment is NULL."
  ]
}
```

400 Example `taxWithholdingNotAllowedWhenTaxesExemption` (taxes_exemption is true with tax_withholding present):

```json
{
  "message": [
    "tax_withholding must be null when taxes_exemption is true."
  ]
}
```

##### Response 404

404 Example `interestAccountNotFound` (Interest account not found):

```json
{
  "message": "interest account not found"
}
```

404 Example `interestPlanNotFound` (Interest plan not found):

```json
{
  "message": "interest plan not found"
}
```

404 Example `benchmarkNotFound` (Benchmark not found):

```json
{
  "message": "benchmark not found"
}
```

##### Response 409

409 Example `example`:

```json
{
  "message": "Conflict: Version with this start date already exists"
}
```

##### Response 500

500 Example `example`:

```json
{
  "message": "Failed to process your request"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `interest-engine-interest-plan-creation-success-1` | https://developers.pismo.io/events/docs/interest-engine-interest-plan-creation-success-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;409;500`, has examples `False`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/TaxWithholding -->
### Schema `TaxWithholding`

Pointer: `#/components/schemas/TaxWithholding`. Type: object (schema `TaxWithholding`).

> Tax withholding configuration. Replaces the standalone `fee_processing_code` field.
> Conditional rules enforced at creation/update time:
> - `ACCRUAL`: `fee_processing_code` is required; `tax_rules` must be omitted.
> - `CAPITALIZATION`: `tax_rules` is required; `fee_processing_code` must be omitted.
> - Omitted `withholding_moment`: both `fee_processing_code` and `tax_rules` must be omitted.
> In GET responses, legacy plans that predate this field may return `fee_processing_code` with a null `withholding_moment`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `withholding_moment` | string (schema `WithholdingMoment`) | yes | Moment at which tax is withheld. When omitted, no withholding applies. | enum: ["ACCRUAL", "CAPITALIZATION"]; example: "ACCRUAL" |
| `fee_processing_code` | string (schema `FeeProcessingCode`) | no | Processing code configured in the [fee model](doc:fee-model) for charging a tax, penalty, or fee. | format: "number"; example: "001100" |
| `tax_rules` | array of object (schema `TaxRule`) | no |  | maxItems: 100 |

<!-- schema: #/components/schemas/InterestByTiers -->
### Schema `InterestByTiers`

Pointer: `#/components/schemas/InterestByTiers`. Type: object (schema `InterestByTiers`).

> Interest by tiers configuration

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `InterestByTiersType`) | yes | Interest type<br>- `TERM`: Interest rate varies according to the period of time since the deposit was made.<br>- `AMOUNT`: Interest rate varies according to the current balance.<br> | enum: ["TERM", "AMOUNT"]; example: "TERM" |
| `tier_calculation` | string (schema `TierCalculation`) | yes | Tier calculation method<br>- `RETROACTIVE`: Interest is recalculated from the beginning based on the new applicable rate.<br>- `NON-RETROACTIVE`: Interest is calculated progressively based on each layer rate.<br> | enum: ["RETROACTIVE", "NON-RETROACTIVE"]; example: "RETROACTIVE" |
| `tiers` | array of object (schema `InterestByTiersArrayObject`) | yes |  |  |

<!-- schema: #/components/schemas/InterestThresholds -->
### Schema `InterestThresholds`

Pointer: `#/components/schemas/InterestThresholds`. Type: object (schema `InterestThresholds`).

> Cap and floor thresholds for the interest plan

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cap_threshold` | number (schema `CapThreshold`) | no | Cap threshold value. If you pass a value for `cap_threshold`, you must also pass a value for `cap_effective_rate`. | format: "double"; example: 1.1 |
| `cap_effective_rate` | number (schema `CapEffectiveRate`) | no | Cap effective rate. If you pass a value for `cap_effective_rate`, you must also pass a value for `cap_threshold`. | format: "double"; example: 1.2 |
| `floor_threshold` | number (schema `FloorThreshold`) | no | Floor threshold value | format: "double"; example: 2.1 |
| `floor_effective_rate` | number (schema `FloorEffectiveRate`) | no | Floor effective rate | format: "double"; example: 2.2 |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error payload generated by the global exception handler.
> `message` is a single string for most errors and an array of strings
> when multiple bean-validation or request-binding errors occur in the same request.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | oneOf: string, array of string | yes |  |  |

<!-- schema: #/components/schemas/ErrorResponseDeserialization -->
### Schema `ErrorResponseDeserialization`

Pointer: `#/components/schemas/ErrorResponseDeserialization`. Type: object (schema `ErrorResponseDeserialization`).

> Error payload generated only when the request body fails JSON deserialization
> (unknown field or invalid JSON structure). Returned with HTTP 400.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error` | string | yes | Short error category. |  |
| `message` | string | no | Details about the field or structure that causes the error. |  |
| `field` | string | no | Name of the invalid field. Present only for unknown-field errors. |  |
| `status` | integer | yes | HTTP status code, always 400 for this shape. |  |

<!-- schema: #/components/schemas/TaxRule -->
### Schema `TaxRule`

Pointer: `#/components/schemas/TaxRule`. Type: object (schema `TaxRule`).

> A single tax rule applied within a tax withholding configuration.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | yes | Description of the tax rule. | maxLength: 128; example: "IOF" |
| `fixed_percentage` | number | yes | Fixed percentage applied by the tax rule. | example: 0.0038 |
| `threshold_amount` | number \\\| null | no | Optional monetary threshold amount associated with the tax rule. Use null when the rule does not depend on a threshold. | format: "double"; example: null |

<!-- schema: #/components/schemas/InterestByTiersArrayObject -->
### Schema `InterestByTiersArrayObject`

Pointer: `#/components/schemas/InterestByTiersArrayObject`. Type: object (schema `InterestByTiersArrayObject`).

> Tier details for interest calculation

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `days` | integer (schema `Days`) | no | Number of days in `interest_by_tier` | format: "int32"; example: 30 |
| `amount` | number \\\| null (schema `Amount`) | no | Amount in the `interest_by_tier` | format: "double"; example: 1000 |
| `margin_rate` | number \\\| null (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you don't pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `fixed_interest_rate` | number (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "float"; example: 0.1 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Interest_engine.yaml` | tag `Interest engine`: GET /v1/interest/plan, POST /v1/interest/plan, GET /v1/interest/plan/{interestPlanId}, PATCH /v1/interest/plan/{interestPlanId} | https://github.com/PismoDevEx/pismo-api-specs | `93ec981c793eff61…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-how-overdraft-works` — How overdraft works
- `KU-BANK-interest-bearing-accounts` — Interest-bearing accounts
- `KU-BANK-penalties-for-cd-accounts` — Penalties and taxes for CD accounts
- `KU-EVT-catalogue-interest` — Event catalogue: interest
- `KU-EVT-interest-management-data-events` — Banking - Interest management
- `KU-LEND-loan-products` — Loan products: overview and creation
