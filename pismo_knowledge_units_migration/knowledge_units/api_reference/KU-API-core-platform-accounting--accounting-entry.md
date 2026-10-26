---
ku_id: KU-API-core-platform-accounting--accounting-entry
title: 'API reference: Core platform - Accounting — Accounting entry'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Accounting.yaml
  sha256: f0272a891eaca0fedca4fa47cc760ff7fd676f50c94a22aa19ac665fa7017451
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
- CreateAccountingEntry
related_kus:
- KU-CORE-accounting-accounts-and-entries
- KU-CORE-accounting-overview
- KU-EVT-accounting-data-events
- KU-EVT-catalogue-other-domains
specification_version: 1.0.0
---

# API reference: Core platform - Accounting — Accounting entry

**KU ID:** `KU-API-core-platform-accounting--accounting-entry` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Accounting entry` in `api-specs/Core_platform_-_Accounting.yaml` (“Core platform - Accounting”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage accounting entries.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/accounting-entries` | `CreateAccountingEntry` | Create accounting entry | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=POST path=/v1/accounting-entries operationId=CreateAccountingEntry -->
### `POST /v1/accounting-entries` — Create accounting entry

- **operationId:** `CreateAccountingEntry`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting entry`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an accounting entry.
>
> This endpoint generates an [Accounting entry created](https://developers.pismo.io/events/docs/accounting-entry-creation-1) event.
>
> Refer to the [How to create accounting entries](doc:create-accounting-entries) guide for more information.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `AccountingEntryPost`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Accounting entry amount |  |
| `entry_type_id` | integer | yes | Entry type ID | format: "int64" |
| `event_date` | string | yes | Event date | format: "date"; example: "2021-06-26T00:00:00.000Z" |
| `program_id` | integer | yes | Related program ID | format: "int64" |
| `account_id` | integer | no | Related account ID, required if Transaction_ID is present. | format: "int64" |
| `credit_accounting_account` | string | no | Credit accounting account |  |
| `debit_accounting_account` | string | no | Debit accounting account |  |
| `tracking_id` | string | no | Tracking ID in UUID format, optional idempotence key. You can use [Online UUID Generator](https://www.uuidgenerator.net/version4) to generate a random UUID value. | maxLength: 50 |
| `transaction_id` | integer | no | Related transaction ID | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 202 | Request accepted but not processed yet. | `application/json`: object (schema `AccountingEntryPost`) |
| 400 | Bad request when a provided parameter is invalid. A JSON field type mismatch in the body<br>(e.g. a numeric ID sent as a quoted string) returns the shared `V1BindTypeMismatchError`<br>shape (`error`, `cid`, `invalid_field`); the offending value is never echoed.<br> | `application/json`: object (schema `V1BindTypeMismatchError`) |
| 409 | Conflict when TrackingId already exists. |  |

##### Response 202

**202 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | yes | Accounting entry amount |  |
| `entry_type_id` | integer | yes | Entry type ID | format: "int64" |
| `event_date` | string | yes | Event date | format: "date"; example: "2021-06-26T00:00:00.000Z" |
| `program_id` | integer | yes | Related program ID | format: "int64" |
| `account_id` | integer | no | Related account ID, required if Transaction_ID is present. | format: "int64" |
| `credit_accounting_account` | string | no | Credit accounting account |  |
| `debit_accounting_account` | string | no | Debit accounting account |  |
| `tracking_id` | string | no | Tracking ID in UUID format, optional idempotence key. You can use [Online UUID Generator](https://www.uuidgenerator.net/version4) to generate a random UUID value. | maxLength: 50 |
| `transaction_id` | integer | no | Related transaction ID | format: "int64" |

##### Response 400

400 Example `example`:

```json
{
  "error": "field 'entry_type_id' must be of type integer number (unquoted) but received a string value",
  "invalid_field": "entry_type_id",
  "cid": "6fdd31b0-c5b9-911a-a713-10158c1fd6ea"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `accounting-entry-creation-1` | https://developers.pismo.io/events/docs/accounting-entry-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `202;400;409`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`, `KU-CORE-accounting-overview`, `KU-EVT-accounting-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/V1BindTypeMismatchError -->
### Schema `V1BindTypeMismatchError`

Pointer: `#/components/schemas/V1BindTypeMismatchError`. Type: object (schema `V1BindTypeMismatchError`).

> Shared V1 error body returned by **every** endpoint that binds a JSON request body when a
> field is sent with the wrong JSON type (a `*json.UnmarshalTypeError`) — e.g. a numeric ID
> sent as a quoted string. It is additive and backward compatible: the HTTP status stays `400`,
> only the free-text `error` value changed and the optional `cid` / `invalid_field` keys were
> added. Any other body-parse failure (malformed JSON, empty body, oversized body) keeps each
> endpoint's pre-existing generic message and is not described by this schema.
>
> Endpoints that emit this shape on a type mismatch:
>   - `POST /v1/accounting-scripts`, `POST /v1/accounting-scripts/deactivate`
>   - `PATCH /v1/accounting-scripts/{accountingScriptId}`, `PATCH /v1/accounting-scripts/batch`
>   - `POST /v1/event-types`, `PATCH /v1/event-types/{eventTypeId}`
>   - `POST /v1/entry-types`, `PATCH /v1/entry-types/{entryTypeId}`
>   - `POST /v1/accounting-accounts`, `PATCH /v1/accounting-accounts/{accountingAccountId}`
>   - `POST /v1/accounting-entries`
>
> The offending user-supplied **value** is never echoed — only the field name and the JSON
> types (expected vs received) appear in the message, and the `cid` correlates to server logs.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error` | string | no | Descriptive message naming the offending field and the expected/received JSON type.<br> | example: "field 'credit_accounting_account_id' must be of type integer number (unquoted) but received a string value" |
| `cid` | string | no | Correlation ID echoed on every 4xx/5xx response body. | example: "6fdd31b0-c5b9-911a-a713-10158c1fd6ea" |
| `invalid_field` | string | no | JSON path of the field whose type did not match the schema. | example: "credit_accounting_account_id" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounting.yaml` | tag `Accounting entry`: POST /v1/accounting-entries | https://github.com/PismoDevEx/pismo-api-specs | `f0272a891eaca0fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-accounting-accounts-and-entries` — Creating accounting accounts and accounting entries
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-EVT-accounting-data-events` — Core platform - Accounting
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
