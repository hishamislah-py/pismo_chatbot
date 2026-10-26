---
ku_id: KU-API-core-platform-accounts--transfer-account
title: 'API reference: Core platform - Accounts — Transfer account'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- PostMigrationProgram
related_kus:
- KU-CORE-accounts-overview
- KU-EVT-accounts-data-events
- KU-EVT-catalogue-account
specification_version: 1.0.0
---

# API reference: Core platform - Accounts — Transfer account

**KU ID:** `KU-API-core-platform-accounts--transfer-account` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Transfer account` in `api-specs/Core_platform_-_Accounts.yaml` (“Core platform - Accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints dealing with account transfer

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /accounts/v1/accounts/programs/migration` | `PostMigrationProgram` | Transfer account to different program | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/accounts/v1/accounts/programs/migration operationId=PostMigrationProgram -->
### `POST /accounts/v1/accounts/programs/migration` — Transfer account to different program

- **operationId:** `PostMigrationProgram`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Transfer account`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Change the program ID for an account. This also changes the program ID for customers and statements associated with the account. Note that the account keeps the original program's flex controls and ignores the new program's flex controls.
>
> Transfer is permitted **only** if both programs (origin and target) have the same:
>
>   * [Program type](doc:program-types)&mdash;For example, you can migrate from credit to credit and from prepaid to prepaid, but not credit to prepaid.
>   * Currency&mdash;For example, USD to USD only or BRL to BRL only.
>   * Brand (if applicable)&mdash;For example, Mastercard to Mastercard.
>   * Due date (credit programs only)&mdash;Account due date must be available in the target program.
>
> **Notes:**
>
> * Transferring an account does not affect account limits
> * When an account is transferred successfully, you need to <a href="https://developers.pismo.io/pismo-docs/reference/post-v1-card-reissue">issue a new card</a> that corresponds to the new program for your customers.
>
> This endpoint generates an [Account migrated to different program](https://developers.pismo.io/events/docs/account-program-migration-1) event.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `MigrateAccountRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 1001 |
| `program` | object | yes | Program object |  |
| `program.id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Program was successfully migrated | `application/json`: object |
| 400 | Bad request | `application/json`: object |
| 404 | Resource not found | `application/json`: no schema |
| 409 | Conflict | `application/json`: no schema |
| 500 | Internal server error | `application/json`: object |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1001 |
| `external_account_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |
| `program` | object | no | Program object |  |
| `program.id` | integer (schema `ProgramID`) | no | Program ID | format: "int64"; example: 12345 |

##### Response 404

404 Example `error1` (Account not found):

```json
{
  "message": "Account with id: 1 not found"
}
```

404 Example `error2` (ProgramId not found):

```json
{
  "message": "Program with id: 1 not found"
}
```

404 Example `error3` (ProgramDueDate not found for program):

```json
{
  "message": "ProgramDueDate not found for the programId: 1"
}
```

404 Example `error4` (Calendar not found):

```json
{
  "message": "Calendars not found for programId: 1"
}
```

##### Response 409

409 Example `error1` (Account is not credit type):

```json
{
  "message": "This account is not credit type"
}
```

409 Example `error2` (The program is the same as the current one):

```json
{
  "message": "The program is the same as the current one"
}
```

409 Example `error3` (New program is not credit type):

```json
{
  "message": "The program is not credit type"
}
```

409 Example `error4` (Standard calendar selection parameter is active):

```json
{
  "message": "Standard calendar selection parameter is active"
}
```

409 Example `error5` (New program does not have the same due date day):

```json
{
  "message": "New program does not have the same due date day"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-program-migration-1` | https://developers.pismo.io/events/docs/account-program-migration-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounts-overview`, `KU-EVT-accounts-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.


## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounts.yaml` | tag `Transfer account`: POST /accounts/v1/accounts/programs/migration | https://github.com/PismoDevEx/pismo-api-specs | `3c621106abf11d41…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-accounts-overview` — Accounts
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-catalogue-account` — Event catalogue: account
