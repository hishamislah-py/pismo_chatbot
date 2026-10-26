---
ku_id: KU-API-banking-integrated-payments--transfer
title: 'API reference: Banking - Integrated payments — Transfer'
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
- post-integrated-payments-api-v1-bankslips-cashout
- get-integrated-payments-api-v1-transfers
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-banking-as-a-service
- KU-BANK-banking-overview
- KU-ERR-codes-eip
- KU-EVT-bank-slips-data-events
- KU-EVT-catalogue-integrated
- KU-EVT-client-webhooks-part-01
specification_version: '1.0'
---

# API reference: Banking - Integrated payments — Transfer

**KU ID:** `KU-API-banking-integrated-payments--transfer` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Transfer` in `api-specs/Banking_-_Integrated_payments.yaml` (“Banking - Integrated payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Operations related to transfer cashin and cashout

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/transfers/cashout` | `post-integrated-payments-api-v1-bankslips-cashout` | Perform cash-out | no |
| `GET /v1/transfers` | `get-integrated-payments-api-v1-transfers` | List transfer | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=POST path=/v1/transfers/cashout operationId=post-integrated-payments-api-v1-bankslips-cashout -->
### `POST /v1/transfers/cashout` — Perform cash-out

- **operationId:** `post-integrated-payments-api-v1-bankslips-cashout`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Transfer`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Perform an external transfer, using a provider to process the outgoing account resources.
> This endpoint generates the following events:
> * [Transfer-out created](https://developers.pismo.io/events/docs/integrated-payments-transfer-out-created-1) - Cash-out event.
> * [Financial transaction status updated](https://developers.pismo.io/events/docs/integrated-payments-transaction-status-change-1) - Cash out status change. Status becomes `SETTLED` after clearing and accounts have been credited and debited.
> * [Integrated payments financial reconciliation](https://developers.pismo.io/events/docs/integrated-payments-financial-reconciliation-1)- This event is generated after the transaction has been cleared and accounts debited or credited.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token. Getting an account token requires you call the [Server login<br>endpoint](ref:post-passport-v2-s2s-access-token) with an account ID. Tokens can expire<br>quickly, which can result in an <b>Unauthorized</b> message. Enter this field under<br>`AUTHENTICATION`.<br> | example: "<account_token>" |
| `x-idempotency-key` | header | yes | string | Unique identifier (UUID) to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> | example: "6a17f82d-7365-4451-a83d-09403f05c1ec" |
| `x-skip-reconciliation` | header | no | boolean | If `true`, the reconciliation process is skipped and the Integrated payments financial reconciliation event is not generated. Default is `false`.<br><br>The financial reconciliation process compares the transaction made on Pismo with the same transaction made on the provider side (i.e., BTG or Celcoin).<br> | example: true |
| `X-Signature` | header | no | string | This header is designed for clients working with a third‑party provider that requires certain transactions to include a certified digital signature for added security. It is optional and should be used only if your provider requires signature validation. When included, our APIs forward the header to the provider, which verifies the signature and approves or rejects the transaction based on its authenticity.<br> | example: "5903AB76A8BC52E2CBD04E83042C32F26A23F022;s0k/tU3m+iAvWfrori8+TdhWqUn0jAAKvq/hyNuAEfxSE;20250909" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `transfers.TransfersCashOutRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | yes | Pismo Platform client ID. | example: 415424 |
| `amount` | number | yes | Dot-separated transfer amount in decimals. | example: 101.11 |
| `currency_code` | string | no | ISO 4217 currency code. Can be either numeric or alphabetic. | example: "BRL" |
| `processing_code` | string | yes | Transfer processing code. Used to identify the type of transfer. | example: "876578435" |
| `creditor` | object (schema `transfers.Client`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Response Body | `application/json`: object (schema `transfers.TransfersCashOutResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 409 | Conflict | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `domain.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `domain.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking identifier. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `correlation_id` | string | no | Correlation ID. |  |
| `external_id` | string | no | External ID of the provider. |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIP0003` (Bad Request):

```json
{
  "code": "EIP0003",
  "message": "Bad Request"
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

400 Example `EIP0016` (Account not found):

```json
{
  "code": "EIP0016",
  "message": "IntlBankAccounts - API Account not found"
}
```

400 Example `EIP0017` (IntlBankAccounts - API returned 4xx error):

```json
{
  "code": "EIP0017",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EIP0020` (P2p - API returned 4xx error):

```json
{
  "code": "EIP0020",
  "message": "P2p - API returned 4xx error"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIP0005` (Missing tenant header):

```json
{
  "code": "EIP0005",
  "message": "Missing required header {x-tenant}"
}
```

403 Example `EIP0006` (Invalid account header):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header {x-account-id}"
}
```

403 Example `EIP0009` (Missing idempotency header):

```json
{
  "code": "EIP0009",
  "message": "Missing required header {x-idempotency-key}"
}
```

403 Example `EIP0029` (Account blocked or cancelled):

```json
{
  "code": "EIP0029",
  "message": "Account blocked or cancelled"
}
```

403 Example `EIP0030` (Entity's account id does not match x-account-id header):

```json
{
  "code": "EIP0030",
  "message": "Entity's account id does not match {x-account-id} header"
}
```

##### Response 409

- Response header `x-cid`: Request tracking identifier. (string)
409 Example `EIP0031` (Idempotency header already exists):

```json
{
  "code": "EIP0031",
  "message": "{x-idempotency-key} already exists"
}
```

409 Example `EIP0065` (BankingGatewayAPI Provider Error):

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
  "message": "IntlBankAccounts API timeout error"
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

502 Example `EIP0021` (P2P - API returned 5xx error):

```json
{
  "code": "EIP0021",
  "message": "P2p - API returned 5xx error"
}
```

502 Example `EIP0024` (BankingGatewayAPI - API returned 5xx error):

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
| 400 | `EIP0003` | Bad Request |
| 400 | `EIP0008` | Validation error |
| 400 | `EIP0010` | Unmarshal error |
| 400 | `EIP0012` | Account not found |
| 400 | `EIP0013` | Accounts - API returned 4xx error |
| 400 | `EIP0016` | IntlBankAccounts - API Account not found |
| 400 | `EIP0017` | IntlBankAccounts - API returned 4xx error |
| 400 | `EIP0020` | P2p - API returned 4xx error |
| 403 | `EIP0005` | Missing required header {x-tenant} |
| 403 | `EIP0006` | Invalid account id header {x-account-id} |
| 403 | `EIP0009` | Missing required header {x-idempotency-key} |
| 403 | `EIP0029` | Account blocked or cancelled |
| 403 | `EIP0030` | Entity's account id does not match {x-account-id} header |
| 409 | `EIP0031` | {x-idempotency-key} already exists |
| 409 | `EIP0065` | BankingGatewayAPI - API returned 409 provider error |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0011` | Accounts API timeout error |
| 500 | `EIP0015` | IntlBankAccounts API timeout error |
| 500 | `EIP0019` | P2p - API timeout error |
| 500 | `EIP0022` | BankingGatewayAPI - API timeout error |
| 500 | `EIP0028` | Transaction database error |
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
| `integrated-payments-financial-reconciliation-1` | https://developers.pismo.io/events/docs/integrated-payments-financial-reconciliation-1 |
| `integrated-payments-transaction-status-change-1` | https://developers.pismo.io/events/docs/integrated-payments-transaction-status-change-1 |
| `integrated-payments-transfer-out-created-1` | https://developers.pismo.io/events/docs/integrated-payments-transfer-out-created-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;409;500;502;504`, has examples `True`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-banking-as-a-service`, `KU-BANK-banking-overview`, `KU-EVT-bank-slips-data-events`, `KU-EVT-client-webhooks-part-01`.

<!-- op: spec=api-specs/Banking_-_Integrated_payments.yaml method=GET path=/v1/transfers operationId=get-integrated-payments-api-v1-transfers -->
### `GET /v1/transfers` — List transfer

- **operationId:** `get-integrated-payments-api-v1-transfers`
- **Specification:** `api-specs/Banking_-_Integrated_payments.yaml` (Banking - Integrated payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/integrated-payments`
- **Tags:** `Transfer`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve transfers list.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `lastEvaluatedCreationDatetime` | query | no | string | Last creation datetime filter. Displayed in ISO 8601 format: `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`.<br> | format: "datetime"; example: "2024-09-11T18:01:44Z" |
| `authorizationId` | query | no | string | Authorization ID filter used for searching fund transfers. | example: "1234" |
| `perPage` | query | no | string | Receipts per page. Min=1, max=100, default=20. | default: "20"; minLength: 1; maxLength: 100; example: "100" |
| `order` | query | no | string | Result ordering is done on bank slip creation datetime. Default is `desc`. | enum: ["asc", "desc"]; example: "desc" |
| `beginDatetime` | query | no | string | Begin datetime filter. ISO 8601 format - `yyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`.<br> | format: "datetime"; example: "2024-09-11T18:01:44Z" |
| `endDatetime` | query | no | string | End datetime filter. ISO 8601 format - `syyyy-MM-ddTHH:mm:ss.SSSSSSSSSZ`.<br> | format: "datetime"; example: "2024-09-11T18:01:44.000Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `transaction.GetTransactionsResponse`) |
| 400 | Bad Request | `application/json`: object (schema `domain.Error`) |
| 403 | Forbidden | `application/json`: object (schema `domain.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `domain.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking identifier. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `transaction.GetTransactionsItem`) | no |  |  |
| `pagination` | object (schema `transaction.OffsetPagination`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking identifier. (string)
400 Example `EIP0010` (Unmarshal error):

```json
{
  "code": "EIP0010",
  "message": "Unmarshal error"
}
```

400 Example `EIP0045` (Invalid per_page query param):

```json
{
  "code": "EIP0045",
  "message": "Invalid value for query param 'per_page'"
}
```

400 Example `EIP0046` (Invalid datetime query param):

```json
{
  "code": "EIP0046",
  "message": "Invalid value for datetime query parameter. RFC3339 format must be used"
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

400 Example `EIP0047` (Invalid authorization_id query param):

```json
{
  "code": "EIP0047",
  "message": "Invalid value for query param 'authorization_id'"
}
```

##### Response 403

- Response header `x-cid`: Request tracking identifier. (string)
403 Example `EIP0005` (Missing required header x-tenant):

```json
{
  "code": "EIP0005",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EIP0006` (Invalid account ID header x-account-id):

```json
{
  "code": "EIP0006",
  "message": "Invalid account id header: 'x-account-id'"
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

500 Example `EIP0014` (Accounts - API returned 5xx error):

```json
{
  "code": "EIP0014",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EIP0028` (Transaction database error):

```json
{
  "code": "EIP0028",
  "message": "Transaction database error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIP0010` | Unmarshal error |
| 400 | `EIP0045` | Invalid value for query param 'per_page' |
| 400 | `EIP0046` | Invalid value for datetime query parameter. RFC3339 format must be used |
| 400 | `EIP0012` | Account not found |
| 400 | `EIP0013` | Accounts - API returned 4xx error |
| 400 | `EIP0047` | Invalid value for query param 'authorization_id' |
| 403 | `EIP0005` | Missing required header: 'x-tenant' |
| 403 | `EIP0006` | Invalid account id header: 'x-account-id' |
| 403 | `EIP0029` | Account blocked or cancelled |
| 500 | `EIP0004` | HTTP request error |
| 500 | `EIP0007` | Internal error |
| 500 | `EIP0011` | Accounts API timeout error |
| 500 | `EIP0014` | Accounts - API returned 5xx error |
| 500 | `EIP0028` | Transaction database error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/transfers.Client -->
### Schema `transfers.Client`

Pointer: `#/components/schemas/transfers.Client`. Type: object (schema `transfers.Client`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account` | object (schema `transfers.Account`) | no |  |  |
| `identification` | string | yes | Identification. Document number or another unique identifier. | example: "12345678900" |
| `name` | string | yes | Full name. | example: "John Doe" |
| `type` | string | yes | Type required by provider; for example: F = Legal person.<br> | example: "F" |

<!-- schema: #/components/schemas/domain.Error -->
### Schema `domain.Error`

Pointer: `#/components/schemas/domain.Error`. Type: object (schema `domain.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code. | example: "EIP0001" |
| `details` | string | no | Error details. | example: "Error details" |
| `message` | string | no | Error message describing the error. | example: "error" |

<!-- schema: #/components/schemas/transaction.GetTransactionsItem -->
### Schema `transaction.GetTransactionsItem`

Pointer: `#/components/schemas/transaction.GetTransactionsItem`. Type: object (schema `transaction.GetTransactionsItem`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Pismo Platform Account ID. |  |
| `amount` | number | no | number. |  |
| `authorization_id` | integer | no | Pismo Platform authorization ID. |  |
| `created_at` | string | no | Date on which the resource was created. |  |
| `currency_code` | string | no | ISO 4217 currency code. Can be either numeric or alphabetic. |  |
| `external_party` | object (schema `transaction.Party`) | no |  |  |
| `internal_party` | object (schema `transaction.Party`) | no |  |  |
| `operation` | string | no | Transaction details. |  |
| `status` | string | no | Transaction status. |  |

<!-- schema: #/components/schemas/transaction.OffsetPagination -->
### Schema `transaction.OffsetPagination`

Pointer: `#/components/schemas/transaction.OffsetPagination`. Type: object (schema `transaction.OffsetPagination`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `last_evaluated_creation_datetime` | string | no | Last creation date time. | format: "date-time" |
| `per_page` | integer | no | Number of items returned per page. | example: 10 |
| `total_items` | integer | no | Total number of items in the request based on the filter. | example: 100 |
| `total_pages` | integer | no | Total pages in the request that maches the filter. | example: 10 |

<!-- schema: #/components/schemas/transfers.Account -->
### Schema `transfers.Account`

Pointer: `#/components/schemas/transfers.Account`. Type: object (schema `transfers.Account`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bank` | object (schema `transfers.Bank`) | no |  |  |
| `identification` | string | yes | Account identification. Unique account identifier, for example a bank account number. | example: "98765432" |
| `type` | string | yes | Account type. | example: "CC" |

<!-- schema: #/components/schemas/transaction.Party -->
### Schema `transaction.Party`

Pointer: `#/components/schemas/transaction.Party`. Type: object (schema `transaction.Party`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bank` | string | no | Bank ID. |  |
| `bank_account` | string | no | Bank account. |  |
| `bank_branch` | string | no | Branch name. |  |
| `document_number` | string | no | Document number. |  |
| `name` | string | no | Full name. |  |

<!-- schema: #/components/schemas/transfers.Bank -->
### Schema `transfers.Bank`

Pointer: `#/components/schemas/transfers.Bank`. Type: object (schema `transfers.Bank`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `branch` | string | yes | Bank branch. | example: "0011" |
| `code` | string | yes | Alternative bank identifier, for example, in brazil is COMPE. | example: "30306294" |
| `identification` | string | yes | Bank identification. The main bank identifier, for example, in brazil is ISPB. | example: "30306294" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Integrated_payments.yaml` | tag `Transfer`: POST /v1/transfers/cashout, GET /v1/transfers | https://github.com/PismoDevEx/pismo-api-specs | `8696ddecc6a5182f…` | 2026-10-13T20:51:51+00:00 |
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
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
