---
ku_id: KU-API-banking-transaction-banking--check-posting
title: 'API reference: Banking - Transaction banking — Check posting'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Transaction_banking.yaml
  sha256: dec6c4900eb2db35c29c0f0380763da5ae0e1a18c4ad1e293216b2b6effdab56
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
- corporate-post-v1-checks
- corporate-get-v1-checks-id
- post-corporate-v1-checks-release
- post-corporate-v1-checks-checkId-cancel
- corporate-get-v1-check-settlement-operations
related_kus:
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-ERR-codes-wcpt
- KU-ERR-codes-wiac-to-wstm
- KU-EVT-catalogue-other-domains
- KU-EVT-corporate-banking-data-events
- KU-PAY-check-posting-and-settlement
- KU-PAY-file-based-check-processing-and-bulk-settlement
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Check posting

**KU ID:** `KU-API-banking-transaction-banking--check-posting` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Check posting` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Check posting endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /corporate/v1/checks` | `corporate-post-v1-checks` | Create check posting | no |
| `GET /corporate/v1/checks/{checkId}` | `corporate-get-v1-checks-id` | Get check posting | no |
| `POST /corporate/v1/checks/release` | `post-corporate-v1-checks-release` | Release check | no |
| `POST /corporate/v1/checks/{checkId}/cancel` | `post-corporate-v1-checks-checkId-cancel` | Cancel check | no |
| `GET /corporate/v1/checks/{checkId}/settlement-operations` | `corporate-get-v1-check-settlement-operations` | List check settlement operations | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/checks operationId=corporate-post-v1-checks -->
### `POST /corporate/v1/checks` — Create check posting

