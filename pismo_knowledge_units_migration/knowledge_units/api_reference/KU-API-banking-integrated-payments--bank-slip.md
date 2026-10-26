---
ku_id: KU-API-banking-integrated-payments--bank-slip
title: 'API reference: Banking - Integrated payments — Bank slip'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Integrated_payments.yaml
  sha256: 8696ddecc6a5182f219956d7bbba779e4dfa8c9d4b356ef282e9e96c407d1716
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
- post-integrated-payments-api-v1-bankslips-pay
- post-integrated-payments-api-v1-bankslips-validate
- get-integrated-payments-api-v1-bankslips-receipts
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-banking-as-a-service
- KU-BANK-banking-overview
- KU-ERR-codes-eip
- KU-EVT-bank-slips-data-events
- KU-EVT-catalogue-integrated
- KU-EVT-catalogue-other-domains
- KU-EVT-client-webhooks-part-01
- KU-PAY-bank-slips
specification_version: '1.0'
---

# API reference: Banking - Integrated payments — Bank slip

**KU ID:** `KU-API-banking-integrated-payments--bank-slip` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Bank slip` in `api-specs/Banking_-_Integrated_payments.yaml` (“Banking - Integrated payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Operations related to pay and get information about a bank slips

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/bankslips/pay` | `post-integrated-payments-api-v1-bankslips-pay` | Pay bank slip | no |
| `POST /v1/bankslips/validate` | `post-integrated-payments-api-v1-bankslips-validate` | Validate bank slip | no |
| `GET /v1/bankslips/receipts` | `get-integrated-payments-api-v1-bankslips-receipts` | List bank slip receipt | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=POST path=/v1/bankslips/pay operationId=post-integrated-payments-api-v1-bankslips-pay -->
### `POST /v1/bankslips/pay` — Pay bank slip

