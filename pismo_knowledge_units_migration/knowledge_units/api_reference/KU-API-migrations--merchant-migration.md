---
ku_id: KU-API-migrations--merchant-migration
title: 'API reference: Migrations — Merchant migration'
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
- PostMerchantsV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Merchant migration

**KU ID:** `KU-API-migrations--merchant-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Merchant migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Merchant migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/merchants` | `PostMerchantsV1` | Migrate merchants | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/merchants operationId=PostMerchantsV1 -->
### `POST /v1/migrations/merchants` — Migrate merchants

- **operationId:** `PostMerchantsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Merchant migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of merchant details, such as marketplace ID, brand name, contact and creditor information.
>
> This endpoint generates the following events:
>
> - [Merchant migration started](https://developers.pismo.io/events/docs/migration-merchant-incoming-1)
>
> - [Merchant migration completed](https://developers.pismo.io/events/docs/migration-merchant-outgoing-1)

#### Request body

Required: no

> Start migration of Merchant details

**Content type `application/json`** — schema: object (schema `PostMerchantsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `origin` | string | no | Migration source type | enum: ["FILE", "API"]; example: "FILE" |
| `migration` | object | yes | Additional migration details |  |
| `migration.id` | string | yes | Merchant ID. To ensure idempotency, when you send two merchant records with the same ID, the Pismo platform rejects the second record **unless** you send a `version_date` that is later than the first record's `version_date`. | maxLength: 255; example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `additional_area_code` | string | no | Area code for the merchant's `additional_phone` number | maxLength: 4; example: "763" |
| `additional_phone` | string | no | Additional phone number of the merchant | maxLength: 25; example: "555-5678" |
| `address` | string | no | Merchant address | maxLength: 80; example: "1000 Main Street San Francisco, CA 94105" |
| `area_code` | string | no | Area code of the merchant's phone number.<br> | maxLength: 4; example: "415" |
| `brand_name` | string | no | Merchant's brand name | maxLength: 50; example: "Merchant Brand" |
| `city` | string | no | Merchant city | maxLength: 60; example: "San Francisco" |
| `city_code` | string | no | Official seven-digit numeric code of the city according to the [IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php) (Brazilian Institute of Geography and Statistics) code table. Used only for cities in Brazil; this code is unique per city. | maxLength: 50; example: "3550308" |
| `complementary_address` | string | no | Merchant's additional address details. Any additional information that helps to identify the merchant's location such as building, apartment, or floor | maxLength: 50; example: "Suite 500" |
| `contact` | string | no | Name of a merchant representative | maxLength: 50; example: "John Doe" |
| `country` | string | no | Merchant address country name | maxLength: 30; example: "United States" |
| `document_number` | string | no | Merchant's <<glossary:document number>><br> | maxLength: 14; example: "54938832011" |
| `email` | string | no | Merchant's email address | maxLength: 255; example: "merchantbrand@gmail.com" |
| `external_code` | string | no | Merchant category code that indicates business type. Use the [Get business category](ref:getbusinesscategory) endpoint to get a list of business categories and their external codes.<br> | maxLength: 45; example: "1234567890" |
| `marketplace_id` | integer | no | Marketplace ID from [Pismo Control Center](doc:pismo-control-center-overview) | format: "int64"; example: 3213 |
| `municipal_registration` | string | no | Merchant's municipal registration number. In Brazil, this is the ID number that a business receives when it registers with the municipal tax department.<br> | maxLength: 15; example: "347219312" |
| `name` | string | no | Merchant's name | maxLength: 100; example: "Lombard Street Coffee & Tea" |
| `neighborhood` | string | no | Merchant's neighborhood details. In Brazil, addresses include the neighborhood name, but in other countries, they might not. | maxLength: 50; example: "Castle" |
| `number` | integer | no | Merchant's address number | format: "int64"; example: 312 |
| `phone` | string | no | Merchant's phone number. Parentheses and dashes are optional. | maxLength: 25; example: "99845767" |
| `program_id` | integer | no | Program ID for the merchant account | format: "int64" |
| `state` | string | no | Abbreviation or full name of the merchant state, province, or administrative division. | maxLength: 2; example: "CA" |
| `zip_code` | string | no | Merchant's postal code. Postal codes are called zip codes in the United States. You can also use other types of postal code here.<br> | maxLength: 9; example: "94105" |
| `creditor` | object | no | Response from merchant creditor. The merchant creditor is the entity the merchant receives money from when settling a transaction. The entity can be an external bank account or a Pismo account.<br> |  |
| `creditor.name` | string | no | Creditor name | maxLength: 100; example: "Merchant name" |
| `creditor.advancement_fee` | number | no | Advancement fee for creditor | format: "float"; example: 15.4 |
| `creditor.discount_rate` | number | no | Discount rate for creditor | format: "float"; example: 11.5 |
| `creditor.maximum_advancement_percentage` | number | no | Maximum advancement percentage for the creditor | format: "float"; example: 10.5 |
| `creditor.crediting_method` | string | no | Crediting method | example: "ACCOUNT" |
| `metadata` | object | no | Merchants's metadata<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"merchant_form_on_us": false, "key2": "value2"} |

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
| `migration-merchant-incoming-1` | https://developers.pismo.io/events/docs/migration-merchant-incoming-1 |
| `migration-merchant-outgoing-1` | https://developers.pismo.io/events/docs/migration-merchant-outgoing-1 |

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
| `api-specs/Migrations.yaml` | tag `Merchant migration`: POST /v1/migrations/merchants | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
