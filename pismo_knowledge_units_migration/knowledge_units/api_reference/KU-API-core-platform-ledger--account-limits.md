---
ku_id: KU-API-core-platform-ledger--account-limits
title: 'API reference: Core platform - Ledger — Account limits'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Ledger.yaml
  sha256: 3ee8fcb5a752cb17b11d88a7026a1b41bf15ab23c16d2e654c533edb3ea1e7f6
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
- get-v1-account-limit
- patch-v1-account-limit
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-account-balance-definitions-for-transaction-banking
- KU-BANK-how-overdraft-works
- KU-CARD-rule-list-part-03
- KU-CORE-over-limit-fee
- KU-CORE-program-limits
- KU-CORE-working-with-limits-objects
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-wiac-to-wstm
- KU-EVT-accounts-data-events
- KU-EVT-catalogue-other-domains
- KU-EVT-ledger-data-events
- KU-PAY-hold-funds
specification_version: 1.0.0
---

# API reference: Core platform - Ledger — Account limits

**KU ID:** `KU-API-core-platform-ledger--account-limits` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Account limits` in `api-specs/Core_platform_-_Ledger.yaml` (“Core platform - Ledger”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage account limits

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/limits` | `get-v1-account-limit` | List account limits | no |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limit` | Update account limits (outdated) | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Ledger.yaml method=GET path=/v1/accounts/{accountId}/limits operationId=get-v1-account-limit -->
### `GET /v1/accounts/{accountId}/limits` — List account limits

- **operationId:** `get-v1-account-limit`
- **Specification:** `api-specs/Core_platform_-_Ledger.yaml` (Core platform - Ledger)
- **Server base URL(s):** `https://sandbox.pismolabs.io/ledger`
- **Tags:** `Account limits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List available limits on the account. 
>
> Refer to the [Account limits](doc:working-with-limits-objects) guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | number | Account ID | example: 123456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountLimitGet`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `max_credit_limit` | number | no | Maximum credit amount approved for this account. | example: 800.01 |
| `available_total_installment_credit` | number | no | Amount available for installments in the credit account. | example: 1000.31 |
| `available_withdrawal_credit` | number | no | Amount available for withdrawal in the credit account. | example: 500.01 |
| `available_savings_account_limit` | number | no | Available limit of the savings account. | example: 10.11 |
| `total_overdraft_limit` | number | no | Maximum limit for over draft spending on the account. | example: 345.61 |
| `total_installment_credit_limit` | number | no | Amount limit for installments in the credit account. | example: 145.78 |
| `total_credit_limit` | number | no | Total credit limit as set by the user. This can be any value up to the `max_credit_limit`. | example: 15.51 |
| `percentage_over_limit` | number | no | Percentage of the maximum credit limit (`max_credit_limit`) made available for purchases over the credit limit on the account. | example: 15.5 |
| `available_monthly_credit` | number | no | Monthly amount available in the credit account. | example: 10000.31 |
| `available_credit_limit` | number | no | Initial available credit limit of the account. | example: 712.02 |
| `monthly_credit_limit` | number | no | Monthly credit limit amount on the account. | example: 324.82 |
| `held_funds` | number | no | Funds held or blocked on the account. | example: 50.01 |
| `additional_funds` | number | no | Additional funds that can be used when needed to supplement credit limit, held funds, or other funds. | example: 100.5 |
| `withdrawal_credit_limit` | number | no | Amount limit for withdrawal in credit programs. | example: 10.34 |
| `currency_code` | string | no | ISO-4217 alphabetic code (3 characters) for transaction currency. | example: "BRL" |
| `currency_numeric_code` | string | no | ISO-4217 numeric code (3 digits) for transaction currency. | example: "986" |

##### Response 400

400 Example `invalidAccountId` (Invalid AccountID):

```json
{
  "code": "WLDG0020",
  "message": "Error parsing accountID to integer number"
}
```

##### Response 404

404 Example `noAccountLimitsFound` (Account not found):

```json
{
  "code": "WLDG0022",
  "message": "No account limits found"
}
```

##### Response 500

500 Example `internalServerError` (Internal Server Error):

```json
{
  "code": "ELDG9999",
  "message": "An Internal Server Error found, please contact the administrator passing the code"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WLDG0020` | Error parsing accountID to integer number |
