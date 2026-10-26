---
ku_id: KU-API-migrations--authorization-migration
title: 'API reference: Migrations — Authorization migration'
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
- PostAuthorizationsV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
specification_version: 0.0.7
---

# API reference: Migrations — Authorization migration

**KU ID:** `KU-API-migrations--authorization-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Authorization migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Authorization migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/authorizations` | `PostAuthorizationsV1` | Migrate authorizations | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/authorizations operationId=PostAuthorizationsV1 -->
### `POST /v1/migrations/authorizations` — Migrate authorizations

- **operationId:** `PostAuthorizationsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Authorization migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start authorizations migration.
>
> This endpoint generates the following events:
>
> - [Authorization migration started](https://developers.pismo.io/events/docs/migration-authorization-incoming-1)
>
> - [Authorization migration completed](https://developers.pismo.io/events/docs/migration-authorization-outgoing-1)

#### Request body

Required: no

> Start migration of authorizations

**Content type `application/json`** — schema: object (schema `PostAuthorizationsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `acquirer_bin` | string | yes | Authorization acquirer BIN | example: "65153141" |
| `arqc_presence` | boolean | yes | Is authorization ARQC (Authorization Request Cryptogram) present? | example: false |
| `authorization_code` | string | yes | Authorization code generated for this operation (6 alphanumeric characters, DE 38). | example: "R1CM3D" |
| `authorization_response_code` | string | yes | Response code of the authorization (DE 39), such as `00` (Approved) or `51` (Insufficient Funds). This value must be a valid code for the card network.<br> | example: "00" |
| `authorization_status` | string | yes | Authorization status<br>- `PENDING`—Authorizations from Base I pending confirmation<br>- `PROCESSED`—Base II confirmation<br>- `DROPPED`—Authorization discarded if the confirmation (Base II confirmation) is not received within 10 days.<br>- `DECLINED`—Authorization denied when the validation fails (response code <> `00`).<br>- `CANCELLED`—Canceled authorization<br>For information about clearing (Base II) and Base I authorization, refer to [Clearing/base II](doc:clearing).<br> | enum: ["PENDING", "PROCESSED", "DROPPED", "DECLINED", "CANCELLED"]; example: "PENDING" |
| `contract_amount` | number | yes | Total authorization amount with fees | format: "float"; example: 19.9 |
| `currency_conversion_date` | string | yes | Authorization currency conversion date. Format = YYYY-MM-DDTHH:mm:ssZ. | format: "date-time"; example: "2021-08-11T11:25:43.56752Z" |
| `cvv_presence` | boolean | yes | Is authorization CVV present? | example: false |
| `entry_mode` | string | yes | Authorization entry mode (such as `05` - Manual entry or `02` - Magnetic stripe read). | example: "01" |
| `event_date_hour` | string | yes | Local authorization date and time according to value received in flag message (DE 12 and 13 + year). Pismo accepts this value but does not adjust for time zones in reporting or other uses. To order authorizations chronologically, use `event_date_hour_utc`. UTC (Coordinated Universal Time) simplifies comparisons for settlement, SLA tracking, and reporting, and prevents mismatches caused by local offsets. Format = YYYY-MM-DDTHH:MM:SS. | format: "date-time"; example: "2021-08-11T11:25:43" |
| `event_date_hour_utc` | string | yes | Authorization event UTC date and time. UTC (Coordinated Universal Time) simplifies comparisons for settlement, SLA tracking, and reporting, and prevents mismatches caused by local offsets. Format = YYYY-MM-DDTHH:MM:SSZ. | example: "2021-08-11T8:25:43Z" |
| `local_amount` | number | yes | Local currency value (DE 04), indicating the amount the cardholder requested in the acquirer's local currency or the transaction's source location. | format: "float"; example: 15.35 |
| `local_currency_code` | string | yes | Local ISO-4217 currency code (DE 49) | example: "986" |
| `migration` | object | yes | Applicant additional migration information |  |
| `migration.account_id` | string | yes | ID of the migrated account. Use the `account_id` when migrating an account. When an account has additional cards with different customer names, the customer ID is taken from the card's migration ID. | example: "account-migration-id" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `migration.card_id` | string | yes | ID of the migrated card. The `card_id` must match the `migration.id` from the [Migrate cards](ref:postcardsv1) endpoint. | maxLength: 255; example: "card-migration-id_1234" |
| `migration.id` | string | yes | Record identifier for migrated authorizations.<br>**Note:** Using PCI or any other sensitive data for a migration ID poses serious security risks. This includes <<glossary:document_number>>, PAN, or telephone number. For enhanced security, use a hash for this field ([SHA-256 with salt](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/) is recommended.)<br> | example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.tokenization_id` | string | no | ID of the migrated token on a tokenized purchase. Must match the `migration.id` field returned from the [Migrate tokens](ref:posttokensv1) endpoint. | example: "tokenization-id-2468" |
| `mti` | string | yes | Authorization ISO 8583 MTI (message type indicator):<br>  `0100`—Purchase<br>  `0120`—Purchase advice<br>  `0200`—Debit purchase<br>  `0400`—Cancellation<br>  `0420`—Cancellation advice<br> | enum: ["0100", "0120", "0200", "0400", "0420"]; example: "0100" |
| `network` | string | yes | Card network used in the authorization (such as Visa or Mastercard) | enum: ["VISA", "MASTERCARD", "ELO"]; example: "VISA" |
| `nsu` | string | yes | Card network-assigned Network Settlement Utility (NSU) code for approved payments. Used to track the flow of funds across payment networks such as VisaNet or BankNet.<br> | maxLength: 6; example: "W12345" |
| `pin_presence` | boolean | yes | Is authorization PIN present? | example: false |
| `postings` | object (map of string) | yes | Posting metadata (key-value pairs) that accepts any value. Maximum size is 1000 bytes. | example: {"key1": "value1", "key2": "value2"} |
| `principal_amount` | number | yes | Total authorization amount, not including fees | format: "float"; example: 171.42 |
| `processing_code` | string | yes | Authorization **processing code** (custom alphanumeric identifier that defines how the Pismo platform handles a certain financial operation type).<br><br>Processing codes are integral to the transactions flow on the Pismo platform. The platform uses predefined processing codes to evaluate and process operations. For more information, refer to [Processing codes and transaction types](doc:processing-codes-and-transaction-types).<br><br>**Note:** This processing code may not exactly match the DE03 (subfield 1) message from Visa, Mastercard or any other network.<br>example: "00"<br> |  |
| `retrieval_reference_number` | string | yes | Authorization retrieval reference number received in flag message (DE 37) | example: "664151" |
| `settlement_amount` | number | yes | Settlement currency amount (DE 05, destination amount). Indicates the amount transferred between the acquirer and the issuer equal to DE 04 (amount, transaction) in the settlement currency. Mastercard programs and services use U.S. dollars as the currency of settlement. | format: "float"; example: 171.42 |
| `settlement_currency_code` | string | yes | Authorization settlement currency code | example: "840" |
| `track1_presence` | boolean | yes | Is authorization magnetic stripe Track 1 data present? | example: false |
| `track2_presence` | boolean | yes | Is authorization magnetic stripe Track 2 data present? | example: false |
| `transaction_identifier` | string | yes | Unique transaction ID (refer to DE 63 for Mastercard, DE 62.2 for Visa).<br><br>**Note**: This field is critical for doing network reconciliations post migration. If you are migrating pending authorizations and you don't have this field, contact your Pismo representative for guidance.<br> | example: "de63" |
| `update_limit` | boolean | yes | Should the authorization affect the account's credit limit?<br><br>**Note:** Only set this to `true` in specific scenarios. Before you enable this option, contact your Pismo representative for guidance.<br> | default: false; example: true |
| `cardholder_amount` | number | no | Transaction amount billed to the cardholder in the issuer's currency (DE 06 optional). | format: "float"; example: 172.42 |
| `cardholder_currency_code` | string | no | Cardholder currency code (DE 51, cardholder), in ISO 4217 numeric code format<br> | example: "840" |
| `cardholder_currency_conversion_rate` | number | no | Conversion rate between local amount and cardholder amount (the DE 10 conversion rate that the brand sends) | format: "float"; example: 0.99 |
| `installment_amount` | number | no | Authorization installment amount | format: "float"; example: 171.42 |
| `merchant_city` | string | no | Authorization merchant city (DE 43 city field, maximum 15 characters) | maxLength: 15; example: "São Paulo" |
| `merchant_name` | string | no | Authorization merchant name | maxLength: 500; example: "Merchant XYZ" |
| `merchant_state_or_country` | string | no | Merchant state or country using ISO 3166-1 alpha-2 or alpha-3 country code | maxLength: 3; example: "RS" |
| `merchant_category_code` | string | no | Authorization merchant category code (MCC), a four-digit ISO 18245 number | example: "1011" |
| `merchant_id` | string | no | Authorization merchant ID | example: "xF5E0" |
| `metadata` | object | no | Authorization metadata (key-value pairs) that accepts any values **except PCI data**. Maximum size is 1000 bytes.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"key1": "value1", "key2": "value2"} |
| `number_of_installments` | integer | no | Total number of installments in the current migration authorization | default: 1; example: 2 |
| `pre_authorization` | boolean | no | Is authorization a pre-authorization? On pending authorizations, this affects the time that it takes to cancel the authorization if no confirmation arrives from the network settlement file. | example: false |
| `referral_updated_at` | string | no | Date and time when the referral was last updated. Identifies when a fraud suspicion is no longer valid. Format = YYYY-MM-ddTHH:mm:ss. | format: "date-time"; example: "2021-08-11T11:25:43" |
| `settlement_currency_rate` | string | no | Authorization settlement currency rate | example: "1.50000112" |
| `terminal_capability` | string | no | Is terminal pre-authorized? Field 130 (Visa) and DE 61 (Mastercard) POS (Point Of Sale). **REQUIRED** for chip purchases. | example: "000001100003" |
| `token_requestor_id` | string | no | Authorization token requestor ID | example: "ZAMBAS" |
| `wallet_identifier` | string | no | Authorization wallet identifier | example: "GOOGLE PAY" |
| `ledger_impact` | array of string | no | Limits impacted by the ledger during the authorization.<br><br>**Note:** This is a legacy field. You should use the `ledger_updates` array instead.<br> | deprecated: true |

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
| `migration-authorization-incoming-1` | https://developers.pismo.io/events/docs/migration-authorization-incoming-1 |
| `migration-authorization-outgoing-1` | https://developers.pismo.io/events/docs/migration-authorization-outgoing-1 |

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
| `api-specs/Migrations.yaml` | tag `Authorization migration`: POST /v1/migrations/authorizations | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
