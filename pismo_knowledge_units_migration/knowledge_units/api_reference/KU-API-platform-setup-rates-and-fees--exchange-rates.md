---
ku_id: KU-API-platform-setup-rates-and-fees--exchange-rates
title: 'API reference: Platform setup - Rates and fees — Exchange rates'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Platform_setup_-_Rates_and_fees.yaml
  sha256: 0a918b57bd00f81ced58e15b5d39c4f56ef2ef685442e55dc4fd59f237383ec3
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
- getExchange
- createExchangeRates
related_kus:
- KU-CC-exchange-rates
- KU-CORE-exchange-rate
specification_version: 1.0.0
---

# API reference: Platform setup - Rates and fees — Exchange rates

**KU ID:** `KU-API-platform-setup-rates-and-fees--exchange-rates` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Exchange rates` in `api-specs/Platform_setup_-_Rates_and_fees.yaml` (“Platform setup - Rates and fees”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Exchange rate endpoints.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/exchange-rates` | `getExchange` | Get exchange rates | no |
| `POST /v1/exchange-rates` | `createExchangeRates` | Create exchange rate | no |

## Authentication

- `bearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=GET path=/v1/exchange-rates operationId=getExchange -->
### `GET /v1/exchange-rates` — Get exchange rates

- **operationId:** `getExchange`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Exchange rates`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Returns exchange rates with paging and filter options

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `beginCreatedAt` | query | yes | string | Start date filter, format = yyyy-mm-dd | example: "2022-05-04" |
| `endCreatedAt` | query | yes | string | End date filter, format = yyyy-mm-dd. 30 days maximum between `beginCreatedAt` and `endCreatedAt`. | example: "2022-06-01T00:00:00.000Z" |
| `perPage` | query | yes | integer | Records per page - 100 records maximum. |  |
| `page` | query | yes | integer | Current page number. |  |
| `Authorization` | header | yes | string | Access token, not an account-specific token. Tokens can expire quickly, which can result in an <b>401 Unauthorized</b> message<br> |  |
| `programId` | query | no | integer | **Deprecated** - use `program_ids` instead. Filters by a single Pismo<br>program ID. Mutually exclusive with `program_ids`: sending both returns<br>400.<br> | deprecated: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `Exchanges`) |
| 400 | Bad Request | `application/json`: array of object (schema `HTTPGetErrors`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 404 | Exchange not found | `application/json`: object (schema `NotFoundError`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-exchange-rate`.

<!-- op: spec=api-specs/Platform_setup_-_Rates_and_fees.yaml method=POST path=/v1/exchange-rates operationId=createExchangeRates -->
### `POST /v1/exchange-rates` — Create exchange rate

- **operationId:** `createExchangeRates`
- **Specification:** `api-specs/Platform_setup_-_Rates_and_fees.yaml` (Platform setup - Rates and fees)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rates`
- **Tags:** `Exchange rates`
- **Deprecated in specification:** no
- **Security requirement:** `bearerAuth`

**Description (from the specification):**

> Define the exchange rate for international transactions.
>
> You **must** use this endpoint or [Pismo Control Center](doc:exchange-rates) to define the exchange rate for today or tomorrow.
>
> Exchange rates are defined at the organization level but, optionally, you can define rates for a specific program and the platform uses this rate and not the org rate for all program-related transactions.
>
>
> **Note:**  For more information, refer to [Exchange rates for international transactions](https://developers.pismo.io/pismo-docs/docs/exchange-rate#exchange-rates-for-international-transactions).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Access token, not an account-specific token. Tokens can expire quickly, which can result in an <b>401 Unauthorized</b> message<br> |  |

#### Request body

Required: yes

> Add exchange rates

**Content type `application/json`** — schema: object (schema `ExchangeRates`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `date` | string | yes | Date for today or tomorrow, format = yyyy-mm-dd. | format: "date"; example: "2022-01-02" |
| `destination_currency_id` | string | yes | Destination ISO 4217 currency. | example: "840" |
| `origin_currency_id` | string | yes | Origin ISO 4217 currency. | example: "032" |
| `exchange_rate` | number | yes | Wholesale exchange rate amount to 4 decimal places in the destination currency. For example 4.8123. | example: 4.8123 |
| `spread` | number | yes | Day rate multiplier to 4 decimal places. For example, 1.1205 is equivalent to 1.1205%, 15.12 is equivalent to 15.12%.. | example: 1.0567 |
| `hour` | string | no | <br>Hour in UTC time zone, format = HH:MM:SSZ. Using this field, you be able to work with seconds precision in your international purchases.<br><br>**Note:** This field will be validated considering an offset of UTC subtracted three seconds just in the validation layer, to prevent you to need increase a few seconds just to pass our validation.<br> | format: "time"; example: "14:30:00Z" |
| `program_id` | number (schema `ProgramID`) | no | Pismo program ID | example: 76589 |
| `apply_fees_without_spread` | boolean | no | Whether `spread` should be ignored in exchange transactions when calculating fee model taxes. Default = `false`. | example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created |  |
| 400 | Bad Request | `application/json`: array of object (schema `HTTPErrors`) |
| 401 | InvalidToken | `application/json`: object (schema `Error`) |
| 422 | Unprocessable Entity | `application/json`: object (schema `Error`) |
| 500 | Internal Server Error | `application/json`: object (schema `Error`) |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;422;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CC-exchange-rates`, `KU-CORE-exchange-rate`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/HTTPGetErrors -->
### Schema `HTTPGetErrors`

Pointer: `#/components/schemas/HTTPGetErrors`. Type: array of object (schema `HTTPGetErrors`).

<!-- schema: #/components/schemas/Error -->
### Schema `Error`

Pointer: `#/components/schemas/Error`. Type: object (schema `Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code ID. | example: "RCAPI-DOMAIN-VIOLATION" |
| `message` | string | no | Error description. | example: "Internal server error" |

<!-- schema: #/components/schemas/NotFoundError -->
### Schema `NotFoundError`

Pointer: `#/components/schemas/NotFoundError`. Type: object (schema `NotFoundError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error_code` | string | no | Error code ID | example: "RCAPI-NOT_FOUND-VIOLATION" |
| `message` | string | no | Error description | example: "" |

<!-- schema: #/components/schemas/HTTPErrors -->
### Schema `HTTPErrors`

Pointer: `#/components/schemas/HTTPErrors`. Type: array of object (schema `HTTPErrors`).

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Platform_setup_-_Rates_and_fees.yaml` | tag `Exchange rates`: GET /v1/exchange-rates, POST /v1/exchange-rates | https://github.com/PismoDevEx/pismo-api-specs | `0a918b57bd00f81c…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CC-exchange-rates` — Exchange rates in Control Center
- `KU-CORE-exchange-rate` — Exchange rates
