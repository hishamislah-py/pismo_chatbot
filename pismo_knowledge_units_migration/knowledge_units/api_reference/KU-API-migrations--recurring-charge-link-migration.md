---
ku_id: KU-API-migrations--recurring-charge-link-migration
title: 'API reference: Migrations — Recurring charge link migration'
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
- PostRecurringChargeLinksV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Recurring charge link migration

**KU ID:** `KU-API-migrations--recurring-charge-link-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Recurring charge link migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Recurring charge link migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/recurring-charge-links` | `PostRecurringChargeLinksV1` | Migrate recurring charge links | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/recurring-charge-links operationId=PostRecurringChargeLinksV1 -->
### `POST /v1/migrations/recurring-charge-links` — Migrate recurring charge links

- **operationId:** `PostRecurringChargeLinksV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Recurring charge link migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of **recurring charge links** for an account. (A recurring charge link associates an active recurring charge plan with an account, so that the charges defined for the plan are applied to the account.)
>
> This endpoint generates the following events:
>
> - [Recurring Charge link migration started](https://developers.pismo.io/events/docs/migration-recurring-charge-link-incoming-1)
>
> - [Recurring charge link migration completed](https://developers.pismo.io/events/docs/migration-recurring-charge-link-outgoing-1) (one event for **each item** in the `links` array in the payload)

#### Request body

Required: no

> Migrates recurring charge links

**Content type `application/json`** — schema: object (schema `PostRecurringChargeLinksV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Additional migration details |  |
| `migration.account_id` | string | yes | Migration ID for the account that will be linked to the recurring charge plans | example: "a-migration-account-id" |
| `links` | array of object (schema `PostRecurringChargePlanLinkV1Item`) | yes |  | minItems: 1 |
| `origin` | string | no | Migration origin | enum: ["FILE", "API"]; example: "FILE" |

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
| `migration-recurring-charge-link-incoming-1` | https://developers.pismo.io/events/docs/migration-recurring-charge-link-incoming-1 |
| `migration-recurring-charge-link-outgoing-1` | https://developers.pismo.io/events/docs/migration-recurring-charge-link-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `2`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/PostRecurringChargePlanLinkV1Item -->
### Schema `PostRecurringChargePlanLinkV1Item`

Pointer: `#/components/schemas/PostRecurringChargePlanLinkV1Item`. Type: object (schema `PostRecurringChargePlanLinkV1Item`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration_id` | string | yes | Link migration ID. ID for the relationship link between account and plan. | example: "a-unique-migration-id" |
| `migration_version` | string | yes | Migration date for updated data. Format = YYYY-MM-DDTHH:mm:ssZ. | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `description` | string | no | Description of the scheduled charge that's linked to the account. Use {counter} to specify where the cycle count should be placed. For example, the `Annuity {counter}` generates `Annuity 2/12` for the second of twelve annuities. If {counter} has not passed, it is placed at the end of the description. If no description is passed, the transaction type's description is used and the counter is not shown. | maxLength: 100; example: "Account-Specific Annuity Fee" |
| `post_installment_charge_on_current_cycle` | boolean | no | Apply the recurring charge on the current account cycle? If `false`, charges are applied in the next account cycle. | example: false |
| `recurring_charge_plan_id` | integer | no | ID of the recurring charge plan to link to the account. When this field is passed, the value in `recurring_charge_plan_migration_id` is ignored. | example: 123321 |
| `recurring_charge_plan_migration_id` | string | no | Migration ID of the recurring charge plan to link to the account, in cases where the plan was also migrated. Either this field or `recurring_charge_plan_id` is **REQUIRED**. | maxLength: 255; example: "migration-plan-id" |
| `renew` | boolean | no | Renew link automatically after the last cycle? | default: false; example: true |
| `start_installment_charge_in` | integer | no | The installment at which charges begin. For example, if `start_installment_charge_in` is `3`, the charge is applied starting with cycle 3. It's not applied to cycles 1 and 2. If `post_installment_charge_on_current_cycle` is `true`, `start_installment_charge_in` should be `null`. If `false`, it must be greater than or equal to the current cycle and less than or equal to `number_of_cycles`. | example: 6 |

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
| `api-specs/Migrations.yaml` | tag `Recurring charge link migration`: POST /v1/migrations/recurring-charge-links | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
