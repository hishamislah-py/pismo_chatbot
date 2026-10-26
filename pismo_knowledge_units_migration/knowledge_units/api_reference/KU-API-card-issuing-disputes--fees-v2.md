---
ku_id: KU-API-card-issuing-disputes--fees-v2
title: 'API reference: Card issuing - Disputes — Fees V2'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Disputes.yaml
  sha256: 5c1d5513e1f3a4d1daa4d6bd654885c4edfeb5135eaa60b50f1a74d62031baad
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
- create-fee-v2
- get-fee-v2
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-disputes-overview
- KU-ERR-codes-acq-to-esma
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — Fees V2

**KU ID:** `KU-API-card-issuing-disputes--fees-v2` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Fees V2` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to create and check status for fees V2

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/fee` | `create-fee-v2` | Create fee V2 | no |
| `GET /v2/fee/{fee_id}` | `get-fee-v2` | Get fee V2 | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v2/fee operationId=create-fee-v2 -->
### `POST /v2/fee` — Create fee V2

- **operationId:** `create-fee-v2`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fees V2`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> A fee, or *fee collection* in network terminology, allows acquirers and issuers to exchange money outside the standard chargeback process. Typically, this means reversing a settled chargeback, but not always.
>
> You can use this endpoint to create a fee collection/funds disbursement with or without a chargeback **case number**.
>
> You can create a fee collection/funds disbursement for an existing **case**, or, if it doesn't exist, you can provide the necessary transaction/card information to create it.
>
> The main differences between fees V2 and V1 are:
>   * V1&mdash;Associated with the dispute/installment
>   * V2&mdash;Can only be created with transaction ID (Full balance), transaction information (Zero balance), card ID and customer ID, or NetworkCaseID (VisaCaseNumber).
>
> For more information, refer to [Dispute fees](https://developers.pismo.io/pismo-docs/docs/disputes-overview#dispute-fees) in the Disputes overview guide. 
>
> This feature is **only** currently available for **Visa**.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |

#### Request body

Required: yes

> Fill out and submit one object

**Content type `application/json`** — schema: anyOf: object (schema `Create_Visa_Fee_From_Transaction_Full_Balance`), object (schema `Create_Visa_Fee_From_Transaction_Zero_Balance`), object (schema `Create_Visa_Fee_From_Card`), object (schema `Create_Visa_Fee_From_Network_Case_ID`)

_anyOf option 1: schema `Create_Visa_Fee_From_Transaction_Full_Balance`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_brand_type` | string (schema `NetworkBrandType`) | yes | Card network brand. Currently, only `Visa`. | enum: ["Visa"]; example: "Visa" |
| `transaction_id` | number (schema `TransactionId`) | yes | Pismo transaction ID. | example: 1234567890 |
| `currency` | string (schema `Currency`) | yes | ISO-4217 currency code. | example: "USD" |
| `amount` | number (schema `Amount`) | yes | Fee amount. | format: "double"; example: 215 |
| `credit_sender` | boolean (schema `CreditSender`) | yes | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean (schema `CreditReceiver`) | yes | Should receiver be credited? |  |
| `fee` | object (schema `VisaFee`) | yes |  |  |

_anyOf option 2: schema `Create_Visa_Fee_From_Transaction_Zero_Balance`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_brand_type` | string (schema `NetworkBrandType`) | yes | Card network brand. Currently, only `Visa`. | enum: ["Visa"]; example: "Visa" |
| `arn` | string (schema `Arn`) | yes | Acquirer Reference Number (ARN). | nullable: true; example: "12345678901234567890123" |
| `transaction_amount` | number (schema `TransactionAmount`) | yes | Transaction amount | example: 86753.09 |
| `transaction_date` | string (schema `TransactionDate`) | yes | Transaction date, format = yyyy-mm-dd.<br> | nullable: true; example: "2025-08-11" |
| `currency` | string (schema `Currency`) | yes | ISO-4217 currency code. | example: "USD" |
| `amount` | number (schema `Amount`) | yes | Fee amount. | format: "double"; example: 215 |
| `credit_sender` | boolean (schema `CreditSender`) | yes | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean (schema `CreditReceiver`) | yes | Should receiver be credited? |  |
| `fee` | object (schema `VisaFee`) | yes |  |  |

_anyOf option 3: schema `Create_Visa_Fee_From_Card`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_brand_type` | string (schema `NetworkBrandType`) | yes | Card network brand. Currently, only `Visa`. | enum: ["Visa"]; example: "Visa" |
| `card_id` | number (schema `CardID`) | yes | Pismo card ID. | example: 123456 |
| `customer_id` | number (schema `CustomerId`) | yes | Pismo customer ID. | example: 10203040 |
| `currency` | string (schema `Currency`) | yes | ISO-4217 currency code. | example: "USD" |
| `amount` | number (schema `Amount`) | yes | Fee amount. | format: "double"; example: 215 |
| `credit_sender` | boolean (schema `CreditSender`) | yes | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean (schema `CreditReceiver`) | yes | Should receiver be credited? |  |
| `fee` | object (schema `VisaFeeCard`) | yes |  |  |

