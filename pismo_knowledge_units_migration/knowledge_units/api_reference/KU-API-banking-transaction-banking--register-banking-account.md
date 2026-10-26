---
ku_id: KU-API-banking-transaction-banking--register-banking-account
title: 'API reference: Banking - Transaction banking — Register banking account'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Transaction_banking.yaml
  sha256: dec6c4900eb2db35c29c0f0380763da5ae0e1a18c4ad1e293216b2b6effdab56
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
- post-corporate-v2-register-account
related_kus:
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Register banking account

**KU ID:** `KU-API-banking-transaction-banking--register-banking-account` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Register banking account` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Register existing banking accounts for transaction banking

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /corporate/v2/corporate-accounts/register` | `post-corporate-v2-register-account` | Register banking accounts with transaction banking | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/corporate-accounts/register operationId=post-corporate-v2-register-account -->
### `POST /corporate/v2/corporate-accounts/register` — Register banking accounts with transaction banking

- **operationId:** `post-corporate-v2-register-account`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Register banking account`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Onboard accounts that already exist in Banking into Transaction Banking. Once onboarded, these accounts are enabled to use transaction banking APIs and features.

#### Request body

Required: no

> Onboard existing banking accounts into transaction banking.

**Content type `application/json`** — schema: object (schema `RegisterAccountv2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `RegisterAccountIdv2`) | yes | Registered account ID. This ID is client-generated. | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 325636216 |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |

Example `Register account`:

```json
{
  "account_id": 325636216,
  "division_code": "my-division-code-1773411878103"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `RegisterAccountResponsev2`) |
| 400 | A Bad Request validation error | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |
| 503 | Service unavailable |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `RegisterAccountIdv2`) | yes | Registered account ID. This ID is client-generated. | format: "int64"; minimum: 1; maximum: 18446744073709552000; example: 325636216 |
| `program_id` | integer (schema `ProgramID3`) | yes | Program ID. This is a client-provided ID. | format: "int64"; example: 2222 |
| `status` | string (schema `RegisterAccountStatusv2`) | yes | Transaction banking account registration status. `COMPLETED` is returned only when the registration succeeds. | example: "COMPLETED" |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |

201 Example `Account registered successfully`:

```json
{
  "account_id": 325636216,
  "division_code": "my-division-code-1773411878103",
  "program_id": 1240,
  "status": "COMPLETED"
}
```

##### Response 400

400 Example `Program not bound to division`:

```json
{
  "code": "WCAC0006",
  "message": "Program not bound to division"
}
```

##### Response 404

404 Example `Account not found in accounts-core`:

```json
{
  "code": "WCAC0041",
  "message": "Account not found in accounts-core"
}
```

404 Example `Division not found`:

```json
{
  "code": "WCDV0002",
  "message": "Division not found"
}
```

##### Response 409

409 Example `Duplicated external_account_id`:

```json
{
  "code": "WCAC0011",
  "message": "Duplicate external_account_id"
}
```

##### Response 422

422 Example `Account has not completed the creation process`:

```json
{
  "code": "WCAC0042",
  "message": "Account has not completed the creation process"
}
```

422 Example `Program type CREDITO cannot be registered`:

```json
{
  "code": "WCAC0043",
  "message": "Program type CREDITO cannot be registered"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0006` | Program not bound to division |
| 404 | `WCAC0041` | Account not found in accounts-core |
| 404 | `WCDV0002` | Division not found |
| 409 | `WCAC0011` | Duplicate external_account_id |
| 422 | `WCAC0042` | Account has not completed the creation process |
| 422 | `WCAC0043` | Program type CREDITO cannot be registered |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;422;500;503`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Register banking account`: POST /corporate/v2/corporate-accounts/register | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
