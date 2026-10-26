---
ku_id: KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value
title: 'API reference: Revolving credit - Interest accruals — Accrual types minimum value'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Interest_accruals.yaml
  sha256: c741d2a41ac47207d0bbbc8f40d9492a64f36e979006c8170c14a065a96978af
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
- getAccrualTypeMinimumValue
- postAccrualTypeMinimumValue
- deleteAccrualTypeMinimumValue
related_kus:
- KU-CORE-program-parameters-reference-table
- KU-CRED-configuring-a-sellos-tax
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
specification_version: 2.74.0
---

# API reference: Revolving credit - Interest accruals — Accrual types minimum value

**KU ID:** `KU-API-revolving-credit-interest-accruals--accrual-types-minimum-value` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Accrual types minimum value` in `api-specs/Revolving_credit_-_Interest_accruals.yaml` (“Revolving credit - Interest accruals”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints for setting minimum values of accrual types

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accrual-type-minimum-value` | `getAccrualTypeMinimumValue` | List minimum value configurations | no |
| `POST /v1/accrual-type-minimum-value` | `postAccrualTypeMinimumValue` | Configure minimum value by accrual type | no |
| `DELETE /v1/accrual-type-minimum-value` | `deleteAccrualTypeMinimumValue` | Delete minimum value configuration | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Interest_accruals.yaml method=GET path=/v1/accrual-type-minimum-value operationId=getAccrualTypeMinimumValue -->
### `GET /v1/accrual-type-minimum-value` — List minimum value configurations

- **operationId:** `getAccrualTypeMinimumValue`
- **Specification:** `api-specs/Revolving_credit_-_Interest_accruals.yaml` (Revolving credit - Interest accruals)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-interest-accruals`
- **Tags:** `Accrual types minimum value`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List the minimum value configurations for an accrual type.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `perPage` | query | no | integer | Number of items per page | default: 100; format: "int32" |
| `page` | query | no | integer | Page number | default: 1; format: "int32" |
| `accrualType` | query | no | string | Accrual type<br> | enum: ["REFINANCING", "OVERDUE", "WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX"]; example: "REFINANCING" |
| `hierarchyName` | query | no | string (schema `HierarchyName`) | Hierarchy name | enum: ["ORG_ID", "PROGRAM_ID", "ACCOUNT_ID"]; example: "ACCOUNT_ID" |
| `hierarchyValue` | query | no | string | Hierarchy value | example: "123456789" |
| `isDeleted` | query | no | boolean | Is deleted | default: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Number of items per page | format: "int32"; example: 20 |
| `total_items` | integer (schema `TotalItems`) | no | Total number of items | format: "int32"; example: 955 |
| `items_on_page` | integer (schema `ItemsOnPage`) | no | Items on page. (This could be less than `per_page` if this is the last page.) | format: "int32"; example: 1 |
| `is_last_page` | boolean (schema `IsLastPage`) | no | Is this the last page? | example: false |
| `items` | array of object (schema `AccrualTypeMinimumValueResponseWithDates`) | no |  |  |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "The header {HeaderName} is required | The property {PropertyName} is required."
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
| 400 | `EX0001` | The header {HeaderName} is required \| The property {PropertyName} is required. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Revolving_credit_-_Interest_accruals.yaml method=POST path=/v1/accrual-type-minimum-value operationId=postAccrualTypeMinimumValue -->
### `POST /v1/accrual-type-minimum-value` — Configure minimum value by accrual type

- **operationId:** `postAccrualTypeMinimumValue`
- **Specification:** `api-specs/Revolving_credit_-_Interest_accruals.yaml` (Revolving credit - Interest accruals)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-interest-accruals`
- **Tags:** `Accrual types minimum value`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Configure a minimum value for an accrual type. At cycle closing, if the calculated value for an accrual of that type is lower that the configured minimum value, the minimum value is used instead.
>
> This is an immutable configuration. So, to override a previous configuration, you have to create a new configuration for the same level in the hierarchy. The old configuration is maintained to track the changes, but it's not used.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `AccrualTypeMinimumValueRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_type` | string (schema `AccrualType`) | yes | Accrual type. Should be one of the following values:<br>  `REFINANCING`<br>  `OVERDUE`<br>  `WITHDRAWAL_INTEREST`<br>  `BILLPAYMENT_INTEREST`<br>  `OVERDRAFT_INTEREST`<br>  `FINANCIAL_TAX`<br> | maxLength: 20; example: "REFINANCING" |
| `hierarchy_name` | string (schema `HierarchyName`) | yes |  | enum: ["ORG_ID", "PROGRAM_ID", "ACCOUNT_ID"]; example: "ACCOUNT_ID" |
| `hierarchy_value` | string (schema `HierarchyValue`) | yes | If `hierarchy_name` is `PROGRAM_ID` or `ACCOUNT_ID`, the hierarchy value must be an integer. If `hierarchy_name` is `ORG_ID`, the value must be a string. | example: "123456789" |
| `minimum_amount_to_post` | number (schema `MinimumAmountToPost`) | yes |  | format: "double"; example: 100.23 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `AccrualTypeMinimumValueResponse`) |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `StandardErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_type` | string (schema `AccrualType`) | yes | Accrual type. Should be one of the following values:<br>  `REFINANCING`<br>  `OVERDUE`<br>  `WITHDRAWAL_INTEREST`<br>  `BILLPAYMENT_INTEREST`<br>  `OVERDRAFT_INTEREST`<br>  `FINANCIAL_TAX`<br> | maxLength: 20; example: "REFINANCING" |
| `hierarchy_name` | string (schema `HierarchyName`) | yes |  | enum: ["ORG_ID", "PROGRAM_ID", "ACCOUNT_ID"]; example: "ACCOUNT_ID" |
| `hierarchy_value` | string (schema `HierarchyValue`) | yes | If `hierarchy_name` is `PROGRAM_ID` or `ACCOUNT_ID`, the hierarchy value must be an integer. If `hierarchy_name` is `ORG_ID`, the value must be a string. | example: "123456789" |
| `minimum_amount_to_post` | number (schema `MinimumAmountToPost`) | yes |  | format: "double"; example: 100.23 |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "The header {HeaderName} is required | The property {PropertyName} is required."
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
| 400 | `EX0001` | The header {HeaderName} is required \| The property {PropertyName} is required. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-program-parameters-reference-table`, `KU-CRED-configuring-a-sellos-tax`.

<!-- op: spec=api-specs/Revolving_credit_-_Interest_accruals.yaml method=DELETE path=/v1/accrual-type-minimum-value operationId=deleteAccrualTypeMinimumValue -->
### `DELETE /v1/accrual-type-minimum-value` — Delete minimum value configuration

- **operationId:** `deleteAccrualTypeMinimumValue`
- **Specification:** `api-specs/Revolving_credit_-_Interest_accruals.yaml` (Revolving credit - Interest accruals)
- **Server base URL(s):** `https://sandbox.pismolabs.io/credit-cycle-interest-accruals`
- **Tags:** `Accrual types minimum value`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete a minimum value configuration for an accrual type.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accrualType` | query | no | string | Accrual type<br> | enum: ["REFINANCING", "OVERDUE", "WITHDRAWAL_INTEREST", "BILLPAYMENT_INTEREST", "OVERDRAFT_INTEREST", "FINANCIAL_TAX"]; example: "REFINANCING" |
| `hierarchyName` | query | no | string (schema `HierarchyName`) | Hierarchy name | enum: ["ORG_ID", "PROGRAM_ID", "ACCOUNT_ID"]; example: "ACCOUNT_ID" |
| `hierarchyValue` | query | no | string | Hierarchy value | example: "123456789" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No content |  |
| 400 | Bad request | `application/json`: object (schema `StandardErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `StandardErrorResponse`) |

