---
ku_id: KU-API-card-issuing-disputes--fraud-report
title: 'API reference: Card issuing - Disputes — Fraud report'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- post-v2-fraud-report
- get-v2-fraud-report
- put-v2-fraud-report
- get-v1-fraud-report-logs
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CARD-visa-dispute-use-case
- KU-ERR-codes-acq-to-esma
- KU-EVT-catalogue-other-domains
- KU-EVT-disputes-endpoint-generated-events
specification_version: 1.0.0
---

# API reference: Card issuing - Disputes — Fraud report

**KU ID:** `KU-API-card-issuing-disputes--fraud-report` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Fraud report` in `api-specs/Card_issuing_-_Disputes.yaml` (“Card issuing - Disputes”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to create and manage fraud reports

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v2/fraud-report` | `post-v2-fraud-report` | Create fraud report | no |
| `GET /v2/fraud-report/{fraudReportId}` | `get-v2-fraud-report` | Get fraud report | no |
| `PUT /v2/fraud-report/{fraudReportId}` | `put-v2-fraud-report` | Update fraud report | no |
| `GET /v1/fraud-report/{fraudReportId}/logs` | `get-v1-fraud-report-logs` | List fraud report logs | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=POST path=/v2/fraud-report operationId=post-v2-fraud-report -->
### `POST /v2/fraud-report` — Create fraud report

- **operationId:** `post-v2-fraud-report`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fraud report`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a fraud report.
>
> This endpoint generates a [Fraud report created](https://developers.pismo.io/events/docs/fraud-report-fraud-report-creation-1) event.
>
>  **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Request body

Required: no

> Fraud report data - fill out and enter one card network object.

**Content type `application/json`** — schema: anyOf: object (schema `Fraud_Report_Create_Elo_International`), object (schema `Fraud_Report_Create_Elo_National`), object (schema `Fraud_Report_Create_Mastercard`), object (schema `Fraud_Report_Create_Visa`), object (schema `Fraud_Report_Create_Visa_Card`)

_anyOf option 1: schema `Fraud_Report_Create_Elo_International`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | number (schema `TransactionId`) | yes | Pismo transaction ID. | example: 1234567890 |
| `report_type` | string (schema `ReportTypeEloInternational`) | yes | Fraud report type. <br> | enum: ["elo_international"]; example: "elo_international" |
| `report` | object (schema `ReportEloInternational`) | yes | Elo international report |  |

_anyOf option 2: schema `Fraud_Report_Create_Elo_National`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | number (schema `TransactionId`) | yes | Pismo transaction ID. | example: 1234567890 |
| `report_type` | string (schema `ReportTypeElo`) | yes | Fraud report type. <br> | enum: ["elo"]; example: "elo" |
| `report` | object (schema `ReportEloNational`) | yes | Elo national report |  |

_anyOf option 3: schema `Fraud_Report_Create_Mastercard`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | number (schema `TransactionId`) | yes | Pismo transaction ID. | example: 1234567890 |
| `report_type` | string (schema `ReportTypeMastercard`) | yes | Fraud report type. <br> | enum: ["mastercard"]; example: "mastercard" |
| `report` | object (schema `ReportMastercard`) | yes | Mastercard report |  |

_anyOf option 4: schema `Fraud_Report_Create_Visa`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_id` | number (schema `TransactionId`) | yes | Pismo transaction ID. | example: 1234567890 |
| `report_type` | string (schema `ReportTypeVisa`) | yes | Fraud report type. <br> | enum: ["visa"]; example: "visa" |
| `report` | object (schema `ReportVisa`) | yes | Visa report |  |

_anyOf option 5: schema `Fraud_Report_Create_Visa_Card`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `report_type` | string (schema `ReportTypeVisaCard`) | yes | Fraud report type. <br> | enum: ["visa_card"]; example: "visa_card" |
| `card_id` | number (schema `CardID`) | yes | Pismo card ID. | example: 123456 |
| `customer_id` | number (schema `CustomerId`) | yes | Pismo customer ID. | example: 10203040 |
| `report` | object (schema `ReportVisa`) | yes | Visa report |  |


Example `Create an Elo National Fraud Report from Transaction`:

```json
{
  "report_type": "elo",
  "transaction_id": 1234567890,
  "report": {
    "fraud_type": "10",
    "report_date": "2021-02-11",
    "authorization_origin_indicator": "Y",
    "notification_code": "1",
    "card_service_code": "C",
    "exchange_value": 0,
    "exchange_indicator": "N"
  }
}
```

Example `Create an Elo International Fraud Report from Transaction`:

```json
{
  "report_type": "elo_international",
  "transaction_id": 1234567890,
  "report": {
    "action": "CREATED",
    "primary_reason": "CA",
    "secondary_reason": "BT"
  }
}
```

Example `Create a Mastercard Fraud Report from Transaction`:

```json
{
  "report_type": "mastercard",
  "transaction_id": 1234567890,
  "report": {
    "fraud_type": "00",
    "acct_status": "ACCT_IS_OPEN",
    "chgbk_indicator": "0",
    "cvc_invalid_indicator": "Y",
    "device_type": "1",
    "sub_type": "K"
  }
}
```

Example `Create a Visa Fraud Report from Transaction`:

