---
ku_id: KU-API-instant-payments-pix-payments--pix-part-01
title: 'API reference: Instant payments - Pix payments — Pix (part 1 of 2)'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- post-pix-out-transfer
- post-pix-reversal
- post-qr-code
- get-receipts
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-banking-as-a-service
- KU-BANK-banking-overview
- KU-ERR-codes-epix
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-pix
- KU-EVT-client-webhooks-part-01
- KU-EVT-pix-payments-data-events
- KU-GS-get-started-with-pismo-apis
- KU-PAY-pix-and-qr-codes
- KU-PAY-pix-automatic
- KU-PAY-pix-instant-payments
specification_version: '1.0'
---

# API reference: Instant payments - Pix payments — Pix (part 1 of 2)

**KU ID:** `KU-API-instant-payments-pix-payments--pix-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Pix` in `api-specs/Instant_payments_-_Pix_payments.yaml` (“Instant payments - Pix payments”, version `1.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /pix/v1/pix/out/transfer` | `post-pix-out-transfer` | Pix-out transfer | no |
| `POST /pix/v1/pix/in/reversal` | `post-pix-reversal` | Pix reversal | no |
| `POST /pix/v1/pix/qrcode/validate` | `post-qr-code` | Validate QR Code | no |
| `GET /pix/v1/pix/receipts` | `get-receipts` | List account receipts | no |

## Operation contracts

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=POST path=/pix/v1/pix/out/transfer operationId=post-pix-out-transfer -->
### `POST /pix/v1/pix/out/transfer` — Pix-out transfer

- **operationId:** `post-pix-out-transfer`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Perform a Pix-out transfer.
>
> If you are using a key or QR Code, you need to call  <a href="https://developers.pismo.io/pismo-docs/reference/post-v2-pix-keys-validate">Validate DICT key</a> or <a href="https://developers.pismo.io/pismo-docs/reference/post-qr-code">Get and validate QR Code</a> before calling this endpoint. You need to enter the `end_to_end_id` returned from those calls here. Validation and transaction need to occur within 10 seconds. If you are not using a key or QR Code, this endpoint generates and returns an `end_to_end_id` value you can use in other endpoints.
>
> The `end_to_end_id` field is a Brazil Central Bank (BCB) requirement to track Pix transactions.  Basically, there are two steps to a Pix transaction: 1. Initialize a transaction and 2. Confirm a transaction. The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. 
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-pix-out-1">Pix-out notification received</a> event and a <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix reconciliation notification received</a> event.
>
> This endpoint also generates a <a href="https://developers.pismo.io/events/docs/pix-pix-in-1">Pix-in notification received</a> event when the funds are deposited in the payee's account, which can be a Pismo account or an external account.
>
> For all events, the `status` or `result` field indicates operation success or failure.
>
> If the request times out and the `end_to_end_id` was not returned, use the [Get Pix transaction by client request ID](ref:post-transactions-search) endpoint passing the same `Idempotency-Key` sent in this request as the `client_request_id` to recover the transaction status.
>
> For more information, see the [Pix instant payments](doc:pix-instant-payments) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `pix.OutTransferRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Pismo account ID. | example: 5869300 |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `bank_account` | object | yes | Payer's bank account details. |  |
| `bank_account.account_number` | string (schema `AccountNumber2`) | yes | Payer's account number. | maxLength: 20; example: "98765432" |
| `bank_account.account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `bank_account.branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `initiation_type` | string (schema `InitiationType`) | yes | Initiation type:  <br><br>  `MANUAL` - Manually initiated. Key is not used - bank account, bank code, document number, and branch are used for identification.<br><br>  `DICT` - Diretorio de Identificadores de Contas de Transacapo (Transaction accounts ID directory). Pix/DICT key is used for identification.<br><br>  `STATIC_QRCODE` - Reusable code that contains only the data necessary to complete a transaction. When using static QR Code, the transaction amount must be provided manually.<br><br>  `DYNAMIC_QRCODE` - The amount and other details for a dynamic code are included automatically. <br>  <br>  `PAYMENT_INITIATOR` - Payment provider initiated. A payment initiator is a 3rd party that has obtained authorization from the Central Bank and has an <a href="https://www.bcb.gov.br/en/financialstability/open_finance" target="_blank">Open Finance</a> certification.<br><br>  `AUTOMATIC_PIX` - Payment order initiated via automatic PIX.<br>  <br>  `DYNAMIC_PROXIMITY_PIX` - Dynamic Near Field Communications (NFC) based initiation.<br><br>  `STATIC_PROXIMITY_PIX` - Static NFC-based initiation.<br> | enum: ["MANUAL", "DICT", "STATIC_QRCODE", "DYNAMIC_QRCODE", "PAYMENT_INITIATOR", "AUTOMATIC_PIX", "DYNAMIC_PROXIMITY_PIX", "STATIC_PROXIMITY_PIX"]; maxLength: 20; example: "DICT" |
| `ispb` | string (schema `ISPB`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `payee` | object | yes | Payee's information. The payee is the transfer receipient. |  |
| `payee.account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `payee.account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `payee.bank` | string (schema `Bank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `payee.branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `payee.document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `payee.name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `payee.beneficiary_id` | string (schema `BeneficiaryID`) | no | Beneficiary ID. This ID created when the [Register beneficiary](ref:post-intl-bank-accounts-v1-bank-accounts-beneficiaries) endpoint is called.<br> | maxLength: 36; example: "97c96d96-9b87-404b-88e5-287f2b0e6e0a" |
| `payee.key` | string (schema `Key`) | no | Pix key value. | maxLength: 77; example: "email@email.com" |
| `payee.type` | string (schema `PersonType`) | no | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `transaction_type` | string (schema `TransactionType`) | yes | Type of transaction the QR Code validation generates.<br>* `TRANSFER` - Standard immediate transfer payment. <br>* `CHANGE` - Occurs when the QR Code validation returns `CHANGE`. For example, the customer buys something and pays more than the product value to receive the difference in cash. <br>* `WITHDRAWAL` - Occurs when the QR Code validation returns `WITHDRAWAL` with `withdrawal` object values.<br>* `REFUND_AUTOMATIC_PIX` - Total or partial to the PSP payer user within the Automatic Pix MED (Pix return mechanism) scope (only when initiated by a `MANUAL`).<br>* `REFUND` = Total or partial refund to the paying user within the scope of MED 2.0, when this refund occurs from the PI Account of the user's PSP who participated in the distribution chain of the resources of the original transaction (only when initiated by a `MANUAL`)<br> | enum: ["TRANSFER", "CHANGE", "WITHDRAWAL", "REFUND_AUTOMATIC_PIX", "REFUND"]; example: "TRANSFER" |
| `charges` | object | no | Charges details. **REQUIRED** if returned from QR Code validation. |  |
| `charges.discount_value` | number (schema `DiscountValue`) | no | Discount value. | example: 0.15 |
| `charges.interest_value` | number (schema `InterestValue`) | no | Interest value. | example: 20.15 |
| `charges.fine_value` | number (schema `FineValue`) | no | Fine value. | example: 5.15 |
| `charges.settled_value` | number | no | Settlement value. Amount to be transferred after all charges have been applied. | example: 10.15 |
| `debtor` | object | no | Debtor information. The debtor could be the payer, or someone who made a purchase on the payer's behalf. |  |
| `debtor.document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `debtor.name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |
| `end_to_end_id` | string | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>  1. Initialize a transaction <br>  2. Confirm a transaction<br><br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information.<br>**REQUIRED** if you are using a Pix key or QR Code. <br> | example: "E3030629420200808195101608910248" |
| `is_device_registered` | boolean (schema `IsDeviceRegistered`) | no | Is device registered to do a Pix-out transfer? Default is `true`. | example: true |
| `initial_amount` | string (schema `InitialAmount`) | no | The initial purchase price amount before charges or withdrawal changes. | example: "10.02" |
| `initiator_document_number` | string | no | Payment initiator CNPJ, validated as a CNPJ.<br><br>Cadastro Nacional da Pessoa Jurídica (CNPJ) is Brazil's 14-character federal taxpayer registration number for companies and legal entities.<br><br>**REQUIRED** when `initiation_type` = `PAYMENT_INITIATOR`.<br><br>Also accepted when `initiation_type` = `AUTOMATIC_PIX`, for a payment initiator Pix out originated in <a href="https://www.bcb.gov.br/en/financialstability/open_finance" target="_blank">Open Finance</a>. <br><br>It is this field's presence, not the `initiation_type` that identifies an Open Finance origin: when it is passed, `transaction_identification` **MUST NOT** be passed.<br> | maxLength: 14; example: "12345678912345" |
| `payment_type` | string (schema `PaymentType`) | no | Payment type.<br>* `IMMEDIATE` - Immediate payment. <br>* `FRAUD` - Payment due to suspected fraud. **NOT ALLOWED** when `transaction_type` is `REFUND`.<br>* `SCHEDULED` - Scheduled payment.<br> | enum: ["IMMEDIATE", "FRAUD", "SCHEDULED"]; example: "IMMEDIATE" |
| `psp_account` | object (schema `pix.OutTransferPSPaccount`) | no | Payment service provider (PSP) information. This object is **REQUIRED** if `transaction_type` = `REFUND`. |  |
| `transaction_identification` | string | no | This field is returned from the [Validate QR Code](ref:post-qr-code) endpoint.<br><br>Transaction ID is **REQUIRED** in the following circumstances:<br><br>*  If `initiation_type` = `DYNAMIC_QRCODE`. <br><br>* `STATIC_QRCODE` contains the transaction ID<br><br>* If `initiation_type` = `PAYMENT_INITIATOR` (must be less than 26 characters).<br><br>* When `initiation_type` = `AUTOMATIC_PIX` and `initiator_document_number` is **NOT** passed. It must have the originating `pain.013` instruction's value (26 to 35 characters). Do **NOT* pass this if `initiator_document_number` is passed.<br> | example: "1a84daf6-a61b-4aba-919a-a9943db7102e" |
| `metadata` | object (schema `Metadata`) | no | Key-value fields for adding custom information to request. Total maximum object size = 3000 bytes.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that  purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `qr_code_additional_information` | array of object (schema `QRcodeAddInfo`) | no | Additional QR Code information. |  |
| `qr_code_additional_information[].name` | string | no | QR Code name | example: "Discount" |
| `qr_code_additional_information[].value` | string | no | QR Code value | example: "Paying until the 5th, there will be a 10% discount" |
| `remittance_information` | string | no | Text payer wents to send to payment receiver.<br> | maxLength: 140 |
| `urgency` | string (schema `Urgency`) | no | Urgency. Default is `HIGH`. | enum: ["NORMAL", "HIGH"]; example: "HIGH" |
| `withdrawal` | object | no | Withdrawal details. For QR codes and `CHANGE` and `WITHDRAWAL` transactions. For example:  a customer goes to a shop, makes a purchase, and also asks for cash back.<br> |  |
| `withdrawal.agent_modality` | string (schema `AgentModality`) | no | Withdrawal service agent. **REQUIRED** for `CHANGE` and `WITHDRAWAL` transactions.<br /><br>  * `AGTEC` - Agente estabelecimento comercial. For commercial establishment.<br /><br>  * `AGFSS` - Agente Facilitador de Serviço de Saque. For cash machine.<br /><br>  * `AGTOT` - Agente Outra Espécie de Pessoa Jurídicas ou correspondente no País. Withdrawal service facilitator.<br /><br> | enum: ["AGTEC", "AGTOT", "AGPSS"]; example: "AGTEC" |
| `withdrawal.amount` | number | no | Amount's value made available. **REQUIRED** for `CHANGE` or `WITHDRAWAL`, cannot be sent for `TRANSFER`. | example: 101.11 |
| `withdrawal.ispb_service_provider` | string | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. **REQUIRED** for `CHANGE` or `WITHDRAWAL`.<br><br>This is the ISPB for the withdrawal service provider.<br> | maxLength: 8; example: "60701190" |
| `withdrawal.purchase_amount` | number | no | Purchase amount. **REQUIRED** for `CHANGE`. | example: 101.11 |
| `psp_transaction_created_at` | string (schema `PSPtransactionCreatedAt`) | no | Datetime since the transaction was created on client-side.<br><br>Format = RFC 3339 Nano.  For example - `2014-03-19T00:08.179780629-04:00`.<br><br> **REQUIRED** when passing `signature_info`<br> | example: "2014-03-19T00:08.179780629-04:00" |
| `signature_info` | object (schema `pix.SignatureInfo`) | no | Signature information, including the digital signature over the request data that a PSTI validates. A Prestadores de Serviços de Tecnologia da Informação (PSTI) - Information and Technology Service Provider in English — is a technology service provider that connects to the banking/financial infrastructure (specifically the Rede do Sistema Financeiro Nacional - RSFN) on participants' behalf.<br><br>The signature here is the digital signature standard using a private asymmetric key (<a href="https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/" target="_blank">RSA</a> or <a href="https://en.wikipedia.org/wiki/Elliptic-curve_cryptography" target="_blank">Elliptic Curve</a>) over an input buffer extracted from the request and provider-defined. <br><br>This field guarantees the request's integrity and authenticity and the transaction messaging non-repudiation (assurance that a party involved in a transaction cannot later deny their involvement) from customer to PSTI.<br><br>For more information, refer to the  [Scheduled Pix-out transfer encryption](doc:pix-out-transfer-encryption) guide.<br><br>**Note:** Customers should contact the PSTI to get more information about the encryption process and how to store the certificate related to the certificate thumbprint. Pismo acts as a pass-through entity in this process.<br> |  |
| `processing_code` | string | no | A 6-digit code that identifies the financial processing category for the transaction, used for accounting and routing purposes.<br><br>This field is optional. When not provided, Pismo automatically assigns a value managed internally. If you provide a custom value, you take full responsibility for its correctness — an invalid or mismatched code may cause processing or reconciliation failures.<br><br>For more information, refer to the [Processing code](doc:processing-codes-and-transaction-types) guide.<br> | maxLength: 6; example: "123456" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Response Body | `application/json`: object (schema `pix.OutTransferResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking ID. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `end_to_end_id` | string (schema `EndToEndID`) | yes | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `payee_name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `payer_name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `status` | string (schema `TransactionStatus`) | yes | Current transaction status:<br><br>  * `VALIDATED` - Payload was validated and sent to provider<br>    <br>  * `PROCESSING` - Waiting response from the provider<br>    <br>  * `SETTLED` - Transaction confirmed<br>    <br>  * `CANCELLED` - Transaction cancelled<br>    <br>  * `ERROR` - Transaction error during processing<br> | enum: ["PROCESSING", "VALIDATED", "SETTLED", "CANCELLED", "ERROR"]; example: "PROCESSING" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EPIX0020` (SPI Gateway - API returned 4xx error):

```json
{
  "code": "EPIX0020",
  "message": "SPI Gateway - API returned 4xx error",
  "details": {
    "external": [
      {
        "code": "PROVIDER_ERROR_CODE",
        "message": "Provider error message"
      }
    ]
  }
}
```

400 Example `EPIX0032` (Error unmarshalling request body):

```json
{
  "code": "EPIX0032",
  "message": "Error unmarshalling request body"
}
```

400 Example `EPIX0139` (Invalid field size for Cid):

```json
{
  "code": "EPIX0139",
  "message": "Invalid field size for Cid"
}
```

400 Example `EPIX0132` (Invalid field size for Idempotency-Key):

```json
{
  "code": "EPIX0132",
  "message": "Invalid field size for Idempotency-Key"
}
```

400 Example `EPIX0067` (Requester account id does not match with body account_id):

```json
{
  "code": "EPIX0067",
  "message": "Requester account id does not match with body account_id"
}
```

400 Example `EPIX0126` (Required Key):

```json
{
  "code": "EPIX0126",
  "message": "Required Key"
}
```

400 Example `EPIX0115` (Missing required transaction identification):

```json
{
  "code": "EPIX0115",
  "message": "Missing required transaction identification"
}
```

400 Example `EPIX0226` (Transaction identification not allowed with initiator document number):

```json
{
  "code": "EPIX0226",
  "message": "Transaction identification not allowed with initiator document number"
}
```

400 Example `EPIX0227` (Invalid transaction identification length for payment initiator):

```json
{
  "code": "EPIX0227",
  "message": "Invalid transaction identification length for payment initiator"
}
```

400 Example `EPIX0228` (Invalid transaction identification length for automatic pix):

```json
{
  "code": "EPIX0228",
  "message": "Invalid transaction identification length for automatic pix"
}
```

400 Example `EPIX0136` (Missing required initiator document number):

```json
{
  "code": "EPIX0136",
  "message": "Missing required initiator document number"
}
```

400 Example `EPIX0022` (Invalid CNPJ):

```json
{
  "code": "EPIX0022",
  "message": "Invalid CNPJ"
}
```

400 Example `EPIX0137` (Invalid value for urgency field. Value must be 'HIGH'):

```json
{
  "code": "EPIX0137",
  "message": "Invalid value for urgency field. Value must be 'HIGH'"
}
```

400 Example `EPIX0138` (Invalid value for transaction type. Value must be 'TRANSFER'):

```json
{
  "code": "EPIX0138",
  "message": "Invalid value for transaction type. Value must be 'TRANSFER'"
}
```

400 Example `EPIX0113` (Invalid initiation type):

```json
{
  "code": "EPIX0113",
  "message": "Invalid initiation type"
}
```

400 Example `EPIX0123` (Required withdrawal):

```json
{
  "code": "EPIX0123",
  "message": "Required withdrawal"
}
```

400 Example `EPIX0120` (Missing required purchase amount):

```json
{
  "code": "EPIX0120",
  "message": "Missing required purchase amount"
}
```

400 Example `EPIX0124` (Invalid amount):

```json
{
  "code": "EPIX0124",
  "message": "Invalid amount"
}
```

400 Example `EPIX0122` (Invalid withdraw amount):

```json
{
  "code": "EPIX0122",
  "message": "Invalid withdraw amount"
}
```

400 Example `EPIX0141` (It's not allow transaction to the same AccountID):

```json
{
  "code": "EPIX0141",
  "message": "It's not allow transaction to the same AccountID"
}
```

400 Example `EPIX0019` (Accounts - API returned 4xx error):

```json
{
  "code": "EPIX0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EPIX0008` (Account blocked or cancelled):

```json
{
  "code": "EPIX0008",
  "message": "Account blocked or cancelled"
}
```

400 Example `EPIX0053` (IntlBankAccounts - API returned 4xx error):

```json
{
  "code": "EPIX0053",
  "message": "IntlBankAccounts - API returned 4xx error"
}
```

400 Example `EPIX0003` (Account not found):

```json
{
  "code": "EPIX0003",
  "message": "Account not found"
}
```

400 Example `EPIX0149` (Beneficiary is not enabled):

```json
{
  "code": "EPIX0113",
  "message": "Beneficiary is not enabled"
}
```

400 Example `EPIX0114` (Beneficiary information does not match Payee's information):

```json
{
  "code": "EPIX0114",
  "message": "Beneficiary information does not match Payee's information"
}
```

400 Example `EPIX0061` (PixDict - API returned 4xx error):

```json
{
  "code": "EPIX0061",
  "message": "PixDict - API returned 4xx error"
}
```

400 Example `EPIX0068` (Invalid EndToEndID):

```json
{
  "code": "EPIX0068",
  "message": "Invalid EndToEndID"
}
```

400 Example `EPIX0130` (Transaction type not found):

```json
{
  "code": "EPIX0130",
  "message": "Transaction type not found"
}
```

400 Example `EPIX0045` (P2P API returned 4xx error):

```json
{
  "code": "EPIX0045",
  "message": "P2P API returned 4xx error"
}
```

400 Example `EPIX0110` (The amount passed is greater than the current balance):

```json
{
  "code": "EPIX0110",
  "message": "The amount passed is greater than the current balance"
}
```

400 Example `EPIX0146` (No Orgs operation found):

```json
{
  "code": "EPIX0146",
  "message": "No Orgs operation found"
}
```

400 Example `EPIX0160` (Field transaction_identification can not be filled when initiation_type is MANUAL or DICT):

```json
{
  "code": "EPIX0160",
  "message": "Field transaction_identification can not be filled when initiation_type is MANUAL or DICT"
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
        "field": "account_id",
        "message": "Field \"account_id\" is required"
      },
      {
        "field": "ispb",
        "message": "Field \"ispb\" is required"
      },
      {
        "field": "branch",
        "message": "Field \"branch\" is required"
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

403 Example `EPIX0069` (Missing required header: "Idempotency-Key"):

```json
{
  "code": "EPIX0069",
  "message": "Missing required header: \"Idempotency-Key\""
}
```

403 Example `EPIX0010` (Invalid account id header: "x-account-id"):

```json
{
  "code": "EPIX0010",
  "message": "Invalid account id header: \"x-account-id\""
}
```

403 Example `EPIX0111` (Anti fraud API error):

```json
{
  "code": "EPIX0111",
  "message": "Anti fraud API error"
}
```

403 Example `EPIX0112` (Rejected by Anti fraud API):

```json
{
  "code": "EPIX0112",
  "message": "Rejected by Anti fraud API"
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EPIX0051` (IntlBankAccounts - Not found):

```json
{
  "code": "EPIX0051",
  "message": "IntlBankAccounts - Not found"
}
```

404 Example `EPIX0041` (SPI Gateway - Not found error. Check details):

```json
{
  "code": "EPIX0041",
  "message": "SPI Gateway - Not found error. Check details"
}
```

##### Response 409

- Response header `x-cid`: Request tracking ID. (string)
409 Example `EPIX0071` (Pix transaction already exists):

```json
{
  "code": "EPIX0071",
  "message": "Pix transaction already exists"
}
```

409 Example `EPIX0142` (Already exist a transaction with this EndToEnd):

```json
{
  "code": "EPIX0142",
  "message": "Already exist a transaction with this EndToEnd"
}
```

409 Example `EPIX0144` (Error recording the idempotency):

```json
{
  "code": "EPIX0144",
  "message": "Error recording the idempotency"
}
```

409 Example `EPIX0085` (Duplicated CorrelationId):

```json
{
  "code": "EPIX0085",
  "message": "Duplicated CorrelationId"
}
```

##### Response 429

- Response header `x-cid`: Request tracking ID. (string)
429 Example `EPIX0031` (SPI Gateway - API returned a rate limit error):

```json
{
  "code": "EPIX0031",
  "message": "SPI Gateway - API returned a rate limit error"
}
```

##### Response 500

- Response header `x-cid`: Request tracking ID. (string)
500 Example `EPIX0004` (Internal error):

```json
{
  "code": "EPIX0004",
  "message": "Internal error"
}
```

500 Example `EPIX0005` (Error unmarshalling object):

```json
{
  "code": "EPIX0005",
  "message": "Error unmarshalling object"
}
```

500 Example `EPIX0007` (HTTP error):

```json
{
  "code": "EPIX0007",
  "message": "HTTP error"
}
```

500 Example `EPIX0042` (Accounts API timeout error):

```json
{
  "code": "EPIX0042",
  "message": "Accounts API timeout error"
}
```

500 Example `EPIX0017` (Accounts - API returned 5xx error):

```json
{
  "code": "EPIX0017",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EPIX0108` (Fail to find banking configs):

```json
{
  "code": "EPIX0108",
  "message": "Fail to find banking configs"
}
```

500 Example `EPIX0109` (Invalid type for banking config parameter value):

```json
{
  "code": "EPIX0109",
  "message": "Invalid type for banking config parameter value"
}
```

500 Example `EPIX0014` (Database internal Error):

```json
{
  "code": "EPIX0014",
  "message": "Database internal Error"
}
```

500 Example `EPIX0043` (P2P API timeout error):

```json
{
  "code": "EPIX0043",
  "message": "P2P API timeout error"
}
```

500 Example `EPIX0089` (P2P returned invalid event date):

```json
{
  "code": "EPIX0089",
  "message": "P2P returned invalid event date"
}
```

500 Example `EPIX0046` (P2P API returned 5xx error):

```json
{
  "code": "EPIX0046",
  "message": "P2P API returned 5xx error"
}
```

500 Example `EPIX0070` (Provider returned transaction with error status):

```json
{
  "code": "EPIX0070",
  "message": "Provider returned transaction with error status"
}
```

##### Response 502

- Response header `x-cid`: Request tracking ID. (string)
502 Example `EPIX0018` (SPI Gateway - API returned error):

```json
{
  "code": "EPIX0018",
  "message": "SPI Gateway - API returned error"
}
```

502 Example `EPIX0051` (IntlBankAccounts - API returned 5xx error):

```json
{
  "code": "EPIX0051",
  "message": "IntlBankAccounts - API returned 5xx error"
}
```

502 Example `EPIX0060` (PixDict - API returned 5xx error):

```json
{
  "code": "EPIX0060",
  "message": "PixDict - API returned 5xx error"
}
```

##### Response 504

- Response header `x-cid`: Request tracking ID. (string)
504 Example `EPIX0030` (SPI Gateway - API returned a timeout error):

```json
{
  "code": "EPIX0030",
  "message": "SPI Gateway - API returned a timeout error"
}
```

504 Example `EPIX0050` (IntlBankAccounts - API timeout):

```json
{
  "code": "EPIX0050",
  "message": "IntlBankAccounts - API timeout"
}
```

504 Example `EPIX0058` (PixDict - API timeout):

```json
{
  "code": "EPIX0058",
  "message": "PixDict - API timeout"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPIX0020` | SPI Gateway - API returned 4xx error |
| 400 | `EPIX0032` | Error unmarshalling request body |
| 400 | `EPIX0139` | Invalid field size for Cid |
| 400 | `EPIX0132` | Invalid field size for Idempotency-Key |
| 400 | `EPIX0067` | Requester account id does not match with body account_id |
| 400 | `EPIX0126` | Required Key |
| 400 | `EPIX0115` | Missing required transaction identification |
| 400 | `EPIX0226` | Transaction identification not allowed with initiator document number |
| 400 | `EPIX0227` | Invalid transaction identification length for payment initiator |
| 400 | `EPIX0228` | Invalid transaction identification length for automatic pix |
| 400 | `EPIX0136` | Missing required initiator document number |
| 400 | `EPIX0022` | Invalid CNPJ |
| 400 | `EPIX0137` | Invalid value for urgency field. Value must be 'HIGH' |
| 400 | `EPIX0138` | Invalid value for transaction type. Value must be 'TRANSFER' |
| 400 | `EPIX0113` | Invalid initiation type |
| 400 | `EPIX0123` | Required withdrawal |
| 400 | `EPIX0120` | Missing required purchase amount |
| 400 | `EPIX0124` | Invalid amount |
| 400 | `EPIX0122` | Invalid withdraw amount |
| 400 | `EPIX0141` | It's not allow transaction to the same AccountID |
| 400 | `EPIX0019` | Accounts - API returned 4xx error |
| 400 | `EPIX0008` | Account blocked or cancelled |
| 400 | `EPIX0053` | IntlBankAccounts - API returned 4xx error |
| 400 | `EPIX0003` | Account not found |
| 400 | `EPIX0114` | Beneficiary information does not match Payee's information |
| 400 | `EPIX0061` | PixDict - API returned 4xx error |
| 400 | `EPIX0068` | Invalid EndToEndID |
| 400 | `EPIX0130` | Transaction type not found |
| 400 | `EPIX0045` | P2P API returned 4xx error |
| 400 | `EPIX0110` | The amount passed is greater than the current balance |
| 400 | `EPIX0146` | No Orgs operation found |
| 400 | `EPIX0160` | Field transaction_identification can not be filled when initiation_type is MANUAL or DICT |
| 400 | `EPIX0049` | Validation error |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0069` | Missing required header: "Idempotency-Key" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 403 | `EPIX0111` | Anti fraud API error |
| 403 | `EPIX0112` | Rejected by Anti fraud API |
| 404 | `EPIX0051` | IntlBankAccounts - Not found |
| 404 | `EPIX0041` | SPI Gateway - Not found error. Check details |
| 409 | `EPIX0071` | Pix transaction already exists |
| 409 | `EPIX0142` | Already exist a transaction with this EndToEnd |
| 409 | `EPIX0144` | Error recording the idempotency |
| 409 | `EPIX0085` | Duplicated CorrelationId |
| 429 | `EPIX0031` | SPI Gateway - API returned a rate limit error |
| 500 | `EPIX0004` | Internal error |
| 500 | `EPIX0005` | Error unmarshalling object |
| 500 | `EPIX0007` | HTTP error |
| 500 | `EPIX0042` | Accounts API timeout error |
| 500 | `EPIX0017` | Accounts - API returned 5xx error |
| 500 | `EPIX0108` | Fail to find banking configs |
| 500 | `EPIX0109` | Invalid type for banking config parameter value |
| 500 | `EPIX0014` | Database internal Error |
| 500 | `EPIX0043` | P2P API timeout error |
| 500 | `EPIX0089` | P2P returned invalid event date |
| 500 | `EPIX0046` | P2P API returned 5xx error |
| 500 | `EPIX0070` | Provider returned transaction with error status |
| 502 | `EPIX0018` | SPI Gateway - API returned error |
| 502 | `EPIX0051` | IntlBankAccounts - API returned 5xx error |
| 502 | `EPIX0060` | PixDict - API returned 5xx error |
| 504 | `EPIX0030` | SPI Gateway - API returned a timeout error |
| 504 | `EPIX0050` | IntlBankAccounts - API timeout |
| 504 | `EPIX0058` | PixDict - API timeout |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-financial-reconciliation-1` | https://developers.pismo.io/events/docs/pix-financial-reconciliation-1 |
| `pix-pix-in-1` | https://developers.pismo.io/events/docs/pix-pix-in-1 |
| `pix-pix-out-1` | https://developers.pismo.io/events/docs/pix-pix-out-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;404;409;429;500;502;504`, has examples `True`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-banking-as-a-service`, `KU-BANK-banking-overview`, `KU-EVT-client-webhooks-part-01`, `KU-EVT-pix-payments-data-events`, `KU-GS-get-started-with-pismo-apis`, `KU-PAY-pix-and-qr-codes`, `KU-PAY-pix-automatic`, `KU-PAY-pix-instant-payments`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=POST path=/pix/v1/pix/in/reversal operationId=post-pix-reversal -->
### `POST /pix/v1/pix/in/reversal` — Pix reversal

- **operationId:** `post-pix-reversal`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Reverse a Pix-out transfer.
>
> This endpoint generates a <a href="https://developers.pismo.io/events/docs/pix-pix-out-reversal-1">Pix-out reversed</a> event and a <a href="https://developers.pismo.io/events/docs/pix-financial-reconciliation-1">Pix  reconciliation notification received</a> event.
>
> This endpoint also generates a <a href="https://developers.pismo.io/events/docs/pix-pix-in-reversal-1">Pix-in reversed</a> event when the funds are transferred from the payee's account, which can be a Pismo account or an external account.
>
> For all events, the `status` or `result` field indicates operation success or failure.
>
> For more information, see the [Pix instant payments](doc:pix-instant-payments) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `Idempotency-Key` | header | yes | string | A unique ID to ensure the operation remains idempotent, allowing for operation repitition without causing unintended effects or duplication. An idempotent operation is one that can be applied multiple times, yet the outcome remains the same. it ensures that network errors, retries, or failures can occur without introducing inconsistencies.<br> |  |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `pix.InReversalRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Pismo account ID. | example: 5869300 |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `end_to_end_id` | string | yes | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br /><br>Basically, there are two steps to a Pix transaction:<br /><br>1. Initialize a transaction <br /><br>2. Confirm a transaction<br /><br><br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information.<br /><br><br>On reversal flow, the `end_to_end_id` is the original transaction `end_to_end_id`.<br /><br> | example: "E3030629420200808195101608910248" |
| `reason` | string (schema `ReversalReason`) | yes | Reversal reason. | enum: ["USER_REQUESTED", "FRAUD", "BANK_ERROR"]; example: "USER_REQUESTED" |
| `additional_information` | string (schema `AdditionalInformation`) | no | Additional information | maxLength: 105 |
| `description` | string | no | Reversal description | maxLength: 140 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Response Body | `application/json`: object (schema `pix.InReversalResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 202

- Response header `x-cid`: Request tracking ID. (string)
**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `reversal_end_to_end_id` | string | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>1. Initialize a transaction <br>2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information.<br><br>Here, the `reversal_end_to_end_id` is generated automatically and begins with a "D".<br> |  |
| `reversal_status` | string | no | Reversal status | enum: ["SETTLED", "PROCESSING", "ERROR"]; example: "SETTLED" |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EPIX0005` (Error unmarshalling object):

```json
{
  "code": "EPIX0005",
  "message": "Error unmarshalling object"
}
```

400 Example `EPIX0020` (SPI Gateway - API returned 4xx error):

```json
{
  "code": "EPIX0020",
  "message": "SPI Gateway - API returned 4xx error",
  "details": {
    "external": [
      {
        "code": "PCE001",
        "message": "The field \"ClientRequestId\" must match the regular expression [a-zA-Z0-9]{1,35}."
      }
    ]
  }
}
```

400 Example `EPIX0045` (P2P API returned 4xx error):

```json
{
  "code": "EPIX0045",
  "message": "P2P API returned 4xx error"
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
        "field": "branch",
        "message": "Field \"branch\" is required"
      },
      {
        "field": "account_number",
        "message": "Field \"account_number\" is required"
      },
      {
        "field": "amount",
        "message": "Field \"amount\" is required"
      }
    ]
  }
}
```

400 Example `EPIX0084` (P2P API returned 400 error - Amount cannot exceed the original transaction amount):

```json
{
  "code": "EPIX0084",
  "message": "P2P API returned 400 error - Amount cannot exceed the original transaction amount"
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

403 Example `EPIX0069` (Missing required header: "Idempotency-Key"):

```json
{
  "code": "EPIX0069",
  "message": "Missing required header: \"Idempotency-Key\""
}
```

403 Example `EPIX0132` (Invalid field size for Idempotency-Key):

```json
{
  "code": "EPIX0132",
  "message": "Invalid field size for Idempotency-Key"
}
```

##### Response 404

- Response header `x-cid`: Request tracking ID. (string)
404 Example `EPIX0003` (Account not found):

```json
{
  "code": "EPIX0003",
  "message": "Account not found"
}
```

404 Example `EPIX0041` (SPI Gateway - Not found error. Check details):

```json
{
  "code": "EPIX0041",
  "message": "SPI Gateway - Not found error. Check details"
}
```

##### Response 409

- Response header `x-cid`: Request tracking ID. (string)
409 Example `EPIX0008` (Account blocked or cancelled):

```json
{
  "code": "EPIX0008",
  "message": "Account blocked or cancelled"
}
```

409 Example `EPIX0071` (Pix transaction already exists):

```json
{
  "code": "EPIX0071",
  "message": "Pix transaction already exists"
}
```

409 Example `EPIX0083` (P2P API returned 409 error - Authorization was already refunded/reversed):

```json
{
  "code": "EPIX0083",
  "message": "P2P API returned 409 error - Authorization was already refunded/reversed"
}
```

409 Example `EPIX0085` (P2P API returned 409 error - Duplicated CorrelationId):

```json
{
  "code": "EPIX0085",
  "message": "P2P API returned 409 error - Duplicated CorrelationId"
}
```

409 Example `EPIX0086` (Pix Transaction not found):

```json
{
  "code": "EPIX0086",
  "message": "Pix Transaction not found"
}
```

##### Response 429

- Response header `x-cid`: Request tracking ID. (string)
429 Example `EPIX0031` (SPI Gateway - API returned a rate limit error):

```json
{
  "code": "EPIX0031",
  "message": "SPI Gateway - API returned a rate limit error"
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

500 Example `EPIX0005` (Error unmarshalling object):

```json
{
  "code": "EPIX0005",
  "message": "Error unmarshalling object"
}
```

500 Example `EPIX0007` (HTTP error):

```json
{
  "code": "EPIX0007",
  "message": "HTTP error"
}
```

500 Example `EPIX0014` (Database internal Error):

```json
{
  "code": "EPIX0014",
  "message": "Database internal Error"
}
```

500 Example `EPIX0043` (P2P API timeout error):

```json
{
  "code": "EPIX0043",
  "message": "P2P API timeout error"
}
```

##### Response 502

- Response header `x-cid`: Request tracking ID. (string)
502 Example `EPIX0018` (SPI Gateway - API returned error):

```json
{
  "code": "EPIX0018",
  "message": "SPI Gateway - API returned error"
}
```

##### Response 504

- Response header `x-cid`: Request tracking ID. (string)
504 Example `EPIX0030` (SPI Gateway - API returned a timeout error):

```json
{
  "code": "EPIX0030",
  "message": "SPI Gateway - API returned a timeout error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPIX0005` | Error unmarshalling object |
| 400 | `EPIX0020` | SPI Gateway - API returned 4xx error |
| 400 | `PCE001` | The field "ClientRequestId" must match the regular expression [a-zA-Z0-9]{1,35}. |
| 400 | `EPIX0045` | P2P API returned 4xx error |
| 400 | `EPIX0049` | Validation error |
| 400 | `EPIX0084` | P2P API returned 400 error - Amount cannot exceed the original transaction amount |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 403 | `EPIX0069` | Missing required header: "Idempotency-Key" |
| 403 | `EPIX0132` | Invalid field size for Idempotency-Key |
| 404 | `EPIX0003` | Account not found |
| 404 | `EPIX0041` | SPI Gateway - Not found error. Check details |
| 409 | `EPIX0008` | Account blocked or cancelled |
| 409 | `EPIX0071` | Pix transaction already exists |
| 409 | `EPIX0083` | P2P API returned 409 error - Authorization was already refunded/reversed |
| 409 | `EPIX0085` | P2P API returned 409 error - Duplicated CorrelationId |
| 409 | `EPIX0086` | Pix Transaction not found |
| 429 | `EPIX0031` | SPI Gateway - API returned a rate limit error |
| 500 | `EPIX0004` | Internal server error |
| 500 | `EPIX0005` | Error unmarshalling object |
| 500 | `EPIX0007` | HTTP error |
| 500 | `EPIX0014` | Database internal Error |
| 500 | `EPIX0043` | P2P API timeout error |
| 502 | `EPIX0018` | SPI Gateway - API returned error |
| 504 | `EPIX0030` | SPI Gateway - API returned a timeout error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `pix-financial-reconciliation-1` | https://developers.pismo.io/events/docs/pix-financial-reconciliation-1 |
| `pix-pix-in-reversal-1` | https://developers.pismo.io/events/docs/pix-pix-in-reversal-1 |
| `pix-pix-out-reversal-1` | https://developers.pismo.io/events/docs/pix-pix-out-reversal-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;403;404;409;429;500;502;504`, has examples `True`, emits events `3`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-client-webhooks-part-01`, `KU-EVT-pix-payments-data-events`, `KU-PAY-pix-instant-payments`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=POST path=/pix/v1/pix/qrcode/validate operationId=post-qr-code -->
### `POST /pix/v1/pix/qrcode/validate` — Validate QR Code

- **operationId:** `post-qr-code`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Retrieve and validate Pix QR Code.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Request Body

**Content type `application/json`** — schema: object (schema `pix.QRCodeRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `emv` | string | yes | BR Code in the Europay, Mastercard, Visa (EMV) format. <br><br>A BR Code is the standard for QR Codes in Brazil and is commonly known as *Boleto Bancario*. A vendor or service provider generates a Boleto Bancario with the necessary information such as the payer's name, the payment amount, the due date, and the vendor's information.<br> | example: "00020126410014BR.GOV.BCB.PIX0119102785947@email.com5204000053039865802BR5915Teste do Fulano6009SAO PAULO61080550900062070503***630495F6" |
| `desired_payment_date` | string | no | Desired payment date, format = YYYY-MM-DD<br><br>This field is used to calculate fees and discounts on QR codes with the due date.<br> | example: "2021-11-18" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `pix.QRCodeResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 409 | Conflict | `application/json`: object (schema `customer.Error`) |
| 429 | Too Many Requests | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |
| 502 | Bad Gateway | `application/json`: object (schema `customer.Error`) |
| 504 | Gateway Timeout | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `additional_information` | array of object (schema `commons.AdditionalInfo`) | no | QR Code additional information. Information generated by payee's participant when transaction is a dynamic QR Code process.<br> |  |
| `allows_value_change` | boolean (schema `AllowsValueChange`) | no | Can the payer change the final amount? | example: false |
| `amount` | number (schema `Amount`) | yes | Amount to be transferred. | example: 1050.44 |
| `charges` | object (schema `commons.Charges`) | no |  |  |
| `dates` | object (schema `commons.Dates`) | no |  |  |
| `debtor` | object (schema `commons.Debtor`) | no |  |  |
| `end_to_end_id` | string (schema `EndToEndID`) | yes | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `initial_amount` | string (schema `InitialAmount`) | no | The initial purchase price amount before charges or withdrawal changes. | example: "10.02" |
| `payee` | object (schema `commons.Payee`) | yes |  |  |
| `payer_solicitation` | string | no | Payer solicitation. The message from the receiver to the payer when using a QR Code. | example: "Enter fidelity card" |
| `qrcode_type` | string (schema `QRcodeType`) | yes | QR Code type: <br>`STATIC` - Static QR Code<br>`STATIC_WITHDRAW` - Static withdrawal<br>`DYNAMIC_COB` - Dynamic QR Code with charge <br>`DYNAMIC_COBV` - Dynamic QR Code with charge that has due date<br>`DYNAMIC_CHANGE`- Dynamic QR Code change<br>`DYNAMIC_WITHDRAW` - Dynamic QR withdrawal<br> | enum: ["STATIC", "STATIC_WITHDRAW", "DYNAMIC_COB", "DYNAMIC_COBV", "DYNAMIC_CHANGE", "DYNAMIC_WITHDRAW"]; example: "DYNAMIC_COB" |
| `remittance_information` | string (schema `RemittanceInformation`) | no | Remittance information. Information from payee when transaction is a static QR Code.<br> | maxLength: 140 |
| `revision` | integer | no | QR Code revision. If the QR Code is changed, the revision changes. | example: 1 |
| `status` | string (schema `QRstatus`) | no | QR Code status: <br>`ATIVA` - Active <br>`CONCLUDIA` - Concluded <br>`REMOVIDA_PELO_USUARIO_RECEBEDOR` - Removed by the receiving user<br>`REMOVIDA_PELO_PSP` - Removed by PSP<br> | enum: ["ATIVA", "CONCLUIDA", "REMOVIDA_PELO_USUARIO_RECEBEDOR", "REMOVIDA_PELO_PSP"]; example: "ATIVA" |
| `transaction_identification` | string | no | Creditor party generated transaction ID. | example: "55d3992a-2f89-46fb-820a-958693bde84d" |
| `transaction_type` | string (schema `TransactionType`) | yes | Type of transaction the QR Code validation generates.<br>* `TRANSFER` - Standard immediate transfer payment. <br>* `CHANGE` - Occurs when the QR Code validation returns `CHANGE`. For example, the customer buys something and pays more than the product value to receive the difference in cash. <br>* `WITHDRAWAL` - Occurs when the QR Code validation returns `WITHDRAWAL` with `withdrawal` object values.<br>* `REFUND_AUTOMATIC_PIX` - Total or partial to the PSP payer user within the Automatic Pix MED (Pix return mechanism) scope (only when initiated by a `MANUAL`).<br>* `REFUND` = Total or partial refund to the paying user within the scope of MED 2.0, when this refund occurs from the PI Account of the user's PSP who participated in the distribution chain of the resources of the original transaction (only when initiated by a `MANUAL`)<br> | enum: ["TRANSFER", "CHANGE", "WITHDRAWAL", "REFUND_AUTOMATIC_PIX", "REFUND"]; example: "TRANSFER" |
| `withdrawal` | object (schema `pix.QRCodeWithdrawResponse`) | no |  |  |
| `recurrence` | object (schema `pix.recurrence`) | no |  |  |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EPIX0003` (Account not found):

```json
{
  "code": "EPIX0003",
  "message": "Account not found"
}
```

400 Example `EPIX0015` (x-account-id is not a valid number):

```json
{
  "code": "EPIX0015",
  "message": "x-account-id is not a valid number"
}
```

400 Example `EPIX0019` (Accounts - API returned 4xx error):

```json
{
  "code": "EPIX0019",
  "message": "Accounts - API returned 4xx error"
}
```

400 Example `EPIX0020` (SPI Gateway - API returned 4xx error):

```json
{
  "code": "EPIX0020",
  "message": "SPI Gateway - API returned 4xx error",
  "details": {
    "external": [
      {
        "code": "PCE001",
        "message": "The value \"000000012345\" is invalid for PI-PayerId. The value must match \"((^[0-9]11$)|(^[0-9]14$))\""
      }
    ]
  }
}
```

400 Example `EPIX0032` (Error unmarshalling request body):

```json
{
  "code": "EPIX0032",
  "message": "Error unmarshalling request body"
}
```

400 Example `EPIX0061` (PixDict - API returned 4xx error):

```json
{
  "code": "EPIX0061",
  "message": "PixDict - API returned 4xx error"
}
```

400 Example `EPIX0070` (QRCPS API do returned a merchant information without key and url):

```json
{
  "code": "EPIX0070",
  "message": "QRCPS API do returned a merchant information without key and url"
}
```

400 Example `EPIX0074` (QRCPS API returned 4xx error):

```json
{
  "code": "EPIX0074",
  "message": "QRCPS API returned 4xx error"
}
```

400 Example `EPIX0076` (QRCPS API do not returned a merchant information):

```json
{
  "code": "EPIX0076",
  "message": "QRCPS API do not returned a merchant information"
}
```

400 Example `EPIX0127` (Invalid field size for merchant category code):

```json
{
  "code": "EPIX0127",
  "message": "Invalid field size for merchant category code"
}
```

400 Example `EPIX0128` (Invalid value for transaction currency. Local currency must be used):

```json
{
  "code": "EPIX0128",
  "message": "Invalid value for transaction currency. Local currency must be used"
}
```

400 Example `EPIX0129` (Invalid value for transaction amount. Transaction amount must be greater than zero):

```json
{
  "code": "EPIX0129",
  "message": "Invalid value for transaction amount. Transaction amount must be greater than zero"
}
```

400 Example `EPIX0131` (Invalid QR Code, the payload format indicator is invalid):

```json
{
  "code": "EPIX0131",
  "message": "Invalid QR Code, the payload format indicator is invalid"
}
```

400 Example `EPIX0134` (Invalid QR Code, a merchant information cannot contain key and url filled in):

```json
{
  "code": "EPIX0134",
  "message": "Invalid QR Code, a merchant information cannot contain key and url filled in"
}
```

400 Example `EPIX0143` (Invalid QR Code, the country code must be BR):

```json
{
  "code": "EPIX0143",
  "message": "Invalid country code on QR Code. Must be `BR`"
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
404 Example `EPIX0041` (SPI Gateway - Not found error. Check details):

```json
{
  "code": "EPIX0041",
  "message": "SPI Gateway - Not found error. Check details"
}
```

404 Example `EPIX0059` (PixDict - Not found):

```json
{
  "code": "EPIX0059",
  "message": "PixDict - Not found"
}
```

##### Response 409

- Response header `x-cid`: Request tracking ID. (string)
409 Example `EPIX0008` (Account blocked or cancelled):

```json
{
  "code": "EPIX0008",
  "message": "Account blocked or cancelled"
}
```

##### Response 429

- Response header `x-cid`: Request tracking ID. (string)
429 Example `EPIX0031` (SPI Gateway - API returned a rate limit error):

```json
{
  "code": "EPIX0031",
  "message": "SPI Gateway - API returned a rate limit error"
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

500 Example `EPIX0005` (Error unmarshalling object):

```json
{
  "code": "EPIX0005",
  "message": "Error unmarshalling object"
}
```

500 Example `EPIX0007` (HTTP error):

```json
{
  "code": "EPIX0007",
  "message": "HTTP error"
}
```

500 Example `EPIX0017` (Accounts - API returned 5xx error):

```json
{
  "code": "EPIX0017",
  "message": "Accounts - API returned 5xx error"
}
```

500 Example `EPIX0042` (Accounts API timeout error):

```json
{
  "code": "EPIX0042",
  "message": "Accounts API timeout error"
}
```

##### Response 502

- Response header `x-cid`: Request tracking ID. (string)
502 Example `EPIX0018` (SPI Gateway - API returned error):

```json
{
  "code": "EPIX0018",
  "message": "SPI Gateway - API returned error"
}
```

502 Example `EPIX0060` (PixDict - API returned 5xx error):

```json
{
  "code": "EPIX0060",
  "message": "PixDict - API returned 5xx error"
}
```

502 Example `EPIX0075` (QRCPS API returned 5xx error):

```json
{
  "code": "EPIX0075",
  "message": "QRCPS API returned 5xx error"
}
```

##### Response 504

- Response header `x-cid`: Request tracking ID. (string)
504 Example `EPIX0073` (QRCPS API timeout error):

```json
{
  "code": "EPIX0073",
  "message": "QRCPS API timeout error"
}
```

504 Example `EPIX0030` (SPI Gateway - API returned a timeout error):

```json
{
  "code": "EPIX0030",
  "message": "SPI Gateway - API returned a timeout error"
}
```

504 Example `EPIX0058` (PixDict - API timeout):

```json
{
  "code": "EPIX0058",
  "message": "PixDict - API timeout"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EPIX0003` | Account not found |
| 400 | `EPIX0015` | x-account-id is not a valid number |
| 400 | `EPIX0019` | Accounts - API returned 4xx error |
| 400 | `EPIX0020` | SPI Gateway - API returned 4xx error |
| 400 | `PCE001` | The value "000000012345" is invalid for PI-PayerId. The value must match "((^[0-9]11$)\|(^[0-9]14$))" |
| 400 | `EPIX0032` | Error unmarshalling request body |
| 400 | `EPIX0061` | PixDict - API returned 4xx error |
| 400 | `EPIX0070` | QRCPS API do returned a merchant information without key and url |
| 400 | `EPIX0074` | QRCPS API returned 4xx error |
| 400 | `EPIX0076` | QRCPS API do not returned a merchant information |
| 400 | `EPIX0127` | Invalid field size for merchant category code |
| 400 | `EPIX0128` | Invalid value for transaction currency. Local currency must be used |
| 400 | `EPIX0129` | Invalid value for transaction amount. Transaction amount must be greater than zero |
| 400 | `EPIX0131` | Invalid QR Code, the payload format indicator is invalid |
| 400 | `EPIX0134` | Invalid QR Code, a merchant information cannot contain key and url filled in |
| 400 | `EPIX0143` | Invalid country code on QR Code. Must be `BR` |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 404 | `EPIX0041` | SPI Gateway - Not found error. Check details |
| 404 | `EPIX0059` | PixDict - Not found |
| 409 | `EPIX0008` | Account blocked or cancelled |
| 429 | `EPIX0031` | SPI Gateway - API returned a rate limit error |
| 500 | `EPIX0004` | Internal server error |
| 500 | `EPIX0005` | Error unmarshalling object |
| 500 | `EPIX0007` | HTTP error |
| 500 | `EPIX0017` | Accounts - API returned 5xx error |
| 500 | `EPIX0042` | Accounts API timeout error |
| 502 | `EPIX0018` | SPI Gateway - API returned error |
| 502 | `EPIX0060` | PixDict - API returned 5xx error |
| 502 | `EPIX0075` | QRCPS API returned 5xx error |
| 504 | `EPIX0073` | QRCPS API timeout error |
| 504 | `EPIX0030` | SPI Gateway - API returned a timeout error |
| 504 | `EPIX0058` | PixDict - API timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;429;500;502;504`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-PAY-pix-and-qr-codes`, `KU-PAY-pix-automatic`.

<!-- op: spec=api-specs/Instant_payments_-_Pix_payments.yaml method=GET path=/pix/v1/pix/receipts operationId=get-receipts -->
### `GET /pix/v1/pix/receipts` — List account receipts

- **operationId:** `get-receipts`
- **Specification:** `api-specs/Instant_payments_-_Pix_payments.yaml` (Instant payments - Pix payments)
- **Server base URL(s):** `https://sandbox-cdn.pismolabs.io`, `https://sandbox-cdn.pismolabs.io/inst-pull-pay`
- **Tags:** `Pix`
- **Deprecated in specification:** no
- **Security requirement:** not declared

**Description (from the specification):**

> Retrieve account's receipts with filter options. The account is parsed from the account authorization token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `perPage` | query | yes | string | Per page amount (min=1, max=100). Default is `20`. |  |
| `beginDate` | query | yes | string | Begin date filter. RFC 3339 format. For example: `2023-04-12T23:20:50.52Z`. <br><br>Maximum days allowed between `beginDate` and `endDate` is 30.<br> | example: "2023-04-12T23:20:50.52Z" |
| `endDate` | query | yes | string | End date filter. RFC 3339 format. For example: `2023-04-12T23:20:50.52Z`. <br><br>Maximum days allowed between `beginDate` and `endDate` is 30.<br> | example: "2023-04-12T23:20:50.52Z" |
| `type` | query | no | string | Pix transaction type filter | enum: ["PIX-IN", "PIX-OUT", "PIX-IN-REVERSAL", "PIX-OUT-REVERSAL"]; example: "PIX-IN" |
| `endToEndId` | query | yes | string | Transaction end-to-end ID filter. This field is a Brazil Central Bank (BCB) requirement to track all Pix transaction steps.<br> |  |
| `reversalEndToEndId` | query | no | string | Reversal end-to-end ID filter. |  |
| `order` | query | no | string | Order to return items: `ASC` = ascending order, `DESC` = descending. Default is `DESC`.<br> | enum: ["ASC", "DESC"] |
| `afterId` | query | no | string | Last returned item ID from response. Use this field to return more results. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Response Body | `application/json`: object (schema `pix.ReceiptFindResponse`) |
| 400 | Bad Request | `application/json`: object (schema `customer.Error`) |
| 403 | Forbidden | `application/json`: object (schema `customer.Error`) |
| 404 | Not Found | `application/json`: object (schema `customer.Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `customer.Error`) |

##### Response 200

- Response header `x-cid`: Request tracking ID. (string)
**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `items` | array of object (schema `pix.ReceiptFindResponseItem`) | no | Receipt list |  |
| `last_id` | integer (schema `LastID`) | no | Last returned item ID. Use this ID to get more results.<br> | example: 1602619 |
| `next_page` | boolean (schema `NextPage`) | no | Are tbere more results? | example: false |
| `per_page` | integer (schema `PerPage`) | no | Max number of items per page. | example: 10 |

##### Response 400

- Response header `x-cid`: Request tracking ID. (string)
400 Example `EPIX0061` (Invalid value for query param):

```json
{
  "code": "EPIX0061",
  "message": "Invalid value for query param"
}
```

400 Example `EPIX0062` (Invalid value for query param. Date must be RFC3339 format, i.e., "2023-04-12T23:20:50.52Z"):

```json
{
  "code": "EPIX0062",
  "message": "Invalid value for query param. Date must be RFC3339 format"
}
```

400 Example `EPIX0063` (Invalid value for query param. Date must be RFC3339 format):

```json
{
  "code": "EPIX0063",
  "message": "Invalid value for query param. Date must be RFC3339 format"
}
```

400 Example `EPIX0065` (? must be greater than ?):

```json
{
  "code": "EPIX0065",
  "message": "? must be greater than ?"
}
```

400 Example `EPIX0077` (query parameter is invalid. Should use the last value of "last_id" field):

```json
{
  "code": "EPIX0077",
  "message": "query parameter is invalid. Should use the last value of \"last_id\" field"
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
404 Example `EPIX0135` (Receipt not found):

```json
{
  "code": "EPIX0135",
  "message": "Receipt not found"
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
| 400 | `EPIX0061` | Invalid value for query param |
| 400 | `EPIX0062` | Invalid value for query param. Date must be RFC3339 format |
| 400 | `EPIX0063` | Invalid value for query param. Date must be RFC3339 format |
| 400 | `EPIX0065` | ? must be greater than ? |
| 400 | `EPIX0077` | query parameter is invalid. Should use the last value of "last_id" field |
| 403 | `EPIX0009` | Missing required header: "x-tenant" |
| 403 | `EPIX0010` | Invalid account id header: "x-account-id" |
| 404 | `EPIX0135` | Receipt not found |
| 500 | `EPIX0004` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/pix.OutTransferPSPaccount -->
### Schema `pix.OutTransferPSPaccount`

Pointer: `#/components/schemas/pix.OutTransferPSPaccount`. Type: object (schema `pix.OutTransferPSPaccount`).

> Payment service provider (PSP) information. This object is **REQUIRED** if `transaction_type` = `REFUND`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | yes | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `bank` | string (schema `Bank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `taxes` | object (schema `Taxes`) | no | Only available in the test environment for direct participants. Tax information related to the transaction.<br> |  |

<!-- schema: #/components/schemas/pix.SignatureInfo -->
### Schema `pix.SignatureInfo`

Pointer: `#/components/schemas/pix.SignatureInfo`. Type: object (schema `pix.SignatureInfo`).

> Signature information, including the digital signature over the request data that a PSTI validates. A Prestadores de Serviços de Tecnologia da Informação (PSTI) - Information and Technology Service Provider in English — is a technology service provider that connects to the banking/financial infrastructure (specifically the Rede do Sistema Financeiro Nacional - RSFN) on participants' behalf.
>
> The signature here is the digital signature standard using a private asymmetric key (<a href="https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/" target="_blank">RSA</a> or <a href="https://en.wikipedia.org/wiki/Elliptic-curve_cryptography" target="_blank">Elliptic Curve</a>) over an input buffer extracted from the request and provider-defined. 
>
> This field guarantees the request's integrity and authenticity and the transaction messaging non-repudiation (assurance that a party involved in a transaction cannot later deny their involvement) from customer to PSTI.
>
> For more information, refer to the  [Scheduled Pix-out transfer encryption](doc:pix-out-transfer-encryption) guide.
>
> **Note:** Customers should contact the PSTI to get more information about the encryption process and how to store the certificate related to the certificate thumbprint. Pismo acts as a pass-through entity in this process.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `algorithm` | string | yes | The <a href="https://en.wikipedia.org/wiki/Digital_Signature_Algorithm" target="_blank">digital signature algorithm</a> (DSA). <br> | enum: ["ECDSA_P256_SHA256", "ECDSA_P384_SHA384", "Ed25519", "RSA_PKCS1_SHA256", "RSA_PSS_SHA256"]; example: "RSA_PKCS1_SHA256" |
| `certificate_thumbprint` | string | yes | The certificate thumbprint calculated using a <a href="https://en.wikipedia.org/wiki/SHA-2" target="_blank">SHA-256 algorithm</a> and encoded in hexadecimal. | maxLength: 512; example: "3a2b4c1b..." |
| `signature` | string | yes | The digital signature calculated over the payload (see the input buffer data and provider-defined format) according to the DSA standard and Base64 encoded.<br> | maxLength: 1024; example: "MIIb2132b==" |

<!-- schema: #/components/schemas/customer.Error -->
### Schema `customer.Error`

Pointer: `#/components/schemas/customer.Error`. Type: object (schema `customer.Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error's code. | example: "EPT0001" |
| `details` | object (schema `customer.DetailMessage`) | no |  |  |
| `message` | string | no | Error's message. | example: "User not found" |

<!-- schema: #/components/schemas/commons.AdditionalInfo -->
### Schema `commons.AdditionalInfo`

Pointer: `#/components/schemas/commons.AdditionalInfo`. Type: object (schema `commons.AdditionalInfo`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | QR Code name information. | example: "Discount" |
| `value` | string | no | QR Code value information. | example: "Paying until the 5th, there will be a 10% discount" |

<!-- schema: #/components/schemas/commons.Charges -->
### Schema `commons.Charges`

Pointer: `#/components/schemas/commons.Charges`. Type: object (schema `commons.Charges`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `discount_value` | number (schema `DiscountValue`) | no | Discount value. | example: 0.15 |
| `interest_value` | number (schema `InterestValue`) | no | Interest value. | example: 20.15 |
| `fine_value` | number (schema `FineValue`) | no | Fine value. | example: 5.15 |
| `settled_value` | number (schema `SettledValue`) | no | Settlement value. Amount to transfer after all charges have been applied. | example: 10.15 |

<!-- schema: #/components/schemas/commons.Dates -->
### Schema `commons.Dates`

Pointer: `#/components/schemas/commons.Dates`. Type: object (schema `commons.Dates`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `creation_datetime` | string | no | UTC creation date time. | example: "2020-09-15T19:39:54.013Z" |
| `due_date` | string | no | Due date, format = YYYY-MM-DD | example: "2020-09-15" |
| `expiration_datetime` | string | no | UTC expiration date time. | example: "2020-09-15T19:39:54.013Z" |
| `presentation_datetime` | string | no | UTC presentation date time. | example: "2020-09-15T19:39:54.013Z" |
| `validity_after_expiration_day` | integer | no | How long, in days, the QR Code is active or functional after the expiration date. | example: 30 |

<!-- schema: #/components/schemas/commons.Debtor -->
### Schema `commons.Debtor`

Pointer: `#/components/schemas/commons.Debtor`. Type: object (schema `commons.Debtor`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |

<!-- schema: #/components/schemas/commons.Payee -->
### Schema `commons.Payee`

Pointer: `#/components/schemas/commons.Payee`. Type: object (schema `commons.Payee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `PersonType`) | no | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `account_number` | string (schema `AccountNumber`) | no | Account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | no | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `address` | string | no | Payee street address. | example: "1542 3rd Ave" |
| `bank` | string (schema `Bank`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `branch` | string (schema `Branch`) | no | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `city` | string | no | Payee city. | example: "New York" |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `key` | string (schema `Key`) | no | Pix key value. | maxLength: 77; example: "email@email.com" |
| `name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |
| `participant_id` | integer | no | Pix participant ID (ISPB). | example: 60701190 |
| `state` | string | no | Payee state. | example: "NY" |
| `zip_code` | string (schema `PostalCode`) | no | Postal/zip code | example: "8675309" |

<!-- schema: #/components/schemas/pix.QRCodeWithdrawResponse -->
### Schema `pix.QRCodeWithdrawResponse`

Pointer: `#/components/schemas/pix.QRCodeWithdrawResponse`. Type: object (schema `pix.QRCodeWithdrawResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `agent_modality` | string (schema `AgentModality`) | no | Withdrawal service agent. **REQUIRED** for `CHANGE` and `WITHDRAWAL` transactions.<br /><br>  * `AGTEC` - Agente estabelecimento comercial. For commercial establishment.<br /><br>  * `AGFSS` - Agente Facilitador de Serviço de Saque. For cash machine.<br /><br>  * `AGTOT` - Agente Outra Espécie de Pessoa Jurídicas ou correspondente no País. Withdrawal service facilitator.<br /><br> | enum: ["AGTEC", "AGTOT", "AGPSS"]; example: "AGTEC" |
| `allows_value_change` | boolean (schema `AllowsValueChange`) | no | Can the payer change the final amount? | example: false |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `ispb_service_provider` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `purchase_amount` | number (schema `PurchaseAmount`) | no | Purchase price before charges, withdrawal changes, or other changes. | example: 1050.44 |

<!-- schema: #/components/schemas/pix.recurrence -->
### Schema `pix.recurrence`

Pointer: `#/components/schemas/pix.recurrence`. Type: object (schema `pix.recurrence`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `recurrence_id` | string | no | Recurrence ID | example: "c80118a7-7cef-4378-a3be-e0e28efbf150" |
| `journey_type` | string (schema `JourneyType`) | no | Recurrence payment type: <br> `AUT1` - Bank notification. If the merchant has the payer's banking information, a push notification can be sent directly to the payer's bank app, prompting them to authorize the recurring payment.<br> <br> `AUT2` - Authorization via QR Code. Payer scans a merchant provided QR Code to authorize recurring payments. This method does not initiate an immediate payment, allowing the first payment to be scheduled for a later date.<br> <br> `AUT3` - Authorization via QR Code with first payment.  Similar to the second method, but the QR Code includes information for both the authorization and the initial payment, enabling the payer to authorize the recurring payment and make the first payment in a single step.<br> <br> `AUT4` - Post-payment sign-up path. After completing a one-time payment via QR Code, the payer is offered the option to authorize recurring payments for future transactions<br><br> For more information, refer to [Pix automatic use cases (journeys)](doc:pix-automatic-beta-copy-2#pix-automatic-use-cases-journeys).<br> | enum: ["AUT1", "AUT2", "AUT3", "AUT4"]; example: "AUT1" |
| `contract_id` | string (schema `ContractID`) | no | Payee-created external ID for their reference.<br> | maxLength: 35; example: "5509-uroo-78944-9987" |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `min_payment_amount` | number (schema `MinPaymentAmount`) | no | Minimum payment amount for dynamic amount recurrences, defined by payee. | example: 10.09 |
| `frequency_type` | string (schema `FrequencyType`) | no | Recurrence payment type | enum: ["WEEK", "MONTH", "QUARTER", "SEMESTER", "YEAR"]; example: "MONTH" |
| `first_payment_date` | string (schema `FirstPaymentDate`) | no | First charge/payment date. Format = YYYY-MM-DD | format: "datetime"; example: "2025-04-25" |
| `last_payment_date` | string (schema `LastPaymentDate`) | no | Last charge/payment date. Format = YYYY-MM-DD | format: "datetime"; example: "2026-06-10" |
| `payee` | object (schema `Payee`) | no |  |  |
| `debtor` | object (schema `Debtor`) | no |  |  |
| `payer` | object (schema `Payer`) | no |  |  |
| `retry` | boolean (schema `Retry`) | no | Retry transaction on failure? | example: true |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime. RFC 3339 format <br> | format: "datetime"; example: "2025-11-14T17:54:40Z" |
| `read_at` | string (schema `ReadAt`) | no | Datetime QR Code was read, RFC 3339 format | example: "2024-11-14T17:54:40Z" |
| `history` | array of object (schema `HistoryItem`) | no | QRcode history |  |

<!-- schema: #/components/schemas/pix.ReceiptFindResponseItem -->
### Schema `pix.ReceiptFindResponseItem`

Pointer: `#/components/schemas/pix.ReceiptFindResponseItem`. Type: object (schema `pix.ReceiptFindResponseItem`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `purchase_amount` | number (schema `PurchaseAmount`) | no | Purchase price before charges, withdrawal changes, or other changes. | example: 1050.44 |
| `withdraw_amount` | number | no | Amount to be withdrawn. | example: 100 |
| `transaction_identification` | string | no | Creditor generated transaction ID. | example: "d4c38871c8354f0fbe91b3c9c7d5b929" |
| `type` | string (schema `PixOutType`) | no | Pix transaction type. | enum: ["PIX-IN", "PIX-OUT", "PIX-IN-REVERSAL", "PIX-OUT-REVERSAL"]; example: "PIX-IN" |
| `authorization_datetime` | string | no | Authorization datetime. RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | example: "2021-10-11T19:01:43.392Z" |
| `charges` | object (schema `pix.ReceiptAmountCharges`) | no |  |  |
| `debtor` | object (schema `pix.ReceiptDebtor`) | no |  |  |
| `description` | string | no | Description. | example: "Transaction Pix" |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `initial_amount` | string (schema `InitialAmount`) | no | The initial purchase price amount before charges or withdrawal changes. | example: "10.02" |
| `initiation_type` | string (schema `InitiationType`) | no | Initiation type:  <br><br>  `MANUAL` - Manually initiated. Key is not used - bank account, bank code, document number, and branch are used for identification.<br><br>  `DICT` - Diretorio de Identificadores de Contas de Transacapo (Transaction accounts ID directory). Pix/DICT key is used for identification.<br><br>  `STATIC_QRCODE` - Reusable code that contains only the data necessary to complete a transaction. When using static QR Code, the transaction amount must be provided manually.<br><br>  `DYNAMIC_QRCODE` - The amount and other details for a dynamic code are included automatically. <br>  <br>  `PAYMENT_INITIATOR` - Payment provider initiated. A payment initiator is a 3rd party that has obtained authorization from the Central Bank and has an <a href="https://www.bcb.gov.br/en/financialstability/open_finance" target="_blank">Open Finance</a> certification.<br><br>  `AUTOMATIC_PIX` - Payment order initiated via automatic PIX.<br>  <br>  `DYNAMIC_PROXIMITY_PIX` - Dynamic Near Field Communications (NFC) based initiation.<br><br>  `STATIC_PROXIMITY_PIX` - Static NFC-based initiation.<br> | enum: ["MANUAL", "DICT", "STATIC_QRCODE", "DYNAMIC_QRCODE", "PAYMENT_INITIATOR", "AUTOMATIC_PIX", "DYNAMIC_PROXIMITY_PIX", "STATIC_PROXIMITY_PIX"]; maxLength: 20; example: "DICT" |
| `transaction_type` | string (schema `TransactionType`) | no | Type of transaction the QR Code validation generates.<br>* `TRANSFER` - Standard immediate transfer payment. <br>* `CHANGE` - Occurs when the QR Code validation returns `CHANGE`. For example, the customer buys something and pays more than the product value to receive the difference in cash. <br>* `WITHDRAWAL` - Occurs when the QR Code validation returns `WITHDRAWAL` with `withdrawal` object values.<br>* `REFUND_AUTOMATIC_PIX` - Total or partial to the PSP payer user within the Automatic Pix MED (Pix return mechanism) scope (only when initiated by a `MANUAL`).<br>* `REFUND` = Total or partial refund to the paying user within the scope of MED 2.0, when this refund occurs from the PI Account of the user's PSP who participated in the distribution chain of the resources of the original transaction (only when initiated by a `MANUAL`)<br> | enum: ["TRANSFER", "CHANGE", "WITHDRAWAL", "REFUND_AUTOMATIC_PIX", "REFUND"]; example: "TRANSFER" |
| `initiator_document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `internal` | boolean (schema `Internal`) | no | Was transaction made between a Pismo organization's accounts? In this case, the instant payment system is not called. | example: false |
| `payee` | object (schema `pix.ReceiptPayee`) | no |  |  |
| `payer` | object (schema `pix.ReceiptPayer`) | no |  |  |
| `qrcode_additional_information` | array of object (schema `pix.ReceiptQRCodeAdditionalInformation`) | no | QRCode Additional information. Information generated by payee's participant when transaction is a Dynamic QR Code process. |  |
| `reversal` | object (schema `pix.ReceiptReversal`) | no |  |  |
| `tx_id` | string | no | Tax ID generated in the static QR Code, intended for the final user's financial reconciliation. | example: "d4c38871c8354f0fbe91b3c9c7d5b929" |
| `taxes` | object (schema `Taxes`) | no | Only available in the test environment for direct participants. Tax information related to the transaction.<br> |  |

<!-- schema: #/components/schemas/Taxes -->
### Schema `Taxes`

Pointer: `#/components/schemas/Taxes`. Type: object (schema `Taxes`).

> Only available in the test environment for direct participants. Tax information related to the transaction.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_identifier` | string (schema `TaxIdentifier`) | no | Tax identifier, referring to the NFe, NFSe or aggregating tax document. <br><br>In Brazil, NF-e and NFS-e are the two primary types of mandatory electronic invoices (Notas Fiscais) used for tax compliance.<br><br> * NF-e (Nota Fiscal Eletrônica): Used for the sale and movement of physical goods or products. It is regulated at the state level by SEFAZ (SEFAZ (Secretaria da Fazenda) is the State Department of Finance in Brazil.) and travels with the goods.<br><br> * NFS-e (Nota Fiscal de Serviços Eletrônica): Used for the provision of services (e.g., consulting, repairs, digital subscriptions). It is regulated by individual city governments.<br><br>The value entered must correspond to the tax document used for calculating the IBS and CBS taxes associated with the transaction.<br> | maxLength: 50; example: "IS0435879820240605bcdb1fhn43a" |
| `records` | array of object (schema `Records`) | no | Tax record types information. You must pass, at a minimum, 2 objects - at least one with `CBS` tax type and at least one with `IBS` tax type.<br> |  |

<!-- schema: #/components/schemas/customer.DetailMessage -->
### Schema `customer.DetailMessage`

Pointer: `#/components/schemas/customer.DetailMessage`. Type: object (schema `customer.DetailMessage`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external` | array of object (schema `customer.ExternalMessage`) | no |  |  |
| `parameters` | array of object (schema `customer.ParameterMessage`) | no |  |  |
| `payload` | array of object (schema `customer.PayloadMessage`) | no |  |  |

<!-- schema: #/components/schemas/Payee -->
### Schema `Payee`

Pointer: `#/components/schemas/Payee`. Type: object (schema `Payee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `document_type` | string (schema `PersonType`) | yes | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `bank` | string (schema `Bank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `account_number` | string (schema `AccountNumber2`) | yes | Payer's account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | yes | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |

<!-- schema: #/components/schemas/Debtor -->
### Schema `Debtor`

Pointer: `#/components/schemas/Debtor`. Type: object (schema `Debtor`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `document_type` | string (schema `PersonType`) | yes | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |

<!-- schema: #/components/schemas/Payer -->
### Schema `Payer`

Pointer: `#/components/schemas/Payer`. Type: object (schema `Payer`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | yes | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `document_type` | string (schema `PersonType`) | yes | Person type:  <br>* `LEGAL_PERSON` - An actual person with legal rights.<br>* `NATURAL_PERSON` - An entity, such as an organization or company.<br> | enum: ["LEGAL_PERSON", "NATURAL_PERSON"]; example: "NATURAL_PERSON" |
| `name` | string (schema `Name`) | yes | Name | maxLength: 200; example: "Walter Melon" |
| `bank` | string (schema `Bank`) | yes | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID for the receiving bank, an 8-digit value. | maxLength: 8; example: "237" |
| `branch` | string (schema `Branch`) | yes | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `account_number` | string (schema `AccountNumber2`) | yes | Payer's account number. | maxLength: 20; example: "98765432" |
| `account_type` | string (schema `AccountType`) | no | Account type:  <br /><br>  `CACC` - Checking/current account.  Known as "conta corrente" in Portuguese, this is a bank account type designed for everyday financial transactions and is the most common type individuals and businesses use for day-to-day banking.<br /><br>  `SVGS` - Savings account<br /><br>  `TRAN` - Payment account. Payment institutions offer payment accounts to move funds and make payments, while banks offer checking accounts that include full financial services such as credit and investments.<br /><br>  `SLRY` - Salary account. Employer deposits a fixed amount every month.<br /><br> | enum: ["CACC", "SLRY", "SVGS", "TRAN"]; maxLength: 4; example: "TRAN" |
| `city_code` | string (schema `CityCode`) | no | The <a href='https://www.ibge.gov.br/explica/codigos-dos-municipios.php' target="_blank">IBGE</a> (Instituto Brasileiro de Geografia e Estatística) city code. | example: "3550308" |

<!-- schema: #/components/schemas/HistoryItem -->
### Schema `HistoryItem`

Pointer: `#/components/schemas/HistoryItem`. Type: object (schema `HistoryItem`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `RecurrenceStatus`) | no | <br>Recurrence status<br><br>  * `CREATED`	  - Recurrence created, waiting on journey acceptance.<br>  * `ACCEPTED`  - Payer accepted recurrence, awaiting confirmation from receiver's PSP.<br>  * `APPROVED`  - Payer accepted recurrence and receiver's PSP confirmed. <br>  * `REJECTED`  - Payer or receiver's PSP rejected recurrence during `ACCEPTED` validation. For example: receiver's account is inactive.<br>  * `EXPIRED`   - Recurrence expired after last scheduled payment date.<br>  * `CANCELLED` - Payer or reciever cancelled recurrence.<br>  * `FINISHED`  - Deprecated<br> | enum: ["CREATED", "ACCEPTED", "APPROVED", "REJECTED", "EXPIRED", "CANCELLED", "FINISHED"]; example: "REJECTED" |
| `updated_at` | string (schema `UpdatedAt`) | no | Scheduled item last updated time, RFC 3339 format | example: "2024-11-14T17:54:40Z" |

<!-- schema: #/components/schemas/pix.ReceiptAmountCharges -->
### Schema `pix.ReceiptAmountCharges`

Pointer: `#/components/schemas/pix.ReceiptAmountCharges`. Type: object (schema `pix.ReceiptAmountCharges`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `discount_value` | number (schema `DiscountValue`) | no | Discount value. | example: 0.15 |
| `interest_value` | number (schema `InterestValue`) | no | Interest value. | example: 20.15 |
| `fine_value` | number (schema `FineValue`) | no | Fine value. | example: 5.15 |
| `settled_value` | number (schema `SettledValue`) | no | Settlement value. Amount to transfer after all charges have been applied. | example: 10.15 |

<!-- schema: #/components/schemas/pix.ReceiptDebtor -->
### Schema `pix.ReceiptDebtor`

Pointer: `#/components/schemas/pix.ReceiptDebtor`. Type: object (schema `pix.ReceiptDebtor`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |

<!-- schema: #/components/schemas/pix.ReceiptPayee -->
### Schema `pix.ReceiptPayee`

Pointer: `#/components/schemas/pix.ReceiptPayee`. Type: object (schema `pix.ReceiptPayee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | no | Account number. | maxLength: 20; example: "98765432" |
| `branch` | string (schema `Branch`) | no | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `ispb` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |

<!-- schema: #/components/schemas/pix.ReceiptPayer -->
### Schema `pix.ReceiptPayer`

Pointer: `#/components/schemas/pix.ReceiptPayer`. Type: object (schema `pix.ReceiptPayer`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_number` | string (schema `AccountNumber`) | no | Account number. | maxLength: 20; example: "98765432" |
| `branch` | string (schema `Branch`) | no | This could be a bank-assigned branch ID or the branch's ISPB number. | maxLength: 4; example: "011" |
| `document_number` | string (schema `DocumentNumber`) | no | A government document number, such as a Social Security number (US) or Cadastro de Pessoas Físicas number (Brazil). Must be numeric with 11-14 digits.<br> | minLength: 1; maxLength: 14; example: "123412341234" |
| `ispb` | string (schema `ISPB`) | no | <a href="https://bank.codes/numero-do-banco/bank/banco-central-do-brasil/" target="_blank">ISPB (Identifcador do Sistema de Pagamento Brazil)</a> - the Brazilian Payment System ID, an 8-digit value. | maxLength: 8; example: "60701190" |
| `name` | string (schema `Name`) | no | Name | maxLength: 200; example: "Walter Melon" |

<!-- schema: #/components/schemas/pix.ReceiptQRCodeAdditionalInformation -->
### Schema `pix.ReceiptQRCodeAdditionalInformation`

Pointer: `#/components/schemas/pix.ReceiptQRCodeAdditionalInformation`. Type: object (schema `pix.ReceiptQRCodeAdditionalInformation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | QR Code name information. | example: "Discount" |
| `value` | string | no | QR Code value information. | example: "Paying until the 5th, there will be a 10% discount" |

<!-- schema: #/components/schemas/pix.ReceiptReversal -->
### Schema `pix.ReceiptReversal`

Pointer: `#/components/schemas/pix.ReceiptReversal`. Type: object (schema `pix.ReceiptReversal`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | no | Amount to be transferred. | example: 1050.44 |
| `authorization_datetime` | string | no | Reversal authorization datetime. RFC 3339 value, i.e., "2023-04-12T23:20:50.52Z". | example: "2021-10-11T19:01:43.392Z" |
| `end_to_end_id` | string (schema `EndToEndID`) | no | This field is a Brazil Central Bank (BCB) requirement to track all steps of Pix transactions. <br>Basically, there are two steps to a Pix transaction:<br>    1. Initialize a transaction <br>    2. Confirm a transaction<br>The `end_to_end_id` is sent to the BCB in both steps in order to identify all transaction information. <br> | example: "E3030629420200808195101608910248" |
| `reason` | string (schema `ReversalReason`) | no | Reversal reason. | enum: ["USER_REQUESTED", "FRAUD", "BANK_ERROR"]; example: "USER_REQUESTED" |

<!-- schema: #/components/schemas/Records -->
### Schema `Records`

Pointer: `#/components/schemas/Records`. Type: object (schema `Records`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tax_type` | string (schema `TaxType`) | no | Tax type:<br><br> `IBS` = Goods and services tax. A state and municipal tax that unifies and replaces the main subnational consumption taxes (state ICMS and municipal ISS).<br><br>`CBS` = Contribution on goods and services. A federal tax that consolidates and replaces previous federal social contributions and taxes (PIS, Cofins, and IPI).<br> | enum: ["CBS", "IBS"]; example: "IBS" |
| `amount` | number (schema `TaxAmount`) | no | Tax amount. Must be greater than zero. | example: 1050.44 |

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
| `api-specs/Instant_payments_-_Pix_payments.yaml` | tag `Pix`: POST /pix/v1/pix/out/transfer, POST /pix/v1/pix/in/reversal, POST /pix/v1/pix/qrcode/validate, GET /pix/v1/pix/receipts | https://github.com/PismoDevEx/pismo-api-specs | `034f2ce79f002354…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-banking-as-a-service` — Banking as a Service
- `KU-BANK-banking-overview` — Banking overview
- `KU-ERR-codes-epix` — Error codes: EPIX
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-pix` — Event catalogue: pix
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-EVT-pix-payments-data-events` — Instant payments - Pix
- `KU-GS-get-started-with-pismo-apis` — Get started with Pismo APIs
- `KU-PAY-pix-and-qr-codes` — Pix and QR Codes
- `KU-PAY-pix-automatic` — Pix Automatic
- `KU-PAY-pix-instant-payments` — Pix instant payments (Brazil)
