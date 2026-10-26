---
ku_id: KU-API-payment-rails-bacs-payments--bacs-direct-credit
title: 'API reference: Payment rails - BACS payments — BACS direct credit'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Payment_rails_-_BACS_payments.yaml
  sha256: 07915101c3111d715b9c41f297af97c15a2ff09aa3c5e18e03d8f3520e8d12b7
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
- post-create-bacs
- get-bacs-in-transaction
- post-cancel-bacs
- post-release-bacs
- post-reversal-bacs
- post-bacs-client-return
- get-bacs-directcredit-list
related_kus:
- KU-ERR-codes-ebacs
- KU-EVT-catalogue-bacs
- KU-PAY-bacs
specification_version: '1.0'
---

# API reference: Payment rails - BACS payments — BACS direct credit

**KU ID:** `KU-API-payment-rails-bacs-payments--bacs-direct-credit` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `BACS direct credit` in `api-specs/Payment_rails_-_BACS_payments.yaml` (“Payment rails - BACS payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/payments/bacs/directcredit/out` | `post-create-bacs` | Send BACS direct credit outbound payment [beta] | no |
| `GET /v1/payments/bacs/directcredit/{id}` | `get-bacs-in-transaction` | Get BACS transaction [beta] | no |
| `POST /v1/payments/bacs/directcredit/cancel/{id}` | `post-cancel-bacs` | Cancel BACS inbound transaction [beta] | no |
| `POST /v1/payments/bacs/directcredit/release/{id}` | `post-release-bacs` | Release BACS inbound transaction [beta] | no |
| `POST /v1/payments/bacs/directcredit/{id}/reversal` | `post-reversal-bacs` | Reverse BACS direct credit outbound payment [beta] | no |
| `POST /v1/payments/bacs/directcredit/return/{id}` | `post-bacs-client-return` | Return BACS direct credit inbound payment [beta] | no |
| `GET /v1/payments/bacs/directcredit` | `get-bacs-directcredit-list` | List BACS direct credit transactions [beta] | no |

## Operation contracts

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directcredit/out operationId=post-create-bacs -->
### `POST /v1/payments/bacs/directcredit/out` — Send BACS direct credit outbound payment [beta]

- **operationId:** `post-create-bacs`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct credit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Send a <a href="https://www.moderntreasury.com/learn/what-is-bacs" target="_blank">Bankers' Automated Clearing System</a> (BACS) direct credit outbound payment.
>
> BACS is a UK service that facilitates electronic money transfers between banks within a 3-day settlement cycle&mdash; Day 1 (submission), Day 2 (processing), and Day 3 (clearing/credit).
>
> There are two main concepts in BACS:
>
> 1. **Direct credit** - A company can use this format to pay their employees.
>
> 2. **Direct debit** - When an electricity company charges their costumers recurrently it will have a subscription (called *mandates*). When a mandate is generated monthly, the originator creates a charge. When this charge comes to the client here at Pismo. Pismo then debits the customer account.
>
> Both of these methods generate a cashin, cashout, and return.
>
> For more information, refer to the [BACS guide](https://developers.pismo.io/pismo-docs/docs/banking-automated-clearing-system).
>
> **Notes:**
>
>   * Participating accounts must be [registered as a UK account](https://developers.pismo.io/pismo-docs/reference/post-intl-bank-accounts-v2-accounts-account-id-bank-accounts-uk-scan)
>
>   * In case of failure, the transaction is updated with `status` = `CANCELLED` and the `status_reason` field details why it failed.
>
>   * If the counterparty bank rejects the transaction, the transaction is still considered `SETTLED` and, when the provider webhook return is processed, a new [BACS direct credit outbound return payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-out-return-status-change-1) event is generated and
> the amount is credited back to the debtor's account.
>
>   * This endpoint generates a [BACS direct credit outbound payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-out-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `Idempotency-key` | header | yes | string | A UUID (without hyphens) to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. Identifies the transaction on future events.<br> | maxLength: 32 |

#### Request body

Required: yes

> Send payment request body

**Content type `application/json`** — schema: object (schema `bacs_out.BacsOutRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reference` | string (schema `bacs_out.RemittanceInformation`) | yes | Remittance reference. | pattern: "^[a-zA-Z0-9\\\\/\\\\-?:().,'+\\\\s#=!\\"%&*<>;{@\\\\r\\\\n]*$"; maxLength: 140; example: "Weekly money for Mom" |
| `creditor_account` | object (schema `bacs_out.CreditorAccount`) | yes | Creditor's account information | pattern: "^[a-zA-Z0-9\\\\/\\\\-?:().,'+\\\\s#=!\\"%&*<>;{@\\\\r\\\\n]*$" |
| `currency` | object (schema `bacs_out.Currency`) | yes |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response Body | `application/json`: object (schema `bacs_out.BacsOutResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `id`) | no | Client-generated transaction ID. This is the idempotency key UUID passed in the [Send direct credit outbound payment](ref:post-create-bacs) endpoint.<br> | maxLength: 32; example: "1374f841568e4ff4b363b023c170ecdr" |
| `status` | string (schema `status`) | no | - `CREATED` - Payment has been created and is pending processing<br /><br>- `PROCESSING` - P2P balance was impacted and waiting for provider confirmation. For cashin, the transaction means the money will be credited on the next Working Day<br /><br>- `SETTLED` - Transaction completed processing and is settled<br /><br>- `CANCELLED` - Something went wrong and the transaction is cancelled. Refer to `reason` for more details<br /><br>- `HOLD` - The payment is on hold, pending further review<br /><br> | enum: ["CREATED", "PROCESSING", "SETTLED", "CANCELLED", "HOLD"]; example: "PROCESSING" |

##### Response 400

400 Example `EBACS0004` (Validation Error):

```json
{
  "code": "EBACS0004",
  "message": "Validation error"
}
```

400 Example `EBACS0016` (Unmarshal Error):

```json
{
  "code": "EBACS0016",
  "message": "Unmarshal error"
}
```

400 Example `EBACS0019` (Accounts API Invalid Request Error):

```json
{
  "code": "EBACS0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EBACS0025` (P2P API Invalid Request Error):

```json
{
  "code": "EBACS0025",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EBACS0029` (Ledger API Invalid Request Error):

```json
{
  "code": "EBACS0029",
  "message": "Ledger - API returned 4xx error"
}
```

400 Example `EBACS0037` (Invalid Creditor Sort Code Account Number):

```json
{
  "code": "EBACS0037",
  "message": "Invalid creditor sort code/account number"
}
```

400 Example `EBACS0038` (Invalid Creditor IBAN):

```json
{
  "code": "EBACS0038",
  "message": "Invalid creditor IBAN"
}
```

400 Example `EBACS0039` (Invalid Creditor BBAN):

```json
{
  "code": "EBACS0039",
  "message": "Invalid creditor BBAN"
}
```

400 Example `EBACS0046` (IntlBankAccounts API Invalid Request Error):

```json
{
  "code": "EBACS0046",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EBACS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EBACS0047",
  "message": "Invalid BACS Request. Check error details for more information."
}
```

400 Example `EBACS0073` (Amount Greater Than Balance):

```json
{
  "code": "EBACS0073",
  "message": "The amount passed is greater than the current balance"
}
```

##### Response 403

403 Example `EBACS0002` (Missing Tenant Header):

```json
{
  "code": "EBACS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EBACS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EBACS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EBACS0033` (Invalid Account Id):

```json
{
  "code": "EBACS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EBACS0034` (Invalid Idempotency Key):

```json
{
  "code": "EBACS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EBACS0035` (Account Has No Active Addresses):

```json
{
  "code": "EBACS0035",
  "message": "Account has no active addresses"
}
```

403 Example `EBACS0040` (BACS Not Enabled):

