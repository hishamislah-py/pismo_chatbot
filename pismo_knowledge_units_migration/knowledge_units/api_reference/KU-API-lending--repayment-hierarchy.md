---
ku_id: KU-API-lending--repayment-hierarchy
title: 'API reference: Lending — Repayment hierarchy'
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
- createRepaymentHierarchyV2
- getRepaymentHierarchyV2
related_kus:
- KU-ERR-codes-elnd
- KU-ERR-codes-wiac-to-wstm
- KU-LEND-loan-products
specification_version: 1.0.0
---

# API reference: Lending — Repayment hierarchy

**KU ID:** `KU-API-lending--repayment-hierarchy` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Repayment hierarchy` in `api-specs/Lending.yaml` (“Lending”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Creates the repayment hierarchy and manages features

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/repayment-hierarchies` | `createRepaymentHierarchyV2` | Create repayment hierarchy | no |
| `GET /v2/repayment-hierarchies/{hierarchyCode}` | `getRepaymentHierarchyV2` | Get repayment hierarchy | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer"}

## Operation contracts

<!-- op: spec=api-specs/Lending.yaml method=POST path=/v2/repayment-hierarchies operationId=createRepaymentHierarchyV2 -->
### `POST /v2/repayment-hierarchies` — Create repayment hierarchy

- **operationId:** `createRepaymentHierarchyV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Repayment hierarchy`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a repayment hierarchy for a loan. The repayment hierarchy determines the order in which loan components are paid during repayment processing.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Idempotency-Key` | header | yes | string | Required UUID that makes the request idempotent, enabling you to retry it multiple times while the system processes it only once. | format: "uuid"; example: "4df987e3-8179-11ed-8209-06c7b022d1ee" |

#### Request body

Required: yes

> Request body containing the hierarchy code and payment order.

**Content type `application/json`** — schema: object (schema `RepaymentHierarchyV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `hierarchy` | array of string (schema `HierarchyV2`) | yes | List that defines the repayment priority order using the order items are listed. Determines which loan components are paid first during repayment processing. All seven items are required. | minItems: 7; maxItems: 7; uniqueItems: true; example: ["PRINCIPAL", "INTEREST", "TAX", "FEE", "CHARGE", "PENALTY", "INSURANCE"]; items.enum: ["PRINCIPAL", "INTEREST", "TAX", "FEE", "CHARGE", "PENALTY", "INSURANCE"] |
| `hierarchy_code` | string (schema `HierarchyCode`) | yes | Repayment hierarchy code. Must be unique and can contain alphanumeric characters, hyphens, and underscores. | minLength: 1; maxLength: 80; example: "CR008" |

Example `Create standard repayment hierarchy`:

```json
{
  "hierarchy_code": "CR008",
  "hierarchy": [
    "PRINCIPAL",
    "INTEREST",
    "TAX",
    "FEE",
    "CHARGE",
    "PENALTY",
    "INSURANCE"
  ]
}
```

Example `Create custom repayment hierarchy`:

