---
ku_id: KU-API-migrations--statement-migration
title: 'API reference: Migrations — Statement migration'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Migrations.yaml
  sha256: 7478abcca92f0932e27157e9dc1cb8c0459b9c128cf72428de43092c903cd59a
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
- PostStatementsV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
- KU-EVT-migrations-data-events
specification_version: 0.0.7
---

# API reference: Migrations — Statement migration

**KU ID:** `KU-API-migrations--statement-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Statement migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Statement migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/statements` | `PostStatementsV1` | Migrate statements | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/statements operationId=PostStatementsV1 -->
### `POST /v1/migrations/statements` — Migrate statements

- **operationId:** `PostStatementsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Statement migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of statements.
>
> This endpoint generates the following events:
>
> - [Statement migration started](https://developers.pismo.io/events/docs/migration-statement-incoming-1)
>
> - [Statement migration completed](https://developers.pismo.io/events/docs/migration-statement-outgoing-1)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | JSON Web Token (JWT). Tokens expire quickly, which can result in an **Unauthorized** message. For more information on authentication best practices, refer to [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials#initial-authentication).<br> | example: "eyJ...F8E" |

#### Request body

Required: no

> Start migration of statements

**Content type `application/json`** — schema: object (schema `PostStatementsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | no | Applicant additional migration information |  |
| `migration.id` | string | yes | ID that you generate for migration purposes | example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `migration.account_id` | string | no | Set to the value in `applicant.migration.id` from the [Migrate accounts](ref:postaccountsv1) endpoint. This field links statements to an account. | example: "EXTID1001" |
| `cycle_closing_date` | string | no | Cycle closing date | format: "date"; example: "2018-03-15" |
| `best_transaction_day` | string | no | Day of best transaction. This is the cycle closing date of a credit card account. For purchases made after the cycle closes, payment is due in the next statement.<br> | format: "date"; example: "2018-03-16" |
| `due_date` | string | no | Due date | format: "date"; example: "2018-03-25" |
| `real_due_date` | string | no | If a due date falls on a nonbusiness day, such as weekend or a holiday, the actual due date is the next business day on which the payment can be made. (Otherwise, it's the same as the due date.) Interest isn't charged until the real due date.<br> | format: "date"; example: "2018-03-25" |
| `previous_balance` | number | no | Value of previous balance | format: "float"; example: 180.52 |
| `debits` | number | no | Total debits of statement | format: "float"; example: 50 |
| `credits` | number | no | Total credits of statement | format: "float"; example: 50 |
| `current_balance` | number | no | Current balance | format: "float"; example: 190.52 |
| `minimum_payment` | number | no | Minimun payment | format: "float"; example: 20 |
| `posted_date` | string | no | Posted date | format: "date-time"; example: "2021-10-25T19:54:41Z" |
| `posted_fine` | boolean | no | Is fine posted? | example: false |
| `metadata` | object | no | Statements metadata<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"key1": "value1", "key2": "value2"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Payload Validation Error` — from `#/components/examples/PayloadValidationError`:

```json
{
  "code": "MIGR00002",
  "field": "field_path (the object that failed validation)",
  "message": "Field required"
}
```

##### Response 500

500 Example `Internal Server Error` — from `#/components/examples/InternalServerError`:

```json
{
  "code": "MIGR00001",
  "message": "Something went wrong"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `MIGR00002` | Field required |
| 500 | `MIGR00001` | Something went wrong |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `migration-statement-incoming-1` | https://developers.pismo.io/events/docs/migration-statement-incoming-1 |
| `migration-statement-outgoing-1` | https://developers.pismo.io/events/docs/migration-statement-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-migrations-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Message describing the error | example: "Internal error" |
| `code` | string | no | Payload validation error | example: "MIGR00001" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Migrations.yaml` | tag `Statement migration`: POST /v1/migrations/statements | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
- `KU-EVT-migrations-data-events` — Migrations events
