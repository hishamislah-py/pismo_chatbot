---
ku_id: KU-API-revolving-credit-statements--multivalue-program-parameters
title: 'API reference: Revolving credit - Statements — Multivalue program parameters'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Statements.yaml
  sha256: 2ffe392a0e56ae3b5bf71474f241d08b9b078bb852ffaeff142b4dd32d278fd1
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
- getProgramParameter
- updateProgramParamenter
- deleteProgramParamenter
related_kus:
- KU-CARD-multivalue-program-parameters
- KU-CRED-accrual-rate-types-and-limits
- KU-CRED-credit-liquidation
- KU-CRED-delinquency-buckets
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Multivalue program parameters

**KU ID:** `KU-API-revolving-credit-statements--multivalue-program-parameters` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Multivalue program parameters` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Program parameter endpoints that take multiple values

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `getProgramParameter` | List multivalue program parameter values | no |
| `PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `updateProgramParamenter` | Update multivalue program parameter values | no |
| `DELETE /statements-v2/v1/programs/{programId}/parameters/{parameterId}` | `deleteProgramParamenter` | Delete multivalue program parameter values | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements-v2/v1/programs/{programId}/parameters/{parameterId} operationId=getProgramParameter -->
### `GET /statements-v2/v1/programs/{programId}/parameters/{parameterId}` — List multivalue program parameter values

- **operationId:** `getProgramParameter`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Multivalue program parameters`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve an array of multivalue program parameter values given a parameter ID and program ID.
>
> For a list of available multivalue parameters, refer to [Multivalue program parameters](doc:multivalue-parameters).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 1122 |
| `parameterId` | path | yes | integer | Parameter ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `ProgramParameterResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `parameter_id` | integer (schema `ParameterID`) | no | Parameter ID. For a list of available multivalue parameters, refer to [Multivalue program parameters](doc:multivalue-parameters) for the list of available multivalue parameters. | format: "int64"; example: 847490277 |
| `values` | array of string (schema `ProgramParameterArray`) | no |  | example: ["100", "200", "300"] |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type"
}
```

##### Response 404

404 Example `Missing request header`:

```json
{
  "code": "CE0001",
  "message": "Settings not found for Program with id {program_id} and Parameter with id {parameter_id}"
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
| 400 | `EX0002` | Missing request header for method parameter of type |
| 404 | `CE0001` | Settings not found for Program with id {program_id} and Parameter with id {parameter_id} |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-accrual-rate-types-and-limits`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PUT path=/statements-v2/v1/programs/{programId}/parameters/{parameterId} operationId=updateProgramParamenter -->
### `PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}` — Update multivalue program parameter values

- **operationId:** `updateProgramParamenter`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Multivalue program parameters`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update multivalue program parameters using an array list.  
>
> For a list of available multivalue parameters, refer to [Multivalue program parameters](doc:multivalue-parameters).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 1122 |
| `parameterId` | path | yes | integer | Parameter ID | format: "int64"; example: 1 |

#### Request body

Required: no

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `values` | array of string | no |  | example: ["100", "200", "300"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `ProgramParameterResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `parameter_id` | integer (schema `ParameterID`) | no | Parameter ID. For a list of available multivalue parameters, refer to [Multivalue program parameters](doc:multivalue-parameters) for the list of available multivalue parameters. | format: "int64"; example: 847490277 |
| `values` | array of string (schema `ProgramParameterArray`) | no |  | example: ["100", "200", "300"] |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "CE0001",
  "message": "The parameter values must be of type INTEGER"
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
| 400 | `CE0001` | The parameter values must be of type INTEGER |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-multivalue-program-parameters`, `KU-CRED-accrual-rate-types-and-limits`, `KU-CRED-credit-liquidation`, `KU-CRED-delinquency-buckets`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=DELETE path=/statements-v2/v1/programs/{programId}/parameters/{parameterId} operationId=deleteProgramParamenter -->
### `DELETE /statements-v2/v1/programs/{programId}/parameters/{parameterId}` — Delete multivalue program parameter values

- **operationId:** `deleteProgramParamenter`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Multivalue program parameters`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete multivalue program parameter values.
>
> For a list of available multivalue parameters, refer to [Multivalue program parameters](doc:multivalue-parameters).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | format: "int64"; example: 1122 |
| `parameterId` | path | yes | integer | Parameter ID | format: "int64"; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Missing request header`:

```json
{
  "code": "CE0001",
  "message": "Settings not found for Program with id {program_id} and Parameter with id {parameter_id}"
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
| 404 | `CE0001` | Settings not found for Program with id {program_id} and Parameter with id {parameter_id} |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CRED-accrual-rate-types-and-limits`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Internal error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Multivalue program parameters`: GET /statements-v2/v1/programs/{programId}/parameters/{parameterId}, PUT /statements-v2/v1/programs/{programId}/parameters/{parameterId}, DELETE /statements-v2/v1/programs/{programId}/parameters/{parameterId} | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-multivalue-program-parameters` — Multivalue program parameters
- `KU-CRED-accrual-rate-types-and-limits` — Accrual rate types, accrual-free transaction types and accrual-day limits
- `KU-CRED-credit-liquidation` — Credit liquidation
- `KU-CRED-delinquency-buckets` — Delinquency buckets
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
