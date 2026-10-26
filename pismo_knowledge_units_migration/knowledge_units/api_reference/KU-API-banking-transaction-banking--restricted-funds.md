---
ku_id: KU-API-banking-transaction-banking--restricted-funds
title: 'API reference: Banking - Transaction banking — Restricted funds'
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
- list-corporate-v1-restricted-funds
- post-corporate-v1-restricted-funds
- get-corporate-v1-restricted-funds
- patch-corporate-v1-restricted-funds
- patch-corporate-v2-restricted-funds
related_kus:
- KU-BANK-file-based-processing
- KU-BANK-restrictions
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-wiac-to-wstm
- KU-ERR-codes-wrfo
- KU-EVT-catalogue-account
- KU-EVT-catalogue-corporate
- KU-EVT-catalogue-other-domains
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Restricted funds

**KU ID:** `KU-API-banking-transaction-banking--restricted-funds` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Restricted funds` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Restricted funds endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /corporate/v1/restricted-funds` | `list-corporate-v1-restricted-funds` | List fund restrictions | no |
| `POST /corporate/v1/restricted-funds` | `post-corporate-v1-restricted-funds` | Create fund restriction | no |
| `GET /corporate/v1/restricted-funds/{restrictedFundsId}` | `get-corporate-v1-restricted-funds` | Get fund restriction | no |
| `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` | `patch-corporate-v1-restricted-funds` | Release restriction | no |
| `PATCH /corporate/v2/restricted-funds/{restrictedFundsId}` | `patch-corporate-v2-restricted-funds` | Update restriction | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/restricted-funds operationId=list-corporate-v1-restricted-funds -->
### `GET /corporate/v1/restricted-funds` — List fund restrictions

- **operationId:** `list-corporate-v1-restricted-funds`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Restricted funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List all account fund restrictions.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cursor` | query | no | string | Cursor to the next page of results. If no value is specified, it fetches the first page. | example: "1234" |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `10` | default: 10; format: "int32"; maximum: 20; example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListRestrictedFundsResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pagination` | object (schema `Pagination`) | yes | Data related to list pagination using a cursor. |  |
| `restricted_funds` | array of object | yes |  |  |
| `restricted_funds[].restricted_funds_id` | string (schema `RestrictedFundsID`) | yes | Restricted funds ID. Only accepts letters, digits, periods, underscores and hyphens.<br>`maxLength: 60` | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `restricted_funds[].hold_method` | string (schema `RestrictedFundsHoldMethod`) | yes | Determines how the Pismo platform processes the restriction request in relation to the available balance at the time of execution.<br><br>Notes:<br>  - `STRICT` applies the full requested amount or fails (no partial holds).<br>  - `FLEXIBLE` can apply only the available portion, resulting in a partial hold.<br>  - `RECURRENT` behaves like `FLEXIBLE` at creation time. After creation, the restriction automatically applies to each incoming credit, re-restricting funds whenever a credit is posted, until the restriction reaches its target amount or `increase_datetime_limit` is reached. | enum: ["STRICT", "FLEXIBLE", "RECURRENT"]; default: "STRICT"; example: "STRICT" |
| `restricted_funds[].requested_amount` | number (schema `RestrictedFundsRequestedAmount`) | yes | Amount originally requested at the time the restriction was created; remains unchanged after the initial request. | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `restricted_funds[].held_amount` | number (schema `RestrictedFundsHeldAmount`) | yes | Amount held by restriction | format: "float"; minimum: 0; maximum: 100000000000000000 |
| `restricted_funds[].created_at` | string (schema `RestrictedFundsCreatedAt`) | yes | Date and time when the restriction was created, displayed in ISO 8601 format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `restricted_funds[].soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `restricted_funds[].type` | string (schema `RestrictedFundsType`) | no | The type/nature of the restriction.<br><br>Notes:<br>  - `REGULATORY`: Restriction created for regulatory or operational reasons<br>  - `JUDICIAL`: Restriction created to comply with a judicial order | enum: ["REGULATORY", "JUDICIAL"]; default: "REGULATORY"; example: "REGULATORY" |
| `restricted_funds[].metadata` | object (schema `RestrictedFundsMainMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>This metadata applies when you don't send metadata for the restricted‑funds operation. It covers cases such as automatic recurrent operations or held‑funds expiration.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `restricted_funds[].increase_datetime_limit` | string (schema `RestrictedFundsIncreaseDatetimeLimit`) | no | The date and time limit, in RFC 3339 format, up to which a `RECURRENT` restriction continues applying to incoming credits on the account.<br><br>Notes:<br>  - Only accepted on creation when `hold_method` is `RECURRENT`<br>  - Must not be in the past | format: "date-time"; example: "2026-12-31T23:59:59Z" |

200 Example `example`:

