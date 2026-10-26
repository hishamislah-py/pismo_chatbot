---
ku_id: KU-API-banking-interest-engine--account-interest
title: 'API reference: Banking - Interest engine — Account interest'
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
operations:
- get-v1-interest-account
- put-v1-interest-account
related_kus:
- KU-AUTH-account-and-external-id-tokens
specification_version: 1.0.0
---

# API reference: Banking - Interest engine — Account interest

**KU ID:** `KU-API-banking-interest-engine--account-interest` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Account interest` in `api-specs/Banking_-_Interest_engine.yaml` (“Banking - Interest engine”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage account interest

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/interest/account/{accountId}` | `get-v1-interest-account` | Get account interest | no |
| `PUT /v1/interest/account/{accountId}` | `put-v1-interest-account` | Update account interest | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest_engine.yaml method=GET path=/v1/interest/account/{accountId} operationId=get-v1-interest-account -->
### `GET /v1/interest/account/{accountId}` — Get account interest

- **operationId:** `get-v1-interest-account`
- **Specification:** `api-specs/Banking_-_Interest_engine.yaml` (Banking - Interest engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/interest-engine`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Account interest`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get account interest details.
>
> **Account identification.** The token identifies the account—the path alone is not
> enough. Exactly one of `x-account-id` or `x-external-account-id` must be passed and must
> match the `{accountId}` path parameter. Otherwise the request is rejected (`403` on a
> mismatch or when neither header is passed, `400` when both are).
>
> **Identifier validation.** The ID encoded in the token is confirmed to exist by calling
> an external API before the interest account is read:
>
> - `x-account-id`: An Accounts API call confirms the account ID exists. If it does not,
>   the request fails with `400` and `account_id not found`.
> - `x-external-account-id`: A Corporate API call resolves the external account ID to a
>   Pismo `account_id`. If the external account ID does not exist, the request fails with
>   `400` and `external_account_id not found`.
>
> A `404` means the identifier is valid but the account has no interest configuration.
> Any other failure of those APIs fails with `500`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID. Must match the account encoded in the account token. This can be a Pismo account ID or an external account ID. A mismatch is rejected with `403 Forbidden`. Maximum 60 characters. | example: "8080" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetInterestAccountResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized. The response body is produced by the upstream authentication gateway and is not defined by this service. |  |
| 403 | Forbidden | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `benchmark` | string (schema `BenchmarkResponse`) | no | Market index returned in responses.<br>  - `BOE`: Bank of England, UK<br>  - `DI`: Interbank Deposit Contract, Brazil<br>  - `FED`: Federal Reserve System, USA<br>  - `FIXED`: Fixed interest rate, no market index<br>  - `RBA`: Reserve Bank of Australia<br>  - `RBI`: Reserve Bank of India<br>  - `TO`: Overnight Interbank Target Rate (Tasa Objetivo), Mexico<br> | enum: ["BOE", "DI", "FED", "FIXED", "RBA", "RBI", "TO"]; example: "FIXED" |
| `fixed_interest_rate` | number (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "float"; example: 0.1 |
| `margin_rate` | number \\\| null (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you don't pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `tax_withholding` | object (schema `TaxWithholding`) | no | Tax withholding configuration. Replaces the standalone `fee_processing_code` field.<br>Conditional rules enforced at creation/update time:<br>- `ACCRUAL`: `fee_processing_code` is required; `tax_rules` must be omitted.<br>- `CAPITALIZATION`: `tax_rules` is required; `fee_processing_code` must be omitted.<br>- Omitted `withholding_moment`: both `fee_processing_code` and `tax_rules` must be omitted.<br>In GET responses, legacy plans that predate this field may return `fee_processing_code` with a null `withholding_moment`.<br> |  |
| `taxes_exemption` | boolean (schema `TaxesExemption`) | no | Is the account exempt from taxes? | example: true |
| `interest_by_tiers` | object (schema `InterestByTiers`) | no | Interest by tiers configuration | example: {"type": "TERM", "tier_calculation": "RETROACTIVE", "tiers": [{"days": 30, "amount": 1000, "margin_rate": 1, "fixed_interest_rate": 1.2}, {"days": 60, "amount": 2000, "margin_rate": 1, "fixed_interest_rate": 1.3}]} |
| `capitalization_frequency` | string (schema `CapitalizationFrequency`) | no | Account-level capitalization frequency configured for the interest account. Returned only when explicitly configured at account level. If not returned, the account uses the capitalization frequency from the associated interest plan during processing. | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |
| `external_account_id` | string (schema `ExternalAccountId`) | no | This is the external account ID parsed from a request's account token. Returned only when a request was made with an external ID token. Omitted otherwise, including if the request used a Pismo account ID token, even if an external account ID was previously stored. | maxLength: 60; example: "account-xyz-987" |
| `account_id` | string | no | Pismo account ID. Returned only when the request was authenticated with a Pismo account ID token. Omitted otherwise. | example: "8080" |

##### Response 400

400 Example `tenantHeader` (Tenant header missing or malformed):

```json
{
  "message": "x-tenant header is missing or malformed"
}
```

400 Example `accountIdNotValid` (Invalid account ID):

```json
{
  "message": "this account_id is not valid"
}
```

400 Example `accountIdentifierNotValid` (Invalid account identifier):

```json
{
  "message": "this account identifier is not valid"
}
```

400 Example `missingAccountID` (Account ID not passed):

```json
{
  "message": "account_id must be informed"
}
```

400 Example `xAccountIdAndXExternalAccountIdBothPassed` (x-account-id and x-external-account-id both passed):

```json
{
  "message": "x-account-id and x-external-account-id must not be informed together"
}
```

400 Example `accountIdNotFound` (Account ID not found):

```json
{
  "message": "account_id not found"
}
```

400 Example `externalAccountIdNotFound` (External account ID not found):

```json
{
  "message": "external_account_id not found"
}
```

##### Response 403

403 Example `example`:

```json
{
  "message": "This request is forbidden"
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


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Interest_engine.yaml method=PUT path=/v1/interest/account/{accountId} operationId=put-v1-interest-account -->
### `PUT /v1/interest/account/{accountId}` — Update account interest

- **operationId:** `put-v1-interest-account`
- **Specification:** `api-specs/Banking_-_Interest_engine.yaml` (Banking - Interest engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/interest-engine`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Account interest`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Apply specific interest accrual options to an account by replacing its full interest
> configuration.
>
> This operation has full-replacement semantics: every request must redeclare the complete
> configuration. Partial updates (sending only the fields you want to change) are not
> supported and cause the validation to fail.
>
> Although every property in the request body is independently optional, the body as a
> whole must satisfy several conditional rules. See the request body schema description
> for the full set of `benchmark`/`fixed_interest_rate`,
> `tax_withholding`, and `taxes_exemption` rules.
>
> **Account identification.** The token identifies the account. Exactly one of
> `x-account-id` or `x-external-account-id` must be passed and must match the
> `{accountId}` path parameter. Otherwise the request is rejected (`403` on a mismatch or
> when neither header is passed, `400` when both are).
>
> **Stored identifiers.** Which identifiers are stored follows the header used:
>
> - `x-account-id`: An Accounts API call confirms the account ID exists, then `account_id`
>   is stored and `external_account_id` is stored as `null` - **any external account ID
>   previously stored for this account is cleared**.
> - `x-external-account-id`: A Corporate API call resolves the external account ID to a
>   Pismo `account_id`, and both IDs are stored.
>
> If the Accounts or Corporate API cannot resolve the identifier the request fails with
> `400` and nothing is persisted. Any other failure of those APIs fails with `500`. In both
> cases, the interest account is left unchanged and no update event is emitted.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID. Must match the account encoded in the account token. This can be a Pismo account ID or an external account ID. A mismatch is rejected with `403 Forbidden`. Maximum 60 characters. | example: "8080" |

#### Request body

Required: yes

> Full interest configuration for the account. See the schema description for the
> conditional required-field rules in `benchmark`, `fixed_interest_rate`,
> `margin_rate`, `margin`, `tax_withholding`, and `taxes_exemption`.

**Content type `application/json`** — schema: object (schema `InterestAccountRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `benchmark` | string (schema `Benchmark`) | no | Market index used to measure interest value over time. For fixed interest, this field must be null.<br>  - `BOE`: Bank of England, UK<br>  - `DI`: Interbank Deposit Contract, Brazil<br>  - `FED`: Federal Reserve System, USA<br>  - `RBA`: Reserve Bank of Australia<br>  - `RBI`: Reserve Bank of India<br>  - `TO`: Overnight Interbank Target Rate (Tasa Objetivo), Mexico<br> | enum: ["BOE", "DI", "FED", "RBA", "RBI", "TO"]; example: "FED" |
| `fixed_interest_rate` | number (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "float"; example: 0.1 |
| `margin_rate` | number \\\| null (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you don't pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `taxes_exemption` | boolean | no | When true, the account is exempt from tax withholding and `tax_withholding` must be null. |  |
| `tax_withholding` | object (schema `TaxWithholding`) | no | Tax withholding configuration. Replaces the standalone `fee_processing_code` field.<br>Conditional rules enforced at creation/update time:<br>- `ACCRUAL`: `fee_processing_code` is required; `tax_rules` must be omitted.<br>- `CAPITALIZATION`: `tax_rules` is required; `fee_processing_code` must be omitted.<br>- Omitted `withholding_moment`: both `fee_processing_code` and `tax_rules` must be omitted.<br>In GET responses, legacy plans that predate this field may return `fee_processing_code` with a null `withholding_moment`.<br> |  |
| `interest_by_tiers` | object (schema `InterestByTiers`) | no | Interest by tiers configuration | example: {"type": "TERM", "tier_calculation": "RETROACTIVE", "tiers": [{"days": 30, "amount": 1000, "margin_rate": 1, "fixed_interest_rate": 1.2}, {"days": 60, "amount": 2000, "margin_rate": 1, "fixed_interest_rate": 1.3}]} |
| `capitalization_frequency` | string (schema `CapitalizationFrequency`) | no | Optional account-level capitalization frequency. When provided with a valid value, it overrides the capitalization frequency configured in the associated interest plan. If omitted or sent as null, the current account-level value remains unchanged. If there is no existing account-level value, then the associated interest plan value is used during processing. | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InterestAccountResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized. The response body is produced by the upstream authentication gateway and is not defined by this service. |  |
| 403 | Forbidden | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `benchmark` | string (schema `BenchmarkResponse`) | no | Market index returned in responses.<br>  - `BOE`: Bank of England, UK<br>  - `DI`: Interbank Deposit Contract, Brazil<br>  - `FED`: Federal Reserve System, USA<br>  - `FIXED`: Fixed interest rate, no market index<br>  - `RBA`: Reserve Bank of Australia<br>  - `RBI`: Reserve Bank of India<br>  - `TO`: Overnight Interbank Target Rate (Tasa Objetivo), Mexico<br> | enum: ["BOE", "DI", "FED", "FIXED", "RBA", "RBI", "TO"]; example: "FIXED" |
| `fixed_interest_rate` | number (schema `FixedInterestRate`) | no | Nominal annual interest rate, expressed as a decimal fraction. 0.10 = 10% per year. 1.00 = 100% per year. Do not send 10 for 10%. Maximum precision: 8 decimal places. The platform converts this annual rate to the accrual period using `accrual_basis` and `interest_type`.<br><br>If you pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "float"; example: 0.1 |
| `margin_rate` | number \\\| null (schema `MarginRate`) | no | Multiplier applied to the benchmark rate, expressed as a decimal fraction of 100%. 1.00 = 100% of the benchmark. 1.10 = 110% of the benchmark. 0.95 = 95% of the benchmark. This is not added to the benchmark—use `margin` for an additive spread.<br><br>If you don't pass a value for `benchmark`, this field must be null. Otherwise, it's required.<br> | format: "double"; example: 1.1 |
| `margin` | number (schema `Margin`) | no | Additive spread, in the same unit and period as the benchmark rate: nominal annual, decimal fraction. If `benchmark` is 0.025 and `margin` is 0.0225, the resulting annual rate is 0.0475.<br><br>If you pass a value for `benchmark`, this field is optional. If `benchmark` is null, this field must be null also.<br> | format: "double"; example: 0.02 |
| `tax_withholding` | object (schema `TaxWithholding`) | no | Tax withholding configuration. Replaces the standalone `fee_processing_code` field.<br>Conditional rules enforced at creation/update time:<br>- `ACCRUAL`: `fee_processing_code` is required; `tax_rules` must be omitted.<br>- `CAPITALIZATION`: `tax_rules` is required; `fee_processing_code` must be omitted.<br>- Omitted `withholding_moment`: both `fee_processing_code` and `tax_rules` must be omitted.<br>In GET responses, legacy plans that predate this field may return `fee_processing_code` with a null `withholding_moment`.<br> |  |
| `taxes_exemption` | boolean (schema `TaxesExemption`) | no | Is the account exempt from taxes? | example: true |
| `interest_by_tiers` | object (schema `InterestByTiers`) | no | Interest by tiers configuration | example: {"type": "TERM", "tier_calculation": "RETROACTIVE", "tiers": [{"days": 30, "amount": 1000, "margin_rate": 1, "fixed_interest_rate": 1.2}, {"days": 60, "amount": 2000, "margin_rate": 1, "fixed_interest_rate": 1.3}]} |
| `capitalization_frequency` | string (schema `CapitalizationFrequency`) | no | Interest payout frequency | enum: ["DAILY", "MONTHLY", "QUARTERLY", "HALF_YEARLY", "YEARLY", "MATURITY"]; example: "DAILY" |
| `external_account_id` | string (schema `ExternalAccountId`) | no | This is the external account ID parsed from a request's account token. Returned only when a request was made with an external ID token. Omitted otherwise, including if the request used a Pismo account ID token, even if an external account ID was previously stored. | maxLength: 60; example: "account-xyz-987" |
| `account_id` | string | no | Pismo account ID. Returned only when the request was authenticated with a Pismo account ID token. Omitted otherwise. | example: "8080" |

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

##### Response 403

403 Example `example`:

```json
{
  "message": "This request is forbidden"
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


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

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
| `api-specs/Banking_-_Interest_engine.yaml` | tag `Account interest`: GET /v1/interest/account/{accountId}, PUT /v1/interest/account/{accountId} | https://github.com/PismoDevEx/pismo-api-specs | `93ec981c793eff61…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