```json
{
  "hierarchy_code": "CR009",
  "hierarchy": [
    "PENALTY",
    "PRINCIPAL",
    "INTEREST",
    "TAX",
    "FEE",
    "CHARGE",
    "INSURANCE"
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Repayment hierarchy created successfully. | `application/json`: object (schema `RepaymentHierarchyV2Response`) |
| 202 | Duplicated request identified by Idempotency key. | `application/json`: object (schema `StandardErrorResponse`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 201

- Response header `Location`: URI of the created repayment hierarchy (string)
**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `hierarchy_code` | string | yes | Repayment hierarchy code | example: "CR008" |

201 Example `Success response`:

```json
{
  "hierarchy_code": "CR008"
}
```

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Lending error code | example: "ELND0001" |
| `message` | string (schema `ErrorMessage`) | no | Lending error message | example: "Unexpected error" |

202 Example `WLND0001`:

```json
{
  "code": "WLND0001",
  "message": "idempotency-key already in use"
}
```

##### Response 400

400 Example `ELND0601`:

```json
{
  "code": "ELND0601",
  "message": "Field hierarchy_code not passed"
}
```

400 Example `ELND0603`:

```json
{
  "code": "ELND0603",
  "message": "Field hierarchy not passed"
}
```

400 Example `ELND0605`:

```json
{
  "code": "ELND0605",
  "message": "Field hierarchy_code length must be lower or equal to 80"
}
```

400 Example `ELND0606`:

```json
{
  "code": "ELND0606",
  "message": "Field hierarchy size must be equal to 7"
}
```

400 Example `ELND0607`:

```json
{
  "code": "ELND0607",
  "message": "Field hierarchy_code contains invalid characters"
}
```

400 Example `ELND0608`:

```json
{
  "code": "ELND0608",
  "message": "Invalid hierarchy type provided"
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
| 202 | `WLND0001` | idempotency-key already in use |
| 400 | `ELND0601` | Field hierarchy_code not passed |
| 400 | `ELND0603` | Field hierarchy not passed |
| 400 | `ELND0605` | Field hierarchy_code length must be lower or equal to 80 |
| 400 | `ELND0606` | Field hierarchy size must be equal to 7 |
| 400 | `ELND0607` | Field hierarchy_code contains invalid characters |
| 400 | `ELND0608` | Invalid hierarchy type provided |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-LEND-loan-products`.

<!-- op: spec=api-specs/Lending.yaml method=GET path=/v2/repayment-hierarchies/{hierarchyCode} operationId=getRepaymentHierarchyV2 -->
### `GET /v2/repayment-hierarchies/{hierarchyCode}` — Get repayment hierarchy

- **operationId:** `getRepaymentHierarchyV2`
- **Specification:** `api-specs/Lending.yaml` (Lending)
- **Server base URL(s):** `https://sandbox.pismolabs.io/lending`
- **Tags:** `Repayment hierarchy`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a repayment hierarchy by its code, including the hierarchy order and current status.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `hierarchyCode` | path | yes | string | Repayment hierarchy code | maxLength: 80; example: "CR008" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Repayment hierarchy retrieved successfully. | `application/json`: object (schema `GetRepaymentHierarchyV2Response`) |
| 400 | A validation error occurred. | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Repayment hierarchy not found. | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `hierarchy` | array of string (schema `HierarchyV2`) | yes | List that defines the repayment priority order using the order items are listed. Determines which loan components are paid first during repayment processing. All seven items are required. | minItems: 7; maxItems: 7; uniqueItems: true; example: ["PRINCIPAL", "INTEREST", "TAX", "FEE", "CHARGE", "PENALTY", "INSURANCE"]; items.enum: ["PRINCIPAL", "INTEREST", "TAX", "FEE", "CHARGE", "PENALTY", "INSURANCE"] |
| `hierarchy_code` | string (schema `HierarchyCode`) | yes | Repayment hierarchy code. Must be unique and can contain alphanumeric characters, hyphens, and underscores. | minLength: 1; maxLength: 80; example: "CR008" |
| `status` | string (schema `HierarchyStatus`) | yes | Repayment hierarchy status | enum: ["ENABLED", "DISABLED", "DELETED"]; example: "ENABLED" |

200 Example `Success response`:

```json
{
  "hierarchy_code": "CR008",
  "hierarchy": [
    "PRINCIPAL",
    "INTEREST",
    "TAX",
    "FEE",
    "CHARGE",
    "PENALTY",
    "INSURANCE"
  ],
  "status": "ENABLED"
}
```

##### Response 400

400 Example `ELND0601`:

```json
{
  "code": "ELND0601",
  "message": "Field hierarchy_code not passed"
}
```

400 Example `ELND0607`:

```json
{
  "code": "ELND0607",
  "message": "Field hierarchy_code contains invalid characters"
}
```

##### Response 404

404 Example `ELND0005`:

```json
{
  "code": "ELND0005",
  "message": "Repayment hierarchy not found"
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
| 400 | `ELND0601` | Field hierarchy_code not passed |
| 400 | `ELND0607` | Field hierarchy_code contains invalid characters |
| 404 | `ELND0005` | Repayment hierarchy not found |
| 500 | `ELND0001` | Unexpected error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

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
| `api-specs/Lending.yaml` | tag `Repayment hierarchy`: POST /v2/repayment-hierarchies, GET /v2/repayment-hierarchies/{hierarchyCode} | https://github.com/PismoDevEx/pismo-api-specs | `6667602e6ada2f81…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-elnd` — Error codes: ELND
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-LEND-loan-products` — Loan products: overview and creation
