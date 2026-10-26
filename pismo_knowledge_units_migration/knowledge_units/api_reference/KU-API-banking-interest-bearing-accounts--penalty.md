---
ku_id: KU-API-banking-interest-bearing-accounts--penalty
title: 'API reference: Banking - Interest-bearing accounts — Penalty'
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
- interest-bearing-v1-simulate-penalty
related_kus:
- KU-BANK-penalties-for-cd-accounts
- KU-ERR-codes-eibacc
specification_version: 1.0.0
---

# API reference: Banking - Interest-bearing accounts — Penalty

**KU ID:** `KU-API-banking-interest-bearing-accounts--penalty` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Penalty` in `api-specs/Banking_-_Interest-bearing_accounts.yaml` (“Banking - Interest-bearing accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that manage penalties for deposit accounts

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /v1/deposits/accounts/{accountId}/penalty-simulation` | `interest-bearing-v1-simulate-penalty` | Simulate penalty | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/deposits/accounts/{accountId}/penalty-simulation operationId=interest-bearing-v1-simulate-penalty -->
### `POST /v1/deposits/accounts/{accountId}/penalty-simulation` — Simulate penalty

- **operationId:** `interest-bearing-v1-simulate-penalty`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Penalty`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Simulate the penalty applied to a specified withdrawal on a given date. The operation is read‑only and does not modify any data.
>
> Use this endpoint to preview penalty fees before making an actual withdrawal.
>
> The simulation evaluates all penalty rules configured in the product, including:
>
> - Early withdrawal penalties
>
> - Grace period penalties
>
> - Tiered interest forfeiture penalties
>
> - Withdrawal fees
>
> - Subsequent withdrawal penalties
>
> Notes:
> - A withdrawal date inside the cool‑off period results in no penalties
> - If `withdrawal_amount` is omitted, the Pismo platform fetches the current book balance from [Get transaction banking account balance](ref:get-account-balances).
> - If `withdrawal_amount` is provided, the balance cannot exceed the current book balance.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PenaltySimulationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `withdrawal_amount` | number | no | The amount the customer intends to withdraw. When omitted, the system fetches the current book balance from Bank Statements API. When provided, it must not exceed the current book balance.<br> | example: 5000 |
| `withdrawal_date` | string | yes | Simulated withdrawal date in ISO 8601 format. | format: "date-time"; example: "2026-06-15T00:00:00Z" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Simulation completed successfully | `application/json`: object (schema `PenaltySimulationResponse`) |
| 400 | Bad Request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 403 | Forbidden | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `external_account_id` | string | no | External account identifier of the resolved account. Returned only when the account has an external account identifier. | example: "a4070788-bbe3-4127-8abc-12345" |
| `withdrawal_amount` | number | no | The withdrawal amount used in the simulation (equals book_balance when omitted in request) | example: 40667.17 |
| `withdrawal_date` | string | no | The withdrawal date used in the simulation in ISO 8601 format. | format: "date-time"; example: "2026-12-15T00:00:00Z" |
| `penalty_rule_applied` | array of object (schema `PenaltyRuleApplied`) | no | List of penalty rules that applies to the withdrawal, omitted if no penalties apply.<br> |  |
| `penalty_amount` | number | no | The total penalty amount applied to the withdrawal, combining all relevant penalty rules. | example: 231.75 |
| `penalty_breakdown` | object (schema `PenaltyBreakdown`) | no | Breakdown of the total penalty amount by calculation type. Omitted when no penalty applies. |  |
| `currency` | string | no | The currency in ISO 4217 alphabetic format, omitted if no penalty applies. | example: "BRL" |
| `gross_amount` | number | no | The gross amount of the deposit account, calculated as the sum of the total balance without interest plus the total interest earned. Always present; 0 when no total record exists.<br> | example: 41329.34 |
| `interest_earned_amount` | number | no | The total interest earned (paid/capitalized) on the account. Always present; 0 when no total record exists.<br> | example: 667.17 |
| `net_amount` | number | no | The net amount after deducting penalties from the gross amount: `gross_amount - penalty_amount`.<br> | example: 41097.59 |
| `simulation_timestamp` | string | no | The date and time of the simulation, formatted according to ISO 8601. | format: "date-time"; example: "2026-06-19T19:22:55Z" |

##### Response 400

400 Example `invalidAccountId` (Invalid account ID path parameter):

```json
{
  "code": "EIBACC0015",
  "message": "Invalid accountId path param"
}
```

400 Example `invalidWithdrawalAmount` (Invalid withdrawal amount (zero or negative)):

```json
{
  "code": "EIBACC0008",
  "message": "Validation error",
  "details": "withdrawal_amount requires a positive number"
}
```

400 Example `missingWithdrawalDate` (Missing withdrawal date):

```json
{
  "code": "EIBACC0008",
  "message": "Validation error",
  "details": "withdrawal_date is required"
}
```

400 Example `invalidWithdrawalDate` (Invalid withdrawal date format):

```json
{
  "code": "EIBACC0008",
  "message": "Validation error",
  "details": "withdrawal_date must be a valid ISO 8601 datetime (e.g. 2026-01-15T15:00:00Z)"
}
```

400 Example `withdrawalAmountExceedsBalance` (Withdrawal amount exceeds book balance):

```json
{
  "code": "EIBACC0338",
  "message": "withdrawal_amount cannot be greater than the account balance",
  "details": "available balance: 40667.17"
}
```

##### Response 403

403 Example `missingTenantHeader` (Missing tenant header):

```json
{
  "code": "EIBACC0005",
  "message": "Missing required header: 'x-tenant'"
}
```

##### Response 404

404 Example `accountNotFound` (Account not found):

```json
{
  "code": "EIBACC0226",
  "message": "Account not found"
}
```

404 Example `productNotAttached` (Product is not attached to account):

```json
{
  "code": "EIBACC0064",
  "message": "Product not found"
}
```

##### Response 422

422 Example `withdrawalDateInPast` (Withdrawal date set in the past):

```json
{
  "code": "EIBACC0294",
  "message": "withdrawalDate must not be in the past"
}
```

422 Example `productNotDeposit` (Product is not a deposit product):

```json
{
  "code": "EIBACC0295",
  "message": "Penalty simulation is only available for deposit accounts"
}
```

422 Example `noPenaltyConfigured` (No penalty configured for simulation):

```json
{
  "code": "EIBACC0296",
  "message": "No penalty is configured for the product attached to this account"
}
```

##### Response 500

500 Example `internalError` (Internal error):

```json
{
  "code": "EIBACC0007",
  "message": "Internal error"
}
```

500 Example `getPenaltyError` (Get penalty error):

```json
{
  "code": "EIBACC0204",
  "message": "Get Penalty error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBACC0015` | Invalid accountId path param |
| 400 | `EIBACC0008` | Validation error |
| 400 | `EIBACC0338` | withdrawal_amount cannot be greater than the account balance |
| 403 | `EIBACC0005` | Missing required header: 'x-tenant' |
| 404 | `EIBACC0226` | Account not found |
| 404 | `EIBACC0064` | Product not found |
| 422 | `EIBACC0294` | withdrawalDate must not be in the past |
| 422 | `EIBACC0295` | Penalty simulation is only available for deposit accounts |
| 422 | `EIBACC0296` | No penalty is configured for the product attached to this account |
| 500 | `EIBACC0007` | Internal error |
| 500 | `EIBACC0204` | Get Penalty error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-penalties-for-cd-accounts`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/PenaltyRuleApplied -->
### Schema `PenaltyRuleApplied`

Pointer: `#/components/schemas/PenaltyRuleApplied`. Type: object (schema `PenaltyRuleApplied`).

> A single penalty rule applied during a simulated withdrawal

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | no | The penalty calculation type.<br>- `PERCENTAGE`: The penalty calculated as a percentage of the withdrawal amount<br>- `FIXED`: The penalty is a fixed amount<br> | enum: ["PERCENTAGE", "FIXED"]; example: "PERCENTAGE" |
| `value` | number | no | The penalty value. For `PERCENTAGE`, this represents the percentage rate. For example, `2.5` = 2.5%. For `FIXED`, this is the absolute amount in the account's currency.<br> | format: "float"; example: 2.5 |
| `description` | string | no | Describes the penalty rule that triggers the penalty | example: "Early withdrawal after opening penalty" |

<!-- schema: #/components/schemas/PenaltyBreakdown -->
### Schema `PenaltyBreakdown`

Pointer: `#/components/schemas/PenaltyBreakdown`. Type: object (schema `PenaltyBreakdown`).

> Breakdown of the total penalty amount by calculation type. Omitted when no penalty applies.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `fixed_amount` | number | no | The sum of all fixed-amount penalties | example: 50 |
| `percentage_amount` | number | no | The sum of all percentage-based penalties | example: 75.5 |

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
| `api-specs/Banking_-_Interest-bearing_accounts.yaml` | tag `Penalty`: POST /v1/deposits/accounts/{accountId}/penalty-simulation | https://github.com/PismoDevEx/pismo-api-specs | `89fc3f8ed0222a57…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-penalties-for-cd-accounts` — Penalties and taxes for CD accounts
- `KU-ERR-codes-eibacc` — Error codes: EIBACC
