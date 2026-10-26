---
ku_id: KU-API-core-platform-balances-and-limits--account-limits
title: 'API reference: Core platform - Balances and limits — Account limits'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- patch-v1-account-limits
related_kus:
- KU-CORE-program-limits
- KU-CORE-working-with-limits-objects
- KU-EVT-catalogue-other-domains
specification_version: 1.0.0
---

# API reference: Core platform - Balances and limits — Account limits

**KU ID:** `KU-API-core-platform-balances-and-limits--account-limits` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Account limits` in `api-specs/Core_platform_-_Balances_and_limits.yaml` (“Core platform - Balances and limits”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage account limits.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PATCH /v1/accounts/{accountId}/limits` | `patch-v1-account-limits` | Update account limits | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Balances_and_limits.yaml method=PATCH path=/v1/accounts/{accountId}/limits operationId=patch-v1-account-limits -->
### `PATCH /v1/accounts/{accountId}/limits` — Update account limits

- **operationId:** `patch-v1-account-limits`
- **Specification:** `api-specs/Core_platform_-_Balances_and_limits.yaml` (Core platform - Balances and limits)
- **Server base URL(s):** `https://sandbox.pismolabs.io/balances-limits`
- **Tags:** `Account limits`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update account limits for a specific account. This endpoint triggers validation against the global program limit configured in the [Configure program limit](ref:post-v1-global-configs) endpoint.
>
> This endpoint generates the [Account limit changed](https://developers.pismo.io/events/docs/ledger-limit-changed-1) event.
>
> Refer to the [Account limits](doc:working-with-limits-objects) guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | number | Account ID | example: 123456 |
| `x-tenant` | header | yes | string | Tenant ID | example: "org-123" |

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
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `ErrorModel`) |
| 500 | Internal server error. | `application/json`: object (schema `ErrorModel`) |


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `ledger-limit-changed-1` | https://developers.pismo.io/events/docs/ledger-limit-changed-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CORE-program-limits`, `KU-CORE-working-with-limits-objects`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

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
| `api-specs/Core_platform_-_Balances_and_limits.yaml` | tag `Account limits`: PATCH /v1/accounts/{accountId}/limits | https://github.com/PismoDevEx/pismo-api-specs | `d7c0d6ed8ee05ff1…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-program-limits` — Program limits
- `KU-CORE-working-with-limits-objects` — Account limits
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