```json
{
  "report_type": "visa",
  "transaction_id": 1234567890,
  "report": {
    "fraud_type": "1",
    "fraud_type_category": "CARDTXN",
    "notification_cd": 1,
    "close_fraud_case_ind": false
  }
}
```

Example `Create a Visa Fraud Report from Card`:

```json
{
  "report_type": "visa_card",
  "card_id": 102030,
  "customer_id": 10203040,
  "report": {
    "fraud_type": "2",
    "fraud_type_category": "NRI",
    "notification_cd": 1,
    "close_fraud_case_ind": false
  }
}
```

**Content type `application/xml`** — schema: object

_No fields declared in the schema._

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: anyOf: object (schema `Fraud_Report_Create_Response_Elo_International`), object (schema `Fraud_Report_Create_Response_Elo_National`), object (schema `Fraud_Report_Create_Response_Mastercard`), object (schema `Fraud_Report_Create_Response_Visa`), object (schema `Fraud_Report_Create_Response_Visa_Card`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: object (schema `ErrorModel`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 504 | Gateway timeout | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Fraud Report from Elo National Transaction`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Elo",
  "fraud_report_network_id": "82702030405",
  "report": {
    "fraud_type": "10",
    "report_date": "2021-02-11",
    "authorization_origin_indicator": "Y",
    "notification_code": "1",
    "card_service_code": "C",
    "exchange_value": 0,
    "exchange_indicator": "N"
  },
  "created_at": "2024-10-18 11:20:22",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "elo"
}
```

200 Example `Fraud Report from Elo International Transaction`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Elo",
  "report": {
    "action": "CREATED",
    "primary_reason": "CA",
    "secondary_reason": "BT"
  },
  "created_at": "2024-10-18 11:20:22",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "elo_international"
}
```

200 Example `Fraud Report from Mastercard Transaction`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Mastercard",
  "report": {
    "fraud_type": "00",
    "acct_status": "ACCT_IS_OPEN",
    "chgbk_indicator": "0",
    "cvc_invalid_indicator": "Y",
    "device_type": "1",
    "sub_type": "K"
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "mastercard"
}
```

200 Example `Fraud Report from Visa Transaction`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Visa",
  "report": {
    "close_fraud_case_ind": false,
    "fraud_type": "0",
    "fraud_type_category": "CARDTXN",
    "notification_cd": 1
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "visa"
}
```

200 Example `Fraud Report from Visa Card`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Visa",
  "report": {
    "close_fraud_case_ind": false,
    "fraud_type": "2",
    "fraud_type_category": "NRI",
    "notification_cd": 1
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "account_id": 10203040,
  "card_id": 123456,
  "customer_id": 40506070,
  "report_type": "visa_card"
}
```

##### Response 400

400 Example `EDPT0002 - Failed during validation of request payload`:

```json
{
  "code": "EDPT0002",
  "message": "Failed during validation of request payload",
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

404 Example `BDPT0006 - Fraud Report [123] not found`:

```json
{
  "code": "BDPT0006",
  "message": "Fraud Report [123] not found",
  "http_status_code": 404
}
```

##### Response 409

409 Example `BDPT0007 - Fraud Report already created using transaction_id [123]`:

```json
{
  "code": "BDPT0007",
  "message": "Fraud Report already created using transaction_id [123]",
  "http_status_code": 409
}
```

409 Example `BDPT0007 - Fraud Report already created using card_id [12345]`:

```json
{
  "code": "BDPT0007",
  "message": "Fraud Report already created using card_id [12345]",
  "http_status_code": 409
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
        "field": "transaction_id",
        "message": "This is field is required"
      },
      {
        "field": "report_type",
        "message": "This is an invalid value"
      }
    ]
  }
}
```

422 Example `BDPT0002 - Fraud Report cannot be edited while in PENDING status`:

```json
{
  "code": "BDPT0002",
  "message": "Fraud Report cannot be edited while in PENDING status.",
  "http_status_code": 422
}
```

##### Response 500

500 Example `EDPT9999 - Something went wrong, please try again later`:

```json
{
  "code": "EDPT9999",
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
| 400 | `EDPT0002` | Failed during validation of request payload |
| 401 | `EDPT0005` | Missing or invalid Authorization header |
| 404 | `BDPT0006` | Fraud Report [123] not found |
| 409 | `BDPT0007` | Fraud Report already created using transaction_id [123] |
| 422 | `BDPT0001` | Error while validating fields |
| 422 | `BDPT0002` | Fraud Report cannot be edited while in PENDING status. |
| 500 | `EDPT9999` | Something went wrong, please try again later |
| 504 | `EDPT0001` | Request timeout |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `fraud-report-fraud-report-creation-1` | https://developers.pismo.io/events/docs/fraud-report-fraud-report-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;409;422;500;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CARD-visa-dispute-use-case`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v2/fraud-report/{fraudReportId} operationId=get-v2-fraud-report -->
### `GET /v2/fraud-report/{fraudReportId}` — Get fraud report

- **operationId:** `get-v2-fraud-report`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fraud report`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a fraud report.
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `fraudReportId` | path | yes | number | Dispute fraud report ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: anyOf: object (schema `Fraud_Report_Get_Response_Elo_National`), object (schema `Fraud_Report_Get_Response_Elo_International`), object (schema `Fraud_Report_Get_Response_Mastercard`), object (schema `Fraud_Report_Get_Response_Visa`), object (schema `Fraud_Report_Get_Response_Visa_Card`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 504 | Gateway timeout | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Fraud Report from Elo National Transaction with PROCESSED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PROCESSED",
  "network": "Elo",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "fraud_type": "10",
    "report_date": "2021-02-11",
    "authorization_origin_indicator": "Y",
    "notification_code": "1",
    "card_service_code": "C",
    "exchange_value": 0,
    "exchange_indicator": "N"
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "elo"
}
```

200 Example `Fraud Report from Elo National Transaction with FAILED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "FAILED",
  "network": "Elo",
  "report": {
    "fraud_type": "10",
    "report_date": "2021-02-11",
    "authorization_origin_indicator": "Y",
    "notification_code": "1",
    "card_service_code": "C",
    "exchange_value": 0,
    "exchange_indicator": "N"
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "elo",
  "network_response": "The network returned [Error to create Fraud Report, invalid field], reasonCode [E-90000000] with the source [NETWORK_EXCEPTION]."
}
```

200 Example `Fraud Report from Elo International Transaction with PROCESSED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PROCESSED",
  "network": "Elo",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "action": "CREATED",
    "primary_reason": "CA",
    "secondary_reason": "BT"
  },
  "created_at": "2024-10-18 11:20:22",
  "updated_at": "2024-10-18 12:20:22",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "elo_international"
}
```

200 Example `Fraud Report from Elo International Transaction with FAILED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "FAILED",
  "network": "Elo",
  "report": {
    "action": "CREATED",
    "primary_reason": "CA",
    "secondary_reason": "BT"
  },
  "created_at": "2024-10-18 11:20:22",
  "updated_at": "2024-10-18 12:20:22",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "elo_international",
  "network_response": "The network returned [Error to create Fraud Report, invalid field], reasonCode [E-90000000] with the source [NETWORK_EXCEPTION]."
}
```

200 Example `Fraud Report from Mastercard Transaction with PROCESSED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PROCESSED",
  "network": "Mastercard",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "fraud_type": "00",
    "acct_status": "ACCT_IS_OPEN",
    "chgbk_indicator": "0",
    "cvc_invalid_indicator": "Y",
    "device_type": "1",
    "sub_type": "K"
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "mastercard"
}
```

200 Example `Fraud Report from Mastercard Transaction with FAILED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "FAILED",
  "network": "Mastercard",
  "report": {
    "fraud_type": "00",
    "acct_status": "ACCT_IS_OPEN",
    "chgbk_indicator": "0",
    "cvc_invalid_indicator": "Y",
    "device_type": "1",
    "sub_type": "K"
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "mastercard",
  "network_response": "The network returned [Error to create Fraud Report, invalid field], reasonCode [E-90000000] with the source [NETWORK_EXCEPTION]."
}
```

200 Example `Fraud Report from Visa Transaction with PROCESSED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PROCESSED",
  "network": "Visa",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "close_fraud_case_ind": false,
    "fraud_type": "0",
    "fraud_type_category": "CARDTXN",
    "notification_cd": 1
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "visa"
}
```

200 Example `Fraud Report from Visa Transaction with FAILED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "FAILED",
  "network": "Visa",
  "report": {
    "close_fraud_case_ind": false,
    "fraud_type": "0",
    "fraud_type_category": "CARDTXN",
    "notification_cd": 1
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "visa",
  "network_response": "The network returned [Error to create Fraud Report, invalid field], reasonCode [E-90000000] with the source [NETWORK_EXCEPTION]."
}
```

200 Example `Fraud Report from Visa Card with PROCESSED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PROCESSED",
  "network": "Visa",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "close_fraud_case_ind": false,
    "fraud_type": "2",
    "fraud_type_category": "NRI",
    "notification_cd": 1
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "account_id": 10203040,
  "card_id": 123456,
  "customer_id": 40506070,
  "report_type": "visa_card"
}
```

200 Example `Fraud Report from Visa Card with FAILED status`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "FAILED",
  "network": "Visa",
  "report": {
    "close_fraud_case_ind": false,
    "fraud_type": "2",
    "fraud_type_category": "NRI",
    "notification_cd": 1
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "account_id": 10203040,
  "card_id": 123456,
  "customer_id": 40506070,
  "report_type": "visa",
  "network_response": "The network returned [Error to create Fraud Report, invalid field], reasonCode [E-90000000] with the source [NETWORK_EXCEPTION]."
}
```

##### Response 400

400 Example `EDPT0004 - Invalid fraud_report_id param`:

```json
{
  "code": "EDPT0004",
  "message": "Invalid fraud_report_id param",
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

404 Example `BDPT0006 - Fraud Report [123] not found`:

```json
{
  "code": "BDPT0006",
  "message": "Fraud Report [123] not found",
  "http_status_code": 404
}
```

##### Response 500

500 Example `EDPT9999 - Something went wrong, please try again later`:

```json
{
  "code": "EDPT9999",
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
| 400 | `EDPT0004` | Invalid fraud_report_id param |
| 401 | `EDPT0005` | Missing or invalid Authorization header |
| 404 | `BDPT0006` | Fraud Report [123] not found |
| 500 | `EDPT9999` | Something went wrong, please try again later |
| 504 | `EDPT0001` | Request timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500;504`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=PUT path=/v2/fraud-report/{fraudReportId} operationId=put-v2-fraud-report -->
### `PUT /v2/fraud-report/{fraudReportId}` — Update fraud report

- **operationId:** `put-v2-fraud-report`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fraud report`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a fraud report. 
>
> This endpoint generates a [Fraud report updated](https://developers.pismo.io/events/docs/fraud-report-fraud-report-change-1) event.
>
> **Notes:** 
>   * This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.
>   * You can only update a fraud report if its status is not `PENDING`.
>

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `fraudReportId` | path | yes | number | Dispute fraud report ID |  |

#### Request body

Required: yes

> Fraud report data - fill out and enter one card network object.

**Content type `application/json`** — schema: anyOf: object (schema `Fraud_Report_Update_Elo_National`), object (schema `Fraud_Report_Update_Elo_International`), object (schema `Fraud_Report_Update_Mastercard`), object (schema `Fraud_Report_Update_Visa`), object (schema `Fraud_Report_Update_Visa_Card`)

_anyOf option 1: schema `Fraud_Report_Update_Elo_National`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `report_type` | string (schema `ReportTypeElo`) | yes | Fraud report type. <br> | enum: ["elo"]; example: "elo" |
| `report` | object (schema `ReportEloNational`) | yes | Elo national report |  |

_anyOf option 2: schema `Fraud_Report_Update_Elo_International`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `report_type` | string (schema `ReportTypeEloInternational`) | yes | Fraud report type. <br> | enum: ["elo_international"]; example: "elo_international" |
| `report` | object (schema `ReportEloInternational`) | yes | Elo international report |  |

_anyOf option 3: schema `Fraud_Report_Update_Mastercard`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `report_type` | string (schema `ReportTypeMastercard`) | yes | Fraud report type. <br> | enum: ["mastercard"]; example: "mastercard" |
| `report` | object (schema `ReportMastercard`) | yes | Mastercard report |  |

_anyOf option 4: schema `Fraud_Report_Update_Visa`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `report_type` | string (schema `ReportTypeVisa`) | yes | Fraud report type. <br> | enum: ["visa"]; example: "visa" |
| `report` | object (schema `ReportVisa`) | yes | Visa report |  |

_anyOf option 5: schema `Fraud_Report_Update_Visa_Card`_

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `report_type` | string (schema `ReportTypeVisaCard`) | yes | Fraud report type. <br> | enum: ["visa_card"]; example: "visa_card" |
| `report` | object (schema `ReportVisaCard`) | yes | Visa card report |  |


Example `Update an Elo National Fraud Report from Transaction`:

```json
{
  "report_type": "elo",
  "report": {
    "fraud_type": "10",
    "report_date": "2021-02-11",
    "authorization_origin_indicator": "Y",
    "notification_code": "1",
    "card_service_code": "C",
    "exchange_value": 0,
    "exchange_indicator": "N"
  }
}
```

Example `Update an Elo International Fraud Report from Transaction`:

```json
{
  "report_type": "elo_international",
  "report": {
    "action": "UPDATED",
    "primary_reason": "CA",
    "secondary_reason": "BT"
  }
}
```

Example `Update a Mastercard Fraud Report from Transaction`:

```json
{
  "report_type": "mastercard",
  "report": {
    "fraud_type": "00",
    "acct_status": "ACCT_IS_OPEN",
    "chgbk_indicator": "0",
    "cvc_invalid_indicator": "Y",
    "device_type": "1",
    "sub_type": "K"
  }
}
```

Example `Update a Visa Fraud Report from Transaction`:

```json
{
  "report_type": "visa",
  "report": {
    "fraud_type": "1",
    "fraud_type_category": "CARDTXN",
    "notification_cd": 1,
    "close_fraud_case_ind": false
  }
}
```

Example `Update a Visa Fraud Report from Card`:

```json
{
  "report_type": "visa_card",
  "report": {
    "fraud_type": "2",
    "fraud_type_category": "NRI",
    "notification_cd": 1,
    "close_fraud_case_ind": false
  }
}
```

**Content type `application/xml`** — schema: object

_No fields declared in the schema._

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: anyOf: object (schema `Fraud_Report_Update_Response_Elo_National`), object (schema `Fraud_Report_Update_Response_Elo_International`), object (schema `Fraud_Report_Update_Response_Mastercard`), object (schema `Fraud_Report_Update_Response_Visa`), object (schema `Fraud_Report_Update_Response_Visa_Card`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 409 | Conflict | `application/json`: object (schema `ErrorModel`) |
| 422 | Unprocessable entity | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 504 | Gateway timeout | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Fraud Report from Elo National Transaction`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Elo",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "fraud_type": "10",
    "report_date": "2021-02-11",
    "authorization_origin_indicator": "Y",
    "notification_code": "1",
    "card_service_code": "C",
    "exchange_value": 0,
    "exchange_indicator": "N"
  },
  "created_at": "2024-10-18 11:20:22",
  "updated_at": "2024-10-18 12:20:22",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "elo"
}
```

200 Example `Fraud Report from Elo International Transaction`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Elo",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "action": "UPDATED",
    "primary_reason": "CA",
    "secondary_reason": "BT"
  },
  "created_at": "2024-10-18 11:20:22",
  "updated_at": "2024-10-18 12:20:22",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "elo_international"
}
```