- **operationId:** `corporate-post-v1-checks`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Check posting`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Allow clients to post a check for a specified external account, with the option to settle the amount either immediately or in the future.
>
> **NOTES**:
>   * This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
>   * This endpoint generates the following events:
>     - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
>     - [Check posting status change](https://developers.pismo.io/events/docs/cash-management-check-status-change-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Request body

Required: yes

> Check posting request body

**Content type `application/json`** — schema: object (schema `CheckPostingRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_id` | string (schema `CheckId`) | yes | Check ID. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |
| `check_amount` | object (schema `CheckAmount`) | yes | Total check amount. |  |
| `settlement_type` | string (schema `CheckSettlementType`) | yes | Indicates when funds become available to the bank: `BEGINNING` or `END`.<br> | enum: ["BEGINNING", "END"]; example: "END" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `description` | string (schema `CheckPostingDescription`) | no | A brief description about a check posting transaction. | maxLength: 100; example: "Check posting" |
| `settlements` | array of object (schema `CheckSettlementRequestItem`) | yes | List of check settlements. Each settlement represents a portion of the check amount to be settled on a specific date, with an associated type and tracking identifier. |  |

Example `Check posting request`:

```json
{
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72",
  "check_amount": {
    "value": 2000,
    "currency": "USD"
  },
  "description": "Check posting",
  "settlement_type": "BEGINNING",
  "business_date": "2025-01-04",
  "settlements": [
    {
      "type": "DEPOSIT",
      "tracking_id": "73cc7fa5-79f1-4b85-9e13-124cc58c651f",
      "settlement_date": "2025-01-05",
      "amount": 100
    },
    {
      "type": "HOLD",
      "tracking_id": "9d7c898e-dd57-4ab4-bfe3-23a48d56851f",
      "settlement_date": "2025-01-10",
      "amount": 800
    },
    {
      "type": "HOLD",
      "tracking_id": "953109dc-e943-454a-95b6-4b15d2c5b31d",
      "settlement_date": "2025-01-20",
      "amount": 900
    },
    {
      "type": "HOLD",
      "tracking_id": "cd593acd-a056-42a1-aec8-3ae14d427a4d",
      "settlement_date": "2025-01-30",
      "amount": 200
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted. Returns the created check posting. | `application/json`: object (schema `CheckPostingResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost |  |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_id` | string (schema `CheckId`) | yes | Check ID. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |

202 Example `Check posting response`:

```json
{
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72"
}
```

##### Response 400

400 Example `Invalid json` (Invalid JSON payload):

```json
{
  "code": "WCPT0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `check_id required` (check_id is a required field):

```json
{
  "message": "check_id is a required field",
  "code": "WCPT0002"
}
```

400 Example `check_id max` (check_id exceeds maximum length):

```json
{
  "message": "check_id must be a maximum of 60 characters in length",
  "code": "WCPT0002"
}
```

400 Example `settlements.tracking_id required` (tracking_id is a required field):

```json
{
  "message": "tracking_id is a required field",
  "code": "WCPT0002"
}
```

400 Example `settlements.tracking_id max` (tracking_id exceeds maximum length):

```json
{
  "message": "tracking_id must be a maximum of 43 characters in length",
  "code": "WCPT0002"
}
```

400 Example `check_amount required` (check_amount is a required field):

```json
{
  "message": "check_amount is a required field",
  "code": "WCPT0002"
}
```

400 Example `check_amount.value decimalGt` (value must be greater than 0):

```json
{
  "message": "value must be greater than 0",
  "code": "WCPT0002"
}
```

400 Example `check_amount.value decimalMax` (value exceeds the maximum allowed):

```json
{
  "message": "value must be 100,000,000,000,000,000 or less",
  "code": "WCPT0002"
}
```

400 Example `check_amount.value must match settlement values` (check_amount.value must be equal to the total sum of all settlement amounts):

```json
{
  "message": "check_amount.value must be equal to the total sum of all settlement amounts",
  "code": "WCPT0002"
}
```

400 Example `decimal places not compatible with currency` (decimal places is not compatible with the specified currency):

```json
{
  "message": "The number of decimal places is not compatible with the specified currency",
  "code": "WCPT0002"
}
```

400 Example `currency iso4217` (currency must be a valid ISO 4217 code):

```json
{
  "message": "currency: invalid currency code",
  "code": "WCPT0002"
}
```

400 Example `description max` (description exceeds maximum length):

```json
{
  "message": "description must be a maximum of 100 characters in length",
  "code": "WCPT0002"
}
```

400 Example `settlement_type required` (settlement_type is a required field):

```json
{
  "message": "settlement_type is a required field",
  "code": "WCPT0002"
}
```

400 Example `settlement_type oneof` (settlement_type must be BEGINNING or END):

```json
{
  "message": "settlement_type must be one of [BEGINNING END]",
  "code": "WCPT0002"
}
```

400 Example `settlement_type BEGINNING with invalid settlements` (settlement_type BEGINNING must contain settlements of type DEPOSIT or HOLD):

```json
{
  "message": "settlement_type BEGINNING must contain up to one settlement of type DEPOSIT and up to three settlements of type HOLD",
  "code": "WCPT0002"
}
```

400 Example `settlement_type END with invalid settlements` (settlement_type END must contain settlement of type PENDING):

```json
{
  "message": "settlement_type END must contain only one settlement of type PENDING",
  "code": "WCPT0002"
}
```

400 Example `settlements.settlement_date required` (settlement_date is a required field):

```json
{
  "message": "settlement_date is a required field",
  "code": "WCPT0002"
}
```

400 Example `settlements.settlement_date max` (settlement_date exceeds maximum length):

```json
{
  "message": "settlement_date must be a maximum of 10 characters in length",
  "code": "WCPT0002"
}
```

400 Example `settlements.settlement_date dateOnly` (settlement_date must be a valid date (yyyy-mm-dd)):

```json
{
  "message": "settlement_date [date] should be formatted as yyyy-mm-dd and be a valid date",
  "code": "WCPT0002"
}
```

400 Example `settlements.settlement_date must be future` (settlements.settlement_date must be in the future when settlements.type is HOLD or PENDING):

```json
{
  "message": "settlements.settlement_date must be in the future when settlements.type is HOLD or PENDING",
  "code": "WCPT0002"
}
```

400 Example `settlements.settlement_date must be today` (settlement_date must be today when settlements.type is DEPOSIT):

```json
{
  "message": "settlement_date must be today when settlements.type is DEPOSIT",
  "code": "WCPT0002"
}
```

400 Example `settlements.settlement_date exceeded` (Settlement date exceeds allowed range):

```json
{
  "message": "settlements.settlement_date cannot surpass current_business_date by more than 30 calendar days when settlements.type is PENDING",
  "code": "WCPT0002"
}
```

400 Example `settlements.settlement_date must be unique` (settlements.settlement_date must be unique):

```json
{
  "message": "settlements.settlement_date must be unique",
  "code": "WCMN0002"
}
```

400 Example `settlements.settlement_date cannot be before business_date` (settlements.settlement_date cannot be before the business_date):

```json
{
  "message": "settlements.settlement_date cannot be before the business_date",
  "code": "WCMN0002"
}
```

400 Example `settlements.type oneof` (type must be DEPOSIT, PENDING, or HOLD):

```json
{
  "message": "type must be one of [DEPOSIT HOLD PENDING]",
  "code": "WCPT0002"
}
```

400 Example `settlements.tracking_id must be unique"`:

```json
{
  "code": "WCPT0002",
  "message": "settlements.tracking_id must be unique"
}
```

400 Example `Holiday` (Posting on a holiday):

```json
{
  "code": "WCPT0006",
  "message": "Cannot post checks on holiday"
}
```

400 Example `Weekend` (Posting on a weekend):

```json
{
  "code": "WCPT0007",
  "message": "Cannot post checks on a weekend"
}
```

400 Example `Invalid BusinessDate` (Invalid business date):

```json
{
  "code": "WCPT0008",
  "message": "Invalid business date for the current business day cycle"
}
```

400 Example `Invalid Processing Code` (Invalid check processing code):

```json
{
  "code": "WCPT0010",
  "message": "Invalid check processing code"
}
```

400 Example `Invalid Check Status` (Invalid check status):

```json
{
  "code": "WCPT0011",
  "message": "Check status is invalid for this operation"
}
```

400 Example `Corporate Account Not Found` (Corporate account not found):

```json
{
  "code": "WCPT0004",
  "message": "Corporate account not found"
}
```

400 Example `Account Onboarding Not Finished` (Account has not finished onboarding):

```json
{
  "code": "WCPT0018",
  "message": "Account has not finished onboarding"
}
```

400 Example `Account Closed` (Account is closed):

```json
{
  "code": "WCPT0009",
  "message": "Action not permitted on a closed account"
}
```

400 Example `Credit Not Active` (Account credit not active):

```json
{
  "code": "WCPT0012",
  "message": "The account cannot be credited. Credit function is not active"
}
```

400 Example `Invalid account currency code` (Invalid account currency code):

```json
{
  "code": "WCPT0014",
  "message": "Invalid account currency code: 999"
}
```

400 Example `Business date before account creation date` (Business date before account creation date):

```json
{
  "code": "WCPT0016",
  "message": "The payment date cannot be earlier than the account creation date"
}
```

400 Example `Business date before account migration date` (Business date before account migration date):

```json
{
  "code": "WCPT0017",
  "message": "The payment date cannot be earlier than the account migration date"
}
```

##### Response 401

401 Example `Unauthorized account`:

```json
{
  "code": "WCAC0001",
  "message": "Account not authorized"
}
```

##### Response 409

409 Example `CheckIdExists` (Check ID already exists):

```json
{
  "code": "WCPT0005",
  "message": "check_id [...] is already in use",
  "data": {
    "check_id": "e219459f-9a7e-48ec-9c2b-1a40a62d5ca3",
    "tracking_id": "e219459f-9a7e-48ec-9c2b-1a40a62d5ca3",
    "status": "UNCLEARED"
  }
}
```

409 Example `TrackingIdExists` (Tracking ID already exists):

```json
{
  "code": "WCPT0013",
  "message": "tracking_id [...] is already in use"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCPT0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WCPT0002` | check_id is a required field |
| 400 | `WCMN0002` | settlements.settlement_date must be unique |
| 400 | `WCPT0006` | Cannot post checks on holiday |
| 400 | `WCPT0007` | Cannot post checks on a weekend |
| 400 | `WCPT0008` | Invalid business date for the current business day cycle |
| 400 | `WCPT0010` | Invalid check processing code |
| 400 | `WCPT0011` | Check status is invalid for this operation |
| 400 | `WCPT0004` | Corporate account not found |
| 400 | `WCPT0018` | Account has not finished onboarding |
| 400 | `WCPT0009` | Action not permitted on a closed account |
| 400 | `WCPT0012` | The account cannot be credited. Credit function is not active |
| 400 | `WCPT0014` | Invalid account currency code: 999 |
| 400 | `WCPT0016` | The payment date cannot be earlier than the account creation date |
| 400 | `WCPT0017` | The payment date cannot be earlier than the account migration date |
| 401 | `WCAC0001` | Account not authorized |
| 409 | `WCPT0005` | check_id [...] is already in use |
| 409 | `WCPT0013` | tracking_id [...] is already in use |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cash-management-check-status-change-1` | https://developers.pismo.io/events/docs/cash-management-check-status-change-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;409;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-corporate-banking-data-events`, `KU-PAY-check-posting-and-settlement`, `KU-PAY-file-based-check-processing-and-bulk-settlement`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/checks/{checkId} operationId=corporate-get-v1-checks-id -->
### `GET /corporate/v1/checks/{checkId}` — Get check posting

- **operationId:** `corporate-get-v1-checks-id`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Check posting`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get information about a posted check using its check ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `checkId` | path | yes | string | Check ID | example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `CheckPosting`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Account ID | format: "int64"; example: 1234 |
| `external_account_id` | string (schema `CheckPostingExternalAccountId`) | yes | Account external ID to which the check is posted. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "6b6e32c3-6f67-453e-8221-bafa8993e113" |
| `check_id` | string (schema `CheckId`) | yes | Check ID. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |
| `check_amount` | object (schema `CheckAmount`) | yes | Total check amount. |  |
| `description` | string (schema `CheckPostingDescription`) | no | A brief description about a check posting transaction. | maxLength: 100; example: "Check posting" |
| `settlement_type` | string (schema `CheckSettlementType`) | yes | Indicates when funds become available to the bank: `BEGINNING` or `END`.<br> | enum: ["BEGINNING", "END"]; example: "END" |
| `status` | string (schema `CheckPostingStatus`) | yes | Check posting status. | enum: ["PENDING", "CREATING", "UNCLEARED", "SETTLING", "PARTIALLY_SETTLED", "SETTLED", "CANCELING", "CANCELED", "PAYMENT_FAILED", "RELEASE_FAILED", "CANCEL_FAILED"]; example: "SETTLED" |
| `available_amount` | number (schema `CheckAvailableAmount`) | yes | Available check amount. | format: "float"; minimum: 0; example: 2000 |
| `uncleared_amount` | number (schema `CheckUnclearedAmount`) | yes | Uncleared check amount. | format: "float"; minimum: 0; example: 0 |
| `held_amount` | number (schema `CheckHeldAmount`) | yes | Held check amount. | format: "float"; minimum: 0; example: 0 |
| `settlements` | array of object (schema `CheckSettlementItem`) | yes |  |  |

200 Example `example`:

```json
{
  "check_id": "b6d31f8f-c908-4d38-b433-c91160e9e11e",
  "account_id": 320669726,
  "external_account_id": "f7846df4-6208-41df-a94d-b966efdd4989",
  "check_amount": {
    "value": 2000,
    "currency": "USD"
  },
  "description": "Check posting",
  "settlement_type": "BEGINNING",
  "status": "PARTIALLY_SETTLED",
  "available_amount": 1800,
  "uncleared_amount": 0,
  "held_amount": 200,
  "settlements": [
    {
      "settlement_id": "59f27b4a-3f23-42ec-9870-762cb65ea6fb",
      "type": "DEPOSIT",
      "amount": 800,
      "settlement_date": "2025-12-22",
      "status": "SETTLED"
    },
    {
      "settlement_id": "ea77559f-5c54-4615-a8dd-ca129d1df301",
      "type": "HOLD",
      "amount": 1000,
      "settlement_date": "2026-01-26",
      "status": "SETTLED"
    },
    {
      "settlement_id": "82a2b73f-cb50-4bfe-8fe5-cdc94f146f33",
      "type": "HOLD",
      "amount": 200,
      "settlement_date": "2026-01-27",
      "status": "UNSETTLED"
    }
  ]
}
```

##### Response 404

404 Example `CheckPosting Not Found` (Check posting not found):

```json
{
  "code": "WCPT0003",
  "message": "Check posting not found"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 404 | `WCPT0003` | Check posting not found |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/checks/release operationId=post-corporate-v1-checks-release -->
### `POST /corporate/v1/checks/release` — Release check

- **operationId:** `post-corporate-v1-checks-release`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Check posting`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Releases a check using the provided payload.
>
> **NOTES**:
> - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
>
> This endpoint generates the following events:
>   - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
>   - [Check posting status change](https://developers.pismo.io/events/docs/cash-management-check-status-change-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `CheckReleaseRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_id` | string (schema `CheckId`) | yes | Check ID. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |
| `tracking_id` | string (schema `CheckReleaseTrackingId`) | no | Tracking ID associated with the check release transaction. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 43; example: "1624db2e-ee81-4294-bc5e-c753b2cc5eb9" |
| `settlement_date` | string (schema `CheckReleaseDate`) | no | The settlement date defined in the settlement to be released.<br><br><b>Notes</b>:<br>- The settlement date must follow the ISO 8601 format (`yyyy-mm-dd`).<br>- If you don't specify a date, the full check amount is released.<br>- If provided, it must match the settlement date of one of the check's settlements. | format: "date"; example: "2025-01-06" |

Example `example`:

```json
{
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72",
  "tracking_id": "1624db2e-ee81-4294-bc5e-c753b2cc5eb9",
  "settlement_date": "2025-01-06"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Check release accepted | `application/json`: object (schema `CheckReleaseResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_id` | string (schema `CheckId`) | yes | Check ID. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |

202 Example `example`:

```json
{
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72"
}
```

##### Response 400

400 Example `invalid json` (Invalid JSON payload):

```json
{
  "code": "WCPT0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `check_id required` (check_id is a required field):

```json
{
  "message": "check_id is a required field",
  "code": "WCPT0002"
}
```

400 Example `check_id max` (check_id exceeds maximum length):

```json
{
  "message": "check_id must be a maximum of 60 characters in length",
  "code": "WCPT0002"
}
```

400 Example `tracking_id required` (tracking_id is a required field):

```json
{
  "message": "tracking_id is a required field",
  "code": "WCPT0002"
}
```

400 Example `tracking_id max` (tracking_id exceeds maximum length):

```json
{
  "message": "tracking_id must be a maximum of 43 characters in length",
  "code": "WCPT0002"
}
```

400 Example `settlement_date max` (settlement date exceeds maximum length):

```json
{
  "message": "settlement_date must be a maximum of 10 characters in length",
  "code": "WCPT0002"
}
```

400 Example `settlement_date invalid format` (settlement_date must be a valid date in yyyy-mm-dd format):

```json
{
  "message": "settlement_date [settlement_date] should be formatted as yyyy-mm-dd and be a valid date",
  "code": "WCPT0002"
}
```

400 Example `settlement_date mandatory when trackingId provided` (settlement_date is mandatory when tracking_id is provided):

```json
{
  "code": "WCPT0002",
  "message": "settlement_date is mandatory when tracking_id is provided"
}
```

400 Example `Corporate Account Not Found` (Corporate account not found):

```json
{
  "code": "WCPT0004",
  "message": "Corporate account not found"
}
```

400 Example `Account Onboarding Not Finished` (Account has not finished onboarding):

```json
{
  "code": "WCPT0018",
  "message": "Account has not finished onboarding"
}
```

400 Example `operations blocked` (Operations blocked):

```json
{
  "message": "Operations blocked for account",
  "code": "WOBK0007"
}
```

400 Example `invalid check status` (Invalid check status):

```json
{
  "code": "WCPT0011",
  "message": "Check status is invalid for this operation"
}
```

400 Example `no releasable settlements found` (No releasable settlements found):

```json
{
  "message": "No releasable settlements found",
  "code": "WCPT0015"
}
```

##### Response 404

404 Example `CheckPostingNotFound` (Check posting not found):

```json
{
  "code": "WCPT0003",
  "message": "Check posting not found"
}
```

##### Response 409

409 Example `TrackingIdExists` (Tracking ID already exists):

```json
{
  "code": "WCPT0013",
  "message": "tracking_id [...] is already in use"
}
```

409 Example `VersionConflict` (Check posting was concurrently modified):

```json
{
  "code": "WCPT0019",
  "message": "Check posting was concurrently modified"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCPT0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WCPT0002` | check_id is a required field |
| 400 | `WCPT0004` | Corporate account not found |
| 400 | `WCPT0018` | Account has not finished onboarding |
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WCPT0011` | Check status is invalid for this operation |
| 400 | `WCPT0015` | No releasable settlements found |
| 404 | `WCPT0003` | Check posting not found |
| 409 | `WCPT0013` | tracking_id [...] is already in use |
| 409 | `WCPT0019` | Check posting was concurrently modified |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cash-management-check-status-change-1` | https://developers.pismo.io/events/docs/cash-management-check-status-change-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;409;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-corporate-banking-data-events`, `KU-PAY-check-posting-and-settlement`, `KU-PAY-file-based-check-processing-and-bulk-settlement`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/checks/{checkId}/cancel operationId=post-corporate-v1-checks-checkId-cancel -->
### `POST /corporate/v1/checks/{checkId}/cancel` — Cancel check

- **operationId:** `post-corporate-v1-checks-checkId-cancel`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Check posting`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel a check using the provided check ID.
>
> **NOTES**:
> - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
>
> This endpoint generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Check posting status change](https://developers.pismo.io/events/docs/cash-management-check-status-change-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `checkId` | path | yes | string | Check ID | example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Check cancel accepted | `application/json`: object (schema `CheckCancelResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Check posting not found | `application/json`: object |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_id` | string (schema `CheckId`) | yes | Check ID. | pattern: "^[a-zA-Z0-9-]+$"; minLength: 1; maxLength: 60; example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |

202 Example `example`:

```json
{
  "check_id": "c462b2f3-55cc-42b4-ae9a-7614df3e8e72"
}
```

##### Response 400

400 Example `check_id max` (check_id exceeds maximum length):

```json
{
  "message": "check_id must be a maximum of 60 characters in length",
  "code": "WCPT0002"
}
```

400 Example `Corporate Account Not Found` (Corporate account not found):

```json
{
  "code": "WCPT0004",
  "message": "Corporate account not found"
}
```

400 Example `Account Onboarding Not Finished` (Account has not finished onboarding):

```json
{
  "code": "WCPT0018",
  "message": "Account has not finished onboarding"
}
```

400 Example `Operations Blocked` (Operations blocked):

```json
{
  "message": "Operations blocked for account",
  "code": "WOBK0007"
}
```

400 Example `Invalid Check Status` (Invalid check status):

```json
{
  "message": "Check status is invalid for this operation",
  "code": "WCPT0011"
}
```

##### Response 404

404 Example `example`:

```json
{
  "message": "Check posting not found",
  "code": "WCPT0003"
}
```

##### Response 409

409 Example `TrackingIdExists` (Tracking ID already exists):

```json
{
  "code": "WCPT0013",
  "message": "Tracking ID already exists for another operation"
}
```

409 Example `VersionConflict` (Check posting was concurrently modified):

```json
{
  "code": "WCPT0019",
  "message": "Check posting was concurrently modified"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCPT0002` | check_id must be a maximum of 60 characters in length |
| 400 | `WCPT0004` | Corporate account not found |
| 400 | `WCPT0018` | Account has not finished onboarding |
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WCPT0011` | Check status is invalid for this operation |
| 404 | `WCPT0003` | Check posting not found |
| 409 | `WCPT0013` | Tracking ID already exists for another operation |
| 409 | `WCPT0019` | Check posting was concurrently modified |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `cash-management-check-status-change-1` | https://developers.pismo.io/events/docs/cash-management-check-status-change-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;404;409;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-EVT-corporate-banking-data-events`, `KU-PAY-check-posting-and-settlement`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/checks/{checkId}/settlement-operations operationId=corporate-get-v1-check-settlement-operations -->
### `GET /corporate/v1/checks/{checkId}/settlement-operations` — List check settlement operations

- **operationId:** `corporate-get-v1-check-settlement-operations`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Check posting`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieve a paginated list of settlement operations for a specific check.
>
> **NOTES**:
> - Requires an account token (access token encoded with a Pismo account ID). Tokens may expire quickly, resulting in a `401 Unauthorized` response.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `checkId` | path | yes | string | Check ID | example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |
| `settlementId` | query | no | string | Filter by settlement ID. |  |
| `limit` | query | no | integer | Maximum number of items to return. | default: 100; minimum: 1; maximum: 100 |
| `offset` | query | no | integer | Number of items to skip before starting to collect the result set. | default: 0; minimum: 0 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Successful response with a list of settlement operations. | `application/json`: object (schema `GetSettlementOperationsResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Check posting not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operations` | array of object (schema `CheckSettlementOperation`) | yes | List of check settlement operations |  |
| `limit` | integer | yes | Maximum number of items returned. | format: "int32" |
| `offset` | integer | yes | Offset of the first item in the result set | format: "int32" |
| `has_next` | boolean | yes | Indicates whether there are more items available after this page. |  |

200 Example `example`:

```json
{
  "operations": [
    {
      "settlement_id": "abc123",
      "tracking_id": "track-001",
      "amount": 1000,
      "type": "BEGINNING",
      "business_date": "2025-01-05",
      "created_at": "2025-01-05T10:00:00Z"
    }
  ],
  "limit": 10,
  "offset": 0,
  "has_next": false
}
```

##### Response 400

400 Example `example`:

```json
{
  "code": "WCPT0002",
  "message": "Invalid request parameters"
}
```

##### Response 404

404 Example `example`:

```json
{
  "code": "WCPT0003",
  "message": "Check posting not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCPT0002` | Invalid request parameters |
| 404 | `WCPT0003` | Check posting not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/CheckAmount -->
### Schema `CheckAmount`

Pointer: `#/components/schemas/CheckAmount`. Type: object (schema `CheckAmount`).

> Total check amount.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `value` | number (schema `AmountValue`) | yes | Amount value | format: "float"; minimum: 0; maximum: 100000000000000000; example: 1000.52 |
| `currency` | string (schema `Currency`) | no | 3-letter code in ISO 4217-compliant format for the currency used in the transaction. | minLength: 3; maxLength: 3; example: "USD" |

<!-- schema: #/components/schemas/CheckSettlementRequestItem -->
### Schema `CheckSettlementRequestItem`

Pointer: `#/components/schemas/CheckSettlementRequestItem`. Type: object (schema `CheckSettlementRequestItem`).

> Check settlement item representing a portion of the check amount to be settled on a specific date.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `SettlementType`) | yes | Settlement type. Indicates the nature of the settlement. | enum: ["DEPOSIT", "PENDING", "HOLD"]; example: "HOLD" |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `settlement_date` | string (schema `CheckSettlementDate`) | yes | Settlement date in ISO 8601 format (yyyy-mm-dd). | format: "date"; example: "2025-01-06" |
| `amount` | number (schema `CheckSettlementAmount`) | yes | Amount to be settled in the specified operation. | format: "decimal"; example: 100 |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/CheckSettlementItem -->
### Schema `CheckSettlementItem`

Pointer: `#/components/schemas/CheckSettlementItem`. Type: object (schema `CheckSettlementItem`).

> Check settlement item.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `settlement_id` | string (schema `CheckSettlementID`) | yes | Check Settlement ID. | pattern: "^[a-zA-Z0-9-]+$"; example: "c462b2f3-55cc-42b4-ae9a-7614df3e8e72" |
| `type` | string (schema `SettlementType`) | yes | Settlement type. Indicates the nature of the settlement. | enum: ["DEPOSIT", "PENDING", "HOLD"]; example: "HOLD" |
| `amount` | number (schema `CheckSettlementAmount`) | yes | Amount to be settled in the specified operation. | format: "decimal"; example: 100 |
| `settlement_date` | string (schema `CheckSettlementDate`) | yes | Settlement date in ISO 8601 format (yyyy-mm-dd). | format: "date"; example: "2025-01-06" |
| `status` | string (schema `CheckSettlementStatus`) | yes | Check settlement status. | enum: ["CREATING", "UNSETTLED", "SETTLED", "PAYMENT_FAILED", "PAYMENT_ROLLING_BACK", "PAYMENT_ROLL_BACK_FAILED", "PAYMENT_ROLLED_BACK", "SETTLING", "RELEASE_FAILED", "RELEASE_ROLLING_BACK", "RELEASE_ROLLED_BACK", "RELEASE_ROLLBACK_FAILED", "CANCELING", "CANCELED", "CANCEL_FAILED"]; example: "SETTLED" |

<!-- schema: #/components/schemas/CheckSettlementOperation -->
### Schema `CheckSettlementOperation`

Pointer: `#/components/schemas/CheckSettlementOperation`. Type: object (schema `CheckSettlementOperation`).

> Check settlement details

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Check settlement amount | format: "float" |
| `business_date` | string | yes | Check settlement business date (yyyy-mm-dd) | format: "date" |
| `created_at` | string | yes | Timestamp indicating when the operation was created (RFC3339) | format: "date-time" |
| `settlement_id` | string | yes | Check settlement ID |  |
| `tracking_id` | string | yes | ID used to track check settlement operation |  |
| `type` | string | yes | Settlement operation type |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Check posting`: POST /corporate/v1/checks, GET /corporate/v1/checks/{checkId}, POST /corporate/v1/checks/release, POST /corporate/v1/checks/{checkId}/cancel, GET /corporate/v1/checks/{checkId}/settlement-operations | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-ERR-codes-wcpt` — Error codes: WCPT
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-PAY-check-posting-and-settlement` — Check posting and settlement
- `KU-PAY-file-based-check-processing-and-bulk-settlement` — File-based check processing and bulk settlement
