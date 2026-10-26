---
ku_id: KU-API-migrations--card-migration
title: 'API reference: Migrations — Card migration'
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
- PostCardsV1
- PostPciCardsV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
- KU-EVT-migrations-data-events
specification_version: 0.0.7
---

# API reference: Migrations — Card migration

**KU ID:** `KU-API-migrations--card-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Card migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Card migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/cards` | `PostCardsV1` | Migrate cards | no |
| `POST /v1/migrations/cards-pci` | `PostPciCardsV1` | Migrate PCI cards | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/cards operationId=PostCardsV1 -->
### `POST /v1/migrations/cards` — Migrate cards

- **operationId:** `PostCardsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Card migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of non-PCI cards.
>
> This endpoint generates the following events:
>
> - [Card migration started](https://developers.pismo.io/events/docs/migration-card-incoming-1)
>
> - [Card migration completed](https://developers.pismo.io/events/docs/migration-card-outgoing-1)
>
> - For COMBO card migrations (that is, `mode = COMBO` and `combo_account_id = NOT NULL`), a third event is also sent: [Combo card mode migration completed](https://developers.pismo.io/events/docs/migration-card-mode-outgoing-1). This applies to the initial card migration only, but not to updates made before Go-live.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | JSON Web Token (JWT). Tokens expire quickly, which can result in an **Unauthorized** message. For more information on authentication best practices, refer to [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials#initial-authentication).<br> | example: "eyJ...F8E" |

#### Request body

Required: no

> Start migration of non-PCI data for cards.

**Content type `application/json`** — schema: object (schema `CardsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `abu_enabled` | boolean | yes | Include card on Mastercard's Automatic Billing Updater (ABU)? | default: false; example: true |
| `bin` | string | yes | New BIN of card (use with template_id) | example: "12345" |
| `contactless_enabled` | boolean | yes | Is contactless enabled? | default: true; example: true |
| `issuing_date` | string | yes | Issuing date and hour of a card. Format = YYYY-MM-ddTHH:mm:SSZ. | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `migration` | object | yes | Additional migration details |  |
| `migration.id` | string | yes | Record identifier for migration purposes. This is a unique ID that you need to generate.<br>**Note:** Using PCI or any other sensitive personal data for migration ID poses serious security risks. This includes a <<glossary:document_number>>, PAN, or telephone number. For enhanced security, use a hash for this field ([SHA-256 with salt](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/) is recommended).<br> | example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `migration.account_id` | string | no | This value must match `applicant.migration.id` from the [Migrate accounts](ref:postaccountsv1) endpoint. Used to link cards to an account. This unique key is **REQUIRED** for named cards.<br> | example: "migration-external-id" |
| `migration.combo_account_id` | string | no | This field is **REQUIRED** to migrate a **combo card**, which has both credit and debit functions. The value **must match the migration ID of the account previously migrated** (from the `migration` object of the [Migrate accounts](ref:postaccountsv2) endpoint). To migrate a combo card, you first need to migrate both of its associated accounts (credit and debit). For more information, refer to [Create combination card with card modes](doc:cards-overview-1#create-a-combination-card-with-card-modes) and [Migrations overview, Cards](doc:migrations-overview#cards).<br><br>**Note**: Both accounts must be registered to the same <<glossary:document_number>>, which identifies their owner on the Pismo platform.<br><br> For example, if migrating the credit account first, do these steps:<br>  1. Migrate the **credit account**: `document number = 123` and `migration_id = abc`.<br>  1. Migrate the **debit account**: `document number = 123` and `migration_id = def`.<br>  1. Migrate the card:<br>      - For **credit** account: `mode = COMBO`, `migration.accountId = 123abc`, `migration.cardId = XXX`, and  `migration.combo_account_id = 123abcXXX`<br>      - For **debit** account: `mode = COMBO`, `migration.accountId = 123def`, migration.cardId = YYY, and  `migration.combo_account_id = 123defYYY`.<br> | minLength: 1; maxLength: 120; example: "123abcYYY" |
| `migration.customer_id` | string | no | Customer ID that is used when a card is linked to an additional customer on the account, instead of the account owner. Use when migrating an additional card for that customer.<br> |  |
| `migration.reissued_id` | string | no | Card reissued migration ID, enabling the system to track the previous card's migration. You must set this ID to the original migration ID of any card that has been reissued.<br> | example: "A7F5B84429989D089D2" |
| `mode` | string | yes | Card mode | enum: ["CREDIT", "DEBIT", "COMBO"]; example: "CREDIT" |
| `name` | string | yes | Nickname of card. An account can have multiple cards. For example, an account could have one plastic card and three virtual cards. You give them nicknames to identify them: "Plastic card", "Netflix card", and so on. You cannot repeat the same nickname for multiple plastic cards.<br> | minLength: 3; maxLength: 50; example: "Personal" |
| `network` | string | yes | Card network name | enum: ["VISA", "MASTERCARD", "ELO"] |
| `status` | string | yes | Card status. For noname cards, it must be `UNBOUND`. For named cards, it must be an allowed value from the table in [Card status](doc:card-lifecycle-and-statuses). Since cards are already issued, the platform does not take embossing under consideration on migrated cards.<br> | enum: ["UNBOUND", "CREATED", "NORMAL", "REISSUED", "UNNUMBERED", "BLOCKED", "PENDING", "WARNING", "INOPERATIVE", "LOST", "ROBBED", "EXPIRED", "DAMAGED", "FRAUD", "CANCELED", "DELETED", "BROKEN", "THEFT", "DEFECT"]; example: "CREATED" |
| `additional` | boolean | no | Is this an additional card? Use when a card is linked to an additional customer on the account, and you must send the previous migration customer's migration ID. | deprecated: true; example: false |
| `atc` | array of integer | no | Card ATC list ([Application Transaction Counter](doc:application-transaction-counter-atc)). For example, `[21,20,19,18,16,15,14]`. Only send if you have the correct information from the current processor. Sends `null` by default. | example: [100, 101] |
| `cvv_rotation_interval` | number | no | **REQUIRED** for a virtual card. Rotation interval in hours for a virtual card's CVV. You can pass "0" if the virtual card does not have CVV rotation. To force a card's CVV rotation, you can call the [Rotate virtual card CVV](ref:post-v2-reset-cvv) endpoint.<br> | default: 24; minimum: 0; maximum: 4320; example: 48 |
| `expiration_date` | string | no | Expiration date of card. Format = YYYY/MM. | pattern: "^\\\\d{4}/(0[1-9]\|1[0-2])$"; example: "2025/12" |
| `metadata` | object | no | Metadata (free-form fields) formatted as a JSON object using any key-value pairs.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"key1": "value1", "key2": "value2"} |
| `phase_id` | string | no | Migration phase ID. Account migration can be split into phases (batches), where each phase must have a unique phase ID. When assigning a phase ID, use a name that is meaningful, such as `Rollout_Jan2025`. **REQUIRED** for noname cards; optional for nominal cards.<br> | example: "Rollout_Jan2025" |
| `printed_name` | string | no | Applicant name to be printed on a card (2 characters minimum, 26 characters max). Use only letters (a-z\|A-Z) and space, as specified in the ISO EMV tag 5F20 for cardholder name. No letters with accents, numbers, or special characters. | minLength: 2; maxLength: 26; example: "Joao S Silva" |
| `program_id` | integer | no | ID of a program created specifically for noname cards. Used to link noname cards to this type of account.<br><br>**Note:** This field is **REQUIRED** for noname cards but otherwise optional.<br> | format: "int32"; example: 23456 |
| `stage` | string | no | Card stage. **REQUIRED** for named cards. Set to `UNBLOCKED` initially. | enum: ["CREATED", "BLOCKED", "UNBLOCKED"]; example: "UNBLOCKED" |
| `template_id` | string | no | Used in order to override the definitions of the program when creating a card. Only send if the card's brand is different from the account's program brand. | example: "VISA" |
| `transaction_limit` | number | no | Card transaction limit. (Only for virtual cards.) Sends "0" by default. | format: "float"; minimum: 0; example: 12500 |
| `type` | string | no | Card type. It is not possible to change the type after migration, so if you need to change it you must recreate the card to get a new type. | enum: ["PLASTIC", "VIRTUAL"]; example: "PLASTIC" |
| `unlock_date` | string | no | Card unlock date and time. Format = YYYY-MM-ddTHH:mm:ss.SSSSSZ. | format: "date-time"; example: "2022-06-06T20:30:00Z" |

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
| `migration-card-incoming-1` | https://developers.pismo.io/events/docs/migration-card-incoming-1 |
| `migration-card-mode-outgoing-1` | https://developers.pismo.io/events/docs/migration-card-mode-outgoing-1 |
| `migration-card-outgoing-1` | https://developers.pismo.io/events/docs/migration-card-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-EVT-migrations-data-events`.

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/cards-pci operationId=PostPciCardsV1 -->
### `POST /v1/migrations/cards-pci` — Migrate PCI cards

