---
ku_id: KU-API-migrations--balance-migration
title: 'API reference: Migrations — Balance migration'
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
- PostBalanceControlV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Balance migration

**KU ID:** `KU-API-migrations--balance-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Balance migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Balance migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/balance-control` | `PostBalanceControlV1` | Migrate balances | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/balance-control operationId=PostBalanceControlV1 -->
### `POST /v1/migrations/balance-control` — Migrate balances

- **operationId:** `PostBalanceControlV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Balance migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> This endpoint enables you to migrate balances from your legacy platform to the Pismo platform &#8212; after statement migration but only before Go-live. This allows the platform to calculate retroactive accruals even if you did not perform daily accruals on your legacy platform. You also may split balances to indicate which ones are accruable and fineable. When migrating balances, all transaction types must be configured. Refer to [Setting transaction types to block accrual charges](https://developers.pismo.io/pismo-docs/docs/configuring-transaction-types-to-not-accrue-charges) for more information.
>
> This endpoint generates the following events:
> - [Balance control migration started](https://developers.pismo.io/events/docs/migration-balance-control-incoming-1)
> - [Balance control migration completed](https://developers.pismo.io/events/docs/migration-balance-control-outgoing-1)
> - [Statement organized completed](https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1) — emitted when the organize-statement process runs, indicating whether the account's statements were organized successfully or the processing failed. Emission is opt-in.

#### Request body

Required: no

> Start migration of a Migration Balance Control

**Content type `application/json`** — schema: object (schema `PostBalanceControlV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Additional information for Balance control migration |  |
| `migration.account_id` | string | yes | ID for the account. Must match the ID used for account migration. | example: "account-migration-id" |
| `migration.id` | string | yes | Migration ID for a balance control | example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `accrual_date_cutoff` | string | yes | Date up to which the Pismo platform should calculate accruals for a migrated balance. Format = `yyyy-mm-dd`. This date should match the Go-live date. The platform calculates accruals starting from the day after the payment due date to the cut-off date.<br> | format: "date"; example: "2024-02-22" |
| `calculate_retroactive_accruals` | boolean | yes | Calculate retroactive accruals on the Pismo platform? | default: false; example: true |
| `balance_types` | array of object | no | A collection of balance type (accrual amount and type) |  |
| `balance_types[].balance_type` | string | no | Customer's categorized balance (accruable and fineable) that needs to be retroactively calculated. Balance migration is necessary to set the initial balance of a migrated account on the Pismo platform. Optionally, you can split closed balances to indicate which ones are accruable (or not) and fineable (or not). To learn more about these calculations, refer to the [Migrations guide](doc:migrations-overview#balances).<br>The values relate to the following transaction types (TT):<br>- `ACCRUABLE_FINEABLE` (TT 6901)<br>- `ACCRUABLE_NOTFINEABLE` (TT 6903)<br>- `NOTACCRUABLE_FINEABLE` (TT 6902)<br>- `NOTACCRUABLE_NOTFINEABLE` (TT 6904)<br>- `CREDIT` (TT 6905)<br> | enum: ["ACCRUABLE_FINEABLE", "ACCRUABLE_NOTFINEABLE", "NOTACCRUABLE_FINEABLE", "NOTACCRUABLE_NOTFINEABLE", "CREDIT"]; example: "CREDIT" |
| `balance_types[].balance_amount` | number | no | The `balance_amount` represents the customer's position based on the most recent due statement at the time of migration. Use the rules below to determine the correct value:<br>- If the account has a statement between the due date and the cycle closing date at the time of migration:<br>  Consider the open statement as M (Migration) and use the current balance of the most recent statement (M-1 statement).<br>- If the account has a statement between the cycle closing date and the due date:<br>  Consider the open statement as M (Migration) and use the current balance of the last statement (M-2 statements).<br>- If the account has no due statements at the time of migration (for example, an account in its first statement cycle):<br>  Set `balance_amount` to 0.<br> | format: "double"; example: 255.96 |

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
| `migration-balance-control-incoming-1` | https://developers.pismo.io/events/docs/migration-balance-control-incoming-1 |
| `migration-balance-control-outgoing-1` | https://developers.pismo.io/events/docs/migration-balance-control-outgoing-1 |
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
| `api-specs/Migrations.yaml` | tag `Balance migration`: POST /v1/migrations/balance-control | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
