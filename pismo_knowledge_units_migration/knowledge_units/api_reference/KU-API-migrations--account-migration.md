---
ku_id: KU-API-migrations--account-migration
title: 'API reference: Migrations — Account migration'
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
- PostAccountsV2
- PostGoLiveV1
- PostPreGoLiveV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
- KU-GS-get-started-with-pismo-apis
specification_version: 0.0.7
---

# API reference: Migrations — Account migration

**KU ID:** `KU-API-migrations--account-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Account migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Account migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/migrations/accounts` | `PostAccountsV2` | Migrate accounts | no |
| `POST /v1/migrations/go-live` | `PostGoLiveV1` | Migrate accounts Go-live | no |
| `POST /v1/migrations/pre-go-live` | `PostPreGoLiveV1` | Migrate accounts pre go-live | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v2/migrations/accounts operationId=PostAccountsV2 -->
### `POST /v2/migrations/accounts` — Migrate accounts

- **operationId:** `PostAccountsV2`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Account migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start accounts migration (v2).
>
> **Note:** This endpoint replaces the Migrate accounts (v1) endpoint.
>
>
> This endpoint generates the following events:
> - [Account migration started](https://developers.pismo.io/events/docs/migration-account-incoming-2)
>
> - [Account migration completed ](https://developers.pismo.io/events/docs/migration-account-outgoing-2)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | JSON Web Token (JWT). Tokens expire quickly, which can result in an **Unauthorized** message. For more information on authentication best practices, refer to [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials#initial-authentication).<br> | example: "eyJ...F8E" |

#### Request body

Required: no

> Start migration of accounts (v2).

**Content type `application/json`** — schema: object (schema `AccountsV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `applicant` | object | yes | Applicant details. At least one of the following objects are **REQUIRED**: `personal` (for personal accounts) or `company` (for business accounts). Pass one or the other but not both.<br> |  |
| `applicant.document_number` | string | yes | Document number | maxLength: 60; example: "111111111" |
| `applicant.migration` | object (schema `AccountsV2Migration`) | yes | Extra information for migration |  |
| `applicant.birth_date` | string | no | Applicant date of birth. Required for personal accounts. For a company, this could be the company incorporation date. Format = YYYY-MM-DD. | format: "date"; example: "1975-01-15" |
| `applicant.personal` | object (schema `AccountsV2Personal`) | no | Applicant personal information. Either this or the `company` object is **REQUIRED**. Pass one or the other but not both. |  |
| `applicant.addresses` | array of object (schema `AccountsV2Address`) | no | Applicant addresses |  |
| `applicant.phones` | array of object (schema `AccountsV2Phone`) | no | Applicant telephone |  |
| `applicant.company` | object (schema `AccountsV2Company`) | no | Applicant company information (for business accounts). Either this or the `personal` object is **REQUIRED**. Pass one or the other but not both. |  |
| `applicant.account` | object (schema `AccountsV2Account`) | no | Applicant account information, for either a personal account or a company account |  |
| `applicant.metadata` | object | no | Account metadata<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key1": "value1", "key2": "value2"} |
| `applicant.corporate_account` | object (schema `AccountsV2Corporate`) | no | Corporate account details. |  |
| `due_date_id` | integer | no | Account due date ID. **REQUIRED** for credit accounts. Uses a value returned from the [Get program due dates](ref:getprogramduedates) endpoint. | format: "int32"; example: 101010 |
| `program_id` | integer | no | Account's program ID. Must be a program ID previously configured on the Pismo platform. | format: "int32"; example: 1234 |

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
| `migration-account-incoming-2` | https://developers.pismo.io/events/docs/migration-account-incoming-2 |
| `migration-account-outgoing-2` | https://developers.pismo.io/events/docs/migration-account-outgoing-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-GS-get-started-with-pismo-apis`.

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/go-live operationId=PostGoLiveV1 -->
### `POST /v1/migrations/go-live` — Migrate accounts Go-live

- **operationId:** `PostGoLiveV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Account migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> **Go-live** is a process that happens at the end of a migration. After migrating accounts, you must call the Go-live endpoint to mark all migrated accounts active. The Pismo platform responds by changing the migration status of each account to `MIGRATED`.
>
> This endpoint generates an [Account go-live completed](https://developers.pismo.io/events/docs/migration-account-go-live-outgoing-1) event. Each unique go-live request generates _N_ events (one for each account that has the specified migration phase ID) with a different x-cid from the initial request.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | JSON Web Token (JWT). Tokens expire quickly, which can result in an **Unauthorized** message. For more information on authentication best practices, refer to [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials#initial-authentication).<br> | example: "eyJ...F8E" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `PostGoLiveV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Applicant additional migration information |  |
| `migration.phase_id` | string | yes | Migration phase ID, which represents a batch of an account migration. Account migration can be split into smaller batches where each batch must have a unique phase ID. When assigning a phase ID, you must a value that is meaningful; for example: `Rollout_Jan2025`.<br><br>**Important:** Calling the [Migrate accounts Go-live](ref:postgolivev1) endpoint migrates every account that has this phase ID. For each successfully migrated account, the operation changes its status to `MIGRATED`.<br> | maxLength: 60; example: "Rollout_Jan2025" |
| `migration.status` | string | no | Account migration status. When present, go-live only proceeds for accounts with this status, so it must match the status of the previous account migration. Typically set to either `TO_MIGRATE` or `MIGRATING`. | enum: ["TO_MIGRATE", "MIGRATING", "NOT_MIGRATE"]; example: "TO_MIGRATE" |
| `type` | string | yes | Accounts go-live domain type. For more information, refer to the [Migrations overview](doc:migrations-overview#go-live-and-pre-go-live) guide. Note that `PCI_CARD` type is deprecated.<br> | enum: ["ACCOUNT", "PRE_GO_LIVE"]; example: "ACCOUNT" |

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
| `migration-account-go-live-outgoing-1` | https://developers.pismo.io/events/docs/migration-account-go-live-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/pre-go-live operationId=PostPreGoLiveV1 -->
### `POST /v1/migrations/pre-go-live` — Migrate accounts pre go-live

- **operationId:** `PostPreGoLiveV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Account migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Pre Go-live enables you to preview the results of the Go-live process without actually implementing them. It performs a series of actions for every account assigned to a specific phase ID. For more information, refer to the [Migrations overview](doc:migrations-overview) guide.
>
> **Note:** Pre Go-live is **REQUIRED** for migrating credit accounts but optional for other account types.
>
> This endpoint generates the following events (one for every migrated account):
> - [Pre Go-live migration completed](https://developers.pismo.io/events/docs/migration-account-pre-go-live-outgoing-1) &#8211; when the Pre Go-live process finishes and the result is reported (SUCCESS or FAIL).
>
> - [Pre-Go-live migration error](https://developers.pismo.io/events/docs/migration-pre-go-live-outgoing-1) &#8211; when the Pre Go-live process runs but errors occur before dispatching the SUCCESS/FAIL event for each migrated account.
>
> - [Statement organized completed](https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1) &#8211; emitted when the organize-statement process runs, indicating whether the account's statements were organized successfully or the processing failed. Emission is opt-in.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `PostPreGoLiveV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Migration data that specifies which accounts should undergo Pre Go-live |  |
| `migration.phase_id` | string | yes | Migration phase ID. The pre go-live process is triggered for every account with the specified phase ID.<br> | maxLength: 60; example: "Feb2025_Phase_3_of_4" |
| `go_live_date` | string | yes | Expected Go-live date for the accounts undergoing Pre Go-live. The Pre Go-live process uses this value to determine which statements to use during account balance validations.<br> | format: "date" |

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
| `migration-account-pre-go-live-outgoing-1` | https://developers.pismo.io/events/docs/migration-account-pre-go-live-outgoing-1 |
| `migration-organize-statement-outgoing-1` | https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1 |
| `migration-pre-go-live-outgoing-1` | https://developers.pismo.io/events/docs/migration-pre-go-live-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `3`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountsV2Migration -->
### Schema `AccountsV2Migration`

Pointer: `#/components/schemas/AccountsV2Migration`. Type: object (schema `AccountsV2Migration`).

> Extra information for migration

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | yes | Record ID for migration purposes | example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `account_status` | string | no | Current account status. For more information on standard account statuses, refer to [Account status](doc:accounts-overview#account-status). Set your system values using the [Create status](ref:v4-post-account-status) endpoint. Migrating accounts typically have `STAND-BY` as their status during migration. Examples are `BLOCKED`, `CANCELLED`, `NORMAL`, `OVERDUE`, or `STAND-BY`.<br> | default: "STAND-BY"; example: "STAND-BY" |
| `creation_date` | string | no | Date that the entry was created on the original system. Format = YYYY-MM-DD or YYYY-MM-DDTHH:MM:SSZ. | format: "datetime"; example: "2024-09-13T12:55:42Z" |
| `go_live_account_status` | string | no | Account status after go-live. Current account status on the original system. For more information, refer to [Account status](doc:accounts-overview#account-status). Set your system values using the [Create status](ref:v4-post-account-status) endpoint. Migrating accounts typically have `STAND-BY` as their status during migration. Examples are `BLOCKED`, `CANCELLED`, `NORMAL`, `OVERDUE`, or `STAND-BY`. | default: "NORMAL"; example: "NORMAL" |
| `open_due_date` | string | no | The Pismo platform uses the earliest unpaid statement to start calculating accrued interest for an overdue account. This date is used as a reference date for accrued interest calculations after the account goes live. If a migrated payment or credit transaction is identified before `PRE_GO_LIVE` and the account is no longer considered overdue, the Pismo platform automatically removes the `open_due_date`. **REQUIRED** for overdue accounts. Format: YYYY-MM-DD<br>**Note**: The `open_due_date` must be equal to the due date of the earliest unpaid statement that created the delinquency. Do *not* provide the date following the statement due date. For credit accounts only.<br><br>For example:<br>- Statement due date: **2026-05-08**<br>- Cardholder does not pay the minimum amount due by that date.<br>- Account becomes overdue.<br>- `open_due_date` = **2026-05-08**<br> | format: "date"; example: "2026-05-08" |
| `phase_id` | string | no | Used to group accounts under the same ID. Used during account go-live, account rollback, and PCI go-live. | maxLength: 60; example: "Rollout_Jan2025" |
| `status` | string | yes | Migration status. The platform does not consider embossing on migrated cards since they are already issued. | enum: ["TO_MIGRATE", "MIGRATING"]; example: "TO_MIGRATE" |

<!-- schema: #/components/schemas/AccountsV2Personal -->
### Schema `AccountsV2Personal`

Pointer: `#/components/schemas/AccountsV2Personal`. Type: object (schema `AccountsV2Personal`).

> Applicant personal information. Either this or the `company` object is **REQUIRED**. Pass one or the other but not both.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string | no | Record ID from an external system | maxLength: 60; example: "3829df2a-e7e2-11eb-aafd-1bb0c073f513" |
| `name` | string | yes | Applicant name | maxLength: 60; example: "João Silva" |
| `email` | string | no | Applicant email | maxLength: 60; example: "joao.silva@pismo.com" |
| `gender` | string | no | Applicant gender | enum: ["M", "F"]; example: "M" |
| `printed_name` | string | no | Applicant name to be printed on a card (2 characters minimum, 25 characters max). Use only letters (a-z\|A-Z) and space, as specified in the ISO EMV tag 5F20 for cardholder name. No letters with accents, numbers, or special characters. | maxLength: 25; example: "Joao Silva" |
| `nickname` | string | no | Applicant nickname | maxLength: 60; example: "João" |
| `social_name` | string | no | Applicant social name | maxLength: 60; example: "João" |
| `country_of_birth` | string | no | Applicant country of birth | maxLength: 60; example: "Brazil" |
| `state_of_birth` | string | no | Applicant state of birth | maxLength: 60; example: "SP" |
| `city_of_birth` | string | no | Applicant city of birth | maxLength: 60; example: "Osasco" |
| `registration` | object | no | Applicant document details |  |
| `registration.number` | string | no | Document's number | maxLength: 30; example: "111111111" |
| `registration.issuer` | string | no | Document's issuer | maxLength: 30; example: "Any" |
| `registration.issuing_state` | string | no | Document's issuing state, using the ISO 3166-2 (2 letter) standard for states and country sub-divisions | maxLength: 2; example: "SP" |
| `registration.issuing_date` | string | no | Document's issue date | format: "date"; example: "2021-07-01" |
| `education_degree` | string | no | Applicant highest education degree | maxLength: 60; example: "Bachelor's Degree" |
| `marital_status` | string | no | Applicant marital status | enum: ["SINGLE", "MARRIED", "DIVORCED", "WIDOWER"]; example: "SINGLE" |
| `fathers_name` | string | no | Applicant father's name | maxLength: 60; example: "Carlos" |
| `mothers_name` | string | no | Applicant mother's name | maxLength: 60; example: "Fátima" |
| `nationality` | string | no | Applicant nationality | maxLength: 60; example: "Brazilian" |
| `other_id_number` | string | no | Additional document number | example: "14564543-32" |
| `document_type` | string | no | Document type for the document associated with `other_id_number` | maxLength: 60; example: "CNPJ - Brazilian tax number" |
| `document_issued_by` | string | no | Issuer for the document associated with `other_id_number` | example: "SSP" |
| `document_issued_at` | string | no | Document issuer location for the document associated with `other_id_number`. Typically a state using the ISO 3166-2 (2 letter) standard for states and country sub-divisions but any string is accepted. | maxLength: 30; example: "CA" |
| `document_issued_date` | string | no | Issued date for the document associated with `other_id_number`. Format = YYYY-MM-DD. | format: "date"; example: "2004-07-05" |
| `occupation` | string | no | Applicant profession | maxLength: 60; example: "Engineer" |
| `assets` | number | no | Applicant assets | format: "float"; minimum: 0; example: 125000 |
| `income` | number | no | Applicant income | format: "float"; minimum: 0; example: 5000 |
| `net_worth` | number | no | Applicant net worth | format: "float"; minimum: 0; example: 200000 |
| `statutory` | boolean | no | Applicant works for a government entity? | example: true |

<!-- schema: #/components/schemas/AccountsV2Address -->
### Schema `AccountsV2Address`

Pointer: `#/components/schemas/AccountsV2Address`. Type: object (schema `AccountsV2Address`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `zip_code` | string | no | Address zip (postal) code | minLength: 1; maxLength: 9; example: "90210" |
| `address` | string | no | Address street | minLength: 1; maxLength: 80; example: "Avenida das Neves" |
| `number` | integer | no | Address number | minLength: 1; maxLength: 10; example: 100 |
| `neighborhood` | string | no | Address neighborhood | minLength: 1; maxLength: 50; example: "Vila Nova" |
| `complementary_address` | string | no | Address complement | minLength: 1; maxLength: 50; example: "Apartamento 500" |
| `city` | string | no | Address city | minLength: 1; maxLength: 60; example: "São Paulo" |
| `state` | string | no | Address state | minLength: 2; maxLength: 2; example: "SP" |
| `country` | string | no | Address country | example: "Brazil" |
| `address_type` | string | no | Address type. Valid values (`RESIDENTIAL`, `COMMERCIAL`, `OTHER`) | enum: ["RESIDENTIAL", "COMMERCIAL", "OTHER"]; example: "RESIDENTIAL" |
| `mailing_address` | boolean | no | Mark as a mailing address? | example: true |
| `date` | string | no | Date since the applicant has resided at this address. Format = YYYY-MM-DD. | format: "date"; example: "2013-05-15" |

<!-- schema: #/components/schemas/AccountsV2Phone -->
### Schema `AccountsV2Phone`

Pointer: `#/components/schemas/AccountsV2Phone`. Type: object (schema `AccountsV2Phone`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `phone_type` | string | no | Telephone type | enum: ["RESIDENTIAL", "COMMERCIAL", "MOBILE"]; example: "RESIDENTIAL" |
| `phone` | string | no | Telephone number | maxLength: 12; example: "91234-5678" |
| `country_code` | string | no | Telephone country code | maxLength: 3; example: "11" |
| `area_code` | string | no | Telephone area code | maxLength: 5; example: "031" |

<!-- schema: #/components/schemas/AccountsV2Company -->
### Schema `AccountsV2Company`

Pointer: `#/components/schemas/AccountsV2Company`. Type: object (schema `AccountsV2Company`).

> Applicant company information (for business accounts). Either this or the `personal` object is **REQUIRED**. Pass one or the other but not both.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string | no | Exterrnal ID | maxLength: 60; example: "312312" |
| `name` | string | no | Company legal name | maxLength: 60; example: "Pismo LTDA" |
| `email` | string | no | Company email address | maxLength: 60; example: "cadastro@pismo.io" |
| `registration_number` | string | no | ID under which the company is registered | maxLength: 30; example: "123456789" |
| `registration_issuer` | string | no | Document issuer | maxLength: 30; example: "123456789" |
| `company_name` | string | no | Company brand name | maxLength: 60; example: "Pismo" |
| `activity` | string | no | Company field of industry | maxLength: 30; example: "Software development" |
| `company_type` | string | no | Company type | maxLength: 60; example: "Ltda" |
| `company_format` | string | no | Company social type | maxLength: 60; example: "Ltda" |
| `company_constitution_date` | string | no | Company incorporation date. Format = YYYY-MM-DD. | format: "date"; example: "2017-11-21" |
| `occupation` | string | no | Company main occupation | maxLength: 60; example: "Engineering" |
| `annual_revenues` | number | no | Company average monthly revenue for the last 12 months | format: "float"; example: 20000000 |
| `type` | string | no | Company business relations type | maxLength: 60; example: "Customer service" |
| `number_of_partners` | integer | no | Number of partners in company | maximum: 999999; example: 2 |
| `fiscal_situation` | string | no | Company fiscal situation | maxLength: 60; example: "Normal" |
| `debt` | number | no | Company debt | format: "float"; example: 500000 |
| `income` | number | no | Company income | format: "float"; minimum: 0; example: 3000000 |
| `net_worth` | number | no | Company net worth | format: "float"; minimum: 0; example: 20000000 |

<!-- schema: #/components/schemas/AccountsV2Account -->
### Schema `AccountsV2Account`

Pointer: `#/components/schemas/AccountsV2Account`. Type: object (schema `AccountsV2Account`).

> Applicant account information, for either a personal account or a company account

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_id` | string | no | A record identifier for external purposes | maxLength: 60; example: "980f2c12-e899-11eb-8639-c37913a46510" |
| `total_credit_limit` | number | no | A user-defined account limit, between 0 and the granted limit | format: "float"; example: 3500 |
| `max_credit_limit` | number | no | Maximum credit limit determined by the issuer, typically by using a credit analysis | format: "float"; example: 5000 |
| `percentage_over_limit` | number | no | For credit accounts (program type `CREDIT`), percentage of the maximum spending limit (`granted_limit`) over the credit limit set on the account | format: "float"; maximum: 100; example: 5.5 |
| `total_overdraft_limit` | number | no | Account balance that goes over the credit limit. This field determines to what extent the account balance limit can go negative for debit account | format: "float"; example: 500 |
| `available_credit_limit` | number | no | Amount available to the applicant's credit or debit account. Despite the name `available_credit_limit`, this field is also used for debit accounts, to represent the available balance. | format: "float"; example: 20000 |
| `exchange_mode` | string | no | Should foreign transaction be charged on the day it occured (`SAME_DAY`) or on the statement's closing date (`CLOSING`)? | enum: ["SAME_DAY", "CLOSING"]; example: "SAME_DAY" |
| `is_overlimit` | boolean | no | Has account exceeded the limit at least once during the current cycle? **Note**: Include this field only when overlimit information exists for migrated accounts.<br> | example: false |
| `parent_account_id` | integer | no | ID of parent account | example: 20 |
| `total_installment_credit_limit` | number | no | Total amount for a separate credit limit, such as for a client-specific credit line | format: "float"; example: 1000 |
| `available_total_installment_credit` | number | no | Available amount for the separate credit limit, whose total is defined by `total_installment_credit_limit` | format: "float"; example: 999 |
| `available_withdrawal_credit` | number | no | Amount available for withdrawal | format: "float"; example: 22 |

<!-- schema: #/components/schemas/AccountsV2Corporate -->
### Schema `AccountsV2Corporate`

Pointer: `#/components/schemas/AccountsV2Corporate`. Type: object (schema `AccountsV2Corporate`).

> Corporate account details.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_creation_datetime` | string | yes | Date-time the account was created (in UTC). The date-time format follows the ISO 8601 standard. Format = `yyyy-MM-ddTHH:mm:ss.sssZ`. <br> | format: "date-time"; example: "2025-02-01T22:07:58.000Z" |
| `currency_code` | string | yes | ISO 4217 currency code that identifies the currency used by the corporate account. Pass either the 3-character alphabetic code (for example, `USD`, `EUR`, `BRL`) or the 3-digit numeric code defined by ISO 4217 (for example, `840`, `978`, or `986`), depending on the data provided by the source system. `currency_code` is **REQUIRED** if the corporate account object is passed.<br> | maxLength: 3; example: "986" |
| `division_code` | string | yes | Code used to identify the division within your organization. `division_code` is **REQUIRED** if the corporate account object is present.<br> | maxLength: 36; example: "United States" |
| `inactive_since` | string | no | If the account is in a dormant division/program, this field is **REQUIRED**. | format: "date-time"; example: "2023-08-04T15:00:44.704Z" |
| `account_status_update_date` | string | no | Date-time the account was updated to its current status. **REQUIRED** in case of status change. If the `account_status_update_date` is not passed, the account creation date is returned.<br> | format: "date-time"; example: "2025-06-09T13:45:01Z" |
| `account_status_reason_ext_id` | string | no | External reason ID specifying account restrictions | enum: ["DEBIT_ONLY", "CREDIT_ONLY", "ALL", "NONE", "CREDIT ONLY - NO FORCE DEBIT ALLOWED", "DEBIT ONLY - NO FORCE CREDIT ALLOWED", "ANY - NO FORCE ALLOWED", "MANUAL - NO FORCE ALLOWED", "FORCE CREDIT ONLY - NO FORCE DEBIT ALLOWED", "FORCE DEBIT ONLY - NO FORCE CREDIT ALLOWED"]; example: "DEBIT_ONLY" |
| `bank_statements` | array of object (schema `BankStatements`) | no | Applicant bank statements |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Message describing the error | example: "Internal error" |
| `code` | string | no | Payload validation error | example: "MIGR00001" |

<!-- schema: #/components/schemas/BankStatements -->
### Schema `BankStatements`

Pointer: `#/components/schemas/BankStatements`. Type: object (schema `BankStatements`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `available_balance` | number | no | Balance used for validating transactions. Equal to the account balance and the credit limit. | format: "float"; maximum: 10000000000; example: 50.55 |
| `book_balance` | number | no | Total amount of all cleared funds. Also known as the consolidated balance. | format: "float"; maximum: 10000000000 |
| `business_date` | string | no | Account balance business date (YYYY-MM-DD). Date of the last balance information. | format: "date"; example: "2023-06-22" |
| `credit_balance` | number | no | Aggregate of the remaining balance from the credit transactions that are posted to the account. | format: "float"; maximum: 10000000000; example: 0 |
| `cycle_closing_time` | string | no | Date the cycle closes for a division. This field follows the timezone configured in division. You can find the division timezone using the [Get division by code](https://developers.pismo.io/pismo-docs/reference/get-division-by-code-v2) endpoint. | format: "date-time"; example: "2025-09-10T19:59:59.999Z" |
| `debit_balance` | number | no | Total balance of debit transactions recorded for the account. | format: "float"; maximum: 10000000000; example: 0 |
| `earmarked_balance` | number | no | An amount that is set aside for future use, but has not been debited from the account. When the earmark is created, the available balance decreases and the earmarked balance increases, however, the book balance stays the same. No debit. When the earmark is executed, the earmarked balance decreases and the available balance is unaffected, however, the book balance decreases. This is the actual debit. | format: "float"; maximum: 10000000000; example: 0 |
| `future_dated_credits_balance` | number | no | Balance that is scheduled to settle on a future date after the posting date. Balance increases when future-dated credits post, and decreases when those payments are either settled or cancelled. | format: "float"; maximum: 10000000000; example: 40 |
| `future_dated_debits_balance` | number | no | Balance that is scheduled to settle on a future date after the initial posting date. The account's book balance is debited when settlement occurs. Balance increases when future-dated debits post, and decreases when those payments are either settled or cancelled. | format: "float"; maximum: 10000000000; example: 0 |
| `ledger_balance` | number | no | The net result of all fund movements, both cleared and uncleared. | format: "float"; maximum: 10000000000; example: 110 |
| `overdraft_limit` | number | no | When the account balance is insufficient, the overdraft limit is used and the available balance decreases. | format: "float"; maximum: 10000000000; example: 40 |
| `restricted_funds` | number | no | Portion of the account balance blocked by regulatory or operational restrictions, such as judicial orders, FDIC receivership, or unavailable transactions. | format: "float"; maximum: 10000000000 |
| `uncleared_checks_balance` | number | no | The total value of checks that have posted to the account, but have not yet cleared. | format: "float"; maximum: 10000000000 |
| `uncleared_funds` | number | no | Balance under consideration for future clearing. Uncleared funds have a settlement date, which is the date the funds are expected to be confirmed. | format: "float"; maximum: 10000000000; example: 40 |
| `value_dated_balance` | number | no | Used to calculate interest accumulation. | format: "float"; maximum: 10000000000; example: 0 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Migrations.yaml` | tag `Account migration`: POST /v2/migrations/accounts, POST /v1/migrations/go-live, POST /v1/migrations/pre-go-live | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
