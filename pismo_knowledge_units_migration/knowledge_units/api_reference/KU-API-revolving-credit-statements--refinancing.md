---
ku_id: KU-API-revolving-credit-statements--refinancing
title: 'API reference: Revolving credit - Statements — Refinancing'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Statements.yaml
  sha256: 2ffe392a0e56ae3b5bf71474f241d08b9b078bb852ffaeff142b4dd32d278fd1
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
- GetInstallmentPayments
- InstallmentPaymentsv4
- GetInstallmentPaymentByPaymentAgreementId
- DeleteInstallmentPaymentByPaymentAgreementId
- updateUserOriginalRate
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CORE-accounting-scripts-examples
- KU-CRED-agreements
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-ex
- KU-EVT-catalogue-balance
- KU-EVT-statement-data-events
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Refinancing

**KU ID:** `KU-API-revolving-credit-statements--refinancing` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Refinancing` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Refinancing endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /statements/v4/accounts/{accountId}/installment-payments` | `GetInstallmentPayments` | List payment agreements | no |
| `POST /statements/v4/accounts/{accountId}/installment-payments` | `InstallmentPaymentsv4` | Create payment agreement | no |
| `GET /statements/v4/accounts/{accountId}/installment-payments/{id}` | `GetInstallmentPaymentByPaymentAgreementId` | Get payment agreement | no |
| `DELETE /statements/v4/accounts/{accountId}/installment-payments/{id}` | `DeleteInstallmentPaymentByPaymentAgreementId` | Cancel payment agreement | no |
| `PATCH /statements-v2/v4/accounts/{accountId}/installment-payments/{paymentsAgreementsId}` | `updateUserOriginalRate` | Update agreement original rate | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements/v4/accounts/{accountId}/installment-payments operationId=GetInstallmentPayments -->
### `GET /statements/v4/accounts/{accountId}/installment-payments` — List payment agreements

