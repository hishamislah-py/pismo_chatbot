---
ku_id: KU-API-core-platform-balances-and-limits--account-balances
title: 'API reference: Core platform - Balances and limits — Account balances'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Balances_and_limits.yaml
  sha256: d7c0d6ed8ee05ff104a1b39a1ebfef06bc337f71776f0baf9b29633ffe36ca0a
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
- get-v1-account-balance
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-account-balance-definitions-for-transaction-banking
- KU-CORE-accounts-overview
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wiac-to-wstm
- KU-PAY-hold-funds
specification_version: 1.0.0
---

# API reference: Core platform - Balances and limits — Account balances

**KU ID:** `KU-API-core-platform-balances-and-limits--account-balances` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Account balances` in `api-specs/Core_platform_-_Balances_and_limits.yaml` (“Core platform - Balances and limits”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage daily balances.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/daily-balances` | `get-v1-account-balance` | Get daily account balance limits | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Balances_and_limits.yaml method=GET path=/v1/accounts/{accountId}/daily-balances operationId=get-v1-account-balance -->
### `GET /v1/accounts/{accountId}/daily-balances` — Get daily account balance limits

- **operationId:** `get-v1-account-balance`
- **Specification:** `api-specs/Core_platform_-_Balances_and_limits.yaml` (Core platform - Balances and limits)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balances-limits`
- **Tags:** `Account balances`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get daily account balance limits for a date range. By default, if only the account ID is specified, the range is 10 days: from 10 days before yesterday's date to yesterday.
>
> You can query the account balance limits as far back as 515 days before the current date and for a maximum range of 90 days. You can't query for today's date.
>
> Refer to the [Get daily account balance limits](doc:accounts-overview#get-daily-account-balance-limits) section in the Accounts guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | number | Account ID | example: 123456 |
| `beginDate` | query | no | string | Beginning date to filter account balances in the yyyy-mm-dd format. This date must be before or equal to `endDate`. If the value is not sent in the request, the default is endDate - 10 days. | format: "date"; example: "2022-01-02" |
| `endDate` | query | no | string | Ending date to filter account balances in the yyyy-mm-dd format. This date must be after or equal to the beginDate and it must be in the past, yesterday or earlier. Only full/complete days are considered. If the value is not sent in the request, the default is yesterday's date (current date - 1 day). | format: "date"; example: "2022-01-05" |
| `perPage` | query | no | integer | Number of entries per page. If the value is not sent in the request, the default value is `10`. | default: 10; example: 10 |
| `page` | query | no | integer | Page number of results to return. If the value is not sent in the request, the default value is `1`. | default: 1; example: 1 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountBalanceResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error. | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer | no | Total number of pages | example: 3 |
| `current_page` | integer | no | Current page of the pagination | example: 1 |
| `per_page` | integer | no | Amount of items that should be returned on each page | example: 1 |
| `total_items` | integer | no | Total amount of items available | example: 3 |
| `items` | array of oneOf: object (schema `AccountBalance`) | no | Array of available entries |  |

##### Response 400

400 Example `validation error` — from `#/components/examples/validationError`:

```json
{
  "message": "Error validating input",
  "code": "WBLS0005"
}
```

400 Example `daily balance error` — from `#/components/examples/dailyBalanceValidationError`:

```json
{
  "message": "Error when parsing the beginDate and/or endDate",
  "code": "WLDG0021"
}
```

##### Response 500

500 Example `system error` — from `#/components/examples/genericSystemError`:

```json
{
  "message": "Internal error found, please contact the administrator",
  "code": "EBLS9999"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBLS0005` | Error validating input |
| 400 | `WLDG0021` | Error when parsing the beginDate and/or endDate |
| 500 | `EBLS9999` | Internal error found, please contact the administrator |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-account-balance-definitions-for-transaction-banking`, `KU-CORE-accounts-overview`, `KU-PAY-hold-funds`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountBalance -->
### Schema `AccountBalance`

Pointer: `#/components/schemas/AccountBalance`. Type: object (schema `AccountBalance`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | number | no | Account ID where the operation is performed | example: 1234 |
| `org_id` | string | no | Org ID where the account exists | example: "08102A0B-D4F8-42A2-8B0E-2052D05577D7" |
| `ref_date` | string | no | Date of the balance | format: "date"; example: "2022-01-02" |
| `available_credit_limit` | number | no | Initial available credit limit of the account. | example: 1500.5 |
| `available_total_installment_credit` | number | no | Amount available for installments in the credit account. | example: 1000.3 |
| `available_withdrawal_credit` | number | no | Amount available for withdrawal in the credit account. | example: 2000.6 |
| `available_savings_account_limit` | number | no | Available limit of the savings account. | example: 2700.34 |
| `held_funds` | number | no | Funds held on the account. Usually, but not always, this occurs due to a legal action. | example: 10.34 |
| `currency_code` | string | no | ISO-4217 alphabetic code (3 characters) for transaction currency. | example: "BRL" |
| `currency_numeric_code` | string | no | ISO-4217 numeric code (3 digits) for transaction currency. | example: "986" |

<!-- schema: #/components/schemas/ErrorModel -->
### Schema `ErrorModel`

Pointer: `#/components/schemas/ErrorModel`. Type: object (schema `ErrorModel`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message that describes the error. | example: "An Internal Server Error found, please contact the administrator" |
| `code` | string | no | Code that identifies the error type. | example: "EBLS9999" |
| `details` | array of object (schema `ErrorDetails`) | no |  |  |

<!-- schema: #/components/schemas/ErrorDetails -->
### Schema `ErrorDetails`

Pointer: `#/components/schemas/ErrorDetails`. Type: object (schema `ErrorDetails`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `location` | string | no | Location describes the attribute when the error is present | example: "payload.attribute" |
| `message` | string | no | Message that describes the error detail | example: "attribute is null" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Balances_and_limits.yaml` | tag `Account balances`: GET /v1/accounts/{accountId}/daily-balances | https://github.com/PismoDevEx/pismo-api-specs | `d7c0d6ed8ee05ff1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-account-balance-definitions-for-transaction-banking` — Account balance definitions for transaction banking
- `KU-CORE-accounts-overview` — Accounts
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-PAY-hold-funds` — Hold funds