```json
{
  "code": "EBACS0040",
  "message": "BACS is not enabled for the creditor sort code"
}
```

403 Example `EBACS0041` (Modulus Check Error):

```json
{
  "code": "EBACS0041",
  "message": "Failed to execute account number modulus check"
}
```

##### Response 404

404 Example `EBACS0010` (Sort Code Not Found):

```json
{
  "code": "EBACS0010",
  "message": "Sort Code not found"
}
```

404 Example `EBACS0018` (Accounts API Not Found Error):

```json
{
  "code": "EBACS0018",
  "message": "Accounts - Not found"
}
```

404 Example `EBACS0028` (Ledger API Not Found Error):

```json
{
  "code": "EBACS0028",
  "message": "Ledger - Not found"
}
```

404 Example `EBACS0031` (IntlBankAccounts API Not Found Error):

```json
{
  "code": "EBACS0031",
  "message": "IntlBankAccounts - Not found"
}
```

##### Response 409

409 Example `EBACS0022` (Transaction Already Exists):

```json
{
  "code": "EBACS0022",
  "message": "A transaction with the specified idempotency key or id already exists"
}
```

409 Example `EBACS0036` (Mismatching Currency Error):

```json
{
  "code": "EBACS0036",
  "message": "The provided currency does not match with the account's configured currency"
}
```

##### Response 429

429 Example `EBACS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EBACS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EBACS0006` (HTTP Error):

```json
{
  "code": "EBACS0006",
  "message": "HTTP request error"
}
```

500 Example `EBACS0009` (IntlBankAccounts API Timeout):

```json
{
  "code": "EBACS0009",
  "message": "IntlBankAccounts API timeout error"
}
```

500 Example `EBACS0011` (IntlBankAccounts API Internal Error):

```json
{
  "code": "EBACS0011",
  "message": "IntlBankAccounts API Internal Server error"
}
```

500 Example `EBACS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EBACS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EBACS0017` (Accounts API Timeout):

```json
{
  "code": "EBACS0017",
  "message": "Accounts API timeout error"
}
```

500 Example `EBACS0020` (Accounts API Server Error):

```json
{
  "code": "EBACS0020",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EBACS0023` (Transaction Database Error):

```json
{
  "code": "EBACS0023",
  "message": "Transaction database error"
}
```

500 Example `EBACS0024` (P2P API Timeout):

```json
{
  "code": "EBACS0024",
  "message": "P2p - API timeout error"
}
```

500 Example `EBACS0026` (P2P API Server Error):

```json
{
  "code": "EBACS0026",
  "message": "P2p - API returned 5xx error"
}
```

500 Example `EBACS0027` (Ledger API Timeout):

```json
{
  "code": "EBACS0027",
  "message": "Ledger API timeout error"
}
```

500 Example `EBACS0030` (Ledger API Server Error):

```json
{
  "code": "EBACS0030",
  "message": "Ledger - API returned 5xx error"
}
```

500 Example `EBACS0032` (IntlBankAccounts API Server Error):

```json
{
  "code": "EBACS0032",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

##### Response 502

502 Example `EBACS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EBACS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 400 | `EBACS0016` | Unmarshal error |
| 400 | `EBACS0019` | Accounts - API returned 4xx error |
| 400 | `EBACS0025` | P2p - API returned 4xx error |
| 400 | `EBACS0029` | Ledger - API returned 4xx error |
| 400 | `EBACS0037` | Invalid creditor sort code/account number |
| 400 | `EBACS0038` | Invalid creditor IBAN |
| 400 | `EBACS0039` | Invalid creditor BBAN |
| 400 | `EBACS0046` | IntlBankAccounts - API returned 4xx error |
| 400 | `EBACS0047` | Invalid BACS Request. Check error details for more information. |
| 400 | `EBACS0073` | The amount passed is greater than the current balance |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0021` | Account blocked or cancelled |
| 403 | `EBACS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EBACS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EBACS0035` | Account has no active addresses |
| 403 | `EBACS0040` | BACS is not enabled for the creditor sort code |
| 403 | `EBACS0041` | Failed to execute account number modulus check |
| 404 | `EBACS0010` | Sort Code not found |
| 404 | `EBACS0018` | Accounts - Not found |
| 404 | `EBACS0028` | Ledger - Not found |
| 404 | `EBACS0031` | IntlBankAccounts - Not found |
| 409 | `EBACS0022` | A transaction with the specified idempotency key or id already exists |
| 409 | `EBACS0036` | The provided currency does not match with the account's configured currency |
| 429 | `EBACS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EBACS0006` | HTTP request error |
| 500 | `EBACS0009` | IntlBankAccounts API timeout error |
| 500 | `EBACS0011` | IntlBankAccounts API Internal Server error |
| 500 | `EBACS0012` | PSPGateway API timeout error |
| 500 | `EBACS0017` | Accounts API timeout error |
| 500 | `EBACS0020` | Accounts - API returned 5xx error |
| 500 | `EBACS0023` | Transaction database error |
| 500 | `EBACS0024` | P2p - API timeout error |
| 500 | `EBACS0026` | P2p - API returned 5xx error |
| 500 | `EBACS0027` | Ledger API timeout error |
| 500 | `EBACS0030` | Ledger - API returned 5xx error |
| 500 | `EBACS0032` | IntlBankAccounts - API returned 5xx error |
| 502 | `EBACS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-direct-credit-out-return-status-change-1` | https://developers.pismo.io/events/docs/bacs-direct-credit-out-return-status-change-1 |
| `bacs-direct-credit-out-status-change-1` | https://developers.pismo.io/events/docs/bacs-direct-credit-out-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;409;429;500;502`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-PAY-bacs`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=GET path=/v1/payments/bacs/directcredit/{id} operationId=get-bacs-in-transaction -->
### `GET /v1/payments/bacs/directcredit/{id}` — Get BACS transaction [beta]

- **operationId:** `get-bacs-in-transaction`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct credit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get a BACS transaction given its ID in the path.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `id` | path | yes | string | BACS transaction ID. | maxLength: 31 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Get BACS transaction response body | `application/json`: object (schema `bacs_get.BacsGetResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `id`) | no | Client-generated transaction ID. This is the idempotency key UUID passed in the [Send direct credit outbound payment](ref:post-create-bacs) endpoint.<br> | maxLength: 32; example: "1374f841568e4ff4b363b023c170ecdr" |
| `status` | string (schema `status`) | no | - `CREATED` - Payment has been created and is pending processing<br /><br>- `PROCESSING` - P2P balance was impacted and waiting for provider confirmation. For cashin, the transaction means the money will be credited on the next Working Day<br /><br>- `SETTLED` - Transaction completed processing and is settled<br /><br>- `CANCELLED` - Something went wrong and the transaction is cancelled. Refer to `reason` for more details<br /><br>- `HOLD` - The payment is on hold, pending further review<br /><br> | enum: ["CREATED", "PROCESSING", "SETTLED", "CANCELLED", "HOLD"]; example: "PROCESSING" |
| `amount` | number (schema `amount`) | no | Transaction amount. | example: 600 |

##### Response 400

400 Example `EBACS0004` (Validation Error):

```json
{
  "code": "EBACS0004",
  "message": "Validation error"
}
```

400 Example `EBACS0016` (Unmarshal Error):

```json
{
  "code": "EBACS0016",
  "message": "Unmarshal error"
}
```

400 Example `EBACS0019` (Accounts API Invalid Request Error):

```json
{
  "code": "EBACS0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EBACS0025` (P2P API Invalid Request Error):

```json
{
  "code": "EBACS0025",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EBACS0029` (Ledger API Invalid Request Error):

```json
{
  "code": "EBACS0029",
  "message": "Ledger - API returned 4xx error"
}
```

400 Example `EBACS0037` (Invalid Creditor Sort Code Account Number):