| 404 | `WLDG0022` | No account limits found |
| 500 | `ELDG9999` | An Internal Server Error found, please contact the administrator passing the code |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-account-balance-definitions-for-transaction-banking`, `KU-CARD-rule-list-part-03`, `KU-CORE-working-with-limits-objects`, `KU-PAY-hold-funds`.

<!-- op: spec=api-specs/Core_platform_-_Ledger.yaml method=PATCH path=/v1/accounts/{accountId}/limits operationId=patch-v1-account-limit -->
### `PATCH /v1/accounts/{accountId}/limits` — Update account limits (outdated)

- **operationId:** `patch-v1-account-limit`
- **Specification:** `api-specs/Core_platform_-_Ledger.yaml` (Core platform - Ledger)
- **Server base URL(s):** `https://sandbox.pismolabs.io/ledger`
- **Tags:** `Account limits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update account limits. 
>
> This endpoint does not validate the account limit against the program’s global limit. To validate the account limit against the program’s global limit, use the [Update account limits](ref:patch-v1-account-limits) endpoint.
>
> This endpoint generates the [Account limit changed](https://developers.pismo.io/events/docs/ledger-limit-changed-1) event.
>
> Refer to the [Account limits](doc:working-with-limits-objects) guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | number | Account ID | example: 123456 |

#### Request body

Required: yes

> Body description to update limits

**Content type `application/json`** — schema: object (schema `AccountLimitPatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `max_credit_limit` | number | no | Maximum credit amount approved for this account. This value must not be less than the `total_credit_limit` or the program’s minimum credit limit parameter, and must not exceed the program’s maximum credit limit parameter. The ledger stores and reports this amount using the exact number of decimal places provided in the request payload. | example: 800.01 |
| `total_credit_limit` | number | no | Total credit limit as set by the user. This can be any value up to the `max_credit_limit`. The ledger stores and reports the amount using the same number of decimal places as supplied in the request payload. | example: 15.51 |
| `total_overdraft_limit` | number | no | Maximum limit amount for overdraft spending on the account. The ledger stores and reports the amount using the same number of decimal places as supplied in the request payload. | example: 340.61 |
| `percentage_over_limit` | number | no | Percentage of the maximum credit limit (`max_credit_limit`) made available for purchases over the credit limit on the account. | example: 15.5 |
| `total_installment_credit_limit` | number | no | Amount limit for installments on this credit account. This value must not exceed the program’s maximum credit limit parameter. The ledger stores and reports this amount using the exact number of decimal places provided in the request payload. | example: 145.78 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No content |  |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorModel`) |

##### Response 400

400 Example `invalidBody` (Invalid body):

```json
{
  "code": "WLDG0021",
  "message": "Invalid body"
}
```

400 Example `parseError` (Parse error):

```json
{
  "code": "WLDG0010",
  "message": "Error when binding request body: code=400, message=error decoding string 'asd': can't convert asd to decimal"
}
```

400 Example `maxCreditLimitIsLowerThanTotalCreditLimitError` (Max credit limit lower than total credit limit):

```json
{
  "code": "WLDG0025",
  "message": "Max credit limit 9000 must be greater than total credit limit 10000"
}
```

400 Example `totalCreditLimitIsGreaterThanMaxCreditLimitError` (Total credit limit exceeds max credit limit):

```json
{
  "code": "WLDG0025",
  "message": "Total credit limit 14000 exceeds max credit limit 13000"
}
```

400 Example `maxCreditLimitExceedsMaxGlobalLimitError` (Max credit limit exceeds max global limit):

```json
{
  "code": "WLDG0025",
  "message": "Max credit limit 20000 exceeds max global limit 15000"
}
```

400 Example `totalCreditLimitExceedsMinGlobalLimitError` (Total credit limit lower than min global limit):

```json
{
  "code": "WLDG0025",
  "message": "Total credit limit 100 is less than min global limit 350"
}
```

##### Response 404

404 Example `noAccountLimitsFound` (Account not found):

```json
{
  "code": "WLDG0022",
  "message": "No account limits found"
}
```

##### Response 500

500 Example `internalServerError` (Internal Server Error):

```json
{
  "code": "ELDG9999",
  "message": "An Internal Server Error found, please contact the administrator passing the code"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WLDG0021` | Invalid body |
| 400 | `WLDG0010` | Error when binding request body: code=400, message=error decoding string 'asd': can't convert asd to decimal |
| 400 | `WLDG0025` | Max credit limit 9000 must be greater than total credit limit 10000 |
| 404 | `WLDG0022` | No account limits found |
| 500 | `ELDG9999` | An Internal Server Error found, please contact the administrator passing the code |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `ledger-limit-changed-1` | https://developers.pismo.io/events/docs/ledger-limit-changed-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-how-overdraft-works`, `KU-CORE-over-limit-fee`, `KU-CORE-program-limits`, `KU-CORE-working-with-limits-objects`, `KU-EVT-accounts-data-events`, `KU-EVT-ledger-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error code |  |
| `message` | string | no | Message that describes the error |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Ledger.yaml` | tag `Account limits`: GET /v1/accounts/{accountId}/limits, PATCH /v1/accounts/{accountId}/limits | https://github.com/PismoDevEx/pismo-api-specs | `3ee8fcb5a752cb17…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-account-balance-definitions-for-transaction-banking` — Account balance definitions for transaction banking
- `KU-BANK-how-overdraft-works` — How overdraft works
- `KU-CARD-rule-list-part-03` — Rule list (part 3 of 4)
- `KU-CORE-over-limit-fee` — Over-limit fees
- `KU-CORE-program-limits` — Program limits
- `KU-CORE-working-with-limits-objects` — Account limits
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-ledger-data-events` — Core platform - Ledger
- `KU-PAY-hold-funds` — Hold funds
