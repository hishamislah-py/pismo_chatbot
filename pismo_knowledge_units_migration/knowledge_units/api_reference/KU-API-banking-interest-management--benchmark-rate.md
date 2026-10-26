---
ku_id: KU-API-banking-interest-management--benchmark-rate
title: 'API reference: Banking - Interest management for B3-listed products — Benchmark rate'
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
operations:
- get-v1-benchmark-rate-org-b3
- post-v1-benchmark-rate-b3
- get-v1-benchmark-rate-b3
related_kus: []
specification_version: 1.0.0
---

# API reference: Banking - Interest management for B3-listed products — Benchmark rate

**KU ID:** `KU-API-banking-interest-management--benchmark-rate` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Benchmark rate` in `api-specs/Banking_-_Interest_management.yaml` (“Banking - Interest management for B3-listed products”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Manage benchmarks

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/interest/benchmark-rate` | `get-v1-benchmark-rate-org-b3` | Get Org benchmark rates for B3-listed products | no |
| `POST /v1/interest/benchmark-rate` | `post-v1-benchmark-rate-b3` | Configure benchmark rate for B3-listed products | no |
| `GET /v1/interest/benchmark-rate/{benchmark}` | `get-v1-benchmark-rate-b3` | Get specific benchmark rates for B3-listed products | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest_management.yaml method=GET path=/v1/interest/benchmark-rate operationId=get-v1-benchmark-rate-org-b3 -->
### `GET /v1/interest/benchmark-rate` — Get Org benchmark rates for B3-listed products

- **operationId:** `get-v1-benchmark-rate-org-b3`
- **Specification:** `api-specs/Banking_-_Interest_management.yaml` (Banking - Interest management for B3-listed products)
- **Server base URL(s):** `https://sandbox-integration.pismolabs.io/interest-management`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Benchmark rate`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get all benchmark rates configured for an organization.
>
> **Note:** Only Brazilian Stock Exchange (B3) customers should use this endpoint.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `content-type` | header | yes | string | Content type | example: "application/json" |
| `authorization` | header | yes | string | Authorization | example: "Bearer ac194ce4-ecbe-4007-91bd-94babf388e7278f243bc-4ad8-4ead-a2c3-f42a548fe760" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetBenchmarkRateOrgResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized access | `application/json`: object |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `get_benchmark_rate_org_list` | array of object (schema `GetBenchmarkRate`) (schema `BenchmarkRateList`) | no | Benchmark rate list | format: "array" |

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

<!-- op: spec=api-specs/Banking_-_Interest_management.yaml method=POST path=/v1/interest/benchmark-rate operationId=post-v1-benchmark-rate-b3 -->
### `POST /v1/interest/benchmark-rate` — Configure benchmark rate for B3-listed products

- **operationId:** `post-v1-benchmark-rate-b3`
- **Specification:** `api-specs/Banking_-_Interest_management.yaml` (Banking - Interest management for B3-listed products)
- **Server base URL(s):** `https://sandbox-integration.pismolabs.io/interest-management`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Benchmark rate`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Configure the benchmark rate and its start date. Used to calculate interest accual for floating and hybrid investments.
>
> **Note:** Only Brazilian Stock Exchange (B3) customers should use this endpoint.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `content-type` | header | yes | string | Content type | example: "application/json" |
| `authorization` | header | yes | string | Authorization | example: "Bearer ac194ce4-ecbe-4007-91bd-94babf388e7278f243bc-4ad8-4ead-a2c3-f42a548fe760" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `BenchmarkRateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `benchmark` | string (schema `BenchmarkRequired`) | yes | Market index used to measure interest value over time.<br>  - BOE: Bank of England, UK<br>  - DI: Interbank Deposit Contract, Brazil<br>  - FED: Federal Reserve System, USA<br>  - RBA: Reserve Bank of Australia<br>  - RBI: Reserve Bank of India   <br> | enum: ["BOE", "DI", "FED", "RBA", "RBI"]; example: "FED" |
| `benchmark_rate` | number (schema `BenchmarkRate`) | yes | Annual market index rate | format: "double"; example: 0.104 |
| `start_date` | string (schema `StartDate`) | yes | Date to start applying the benchmark rate in the accrual process. Format = YYYY-MM-DD. | format: "date"; example: "2024-09-10" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `BenchmarkRateResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized access | `application/json`: object |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `benchmark_rate` | number (schema `BenchmarkRate`) | no | Annual market index rate | format: "double"; example: 0.104 |
| `start_date` | string (schema `StartDate`) | no | Date to start applying the benchmark rate in the accrual process. Format = YYYY-MM-DD. | format: "date"; example: "2024-09-10" |
| `version` | string (schema `Version`) | no | Benchmark rate version. Format = YYYY-MM. | example: "2024-09" |

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

