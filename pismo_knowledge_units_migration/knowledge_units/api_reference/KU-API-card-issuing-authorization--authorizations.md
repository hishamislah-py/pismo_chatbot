---
ku_id: KU-API-card-issuing-authorization--authorizations
title: 'API reference: Card issuing - Authorization — Authorizations'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Authorization.yaml
  sha256: f64e4226c94e8ce58acbcc3ae5835d737d64957bb63ba0368335f3f8c54a126f
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
- post_v1-authorizations
- get-network-authorizations
- cancel-network-authorizations
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-simulate-authorizations
- KU-CORE-fee-models-create-and-simulate
- KU-CORE-flex-controls
- KU-EVT-catalogue-other-domains
specification_version: 1.0.0
---

# API reference: Card issuing - Authorization — Authorizations

**KU ID:** `KU-API-card-issuing-authorization--authorizations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Authorizations` in `api-specs/Card_issuing_-_Authorization.yaml` (“Card issuing - Authorization”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /networktransactions/v1/authorizations` | `post_v1-authorizations` | Simulate authorization | no |
| `GET /direct-network-transactions/v1/authorizations/desc` | `get-network-authorizations` | List account authorizations | no |
| `POST /direct-network-transactions/v1/cancellation` | `cancel-network-authorizations` | Cancel authorization | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Authorization.yaml method=POST path=/networktransactions/v1/authorizations operationId=post_v1-authorizations -->
### `POST /networktransactions/v1/authorizations` — Simulate authorization

- **operationId:** `post_v1-authorizations`
- **Specification:** `api-specs/Card_issuing_-_Authorization.yaml` (Card issuing - Authorization)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://api-networktransactions-http-ext.pismolabs.io`
- **Tags:** `Authorizations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> You can use this endpoint to simulate a real-world authorization from the network in the sandbox environment. This simulation does not go through all the card network services as it would in production, but it does check for card status and balance. The call gives you a chance to see how Pismo might respond to a network authorization. The fields returned can be used to cancel or confirm the request with this endpoint.
>
> You can also use this endpoint to cancel (total or partial) the simulated authorization in the EXT/HOMOLOG environment. To cancel in the production environments, use the [Cancel authorization](ref:cancel-network-authorizations) endpoint.
>
> This endpoint generates the simulated [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event which you can receive and view. This event occurs in production when the Pismo platform cancels or confirms an authorization.  You can also use this endpoint to test connectivity to your [anti-fraud webhook url](doc:anti-fraud-integration).
>
> For more information, see the [Simulate authorizations](doc:simulate-authorizations) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | no | string | Organization/tenant ID | example: "TN-beaecb37-d149-4674-a485-af0d11e40d85" |

#### Request body

Required: no

**Content type `application/json`** — schema: anyOf: object (schema `CreateAuthorization`), object (schema `CreateCrediarioAuthorization`), object (schema `CreateWithdrawAuthorization`), object (schema `CreateRefundAuthorization`), object (schema `CreateCancelAuthorization`), object (schema `InstallmentAuthorization`), object (schema `ReplacementAuthorization`)

_anyOf option 1: schema `CreateAuthorization`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `card_id` | number | yes | Transaction card ID | example: 1234567 |
| `entry_mode` | string | yes | Method used for PAN entry to initiate a transaction and the PIN entry capabilities. This field is required and must have 3 or 4 digits. For example, `901` or `9010` for magnetic stripe transaction simulation.<br> | example: "901" |
| `local_amount` | number | yes | Local transaction amount in the currency of the place where the authorization is requested. | example: 100.5 |
| `local_currency` | string | yes | Local ISO 4217 currency code number where transaction occurred. For example, 986 (Brazil) or 840 (US). | maxLength: 3; example: "986" |
| `merchant` | object | yes | Merchant details | example: {"name": "merchantName", "city": "São Paulo", "country": "BR", "code": "5542", "id": "merchantId"} |
| `merchant.name` | string | yes | Merchant name |  |
| `merchant.city` | string | no | Merchant city name |  |
| `merchant.country` | string | no | Merchant country code in ISO 3166 format. For example, `BR` or `BRA` (Brazil). |  |
| `merchant.code` | string | no | Merchant code |  |
| `merchant.id` | string | no | Merchant ID |  |
| `mti` | string (schema `MTI`) | yes | Message type ID. For example: `0100` = auth. request, `0110`` = auth. response, `0120` = auth. advice. For more information, see [MTI](https://en.wikipedia.org/wiki/ISO_8583#Message_type_indicator_(MTI)).<br> | nullable: false; example: "0100" |
| `account_type` | string | no | Authorization mode being simulated. Use `20` for debit simulation and `30` for credit simulation. | example: "20" |
| `acquirer_reference_number` | string | no | Acquirer generated number | example: "1234569876541" |
| `advice_detail_code` | string | no | Advice detail code | example: "0004" |
| `advice_reason_code` | string (schema `AdviceReasonCode`) | no | If this is an *advice*, this is the reason code. For more information about the Advice reason code (DE 60 subfield 01) and Advice detail code (DE 60 subfield 02) refer to the network manual. For example, the specification for Mastercard can be found in the section "Customer Interface Specification (2020-MasterCard-CustomerInterfaceSpecification.pdf)".  <br> |  |
| `airport_tax` | number | no | Boarding fee—in a purchase with installments, this value is present at first installment. In a purchase without installments, this value should not be sent since it is included in the authorization amount.<br> | example: 3.5 |
| `atc` | string | no | Application transaction counter (ATC). The chip card application maintains and increments this counter. The ATC provides a sequential reference for each transaction. For more information, refer to [Application Transaction Counter (ATC)](doc:application-transaction-counter-atc).<br> | example: "0100" |
| `arqc_present` | boolean | no | Is chip present? | default: false; example: true |
| `authorization_code` | string | no | Authorization code | example: "ABCDEF" |
| `bin` | string | no | A bank identification number (BIN) represents the first four to eight digits on a credit card and identifies the financial institution that issued the card. | example: "587498" |
| `cardholder_billing_amount` | number | no | Transaction amount in cardholder currency | example: 11.5 |
| `cardholder_billing_currency` | string | no | Cardholder ISO 4217 currency code | example: "840" |
| `cash_back_amount` | number | no | Cash back amount used to simulate purchase with cash back | example: 2 |
| `cvv_present` | boolean | no | Is CVV present? | default: false; example: true |
| `clearing_s3_path` | string (schema `ClearingS3path`) | no | The clearing settlement file path in the AWS S3 (storage service). This field must be used when the `mti` field equals `clearing` (representing the simulation of a clearing settlement file processing).<br>The composition of this field is:<br><tenant>/from<KNetwork_name>/<specific_clearing_file_name>/<year>/<julian_date>/<file_name><br>Where:<br>- `<tenant>` is the tenant ID, for example, `TN-c9cccb07-41f7-493c-b796-60cc880bff4f`<br>- `<Network_name>` is the name of the card network, for example, Visa, Mastercard, TecBan, etc.<br>- `<specific_clearing_file_name>` is the name of the clearing file, for example, ServiceB, Base II, T112, T464, and so on.<br>- `<year>` is the year of the clearing file, for example, 2023.<br>- `<julian_date>` is the Julian date of the clearing file, for example, 105, where 10 is the day and 5 is the month.<br>- `<file_name>` is the name of the clearing file, for example, 17275501C489639.txt.<br> | example: "TN-c9cccb07-41f7-493c-b796-60cc880bff4f/fromVisa/C489639/baseii/2023/105/17275501C489639.txt" |
| `invoice_address` | string | no | Invoice address | example: "Avenue Five, 222" |
| `message_number` | string | no | Message number assigned to a clearing message. This **must** be a numeric and sequential number. | example: "123" |
| `nsu` | string (schema `NSU`) | no | Authorization Network Settlement Utility (NSU) number - tracks the flow of funds between parties involved in a payment card transaction, including the bank, the merchant, and the card network. Different payment card networks may have their own NSU systems, ie, Visa - VisaNet, Mastercard - BankNet, or they may use a third party.<br> | example: "15469" |
| `password_present` | boolean | no | Is PIN entered? | default: false; example: true |
| `processing_julian_date` | string | no | Reconciliation processing date. Format = YYDDD. **REQUIRED** for clearing simulations. | example: "25147" |
| `processing_code` | string | no | Transaction's effect on the customer account and the type of accounts affected. For purchase, use "00"; for withdraw, use "01"; for refund, use "20"; for payment, use "28".<br><br>For information about processing codes, refer to [Processing codes](doc:processing-codes-and-transaction-types).<br> | enum: ["00", "01", "20", "28"]; example: "00" |
| `retrieval_reference_number` | string | no | Merchant POS system generated number | example: "5600001085571" |
| `settlement_amount` | number | no | Settlement amount—**must** be the transaction amount in dollar currency. | example: 10.5 |
| `settlement_currency` | string | no | Settlement ISO 4217 currency code | example: "840" |
| `simule_tokenized_transaction` | boolean | no | Does the simulation use a tokenized transaction? | enum: [false, true]; default: false; example: true |
| `track1_present` | boolean | no | Is magnetic stripe track 1 data present? | default: false; example: true |
| `track2_present` | boolean | no | Is magnetic stripe track 2 data present? | default: false; example: true |
| `transaction_identifier` | string | no | Transaction ID | example: "589256582795978" |
| `wallet_identifier` | string | no | Wallet ID | example: "618" |

_anyOf option 2: schema `CreateCrediarioAuthorization`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `installments` | object | no | If this is a Crediario Authorization, this field is required to deal with installments. | example: {"is_crediario": true, "number": 2, "with_interest": true} |
| `installments.is_crediario` | boolean | no | Is this a credit authorization? | default: true |
| `installments.number` | number | no | Number of installments |  |
| `installments.with_interest` | boolean | no | Does the installment have an interest rate? | default: true |

_anyOf option 3: schema `CreateWithdrawAuthorization`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | no | Processing code for international withdrawal | example: "01" |

_anyOf option 4: schema `CreateRefundAuthorization`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `processing_code` | string | no | Processing code for refund/credit authorization | example: "20" |

_anyOf option 5: schema `CreateCancelAuthorization`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `mti` | string (schema `MTI`) | yes | Message type ID. For example: `0100` = auth. request, `0110`` = auth. response, `0120` = auth. advice. For more information, see [MTI](https://en.wikipedia.org/wiki/ISO_8583#Message_type_indicator_(MTI)).<br> | nullable: false; example: "0100" |

_anyOf option 6: schema `InstallmentAuthorization`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `caller` | string | no | Name of the network that performed this authorization request | example: "MASTERCARD, VISA, or TECBAN" |
| `card_id` | number | yes | Identifier of the card used for the transaction. | example: 1234567 |
| `mti` | string | yes | Message type indicator that defines which flows are going to be performed, such as authorization, cancellation, or clearing | example: "0100" |
| `local_amount` | number | yes | Local transaction amount—the amount in the currency of the place where the authorization is requested | example: 100.5 |
| `local_currency` | string | yes | Local currency code number where transaction occurred | enum: ["986", "840"] |
| `entry_mode` | string | yes | Indicates the method used for PAN entry to initiate a transaction and the PIN entry capabilities | example: "901" |
| `processing_code` | string | no | Describes the effect of a transaction on the customer account and the type of accounts affected. For purchase, use `00`; for withdraw, use `01`; for refund, use `20`; for payment, use `28`.<br><br>For information about processing codes, refer to [Processing code](docs:processing-codes-and-transaction-types).          <br> | enum: ["00", "01", "20", "28"]; example: "00" |
| `installments` | object | no | If this is a credit authorization, this field is required to deal with installments. | example: {"number": 4, "with_interest": "true", "payment_number": 2, "amount_of_each_installment": 50} |
| `installments.number` | number | no | Number of installments |  |
| `installments.with_interest` | string | no | Indicates if the installment has an interest rate. |  |
| `installments.payment_number` | number | no | Current installment number |  |
| `installments.amount_of_each_installment` | number | no | Amount of each installment |  |
| `merchant` | object | yes | Details about the merchant | example: {"name": "merchantName", "city": "São Paulo", "country": "Brazil", "code": "BR", "id": "merchantId"} |
| `merchant.name` | string | yes | Merchant name |  |
| `merchant.city` | string | no | Merchant city name |  |
| `merchant.country` | string | no | Merchant country code |  |
| `merchant.code` | string | no | Merchant code |  |
| `merchant.id` | string | no | Merchant ID |  |
| `atc` | string | no | Application transaction counter | example: "0100" |
| `settlement_amount` | number | no | Settlement amount—this must be the amount of the transaction in Dollar currency. | example: 10.5 |
| `settlement_currency` | string | no | Settlement currency | example: "840" |
| `cardholder_billing_amount` | number | no | Amount of the transaction in the Cardholder currency | example: 11.5 |
| `cardholder_billing_currency` | string | no | Currency code of the cardholder | example: "840" |
| `account_type` | string | no | Defines the mode of the authorization being simulated. Use `20` for debit simulation and `30` for credit simulation. | example: "00" |
| `invoice_address` | string | no | Invoice address | example: "222 Fifth Avenue" |
| `authorization_code` | string | no | Authorization code | example: "ABCDEF" |
| `retrieval_reference_number` | string | no | Number generated by merchant POS systems | example: "5600001085571" |
| `nsu` | string | no | Unique sequence number to identify one transaction | example: "085581" |
| `processing_julian_date` | string | no | Date assigned to the reconciliation processing. This is required for clearing simulations and must have the format YDDD. | example: "1360" |
| `acquirer_reference_number` | string | no | Number generated by Acquirer. | example: "1234569876541" |
| `airport_tax` | number | no | Boarding fee. In a purchase with installment, this value will be present at first installment. In a purchase without installment, this value should not be sent since it should be summed to the authorization amount. | example: 3.5 |
| `message_number` | string | no | Message number assigned to a clearing message. It must be a sequential number. | example: "1234" |
| `transaction_identifier` | string | no | Transaction identifier | example: "589256582795978" |
| `simule_tokenized_transaction` | boolean | no | Indicates if the simulation will use a tokenized transaction | enum: [false, true]; example: true |
| `cash_back_amount` | number | no | Cash back amount used to simulate purchase with cash back | example: 2 |
| `advice_reason_code` | string | no | Advice reason code | example: "112" |
| `advice_detail_code` | string | no | Advice detail code | example: "0004" |
| `wallet_identifier` | string | no | Wallet identifier | example: "618" |
| `bin` | string | no | BIN represents the Bank Identification Number and corresponds to the first 6 or 8 digits of a card. In general terms, the BIN explains which bank institution issued that card. | example: "82327110" |

_anyOf option 7: schema `ReplacementAuthorization`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `caller` | string | no | Name of the network that performed this authorization request | example: "MASTERCARD or VISA" |
| `card_id` | number | yes | ID of the card used for the transaction | example: 1234567 |
| `mti` | string | yes | Message type indicator that defines with flow are going to be performed like authorization, cancellation or clearing | example: "0400" |
| `local_amount` | number | yes | Local transaction amount. It is the amount in the currency of the place where the authorization is requested. | example: 100.5 |
| `local_currency` | string | yes | Local currency code number where transaction occurred | enum: ["986", "840"] |
| `replacement_amount` | number | no | Replacement transaction amount. This is the value that will be used to replace the original authorization value. | example: 90.5 |
| `authorization_code` | string | no | Authorization code | example: "ABCDEF" |
| `entry_mode` | string | yes | Indicates the method used for PAN entry to initiate a transaction and the PIN entry capabilities. | example: "051" |
| `processing_code` | string | no | Describes the effect of a transaction on the customer account and the type of accounts affected. For purchase, use `00`; for withdraw, use `01`; for refund, use `20`; for payment, use `28`. | enum: ["00", "01", "20", "28"]; example: "00" |
| `merchant` | object | yes | Details about the merchant | example: {"name": "merchantName", "city": "São Paulo", "country": "Brazil", "code": "BR", "id": "merchantId"} |
| `merchant.name` | string | yes | Merchant name |  |
| `merchant.city` | string | no | Merchant city name |  |
| `merchant.country` | string | no | Merchant country code |  |
| `merchant.code` | string | no | Merchant code |  |
| `merchant.id` | string | no | Merchant ID |  |


Example `Create authorization`:

```json
{
  "caller": "visa",
  "card_id": 186266181,
  "mti": "0100",
  "local_amount": 5,
  "local_currency": "986",
  "settlement_amount": 5,
  "settlement_currency": "840",
  "entry_mode": "051",
  "processing_code": "00",
  "nsu": "0855861",
  "merchant": {
    "name": "merchantName",
    "city": "merchantCity",
    "country": "GB",
    "code": "016205",
    "id": "12121212"
  }
}
```

Example `National purchase`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0100",
  "local_amount": 50.5,
  "local_currency": "986",
  "settlement_amount": 50.5,
  "settlement_currency": "840",
  "entry_mode": "901",
  "processing_code": "00",
  "merchant": {
    "name": "merchantName"
  }
}
```

Example `National withdrawal`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0100",
  "local_amount": 50.5,
  "local_currency": "986",
  "settlement_amount": 50.5,
  "settlement_currency": "840",
  "entry_mode": "901",
  "processing_code": "01",
  "merchant": {
    "name": "merchantName"
  }
}
```

Example `Tecban Withdrawal`:

```json
{
  "caller": "tecban",
  "card_id": 6752905,
  "mti": "0200",
  "local_amount": 10,
  "local_currency": "986",
  "settlement_amount": 10,
  "settlement_currency": "840",
  "retrieval_reference_number": "00000004500000130",
  "entry_mode": "051",
  "account_type": "30",
  "processing_code": "01",
  "merchant": {
    "name": "merchantName"
  }
}
```

Example `Tecban Cancellation Withdrawal`:

```json
{
  "caller": "tecban",
  "card_id": 6752905,
  "mti": "0202",
  "local_amount": 10,
  "local_currency": "986",
  "settlement_amount": 10,
  "settlement_currency": "840",
  "retrieval_reference_number": "00000004500000130",
  "entry_mode": "051",
  "account_type": "30",
  "processing_code": "01",
  "authorization_code": "RHRCDM",
  "response_code": "W4",
  "merchant": {
    "name": "merchantName"
  }
}
```

Example `Internacional purchase`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0100",
  "local_amount": 50.5,
  "local_currency": "840",
  "settlement_amount": 50.5,
  "settlement_currency": "840",
  "entry_mode": "901",
  "merchant": {
    "name": "merchantName"
  },
  "processing_code": "00"
}
```

Example `Internacional withdrawal`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0100",
  "local_amount": 50.5,
  "local_currency": "840",
  "settlement_amount": 50.5,
  "settlement_currency": "840",
  "entry_mode": "901",
  "merchant": {
    "name": "merchantName"
  },
  "processing_code": "01"
}
```

Example `Crediario authorization`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0100",
  "local_amount": 50.5,
  "local_currency": "986",
  "settlement_amount": 50.5,
  "settlement_currency": "840",
  "entry_mode": "901",
  "merchant": {
    "name": "merchantName"
  },
  "installments": {
    "is_crediario": true,
    "number": 2,
    "with_interest": true
  }
}
```

