---
ku_id: KU-API-banking-transaction-banking--earmarking-external-accounts
title: 'API reference: Banking - Transaction banking — Earmarking (external accounts)'
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
- post-corporate-v2-earmarks
- patch-corporate-v2-earmarks-earmarkid
- post-corporate-v2-earmarks-earmarkid-cancel
- get-corporate-earmarks
- find-corporate-earmark
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-earmarks
- KU-BANK-get-started-demand-deposit-accounts
- KU-BANK-transaction-banking-accounts
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-ERR-codes-weam
- KU-ERR-codes-wiac-to-wstm
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-EVT-corporate-banking-data-events
- KU-PAY-payment-overview-and-instant-payments
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Earmarking (external accounts)

**KU ID:** `KU-API-banking-transaction-banking--earmarking-external-accounts` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Earmarking (external accounts)` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Earmarking endpoints supporting external accounts

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /corporate/v2/earmarks` | `post-corporate-v2-earmarks` | Create earmark | no |
| `PATCH /corporate/v2/earmarks/{earmarkId}` | `patch-corporate-v2-earmarks-earmarkid` | Update earmark | no |
| `POST /corporate/v2/earmarks/{earmarkId}/cancel` | `post-corporate-v2-earmarks-earmarkid-cancel` | Cancel earmark | no |
| `GET /corporate/v1/earmarks` | `get-corporate-earmarks` | List earmarks | no |
| `GET /corporate/v1/earmarks/{earmarkId}` | `find-corporate-earmark` | Get earmark | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/earmarks operationId=post-corporate-v2-earmarks -->
### `POST /corporate/v2/earmarks` — Create earmark

