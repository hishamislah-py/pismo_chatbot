---
ku_id: KU-API-banking-interest-bearing-accounts--deposit-account-lifecycle
title: 'API reference: Banking - Interest-bearing accounts — Deposit account lifecycle'
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
operations:
- interest-bearing-v1-get-cycle-snapshot
related_kus:
- KU-ERR-codes-eibacc
specification_version: 1.0.0
---

# API reference: Banking - Interest-bearing accounts — Deposit account lifecycle

**KU ID:** `KU-API-banking-interest-bearing-accounts--deposit-account-lifecycle` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Deposit account lifecycle` in `api-specs/Banking_-_Interest-bearing_accounts.yaml` (“Banking - Interest-bearing accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that allow consolidated, point‑in‑time snapshots of a deposit account lifecycle

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/deposits/accounts/{accountId}/cycle-snapshot` | `interest-bearing-v1-get-cycle-snapshot` | Get cycle snapshot for deposit account | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=GET path=/v1/deposits/accounts/{accountId}/cycle-snapshot operationId=interest-bearing-v1-get-cycle-snapshot -->
### `GET /v1/deposits/accounts/{accountId}/cycle-snapshot` — Get cycle snapshot for deposit account

- **operationId:** `interest-bearing-v1-get-cycle-snapshot`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Deposit account lifecycle`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Return a consolidated point‑in‑time snapshot of a deposit account lifecycle, providing current and previous cycle details such as active and prior product attachments, key dates (cycle start, maturity, rollover), interest plan information, and principal context to support audit, statement, and reconciliation use cases.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | example: 123456 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Cycle snapshot returned successfully | `application/json`: object (schema `CycleSnapshotResponse`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 403 | Forbidden |  |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Deposit account ID | example: 1234567 |
| `status` | string | no | Cycle status, this can be either `ACTIVE` or `INACTIVE` | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `current_product_id` | string | no | Product ID currently attached to the account | example: "ze2b8k77-f6a0-4ba4-890a-0dc23f13fhg4" |
| `current_attachment_id` | string | no | Current attachment ID | example: "1234test" |
| `current_interest_plan_id` | string | no | Current interest plan ID | example: "ee2b8b77-f6a0-4ba4-890a-0dc23f13fcb4" |
| `current_grace_period` | integer | no | Grace‑period duration in days for the current cycle. For non‑first cycles, the grace window opens at the start of the cycle, spanning `cycle_start_date`, `cycle_start_date` + `current_grace_period`. The first cycle does not include a grace window. | example: 10 |
| `current_rollover_date` | string | no | Date the current cycle rolls into the next one (`current_calendar_maturity_date` + 1 or the next cycle’s `cycle_start_date`). Rollover occurs at the maturity date, so grace no longer sits between maturity and rollover. Format = `yyyy-mm-ddThh:mm:ss.sssZ`. | format: "date-time"; example: "2026-02-01T00:00:00Z" |
| `current_calendar_maturity_date` | string | no | Maturity date of the current cycle. Uses inclusive day count (day 1 is `cycle_start_date`). For the first cycle, the maturity date is `cycle_start_date` + term - 1. For a renewed cycle, the maturity date is `cycle_start_date` + `current_grace_period` + term - 1 because grace extends the cycle. Format = `yyyy-mm-ddThh:mm:ss.sssZ`. | format: "date-time"; example: "2026-01-26T12:00:00Z" |
| `previous_product_id` | string | no | Previous product ID | example: "ae2b8k77-f6a0-4ba4-890a-0dc23f13fcb4" |
| `previous_attachment_id` | string | no | Previous attachment ID | example: "attach685" |
| `previous_interest_plan_id` | string | no | Previous interest plan ID | example: "ee2b8b77-f6a0-4ba4-890a-0dc23f13fcb4" |
| `previous_grace_period` | integer | no | Previous grace period in days | example: 5 |
| `previous_calendar_maturity_date` | string \\\| null | no | Previous calendar maturity date. The datetime format follows the ISO 8601 standard `yyyy-mm-ddThh:mm:ss.sssZ`. | format: "date-time"; example: "2025-12-01T00:00:00Z" |
| `cycle_start_date` | string | no | Cycle start date. The datetime format follows the ISO 8601 standard `yyyy-mm-ddThh:mm:ss.sssZ`. | format: "date-time"; example: "2026-01-26T12:00:00Z" |
| `start_date` | string | no | Start date of the cycle. The datetime format follows the ISO 8601 standard `yyyy-mm-ddThh:mm:ss.sssZ`. | format: "date-time"; example: "2024-12-01T00:00:00Z" |

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

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

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
| `api-specs/Banking_-_Interest-bearing_accounts.yaml` | tag `Deposit account lifecycle`: GET /v1/deposits/accounts/{accountId}/cycle-snapshot | https://github.com/PismoDevEx/pismo-api-specs | `89fc3f8ed0222a57…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-eibacc` — Error codes: EIBACC