_anyOf option 4: schema `Create_Visa_Fee_From_Network_Case_ID`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `network_brand_type` | string (schema `NetworkBrandType`) | yes | Card network brand. Currently, only `Visa`. | enum: ["Visa"]; example: "Visa" |
| `network_case_id` | string (schema `NetworkCaseId`) | yes | Network case ID. | nullable: true; example: "1234567890" |
| `currency` | string (schema `Currency`) | yes | ISO-4217 currency code. | example: "USD" |
| `amount` | number (schema `Amount`) | yes | Fee amount. | format: "double"; example: 215 |
| `credit_sender` | boolean (schema `CreditSender`) | yes | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean (schema `CreditReceiver`) | yes | Should receiver be credited? |  |
| `fee` | object (schema `VisaFee`) | yes |  |  |


Example `FeeVisaFromTransactionFullBalance` (Create Visa Fee from Transaction - Full Balance):

```json
{
  "network_brand_type": "Visa",
  "transaction_id": 1234567890,
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "Reason": "350",
    "Message": "Fee collection created via SYSTEM",
    "DestinationBin": "474749",
    "EventDate": "2025-08-28"
  }
}
```

Example `FeeFromTransactionZeroBalance` (Create Visa Fee from Transaction - Zero Balance):

```json
{
  "network_brand_type": "Visa",
  "arn": "0000000000539598",
  "transaction_date": "2022-09-02",
  "transaction_amount": 150,
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "Reason": "100",
    "Message": "Fee collection created via SYSTEM",
    "DestinationBin": "484884"
  }
}
```

Example `FeeFromCard` (Create Visa Fee from Card):

```json
{
  "network_brand_type": "Visa",
  "currency": "USD",
  "amount": 150,
  "credit_sender": true,
  "credit_receiver": false,
  "card_id": 123456,
  "customer_id": 7890123,
  "fee": {
    "Reason": "130",
    "Message": "Fee collection created via SYSTEM",
    "DestinationBin": "484884"
  }
}
```

Example `FeeFromNetworkCaseID` (Create Visa Fee from Network Case ID):

```json
{
  "network_brand_type": "Visa",
  "network_case_id": "10203040",
  "currency": "USD",
  "amount": 150,
  "credit_sender": true,
  "credit_receiver": false,
  "fee": {
    "Reason": "350",
    "Message": "Fee collection created via SYSTEM",
    "EventDate": "2025-08-28"
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: anyOf: object (schema `Fee_Response_From_Transaction_Full_Balance`), object (schema `Fee_Response_From_Transaction_Zero_Balance`), object (schema `Fee_Response_From_Card`), object (schema `Fee_Response_From_Network_Case_ID`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 504 | Gateway timeout | `application/json`: object (schema `ErrorModel`) |

##### Response 201

**201 `application/json` body fields:**

_No fields declared in the schema._

201 Example `FeeResponseFromTransactionFullBalance` (Visa Fee from Transaction - Full Balance):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "transaction_id": 1234567890,
  "arn": "ABC123YZ25",
  "transaction_amount": 150,
  "transaction_date": "2024-09-27",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:08",
  "status": "PENDING",
  "source": "ISSUER"
}
```

201 Example `FeeResponseFromTransactionZeroBalance` (Visa Fee from Transaction - Zero Balance):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "arn": "0000000000539598",
  "transaction_amount": 150,
  "transaction_date": "2022-09-02",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "message": "Fee collection created via SYSTEM",
    "reason": "100"
  },
  "created_at": "2025-08-29 18:05:29",
  "status": "PENDING",
  "source": "ISSUER"
}
```

201 Example `FeeResponseFromCard` (Visa Fee from Card):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "currency": "USD",
  "amount": 150,
  "credit_sender": true,
  "credit_receiver": false,
  "fee": {
    "destination_bin": "234324",
    "message": "Fee collection created via SYSTEM",
    "reason": "130",
    "source_bin": "123456"
  },
  "created_at": "2025-08-29 18:05:43",
  "card_id": 405060,
  "status": "PENDING",
  "source": "ISSUER"
}
```