```json
{
  "code": "EBACS0037",
  "message": "Invalid creditor sort code/account number"
}
```

400 Example `EBACS0038` (Invalid Creditor IBAN):

```json
{
  "code": "EBACS0038",
  "message": "Invalid creditor IBAN"
}
```

400 Example `EBACS0039` (Invalid Creditor BBAN):

```json
{
  "code": "EBACS0039",
  "message": "Invalid creditor BBAN"
}
```

400 Example `EBACS0046` (IntlBankAccounts API Invalid Request Error):

```json
{
  "code": "EBACS0046",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EBACS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EBACS0047",
  "message": "Invalid BACS Request. Check error details for more information."
}
```

##### Response 403

403 Example `EBACS0002` (Missing Tenant Header):

```json
{
  "code": "EBACS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EBACS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EBACS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EBACS0033` (Invalid Account Id):

```json
{
  "code": "EBACS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EBACS0034` (Invalid Idempotency Key):

```json
{
  "code": "EBACS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EBACS0035` (Account Has No Active Addresses):

```json
{
  "code": "EBACS0035",
  "message": "Account has no active addresses"
}
```

403 Example `EBACS0040` (BACS Not Enabled):

```json
{
  "code": "EBACS0040",
  "message": "BACS is not enabled for the creditor sort code"
}
```

403 Example `EBACS0041` (Modulus Check Error):

```json
{
  "code": "EBACS0041",
  "message": "Failed to execute account number modulus check"
}
```

##### Response 404

404 Example `EBACS0010` (Sort Code Not Found):

```json
{
  "code": "EBACS0010",
  "message": "Sort Code not found"
}
```

404 Example `EBACS0018` (Accounts API Not Found Error):

```json
{
  "code": "EBACS0018",
  "message": "Accounts - Not found"
}
```

404 Example `EBACS0028` (Ledger API Not Found Error):

```json
{
  "code": "EBACS0028",
  "message": "Ledger - Not found"
}
```

404 Example `EBACS0031` (IntlBankAccounts API Not Found Error):

```json
{
  "code": "EBACS0031",
  "message": "IntlBankAccounts - Not found"
}
```

##### Response 409

409 Example `EBACS0022` (Transaction Already Exists):

```json
{
  "code": "EBACS0022",
  "message": "A transaction with the specified idempotency key and id already exists"
}
```

409 Example `EBACS0036` (Mismatching Currency Error):

```json
{
  "code": "EBACS0036",
  "message": "The provided currency does not match with the account's configured currency"
}
```

##### Response 429

429 Example `EBACS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EBACS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EBACS0006` (HTTP Error):

```json
{
  "code": "EBACS0006",
  "message": "HTTP request error"
}
```

500 Example `EBACS0009` (IntlBankAccounts API Timeout):

```json
{
  "code": "EBACS0009",
  "message": "IntlBankAccounts API timeout error"
}
```

500 Example `EBACS0011` (IntlBankAccounts API Internal Error):

```json
{
  "code": "EBACS0011",
  "message": "IntlBankAccounts API Internal Server error"
}
```

500 Example `EBACS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EBACS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EBACS0017` (Accounts API Timeout):

```json
{
  "code": "EBACS0017",
  "message": "Accounts API timeout error"
}
```

500 Example `EBACS0020` (Accounts API Server Error):

```json
{
  "code": "EBACS0020",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EBACS0023` (Transaction Database Error):

```json
{
  "code": "EBACS0023",
  "message": "Transaction database error"
}
```

500 Example `EBACS0024` (P2P API Timeout):

```json
{
  "code": "EBACS0024",
  "message": "P2p - API timeout error"
}
```

500 Example `EBACS0026` (P2P API Server Error):

```json
{
  "code": "EBACS0026",
  "message": "P2p - API returned 5xx error"
}
```

500 Example `EBACS0027` (Ledger API Timeout):

```json
{
  "code": "EBACS0027",
  "message": "Ledger API timeout error"
}
```

500 Example `EBACS0030` (Ledger API Server Error):

```json
{
  "code": "EBACS0030",
  "message": "Ledger - API returned 5xx error"
}
```

500 Example `EBACS0032` (IntlBankAccounts API Server Error):

```json
{
  "code": "EBACS0032",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

##### Response 502

502 Example `EBACS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EBACS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 400 | `EBACS0016` | Unmarshal error |
| 400 | `EBACS0019` | Accounts - API returned 4xx error |
| 400 | `EBACS0025` | P2p - API returned 4xx error |
| 400 | `EBACS0029` | Ledger - API returned 4xx error |
| 400 | `EBACS0037` | Invalid creditor sort code/account number |
| 400 | `EBACS0038` | Invalid creditor IBAN |
| 400 | `EBACS0039` | Invalid creditor BBAN |
| 400 | `EBACS0046` | IntlBankAccounts - API returned 4xx error |
| 400 | `EBACS0047` | Invalid BACS Request. Check error details for more information. |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0021` | Account blocked or cancelled |
| 403 | `EBACS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EBACS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EBACS0035` | Account has no active addresses |
| 403 | `EBACS0040` | BACS is not enabled for the creditor sort code |
| 403 | `EBACS0041` | Failed to execute account number modulus check |
| 404 | `EBACS0010` | Sort Code not found |
| 404 | `EBACS0018` | Accounts - Not found |
| 404 | `EBACS0028` | Ledger - Not found |
| 404 | `EBACS0031` | IntlBankAccounts - Not found |
| 409 | `EBACS0022` | A transaction with the specified idempotency key and id already exists |
| 409 | `EBACS0036` | The provided currency does not match with the account's configured currency |
| 429 | `EBACS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EBACS0006` | HTTP request error |
| 500 | `EBACS0009` | IntlBankAccounts API timeout error |
| 500 | `EBACS0011` | IntlBankAccounts API Internal Server error |
| 500 | `EBACS0012` | PSPGateway API timeout error |
| 500 | `EBACS0017` | Accounts API timeout error |
| 500 | `EBACS0020` | Accounts - API returned 5xx error |
| 500 | `EBACS0023` | Transaction database error |
| 500 | `EBACS0024` | P2p - API timeout error |
| 500 | `EBACS0026` | P2p - API returned 5xx error |
| 500 | `EBACS0027` | Ledger API timeout error |
| 500 | `EBACS0030` | Ledger - API returned 5xx error |
| 500 | `EBACS0032` | IntlBankAccounts - API returned 5xx error |
| 502 | `EBACS0014` | PSPGateway API Bad Gateway |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;429;500;502`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directcredit/cancel/{id} operationId=post-cancel-bacs -->
### `POST /v1/payments/bacs/directcredit/cancel/{id}` — Cancel BACS inbound transaction [beta]

- **operationId:** `post-cancel-bacs`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct credit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Cancel a suspended transaction, which was kept on hold based on client's anti-fraud (AF) provider analysis, and return the transaction.
>
> **Suspense transaction flow**
>
> You can use the suspense transaction flow to manage incoming BACS transactions that have been temporarily placed on hold due to suspected fraud pending a decision from the client's anti-fraud (AF) provider.
>
> **Supported scenarios:**
>
>   * An incoming (cash-in) BACS transaction is received.
>
>   * Client' s anti-fraud provider returns "hold" instead of approve or reject.
>
>   * Pismo places the transaction amount into additional fund (unavailable balance) so the beneficiary cannot use the funds until a final decision is made.
>
>   * The client later calls Pismo's [release](ref:post-release-bacs) or cancel endpoints to finalize the transaction.
>
> **Day 2 recall (pre-settlement cancellation)**
>
> This endpoint also supports cancelling an inbound (cash-in) BACS Direct Credit that is still `PROCESSING` and awaiting the Day 3 posting cycle, so it is never credited to the beneficiary. The optional `returnFunds` flag (default `true`) controls whether the funds are returned to the originating institution:
>
>   * `returnFunds` = `true` - Cancel the transaction and generate a return instruction (debiting the beneficiary if the amount was already credited).
>
>   * `returnFunds` = `false` - Cancel the transaction only; no return instruction is created.
>
> In all cases the transaction is removed from the Day 3 settlement queue and marked `CANCELLED`.
>
> This endpoint generates a [BACS direct credit inbound payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-in-status-change-1) event with `status` = `CANCELLED`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `id` | path | yes | string | BACS transaction ID. | maxLength: 31 |