- **operationId:** `post-integrated-payments-api-v1-bankslips-pay`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Bank slip`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> In Brazil, bank slips, known as *Boleto Bancarios* or simply *Boletos* in Portuguese, are a popular payment method for various services, bills, and purchases. When a payment needs to be made, the recipient (such as a business or service provider) generates a Boleto with the necessary payment details, such as the recipent's information, the payment amount, due date, barcode, and other relevant information.
> Pismo works with [BTG Pactual](https://www.btgpactual.us), [Celcoin](https://celcoin.com.br), and [Itaú](https://www.itau.com.br) to implement Boleto payments. In the future, Pismo may work with additional financial companies.
> This endpoint generates the following events:
> * [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) - This event contains bank slip information (beneficiary name and document number, digitable line, amount, payment date, interest/fine and discount (if any) in the `metadata` field.
> * [Financial bank slip status changed](https://developers.pismo.io/events/docs/integrated-payments-bankslip-status-change-1) - Before clearing, a bank slip's status is `PAID`. After clearing, Pismo changes its status to `SETTLED`.
> * [Integrated payments financial reconciliation](https://developers.pismo.io/events/docs/integrated-payments-financial-reconciliation-1)- This event is generated after the transaction has been cleared and accounts debited or credited. If `x-skip-reconciliation` is `true` or the provider is JD Consultores, this event is not generated.<br>
> See [Bank slips](doc:bank-slips) for more information.<br>
> **Important**: You need to call [Validate bank slip](ref:post-integrated-payments-api-v1-bankslips-validate) before calling this endpoint and pass the `external_authorization` field value if it is returned from that call here.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token. Getting an account token requires you call the [Server login<br>endpoint](ref:post-passport-v2-s2s-access-token) with an account ID. Tokens can expire<br>quickly, which can result in an <b>Unauthorized</b> message. Enter this field under<br>`AUTHENTICATION`.<br> | example: "<account_token>" |
| `x-idempotency-key` | header | yes | string | Unique identifier (UUID) to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "6a17f82d-7365-4451-a83d-09403f05c1ec" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `bankslips.bankslipsPayRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | yes | Pismo Platform Account ID. | example: 7989342 |
| `amount` | number | yes | Amount to pay. | example: 100 |
| `bankslip` | object | no | Bank slip information |  |
| `bankslip.type` | integer | yes | bank slip type. (`1` = compensation form, `2` = dealership).<br><br>Compensation form refers to the method for processing the bank slip. Dealership (cedente) refers to the entity or individual that issues the bank slip.<br> | enum: [1, 2]; example: 1 |
| `bankslip.bar_code` | string | no | Bar code encoding bank slip information such as the bank code, currency code, check digit, due date, amount, and beneficiary information.<br> | example: "22323423423423423" |
| `bankslip.digitable_line` | string | no | Digitable line. On a Brazilian bank slip, the digitable line contains numerical payment information encoding details like the payment amount, due date, beneficiary information, and other transaction-specific data. | example: "23792374039002121400385000334004688970000050227" |
| `bankslip.due_datetime` | string | no | Due datetime. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. | format: "date-time"; example: "2022-08-15T00:00:00.000Z" |
| `bankslip.original_amount` | number | no | Original amount. | example: 100 |
| `currency_code` | string | no | ISO 4217 currency code. Can be either numeric or alphabetic. | example: "BRL" |
| `external_authorization` | string | no | External authorization. Some providers return this value<br>to the `/v1/bankslips/validate` endpoint. If returned, this value must<br>be passed on to a bank slip payment request.<br>Some providers return this to a [Validate bank slip](ref:post-integrated-payments-api-v1-bankslips-validate) call. If returned, you **must** pass it in a [Pay bank slip](ref:post-integrated-payments-api-v1-bankslips-pay) endpoint call.<br> | example: "123456" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `bankslips.bankslipsPayResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `domain.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Pismo Platform Account ID. | example: 12434 |
| `amount` | number | no | Amount paid. | example: 100 |
| `authorization_id` | integer | no | Pismo Platform Account ID. | example: 12434 |
| `bar_code` | string | no | Bar code encoding bank slip information such as the bank code, currency code, check digit, due date, amount, and beneficiary information.<br> | example: "22323423423423423" |
| `currency_code` | string | no | ISO 4217 currency code. Can be either numeric or alphabetic. | example: "BRL" |
| `customer_name` | string | no | Customer name. | example: "Customer Name" |
| `digitable_line` | string | no | Digitable line. On a Brazilian bank slip, the digitable line contains numerical payment information encoding details like the payment amount, due date, beneficiary information, and other transaction-specific data. | example: "23792374039002121400385000334004688970000050227" |
| `due_datetime` | string | no | Due datetime. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. | format: "date-time"; example: "2021-05-25T00:00:00.000Z" |
| `external_id` | string | no | Client-generated ID for client tracking and monitoring. | example: "12434" |
| `payment_datetime` | string | no | Payment datetime. | format: "date-time"; example: "2021-05-25T00:00:00.000Z" |
| `status` | string | no | Bank slip status. Possible values are `PAID`, `PROCESSING`, `SETTLED`, `ERROR`, and `TIMEOUT`.<br> | example: "PROCESSING" |
| `additional_info` | string | no | Additional information about the bank slip payment, including provider-specific details.<br> | example: "NumCtrl = 123456" |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIP0005` (Missing header):

```json
{
  "code": "EIP0005",
  "message": "Missing required header {x-tenant}"
}
```

400 Example `EIP0006` (Missing header):

```json
{
  "code": "EIP0006",
  "message": "Missing account-id header {x-account-id}"
}
```

400 Example `EIP0008` (Validation error):

```json
{
  "code": "EIP0008",
  "message": "Validation error"
}
```

400 Example `EIP0010` (Unmarshal error):

```json
{
  "code": "EIP0010",
  "message": "Unmarshal error"
}
```

400 Example `EIP0012` (Account not found):

```json
{
  "code": "EIP0012",
  "message": "Account not found"
}
```

400 Example `EIP0013` (Accounts - API returned 4xx error):

```json
{
  "code": "EIP0013",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EIP0017` (IntlBankAccounts - API returned 4xx error):

```json
{
  "code": "EIP0017",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EIP0023` (Banking gateway API error):

```json
{
  "code": "EIP0023",
  "message": "BankingGatewayAPI - API returned 4xx error"
}
```

400 Example `EIP0020` (P2P API returned 4xx error):

```json
{
  "code": "EIP0020",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EIP0061` (Invalid bill for payment):

```json
{
  "code": "EIP0061",
  "message": "BankingGatewayAPI - Invalid bill for payment"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIP0005` (Missing header):

```json
{
  "code": "EIP0005",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIP0006` (Invalid account ID header):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EIP0009` (Missing idempotency key header):

```json
{
  "code": "EIP0009",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EIP0030` (Account ID mismatch):

```json
{
  "code": "EIP0030",
  "message": "Entity's account id does not match x-account-id header"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIP0049` (Convert barcode to digitable line failure):

```json
{
  "code": "EIP0049",
  "message": "Convert barcode to digitable line failed"
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `EIP0063` (Bankslip already processing or paid):

```json
{
  "code": "EIP0063",
  "message": "Bankslips is already in processing or paid"
}
```

409 Example `EIP0065` (Provider conflict error):

```json
{
  "code": "EIP0065",
  "message": "BankingGatewayAPI - API returned 409 provider error"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIP0004` (HTTP request error):

```json
{
  "code": "EIP0004",
  "message": "HTTP request error"
}
```

500 Example `EIP0007` (Internal error):

```json
{
  "code": "EIP0007",
  "message": "Internal error"
}
```

500 Example `EIP0011` (Accounts API timeout error):

```json
{
  "code": "EIP0011",
  "message": "Accounts API timeout error"
}
```

500 Example `EIP0015` (IntlBankAccounts API timeout error):

```json
{
  "code": "EIP0015",
  "message": "IntlBankAccounts - API timeout error"
}
```

500 Example `EIP0019` (P2P API timeout error):

```json
{
  "code": "EIP0019",
  "message": "P2p - API timeout error"
}
```

500 Example `EIP0022` (BankingGatewayAPI API timeout error):

```json
{
  "code": "EIP0022",
  "message": "BankingGatewayAPI - API timeout error"
}
```

500 Example `EIP0028` (Transaction database error):

```json
{
  "code": "EIP0028",
  "message": "Transaction database error"
}
```

500 Example `EIP0041` (Bank slip database error):

```json
{
  "code": "EIP0041",
  "message": "Bankslips database error"
}
```

500 Example `EIP0051` (Schedule conciliation error):

```json
{
  "code": "EIP0051",
  "message": "Schedule conciliation error"
}
```

500 Example `EIP0053` (Send integrity message error):

```json
{
  "code": "EIP0053",
  "message": "Send integrity message error"
}
```

500 Example `EIP0069` (P2P API - Failure to unmarshal error):

```json
{
  "code": "EIP0069",
  "message": "P2P API - Failed to unmarshal error response body"
}
```

500 Example `EIP0070` (BankingGateway API - Failed to unmarshal error response):

```json
{
  "code": "EIP0070",
  "message": "BankingGateway API - Failed to unmarshal error response body"
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `EIP0018` (IntlBankAccounts - API returned 5xx error):

```json
{
  "code": "EIP0018",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

502 Example `EIP0021` (P2P API returned 5xx error):

```json
{
  "code": "EIP0021",
  "message": "P2p - API returned 5xx error"
}
```

502 Example `EIP0024` (Bad Gateway):

```json
{
  "code": "EIP0024",
  "message": "BankingGatewayAPI - API returned 5xx error"
}
```

##### Response 504

- Response header `x-cid`: Request tracking identifier. (string)
504 Example `EIP0002` (Gateway Timeout):

```json
{
  "code": "EIP0002",
  "message": "API request timeout"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIP0005` | Missing required header {x-tenant} |
| 400 | `EIP0006` | Missing account-id header {x-account-id} |
| 400 | `EIP0008` | Validation error |
| 400 | `EIP0010` | Unmarshal error |
| 400 | `EIP0012` | Account not found |
| 400 | `EIP0013` | Accounts - API returned 4xx error |
| 400 | `EIP0017` | IntlBankAccounts - API returned 4xx error |
| 400 | `EIP0023` | BankingGatewayAPI - API returned 4xx error |
| 400 | `EIP0020` | P2p - API returned 4xx error |
| 400 | `EIP0061` | BankingGatewayAPI - Invalid bill for payment |
| 403 | `EIP0005` | Missing required header: 'x-tenant' |
| 403 | `EIP0006` | Invalid account id header: 'x-account-id' |
| 403 | `EIP0009` | Missing required header: 'x-idempotency-key' |
| 403 | `EIP0030` | Entity's account id does not match x-account-id header |
| 404 | `EIP0049` | Convert barcode to digitable line failed |
| 409 | `EIP0063` | Bankslips is already in processing or paid |
| 409 | `EIP0065` | BankingGatewayAPI - API returned 409 provider error |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0011` | Accounts API timeout error |
| 500 | `EIP0015` | IntlBankAccounts - API timeout error |
| 500 | `EIP0019` | P2p - API timeout error |
| 500 | `EIP0022` | BankingGatewayAPI - API timeout error |
| 500 | `EIP0028` | Transaction database error |
| 500 | `EIP0041` | Bankslips database error |
| 500 | `EIP0051` | Schedule conciliation error |
| 500 | `EIP0053` | Send integrity message error |
| 500 | `EIP0069` | P2P API - Failed to unmarshal error response body |
| 500 | `EIP0070` | BankingGateway API - Failed to unmarshal error response body |
| 502 | `EIP0018` | IntlBankAccounts - API returned 5xx error |
| 502 | `EIP0021` | P2p - API returned 5xx error |
| 502 | `EIP0024` | BankingGatewayAPI - API returned 5xx error |
| 504 | `EIP0002` | API request timeout |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `authorization-authorization-event-1` | https://developers.pismo.io/events/docs/authorization-authorization-event-1 |
| `integrated-payments-bankslip-status-change-1` | https://developers.pismo.io/events/docs/integrated-payments-bankslip-status-change-1 |
| `integrated-payments-financial-reconciliation-1` | https://developers.pismo.io/events/docs/integrated-payments-financial-reconciliation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;404;409;500;502;504`, has examples `True`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-banking-as-a-service`, `KU-BANK-banking-overview`, `KU-EVT-bank-slips-data-events`, `KU-EVT-client-webhooks-part-01`, `KU-PAY-bank-slips`.

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=POST path=/v1/bankslips/validate operationId=post-integrated-payments-api-v1-bankslips-validate -->
### `POST /v1/bankslips/validate` — Validate bank slip

- **operationId:** `post-integrated-payments-api-v1-bankslips-validate`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Bank slip`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Validate bank slip with provider partner.<br>
> You need to call this endpoint before calling [Pay bank slip](ref:post-integrated-payments-api-v1-bankslips-pay). If this endpoint returns an `external_authorization` field value, you must pass it in the Pay bank slip call.<br>
> For this endpoint, either `bar_code` or `digitable_line` **must** be passed.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token. Getting an account token requires you call the [Server login<br>endpoint](ref:post-passport-v2-s2s-access-token) with an account ID. Tokens can expire<br>quickly, which can result in an <b>Unauthorized</b> message. Enter this field under<br>`AUTHENTICATION`.<br> | example: "<account_token>" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `bankslips.bankslipsValidateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | integer | yes | Banslip type. (`1` = compensation form, `2` = dealership)<br><br>Compensation form refers to the method for processing the bank slip. Dealership (cedente) refers to the entity or individual that issues the bank slip.<br> | enum: [1, 2]; example: 1 |
| `bar_code` | string | no | Bar code encoding bank slip information such as the bank code, currency code, check digit, due date, amount, and beneficiary information. | example: "22323423423423423" |
| `digitable_line` | string | no | Digitable line. On a Brazilian bank slip, the digitable line contains numerical payment information encoding details like the payment amount, due date, beneficiary information, and other transaction-specific data. | example: "20890001091000001090980008176705191030000002000" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `bankslips.bankslipsValidateResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 404 | Not Found | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | no | Amount to pay. | example: 10 |
| `assignor` | string | no | The name of the receiver bank. | example: "BANCO ITAU S.A." |
| `bar_code` | string | no | Bar code. | example: "22323423423423423" |
| `beneficiary_document_number` | string | no | A government document number, such as a CPF (Brazil) - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number, CNPJ (Brazil) - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number - unique ID for legal entities, such as companies and organizations.<br> | example: "123456789" |
| `beneficiary_name` | string | no | Beneficiary name. | example: "Beneficiary name" |
| `digitable_line` | string | no | Digitable line. On a Brazilian bank slip, the digitable line contains numerical payment information encoding details like the payment amount, due date, beneficiary information, and other transaction-specific data. | example: "34192374039002121400385000334004688970000050227" |
| `discount_value` | number | no | Discount value. | example: 0 |
| `due_date` | string | no | Due datetime. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. | format: "datetime"; example: "2022-08-15T00:00:00.000Z" |
| `external_authorization` | string | no | Some providers return this to a [Validate bank slip](ref:post-integrated-payments-api-v1-bankslips-validate) call. If returned, you must pass it in a Pay bank slip](ref:post-integrated-payments-api-v1-bankslips-pay) endpoint call.<br>If returned, this value must be passed on to a bank slip payment request.<br> | example: "123" |
| `fine_value` | number | no | Fine value. | example: 0 |
| `interest_value` | number | no | Interest value. | example: 0 |
| `limit_date` | string | no | Limit datetime to pay. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. | format: "date"; example: "2022-08-15T00:00:00.000Z" |
| `max_value` | number | no | Maximum value. | example: 10 |
| `min_value` | number | no | Minimum value. | example: 10 |
| `original_value` | number | no | Original value. | example: 10 |
| `payer_document_number` | string | no | A government document number, such as a CPF (Brazil) - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number, CNPJ (Brazil) - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number - unique ID for legal entities, such as companies and organizations. | example: "923456789" |
| `payer_name` | string | no | Payer's name. | example: "Payer's name" |
| `settle_date` | string | no | Settlement date. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. | format: "date"; example: "2022-08-15T00:00:00.000Z" |
| `type` | integer | no | bank slip type. (`1` = compensation form, `2` = dealership).<br><br>Compensation form refers to the method for processing the bank slip. Dealership (cedente) refers to the entity or individual that issues the bank slip.<br> | example: 1 |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIP0008` (Validation error):

```json
{
  "code": "EIP0008",
  "message": "Validation error"
}
```

400 Example `EIP0010` (Unmarshal error):

```json
{
  "code": "EIP0010",
  "message": "Unmarshal error"
}
```

400 Example `EIP0023` (Banking gateway API error):

```json
{
  "code": "EIP0023",
  "message": "BankingGatewayAPI - API returned 4xx error"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIP0005` (Missing header):

```json
{
  "code": "EIP0005",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIP0006` (Invalid account ID header):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header: 'x-account-id'"
}
```

##### Response 404

- Response header `x-cid`: Request tracking identifier. (string)
404 Example `EIP0049` (Convert barcode to digitable line failure):

```json
{
  "code": "EIP0049",
  "message": "Convert barcode to digitable line failed"
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `EIP0065` (BankingGatewayAPI - Provider error):

```json
{
  "code": "EIP0065",
  "message": "BankingGatewayAPI - API returned 409 provider error"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIP0004` (HTTP request error):

```json
{
  "code": "EIP0004",
  "message": "HTTP request error"
}
```

500 Example `EIP0007` (Internal error):

```json
{
  "code": "EIP0007",
  "message": "Internal error"
}
```

500 Example `EIP0022` (BankingGatewayAPI API timeout error):

```json
{
  "code": "EIP0022",
  "message": "BankingGatewayAPI - API timeout error"
}
```

500 Example `EIP0070` (BankingGateway API - Failed to unmarshal error response):

```json
{
  "code": "EIP0070",
  "message": "BankingGateway API - Failed to unmarshal error response body"
}
```

##### Response 502

- Response header `x-cid`: Request tracking identifier. (string)
502 Example `EIP0024` (BankingGatewayAPI - API returned 5xx error):

```json
{
  "code": "EIP0024",
  "message": "BankingGatewayAPI - API returned 5xx error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIP0008` | Validation error |
| 400 | `EIP0010` | Unmarshal error |
| 400 | `EIP0023` | BankingGatewayAPI - API returned 4xx error |
| 403 | `EIP0005` | Missing required header: 'x-tenant' |
| 403 | `EIP0006` | Invalid account id header: 'x-account-id' |
| 404 | `EIP0049` | Convert barcode to digitable line failed |
| 409 | `EIP0065` | BankingGatewayAPI - API returned 409 provider error |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0022` | BankingGatewayAPI - API timeout error |
| 500 | `EIP0070` | BankingGateway API - Failed to unmarshal error response body |
| 502 | `EIP0024` | BankingGatewayAPI - API returned 5xx error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;500;502`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-PAY-bank-slips`.

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=GET path=/v1/bankslips/receipts operationId=get-integrated-payments-api-v1-bankslips-receipts -->
### `GET /v1/bankslips/receipts` — List bank slip receipt

- **operationId:** `get-integrated-payments-api-v1-bankslips-receipts`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Bank slip`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve bank slip payment receipts with filtering options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `lastEvaluatedPaymentDatetimeQuery` | query | no | string | Last payment datetime evaluated. This is the last_evaluated_payment_datetime field returned in the response and is used to find and return additional results. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`.<br> | format: "datetime"; example: "2024-09-11T18:01:44Z" |
| `authorizationId` | query | no | string | Authorization ID filter used for searching fund transfers. | example: "1234" |
| `perPage` | query | no | string | Receipts per page. Min=1, max=100, default=20. | default: "20"; minLength: 1; maxLength: 100; example: "100" |
| `order` | query | no | string | Result ordering is done on bank slip creation datetime. Default is `desc`. | enum: ["asc", "desc"]; example: "desc" |
| `beginDatetime` | query | no | string | Begin datetime filter. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`.<br> | format: "datetime"; example: "2024-09-11T18:01:44Z" |
| `endDatetime` | query | no | string | End datetime filter. ISO 8601 format - `syyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`.<br> | format: "datetime"; example: "2024-09-11T18:01:44.000Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `bankslips.GetbankslipsReceiptsResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `begin_datetime` | string | no | Begin datetime. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. | format: "date-time" |
| `end_datetime` | string | no | End datetime. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. | format: "date-time" |
| `items` | array of object (schema `bankslips.bankslipReceipt`) | no |  |  |
| `last_evaluated_payment_datetime` | string | no | Last evaluated payment datetime. | format: "date-time" |
| `per_page` | integer | no | Number of results per page. | example: 10 |
| `total_items` | integer | no | Total items matching the filtering criteria. | example: 100 |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIP0010` (Unmarshal error):

```json
{
  "code": "EIP0010",
  "message": "Unmarshal error"
}
```

400 Example `EIP0012` (Account not found):

```json
{
  "code": "EIP0012",
  "message": "Account not found"
}
```

400 Example `EIP0013` (Accounts - API returned 4xx error):

```json
{
  "code": "EIP0013",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EIP0045` (Invalid query param):

```json
{
  "code": "EIP0045",
  "message": "Invalid value for query param {value}"
}
```

400 Example `EIP0046` (Invalid datetime query param):

```json
{
  "code": "EIP0046",
  "message": "Invalid value for datetime query parameter. RFC3339 format must be used"
}
```

400 Example `EIP0047` (Invalid query param):

```json
{
  "code": "EIP0047",
  "message": "Invalid value for query param {value}"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIP0005` (Missing header):

```json
{
  "code": "EIP0005",
  "message": "Missing required header {x-tenant}"
}
```

403 Example `EIP0006` (Missing header):

```json
{
  "code": "EIP0006",
  "message": "Missing account-id header {x-account-id}"
}
```

403 Example `EIP0029` (Account blocked or cancelled):

```json
{
  "code": "EIP0029",
  "message": "Account blocked or cancelled"
}
```

##### Response 500

- Response header `x-cid`: Request tracking identifier. (string)
500 Example `EIP0004` (HTTP request error):

```json
{
  "code": "EIP0004",
  "message": "HTTP request error"
}
```

500 Example `EIP0011` (Accounts API timeout error):

```json
{
  "code": "EIP0011",
  "message": "Accounts API timeout error"
}
```

500 Example `EIP0014` (Accounts - API returned 5xx error):

```json
{
  "code": "EIP0014",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIP0041` (Bank slip database error):

```json
{
  "code": "EIP0041",
  "message": "Bank slip database error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIP0010` | Unmarshal error |
| 400 | `EIP0012` | Account not found |
| 400 | `EIP0013` | Accounts - API returned 4xx error |
| 400 | `EIP0045` | Invalid value for query param {value} |
| 400 | `EIP0046` | Invalid value for datetime query parameter. RFC3339 format must be used |
| 400 | `EIP0047` | Invalid value for query param {value} |
| 403 | `EIP0005` | Missing required header {x-tenant} |
| 403 | `EIP0006` | Missing account-id header {x-account-id} |
| 403 | `EIP0029` | Account blocked or cancelled |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0011` | Accounts API timeout error |
| 500 | `EIP0014` | Accounts - API returned 5xx error |
| 500 | `EIP0041` | Bank slip database error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-PAY-bank-slips`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/domain.Error -->
### Schema `domain.Error`

Pointer: `#/components/schemas/domain.Error`. Type: object (schema `domain.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code. | example: "EIP0001" |
| `details` | string | no | Error details. | example: "Error details" |
| `message` | string | no | Error message describing the error. | example: "error" |

<!-- schema: #/components/schemas/bankslips.bankslipReceipt -->
### Schema `bankslips.bankslipReceipt`

Pointer: `#/components/schemas/bankslips.bankslipReceipt`. Type: object (schema `bankslips.bankslipReceipt`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Pismo account ID. |  |
| `amount` | number | no |  |  |
| `authorization_id` | integer | no | Authorization ID. |  |
| `beneficiary_document_number` | string | no | A government document number, such as a CPF (Brazil) - Cadastro de Pessoas Fisicas (Indiviual Taxpayer Registry) number, CNPJ (Brazil) - Cadastro Nacional de Pessoa Juridica (National Registry of Legal Entities) number - unique ID for legal entities, such as companies and organizations.<br> |  |
| `beneficiary_name` | string | no | Beneficiary name. |  |
| `client_request_id` | string | no | Client request ID. |  |
| `currency_code` | string | no | ISO 4217 currency code. Can be either numeric or alphabetic. |  |
| `customer_name` | string | no | Customer name. |  |
| `description` | string | no | Bank slip description. |  |
| `digitable_line` | string | no | Digitable line. |  |
| `discount` | number | no | Discount displayed in percentage granted to this bank slips if paid until the due datetime specified in `due_datetime`. |  |
| `document_number` | string | no | Document number related to the owner of bank slips. |  |
| `due_datetime` | string | no | Due datetime. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`. | format: "date-time" |
| `external_id` | string | no | External provider transaction ID. |  |
| `fine` | number | no | Fine applied to the bank slip amount in case of overdue. |  |
| `interest` | number | no | Interest applied to the bank slip amount when overdue. |  |
| `payment_datetime` | string | no | Date on which payment is made. | format: "date-time" |
| `settlement_partner` | string | no | Settlement partner. |  |
| `status` | string | no | Bank slip status. Possible values are `CREATED`, `REGISTERED`, and `CANCELLED`. |  |
| `additional_info` | string | no | Additional information about the bank slip payment, including provider-specific details.<br> | example: "NumCtrl = 123456" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Integrated_payments.yaml` | tag `Bank slip`: POST /v1/bankslips/pay, POST /v1/bankslips/validate, GET /v1/bankslips/receipts | https://github.com/PismoDevEx/pismo-api-specs | `8696ddecc6a5182f…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-banking-as-a-service` — Banking as a Service
- `KU-BANK-banking-overview` — Banking overview
- `KU-ERR-codes-eip` — Error codes: EIP
- `KU-EVT-bank-slips-data-events` — Banking - Integrated payments
- `KU-EVT-catalogue-integrated` — Event catalogue: integrated
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-PAY-bank-slips` — Bank slips
