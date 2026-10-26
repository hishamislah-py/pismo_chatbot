---
ku_id: KU-API-instant-payments-pix-payments--pix-part-02
title: 'API reference: Instant payments - Pix payments — Pix (part 2 of 2)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Instant_payments_-_Pix_payments.yaml
  sha256: 034f2ce79f002354b67746b854ac39de6bcc9063b279eec88e9a7207202ad8f7
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
operations:
- get-transaction-e2e
- post-transactions-search
- get-pix-transaction
related_kus:
- KU-ERR-codes-epix
specification_version: '1.0'
---

# API reference: Instant payments - Pix payments — Pix (part 2 of 2)

**KU ID:** `KU-API-instant-payments-pix-payments--pix-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Pix` in `api-specs/Instant_payments_-_Pix_payments.yaml` (“Instant payments - Pix payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction` | `get-transaction-e2e` | Get Pix transaction by end-to-end ID | no |
| `POST /pix/v1/pix/transactions/search` | `post-transactions-search` | Get Pix transaction by client request ID | no |
| `GET /pix/v1/pix/provider/transaction/type/{type}/end-to-end/{end_to_end_id}` | `get-pix-transaction` | Get transaction from provider | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=GET path=/pix/v1/pix/end-to-end/{end_to_end_id}/transaction operationId=get-transaction-e2e -->
### `GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction` — Get Pix transaction by end-to-end ID

- **operationId:** `get-transaction-e2e`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Retrieve transaction information given an `end-to-end` value in the path.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo accound ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `end_to_end_id` | path | yes | string | Transaction end-to-end ID. This field is a Brazil Central Bank (BCB) requirement to track all Pix transaction steps. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `pix.TransactionWithDetailResponse`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `org_id` | string | no | Organization/tenant ID. | example: "TN-1234..." |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID. | example: 5869300 |
| `ispb` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `type` | string (schema `PixOutType`) | no | Pix transaction type. | enum: ["PIX-IN", "PIX-OUT", "PIX-IN-REVERSAL", "PIX-OUT-REVERSAL"]; example: "PIX-IN" |
| `transaction_type` | string (schema `TransactionType`) | no | Type of transaction the QR Code validation generates.<br>* `TRANSFER` - Standard immediate transfer payment. <br>* `CHANGE` - Occurs when the QR Code validation returns `CHANGE`. For example, the customer buys something and pays more than the product value to receive the difference in cash. <br>* `WITHDRAWAL` - Occurs when the QR Code validation returns `WITHDRAWAL` with `withdrawal` object values.<br>* `REFUND_AUTOMATIC_PIX` - Total or partial to the PSP payer user within the Automatic Pix MED (Pix return mechanism) scope (only when initiated by a `MANUAL`).<br>* `REFUND` = Total or partial refund to the paying user within the scope of MED 2.0, when this refund occurs from the PI Account of the user's PSP who participated in the distribution chain of the resources of the original transaction (only when initiated by a `MANUAL`)<br> | enum: ["TRANSFER", "CHANGE", "WITHDRAWAL", "REFUND_AUTOMATIC_PIX", "REFUND"]; example: "TRANSFER" |
| `initiation_type` | string (schema `InitiationType`) | no | Initiation type:  <br><br>  `MANUAL` - Manually initiated. Key is not used - bank account, bank code, document number, and branch are used for identification.<br><br>  `DICT` - Diretorio de Identificadores de Contas de Transacapo (Transaction accounts ID directory). Pix/DICT key is used for identification.<br><br>  `STATIC_QRCODE` - Reusable code that contains only the data necessary to complete a transaction. When using static QR Code, the transaction amount must be provided manually.<br><br>  `DYNAMIC_QRCODE` - The amount and other details for a dynamic code are included automatically. <br>  <br>  `PAYMENT_INITIATOR` - Payment provider initiated. A payment initiator is a 3rd party that has obtained authorization from the Central Bank and has an <a href="https://www.bcb.gov.br/en/financialstability/open_finance" target="_blank">Open Finance</a> certification.<br><br>  `AUTOMATIC_PIX` - Payment order initiated via automatic PIX.<br>  <br>  `DYNAMIC_PROXIMITY_PIX` - Dynamic Near Field Communications (NFC) based initiation.<br><br>  `STATIC_PROXIMITY_PIX` - Static NFC-based initiation.<br> | enum: ["MANUAL", "DICT", "STATIC_QRCODE", "DYNAMIC_QRCODE", "PAYMENT_INITIATOR", "AUTOMATIC_PIX", "DYNAMIC_PROXIMITY_PIX", "STATIC_PROXIMITY_PIX"]; maxLength: 20; example: "DICT" |
| `status` | string (schema `TransactionStatus`) | no | Current transaction status:<br><br>  * `VALIDATED` - Payload was validated and sent to provider<br>    <br>  * `PROCESSING` - Waiting response from the provider<br>    <br>  * `SETTLED` - Transaction confirmed<br>    <br>  * `CANCELLED` - Transaction cancelled<br>    <br>  * `ERROR` - Transaction error during processing<br> | enum: ["PROCESSING", "VALIDATED", "SETTLED", "CANCELLED", "ERROR"]; example: "PROCESSING" |
| `correlation_id` | string | no | Correlation tracking ID (CID) | example: "8675309" |
| `authorization_id` | integer (schema `AuthorizationID`) | no | Generated authorization ID on P2P | example: 82725717 |
| `client_request_id` | string (schema `ClientRequestID`) | no | For Pix-out, this is the client-generated ID used for idempotency.<br>For Pix-in, this is the confirmation request ID the provider received.<br> | example: "b84da2fc-dd63-4c6c-a346-797b65f334c7" |
| `payee` | object (schema `pix.TransactionExternalAccount`) | no |  |  |
| `payer` | object (schema `pix.TransactionExternalAccount`) | no |  |  |
| `initiator_document_number` | string | no | Payment initiator document number when `type` is `PAYMENT_INITIATOR` | maxLength: 14; example: "12345678900" |
| `initial_amount` | string (schema `InitialAmount`) | no | The initial purchase price amount before charges or withdrawal changes. | example: "10.02" |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `internal` | boolean (schema `Internal`) | no | Was transaction made between a Pismo organization's accounts? In this case, the instant payment system is not called. | example: false |
| `additional_description` | string | no | Additional description | example: "Charge #1" |
| `qr_code_additional_information` | array of object (schema `QRcodeAddInfo`) | no | Additional QR Code information. |  |
| `qr_code_additional_information[].name` | string | no | QR Code name | example: "Discount" |
| `qr_code_additional_information[].value` | string | no | QR Code value | example: "Paying until the 5th, there will be a 10% discount" |
| `transaction_identification` | string (schema `TransactionID`) | no | This field is returned from the [Validate QR Code](ref:post-qr-code) endpoint.<br><br>Transaction ID is **REQUIRED** when `initiation_type` is `DYNAMIC_QRCODE` and should not be passed otherwise. If a `STATIC_QRCODE` contains the transaction identification, it is also **REQUIRED** to pass it. <br> | example: "1a84daf6-a61b-4aba-919a-a9943db7102e" |
| `reason` | string (schema `ReversalReason`) | no | Reversal reason. | enum: ["USER_REQUESTED", "FRAUD", "BANK_ERROR"]; example: "USER_REQUESTED" |
| `external_id` | string | no | Provider external ID | example: "1236723" |
| `external_movement_id` | string | no | Provider external movement identification | example: "12345678" |
| `migration_id` | string | no | Transaction migration ID (if migrated). | example: "c80118a7-7cef-4378-a3be-e0e28efbf150" |
| `charges` | object (schema `pix.TransactionCharge`) | no |  |  |
| `dates` | object (schema `pix.TransactionDates`) | no |  |  |
| `taxes` | object (schema `Taxes`) | no | Only available in the test environment for direct participants. Tax information related to the transaction.<br> |  |

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
403 Example `EPIX0009` (Missing required header: "x-tenant"):

```json
{
  "code": "EPIX0009",
  "message": "Missing required header: \"x-tenant\""
}
```

403 Example `EPIX0010` (Invalid account id header: "x-account-id"):

```json
{
  "code": "EPIX0010",
  "message": "Invalid account id header: \"x-account-id\""
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EPIX0086` (Transaction not found.):

```json
{
  "code": "EPIX0086",
  "message": "Transaction not found."
}
```

404 Example `EPIX0087` (Pix TransactionDetail not found.):

```json
{
  "code": "EPIX0087",
  "message": "Pix TransactionDetail not found."
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
500 Example `EPIX0004` (Internal server error):

```json
{
  "code": "EPIX0004",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 404 | `EPIX0086` | Transaction not found. |
| 404 | `EPIX0087` | Pix TransactionDetail not found. |
| 500 | `EPIX0004` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=POST path=/pix/v1/pix/transactions/search operationId=post-transactions-search -->
### `POST /pix/v1/pix/transactions/search` — Get Pix transaction by client request ID

- **operationId:** `post-transactions-search`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get a Pix transaction using the `client_request_id` passed when the transaction was created.
>
> The `client_request_id` is the value passed in the `Idempotency-Key` header when creating a cashin (Pix-in) or cashout (Pix-out) transaction. 
>
> This endpoint is useful, for example, when a [Pix-out transfer](ref:post-pix-out-transfer) request times out and the client does not yet have the `end_to_end_id` needed to query the transaction through the [Get Pix transaction by end-to-end ID](ref:get-transaction-e2e) endpoint.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `pix.TransactionSearchRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `client_request_id` | string (schema `ClientRequestID`) | yes | For Pix-out, this is the client-generated ID used for idempotency.<br>For Pix-in, this is the confirmation request ID the provider received.<br> | example: "b84da2fc-dd63-4c6c-a346-797b65f334c7" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `pix.TransactionWithDetailResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `org_id` | string | no | Organization/tenant ID. | example: "TN-1234..." |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID. | example: 5869300 |
| `ispb` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `type` | string (schema `PixOutType`) | no | Pix transaction type. | enum: ["PIX-IN", "PIX-OUT", "PIX-IN-REVERSAL", "PIX-OUT-REVERSAL"]; example: "PIX-IN" |
| `transaction_type` | string (schema `TransactionType`) | no | Type of transaction the QR Code validation generates.<br>* `TRANSFER` - Standard immediate transfer payment. <br>* `CHANGE` - Occurs when the QR Code validation returns `CHANGE`. For example, the customer buys something and pays more than the product value to receive the difference in cash. <br>* `WITHDRAWAL` - Occurs when the QR Code validation returns `WITHDRAWAL` with `withdrawal` object values.<br>* `REFUND_AUTOMATIC_PIX` - Total or partial to the PSP payer user within the Automatic Pix MED (Pix return mechanism) scope (only when initiated by a `MANUAL`).<br>* `REFUND` = Total or partial refund to the paying user within the scope of MED 2.0, when this refund occurs from the PI Account of the user's PSP who participated in the distribution chain of the resources of the original transaction (only when initiated by a `MANUAL`)<br> | enum: ["TRANSFER", "CHANGE", "WITHDRAWAL", "REFUND_AUTOMATIC_PIX", "REFUND"]; example: "TRANSFER" |
| `initiation_type` | string (schema `InitiationType`) | no | Initiation type:  <br><br>  `MANUAL` - Manually initiated. Key is not used - bank account, bank code, document number, and branch are used for identification.<br><br>  `DICT` - Diretorio de Identificadores de Contas de Transacapo (Transaction accounts ID directory). Pix/DICT key is used for identification.<br><br>  `STATIC_QRCODE` - Reusable code that contains only the data necessary to complete a transaction. When using static QR Code, the transaction amount must be provided manually.<br><br>  `DYNAMIC_QRCODE` - The amount and other details for a dynamic code are included automatically. <br>  <br>  `PAYMENT_INITIATOR` - Payment provider initiated. A payment initiator is a 3rd party that has obtained authorization from the Central Bank and has an <a href="https://www.bcb.gov.br/en/financialstability/open_finance" target="_blank">Open Finance</a> certification.<br><br>  `AUTOMATIC_PIX` - Payment order initiated via automatic PIX.<br>  <br>  `DYNAMIC_PROXIMITY_PIX` - Dynamic Near Field Communications (NFC) based initiation.<br><br>  `STATIC_PROXIMITY_PIX` - Static NFC-based initiation.<br> | enum: ["MANUAL", "DICT", "STATIC_QRCODE", "DYNAMIC_QRCODE", "PAYMENT_INITIATOR", "AUTOMATIC_PIX", "DYNAMIC_PROXIMITY_PIX", "STATIC_PROXIMITY_PIX"]; maxLength: 20; example: "DICT" |
| `status` | string (schema `TransactionStatus`) | no | Current transaction status:<br><br>  * `VALIDATED` - Payload was validated and sent to provider<br>    <br>  * `PROCESSING` - Waiting response from the provider<br>    <br>  * `SETTLED` - Transaction confirmed<br>    <br>  * `CANCELLED` - Transaction cancelled<br>    <br>  * `ERROR` - Transaction error during processing<br> | enum: ["PROCESSING", "VALIDATED", "SETTLED", "CANCELLED", "ERROR"]; example: "PROCESSING" |
| `correlation_id` | string | no | Correlation tracking ID (CID) | example: "8675309" |
| `authorization_id` | integer (schema `AuthorizationID`) | no | Generated authorization ID on P2P | example: 82725717 |
| `client_request_id` | string (schema `ClientRequestID`) | no | For Pix-out, this is the client-generated ID used for idempotency.<br>For Pix-in, this is the confirmation request ID the provider received.<br> | example: "b84da2fc-dd63-4c6c-a346-797b65f334c7" |
| `payee` | object (schema `pix.TransactionExternalAccount`) | no |  |  |
| `payer` | object (schema `pix.TransactionExternalAccount`) | no |  |  |
| `initiator_document_number` | string | no | Payment initiator document number when `type` is `PAYMENT_INITIATOR` | maxLength: 14; example: "12345678900" |
| `initial_amount` | string (schema `InitialAmount`) | no | The initial purchase price amount before charges or withdrawal changes. | example: "10.02" |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `internal` | boolean (schema `Internal`) | no | Was transaction made between a Pismo organization's accounts? In this case, the instant payment system is not called. | example: false |
| `additional_description` | string | no | Additional description | example: "Charge #1" |
| `qr_code_additional_information` | array of object (schema `QRcodeAddInfo`) | no | Additional QR Code information. |  |
| `qr_code_additional_information[].name` | string | no | QR Code name | example: "Discount" |
| `qr_code_additional_information[].value` | string | no | QR Code value | example: "Paying until the 5th, there will be a 10% discount" |
| `transaction_identification` | string (schema `TransactionID`) | no | This field is returned from the [Validate QR Code](ref:post-qr-code) endpoint.<br><br>Transaction ID is **REQUIRED** when `initiation_type` is `DYNAMIC_QRCODE` and should not be passed otherwise. If a `STATIC_QRCODE` contains the transaction identification, it is also **REQUIRED** to pass it. <br> | example: "1a84daf6-a61b-4aba-919a-a9943db7102e" |
| `reason` | string (schema `ReversalReason`) | no | Reversal reason. | enum: ["USER_REQUESTED", "FRAUD", "BANK_ERROR"]; example: "USER_REQUESTED" |
| `external_id` | string | no | Provider external ID | example: "1236723" |
| `external_movement_id` | string | no | Provider external movement identification | example: "12345678" |
| `migration_id` | string | no | Transaction migration ID (if migrated). | example: "c80118a7-7cef-4378-a3be-e0e28efbf150" |
| `charges` | object (schema `pix.TransactionCharge`) | no |  |  |
| `dates` | object (schema `pix.TransactionDates`) | no |  |  |
| `taxes` | object (schema `Taxes`) | no | Only available in the test environment for direct participants. Tax information related to the transaction.<br> |  |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EPIX0032` (Error unmarshalling request body):

```json
{
  "code": "EPIX0032",
  "message": "Error unmarshalling request body"
}
```

400 Example `EPIX0049` (Payload validation):

```json
{
  "code": "EPIX0049",
  "message": "Validation error",
  "details": {
    "payload": [
      {
        "field": "client_request_id",
        "message": "Field \"client_request_id\" is required"
      }
    ]
  }
}
```

##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
403 Example `EPIX0009` (Missing required header: "x-tenant"):

```json
{
  "code": "EPIX0009",
  "message": "Missing required header: \"x-tenant\""
}
```

403 Example `EPIX0010` (Invalid account id header: "x-account-id"):

```json
{
  "code": "EPIX0010",
  "message": "Invalid account id header: \"x-account-id\""
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EPIX0086` (Pix Transaction not found):

```json
{
  "code": "EPIX0086",
  "message": "Pix Transaction not found"
}
```

404 Example `EPIX0087` (Pix TransactionDetail is not found):

```json
{
  "code": "EPIX0087",
  "message": "Pix TransactionDetail is not found"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
500 Example `EPIX0004` (Internal server error):

```json
{
  "code": "EPIX0004",
  "message": "Internal server error"
}
```

500 Example `EPIX0014` (Database internal Error):

```json
{
  "code": "EPIX0014",
  "message": "Database internal Error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPIX0032` | Error unmarshalling request body |
| 400 | `EPIX0049` | Validation error |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 404 | `EPIX0086` | Pix Transaction not found |
| 404 | `EPIX0087` | Pix TransactionDetail is not found |
| 500 | `EPIX0004` | Internal server error |
| 500 | `EPIX0014` | Database internal Error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=GET path=/pix/v1/pix/provider/transaction/type/{type}/end-to-end/{end_to_end_id} operationId=get-pix-transaction -->
### `GET /pix/v1/pix/provider/transaction/type/{type}/end-to-end/{end_to_end_id}` — Get transaction from provider

- **operationId:** `get-pix-transaction`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Get Pix transaction from the provider given its type and end-to-end-ID in the path. Can be used to verify that both provider and Pismo have the same information. 
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo accound ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `type` | path | yes | string | Pix transaction type | enum: ["PIX-IN", "PIX-OUT", "PIX-IN-REVERSAL", "PIX-OUT-REVERSAL"]; example: "PIX-IN" |
| `end_to_end_id` | path | yes | string | Transaction end-to-end ID. This field is a Brazil Central Bank (BCB) requirement to track all Pix transaction steps. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `pix.GetTransactionByTypeAndE2EResponse`) |
| 400 | Bad request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `payee` | object (schema `pix.TransactionExternalAccount`) | no |  |  |
| `payer` | object (schema `pix.TransactionExternalAccount`) | no |  |  |
| `status` | string (schema `TransactionStatus`) | no | Current transaction status:<br><br>  * `VALIDATED` - Payload was validated and sent to provider<br>    <br>  * `PROCESSING` - Waiting response from the provider<br>    <br>  * `SETTLED` - Transaction confirmed<br>    <br>  * `CANCELLED` - Transaction cancelled<br>    <br>  * `ERROR` - Transaction error during processing<br> | enum: ["PROCESSING", "VALIDATED", "SETTLED", "CANCELLED", "ERROR"]; example: "PROCESSING" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
##### Response 403

- Response header `x-cid`: Request tracking ID. (string)
##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
##### Response 500

- Response header `x-cid`: Request tracking ID. (string)

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/pix.TransactionExternalAccount -->
### Schema `pix.TransactionExternalAccount`

Pointer: `#/components/schemas/pix.TransactionExternalAccount`. Type: object (schema `pix.TransactionExternalAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `bank_account` | object (schema `pix.TransactionExternalBankAccount`) | no | Bank account details. |  |
| `document` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |

<!-- schema: #/components/schemas/pix.TransactionCharge -->
### Schema `pix.TransactionCharge`

Pointer: `#/components/schemas/pix.TransactionCharge`. Type: object (schema `pix.TransactionCharge`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `discount_value` | number (schema `DiscountValue`) | no | Discount value. | example: 0.15 |
| `fine_value` | number (schema `FineValue`) | no | Fine value. | example: 5.15 |
| `interest_value` | number (schema `InterestValue`) | no | Interest value. | example: 20.15 |
| `settlement_value` | number | no | Settlement value |  |

<!-- schema: #/components/schemas/pix.TransactionDates -->
### Schema `pix.TransactionDates`

Pointer: `#/components/schemas/pix.TransactionDates`. Type: object (schema `pix.TransactionDates`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `created_datetime` | string | no | Date/time created on Pismo platform. RFC 3339 format. | example: "2021-10-11T19:01:43.392Z" |
| `psp_transaction_created_at` | string | no | PSP-generated transaction date/time. If not passed, Pismo generates this field upon request. RFC 3339 format. | example: "2021-10-12T19:01:43.392Z" |
| `received_datetime` | string | no | Date/time when Pismo received request. | example: "2021-10-12T19:01:43.392Z" |
| `updated_datetime` | string | no | Last update date/time. RFC 3339 format. | example: "2021-10-12T19:01:43.392Z" |

<!-- schema: #/components/schemas/Taxes -->
### Schema `Taxes`

Pointer: `#/components/schemas/Taxes`. Type: object (schema `Taxes`).

> Only available in the test environment for direct participants. Tax information related to the transaction.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_identifier` | string (schema `TaxIdentifier`) | no | Tax identifier, referring to the NFe, NFSe or aggregating tax document. <br><br>In Brazil, NF-e and NFS-e are the two primary types of mandatory electronic invoices (Notas Fiscais) used for tax compliance.<br><br> * NF-e (Nota Fiscal Eletrônica): Used for the sale and movement of physical goods or products. It is regulated at the state level by SEFAZ (SEFAZ (Secretaria da Fazenda) is the State Department of Finance in Brazil.) and travels with the goods.<br><br> * NFS-e (Nota Fiscal de Serviços Eletrônica): Used for the provision of services (e.g., consulting, repairs, digital subscriptions). It is regulated by individual city governments.<br><br>The value entered must correspond to the tax document used for calculating the IBS and CBS taxes associated with the transaction.<br> | maxLength: 50; example: "IS0435879820240605bcdb1fhn43a" |
| `records` | array of object (schema `Records`) | no | Tax record types information. You must pass, at a minimum, 2 objects - at least one with `CBS` tax type and at least one with `IBS` tax type.<br> |  |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

<!-- schema: #/components/schemas/pix.TransactionExternalBankAccount -->
### Schema `pix.TransactionExternalBankAccount`

Pointer: `#/components/schemas/pix.TransactionExternalBankAccount`. Type: object (schema `pix.TransactionExternalBankAccount`).

> Bank account details.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |

<!-- schema: #/components/schemas/Records -->
### Schema `Records`

Pointer: `#/components/schemas/Records`. Type: object (schema `Records`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_type` | string (schema `TaxType`) | no | Tax type:<br><br> `IBS` = Goods and services tax. A state and municipal tax that unifies and replaces the main subnational consumption taxes (state ICMS and municipal ISS).<br><br>`CBS` = Contribution on goods and services. A federal tax that consolidates and replaces previous federal social contributions and taxes (PIS, Cofins, and IPI).<br> | enum: ["CBS", "IBS"]; example: "IBS" |
| `amount` | number (schema `TaxAmount`) | no | Tax amount. Must be greater than zero. | example: 1050.44 |

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
| `code` | string | yes | Error code. | example: "PBE315" |
| `message` | string | yes | Error message. | example: "Generic error" |

<!-- schema: #/components/schemas/customer.ParameterMessage -->
### Schema `customer.ParameterMessage`

Pointer: `#/components/schemas/customer.ParameterMessage`. Type: object (schema `customer.ParameterMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Parameter field | example: "Query parameter" |
| `message` | string | yes | Message about parameter | example: "Generic error" |

<!-- schema: #/components/schemas/customer.PayloadMessage -->
### Schema `customer.PayloadMessage`

Pointer: `#/components/schemas/customer.PayloadMessage`. Type: object (schema `customer.PayloadMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string | yes | Payload parameter | example: "Entity.field" |
| `message` | string | yes | Message about error | example: "Generic error" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Instant_payments_-_Pix_payments.yaml` | tag `Pix`: GET /pix/v1/pix/end-to-end/{end_to_end_id}/transaction, POST /pix/v1/pix/transactions/search, GET /pix/v1/pix/provider/transaction/type/{type}/end-to-end/{end_to_end_id} | https://github.com/PismoDevEx/pismo-api-specs | `034f2ce79f002354…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-epix` — Error codes: EPIX
