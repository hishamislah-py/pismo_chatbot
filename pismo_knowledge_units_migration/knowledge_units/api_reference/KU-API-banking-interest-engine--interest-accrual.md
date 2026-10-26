---
ku_id: KU-API-banking-interest-engine--interest-accrual
title: 'API reference: Banking - Interest engine — Interest accrual'
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
- post-v1-interest-accrual-setup
related_kus: []
specification_version: 1.0.0
---

# API reference: Banking - Interest engine — Interest accrual

**KU ID:** `KU-API-banking-interest-engine--interest-accrual` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Interest accrual` in `api-specs/Banking_-_Interest_engine.yaml` (“Banking - Interest engine”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Interest accrual

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/interest/accrual/setup` | `post-v1-interest-accrual-setup` | Configure timing for accrual calculation | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest_engine.yaml method=POST path=/v1/interest/accrual/setup operationId=post-v1-interest-accrual-setup -->
### `POST /v1/interest/accrual/setup` — Configure timing for accrual calculation

- **operationId:** `post-v1-interest-accrual-setup`
- **Specification:** `api-specs/Banking_-_Interest_engine.yaml` (Banking - Interest engine)
- **Server base URL(s):** `https://sandbox.pismolabs.io/interest-engine`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Interest accrual`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Set up the time when the daily accrual calculations should occur.
>
> If you pass a value for `division_id`, then the value passed in `time_utc` is only used for the corresponding division. That is, it's only used for the accruals of installment plans associated with that division.
>
> If you don't pass a value for `division_id`, then the value passed in `time_utc` is used for all installment plans in the program's org, unless they are associated with a division that already has a time assigned to it. (That is, unless you already ran the endpoint with `division_id` set to the ID for that division.)
>
> <b>Note:</b> If you run the endpoint a second time using the same value `division_id`, it generates an error. This also happens if you run the endpoint twice without passing a value for `division_id`.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `InterestAccrualSetupRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `time_utc` | string (schema `TimeUTC`) | yes | Time when accrual calculation is performed, specified in hours and minutes. `04:05`, `05:05`, `06:05`, `07:05`, `08:05`, `09:05`, `10:05` and `19:15` are the only values accepted. | enum: ["04:05", "05:05", "06:05", "07:05", "08:05", "09:05", "10:05", "19:15"]; example: "19:15" |
| `division_id` | string (schema `DivisionId`) | no | Division ID attached to the interest plan for accrual by division | example: "d9b2c9e1-4633-4a10-841b-270f7f1493cd" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `InterestAccrualSetupResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized. The response body is produced by the upstream authentication gateway and is not defined by this service. |  |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `time_utc` | string (schema `TimeUTC`) | yes | Time when accrual calculation is performed, specified in hours and minutes. `04:05`, `05:05`, `06:05`, `07:05`, `08:05`, `09:05`, `10:05` and `19:15` are the only values accepted. | enum: ["04:05", "05:05", "06:05", "07:05", "08:05", "09:05", "10:05", "19:15"]; example: "19:15" |
| `division_id` | string (schema `DivisionId`) | no | Division ID attached to the interest plan for accrual by division | example: "d9b2c9e1-4633-4a10-841b-270f7f1493cd" |

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
| `api-specs/Banking_-_Interest_engine.yaml` | tag `Interest accrual`: POST /v1/interest/accrual/setup | https://github.com/PismoDevEx/pismo-api-specs | `93ec981c793eff61…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
