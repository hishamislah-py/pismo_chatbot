---
ku_id: KU-API-migrations--customer-migration
title: 'API reference: Migrations — Customer migration'
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
- PostCustomersV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Customer migration

**KU ID:** `KU-API-migrations--customer-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Customer migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Customer migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/customers` | `PostCustomersV1` | Migrate customers | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/customers operationId=PostCustomersV1 -->
### `POST /v1/migrations/customers` — Migrate customers

- **operationId:** `PostCustomersV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Customer migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start customer migration. Use this endpoint to migrate additional customers after an account is migrated using the [Migrate accounts endpoint](ref:postaccountsv2).
>
> This endpoint produces the following events:
>   - [Customer migration started](https://developers.pismo.io/events/docs/migration-customer-incoming-1)
>
>   - [Customer migration completed](https://developers.pismo.io/events/docs/migration-customer-outgoing-1)

#### Request body

Required: no

> Start migration of customers

**Content type `application/json`** — schema: object (schema `PostCustomersV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Applicant additional migration information |  |
| `migration.account_id` | string | yes | Record identifier for the account migration | maxLength: 60; example: "account-migration-id" |
| `migration.id` | string | yes | Record customer identifier that you provide for migration purposes.<br><br>**Note**: Using [LGPD](https://en.wikipedia.org/wiki/General_Personal_Data_Protection_Law) (Lei Geral de Proteção de Dados Pessoais), PCI or any other sensitive personal data for migration ID poses serious security risks, this includes your <<glossary:document_number>>, PAN, or telephone number. For enhanced security, use hash for this field ([SHA-256 with salt](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/) is recommended).<br> | maxLength: 60; example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `is_active` | boolean | no | Is customer active?<br><br>**Note:** If the program containing the account is configured to prevent multiple cardholders, `is_active = false`, overrides this block.<br> | default: true; example: false |
| `social_name` | string | no | Social name of the customer | example: "John Doe" |
| `email` | string | no | Customer's email address | example: "john_doe@email.com" |
| `entity` | object | no | Customer entity |  |
| `entity.name` | string | no | Customer's name | example: "John Doe" |
| `entity.document_number` | string | no | Customer's <<glossary:document_number>> | example: "12345678901" |
| `entity.registration` | string | no | Customer's registration number | example: "12345678901" |
| `entity.birth_date` | string | no | Customer's birth date | format: "date"; example: "1985-01-19" |
| `entity.gender` | string | no | Customer's gender | enum: ["F", "M"]; example: "F" |
| `entity.mother_name` | string | no | Customer's mother's name. When applying for a registration number in Brazil, such as a Brazilian ID card (also known as Registro Geral), it is customary to also use the name of the applicant's mother to apply, this ensures that the applicant's ID is unique. | example: "Jane Doe" |
| `entity.marital_status` | (type not declared) | no | Customer's marital status | enum: ["SINGLE", "MARRIED", "DIVORCED", "WIDOWER"]; example: "SINGLE" |

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
| `migration-customer-incoming-1` | https://developers.pismo.io/events/docs/migration-customer-incoming-1 |
| `migration-customer-outgoing-1` | https://developers.pismo.io/events/docs/migration-customer-outgoing-1 |

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
| `api-specs/Migrations.yaml` | tag `Customer migration`: POST /v1/migrations/customers | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
