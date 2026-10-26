---
ku_id: KU-API-migrations--accrual-migration
title: 'API reference: Migrations — Accrual migration'
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
- PostAccrualsV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Accrual migration

**KU ID:** `KU-API-migrations--accrual-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Accrual migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Accrual migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/accruals` | `PostAccrualsV1` | Migrate accruals | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/accruals operationId=PostAccrualsV1 -->
### `POST /v1/migrations/accruals` — Migrate accruals

- **operationId:** `PostAccrualsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Accrual migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start accruals migration.
>
> This endpoint generates the following events:
>
> - [Accrual migration started](https://developers.pismo.io/events/docs/migration-accrual-incoming-1)
>
> - [Accrual migration completed](https://developers.pismo.io/events/docs/migration-accrual-outgoing-1)
>
> - [Statement organized completed](https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1) — emitted when the organize-statement process runs, indicating whether the account's statements were organized successfully or the processing failed. Emission is opt-in.

#### Request body

Required: no

> Start an accruals migration

**Content type `application/json`** — schema: object (schema `PostAccrualsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Client-provided migration details |  |
| `migration.account_id` | string | yes | ID for the account. Must match the ID used for migration. | example: "account-migration-id" |
| `migration.id` | string | yes | ID that you generate for accruals migration. When you send two accruals records with the same ID, only the first record is created.<br><br>When you send two records with the same ID, the system rejects the second record **unless** you send a later `version_date` than the first record's `version_date` to ensure idempotency.<br> | maxLength: 60; example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `migration.authorization_id` | string | no | Record ID for `DECENDIAL_IOF` accruals that identifies the authorization of the accrual. `DECENDIAL_IOF` is a Brazilian tax charged on a loan or an installment. (Installments are considered a type of loan.)<br> | example: "accountMigrationId_referenceNumber_planCode_authorizationType" |
| `accounting_date` | string | no | Accounting date for the migration, which you must set to the go-live date. Format = YYYY-MM-DD. | format: "date"; example: "2022-03-28" |
| `metadata` | object | no | Accruals metadata (free-form fields) formatted as a JSON object using any key-value pairs.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"key1": "value1", "key2": "value2"} |
| `type` | string | no | Accrual type <br><br>**Note:** Do not use `DECENDIAL_IOF` or `WITHDRAW_IOF` as these are **outdated**.<br><br>- `REFINANCING`—Interest accrual amounts where the cardholder pays less than the minumum invoice amount<br>- `NOTACCRUABLE_NOTFINEABLE`—Amounts that are not subject to accruals or fines<br> | enum: ["REFINANCING", "DECENDIAL_IOF", "WITHDRAW_IOF", "NOTACCRUABLE_NOTFINEABLE"]; example: "REFINANCING" |
| `authorization_type` | string | no | Authorization type of the transaction. **Note:** Required when accrual type is `DECENDIAL_IOF`, however `DECENDIAL_IOF` is outdated and should not be used. | enum: ["PLATFORM", "NETWORK", "ON_US", "BANKING"]; deprecated: true; example: "PLATFORM" |
| `projected_values` | array of object | no | List of projected accrual values, for an account between cycle closing and due date. (For pending accruals, use a `values` array.) These values will be split between the dates ranging from cycle closing date (exclusive) up to the due date. For projected `REFINANCING` accruals, the interest is on revolving charges. These charges might be reversed if the account receives an advance payment. If the projection occurs on the cutoff date, the projected balance is calculated to match the actual amount between the cutoff and the invoice due date. |  |
| `projected_values[].type` | string | no | The type of accrual value | enum: ["REFINANCING", "IOF", "OVERDUE", "FINE"]; example: "REFINANCING" |
| `projected_values[].amount` | string | no | The calculated accrual amount. | example: "2.55" |
| `projected_values[].interest_rate` | number | no | Accrual interest rate | format: "float"; minimum: 0; example: 1 |
| `values` | array of object | no | List of accrual values for pending accruals. (For projected accruals, use a `projected_values` array.)<br>For pending `REFINANCING` accruals, the original processor calculated the value for revolving overdue charges. The pending amount refers to a daily amount for the period from the day after the due date in the prior month (M-1) up to the go-live date (known in Brazil as "saldo rotativo"). Pass the value when the account holder paid less than the Total Amount Due (TAD).<br> |  |
| `values[].amount` | string | no | Accrual amount | example: "2.55" |
| `values[].type` | string | no | Accrual amount type<br><br>- `REFINANCING`—Original processor's interest amounts. These daily accruals are applied to transactions on the cycle closing date and relate to overdue balances—either revolving balances (known in Brazil as "saldo rotativo") or overdue amounts from payment agreements. The pending accruals are summarized by account using two decimal places. This accrual split covers the period from the day after the due date in the prior month (M-1) up to the go-live date.<br>- `IOF`—Accrual related to the Brazilian tax calculated on a loan or an installment<br>- `OVERDUE`—Interest accrued on late payment<br>- `FINE`—Provides the fine value for the next cycle. Send this `FINE` accrual type when the account holder paid less than the minimum invoice amount.<br> | enum: ["REFINANCING", "IOF", "OVERDUE", "FINE"]; example: "REFINANCING" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 500 | Internal Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

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
| `migration-accrual-incoming-1` | https://developers.pismo.io/events/docs/migration-accrual-incoming-1 |
| `migration-accrual-outgoing-1` | https://developers.pismo.io/events/docs/migration-accrual-outgoing-1 |
| `migration-organize-statement-outgoing-1` | https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `3`, deprecated `False`.

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
| `api-specs/Migrations.yaml` | tag `Accrual migration`: POST /v1/migrations/accruals | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