Example `Cancel authorization (partial)`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0400",
  "local_amount": 5,
  "local_currency": "986",
  "settlement_amount": 5,
  "settlement_currency": "840",
  "entry_mode": "051",
  "account_type": "20",
  "processing_code": "00",
  "nsu": "0855861",
  "merchant": {
    "name": "MERCHANT test",
    "city": "MERCHANT CITY",
    "country": "BRA",
    "code": "5199"
  },
  "authorization_code": "Z3DDJ7",
  "replacement_amount": 4,
  "settlement_replacement_amount": 1
}
```

Example `Refund/credit authorization`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0400",
  "local_amount": 50.5,
  "local_currency": "986",
  "settlement_amount": 50.5,
  "settlement_currency": "840",
  "entry_mode": "901",
  "processing_code": "00",
  "merchant": {
    "name": "merchantName"
  }
}
```

Example `Credit voucher`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0100",
  "local_amount": 50.5,
  "local_currency": "986",
  "settlement_amount": 50.5,
  "settlement_currency": "840",
  "entry_mode": "901",
  "processing_code": "20",
  "merchant": {
    "name": "merchantName"
  }
}
```

Example `Installment Authorization`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0100",
  "local_amount": 100,
  "local_currency": "986",
  "settlement_amount": 100,
  "settlement_currency": "840",
  "entry_mode": "071",
  "processing_code": "00",
  "account_type": "30",
  "retrieval_reference_number": "000002",
  "nsu": "000002",
  "installments": {
    "number": 2,
    "with_interest": true,
    "payment_number": 1,
    "amount_of_each_installment": 50
  },
  "merchant": {
    "name": "merchantName",
    "city": "Teresina",
    "country": "BRA"
  }
}
```

