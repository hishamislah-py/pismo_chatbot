---
ku_id: KU-API-migrations--dispute-migration
title: 'API reference: Migrations — Dispute migration'
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
operations:
- PostDisputeV1
related_kus:
- KU-ERR-codes-esmg-to-whis
specification_version: 0.0.7
---

# API reference: Migrations — Dispute migration

**KU ID:** `KU-API-migrations--dispute-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Dispute migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Dispute migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/disputes` | `PostDisputeV1` | Migrate disputes | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/disputes operationId=PostDisputeV1 -->
### `POST /v1/migrations/disputes` — Migrate disputes

- **operationId:** `PostDisputeV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Dispute migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Starts the migration of a dispute

#### Request body

Required: no

> Migrate disputes

**Content type `application/json`** — schema: object (schema `PostDisputeV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes |  |  |
| `migration.id` | string | yes | Record ID for migration purposes | pattern: "^[a-zA-Z0-9-._]+$"; maxLength: 255; example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `migration.authorization_id` | string | no | Migration ID of the authorization this dispute is associated with, if applicable. | pattern: "^[a-zA-Z0-9-._]+$"; maxLength: 255 |
| `migration.card_id` | string | no | Migration ID of the card this dispute is associated with, if applicable. This field is **required** when an `authorization_id` is not provided. | pattern: "^[a-zA-Z0-9-._]+$"; maxLength: 255 |
| `modality` | integer | no | Reason code for the dispute, as defined by the card network. | example: 30 |
| `comment` | string | no | Client custom dispute comment (used to explain why a dispute is partial, for example). | maxLength: 5000; example: "Custom comment" |
| `disputed_amount` | number | no | Amount being disputed. | format: "float"; minimum: 0; example: 50.42 |
| `network_brand_type` | string | no | Network brand where the transaction under dispute occurred. | maxLength: 255; example: "ELO" |
| `is_partial` | boolean | no | Is this a partial dispute? | example: true |
| `airport_tax` | boolean | no | Is this dispute related to an airport tax? | example: true |
| `airport_tax_partial` | boolean | no | Should the airport tax be partially disputed? | example: true |
| `airport_tax_amount` | number | no | Airport tax amount being disputed. | minimum: 0; example: 30 |
| `arn` | string | no | Acquirer reference number. | pattern: "^[a-zA-Z0-9-._]+$"; maxLength: 255; example: "123456" |
| `transaction_date` | string | no | Date of the transaction this dispute is associated with. **Required** when `authorization_id` is not provided. | format: "date"; example: "2024-09-08" |
| `transaction_amount` | number | no | Amount of the transaction this dispute is associated with. **Required** when `authorization_id` is not provided. | format: "float"; minimum: 0; example: 40 |
| `authorization_code` | string | no | Authorization code of of the transaction this dispute is associated with. **Required** when `authorization_id` is not provided. | example: "123455" |
| `status` | string | no | Status of the dispute being migrated. For a glossary of valid statuses, refer to [Migration statuses and events](doc:disputes-state-machine#migration-statuses-and-events). | example: "SECOND_PRESENTMENT" |
| `installment_number` | integer | no | Number of the installment the dispute is associated to. **Required** when the dispute is related to an installment transaction. | minimum: 1; example: 1 |
| `installment_disputed_amount` | number | no | Installment amount being disputed. **Required** when the dispute is related to an installment transaction. | format: "float"; minimum: 0 |
| `pre_arb_is_partial` | boolean | no | Is the pre-arbitration amount for a partial amount dispute, represented by `pre_arb_amount`? If empty, disputes are created as full amount, same as `false`. | example: true |
| `pre_arb_amount` | number | no | Pre-arbitration amount being disputed. **REQUIRED** when `pre_arb_is_partial` = `true`. | format: "float"; minimum: 0; example: 30 |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `0`, deprecated `False`.

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
| `api-specs/Migrations.yaml` | tag `Dispute migration`: POST /v1/migrations/disputes | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
