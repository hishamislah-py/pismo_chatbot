---
ku_id: KU-API-banking-interest-bearing-accounts--average-balance
title: 'API reference: Banking - Interest-bearing accounts — Average balance'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Interest-bearing_accounts.yaml
  sha256: 89fc3f8ed0222a57b553ff94305ed0b9cb03db5dd58afd0c3f23ba1474ec87a2
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
- interest-bearing-get-average-balance
- interest-bearing-calculate-average-balance
related_kus:
- KU-BANK-banking-overview
- KU-ERR-codes-eibacc
- KU-EVT-catalogue-other-domains
specification_version: 1.0.0
---

# API reference: Banking - Interest-bearing accounts — Average balance

**KU ID:** `KU-API-banking-interest-bearing-accounts--average-balance` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Average balance` in `api-specs/Banking_-_Interest-bearing_accounts.yaml` (“Banking - Interest-bearing accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that enable calculating average balances for an account

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/average-balance` | `interest-bearing-get-average-balance` | Get average balance | no |
| `POST /v1/accounts/{accountId}/average-balance` | `interest-bearing-calculate-average-balance` | Calculate average balance | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=GET path=/v1/accounts/{accountId}/average-balance operationId=interest-bearing-get-average-balance -->
### `GET /v1/accounts/{accountId}/average-balance` — Get average balance

- **operationId:** `interest-bearing-get-average-balance`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Average balance`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get an already calculated average balance for an account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `idempotency` | header | yes | string | A unique identifier for the request. If you need to retry a request, use the same idempotency key to avoid creating duplicate resources.<br> | example: "123e4567-e89b-12d3-a456-426614174000" |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `GetAverageBalanceResponse`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | number | no | Account ID. | example: 123456 |
| `external_account_id` | string | no | External account ID resolved from the account context. Returned when available, including while the calculation status is `PROCESSING`. | example: "ext-acct-001" |
| `begin_date_datetime` | string | no | The date and time when the calculation begins. The date and time are displayed in RFC 3339 format, for example: `2024-01-28T10:33:01Z`.<br> | format: "date-time"; example: "2024-01-28T10:33:01.000Z" |
| `end_date_datetime` | string | no | The date and time when the calculation ends. The date and time are displayed in RFC 3339 format, for example: `2024-01-29T10:33:01Z`.<br> | format: "date-time"; example: "2024-01-30T10:33:01.000Z" |
| `balance_types_to_calculate` | array of string | no | Choose a balance to calculate its average balance, you can select multiple balance types to calculate their average balances simultaneously. The balance types are:<br><br>* `available`<br>* `savings`<br>* `held_funds`<br> example: [ "AVAILABLE", "SAVINGS", "HELD_FUNDS" ]<br> | items.enum: ["AVAILABLE", "SAVINGS", "HELD_FUNDS"] |

##### Response 400

400 Example `invalidRequestBody` (Bad Request):

```json
{
  "code": "EIBACC0008",
  "message": "Bad Request",
  "details": "error EIBACC0008: Validation error [(Field 'Order' is invalid)]"
}
```

##### Response 404

404 Example `invalidRequestBody` (Bad Request):

```json
{
  "code": "EIBACC0064",
  "message": "Product not found"
}
```

##### Response 500

500 Example `internalProcessingError` (Internal processing error):

```json
{
  "code": "EIBACC0007",
  "message": "Internal error",
  "detail": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBACC0008` | Bad Request |
| 404 | `EIBACC0064` | Product not found |
| 500 | `EIBACC0007` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-overview`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/accounts/{accountId}/average-balance operationId=interest-bearing-calculate-average-balance -->
### `POST /v1/accounts/{accountId}/average-balance` — Calculate average balance

- **operationId:** `interest-bearing-calculate-average-balance`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Average balance`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Calculate an average balance for an account.<br>
> Using this endpoint, you specify a datetime range and calculate the [average balance](https://www.investopedia.com/terms/a/average-balance.asp) of an account for that period. The calculation multiplies each unchanged balance by the number of days it remains constant, sums those values, and divides the total by the number of days in the selected range.<br>
> This endpoint generates the [Average balance calculated](https://developers.pismo.io/events/docs/average-balance-calculated-average-balance-1) event once calculation is complete.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `idempotency` | header | yes | string | A unique identifier for the request. If you need to retry a request, use the same idempotency key to avoid creating duplicate resources.<br> | example: "123e4567-e89b-12d3-a456-426614174000" |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `CalculateAverageBalanceRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `begin_date_datetime` | string | no | The specified datetime when the average balance calculation begins. The datetime is displayed in the RFC 3339 format; for example: `2024-01-28T10:33:01Z`.<br> | format: "date-time"; example: "2024-01-28T10:33:01.000Z" |
| `end_date_datetime` | string | no | The specified datetime when the average balance calculation ends. The datetime is displayed in the RFC 3339 format; for example: `2024-01-29T10:33:01Z`.<br> | format: "date-time"; example: "2024-01-30T10:33:01.000Z" |
| `balance_types_to_calculate` | array of string | no | Choose a balance to calculate its average balance, you can select multiple balance types to calculate their average balances simultaneously. The balance types are:<br><br>* `available`<br>* `savings`<br>* `held_funds`<br> | example: ["available", "savings", "held_funds"]; items.enum: ["available", "savings", "held_funds"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Accepted | `application/json`: object (schema `CalculateAverageBalanceResponse`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | number | no | Account ID. | example: 123456 |
| `idempotency_key` | string | no | Idempotency key. | example: "123e4567-e89b-12d3-a456-xyz" |
| `status` | string | no | Status of the average balance calculation request. | enum: ["PROCESSING", "COMPLETE"] |
| `message` | string | no | Message. | example: "Request is under progress" |

##### Response 400

400 Example `invalidRequestBody` (Bad Request):

```json
{
  "code": "EIBACC0008",
  "message": "Bad Request",
  "details": "error EIBACC0008: Validation error [(Field 'Order' is invalid)]"
}
```

##### Response 404

404 Example `invalidRequestBody` (Bad Request):

```json
{
  "code": "EIBACC0064",
  "message": "Product not found"
}
```

##### Response 409

409 Example `conflict` (Conflict):

```json
{
  "code": "EIBACC0114",
  "message": "Product is already detached"
}
```

##### Response 500

500 Example `internalProcessingError` (Internal processing error):

```json
{
  "code": "EIBACC0007",
  "message": "Internal error",
  "detail": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBACC0008` | Bad Request |
| 404 | `EIBACC0064` | Product not found |
| 409 | `EIBACC0114` | Product is already detached |
| 500 | `EIBACC0007` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `average-balance-calculated-average-balance-1` | https://developers.pismo.io/events/docs/average-balance-calculated-average-balance-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;404;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-banking-overview`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code | example: "EIBACC0003" |
| `details` | string | no | Error details | example: "error EIBACC0008: Validation error [(Field 'Order' is invalid)]" |
| `message` | string | no | Error message | example: "Bad Request" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Interest-bearing_accounts.yaml` | tag `Average balance`: GET /v1/accounts/{accountId}/average-balance, POST /v1/accounts/{accountId}/average-balance | https://github.com/PismoDevEx/pismo-api-specs | `89fc3f8ed0222a57…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-banking-overview` — Banking overview
- `KU-ERR-codes-eibacc` — Error codes: EIBACC
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
