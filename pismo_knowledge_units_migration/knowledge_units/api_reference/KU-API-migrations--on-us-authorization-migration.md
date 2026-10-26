---
ku_id: KU-API-migrations--on-us-authorization-migration
title: 'API reference: Migrations — On-us authorization migration'
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
- PostOnUsAuthorizationsV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — On-us authorization migration

**KU ID:** `KU-API-migrations--on-us-authorization-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `On-us authorization migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> On-us authorization migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/on-us-authorizations` | `PostOnUsAuthorizationsV1` | Migrate on-us authorizations | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/on-us-authorizations operationId=PostOnUsAuthorizationsV1 -->
### `POST /v1/migrations/on-us-authorizations` — Migrate on-us authorizations

- **operationId:** `PostOnUsAuthorizationsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `On-us authorization migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of **on-us authorizations** to the Pismo platform. (An on-us authorization is one that Pismo processes without involving card networks, such as Mastercard or Visa).
>
> This endpoint generates the following events:
>
> - [On-us authorization migration started](https://developers.pismo.io/events/docs/migration-on-us-authorization-incoming-1)
>
> - [On-us authorization migration completed](https://developers.pismo.io/events/docs/migration-on-us-authorization-outgoing-1)

#### Request body

Required: no

> Start migration of on-us authorization data to the Pismo platform

**Content type `application/json`** — schema: object (schema `PostOnUsAuthorizationsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Additional migration details |  |
| `migration.account_id` | string | yes | Client-generated account ID. This value must match `applicant.migration.id` from the [Migrate accounts](https://developers.pismo.io/pismo-docs/reference/postaccountsv1) endpoint. | maxLength: 60; example: "5a8ade4ee89a11eb9dd14b56d86f7a21" |
| `migration.id` | string | yes | ID you generate for on-us authorizations<br><br>**Note:** Using PCI or any other sensitive personal data for migration ID poses serious security risks. This includes a document number, PAN, or telephone number. For enhanced security, use a hash for this field. (SHA-256 with salt is recommended.)<br> | example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `authorization_code` | string | no | Alphanumeric code generated in an authorization request and assigned to the authorization response. | example: "R1CM3D" |
| `authorization_response_code` | string | no | Possible platform-generated response codes returned after authorization is processed.<br> `00`—Successfully authorized <br> `01`—Account not permitted<br> `02`—Processing code not permitted<br> `03`—Authorization denied by flex controls<br> `04`—Insufficient funds<br> `05`—Authorization denied by anti-fraud system<br> `06`—Action not permitted<br> `98`—Request error<br> `99`—Internal platform error<br> | example: "00" |
| `contract_amount` | number | no | Total authorized amount, including fees | format: "float"; example: 15 |
| `currency` | string | no | Requested authorization currency code (ISO 4217) | example: "USD" |
| `datetime_utc` | string | no | Original authorization date (UTC). Format = YYYY-MM-DDThh:mm:ssZ | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `destination_currency` | string | no | Authorized transaction converted to the target currency. This is either a 3-character alphabetic or numeric operation currency code (ISO-4217). | example: "BRL" |
| `entry_mode` | string | no | Method used to capture card data during the authorization process. This field is **REQUIRED** for OnUs transactions. Values typically include:<br>`01`—Chip<br>`02`—Magnetic stripe read<br>`05`—Manual entry<br> | example: "01" |
| `local_amount` | number | no | Authorization amount in local currency | format: "float"; example: 10 |
| `number_of_installments` | integer | no | Total number of installments related to the migrated authorization | example: 1 |
| `payment_datetime` | string | no | Payment date and time (UTC). Determines eligibility for time-based cancellations. Format = yyyy-MM-ddTHH:mm:ssZ | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `principal_amount` | number | no | Total authorized amount (excluding fees) | example: 15 |
| `processing_code` | string | no | Pismo **processing code** (custom alphanumeric identifier that defines how the platform handles a certain financial operation type).<br><br>Processing codes are integral to the transactions flow on the Pismo platform. The platform uses predefined processing codes to evaluate and process operations. For more information, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br><br>**Note:** Check that your computer is already parameterized on the platform before sending the authorization.<br> | example: "00" |
| `tracking_id` | string | no | ID you provide for authorizations<br><br>This field is **REQUIRED** to guarantee the idempotency of a request. Requests that use the same `tracking_id` are considered the same. If `tracking_id` is not passed, each request is treated as a new one.<br><br>A tracking ID is also used after migration for cancellations and confirmations.<br> | example: "example_id_0123" |
| `authorization_denial_code` | string | no | Code for a denied authorization. This is **REQUIRED** if the authorization is denied. | example: "EX001" |
| `authorization_status_id` | integer | no | Authorization status identifier:<br>`1`—TO BE PROCESSED<br>`2`—PROCESSED<br>`3`—DENIED<br>`4`—CANCELED<br>`6`—CANCEL AUTHORIZATION<br>`7`—PRE-AUTHORIZATION<br> | format: "int64"; example: 2 |
| `card_id` | string | no | Record ID for card migration. This is the ID for private label cards.<br><br>**Note:** Using PCI or any other sensitive personal data for migration ID poses serious security risks. This includes a document number, PAN, or telephone number. For enhanced security, use a hash for this field (SHA-256 with salt is recommended).<br> | example: "example_id_0123" |
| `custom_response_code` | string | no | Custom response code for the authorization such as `FL1` for referral authorization | example: "FL1" |
| `description` | string | no | Authorization description | example: "Payment" |
| `installments_plan` | string | no | ID of the installment plan used to calculate this purchase | example: "R1CM3D" |
| `installments_details` | array of object | no | Details about each installment related to the authorization that is being migrated. |  |
| `installments_details[].amortization_amount` | number | no | Amortization amount related to this installment. | format: "float"; example: 111 |
| `installments_details[].installment_amount` | number | no | Amount of this installment. **Note:** Total contract purchase amount is the sum total of all installment amounts.<br> | format: "float"; example: 111 |
| `installments_details[].number` | number | no | Installment number. Used with `number_of_installments` to identify which installment this is. | example: 2 |
| `installments_details[].principal_amount` | number | no | Installment amount without the addition of any fees | format: "float"; example: 111 |
| `ledger_impact` | array of string | no | Limits impacted by the ledger during the authorization<br><br>**Note:** This is a legacy field. Use the `ledger_updates` array instead.<br> | deprecated: true |
| `marketplace_id` | integer | no | Marketplace ID associated with the merchant | format: "int64"; example: 123 |
| `merchant_id` | string | no | Merchant ID associated with the authorization (in case it was not created via migration) | maxLength: 60; example: "example_id_0123" |
| `metadata` | object | no | Any valid JSON (free-form field) formatted as a JSON object using any key-value pairs.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"key1": "value1", "key2": "value2"} |
| `mti` | string | no | Identifies the type of authorization being migrated. Either authorization, cancellation, or confirmation request.<br> `0100`—Authorization <br> `0400`—Cancellation<br> `0202`—Confirmation<br> | example: "0100" |
| `network` | string | no | Card network used in the authorization (such as `VISA`, `MASTERCARD`, or `ELO`) | enum: ["VISA", "MASTERCARD", "ELO"]; example: "VISA" |
| `nsu` | string | no | Card network authorization code sent when a card payment has been approved.<br><br>A NSU (Network Settlement Utility) tracks the flow of funds between parties involved in a payment card transaction. Different payment card networks could have their own NSU systems. For example, Visa has VisaNet, Mastercard has BankNet, or it could be a third-party network.<br> | example: "W123456" |
| `original_authorization_id` | string | no | Pass this field if the authorization is a cancellation. The value must be the cancelled purchase's original migration ID. | example: "example_id_0123" |
| `terminal_id` | string | no | POS terminal ID (TID) associated with the merchant; identifies where an authorization is processed | example: "123" |
| `tid` | string | no | Network transaction ID | example: "123" |
| `update_limit` | boolean | no | Should the authorization affect the account's credit limit?<br><br>**Note:** Only set this to `true` in specific scenarios. Before you enable this option, contact your Pismo representative for guidance.<br> | default: false |

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
| `migration-on-us-authorization-incoming-1` | https://developers.pismo.io/events/docs/migration-on-us-authorization-incoming-1 |
| `migration-on-us-authorization-outgoing-1` | https://developers.pismo.io/events/docs/migration-on-us-authorization-outgoing-1 |

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
| `api-specs/Migrations.yaml` | tag `On-us authorization migration`: POST /v1/migrations/on-us-authorizations | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