Example `Replacement Authorization`:

```json
{
  "caller": "mastercard",
  "card_id": 4926027,
  "mti": "0400",
  "local_amount": 100,
  "local_currency": "986",
  "settlement_amount": 100,
  "settlement_currency": "840",
  "replacement_amount": 90,
  "authorization_code": "Z3DDJ7",
  "entry_mode": "071",
  "processing_code": "00",
  "account_type": "30",
  "retrieval_reference_number": "000002",
  "nsu": "000002",
  "merchant": {
    "name": "merchantName",
    "city": "Teresina",
    "country": "BRA"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Resource founded | `application/json`: object (schema `AuthorizationResponse`) |
| 400 | The request is acceptable but the syntax is malformed, for example, some type number parameter with a text content. |  |
| 404 | Specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `mti` | string (schema `MTI`) | no | Message type ID. For example: `0100` = auth. request, `0110`` = auth. response, `0120` = auth. advice. For more information, see [MTI](https://en.wikipedia.org/wiki/ISO_8583#Message_type_indicator_(MTI)).<br> | nullable: false; example: "0100" |
| `authorization_code` | string | no | Authorization code. | example: "F0JR9H" |
| `response_code` | string (schema `ResponseCode`) | no | Network two-digit response code. For example: 00 = approve, 51 = insufficient funds, 57 = card not active, 96 = system failure, etc. For more information, see [Validation codes for authorization events](doc:validation-codes-for-authorization-events). If `approve` = `false`, you can use this value to respond to the network.<br> | example: "00" |
| `authorization_date_time` | string | no | Authorization date and time in Coordinated Universal Time (UTC), i.e., 2020-01-01T10:10:00.000-03:00. | example: "2020-01-01T10:10:00.000-03:00" |
| `custom_code` | string (schema `CustomCode`) | no | Internal custom code generated in authorization flow for declined requests, indicating the reason the request was declined.<br><br>For more information, see [authorization validations](doc:validation-codes-for-authorization-events#authorization-validations).<br> | enum: ["FL2", "FL8", "FLB", "FLE", "DCM", "VMN", "998", "LUD", "LUE", "LUT", "LGE", "810", "PFT", "IAT", "BND", "ANF", "CTE", "CED", "ZBD", "FRB", "UBT", "FL6", "BNF", "BNP", "BNR", "VED", "BNU", "VEV", "UBN", "CSU", "NPL", "OP1", "TNF", "Z26", "Z24", "Z29", "Z23", "Z22"]; example: "FLB" |
| `match_address` | boolean | no | Is cardholder address street and number the same as that contained on the platform? | default: false; example: true |
| `match_postal_code` | boolean | no | Is cardholder postal code the same as the one contained on the platform? | default: false; example: true |
| `postal_five_digits` | boolean | no | Is this a valid postal code with five digits? | default: false; example: true |
| `no_address_data` | boolean | no | Is address registered on platform? | default: false; example: true |
| `authorization_id` | integer | no | Authorization ID | example: 4923745 |
| `account_id` | integer | no | Account ID | example: 24141240 |
| `installment_value` | string | no | Installment value. If there are no installments, this is the same as `contract_amount`. | example: "100.00" |
| `interest_rate` | number | no | Monthly interest rate | example: 2 |
| `number_of_installments` | number | no | Number of installments | example: 2 |
| `contract_amount` | string | no | Transaction value | example: "100.00" |
| `crediario_responses` | array of object (schema `CrediarioResponse`) | no | If there is more than one installment, this is the data for them. | example: [{"installmentValue": "51.86", "monthlyInterestRate": "2.00", "totalAmount": "103.72", "numberOfInstallments": "2", "feeAmount": "0.00", "taxesAmount": "0.86", "taxesPercentageOfTotalAmount": "0.83", "feePercentageOfTotalAmount": "0.00", "planType": "", "annualInterestRate": "", "monthlyTotalEffectiveCost": "", "annualTotalEffectiveCost": "", "installmentDate": "", "insurance": "", "insurancePercentageOfTotalAmount": "", "other": "", "otherPercentageOfTotalAmount": "", "totalAmountToMerchant": "", "merchantAmountPercentage": "", "reservedForFutureUse": ""}] |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `networktransactions-network-authorization-1` | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-simulate-authorizations`, `KU-CORE-fee-models-create-and-simulate`, `KU-CORE-flex-controls`.

<!-- op: spec=api-specs/Card_issuing_-_Authorization.yaml method=GET path=/direct-network-transactions/v1/authorizations/desc operationId=get-network-authorizations -->
### `GET /direct-network-transactions/v1/authorizations/desc` — List account authorizations

- **operationId:** `get-network-authorizations`
- **Specification:** `api-specs/Card_issuing_-_Authorization.yaml` (Card issuing - Authorization)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://api-networktransactions-http-ext.pismolabs.io`
- **Tags:** `Authorizations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List authorizations by account, tenant, or authorization ID. The response is an array of objects ordered by authorization ID. In descending order, the response includes every authorization for the account. Each page contains 20 items per page. If the authorization ID is used in the query parameter, the first record in the result will be the authorization related to this ID and the following results will be in descending order.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `authorization-id` | query | no | string | Authorization ID | example: "12345" |
| `page` | query | no | string | Indicates the selected page | example: "1" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Records found | `application/json`: object (schema `AuthorizationPaginatedResponse`) |
| 400 | The request is acceptable but the syntax is malformed, for example, some type number parameter with a text content. |  |
| 403 | Access forbidden. |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `current_page` | integer | no | Current page | example: 1 |
| `per_page` | integer | no | Records per page | default: 20; example: 20 |
| `pages` | integer | no | Total number of pages. | example: 1 |
| `total_items` | integer | no | Total number of items. | example: 1 |
| `items` | array of object (schema `AuthorizationPaginatedItemResponse`) | no | Authorization items |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Card_issuing_-_Authorization.yaml method=POST path=/direct-network-transactions/v1/cancellation operationId=cancel-network-authorizations -->
### `POST /direct-network-transactions/v1/cancellation` — Cancel authorization

- **operationId:** `cancel-network-authorizations`
- **Specification:** `api-specs/Card_issuing_-_Authorization.yaml` (Card issuing - Authorization)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://api-networktransactions-http-ext.pismolabs.io`
- **Tags:** `Authorizations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Perform a full cancellation of an authorization. The authorization must have the status `PENDING` or `PROCESSED` and must also not have been previously confirmed (cleared).
> This endpoint generates a [Network authorization received](https://developers.pismo.io/events/docs/networktransactions-network-authorization-1) event.

#### Request body

Required: yes

> Form details

**Content type `application/json`** — schema: object (schema `CancellationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_authorization_id` | integer | yes | Authorization ID—this field is mandatory if the `authorization_code` field is not provided. | example: 1231232 |
| `authorization_code` | string | yes | Authorization code—this field is mandatory if the `network_authorization_id` field is not provided. | example: "000SHK" |
| `transaction_identifier` | string | no | Transaction ID | example: "ZZIR8T" |
| `retrieval_reference_number` | string | no | Number generated by merchant point of sale (POS) system. | example: "000000000000355" |
| `card_id` | integer | yes | Transaction card ID | example: 124123 |
| `origin` | string | no | This field identifies the origin of the operation to be cancelled as MIGRATION, ONUS, or STRIKER. | maxLength: 15; example: "ONUS" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Full cancellation accepted | `application/json`: object (schema `CancellationResponse`) |
| 400 | The request is acceptable but the syntax is malformed, for example, some type number parameter with a text content. |  |
| 403 | Access forbidden. |  |
| 404 | Specified resource was not found |  |
| 409 | The specified resource status conflict with the current request |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Success message | example: "Success" |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `networktransactions-network-authorization-1` | https://developers.pismo.io/events/docs/networktransactions-network-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-simulate-authorizations`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/CrediarioResponse -->
### Schema `CrediarioResponse`

Pointer: `#/components/schemas/CrediarioResponse`. Type: object (schema `CrediarioResponse`).

> Data related to installments

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `installmentValue` | string | no | Installment value | example: "51.86" |
| `monthlyInterestRate` | string | no | Monthly interest rate | example: "2.00" |
| `totalAmount` | string | no | Total amount | example: "103.72" |
| `numberOfInstallments` | string | no | Number of installments | example: "2" |
| `feeAmount` | string | no | Fee amount | example: "0.00" |
| `taxesAmount` | string | no | Taxes amount | example: "0.86" |
| `taxesPercentageOfTotalAmount` | string | no | Taxes percentage of total amount | example: "0.83" |
| `feePercentageOfTotalAmount` | string | no | Fee percentage of total amount | example: "0.00" |
| `planType` | string | no | Plan type - with interest (20), without interest(21) or a crediario type(25) | example: "20" |
| `annualInterestRate` | string | no | Annual interest rate | example: "10.2" |
| `monthlyTotalEffectiveCost` | string | no | Monthly total effective cost | example: "1.40" |
| `annualTotalEffectiveCost` | string | no | Aannual total effective cost | example: "0.00" |
| `installmentDate` | string | no | Installment date - format = yyyymmdd | example: "20201129" |
| `insurance` | string | no | Insurance | example: "1" |
| `insurancePercentageOfTotalAmount` | string | no | Insurance percentage of total amount | example: "2" |
| `other` | string | no | Any other added values, if applicable, that the cardholder is paying | example: "" |
| `otherPercentageOfTotalAmount` | string | no | Other percentage of total amount | example: "" |
| `totalAmountToMerchant` | string | no | Total amount to be paid to merchant (purchase amount) | example: "4" |
| `merchantAmountPercentage` | string | no | Percentage of the total amount to be paid to merchant | example: "0008" |
| `reservedForFutureUse` | string | no | Reserved for future use |  |

<!-- schema: #/components/schemas/AuthorizationPaginatedItemResponse -->
### Schema `AuthorizationPaginatedItemResponse`

Pointer: `#/components/schemas/AuthorizationPaginatedItemResponse`. Type: object (schema `AuthorizationPaginatedItemResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `correlation_id` | string | no | Correlation ID, which is used to link related API requests and events. The Pismo engineering team can use this to track everything related to a call. If one is not passed, it is automatically generated and returned to the client in a response header. | example: "22222222-2222-2222-2222-222222222222" |
| `id` | integer | no | Authorization ID | example: 1 |
| `message_type_indicator` | string (schema `MTI`) | no | Message type ID. For example: `0100` = auth. request, `0110`` = auth. response, `0120` = auth. advice. For more information, see [MTI](https://en.wikipedia.org/wiki/ISO_8583#Message_type_indicator_(MTI)).<br> | nullable: false; example: "0100" |
| `soft_descriptor` | string | no | Soft descriptor, which is temporary text displayed on the customer statement after a transaction authorization. | example: "Descriptor" |
| `partial_cancellation_total_amount` | string | no | Total amount of partial cancellation. | example: "1000.51" |
| `org_operation_id` | integer | no | Org operation ID. | example: 10 |
| `nsu` | string (schema `NSU`) | no | Authorization Network Settlement Utility (NSU) number - tracks the flow of funds between parties involved in a payment card transaction, including the bank, the merchant, and the card network. Different payment card networks may have their own NSU systems, ie, Visa - VisaNet, Mastercard - BankNet, or they may use a third party.<br> | example: "15469" |
| `status_id` | string | no | Authorization status ID | example: "1" |
| `authorization_code` | string | no | Authorization code | example: "ABC123" |
| `account_id` | integer | no | Account ID | example: 123456789 |
| `card_id` | integer | no | Card ID | example: 987654321 |
| `cardholder_currency_transaction_amount` | string | no | Transaction amount in cardholder currency. | example: "20.78" |
| `cardholder_currency_code` | string | no | Cardholder currency code. | example: "986" |
| `settlement_currency_code` | string | no | Three-digit code of the settlement currency. | example: "840" |
| `settlement_currency_transaction_amount` | string | no | Transaction amount in settlement currency. | example: "4.00" |
| `entry_mode` | string | no | Entry mode | example: "051" |
| `response_code` | string | no | Response code | example: "00" |
| `merchant_name` | string | no | Merchant name | example: "Store 007" |
| `merchant_city` | string | no | Merchant city | example: "Sao Paulo" |
| `merchant_state_or_country` | string | no | Merchant state or country | example: "BRA" |
| `org_id` | string | no | Org ID or tenant ID | example: "TN-11111111-1111-1111-1111-111111111111" |
| `retrieval_reference_number` | string | no | Retrieval reference number | example: "9999998877" |
| `original_network_transaction_id` | string | no | Original network transaction ID or TID | example: "987ABB" |
| `transmission_datetime` | string | no | Transmission date time | format: "date-time"; example: "2022-11-30 00:00:00" |
| `event_datetime` | string | no | Event date time | format: "date-time"; example: "2023-11-07 15:02:28" |
| `event_datetime_utc` | string | no | Event date and time in UTC. | example: "2023-11-07 18:02:28" |
| `datetime` | string | no | Authorization date and time. | example: "2023-11-07 15:02:28" |
| `local_currency_code` | string | no | Three-digit local currency code | example: "840" |
| `number_of_installments` | integer | no | Number of installments | example: 1 |
| `principal_amount` | string | no | Principal amount | example: "20.78" |
| `local_currency_transaction_amount` | string | no | Transaction amount in local currency. | example: "4.00" |
| `fee_amount` | string | no | Fee amount. | example: "0.00" |
| `cardholder_currency_conversion_rate` | string | no | Cardholder currency conversion rate. | example: "5.19000000" |
| `merchant_category_id` | integer | no | Merchant Category Code (MCC) | format: "int32"; example: 5199 |
| `processing_code` | string | no | Processing code | example: "00" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Authorization.yaml` | tag `Authorizations`: POST /networktransactions/v1/authorizations, GET /direct-network-transactions/v1/authorizations/desc, POST /direct-network-transactions/v1/cancellation | https://github.com/PismoDevEx/pismo-api-specs | `f64e4226c94e8ce5…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-simulate-authorizations` — Simulate authorizations
- `KU-CORE-fee-models-create-and-simulate` — Creating, applying and simulating fee models
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