```json
{
  "pagination": {
    "limit": 10,
    "cursor": "eyJpZCI6MTMyfQ=="
  },
  "restricted_funds": [
    {
      "restricted_funds_id": "4a4060d5-3649-46e8-8d64-93949b212918",
      "soft_descriptor": "FDIC 12 C.F.R. 360.9",
      "hold_method": "FLEXIBLE",
      "requested_amount": 100.99,
      "held_amount": 90.22,
      "created_at": "2025-05-29T11:33:22Z"
    }
  ]
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
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-restrictions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v1/restricted-funds operationId=post-corporate-v1-restricted-funds -->
### `POST /corporate/v1/restricted-funds` — Create fund restriction

- **operationId:** `post-corporate-v1-restricted-funds`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Restricted funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create fund restriction. You can move funds from the `available_balance` to the `restricted_funds` balance.
>
> For details, refer to [Restrict funds](doc:restrict-funds).
>
> NOTE:
> - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
> This endpoint generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)
> - [Restricted Funds created or released](https://developers.pismo.io/events/docs/corporate-restricted-funds-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information on events and setting up event notifications.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `RestrictedFundsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `hold_method` | string (schema `RestrictedFundsHoldMethod`) | yes | Determines how the Pismo platform processes the restriction request in relation to the available balance at the time of execution.<br><br>Notes:<br>  - `STRICT` applies the full requested amount or fails (no partial holds).<br>  - `FLEXIBLE` can apply only the available portion, resulting in a partial hold.<br>  - `RECURRENT` behaves like `FLEXIBLE` at creation time. After creation, the restriction automatically applies to each incoming credit, re-restricting funds whenever a credit is posted, until the restriction reaches its target amount or `increase_datetime_limit` is reached. | enum: ["STRICT", "FLEXIBLE", "RECURRENT"]; default: "STRICT"; example: "STRICT" |
| `amount` | number (schema `RestrictedFundsAmount`) | yes | Amount requested by the operation<br><br>The final applied amount might vary (refer to `applied_amount`) based on execution rules and the available balance at the time of execution.<br><br><br>**Note**:<br>  * For `RESTRICT_FUNDS`, this is the amount to be held.<br>  * For `RELEASE_FUNDS`, this is the amount to be released.<br>  * For `EXECUTE_FUNDS`, this is the amount to be debited from the held funds.<br>  * Precision follows the currency's minor units. For example:<br>    * Two decimals (USD, EUR): values use increments of 0.01<br>    * Three decimals (BHD, JOD, KWD, OMR, TND): values use increments of 0.001<br>    * Four‑decimal (CLF): values use increments of 0.0001<br> | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `operation` | object (schema `RestrictedFundsRequestOperation`) | yes | Represents the data of the hold or release transaction. |  |
| `restricted_funds_id` | string (schema `RestrictedFundsID`) | no | Restricted funds ID. Only accepts letters, digits, periods, underscores and hyphens.<br>`maxLength: 60` | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `type` | string (schema `RestrictedFundsType`) | no | The type/nature of the restriction.<br><br>Notes:<br>  - `REGULATORY`: Restriction created for regulatory or operational reasons<br>  - `JUDICIAL`: Restriction created to comply with a judicial order | enum: ["REGULATORY", "JUDICIAL"]; default: "REGULATORY"; example: "REGULATORY" |
| `metadata` | object (schema `RestrictedFundsMainMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>This metadata applies when you don't send metadata for the restricted‑funds operation. It covers cases such as automatic recurrent operations or held‑funds expiration.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `increase_datetime_limit` | string (schema `RestrictedFundsIncreaseDatetimeLimit`) | no | The date and time limit, in RFC 3339 format, up to which a `RECURRENT` restriction continues applying to incoming credits on the account.<br><br>Notes:<br>  - Only accepted on creation when `hold_method` is `RECURRENT`<br>  - Must not be in the past | format: "date-time"; example: "2026-12-31T23:59:59Z" |

Example `example`:

```json
{
  "restricted_funds_id": "4a4060d5-3649-46e8-8d64-93949b212918",
  "hold_method": "FLEXIBLE",
  "amount": 100.21,
  "operation": {
    "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
    "soft_descriptor": "Funds restriction requested by FDIC 12 C.F.R. 360.9",
    "metadata": {
      "key": "value"
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `RestrictedFunds`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 429 | Too Many Requests | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `restricted_funds_id` | string (schema `RestrictedFundsID`) | yes | Restricted funds ID. Only accepts letters, digits, periods, underscores and hyphens.<br>`maxLength: 60` | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `hold_method` | string (schema `RestrictedFundsHoldMethod`) | yes | Determines how the Pismo platform processes the restriction request in relation to the available balance at the time of execution.<br><br>Notes:<br>  - `STRICT` applies the full requested amount or fails (no partial holds).<br>  - `FLEXIBLE` can apply only the available portion, resulting in a partial hold.<br>  - `RECURRENT` behaves like `FLEXIBLE` at creation time. After creation, the restriction automatically applies to each incoming credit, re-restricting funds whenever a credit is posted, until the restriction reaches its target amount or `increase_datetime_limit` is reached. | enum: ["STRICT", "FLEXIBLE", "RECURRENT"]; default: "STRICT"; example: "STRICT" |
| `requested_amount` | number (schema `RestrictedFundsRequestedAmount`) | yes | Amount originally requested at the time the restriction was created; remains unchanged after the initial request. | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `held_amount` | number (schema `RestrictedFundsHeldAmount`) | yes | Amount held by restriction | format: "float"; minimum: 0; maximum: 100000000000000000 |
| `created_at` | string (schema `RestrictedFundsCreatedAt`) | yes | Date and time when the restriction was created, displayed in ISO 8601 format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `operations` | array of object (schema `RestrictedFundsOperation`) (schema `RestrictedFundsOperations`) | no | List of operations performed to restrict or release funds |  |
| `type` | string (schema `RestrictedFundsType`) | no | The type/nature of the restriction.<br><br>Notes:<br>  - `REGULATORY`: Restriction created for regulatory or operational reasons<br>  - `JUDICIAL`: Restriction created to comply with a judicial order | enum: ["REGULATORY", "JUDICIAL"]; default: "REGULATORY"; example: "REGULATORY" |
| `metadata` | object (schema `RestrictedFundsMainMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>This metadata applies when you don't send metadata for the restricted‑funds operation. It covers cases such as automatic recurrent operations or held‑funds expiration.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `increase_datetime_limit` | string (schema `RestrictedFundsIncreaseDatetimeLimit`) | no | The date and time limit, in RFC 3339 format, up to which a `RECURRENT` restriction continues applying to incoming credits on the account.<br><br>Notes:<br>  - Only accepted on creation when `hold_method` is `RECURRENT`<br>  - Must not be in the past | format: "date-time"; example: "2026-12-31T23:59:59Z" |

201 Example `example`:

```json
{
  "restricted_funds_id": "4a4060d5-3649-46e8-8d64-93949b212918",
  "hold_method": "FLEXIBLE",
  "requested_amount": 100.21,
  "held_amount": 99.9,
  "created_at": "2025-05-29T11:33:22Z",
  "operations": [
    {
      "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
      "type": "RESTRICT_FUNDS",
      "status": "SUCCEEDED",
      "processing_code": "PSM045",
      "soft_descriptor": "Funds restriction requested by FDIC 12 C.F.R. 360.9",
      "requested_amount": 100.21,
      "applied_amount": 99.9,
      "created_at": "2025-05-29T11:33:22Z",
      "applied_at": "2025-05-29T11:33:52Z",
      "metadata": {
        "key": "value"
      }
    }
  ]
}
```

##### Response 400

400 Example `Invalid JSON`:

```json
{
  "code": "WRFO0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Insufficient funds`:

```json
{
  "code": "WRFO0006",
  "message": "Insufficient funds"
}
```

400 Example `Invalid decimal places`:

```json
{
  "code": "WRFO0009",
  "message": "The number of decimal places is not compatible with the specified currency"
}
```

400 Example `Operation Blocked`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid account status`:

```json
{
  "code": "WRFO0011",
  "message": "Invalid account status"
}
```

400 Example `Account has not finished onboarding`:

```json
{
  "code": "WRFO0012",
  "message": "Account has not finished onboarding"
}
```

400 Example `Invalid account currency code`:

```json
{
  "code": "WRFO0013",
  "message": "Invalid account currency code: 999"
}
```

400 Example `Invalid restricted funds processing code`:

```json
{
  "code": "WRFO0014",
  "message": "Invalid restricted funds processing code"
}
```

400 Example `Increase datetime limit not allowed`:

```json
{
  "code": "WRFO0015",
  "message": "increase_datetime_limit is only allowed when hold_method is RECURRENT"
}
```

400 Example `Increase datetime limit in the past`:

```json
{
  "code": "WRFO0016",
  "message": "increase_datetime_limit cannot be in the past"
}
```

##### Response 401

401 Example `Unauthorized account`:

```json
{
  "code": "WRFO0010",
  "message": "Account not authorized"
}
```

##### Response 409

409 Example `Already exist`:

```json
{
  "code": "WRFO0004",
  "message": "Restricted funds already exist"
}
```

409 Example `Tracking ID already exist`:

```json
{
  "code": "WRFO0005",
  "message": "tracking_id is already in use"
}
```

##### Response 429

429 Example `Account locked`:

```json
{
  "code": "WRFO0003",
  "message": "Account is locked, please try again later"
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
| 400 | `WRFO0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WRFO0006` | Insufficient funds |
| 400 | `WRFO0009` | The number of decimal places is not compatible with the specified currency |
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WRFO0011` | Invalid account status |
| 400 | `WRFO0012` | Account has not finished onboarding |
| 400 | `WRFO0013` | Invalid account currency code: 999 |
| 400 | `WRFO0014` | Invalid restricted funds processing code |
| 400 | `WRFO0015` | increase_datetime_limit is only allowed when hold_method is RECURRENT |
| 400 | `WRFO0016` | increase_datetime_limit cannot be in the past |
| 401 | `WRFO0010` | Account not authorized |
| 409 | `WRFO0004` | Restricted funds already exist |
| 409 | `WRFO0005` | tracking_id is already in use |
| 429 | `WRFO0003` | Account is locked, please try again later |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `corporate-restricted-funds-1` | https://developers.pismo.io/events/docs/corporate-restricted-funds-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;409;429;500`, has examples `True`, emits events `4`, deprecated `False`.

Guides that link to this operation: `KU-BANK-file-based-processing`, `KU-BANK-restrictions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/restricted-funds/{restrictedFundsId} operationId=get-corporate-v1-restricted-funds -->
### `GET /corporate/v1/restricted-funds/{restrictedFundsId}` — Get fund restriction

- **operationId:** `get-corporate-v1-restricted-funds`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Restricted funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get details of a specific fund restriction by `restricted_funds_id`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `restrictedFundsId` | path | yes | string | Restricted funds ID | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `RestrictedFunds`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `restricted_funds_id` | string (schema `RestrictedFundsID`) | yes | Restricted funds ID. Only accepts letters, digits, periods, underscores and hyphens.<br>`maxLength: 60` | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `hold_method` | string (schema `RestrictedFundsHoldMethod`) | yes | Determines how the Pismo platform processes the restriction request in relation to the available balance at the time of execution.<br><br>Notes:<br>  - `STRICT` applies the full requested amount or fails (no partial holds).<br>  - `FLEXIBLE` can apply only the available portion, resulting in a partial hold.<br>  - `RECURRENT` behaves like `FLEXIBLE` at creation time. After creation, the restriction automatically applies to each incoming credit, re-restricting funds whenever a credit is posted, until the restriction reaches its target amount or `increase_datetime_limit` is reached. | enum: ["STRICT", "FLEXIBLE", "RECURRENT"]; default: "STRICT"; example: "STRICT" |
| `requested_amount` | number (schema `RestrictedFundsRequestedAmount`) | yes | Amount originally requested at the time the restriction was created; remains unchanged after the initial request. | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `held_amount` | number (schema `RestrictedFundsHeldAmount`) | yes | Amount held by restriction | format: "float"; minimum: 0; maximum: 100000000000000000 |
| `created_at` | string (schema `RestrictedFundsCreatedAt`) | yes | Date and time when the restriction was created, displayed in ISO 8601 format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `operations` | array of object (schema `RestrictedFundsOperation`) (schema `RestrictedFundsOperations`) | no | List of operations performed to restrict or release funds |  |
| `type` | string (schema `RestrictedFundsType`) | no | The type/nature of the restriction.<br><br>Notes:<br>  - `REGULATORY`: Restriction created for regulatory or operational reasons<br>  - `JUDICIAL`: Restriction created to comply with a judicial order | enum: ["REGULATORY", "JUDICIAL"]; default: "REGULATORY"; example: "REGULATORY" |
| `metadata` | object (schema `RestrictedFundsMainMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>This metadata applies when you don't send metadata for the restricted‑funds operation. It covers cases such as automatic recurrent operations or held‑funds expiration.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `increase_datetime_limit` | string (schema `RestrictedFundsIncreaseDatetimeLimit`) | no | The date and time limit, in RFC 3339 format, up to which a `RECURRENT` restriction continues applying to incoming credits on the account.<br><br>Notes:<br>  - Only accepted on creation when `hold_method` is `RECURRENT`<br>  - Must not be in the past | format: "date-time"; example: "2026-12-31T23:59:59Z" |

200 Example `example`:

```json
{
  "restricted_funds_id": "4a4060d5-3649-46e8-8d64-93949b212918",
  "hold_method": "FLEXIBLE",
  "requested_amount": 100.21,
  "held_amount": 0,
  "created_at": "2025-05-29T11:33:22Z",
  "operations": [
    {
      "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
      "type": "RESTRICT_FUNDS",
      "status": "SUCCEEDED",
      "processing_code": "PSM045",
      "soft_descriptor": "Funds restriction requested by FDIC 12 C.F.R. 360.9",
      "requested_amount": 100.21,
      "applied_amount": 99.9,
      "created_at": "2025-05-29T11:33:22Z",
      "applied_at": "2025-05-29T11:33:52Z",
      "metadata": {
        "key": "value"
      }
    },
    {
      "tracking_id": "4c9b7b9f-7959-40dc-9cf4-0019c1f12c7f",
      "type": "RELEASE_FUNDS",
      "status": "SUCCEEDED",
      "processing_code": "PSM047",
      "requested_amount": 99.9,
      "applied_amount": 99.9,
      "created_at": "2025-05-29T12:14:12Z",
      "applied_at": "2025-05-29T12:14:22Z",
      "metadata": {
        "key": "value"
      }
    }
  ]
}
```

##### Response 404

404 Example `Not found`:

```json
{
  "code": "WRFO0007",
  "message": "Restricted funds not found"
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
| 404 | `WRFO0007` | Restricted funds not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-restrictions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v1/restricted-funds/{restrictedFundsId} operationId=patch-corporate-v1-restricted-funds -->
### `PATCH /corporate/v1/restricted-funds/{restrictedFundsId}` — Release restriction

- **operationId:** `patch-corporate-v1-restricted-funds`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Restricted funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Releases all or part of the funds from an existing restriction by restricted funds ID.
>
> NOTE:
> - This endpoint requires an account token - an access token encoded with an external account ID. Tokens can expire quickly, which can result in a `401 Unauthorized` message.
> This endpoint generates the following events:
> - [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)
> - [Restricted Funds created or released](https://developers.pismo.io/events/docs/corporate-restricted-funds-1)
> - [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information on events and setting up event notifications.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `restrictedFundsId` | path | yes | string | Restricted funds ID | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `RestrictedFundsReleaseRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `RestrictedFundsAmount`) | yes | Amount requested by the operation<br><br>The final applied amount might vary (refer to `applied_amount`) based on execution rules and the available balance at the time of execution.<br><br><br>**Note**:<br>  * For `RESTRICT_FUNDS`, this is the amount to be held.<br>  * For `RELEASE_FUNDS`, this is the amount to be released.<br>  * For `EXECUTE_FUNDS`, this is the amount to be debited from the held funds.<br>  * Precision follows the currency's minor units. For example:<br>    * Two decimals (USD, EUR): values use increments of 0.01<br>    * Three decimals (BHD, JOD, KWD, OMR, TND): values use increments of 0.001<br>    * Four‑decimal (CLF): values use increments of 0.0001<br> | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `operation` | object (schema `RestrictedFundsRequestOperation`) | yes | Represents the data of the hold or release transaction. |  |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |

Example `example`:

```json
{
  "amount": 100.21,
  "operation": {
    "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
    "soft_descriptor": "Funds restriction requested by FDIC 12 C.F.R. 360.9",
    "metadata": {
      "key": "value"
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `RestrictedFunds`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 429 | Too many requests | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `restricted_funds_id` | string (schema `RestrictedFundsID`) | yes | Restricted funds ID. Only accepts letters, digits, periods, underscores and hyphens.<br>`maxLength: 60` | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `hold_method` | string (schema `RestrictedFundsHoldMethod`) | yes | Determines how the Pismo platform processes the restriction request in relation to the available balance at the time of execution.<br><br>Notes:<br>  - `STRICT` applies the full requested amount or fails (no partial holds).<br>  - `FLEXIBLE` can apply only the available portion, resulting in a partial hold.<br>  - `RECURRENT` behaves like `FLEXIBLE` at creation time. After creation, the restriction automatically applies to each incoming credit, re-restricting funds whenever a credit is posted, until the restriction reaches its target amount or `increase_datetime_limit` is reached. | enum: ["STRICT", "FLEXIBLE", "RECURRENT"]; default: "STRICT"; example: "STRICT" |
| `requested_amount` | number (schema `RestrictedFundsRequestedAmount`) | yes | Amount originally requested at the time the restriction was created; remains unchanged after the initial request. | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `held_amount` | number (schema `RestrictedFundsHeldAmount`) | yes | Amount held by restriction | format: "float"; minimum: 0; maximum: 100000000000000000 |
| `created_at` | string (schema `RestrictedFundsCreatedAt`) | yes | Date and time when the restriction was created, displayed in ISO 8601 format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `operations` | array of object (schema `RestrictedFundsOperation`) (schema `RestrictedFundsOperations`) | no | List of operations performed to restrict or release funds |  |
| `type` | string (schema `RestrictedFundsType`) | no | The type/nature of the restriction.<br><br>Notes:<br>  - `REGULATORY`: Restriction created for regulatory or operational reasons<br>  - `JUDICIAL`: Restriction created to comply with a judicial order | enum: ["REGULATORY", "JUDICIAL"]; default: "REGULATORY"; example: "REGULATORY" |
| `metadata` | object (schema `RestrictedFundsMainMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>This metadata applies when you don't send metadata for the restricted‑funds operation. It covers cases such as automatic recurrent operations or held‑funds expiration.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `increase_datetime_limit` | string (schema `RestrictedFundsIncreaseDatetimeLimit`) | no | The date and time limit, in RFC 3339 format, up to which a `RECURRENT` restriction continues applying to incoming credits on the account.<br><br>Notes:<br>  - Only accepted on creation when `hold_method` is `RECURRENT`<br>  - Must not be in the past | format: "date-time"; example: "2026-12-31T23:59:59Z" |

200 Example `example`:

```json
{
  "restricted_funds_id": "4a4060d5-3649-46e8-8d64-93949b212918",
  "hold_method": "FLEXIBLE",
  "requested_amount": 100.21,
  "held_amount": 99.9,
  "created_at": "2025-05-29T11:33:22Z",
  "operations": [
    {
      "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
      "type": "RESTRICT_FUNDS",
      "status": "SUCCEEDED",
      "processing_code": "PSM045",
      "soft_descriptor": "Funds restriction requested by FDIC 12 C.F.R. 360.9",
      "requested_amount": 100.21,
      "applied_amount": 99.9,
      "created_at": "2025-05-29T11:33:22Z",
      "applied_at": "2025-05-29T11:33:52Z",
      "metadata": {
        "key": "value"
      }
    },
    {
      "tracking_id": "4c9b7b9f-7959-40dc-9cf4-0019c1f12c7f",
      "type": "RELEASE_FUNDS",
      "status": "SUCCEEDED",
      "processing_code": "PSM047",
      "requested_amount": 99.9,
      "applied_amount": 99.9,
      "created_at": "2025-05-29T12:14:12Z",
      "applied_at": "2025-05-29T12:14:22Z",
      "metadata": {
        "key": "value"
      }
    }
  ]
}
```

##### Response 400

400 Example `Invalid JSON`:

```json
{
  "code": "WRFO0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Amount exceeds the held amount`:

```json
{
  "code": "WRFO0008",
  "message": "Release amount exceeds the currently held amount"
}
```

400 Example `Invalid decimal places`:

```json
{
  "code": "WRFO0009",
  "message": "The number of decimal places is not compatible with the specified currency"
}
```

400 Example `Operation Blocked`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid account status`:

```json
{
  "code": "WRFO0011",
  "message": "Invalid account status"
}
```

##### Response 409

409 Example `Tracking ID already exist`:

```json
{
  "code": "WRFO0005",
  "message": "tracking_id is already in use"
}
```

409 Example `Version conflict`:

```json
{
  "code": "WRFO0019",
  "message": "Restricted funds was concurrently modified"
}
```

##### Response 429

429 Example `Account locked`:

```json
{
  "code": "WRFO0003",
  "message": "Account is locked"
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
| 400 | `WRFO0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WRFO0008` | Release amount exceeds the currently held amount |
| 400 | `WRFO0009` | The number of decimal places is not compatible with the specified currency |
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WRFO0011` | Invalid account status |
| 409 | `WRFO0005` | tracking_id is already in use |
| 409 | `WRFO0019` | Restricted funds was concurrently modified |
| 429 | `WRFO0003` | Account is locked |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `corporate-restricted-funds-1` | https://developers.pismo.io/events/docs/corporate-restricted-funds-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;429;500`, has examples `True`, emits events `4`, deprecated `False`.

Guides that link to this operation: `KU-BANK-file-based-processing`, `KU-BANK-restrictions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v2/restricted-funds/{restrictedFundsId} operationId=patch-corporate-v2-restricted-funds -->
### `PATCH /corporate/v2/restricted-funds/{restrictedFundsId}` — Update restriction

- **operationId:** `patch-corporate-v2-restricted-funds`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Restricted funds`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> This endpoint combines the increase, release, and execution flows into a single typed operation.<br>
>
> It applies one operation to an existing fund restriction identified by `restricted_funds_id`. The operation type in `operation.type` determines how the held funds change:
>
>   * `RESTRICT_FUNDS`: increases the held amount of the restriction. A restriction with a zero held amount cannot be increased.
>
>   * `RELEASE_FUNDS`: releases all or part of the held funds back to the available_balance.
>
>   * `EXECUTE_FUNDS`: debits all or part of the held funds from the restriction.
>
> **NOTE**: This endpoint requires an account token, which is an access token encoded with an external account ID. Tokens expire quickly and can result in a `401 Unauthorized` message.
>
> This endpoint generates the following events:
> * [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1)
> * [Account ledger balance changed](https://developers.pismo.io/events/docs/availables-change-available-1)
> * [Restricted funds created, released, or executed](https://developers.pismo.io/events/docs/corporate-restricted-funds-1)
> * [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)
>
> See [Data and reporting](doc:data-reporting-overview) for more information on events and setting up event notifications.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `restrictedFundsId` | path | yes | string | Restricted funds ID | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `RestrictedFundsPatchV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `RestrictedFundsAmount`) | yes | Amount requested by the operation<br><br>The final applied amount might vary (refer to `applied_amount`) based on execution rules and the available balance at the time of execution.<br><br><br>**Note**:<br>  * For `RESTRICT_FUNDS`, this is the amount to be held.<br>  * For `RELEASE_FUNDS`, this is the amount to be released.<br>  * For `EXECUTE_FUNDS`, this is the amount to be debited from the held funds.<br>  * Precision follows the currency's minor units. For example:<br>    * Two decimals (USD, EUR): values use increments of 0.01<br>    * Three decimals (BHD, JOD, KWD, OMR, TND): values use increments of 0.001<br>    * Four‑decimal (CLF): values use increments of 0.0001<br> | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `operation` | object (schema `RestrictedFundsV2RequestOperation`) | yes | Represents the type and data of the operation to apply to the restriction |  |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |

Example `Increase restriction`:

```json
{
  "amount": 50,
  "operation": {
    "type": "RESTRICT_FUNDS",
    "tracking_id": "1b2c3d4e-5f60-4a7b-8c9d-0e1f2a3b4c5d",
    "soft_descriptor": "Additional hold requested by FDIC 12 C.F.R. 360.9",
    "metadata": {
      "key": "value"
    }
  }
}
```

Example `Release restriction`:

```json
{
  "amount": 100.21,
  "operation": {
    "type": "RELEASE_FUNDS",
    "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
    "soft_descriptor": "Funds release requested by FDIC 12 C.F.R. 360.9",
    "metadata": {
      "key": "value"
    }
  }
}
```

Example `Execute restriction`:

```json
{
  "amount": 100.21,
  "operation": {
    "type": "EXECUTE_FUNDS",
    "tracking_id": "4c9b7b9f-7959-40dc-9cf4-0019c1f12c7f",
    "soft_descriptor": "Judicial execution of restricted funds",
    "metadata": {
      "key": "value"
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `RestrictedFunds`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `ErrorResponse`) |
| 429 | Too many requests | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `restricted_funds_id` | string (schema `RestrictedFundsID`) | yes | Restricted funds ID. Only accepts letters, digits, periods, underscores and hyphens.<br>`maxLength: 60` | pattern: "^[A-Za-z0-9._-]+$"; maxLength: 60; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `hold_method` | string (schema `RestrictedFundsHoldMethod`) | yes | Determines how the Pismo platform processes the restriction request in relation to the available balance at the time of execution.<br><br>Notes:<br>  - `STRICT` applies the full requested amount or fails (no partial holds).<br>  - `FLEXIBLE` can apply only the available portion, resulting in a partial hold.<br>  - `RECURRENT` behaves like `FLEXIBLE` at creation time. After creation, the restriction automatically applies to each incoming credit, re-restricting funds whenever a credit is posted, until the restriction reaches its target amount or `increase_datetime_limit` is reached. | enum: ["STRICT", "FLEXIBLE", "RECURRENT"]; default: "STRICT"; example: "STRICT" |
| `requested_amount` | number (schema `RestrictedFundsRequestedAmount`) | yes | Amount originally requested at the time the restriction was created; remains unchanged after the initial request. | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `held_amount` | number (schema `RestrictedFundsHeldAmount`) | yes | Amount held by restriction | format: "float"; minimum: 0; maximum: 100000000000000000 |
| `created_at` | string (schema `RestrictedFundsCreatedAt`) | yes | Date and time when the restriction was created, displayed in ISO 8601 format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `operations` | array of object (schema `RestrictedFundsOperation`) (schema `RestrictedFundsOperations`) | no | List of operations performed to restrict or release funds |  |
| `type` | string (schema `RestrictedFundsType`) | no | The type/nature of the restriction.<br><br>Notes:<br>  - `REGULATORY`: Restriction created for regulatory or operational reasons<br>  - `JUDICIAL`: Restriction created to comply with a judicial order | enum: ["REGULATORY", "JUDICIAL"]; default: "REGULATORY"; example: "REGULATORY" |
| `metadata` | object (schema `RestrictedFundsMainMetadata`) | no | Key-value pairs containing data intended for storage in the Pismo system.<br><br><br>This metadata applies when you don't send metadata for the restricted‑funds operation. It covers cases such as automatic recurrent operations or held‑funds expiration.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> |  |
| `increase_datetime_limit` | string (schema `RestrictedFundsIncreaseDatetimeLimit`) | no | The date and time limit, in RFC 3339 format, up to which a `RECURRENT` restriction continues applying to incoming credits on the account.<br><br>Notes:<br>  - Only accepted on creation when `hold_method` is `RECURRENT`<br>  - Must not be in the past | format: "date-time"; example: "2026-12-31T23:59:59Z" |

200 Example `example`:

```json
{
  "restricted_funds_id": "4a4060d5-3649-46e8-8d64-93949b212918",
  "hold_method": "FLEXIBLE",
  "requested_amount": 100.21,
  "held_amount": 0,
  "created_at": "2025-05-29T11:33:22Z",
  "operations": [
    {
      "tracking_id": "9d15bfd1-5db9-4e96-b846-8d8707454430",
      "type": "RESTRICT_FUNDS",
      "status": "SUCCEEDED",
      "processing_code": "PSM045",
      "soft_descriptor": "Funds restriction requested by FDIC 12 C.F.R. 360.9",
      "requested_amount": 100.21,
      "applied_amount": 99.9,
      "created_at": "2025-05-29T11:33:22Z",
      "applied_at": "2025-05-29T11:33:52Z",
      "metadata": {
        "key": "value"
      }
    },
    {
      "tracking_id": "4c9b7b9f-7959-40dc-9cf4-0019c1f12c7f",
      "type": "EXECUTE_FUNDS",
      "status": "SUCCEEDED",
      "processing_code": "PSM164",
      "soft_descriptor": "Judicial execution of restricted funds",
      "requested_amount": 99.9,
      "applied_amount": 99.9,
      "created_at": "2025-05-29T12:14:12Z",
      "applied_at": "2025-05-29T12:14:22Z",
      "metadata": {
        "key": "value"
      }
    }
  ]
}
```

##### Response 400

400 Example `Invalid JSON`:

```json
{
  "code": "WRFO0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Insufficient funds`:

```json
{
  "code": "WRFO0006",
  "message": "Insufficient funds"
}
```

400 Example `Amount exceeds the held amount`:

```json
{
  "code": "WRFO0008",
  "message": "Requested amount exceeds the currently held amount"
}
```

400 Example `Invalid decimal places`:

```json
{
  "code": "WRFO0009",
  "message": "The number of decimal places is not compatible with the specified currency"
}
```

400 Example `Operation Blocked`:

```json
{
  "code": "WOBK0007",
  "message": "Operations blocked for account"
}
```

400 Example `Invalid account status`:

```json
{
  "code": "WRFO0011",
  "message": "Invalid account status"
}
```

##### Response 401

401 Example `Account not authorized`:

```json
{
  "code": "WRFO0010",
  "message": "Account not authorized"
}
```

##### Response 404

404 Example `Not found`:

```json
{
  "code": "WRFO0007",
  "message": "Restricted funds not found"
}
```

##### Response 409

409 Example `Tracking ID already exist`:

```json
{
  "code": "WRFO0005",
  "message": "tracking_id is already in use"
}
```

409 Example `Version conflict`:

```json
{
  "code": "WRFO0019",
  "message": "Restricted funds was concurrently modified"
}
```

##### Response 422

422 Example `Cannot increase restriction with zero held amount`:

```json
{
  "code": "WRFO0017",
  "message": "Cannot increase a restriction with zero held amount"
}
```

##### Response 429

429 Example `Account locked`:

```json
{
  "code": "WRFO0003",
  "message": "Account is locked"
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
| 400 | `WRFO0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WRFO0006` | Insufficient funds |
| 400 | `WRFO0008` | Requested amount exceeds the currently held amount |
| 400 | `WRFO0009` | The number of decimal places is not compatible with the specified currency |
| 400 | `WOBK0007` | Operations blocked for account |
| 400 | `WRFO0011` | Invalid account status |
| 401 | `WRFO0010` | Account not authorized |
| 404 | `WRFO0007` | Restricted funds not found |
| 409 | `WRFO0005` | tracking_id is already in use |
| 409 | `WRFO0019` | Restricted funds was concurrently modified |
| 422 | `WRFO0017` | Cannot increase a restriction with zero held amount |
| 429 | `WRFO0003` | Account is locked |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-change-1 |
| `availables-change-available-1` | https://developers.pismo.io/events/docs/availables-change-available-1 |
| `corporate-restricted-funds-1` | https://developers.pismo.io/events/docs/corporate-restricted-funds-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;409;422;429;500`, has examples `True`, emits events `4`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/Pagination -->
### Schema `Pagination`

Pointer: `#/components/schemas/Pagination`. Type: object (schema `Pagination`).

> Data related to list pagination using a cursor.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `cursor` | string (schema `Cursor`) | no | Cursor pointing to the next page of results | example: "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0=" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/RestrictedFundsRequestOperation -->
### Schema `RestrictedFundsRequestOperation`

Pointer: `#/components/schemas/RestrictedFundsRequestOperation`. Type: object (schema `RestrictedFundsRequestOperation`).

> Represents the data of the hold or release transaction.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `metadata` | object (schema `Metadata`) | no | Key-value pairs that contain data intended for storage on the Pismo platform.<br><br><br>**Note**: The `metadata` field includes a `corporate_metadata` object with the following attributes:<br><br>  * `credit_external_account_id`: present when supplied in the credit leg.<br><br>  * `debit_external_account_id`: present when supplied in the debit leg.<br><br>  * `earmark_id`: present when supplied in the debit leg.<br><br>  The `corporate_metadata` attribute must be an object. A type mismatch results in an error as described in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"my-id": 2932} |

<!-- schema: #/components/schemas/RestrictedFundsOperation -->
### Schema `RestrictedFundsOperation`

Pointer: `#/components/schemas/RestrictedFundsOperation`. Type: object (schema `RestrictedFundsOperation`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `type` | string (schema `RestrictedFundsOperationType`) | yes | Represents the kind of financial operation being performed.<br>Indicates whether the operation increased a funds restriction, released funds, or executed (debited) held funds.<br> | enum: ["RESTRICT_FUNDS", "RELEASE_FUNDS", "EXECUTE_FUNDS"]; example: "RELEASE_FUNDS" |
| `status` | string (schema `RestrictedFundsOperationStatus`) | yes | Indicates the operation’s current execution state<br> | enum: ["PROCESSING", "SUCCEEDED", "FAILED", "TIMED_OUT"]; example: "SUCCEEDED" |
| `processing_code` | string (schema `RestrictedFundsProcessingCode`) | yes | Processing code used to create the underlying transaction. Each operation type uses a default processing code.<br><br>`minLength: 1`<br>`maxLength: 6`<br> | minLength: 1; maxLength: 6; example: "PSM045" |
| `requested_amount` | number (schema `RestrictedFundsAmount`) | yes | Amount requested by the operation<br><br>The final applied amount might vary (refer to `applied_amount`) based on execution rules and the available balance at the time of execution.<br><br><br>**Note**:<br>  * For `RESTRICT_FUNDS`, this is the amount to be held.<br>  * For `RELEASE_FUNDS`, this is the amount to be released.<br>  * For `EXECUTE_FUNDS`, this is the amount to be debited from the held funds.<br>  * Precision follows the currency's minor units. For example:<br>    * Two decimals (USD, EUR): values use increments of 0.01<br>    * Three decimals (BHD, JOD, KWD, OMR, TND): values use increments of 0.001<br>    * Four‑decimal (CLF): values use increments of 0.0001<br> | format: "float"; minimum: 0.0001; maximum: 100000000000000000 |
| `applied_amount` | number (schema `RestrictedFundsAppliedAmount`) | yes | Amount actually executed by the operation at the time it was applied<br><br>Depending on the `hold_method`, this value might be different from `requested_amount`.<br><br>Hold method:<br>  * `STRICT` holds require the full requested amount. If that amount cannot be held, the operation fails.<br>  * `FLEXIBLE` might apply only the available portion<br><br>Type:<br>  - For `RESTRICT_FUNDS`, it is the portion of the requested amount that was successfully held.<br>  - For `RELEASE_FUNDS`, it is the portion that was actually released back to the available balance.<br>  - For `EXECUTE_FUNDS`, it is the portion of the held funds that was actually debited from the restricted amount.<br> | format: "float"; minimum: 0; maximum: 100000000000000000; multipleOf: 0.0001; example: 800.22 |
| `created_at` | string (schema `RestrictedFundsCreatedAt`) | yes | Date and time when the restriction was created, displayed in ISO 8601 format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `applied_at` | string (schema `RestrictedFundsAppliedAt`) | no | Date and time when the financial operation was actually executed, displayed in ISO 8601 format.<br><br>`minLength: 1`<br>`maxLength: 30`<br> | format: "date-time"; minLength: 1; maxLength: 30; example: "2023-04-27T12:01:24Z" |
| `metadata` | object (schema `Metadata`) | no | Key-value pairs that contain data intended for storage on the Pismo platform.<br><br><br>**Note**: The `metadata` field includes a `corporate_metadata` object with the following attributes:<br><br>  * `credit_external_account_id`: present when supplied in the credit leg.<br><br>  * `debit_external_account_id`: present when supplied in the debit leg.<br><br>  * `earmark_id`: present when supplied in the debit leg.<br><br>  The `corporate_metadata` attribute must be an object. A type mismatch results in an error as described in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"my-id": 2932} |

<!-- schema: #/components/schemas/RestrictedFundsV2RequestOperation -->
### Schema `RestrictedFundsV2RequestOperation`

Pointer: `#/components/schemas/RestrictedFundsV2RequestOperation`. Type: object (schema `RestrictedFundsV2RequestOperation`).

> Represents the type and data of the operation to apply to the restriction

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string (schema `RestrictedFundsV2OperationType`) | yes | Type of operation applied to an existing restriction<br><br>**Note**:<br>  * `RESTRICT_FUNDS`: increases the held amount of the existing restriction.<br>  * `RELEASE_FUNDS`: releases all or part of the held funds back to the available balance.<br>  * `EXECUTE_FUNDS`: debits all or part of the held funds against the restriction.<br> | enum: ["RESTRICT_FUNDS", "RELEASE_FUNDS", "EXECUTE_FUNDS"]; example: "EXECUTE_FUNDS" |
| `tracking_id` | string (schema `TrackingID`) | yes | A unique payment tracking number provided by the client. If an existing `tracking_id` is found on the Pismo platform, the API returns a `409` error.<br><br>This field is:<br>  * Unique within the organization<br>  * Immutable: It can't be updated<br>  * Not recyclable: You can't reuse a `tracking_id`<br> | minLength: 1; maxLength: 43; example: "0a50c88a-ade8-4bcc-a639-9a0b0f11e244" |
| `soft_descriptor` | string (schema `RestrictedFundsSoftDescriptor`) | no | Brief description that helps identify a restriction | minLength: 0; maxLength: 100; example: "FDIC 12 C.F.R. § 360.9" |
| `metadata` | object (schema `Metadata`) | no | Key-value pairs that contain data intended for storage on the Pismo platform.<br><br><br>**Note**: The `metadata` field includes a `corporate_metadata` object with the following attributes:<br><br>  * `credit_external_account_id`: present when supplied in the credit leg.<br><br>  * `debit_external_account_id`: present when supplied in the debit leg.<br><br>  * `earmark_id`: present when supplied in the debit leg.<br><br>  The `corporate_metadata` attribute must be an object. A type mismatch results in an error as described in the responses section.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"my-id": 2932} |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Restricted funds`: GET /corporate/v1/restricted-funds, POST /corporate/v1/restricted-funds, GET /corporate/v1/restricted-funds/{restrictedFundsId}, PATCH /corporate/v1/restricted-funds/{restrictedFundsId}, PATCH /corporate/v2/restricted-funds/{restrictedFundsId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-file-based-processing` — File-based processing, file signature and encryption
- `KU-BANK-restrictions` — Restrictions: restrict funds, restriction management and operation blocks
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-ERR-codes-wrfo` — Error codes: WRFO
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