##### Response 400

400 Example `Missing request header or param`:

```json
{
  "code": "EX0001",
  "message": "The header {HeaderName} is required | The property {PropertyName} is required."
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
| 400 | `EX0001` | The header {HeaderName} is required \| The property {PropertyName} is required. |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccrualTypeMinimumValueResponseWithDates -->
### Schema `AccrualTypeMinimumValueResponseWithDates`

Pointer: `#/components/schemas/AccrualTypeMinimumValueResponseWithDates`. Type: object (schema `AccrualTypeMinimumValueResponseWithDates`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `accrual_type` | string (schema `AccrualType`) | yes | Accrual type. Should be one of the following values:<br>  `REFINANCING`<br>  `OVERDUE`<br>  `WITHDRAWAL_INTEREST`<br>  `BILLPAYMENT_INTEREST`<br>  `OVERDRAFT_INTEREST`<br>  `FINANCIAL_TAX`<br> | maxLength: 20; example: "REFINANCING" |
| `hierarchy_name` | string (schema `HierarchyName`) | yes |  | enum: ["ORG_ID", "PROGRAM_ID", "ACCOUNT_ID"]; example: "ACCOUNT_ID" |
| `hierarchy_value` | string (schema `HierarchyValue`) | yes | If `hierarchy_name` is `PROGRAM_ID` or `ACCOUNT_ID`, the hierarchy value must be an integer. If `hierarchy_name` is `ORG_ID`, the value must be a string. | example: "123456789" |
| `minimum_amount_to_post` | number (schema `MinimumAmountToPost`) | yes |  | format: "double"; example: 100.23 |
| `created_at` | string (schema `CreatedAt`) | no | Date created. Format = YYYY-MM-DDThh:mm:ss.sssz. | example: "2023-08-18T20:53:27.498Z" |
| `deleted_at` | string (schema `DeletedAt`) | no | Date deleted. Format = YYYY-MM-DDThh:mm:ss.sssz. | example: "2023-10-10T10:50:18.212Z" |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Interest_accruals.yaml` | tag `Accrual types minimum value`: GET /v1/accrual-type-minimum-value, POST /v1/accrual-type-minimum-value, DELETE /v1/accrual-type-minimum-value | https://github.com/PismoDevEx/pismo-api-specs | `c741d2a41ac47207…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-program-parameters-reference-table` — Program parameters
- `KU-CRED-configuring-a-sellos-tax` — Configuring a sellos tax
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