- **operationId:** `PostPciCardsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Card migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migrations of PCI cards.
>
> This endpoint generates the [PCI card migration completed](https://developers.pismo.io/events/docs/migration-pci-card-outgoing-1) event. The result is either `SUCCESS` or `FAIL`.
>
> **Note:** This is a PCI endpoint. Use the <a href="https://gw-pci.pismolabs.io">https://gw-pci.pismolabs.io</a> environment.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | JSON Web Token (JWT). Tokens expire quickly, which can result in an **Unauthorized** message. For more information on authentication best practices, refer to [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials#initial-authentication).<br> | example: "eyJ...F8E" |

#### Request body

Required: no

> Start migration of PCI cards

**Content type `application/json`** — schema: object (schema `PciCardsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | no | Applicant additional migration information |  |
| `migration.id` | string | yes | Card migration ID; the same ID used in the `migration.id` field in [Migrate cards](ref:postcardsv1). You use this ID to link card information with its PCI data. | example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `pan` | string | no | Card's PAN (Primary Account Number). If provided, takes precedence over encrypted PAN fields. Either `pan` or the encrypted PAN fields (`key_id`, `encrypted_pan`, `iv`) are **REQUIRED**.<br><br>**Note:** The PAN shown here is a fictional example used for documentation purposes. It does not represent a real card number.<br> | example: "123456******7890" |
| `pin_block` | string | no | Card's PIN block password. Must conform to ISO-9564 Format 0 and be encrypted using Zone PIN Key (ZPK). If you do not provide a value in this field, Pismo generates a random password for you.<br> | deprecated: true; example: "670D35C104A6E41F" |
| `encrypted_pin` | string | no | Card's PIN block password with two available formats. The first format conforms to ISO-9564 Format 0 and must be encrypted using Zone PIN Key (ZPK). The second format is a PIN offset.<br> |  |
| `password_tries` | string | no | Cardholder password failure attempts, from 0 to 3. | example: "0" |
| `password_updated` | string | no | Is the PIN block password changed? Defaults to changed.<br>`0`—Not changed<br>`1`—Changed<br> | enum: ["0", "1"]; default: "1"; example: "1" |
| `pin_type` | string | yes | Format used for the password. Can be either `PINOFFSET_IBM3624` or `PINBLOCK_FORMAT_0`. When using `PINOFFSET_IBM3624`, you must use PIN Verification Key (PVK) exchange. For `PINBLOCK_FORMAT_0`, use Zone PIN Key (ZPK) exchange.<br> | enum: ["PINOFFSET_IBM3624", "PINBLOCK_FORMAT_0"]; default: "PINBLOCK_FORMAT_0" |
| `pin_validation_data` | string | no | **REQUIRED** if `pin_type` = `PINOFFSET_IBM3624`. Format = 11-digit primary account number (PAN) + letter N.<br> | example: "59999900017N" |
| `service_code` | string | yes | Card service code for Card Verification Value 2 (CVV2). If your virtual card has a different service code, contact your Pismo representative.<br> | example: "000" |
| `key_id` | string | no | Key ID identifying the AES symmetric key registered with Pismo for PAN decryption. **REQUIRED** when `pan` is not provided. Must be provided together with `encrypted_pan` and `iv`.<br> | example: "pan-key-001" |
| `encrypted_pan` | string | no | Base64-encoded encrypted PAN data using AES/GCM/NoPadding algorithm. **REQUIRED** when `pan` is not provided. Must be provided together with `key_id` and `iv`.<br> | example: "dGVzdC1lbmNyeXB0ZWQtcGFuLWRhdGE=" |
| `iv` | string | no | Base64-encoded initialization vector (16 bytes) for AES/GCM decryption. **REQUIRED** when `pan` is not provided. Must be provided together with `key_id` and `encrypted_pan`.<br> | example: "YWJjZGVmZ2hpamtsbW5vcA==" |

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
| `migration-pci-card-outgoing-1` | https://developers.pismo.io/events/docs/migration-pci-card-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `1`, deprecated `False`.

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
| `api-specs/Migrations.yaml` | tag `Card migration`: POST /v1/migrations/cards, POST /v1/migrations/cards-pci | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
- `KU-EVT-migrations-data-events` — Migrations events
