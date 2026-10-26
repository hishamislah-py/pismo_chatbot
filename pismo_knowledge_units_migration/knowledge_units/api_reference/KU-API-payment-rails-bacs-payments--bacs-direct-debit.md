---
ku_id: KU-API-payment-rails-bacs-payments--bacs-direct-debit
title: 'API reference: Payment rails - BACS payments — BACS direct debit'
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
- post-create-mandate
- get-bacs-claim-list
- post-create-claim
- post-raise-claim-reversal
- get-bacs-mandate-list
- patch-amend-mandate
- get-bacs-directdebit-list
- post-cancel-mandate
related_kus:
- KU-ERR-codes-ebacs
- KU-EVT-catalogue-bacs
- KU-PAY-bacs
specification_version: '1.0'
---

# API reference: Payment rails - BACS payments — BACS direct debit

**KU ID:** `KU-API-payment-rails-bacs-payments--bacs-direct-debit` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 8 operation(s) tagged `BACS direct debit` in `api-specs/Payment_rails_-_BACS_payments.yaml` (“Payment rails - BACS payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/payments/bacs/directdebit/paper-mandates` | `post-create-mandate` | Create BACS mandate [beta] | no |
| `GET /v1/payments/bacs/directdebit/claims` | `get-bacs-claim-list` | List BACS Direct Debit indemnity claims [beta] | no |
| `POST /v1/payments/bacs/directdebit/claims` | `post-create-claim` | Raise BACS Direct Debit indemnity claim [beta] | no |
| `POST /v1/payments/bacs/directdebit/claims/reversal/{id}` | `post-raise-claim-reversal` | Reverse BACS Direct Debit indemnity claim [beta] | no |
| `GET /v1/payments/bacs/directdebit/mandates` | `get-bacs-mandate-list` | List BACS direct debit mandates [beta] | no |
| `PATCH /v1/payments/bacs/directdebit/mandates/{id}` | `patch-amend-mandate` | Amend BACS mandate [beta] | no |
| `GET /v1/payments/bacs/directdebit` | `get-bacs-directdebit-list` | List BACS direct debit transactions [beta] | no |
| `POST /v1/payments/bacs/directdebit/mandates/{id}/cancel` | `post-cancel-mandate` | Cancel BACS mandate [beta] | no |

## Operation contracts

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directdebit/paper-mandates operationId=post-create-mandate -->
### `POST /v1/payments/bacs/directdebit/paper-mandates` — Create BACS mandate [beta]

- **operationId:** `post-create-mandate`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct debit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

>
> Create a BACS direct debit mandate.
>
> A BACS direct debit mandate captures a payer's authorisation, taken from a signed paper form, for a business to collect direct debit payments from their UK bank account through the BACS scheme.
>
> **Notes:**
>
>   * The operation is idempotent via the `Idempotency-key` header. Repeating the same key replays the original mandate; reusing the same `reference` with a different key is rejected with a **409 Conflict**.
>
>   * Creation does not generate an event. Subsequent status transitions generate a [BACS mandate status changed](https://developers.pismo.io/events/docs/bacs-mandate-status-change-1) event (for example `SUBMITTED`, `CONFIRMED`, `FAILED`).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `Idempotency-key` | header | yes | string | A UUID (without hyphens) to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. Identifies the transaction on future events.<br> | maxLength: 32 |

#### Request body

Required: yes

> Create mandate request body

**Content type `application/json`** — schema: object (schema `mandate.CreateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `debtor` | object (schema `mandate.Debtor`) | yes | Debtor (payer) bank details captured from the signed mandate form. |  |
| `beneficiary` | object (schema `mandate.Beneficiary`) | yes | Beneficiary (creditor) details. |  |
| `clearing_id` | string (schema `mandateClearingId`) | yes | Six-digit clearing ID for the mandate | pattern: "^[0-9]{6}$"; example: "123456" |
| `reference` | string (schema `mandateReference`) | yes | Mandate reference. Must be unique per organization and use the standard BACS reference character set.<br><br>The standard BACS reference character set is the restricted set of characters BACS permits in the text fields of a Standard 18 record — the format used for Direct Debit/Direct Credit instructions. It maps to the reference field on the mandate<br>schemas.<br><br>BACS Standard 18 (STD18) is a fixed-width, 80-to-106-character line-based file format used to submit Direct Credit and Direct Debit payment instructions in the UK. Files strictly follow a defined sequence starting with volume and header labels, proceeding to transaction records, and ending with trailer and total lines.<br><br>**Permitted characters**:<br>  - Uppercase letters A-Z (lowercase is not allowed — it gets force-uppercased)<br>  - Digits 0-9<br>  - Space<br>  - These four specials only: - (hyphen), . (full stop), & (ampersand), / (solidus)<br><br>**Reference-field rules on top of the character set**:<br>  - 6-18 characters<br>  - Must not begin with a space<br>  - Must not be all the same character (e.g. all zeros)<br>  - First 4 chars must not be DDIC (reserved for bank/indemnity-claim use)<br>  - Should be unique per Direct Debit<br> | maxLength: 18; example: "MANDATE-REF-001" |
| `processing_date` | string (schema `processingDate`) | yes | Processing date. Format = yyyy-mm-dd | example: "2026-08-10" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Mandate created | `application/json`: object (schema `mandate.CreateResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `mandateId`) | no | Form3-assigned mandate ID | example: "b254bb5e-6f1a-4c2b-9c1e-2f0a6d3e8c11" |
| `status` | string (schema `mandate.CreateStatus`) | no | Lifecycle status reachable for a created mandate.<br>  * `CREATED` - Mandate persisted; pending submission to Form3 via the PSP gateway<br>  * `SUBMITTED` - Mandate submitted to the scheme<br>  * `CONFIRMED` - Mandate confirmed and active<br>  * `FAILED` - Mandate processing failed. Terminal state<br> | enum: ["CREATED", "SUBMITTED", "CONFIRMED", "FAILED"]; example: "CREATED" |

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

403 Example `EBACS0085` (Missing Account Id):

```json
{
  "code": "EBACS0085",
  "message": "Missing required account-id"
}
```

403 Example `EBACS0034` (Invalid Idempotency Key):

```json
{
  "code": "EBACS0034",
  "message": "Missing required header: 'x-idempotency-key'"
}
```

403 Example `EBACS0105` (BACS Mandates Not Enabled For Account):

```json
{
  "code": "EBACS0105",
  "message": "BACS mandates are not enabled for the account"
}
```

403 Example `EBACS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EBACS0021",
  "message": "Account blocked or cancelled"
}
```

##### Response 409

409 Example `EBACS0058` (Record Already Exists):

```json
{
  "code": "EBACS0058",
  "message": "Record already exists"
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
| 400 | `EBACS0016` | Unmarshal error |
| 400 | `EBACS0047` | Invalid BACS Request. Check error details for more information. |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0085` | Missing required account-id |
| 403 | `EBACS0034` | Missing required header: 'x-idempotency-key' |
| 403 | `EBACS0105` | BACS mandates are not enabled for the account |
| 403 | `EBACS0021` | Account blocked or cancelled |
| 409 | `EBACS0058` | Record already exists |
| 500 | `EBACS0023` | Transaction database error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-mandate-status-change-1` | https://developers.pismo.io/events/docs/bacs-mandate-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;409;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=GET path=/v1/payments/bacs/directdebit/claims operationId=get-bacs-claim-list -->
### `GET /v1/payments/bacs/directdebit/claims` — List BACS Direct Debit indemnity claims [beta]

- **operationId:** `get-bacs-claim-list`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct debit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> List DDIC claims for an account. 
>
> This endpoint takes an account token - an access token encoded with a Pismo account ID.  The account is parsed from the token. 
>
> This endpoint does not return claim reversals.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `id` | query | no | string | Transaction or mandate ID filter | maxLength: 36 |
| `status` | query | no | string | DDIC claim status filter | enum: ["CREATED", "PROCESSING", "CONFIRMED", "FAILED"] |
| `beginDate` | query | no | string | Return records created on or after this date/time (RFC3339). | maxLength: 40; example: "2026-08-01T00:00:00Z" |
| `endDate` | query | no | string | Return records created on or before this date/time (RFC3339). | maxLength: 40; example: "2026-08-31T23:59:59Z" |
| `afterId` | query | no | string | Pagination cursor. Pass this field as a query parameter to get the next page. | maxLength: 2000 |
| `pageSize` | query | no | integer | Maximum number of items to return per page. Default is `10`. | default: 10; format: "int64"; minimum: 1; maximum: 100; example: 50 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of DDIC claims | `application/json`: object (schema `listing.ClaimListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `listing.Claim`) | no |  |  |
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

500 Example `EBACS0003` (Internal Error):

```json
{
  "code": "EBACS0003",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0085` | Missing required account-id |
| 500 | `EBACS0003` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-bacs`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directdebit/claims operationId=post-create-claim -->
### `POST /v1/payments/bacs/directdebit/claims` — Raise BACS Direct Debit indemnity claim [beta]

- **operationId:** `post-create-claim`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct debit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

>
> Create a BACS Direct Debit Indemnity Claim (DDIC).
>
> A DDIC reclaims money that was incorrectly debited from a payer's account under the Direct Debit Guarantee. The claim is validated and persisted, then submitted asynchronously to the BACS scheme via Form3.
>
> **Notes:**
>
>   * The operation is idempotent via the `Idempotency-key` header. 
>
>   * The claim is persisted with `status` = `CREATED` and submitted asynchronously. Creation itself returns immediately. 
>
>   * Subsequent status transitions generate a [BACS direct debit claim status changed](https://developers.pismo.io/events/docs/bacs-direct-debit-claim-status-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `Idempotency-key` | header | yes | string | A UUID (without hyphens) to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. Identifies the transaction on future events.<br> | maxLength: 32 |

#### Request body

Required: yes

> Raise claim request body

**Content type `application/json`** — schema: object (schema `claim.CreateRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `clearing_id` | object | yes |  |  |
| `reference` | string (schema `claim.reference`) | yes | Claim reference. Must begin with `DDIC` followed by 2-6 alphanumeric characters (maximum length 18). <br><br>BACS reserves the `DDIC` prefix for indemnity-claim references.<br> | pattern: "^DDIC[A-Za-z0-9]{2,14}$"; maxLength: 18; example: "DDIC0001AB" |
| `reason_code` | string (schema `claim.reasonCode`) | yes | Direct Debit Indemnity Claim (DDIC) reason code. BACS DDIC scheme rules that indicate why the indemnity claim is being raised:<br><br>  * `1`— The amount and/or date collected differs from the advance notice.<br><br>  * `2`— No advance notice was received (or the payment was collected earlier than notified).<br><br>  * `3`— The Direct Debit Instruction (DDI) is disputed / no valid mandate is held.<br><br>  * `4`— The payer canceled the DDI directly with the service user.<br><br>  * `5`— The account holder is deceased.<br><br>  * `6`— The payer canceled the DDI with their bank.<br><br>  * `7`— Claim raised at the service user's request.<br><br>  * `8`— Service user name disputed / the payer does not recognise the collecting service user.<br><br>Conditional fields:<br><br>  * `3`—`processing_date` is **REQUIRED**.<br><br>  * `7`—`contact_name` and `request_date` are **REQUIRED**.<br> | enum: ["1", "2", "3", "4", "5", "6", "7", "8"]; example: "1" |
| `original_instruction` | object (schema `claim.OriginalInstruction`) | yes | Original Direct Debit Instruction (DDI) the claim relates to |  |
| `disputed_transactions` | array of object (schema `claim.DisputedTransaction`) | yes |  | minItems: 1; maxItems: 12 |
| `number_of_transactions` | integer | no | If passed, it **must** equal the number of `disputed_transactions`. Maximum 12.<br> | format: "int32"; maximum: 12; example: 1 |
| `processing_date` | string | no | Processing date.<br><br>**REQUIRED** when `reason_code` = `3`. Do **NOT** pass otherwise. <br><br>Format = YYYY-MM-DD.<br> | format: "date"; example: "2026-08-20" |
| `contact_name` | string | no | Service user contact name. <br><br>**REQUIRED** if `reason_code` = `7`. Do **NOT** pass otherwise. <br><br>Must **NOT** be all spaces.<br> | maxLength: 51; example: "Jane Smith" |
| `request_date` | string | no | Service user request date. Format = YYYY-MM-DD.<br><br>**REQUIRED** when `reason_code` = `7`. Do **NOT** pass otherwise. <br> | format: "date"; example: "2026-08-18" |
| `reason` | string | no | Free-text reason for the claim | maxLength: 255; example: "Duplicate collection" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Claim created | `application/json`: object (schema `claim.CreateResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `claim.id`) | no | Pismo-assigned local claim ID | example: "019e92ec-3362-7c54-9d17-89f5542a06e4" |
| `status` | string (schema `claim.status`) | no | DDIC claim / claim-reversal lifecycle status_reason:<br><br>  * `CREATED`—Claim persisted, pending submission to the scheme via Form3.<br><br>  * `PROCESSING`—Claim submitted and in flight through Form3 / the scheme.<br><br>  * `CONFIRMED`—Claim delivery confirmed by the scheme. Terminal state.<br><br>  * `FAILED`—Claim rejected or failed validation/submission. Terminal state.<br> | enum: ["CREATED", "PROCESSING", "CONFIRMED", "FAILED"]; example: "CREATED" |

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

403 Example `EBACS0086` (Missing Idempotency Key):

```json
{
  "code": "EBACS0086",
  "message": "Missing required header: 'Idempotency-Key'"
}
```

403 Example `EBACS0021` (Account Blocked Or Cancelled):

```json
{
  "code": "EBACS0021",
  "message": "Account blocked or cancelled"
}
```

##### Response 409

409 Example `EBACS0058` (Record Already Exists):

```json
{
  "code": "EBACS0058",
  "message": "Record already exists"
}
```

##### Response 500

500 Example `EBACS0003` (Internal Error):

```json
{
  "code": "EBACS0003",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0085` | Missing required account-id |
| 403 | `EBACS0086` | Missing required header: 'Idempotency-Key' |
| 403 | `EBACS0021` | Account blocked or cancelled |
| 409 | `EBACS0058` | Record already exists |
| 500 | `EBACS0003` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-direct-debit-claim-status-change-1` | https://developers.pismo.io/events/docs/bacs-direct-debit-claim-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-bacs`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directdebit/claims/reversal/{id} operationId=post-raise-claim-reversal -->
### `POST /v1/payments/bacs/directdebit/claims/reversal/{id}` — Reverse BACS Direct Debit indemnity claim [beta]

- **operationId:** `post-raise-claim-reversal`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct debit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

>
> Reverse a previously raised BACS Direct Debit indemnity claim.
>
> Only a claim that has been delivery-confirmed (`status` = `CONFIRMED`) can be reversed. The reversal is persisted with `status` = `CREATED` and submitted asynchronously to the BACS scheme via Form3.
>
> **Notes:**
>
>   * The operation is idempotent via the `Idempotency-key` header.
>
>   * Subsequent status transitions generate a [BACS direct debit claim reversal status changed](https://developers.pismo.io/events/docs/bacs-direct-debit-claim-reversal-status-change-1) event.
>

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `Idempotency-key` | header | yes | string | A UUID (without hyphens) to ensure the operation remains idempotent, allowing for operation repetition without causing unintended effects or duplication. Identifies the transaction on future events.<br> | maxLength: 32 |
| `id` | path | yes | string | Local claim ID (the Pismo-assigned ID returned when the claim was raised) of the claim to reverse | maxLength: 36 |

#### Request body

Required: yes

> Raise claim reversal request body

**Content type `application/json`** — schema: object (schema `claim.RaiseReversalRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `original_instruction_id` | string | yes | Claim being reversed's DDIC claim sequence number. Forwarded to the scheme. | maxLength: 20; example: "0000000000001234" |
| `reason` | string (schema `reversalReason`) | no | Free-text reason for reversal | maxLength: 255; example: "Claim raised in error" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Claim reversal created | `application/json`: object (schema `claim.RaiseReversalResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Pismo-assigned local claim-reversal ID | example: "019e9300-1111-7c54-9d17-89f5542a06e4" |
| `claim_id` | string (schema `claim.id`) | no | Pismo-assigned local claim ID | example: "019e92ec-3362-7c54-9d17-89f5542a06e4" |
| `status` | string (schema `claim.status`) | no | DDIC claim / claim-reversal lifecycle status_reason:<br><br>  * `CREATED`—Claim persisted, pending submission to the scheme via Form3.<br><br>  * `PROCESSING`—Claim submitted and in flight through Form3 / the scheme.<br><br>  * `CONFIRMED`—Claim delivery confirmed by the scheme. Terminal state.<br><br>  * `FAILED`—Claim rejected or failed validation/submission. Terminal state.<br> | enum: ["CREATED", "PROCESSING", "CONFIRMED", "FAILED"]; example: "CREATED" |

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

403 Example `EBACS0086` (Missing Idempotency Key):

```json
{
  "code": "EBACS0086",
  "message": "Missing required header: 'Idempotency-Key'"
}
```

##### Response 404

404 Example `EBACS0107` (Claim Not Found):

```json
{
  "code": "EBACS0107",
  "message": "Claim not found"
}
```

##### Response 409

409 Example `EBACS0108` (Claim Reversal Not Allowed):

```json
{
  "code": "EBACS0108",
  "message": "Claim reversal not allowed: claim must be CONFIRMED (delivery confirmed)"
}
```

##### Response 500

500 Example `EBACS0003` (Internal Error):

```json
{
  "code": "EBACS0003",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0085` | Missing required account-id |
| 403 | `EBACS0086` | Missing required header: 'Idempotency-Key' |
| 404 | `EBACS0107` | Claim not found |
| 409 | `EBACS0108` | Claim reversal not allowed: claim must be CONFIRMED (delivery confirmed) |
| 500 | `EBACS0003` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-direct-debit-claim-reversal-status-change-1` | https://developers.pismo.io/events/docs/bacs-direct-debit-claim-reversal-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;403;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-bacs`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=GET path=/v1/payments/bacs/directdebit/mandates operationId=get-bacs-mandate-list -->
### `GET /v1/payments/bacs/directdebit/mandates` — List BACS direct debit mandates [beta]

- **operationId:** `get-bacs-mandate-list`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct debit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> List BACS direct debit mandates for an account. 
>
> This endpoint takes an account token - an access token encoded with a Pismo account ID.  The account is parsed from the token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `id` | query | no | string | Transaction or mandate ID filter | maxLength: 36 |
| `status` | query | no | string | Mandate status filter. | enum: ["CREATED", "CANCELLED"] |
| `source` | query | no | string | Mandate source filter:<br>  * `auddis` - Electronic<br>  * `non-electronic` - Paper<br /><br>Default is all.<br> | enum: ["auddis", "non-electronic"]; example: "auddis" |
| `beginDate` | query | no | string | Return records created on or after this date/time (RFC3339). | maxLength: 40; example: "2026-08-01T00:00:00Z" |
| `endDate` | query | no | string | Return records created on or before this date/time (RFC3339). | maxLength: 40; example: "2026-08-31T23:59:59Z" |
| `afterId` | query | no | string | Pagination cursor. Pass this field as a query parameter to get the next page. | maxLength: 2000 |
| `pageSize` | query | no | integer | Maximum number of items to return per page. Default is `10`. | default: 10; format: "int64"; minimum: 1; maximum: 100; example: 50 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of direct debit mandates | `application/json`: object (schema `listing.MandateListResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `listing.Mandate`) | no |  |  |
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

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=PATCH path=/v1/payments/bacs/directdebit/mandates/{id} operationId=patch-amend-mandate -->
### `PATCH /v1/payments/bacs/directdebit/mandates/{id}` — Amend BACS mandate [beta]

- **operationId:** `patch-amend-mandate`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct debit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Amend a BACS direct debit mandate.
>
> Registers a change to a mandate's debtor and/or beneficiary details, applied asynchronously through the BACS scheme.
>
> **Notes:**
>
>   * The amend is persisted with `status` = `AMEND_PENDING`, and enqueued for the asynchronous submission worker, which submits it to Form3 through the PSP gateway.
>
>   * Allowed only when the mandate is in `CREATED`, `SUBMITTED`, or `CONFIRMED`; any other state is rejected with a **409 Conflict** (`EBACS0103`).
>
>   * `version` is a Form3 optimistic-concurrency passthrough that must equal the stored version; a mismatch is rejected with a **409 Conflict** (`EBACS0104`). This call does not increment this field.
>
>   * This endpoint moves the mandate to `status` = `AMEND_PENDING` and generates a [BACS mandate status changed](https://developers.pismo.io/events/docs/bacs-mandate-status-change-1) event. Subsequent status transitions generate further events (for example `AMENDED`, `FAILED`).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `id` | path | yes | string | Mandate ID (the Form3-assigned ID returned at creation). | maxLength: 36 |

#### Request body

Required: yes

> Amend mandate request body

**Content type `application/json`** — schema: object (schema `mandate.AmendRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `version` | integer | yes | Caller's expected current mandate version. A Form3 optimistic-concurrency passthrough that must match the stored version. This call does not increment this field.<br> | example: 0 |
| `debtor` | object (schema `mandate.Debtor`) | no | Debtor (payer) bank details captured from the signed mandate form. |  |
| `beneficiary` | object (schema `mandate.Beneficiary`) | no | Beneficiary (creditor) details. |  |
| `advice_reason` | string (schema `mandate.AdviceReason`) | no | Why an amendment is advised to the originator. Mapped to the matching ADDACS advice code on the mandate submission raised for the amendment; scheme codes are not accepted here.<br>  * `advance_notice_disputed` - The payer disputes the advance notice of a collection. An advice on its own, with no accompanying change of details<br>  * `instruction_details_amended` - The payer's account details on the instruction have changed<br> | enum: ["advance_notice_disputed", "instruction_details_amended"]; example: "advance_notice_disputed" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Amend intent accepted and enqueued | `application/json`: object (schema `mandate.AmendResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `mandateId`) | no | Form3-assigned mandate ID | example: "b254bb5e-6f1a-4c2b-9c1e-2f0a6d3e8c11" |
| `status` | string (schema `mandate.AmendStatus`) | no | Lifecycle status reachable when amending a mandate.<br>  * `AMEND_PENDING` - Amend intent accepted; pending submission to Form3 via the PSP gateway<br>  * `AMENDED` - Amend confirmed<br>  * `FAILED` - Amend processing failed. Terminal state<br> | enum: ["AMEND_PENDING", "AMENDED", "FAILED"]; example: "AMEND_PENDING" |
| `version` | integer (schema `mandateVersion`) | no | The mandate version. Unchanged by the amend mandate endpoint call (Form3 passthrough — not incremented).<br> | example: 2 |

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

##### Response 404

404 Example `EBACS0102` (Mandate Not Found):

```json
{
  "code": "EBACS0102",
  "message": "Mandate not found"
}
```

##### Response 409

409 Example `EBACS0103` (Mandate Invalid State):

```json
{
  "code": "EBACS0103",
  "message": "Mandate cannot perform the requested operation in its current status"
}
```

409 Example `EBACS0104` (Mandate Version Conflict):

```json
{
  "code": "EBACS0104",
  "message": "Mandate version does not match the current version"
}
```

##### Response 500

500 Example `EBACS0003` (Internal Error):

```json
{
  "code": "EBACS0003",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 400 | `EBACS0016` | Unmarshal error |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0085` | Missing required account-id |
| 404 | `EBACS0102` | Mandate not found |
| 409 | `EBACS0103` | Mandate cannot perform the requested operation in its current status |
| 409 | `EBACS0104` | Mandate version does not match the current version |
| 500 | `EBACS0003` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-mandate-status-change-1` | https://developers.pismo.io/events/docs/bacs-mandate-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=GET path=/v1/payments/bacs/directdebit operationId=get-bacs-directdebit-list -->
### `GET /v1/payments/bacs/directdebit` — List BACS direct debit transactions [beta]

- **operationId:** `get-bacs-directdebit-list`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct debit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> List BACS direct debit transactions.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `x-cid` | header | no | string | Request tracking ID. If not provided, a random UUID is generated.<br> |  |
| `id` | query | no | string | Transaction or mandate ID filter | maxLength: 36 |
| `status` | query | no | string | Transaction status filter | enum: ["CREATED", "PROCESSING", "SETTLED", "CANCELLED", "HOLD"] |
| `transactionType` | query | no | string | Direct debit transaction type filter | enum: ["DIRECTDEBIT_INBOUND", "DIRECTDEBIT_OUTBOUND", "DIRECTDEBIT_IN_RETURN", "DIRECTDEBIT_OUT_RETURN", "DIRECTDEBIT_IN_REVERSAL", "DIRECTDEBIT_OUT_REVERSAL"] |
| `mandateID` | query | no | string | Associated mandate ID filter | maxLength: 36 |
| `beginDate` | query | no | string | Return records created on or after this date/time (RFC3339). | maxLength: 40; example: "2026-08-01T00:00:00Z" |
| `endDate` | query | no | string | Return records created on or before this date/time (RFC3339). | maxLength: 40; example: "2026-08-31T23:59:59Z" |
| `afterId` | query | no | string | Pagination cursor. Pass this field as a query parameter to get the next page. | maxLength: 2000 |
| `pageSize` | query | no | integer | Maximum number of items to return per page. Default is `10`. | default: 10; format: "int64"; minimum: 1; maximum: 100; example: 50 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Paginated list of direct debit transactions | `application/json`: object (schema `listing.TransactionListResponse`) |
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

<!-- op: spec=api-specs/Payment_rails_-_BACS_payments.yaml method=POST path=/v1/payments/bacs/directdebit/mandates/{id}/cancel operationId=post-cancel-mandate -->
### `POST /v1/payments/bacs/directdebit/mandates/{id}/cancel` — Cancel BACS mandate [beta]

- **operationId:** `post-cancel-mandate`
- **Specification:** `api-specs/Payment_rails_-_BACS_payments.yaml` (Payment rails - BACS payments)
- **Server base URL(s):** `https://sandbox.pismolabs.io/bacs`
- **Tags:** `BACS direct debit`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Cancel a BACS direct debit mandate.
>
> Cancel of an existing mandate, applied asynchronously through the BACS scheme.
>
> **Notes:**
>
>   * The cancel is persisted with `status` = `CANCEL_PENDING` under the payer account, and enqueued for the asynchronous submission worker, which submits it to Form3 through the PSP gateway.
>
>   * Allowed only when the mandate is in `SUBMITTED` or `CONFIRMED`; any other state is rejected with a **409 Conflict** (`EBACS0103`).
>
>   * `version` is a Form3 optimistic-concurrency passthrough that must equal the stored version; a mismatch is rejected with a **409 Conflict** (`EBACS0104`). This call does not increment it.
>
>   * The optional `status_reason` records why the mandate is being cancelled; it is persisted on the mandate and forwarded on the generated event.
>
>   * This endpoint moves the mandate to `status` = `CANCEL_PENDING` and generates a [BACS mandate status changed](https://developers.pismo.io/events/docs/bacs-mandate-status-change-1) event. Subsequent status transitions generate further events (for example `CANCELLED`, `FAILED`).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message<br> |  |
| `id` | path | yes | string | Mandate ID (the Form3-assigned ID returned at creation). | maxLength: 36 |

#### Request body

Required: yes

> Cancel mandate request body

**Content type `application/json`** — schema: object (schema `mandate.CancelRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `version` | integer | yes | Caller's expected current mandate version. A Form3 optimistic-concurrency passthrough that must match the stored version. This call does not increment this. | example: 0 |
| `status_reason` | string (schema `mandate.CancellationReason`) | no | Reason code for the cancellation (mirrors Form3's mandate cancellation reasons). The client sends only the code; the human-readable description is derived server-side.<br>  * `account_closed` - Account closed<br>  * `account_transferred_to_new_psp` - Account transferred to a new PSP<br>  * `cancelled_by_originator` - Cancelled by originator<br>  * `cancelled_by_payer` - Cancelled by payer<br>  * `payer_deceased` - Payer deceased<br>  * `paying_bank_cancellation` - Paying bank cancellation<br> | enum: ["account_closed", "account_transferred_to_new_psp", "cancelled_by_originator", "cancelled_by_payer", "payer_deceased", "paying_bank_cancellation"]; example: "account_closed" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Cancel intent accepted and enqueued | `application/json`: object (schema `mandate.CancelResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `mandateId`) | no | Form3-assigned mandate ID | example: "b254bb5e-6f1a-4c2b-9c1e-2f0a6d3e8c11" |
| `status` | string (schema `mandate.CancelStatus`) | no | Lifecycle status reachable when cancelling a mandate.<br>  * `CANCEL_PENDING` - Cancel intent accepted; pending submission to Form3 via the PSP gateway<br>  * `CANCELLED` - Mandate cancelled. Terminal state<br>  * `FAILED` - Cancel processing failed. Terminal state<br> | enum: ["CANCEL_PENDING", "CANCELLED", "FAILED"]; example: "CANCEL_PENDING" |
| `version` | integer | no | Mandate version. This call does not change it (Form3 passthrough — not incremented). | example: 0 |

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

##### Response 404

404 Example `EBACS0102` (Mandate Not Found):

```json
{
  "code": "EBACS0102",
  "message": "Mandate not found"
}
```

##### Response 409

409 Example `EBACS0103` (Mandate Invalid State):

```json
{
  "code": "EBACS0103",
  "message": "Mandate cannot perform the requested operation in its current status"
}
```

409 Example `EBACS0104` (Mandate Version Conflict):

```json
{
  "code": "EBACS0104",
  "message": "Mandate version does not match the current version"
}
```

##### Response 500

500 Example `EBACS0003` (Internal Error):

```json
{
  "code": "EBACS0003",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBACS0004` | Validation error |
| 400 | `EBACS0016` | Unmarshal error |
| 403 | `EBACS0002` | Missing required header: 'x-tenant' |
| 403 | `EBACS0085` | Missing required account-id |
| 404 | `EBACS0102` | Mandate not found |
| 409 | `EBACS0103` | Mandate cannot perform the requested operation in its current status |
| 409 | `EBACS0104` | Mandate version does not match the current version |
| 500 | `EBACS0003` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `bacs-mandate-status-change-1` | https://developers.pismo.io/events/docs/bacs-mandate-status-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/mandate.Debtor -->
### Schema `mandate.Debtor`

Pointer: `#/components/schemas/mandate.Debtor`. Type: object (schema `mandate.Debtor`).

> Debtor (payer) bank details captured from the signed mandate form.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | Debtor account holder name | maxLength: 18; example: "John Debtor" |
| `account_number` | string (schema `accountNumber`) | yes | UK account number (8 digits) | pattern: "^[0-9]{8}$"; example: "87654321" |
| `sort_code` | string (schema `sortCode`) | yes | UK sort code (6 digits). | pattern: "^[0-9]{6}$"; example: "200000" |

<!-- schema: #/components/schemas/mandate.Beneficiary -->
### Schema `mandate.Beneficiary`

Pointer: `#/components/schemas/mandate.Beneficiary`. Type: object (schema `mandate.Beneficiary`).

> Beneficiary (creditor) details.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `beneficiaryName`) | yes | Beneficiary name. | maxLength: 18; example: "Mac Donalds" |
| `account_number` | string (schema `accountNumber`) | no | UK account number (8 digits) | pattern: "^[0-9]{8}$"; example: "87654321" |
| `sort_code` | string (schema `sortCode`) | no | UK sort code (6 digits). | pattern: "^[0-9]{6}$"; example: "200000" |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

<!-- schema: #/components/schemas/listing.Claim -->
### Schema `listing.Claim`

Pointer: `#/components/schemas/listing.Claim`. Type: object (schema `listing.Claim`).

> DDIC claim record returned by the claim list endpoint

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `claim.id`) | no | Pismo-assigned local claim ID | example: "019e92ec-3362-7c54-9d17-89f5542a06e4" |
| `org_id` | string (schema `orgId`) | no | Organization/tenant ID | example: "TN-KGIOODJD...1000" |
| `account_id` | integer (schema `accountId`) | no | Account ID | example: 12345678 |
| `claim_id` | string | no | Form3-assigned claim ID. (Scheme reference. Omitted until the claim is submitted.) | example: "3fa85f64-5717-4562-b3fc-2c963f66afa6" |
| `status` | string (schema `claim.status`) | no | DDIC claim / claim-reversal lifecycle status_reason:<br><br>  * `CREATED`—Claim persisted, pending submission to the scheme via Form3.<br><br>  * `PROCESSING`—Claim submitted and in flight through Form3 / the scheme.<br><br>  * `CONFIRMED`—Claim delivery confirmed by the scheme. Terminal state.<br><br>  * `FAILED`—Claim rejected or failed validation/submission. Terminal state.<br> | enum: ["CREATED", "PROCESSING", "CONFIRMED", "FAILED"]; example: "CREATED" |
| `reason_code` | string (schema `claim.reasonCode`) | no | Direct Debit Indemnity Claim (DDIC) reason code. BACS DDIC scheme rules that indicate why the indemnity claim is being raised:<br><br>  * `1`— The amount and/or date collected differs from the advance notice.<br><br>  * `2`— No advance notice was received (or the payment was collected earlier than notified).<br><br>  * `3`— The Direct Debit Instruction (DDI) is disputed / no valid mandate is held.<br><br>  * `4`— The payer canceled the DDI directly with the service user.<br><br>  * `5`— The account holder is deceased.<br><br>  * `6`— The payer canceled the DDI with their bank.<br><br>  * `7`— Claim raised at the service user's request.<br><br>  * `8`— Service user name disputed / the payer does not recognise the collecting service user.<br><br>Conditional fields:<br><br>  * `3`—`processing_date` is **REQUIRED**.<br><br>  * `7`—`contact_name` and `request_date` are **REQUIRED**.<br> | enum: ["1", "2", "3", "4", "5", "6", "7", "8"]; example: "1" |
| `reference` | string (schema `claim.reference`) | no | Claim reference. Must begin with `DDIC` followed by 2-6 alphanumeric characters (maximum length 18). <br><br>BACS reserves the `DDIC` prefix for indemnity-claim references.<br> | pattern: "^DDIC[A-Za-z0-9]{2,14}$"; maxLength: 18; example: "DDIC0001AB" |
| `clearing_id` | string (schema `mandateClearingId`) | no | Six-digit clearing ID for the mandate | pattern: "^[0-9]{6}$"; example: "123456" |
| `original_instruction` | object (schema `claim.OriginalInstruction`) | no | Original Direct Debit Instruction (DDI) the claim relates to |  |
| `disputed_transactions` | array of object (schema `claim.DisputedTransaction`) | no |  |  |
| `number_of_transactions` | integer | no | Number of transactions | format: "int32"; example: 1 |
| `processing_date` | string | no | Processing date. Format = YYYY-MM-DD. | format: "date"; example: "2026-08-20" |
| `contact_name` | string | no | Contact name | maxLength: 51; example: "Jane Smith" |
| `request_date` | string | no | Request date. Format = YYYY-MM-DD. | format: "date"; example: "2026-08-18" |
| `reason` | string (schema `reversalReason`) | no | Free-text reason for reversal | maxLength: 255; example: "Claim raised in error" |
| `created_at` | string (schema `createdAtDateTime`) | no | Created at date-time. RFC 3339 format | format: "date-time"; example: "2026-08-05T10:15:00Z" |
| `updated_at` | string (schema `updatedAtDateTime`) | no | Updated at date-time. RFC 3339 format | format: "date-time"; example: "2026-08-05T10:15:00Z" |

<!-- schema: #/components/schemas/claim.OriginalInstruction -->
### Schema `claim.OriginalInstruction`

Pointer: `#/components/schemas/claim.OriginalInstruction`. Type: object (schema `claim.OriginalInstruction`).

> Original Direct Debit Instruction (DDI) the claim relates to

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `clearing_id` | string (schema `mandateClearingId`) | yes | Six-digit clearing ID for the mandate | pattern: "^[0-9]{6}$"; example: "123456" |
| `reference` | string | yes | Original Direct Debit Instruction reference | maxLength: 18; example: "MANDATE-REF-001" |

<!-- schema: #/components/schemas/claim.DisputedTransaction -->
### Schema `claim.DisputedTransaction`

Pointer: `#/components/schemas/claim.DisputedTransaction`. Type: object (schema `claim.DisputedTransaction`).

> Single disputed Direct Debit collection included in the claim

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | string | yes | Disputed transaction amount | maxLength: 20; example: "125.00" |
| `date` | string | yes | Disputed transaction date. Format = YYYY-MM-DD. | format: "date"; example: "2026-08-15" |

<!-- schema: #/components/schemas/listing.Mandate -->
### Schema `listing.Mandate`

Pointer: `#/components/schemas/listing.Mandate`. Type: object (schema `listing.Mandate`).

> A BACS direct debit mandate record returned by the mandate list endpoint.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `mandateId`) | no | Form3-assigned mandate ID | example: "b254bb5e-6f1a-4c2b-9c1e-2f0a6d3e8c11" |
| `external_id` | string (schema `externalId`) | no | Form3-assigned mandate ID (omitted until submitted)<br> | example: "3fa85f64-5717-4562-b3fc-2c963f66afa6" |
| `org_id` | string (schema `orgId`) | no | Organization/tenant ID | example: "TN-KGIOODJD...1000" |
| `account_id` | integer (schema `accountId`) | no | Account ID | example: 12345678 |
| `role` | string (schema `role`) | no | Transaction role | enum: ["PAYER", "PAYEE"]; example: "PAYER" |
| `source` | string (schema `mandateSource`) | no | Distinguishes electronic (AUDDIS) from paper mandates, per Form3's mandate `source` field.<br>  * `auddis` - electronic mandate<br>  * `non-electronic` - paper mandate<br> | enum: ["auddis", "non-electronic"]; example: "auddis" |
| `status` | string (schema `mandate.status`) | no | Mandate lifecycle status.<br>  * `CREATED` - Mandate persisted and imported into Form3; pending submission<br>  * `SUBMITTED` - Mandate submitted to the scheme<br>  * `CONFIRMED` - Mandate confirmed and active<br>  * `AMEND_PENDING` - Amend intent accepted; pending submission to Form3<br>  * `AMENDED` - Amend confirmed<br>  * `CANCEL_PENDING` - Cancel intent accepted; pending submission to Form3<br>  * `CANCELLED` - Mandate cancelled. Terminal state<br>  * `FAILED` - Mandate processing failed. Terminal state<br> | enum: ["CREATED", "SUBMITTED", "CONFIRMED", "AMEND_PENDING", "AMENDED", "CANCEL_PENDING", "CANCELLED", "FAILED"]; example: "CREATED" |
| `reference` | string (schema `reference`) | no | Reference note | example: "Weekly money for Mom" |
| `form3_submission_id` | string (schema `form3SubmissionId`) | no | Form 3 submission ID | example: "9f8c7d6e-5b4a-3c2d-1e0f-a1b2c3d4e5f6" |
| `status_reason` | object (schema `listing.StatusReason`) | no | Present on rejections or returns. |  |
| `created_at` | string (schema `createdAtDateTime`) | no | Created at date-time. RFC 3339 format | format: "date-time"; example: "2026-08-05T10:15:00Z" |
| `updated_at` | string (schema `updatedAtDateTime`) | no | Updated at date-time. RFC 3339 format | format: "date-time"; example: "2026-08-05T10:15:00Z" |

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

<!-- schema: #/components/schemas/listing.StatusReason -->
### Schema `listing.StatusReason`

Pointer: `#/components/schemas/listing.StatusReason`. Type: object (schema `listing.StatusReason`).

> Present on rejections or returns.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `statusReasonCode`) | no | Reason for the return:<br>  * `1` - Instruction cancelled by payer<br>  * `2` - Payer deceased<br>  * `3` - Account transferred to a new bank or building society<br>  * `5` - No account. Handled automatically by Form3 when using Bacs Mandate Management.<br>  * `6` - No instruction. Handled automatically by Form3 when using Bacs Mandate Management.<br>  * `B` - Account closed<br>  * `C` - Account transferred to a different branch of the bank/building society<br>  * `F` - Invalid account type<br>  * `G` - Bank will not accept direct debits on account<br>  * `H` - Instruction has expired. Handled automatically by Form3 when using Bacs Mandate Management.<br>  * `I` - Payer reference is not unique. Handled automatically by Form3 when using Bacs Mandate Management.<br>  * `K` - Instruction cancelled by paying bank.<br> | enum: ["1", "2", "3", "5", "6", "B", "C", "F", "G", "H", "I", "K"]; example: "2" |
| `description` | string | no | Human-readable status reason. | example: "Mandate transferred to a new bank" |

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
| `api-specs/Payment_rails_-_BACS_payments.yaml` | tag `BACS direct debit`: POST /v1/payments/bacs/directdebit/paper-mandates, GET /v1/payments/bacs/directdebit/claims, POST /v1/payments/bacs/directdebit/claims, POST /v1/payments/bacs/directdebit/claims/reversal/{id}, GET /v1/payments/bacs/directdebit/mandates, PATCH /v1/payments/bacs/directdebit/mandates/{id}, GET /v1/payments/bacs/directdebit, POST /v1/payments/bacs/directdebit/mandates/{id}/cancel | https://github.com/PismoDevEx/pismo-api-specs | `07915101c3111d71…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-ebacs` — Error codes: EBACS
- `KU-EVT-catalogue-bacs` — Event catalogue: bacs
- `KU-PAY-bacs` — BACS: clearing, Direct Debit mandates and indemnity claims
