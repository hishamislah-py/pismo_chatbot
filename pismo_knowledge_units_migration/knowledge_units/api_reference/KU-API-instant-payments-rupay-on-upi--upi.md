---
ku_id: KU-API-instant-payments-rupay-on-upi--upi
title: 'API reference: Instant payments - RuPay on UPI — UPI'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_RuPay_on_UPI.yaml
  sha256: 5f264e17cce9a121173351bca8ff471e33630be756e8c8d494c9c2aa12b4c9a1
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
- post-list-cards
- post-validate-card-data
- post-funds-transfer
- emi-select
- get-transfer-funds-status
- post-balance-enquiry
- post-card-bill
related_kus:
- KU-ERR-codes-eupi
- KU-EVT-catalogue-other-domains
- KU-PAY-united-payments-interface
specification_version: '1.0'
---

# API reference: Instant payments - RuPay on UPI — UPI

**KU ID:** `KU-API-instant-payments-rupay-on-upi--upi` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `UPI` in `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` (“Instant payments - RuPay on UPI”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage UPI operations

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/cards/list` | `post-list-cards` | List cards | no |
| `POST /v1/cards/validate` | `post-validate-card-data` | Validate card data | no |
| `POST /v1/cards/transfer` | `post-funds-transfer` | Transfer UPI funds | no |
| `POST /v1/cards/emi-select` | `emi-select` | EMI select | no |
| `GET /v1/transactions/inquiry/account-reference-number/{account_reference_number}/external-transaction-id/{external_transaction_id}` | `get-transfer-funds-status` | Get funds transfer status | no |
| `POST /v1/cards/balance` | `post-balance-enquiry` | Get balance for account | no |
| `POST /v1/cards/credit-card-bill` | `post-card-bill` | Get card bill | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account token - token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** error.<br>

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_RuPay_on_UPI.yaml method=POST path=/v1/cards/list operationId=post-list-cards -->
### `POST /v1/cards/list` — List cards

- **operationId:** `post-list-cards`
- **Specification:** `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` (Instant payments - RuPay on UPI)
- **Server base URL(s):** `https://sandbox.pismolabs.io/upi-gateway`
- **Tags:** `UPI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Return active account card list

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token. Tokens can expire quickly, which can result in a **401 Unauthorized** message. | example: "Bearer eyJhbGci...IUzUx" |
| `user-agent` | header | yes | string | Client consuming API. |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `cards.ListCardsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | yes | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `phone` | object (schema `phone`) | yes |  | example: {"country_code": "91", "phone": "9592714958"} |
| `type` | string (schema `cardType`) | no | Pismo card type. For more information, see [Cards management](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#card-types). Default is empty string, meaning all card types are returned. | enum: ["", "PLASTIC", "VIRTUAL", "TEMPORARY"]; example: "PLASTIC" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `cards.ListCardsResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 422 | UnprocessableEntity | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cards` | array of object (schema `cards.CardsData`) | yes | Account cards |  |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | yes | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `owner` | object | yes | Account owner data |  |
| `owner.name` | string | yes | Owner name |  |
| `phone` | object (schema `phone`) | yes |  | example: {"country_code": "91", "phone": "9592714958"} |

##### Response 400

400 Example `EUPI0003` (Bad Request):

```json
{
  "code": "EUPI0003",
  "message": "Bad Request"
}
```

400 Example `EUPI0023` (number is a required field):

```json
{
  "code": "EUPI0023",
  "message": "number is a required field"
}
```

400 Example `EUPI0002` (Validation error):

```json
{
  "code": "EUPI0002",
  "message": "Validation error"
}
```

##### Response 403

403 Example `EUPI0004` (Missing required header 'x-tenant'):

```json
{
  "code": "EUPI0004",
  "message": "Missing required header 'x-tenant'"
}
```

##### Response 404

404 Example `EUPI0028` (Cards not found.):

```json
{
  "code": "EUPI0028",
  "message": "Cards not found."
}
```

404 Example `EUPI0032` (Not found.):

```json
{
  "code": "EUPI0032",
  "message": "Not found."
}
```

404 Example `EUPI0007` (Account not found.):

```json
{
  "code": "EUPI0007",
  "message": "Account not found."
}
```

##### Response 409

409 Example `EUPI0024` (card type invalid):

```json
{
  "code": "EUPI0024",
  "message": "card type invalid"
}
```

409 Example `EUPI0014` (Not unique owner for the phone number):

```json
{
  "code": "EUPI0014",
  "message": "Not unique owner for the phone number"
}
```

##### Response 422

422 Example `EUPI0004` (An unexpected error has occurred):

```json
{
  "code": "EUPI0042",
  "message": "An unexpected error has occurred"
}
```

##### Response 500

500 Example `EUPI0001` (An unexpected error happened):

```json
{
  "code": "EUPI0001",
  "message": "An unexpected error happened"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EUPI0003` | Bad Request |
| 400 | `EUPI0023` | number is a required field |
| 400 | `EUPI0002` | Validation error |
| 403 | `EUPI0004` | Missing required header 'x-tenant' |
| 404 | `EUPI0028` | Cards not found. |
| 404 | `EUPI0032` | Not found. |
| 404 | `EUPI0007` | Account not found. |
| 409 | `EUPI0024` | card type invalid |
| 409 | `EUPI0014` | Not unique owner for the phone number |
| 422 | `EUPI0042` | An unexpected error has occurred |
| 500 | `EUPI0001` | An unexpected error happened |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;422;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_RuPay_on_UPI.yaml method=POST path=/v1/cards/validate operationId=post-validate-card-data -->
### `POST /v1/cards/validate` — Validate card data

- **operationId:** `post-validate-card-data`
- **Specification:** `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` (Instant payments - RuPay on UPI)
- **Server base URL(s):** `https://sandbox.pismolabs.io/upi-gateway`
- **Tags:** `UPI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Validate client card data for [Transfer funds](ref:post-funds-transfer)

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token. Tokens can expire quickly, which can result in a **401 Unauthorized** message. | example: "Bearer eyJhbGci...IUzUx" |
| `user-agent` | header | yes | string | Client consuming API. |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `cards.ValidateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_reference_number` | string (schema `accountReferenceNumber`) | yes | <br>Account reference number. Pismo creates this automatically when creating a card linked to RuPay on UPI.<br><br>This number combines 10 BIN digits and the credit account number. If BIN is 6 digits, the remaining 4 digits  are set to zero (`0`). If BIN is 8 digits, then the remaining 2 digits are set to zero. This is a [NPCI](https://www.npci.org.in/what-we-do/rupay/product-overview) standard. For example, if the account reference number = `1234560000987654321`, the first six digits are the BIN, appended with 4 zeros and then the credit account number (`987654321``).<br><br>You can call [List cards](ref:post-list-cards) to get a card's account reference number.<br> | example: "12345600000000001140340134" |
| `card_data` | object | yes | Card data |  |
| `card_data.card_expiration` | string | yes | Card expiration, format = MMYY. **REQUIRED** if `last_six_digits` is passed. | example: "0529" |
| `card_data.last_six_digits` | string | yes | Card's last six digits. **REQUIRED** if `card_expiration` is passed | example: "657114" |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | yes | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `pin_data` | object | no | Pin data |  |
| `pin_data.pin_block` | string | yes | Pin block | example: "3FE661D50EF1F6F1" |
| `pin_data.key_id` | string | yes | Key encryption ID | example: "7d14ca2e-1057-11ee-8cee-060f666de710" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `cards.ValidateResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 422 | UnprocessableEntity | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_reference_number` | string (schema `accountReferenceNumber`) | yes | <br>Account reference number. Pismo creates this automatically when creating a card linked to RuPay on UPI.<br><br>This number combines 10 BIN digits and the credit account number. If BIN is 6 digits, the remaining 4 digits  are set to zero (`0`). If BIN is 8 digits, then the remaining 2 digits are set to zero. This is a [NPCI](https://www.npci.org.in/what-we-do/rupay/product-overview) standard. For example, if the account reference number = `1234560000987654321`, the first six digits are the BIN, appended with 4 zeros and then the credit account number (`987654321``).<br><br>You can call [List cards](ref:post-list-cards) to get a card's account reference number.<br> | example: "12345600000000001140340134" |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | yes | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `result` | string | yes | Validation result. If not valid, an error message is returned. | example: "VALIDATED" |

##### Response 400

400 Example `EUPI0041` (last_six_digits is a required field):

```json
{
  "code": "EUPI0041",
  "message": "last_six_digits is a required field"
}
```

400 Example `EUPI0040` (cvv is a required field):

```json
{
  "code": "EUPI0040",
  "message": "cvv is a required field"
}
```

400 Example `EUPI0039` (card_expiration is a required field):

```json
{
  "code": "EUPI0039",
  "message": "card_expiration is a required field"
}
```

400 Example `EUPI0038` (pin is a required field):

```json
{
  "code": "EUPI0038",
  "message": "pin is a required field"
}
```

400 Example `EUPI0003` (Bad Request):

```json
{
  "code": "EUPI0003",
  "message": "Bad Request"
}
```

400 Example `EUPI0002` (Validation error):

```json
{
  "code": "EUPI0002",
  "message": "Validation error"
}
```

##### Response 403

403 Example `EUPI0004` (Missing required header 'x-tenant'):

```json
{
  "code": "EUPI0004",
  "message": "Missing required header 'x-tenant'"
}
```

##### Response 404

404 Example `EUPI0028` (Cards not found.):

```json
{
  "code": "EUPI0028",
  "message": "Cards not found."
}
```

404 Example `EUPI0032` (Not found.):

```json
{
  "code": "EUPI0032",
  "message": "Not found."
}
```

##### Response 409

409 Example `EUPI0036` (pinblock sent is not equal as original card pinblock):

```json
{
  "code": "EUPI0036",
  "message": "pinblock sent is not equal as original card pinblock"
}
```

409 Example `EUPI0035` (card_expiration sent is not equal as original card data):

```json
{
  "code": "EUPI0035",
  "message": "card_expiration sent is not equal as original card data"
}
```

409 Example `EUPI0034` (last_six_digits sent is not equal as original card data):

```json
{
  "code": "EUPI0034",
  "message": "last_six_digits sent is not equal as original card data"
}
```

409 Example `EUPI0033` (Card with SUSPENDED status):

```json
{
  "code": "EUPI0033",
  "message": "Card with SUSPENDED status"
}
```

##### Response 422

422 Example `EUPI0004` (An unexpected error has occurred):

```json
{
  "code": "EUPI0042",
  "message": "An unexpected error has occurred"
}
```

##### Response 500

500 Example `EUPI0001` (An unexpected error happened):

```json
{
  "code": "EUPI0001",
  "message": "An unexpected error happened"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EUPI0041` | last_six_digits is a required field |
| 400 | `EUPI0040` | cvv is a required field |
| 400 | `EUPI0039` | card_expiration is a required field |
| 400 | `EUPI0038` | pin is a required field |
| 400 | `EUPI0003` | Bad Request |
| 400 | `EUPI0002` | Validation error |
| 403 | `EUPI0004` | Missing required header 'x-tenant' |
| 404 | `EUPI0028` | Cards not found. |
| 404 | `EUPI0032` | Not found. |
| 409 | `EUPI0036` | pinblock sent is not equal as original card pinblock |
| 409 | `EUPI0035` | card_expiration sent is not equal as original card data |
| 409 | `EUPI0034` | last_six_digits sent is not equal as original card data |
| 409 | `EUPI0033` | Card with SUSPENDED status |
| 422 | `EUPI0042` | An unexpected error has occurred |
| 500 | `EUPI0001` | An unexpected error happened |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;422;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_RuPay_on_UPI.yaml method=POST path=/v1/cards/transfer operationId=post-funds-transfer -->
### `POST /v1/cards/transfer` — Transfer UPI funds

- **operationId:** `post-funds-transfer`
- **Specification:** `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` (Instant payments - RuPay on UPI)
- **Server base URL(s):** `https://sandbox.pismolabs.io/upi-gateway`
- **Tags:** `UPI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> United Payments Interface (UPI) funds transfer for RuPay, an Indian card network.
>
> Before calling this endpoint, you can call [List cards](ref:post-list-cards) to get the `account_reference_number`. You should also call [Validate card](ref:post-validate-card-data) to make sure the card data for the transfer request is genuine.
>
> This endpoint generates a [Payment methods authorization created](https://developers.pismo.io/events/docs/payment-methods-authorization-1) event and a [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event.
>
> This operation is **idempotent**, meaning, it can be applied multiple times, yet the outcome remains the same. To guarantee this, the request has an `external_transaction_id` field, which must be unique by transaction type in the context of the same account reference number. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token. Tokens can expire quickly, which can result in a **401 Unauthorized** message. | example: "Bearer eyJhbGci...IUzUx" |
| `user-agent` | header | yes | string | Client consuming API. |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `cards.TransferRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Transaction amount | example: 500 |
| `currency` | string | yes | Transaction currency. ISO 4217 3-digit currency code. For example - `INR` (Indian rupee) | example: "INR" |
| `account_reference_number` | string (schema `accountReferenceNumber`) | yes | <br>Account reference number. Pismo creates this automatically when creating a card linked to RuPay on UPI.<br><br>This number combines 10 BIN digits and the credit account number. If BIN is 6 digits, the remaining 4 digits  are set to zero (`0`). If BIN is 8 digits, then the remaining 2 digits are set to zero. This is a [NPCI](https://www.npci.org.in/what-we-do/rupay/product-overview) standard. For example, if the account reference number = `1234560000987654321`, the first six digits are the BIN, appended with 4 zeros and then the credit account number (`987654321``).<br><br>You can call [List cards](ref:post-list-cards) to get a card's account reference number.<br> | example: "12345600000000001140340134" |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | yes | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `mcc` | string | yes | Transaction Merchant Category Code (MCC) | example: "6012" |
| `merchant_name` | string | yes | Merchant name | example: "Cafe Coffee Day" |
| `merchant` | object (schema `merchant`) | no |  |  |
| `phone` | object (schema `phone`) | yes |  | example: {"country_code": "91", "phone": "9592714958"} |
| `transaction_type` | string (schema `transactionType`) | yes | Transaction type:<br> * `C` - Credit<br> * `D` - Debit<br> * `R` - Reversal<br> * `E` - Equated monthly installments (EMI)<br> * `F` - Foreclose<br> | enum: ["C", "D", "R", "E", "F"]; example: "C" |
| `upi_reference_number` | string (schema `upiReferenceNumber`) | yes | UPI reference number | minLength: 12; maxLength: 12; example: "165238546812" |
| `transaction_reference` | string | no | Transaction reference | example: "Lunch" |
| `credit_account_number` | string | no | Payee account number if available | example: "98765004371" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Transfer created | `application/json`: object (schema `cards.TransferResponse`) |
| 202 | It is returned for duplicated requests, when the transfer is still being processed | `application/json`: object (schema `cards.TransferResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 401 | Unauthorized | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 408 | Timeout | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `status` | string (schema `transactionStatus`) | yes | Transaction status | enum: ["PROCESSING", "ACCEPTED", "ERROR", "CANCELLED"]; example: "PROCESSING" |
| `upi_reference_number` | string (schema `upiReferenceNumber`) | yes | UPI reference number | minLength: 12; maxLength: 12; example: "165238546812" |
| `authorization_id` | number (schema `authorizationID`) | no | Authorization ID | example: 2263052808 |
| `authorization_datetime` | string (schema `authorizationDatetime`) | no | When transfer was authorised. RFC 3339 format. | format: "datetime" |

201 Example `example`:

```json
{
  "upi_reference_number": "165238546812",
  "external_transaction_id": "MGS584A1244F6BC4D50A3FABE6D93DF913C",
  "authorization_id": 2263052808,
  "authorization_datetime": "2024-09-04T13:22:09.579Z",
  "status": "ACCEPTED"
}
```

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `status` | string (schema `transactionStatus`) | yes | Transaction status | enum: ["PROCESSING", "ACCEPTED", "ERROR", "CANCELLED"]; example: "PROCESSING" |
| `upi_reference_number` | string (schema `upiReferenceNumber`) | yes | UPI reference number | minLength: 12; maxLength: 12; example: "165238546812" |
| `authorization_id` | number (schema `authorizationID`) | no | Authorization ID | example: 2263052808 |
| `authorization_datetime` | string (schema `authorizationDatetime`) | no | When transfer was authorised. RFC 3339 format. | format: "datetime" |

202 Example `example`:

```json
{
  "upi_reference_number": "165238546812",
  "external_transaction_id": "MGS584A1244F6BC4D50A3FABE6D93DF913C",
  "status": "PROCESSING"
}
```

##### Response 400

400 Example `EUPI0002` (Validation error):

```json
{
  "code": "EUPI0002",
  "message": "Validation error",
  "details": {
    "payload": [
      {
        "field": "external_transaction_id",
        "message": "Field 'external_transaction_id' is required"
      }
    ]
  }
}
```

400 Example `EUPI0003` (Bad request):

```json
{
  "code": "EUPI0003",
  "message": "Bad request"
}
```

400 Example `EUPI0104` (Invalid transaction type):

```json
{
  "code": "EUPI0104",
  "message": "Invalid transaction type"
}
```

400 Example `EUPI0101` (The transaction was cancelled due authorization request validation error):

```json
{
  "code": "EUPI0101",
  "message": "The transaction was cancelled due authorization request validation error"
}
```

400 Example `EUPI0108` (The transaction was cancelled due to authorization error):

```json
{
  "code": "EUPI0108",
  "message": "The transaction was cancelled due to an authorization error"
}
```

##### Response 401

401 Example `EUPI0120` (Transfer amount is greater than the account available limits):

```json
{
  "code": "EUPI0120",
  "message": "Transfer amount is greater than the account available limits"
}
```

##### Response 403

403 Example `EUPI0004` (Missing required header 'x-tenant'):

```json
{
  "code": "EUPI0004",
  "message": "Missing required header 'x-tenant'"
}
```

##### Response 404

404 Example `EUPI0110` (Original transaction not found on reversal operation):

```json
{
  "code": "EUPI0110",
  "message": "Original transaction not found on reversal operation"
}
```

##### Response 408

408 Example `EUPI0020` (Upi - API returned a timeout error):

```json
{
  "code": "EUPI0020",
  "message": "Upi - API returned a timeout error"
}
```

##### Response 409

409 Example `EUPI0100` (Transaction already exists with the external_transaction_id):

```json
{
  "code": "EUPI0100",
  "message": "Transaction already exists with the external_transaction_id"
}
```

409 Example `EUPI0112` (Original transaction is still being processed):

```json
{
  "code": "EUPI0112",
  "message": "Original transaction is still being processed"
}
```

409 Example `EUPI0113` (Original transaction is not accepted, then it can't be reverted):

```json
{
  "code": "EUPI0113",
  "message": "Original transaction is not accepted, then it can't be reverted"
}
```

409 Example `EUPI0114` (Reversal transaction amount must be equals to the original transaction):

```json
{
  "code": "EUPI0114",
  "message": "Reversal transaction amount must be equals to the original transaction"
}
```

409 Example `EUPI0121` (Invalid card status):

```json
{
  "code": "EUPI0121",
  "message": "Invalid card status"
}
```

##### Response 500

500 Example `EUPI0001` (An unexpected error happened):

```json
{
  "code": "EUPI0001",
  "message": "An unexpected error happened"
}
```

500 Example `EUPI0105` (The transaction will be cancelled due to internal error):

```json
{
  "code": "EUPI0105",
  "message": "The transaction will be cancelled due to internal error"
}
```

500 Example `EUPI0106` (The transaction was authorized but will be canceled due to internal error):

```json
{
  "code": "EUPI0106",
  "message": "The transaction was authorized but will be canceled due to internal error"
}
```

##### Response 502

502 Example `EUPI0109` (The transaction will be cancelled due to authorization error):

```json
{
  "code": "EUPI0109",
  "message": "The transaction will be cancelled due to authorization error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EUPI0002` | Validation error |
| 400 | `EUPI0003` | Bad request |
| 400 | `EUPI0104` | Invalid transaction type |
| 400 | `EUPI0101` | The transaction was cancelled due authorization request validation error |
| 400 | `EUPI0108` | The transaction was cancelled due to an authorization error |
| 401 | `EUPI0120` | Transfer amount is greater than the account available limits |
| 403 | `EUPI0004` | Missing required header 'x-tenant' |
| 404 | `EUPI0110` | Original transaction not found on reversal operation |
| 408 | `EUPI0020` | Upi - API returned a timeout error |
| 409 | `EUPI0100` | Transaction already exists with the external_transaction_id |
| 409 | `EUPI0112` | Original transaction is still being processed |
| 409 | `EUPI0113` | Original transaction is not accepted, then it can't be reverted |
| 409 | `EUPI0114` | Reversal transaction amount must be equals to the original transaction |
| 409 | `EUPI0121` | Invalid card status |
| 500 | `EUPI0001` | An unexpected error happened |
| 500 | `EUPI0105` | The transaction will be cancelled due to internal error |
| 500 | `EUPI0106` | The transaction was authorized but will be canceled due to internal error |
| 502 | `EUPI0109` | The transaction will be cancelled due to authorization error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `payment-methods-authorization-1` | https://developers.pismo.io/events/docs/payment-methods-authorization-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;401;403;404;408;409;500;502`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-PAY-united-payments-interface`.

<!-- op: spec=api-specs/Instant_payments_-_RuPay_on_UPI.yaml method=POST path=/v1/cards/emi-select operationId=emi-select -->
### `POST /v1/cards/emi-select` — EMI select

- **operationId:** `emi-select`
- **Specification:** `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` (Instant payments - RuPay on UPI)
- **Server base URL(s):** `https://sandbox.pismolabs.io/upi-gateway`
- **Tags:** `UPI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> United Payments Interface (UPI) funds Equated Monthly Installments (EMI) for RuPay, an Indian card network.
>
> Before calling this endpoint, you can call [List cards](ref:post-list-cards) to get the `account_reference_number`. You should also call [Validate card](ref:post-validate-card-data) to make sure the card data for the transfer request is genuine.
>
> This endpoint generates a [Payment methods authorization created](https://developers.pismo.io/events/docs/payment-methods-authorization-1) event and a [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event.
>
> This operation is **idempotent**, meaning, it can be applied multiple times, yet the outcome remains the same. To guarantee this, the request has an `external_transaction_id` field, which must be unique by transaction type in the context of the same account reference number. 

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token. Tokens can expire quickly, which can result in a **401 Unauthorized** message. | example: "Bearer eyJhbGci...IUzUx" |
| `user-agent` | header | yes | string | Client consuming API. |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `cards.EmiRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Transaction amount | example: 500 |
| `currency` | string | yes | Transaction currency. ISO 4217 3-digit currency code. For example - `INR` (Indian rupee) | example: "INR" |
| `account_reference_number` | string (schema `accountReferenceNumber`) | yes | <br>Account reference number. Pismo creates this automatically when creating a card linked to RuPay on UPI.<br><br>This number combines 10 BIN digits and the credit account number. If BIN is 6 digits, the remaining 4 digits  are set to zero (`0`). If BIN is 8 digits, then the remaining 2 digits are set to zero. This is a [NPCI](https://www.npci.org.in/what-we-do/rupay/product-overview) standard. For example, if the account reference number = `1234560000987654321`, the first six digits are the BIN, appended with 4 zeros and then the credit account number (`987654321``).<br><br>You can call [List cards](ref:post-list-cards) to get a card's account reference number.<br> | example: "12345600000000001140340134" |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | yes | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `original_external_transaction_id` | string (schema `originalExternalTransactionId`) | yes | Request identification code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `emi_status` | string | yes | EMI status | enum: ["PRE", "POST", "DURING", "FORECLOSE"]; example: "DURING" |
| `mcc` | string | yes | Transaction Merchant Category Code (MCC) | example: "6012" |
| `merchant_name` | string | yes | Merchant name | example: "Cafe Coffee Day" |
| `phone` | object (schema `phone`) | yes |  | example: {"country_code": "91", "phone": "9592714958"} |
| `transaction_type` | string (schema `transactionType`) | yes | Transaction type:<br> * `C` - Credit<br> * `D` - Debit<br> * `R` - Reversal<br> * `E` - Equated monthly installments (EMI)<br> * `F` - Foreclose<br> | enum: ["C", "D", "R", "E", "F"]; example: "C" |
| `upi_reference_number` | string (schema `upiReferenceNumber`) | yes | UPI reference number | minLength: 12; maxLength: 12; example: "165238546812" |
| `transaction_reference` | string | no | Transaction reference | example: "Lunch" |
| `credit_account_number` | string | no | Payee account number if available | example: "98765004371" |
| `foreclose_data` | object (schema `forecloseData`) | no |  |  |
| `emi_data` | object (schema `emiData`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Emi created | `application/json`: object (schema `cards.EmiResponse`) |
| 202 | It is returned for duplicated requests, when the transfer is still being processed | `application/json`: object (schema `cards.EmiResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 401 | Unauthorized | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 408 | Timeout | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `status` | string (schema `transactionStatus`) | yes | Transaction status | enum: ["PROCESSING", "ACCEPTED", "ERROR", "CANCELLED"]; example: "PROCESSING" |
| `upi_reference_number` | string (schema `upiReferenceNumber`) | yes | UPI reference number | minLength: 12; maxLength: 12; example: "165238546812" |
| `authorization_id` | number (schema `authorizationID`) | no | Authorization ID | example: 2263052808 |
| `authorization_datetime` | string (schema `authorizationDatetime`) | no | When transfer was authorised. RFC 3339 format. | format: "datetime" |
| `foreclose_data` | object (schema `forecloseData`) | no |  |  |
| `emi_data` | object (schema `emiData`) | no |  |  |

201 Example `example`:

```json
{
  "upi_reference_number": "E0ADFEC95DCA",
  "external_transaction_id": "MGSA5888297390E471980C85F56615A87FB",
  "authorization_id": 2270052278,
  "status": "ACCEPTED",
  "emi_data": {
    "contract_amount": 10143.64,
    "principal_amount": 10000,
    "number_of_installments": 3,
    "fees": [
      {
        "type": "FIXED",
        "amount": 10
      }
    ],
    "interests": [
      {
        "type": "monthly",
        "amount": 44.54,
        "rate": 8
      },
      {
        "type": "monthly",
        "amount": 44.54,
        "rate": 8
      },
      {
        "type": "monthly",
        "amount": 44.54,
        "rate": 8
      }
    ],
    "taxes": null,
    "installments": [
      {
        "number": 1,
        "contract_amount": 3387.88,
        "principal_amount": 3333.33,
        "fees": [
          {
            "type": "FIXED",
            "amount": 10
          }
        ],
        "interests": [
          {
            "type": "monthly",
            "amount": 44.54,
            "rate": 8
          }
        ],
        "taxes": null
      },
      {
        "number": 2,
        "contract_amount": 3377.88,
        "principal_amount": 3333.33,
        "fees": null,
        "interests": [
          {
            "type": "monthly",
            "amount": 44.54,
            "rate": 8
          }
        ],
        "taxes": null
      },
      {
        "number": 3,
        "contract_amount": 3377.88,
        "principal_amount": 3333.33,
        "fees": null,
        "interests": [
          {
            "type": "monthly",
            "amount": 44.54,
            "rate": 8
          }
        ],
        "taxes": null
      }
    ]
  }
}
```

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `status` | string (schema `transactionStatus`) | yes | Transaction status | enum: ["PROCESSING", "ACCEPTED", "ERROR", "CANCELLED"]; example: "PROCESSING" |
| `upi_reference_number` | string (schema `upiReferenceNumber`) | yes | UPI reference number | minLength: 12; maxLength: 12; example: "165238546812" |
| `authorization_id` | number (schema `authorizationID`) | no | Authorization ID | example: 2263052808 |
| `authorization_datetime` | string (schema `authorizationDatetime`) | no | When transfer was authorised. RFC 3339 format. | format: "datetime" |
| `foreclose_data` | object (schema `forecloseData`) | no |  |  |
| `emi_data` | object (schema `emiData`) | no |  |  |

202 Example `example`:

```json
{
  "upi_reference_number": "E0ADFEC95DCA",
  "external_transaction_id": "MGSA5888297390E471980C85F56615A87FB",
  "status": "PROCESSING",
  "emi_data": {
    "contract_amount": 10143.64,
    "principal_amount": 10000,
    "number_of_installments": 3,
    "fees": [
      {
        "type": "FIXED",
        "amount": 10
      }
    ],
    "interests": [
      {
        "type": "monthly",
        "amount": 44.54,
        "rate": 8
      },
      {
        "type": "monthly",
        "amount": 44.54,
        "rate": 8
      },
      {
        "type": "monthly",
        "amount": 44.54,
        "rate": 8
      }
    ],
    "taxes": null,
    "installments": [
      {
        "number": 1,
        "contract_amount": 3387.88,
        "principal_amount": 3333.33,
        "fees": [
          {
            "type": "FIXED",
            "amount": 10
          }
        ],
        "interests": [
          {
            "type": "monthly",
            "amount": 44.54,
            "rate": 8
          }
        ],
        "taxes": null
      },
      {
        "number": 2,
        "contract_amount": 3377.88,
        "principal_amount": 3333.33,
        "fees": null,
        "interests": [
          {
            "type": "monthly",
            "amount": 44.54,
            "rate": 8
          }
        ],
        "taxes": null
      },
      {
        "number": 3,
        "contract_amount": 3377.88,
        "principal_amount": 3333.33,
        "fees": null,
        "interests": [
          {
            "type": "monthly",
            "amount": 44.54,
            "rate": 8
          }
        ],
        "taxes": null
      }
    ]
  }
}
```

##### Response 400

400 Example `EUPI0002` (Validation error):

```json
{
  "code": "EUPI0002",
  "message": "Validation error",
  "details": {
    "payload": [
      {
        "field": "external_transaction_id",
        "message": "Field 'external_transaction_id' is required"
      }
    ]
  }
}
```

400 Example `EUPI0003` (Bad request):

```json
{
  "code": "EUPI0003",
  "message": "Bad request"
}
```

400 Example `EUPI0104` (Invalid transaction type):

```json
{
  "code": "EUPI0104",
  "message": "Invalid transaction type"
}
```

400 Example `EUPI0101` (The transaction was cancelled due authorization request validation error):

```json
{
  "code": "EUPI0101",
  "message": "The transaction was cancelled due authorization request validation error"
}
```

400 Example `EUPI0108` (The transaction was cancelled due to authorization error):

```json
{
  "code": "EUPI0108",
  "message": "The transaction was cancelled due to an authorization error"
}
```

##### Response 401

401 Example `EUPI0120` (Transfer amount is greater than the account available limits):

```json
{
  "code": "EUPI0120",
  "message": "Transfer amount is greater than the account available limits"
}
```

##### Response 403

403 Example `EUPI0004` (Missing required header 'x-tenant'):

```json
{
  "code": "EUPI0004",
  "message": "Missing required header 'x-tenant'"
}
```

##### Response 404

404 Example `EUPI0110` (Original transaction not found on reversal operation):

```json
{
  "code": "EUPI0110",
  "message": "Original transaction not found on reversal operation"
}
```

##### Response 408

408 Example `EUPI0020` (Upi - API returned a timeout error):

```json
{
  "code": "EUPI0020",
  "message": "Upi - API returned a timeout error"
}
```

##### Response 409

409 Example `EUPI0100` (Transaction already exists with the external_transaction_id):

```json
{
  "code": "EUPI0100",
  "message": "Transaction already exists with the external_transaction_id"
}
```

409 Example `EUPI0112` (Original transaction is still being processed):

```json
{
  "code": "EUPI0112",
  "message": "Original transaction is still being processed"
}
```

409 Example `EUPI0113` (Original transaction is not accepted, then it can't be reverted):

```json
{
  "code": "EUPI0113",
  "message": "Original transaction is not accepted, then it can't be reverted"
}
```

409 Example `EUPI0114` (Reversal transaction amount must be equals to the original transaction):

```json
{
  "code": "EUPI0114",
  "message": "Reversal transaction amount must be equals to the original transaction"
}
```

409 Example `EUPI0121` (Invalid card status):

```json
{
  "code": "EUPI0121",
  "message": "Invalid card status"
}
```

##### Response 500

500 Example `EUPI0001` (An unexpected error happened):

```json
{
  "code": "EUPI0001",
  "message": "An unexpected error happened"
}
```

500 Example `EUPI0105` (The transaction will be cancelled due to internal error):

```json
{
  "code": "EUPI0105",
  "message": "The transaction will be cancelled due to internal error"
}
```

500 Example `EUPI0106` (The transaction was authorized but will be canceled due to internal error):

```json
{
  "code": "EUPI0106",
  "message": "The transaction was authorized but will be canceled due to internal error"
}
```

##### Response 502

502 Example `EUPI0109` (The transaction will be cancelled due to authorization error):

```json
{
  "code": "EUPI0109",
  "message": "The transaction will be cancelled due to authorization error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EUPI0002` | Validation error |
| 400 | `EUPI0003` | Bad request |
| 400 | `EUPI0104` | Invalid transaction type |
| 400 | `EUPI0101` | The transaction was cancelled due authorization request validation error |
| 400 | `EUPI0108` | The transaction was cancelled due to an authorization error |
| 401 | `EUPI0120` | Transfer amount is greater than the account available limits |
| 403 | `EUPI0004` | Missing required header 'x-tenant' |
| 404 | `EUPI0110` | Original transaction not found on reversal operation |
| 408 | `EUPI0020` | Upi - API returned a timeout error |
| 409 | `EUPI0100` | Transaction already exists with the external_transaction_id |
| 409 | `EUPI0112` | Original transaction is still being processed |
| 409 | `EUPI0113` | Original transaction is not accepted, then it can't be reverted |
| 409 | `EUPI0114` | Reversal transaction amount must be equals to the original transaction |
| 409 | `EUPI0121` | Invalid card status |
| 500 | `EUPI0001` | An unexpected error happened |
| 500 | `EUPI0105` | The transaction will be cancelled due to internal error |
| 500 | `EUPI0106` | The transaction was authorized but will be canceled due to internal error |
| 502 | `EUPI0109` | The transaction will be cancelled due to authorization error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `payment-methods-authorization-1` | https://developers.pismo.io/events/docs/payment-methods-authorization-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;202;400;401;403;404;408;409;500;502`, has examples `True`, emits events `2`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_RuPay_on_UPI.yaml method=GET path=/v1/transactions/inquiry/account-reference-number/{account_reference_number}/external-transaction-id/{external_transaction_id} operationId=get-transfer-funds-status -->
### `GET /v1/transactions/inquiry/account-reference-number/{account_reference_number}/external-transaction-id/{external_transaction_id}` — Get funds transfer status

- **operationId:** `get-transfer-funds-status`
- **Specification:** `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` (Instant payments - RuPay on UPI)
- **Server base URL(s):** `https://sandbox.pismolabs.io/upi-gateway`
- **Tags:** `UPI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get funds transfer status

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account_reference_number` | path | yes | string | Account reference number. Pismo creates this automatically when creating a card linked to RuPay on UPI<br><br>This number combines 10 BIN digits and the credit account number. If BIN is 6 digits, the remaining 4 digits  are set to zero (`0`). If BIN is 8 digits, then the remaining 2 digits are set to zero. This is a [NPCI](https://www.npci.org.in/what-we-do/rupay/product-overview) standard. For example, if the account reference number = `1234560000987654321`, the first six digits are the BIN, appended with 4 zeros and then the credit account number (`987654321``).<br><br>You can call [List cards](ref:post-list-cards) to get a card's account reference number.<br> |  |
| `Authorization` | header | yes | string | Authorization token. Tokens can expire quickly, which can result in a **401 Unauthorized** message. | example: "Bearer eyJhbGci...IUzUx" |
| `user-agent` | header | yes | string | Client consuming API. |  |
| `external_transaction_id` | path | yes | string | External transaction ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `cards.InquiryResponse`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 408 | Timeout | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | yes | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |
| `status` | string (schema `transactionStatus`) | yes | Transaction status | enum: ["PROCESSING", "ACCEPTED", "ERROR", "CANCELLED"]; example: "PROCESSING" |
| `transaction_type` | string (schema `transactionType`) | yes | Transaction type:<br> * `C` - Credit<br> * `D` - Debit<br> * `R` - Reversal<br> * `E` - Equated monthly installments (EMI)<br> * `F` - Foreclose<br> | enum: ["C", "D", "R", "E", "F"]; example: "C" |
| `upi_reference_number` | string (schema `upiReferenceNumber`) | yes | UPI reference number | minLength: 12; maxLength: 12; example: "165238546812" |
| `reason` | object (schema `reason`) | no | Reason |  |
| `authorization_id` | number (schema `authorizationID`) | no | Authorization ID | example: 2263052808 |
| `authorization_datetime` | string (schema `authorizationDatetime`) | no | When transfer was authorised. RFC 3339 format. | format: "datetime" |

200 Example `ACCEPTED` (Transaction accepted):

```json
{
  "external_transaction_id": "MGS584A1244F6BC4D50A3FABE6D93DF913C",
  "external_transaction_datetime": "2020-09-15T19:39:54.013Z",
  "upi_reference_number": "165238546812",
  "transaction_type": "C",
  "authorization_id": 2263052808,
  "authorization_datetime": "2024-09-04T13:22:09.579Z",
  "status": "ACCEPTED"
}
```

200 Example `CANCELLED` (Transaction cancelled):

```json
{
  "external_transaction_id": "MGS584A1244F6BC4D50A3FABE6D93DF913C",
  "external_transaction_datetime": "2020-09-15T19:39:54.013Z",
  "upi_reference_number": "165238546812",
  "transaction_type": "C",
  "authorization_id": 2263052808,
  "status": "CANCELLED",
  "reason": {
    "code": "EUPI0120",
    "message": "Transfer amount is greater than the account available limits"
  }
}
```

##### Response 403

403 Example `EUPI0004` (Missing required header 'x-tenant'):

```json
{
  "code": "EUPI0004",
  "message": "Missing required header 'x-tenant'"
}
```

##### Response 404

404 Example `EUPI0103` (Transaction not found):

```json
{
  "code": "EUPI0103",
  "message": "Transaction not found"
}
```

##### Response 408

408 Example `EUPI0020` (Upi - API returned a timeout error):

```json
{
  "code": "EUPI0020",
  "message": "Upi - API returned a timeout error"
}
```

##### Response 500

500 Example `example`:

```json
{
  "code": "EUPI0001",
  "message": "An unexpected error happened"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 200 | `EUPI0120` | Transfer amount is greater than the account available limits |
| 403 | `EUPI0004` | Missing required header 'x-tenant' |
| 404 | `EUPI0103` | Transaction not found |
| 408 | `EUPI0020` | Upi - API returned a timeout error |
| 500 | `EUPI0001` | An unexpected error happened |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;403;404;408;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_RuPay_on_UPI.yaml method=POST path=/v1/cards/balance operationId=post-balance-enquiry -->
### `POST /v1/cards/balance` — Get balance for account

- **operationId:** `post-balance-enquiry`
- **Specification:** `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` (Instant payments - RuPay on UPI)
- **Server base URL(s):** `https://sandbox.pismolabs.io/upi-gateway`
- **Tags:** `UPI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Balance inquiry

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token. Tokens can expire quickly, which can result in a **401 Unauthorized** message. | example: "Bearer eyJhbGci...IUzUx" |
| `user-agent` | header | yes | string | Client consuming API. |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `cards.BalanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_reference_number` | string (schema `accountReferenceNumber`) | yes | <br>Account reference number. Pismo creates this automatically when creating a card linked to RuPay on UPI.<br><br>This number combines 10 BIN digits and the credit account number. If BIN is 6 digits, the remaining 4 digits  are set to zero (`0`). If BIN is 8 digits, then the remaining 2 digits are set to zero. This is a [NPCI](https://www.npci.org.in/what-we-do/rupay/product-overview) standard. For example, if the account reference number = `1234560000987654321`, the first six digits are the BIN, appended with 4 zeros and then the credit account number (`987654321``).<br><br>You can call [List cards](ref:post-list-cards) to get a card's account reference number.<br> | example: "12345600000000001140340134" |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | yes | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | yes | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `cards.BalanceResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 422 | UnprocessableEntity | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card` | object | yes | Card balance |  |
| `card.available_balance` | number | yes | Available card balance | example: 150000 |
| `card.ledger_balance` | number | yes | Ledger balance | example: 1000 |
| `account_reference_number` | string (schema `accountReferenceNumber`) | no | <br>Account reference number. Pismo creates this automatically when creating a card linked to RuPay on UPI.<br><br>This number combines 10 BIN digits and the credit account number. If BIN is 6 digits, the remaining 4 digits  are set to zero (`0`). If BIN is 8 digits, then the remaining 2 digits are set to zero. This is a [NPCI](https://www.npci.org.in/what-we-do/rupay/product-overview) standard. For example, if the account reference number = `1234560000987654321`, the first six digits are the BIN, appended with 4 zeros and then the credit account number (`987654321``).<br><br>You can call [List cards](ref:post-list-cards) to get a card's account reference number.<br> | example: "12345600000000001140340134" |
| `external_transaction_datetime` | string (schema `externalTransactionDatetime`) | no | Request datetime. ISO 8601 format. | example: "2020-09-15T19:39:54.013Z" |
| `external_transaction_id` | string (schema `externalTransactionID`) | no | Request ID code | example: "MGS584A1244F6BC4D50A3FABE6D93DF913C" |

##### Response 400

400 Example `EUPI0003` (Bad Request):

```json
{
  "code": "EUPI0003",
  "message": "Bad Request"
}
```

400 Example `EUPI0002` (Validation error):

```json
{
  "code": "EUPI0002",
  "message": "Validation error"
}
```

##### Response 403

403 Example `EUPI0004` (Missing required header 'x-tenant'):

```json
{
  "code": "EUPI0004",
  "message": "Missing required header 'x-tenant'"
}
```

##### Response 404

404 Example `EUPI0028` (Cards not found.):

```json
{
  "code": "EUPI0028",
  "message": "Cards not found."
}
```

404 Example `EUPI0031` (An unexpected error has occurred while fetching Ledger information.):

```json
{
  "code": "EUPI0031",
  "message": "An unexpected error has occurred while fetching Ledger information."
}
```

404 Example `EUPI0032` (Not found.):

```json
{
  "code": "EUPI0032",
  "message": "Not found."
}
```

404 Example `EUPI0007` (Account not foundd.):

```json
{
  "code": "EUPI0007",
  "message": "Account not found."
}
```

##### Response 422

422 Example `EUPI0004` (An unexpected error has occurred):

```json
{
  "code": "EUPI0042",
  "message": "An unexpected error has occurred"
}
```

##### Response 500

500 Example `EUPI0001` (An unexpected error happened):

```json
{
  "code": "EUPI0001",
  "message": "An unexpected error happened"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EUPI0003` | Bad Request |
| 400 | `EUPI0002` | Validation error |
| 403 | `EUPI0004` | Missing required header 'x-tenant' |
| 404 | `EUPI0028` | Cards not found. |
| 404 | `EUPI0031` | An unexpected error has occurred while fetching Ledger information. |
| 404 | `EUPI0032` | Not found. |
| 404 | `EUPI0007` | Account not found. |
| 422 | `EUPI0042` | An unexpected error has occurred |
| 500 | `EUPI0001` | An unexpected error happened |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_RuPay_on_UPI.yaml method=POST path=/v1/cards/credit-card-bill operationId=post-card-bill -->
### `POST /v1/cards/credit-card-bill` — Get card bill

- **operationId:** `post-card-bill`
- **Specification:** `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` (Instant payments - RuPay on UPI)
- **Server base URL(s):** `https://sandbox.pismolabs.io/upi-gateway`
- **Tags:** `UPI`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Return card bill details

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Authorization token. Tokens can expire quickly, which can result in a **401 Unauthorized** message. | example: "Bearer eyJhbGci...IUzUx" |
| `user-agent` | header | yes | string | Client consuming API. |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `cards.CardBillRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_info` | object (schema `card_info`) | yes | Card information | example: {"account_reference_number": "789012000087442038", "last_4_digit": "2432"} |
| `phone` | object (schema `phone`) | yes |  | example: {"country_code": "91", "phone": "9592714958"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `cards.CardBillResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 422 | UnprocessableEntity | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `total_due_amount` | number | yes | Total due amount | example: 500 |
| `minimum_due_amount` | number | yes | Minimum due amount | example: 500 |
| `due_date` | string | yes | Bill due date | example: "23012025" |
| `card_masked_number` | string | yes | Card masked number | example: "123456XXXXXXXX78" |
| `account_reference_number` | string | yes | Card account reference number | example: "789012000087442038" |

##### Response 400

400 Example `EUPI0003` (Bad Request):

```json
{
  "code": "EUPI0003",
  "message": "Bad Request"
}
```

400 Example `EUPI0023` (number is a required field):

```json
{
  "code": "EUPI0023",
  "message": "number is a required field"
}
```

400 Example `EUPI0002` (Validation error):

```json
{
  "code": "EUPI0002",
  "message": "Validation error"
}
```

##### Response 403

403 Example `EUPI0004` (Missing required header 'x-tenant'):

```json
{
  "code": "EUPI0004",
  "message": "Missing required header 'x-tenant'"
}
```

##### Response 404

404 Example `EUPI0028` (Cards not found.):

```json
{
  "code": "EUPI0028",
  "message": "Cards not found."
}
```

404 Example `EUPI0032` (Not found.):

```json
{
  "code": "EUPI0032",
  "message": "Not found."
}
```

404 Example `EUPI0007` (Account not found.):

```json
{
  "code": "EUPI0007",
  "message": "Account not found."
}
```

##### Response 422

422 Example `EUPI0004` (An unexpected error has occurred):

```json
{
  "code": "EUPI0042",
  "message": "An unexpected error has occurred"
}
```

##### Response 500

500 Example `EUPI0001` (An unexpected error happened):

```json
{
  "code": "EUPI0001",
  "message": "An unexpected error happened"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EUPI0003` | Bad Request |
| 400 | `EUPI0023` | number is a required field |
| 400 | `EUPI0002` | Validation error |
| 403 | `EUPI0004` | Missing required header 'x-tenant' |
| 404 | `EUPI0028` | Cards not found. |
| 404 | `EUPI0032` | Not found. |
| 404 | `EUPI0007` | Account not found. |
| 422 | `EUPI0042` | An unexpected error has occurred |
| 500 | `EUPI0001` | An unexpected error happened |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-united-payments-interface`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/phone -->
### Schema `phone`

Pointer: `#/components/schemas/phone`. Type: object (schema `phone`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `country_code` | string | yes | Phone number country code | example: "55" |
| `phone` | string | yes | Phone number | example: "999167803" |
| `area_code` | string | no | Phone number area code | example: "47" |

<!-- schema: #/components/schemas/cards.CardsData -->
### Schema `cards.CardsData`

Pointer: `#/components/schemas/cards.CardsData`. Type: object (schema `cards.CardsData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_reference_number` | string (schema `accountReferenceNumber`) | yes | <br>Account reference number. Pismo creates this automatically when creating a card linked to RuPay on UPI.<br><br>This number combines 10 BIN digits and the credit account number. If BIN is 6 digits, the remaining 4 digits  are set to zero (`0`). If BIN is 8 digits, then the remaining 2 digits are set to zero. This is a [NPCI](https://www.npci.org.in/what-we-do/rupay/product-overview) standard. For example, if the account reference number = `1234560000987654321`, the first six digits are the BIN, appended with 4 zeros and then the credit account number (`987654321``).<br><br>You can call [List cards](ref:post-list-cards) to get a card's account reference number.<br> | example: "12345600000000001140340134" |
| `bin` | string | yes | Card Bank Identification Number (BIN) | example: "123456" |
| `masked_number` | string | yes | Card masked number | example: "123456XXXXXXXX78" |
| `printed_name` | string | yes | Card printed name | example: "Nan Tucket" |
| `status` | string | yes | Card status. For more information, see [Card lifecycle and statuses](https://developers.pismo.io/pismo-docs/docs/card-lifecycle-and-statuses). | example: "ACTIVE" |
| `type` | string (schema `cardType`) | yes | Pismo card type. For more information, see [Cards management](https://developers.pismo.io/pismo-docs/docs/cards-overview-1#card-types). Default is empty string, meaning all card types are returned. | enum: ["", "PLASTIC", "VIRTUAL", "TEMPORARY"]; example: "PLASTIC" |

<!-- schema: #/components/schemas/domain.Error -->
### Schema `domain.Error`

Pointer: `#/components/schemas/domain.Error`. Type: object (schema `domain.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code | example: "EPT0001" |
| `details` | object | no | Detailed error message |  |
| `details.external` | array of object (schema `domain.ExternalMessage`) | no |  |  |
| `details.parameters` | array of object (schema `domain.ParameterMessage`) | no |  |  |
| `details.payload` | array of object (schema `domain.PayloadMessage`) | no |  |  |
| `message` | string | no | Error message | example: "User not found" |

<!-- schema: #/components/schemas/merchant -->
### Schema `merchant`

Pointer: `#/components/schemas/merchant`. Type: object (schema `merchant`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `mid` | string | no | Merchant ID number | example: "HDFC000018966129" |
| `tid` | string | no | Terminal ID | example: "42284754" |
| `sid` | string | no | Service ID - payment network (like NPCI) assigned unique code to a merchant or service provider. | example: "18994373" |

<!-- schema: #/components/schemas/forecloseData -->
### Schema `forecloseData`

Pointer: `#/components/schemas/forecloseData`. Type: object (schema `forecloseData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contract_amount` | number | yes | Total installment amount after calculation and addition of any necessary fees | example: 122.98 |

<!-- schema: #/components/schemas/emiData -->
### Schema `emiData`

Pointer: `#/components/schemas/emiData`. Type: object (schema `emiData`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contract_amount` | number | yes | Total installment amount calculation and addition of any necessary fees | example: 122.98 |
| `principal_amount` | number | yes | Total installment amount after calculation without the addition of any fees | example: 100.98 |
| `number_of_installments` | number | yes | Number of installments in this calculation | example: 3 |
| `fees` | array of object (schema `amountAndRateEntity`) | no | All applied fees on this calculation |  |
| `taxes` | array of object (schema `amountAndRateEntity`) | no | All applied taxes on this calculation |  |
| `interests` | array of object (schema `amountAndRateEntity`) | no | All applied taxes on this calculation |  |
| `installments` | array of object (schema `installment`) | yes | Installments applied |  |

<!-- schema: #/components/schemas/reason -->
### Schema `reason`

Pointer: `#/components/schemas/reason`. Type: object (schema `reason`).

> Reason

Composition: includes the fields of schema `cards.Error` (allOf).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Error code | example: "EUPI0001" |
| `message` | string | yes | Error message | example: "An unexpected error happened" |

<!-- schema: #/components/schemas/card_info -->
### Schema `card_info`

Pointer: `#/components/schemas/card_info`. Type: object (schema `card_info`).

> Card information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_reference_number` | string | no | Card account reference number. Either this field or `last_4_digits` is **REQUIRED**. | example: "789012000087442038" |
| `last_4_digit` | string | no | Card last 4 PAN digits. Either this field or `account_reference_number` is **REQUIRED**. | example: "2432" |

<!-- schema: #/components/schemas/domain.ExternalMessage -->
### Schema `domain.ExternalMessage`

Pointer: `#/components/schemas/domain.ExternalMessage`. Type: object (schema `domain.ExternalMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Code | example: "PBE315" |
| `message` | string | yes | Message | example: "Generic error" |

<!-- schema: #/components/schemas/domain.ParameterMessage -->
### Schema `domain.ParameterMessage`

Pointer: `#/components/schemas/domain.ParameterMessage`. Type: object (schema `domain.ParameterMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Field | example: "Query parameter" |
| `message` | string | yes | Message | example: "Generic error" |

<!-- schema: #/components/schemas/domain.PayloadMessage -->
### Schema `domain.PayloadMessage`

Pointer: `#/components/schemas/domain.PayloadMessage`. Type: object (schema `domain.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Field | example: "Entity.field" |
| `message` | string | yes | Error message | example: "Generic error" |

<!-- schema: #/components/schemas/amountAndRateEntity -->
### Schema `amountAndRateEntity`

Pointer: `#/components/schemas/amountAndRateEntity`. Type: object (schema `amountAndRateEntity`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | no | Entity type |  |
| `amount` | number | no | Entity applied amount | example: 20.98 |
| `rate` | number | no | Percentage rate used for calculating | example: 5.9 |

<!-- schema: #/components/schemas/installment -->
### Schema `installment`

Pointer: `#/components/schemas/installment`. Type: object (schema `installment`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contract_amount` | number | yes | Total installment amount after calculation and addition of any necessary fees | example: 122.98 |
| `principal_amount` | number | yes | Total installment amount after calculation without the addition of any fees | example: 100.98 |
| `number_of_installments` | number | yes | Number of installments in this calculation | example: 3 |
| `fees` | array of object (schema `amountAndRateEntity`) | no | Applied fees in this calculation |  |
| `taxes` | array of object (schema `amountAndRateEntity`) | no | Applied taxes in this calculation |  |
| `interests` | array of object (schema `amountAndRateEntity`) | no | Applied interests in this calculation |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_RuPay_on_UPI.yaml` | tag `UPI`: POST /v1/cards/list, POST /v1/cards/validate, POST /v1/cards/transfer, POST /v1/cards/emi-select, GET /v1/transactions/inquiry/account-reference-number/{account_reference_number}/external-transaction-id/{external_transaction_id}, POST /v1/cards/balance, POST /v1/cards/credit-card-bill | https://github.com/PismoDevEx/pismo-api-specs | `5f264e17cce9a121…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-eupi` — Error codes: EUPI
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-united-payments-interface` — RuPay and UPI instant payments (India)
