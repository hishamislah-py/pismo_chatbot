---
ku_id: KU-API-banking-interest-management--interest-plan
title: 'API reference: Banking - Interest management for B3-listed products — Interest plan'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Interest_management.yaml
  sha256: 3ea9e4fd670aed59a95c466526c853b12511bbdaf3da239d5da4e460f7bb756e
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
- post-v1-interest-plan-b3
- get-v1-interest-plan-b3
related_kus:
- KU-EVT-catalogue-interest
specification_version: 1.0.0
---

# API reference: Banking - Interest management for B3-listed products — Interest plan

**KU ID:** `KU-API-banking-interest-management--interest-plan` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Interest plan` in `api-specs/Banking_-_Interest_management.yaml` (“Banking - Interest management for B3-listed products”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage interest plans

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/interest/plan` | `post-v1-interest-plan-b3` | Create interest plan for B3-listed products | no |
| `GET /v1/interest/plan/{interestPlanId}` | `get-v1-interest-plan-b3` | Get interest plan for B3-listed products | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest_management.yaml method=POST path=/v1/interest/plan operationId=post-v1-interest-plan-b3 -->
### `POST /v1/interest/plan` — Create interest plan for B3-listed products

- **operationId:** `post-v1-interest-plan-b3`
- **Specification:** `api-specs/Banking_-_Interest_management.yaml` (Banking - Interest management for B3-listed products)
- **Server base URL(s):** `https://sandbox-integration.pismolabs.io/interest-management`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Interest plan`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates an interest plan configuration that defines how the platform calculates interest accrual.
>
> **Note:** Only Brazilian Stock Exchange (B3) customers should use this endpoint.
>
> Once created, you can apply the interest plan to a specific product or account. For example, you can provide the `interest_plan_id` when creating a [deposit product](ref:interest-bearing-v1-create-deposit-product), when creating a [savings account](ref:interest-bearing-v1-create-savings-account-product), or when [depositing money](ref:post-v1-interest-deposit) into an account.
>
> This endpoint generates an [Interest plan creation succeeded](https://developers.pismo.io/events/docs/interest-management-interest-plan-creation-success-1) event.
>
> For more information, refer to the [Interest-bearing accounts](doc:interest-bearing-accounts) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `authorization` | header | yes | string | Authorization | example: "Bearer ac194ce4-ecbe-4007-91bd-94babf388e7278f243bc-4ad8-4ead-a2c3-f42a548fe760" |
| `content-type` | header | yes | string | Content type | example: "application/json" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `InterestPlanRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_basis` | string (schema `AccrualBasis`) | yes | Method used to calculate interest accrual.<br>  * `BD/252`: Calculates daily interest using a 252-day year and the actual number of business days in each time period.<br>  * `ACTUAL/360`: Calculates daily interest using a 360-day year and the actual number of days in each time period.<br>  * `ACTUAL/365`: Calculates daily interest using a 365-day year and the actual number of days in each time period.<br>  * `ACTUAL/ACTUAL`: Calculates daily interest using the actual number of days in the year (which in the leap year is 366) and the actual number of days in each time period.<br> | enum: ["BD/252", "ACTUAL/360", "ACTUAL/365", "ACTUAL/ACTUAL"]; example: "ACTUAL/365" |
| `accrual_frequency` | string (schema `AccrualFrequency`) | yes | Interest accrual frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF-YEARLY", "YEARLY"]; example: "DAILY" |
| `capitalisation_frequency` | string (schema `CapitalisationFrequency`) | yes | Interest payout frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF-YEARLY", "YEARLY"]; example: "DAILY" |
| `currency_code` | string (schema `CurrencyCode`) | yes | Numeric currency code in ISO 4217 standard | format: "number"; example: "986" |
| `description` | string (schema `Description`) | yes | Interest plan name | example: "Banking plan" |
| `interest_type` | string (schema `InterestType`) | yes | Interest calculation type.<br>- SIMPLE: Calculated on the original deposit or investment value.<br>- COMPOUND: Calculated on the original value plus the last accumulated interest.<br> | enum: ["SIMPLE", "COMPOUND"]; example: "SIMPLE" |
| `benchmark` | string (schema `Benchmark`) | no | Market index used to measure interest value over time. For fixed interest, this field must be null.<br>  - BOE: Bank of England, UK<br>  - DI: Interbank Deposit Contract, Brazil<br>  - FED: Federal Reserve System, USA<br>  - RBA: Reserve Bank of Australia<br>  - RBI: Reserve Bank of India   <br> | enum: ["BOE", "DI", "FED", "RBA", "RBI"]; example: "FED" |
| `fee_processing_code` | string (schema `FeeProcessingCode`) | no | Processing code configured in the [fee model](doc:fee-model) for charging a tax, penalty, or fee. | format: "number"; example: "001100" |
| `fixed_interest_rate` | string (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "number"; example: "0.10" |
| `margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `margin_rate` | number (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you do not pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InterestPlanResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized access | `application/json`: object |
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
  "message": "Field 'foo' is not allowed. Only the following fields can be updated: start_date, description, benchmark, fixed_interest_rate, margin_rate, margin, interest_by_tiers, interest_thresholds",
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
  "message": "Interest plan not found"
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
| `interest-management-interest-plan-creation-success-1` | https://developers.pismo.io/events/docs/interest-management-interest-plan-creation-success-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `False`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Interest_management.yaml method=GET path=/v1/interest/plan/{interestPlanId} operationId=get-v1-interest-plan-b3 -->
### `GET /v1/interest/plan/{interestPlanId}` — Get interest plan for B3-listed products

- **operationId:** `get-v1-interest-plan-b3`
- **Specification:** `api-specs/Banking_-_Interest_management.yaml` (Banking - Interest management for B3-listed products)
- **Server base URL(s):** `https://sandbox-integration.pismolabs.io/interest-management`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Interest plan`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get interest plan details.
>
> **Note:** Only Brazilian Stock Exchange (B3) customers should use this endpoint.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `authorization` | header | yes | string | Authorization | example: "Bearer ac194ce4-ecbe-4007-91bd-94babf388e7278f243bc-4ad8-4ead-a2c3-f42a548fe760" |
| `interestPlanId` | path | yes | string | Interest plan ID generated during the plan's creation. Must be an alphanumeric UUID with the alphabetical characters in lowercase. | example: "d9b2c9e1-4633-4a10-841b-270f7f1493cd" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetInterestPlanResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized access | `application/json`: object |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_plan_id` | string (schema `InterestPlanId`) | no | Interest plan ID generated during the plan's creation. Must be an alphanumeric UUID with the alphabetical characters in lowercase. | format: "UUID"; example: "07d84f79-3027-47bd-b628-65528ccc8fb2" |
| `org_id` | string (schema `OrgId`) | no | Organization ID generated in the onboarding process | example: "TN-cc8f8b89-233a-4582-9f36-63ee85278d6d" |
| `description` | string (schema `Description`) | no | Interest plan name | example: "Banking plan" |
| `currency_code` | string (schema `CurrencyCode`) | no | Numeric currency code in ISO 4217 standard | format: "number"; example: "986" |
| `benchmark` | string (schema `Benchmark`) | no | Market index used to measure interest value over time. For fixed interest, this field must be null.<br>  - BOE: Bank of England, UK<br>  - DI: Interbank Deposit Contract, Brazil<br>  - FED: Federal Reserve System, USA<br>  - RBA: Reserve Bank of Australia<br>  - RBI: Reserve Bank of India   <br> | enum: ["BOE", "DI", "FED", "RBA", "RBI"]; example: "FED" |
| `fixed_interet_rate` | string (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "number"; example: "0.10" |
| `margin_rate` | number (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you do not pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `fee_processing_code` | string (schema `FeeProcessingCode`) | no | Processing code configured in the [fee model](doc:fee-model) for charging a tax, penalty, or fee. | format: "number"; example: "001100" |
| `accrual_basis` | string (schema `AccrualBasis`) | no | Method used to calculate interest accrual.<br>  * `BD/252`: Calculates daily interest using a 252-day year and the actual number of business days in each time period.<br>  * `ACTUAL/360`: Calculates daily interest using a 360-day year and the actual number of days in each time period.<br>  * `ACTUAL/365`: Calculates daily interest using a 365-day year and the actual number of days in each time period.<br>  * `ACTUAL/ACTUAL`: Calculates daily interest using the actual number of days in the year (which in the leap year is 366) and the actual number of days in each time period.<br> | enum: ["BD/252", "ACTUAL/360", "ACTUAL/365", "ACTUAL/ACTUAL"]; example: "ACTUAL/365" |
| `interest_type` | string (schema `InterestType`) | no | Interest calculation type.<br>- SIMPLE: Calculated on the original deposit or investment value.<br>- COMPOUND: Calculated on the original value plus the last accumulated interest.<br> | enum: ["SIMPLE", "COMPOUND"]; example: "SIMPLE" |
| `capitalisation_frequency` | string (schema `CapitalisationFrequency`) | no | Interest payout frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF-YEARLY", "YEARLY"]; example: "DAILY" |
| `accrual_frequency` | string (schema `AccrualFrequency`) | no | Interest accrual frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF-YEARLY", "YEARLY"]; example: "DAILY" |

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
  "message": "Field 'foo' is not allowed. Only the following fields can be updated: start_date, description, benchmark, fixed_interest_rate, margin_rate, margin, interest_by_tiers, interest_thresholds",
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
  "message": "Interest plan not found"
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

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

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

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Interest_management.yaml` | tag `Interest plan`: POST /v1/interest/plan, GET /v1/interest/plan/{interestPlanId} | https://github.com/PismoDevEx/pismo-api-specs | `3ea9e4fd670aed59…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-EVT-catalogue-interest` — Event catalogue: interest
