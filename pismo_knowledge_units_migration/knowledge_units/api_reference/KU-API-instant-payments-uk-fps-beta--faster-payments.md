---
ku_id: KU-API-instant-payments-uk-fps-beta--faster-payments
title: 'API reference: Instant payments - Faster payments — Faster payments'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_UK_FPS_beta.yaml
  sha256: c65cc92bfad92bbd82792aa08177e46d412ba0918974c8922858b06ca823e0be
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
- post-create-fps
- post-cop-verification
- get-fps-in-transaction
- post-cancel-fps
- post-release-fps
- post-return-fps
related_kus:
- KU-BANK-banking-overview
- KU-ERR-codes-efps
- KU-EVT-catalogue-fps
- KU-EVT-faster-payments-events
- KU-PAY-faster-payment-system
specification_version: '1.0'
---

# API reference: Instant payments - Faster payments — Faster payments

**KU ID:** `KU-API-instant-payments-uk-fps-beta--faster-payments` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Faster payments` in `api-specs/Instant_payments_-_UK_FPS_beta.yaml` (“Instant payments - Faster payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Faster Payment Service (FPS) endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/payments/fps/out` | `post-create-fps` | Send Faster Payment [beta] | no |
| `POST /v1/payments/fps/cop` | `post-cop-verification` | Confirmation of payee [beta] | no |
| `GET /v1/payments/fps/{endToEndId}` | `get-fps-in-transaction` | Get FPS transaction [beta] | no |
| `POST /v1/payments/fps/cancel/{endToEndId}` | `post-cancel-fps` | Cancel FPS inbound transaction [beta] | no |
| `POST /v1/payments/fps/release/{endToEndId}` | `post-release-fps` | Release FPS inbound transaction [beta] | no |
| `POST /v1/payments/fps/return/{endToEndId}` | `post-return-fps` | Return FPS payment [beta] | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_UK_FPS_beta.yaml method=POST path=/v1/payments/fps/out operationId=post-create-fps -->
### `POST /v1/payments/fps/out` — Send Faster Payment [beta]