- **operationId:** `GetInstallmentPayments`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Refinancing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List payment agreements for a specified account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `page` | query | no | integer | Page number | default: 1; format: "int32"; example: 1 |
| `perPage` | query | no | integer | Items per page. Default is 10. | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: oneOf: object (schema `GetInstallmentsPaymentsV4SuccessResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-agreements`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=POST path=/statements/v4/accounts/{accountId}/installment-payments operationId=InstallmentPaymentsv4 -->
### `POST /statements/v4/accounts/{accountId}/installment-payments` — Create payment agreement

- **operationId:** `InstallmentPaymentsv4`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Refinancing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a payment agreement and post the refinanced debt as new installment transactions, beginning from the currently open statement.
>
> The `statement_agreement` and `compulsory` flags are used to specify the transaction types of the transactions that are created on the customer's statement. Here are the possible combinations.
>
> <b>Type of payment agreement:</b> Statement agreement
> Description: The customer renegotiates all debt for all their statements.
> `statement_agreement`: true 
> `compulsory`: false 
> Transaction types of transactions: 
> 712 (INSTALLMENT AGREEMENT) 
> 711 (CREDIT BY AGREEMENT) 
> 713 (CONTRACT AGREEMENT)
>
> <b>Type of payment agreement:</b> Installment agreement
> Description: This an agreement that the customer makes with their credit card issuer stating that they aren't able to pay off their debt within the current month, so they intend to settle the amount over the next few bills. In other words, the amount that remains outstanding is added to their statement for the following month.
> `statement_agreement`: false 
> `compulsory`: false 
> Transaction types of transactions:
> 702 (REFINANCING INSTALLMENT) 
> 701 (INSTALLMENT CREDIT)
> 703 (REFINANCING CONTRACT)
>
> <b>Type of payment agreement:</b> Compulsory agreement
> Description: This is the same as an installment agreement, except that it's the result of a renegotiation that was made independently of the customer. This is mandatory in Brazil, due to a measure initiated by the Central Bank to protect customers from revolving credit interest charged on the unpaid amount of the invoice. According to this measure, after 30 days, the bank or financial institution must offer more advantageous conditions for the customer to pay off the debt. In practice, the amount owed is automatically divided into installments, allowing the user to fit the payment of the debt into their monthly budget.
> `statement_agreement`: false
> `compulsory`: true 
> Transaction types of transactions:
> 722 (CP REFINANCING INSTALLMENT) 
> 721 (CP INSTALLMENT CREDIT) 
> 723 (CP REFINANCING CONTRACT)
>
> <b>Notes:</b>
> - The installment transactions for the refinanced debt have transaction type `REFINANCING AGREEMENT`.
> - The following combination is not valid. It returns the error message "A compulsory request requires the statement agreement field to be set to false."
> `statement_agreement`: true 
> `compulsory`: true 
> - After the installments are created, the Pismo platform asynchronously generates an [Installment payment processed](https://developers.pismo.io/events/docs/balance-installment-payment-processed-1) event. You should not try to access the new payment agreement until you receive this event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `InstallmentPaymentsV4Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `statement_agreement` | boolean (schema `StatementAgreement`) | yes | Is the generated agreement a statement agreement (`true`) or an installment agreement (`false`)? | example: true |
| `installments` | array of object | yes | Installment payments.<br><br><b>Note:</b> You must define at least 2 installment payments.<br> | example: [{"installment_number": 1, "total_amount": 40, "principal_amount": 38, "interest_amount": 1, "interest_rate": 0.1, "iof_amount": 0.5, "daily_iof_amount": 0.5, "description": "installment #1", "custom_transactions": [{"custom_key": "tax", "amount": 1}]}, {"installment_number": 2, "total_amount": 40, "principal_amount": 38, "interest_amount": 1, "interest_rate": 0.1, "iof_amount": 0.5, "daily_iof_amount": 0.5, "description": "installment #2", "custom_transactions": [{"custom_key": "insurance", "amount": 3.99}]}] |
| `installments[].installment_number` | integer (schema `InstallmentNumber`) | yes | Installment number | format: "int32"; minimum: 1; maximum: 36; example: 1 |
| `installments[].total_amount` | number (schema `SumPrincipalWithInterestAndFees`) | yes | Sum of this installment's principal amount with its interest and fees. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 40 |
| `installments[].principal_amount` | number (schema `TotalPrincipalAmountOfInstallments`) | yes | Principal amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 600 |
| `installments[].interest_amount` | number (schema `InterestAmount`) | yes | Interest amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 12.35 |
| `installments[].interest_rate` | number (schema `InstallmentInterestRate`) | yes | Installment's interest rate | format: "float"; minimum: 0; maximum: 999.9; example: 0.1 |
| `installments[].iof_amount` | number (schema `IofAmount`) | yes | IOF (Brazilian tax) amount. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 1.35 |
| `installments[].daily_iof_amount` | number (schema `DailyIofAmount`) | no | Daily IOF (Brazilian tax) amount for installment. Maximum of 2 digits allowed after the decimal place. | format: "float"; example: 0.5 |
| `installments[].description` | string (schema `OptionalDescription`) | no | Optional description for this installment transaction | minLength: 0; maxLength: 32; example: "Installment 1" |
| `installments[].custom_transactions` | array of object (schema `CustomTransaction`) | no | Allows to register a separate custom contract transaction | example: [{"custom_key": "tax", "amount": 100}, {"custom_key": "insurance", "amount": 200}] |
| `installments[].custom_transactions[].custom_key` | string | no | Key for the custom transaction. |  |
| `installments[].custom_transactions[].amount` | number | no | Amount for the custom transaction. | format: "float" |
| `compulsory` | boolean (schema `Compulsory`) | no | Is the generated agreement a compulsory agreement (`true`) or not (`false`)? | default: false; example: true |
| `settle_accrual` | boolean (schema `SettleAccrual`) | no | Is the generated agreement settled to accrual (`true`) or not (`false`)? If `true`, pending accruals are included when calculating the refinanced amount.<br> | default: false; example: false |
| `split_iof` | boolean (schema `SplitIof`) | no | Should IOF be split? If `true`, the Pismo platform generates a separate transaction for the IOF tax. | default: false; example: false |
| `use_original_rate` | boolean (schema `UseOriginalRate`) | no | Set to `true` if the original installment rate should be used to generate accruals. Set to `false`, otherwise. The original installment rate is the payment agreement contract interest rate. So, if this field is set to `true`, this rate is used instead of the transaction category interest rate when a payment agreement installment is due. | default: false; example: false |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Date/time of the down payment. Format = YYYY-MM-DDThr:mm:ss.<br><br>This field may represent the payment date for the down payment. When provided, this date is used as the transaction event date for credit and installments.<br> | format: "date-time"; example: "2021-04-14T12:00:00-03:00" |
| `credit_transaction_description` | string (schema `CreditTransactionDescription`) | no | Credit Transaction Description field is up to 100 characters. | example: "CREDIT TRANSACTION" |
| `metadata` | object (schema `MetadataPaymentAgreementV4`) | no | This is a JSON object converted to a string with additional information relevant to the customer. No business rule validation is performed on it.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> | example: {"key-1": 10, "key-2": 5} |
| `custom_contract_transactions` | array of object (schema `CustomTransaction`) | no | Allows to register a separate custom contract transaction | example: [{"custom_key": "tax", "amount": 100}, {"custom_key": "insurance", "amount": 200}] |
| `custom_contract_transactions[].custom_key` | string | no | Key for the custom transaction. |  |
| `custom_contract_transactions[].amount` | number | no | Amount for the custom transaction. | format: "float" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `InstallmentPaymentsV4SuccessResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `InvalidFieldErrorResponse`), object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `PaymentAgreementID`) | no | Payment agreement ID | format: "int64"; example: 1000 |
| `statement_agreement` | boolean (schema `StatementAgreement`) | no | Is the generated agreement a statement agreement (`true`) or an installment agreement (`false`)? | example: true |
| `compulsory` | boolean (schema `Compulsory`) | no | Is the generated agreement a compulsory agreement (`true`) or not (`false`)? | default: false; example: true |
| `settle_agreement` | boolean (schema `SettledAgreement`) | no | Is the generated agreement settled (`true`) or not (`false`)? | default: false; example: false |
| `split_iof` | boolean (schema `SplitIof`) | no | Should IOF be split? If `true`, the Pismo platform generates a separate transaction for the IOF tax. | default: false; example: false |
| `created_at` | string (schema `CreatedAt`) | no | Creation date/time. Format = yyyy-mm-ddThh:mm:ss. | example: "2021-08-10T00:00:00" |

##### Response 400

400 Example `Compulsory Mode`:

```json
{
  "message": "A compulsory request requires the statement agreement field to be set to false"
}
```

400 Example `Installments Empty`:

```json
{
  "message": "Installments are empty"
}
```

400 Example `Missing Installment Number`:

```json
{
  "message": "Missing installment number"
}
```

400 Example `Invalid Total Amount`:

```json
{
  "message": "The total amount should be equals to the sum of the principal amount, interest amount, and IOF (Brazilian tax) amount"
}
```

400 Example `PaymentAgreement Pending Already exists`:

```json
{
  "message": "PaymentAgreement already exists"
}
```

400 Example `PaymentAgreement Processed Already exists`:

```json
{
  "message": "PaymentAgreement already exists"
}
```

400 Example `Invalid Field`:

```json
{
  "message": "fieldName must not be empty",
  "field": "fieldName"
}
```

##### Response 404

404 Example `Account Not Found` — from `#/components/examples/AccountNotFoundOrInFirstCycle`:

```json
{
  "message": "Account not found or account in first cycle"
}
```

##### Response 423

423 Example `Account Locked`:

```json
{
  "message": "The operation could not be completed because another process is manipulating the account (the account lock could not be obtained). Try again in a moment."
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 500 | `GN0001` | Service is unavailable |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `balance-installment-payment-processed-1` | https://developers.pismo.io/events/docs/balance-installment-payment-processed-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;423;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CORE-accounting-scripts-examples`, `KU-CRED-agreements`, `KU-EVT-statement-data-events`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=GET path=/statements/v4/accounts/{accountId}/installment-payments/{id} operationId=GetInstallmentPaymentByPaymentAgreementId -->
### `GET /statements/v4/accounts/{accountId}/installment-payments/{id}` — Get payment agreement

- **operationId:** `GetInstallmentPaymentByPaymentAgreementId`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Refinancing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a payment agreement by account ID and payment agreement ID.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `id` | path | yes | string | Payment agreement ID | example: "4101" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: oneOf: object (schema `GetInstallmentsPaymentV4SuccessResponse`) |
| 404 | Not Found | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 404

404 Example `PaymentAgreement Not Found`:

```json
{
  "message": "PaymentAgreement not found"
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=DELETE path=/statements/v4/accounts/{accountId}/installment-payments/{id} operationId=DeleteInstallmentPaymentByPaymentAgreementId -->
### `DELETE /statements/v4/accounts/{accountId}/installment-payments/{id}` — Cancel payment agreement

- **operationId:** `DeleteInstallmentPaymentByPaymentAgreementId`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Refinancing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel a payment agreement by account ID and payment agreement ID.
>
> **Note:** A payment agreement can only be canceled within 30 days of the creation date. If you try to cancel an agreement after 30 days, the endpoint returns a 400 error with the message: 'Payment Agreement cancellation period expired'.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token, not a regular access token. Account tokens are encoded with an account ID. Tokens can expire quickly, which can result in an **Unauthorized** message.<br> |  |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `id` | path | yes | string | Payment agreement ID | example: "4101" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: oneOf: object (schema `DeleteInstallmentsPaymentV4SuccessResponse`) |
| 400 | Bad Request | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: anyOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Idempotent Error` — from `#/components/examples/IdempotentError`:

```json
{
  "message": "Already exists an operation with the same data."
}
```

##### Response 404

404 Example `PaymentAgreement Not Found`:

```json
{
  "message": "PaymentAgreement not found"
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CRED-agreements`.

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PATCH path=/statements-v2/v4/accounts/{accountId}/installment-payments/{paymentsAgreementsId} operationId=updateUserOriginalRate -->
### `PATCH /statements-v2/v4/accounts/{accountId}/installment-payments/{paymentsAgreementsId}` — Update agreement original rate

- **operationId:** `updateUserOriginalRate`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Refinancing`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a payment agreement's `use_original_rate` attribute.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |
| `paymentsAgreementsId` | path | yes | integer | Payment agreement ID | format: "int64"; example: 1 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `InstallmentPaymentsV4PatchRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_original_rate` | boolean (schema `UseOriginalRate`) | no | Set to `true` if the original installment rate should be used to generate accruals. Set to `false`, otherwise. The original installment rate is the payment agreement contract interest rate. So, if this field is set to `true`, this rate is used instead of the transaction category interest rate when a payment agreement installment is due. | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `InstallmentPaymentsV4PatchResponse`) |
| 400 | Bad Request | `application/json`: object (schema `StandardErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `StandardErrorResponse`) |
| 503 | Service unavailable | `application/json`: object (schema `StandardErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `previous_use_original_rate` | boolean (schema `PreviousUseOriginalRate`) | no | Previous value for `use_original_rate`. | example: true |
| `current_use_original_rate` | boolean (schema `CurrentUseOriginalRate`) | no | Current value for `use_original_rate`.<br> | example: false |
| `message` | string | no | Update message | example: "This contract’s overdue transactions accrue using the original rate." |

##### Response 400

400 Example `Missing request header`:

```json
{
  "code": "EX0002",
  "message": "Missing request header for method parameter of type String"
}
```

##### Response 404

404 Example `Resource not found`:

```json
{
  "code": "CE0001",
  "message": "Resource not found for given accountId and paymentsAgreementId"
}
```

##### Response 503

503 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EX0002` | Missing request header for method parameter of type String |
| 404 | `CE0001` | Resource not found for given accountId and paymentsAgreementId |
| 503 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;503`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Internal error" |

<!-- schema: #/components/schemas/InvalidFieldErrorResponse -->
### Schema `InvalidFieldErrorResponse`

Pointer: `#/components/schemas/InvalidFieldErrorResponse`. Type: object (schema `InvalidFieldErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Amount must not be empty." |
| `field` | string | yes | Field where error occurred. | example: "amount" |

<!-- schema: #/components/schemas/StandardErrorResponse -->
### Schema `StandardErrorResponse`

Pointer: `#/components/schemas/StandardErrorResponse`. Type: object (schema `StandardErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "1020030" |
| `message` | string | no |  | example: "Error message" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Refinancing`: GET /statements/v4/accounts/{accountId}/installment-payments, POST /statements/v4/accounts/{accountId}/installment-payments, GET /statements/v4/accounts/{accountId}/installment-payments/{id}, DELETE /statements/v4/accounts/{accountId}/installment-payments/{id}, PATCH /statements-v2/v4/accounts/{accountId}/installment-payments/{paymentsAgreementsId} | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CORE-accounting-scripts-examples` — Accounting scripts examples
- `KU-CRED-agreements` — Agreements: compulsory, statement, installment and payment agreements
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-ex` — Error codes: EX
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-statement-data-events` — Revolving credit - Statements