#### Request body

Required: no

> Optional cancellation options. When not passed, `returnFunds` defaults to `true`.

**Content type `application/json`** — schema: object (schema `bacs_cancel.BacsCancelRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `returnFunds` | boolean | no | Should a return instruction be generated as part of the cancellation? Default is `true`.<br><br>* `true`- Cancel the transaction and return the funds to the originating institution (debiting the beneficiary if the amount was already credited).<br><br>* `false` - Cancel the transaction only. No return instruction is created.<br> | default: true; example: true |
| `reason` | string | no | Optional business reason for the cancellation (for example, `DAY2_RECALL`).<br> | example: "DAY2_RECALL" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `bacs_cancel.BacsCancelResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `id`) | no | Client-generated transaction ID. This is the idempotency key UUID passed in the [Send direct credit outbound payment](ref:post-create-bacs) endpoint.<br> | maxLength: 32; example: "1374f841568e4ff4b363b023c170ecdr" |
| `status` | string (schema `bacs_cancel.status`) | no | - `CANCELLED` - Something went wrong and the transaction was cancelled. Refer to `reason` for details,<br> | enum: ["CANCELLED"]; example: "CANCELLED" |
| `returnFunds` | boolean | no | Cancellation's effective return funds value | example: true |

##### Response 400

400 Example `EBACS0004` (Validation Error):

```json
{
  "code": "EBACS0004",
  "message": "Validation error"
}
```

400 Example `EBACS0016` (Unmarshal Error):

```json
{
  "code": "EBACS0016",
  "message": "Unmarshal error"
}
```

400 Example `EBACS0019` (Accounts API Invalid Request Error):

```json
{
  "code": "EBACS0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EBACS0025` (P2P API Invalid Request Error):

```json
{
  "code": "EBACS0025",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EBACS0029` (Ledger API Invalid Request Error):

```json
{
  "code": "EBACS0029",
  "message": "Ledger - API returned 4xx error"
}
```

400 Example `EBACS0037` (Invalid Creditor Sort Code Account Number):

```json
{
  "code": "EBACS0037",
  "message": "Invalid creditor sort code/account number"
}
```

400 Example `EBACS0038` (Invalid Creditor IBAN):

```json
{
  "code": "EBACS0038",
  "message": "Invalid creditor IBAN"
}
```

400 Example `EBACS0039` (Invalid Creditor BBAN):

```json
{
  "code": "EBACS0039",
  "message": "Invalid creditor BBAN"
}
```

400 Example `EBACS0046` (IntlBankAccounts API Invalid Request Error):

```json
{
  "code": "EBACS0046",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EBACS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EBACS0047",
  "message": "Invalid BACS Request. Check error details for more information."
}
```

##### Response 403

403 Example `EBACS0002` (Missing Tenant Header):

```json
{
  "code": "EBACS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EBACS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EBACS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EBACS0033` (Invalid Account Id):

```json
{
  "code": "EBACS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EBACS0034` (Invalid Idempotency Key):

```json
{
  "code": "EBACS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EBACS0035` (Account Has No Active Addresses):

```json
{
  "code": "EBACS0035",
  "message": "Account has no active addresses"
}
```

403 Example `EBACS0040` (BACS Not Enabled):

```json
{
  "code": "EBACS0040",
  "message": "BACS is not enabled for the creditor sort code"
}
```

403 Example `EBACS0041` (Modulus Check Error):

```json
{
  "code": "EBACS0041",
  "message": "Failed to execute account number modulus check"
}
```

##### Response 404

404 Example `EBACS0010` (Sort Code Not Found):

```json
{
  "code": "EBACS0010",
  "message": "Sort Code not found"
}
```

404 Example `EBACS0018` (Accounts API Not Found Error):

```json
{
  "code": "EBACS0018",
  "message": "Accounts - Not found"
}
```

404 Example `EBACS0028` (Ledger API Not Found Error):

```json
{
  "code": "EBACS0028",
  "message": "Ledger - Not found"
}
```

404 Example `EBACS0031` (IntlBankAccounts API Not Found Error):

```json
{
  "code": "EBACS0031",
  "message": "IntlBankAccounts - Not found"
}
```

##### Response 409

409 Example `EBACS0022` (Transaction Already Exists):

```json
{
  "code": "EBACS0022",
  "message": "A transaction with the specified idempotency key and id already exists"
}
```

409 Example `EBACS0036` (Mismatching Currency Error):

```json
{
  "code": "EBACS0036",
  "message": "The provided currency does not match with the account's configured currency"
}
```

409 Example `EBACS0096` (Cancel Not Allowed - Invalid Status):

```json
{
  "code": "EBACS0096",
  "message": "Cancel not allowed: transaction is already finalised"
}
```

##### Response 429

429 Example `EBACS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EBACS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EBACS0006` (HTTP Error):

```json
{
  "code": "EBACS0006",
  "message": "HTTP request error"
}
```

500 Example `EBACS0009` (IntlBankAccounts API Timeout):

```json
{
  "code": "EBACS0009",
  "message": "IntlBankAccounts API timeout error"
}
```

500 Example `EBACS0011` (IntlBankAccounts API Internal Error):

```json
{
  "code": "EBACS0011",
  "message": "IntlBankAccounts API Internal Server error"
}
```

500 Example `EBACS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EBACS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EBACS0017` (Accounts API Timeout):

```json
{
  "code": "EBACS0017",
  "message": "Accounts API timeout error"
}
```

500 Example `EBACS0020` (Accounts API Server Error):

```json
{
  "code": "EBACS0020",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EBACS0023` (Transaction Database Error):

```json
{
  "code": "EBACS0023",
  "message": "Transaction database error"
}
```

500 Example `EBACS0024` (P2P API Timeout):

```json
{
  "code": "EBACS0024",
  "message": "P2p - API timeout error"
}
```

500 Example `EBACS0026` (P2P API Server Error):

```json
{
  "code": "EBACS0026",
  "message": "P2p - API returned 5xx error"
}
```

500 Example `EBACS0027` (Ledger API Timeout):

```json
{
  "code": "EBACS0027",
  "message": "Ledger API timeout error"
}
```

500 Example `EBACS0030` (Ledger API Server Error):

```json
{
  "code": "EBACS0030",
  "message": "Ledger - API returned 5xx error"
}
```

500 Example `EBACS0032` (IntlBankAccounts API Server Error):

