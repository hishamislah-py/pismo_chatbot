---
ku_id: KU-API-core-platform-balances-and-limits--related-accounts
title: 'API reference: Core platform - Balances and limits — Related accounts'
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
- get-v1-accounts-limits-related-accounts
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-CORE-accounts-overview
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
specification_version: 1.0.0
---

# API reference: Core platform - Balances and limits — Related accounts

**KU ID:** `KU-API-core-platform-balances-and-limits--related-accounts` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Related accounts` in `api-specs/Core_platform_-_Balances_and_limits.yaml` (“Core platform - Balances and limits”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage related accounts.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounts/{accountId}/related-accounts-limits` | `get-v1-accounts-limits-related-accounts` | Get related accounts | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Balances_and_limits.yaml method=GET path=/v1/accounts/{accountId}/related-accounts-limits operationId=get-v1-accounts-limits-related-accounts -->
### `GET /v1/accounts/{accountId}/related-accounts-limits` — Get related accounts

- **operationId:** `get-v1-accounts-limits-related-accounts`
- **Specification:** `api-specs/Core_platform_-_Balances_and_limits.yaml` (Core platform - Balances and limits)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balances-limits`
- **Tags:** `Related accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get balances and limits of all related accounts given the main account ID. 
>
> Refer to the [Related accounts](doc:accounts-overview#related-accounts) section in the Accounts guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | number | Account ID | example: 9999999 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `RelatedAccountsResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 404 | Not found. | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error. | `application/json`: object (schema `ErrorModel`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Account ID. | example: 259875469 |
| `program_id` | integer | no | Program ID. | example: 1111 |
| `available_credit_limit` | number | no | Initial available credit limit of the account. | example: 712.02 |
| `available_savings_account_limit` | number | no | Available limit of the savings account. | example: 2700.34 |
| `available_withdrawal_credit` | number | no | Amount available for withdrawal in the credit account. | example: 500 |
| `held_funds` | number | no | Funds held on the account. Usually, but not always, this occurs due to a legal action. | example: 50 |
| `max_credit_limit` | number | no | Maximum credit amount approved for this account. This value can not be lower than `total_credit_limit`. | example: 800 |
| `total_credit_limit` | number | no | Total credit limit amount as set by the user. This can be any value up to the `max_credit_limit`. | example: 15.5 |
| `withdrawal_credit_limit` | number | no | Amount limit for withdrawal in credit programs. | example: 10.34 |
| `total_overdraft_limit` | number | no | Maximum limit amount for over draft spending on the account. | example: 340.6 |
| `percentage_over_limit` | number | no | Percentage of the maximum credit limit (`max_credit_limit`) made available for purchases over the credit limit on the account. | example: 15.5 |
| `total_installment_credit_limit` | number | no | Amount limit for installments in the credit account. | example: 145.78 |
| `available_total_installment_credit` | number | no | Available amount for installments in the credit account. | example: 120 |
| `currency_code` | string | no | ISO-4217 alphabetic code (3 characters) for transaction currency. | example: "BRL" |
| `currency_numeric_code` | string | no | ISO-4217 numeric code (3 digits) for transaction currency. | example: "986" |
| `related_accounts` | array of object (schema `RelatedAccountResponse`) | no | Return related account |  |

200 Example `related accounts found` — from `#/components/examples/relatedAccountFound`:

```json
{
  "account_id": 259875469,
  "program_id": 1111,
  "available_credit_limit": 712.02,
  "available_savings_account_limit": 2700.34,
  "available_withdrawal_credit": 500,
  "held_funds": 50,
  "max_credit_limit": 800,
  "total_credit_limit": 15.5,
  "withdrawal_credit_limit": 10.34,
  "total_overdraft_limit": 340.6,
  "percentage_over_limit": 15.5,
  "related_accounts": [
    {
      "account_id": 55668877,
      "program_id": 1111,
      "available_credit_limit": 712.02,
      "available_savings_account_limit": 2700.34,
      "available_withdrawal_credit": 500,
      "held_funds": 50,
      "max_credit_limit": 800,
      "total_credit_limit": 15.5,
      "withdrawal_credit_limit": 10.34,
      "total_overdraft_limit": 340.6,
      "percentage_over_limit": 15.5
    }
  ]
}
```

200 Example `related accounts not found` — from `#/components/examples/relatedAccountsNotFound`:

```json
{
  "account_id": 259875469,
  "program_id": 1111,
  "available_credit_limit": 712.02,
  "available_savings_account_limit": 2700.34,
  "available_withdrawal_credit": 500,
  "held_funds": 50,
  "max_credit_limit": 800,
  "total_credit_limit": 15.5,
  "withdrawal_credit_limit": 10.34,
  "total_overdraft_limit": 340.6,
  "percentage_over_limit": 15.5,
  "related_accounts": []
}
```

##### Response 400

400 Example `header validation error` — from `#/components/examples/headerValidationError`:

```json
{
  "message": "Some required headers are missing",
  "code": "WBLS0001"
}
```

400 Example `invalid account id error` — from `#/components/examples/invalidAccountIdError`:

```json
{
  "message": "Invalid account id",
  "code": "WBLS0004"
}
```

##### Response 404

404 Example `main account not found` — from `#/components/examples/accountNotFoundError`:

```json
{
  "message": "Account not found",
  "code": "WBLS0006"
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
| 400 | `WBLS0001` | Some required headers are missing |
| 400 | `WBLS0004` | Invalid account id |
| 404 | `WBLS0006` | Account not found |
| 500 | `EBLS9999` | Internal error found, please contact the administrator |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-CORE-accounts-overview`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/RelatedAccountResponse -->
### Schema `RelatedAccountResponse`

Pointer: `#/components/schemas/RelatedAccountResponse`. Type: object (schema `RelatedAccountResponse`).

> Related account response.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Account ID. | example: 259875469 |
| `parent_account_id` | integer | no | Parent Account ID. | example: 259875000 |
| `program_id` | integer | no | Program ID. | example: 1111 |
| `available_credit_limit` | number | no | Initial available credit limit of the account. | example: 712.02 |
| `available_savings_account_limit` | number | no | Available limit of the savings account. | example: 2700.34 |
| `available_withdrawal_credit` | number | no | Amount available for withdrawal in the credit account. | example: 500 |
| `held_funds` | number | no | Funds held on the account. Usually, but not always, this occurs due to a legal action. | example: 50 |
| `max_credit_limit` | number | no | Maximum credit amount approved for this account. This value can not be lower than `total_credit_limit`. | example: 800 |
| `total_credit_limit` | number | no | Total credit limit amount as set by the user. This can be any value up to the `max_credit_limit`. | example: 15.5 |
| `withdrawal_credit_limit` | number | no | Amount limit for withdrawal in credit programs. | example: 10.34 |
| `total_overdraft_limit` | number | no | Maximum limit amount for over draft spending on the account. | example: 340.6 |
| `percentage_over_limit` | number | no | Percentage of the maximum credit limit (`max_credit_limit`) made available for purchases over the credit limit on the account. | example: 15.5 |
| `total_installment_credit_limit` | number | no | Amount limit for installments in the credit account. | example: 145.78 |
| `available_total_installment_credit` | number | no | Available amount for installments in the credit account. | example: 120 |
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
| `api-specs/Core_platform_-_Balances_and_limits.yaml` | tag `Related accounts`: GET /v1/accounts/{accountId}/related-accounts-limits | https://github.com/PismoDevEx/pismo-api-specs | `d7c0d6ed8ee05ff1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-CORE-accounts-overview` — Accounts
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
