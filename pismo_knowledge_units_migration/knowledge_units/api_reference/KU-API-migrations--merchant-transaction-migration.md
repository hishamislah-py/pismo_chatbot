---
ku_id: KU-API-migrations--merchant-transaction-migration
title: 'API reference: Migrations — Merchant transaction migration'
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
- PostMerchantTransactionsV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Merchant transaction migration

**KU ID:** `KU-API-migrations--merchant-transaction-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Merchant transaction migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Merchant transaction migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/merchants/transactions` | `PostMerchantTransactionsV1` | Migrate merchant transactions | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/merchants/transactions operationId=PostMerchantTransactionsV1 -->
### `POST /v1/migrations/merchants/transactions` — Migrate merchant transactions

- **operationId:** `PostMerchantTransactionsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Merchant transaction migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of Merchant transaction details such as authorization ID, merchant ID, marketplace ID, and so on.
>
> This endpoint generates the following events:
>
> - [Merchant Transaction migration started](https://developers.pismo.io/events/docs/migration-merchant-transaction-incoming-1)
>
> - [Merchant transactions migration completed](https://developers.pismo.io/events/docs/migration-merchant-transaction-outgoing-1)

#### Request body

Required: no

> Start migration of Merchant transactions

**Content type `application/json`** — schema: object (schema `PostMerchantTransactionsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Applicant additional migration information |  |
| `migration.authorization_id` | string | yes | ID for OnUs authorization. This must be the same ID used in OnUs authorization migration.<br> | example: "authorization-migration-id" |
| `migration.id` | string | yes | Client-generated ID for a merchant transaction<br> | maxLength: 255; example: "merchantid" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `migration.merchant_id` | string | no | Client-generated ID for the merchant. This must be the same ID used in merchant migration. | example: "merchant-migration-id" |
| `migration.original_authorization_id` | string | no | Record identifier for the original authorization. You use this field to cancel transactions. | example: "original-authorization-migration-id" |
| `origin` | string | no | Migration source type | enum: ["FILE", "API"]; example: "FILE" |
| `merchant_id` | integer | no | Merchant ID assigned by the Pismo platform. If you provide this ID, the `migration.merchant_id` is not used. | format: "int64"; example: 3213 |
| `marketplace_id` | integer | no | Marketplace ID on the Pismo platform | format: "int64"; example: 3213 |
| `terminal_id` | string | no | Merchant's external terminal ID previously saved on the Pismo platform (terminal registration flow). You must pass the terminal ID if the terminal has relevance for the operation.<br> | maxLength: 50; example: "1234567890" |
| `processing_code` | string | no | Pismo platform **processing code** (custom alphanumeric identifier that defines how to handle a certain financial operation type).<br><br>Processing codes integrate with the transaction flow on the platform. The platform uses predefined processing codes to evaluate and process operations. For more information, refer to [Processing codes and transaction types](doc:processing-codes-and-transaction-types).<br> | example: "00" |
| `transaction_amount` | number | no | Transaction amount. If the transaction is an installment, this value must be the installment amount. | format: "float"; example: 56.78 |
| `mdr_amount` | number | no | Merchant Discount Rate (MDR) tax amount (Brazil only). Default is `0`. For details about MDR, refer to the [Marketplace Creditor Operation](doc:seller-management-overview#marketplace-creditor-operation) section of the *Seller management overview* guide.<br> | default: 0; format: "float"; example: 1.15 |
| `installment` | integer | no | Current installment | example: 1 |
| `number_of_installments` | integer | no | Total number of installments related to the migrated authorization | example: 1 |
| `event_date` | string | no | Transaction creation date and time (UTC format). Format = YYYY-MM-DDThh:mm:ssZ. | format: "date-time"; example: "2021-09-21T12:00:00Z" |
| `scheduled_payment_date` | string | no | Scheduled date to settle the transaction. Setting a future date and the status to `PENDING` schedules the transaction. For settlements that already occurred, the status is `PAID`. | format: "date"; example: "2021-09-21" |
| `transaction_status` | string | no | Transaction status<br> | enum: ["PENDING", "SCHEDULED", "SETTLED", "PAID", "CANCELED"]; default: "PENDING" |
| `type` | string | no | Transaction type | enum: ["SALE", "CANCEL"]; example: "SALE" |
| `transaction_fee` | number | no | Transaction fee<br> | default: 0; example: 0.25 |
| `mdr_tax` | number | no | Additional MDR tax amount<br> | default: 0; format: "float"; example: 0.25 |
| `metadata` | object | no | Merchant's metadata<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"merchant_form_on_us": false, "key2": "value2"} |

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
| `migration-merchant-transaction-incoming-1` | https://developers.pismo.io/events/docs/migration-merchant-transaction-incoming-1 |
| `migration-merchant-transaction-outgoing-1` | https://developers.pismo.io/events/docs/migration-merchant-transaction-outgoing-1 |

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
| `api-specs/Migrations.yaml` | tag `Merchant transaction migration`: POST /v1/migrations/merchants/transactions | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