200 Example `Fraud Report from Mastercard Transaction`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Mastercard",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "action": "UPDATED",
    "primary_reason": "CA",
    "secondary_reason": "BT"
  },
  "created_at": "2024-10-18 11:20:22",
  "updated_at": "2024-10-18 12:20:22",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "mastercard"
}
```

200 Example `Fraud Report from Visa Transaction`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Visa",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "close_fraud_case_ind": false,
    "fraud_type": "0",
    "fraud_type_category": "CARDTXN",
    "notification_cd": 1
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "network_authorization_id": 1234567890,
  "authorization_code": "F0JR9H",
  "transaction_id": 1234567890,
  "account_id": 10203040,
  "card_id": 123456,
  "report_type": "visa"
}
```

200 Example `Fraud Report from Visa Card`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "status": "PENDING",
  "network": "Visa",
  "fraud_report_network_id": "82702030405",
  "case_number": "30405060",
  "report": {
    "close_fraud_case_ind": false,
    "fraud_type": "2",
    "fraud_type_category": "NRI",
    "notification_cd": 1
  },
  "created_at": "2024-10-18T11:20:22.000Z",
  "updated_at": "2024-10-18T12:20:22.000Z",
  "account_id": 10203040,
  "card_id": 123456,
  "customer_id": 40506070,
  "report_type": "visa_card"
}
```

##### Response 400

400 Example `EDPT0002 - Failed during validation of request payload`:

```json
{
  "code": "EDPT0002",
  "message": "Failed during validation of request payload",
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

404 Example `BDPT0006 - Fraud Report [123] not found`:

```json
{
  "code": "BDPT0006",
  "message": "Fraud Report [123] not found",
  "http_status_code": 404
}
```

##### Response 409

409 Example `BDPT0007 - Fraud Report already created using transaction_id [123]`:

```json
{
  "code": "BDPT0007",
  "message": "Fraud Report already created using transaction_id [123]",
  "http_status_code": 409
}
```

409 Example `BDPT0007 - Fraud Report already created using card_id [12345]`:

```json
{
  "code": "BDPT0007",
  "message": "Fraud Report already created using card_id [12345]",
  "http_status_code": 409
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
        "field": "transaction_id",
        "message": "This field is required"
      },
      {
        "field": "report_type",
        "message": "This is an invalid value"
      }
    ]
  }
}
```

422 Example `BDPT0002 - Fraud Report cannot be edited while in PENDING status`:

```json
{
  "code": "BDPT0002",
  "message": "Fraud Report cannot be edited while in PENDING status.",
  "http_status_code": 422
}
```

##### Response 500

500 Example `EDPT9999 - Something went wrong, please try again later`:

```json
{
  "code": "EDPT9999",
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
| 400 | `EDPT0002` | Failed during validation of request payload |
| 401 | `EDPT0005` | Missing or invalid Authorization header |
| 404 | `BDPT0006` | Fraud Report [123] not found |
| 409 | `BDPT0007` | Fraud Report already created using transaction_id [123] |
| 422 | `BDPT0001` | Error while validating fields |
| 422 | `BDPT0002` | Fraud Report cannot be edited while in PENDING status. |
| 500 | `EDPT9999` | Something went wrong, please try again later |
| 504 | `EDPT0001` | Request timeout |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `fraud-report-fraud-report-change-1` | https://developers.pismo.io/events/docs/fraud-report-fraud-report-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;409;422;500;504`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-disputes-endpoint-generated-events`.

<!-- op: spec=api-specs/Card_issuing_-_Disputes.yaml method=GET path=/v1/fraud-report/{fraudReportId}/logs operationId=get-v1-fraud-report-logs -->
### `GET /v1/fraud-report/{fraudReportId}/logs` — List fraud report logs

- **operationId:** `get-v1-fraud-report-logs`
- **Specification:** `api-specs/Card_issuing_-_Disputes.yaml` (Card issuing - Disputes)
- **Server base URL(s):** `https://sandbox.pismolabs.io/disputes`
- **Tags:** `Fraud report`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve a fraud report's logs. 
>
> **Note:** This endpoint takes an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a <b>401 Unauthorized</b> message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `fraudReportId` | path | yes | number | Dispute fraud report ID |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `FraudReportGetLogs`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |
| 504 | Gateway timeout | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fraud_report_id` | number (schema `FraudReportId`) | no | Pismo fraud report ID. | example: 123 |
| `org_id` | string (schema `OrgId`) | no | Organization/tenant ID. | example: "TN-34778262-f4f0-464d-b4c6-a14exxxxxxxx" |
| `logs` | array of object (schema `FraudReportLogs`) | no |  |  |
| `logs[].fraud_report_log_id` | number (schema `FraudReportLogId`) | no | Pismo fraud report log ID. | example: 456 |
| `logs[].action` | string (schema `Action`) | no | Fraud report action | enum: ["CREATE", "UPDATE"] |
| `logs[].report` | object (schema `ReportVisa`) | no | Visa report |  |
| `logs[].correlation_id` | string (schema `CorrelationId`) | no | The Correlation IDentifier field links related API requests and events | example: "correlation-id" |
| `logs[].created_at` | string (schema `CreatedAt`) | no | Created at datetime, format = yyyy-mm-dd hh:mm:ss" | example: "2024-10-18 11:21:45" |
| `logs[].status` | string (schema `Status`) | no | Fraud report ststus | enum: ["PENDING", "FAILED", "PROCESSED"]; example: "PENDING" |

200 Example `Fraud Report with complete journey of Fraud Report endpoints`:

```json
{
  "fraud_report_id": 1,
  "org_id": "TN-123",
  "logs": [
    {
      "fraud_report_log_id": 1,
      "action": "CREATE",
      "report": {
        "close_fraud_case_ind": false,
        "fraud_type": "1",
        "fraud_type_category": "CARDTXN",
        "notification_cd": 1
      },
      "correlation_id": "correlation-id-1",
      "created_at": "2024-10-18 16:20:21",
      "status": "PENDING"
    },
    {
      "fraud_report_log_id": 2,
      "action": "UPDATE",
      "report": {
        "close_fraud_case_ind": false,
        "fraud_type": "1",
        "fraud_type_category": "CARDTXN",
        "notification_cd": 1
      },
      "correlation_id": "correlation-id-2",
      "created_at": "2024-10-18 16:20:22",
      "status": "FAILED",
      "network_response": "The network returned [Error to create Fraud Report, invalid field], reasonCode [E-90000000] with the source [NETWORK_EXCEPTION]."
    },
    {
      "fraud_report_log_id": 3,
      "action": "UPDATE",
      "report": {
        "close_fraud_case_ind": false,
        "fraud_type": "1",
        "fraud_type_category": "CARDTXN",
        "notification_cd": 1
      },
      "correlation_id": "correlation-id-3",
      "created_at": "2024-10-18 16:20:23",
      "status": "PENDING"
    },
    {
      "fraud_report_log_id": 4,
      "action": "UPDATE",
      "report": {
        "close_fraud_case_ind": false,
        "fraud_type": "1",
        "fraud_type_category": "CARDTXN",
        "notification_cd": 1
      },
      "correlation_id": "correlation-id-4",
      "created_at": "2024-10-18 16:20:24",
      "status": "PROCESSED",
      "fraud_report_network_id": "8070223455",
      "case_number": "5150000024",
      "network_response": null
    }
  ]
}
```

##### Response 400

400 Example `EDPT0004 - Invalid fraud_report_id param`:

```json
{
  "code": "EDPT0004",
  "message": "Invalid fraud_report_id param",
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

404 Example `BDPT0006 - Fraud Report [123] not found`:

```json
{
  "code": "BDPT0006",
  "message": "Fraud Report [123] not found",
  "http_status_code": 404
}
```

##### Response 500

500 Example `EDPT9999 - Something went wrong, please try again later`:

```json
{
  "code": "EDPT9999",
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
| 400 | `EDPT0004` | Invalid fraud_report_id param |
| 401 | `EDPT0005` | Missing or invalid Authorization header |
| 404 | `BDPT0006` | Fraud Report [123] not found |
| 500 | `EDPT9999` | Something went wrong, please try again later |
| 504 | `EDPT0001` | Request timeout |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500;504`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ReportEloInternational -->
### Schema `ReportEloInternational`

Pointer: `#/components/schemas/ReportEloInternational`. Type: object (schema `ReportEloInternational`).

> Elo international report

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `action` | string (schema `EloInternationalAction`) | yes | Elo international action | enum: ["CREATED", "UPDATED", "DELETED"]; example: "CREATED" |
| `primary_reason` | string (schema `EloInternationalPrimaryReason`) | yes | Fraud report reasons:<br><br>`AT`: Account Takeover - The unauthorized use of a card account by any person who gains access to that card account with the intent to defraud the Issuer.<br><br>`CA`: Counterfeit/altered Cards - Any card that is manufactured illegally, stamped, or coded.<br><br>`ED`: Employee Fraud - Any manipulation or misuse of a card account by an employee of the issuer with the intention of defrauding the issuer.<br><br>`FA`: Application fraud - Acquisition of a card account as a result of presenting false or incorrect information with the intention of deceiving and  defrauding an issuer.<br><br>`LS`: Lost/Stolen - Unauthorized use of lost or stolen card, checks, or balance transfer coupons.<br><br>`MS`: Skimmed - Unauthorized use or possession of an account through theft of content of the complete magnetic stripe data of a valid card and duplication on the stripe magnetic from another card.<br><br>`ND`: No device - Unauthorized use of a valid card number to make purchases by mail, telephone, or electronic order.<br><br>`NR`: Non-Receipt - Non-receipt or theft through the card sending process by mail, checks, or balance transfer coupons.<br><br>`OT`: Others - Generally not used. This type of fraud is only used when the fraud activity cannot be classified by the remaining fraud types. **Exception for prepaid only**: This type of fraud must be used to classify the activity determined to be the conversion of unsettled funds.<br><br> | enum: ["AT", "CA", "ED", "FA", "LS", "MS", "ND", "NR", "OT"]; example: "AT" |
| `secondary_reason` | string (schema `EloInternationalSecondaryReason`) | yes | Secondary fraud report reasons.<br><br>`BT`\\* - Balance Transfer Coupon - An unauthorized, completed balance transfer by telephone, at the request of a person claiming to be the Owner.<br><br>`CD` - Card - An altered card.<br><br>`CK`\\* - Verification - Any non-receipt of money access checks or balance transfer. Or changed check(s).<br><br>`FF`\\* - Family Fraud - The information (Name, social security number (SSN), date of birth, etc.) belongs to another person (the victim), who actually knows the individual(fraudster) who committed the fraud, forging his (the victim's) identity. The fraudster may be a household, non-domestic, or a distant family member relative or friend. This is the most common application of fraud.<br><br>`FP` - Forced emission of plastic - Plastics that were sent due to the update platinum, marketing initiative, or any issue outside the usual reissue cycle.<br><br>`IT`\\* - Internet - An unauthorized change of address made via the internet.<br><br>`MI`\\* - Mail - An unauthorized address change request sent via US mail.<br><br>`NA` - Nova Conta - Plastics shipped upon issuance of a new bill.<br><br>`P!`\\* - Telephone - A request for authorization for a change of address, plastics, or checks by a person claiming to be the holder.<br><br>`PN` - Card and PIN - unauthorized cash advances at an ATM for a lost or stolen personal card number and password (PIN).<br><br>`RI` - Card reissuance - Plastics sent automatically to replace those that approaching their expiration date.<br><br>`RT` - Retail - Sales are keyed in commercial establishments where a card is normally necessary and there is no direct evidence that any card was present at the time of sale.<br><br>`ST`\\* - Student - A long format "student" application, usually requested in university campuses.<br><br>`TM`\\* - Telemarketing - A request made over the telephone via an outgoing call from the center or via marketing service.<br><br>`TO`\\* - Take One - Unsolicited Application. This is the most common type of application. Lots of It are sometimes displayed at sales counters.<br><br>`TP` - Telephone - An inbound telephone call to the Customer Service Department to the cardholder, in which the representative, assumed the information provided  by telephone.<br><br>`TR`- Account Transfer - Plastics that were shipped as a result of any type replacement account.<br><br><br>\\* - Can only be used for Credit.<br> | enum: ["BT", "CD", "CK", "FF", "FP", "IT", "MI", "NA", "PI", "PN", "RI", "RT", "ST", "TM", "TO", "TP", "TR"]; example: "BT" |

<!-- schema: #/components/schemas/ReportEloNational -->
### Schema `ReportEloNational`

Pointer: `#/components/schemas/ReportEloNational`. Type: object (schema `ReportEloNational`).

> Elo national report

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fraud_type` | string (schema `EloNationalFraudType`) | yes | Elo national fraud type:<br><br><br>  `00` - Cartão Perdido pelo Portador/ Lost card<br><br>  `01` - Cartão Roubado do Portador/ Stolen card<br><br>  `02` - Cartão extraviado (Portador não recebeu cartão do emissor, porém emissor alega que enviou o cartão)/ Card not received as issued<br><br>  `03` - Falsidade ideológica/ Fraudulent use<br><br>  `04` - Cartão clonado/falsificado/ Cloned card<br><br>  `05` - Transação autorizada sem o envolvimento do portador/invasão da conta/ Fraudulent use of account number<br><br>  `06` - Número do cartão foi usado em transação de marketing direto ou no comércio eletrônico/ Card number was used in a direct marketing or e-commerce transaction.<br><br>  `07` - Fraude Familiar / Friendly fraud<br><br>  `08` - Suspeita de Golpe / Suspected scam<br><br>  `09` - Auto Fraude / Auto fraud<br><br>  `10` - Fraude Interna / Internal fraud<br><br>  `11` - Prilex / Brazilian malware<br><br> | enum: ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11"]; example: "01" |
| `report_date` | string (schema `ReportDate`) | yes | Fraud report date, format = yyyy-mm-dd.<br> | example: "2025-08-11" |
| `authorization_origin_indicator` | string (schema `EloNationalAuthorizationOriginIndicator`) | yes | Authorization origin indicator.<br><br>  `Y` - Issuer authorized<br><br>  `X` - Parameter authorized<br><br>  `N` - Not authorized<br><br> | enum: ["Y", "N", "X"]; example: "Y" |
| `notification_code` | string (schema `EloNationalNotificationCode`) | yes | Notification type code.<br><br>`1` - First notification<br><br>`2` - Notification sent again<br><br>`3` - Change<br><br>`4` - Deletion (cancellation fraud warning)<br><br>`5` = Reactivation<br><br> | enum: ["1", "2", "3", "4", "5"]; example: "1" |
| `card_service_code` | string (schema `EloNationalCardServiceCode`) | yes | Card type:<br><br>  * `C` - Chip<br><br>  * `M` - Stripe<br><br> | enum: ["C", "M"]; example: "C" |
| `exchange_value` | number (schema `EloNationalExchangeValue`) | yes | Exchange value. | format: "double"; example: 9 |
| `exchange_indicator` | string (schema `EloNationalExchangeIndicator`) | yes | Is this an exchange? Default is `N` (no).<br> | enum: ["Y", "N"]; example: "N" |

<!-- schema: #/components/schemas/ReportMastercard -->
### Schema `ReportMastercard`

Pointer: `#/components/schemas/ReportMastercard`. Type: object (schema `ReportMastercard`).

> Mastercard report

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fraud_type` | string (schema `MastercardFraudType`) | yes | <a href="https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-1-fraud-type-codes" target="_blank">Mastercard fraud type</a>.<br> | enum: ["00", "01", "02", "03", "04", "05", "06", "51", "55", "56", "57"]; example: "01" |
| `acct_status` | string (schema `MastercardAcctStatus`) | yes | Mastercard account status | enum: ["ACCT_IS_OPEN", "ACCT_HAS_BEEN_CLOSED"]; example: "ACCT_IS_OPEN" |
| `chgbk_indicator` | string (schema `MastercardChargebackIndicator`) | yes | Mastercard chargeback indicator. true =  `1`, false = `0`. | enum: ["0", "1"]; example: "1" |
| `cvc_invalid_indicator` | string (schema `MastercardCvcInvalidIndicator`) | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-15-card-validation-code-cvc-indicator' target='_blank'>CVC invalid code indicator</a><br> | enum: ["Y", "*", "M", "N", "P", "U", "?", "E"]; example: "Y" |
| `device_type` | string (schema `MastercardDeviceType`) | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-3-account-device-type-codes' target='_blank'>account device type</a>.<br> | enum: ["1", "2", "3", "4", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]; example: "1" |
| `sub_type` | string (schema `MastercardSubType`) | yes | Mastercard <a href='https://developer.mastercard.com/fld-fraud-submission/documentation/parameters/annexure-1/#table-2-fraud-sub-type-codes' target='_blank'>fraud sub type codes</a><br> | enum: ["K", "N", "P", "U", "H", "R", "I", "V", "A"]; example: "K" |

<!-- schema: #/components/schemas/ReportVisa -->
### Schema `ReportVisa`

Pointer: `#/components/schemas/ReportVisa`. Type: object (schema `ReportVisa`).

> Visa report

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fraud_type` | string (schema `VisaFraudType`) | yes | Visa fraud type:<br><br><br>  `0` - Lost<br><br>  `1` - Stolen<br><br>  `2` - Card not received as issued (NRI)<br><br>  `3` - Fraudulent application (cardholder never applied for the card)<br><br>  `4` - Issuer-reported counterfeit<br><br>  `5` - Miscellaneous<br><br>  `6` - Fraudulent use of account number<br><br>  `A` = Incorrect processing<br><br>  `B` = Account or credentials takeover<br><br>  `C` = Merchant misrepresentation<br><br>  `D` = Manipulation of account holder<br><br> | enum: ["0", "1", "2", "3", "4", "5", "6", "A", "B", "C", "D"]; example: "0" |
| `fraud_type_category` | string (schema `VisaFraudTypeCategory`) | yes | Visa fraud type category: <br><br>  `CARDTXN` - Card transaction<br><br>  `NRI` - Not received as issued<br><br> | enum: ["CARDTXN", "NRI"]; default: "CARDTXN"; example: "CARDTXN" |
| `notification_cd` | number (schema `VisaNotificationCd`) | yes | Notification code specifying action performed on the fraud report. Domain values:<br><br>  `1`: Addition<br><br>  `2`: Addition of dup<br><br>  `3`: Change<br><br>  `4`: Delete<br><br>  `5`: Reactivate. No edits restricting values based on the value of existing report in case.<br> |  |
| `close_fraud_case_ind` | boolean (schema `VisaCloseFraudCaseInd`) | yes | Should the case be closed on the Visa's side? Default is `false`.<br> | default: false; example: false |

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

<!-- schema: #/components/schemas/ReportVisaCard -->
### Schema `ReportVisaCard`

Pointer: `#/components/schemas/ReportVisaCard`. Type: object (schema `ReportVisaCard`).

> Visa card report

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fraud_type` | string (schema `VisaFraudType`) | yes | Visa fraud type:<br><br><br>  `0` - Lost<br><br>  `1` - Stolen<br><br>  `2` - Card not received as issued (NRI)<br><br>  `3` - Fraudulent application (cardholder never applied for the card)<br><br>  `4` - Issuer-reported counterfeit<br><br>  `5` - Miscellaneous<br><br>  `6` - Fraudulent use of account number<br><br>  `A` = Incorrect processing<br><br>  `B` = Account or credentials takeover<br><br>  `C` = Merchant misrepresentation<br><br>  `D` = Manipulation of account holder<br><br> | enum: ["0", "1", "2", "3", "4", "5", "6", "A", "B", "C", "D"]; example: "0" |
| `fraud_type_category` | string (schema `VisaFraudTypeCategory`) | yes | Visa fraud type category: <br><br>  `CARDTXN` - Card transaction<br><br>  `NRI` - Not received as issued<br><br> | enum: ["CARDTXN", "NRI"]; default: "CARDTXN"; example: "CARDTXN" |
| `notification_cd` | number (schema `VisaNotificationCd`) | yes | Notification code specifying action performed on the fraud report. Domain values:<br><br>  `1`: Addition<br><br>  `2`: Addition of dup<br><br>  `3`: Change<br><br>  `4`: Delete<br><br>  `5`: Reactivate. No edits restricting values based on the value of existing report in case.<br> |  |
| `close_fraud_case_ind` | boolean (schema `VisaCloseFraudCaseInd`) | yes | Should the case be closed on the Visa's side? Default is `false`.<br> | default: false; example: false |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Disputes.yaml` | tag `Fraud report`: POST /v2/fraud-report, GET /v2/fraud-report/{fraudReportId}, PUT /v2/fraud-report/{fraudReportId}, GET /v1/fraud-report/{fraudReportId}/logs | https://github.com/PismoDevEx/pismo-api-specs | `5c1d5513e1f3a4d1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CARD-visa-dispute-use-case` — Visa dispute use case
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-disputes-endpoint-generated-events` — Card issuing - Disputes