<!-- op: spec=api-specs/Banking_-_Interest_management.yaml method=GET path=/v1/interest/benchmark-rate/{benchmark} operationId=get-v1-benchmark-rate-b3 -->
### `GET /v1/interest/benchmark-rate/{benchmark}` — Get specific benchmark rates for B3-listed products

- **operationId:** `get-v1-benchmark-rate-b3`
- **Specification:** `api-specs/Banking_-_Interest_management.yaml` (Banking - Interest management for B3-listed products)
- **Server base URL(s):** `https://sandbox-integration.pismolabs.io/interest-management`, `https://sandbox.pismolabs.io/passport/v2/s2s/access-token`
- **Tags:** `Benchmark rate`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get all rates configured for a specific benchmark.
>
> **Note:** Only Brazilian Stock Exchange (B3) customers should use this endpoint.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `content-type` | header | yes | string | Content type | example: "application/json" |
| `authorization` | header | yes | string | Authorization | example: "Bearer ac194ce4-ecbe-4007-91bd-94babf388e7278f243bc-4ad8-4ead-a2c3-f42a548fe760" |
| `benchmark` | path | yes | string | Market index used to measure the interest a value has over time | example: "FED" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetBenchmarkRateResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `ErrorResponseDeserialization`) |
| 401 | Unauthorized access | `application/json`: object |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `get_benchmark_rate_list` | array of object (schema `GetBenchmarkRate`) (schema `BenchmarkRateList`) | no | Benchmark rate list | format: "array" |

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

<!-- schema: #/components/schemas/GetBenchmarkRate -->
### Schema `GetBenchmarkRate`

Pointer: `#/components/schemas/GetBenchmarkRate`. Type: object (schema `GetBenchmarkRate`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `benchmark` | string (schema `BenchmarkRequired`) | no | Market index used to measure interest value over time.<br>  - BOE: Bank of England, UK<br>  - DI: Interbank Deposit Contract, Brazil<br>  - FED: Federal Reserve System, USA<br>  - RBA: Reserve Bank of Australia<br>  - RBI: Reserve Bank of India   <br> | enum: ["BOE", "DI", "FED", "RBA", "RBI"]; example: "FED" |
| `benchmark_rate` | number (schema `BenchmarkRate`) | no | Annual market index rate | format: "double"; example: 0.104 |
| `start_date` | string (schema `StartDate`) | no | Date to start applying the benchmark rate in the accrual process. Format = YYYY-MM-DD. | format: "date"; example: "2024-09-10" |
| `version` | string (schema `Version`) | no | Benchmark rate version. Format = YYYY-MM. | example: "2024-09" |

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
| `api-specs/Banking_-_Interest_management.yaml` | tag `Benchmark rate`: GET /v1/interest/benchmark-rate, POST /v1/interest/benchmark-rate, GET /v1/interest/benchmark-rate/{benchmark} | https://github.com/PismoDevEx/pismo-api-specs | `3ea9e4fd670aed59…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- None.
