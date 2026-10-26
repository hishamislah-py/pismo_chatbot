---
ku_id: KU-API-banking-transaction-banking--bulk-settlement
title: 'API reference: Banking - Transaction banking — Bulk settlement'
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
operations:
- post-bulk-settlement
related_kus:
- KU-BANK-calendars-and-holidays
- KU-BANK-dated-transactions
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-wiac-to-wstm
- KU-PAY-file-based-check-processing-and-bulk-settlement
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Bulk settlement

**KU ID:** `KU-API-banking-transaction-banking--bulk-settlement` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Bulk settlement` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Bulk settlement related endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /corporate/v1/bulk-settlement` | `post-bulk-settlement` | Request bulk settlement | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/bulk-settlement operationId=post-bulk-settlement -->
### `POST /corporate/v1/bulk-settlement` — Request bulk settlement

- **operationId:** `post-bulk-settlement`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bulk settlement`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> This endpoint triggers the clearing of future value-dated payments and check-release operations in bulk.<br>
> A future value dated payment is a banking transaction that is scheduled to occur on a future date, such as a prepayment or normal payment. The bank is instructed to send the payment on a specific date, which can be the next day or later. When a payment is scheduled for a future date, the funds remain in the payer's account, continuing to accrue interest until the payment is settled on the scheduled date.
>
> A check release is the process that moves funds from an uncleared or held state into the customer’s available balance. After a check is deposited, some or all of its amount remains pending until a scheduled release. When the check is released, the pending funds are applied, and the account balances are updated so that the amount becomes fully available for use.
>
> <b>NOTE</b>: You can call this endpoint once with the same parameters, per division, settlement date, and operation type. If the process fails, you can retry up to 9 times per division, per business day.

#### Request body

Required: yes

> Bulk settlement request body

**Content type `application/json`** — schema: object (schema `BulkSettlementRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operation_type` | string (schema `OperationType`) | yes | Operation type.<br><br>The maximum number of times you can call the Request bulk settlement endpoint per division per business day is 10, regardless of the operation type. For example, you can retry up to 9 times if the first call fails.<br> | enum: ["future-dated", "check-release"]; example: "check-release" |
| `settlement_date` | string (schema `SettlementDate`) | yes | Future date on which the `float_amount` is settled. Corresponds to the cycle closing date relative to the payment date.<br><br><b>Notes</b>:<br>  - The settlement date is in ISO 8601 format.<br>  - It's similar to the `business_date` attribute for regular payment operations.<br> | format: "date"; example: "2023-03-09" |
| `division_code` | string (schema `DivisionCode2`) | yes | Division code registered in the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint. | maxLength: 36; example: "US" |
| `bulk_id` | string (schema `BulkID`) | yes | Bulk settlement request ID provided by the requester. | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |

Example `Request bulk settlement`:

```json
{
  "operation_type": "check-release",
  "settlement_date": "2024-07-03",
  "bulk_id": "74f8e8df",
  "division_code": "74f8e8df-2c2b-412f-8d35-abdf17d896ec"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted |  |
| 400 | A Bad Request validation error | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 429 | Too many requests | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Errors | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `invalid JSON payload`:

```json
{
  "code": "WSTM0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `bulk id required`:

```json
{
  "code": "WSTM0002",
  "message": "bulk_id is a required field"
}
```

400 Example `bulk id max length`:

```json
{
  "code": "WSTM0002",
  "message": "bulk_id must be a maximum of 60 characters in length"
}
```

400 Example `bulk id invalid characters`:

```json
{
  "code": "WSTM0002",
  "message": "bulk_id contains invalid characters: [characters]"
}
```

400 Example `operation type required`:

```json
{
  "code": "WSTM0002",
  "message": "operation_type is a required field"
}
```

400 Example `operation type invalid`:

```json
{
  "code": "WSTM0002",
  "message": "operation_type must be one of [future-dated check-release]"
}
```

400 Example `settlement date required`:

```json
{
  "code": "WSTM0002",
  "message": "settlement_date is a required field"
}
```

400 Example `settlement date max length`:

```json
{
  "code": "WSTM0002",
  "message": "settlement_date must be a maximum of 10 characters in length"
}
```

400 Example `settlement date wrong format`:

```json
{
  "code": "WSTM0002",
  "message": "settlement_date 07/15/2024 should be formatted as yyyy-mm-dd and be a valid date"
}
```

400 Example `division code required`:

```json
{
  "code": "WSTM0002",
  "message": "division_code is a required field"
}
```

400 Example `division code max length`:

```json
{
  "code": "WSTM0002",
  "message": "division_code must be a maximum of 36 characters in length"
}
```

400 Example `settlement date in the future`:

```json
{
  "code": "WSTM0003",
  "message": "Settlement date cannot be a future date"
}
```

400 Example `settlement date before allowed time`:

```json
{
  "code": "WSTM0004",
  "message": "Current date can be the same as settlement date only after 00:15 in the division's time zone"
}
```

400 Example `division not found`:

```json
{
  "code": "WSTM0005",
  "message": "Division not found"
}
```

400 Example `settlement date invalid`:

```json
{
  "code": "WSTM0006",
  "message": "Settlement date must be a valid date in ISO 8601 format"
}
```

400 Example `Settlement not yet allowed`:

```json
{
  "code": "WSTM0010",
  "message": "Bulk settlement for the current date is allowed only after {hour}:{minute}, according to the division’s time zone"
}
```

400 Example `administrative division is misconfigured`:

```json
{
  "code": "WSTM0011",
  "message": "Administrative division is misconfigured"
}
```

##### Response 409

409 Example `duplicated parameters`:

```json
{
  "code": "WSTM0007",
  "message": "Bulk settlement already posted with parameters division code [division], settlement date [date] and type [type]"
}
```

409 Example `duplicated bulk id`:

```json
{
  "code": "WSTM0009",
  "message": "Bulk id [id] is already in use"
}
```

##### Response 429

429 Example `posts limit`:

```json
{
  "code": "WSTM0008",
  "message": "You cannot post more than 10 daily bulk settlements"
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
| 400 | `WSTM0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WSTM0002` | bulk_id is a required field |
| 400 | `WSTM0003` | Settlement date cannot be a future date |
| 400 | `WSTM0004` | Current date can be the same as settlement date only after 00:15 in the division's time zone |
| 400 | `WSTM0005` | Division not found |
| 400 | `WSTM0006` | Settlement date must be a valid date in ISO 8601 format |
| 400 | `WSTM0010` | Bulk settlement for the current date is allowed only after {hour}:{minute}, according to the division’s time zone |
| 400 | `WSTM0011` | Administrative division is misconfigured |
| 409 | `WSTM0007` | Bulk settlement already posted with parameters division code [division], settlement date [date] and type [type] |
| 409 | `WSTM0009` | Bulk id [id] is already in use |
| 429 | `WSTM0008` | You cannot post more than 10 daily bulk settlements |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;401;403;409;429;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-calendars-and-holidays`, `KU-BANK-dated-transactions`, `KU-PAY-file-based-check-processing-and-bulk-settlement`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Bulk settlement`: POST /corporate/v1/bulk-settlement | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-calendars-and-holidays` — Calendars, holidays and posting transactions on holidays in transaction banking
- `KU-BANK-dated-transactions` — Business-dated and value-dated transactions
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-PAY-file-based-check-processing-and-bulk-settlement` — File-based check processing and bulk settlement