```json
{
  "code": "EBACS0032",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

##### Response 502

502 Example `EBACS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EBACS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 400 | `EBACS0016` | Unmarshal error |
| 400 | `EBACS0019` | Accounts - API returned 4xx error |
| 400 | `EBACS0025` | P2p - API returned 4xx error |
| 400 | `EBACS0029` | Ledger - API returned 4xx error |
| 400 | `EBACS0037` | Invalid creditor sort code/account number |
| 400 | `EBACS0038` | Invalid creditor IBAN |
| 400 | `EBACS0039` | Invalid creditor BBAN |
| 400 | `EBACS0046` | IntlBankAccounts - API returned 4xx error |
| 400 | `EBACS0047` | Invalid BACS Request. Check error details for more information. |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0021` | Account blocked or cancelled |
| 403 | `EBACS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EBACS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EBACS0035` | Account has no active addresses |
| 403 | `EBACS0040` | BACS is not enabled for the creditor sort code |
| 403 | `EBACS0041` | Failed to execute account number modulus check |
| 404 | `EBACS0010` | Sort Code not found |
| 404 | `EBACS0018` | Accounts - Not found |
| 404 | `EBACS0028` | Ledger - Not found |
| 404 | `EBACS0031` | IntlBankAccounts - Not found |
| 409 | `EBACS0022` | A transaction with the specified idempotency key and id already exists |
| 409 | `EBACS0036` | The provided currency does not match with the account's configured currency |
| 409 | `EBACS0096` | Cancel not allowed: transaction is already finalised |
| 429 | `EBACS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EBACS0006` | HTTP request error |
| 500 | `EBACS0009` | IntlBankAccounts API timeout error |
| 500 | `EBACS0011` | IntlBankAccounts API Internal Server error |
| 500 | `EBACS0012` | PSPGateway API timeout error |
| 500 | `EBACS0017` | Accounts API timeout error |
| 500 | `EBACS0020` | Accounts - API returned 5xx error |
| 500 | `EBACS0023` | Transaction database error |
| 500 | `EBACS0024` | P2p - API timeout error |
| 500 | `EBACS0026` | P2p - API returned 5xx error |
| 500 | `EBACS0027` | Ledger API timeout error |
| 500 | `EBACS0030` | Ledger - API returned 5xx error |
| 500 | `EBACS0032` | IntlBankAccounts - API returned 5xx error |
| 502 | `EBACS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-direct-credit-in-status-change-1` | https://developers.pismo.io/events/docs/bacs-direct-credit-in-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;429;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-bacs`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directcredit/release/{id} operationId=post-release-bacs -->
### `POST /v1/payments/bacs/directcredit/release/{id}` — Release BACS inbound transaction [beta]