- **operationId:** `post-create-fps`
- **Specification:** `api-specs/Instant_payments_-_UK_FPS_beta.yaml` (Instant payments - Faster payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/fps`
- **Tags:** `Faster payments`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Send a Faster Payments payment.
>
> The Faster Payments System (FPS) is a UK service that allows near-instant electronic money transfers between banks.
>
> **Notes:**
>   * Before calling this endpoint, you **must** call [Confirmation of Payee](ref:post-cop-verification) to verify the payee.
>
>   * In case of failure, the transaction is updated with `status` = `CANCELLED`, and the `status_reason` field explains why.
>
>   * If the counterparty bank rejects the transaction, the transaction is still considered `SETTLED` and, when the provider webhook return is processed, a new [FPS out return](https://developers.pismo.io/events/docs/fps-fps-out-return-status-change-1)  event is generated and the amount is credited back to the debtor's account.
>
>   * This endpoint generates a [FPS out payment transaction](https://developers.pismo.io/events/docs/fps-fps-out-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token—token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |
| `Idempotency-key` | header | yes | string | A UUID to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |

#### Request body

Required: yes

> Send payment request body

**Content type `application/json`** — schema: object (schema `fps_out.FpsOutRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `end_to_end_id` | string (schema `endToEndID`) | yes | Client-generated transaction identifier. Must be unique for each transaction.<br> | maxLength: 31; example: "1374f841568e4ff4b3a63b023c170ec" |
| `creditor_account` | object (schema `fps_out.CreditorAccount`) | yes | Creditor's account information | pattern: "^[a-zA-Z0-9\\\\/\\\\-?:().,'+\\\\s#=!\\"%&*<>;{@\\\\r\\\\n]*$" |
| `scheme_payment_type` | string (schema `fps_out.SchemaPaymentType`) | yes | Payment scheme to be used.<br><br>* `ImmediatePayment` — Single Immediate Payment (SIP)<br><br>* `StandingOrder` — Standing Order Payment (SOP)<br><br>* `ForwardDatedPayment`— Forward Dated Payment (FDP)<br><br> | enum: ["ImmediatePayment", "StandingOrder", "ForwardDatedPayment"]; example: "ImmediatePayment" |
| `currency` | object (schema `fps_out.Currency`) | yes |  |  |
| `remittance_information` | object (schema `fps_out.RemittanceInformation`) | no |  |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Response Body | `application/json`: object (schema `fps_out.FpsOutResponse`) |
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
| `end_to_end_id` | string (schema `endToEndID`) | no | Client-generated transaction identifier. Must be unique for each transaction.<br> | maxLength: 31; example: "1374f841568e4ff4b3a63b023c170ec" |
| `status` | string (schema `status`) | no | - `CREATED` - Payment has been created and is pending processing<br>- `PROCESSING` - P2P balance was impacted and waiting for provider confirmation<br>- `SETTLED` - Transaction completed processing and is settled<br>- `CANCELLED` - Something went wrong and the transaction is cancelled. Refer to `reason` for more details<br>- `HOLD` - The payment is on hold, pending further review<br> | enum: ["CREATED", "PROCESSING", "SETTLED", "CANCELLED", "HOLD"]; example: "PROCESSING" |

##### Response 400

400 Example `EFPS0004` (Validation Error):

```json
{
  "code": "EFPS0004",
  "message": "Validation error"
}
```

400 Example `EFPS0016` (Unmarshal Error):

```json
{
  "code": "EFPS0016",
  "message": "Unmarshal error"
}
```

400 Example `EFPS0019` (Accounts API Invalid Request Error):

```json
{
  "code": "EFPS0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EFPS0025` (P2P API Invalid Request Error):

```json
{
  "code": "EFPS0025",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EFPS0029` (Ledger API Invalid Request Error):

```json
{
  "code": "EFPS0029",
  "message": "Ledger - API returned 4xx error"
}
```

400 Example `EFPS0037` (Invalid Creditor Sort Code Account Number):

```json
{
  "code": "EFPS0037",
  "message": "Invalid creditor sort code/account number"
}
```

400 Example `EFPS0038` (Invalid Creditor IBAN):

```json
{
  "code": "EFPS0038",
  "message": "Invalid creditor IBAN"
}
```

400 Example `EFPS0039` (Invalid Creditor BBAN):

```json
{
  "code": "EFPS0039",
  "message": "Invalid creditor BBAN"
}
```

400 Example `EFPS0046` (IntlBankAccounts API Invalid Request Error):

```json
{
  "code": "EFPS0046",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EFPS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EFPS0047",
  "message": "Invalid FPS Request. Check error details for more information."
}
```

400 Example `EFPS0073` (Amount Greater Than Balance):

```json
{
  "code": "EFPS0073",
  "message": "The amount passed is greater than the current balance"
}
```

##### Response 403

403 Example `EFPS0002` (Missing Tenant Header):

```json
{
  "code": "EFPS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EFPS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EFPS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EFPS0033` (Invalid Account Id):

```json
{
  "code": "EFPS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EFPS0034` (Invalid Idempotency Key):

```json
{
  "code": "EFPS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EFPS0035` (Account Has No Active Addresses):

```json
{
  "code": "EFPS0035",
  "message": "Account has no active addresses"
}
```

403 Example `EFPS0040` (FPS Not Enabled):

```json
{
  "code": "EFPS0040",
  "message": "FPS is not enabled for the creditor sort code"
}
```

403 Example `EFPS0041` (Modulus Check Error):

```json
{
  "code": "EFPS0041",
  "message": "Failed to execute account number modulus check"
}
```

##### Response 404

404 Example `EFPS0010` (Sort Code Not Found):

```json
{
  "code": "EFPS0010",
  "message": "Sort Code not found"
}
```

404 Example `EFPS0018` (Accounts API Not Found Error):

```json
{
  "code": "EFPS0018",
  "message": "Accounts - Not found"
}
```

404 Example `EFPS0028` (Ledger API Not Found Error):

```json
{
  "code": "EFPS0028",
  "message": "Ledger - Not found"
}
```

404 Example `EFPS0031` (IntlBankAccounts API Not Found Error):

```json
{
  "code": "EFPS0031",
  "message": "IntlBankAccounts - Not found"
}
```

##### Response 409

409 Example `EFPS0022` (Transaction Already Exists):

```json
{
  "code": "EFPS0022",
  "message": "A transaction with the specified idempotency key and end_to_end_id already exists"
}
```

409 Example `EFPS0036` (Mismatching Currency Error):

```json
{
  "code": "EFPS0036",
  "message": "The provided currency does not match with the account's configured currency"
}
```

##### Response 429

429 Example `EFPS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EFPS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EFPS0006` (HTTP Error):

```json
{
  "code": "EFPS0006",
  "message": "HTTP request error"
}
```

500 Example `EFPS0009` (IntlBankAccounts API Timeout):

```json
{
  "code": "EFPS0009",
  "message": "IntlBankAccounts API timeout error"
}
```

500 Example `EFPS0011` (IntlBankAccounts API Internal Error):

```json
{
  "code": "EFPS0011",
  "message": "IntlBankAccounts API Internal Server error"
}
```

500 Example `EFPS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EFPS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EFPS0017` (Accounts API Timeout):

```json
{
  "code": "EFPS0017",
  "message": "Accounts API timeout error"
}
```

500 Example `EFPS0020` (Accounts API Server Error):

```json
{
  "code": "EFPS0020",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EFPS0023` (Transaction Database Error):

```json
{
  "code": "EFPS0023",
  "message": "Transaction database error"
}
```

500 Example `EFPS0024` (P2P API Timeout):

```json
{
  "code": "EFPS0024",
  "message": "P2p - API timeout error"
}
```

500 Example `EFPS0026` (P2P API Server Error):

```json
{
  "code": "EFPS0026",
  "message": "P2p - API returned 5xx error"
}
```

500 Example `EFPS0027` (Ledger API Timeout):

```json
{
  "code": "EFPS0027",
  "message": "Ledger API timeout error"
}
```

500 Example `EFPS0030` (Ledger API Server Error):

```json
{
  "code": "EFPS0030",
  "message": "Ledger - API returned 5xx error"
}
```

500 Example `EFPS0032` (IntlBankAccounts API Server Error):

```json
{
  "code": "EFPS0032",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

##### Response 502

502 Example `EFPS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EFPS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFPS0004` | Validation error |
| 400 | `EFPS0016` | Unmarshal error |
| 400 | `EFPS0019` | Accounts - API returned 4xx error |
| 400 | `EFPS0025` | P2p - API returned 4xx error |
| 400 | `EFPS0029` | Ledger - API returned 4xx error |
| 400 | `EFPS0037` | Invalid creditor sort code/account number |
| 400 | `EFPS0038` | Invalid creditor IBAN |
| 400 | `EFPS0039` | Invalid creditor BBAN |
| 400 | `EFPS0046` | IntlBankAccounts - API returned 4xx error |
| 400 | `EFPS0047` | Invalid FPS Request. Check error details for more information. |
| 400 | `EFPS0073` | The amount passed is greater than the current balance |
| 403 | `EFPS0002` | Missing required header: 'x-tenant' |
| 403 | `EFPS0021` | Account blocked or cancelled |
| 403 | `EFPS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EFPS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EFPS0035` | Account has no active addresses |
| 403 | `EFPS0040` | FPS is not enabled for the creditor sort code |
| 403 | `EFPS0041` | Failed to execute account number modulus check |
| 404 | `EFPS0010` | Sort Code not found |
| 404 | `EFPS0018` | Accounts - Not found |
| 404 | `EFPS0028` | Ledger - Not found |
| 404 | `EFPS0031` | IntlBankAccounts - Not found |
| 409 | `EFPS0022` | A transaction with the specified idempotency key and end_to_end_id already exists |
| 409 | `EFPS0036` | The provided currency does not match with the account's configured currency |
| 429 | `EFPS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EFPS0006` | HTTP request error |
| 500 | `EFPS0009` | IntlBankAccounts API timeout error |
| 500 | `EFPS0011` | IntlBankAccounts API Internal Server error |
| 500 | `EFPS0012` | PSPGateway API timeout error |
| 500 | `EFPS0017` | Accounts API timeout error |
| 500 | `EFPS0020` | Accounts - API returned 5xx error |
| 500 | `EFPS0023` | Transaction database error |
| 500 | `EFPS0024` | P2p - API timeout error |
| 500 | `EFPS0026` | P2p - API returned 5xx error |
| 500 | `EFPS0027` | Ledger API timeout error |
| 500 | `EFPS0030` | Ledger - API returned 5xx error |
| 500 | `EFPS0032` | IntlBankAccounts - API returned 5xx error |
| 502 | `EFPS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `fps-fps-out-return-status-change-1` | https://developers.pismo.io/events/docs/fps-fps-out-return-status-change-1 |
| `fps-fps-out-status-change-1` | https://developers.pismo.io/events/docs/fps-fps-out-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;409;429;500;502`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-overview`, `KU-EVT-faster-payments-events`, `KU-PAY-faster-payment-system`.

<!-- op: spec=api-specs/Instant_payments_-_UK_FPS_beta.yaml method=POST path=/v1/payments/fps/cop operationId=post-cop-verification -->
### `POST /v1/payments/fps/cop` — Confirmation of payee [beta]

- **operationId:** `post-cop-verification`
- **Specification:** `api-specs/Instant_payments_-_UK_FPS_beta.yaml` (Instant payments - Faster payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/fps`
- **Tags:** `Faster payments`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Verify a beneficiary's account name before making an FPS payment using the [Confirmation of Payee (CoP)](https://www.wearepay.uk/what-we-do/overlay-services/confirmation-of-payee/) service.
>
> CoP allows payers to check that the name they have for the intended recipient matches the actual name on the recipient's account, reducing the risk of fraud and misdirected payments.
>
> This verification does not create an FPS payment transaction. The request is forwarded to the payment provider for real-time name verification.
>
> This endpoint generates a [CoP name verification requested](https://developers.pismo.io/events/docs/fps-cop-name-verification-submissions-1) event. The result is received in a [CoP name verification result received](https://developers.pismo.io/events/docs/fps-cop-name-verification-admissions-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token—token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |
| `x-tenant` | header | yes | string | Organization ID |  |
| `Idempotency-key` | header | yes | string | A UUID to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |
| `x-cid` | header | no | string | Request tracking identifier. If not provided, a random UUID will be generated.<br> |  |

#### Request body

Required: yes

> COP verification request body

**Content type `application/json`** — schema: object (schema `cop.COPVerificationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `cop.ID`) | yes | UUID identifier for this COP verification request. | format: "uuid"; maxLength: 36; example: "4942f12c-5430-4d1b-8b56-c7f1c8a9118d" |
| `account_classification` | string (schema `cop.AccountClassification`) | yes | Account classification type | enum: ["personal", "business"]; example: "personal" |
| `account_number` | string (schema `cop.AccountNumber`) | yes | BBAN account number (exactly 8 numeric characters) | pattern: "^[0-9]{8}$"; minLength: 8; maxLength: 8; example: "12345678" |
| `account_number_code` | string (schema `cop.AccountNumberCode`) | yes | Account number format code.<br>* `BBAN` - Basic Bank Account Number. Currently the only supported format.<br> | enum: ["BBAN"]; example: "BBAN" |
| `bank_id` | string (schema `cop.BankID`) | yes | Bank identifier - sort code (exactly 6 numeric characters). | pattern: "^[0-9]{6}$"; minLength: 6; maxLength: 6; example: "123456" |
| `bank_id_code` | string (schema `cop.BankIdCode`) | yes | Bank identifier code type<br>* `GBDSC`—Great Britain Domestic Sort Code. Currently the only supported format.<br> | enum: ["GBDSC"]; example: "GBDSC" |
| `name` | string (schema `cop.Name`) | yes | Account name to verify<br> | maxLength: 135; example: "Doe Reetos" |
| `secondary_identification` | string (schema `cop.SecondaryID`) | no | Secondary reference to identify the account, such as a roll number for building society accounts. A building society roll number is a unique alphanumeric identifier—often 10-12 digits or a mix of letters and numbers—used to identify specific savings or mortgage accounts.<br> | maxLength: 35; example: "A1B2C3D" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | COP verification result | `application/json`: object (schema `cop.COPVerificationResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `cop.Status`) | no | COP request status<br>  * `confirmed`—Verification request was delivered and a response received.<br>  * `delivery_failed`—Verification request could not be delivered.<br> | enum: ["confirmed", "delivery_failed"]; example: "confirmed" |
| `answer` | string (schema `cop.Answer`) | no | Verification result:<br>* `match`—Name matches the account holder.<br>* `close_match`—Close match<br>* `no_match`—Does not match<br>* `rejected`—Verification was rejected.<br> | enum: ["match", "close_match", "no_match", "rejected"]; example: "match" |
| `actual_name` | string (schema `cop.ActualName`) | no | Actual name on the account. Returned for `close_match` or `no_match` results. | example: "Mabel Syrup" |
| `name_in_request` | array of string (schema `cop.NameInResponse`) | no |  | example: ["Tam Arind"] |
| `reason_code` | string (schema `cop.ReasonCode`) | no | Reason code for the verification result. Known values include (non-exhaustive):<br><br>    * `AC01` - No account with the given account number<br><br>    * `ACNS` - Account does not support Confirmation of Payee<br><br>    * `ANNM` - String does not match the account name<br><br>    * `BAMM` - Close match to the account name. Account type is Business when Personal was indicated<br><br>    * `BANM` - Match to the account name, but account type is Business when Personal was indicated<br><br>    * `CASS` - Account has been switched to a different organisation<br><br>    * `IVCR` - Invalid secondary customer reference data<br><br>    * `MBAM` - Close match to the account name<br><br>    * `OPTO` - Account opted out of Confirmation of Payee<br><br>    * `PAMM` - Close match to the account name. Account type is Personal when Business was indicated<br><br>    * `PANM` - Match to the account name, but account type is Personal when Business was indicated<br><br>    * `SCNS` - Organisation doesn't own the passed sort code<br><br>example: "MBAM"<br> |  |
| `reason` | string (schema `cop.Reason`) | no | Human-readable reason description | example: "String is a close match to the account" |
| `sort_code_validation` | object | no | Sort code and account number validation result. |  |
| `sort_code_validation.status` | string | no | Validation status. | enum: ["VALID", "INVALID"]; example: "VALID" |
| `sort_code_validation.bank_code` | string | no | Bank code identifier. | example: "1234" |
| `sort_code_validation.bank_name` | string | no | Bank name. | example: "NATIONAL WESTMINSTER BANK PLC" |
| `sort_code_validation.bank_office_title` | string | no | Bank branch office title. | example: "LONDON OFFICE" |
| `sort_code_validation.fps_supported` | boolean | no | Does the bank support Faster Payments? | example: true |
| `sort_code_validation.messages` | array of string | no | Validation error messages when status is `INVALID`. | example: ["Some message"] |

200 Example `match` (Name matches the account holder):

```json
{
  "status": "confirmed",
  "answer": "match",
  "name_in_request": [
    "Penny Loafer"
  ],
  "sort_code_validation": {
    "status": "VALID",
    "bank_code": "1234",
    "bank_name": "NATIONAL WESTMINSTER BANK PLC",
    "bank_office_title": "LONDON OFFICE",
    "fps_supported": true,
    "messages": []
  }
}
```

200 Example `close_match` (Name is a close match):

```json
{
  "status": "confirmed",
  "answer": "close_match",
  "actual_name": "Al Mond",
  "name_in_request": [
    "Al Mnd"
  ],
  "reason_code": "MBAM",
  "reason": "String is a close match to the account",
  "sort_code_validation": {
    "status": "VALID",
    "bank_code": "1234",
    "bank_name": "NATIONAL WESTMINSTER BANK PLC",
    "bank_office_title": "LONDON OFFICE",
    "fps_supported": true,
    "messages": []
  }
}
```

200 Example `no_match` (Name does not match):

```json
{
  "status": "confirmed",
  "answer": "no_match",
  "actual_name": "Mac Adamia",
  "name_in_request": [
    "Al Mond"
  ],
  "reason_code": "ANNM",
  "reason": "Account name does not match",
  "sort_code_validation": {
    "status": "INVALID",
    "bank_code": "",
    "bank_name": "",
    "bank_office_title": "",
    "fps_supported": false,
    "messages": [
      "MOD check failed"
    ]
  }
}
```

##### Response 400

400 Example `EFPS0004` (Validation Error):

```json
{
  "code": "EFPS0004",
  "message": "Validation error"
}
```

400 Example `EFPS0016` (Unmarshal Error):

```json
{
  "code": "EFPS0016",
  "message": "Unmarshal error"
}
```

##### Response 403

403 Example `EFPS0002` (Missing Tenant Header):

```json
{
  "code": "EFPS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EFPS0086` (Missing Idempotency Key):

```json
{
  "code": "EFPS0086",
  "message": "Missing required header: 'Idempotency-Key'"
}
```

##### Response 409

409 Example `EFPS0058` (Record Already Exists):

```json
{
  "code": "EFPS0058",
  "message": "Record already exists"
}
```

##### Response 429

429 Example `EFPS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EFPS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EFPS0006` (HTTP Error):

```json
{
  "code": "EFPS0006",
  "message": "HTTP request error"
}
```

500 Example `EFPS0023` (Database Error):

```json
{
  "code": "EFPS0023",
  "message": "Transaction database error"
}
```

##### Response 502

502 Example `EFPS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EFPS0014",
  "message": "PSPGateway API Bad Gateway"
}
```

##### Response 504

504 Example `EFPS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EFPS0012",
  "message": "PSPGateway API timeout error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFPS0004` | Validation error |
| 400 | `EFPS0016` | Unmarshal error |
| 403 | `EFPS0002` | Missing required header: 'x-tenant' |
| 403 | `EFPS0086` | Missing required header: 'Idempotency-Key' |
| 409 | `EFPS0058` | Record already exists |
| 429 | `EFPS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EFPS0006` | HTTP request error |
| 500 | `EFPS0023` | Transaction database error |
| 502 | `EFPS0014` | PSPGateway API Bad Gateway |
| 504 | `EFPS0012` | PSPGateway API timeout error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `fps-cop-name-verification-admissions-1` | https://developers.pismo.io/events/docs/fps-cop-name-verification-admissions-1 |
| `fps-cop-name-verification-submissions-1` | https://developers.pismo.io/events/docs/fps-cop-name-verification-submissions-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;409;429;500;502;504`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-PAY-faster-payment-system`.

<!-- op: spec=api-specs/Instant_payments_-_UK_FPS_beta.yaml method=GET path=/v1/payments/fps/{endToEndId} operationId=get-fps-in-transaction -->
### `GET /v1/payments/fps/{endToEndId}` — Get FPS transaction [beta]

- **operationId:** `get-fps-in-transaction`
- **Specification:** `api-specs/Instant_payments_-_UK_FPS_beta.yaml` (Instant payments - Faster payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/fps`
- **Tags:** `Faster payments`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Gets a FPS transaction given its end-to-end identifier in the path.
>
> The Faster Payments System (FPS) is a UK service that allows near-instant electronic money transfers between banks.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token—token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |
| `x-tenant` | header | yes | string | Organization ID |  |
| `x-cid` | header | no | string | Request tracking identifier. If not provided, a random UUID will be generated.<br> |  |
| `endToEndId` | path | yes | string | FPS transaction's end to end ID. | maxLength: 31 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `fps_get.FpsGetResponse`) |
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
| `end_to_end_id` | string (schema `endToEndID`) | no | Client-generated transaction identifier. Must be unique for each transaction.<br> | maxLength: 31; example: "1374f841568e4ff4b3a63b023c170ec" |
| `status` | string (schema `status`) | no | - `CREATED` - Payment has been created and is pending processing<br>- `PROCESSING` - P2P balance was impacted and waiting for provider confirmation<br>- `SETTLED` - Transaction completed processing and is settled<br>- `CANCELLED` - Something went wrong and the transaction is cancelled. Refer to `reason` for more details<br>- `HOLD` - The payment is on hold, pending further review<br> | enum: ["CREATED", "PROCESSING", "SETTLED", "CANCELLED", "HOLD"]; example: "PROCESSING" |
| `amount` | number (schema `Amount`) | no | Transaction amount | example: 853.09 |

##### Response 400

400 Example `EFPS0004` (Validation Error):

```json
{
  "code": "EFPS0004",
  "message": "Validation error"
}
```

400 Example `EFPS0016` (Unmarshal Error):

```json
{
  "code": "EFPS0016",
  "message": "Unmarshal error"
}
```

400 Example `EFPS0019` (Accounts API Invalid Request Error):

```json
{
  "code": "EFPS0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EFPS0025` (P2P API Invalid Request Error):

```json
{
  "code": "EFPS0025",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EFPS0029` (Ledger API Invalid Request Error):

```json
{
  "code": "EFPS0029",
  "message": "Ledger - API returned 4xx error"
}
```

400 Example `EFPS0037` (Invalid Creditor Sort Code Account Number):

```json
{
  "code": "EFPS0037",
  "message": "Invalid creditor sort code/account number"
}
```

400 Example `EFPS0038` (Invalid Creditor IBAN):

```json
{
  "code": "EFPS0038",
  "message": "Invalid creditor IBAN"
}
```

400 Example `EFPS0039` (Invalid Creditor BBAN):

```json
{
  "code": "EFPS0039",
  "message": "Invalid creditor BBAN"
}
```

400 Example `EFPS0046` (IntlBankAccounts API Invalid Request Error):

```json
{
  "code": "EFPS0046",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EFPS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EFPS0047",
  "message": "Invalid FPS Request. Check error details for more information."
}
```

##### Response 403

403 Example `EFPS0002` (Missing Tenant Header):

```json
{
  "code": "EFPS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EFPS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EFPS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EFPS0033` (Invalid Account Id):

```json
{
  "code": "EFPS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EFPS0034` (Invalid Idempotency Key):

```json
{
  "code": "EFPS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EFPS0035` (Account Has No Active Addresses):

```json
{
  "code": "EFPS0035",
  "message": "Account has no active addresses"
}
```

403 Example `EFPS0040` (FPS Not Enabled):

```json
{
  "code": "EFPS0040",
  "message": "FPS is not enabled for the creditor sort code"
}
```

403 Example `EFPS0041` (Modulus Check Error):

```json
{
  "code": "EFPS0041",
  "message": "Failed to execute account number modulus check"
}
```

##### Response 404

404 Example `EFPS0010` (Sort Code Not Found):

```json
{
  "code": "EFPS0010",
  "message": "Sort Code not found"
}
```

404 Example `EFPS0018` (Accounts API Not Found Error):

```json
{
  "code": "EFPS0018",
  "message": "Accounts - Not found"
}
```

404 Example `EFPS0028` (Ledger API Not Found Error):

```json
{
  "code": "EFPS0028",
  "message": "Ledger - Not found"
}
```

404 Example `EFPS0031` (IntlBankAccounts API Not Found Error):

```json
{
  "code": "EFPS0031",
  "message": "IntlBankAccounts - Not found"
}
```

##### Response 409

409 Example `EFPS0022` (Transaction Already Exists):

```json
{
  "code": "EFPS0022",
  "message": "A transaction with the specified idempotency key and end_to_end_id already exists"
}
```

409 Example `EFPS0036` (Mismatching Currency Error):

```json
{
  "code": "EFPS0036",
  "message": "The provided currency does not match with the account's configured currency"
}
```

##### Response 429

429 Example `EFPS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EFPS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EFPS0006` (HTTP Error):

```json
{
  "code": "EFPS0006",
  "message": "HTTP request error"
}
```

500 Example `EFPS0009` (IntlBankAccounts API Timeout):

```json
{
  "code": "EFPS0009",
  "message": "IntlBankAccounts API timeout error"
}
```

500 Example `EFPS0011` (IntlBankAccounts API Internal Error):

```json
{
  "code": "EFPS0011",
  "message": "IntlBankAccounts API Internal Server error"
}
```

500 Example `EFPS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EFPS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EFPS0017` (Accounts API Timeout):

```json
{
  "code": "EFPS0017",
  "message": "Accounts API timeout error"
}
```

500 Example `EFPS0020` (Accounts API Server Error):

```json
{
  "code": "EFPS0020",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EFPS0023` (Transaction Database Error):

```json
{
  "code": "EFPS0023",
  "message": "Transaction database error"
}
```

500 Example `EFPS0024` (P2P API Timeout):

```json
{
  "code": "EFPS0024",
  "message": "P2p - API timeout error"
}
```

500 Example `EFPS0026` (P2P API Server Error):

```json
{
  "code": "EFPS0026",
  "message": "P2p - API returned 5xx error"
}
```

500 Example `EFPS0027` (Ledger API Timeout):

```json
{
  "code": "EFPS0027",
  "message": "Ledger API timeout error"
}
```

500 Example `EFPS0030` (Ledger API Server Error):

```json
{
  "code": "EFPS0030",
  "message": "Ledger - API returned 5xx error"
}
```

500 Example `EFPS0032` (IntlBankAccounts API Server Error):

```json
{
  "code": "EFPS0032",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

##### Response 502

502 Example `EFPS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EFPS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFPS0004` | Validation error |
| 400 | `EFPS0016` | Unmarshal error |
| 400 | `EFPS0019` | Accounts - API returned 4xx error |
| 400 | `EFPS0025` | P2p - API returned 4xx error |
| 400 | `EFPS0029` | Ledger - API returned 4xx error |
| 400 | `EFPS0037` | Invalid creditor sort code/account number |
| 400 | `EFPS0038` | Invalid creditor IBAN |
| 400 | `EFPS0039` | Invalid creditor BBAN |
| 400 | `EFPS0046` | IntlBankAccounts - API returned 4xx error |
| 400 | `EFPS0047` | Invalid FPS Request. Check error details for more information. |
| 403 | `EFPS0002` | Missing required header: 'x-tenant' |
| 403 | `EFPS0021` | Account blocked or cancelled |
| 403 | `EFPS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EFPS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EFPS0035` | Account has no active addresses |
| 403 | `EFPS0040` | FPS is not enabled for the creditor sort code |
| 403 | `EFPS0041` | Failed to execute account number modulus check |
| 404 | `EFPS0010` | Sort Code not found |
| 404 | `EFPS0018` | Accounts - Not found |
| 404 | `EFPS0028` | Ledger - Not found |
| 404 | `EFPS0031` | IntlBankAccounts - Not found |
| 409 | `EFPS0022` | A transaction with the specified idempotency key and end_to_end_id already exists |
| 409 | `EFPS0036` | The provided currency does not match with the account's configured currency |
| 429 | `EFPS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EFPS0006` | HTTP request error |
| 500 | `EFPS0009` | IntlBankAccounts API timeout error |
| 500 | `EFPS0011` | IntlBankAccounts API Internal Server error |
| 500 | `EFPS0012` | PSPGateway API timeout error |
| 500 | `EFPS0017` | Accounts API timeout error |
| 500 | `EFPS0020` | Accounts - API returned 5xx error |
| 500 | `EFPS0023` | Transaction database error |
| 500 | `EFPS0024` | P2p - API timeout error |
| 500 | `EFPS0026` | P2p - API returned 5xx error |
| 500 | `EFPS0027` | Ledger API timeout error |
| 500 | `EFPS0030` | Ledger - API returned 5xx error |
| 500 | `EFPS0032` | IntlBankAccounts - API returned 5xx error |
| 502 | `EFPS0014` | PSPGateway API Bad Gateway |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;429;500;502`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_UK_FPS_beta.yaml method=POST path=/v1/payments/fps/cancel/{endToEndId} operationId=post-cancel-fps -->
### `POST /v1/payments/fps/cancel/{endToEndId}` — Cancel FPS inbound transaction [beta]

- **operationId:** `post-cancel-fps`
- **Specification:** `api-specs/Instant_payments_-_UK_FPS_beta.yaml` (Instant payments - Faster payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/fps`
- **Tags:** `Faster payments`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Call this endpoint to cancel the suspended transaction which was kept on hold based on client's antifraud provider analysis and  return the transaction.
>
> This endpoint generates a [FPS inbound payment processed](https://developers.pismo.io/events/docs/fps-fps-in-status-change-1) event with `status` = `CANCELLED`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token—token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |
| `x-tenant` | header | yes | string | Organization ID |  |
| `endToEndId` | path | yes | string | FPS transaction's end to end ID. | maxLength: 31 |
| `x-cid` | header | no | string | Request tracking identifier. If not provided, a random UUID will be generated.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `fps_cancel.FpsCancelResponse`) |
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
| `end_to_end_id` | string (schema `endToEndID`) | no | Client-generated transaction identifier. Must be unique for each transaction.<br> | maxLength: 31; example: "1374f841568e4ff4b3a63b023c170ec" |
| `status` | string (schema `fps_cancel.status`) | no | - `CANCELLED` - Something went wrong and the transaction was cancelled. Refer to `reason` for details,<br> | enum: ["CANCELLED"]; example: "CANCELLED" |

##### Response 400

400 Example `EFPS0004` (Validation Error):

```json
{
  "code": "EFPS0004",
  "message": "Validation error"
}
```

400 Example `EFPS0016` (Unmarshal Error):

```json
{
  "code": "EFPS0016",
  "message": "Unmarshal error"
}
```

400 Example `EFPS0019` (Accounts API Invalid Request Error):

```json
{
  "code": "EFPS0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EFPS0025` (P2P API Invalid Request Error):

```json
{
  "code": "EFPS0025",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EFPS0029` (Ledger API Invalid Request Error):

```json
{
  "code": "EFPS0029",
  "message": "Ledger - API returned 4xx error"
}
```

400 Example `EFPS0037` (Invalid Creditor Sort Code Account Number):

```json
{
  "code": "EFPS0037",
  "message": "Invalid creditor sort code/account number"
}
```

400 Example `EFPS0038` (Invalid Creditor IBAN):

```json
{
  "code": "EFPS0038",
  "message": "Invalid creditor IBAN"
}
```

400 Example `EFPS0039` (Invalid Creditor BBAN):

```json
{
  "code": "EFPS0039",
  "message": "Invalid creditor BBAN"
}
```

400 Example `EFPS0046` (IntlBankAccounts API Invalid Request Error):

```json
{
  "code": "EFPS0046",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EFPS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EFPS0047",
  "message": "Invalid FPS Request. Check error details for more information."
}
```

##### Response 403

403 Example `EFPS0002` (Missing Tenant Header):

```json
{
  "code": "EFPS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EFPS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EFPS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EFPS0033` (Invalid Account Id):

```json
{
  "code": "EFPS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EFPS0034` (Invalid Idempotency Key):

```json
{
  "code": "EFPS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EFPS0035` (Account Has No Active Addresses):

```json
{
  "code": "EFPS0035",
  "message": "Account has no active addresses"
}
```

403 Example `EFPS0040` (FPS Not Enabled):

```json
{
  "code": "EFPS0040",
  "message": "FPS is not enabled for the creditor sort code"
}
```

403 Example `EFPS0041` (Modulus Check Error):

```json
{
  "code": "EFPS0041",
  "message": "Failed to execute account number modulus check"
}
```

##### Response 404

404 Example `EFPS0010` (Sort Code Not Found):

```json
{
  "code": "EFPS0010",
  "message": "Sort Code not found"
}
```

404 Example `EFPS0018` (Accounts API Not Found Error):

```json
{
  "code": "EFPS0018",
  "message": "Accounts - Not found"
}
```

404 Example `EFPS0028` (Ledger API Not Found Error):

```json
{
  "code": "EFPS0028",
  "message": "Ledger - Not found"
}
```

404 Example `EFPS0031` (IntlBankAccounts API Not Found Error):

```json
{
  "code": "EFPS0031",
  "message": "IntlBankAccounts - Not found"
}
```

##### Response 409

409 Example `EFPS0022` (Transaction Already Exists):

```json
{
  "code": "EFPS0022",
  "message": "A transaction with the specified idempotency key and end_to_end_id already exists"
}
```

409 Example `EFPS0036` (Mismatching Currency Error):

```json
{
  "code": "EFPS0036",
  "message": "The provided currency does not match with the account's configured currency"
}
```

409 Example `EFPS0095` (Transaction Not on Hold for Cancel):

```json
{
  "code": "EFPS0095",
  "message": "Transaction status is not HOLD, cancel is not allowed"
}
```

##### Response 429

429 Example `EFPS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EFPS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EFPS0006` (HTTP Error):

```json
{
  "code": "EFPS0006",
  "message": "HTTP request error"
}
```

500 Example `EFPS0009` (IntlBankAccounts API Timeout):

```json
{
  "code": "EFPS0009",
  "message": "IntlBankAccounts API timeout error"
}
```

500 Example `EFPS0011` (IntlBankAccounts API Internal Error):

```json
{
  "code": "EFPS0011",
  "message": "IntlBankAccounts API Internal Server error"
}
```

500 Example `EFPS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EFPS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EFPS0017` (Accounts API Timeout):

```json
{
  "code": "EFPS0017",
  "message": "Accounts API timeout error"
}
```

500 Example `EFPS0020` (Accounts API Server Error):

```json
{
  "code": "EFPS0020",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EFPS0023` (Transaction Database Error):

```json
{
  "code": "EFPS0023",
  "message": "Transaction database error"
}
```

500 Example `EFPS0024` (P2P API Timeout):

```json
{
  "code": "EFPS0024",
  "message": "P2p - API timeout error"
}
```

500 Example `EFPS0026` (P2P API Server Error):

```json
{
  "code": "EFPS0026",
  "message": "P2p - API returned 5xx error"
}
```

500 Example `EFPS0027` (Ledger API Timeout):

```json
{
  "code": "EFPS0027",
  "message": "Ledger API timeout error"
}
```

500 Example `EFPS0030` (Ledger API Server Error):

```json
{
  "code": "EFPS0030",
  "message": "Ledger - API returned 5xx error"
}
```

500 Example `EFPS0032` (IntlBankAccounts API Server Error):

```json
{
  "code": "EFPS0032",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

##### Response 502

502 Example `EFPS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EFPS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFPS0004` | Validation error |
| 400 | `EFPS0016` | Unmarshal error |
| 400 | `EFPS0019` | Accounts - API returned 4xx error |
| 400 | `EFPS0025` | P2p - API returned 4xx error |
| 400 | `EFPS0029` | Ledger - API returned 4xx error |
| 400 | `EFPS0037` | Invalid creditor sort code/account number |
| 400 | `EFPS0038` | Invalid creditor IBAN |
| 400 | `EFPS0039` | Invalid creditor BBAN |
| 400 | `EFPS0046` | IntlBankAccounts - API returned 4xx error |
| 400 | `EFPS0047` | Invalid FPS Request. Check error details for more information. |
| 403 | `EFPS0002` | Missing required header: 'x-tenant' |
| 403 | `EFPS0021` | Account blocked or cancelled |
| 403 | `EFPS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EFPS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EFPS0035` | Account has no active addresses |
| 403 | `EFPS0040` | FPS is not enabled for the creditor sort code |
| 403 | `EFPS0041` | Failed to execute account number modulus check |
| 404 | `EFPS0010` | Sort Code not found |
| 404 | `EFPS0018` | Accounts - Not found |
| 404 | `EFPS0028` | Ledger - Not found |
| 404 | `EFPS0031` | IntlBankAccounts - Not found |
| 409 | `EFPS0022` | A transaction with the specified idempotency key and end_to_end_id already exists |
| 409 | `EFPS0036` | The provided currency does not match with the account's configured currency |
| 409 | `EFPS0095` | Transaction status is not HOLD, cancel is not allowed |
| 429 | `EFPS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EFPS0006` | HTTP request error |
| 500 | `EFPS0009` | IntlBankAccounts API timeout error |
| 500 | `EFPS0011` | IntlBankAccounts API Internal Server error |
| 500 | `EFPS0012` | PSPGateway API timeout error |
| 500 | `EFPS0017` | Accounts API timeout error |
| 500 | `EFPS0020` | Accounts - API returned 5xx error |
| 500 | `EFPS0023` | Transaction database error |
| 500 | `EFPS0024` | P2p - API timeout error |
| 500 | `EFPS0026` | P2p - API returned 5xx error |
| 500 | `EFPS0027` | Ledger API timeout error |
| 500 | `EFPS0030` | Ledger - API returned 5xx error |
| 500 | `EFPS0032` | IntlBankAccounts - API returned 5xx error |
| 502 | `EFPS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `fps-fps-in-status-change-1` | https://developers.pismo.io/events/docs/fps-fps-in-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;429;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-faster-payment-system`.

<!-- op: spec=api-specs/Instant_payments_-_UK_FPS_beta.yaml method=POST path=/v1/payments/fps/release/{endToEndId} operationId=post-release-fps -->
### `POST /v1/payments/fps/release/{endToEndId}` — Release FPS inbound transaction [beta]

- **operationId:** `post-release-fps`
- **Specification:** `api-specs/Instant_payments_-_UK_FPS_beta.yaml` (Instant payments - Faster payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/fps`
- **Tags:** `Faster payments`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> This endpoint moves the suspended transaction amount from additional funds to available balance and marks the transaction as settled.
>
> This endpoint generates a [FPS inbound payment processed](https://developers.pismo.io/events/docs/fps-fps-in-status-change-1) event with status `SETTLED`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token—token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |
| `x-tenant` | header | yes | string | Organization ID |  |
| `endToEndId` | path | yes | string | FPS transaction's end to end ID. | maxLength: 31 |
| `x-cid` | header | no | string | Request tracking identifier. If not provided, a random UUID will be generated.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `fps_release.FpsReleaseResponse`) |
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
| `end_to_end_id` | string (schema `endToEndID`) | no | Client-generated transaction identifier. Must be unique for each transaction.<br> | maxLength: 31; example: "1374f841568e4ff4b3a63b023c170ec" |
| `status` | string (schema `fps_release.status`) | no | - `SETTLED` - Transaction was completed processed and settled<br> | enum: ["SETTLED"]; example: "SETTLED" |
| `amount` | number (schema `Amount`) | no | Transaction amount | example: 853.09 |

##### Response 400

400 Example `EFPS0004` (Validation Error):

```json
{
  "code": "EFPS0004",
  "message": "Validation error"
}
```

400 Example `EFPS0016` (Unmarshal Error):

```json
{
  "code": "EFPS0016",
  "message": "Unmarshal error"
}
```

400 Example `EFPS0019` (Accounts API Invalid Request Error):

```json
{
  "code": "EFPS0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EFPS0025` (P2P API Invalid Request Error):

```json
{
  "code": "EFPS0025",
  "message": "P2p - API returned 4xx error"
}
```

400 Example `EFPS0029` (Ledger API Invalid Request Error):

```json
{
  "code": "EFPS0029",
  "message": "Ledger - API returned 4xx error"
}
```

400 Example `EFPS0037` (Invalid Creditor Sort Code Account Number):

```json
{
  "code": "EFPS0037",
  "message": "Invalid creditor sort code/account number"
}
```

400 Example `EFPS0038` (Invalid Creditor IBAN):

```json
{
  "code": "EFPS0038",
  "message": "Invalid creditor IBAN"
}
```

400 Example `EFPS0039` (Invalid Creditor BBAN):

```json
{
  "code": "EFPS0039",
  "message": "Invalid creditor BBAN"
}
```

400 Example `EFPS0046` (IntlBankAccounts API Invalid Request Error):

```json
{
  "code": "EFPS0046",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EFPS0047` (PSP Gateway API Bad Request):

```json
{
  "code": "EFPS0047",
  "message": "Invalid FPS Request. Check error details for more information."
}
```

##### Response 403

403 Example `EFPS0002` (Missing Tenant Header):

```json
{
  "code": "EFPS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EFPS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EFPS0021",
  "message": "Account blocked or cancelled"
}
```

403 Example `EFPS0033` (Invalid Account Id):

```json
{
  "code": "EFPS0033",
  "message": "Invalid account id header: 'x-account-id'"
}
```

403 Example `EFPS0034` (Invalid Idempotency Key):

```json
{
  "code": "EFPS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EFPS0035` (Account Has No Active Addresses):

```json
{
  "code": "EFPS0035",
  "message": "Account has no active addresses"
}
```

403 Example `EFPS0040` (FPS Not Enabled):

```json
{
  "code": "EFPS0040",
  "message": "FPS is not enabled for the creditor sort code"
}
```

403 Example `EFPS0041` (Modulus Check Error):

```json
{
  "code": "EFPS0041",
  "message": "Failed to execute account number modulus check"
}
```

##### Response 404

404 Example `EFPS0010` (Sort Code Not Found):

```json
{
  "code": "EFPS0010",
  "message": "Sort Code not found"
}
```

404 Example `EFPS0018` (Accounts API Not Found Error):

```json
{
  "code": "EFPS0018",
  "message": "Accounts - Not found"
}
```

404 Example `EFPS0028` (Ledger API Not Found Error):

```json
{
  "code": "EFPS0028",
  "message": "Ledger - Not found"
}
```

404 Example `EFPS0031` (IntlBankAccounts API Not Found Error):

```json
{
  "code": "EFPS0031",
  "message": "IntlBankAccounts - Not found"
}
```

##### Response 409

409 Example `EFPS0022` (Transaction Already Exists):

```json
{
  "code": "EFPS0022",
  "message": "A transaction with the specified idempotency key and end_to_end_id already exists"
}
```

409 Example `EFPS0036` (Mismatching Currency Error):

```json
{
  "code": "EFPS0036",
  "message": "The provided currency does not match with the account's configured currency"
}
```

409 Example `EFPS0094` (Transaction Not on Hold for Release):

```json
{
  "code": "EFPS0094",
  "message": "Transaction status is not HOLD, release is not allowed"
}
```

##### Response 429

429 Example `EFPS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EFPS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EFPS0006` (HTTP Error):

```json
{
  "code": "EFPS0006",
  "message": "HTTP request error"
}
```

500 Example `EFPS0009` (IntlBankAccounts API Timeout):

```json
{
  "code": "EFPS0009",
  "message": "IntlBankAccounts API timeout error"
}
```

500 Example `EFPS0011` (IntlBankAccounts API Internal Error):

```json
{
  "code": "EFPS0011",
  "message": "IntlBankAccounts API Internal Server error"
}
```

500 Example `EFPS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EFPS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EFPS0017` (Accounts API Timeout):

```json
{
  "code": "EFPS0017",
  "message": "Accounts API timeout error"
}
```

500 Example `EFPS0020` (Accounts API Server Error):

```json
{
  "code": "EFPS0020",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EFPS0023` (Transaction Database Error):

```json
{
  "code": "EFPS0023",
  "message": "Transaction database error"
}
```

500 Example `EFPS0024` (P2P API Timeout):

```json
{
  "code": "EFPS0024",
  "message": "P2p - API timeout error"
}
```

500 Example `EFPS0026` (P2P API Server Error):

```json
{
  "code": "EFPS0026",
  "message": "P2p - API returned 5xx error"
}
```

500 Example `EFPS0027` (Ledger API Timeout):

```json
{
  "code": "EFPS0027",
  "message": "Ledger API timeout error"
}
```

500 Example `EFPS0030` (Ledger API Server Error):

```json
{
  "code": "EFPS0030",
  "message": "Ledger - API returned 5xx error"
}
```

500 Example `EFPS0032` (IntlBankAccounts API Server Error):

```json
{
  "code": "EFPS0032",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

##### Response 502

502 Example `EFPS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EFPS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFPS0004` | Validation error |
| 400 | `EFPS0016` | Unmarshal error |
| 400 | `EFPS0019` | Accounts - API returned 4xx error |
| 400 | `EFPS0025` | P2p - API returned 4xx error |
| 400 | `EFPS0029` | Ledger - API returned 4xx error |
| 400 | `EFPS0037` | Invalid creditor sort code/account number |
| 400 | `EFPS0038` | Invalid creditor IBAN |
| 400 | `EFPS0039` | Invalid creditor BBAN |
| 400 | `EFPS0046` | IntlBankAccounts - API returned 4xx error |
| 400 | `EFPS0047` | Invalid FPS Request. Check error details for more information. |
| 403 | `EFPS0002` | Missing required header: 'x-tenant' |
| 403 | `EFPS0021` | Account blocked or cancelled |
| 403 | `EFPS0033` | Invalid account id header: 'x-account-id' |
| 403 | `EFPS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EFPS0035` | Account has no active addresses |
| 403 | `EFPS0040` | FPS is not enabled for the creditor sort code |
| 403 | `EFPS0041` | Failed to execute account number modulus check |
| 404 | `EFPS0010` | Sort Code not found |
| 404 | `EFPS0018` | Accounts - Not found |
| 404 | `EFPS0028` | Ledger - Not found |
| 404 | `EFPS0031` | IntlBankAccounts - Not found |
| 409 | `EFPS0022` | A transaction with the specified idempotency key and end_to_end_id already exists |
| 409 | `EFPS0036` | The provided currency does not match with the account's configured currency |
| 409 | `EFPS0094` | Transaction status is not HOLD, release is not allowed |
| 429 | `EFPS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EFPS0006` | HTTP request error |
| 500 | `EFPS0009` | IntlBankAccounts API timeout error |
| 500 | `EFPS0011` | IntlBankAccounts API Internal Server error |
| 500 | `EFPS0012` | PSPGateway API timeout error |
| 500 | `EFPS0017` | Accounts API timeout error |
| 500 | `EFPS0020` | Accounts - API returned 5xx error |
| 500 | `EFPS0023` | Transaction database error |
| 500 | `EFPS0024` | P2p - API timeout error |
| 500 | `EFPS0026` | P2p - API returned 5xx error |
| 500 | `EFPS0027` | Ledger API timeout error |
| 500 | `EFPS0030` | Ledger - API returned 5xx error |
| 500 | `EFPS0032` | IntlBankAccounts - API returned 5xx error |
| 502 | `EFPS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `fps-fps-in-status-change-1` | https://developers.pismo.io/events/docs/fps-fps-in-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;429;500;502`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-faster-payment-system`.

<!-- op: spec=api-specs/Instant_payments_-_UK_FPS_beta.yaml method=POST path=/v1/payments/fps/return/{endToEndId} operationId=post-return-fps -->
### `POST /v1/payments/fps/return/{endToEndId}` — Return FPS payment [beta]

- **operationId:** `post-return-fps`
- **Specification:** `api-specs/Instant_payments_-_UK_FPS_beta.yaml` (Instant payments - Faster payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/fps`
- **Tags:** `Faster payments`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Manually trigger a return for a previously credited FPS inbound transaction.
>
> This endpoint allows clients to initiate a return of funds for an inbound FPS payment that has already been credited to the beneficiary's account. The return is submitted to the payment provider (Form3) for processing.
>
> Returns initiated through this endpoint are marked with `return_origin` = `CLIENT` to distinguish them from provider-initiated returns.
>
> The `return_reason` must be one of the 14 standardized Form3 reason codes (`00000001` through `00000014`).
>
> This endpoint generates an [FPS inbound payment return processed](https://developers.pismo.io/events/docs/fps-fps-in-return-status-change-1) event with `return_origin` = `CLIENT`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token—token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.<br> |  |
| `x-tenant` | header | yes | string | Organization ID |  |
| `Idempotency-key` | header | yes | string | A UUID to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |
| `x-cid` | header | no | string | Request tracking identifier. If not provided, a random UUID will be generated.<br> |  |
| `endToEndId` | path | yes | string | FPS transaction's end to end ID. | maxLength: 31 |

#### Request body

Required: yes

> Return payment request body

**Content type `application/json`** — schema: object (schema `fps_return.FpsReturnRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `return_reason` | string (schema `fps_return.ReturnReason`) | yes | <a href="https://www.form3.tech/" target="_blank">Form3</a> return reason code. Must be one of the following 14 codes:<br>  * `00000001`—Beneficiary sort code/account number unknown<br>  * `00000002`—Beneficiary account closed<br>  * `00000003`—Beneficiary account stopped<br>  * `00000004`—Beneficiary deceased<br>  * `00000005`—Account cannot be identified without data in reference field<br>  * `00000006`—Beneficiary account name does not match beneficiary account number<br>  * `00000007`—Sender of original payment requested this return<br>  * `00000008`—Account is not in currency quoted<br>  * `00000009`—Beneficiary not expecting funds/instructed return<br>  * `00000010`—Terms and conditions of account do not permit crediting of these funds<br>  * `00000011`—Sending institution action required<br>  * `00000012`—Account transferred<br>  * `00000013`—Payment cannot be applied because of beneficiary sensitivities<br>  * `00000014`—Reason not given<br> | enum: ["00000001", "00000002", "00000003", "00000004", "00000005", "00000006", "00000007", "00000008", "00000009", "00000010", "00000011", "00000012", "00000013", "00000014"]; example: "00000001" |
| `amount` | string | yes | Amount to return. Must match the original transaction amount, since the Pismo platform does not support partial returns. | maxLength: 20; example: "10.50" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `fps_return.FpsReturnResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string | no | Return request status | example: "ACCEPTED" |
| `return_transaction_id` | string | no | Return transaction ID | example: "a1b2c3d4-e5f6-7890-abcd-ef1234567890" |
| `original_transaction_id` | string | no | ID of the original inbound transaction being returned | example: "f1e2d3c4-b5a6-7890-abcd-ef1234567890" |
| `return_origin` | string | no | Origin of the return request.<br>  * `CLIENT` — The client manually triggered the return via this endpoint.<br> | example: "CLIENT" |

##### Response 400

400 Example `EFPS0004` (Validation Error):

```json
{
  "code": "EFPS0004",
  "message": "Validation error"
}
```

400 Example `EFPS0016` (Unmarshal Error):

```json
{
  "code": "EFPS0016",
  "message": "Unmarshal error"
}
```

400 Example `EFPS0096` (Partial Return Not Allowed):

```json
{
  "code": "EFPS0096",
  "message": "Partial returns are not allowed. Return amount must match the original transaction amount"
}
```

##### Response 403

403 Example `EFPS0002` (Missing Tenant Header):

```json
{
  "code": "EFPS0002",
  "message": "Missing required header: 'x-tenant'"
}
```

403 Example `EFPS0085` (Missing Account ID Header):

```json
{
  "code": "EFPS0085",
  "message": "Missing required account-id"
}
```

403 Example `EFPS0086` (Missing Idempotency Key):

```json
{
  "code": "EFPS0086",
  "message": "Missing required header: 'Idempotency-Key'"
}
```

##### Response 404

404 Example `EFPS0067` (Transaction Not Found):

```json
{
  "code": "EFPS0067",
  "message": "Transaction API not found error"
}
```

##### Response 409

409 Example `EFPS0058` (Record Already Exists):

```json
{
  "code": "EFPS0058",
  "message": "Record already exists"
}
```

##### Response 422

422 Example `EFPS0093` (Payment Not Eligible For Return):

```json
{
  "code": "EFPS0093",
  "message": "Payment is not eligible for return"
}
```

##### Response 429

429 Example `EFPS0015` (PSP Gateway API Rate Limit):

```json
{
  "code": "EFPS0015",
  "message": "PSPGateway API Rate Limit exceeded"
}
```

##### Response 500

500 Example `EFPS0006` (HTTP Error):

```json
{
  "code": "EFPS0006",
  "message": "HTTP request error"
}
```

500 Example `EFPS0012` (PSP Gateway API Timeout):

```json
{
  "code": "EFPS0012",
  "message": "PSPGateway API timeout error"
}
```

500 Example `EFPS0023` (Transaction Database Error):

```json
{
  "code": "EFPS0023",
  "message": "Transaction database error"
}
```

##### Response 502

502 Example `EFPS0014` (PSP Gateway API Bad Gateway):

```json
{
  "code": "EFPS0014",
  "message": "PSPGateway API Bad Gateway"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EFPS0004` | Validation error |
| 400 | `EFPS0016` | Unmarshal error |
| 400 | `EFPS0096` | Partial returns are not allowed. Return amount must match the original transaction amount |
| 403 | `EFPS0002` | Missing required header: 'x-tenant' |
| 403 | `EFPS0085` | Missing required account-id |
| 403 | `EFPS0086` | Missing required header: 'Idempotency-Key' |
| 404 | `EFPS0067` | Transaction API not found error |
| 409 | `EFPS0058` | Record already exists |
| 422 | `EFPS0093` | Payment is not eligible for return |
| 429 | `EFPS0015` | PSPGateway API Rate Limit exceeded |
| 500 | `EFPS0006` | HTTP request error |
| 500 | `EFPS0012` | PSPGateway API timeout error |
| 500 | `EFPS0023` | Transaction database error |
| 502 | `EFPS0014` | PSPGateway API Bad Gateway |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `fps-fps-in-return-status-change-1` | https://developers.pismo.io/events/docs/fps-fps-in-return-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;404;409;422;429;500;502`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/fps_out.CreditorAccount -->
### Schema `fps_out.CreditorAccount`

Pointer: `#/components/schemas/fps_out.CreditorAccount`. Type: object (schema `fps_out.CreditorAccount`).

> Creditor's account information

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | Creditor name. | maxLength: 40; example: "Len Lease" |
| `scheme_name` | string (schema `schemeName`) | yes | Bank scheme that identifies the account<br>  * `uk-scan`—Sort code and account number (SCAN) scheme<br>  * `bban`—Basic Bank Account Number scheme<br>  * `iban`—International Bank Account Number scheme<br> | enum: ["uk-scan", "bban", "iban"]; example: "iban" |
| `identification` | string (schema `schemeID`) | yes | Creditor's scheme value. A scheme identifies an account - UK-SCAN, IBAN, or BBAN. Refer to `schemeName` for details.<br>  * `uk-scan`—Sort code and account number (SCAN) scheme. Format: `sortcode + accountnumber`<br>  * `bban`—Basic Bank Account Number scheme. Format: `bankidentifier + branchidentifier + accountnumber`<br>  * `iban`—International Bank Account Number scheme. Format: `country code + check digits + bban`<br><br>For example, for an IBAN account `GB93UBKL12345612345678`, the identification would be:<br><br>  `iban`: `GB93UBKL12345612345678`<br>  `bban`: `UBKL12345612345678`<br>  `uk-scan`: `12345612345678`<br> | maxLength: 22; example: "AA00AAA000000000000000" |

<!-- schema: #/components/schemas/fps_out.Currency -->
### Schema `fps_out.Currency`

Pointer: `#/components/schemas/fps_out.Currency`. Type: object (schema `fps_out.Currency`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | yes | Transaction amount | example: 853.09 |
| `code` | string | no | Transaction currency (ISO 4217 3-letter code). | enum: ["GBP"]; example: "GBP" |

<!-- schema: #/components/schemas/fps_out.RemittanceInformation -->
### Schema `fps_out.RemittanceInformation`

Pointer: `#/components/schemas/fps_out.RemittanceInformation`. Type: object (schema `fps_out.RemittanceInformation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reference` | string | no | Remittance reference. | pattern: "^[a-zA-Z0-9\\\\/\\\\-?:().,'+\\\\s#=!\\"%&*<>;{@\\\\r\\\\n]*$"; maxLength: 140; example: "Reference information" |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

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
| `api-specs/Instant_payments_-_UK_FPS_beta.yaml` | tag `Faster payments`: POST /v1/payments/fps/out, POST /v1/payments/fps/cop, GET /v1/payments/fps/{endToEndId}, POST /v1/payments/fps/cancel/{endToEndId}, POST /v1/payments/fps/release/{endToEndId}, POST /v1/payments/fps/return/{endToEndId} | https://github.com/PismoDevEx/pismo-api-specs | `c65cc92bfad92bbd…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-banking-overview` — Banking overview
- `KU-ERR-codes-efps` — Error codes: EFPS
- `KU-EVT-catalogue-fps` — Event catalogue: fps
- `KU-EVT-faster-payments-events` — Instant payments - Faster Payments
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
