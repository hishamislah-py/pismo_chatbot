---
ku_id: KU-API-migrations--token-migration
title: 'API reference: Migrations — Token migration'
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
- PostTokensV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Token migration

**KU ID:** `KU-API-migrations--token-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Token migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Token migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/tokens` | `PostTokensV1` | Migrate tokens | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/tokens operationId=PostTokensV1 -->
### `POST /v1/migrations/tokens` — Migrate tokens

- **operationId:** `PostTokensV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Token migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of tokens.
>
> This endpoint generates the following events:
>
> - [Token migration started](https://developers.pismo.io/events/docs/migration-token-incoming-1)
>
> - [Token migration completed](https://developers.pismo.io/events/docs/migration-token-outgoing-1)

#### Request body

Required: no

> Start migration of tokens

**Content type `application/json`** — schema: object (schema `TokensV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `expiry_date` | string | yes | Token expiration date. Format = YYMM | pattern: "\\\\d{4}"; example: "1712" |
| `migration` | object | yes | Applicant additional migration information |  |
| `migration.card_id` | string | yes | Card ID. Matches the `migration.id` value from the [Migrate cards](ref:postcardsv1) endpoint. | minLength: 1; example: "card-migration-id" |
| `migration.id` | string | yes | Record ID for migration purposes | minLength: 1; example: "93dd64fe-6819-4820-b776-aee0aad331" |
| `migration.phase_id` | string | yes | Migration phase ID. Account migration usually is split into multiple phases, where each phase has a unique ID. When assigning a phase ID, you should use a name that is meaningful.<br> | minLength: 1; maxLength: 60; example: "Feb2025_Phase_3_of_4" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `network` | string | yes | Product code of flag tokenization | minLength: 1; maxLength: 10; example: "MDES" |
| `status` | string | yes | Token status. Card status is not considered for token migration. | enum: ["ACTIVE", "INACTIVE", "FAILED", "SUSPENDED", "DEACTIVATED"]; example: "ACTIVE" |
| `tc_date_time` | string | yes | Date-time of token confirmation message (token creation). Format = `yyyy-MM-ddTHH:mm:ssZ` | format: "date-time"; example: "2022-01-06T18:00:00Z" |
| `token` | string | yes | MASTERCARD/VISA token ID. Not used for online authorizations, only provisioning. | maxLength: 255; example: "TOKEN-00000123123123123" |
| `token_unique_ref` | string | yes | Brand network token ID | maxLength: 255; example: "DSAPMC0000128257301397f527cb486988267a975ec78d9m" |
| `wallet_identifier` | string | yes | Digital wallet identifier from the network<br>Examples: <br>`40010036958` -PayPal<br>`40010075338` -Visa Checkout<br>`101` -Masterpass by Mastercard<br> | minLength: 1; maxLength: 50; example: "101" |
| `card_holder_name` | string | no | Cardholder name. Note that the client can customize the name displayed in a wallet. For sandbox testing, pass `SKIP NETWORK CALL` to bypass network validation. | example: "card_holder_name-value" |
| `correlation_id` | string | no | Tokenization request ID | minLength: 1; maxLength: 52 |
| `device_id` | string | no | Device identifier | minLength: 1; maxLength: 48 |
| `devices_binding` | boolean | no | Is the token bound to the device? | default: false; example: true |
| `event_date_time` | string | no | Date of last token status change or creation date if no changes occurred. Format = yyyy-MM-dd-HH.mm.ss.SSSSSS | format: "date-time"; example: "2022-01-06T18:00:00Z" |
| `line_number` | string | no | File line number (when using batch file import migration) in the migrating entity file. | example: "232" |
| `metadata` | object | no | JSON format (free-form field)<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |
| `pan_unique_ref` | string | no | PAN reference code | minLength: 1; maxLength: 255; example: "FM4MMC0000128257de72f1876cf2420595c01161f10558a1" |
| `payment_application_instance_id` | string | no | Payment application ID installed on a device. Mastercard only. | minLength: 48; maxLength: 48; example: "MTUwMjIyMDEwNjAwMzA3MDUz00J1VKm8QDQ7esDjkz0dnu4i" |
| `token_type` | string | no | MASTERCARD/VISA token type. Not used for online authorizations, only provisioning. | enum: ["HCE", "QRC", "1", "5", "MASTERCARD_CLOUD_BASED_PAYMENTS", "CARD_ON_FILE", "ECOMMERCE", "SECURE_ELEMENT", "EMBEDDED_SECURE_ELEMENT", "C", "S"]; example: "ECOMMERCE" |

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
| `migration-token-incoming-1` | https://developers.pismo.io/events/docs/migration-token-incoming-1 |
| `migration-token-outgoing-1` | https://developers.pismo.io/events/docs/migration-token-outgoing-1 |

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
| `api-specs/Migrations.yaml` | tag `Token migration`: POST /v1/migrations/tokens | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