- **operationId:** `post-release-bacs`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct credit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Move a suspended transaction amount from additional funds to available balance and mark the transaction as settled.
>
> **Suspense transaction flow**
>
> You can use the suspense transaction flow to manage incoming BACS transactions that have been temporarily placed on hold due to suspected fraud pending a decision from the client's anti-fraud (AF) provider.
>
> **Supported scenarios:**
>
>   * A incoming (cash-in) BACS transaction is received.
>
>   * Client' s anti-fraud provider returns "hold" instead of approve or reject.
>
>   * Pismo places the transaction amount into additional funds (unavailable balance) so the beneficiary cannot use the funds until a final decision is made.
>
>   * The client later calls Pismo's release or [cancel](ref:post-cancel-bacs) endpoints to finalize the transaction.
>
> This endpoint generates a [BACS direct credit inbound payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-in-status-change-1) event with status `SETTLED`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `id` | path | yes | string | BACS transaction ID. | maxLength: 31 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `bacs_release.BacsReleaseResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `id`) | no | Client-generated transaction ID. This is the idempotency key UUID passed in the [Send direct credit outbound payment](ref:post-create-bacs) endpoint.<br> | maxLength: 32; example: "1374f841568e4ff4b363b023c170ecdr" |
| `status` | string (schema `bacs_release.status`) | no | - `SETTLED`—Transaction completed, processed, and settled.<br> | enum: ["SETTLED"]; example: "SETTLED" |
| `amount` | number (schema `amount`) | no | Transaction amount. | example: 600 |

##### Response 400

400 Example `EBACS0004` (Validation Error):

```json
{
  "code": "EBACS0004",
  "message": "Validation error"
}
```

400 Example `EBACS0016` (Unmarshal Error):

```json
{
  "code": "EBACS0016",
  "message": "Unmarshal error"
}
```

400 Example `EBACS0019` (Accounts API Invalid Request Error):

```json
{
  "code": "EBACS0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EBACS0025` (P2P API Invalid Request Error):

```json
{
  "code": "EBACS0025",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EBACS0029` (Ledger API Invalid Request Error):

```json
{
  "code": "EBACS0029",
  "message": "Ledger - API returned 4xx error"
}
```

400 Example `EBACS0037` (Invalid Creditor Sort Code Account Number):

```json
{
  "code": "EBACS0037",
  "message": "Invalid creditor sort code/account number"
}
```

400 Example `EBACS0038` (Invalid Creditor IBAN):

```json
{
  "code": "EBACS0038",
  "message": "Invalid creditor IBAN"
}
```

400 Example `EBACS0039` (Invalid Creditor BBAN):

```json
{
  "code": "EBACS0039",
  "message": "Invalid creditor BBAN"
}
```

400 Example `EBACS0046` (IntlBankAccounts API Invalid Request Error):

```json
{
  "code": "EBACS0046",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EBACS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EBACS0047",
  "message": "Invalid BACS Request. Check error details for more information."
}
```

##### Response 403

403 Example `EBACS0002` (Missing Tenant Header):

```json
{
  "code": "EBACS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EBACS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EBACS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EBACS0033` (Invalid Account Id):

```json
{
  "code": "EBACS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EBACS0034` (Invalid Idempotency Key):

```json
{
  "code": "EBACS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EBACS0035` (Account Has No Active Addresses):

```json
{
  "code": "EBACS0035",
  "message": "Account has no active addresses"
}
```

403 Example `EBACS0040` (BACS Not Enabled):

```json
{
  "code": "EBACS0040",
  "message": "BACS is not enabled for the creditor sort code"
}
```

403 Example `EBACS0041` (Modulus Check Error):

```json
{
  "code": "EBACS0041",
  "message": "Failed to execute account number modulus check"
}
```

##### Response 404

404 Example `EBACS0010` (Sort Code Not Found):

```json
{
  "code": "EBACS0010",
  "message": "Sort Code not found"
}
```

404 Example `EBACS0018` (Accounts API Not Found Error):

```json
{
  "code": "EBACS0018",
  "message": "Accounts - Not found"
}
```

404 Example `EBACS0028` (Ledger API Not Found Error):

```json
{
  "code": "EBACS0028",
  "message": "Ledger - Not found"
}
```

404 Example `EBACS0031` (IntlBankAccounts API Not Found Error):

```json
{
  "code": "EBACS0031",
  "message": "IntlBankAccounts - Not found"
}
```

##### Response 409

409 Example `EBACS0022` (Transaction Already Exists):

```json
{
  "code": "EBACS0022",
  "message": "A transaction with the specified idempotency key and id already exists"
}
```

409 Example `EBACS0036` (Mismatching Currency Error):

```json
{
  "code": "EBACS0036",
  "message": "The provided currency does not match with the account's configured currency"
}
```

409 Example `EBACS0097` (Release Not Allowed - Invalid Status):

```json
{
  "code": "EBACS0097",
  "message": "Release not allowed: transaction is already finalised"
}
```

##### Response 429

429 Example `EBACS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EBACS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EBACS0006` (HTTP Error):

```json
{
  "code": "EBACS0006",
  "message": "HTTP request error"
}
```

500 Example `EBACS0009` (IntlBankAccounts API Timeout):

```json
{
  "code": "EBACS0009",
  "message": "IntlBankAccounts API timeout error"
}
```

500 Example `EBACS0011` (IntlBankAccounts API Internal Error):

```json
{
  "code": "EBACS0011",
  "message": "IntlBankAccounts API Internal Server error"
}
```

500 Example `EBACS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EBACS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EBACS0017` (Accounts API Timeout):

```json
{
  "code": "EBACS0017",
  "message": "Accounts API timeout error"
}
```

500 Example `EBACS0020` (Accounts API Server Error):

```json
{
  "code": "EBACS0020",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EBACS0023` (Transaction Database Error):

```json
{
  "code": "EBACS0023",
  "message": "Transaction database error"
}
```

500 Example `EBACS0024` (P2P API Timeout):

```json
{
  "code": "EBACS0024",
  "message": "P2p - API timeout error"
}
```

500 Example `EBACS0026` (P2P API Server Error):

```json
{
  "code": "EBACS0026",
  "message": "P2p - API returned 5xx error"
}
```

500 Example `EBACS0027` (Ledger API Timeout):

```json
{
  "code": "EBACS0027",
  "message": "Ledger API timeout error"
}
```

500 Example `EBACS0030` (Ledger API Server Error):

```json
{
  "code": "EBACS0030",
  "message": "Ledger - API returned 5xx error"
}
```

500 Example `EBACS0032` (IntlBankAccounts API Server Error):

```json
{
  "code": "EBACS0032",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

##### Response 502

502 Example `EBACS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EBACS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 400 | `EBACS0016` | Unmarshal error |
| 400 | `EBACS0019` | Accounts - API returned 4xx error |
| 400 | `EBACS0025` | P2p - API returned 4xx error |
| 400 | `EBACS0029` | Ledger - API returned 4xx error |
| 400 | `EBACS0037` | Invalid creditor sort code/account number |
| 400 | `EBACS0038` | Invalid creditor IBAN |
| 400 | `EBACS0039` | Invalid creditor BBAN |
| 400 | `EBACS0046` | IntlBankAccounts - API returned 4xx error |
| 400 | `EBACS0047` | Invalid BACS Request. Check error details for more information. |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0021` | Account blocked or cancelled |
| 403 | `EBACS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EBACS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EBACS0035` | Account has no active addresses |
| 403 | `EBACS0040` | BACS is not enabled for the creditor sort code |
| 403 | `EBACS0041` | Failed to execute account number modulus check |
| 404 | `EBACS0010` | Sort Code not found |
| 404 | `EBACS0018` | Accounts - Not found |
| 404 | `EBACS0028` | Ledger - Not found |
| 404 | `EBACS0031` | IntlBankAccounts - Not found |
| 409 | `EBACS0022` | A transaction with the specified idempotency key and id already exists |
| 409 | `EBACS0036` | The provided currency does not match with the account's configured currency |
| 409 | `EBACS0097` | Release not allowed: transaction is already finalised |
| 429 | `EBACS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EBACS0006` | HTTP request error |
| 500 | `EBACS0009` | IntlBankAccounts API timeout error |
| 500 | `EBACS0011` | IntlBankAccounts API Internal Server error |
| 500 | `EBACS0012` | PSPGateway API timeout error |
| 500 | `EBACS0017` | Accounts API timeout error |
| 500 | `EBACS0020` | Accounts - API returned 5xx error |
| 500 | `EBACS0023` | Transaction database error |
| 500 | `EBACS0024` | P2p - API timeout error |
| 500 | `EBACS0026` | P2p - API returned 5xx error |
| 500 | `EBACS0027` | Ledger API timeout error |
| 500 | `EBACS0030` | Ledger - API returned 5xx error |
| 500 | `EBACS0032` | IntlBankAccounts - API returned 5xx error |
| 502 | `EBACS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-direct-credit-in-status-change-1` | https://developers.pismo.io/events/docs/bacs-direct-credit-in-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;429;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-bacs`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directcredit/{id}/reversal operationId=post-reversal-bacs -->
### `POST /v1/payments/bacs/directcredit/{id}/reversal` — Reverse BACS direct credit outbound payment [beta]

- **operationId:** `post-reversal-bacs`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct credit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

>
> Reverse a BACS direct credit outbound payment that is on hold.
>
> A reversal is only allowed when:
> - The payment is an outbound payment with status `HOLD`
> - The reversal is requested on the same day as the payment creation date
>
> This endpoint generates a [BACS direct credit outbound reversal processed](https://developers.pismo.io/events/docs/bacs-direct-credit-out-reversal-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `Idempotency-key` | header | yes | string | A UUID (without hyphens) to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. Identifies the transaction on future events.<br> | maxLength: 32 |
| `id` | path | yes | string | BACS transaction ID. | maxLength: 31 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `bacs_reversal.BacsReversalResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payment_id` | string (schema `id`) | no | Client-generated transaction ID. This is the idempotency key UUID passed in the [Send direct credit outbound payment](ref:post-create-bacs) endpoint.<br> | maxLength: 32; example: "1374f841568e4ff4b363b023c170ecdr" |
| `outbound_reversal_id` | string (schema `id`) | no | Client-generated transaction ID. This is the idempotency key UUID passed in the [Send direct credit outbound payment](ref:post-create-bacs) endpoint.<br> | maxLength: 32; example: "1374f841568e4ff4b363b023c170ecdr" |
| `status` | string (schema `bacs_reversal.status`) | no | - `PROCESSING` - Reversal has been submitted and is awaiting settlement<br> | enum: ["PROCESSING"]; example: "PROCESSING" |

##### Response 400

400 Example `EBACS0004` (Validation Error):

```json
{
  "code": "EBACS0004",
  "message": "Validation error"
}
```

400 Example `EBACS0016` (Unmarshal Error):

```json
{
  "code": "EBACS0016",
  "message": "Unmarshal error"
}
```

400 Example `EBACS0093` (Reversal Not Allowed - Invalid Status):

```json
{
  "code": "EBACS0093",
  "message": "Reversal not allowed: payment must be OUTBOUND with HOLD status"
}
```

400 Example `EBACS0094` (Reversal Not Allowed - Time Expired):

```json
{
  "code": "EBACS0094",
  "message": "Reversal not allowed: current time is past the payment creation day"
}
```

400 Example `EBACS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EBACS0047",
  "message": "Invalid BACS Request. Check error details for more information."
}
```

##### Response 403

403 Example `EBACS0002` (Missing Tenant Header):

```json
{
  "code": "EBACS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EBACS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EBACS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EBACS0033` (Invalid Account Id):

```json
{
  "code": "EBACS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EBACS0034` (Invalid Idempotency Key):

```json
{
  "code": "EBACS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

##### Response 404

404 Example `EBACS0010` (Transaction Not Found):

```json
{
  "code": "EBACS0010",
  "message": "Transaction not found"
}
```

404 Example `EBACS0092` (PSP Gateway Not Found):

```json
{
  "code": "EBACS0092",
  "message": "PSPGateway API Not found"
}
```

##### Response 429

429 Example `EBACS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EBACS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EBACS0006` (HTTP Error):

```json
{
  "code": "EBACS0006",
  "message": "HTTP request error"
}
```

500 Example `EBACS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EBACS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EBACS0023` (Transaction Database Error):

```json
{
  "code": "EBACS0023",
  "message": "Transaction database error"
}
```

##### Response 502

502 Example `EBACS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EBACS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 400 | `EBACS0016` | Unmarshal error |
| 400 | `EBACS0093` | Reversal not allowed: payment must be OUTBOUND with HOLD status |
| 400 | `EBACS0094` | Reversal not allowed: current time is past the payment creation day |
| 400 | `EBACS0047` | Invalid BACS Request. Check error details for more information. |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0021` | Account blocked or cancelled |
| 403 | `EBACS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EBACS0034` | Missing required header: 'x-idempotency-key' |
| 404 | `EBACS0010` | Transaction not found |
| 404 | `EBACS0092` | PSPGateway API Not found |
| 429 | `EBACS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EBACS0006` | HTTP request error |
| 500 | `EBACS0012` | PSPGateway API timeout error |
| 500 | `EBACS0023` | Transaction database error |
| 502 | `EBACS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-direct-credit-out-reversal-status-change-1` | https://developers.pismo.io/events/docs/bacs-direct-credit-out-reversal-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;429;500;502`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directcredit/return/{id} operationId=post-bacs-client-return -->
### `POST /v1/payments/bacs/directcredit/return/{id}` — Return BACS direct credit inbound payment [beta]

- **operationId:** `post-bacs-client-return`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct credit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Initiates a client return for a settled BACS direct credit inbound payment. The return amount must match the original transaction amount exactly, since the platform does not allow partial returns. The platform permits only one return per original transaction.
>
> Returns initiated through this endpoint are marked with `return_origin` = `CLIENT` to distinguish them from system-initiated returns (`return_origin` = `SYSTEM`).
>
> This endpoint generates a [BACS direct credit inbound return payment processed](https://developers.pismo.io/events/docs/bacs-direct-credit-in-return-status-change-1) event with `return_origin` = `CLIENT`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `Idempotency-key` | header | yes | string | A UUID (without hyphens) to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. Identifies the transaction on future events.<br> | maxLength: 32 |
| `id` | path | yes | string | BACS transaction ID. | maxLength: 31 |

#### Request body

Required: yes

> Client return request body

**Content type `application/json`** — schema: object (schema `bacs_return.ClientReturnRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `return_reason` | string (schema `returnReason`) | yes | The reason for the return.<br>  * `account_closed` — The beneficiary account is no longer active.<br>  * `account_currency_mismatch` — The payment currency does not match the account currency.<br>  * `other` — A reason that the other specific codes do not cover.<br>  * `cancelled_by_payer`— The payer requests cancellation of the payment.<br> | enum: ["account_closed", "account_currency_mismatch", "cancelled_by_payer", "other"]; example: "account_closed" |
| `amount` | number | yes | Amount to return. Must match the original transaction amount, since the Pismo platform does not support partial returns.<br> | format: "float"; example: 100 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `bacs_return.ClientReturnResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `returnStatus`) | no | * `PROCESSING`—The system processes the return and awaits settlement.<br>*`SETTLED`—The return settles successfully.<br>*`CANCELLED`—The system cancels the return due to an error.<br> | enum: ["PROCESSING", "SETTLED", "CANCELLED"]; example: "PROCESSING" |
| `return_transaction_id` | string (schema `returnTransactionId`) | no | The ID of the new return transaction. | example: "019e92ec-3362-7c54-9d17-89f5542a06e4" |
| `original_transaction_id` | string (schema `originalTransactionId`) | no | Original transaction ID | example: "08ec4cf7-2d74-5453-80e0-e940ac8fc219" |
| `return_origin` | string (schema `returnOrigin`) | no | Indicates whether the client or the system initiates the return<br>  * `CLIENT`—The client initiates the return via this endpoint<br>  * `SYSTEM`—The system initiates the return automatically<br> | enum: ["CLIENT", "SYSTEM"]; example: "SYSTEM" |

##### Response 400

400 Example `EBACS0004` (Validation Error):

```json
{
  "code": "EBACS0004",
  "message": "Validation error"
}
```

400 Example `EBACS0095` (Partial Returns Not Allowed):

```json
{
  "code": "EBACS0095",
  "message": "Partial returns are not allowed"
}
```

##### Response 403

403 Example `EBACS0002` (Missing Tenant Header):

```json
{
  "code": "EBACS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EBACS0033` (Invalid Account Id):

```json
{
  "code": "EBACS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EBACS0086` (Missing Idempotency Key):

```json
{
  "code": "EBACS0086",
  "message": "Missing required header: 'Idempotency-key'"
}
```

##### Response 404

404 Example `EBACS0067` (Transaction Not Found):

```json
{
  "code": "EBACS0067",
  "message": "Transaction not found"
}
```

##### Response 429

429 Example `EBACS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EBACS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EBACS0006` (HTTP Error):

```json
{
  "code": "EBACS0006",
  "message": "HTTP request error"
}
```

500 Example `EBACS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EBACS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EBACS0023` (Transaction Database Error):

```json
{
  "code": "EBACS0023",
  "message": "Transaction database error"
}
```

500 Example `EBACS0048` (PSP Gateway Client Error):

```json
{
  "code": "EBACS0048",
  "message": "PSPGateway API returned 4xx error"
}
```

500 Example `EBACS0049` (PSP Gateway Server Error):

```json
{
  "code": "EBACS0049",
  "message": "PSPGateway API returned 5xx error"
}
```

##### Response 502

502 Example `EBACS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EBACS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 400 | `EBACS0095` | Partial returns are not allowed |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EBACS0086` | Missing required header: 'Idempotency-key' |
| 404 | `EBACS0067` | Transaction not found |
| 429 | `EBACS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EBACS0006` | HTTP request error |
| 500 | `EBACS0012` | PSPGateway API timeout error |
| 500 | `EBACS0023` | Transaction database error |
| 500 | `EBACS0048` | PSPGateway API returned 4xx error |
| 500 | `EBACS0049` | PSPGateway API returned 5xx error |
| 502 | `EBACS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-direct-credit-in-return-status-change-1` | https://developers.pismo.io/events/docs/bacs-direct-credit-in-return-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;429;500;502`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=GET path=/v1/payments/bacs/directcredit operationId=get-bacs-directcredit-list -->
### `GET /v1/payments/bacs/directcredit` — List BACS direct credit transactions [beta]

- **operationId:** `get-bacs-directcredit-list`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct credit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> List BACS direct credit transactions for an account.
>
> This endpoint takes an account token - an access token encoded with a Pismo account ID.  The account is parsed from the token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `id` | query | no | string | Transaction or mandate ID filter | maxLength: 36 |
| `status` | query | no | string | Transaction status filter | enum: ["CREATED", "PROCESSING", "SETTLED", "CANCELLED", "HOLD"] |
| `transactionType` | query | no | string | Direct debit transaction type filter | enum: ["DIRECTDEBIT_INBOUND", "DIRECTDEBIT_OUTBOUND", "DIRECTDEBIT_IN_RETURN", "DIRECTDEBIT_OUT_RETURN", "DIRECTDEBIT_IN_REVERSAL", "DIRECTDEBIT_OUT_REVERSAL"] |
| `beginDate` | query | no | string | Return records created on or after this date/time (RFC3339). | maxLength: 40; example: "2026-08-01T00:00:00Z" |
| `endDate` | query | no | string | Return records created on or before this date/time (RFC3339). | maxLength: 40; example: "2026-08-31T23:59:59Z" |
| `afterId` | query | no | string | Pagination cursor. Pass this field as a query parameter to get the next page. | maxLength: 2000 |
| `pageSize` | query | no | integer | Maximum number of items to return per page. Default is `10`. | default: 10; format: "int64"; minimum: 1; maximum: 100; example: 50 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of direct credit transactions | `application/json`: object (schema `listing.TransactionListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `listing.Transaction`) | no |  |  |
| `next_page` | boolean (schema `nextPage`) | no | Are there more results? | example: true |
| `after_id` | string (schema `afterId`) | no | Pagination cursor to pass as query parameter to get the next page<br> | example: "019e92ec-3362-7c54-9d17-89f5542a06e4" |

##### Response 400

400 Example `EBACS0004` (Validation Error):

```json
{
  "code": "EBACS0004",
  "message": "Validation error"
}
```

##### Response 403

403 Example `EBACS0002` (Missing Tenant Header):

```json
{
  "code": "EBACS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EBACS0085` (Missing Account Id):

```json
{
  "code": "EBACS0085",
  "message": "Missing required account-id"
}
```

##### Response 500

500 Example `EBACS0023` (Transaction Database Error):

```json
{
  "code": "EBACS0023",
  "message": "Transaction database error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0085` | Missing required account-id |
| 500 | `EBACS0023` | Transaction database error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/bacs_out.CreditorAccount -->
### Schema `bacs_out.CreditorAccount`

Pointer: `#/components/schemas/bacs_out.CreditorAccount`. Type: object (schema `bacs_out.CreditorAccount`).

> Creditor's account information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `creditorName`) | yes | Creditor name. | maxLength: 40; example: "Len Lease" |
| `scheme_name` | string (schema `schemeName`) | yes | Bank scheme that identifies the account.<br>  * `uk-scan` - Sort code and account number (SCAN) scheme<br>  * `bban` - Basic Bank Account Number scheme<br>  * `iban` - International Bank Account Number scheme<br> | enum: ["uk-scan", "bban", "iban"]; example: "iban" |
| `identification` | string (schema `schemeID`) | yes | Creditor's scheme value. A scheme identifies an account - UK-SCAN, IBAN, or BBAN. Refer to `schemeName` for details.<br><br>  * `uk-scan` - Sort code and account number (SCAN) scheme. Format: `sortcode + accountnumber`<br>  * `bban` - Basic Bank Account Number scheme. Format: `bankidentifier + branchidentifier + accountnumber`<br>  * `iban` - International Bank Account Number scheme. Format: `country code + check digits + bban`<br><br>For example, for an IBAN account `GB93UBKL12345612345678`, the identification would be:<br><br>  `iban`: `GB93UBKL12345612345678`<br>  `bban`: `UBKL12345612345678`<br>  `uk-scan`: `12345612345678`<br> | maxLength: 22; example: "AA00AAA000000000000000" |

<!-- schema: #/components/schemas/bacs_out.Currency -->
### Schema `bacs_out.Currency`

Pointer: `#/components/schemas/bacs_out.Currency`. Type: object (schema `bacs_out.Currency`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `amount`) | yes | Transaction amount. | example: 600 |
| `code` | string | no | Transaction currency (ISO 4217 3-letter code). | enum: ["GBP"]; example: "GBP" |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

<!-- schema: #/components/schemas/listing.Transaction -->
### Schema `listing.Transaction`

Pointer: `#/components/schemas/listing.Transaction`. Type: object (schema `listing.Transaction`).

> A BACS transaction record returned by the list endpoints.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `transactionId`) | no | Transaction ID | example: "019e92ec-3362-7c54-9d17-89f5542a06e4" |
| `org_id` | string (schema `orgId`) | no | Organization/tenant ID | example: "TN-KGIOODJD...1000" |
| `account_id` | integer (schema `accountId`) | no | Account ID | example: 12345678 |
| `transaction_type` | string (schema `transactionType`) | no | Transaction type | enum: ["DIRECTCREDIT_INBOUND", "DIRECTCREDIT_OUTBOUND", "DIRECTCREDIT_REVERSAL", "DIRECTCREDIT_OUTBOUND_REVERSAL", "DIRECTCREDIT_IN_RETURN", "DIRECTCREDIT_OUT_RETURN", "DIRECTDEBIT_OUTBOUND", "DIRECTDEBIT_OUT_RETURN"]; example: "DIRECTCREDIT_OUTBOUND" |
| `reference` | string (schema `reference`) | no | Reference note | example: "Weekly money for Mom" |
| `mandate_id` | string (schema `mandateId`) | no | Form3-assigned mandate ID | example: "b254bb5e-6f1a-4c2b-9c1e-2f0a6d3e8c11" |
| `payment_scheme` | string (schema `paymentScheme`) | no | Payment scheme | enum: ["BACS"]; example: "BACS" |
| `transaction_status` | string (schema `status`) | no | - `CREATED` - Payment has been created and is pending processing<br /><br>- `PROCESSING` - P2P balance was impacted and waiting for provider confirmation. For cashin, the transaction means the money will be credited on the next Working Day<br /><br>- `SETTLED` - Transaction completed processing and is settled<br /><br>- `CANCELLED` - Something went wrong and the transaction is cancelled. Refer to `reason` for more details<br /><br>- `HOLD` - The payment is on hold, pending further review<br /><br> | enum: ["CREATED", "PROCESSING", "SETTLED", "CANCELLED", "HOLD"]; example: "PROCESSING" |
| `amount` | number (schema `amount`) | no | Transaction amount. | example: 600 |
| `currency_code` | integer (schema `currencyCode`) | no | ISO 4217 numeric currency code | example: 826 |
| `processing_date` | string (schema `processingDate`) | no | Processing date. Format = yyyy-mm-dd | example: "2026-08-10" |
| `return_reason` | string (schema `returnReason`) | no | The reason for the return.<br>  * `account_closed` — The beneficiary account is no longer active.<br>  * `account_currency_mismatch` — The payment currency does not match the account currency.<br>  * `other` — A reason that the other specific codes do not cover.<br>  * `cancelled_by_payer`— The payer requests cancellation of the payment.<br> | enum: ["account_closed", "account_currency_mismatch", "cancelled_by_payer", "other"]; example: "account_closed" |
| `return_code` | string (schema `returnCode`) | no | ARUDD (Automated Return of Unpaid Direct Debit) return code:<br>  * `0` - Refer to payer<br>  * `1` - Instruction cancelled<br>  * `2` - Payer deceased<br>  * `3` - Account transferred<br>  * `4` - Advance notice disputed<br>  * `5` - No account<br>  * `6` - No instruction<br>  * `7` - Amount differs<br>  * `8` - Amount not due<br>  * `9` - Presentation overdue<br>  * `A` - Originator differs<br>  * `B` - Account closed<br> | enum: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B"]; example: "A" |
| `return_origin` | string (schema `returnOrigin`) | no | Indicates whether the client or the system initiates the return<br>  * `CLIENT`—The client initiates the return via this endpoint<br>  * `SYSTEM`—The system initiates the return automatically<br> | enum: ["CLIENT", "SYSTEM"]; example: "SYSTEM" |
| `original_transaction_id` | string (schema `originalTransactionId`) | no | Original transaction ID | example: "08ec4cf7-2d74-5453-80e0-e940ac8fc219" |
| `created_at` | string (schema `createdAtDateTime`) | no | Created at date-time. RFC 3339 format | format: "date-time"; example: "2026-08-05T10:15:00Z" |
| `updated_at` | string (schema `updatedAtDateTime`) | no | Updated at date-time. RFC 3339 format | format: "date-time"; example: "2026-08-05T10:15:00Z" |

<!-- schema: #/components/schemas/customer.DetailMessage -->
### Schema `customer.DetailMessage`

Pointer: `#/components/schemas/customer.DetailMessage`. Type: object (schema `customer.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `customer.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `customer.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `customer.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/customer.ExternalMessage -->
### Schema `customer.ExternalMessage`

Pointer: `#/components/schemas/customer.ExternalMessage`. Type: object (schema `customer.ExternalMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Code | example: "PBE315" |
| `message` | string | yes | Message | example: "Generic error" |

<!-- schema: #/components/schemas/customer.ParameterMessage -->
### Schema `customer.ParameterMessage`

Pointer: `#/components/schemas/customer.ParameterMessage`. Type: object (schema `customer.ParameterMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Field | example: "Query parameter" |
| `message` | string | yes | Message | example: "Generic error" |

<!-- schema: #/components/schemas/customer.PayloadMessage -->
### Schema `customer.PayloadMessage`

Pointer: `#/components/schemas/customer.PayloadMessage`. Type: object (schema `customer.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Field | example: "Entity.field" |
| `message` | string | yes | Message | example: "Generic error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Payment_rails_-_BACS_payments.yaml` | tag `BACS direct credit`: POST /v1/payments/bacs/directcredit/out, GET /v1/payments/bacs/directcredit/{id}, POST /v1/payments/bacs/directcredit/cancel/{id}, POST /v1/payments/bacs/directcredit/release/{id}, POST /v1/payments/bacs/directcredit/{id}/reversal, POST /v1/payments/bacs/directcredit/return/{id}, GET /v1/payments/bacs/directcredit | https://github.com/PismoDevEx/pismo-api-specs | `07915101c3111d71…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-ebacs` — Error codes: EBACS
- `KU-EVT-catalogue-bacs` — Event catalogue: bacs
- `KU-PAY-bacs` — BACS: clearing, Direct Debit mandates and indemnity claims
