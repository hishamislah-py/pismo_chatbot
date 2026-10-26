---
ku_id: KU-API-core-platform-accounts--account-parameters
title: 'API reference: Core platform - Accounts — Account parameters'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Accounts.yaml
  sha256: 3c621106abf11d41435170a356ae695e023a5d963bdb0b1e8772209bf0b88c49
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
- account-parameters-get
- account-parameters-update
- account-parameters-find
related_kus:
- KU-CORE-account-parameters-reference-table
- KU-CRED-managing-the-charge-order-for-debit-transactions
specification_version: 1.0.0
---

# API reference: Core platform - Accounts — Account parameters

**KU ID:** `KU-API-core-platform-accounts--account-parameters` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Account parameters` in `api-specs/Core_platform_-_Accounts.yaml` (“Core platform - Accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage account parameters

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /accounts/v1/accounts/{accountId}/parameters/{parameterId}` | `account-parameters-get` | Get parameter | no |
| `PUT /accounts/v1/accounts/{accountId}/parameters/{parameterId}` | `account-parameters-update` | Update parameter | no |
| `GET /accounts/v1/accounts/{accountId}/parameters` | `account-parameters-find` | List parameters | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/accounts/{accountId}/parameters/{parameterId} operationId=account-parameters-get -->
### `GET /accounts/v1/accounts/{accountId}/parameters/{parameterId}` — Get parameter

- **operationId:** `account-parameters-get`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Account parameters`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get account parameter registered for the organization.  For more information on account parameters, refer to the [account parameters guide](doc:account-parameters-reference-table). Account parameters are a subset of [program parameters](doc:program-parameters-reference-table).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `parameterId` | path | yes | integer | Parameter ID.<br><br>For more information on program/account parameters, refer to the [program parameters reference table](doc:program-parameters-reference-table).<br><br>Call the [List program parameters](ref:programparameter) endpoint to get the ID (`parameter_id`) to pass here.<br> | format: "int64"; example: 123456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: oneOf: object (schema `ParametersDataResponse`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Internal server error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PUT path=/accounts/v1/accounts/{accountId}/parameters/{parameterId} operationId=account-parameters-update -->
### `PUT /accounts/v1/accounts/{accountId}/parameters/{parameterId}` — Update parameter

- **operationId:** `account-parameters-update`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Account parameters`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update account parameter value. For more information on account parameters, refer to the [account parameters guide](doc:account-parameters-reference-table). Account parameters are a subset of [program parameters](doc:program-parameters-reference-table).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |
| `parameterId` | path | yes | integer | Parameter ID.<br><br>For more information on program/account parameters, refer to the [program parameters reference table](doc:program-parameters-reference-table).<br><br>Call the [List program parameters](ref:programparameter) endpoint to get the ID (`parameter_id`) to pass here.<br> | format: "int64"; example: 123456 |

#### Request body

Required: yes

> Parameter data to update

**Content type `application/json`** — schema: object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `value` | number | no | Parameter value | format: "float"; example: 0.01 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK |  |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Internal server error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-account-parameters-reference-table`, `KU-CRED-managing-the-charge-order-for-debit-transactions`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/accounts/{accountId}/parameters operationId=account-parameters-find -->
### `GET /accounts/v1/accounts/{accountId}/parameters` — List parameters

- **operationId:** `account-parameters-find`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Account parameters`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account parameters. For more information on account parameters, refer to the [account parameters guide](doc:account-parameters-reference-table). Account parameters are a subset of [program parameters](doc:program-parameters-reference-table).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Internal server error"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-account-parameters-reference-table`, `KU-CRED-managing-the-charge-order-for-debit-transactions`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/SimpleError -->
### Schema `SimpleError`

Pointer: `#/components/schemas/SimpleError`. Type: object (schema `SimpleError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounts.yaml` | tag `Account parameters`: GET /accounts/v1/accounts/{accountId}/parameters/{parameterId}, PUT /accounts/v1/accounts/{accountId}/parameters/{parameterId}, GET /accounts/v1/accounts/{accountId}/parameters | https://github.com/PismoDevEx/pismo-api-specs | `3c621106abf11d41…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-account-parameters-reference-table` — Account parameters
- `KU-CRED-managing-the-charge-order-for-debit-transactions` — Managing the charge order for debit transactions