- **operationId:** `post-corporate-v2-earmarks`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Earmarking (external accounts)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an earmark.
> An account holder can use an earmark to hold needed funds in reserve until a specified release date and time.
>
> Optionally, the account holder can schedule a payout for the release date and time. At that time, an automatic process releases the earmarked funds and settles the payout.
>
> It's possible to force the creation of an earmark by not performing any regular validations, such as account status, account balance, or flex controls validations.
>
> This endpoint generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
> - [Account balance changed (Availables)](https://developers.pismo.io/events/docs/availables-change-available-1)
> - [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)
> - [Earmark created, updated, or canceled](https://developers.pismo.io/events/docs/corporate-earmark-1) with `CREATED` action.
>
> **NOTES**:
>   - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: oneOf: (type not declared), (type not declared) (schema `CreateEarmarkRequestV2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `EarmarkAmount`) | yes | Earmark amount<br><br>`minimum: 0.01`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0.01; maximum: 18446744073709552000; example: 50 |
| `internal_operation` | object (schema `InternalOperation2`) | yes | Data used in transactions executed internally during the request. |  |
| `external_account_id` | string (schema `ExternalAccountIdForEarmark`) | no | External ID of the account on which the earmark is created.<br>Should be the same `external_account_id` that was used to log in.<br>Should be the same `external_account_id` used in [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `earmark_id` | string (schema `EarmarkIdCreation`) | no | Optional earmark ID. If `earmark_id` already exists, the caller receives a 409 error.<br>If provided, the earmark is created with this ID.<br>If not provided, a random earmark ID is generated.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "da85b309-a7f7-4316-b2ad-f069f0838058" |
| `description` | string (schema `EarmarkDescription`) | no | Earmark description | minLength: 1; maxLength: 40 |
| `release_datetime` | string (schema `EarmarkReleaseDatetime`) | no | RFC 3339 date/time for earmark release.<br>Used to schedule a cash-out (usually a payment) at the specified release date and time.<br>At `release_datetime`, an automatic process releases the earmarked funds and settles the cash-out.<br>If no `release_datetime` is set, the earmarked amount is held indefinitely until the customer cancels the earmark.<br> | format: "date-time"; minLength: 20; maxLength: 30; example: "2022-02-10T15:00:00Z" |
| `force_post` | boolean (schema `EarmarkForcePost`) | no | If the account has any reason-based force debit payment restrictions, and the force earmark creation violates any of those restrictions, it fails. The reasons that restrict force debit operations are:<br>  - `CREDIT ONLY`: No force debit allowed<br>  - `ANY`: No force allowed<br>  - `MANUAL`: No force allowed<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `EarmarkResponse`) |
| 400 | A Bad Request validation error. | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized operation. | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost |  |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `earmark_id` | string (schema `EarmarkIdReturned`) | no | Earmark ID. Used as the primary key for query and update operations. It has the same value as the tracking ID, if one is provided. Generated by [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks). | example: "da85b309-a7f7-4316-b2ad-f069f0838058" |
| `account_id` | integer (schema `AccountID3`) | no | Account ID generated by [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br><br>`minimum: 1`<br> | format: "int64"; example: 102701621 |
| `external_account_id` | string (schema `ExternalAccountIdForEarmark`) | no | External ID of the account on which the earmark is created.<br>Should be the same `external_account_id` that was used to log in.<br>Should be the same `external_account_id` used in [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `description` | string (schema `EarmarkDescription`) | no | Earmark description | minLength: 1; maxLength: 40 |
| `amount` | number (schema `EarmarkAmount`) | no | Earmark amount<br><br>`minimum: 0.01`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0.01; maximum: 18446744073709552000; example: 50 |
| `balance` | number (schema `EarmarkBalance`) | no | Earmark balance. Initially equal to the earmarked amount and decreases as the reserved funds are used up or decreased in a decrease operation. It can also increase if an increase operation is performed.<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `release_datetime` | string (schema `EarmarkReleaseDatetime`) | no | RFC 3339 date/time for earmark release.<br>Used to schedule a cash-out (usually a payment) at the specified release date and time.<br>At `release_datetime`, an automatic process releases the earmarked funds and settles the cash-out.<br>If no `release_datetime` is set, the earmarked amount is held indefinitely until the customer cancels the earmark.<br> | format: "date-time"; minLength: 20; maxLength: 30; example: "2022-02-10T15:00:00Z" |
| `internal_operations` | array of object (schema `InternalOperation`) (schema `InternalOperations`) | no | List of internal operations performed to hold or release the earmark funds. |  |

201 Example `Earmark created`:

```json
{
  "earmark_id": "da85b309-a7f7-4316-b2ad-f069f0838058",
  "account_id": 102701621,
  "description": "string",
  "amount": 50,
  "balance": 50,
  "release_datetime": "2022-02-10T15:00:00.000Z",
  "internal_operations": [
    {
      "type": "HOLD_FUNDS",
      "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
      "business_date": "2022-02-10",
      "processing_code": "219248",
      "amount": 50,
      "created_at": "2022-02-10T15:00:00.000Z"
    }
  ]
}
```

##### Response 400

400 Example `Operations blocked for account`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WEAM0014",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `earmark_id must be a maximum of 60 characters in length`:

```json
{
  "code": "WEAM0015",
  "message": "earmark_id must be a maximum of 60 characters in length"
}
```

400 Example `earmark_id contains characters not permitted`:

```json
{
  "code": "WEAM0015",
  "message": "earmark_id contains characters not permitted: {characters}"
}
```

400 Example `amount must be 100,000,000,000,000,000 or less`:

```json
{
  "code": "WEAM0015",
  "message": "amount must be 100,000,000,000,000,000 or less"
}
```

400 Example `amount must be greater than 0`:

```json
{
  "code": "WEAM0015",
  "message": "amount must be greater than 0"
}
```

400 Example `Missing account identifier`:

```json
{
  "code": "WEAM0015",
  "message": "Either of these fields must be provided: account_id, external_account_id"
}
```

400 Example `external_account_id must be a maximum of 60 characters in length`:

```json
{
  "code": "WEAM0015",
  "message": "external_account_id must be a maximum of 60 characters in length"
}
```

400 Example `external_account_id contains characters not permitted`:

```json
{
  "code": "WEAM0015",
  "message": "external_account_id contains characters not permitted: {characters}"
}
```

400 Example `description must be a maximum of 40 characters in length`:

```json
{
  "code": "WEAM0015",
  "message": "description must be a maximum of 40 characters in length"
}
```

400 Example `tracking_id is a required field`:

```json
{
  "code": "WEAM0015",
  "message": "tracking_id is a required field"
}
```

400 Example `release_datetime cannot be in the past`:

```json
{
  "code": "WEAM0015",
  "message": "release_datetime cannot be in the past"
}
```

400 Example `amount has invalid decimal places for currency`:

```json
{
  "code": "WEAM0015",
  "message": "The number of decimal places is not compatible with the specified currency"
}
```

400 Example `Invalid account status`:

```json
{
  "code": "WEAM0005",
  "message": "Invalid account status"
}
```

400 Example `Insufficient funds`:

```json
{
  "code": "WEAM0006",
  "message": "Insufficient funds"
}
```

400 Example `Orgs operation not found or parameterized`:

```json
{
  "code": "WEAM0017",
  "message": "Orgs operations not found or parameters are incorrect or invalid"
}
```

400 Example `Invalid account program type`:

```json
{
  "code": "WEAM0019",
  "message": "The account's program type is invalid"
}
```

400 Example `Account closed`:

```json
{
  "code": "WEAM0026",
  "message": "Action not permitted on a closed account"
}
```

400 Example `Misconfigured administrative division`:

```json
{
  "code": "WEAM0036",
  "message": "Administrative division is misconfigured"
}
```

400 Example `Account has not finished onboarding`:

```json
{
  "code": "WEAM0037",
  "message": "Account has not finished onboarding"
}
```

400 Example `Invalid business date for the current business day cycle`:

```json
{
  "code": "WEAM0039",
  "message": "Invalid business date for the current business day cycle"
}
```

400 Example `Business date before account creation date`:

```json
{
  "code": "WEAM0040",
  "message": "The payment date cannot be earlier than the account creation date"
}
```

400 Example `Business date before account migration date` (Business date before account migration date):

```json
{
  "code": "WEAM0047",
  "message": "The payment date cannot be earlier than the account migration date"
}
```

400 Example `Future dated earmark operations are not allowed`:

```json
{
  "code": "WEAM0042",
  "message": "Future dated earmark operations are not allowed"
}
```

400 Example `Cannot post transaction on holidays`:

```json
{
  "code": "WEAM0043",
  "message": "Cannot post transaction on holidays"
}
```

400 Example `Cannot post transaction on weekends`:

```json
{
  "code": "WEAM0044",
  "message": "Cannot post transaction on weekends"
}
```

400 Example `Back business dating disabled`:

```json
{
  "code": "WEAM0045",
  "message": "Back business dating is disabled"
}
```

400 Example `Invalid account currency code`:

```json
{
  "code": "WEAM0046",
  "message": "Invalid account currency code: 999"
}
```

400 Example `Invalid account header`:

```json
{
  "code": "WEAM0016",
  "message": "Invalid header account"
}
```

400 Example `Operation already executed`:

```json
{
  "code": "WEAM0018",
  "message": "operation already made"
}
```

##### Response 401

401 Example `Account not authorized`:

```json
{
  "code": "WEAM0009",
  "message": "Account not authorized"
}
```

401 Example `Invalid Account token`:

```json
{
  "code": "WEAM0020",
  "message": "Use of a valid token for a valid account is required"
}
```

401 Example `Account cannot be debited`:

```json
{
  "code": "WEAM0023",
  "message": "The account cannot be debited. Debit function is not active"
}
```

401 Example `Account cannot be credited`:

```json
{
  "code": "WEAM0024",
  "message": "The account cannot be credited. Credit function is not active"
}
```

##### Response 409

409 Example `earmark_id [] is already in use`:

```json
{
  "code": "WEAM0001",
  "message": "earmark_id [{earmark_id}] is already in use",
  "data": {
    "earmark_id": "da85b309-a7f7-4316-b2ad-f069f0838058",
    "account_id": 102701621,
    "description": "string",
    "amount": 20,
    "balance": 20,
    "release_datetime": "2022-02-10T15:00:00.000Z",
    "internal_operations": [
      {
        "type": "HOLD_FUNDS",
        "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
        "processing_code": "219248",
        "amount": 10,
        "created_at": "2022-02-10T15:00:00.000Z"
      },
      {
        "type": "INCREASE",
        "tracking_id": "77260e09-2839-4b9e-a663-4aee4cf1568f",
        "processing_code": "219248",
        "amount": 10,
        "created_at": "2022-02-10T15:01:00.000Z"
      }
    ]
  }
}
```

409 Example `Tracking ID already in use`:

```json
{
  "code": "WEAM0025",
  "message": "Tracking ID is already in use",
  "data": {
    "earmark_id": "da85b309-a7f7-4316-b2ad-f069f0838058",
    "account_id": 102701621,
    "description": "string",
    "amount": 20,
    "balance": 20,
    "release_datetime": "2022-02-10T15:00:00.000Z",
    "internal_operations": [
      {
        "type": "HOLD_FUNDS",
        "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
        "processing_code": "219248",
        "amount": 10,
        "created_at": "2022-02-10T15:00:00.000Z"
      },
      {
        "type": "INCREASE",
        "tracking_id": "77260e09-2839-4b9e-a663-4aee4cf1568f",
        "processing_code": "219248",
        "amount": 10,
        "created_at": "2022-02-10T15:01:00.000Z"
      }
    ]
  }
}
```

409 Example `Tracking ID already in use by another earmark or account`:

```json
{
  "code": "WEAM0034",
  "message": "Tracking ID is already in use"
}
```

##### Response 423

423 Example `Transaction using this tracking ID in progress`:

```json
{
  "code": "WEAM0033",
  "message": "transaction using this tracking_id is in progress, please try again later"
}
```

423 Example `Earmark locked by a concurrent operation`:

```json
{
  "code": "WEAM0048",
  "message": "Earmark locked by a concurrent operation"
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
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WEAM0014` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WEAM0015` | earmark_id must be a maximum of 60 characters in length |
| 400 | `WEAM0005` | Invalid account status |
| 400 | `WEAM0006` | Insufficient funds |
| 400 | `WEAM0017` | Orgs operations not found or parameters are incorrect or invalid |
| 400 | `WEAM0019` | The account's program type is invalid |
| 400 | `WEAM0026` | Action not permitted on a closed account |
| 400 | `WEAM0036` | Administrative division is misconfigured |
| 400 | `WEAM0037` | Account has not finished onboarding |
| 400 | `WEAM0039` | Invalid business date for the current business day cycle |
| 400 | `WEAM0040` | The payment date cannot be earlier than the account creation date |
| 400 | `WEAM0047` | The payment date cannot be earlier than the account migration date |
| 400 | `WEAM0042` | Future dated earmark operations are not allowed |
| 400 | `WEAM0043` | Cannot post transaction on holidays |
| 400 | `WEAM0044` | Cannot post transaction on weekends |
| 400 | `WEAM0045` | Back business dating is disabled |
| 400 | `WEAM0046` | Invalid account currency code: 999 |
| 400 | `WEAM0016` | Invalid header account |
| 400 | `WEAM0018` | operation already made |
| 401 | `WEAM0009` | Account not authorized |
| 401 | `WEAM0020` | Use of a valid token for a valid account is required |
| 401 | `WEAM0023` | The account cannot be debited. Debit function is not active |
| 401 | `WEAM0024` | The account cannot be credited. Credit function is not active |
| 409 | `WEAM0001` | earmark_id [{earmark_id}] is already in use |
| 409 | `WEAM0025` | Tracking ID is already in use |
| 409 | `WEAM0034` | Tracking ID is already in use |
| 423 | `WEAM0033` | transaction using this tracking_id is in progress, please try again later |
| 423 | `WEAM0048` | Earmark locked by a concurrent operation |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `corporate-earmark-1` | https://developers.pismo.io/events/docs/corporate-earmark-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |
| `transaction-creation-1` | https://developers.pismo.io/events/docs/transaction-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;423;500`, has examples `True`, emits events `5`, deprecated `False`.

Guides that link to this operation: `KU-BANK-earmarks`, `KU-BANK-get-started-demand-deposit-accounts`, `KU-BANK-transaction-banking-accounts`, `KU-EVT-corporate-banking-data-events`, `KU-PAY-payment-overview-and-instant-payments`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v2/earmarks/{earmarkId} operationId=patch-corporate-v2-earmarks-earmarkid -->
### `PATCH /corporate/v2/earmarks/{earmarkId}` — Update earmark

- **operationId:** `patch-corporate-v2-earmarks-earmarkid`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Earmarking (external accounts)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update an earmark balance.
>
> This endpoint generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
> - [Account balance changed (Availables)](https://developers.pismo.io/events/docs/availables-change-available-1)
> - [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)
> - [Earmark created, updated, or canceled](https://developers.pismo.io/events/docs/corporate-earmark-1) with `UPDATED` action.
>
> **NOTES**:
> - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.
> - To find the correct reason IDs, refer to the [List account status reasons](https://developers.pismo.io/pismo-docs/reference/get-accounts-v1-accounts-status-reasons) endpoint.
> - The maximum number of internal operation inputs (updates that change the earmark amount) allowed is 2,000. Update requests that exceed this limit return bad request errors.
> - An earmark balance cannot be reduced to zero as a result of this operation. If successfully executing the request would result in a zero balance, the request fails and a bad request error is returned. If you want to reduce the balance to zero, you must use [Cancel earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks-earmarkid-cancel), instead.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `earmarkId` | path | yes | string | Earmark ID generated by [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks). | example: "1234" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateEarmarkRequestV2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `internal_operation` | object (schema `InternalOperation2`) | yes | Data used in transactions executed internally during the request. |  |
| `description` | string (schema `EarmarkDescription`) | no | Earmark description | minLength: 1; maxLength: 40 |
| `update_type` | string (schema `EarmarkUpdateType`) | no | Operation type. Default is `SET_AMOUNT`. | enum: ["INCREASE", "DECREASE", "SET_AMOUNT"]; default: "SET_AMOUNT"; example: "INCREASE" |
| `amount` | number (schema `EarmarkUpdateAmount`) | no | New amount to be set when `update_type` is `SET_AMOUNT` or delta. Value cannot be zero.<br><br>`minimum: 0.01`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0.01; maximum: 18446744073709552000; example: 1000.53 |
| `release_datetime` | string (schema `EarmarkReleaseDatetime`) | no | RFC 3339 date/time for earmark release.<br>Used to schedule a cash-out (usually a payment) at the specified release date and time.<br>At `release_datetime`, an automatic process releases the earmarked funds and settles the cash-out.<br>If no `release_datetime` is set, the earmarked amount is held indefinitely until the customer cancels the earmark.<br> | format: "date-time"; minLength: 20; maxLength: 30; example: "2022-02-10T15:00:00Z" |
| `force_post` | boolean (schema `EarmarkForcePost`) | no | If the account has any reason-based force debit payment restrictions, and the force earmark creation violates any of those restrictions, it fails. The reasons that restrict force debit operations are:<br>  - `CREDIT ONLY`: No force debit allowed<br>  - `ANY`: No force allowed<br>  - `MANUAL`: No force allowed<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `EarmarkResponse`) |
| 400 | A Bad Request validation error. | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized operation. | `application/json`: object (schema `ErrorResponse`) |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `earmark_id` | string (schema `EarmarkIdReturned`) | no | Earmark ID. Used as the primary key for query and update operations. It has the same value as the tracking ID, if one is provided. Generated by [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks). | example: "da85b309-a7f7-4316-b2ad-f069f0838058" |
| `account_id` | integer (schema `AccountID3`) | no | Account ID generated by [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br><br>`minimum: 1`<br> | format: "int64"; example: 102701621 |
| `external_account_id` | string (schema `ExternalAccountIdForEarmark`) | no | External ID of the account on which the earmark is created.<br>Should be the same `external_account_id` that was used to log in.<br>Should be the same `external_account_id` used in [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `description` | string (schema `EarmarkDescription`) | no | Earmark description | minLength: 1; maxLength: 40 |
| `amount` | number (schema `EarmarkAmount`) | no | Earmark amount<br><br>`minimum: 0.01`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0.01; maximum: 18446744073709552000; example: 50 |
| `balance` | number (schema `EarmarkBalance`) | no | Earmark balance. Initially equal to the earmarked amount and decreases as the reserved funds are used up or decreased in a decrease operation. It can also increase if an increase operation is performed.<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `release_datetime` | string (schema `EarmarkReleaseDatetime`) | no | RFC 3339 date/time for earmark release.<br>Used to schedule a cash-out (usually a payment) at the specified release date and time.<br>At `release_datetime`, an automatic process releases the earmarked funds and settles the cash-out.<br>If no `release_datetime` is set, the earmarked amount is held indefinitely until the customer cancels the earmark.<br> | format: "date-time"; minLength: 20; maxLength: 30; example: "2022-02-10T15:00:00Z" |
| `internal_operations` | array of object (schema `InternalOperation`) (schema `InternalOperations`) | no | List of internal operations performed to hold or release the earmark funds. |  |

200 Example `Earmark updated`:

```json
{
  "earmark_id": "da85b309-a7f7-4316-b2ad-f069f0838058",
  "account_id": 102701621,
  "description": "string",
  "amount": 20,
  "balance": 20,
  "release_datetime": "2022-02-10T15:00:00.000Z",
  "internal_operations": [
    {
      "type": "HOLD_FUNDS",
      "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
      "business_date": "2022-02-10",
      "processing_code": "219248",
      "amount": 10,
      "created_at": "2022-02-10T15:00:00.000Z"
    },
    {
      "type": "INCREASE",
      "tracking_id": "77260e09-2839-4b9e-a663-4aee4cf1568f",
      "business_date": "2023-03-09",
      "processing_code": "219248",
      "amount": 10,
      "created_at": "2022-02-10T15:01:00.000Z"
    }
  ]
}
```

##### Response 400

400 Example `Operations blocked for account`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WEAM0014",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `amount must be 100,000,000,000,000,000 or less`:

```json
{
  "code": "WEAM0015",
  "message": "amount must be 100,000,000,000,000,000 or less"
}
```

400 Example `amount must be greater than 0`:

```json
{
  "code": "WEAM0015",
  "message": "amount must be greater than 0"
}
```

400 Example `description must be a maximum of 40 characters in length`:

```json
{
  "code": "WEAM0015",
  "message": "description must be a maximum of 40 characters in length"
}
```

400 Example `tracking_id is a required field`:

```json
{
  "code": "WEAM0015",
  "message": "tracking_id is a required field"
}
```

400 Example `release_datetime cannot be in the past`:

```json
{
  "code": "WEAM0015",
  "message": "release_datetime cannot be in the past"
}
```

400 Example `amount has invalid decimal places for currency`:

```json
{
  "code": "WEAM0015",
  "message": "The number of decimal places is not compatible with the specified currency"
}
```

400 Example `Invalid header account`:

```json
{
  "code": "WEAM0016",
  "message": "Invalid header account"
}
```

400 Example `Orgs operation not found or parameterized`:

```json
{
  "code": "WEAM0017",
  "message": "Orgs operations not found or parameters are incorrect or invalid"
}
```

400 Example `operation already made`:

```json
{
  "code": "WEAM0018",
  "message": "operation already made"
}
```

400 Example `Invalid account program type`:

```json
{
  "code": "WEAM0019",
  "message": "The account's program type is invalid"
}
```

400 Example `Account closed`:

```json
{
  "code": "WEAM0026",
  "message": "Action not permitted on a closed account"
}
```

400 Example `Force earmark decrease not allowed`:

```json
{
  "code": "WEAM0027",
  "message": "You cannot force a release that results in the decrease of the earmark balance"
}
```

400 Example `Maximum internal operations reached`:

```json
{
  "code": "WEAM0030",
  "message": "Maximum number of internal operations reached [limit]"
}
```

400 Example `Balance reduced to zero`:

```json
{
  "code": "WEAM0031",
  "message": "Balance cannot be reduced to zero as a result of this operation"
}
```

400 Example `Misconfigured administrative division`:

```json
{
  "code": "WEAM0036",
  "message": "Administrative division is misconfigured"
}
```

400 Example `Balance unchanged`:

```json
{
  "code": "WEAM0038",
  "message": "Earmark balance is unchanged"
}
```

400 Example `Invalid business date for the current business day cycle`:

```json
{
  "code": "WEAM0039",
  "message": "Invalid business date for the current business day cycle"
}
```

400 Example `Business date before account creation date`:

```json
{
  "code": "WEAM0040",
  "message": "The payment date cannot be earlier than the account creation date"
}
```

400 Example `Business date before account migration date` (Business date before account migration date):

```json
{
  "code": "WEAM0047",
  "message": "The payment date cannot be earlier than the account migration date"
}
```

400 Example `Business date cannot be earlier than the earmark creation date`:

```json
{
  "code": "WEAM0041",
  "message": "Business date cannot be earlier than the earmark creation date"
}
```

400 Example `Future dated earmark operations are not allowed`:

```json
{
  "code": "WEAM0042",
  "message": "Future dated earmark operations are not allowed"
}
```

400 Example `Cannot post transaction on holidays`:

```json
{
  "code": "WEAM0043",
  "message": "Cannot post transaction on holidays"
}
```

400 Example `Cannot post transaction on weekends`:

```json
{
  "code": "WEAM0044",
  "message": "Cannot post transaction on weekends"
}
```

400 Example `Back business dating disabled`:

```json
{
  "code": "WEAM0045",
  "message": "Back business dating is disabled"
}
```

400 Example `Invalid account currency code`:

```json
{
  "code": "WEAM0046",
  "message": "Invalid account currency code: 999"
}
```

##### Response 401

401 Example `Account cannot be debited`:

```json
{
  "code": "WEAM0023",
  "message": "The account cannot be debited. Debit function is not active"
}
```

401 Example `Account cannot be credited`:

```json
{
  "code": "WEAM0024",
  "message": "The account cannot be credited. Credit function is not active"
}
```

##### Response 409

409 Example `Tracking ID already in use`:

```json
{
  "code": "WEAM0025",
  "message": "Tracking ID is already in use",
  "data": {
    "earmark_id": "da85b309-a7f7-4316-b2ad-f069f0838058",
    "account_id": 102701621,
    "description": "string",
    "amount": 20,
    "balance": 20,
    "release_datetime": "2022-02-10T15:00:00.000Z",
    "internal_operations": [
      {
        "type": "HOLD_FUNDS",
        "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
        "processing_code": "219248",
        "amount": 10,
        "created_at": "2022-02-10T15:00:00.000Z"
      },
      {
        "type": "INCREASE",
        "tracking_id": "77260e09-2839-4b9e-a663-4aee4cf1568f",
        "processing_code": "219248",
        "amount": 10,
        "created_at": "2022-02-10T15:01:00.000Z"
      }
    ]
  }
}
```

409 Example `Tracking ID already in use by another earmark or account`:

```json
{
  "code": "WEAM0034",
  "message": "Tracking id is already in use"
}
```

409 Example `Earmark was concurrently modified`:

```json
{
  "code": "WEAM0049",
  "message": "Earmark was concurrently modified"
}
```

##### Response 423

423 Example `Earmark locked by a concurrent operation`:

```json
{
  "code": "WEAM0048",
  "message": "Earmark locked by a concurrent operation"
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
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WEAM0014` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WEAM0015` | amount must be 100,000,000,000,000,000 or less |
| 400 | `WEAM0016` | Invalid header account |
| 400 | `WEAM0017` | Orgs operations not found or parameters are incorrect or invalid |
| 400 | `WEAM0018` | operation already made |
| 400 | `WEAM0019` | The account's program type is invalid |
| 400 | `WEAM0026` | Action not permitted on a closed account |
| 400 | `WEAM0027` | You cannot force a release that results in the decrease of the earmark balance |
| 400 | `WEAM0030` | Maximum number of internal operations reached [limit] |
| 400 | `WEAM0031` | Balance cannot be reduced to zero as a result of this operation |
| 400 | `WEAM0036` | Administrative division is misconfigured |
| 400 | `WEAM0038` | Earmark balance is unchanged |
| 400 | `WEAM0039` | Invalid business date for the current business day cycle |
| 400 | `WEAM0040` | The payment date cannot be earlier than the account creation date |
| 400 | `WEAM0047` | The payment date cannot be earlier than the account migration date |
| 400 | `WEAM0041` | Business date cannot be earlier than the earmark creation date |
| 400 | `WEAM0042` | Future dated earmark operations are not allowed |
| 400 | `WEAM0043` | Cannot post transaction on holidays |
| 400 | `WEAM0044` | Cannot post transaction on weekends |
| 400 | `WEAM0045` | Back business dating is disabled |
| 400 | `WEAM0046` | Invalid account currency code: 999 |
| 401 | `WEAM0023` | The account cannot be debited. Debit function is not active |
| 401 | `WEAM0024` | The account cannot be credited. Credit function is not active |
| 409 | `WEAM0025` | Tracking ID is already in use |
| 409 | `WEAM0034` | Tracking id is already in use |
| 409 | `WEAM0049` | Earmark was concurrently modified |
| 423 | `WEAM0048` | Earmark locked by a concurrent operation |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `corporate-earmark-1` | https://developers.pismo.io/events/docs/corporate-earmark-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |
| `transaction-creation-1` | https://developers.pismo.io/events/docs/transaction-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;409;423;500`, has examples `True`, emits events `5`, deprecated `False`.

Guides that link to this operation: `KU-BANK-earmarks`, `KU-BANK-transaction-banking-accounts`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/earmarks/{earmarkId}/cancel operationId=post-corporate-v2-earmarks-earmarkid-cancel -->
### `POST /corporate/v2/earmarks/{earmarkId}/cancel` — Cancel earmark

- **operationId:** `post-corporate-v2-earmarks-earmarkid-cancel`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Earmarking (external accounts)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel a previously set earmark, releasing the earmarked funds, and preventing the earmark from executing at its scheduled expiration date/time.
> For more information about earmark operations, refer to the [Earmarks launch reference](doc:earmarks) guide.
>
> This endpoint generates the follow events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
> - [Account balance changed (Availables)](https://developers.pismo.io/events/docs/availables-change-available-1)
> - [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1)
> - [Earmark created, updated, or canceled](https://developers.pismo.io/events/docs/corporate-earmark-1) with `CANCELED` Action.
>
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.
>
> **NOTE**: This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `earmarkId` | path | yes | string | Earmark ID generated by [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks). | example: "1234" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `CancelEarmarkRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `internal_operation` | object (schema `InternalOperation2`) | yes | Data used in transactions executed internally during the request. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `EarmarkResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized operation. | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 423 | Locked | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `earmark_id` | string (schema `EarmarkIdReturned`) | no | Earmark ID. Used as the primary key for query and update operations. It has the same value as the tracking ID, if one is provided. Generated by [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks). | example: "da85b309-a7f7-4316-b2ad-f069f0838058" |
| `account_id` | integer (schema `AccountID3`) | no | Account ID generated by [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br><br>`minimum: 1`<br> | format: "int64"; example: 102701621 |
| `external_account_id` | string (schema `ExternalAccountIdForEarmark`) | no | External ID of the account on which the earmark is created.<br>Should be the same `external_account_id` that was used to log in.<br>Should be the same `external_account_id` used in [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `description` | string (schema `EarmarkDescription`) | no | Earmark description | minLength: 1; maxLength: 40 |
| `amount` | number (schema `EarmarkAmount`) | no | Earmark amount<br><br>`minimum: 0.01`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0.01; maximum: 18446744073709552000; example: 50 |
| `balance` | number (schema `EarmarkBalance`) | no | Earmark balance. Initially equal to the earmarked amount and decreases as the reserved funds are used up or decreased in a decrease operation. It can also increase if an increase operation is performed.<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `release_datetime` | string (schema `EarmarkReleaseDatetime`) | no | RFC 3339 date/time for earmark release.<br>Used to schedule a cash-out (usually a payment) at the specified release date and time.<br>At `release_datetime`, an automatic process releases the earmarked funds and settles the cash-out.<br>If no `release_datetime` is set, the earmarked amount is held indefinitely until the customer cancels the earmark.<br> | format: "date-time"; minLength: 20; maxLength: 30; example: "2022-02-10T15:00:00Z" |
| `internal_operations` | array of object (schema `InternalOperation`) (schema `InternalOperations`) | no | List of internal operations performed to hold or release the earmark funds. |  |

200 Example `Earmark canceled`:

```json
{
  "earmark_id": "da85b309-a7f7-4316-b2ad-f069f0838058",
  "account_id": 102701621,
  "description": "string",
  "amount": 50,
  "balance": 0,
  "release_datetime": "2022-02-10T15:00:00.000Z",
  "internal_operations": [
    {
      "type": "HOLD_FUNDS",
      "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
      "business_date": "2022-02-10",
      "processing_code": "219248",
      "amount": 50,
      "created_at": "2022-02-10T15:00:00.000Z"
    },
    {
      "type": "RELEASE_FUNDS",
      "tracking_id": "77260e09-2839-4b9e-a663-4aee4cf1568f",
      "business_date": "2023-03-09",
      "processing_code": "219251",
      "amount": 50,
      "created_at": "2022-02-10T15:01:00.000Z"
    }
  ]
}
```

##### Response 400

400 Example `Operations blocked for account`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid JSON payload`:

```json
{
  "code": "WEAM0014",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `tracking_id is a required field`:

```json
{
  "code": "WEAM0015",
  "message": "tracking_id is a required field"
}
```

400 Example `Earmark not active`:

```json
{
  "code": "WEAM0008",
  "message": "Earmark ID {earmarkId} not active"
}
```

400 Example `Orgs operation not found or parameterized`:

```json
{
  "code": "WEAM0017",
  "message": "Orgs operations not found or parameters are incorrect or invalid"
}
```

400 Example `operation already made`:

```json
{
  "code": "WEAM0018",
  "message": "operation already made"
}
```

400 Example `Invalid account program type`:

```json
{
  "code": "WEAM0019",
  "message": "The account's program type is invalid"
}
```

400 Example `Earmark has no balance to cancel`:

```json
{
  "code": "WEAM0022",
  "message": "Earmark with ID {earmarkId} has zero balance"
}
```

400 Example `Corporate account not found`:

```json
{
  "code": "WCAC0012",
  "message": "Corporate account not found"
}
```

400 Example `Misconfigured administrative division`:

```json
{
  "code": "WEAM0036",
  "message": "Administrative division is misconfigured"
}
```

400 Example `Invalid business date for the current business day cycle`:

```json
{
  "code": "WEAM0039",
  "message": "Invalid business date for the current business day cycle"
}
```

400 Example `Business date before account creation date`:

```json
{
  "code": "WEAM0040",
  "message": "The payment date cannot be earlier than the account creation date"
}
```

400 Example `Business date before account migration date` (Business date before account migration date):

```json
{
  "code": "WEAM0047",
  "message": "The payment date cannot be earlier than the account migration date"
}
```

400 Example `Business date cannot be earlier than the earmark creation date`:

```json
{
  "code": "WEAM0041",
  "message": "Business date cannot be earlier than the earmark creation date"
}
```

400 Example `Future dated earmark operations are not allowed`:

```json
{
  "code": "WEAM0042",
  "message": "Future dated earmark operations are not allowed"
}
```

400 Example `Cannot post transaction on holidays`:

```json
{
  "code": "WEAM0043",
  "message": "Cannot post transaction on holidays"
}
```

400 Example `Cannot post transaction on weekends`:

```json
{
  "code": "WEAM0044",
  "message": "Cannot post transaction on weekends"
}
```

400 Example `Back business dating disabled`:

```json
{
  "code": "WEAM0045",
  "message": "Back business dating is disabled"
}
```

400 Example `Invalid account currency code`:

```json
{
  "code": "WEAM0046",
  "message": "Invalid account currency code: 999"
}
```

##### Response 401

401 Example `Account cannot be credited`:

```json
{
  "code": "WEAM0024",
  "message": "The account cannot be credited. Credit function is not active"
}
```

##### Response 404

404 Example `Earmark not found`:

```json
{
  "code": "WEAM0007",
  "message": "Earmark with ID {earmarkId} not found"
}
```

##### Response 409

409 Example `Tracking ID already in use`:

```json
{
  "code": "WEAM0025",
  "message": "Tracking ID is already in use",
  "data": {
    "earmark_id": "da85b309-a7f7-4316-b2ad-f069f0838058",
    "account_id": 102701621,
    "description": "string",
    "amount": 20,
    "balance": 20,
    "release_datetime": "2022-02-10T15:00:00.000Z",
    "internal_operations": [
      {
        "type": "HOLD_FUNDS",
        "tracking_id": "10027506-171f-b1e1-8412-67f5f5145a3b",
        "processing_code": "219248",
        "amount": 10,
        "created_at": "2022-02-10T15:00:00.000Z"
      },
      {
        "type": "INCREASE",
        "tracking_id": "77260e09-2839-4b9e-a663-4aee4cf1568f",
        "processing_code": "219248",
        "amount": 10,
        "created_at": "2022-02-10T15:01:00.000Z"
      }
    ]
  }
}
```

409 Example `Tracking ID already in use by another earmark or account`:

```json
{
  "code": "WEAM0034",
  "message": "Tracking id is already in use"
}
```

409 Example `Earmark was concurrently modified`:

```json
{
  "code": "WEAM0049",
  "message": "Earmark was concurrently modified"
}
```

##### Response 423

423 Example `Earmark locked by a concurrent operation`:

```json
{
  "code": "WEAM0048",
  "message": "Earmark locked by a concurrent operation"
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
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WEAM0014` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WEAM0015` | tracking_id is a required field |
| 400 | `WEAM0008` | Earmark ID {earmarkId} not active |
| 400 | `WEAM0017` | Orgs operations not found or parameters are incorrect or invalid |
| 400 | `WEAM0018` | operation already made |
| 400 | `WEAM0019` | The account's program type is invalid |
| 400 | `WEAM0022` | Earmark with ID {earmarkId} has zero balance |
| 400 | `WCAC0012` | Corporate account not found |
| 400 | `WEAM0036` | Administrative division is misconfigured |
| 400 | `WEAM0039` | Invalid business date for the current business day cycle |
| 400 | `WEAM0040` | The payment date cannot be earlier than the account creation date |
| 400 | `WEAM0047` | The payment date cannot be earlier than the account migration date |
| 400 | `WEAM0041` | Business date cannot be earlier than the earmark creation date |
| 400 | `WEAM0042` | Future dated earmark operations are not allowed |
| 400 | `WEAM0043` | Cannot post transaction on holidays |
| 400 | `WEAM0044` | Cannot post transaction on weekends |
| 400 | `WEAM0045` | Back business dating is disabled |
| 400 | `WEAM0046` | Invalid account currency code: 999 |
| 401 | `WEAM0024` | The account cannot be credited. Credit function is not active |
| 404 | `WEAM0007` | Earmark with ID {earmarkId} not found |
| 409 | `WEAM0025` | Tracking ID is already in use |
| 409 | `WEAM0034` | Tracking id is already in use |
| 409 | `WEAM0049` | Earmark was concurrently modified |
| 423 | `WEAM0048` | Earmark locked by a concurrent operation |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `corporate-earmark-1` | https://developers.pismo.io/events/docs/corporate-earmark-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |
| `transaction-creation-1` | https://developers.pismo.io/events/docs/transaction-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;409;423;500`, has examples `True`, emits events `5`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-earmarks`, `KU-BANK-transaction-banking-accounts`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/earmarks operationId=get-corporate-earmarks -->
### `GET /corporate/v1/earmarks` — List earmarks

- **operationId:** `get-corporate-earmarks`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Earmarking (external accounts)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List all created earmarks, including ones that are canceled or have already been executed.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cursor` | query | no | string | Cursor to the next page of results. If no value is specified, it fetches the first page. | example: "1234" |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `10` | default: 10; format: "int32"; example: 20 |
| `balanceGt` | query | no | number | Filters earmarks whose balance exceeds the specified amount. | format: "float"; example: 10.01 |
| `balanceGe` | query | no | number | Filters earmarks with a balance greater than or equal to the specified amount. | format: "float"; example: 22.5 |
| `balanceLt` | query | no | number | Filters earmarks with a balance less than the specified amount. | format: "float"; example: 15.21 |
| `balanceLe` | query | no | number | Filters earmarks with a balance less than or equal to the specified amount. | format: "float"; example: 11.33 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListEarmarksResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `earmarks` | array of object (schema `EarmarkResponse`) | no | List of earmarks |  |
| `pagination` | object (schema `Pagination`) | no | Data related to list pagination using a cursor. |  |

200 Example `Example earmarks list`:

```json
{
  "earmarks": [
    {
      "earmark_id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "release_datetime": "2023-03-08T13:06:04.669Z",
      "amount": 12.34,
      "balance": 10.2,
      "account_id": 111111111,
      "description": "string 1",
      "internal_operations": [
        {
          "type": "HOLD_FUNDS",
          "tracking_id": "084cf80f-8e0c-4be5-8083-c3225075323e",
          "business_date": "2023-03-08",
          "processing_code": "000000",
          "amount": 12.34,
          "created_at": "2023-03-08T11:01:02.669Z",
          "metadata": {
            "my-id": 2932
          }
        }
      ]
    },
    {
      "earmark_id": "629858d0-21b3-4eb7-be7b-af0850d7a1da",
      "release_datetime": "2023-03-08T13:06:04.669Z",
      "amount": 15.78,
      "balance": 20.34,
      "account_id": 111111111,
      "description": "string 2",
      "internal_operations": [
        {
          "type": "HOLD_FUNDS",
          "tracking_id": "084cf80f-8e0c-4be5-8083-c3225075323e",
          "business_date": "2023-03-09",
          "processing_code": "000000",
          "amount": 15.78,
          "created_at": "2023-03-09T11:01:02.669Z",
          "metadata": {
            "my-id": 2933
          }
        }
      ]
    }
  ],
  "pagination": {
    "limit": 10,
    "cursor": "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0="
  }
}
```

##### Response 400

400 Example `Invalid query parameter`:

```json
{
  "code": "WCMN0005",
  "message": "Invalid query parameter"
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
| 400 | `WCMN0005` | Invalid query parameter |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-earmarks`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/earmarks/{earmarkId} operationId=find-corporate-earmark -->
### `GET /corporate/v1/earmarks/{earmarkId}` — Get earmark

- **operationId:** `find-corporate-earmark`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Earmarking (external accounts)`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get an earmark by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `earmarkId` | path | yes | string | Earmark ID generated by [Create earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks). | example: "1234" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `EarmarkResponse`) |
| 404 | The specified resource was not found |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `earmark_id` | string (schema `EarmarkIdReturned`) | no | Earmark ID. Used as the primary key for query and update operations. It has the same value as the tracking ID, if one is provided. Generated by [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks). | example: "da85b309-a7f7-4316-b2ad-f069f0838058" |
| `account_id` | integer (schema `AccountID3`) | no | Account ID generated by [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br><br>`minimum: 1`<br> | format: "int64"; example: 102701621 |
| `external_account_id` | string (schema `ExternalAccountIdForEarmark`) | no | External ID of the account on which the earmark is created.<br>Should be the same `external_account_id` that was used to log in.<br>Should be the same `external_account_id` used in [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `description` | string (schema `EarmarkDescription`) | no | Earmark description | minLength: 1; maxLength: 40 |
| `amount` | number (schema `EarmarkAmount`) | no | Earmark amount<br><br>`minimum: 0.01`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0.01; maximum: 18446744073709552000; example: 50 |
| `balance` | number (schema `EarmarkBalance`) | no | Earmark balance. Initially equal to the earmarked amount and decreases as the reserved funds are used up or decreased in a decrease operation. It can also increase if an increase operation is performed.<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `release_datetime` | string (schema `EarmarkReleaseDatetime`) | no | RFC 3339 date/time for earmark release.<br>Used to schedule a cash-out (usually a payment) at the specified release date and time.<br>At `release_datetime`, an automatic process releases the earmarked funds and settles the cash-out.<br>If no `release_datetime` is set, the earmarked amount is held indefinitely until the customer cancels the earmark.<br> | format: "date-time"; minLength: 20; maxLength: 30; example: "2022-02-10T15:00:00Z" |
| `internal_operations` | array of object (schema `InternalOperation`) (schema `InternalOperations`) | no | List of internal operations performed to hold or release the earmark funds. |  |

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
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-earmarks`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/InternalOperation2 -->
### Schema `InternalOperation2`

Pointer: `#/components/schemas/InternalOperation2`. Type: object (schema `InternalOperation2`).

> Data used in transactions executed internally during the request.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `metadata` | object (schema `CancelEarmarkMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

<!-- schema: #/components/schemas/InternalOperation -->
### Schema `InternalOperation`

Pointer: `#/components/schemas/InternalOperation`. Type: object (schema `InternalOperation`).

> Internal operation performed to hold or release funds

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `type` | string (schema `InternalOperationType`) | no | Internal operation type.<br><br>`minLength: 1`<br>`maxLength: 13`<br> | enum: ["HOLD_FUNDS", "RELEASE_FUNDS", "INCREASE", "DECREASE"]; example: "HOLD_FUNDS" |
| `processing_code` | string (schema `ProcessingCode`) | no | Processing code used to create the underlying transaction. Each internal operation type uses a default processing code.<br><br>`minLength: 1`<br>`maxLength: 6`<br> | minLength: 1; maxLength: 6; example: "219248" |
| `amount` | number (schema `InternalOperationAmount`) | no | Internal operation amount<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 50 |
| `validation_rules` | object (map of object (schema `ValidationRule`)) (schema `ValidationRules`) | no | Rules that determine which validations are executed during the payment process.<br><br>Available validation rules:<br>  - `LEDGER`<br>  - `ACCOUNT_STATUS`<br>  - `FLEX_CONTROLS`<br>  - `RATES`<br><br><br>`force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.<br> | example: {"ACCOUNT_STATUS": {"override": false}, "LEDGER": {"force": false}, "FLEX_CONTROLS": {"override": true}, "RATES": {"override": true}} |
| `created_at` | string (schema `InternalOperationCreatedAt`) | no | Internal operation creation time. Format = yyyy-mm-dd:hr:mm:ss.<br> | format: "date-time"; example: "2022-02-10T15:00:00Z" |
| `metadata` | object (schema `InternalOperationMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis).<br> |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/EarmarkResponse -->
### Schema `EarmarkResponse`

Pointer: `#/components/schemas/EarmarkResponse`. Type: object (schema `EarmarkResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `earmark_id` | string (schema `EarmarkIdReturned`) | no | Earmark ID. Used as the primary key for query and update operations. It has the same value as the tracking ID, if one is provided. Generated by [Create Earmark](https://developers.pismo.io/pismo-docs/reference/post-corporate-v2-earmarks). | example: "da85b309-a7f7-4316-b2ad-f069f0838058" |
| `account_id` | integer (schema `AccountID3`) | no | Account ID generated by [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br><br>`minimum: 1`<br> | format: "int64"; example: 102701621 |
| `external_account_id` | string (schema `ExternalAccountIdForEarmark`) | no | External ID of the account on which the earmark is created.<br>Should be the same `external_account_id` that was used to log in.<br>Should be the same `external_account_id` used in [Create Corporate Account](https://developers.pismo.io/pismo-docs/reference/post-account).<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `description` | string (schema `EarmarkDescription`) | no | Earmark description | minLength: 1; maxLength: 40 |
| `amount` | number (schema `EarmarkAmount`) | no | Earmark amount<br><br>`minimum: 0.01`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0.01; maximum: 18446744073709552000; example: 50 |
| `balance` | number (schema `EarmarkBalance`) | no | Earmark balance. Initially equal to the earmarked amount and decreases as the reserved funds are used up or decreased in a decrease operation. It can also increase if an increase operation is performed.<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `release_datetime` | string (schema `EarmarkReleaseDatetime`) | no | RFC 3339 date/time for earmark release.<br>Used to schedule a cash-out (usually a payment) at the specified release date and time.<br>At `release_datetime`, an automatic process releases the earmarked funds and settles the cash-out.<br>If no `release_datetime` is set, the earmarked amount is held indefinitely until the customer cancels the earmark.<br> | format: "date-time"; minLength: 20; maxLength: 30; example: "2022-02-10T15:00:00Z" |
| `internal_operations` | array of object (schema `InternalOperation`) (schema `InternalOperations`) | no | List of internal operations performed to hold or release the earmark funds. |  |

<!-- schema: #/components/schemas/Pagination -->
### Schema `Pagination`

Pointer: `#/components/schemas/Pagination`. Type: object (schema `Pagination`).

> Data related to list pagination using a cursor.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `cursor` | string (schema `Cursor`) | no | Cursor pointing to the next page of results | example: "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0=" |

<!-- schema: #/components/schemas/ValidationRules -->
### Schema `ValidationRules`

Pointer: `#/components/schemas/ValidationRules`. Type: object (map of object (schema `ValidationRule`)) (schema `ValidationRules`).

> Rules that determine which validations are executed during the payment process.<br>
> Available validation rules:
>   - `LEDGER`
>   - `ACCOUNT_STATUS`
>   - `FLEX_CONTROLS`
>   - `RATES`<br>
>
> `force` is only supported for `LEDGER`. `override` is supported for `ACCOUNT_STATUS`, `FLEX_CONTROLS`, and `RATES`.

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Earmarking (external accounts)`: POST /corporate/v2/earmarks, PATCH /corporate/v2/earmarks/{earmarkId}, POST /corporate/v2/earmarks/{earmarkId}/cancel, GET /corporate/v1/earmarks, GET /corporate/v1/earmarks/{earmarkId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-earmarks` — Earmarks
- `KU-BANK-get-started-demand-deposit-accounts` — Get started with demand deposit accounts (DDAs)
- `KU-BANK-transaction-banking-accounts` — Transaction banking and transaction banking accounts
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-ERR-codes-weam` — Error codes: WEAM
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
- `KU-PAY-payment-overview-and-instant-payments` — Banking payment overview, instant payments and integrated payments