201 Example `FeeResponseFromNetworkCaseId` (Visa Fee from Network Case ID):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:57",
  "status": "PENDING",
  "source": "ISSUER"
}
```

##### Response 400

400 Example `EDPT0002 - Failed during validation of request payload`:

```json
{
  "code": "EDPT0003",
  "message": "Failed to parse request payload",
  "http_status_code": 400
}
```

400 Example `BDPT0019 - Unsupported Fee brand type`:

```json
{
  "code": "BDPT0019",
  "message": "Unsupported Fee brand type",
  "http_status_code": 400
}
```

##### Response 401

401 Example `EDPT0005 - Missing or invalid Authorization header`:

```json
{
  "code": "EDPT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

##### Response 404

404 Example `EDPT0009 - TransactionById returned not found`:

```json
{
  "code": "EDPT0009",
  "message": "TransactionById returned [Not found] using ID: 1234567890",
  "http_status_code": 404
}
```

404 Example `EDPT0009 - Cards returned not found`:

```json
{
  "code": "EDPT0009",
  "message": "Cards returned [Not found] using ID: 405060",
  "http_status_code": 404
}
```

##### Response 422

422 Example `BDPT0001 - Error while validating fields`:

```json
{
  "code": "BDPT0001",
  "message": "Error while validating fields",
  "http_status_code": 422,
  "details": {
    "payload": [
      {
        "field": "network_brand_type",
        "message": "This is field is required"
      },
      {
        "field": "currency",
        "message": "This is field is required"
      },
      {
        "field": "amount",
        "message": "This is field is required"
      },
      {
        "field": "credit_sender",
        "message": "This is field is required"
      },
      {
        "field": "credit_sender",
        "message": "This field cannot have the same value as the: 'credit_receiver'"
      },
      {
        "field": "credit_receiver",
        "message": "This is field is required"
      },
      {
        "field": "credit_receiver",
        "message": "This field cannot have the same value as the: 'credit_sender'"
      },
      {
        "field": "fee",
        "message": "This is field is required"
      },
      {
        "field": "currency",
        "message": "This field does not comply with the ISO 4217 standard"
      },
      {
        "field": "transaction_date",
        "message": "This field has an invalid date format. The correct format is yyyy-MM-dd"
      },
      {
        "field": "reason",
        "message": "This field has an invalid value. The accepted values are: 100, 110, 130, 140, 150, 170, 200, 210, 220, 230, 240, 250, 350, 401, 402"
      },
      {
        "field": "transaction_id",
        "message": "This field is required when the other fields are not filled: 'network_case_id', 'destination_bin', 'arn', 'transaction_amount', 'transaction_date'"
      },
      {
        "field": "arn",
        "message": "This field is required when the other fields are not filled: 'transaction_id', 'network_case_id', 'destination_bin'"
      },
      {
        "field": "transaction_amount",
        "message": "This field is required when the other fields are not filled: 'transaction_id', 'network_case_id', 'destination_bin'"
      },
      {
        "field": "transaction_date",
        "message": "This field is required when the other fields are not filled: 'transaction_id', 'network_case_id', 'destination_bin'"
      },
      {
        "field": "network_case_id",
        "message": "This field is required when the other fields are not filled: 'transaction_id', 'destination_bin', 'arn', 'transaction_amount', 'transaction_date'"
      },
      {
        "field": "destination_bin",
        "message": "This field is required when the other fields are not filled: 'transaction_id', 'network_case_id', 'arn', 'transaction_amount', 'transaction_date'"
      },
      {
        "field": "card_id",
        "message": "This field is required when 'destination_bin' is filled in"
      }
    ]
  }
}
```

422 Example `BDPT0021 - Authorized Account is different from request`:

```json
{
  "code": "BDPT0021",
  "message": "Authorized Account is different from request",
  "http_status_code": 422
}
```

422 Example `BDPT0022 - Network Brand Type Mismatch`:

```json
{
  "code": "BDPT0022",
  "message": "The 'network_brand_type' [Visa] of the request does not match the 'network' [Mastercard] associated with the Transaction",
  "http_status_code": 422
}
```

##### Response 500

500 Example `EDPT9998 - Something went wrong, please try again later`:

```json
{
  "code": "EDPT9998",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `EDPT0001 - Request timeout`:

```json
{
  "code": "EDPT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EDPT0003` | Failed to parse request payload |
| 400 | `BDPT0019` | Unsupported Fee brand type |
| 401 | `EDPT0005` | Missing or invalid Authorization header |
| 404 | `EDPT0009` | TransactionById returned [Not found] using ID: 1234567890 |
| 422 | `BDPT0001` | Error while validating fields |
| 422 | `BDPT0021` | Authorized Account is different from request |
| 422 | `BDPT0022` | The 'network_brand_type' [Visa] of the request does not match the 'network' [Mastercard] associated with the Transaction |
| 500 | `EDPT9998` | Something went wrong, please try again later |
| 504 | `EDPT0001` | Request timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;404;422;500;504`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-disputes-overview`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v2/fee/{fee_id} operationId=get-fee-v2 -->
### `GET /v2/fee/{fee_id}` — Get fee V2

- **operationId:** `get-fee-v2`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fees V2`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get details about a specific fee.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message. | example: "Bearer eyJhbGci...IUzUx" |
| `fee_id` | path | yes | number | Fee ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Specific fee information response. | `application/json`: object (schema `GetFeeResponseModel`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 504 | Gateway timeout | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fee_id` | number (schema `FeeId`) | no | Pismo fee ID. | example: 123 |
| `org_id` | string (schema `OrgId`) | no | Organization/tenant ID. | example: "TN-34778262-f4f0-464d-b4c6-a14exxxxxxxx" |
| `account_id` | number (schema `AccountID`) | no | Pismo account ID | example: 577830 |
| `card_id` | number (schema `CardID`) | no | Pismo card ID. | example: 123456 |
| `transaction_id` | number (schema `TransactionId`) | no | Pismo transaction ID. | example: 1234567890 |
| `arn` | string (schema `Arn`) | no | Acquirer Reference Number (ARN). | nullable: true; example: "12345678901234567890123" |
| `transaction_amount` | number (schema `TransactionAmount`) | no | Transaction amount | example: 86753.09 |
| `transaction_date` | string (schema `TransactionDate`) | no | Transaction date, format = yyyy-mm-dd.<br> | nullable: true; example: "2025-08-11" |
| `network_brand_type` | string (schema `NetworkBrandType`) | no | Card network brand. Currently, only `Visa`. | enum: ["Visa"]; example: "Visa" |
| `currency` | string (schema `Currency`) | no | ISO-4217 currency code. | example: "USD" |
| `amount` | number (schema `Amount`) | no | Fee amount. | format: "double"; example: 215 |
| `credit_sender` | boolean (schema `CreditSender`) | no | Credit the sender? Default is `false`. | default: false |
| `credit_receiver` | boolean (schema `CreditReceiver`) | no | Should receiver be credited? |  |
| `network_case_id` | string (schema `NetworkCaseId`) | no | Network case ID. | nullable: true; example: "1234567890" |
| `network_fee_id` | string (schema `NetworkFeeId`) | no | Network fee ID. | nullable: true; example: "1234567890" |
| `network_response` | string (schema `NetworkResponse`) | no | Network response for something wrong.<br> | example: "The network returned [Error to create Fraud Report, invalid field], reasonCode [E-90000000] with the source [NETWORK_EXCEPTION]." |
| `fee` | object (schema `VisaFeeResponse`) | no |  |  |
| `created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `updated_at` | string (schema `UpdatedAt`) | no | Datetime when updated, format = yyyy-mm-dd hh:mm:ss | example: "2024-10-18 11:21:45" |
| `source` | string (schema `Source`) | no | Who initiated the fee. | enum: ["ISSUER", "ACQUIRER"] |
| `status` | string (schema `FeeStatus`) | no | Fee status:<br><br><br>- `PENDING`&mdash;The fee creation request has been received and is awaiting Pismo processing within the network.<br><br>- `FAILED`&mdash;An error occurred while attempting to create the fee in the network. The operation was not completed.<br><br>- `WAITING_NETWORK`&mdash;The request has been successfully sent to the network and is currently awaiting a response.<br><br>- `PROCESSED`&mdash;The fee was successfully created and network-confirmed.<br><br>- `REJECTED`&mdash;The network declined the fee creation request.<br><br> | enum: ["PENDING", "FAILED", "WAITING_NETWORK", "PROCESSED", "REJECTED"]; example: "PENDING" |

200 Example `FeeResponseFromTransactionFullBalancePending` (Visa Fee from Transaction - Full balance with `PENDING` status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "transaction_id": 1234567890,
  "arn": "ABC123YZ25",
  "transaction_amount": 150,
  "transaction_date": "2024-09-27",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:08",
  "status": "PENDING",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionFullBalanceWaitingNetwork` (Visa Fee from Transaction - Full Balance with WAITING_NETWORK status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "transaction_id": 1234567890,
  "arn": "ABC123YZ25",
  "transaction_amount": 150,
  "transaction_date": "2024-09-27",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:08",
  "updated_at": "2025-09-01 15:39:22",
  "status": "WAITING_NETWORK",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionFullBalanceFailed` (Visa Fee from Transaction - Full Balance with FAILED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_response": "Message: Message of Error - ReasonCode: E-000000000 - Source: Source of Error",
  "transaction_id": 1234567890,
  "arn": "ABC123YZ25",
  "transaction_amount": 150,
  "transaction_date": "2024-09-27",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:08",
  "updated_at": "2025-09-01 15:39:22",
  "status": "FAILED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionFullBalanceProcessed` (Visa Fee from Transaction - Full Balance with PROCESSED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "network_response": "[{\"StatusCode\": null, \"StatusMessage\": \"Acknowledged\"}]",
  "transaction_id": 1234567890,
  "arn": "ABC123YZ25",
  "transaction_amount": 150,
  "transaction_date": "2024-09-27",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:08",
  "updated_at": "2025-09-01 15:39:22",
  "status": "PROCESSED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionFullBalanceRejected` (Visa Fee from Transaction - Full Balance with `REJECTED` status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "network_response": "[{\"StatusCode\": \"RC14\", \"StatusMessage\": \"Reason of Rejection\"}]",
  "transaction_id": 1234567890,
  "arn": "ABC123YZ25",
  "transaction_amount": 150,
  "transaction_date": "2024-09-27",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:08",
  "updated_at": "2025-09-01 15:39:22",
  "status": "REJECTED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionZeroBalancePending` (Visa Fee from Transaction - Zero Balance with PENDING status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "arn": "0000000000539598",
  "transaction_amount": 150,
  "transaction_date": "2022-09-02",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:29",
  "status": "PENDING",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionZeroBalanceWaitingNetwork` (Visa Fee from Transaction - Zero Balance with WAITING_NETWORK status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "arn": "0000000000539598",
  "transaction_amount": 150,
  "transaction_date": "2022-09-02",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:29",
  "updated_at": "2025-09-01 15:39:22",
  "status": "WAITING_NETWORK",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionZeroBalanceFailed` (Visa Fee from Transaction - Zero Balance with FAILED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_response": "Message: Message of Error - ReasonCode: E-000000000 - Source: Source of Error",
  "arn": "0000000000539598",
  "transaction_amount": 150,
  "transaction_date": "2022-09-02",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:29",
  "updated_at": "2025-09-01 15:39:22",
  "status": "FAILED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionZeroBalanceProcessed` (Visa Fee from Transaction - Zero Balance with PROCESSED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "network_response": "[{\"StatusCode\": null, \"StatusMessage\": \"Acknowledged\"}]",
  "arn": "0000000000539598",
  "transaction_amount": 150,
  "transaction_date": "2022-09-02",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:29",
  "updated_at": "2025-09-01 15:39:22",
  "status": "PROCESSED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromTransactionZeroBalanceRejected` (Visa Fee from Transaction - Zero Balance with REJECTED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "network_response": "[{\"StatusCode\": \"RC14\", \"StatusMessage\": \"Reason of Rejection\"}]",
  "arn": "0000000000539598",
  "transaction_amount": 150,
  "transaction_date": "2022-09-02",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:29",
  "updated_at": "2025-09-01 15:39:22",
  "status": "REJECTED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromCardPending` (Visa Fee from Card with PENDING status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "currency": "USD",
  "amount": 150,
  "credit_sender": true,
  "credit_receiver": false,
  "fee": {
    "destination_bin": "5678",
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350",
    "source_bin": "1234"
  },
  "created_at": "2025-08-29 18:05:43",
  "card_id": 405060,
  "status": "PENDING",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromCardWaitingNetwork` (Visa Fee from Card with WAITING_NETWORK status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_fee_id": "5678",
  "currency": "USD",
  "amount": 150,
  "credit_sender": true,
  "credit_receiver": false,
  "fee": {
    "destination_bin": "5678",
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350",
    "source_bin": "1234"
  },
  "created_at": "2025-08-29 18:05:43",
  "updated_at": "2025-09-01 15:39:22",
  "card_id": 405060,
  "status": "WAITING_NETWORK",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromCardFailed` (Visa Fee from Card with FAILED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_response": "Message: Message of Error - ReasonCode: E-000000000 - Source: Source of Error",
  "currency": "USD",
  "amount": 150,
  "credit_sender": true,
  "credit_receiver": false,
  "fee": {
    "destination_bin": "5678",
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350",
    "source_bin": "1234"
  },
  "created_at": "2025-08-29 18:05:43",
  "updated_at": "2025-09-01 15:39:22",
  "card_id": 405060,
  "status": "FAILED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromCardProcessed` (Visa Fee from Card with PROCESSED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_fee_id": "5678",
  "network_response": "[{\"StatusCode\": null, \"StatusMessage\": \"Acknowledged\"}]",
  "currency": "USD",
  "amount": 150,
  "credit_sender": true,
  "credit_receiver": false,
  "fee": {
    "destination_bin": "5678",
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350",
    "source_bin": "1234"
  },
  "created_at": "2025-08-29 18:05:43",
  "updated_at": "2025-09-01 15:39:22",
  "card_id": 405060,
  "status": "PROCESSED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromCardRejected` (Visa Fee from Card with REJECTED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_fee_id": "5678",
  "network_response": "[{\"StatusCode\": \"RC14\", \"StatusMessage\": \"Reason of Rejection\"}]",
  "currency": "USD",
  "amount": 150,
  "credit_sender": true,
  "credit_receiver": false,
  "fee": {
    "destination_bin": "5678",
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350",
    "source_bin": "1234"
  },
  "created_at": "2025-08-29 18:05:43",
  "updated_at": "2025-09-01 15:39:22",
  "card_id": 405060,
  "status": "REJECTED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromNetworkCaseIdPending` (Visa Fee from Network Case ID with PENDING status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:57",
  "status": "PENDING",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromNetworkCaseIdWaitingNetwork` (Visa Fee from Network Case ID with WAITING_NETWORK status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:57",
  "updated_at": "2025-09-01 15:39:22",
  "status": "WAITING_NETWORK",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromNetworkCaseIdFailed` (Visa Fee from Network Case ID with FAILED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_response": "Message: Message of Error - ReasonCode: E-000000000 - Source: Source of Error",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:57",
  "updated_at": "2025-09-01 15:39:22",
  "status": "FAILED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromNetworkCaseIdProcessed` (Visa Fee from Network Case ID with PROCESSED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "network_response": "[{\"StatusCode\": null, \"StatusMessage\": \"Acknowledged\"}]",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:57",
  "updated_at": "2025-09-01 15:39:22",
  "status": "PROCESSED",
  "source": "ISSUER"
}
```

200 Example `FeeResponseFromNetworkCaseIdRejected` (Visa Fee from Network Case ID with REJECTED status):

```json
{
  "fee_id": 1,
  "org_id": "TN-123",
  "account_id": 102030,
  "network_brand_type": "Visa",
  "network_case_id": "1234",
  "network_fee_id": "5678",
  "network_response": "[{\"StatusCode\": \"RC14\", \"StatusMessage\": \"Reason of Rejection\"}]",
  "currency": "USD",
  "amount": 150,
  "credit_sender": false,
  "credit_receiver": true,
  "fee": {
    "event_date": "2025-08-28",
    "message": "Fee collection created via SYSTEM",
    "reason": "350"
  },
  "created_at": "2025-08-29 18:05:57",
  "updated_at": "2025-09-01 15:39:22",
  "status": "REJECTED",
  "source": "ISSUER"
}
```

##### Response 400

400 Example `EDPT0004 - Invalid fee_id param`:

```json
{
  "code": "EDPT0004",
  "message": "Invalid fee_id param",
  "http_status_code": 400
}
```

##### Response 401

401 Example `EDPT0005 - Missing or invalid Authorization header`:

```json
{
  "code": "EDPT0005",
  "message": "Missing or invalid Authorization header",
  "http_status_code": 401
}
```

##### Response 404

404 Example `BDPT0006 - Fee [123] not found`:

```json
{
  "code": "BDPT0006",
  "message": "Fee [123] not found",
  "http_status_code": 404
}
```

##### Response 422

422 Example `BDPT0021 - Authorized Account is different from request`:

```json
{
  "code": "BDPT0021",
  "message": "Authorized Account is different from request",
  "http_status_code": 422
}
```

##### Response 500

500 Example `EDPT9998 - Something went wrong, please try again later`:

```json
{
  "code": "EDPT9998",
  "message": "Something went wrong, please try again later",
  "http_status_code": 500
}
```

##### Response 504

504 Example `EDPT0001 - Request timeout`:

```json
{
  "code": "EDPT0001",
  "message": "Request timeout",
  "http_status_code": 504
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EDPT0004` | Invalid fee_id param |
| 401 | `EDPT0005` | Missing or invalid Authorization header |
| 404 | `BDPT0006` | Fee [123] not found |
| 422 | `BDPT0021` | Authorized Account is different from request |
| 500 | `EDPT9998` | Something went wrong, please try again later |
| 504 | `EDPT0001` | Request timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;422;500;504`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/VisaFee -->
### Schema `VisaFee`

Pointer: `#/components/schemas/VisaFee`. Type: object (schema `VisaFee`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `Reason` | string (schema `FeeReasonCode`) | yes | Fee reason code.<br><br> `100`&mdash;Telecommunication charges (non-US)<br><br> `110`&mdash;Auto telex charges (non-US)<br><br> `130`&mdash;Lost/stolen card report fees<br><br> `140`&mdash;Merchant service fees<br><br> `150`&mdash;Recovered Visa card, Electron card, or Visa Electron card. Handling fees/rewards. Non-US - Recovered card handling fee<br><br> `170`&mdash;Recovery of retrieval request fees. <br><br> `200`&mdash;Emergency replacement card distribution fee<br><br> `210`&mdash;Emergency cash disbursement handling fee<br><br> `220`&mdash;Arbitration/compliance/resolution case decision or filing fee<br><br> `230`&mdash;Incorrect merchant ID/transacton date handling<br><br> `240`&mdash;"Good faith" collection letter settlement funds disbursement. Non-US - Funds disbursement transactions<br><br> `250`&mdash;Cardholder does not recognize transacton chargeback handling fee.<br><br> `350`&mdash;Pre-arbitration/Pre-compliance settlement funds disbursement<br><br> `401`&mdash;Prepaid load revenue sharing<br><br> `402`&mdash;Non-US - Collection for an unsettled prepaid of original credit authorization<br><br><br>**Note:** This is from the Visa IES spreadsheet. This spreadsheet is updated every 6 months or so. Check periodically with Visa for latest fee reason codes.<br> | enum: ["100", "110", "130", "140", "150", "170", "200", "210", "220", "230", "240", "250", "350", "401", "402"] |
| `Message` | string (schema `FeeMessage`) | yes | Fee message. 70 chars maximum. | maxLength: 70; nullable: true |
| `EventDate` | string (schema `FeeEventDate`) | no | <br>Use this field to pass:<br><br>    - Date the card was recovered (Reason 150)<br>    - Collection letter date (Reason 240)<br>    - Pre-Compliance / Pre-Arbitration Letter Date (Reason 350)<br>    <br>**REQUIRED** when `Reason` is `150`, `240`, or `350` (US domestic); otherwise, it is not valid. <br>    <br>Format = yyyy-mm-dd<br> |  |

<!-- schema: #/components/schemas/VisaFeeCard -->
### Schema `VisaFeeCard`

Pointer: `#/components/schemas/VisaFeeCard`. Type: object (schema `VisaFeeCard`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `Reason` | string (schema `FeeReasonCode`) | yes | Fee reason code.<br><br> `100`&mdash;Telecommunication charges (non-US)<br><br> `110`&mdash;Auto telex charges (non-US)<br><br> `130`&mdash;Lost/stolen card report fees<br><br> `140`&mdash;Merchant service fees<br><br> `150`&mdash;Recovered Visa card, Electron card, or Visa Electron card. Handling fees/rewards. Non-US - Recovered card handling fee<br><br> `170`&mdash;Recovery of retrieval request fees. <br><br> `200`&mdash;Emergency replacement card distribution fee<br><br> `210`&mdash;Emergency cash disbursement handling fee<br><br> `220`&mdash;Arbitration/compliance/resolution case decision or filing fee<br><br> `230`&mdash;Incorrect merchant ID/transacton date handling<br><br> `240`&mdash;"Good faith" collection letter settlement funds disbursement. Non-US - Funds disbursement transactions<br><br> `250`&mdash;Cardholder does not recognize transacton chargeback handling fee.<br><br> `350`&mdash;Pre-arbitration/Pre-compliance settlement funds disbursement<br><br> `401`&mdash;Prepaid load revenue sharing<br><br> `402`&mdash;Non-US - Collection for an unsettled prepaid of original credit authorization<br><br><br>**Note:** This is from the Visa IES spreadsheet. This spreadsheet is updated every 6 months or so. Check periodically with Visa for latest fee reason codes.<br> | enum: ["100", "110", "130", "140", "150", "170", "200", "210", "220", "230", "240", "250", "350", "401", "402"] |
| `Message` | string (schema `FeeMessage`) | yes | Fee message. 70 chars maximum. | maxLength: 70; nullable: true |
| `DestinationBin` | string (schema `DestinationBIN`) | yes | This is the BIN that represents the organization who will receive the Fee Collection/Funds Disbursement.<br><br>**REQUIRED** when use `card_id` and `customer_id`<br> | nullable: true |
| `EventDate` | string (schema `FeeEventDate`) | no | <br>Use this field to pass:<br><br>    - Date the card was recovered (Reason 150)<br>    - Collection letter date (Reason 240)<br>    - Pre-Compliance / Pre-Arbitration Letter Date (Reason 350)<br>    <br>**REQUIRED** when `Reason` is `150`, `240`, or `350` (US domestic); otherwise, it is not valid. <br>    <br>Format = yyyy-mm-dd<br> |  |

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

> API generic returned error.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code. |  |
| `message` | string | no | Error description. |  |
| `http_status_code` | number | no | HTTP status code following RCF-9110 |  |
| `details` | object | no | Payload array returning all fields with problems on request validation. <br><br>These validations can be: <br><br>  * Invalid length <br><br>  * Invalid type <br><br>  * Invalid accepted <br><br><br>Values are explained in the message.<br><br> |  |

<!-- schema: #/components/schemas/VisaFeeResponse -->
### Schema `VisaFeeResponse`

Pointer: `#/components/schemas/VisaFeeResponse`. Type: object (schema `VisaFeeResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `Reason` | string (schema `FeeReasonCode`) | no | Fee reason code.<br><br> `100`&mdash;Telecommunication charges (non-US)<br><br> `110`&mdash;Auto telex charges (non-US)<br><br> `130`&mdash;Lost/stolen card report fees<br><br> `140`&mdash;Merchant service fees<br><br> `150`&mdash;Recovered Visa card, Electron card, or Visa Electron card. Handling fees/rewards. Non-US - Recovered card handling fee<br><br> `170`&mdash;Recovery of retrieval request fees. <br><br> `200`&mdash;Emergency replacement card distribution fee<br><br> `210`&mdash;Emergency cash disbursement handling fee<br><br> `220`&mdash;Arbitration/compliance/resolution case decision or filing fee<br><br> `230`&mdash;Incorrect merchant ID/transacton date handling<br><br> `240`&mdash;"Good faith" collection letter settlement funds disbursement. Non-US - Funds disbursement transactions<br><br> `250`&mdash;Cardholder does not recognize transacton chargeback handling fee.<br><br> `350`&mdash;Pre-arbitration/Pre-compliance settlement funds disbursement<br><br> `401`&mdash;Prepaid load revenue sharing<br><br> `402`&mdash;Non-US - Collection for an unsettled prepaid of original credit authorization<br><br><br>**Note:** This is from the Visa IES spreadsheet. This spreadsheet is updated every 6 months or so. Check periodically with Visa for latest fee reason codes.<br> | enum: ["100", "110", "130", "140", "150", "170", "200", "210", "220", "230", "240", "250", "350", "401", "402"] |
| `Message` | string (schema `FeeMessage`) | no | Fee message. 70 chars maximum. | maxLength: 70; nullable: true |
| `EventDate` | string (schema `FeeEventDate`) | no | <br>Use this field to pass:<br><br>    - Date the card was recovered (Reason 150)<br>    - Collection letter date (Reason 240)<br>    - Pre-Compliance / Pre-Arbitration Letter Date (Reason 350)<br>    <br>**REQUIRED** when `Reason` is `150`, `240`, or `350` (US domestic); otherwise, it is not valid. <br>    <br>Format = yyyy-mm-dd<br> |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `Fees V2`: POST /v2/fee, GET /v2/fee/{fee_id} | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
