---
ku_id: KU-API-migrations--recurring-charge-plan-migration
title: 'API reference: Migrations — Recurring charge plan migration'
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
- PostRecurringChargePlansV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Recurring charge plan migration

**KU ID:** `KU-API-migrations--recurring-charge-plan-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Recurring charge plan migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Recurring charge plan migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/recurring-charge-plans` | `PostRecurringChargePlansV1` | Migrate recurring charge plans | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/recurring-charge-plans operationId=PostRecurringChargePlansV1 -->
### `POST /v1/migrations/recurring-charge-plans` — Migrate recurring charge plans

- **operationId:** `PostRecurringChargePlansV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Recurring charge plan migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of **recurring charge plans**. (A recurring charge plan defines a recurring charge such as an annual fee, which is applied on a fixed schedule, and the number of installments [cycles] to which the charge should be applied.)
>
> This endpoint generates the following events:
>
> - [Recurring Charge plan migration started](https://developers.pismo.io/events/docs/migration-recurring-charge-plan-incoming-1)
>
> - [Recurring charge plan migration completed](https://developers.pismo.io/events/docs/migration-recurring-charge-plan-outgoing-1)

#### Request body

Required: no

> Migrates a recurring charge plan

**Content type `application/json`** — schema: object (schema `PostRecurringChargePlansV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `origin` | string | no | Migration origin | enum: ["FILE", "API"]; example: "FILE" |
| `migration` | object | yes | Additional migration details |  |
| `migration.id` | string | yes | Migration ID | maxLength: 255; example: "a-unique-plan-id" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `description` | string | no | Description for the recurring charge transactions. Use the placeholder {counter} to indicate where the cycle count should be placed. <br><br>For example, `{counter} Annuity` generates `2/12 Annuity`.<br> | example: "Additional Card Annuity {counter}" |
| `discount_percentage` | number | no | Percentage value to be discounted if `first_cycles_to_discount` is configured. Typically, a number from 0 to 100. | format: "double"; example: 12.5 |
| `first_cycles_to_discount` | integer | no | Number of cycles the `discount_percentage` is applied to before reverting to the full charge. This value must be less than `number_of_cycles`. | example: 3 |
| `installment_amount` | number | no | Full amount of a recurring charge installment before any discount is applied | format: "double"; example: 500.61 |
| `minimum_spend_to_charge` | number | no | Minimum debit amount on statement to enable cycle charging. If not configured, the charge plan does not check the debit statement amount. | format: "double"; example: 100 |
| `number_of_cycles` | integer | no | Number of cycles for which the plan generates charges. Must be greater than `first_cycles_to_discount`. | format: "int32"; example: 12 |
| `processing_code` | string | no | Transaction processing code. If `split_transaction` is `true`, this is the processing code for the debit (primary) transaction. | example: "220042" |
| `renew_method` | string | no | Renewal method. Options to automatically renew the recurring charge plan at the end of the cycle. | enum: ["NO_RENEW", "WITHOUT_DISCOUNT", "WITH_DISCOUNT"]; example: "NO_RENEW" |
| `secondary_description` | string | no | Description for the credit (secondary) transaction, created when `split_transaction` is set to `true`. For example, use `Annual Plan Discount {counter}` to indicate cycle count placement. | example: "Annual Plan Discount" |
| `secondary_processing_code` | string | no | Processing code used to create the secondary transaction, when `split_transaction` is set to `true`. | example: "200032" |
| `split_transaction` | boolean | no | Split transaction for the recurring charge amount? <br><br>Controls how installment amount and discounts are applied in each cycle. If `false`, a single debit transaction for the net amount is posted. If `true`, separate debit and credit transactions are posted. These consist of the full `installment_amount` (primary transaction) and the discount value (secondary transaction).<br> | example: true |

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
| `migration-recurring-charge-plan-incoming-1` | https://developers.pismo.io/events/docs/migration-recurring-charge-plan-incoming-1 |
| `migration-recurring-charge-plan-outgoing-1` | https://developers.pismo.io/events/docs/migration-recurring-charge-plan-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `2`, deprecated `False`.

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
| `api-specs/Migrations.yaml` | tag `Recurring charge plan migration`: POST /v1/migrations/recurring-charge-plans | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
