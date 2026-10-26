---
ku_id: KU-API-migrations--transaction-migration
title: 'API reference: Migrations — Transaction migration'
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
- PostTransactionsV1
related_kus:
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-migration
- KU-EVT-migrations-data-events
specification_version: 0.0.7
---

# API reference: Migrations — Transaction migration

**KU ID:** `KU-API-migrations--transaction-migration` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Transaction migration` in `api-specs/Migrations.yaml` (“Migrations”, version `0.0.7`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Transaction migration

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/migrations/transactions` | `PostTransactionsV1` | Migrate transactions | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Migrations.yaml method=POST path=/v1/migrations/transactions operationId=PostTransactionsV1 -->
### `POST /v1/migrations/transactions` — Migrate transactions

- **operationId:** `PostTransactionsV1`
- **Specification:** `api-specs/Migrations.yaml` (Migrations)
- **Server base URL(s):** `https://gw-pci.pismolabs.io/migrations`, `https://sandbox.pismolabs.io/migrations`
- **Tags:** `Transaction migration`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Start migration of transactions.
>
> This endpoint generates the following events:
> - [Transaction migration started](https://developers.pismo.io/events/docs/migration-transaction-incoming-1)
> - [Transaction migration completed](https://developers.pismo.io/events/docs/migration-transaction-outgoing-1)
> - [Payment agreements migration completed](https://developers.pismo.io/events/docs/migration-payment-agreements-outgoing-1) (generated when the migration has the `payment_agreement` field set to `true`)
> - [Instant payment transaction migration completed](https://developers.pismo.io/events/docs/migration-instant-payment-outgoing-1) (generated when migration.type is `INSTANT_PAYMENT`)
> - [Statement organized completed](https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1) — emitted when migrating to-be-billed or installment transactions and the organize-statement process runs, indicating whether the account's statements were organized successfully or the processing failed. Emission is opt-in.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | JSON Web Token (JWT). Tokens expire quickly, which can result in an **Unauthorized** message. For more information on authentication best practices, refer to [Basic authentication with client credentials](https://developers.pismo.io/pismo-docs/docs/basic-authentication-with-client-credentials#initial-authentication).<br> | example: "eyJ...F8E" |

#### Request body

Required: no

> Start migration of transactions

**Content type `application/json`** — schema: object (schema `PostTransactionsV1Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `migration` | object | yes | Applicant additional migration information |  |
| `migration.account_id` | string | yes | Account ID. This matches the applicant migration ID value from the [Migrate accounts](ref:postaccountsv1) endpoint. This field links transactions to an account. | example: "account-migration-id" |
| `migration.authorization_id` | string | yes | Record identifier for migrating transaction authorizations. All transactions from the same contract must have the same `authorization_id`. If an authorization ID does not exist when you migrate a transaction record, Pismo creates one for you.<br><br><br>A contract comprises all transactions (or installments) in a purchase. When you migrate a transaction record, make sure that all transactions in a contract have the same `authorization_id`.<br> | example: "40e95789-e29f-4dea-a085-4468a19ad3cd" |
| `migration.id` | string | yes | Record identifier for migration purposes. This is a unique ID that you must generate. | example: "5a8ade4e-e89a-11eb-9dd1-4b56d86f7a21" |
| `migration.version_date` | string (schema `VersionDate`) | yes | Date-time when the record was created or last updated. Format = `yyyy-MM-ddTHH:mm:ss[.SSS][.SS][.S]Z`. Used together with the migration ID to ensure idempotency when updating data.<br><br>When the Pismo platform receives a request with an existing migration ID, it rejects the request **unless** the `version_date` is later than the existing record's `version_date`.<br> | format: "date-time"; example: "2021-09-13T19:54:41Z" |
| `migration.statement_id` | string | no | ID for statement migration. Required for `BILLED` transactions that are being migrated on `CREDIT` accounts. The `program_id` attribute defines the account type. Do not use a `statement_id` for `BILLED` transactions on `DEBIT` accounts. Do not use a `statement_id` for transactions with `TO_BE_BILLED`, `INSTALLMENTS`, or `STORED` type transactions since the Pismo platform adds them to the corresponding current or future statement automatically. | example: "statement-migration-id" |
| `migration.card_id` | string | no | Unique key for card—the same used in card migration. **REQUIRED** for `NETWORK` `authorization_type`. | example: "card-migration-id" |
| `migration.type` | string | no | An extension of `transaction_type` that affects the migration and authorization flows. `INSTANT_PAYMENT` indicates the transaction is an instant payment. This type requires an `instant_payment_data` object with details of the transaction.<br><br>When the migration type is `INSTANT_PAYMENT`, the `authorization_type` must be `BANKING`. Otherwise, the `authorization_type` should be `PLATFORM`, `ON_US`, or `NETWORK`.<br> | enum: ["INSTANT_PAYMENT"]; example: "INSTANT_PAYMENT" |
| `soft_descriptor` | string | yes | Identifies the transaction. For an installment purchase, this usually is the **merchant name**, the **city/state**, and the **installment number**. For example, the value `Wellmart NYC 2/4` indicates the merchant is `Wellmart`, the transaction was made in `New York City`, and it is installment `2` of `4`.<br> | maxLength: 100; example: "Wellmart NYC 2/4" |
| `type` | string | yes | Transaction types:<br>- `BILLED`—The customer has already been billed for the transaction. Debit accounts and banking transactions typically use this type.<br>- `TO_BE_BILLED`—The transaction has not been billed according to the platform records. That transaction will be added to the "opened statement" of the account.<br>- `INSTALLMENTS`—Represents an entire installment contract with pending future installments, including information for each individual (past or future) installment. For contracts fully in the past, it is sufficient to migrate past individual installments as `BILLED` or `TO_BE_BILLED` transactions, and the `INSTALLMENTS` type is not necessary.<br>- `STORED`—The transaction gets allocated to a future statement.<br> | enum: ["BILLED", "TO_BE_BILLED", "ADJUSTMENT", "INSTALLMENTS", "STORED"]; example: "BILLED" |
| `authorization_type` | string | no | Type of authorized transaction you want to migrate to Pismo:<br>- `NETWORK`—Network-authorized transaction, such as VISA or Mastercard<br>- `PLATFORM`—Bank-authorized transaction, such as fines, fees, or adjustments<br>- `ON_US`—Merchant-authorized transaction, such as private label cards used in the marketplace<br>- `BANKING`—Instant-payment transaction, such as the Pix system in Brazil<br><br>**Note:** This parameter is **REQUIRED** for the following transaction types:<br>- `BILLED`<br>- `TO_BE_BILLED`<br>- `INSTALLMENTS`<br>- `STORED`<br> | enum: ["NETWORK", "PLATFORM", "ON_US", "BANKING"]; example: "NETWORK" |
| `processing_code` | string | no | Pismo processing code. Requires previous configuration in Pismo Control Center. | example: "00" |
| `processing_descriptor` | string | no | Pismo processing descriptor. Requires previous configuration in Pismo Control Center. | example: "purchase" |
| `transaction_type` | object | no | Pismo transaction type ID. Requires previous configuration in Pismo Control Center. |  |
| `transaction_type.id` | integer | no | Pismo identifier (case available) | example: 314 |
| `network` | string | no | Card network name. Required for `NETWORK` authorization type. | enum: ["MASTER", "VISA", "ELO"]; example: "VISA" |
| `network_transaction_identifier` | string | no | Card-network-provided original transaction ID (DE 63 for Mastercard, DE 62.2 for Visa). The Pismo platform uses this field to retrieve corresponding network authorization during migration process.<br><br>**Note**: This field is critical for performing network reconciliations after migration. If you need to migrate pending authorizations but you don't have this ID, contact your Pismo representative for guidance.<br> |  |
| `merchant_id` | string | no | ID of the merchant accepting the card for network authorization. (Only for `NETWORK` authorization type.) | example: "000000079984185" |
| `merchant_city` | string | no | Merchant city (DE 43 city field, maximum 15 characters) | maxLength: 15; example: "San Diego" |
| `merchant_name` | string | no | Merchant name. (Only for `NETWORK` authorization type.) | example: "RIO SUL IMPERADOR MAGE BRA" |
| `merchant_category_code` | integer | no | ID of merchant category. (Only for `NETWORK` authorization type.) | example: 742 |
| `merchant_state_or_country` | string | no | Merchant state or country. (Only for `NETWORK` authorization type.) | example: "BR" |
| `retrieval_reference_number` | string | no | Retrieval reference number. (Only for `NETWORK` authorization type.) | example: "130720000148" |
| `clearing_date` | string | no | Confirmation date for clearing. Format = YYYY-MM-DD. (Only for `NETWORK` authorization type.) | format: "date"; example: "2019-12-11" |
| `number_of_installments` | integer | no | Total number of installments related to the migrated authorization | format: "int32"; minimum: 1; example: 5 |
| `is_installment` | boolean | no | Is this transaction part of an installment contract? Set to `true` only if transaction type is `BILLED` or `TO_BE_BILLED`. | example: true |
| `has_interest` | boolean | no | Is the transaction part of an installment contract and does it have interest? Set to `true` only if the transaction type is `BILLED` or `TO_BE_BILLED`. | example: true |
| `installment_transaction_type_id` | integer | no | ID of transaction type for managing installments with flexible transaction types and processing codes | example: 8889 |
| `installment` | integer | no | Installment number, starting with 1. Only for installment sent as `BILLED` or `TO_BE_BILLED` type. Not necessary to send with `INSTALLMENTS` type.  (First installment has installment number 1.) | example: 2 |
| `event_date_hour` | string | no | Original transaction date and hour. Format = YYYY-MM-DDTHH:mm:ssZ. | format: "date-time"; example: "2021-09-21T12:00:00Z" |
| `due_date_hour` | string | no | Date and time when transaction is due | format: "date-time"; example: "2020-09-21T12:00:00Z" |
| `accounting_date` | string | no | Creation date of accounting record. Using the go-live date is recommended. Format = YYYY-MM-DD. | format: "date"; example: "2019-12-11" |
| `settlement_currency_rate` | number | no | Settlement currency rate. (Only for `NETWORK` authorization type.) | format: "float"; example: 12.55 |
| `cardholder_amount` | number | no | Transaction's cardholder amount | format: "float"; example: 171.42 |
| `cardholder_currency_code` | string | no | Transaction's cardholder currency code | example: "840" |
| `cardholder_currency_rate` | number | no | Conversion rate between local value and cardholder value. (Only for `NETWORK` authorization type.) | format: "float"; example: 12.6 |
| `interest_rate` | number | no | Interest rate. When using `INSTALLMENTS` transaction type, this sets the interest rate for all installment contracts. | format: "float"; example: 12.31 |
| `interest_amount` | number | no | Interest amount. When using `INSTALLMENTS` transaction type, sets the interest amount for all installment contracts. | format: "float"; example: 12.42 |
| `iof_amount` | number | no | IOF amount (Brazil only). If the transaction did not take place in Brazil, this should be left blank.<br> | format: "float"; example: 1.55 |
| `authorization_code` | string | no | Authorization code | example: "444" |
| `amounts` | array of object | no | List of amounts |  |
| `amounts[].type` | string | no | Amount type, where `LOCAL` refers to the amount the cardholder requested in the currency of the acquirer or source location of the transaction. `PRINCIPAL` refers to the transaction principal amount (without interest). `SETTLEMENT` refers to the amount transferred between the acquirer and the issuer in the settlement currency. Mastercard programs and services use U.S. dollars as the currency of settlement.<br> | enum: ["PRINCIPAL", "LOCAL", "SETTLEMENT"]; example: "PRINCIPAL" |
| `amounts[].currency` | integer | no | Settlement amount currency code, such as 840 for U.S. dollar | example: 986 |
| `amounts[].value` | number | no | Amount value | format: "float"; example: 2.55 |
| `installments_type` | string | no | Installment type (`WITHOUT_INTEREST`, `WITH_INTEREST`, or `STATEMENT`). Note that you use `STATEMENT` to migrate `payment_agreement` data.<br> | enum: ["WITHOUT_INTEREST", "WITH_INTEREST", "STATEMENT"]; example: "WITHOUT_INTEREST" |
| `installments` | array of object | no | Installment list |  |
| `installments[].installment` | integer | yes | Number of installments | example: 2 |
| `installments[].release_date` | string | yes | Release date | format: "date"; example: "2022-02-01" |
| `installments[].amount` | number | no | Installment amount | format: "float"; example: 56.78 |
| `installments[].interest_rate` | number | no | Installment interest rate | format: "float"; example: 0 |
| `installments[].interest_amount` | number | no | Installment interest amount | format: "float"; example: 0 |
| `installments[].interest_amount_pend_approp` | number | no | Amount of pending interest in an installment transaction. When you migrate an installment transaction that still has pending interests to be charged, you must also provide the interest amount so that the Pismo platform can calculate the interest accruals for you.<br> | format: "float"; example: 0 |
| `installments[].iof_amount` | number | no | Installment IOF amount | format: "float"; example: 0 |
| `installments[].status` | string | no | Installment status:<br>- `0`—Future installment<br>- `1`—Advancement request<br>- `2`—Posted installment, either `BILLED` or `TO_BE_BILLED`<br>- `4`—Advanced installment<br>- `6`—Canceled installment<br> | enum: ["0", "1", "2", "4", "6"]; example: "1" |
| `interest_amount_pend_approp` | number | no | Amount of pending interest in an installment transaction. When you migrate an installment transaction that still has pending interest, you must provide the interest amount so that the Pismo platform can calculate the accruals. This value must only be used on `BILLED` and `TO_BE_BILLED` transactions when they are `WITH_INTEREST`. Otherwise, the value must be zero or omitted.<br> | format: "float"; example: 0 |
| `metadata` | object | no | Transaction metadata<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"key1": "value1", "key2": "value2"} |
| `payment_agreement` | boolean | no | Is this an installment or a refinancing product? If `true`, the Pismo platform creates the `payment_agreement` entity automatically, so you do not have to call the [Create payment agreement](ref:installmentpaymentsv4) endpoint separately after transaction migration. This field only affects the `INSTALLMENTS` type transaction.<br> | default: false; example: true |
| `payment_agreement_data` | object | no | Payment agreement data. This object only affects `INSTALLMENTS` type transactions and only when the `payment_agreement` attribute is set to `true`. |  |
| `payment_agreement_data.compulsory` | boolean | yes | Is the transaction compulsory? If `true`, indicates transaction is a statement agreement. When transaction is either a statement agreement or an installment agreement, set to `false`.<br> | example: true |
| `payment_agreement_data.settle_accrual` | boolean | yes | Should the pending interest accrual be settled (forgiven) when the agreement is created? Required when `payment_agreement` is `true`.<br> | example: true |
| `payment_agreement_data.split_iof` | boolean | yes | (Brazil only) Generate transaction for IOF separately? Required when `payment_agreement` is `true`.<br> | example: true |
| `payment_agreement_data.statement_agreement` | boolean | yes | Is transaction a payment agreement or a statement agreement? When the transaction is either a compulsory or an installment agreement, set to `false`.<br> | example: true |
| `payment_agreement_data.use_original_rate` | boolean | yes | Use value from the `interest_rate` field for accrued interest? Required when `payment_agreement` is `true`.<br> | example: false |
| `instant_payment_data` | object | no | Defines specific options for instant payment transactions. **REQUIRED** when the `transaction_type` is `INSTANT_PAYMENT`. |  |
| `instant_payment_data.internal_transaction` | boolean | no | Did both transactions occur in the same <<glossary:Org>>? An instant payment requires two transactions to be completed (such as PIX-IN/PIX-OUT or PIX-IN-REVERSAL/PIX-OUT-REVERSAL). |  |
| `instant_payment_data.external_id` | string | no | Provider transaction ID. **REQUIRED** for Pix cancellation under 90 days when type is `PIX-IN`. | example: "external-id" |
| `instant_payment_data.external_bank` | string | no | Counterparty bank code (from payer or receiver). **REQUIRED** when type is `PIX-IN` or `PIX-OUT`. | example: "external-bank" |
| `instant_payment_data.external_document_number` | string | no | Counterparty <<glossary:document number>> (from payer or receiver). **REQUIRED** when type is `PIX-IN` or `PIX-OUT`. | example: "external-document-number" |
| `instant_payment_data.external_name` | string | no | Counterparty name (from payer or receiver). | example: "John Doe" |
| `instant_payment_data.key` | string | no | Pix key of the payee. **REQUIRED** when the `initiation_type` is `DICT`, `STATIC_QRCODE`, or `DYNAMIC_QRCODE`.<br> | example: "000.000.000-00" |
| `instant_payment_data.initiation_type` | string | no | Transaction initiation type:<br>- `MANUAL`—Manually initiated. Key is not used. Instead, bank account, bank code, document number, and branch are used for identification.<br>- `DICT`—Pix key is used for identification. (DICT is the national Pix key registry and database.)<br>- `STATIC_QRCODE`—Reusable code that contains only the essential data needed to complete a transaction. The transaction amount must be entered manually.<br>- `DYNAMIC_QRCODE`—Reusable code that includes the transaction amount and other details.<br>- `PAYMENT_INITIATOR`—Payment provider initiator. (A payment initiator is a third party that is authorized by the Central Bank and has an Open Finance certification.)<br> | enum: ["MANUAL", "DICT", "STATIC_QRCODE", "DYNAMIC_QRCODE", "PAYMENT_INITIATOR"]; example: "MANUAL" |
| `instant_payment_data.transaction_type` | string | no | Instant payment transaction type:<br>- `TRANSFER`—Simple transfer (purchase or cash only)<br>- `WITHDRAWAL`—Cash-only transaction (only when initiated by a `WITHDRAWAL` type QR code)<br>- `CHANGE`—Transfer of cash in addition to purchase amount (only when initiated by a `CHANGE` type QR code).<br> | enum: ["TRANSFER", "WITHDRAWAL", "CHANGE"]; default: "TRANSFER"; example: "TRANSFER" |

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
| `migration-instant-payment-outgoing-1` | https://developers.pismo.io/events/docs/migration-instant-payment-outgoing-1 |
| `migration-organize-statement-outgoing-1` | https://developers.pismo.io/events/docs/migration-organize-statement-outgoing-1 |
| `migration-payment-agreements-outgoing-1` | https://developers.pismo.io/events/docs/migration-payment-agreements-outgoing-1 |
| `migration-transaction-incoming-1` | https://developers.pismo.io/events/docs/migration-transaction-incoming-1 |
| `migration-transaction-outgoing-1` | https://developers.pismo.io/events/docs/migration-transaction-outgoing-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;500`, has examples `True`, emits events `5`, deprecated `False`.

Guides that link to this operation: `KU-EVT-migrations-data-events`.

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
| `api-specs/Migrations.yaml` | tag `Transaction migration`: POST /v1/migrations/transactions | https://github.com/PismoDevEx/pismo-api-specs | `7478abcca92f0932…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-migration` — Event catalogue: migration
- `KU-EVT-migrations-data-events` — Migrations events
