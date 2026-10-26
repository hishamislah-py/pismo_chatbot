---
ku_id: KU-API-banking-interest-bearing-accounts--product
title: 'API reference: Banking - Interest-bearing accounts — Product'
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
- interest-bearing-v1-list-products
- interest-bearing-v1-create-deposit-product
- interest-bearing-v1-get-deposit-products
- interest-bearing-v1-patch-deposit-product
- interest-bearing-v1-create-savings-account-product
- interest-bearing-v1-get-savings-account-products
- interest-bearing-v1-patch-savings-account-product
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-how-overdraft-works
- KU-BANK-interest-bearing-accounts
- KU-BANK-penalties-for-cd-accounts
- KU-ERR-codes-eibacc
- KU-EVT-catalogue-deposit
- KU-EVT-catalogue-other-domains
- KU-EVT-interest-management-data-events
specification_version: 1.0.0
---

# API reference: Banking - Interest-bearing accounts — Product

**KU ID:** `KU-API-banking-interest-bearing-accounts--product` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Product` in `api-specs/Banking_-_Interest-bearing_accounts.yaml` (“Banking - Interest-bearing accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that manage Interest-bearing accounts products

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/products` | `interest-bearing-v1-list-products` | List products | no |
| `POST /v1/deposits` | `interest-bearing-v1-create-deposit-product` | Create deposit product | no |
| `GET /v1/deposits/{productId}` | `interest-bearing-v1-get-deposit-products` | Get deposit product | no |
| `PATCH /v1/deposits/{productId}` | `interest-bearing-v1-patch-deposit-product` | Update deposit product | no |
| `POST /v1/savings-accounts` | `interest-bearing-v1-create-savings-account-product` | Create savings account product | no |
| `GET /v1/savings-accounts/{productId}` | `interest-bearing-v1-get-savings-account-products` | Get savings account product | no |
| `PATCH /v1/savings-accounts/{productId}` | `interest-bearing-v1-patch-savings-account-product` | Update savings account product | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=GET path=/v1/products operationId=interest-bearing-v1-list-products -->
### `GET /v1/products` — List products

- **operationId:** `interest-bearing-v1-list-products`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Return a list of an organization's savings and time-deposit accounts.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `beginDatetime` | query | no | string | Queries for the date and time of products after the value of this field. Date and time are displayed in RFC 3339 format, for example: `2024-01-28T10:33:01Z`.<br> | format: "date-time"; example: "2024-01-28T10:33:01.000Z" |
| `endDatetime` | query | no | string | Queries for the date and time of products created before the value of this field. Date and time are displayed in RFC 3339 format, for example: `2024-01-29T10:33:01Z`.<br> | format: "date-time"; example: "2024-01-30T10:33:01.000Z" |
| `afterId` | query | no | integer | This is the `last_id` field returned in the response which you can use to get the next result set. This is displayed in UNIX timestamp.<br> | example: 1706027185000 |
| `perPage` | query | no | integer | Number of items per page. | default: 20; maximum: 100; example: 20 |
| `order` | query | no | string | List result order of the `created_at` value. It can be sorted in ascending (`ASC`) or descending (`DESC`) order. Default is `DESC`. | enum: ["ASC", "DESC"]; default: "DESC"; example: "DESC" |
| `productType` | query | no | string | Filter results by product type. | enum: ["deposit", "savings-account"]; example: "deposit" |
| `status` | query | no | string | Filter results by status. | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "ACTIVE" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `ProductList`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `last_id` | integer | no | Pagination reference, displayed in UNIX timestamp. | example: 1706027185000 |
| `next_page` | boolean | no | Indicates whether there is a next page of results. | example: true |
| `per_page` | integer | no | Number of items per page. Default `20`, maximum is `100`. | default: 20; minimum: 1; maximum: 100; example: 20 |
| `items` | object | no | A collection of individual product objects. |  |
| `items.cool_off_period` | integer | no | Period in days when a withdrawal can be made without penalty. | example: 0 |
| `items.created_at` | string | no | Date and time the product was created | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `items.funding_duration` | integer | no | Period during which money is allowed to deposit into the account before the account is blocked. The value of this field is calculated in days. | example: 12 |
| `items.interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `items.maturity_instructions` | object (schema `DepositMaturityInstructions`) | no | - If the principal or interest are `ROLLOVER,` the respective amounts is rolled over to a new deposit term.<br>- If the principal is `NO_ACTION`, no action is taken with the principal amount at maturity.<br>- If the interest is `PAY` and the accrued interest is greater than zero, it's paid to the account's cash balance.<br> |  |
| `items.min_amount` | number | no | The minimum balance required to earn yield. If the balance is below this amount, yield is not calculated, and if no value is specified, any available amount is treated as accrued interest. | example: 1000 |
| `items.max_amount` | number | no | Maximum deposit amount. | example: 5000 |
| `items.min_term` | integer | no | Minimum term duration. The value of this field is calculated in days. | example: 265 |
| `items.max_term` | integer | no | Maximum term duration. The value of this field is calculated in days. | example: 1025 |
| `items.grace_period_duration_days` | integer | no | The number of days in the grace period. Applies only when no grace‑period penalty is defined. The grace‑period window opens at the start of the next cycle, spanning `cycle_start_date`, `cycle_start_date` + `grace_period_duration_days`, and the renewed cycle’s maturity extends by these days (`cycle_start_date` + `grace_period_duration_days` + term - 1, inclusive). The first cycle does not include a grace period. During grace period, interest accrues daily only when `accrue_during_grace_period` is `true`. | example: 30 |
| `items.accrue_during_grace_period` | boolean | no | Whether interest accrues daily during the grace window. Defaults to true. When false, no submissions are sent to the Interest Engine during grace (audited as `IN_GRACE_NO_ACCRUAL`) and accrual starts when grace ends. Deposit products only. | example: true |
| `items.name` | string | no | Product name | example: "Tax 1 Default" |
| `items.penalties` | object (schema `DepositPenalties`) | no | Set of penalty configurations that can be applied to a deposit product. Each penalty type corresponds to a specific fee ID and transaction flow within the Pismo platform.<br>For details about penalty types, refer to the [Penalty types](doc:penalties-for-cd-accounts#penalty-types) section of Penalties for CD accounts.<br> |  |
| `items.notices` | array of object (schema `MaturityNotice`) | no | Advance maturity notice configurations for deposit products only, rejected for savings‑account products. If this field is included in a savings‑account request, the API returns `HTTP 400`. When provided, the field must contain one to three entries, each with a unique `days_before_maturity` value. If the field is absent or the array is empty, no notices are configured.<br> | maxItems: 3 |
| `items.processing_codes` | object (schema `DepositProcessingCodes`) | no |  |  |
| `items.product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `items.product_type` | string | no | Product type | enum: ["deposit", "savings-account"] |
| `items.status` | string | no | Indicates the current state of the product. For example, `CREATED`. | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "CREATED" |
| `items.term_type` | string | no | Term type. For example, `FIXED` or `FLEXIBLE`.<br> | enum: ["FIXED", "FLEXIBLE"]; example: "FIXED" |
| `items.accrual_model` | string | no | Interest accrual model configured at the product level and returned in both the creation event and API response.<br>With `DEPOSIT_BASIS`, the Pismo platform calculates accruals based on the net daily balance change (credits minus debits) at the end of each day.<br>With `BALANCE_BASIS`, accruals are calculated using the account's closing balance at the end of the day, regardless of whether any transactions occurred. For example, if an account has a balance of 1000 and no transactions are made during the day, the platform still uses 1000 as the accrual basis.<br>At creation, the interest plan determines the model: `BALANCE-CHANGE` maps to `DEPOSIT_BASIS`, and `CLOSING-BALANCE` maps to `BALANCE_BASIS`.<br> | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; example: "DEPOSIT_BASIS" |
| `items.balance_type` | string | no | Which balance of the `balance_history` event is submitted when `accrual_model` is `BALANCE_BASIS`. `VALUE_DATED_BALANCE` uses the cleared balance (default); `LEDGER_BALANCE` includes uncleared funds. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `items.start_date` | string | no | Defines the earliest date from which the product can be attached to an account or program. Date is displayed in UTC. | format: "date"; example: "2025-11-01" |
| `items.end_date` | string | no | Defines the final date when the product can be attached to an account or program, rejects any attach operations submitted after that date, uses the `yyyy‑mm‑dd` format with all dates shown in UTC+0 regardless of your timezone, and must be set at least one day after the current date (D+1). | format: "date"; example: "2027-12-31" |
| `items.metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>Metadata content is not controlled by the Pismo platform and is instead controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |
| `items.created_at` | string | no | The moment when a product is created. | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `items.updated_at` | string | no | The moment when a product is updated. | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `items.interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `items.name` | string | no | The product name. | example: "Tax 1 Default" |
| `items.accrual_model` | string | no | Interest accrual model configured at the product level and returned in both the creation event and API response.<br>With `DEPOSIT_BASIS`, the Pismo platform calculates accruals based on the net daily balance change (credits minus debits) at the end of each day.<br>With `BALANCE_BASIS`, accruals are calculated using the account's closing balance at the end of the day, regardless of whether any transactions occurred. For example, if an account has a balance of 1000 and no transactions are made during the day, the platform still uses 1000 as the accrual basis.<br>At creation, the interest plan determines the model: `BALANCE-CHANGE` maps to `DEPOSIT_BASIS`, and `CLOSING-BALANCE` maps to `BALANCE_BASIS`.<br> | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; example: "DEPOSIT_BASIS" |
| `items.balance_type` | string | no | Which balance of the `balance_history` event is submitted when `accrual_model` is `BALANCE_BASIS`. `VALUE_DATED_BALANCE` uses the cleared balance (default). `LEDGER_BALANCE` includes uncleared funds. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `items.min_amount` | number | no | Minimum amount for yield. If balance is below this value, yield is not calculated. If no value is provided, any available amount is treated as accrued interest. | format: "float"; example: 1000 |
| `items.processing_codes` | object (schema `SavingsAccountProcessingCodes`) | no |  |  |
| `items.product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `items.product_type` | string | no | Product type. | enum: ["deposit", "savings-account"] |
| `items.status` | string | no | Product status | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `items.start_date` | string | no | Define the earliest date from which the product can be attached to an account or program. Date is displayed in UTC. | format: "date"; example: "2025-11-01" |
| `items.metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>Metadata content is not controlled by the Pismo platform and is instead controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

##### Response 400

400 Example `invalidRequestBody` (Bad Request):

```json
{
  "code": "EIBACC0008",
  "message": "Bad Request",
  "details": "error EIBACC0008: Validation error [(Field 'Order' is invalid)]"
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
| 500 | `EIBACC0007` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-how-overdraft-works`, `KU-BANK-interest-bearing-accounts`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/deposits operationId=interest-bearing-v1-create-deposit-product -->
### `POST /v1/deposits` — Create deposit product

- **operationId:** `interest-bearing-v1-create-deposit-product`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an organization's time deposit accounts. Time deposit accounts, such as CDs, require you to keep your funds in the account for a mutually agreed amount for a specific period of time.<br>
> This endpoint generates the [Deposit product created](https://developers.pismo.io/events/docs/deposit-product-creation-1) event.
> For information about interest-bearing accounts, refer to [Interest-bearing accounts](doc:interest-bearing-accounts).
> The interest plan is fetched once and used to resolve or validate `accrual_model` before any resource configuration. Missing, null, or empty values derive the model from the plan. An explicit mismatch returns `HTTP 400 EIBACC0365`. An unknown nonempty plan model or a missing plan object returns `HTTP 500 EIBACC0007`, and errors from the interest plan API are passed through. None of these failures configure resources, persist a product, or publish a creation event.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `CreateDepositProductRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | The product name. | example: "Tax 1 Default" |
| `interest_plan_id` | string | yes | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `term_type` | string | yes | Term type. For example, `FIXED` or `FLEXIBLE`.<br> | enum: ["FIXED", "FLEXIBLE"]; example: "FIXED" |
| `accrual_model` | string \\\| null | no | Defines the balance basis for daily interest accrual:<br>- `DEPOSIT_BASIS`: Net daily balance change (credits minus debits), determined at the end of the day.<br>- `BALANCE_BASIS`: Daily closing balance.<br><br>If not provided (omitted, `null`, or empty string `""`), the value is derived from the interest plan: `BALANCE-CHANGE` → `DEPOSIT_BASIS` or `CLOSING-BALANCE` → `BALANCE_BASIS`. An explicit value must match the plan; otherwise, the request returns a `400` error: `EIBACC0365`.<br><br>If the plan's `interest_base_model` is missing, `null`, or empty, the Pismo platform treats it as `CLOSING-BALANCE`, which produces `BALANCE_BASIS` when the request does not set `accrual_model`.<br> | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS", "", null]; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Which balance of the `balance_history` event is submitted when `accrual_model` is `BALANCE_BASIS`. `VALUE_DATED_BALANCE` uses the cleared balance (default); `LEDGER_BALANCE` includes uncleared funds. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `maturity_instructions` | object (schema `DepositMaturityInstructions`) | no | - If the principal or interest are `ROLLOVER,` the respective amounts is rolled over to a new deposit term.<br>- If the principal is `NO_ACTION`, no action is taken with the principal amount at maturity.<br>- If the interest is `PAY` and the accrued interest is greater than zero, it's paid to the account's cash balance.<br> |  |
| `processing_codes` | object (schema `DepositProcessingCodes`) | no |  |  |
| `cool_off_period` | integer | no | Period in days when a withdrawal can be made without penalty. | example: 0 |
| `funding_duration` | integer | no | Period during which money is allowed to deposit into the account before the account is blocked. The value of this field is calculated in days. | example: 12 |
| `grace_period_duration_days` | integer | no | Grace‑period duration in days. The maturity date is a hard boundary, and pay, rollover, and detach execute at maturity. The grace window opens at the start of the next cycle, spanning `cycle_start_date`, `cycle_start_date` + `grace_period`. The first cycle does not include a grace-period window. During grace period, interest accrues daily only when `accrue_during_grace_period` is `true`. If you define a grace‑period penalty, configure it under `penalties.grace_period` (`penalty‑grace` still pauses at maturity and is not relocated). | format: "int32"; example: 10 |
| `accrue_during_grace_period` | boolean | no | Controls whether interest continues to accrue during the post‑maturity grace period. When set to `true` (the default), the Pismo platform submits daily accruals to the interest engine. When set to `false`, those submissions stop. If the field is omitted or null, it is treated as `true`. Note that this setting does not change the grace‑period lifecycle. | default: true; example: true |
| `min_amount` | number | no | The minimum balance required to earn yield. If the balance is below this amount, yield is not calculated, and if no value is specified, any available amount is treated as accrued interest. | example: 1000 |
| `max_amount` | number | no | Maximum deposit amount. | example: 5000 |
| `min_term` | integer | no | Minimum term duration. The value of this field is calculated in days. | example: 265 |
| `max_term` | integer | no | Maximum term duration. The value of this field is calculated in days. | example: 1025 |
| `penalties` | object (schema `DepositPenalties`) | no | Set of penalty configurations that can be applied to a deposit product. Each penalty type corresponds to a specific fee ID and transaction flow within the Pismo platform.<br>For details about penalty types, refer to the [Penalty types](doc:penalties-for-cd-accounts#penalty-types) section of Penalties for CD accounts.<br> |  |
| `notices` | array of object (schema `MaturityNotice`) | no | Advance maturity notice configurations for deposit products only, rejected for savings‑account products. If this field is included in a savings‑account request, the API returns `HTTP 400`. When provided, the field must contain one to three entries, each with a unique `days_before_maturity` value. If the field is absent or the array is empty, no notices are configured.<br> | maxItems: 3; example: [{"days_before_maturity": 30, "description": "30-day advance notice"}, {"days_before_maturity": 14, "description": "Final reminder"}] |
| `start_date` | string | no | Define the earliest date from which the product can be attached to an account or program. Attach operations attempted before this date are rejected. Date is displayed in UTC. | format: "date"; example: "2025-11-01" |
| `end_date` | string | no | Defines the final date when the product can be attached to an account or program, rejects any attach operations submitted after that date, uses the `yyyy‑mm‑dd` format with all dates shown in UTC+0 regardless of your timezone, and must be set at least one day after the current date (D+1). | format: "date"; example: "2027-12-31" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>Metadata content is not controlled by the Pismo platform and is instead controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `DepositProduct`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict — the penalty processing code already has a divergent tenant balance-config | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cool_off_period` | integer | no | Period in days when a withdrawal can be made without penalty. | example: 0 |
| `created_at` | string | no | Date and time the product was created | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `funding_duration` | integer | no | Period during which money is allowed to deposit into the account before the account is blocked. The value of this field is calculated in days. | example: 12 |
| `interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `maturity_instructions` | object (schema `DepositMaturityInstructions`) | no | - If the principal or interest are `ROLLOVER,` the respective amounts is rolled over to a new deposit term.<br>- If the principal is `NO_ACTION`, no action is taken with the principal amount at maturity.<br>- If the interest is `PAY` and the accrued interest is greater than zero, it's paid to the account's cash balance.<br> |  |
| `min_amount` | number | no | The minimum balance required to earn yield. If the balance is below this amount, yield is not calculated, and if no value is specified, any available amount is treated as accrued interest. | example: 1000 |
| `max_amount` | number | no | Maximum deposit amount. | example: 5000 |
| `min_term` | integer | no | Minimum term duration. The value of this field is calculated in days. | example: 265 |
| `max_term` | integer | no | Maximum term duration. The value of this field is calculated in days. | example: 1025 |
| `grace_period_duration_days` | integer | no | The number of days in the grace period. Applies only when no grace‑period penalty is defined. The grace‑period window opens at the start of the next cycle, spanning `cycle_start_date`, `cycle_start_date` + `grace_period_duration_days`, and the renewed cycle’s maturity extends by these days (`cycle_start_date` + `grace_period_duration_days` + term - 1, inclusive). The first cycle does not include a grace period. During grace period, interest accrues daily only when `accrue_during_grace_period` is `true`. | example: 30 |
| `accrue_during_grace_period` | boolean | no | Whether interest accrues daily during the grace window. Defaults to true. When false, no submissions are sent to the Interest Engine during grace (audited as `IN_GRACE_NO_ACCRUAL`) and accrual starts when grace ends. Deposit products only. | example: true |
| `name` | string | no | Product name | example: "Tax 1 Default" |
| `penalties` | object (schema `DepositPenalties`) | no | Set of penalty configurations that can be applied to a deposit product. Each penalty type corresponds to a specific fee ID and transaction flow within the Pismo platform.<br>For details about penalty types, refer to the [Penalty types](doc:penalties-for-cd-accounts#penalty-types) section of Penalties for CD accounts.<br> |  |
| `notices` | array of object (schema `MaturityNotice`) | no | Advance maturity notice configurations for deposit products only, rejected for savings‑account products. If this field is included in a savings‑account request, the API returns `HTTP 400`. When provided, the field must contain one to three entries, each with a unique `days_before_maturity` value. If the field is absent or the array is empty, no notices are configured.<br> | maxItems: 3 |
| `processing_codes` | object (schema `DepositProcessingCodes`) | no |  |  |
| `product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `product_type` | string | no | Product type | enum: ["deposit", "savings-account"] |
| `status` | string | no | Indicates the current state of the product. For example, `CREATED`. | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "CREATED" |
| `term_type` | string | no | Term type. For example, `FIXED` or `FLEXIBLE`.<br> | enum: ["FIXED", "FLEXIBLE"]; example: "FIXED" |
| `accrual_model` | string | no | Interest accrual model configured at the product level and returned in both the creation event and API response.<br>With `DEPOSIT_BASIS`, the Pismo platform calculates accruals based on the net daily balance change (credits minus debits) at the end of each day.<br>With `BALANCE_BASIS`, accruals are calculated using the account's closing balance at the end of the day, regardless of whether any transactions occurred. For example, if an account has a balance of 1000 and no transactions are made during the day, the platform still uses 1000 as the accrual basis.<br>At creation, the interest plan determines the model: `BALANCE-CHANGE` maps to `DEPOSIT_BASIS`, and `CLOSING-BALANCE` maps to `BALANCE_BASIS`.<br> | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Which balance of the `balance_history` event is submitted when `accrual_model` is `BALANCE_BASIS`. `VALUE_DATED_BALANCE` uses the cleared balance (default); `LEDGER_BALANCE` includes uncleared funds. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `start_date` | string | no | Defines the earliest date from which the product can be attached to an account or program. Date is displayed in UTC. | format: "date"; example: "2025-11-01" |
| `end_date` | string | no | Defines the final date when the product can be attached to an account or program, rejects any attach operations submitted after that date, uses the `yyyy‑mm‑dd` format with all dates shown in UTC+0 regardless of your timezone, and must be set at least one day after the current date (D+1). | format: "date"; example: "2027-12-31" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>Metadata content is not controlled by the Pismo platform and is instead controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

##### Response 400

400 Example `invalidRequestBody` (Bad Request):

```json
{
  "code": "EIBACC0008",
  "message": "Bad Request",
  "details": "error EIBACC0008: Validation error [(Field 'Order' is invalid)]"
}
```

##### Response 409

409 Example `divergentPenaltyBalanceConfig` (The penalty processing code already has a divergent tenant balance-config (deposit with penalties)):

```json
{
  "code": "EIBACC0393",
  "message": "Penalty processing code has a balance‑config that conflicts with the required penalty configuration"
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
| 409 | `EIBACC0393` | Penalty processing code has a balance‑config that conflicts with the required penalty configuration |
| 500 | `EIBACC0007` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `deposit-product-creation-1` | https://developers.pismo.io/events/docs/deposit-product-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-interest-bearing-accounts`, `KU-BANK-penalties-for-cd-accounts`, `KU-EVT-interest-management-data-events`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=GET path=/v1/deposits/{productId} operationId=interest-bearing-v1-get-deposit-products -->
### `GET /v1/deposits/{productId}` — Get deposit product

- **operationId:** `interest-bearing-v1-get-deposit-products`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get deposit product by product ID. Note that product ID is Pismo-generated.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | yes | string | Product ID | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `DepositProduct`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cool_off_period` | integer | no | Period in days when a withdrawal can be made without penalty. | example: 0 |
| `created_at` | string | no | Date and time the product was created | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `funding_duration` | integer | no | Period during which money is allowed to deposit into the account before the account is blocked. The value of this field is calculated in days. | example: 12 |
| `interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `maturity_instructions` | object (schema `DepositMaturityInstructions`) | no | - If the principal or interest are `ROLLOVER,` the respective amounts is rolled over to a new deposit term.<br>- If the principal is `NO_ACTION`, no action is taken with the principal amount at maturity.<br>- If the interest is `PAY` and the accrued interest is greater than zero, it's paid to the account's cash balance.<br> |  |
| `min_amount` | number | no | The minimum balance required to earn yield. If the balance is below this amount, yield is not calculated, and if no value is specified, any available amount is treated as accrued interest. | example: 1000 |
| `max_amount` | number | no | Maximum deposit amount. | example: 5000 |
| `min_term` | integer | no | Minimum term duration. The value of this field is calculated in days. | example: 265 |
| `max_term` | integer | no | Maximum term duration. The value of this field is calculated in days. | example: 1025 |
| `grace_period_duration_days` | integer | no | The number of days in the grace period. Applies only when no grace‑period penalty is defined. The grace‑period window opens at the start of the next cycle, spanning `cycle_start_date`, `cycle_start_date` + `grace_period_duration_days`, and the renewed cycle’s maturity extends by these days (`cycle_start_date` + `grace_period_duration_days` + term - 1, inclusive). The first cycle does not include a grace period. During grace period, interest accrues daily only when `accrue_during_grace_period` is `true`. | example: 30 |
| `accrue_during_grace_period` | boolean | no | Whether interest accrues daily during the grace window. Defaults to true. When false, no submissions are sent to the Interest Engine during grace (audited as `IN_GRACE_NO_ACCRUAL`) and accrual starts when grace ends. Deposit products only. | example: true |
| `name` | string | no | Product name | example: "Tax 1 Default" |
| `penalties` | object (schema `DepositPenalties`) | no | Set of penalty configurations that can be applied to a deposit product. Each penalty type corresponds to a specific fee ID and transaction flow within the Pismo platform.<br>For details about penalty types, refer to the [Penalty types](doc:penalties-for-cd-accounts#penalty-types) section of Penalties for CD accounts.<br> |  |
| `notices` | array of object (schema `MaturityNotice`) | no | Advance maturity notice configurations for deposit products only, rejected for savings‑account products. If this field is included in a savings‑account request, the API returns `HTTP 400`. When provided, the field must contain one to three entries, each with a unique `days_before_maturity` value. If the field is absent or the array is empty, no notices are configured.<br> | maxItems: 3 |
| `processing_codes` | object (schema `DepositProcessingCodes`) | no |  |  |
| `product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `product_type` | string | no | Product type | enum: ["deposit", "savings-account"] |
| `status` | string | no | Indicates the current state of the product. For example, `CREATED`. | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "CREATED" |
| `term_type` | string | no | Term type. For example, `FIXED` or `FLEXIBLE`.<br> | enum: ["FIXED", "FLEXIBLE"]; example: "FIXED" |
| `accrual_model` | string | no | Interest accrual model configured at the product level and returned in both the creation event and API response.<br>With `DEPOSIT_BASIS`, the Pismo platform calculates accruals based on the net daily balance change (credits minus debits) at the end of each day.<br>With `BALANCE_BASIS`, accruals are calculated using the account's closing balance at the end of the day, regardless of whether any transactions occurred. For example, if an account has a balance of 1000 and no transactions are made during the day, the platform still uses 1000 as the accrual basis.<br>At creation, the interest plan determines the model: `BALANCE-CHANGE` maps to `DEPOSIT_BASIS`, and `CLOSING-BALANCE` maps to `BALANCE_BASIS`.<br> | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Which balance of the `balance_history` event is submitted when `accrual_model` is `BALANCE_BASIS`. `VALUE_DATED_BALANCE` uses the cleared balance (default); `LEDGER_BALANCE` includes uncleared funds. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `start_date` | string | no | Defines the earliest date from which the product can be attached to an account or program. Date is displayed in UTC. | format: "date"; example: "2025-11-01" |
| `end_date` | string | no | Defines the final date when the product can be attached to an account or program, rejects any attach operations submitted after that date, uses the `yyyy‑mm‑dd` format with all dates shown in UTC+0 regardless of your timezone, and must be set at least one day after the current date (D+1). | format: "date"; example: "2027-12-31" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>Metadata content is not controlled by the Pismo platform and is instead controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

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

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=PATCH path=/v1/deposits/{productId} operationId=interest-bearing-v1-patch-deposit-product -->
### `PATCH /v1/deposits/{productId}` — Update deposit product

- **operationId:** `interest-bearing-v1-patch-deposit-product`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update deposit by product ID. Note that product ID is Pismo-generated.<br>
> This endpoint generates the [Deposit product updated](https://developers.pismo.io/events/docs/deposit-product-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | yes | string | Product ID | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `PatchProductRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string | no | Product status | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `reason` | string | no | Status update reason. Required when `status` is provided. | maxLength: 128; example: "Activating product" |
| `min_amount` | number | no | The minimum balance required to earn yield. When provided, must be greater than 0. Applied from the moment of a successful update (Not retroactive. Accounts already opened are not revalidated). | example: 50 |
| `notices` | array of object (schema `MaturityNotice`) | no | Advance maturity notice configurations for deposit products only, rejected for savings‑account products. If this field is included in a savings‑account request, the API returns `HTTP 400`. When provided, the field must contain one to three entries, each with a unique `days_before_maturity` value. If the field is absent or the array is empty, no notices are configured.<br> | maxItems: 3; example: [{"days_before_maturity": 60, "description": "Updated single 60-day notice"}] |
| `accrue_during_grace_period` | boolean | no | Controls whether interest accrual continues during the post‑maturity grace period. Applies only to deposit products. The value is read live and takes effect on the next daily cycle. It does not alter the grace‑period lifecycle. | example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Success |  |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `deposit-product-update-1` | https://developers.pismo.io/events/docs/deposit-product-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-interest-bearing-accounts`, `KU-EVT-interest-management-data-events`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/savings-accounts operationId=interest-bearing-v1-create-savings-account-product -->
### `POST /v1/savings-accounts` — Create savings account product

- **operationId:** `interest-bearing-v1-create-savings-account-product`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an organization's savings account product. Savings account products accrue interest based on the balance at the time of the interest calculation.<br>
> This endpoint generates the [Savings account product created](https://developers.pismo.io/events/docs/savings-account-product-creation-1) event.
> For information about interest-bearing accounts, see [Interest-bearing accounts](doc:interest-bearing-accounts).
> The interest plan is fetched once and used to resolve or validate `accrual_model` before any resource configuration. Missing, null, or empty values derive the model from the plan. An explicit mismatch returns `HTTP 400 EIBACC0365`. An unknown nonempty plan model or a missing plan object returns `HTTP 500 EIBACC0007`, and errors from the interest plan API are passed through. None of these failures configure resources, persist a product, or publish a creation event.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `CreateSavingsAccountProductRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_plan_id` | string | yes | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `name` | string | yes | The product name. | example: "Tax 1 Default" |
| `accrual_model` | string \\\| null | no | Defines the balance basis for daily interest accrual:<br>- `DEPOSIT_BASIS`: Net daily balance change (credits minus debits), determined at the end of the day.<br>- `BALANCE_BASIS`: Daily closing balance.<br><br>If not provided (omitted, `null`, or empty string `""`), the value is derived from the interest plan: `BALANCE-CHANGE` → `DEPOSIT_BASIS` or `CLOSING-BALANCE` → `BALANCE_BASIS`. An explicit value must match the plan; otherwise, the request returns a `400` error: `EIBACC0365`.<br><br>If the plan's `interest_base_model` is missing, `null`, or empty, the Pismo platform treats it as `CLOSING-BALANCE`, which produces `BALANCE_BASIS` when the request does not set `accrual_model`.<br> | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS", "", null]; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Which balance of the `balance_history` event is submitted when `accrual_model` is `BALANCE_BASIS`. `VALUE_DATED_BALANCE` uses the cleared balance (default). `LEDGER_BALANCE` includes uncleared funds. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `min_amount` | number | no | Minimum amount for yield. If balance is below this value, yield is not calculated. If no value is provided, any available amount is treated as accrued interest. | format: "float"; example: 1000 |
| `processing_codes` | object (schema `SavingsAccountProcessingCodes`) | yes |  |  |
| `start_date` | string | no | Defines the earliest date from which the product can be attached to an account or program. Attach operations attempted before this date are rejected. Date is displayed in UTC. | format: "date"; example: "2025-11-01" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>The platform has no control over its content, but rather controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Success | `application/json`: object (schema `SavingsAccountProduct`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `created_at` | string | no | The moment when a product is created. | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `updated_at` | string | no | The moment when a product is updated. | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `name` | string | no | The product name. | example: "Tax 1 Default" |
| `accrual_model` | string | no | Interest accrual model configured at the product level and returned in both the creation event and API response.<br>With `DEPOSIT_BASIS`, the Pismo platform calculates accruals based on the net daily balance change (credits minus debits) at the end of each day.<br>With `BALANCE_BASIS`, accruals are calculated using the account's closing balance at the end of the day, regardless of whether any transactions occurred. For example, if an account has a balance of 1000 and no transactions are made during the day, the platform still uses 1000 as the accrual basis.<br>At creation, the interest plan determines the model: `BALANCE-CHANGE` maps to `DEPOSIT_BASIS`, and `CLOSING-BALANCE` maps to `BALANCE_BASIS`.<br> | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Which balance of the `balance_history` event is submitted when `accrual_model` is `BALANCE_BASIS`. `VALUE_DATED_BALANCE` uses the cleared balance (default). `LEDGER_BALANCE` includes uncleared funds. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `min_amount` | number | no | Minimum amount for yield. If balance is below this value, yield is not calculated. If no value is provided, any available amount is treated as accrued interest. | format: "float"; example: 1000 |
| `processing_codes` | object (schema `SavingsAccountProcessingCodes`) | no |  |  |
| `product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `product_type` | string | no | Product type. | enum: ["deposit", "savings-account"] |
| `status` | string | no | Product status | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `start_date` | string | no | Define the earliest date from which the product can be attached to an account or program. Date is displayed in UTC. | format: "date"; example: "2025-11-01" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>Metadata content is not controlled by the Pismo platform and is instead controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

##### Response 400

400 Example `invalidRequestBody` (Bad Request):

```json
{
  "code": "EIBACC0008",
  "message": "Bad Request",
  "details": "error EIBACC0008: Validation error [(Field 'Order' is invalid)]"
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
| 500 | `EIBACC0007` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `savings-account-product-creation-1` | https://developers.pismo.io/events/docs/savings-account-product-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-interest-bearing-accounts`, `KU-EVT-interest-management-data-events`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=GET path=/v1/savings-accounts/{productId} operationId=interest-bearing-v1-get-savings-account-products -->
### `GET /v1/savings-accounts/{productId}` — Get savings account product

- **operationId:** `interest-bearing-v1-get-savings-account-products`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get saving accounts product by product ID. Note that product ID is Pismo-generated.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | yes | string | Product ID | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `SavingsAccountProduct`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `created_at` | string | no | The moment when a product is created. | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `updated_at` | string | no | The moment when a product is updated. | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `name` | string | no | The product name. | example: "Tax 1 Default" |
| `accrual_model` | string | no | Interest accrual model configured at the product level and returned in both the creation event and API response.<br>With `DEPOSIT_BASIS`, the Pismo platform calculates accruals based on the net daily balance change (credits minus debits) at the end of each day.<br>With `BALANCE_BASIS`, accruals are calculated using the account's closing balance at the end of the day, regardless of whether any transactions occurred. For example, if an account has a balance of 1000 and no transactions are made during the day, the platform still uses 1000 as the accrual basis.<br>At creation, the interest plan determines the model: `BALANCE-CHANGE` maps to `DEPOSIT_BASIS`, and `CLOSING-BALANCE` maps to `BALANCE_BASIS`.<br> | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Which balance of the `balance_history` event is submitted when `accrual_model` is `BALANCE_BASIS`. `VALUE_DATED_BALANCE` uses the cleared balance (default). `LEDGER_BALANCE` includes uncleared funds. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `min_amount` | number | no | Minimum amount for yield. If balance is below this value, yield is not calculated. If no value is provided, any available amount is treated as accrued interest. | format: "float"; example: 1000 |
| `processing_codes` | object (schema `SavingsAccountProcessingCodes`) | no |  |  |
| `product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `product_type` | string | no | Product type. | enum: ["deposit", "savings-account"] |
| `status` | string | no | Product status | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `start_date` | string | no | Define the earliest date from which the product can be attached to an account or program. Date is displayed in UTC. | format: "date"; example: "2025-11-01" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>Metadata content is not controlled by the Pismo platform and is instead controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

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

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=PATCH path=/v1/savings-accounts/{productId} operationId=interest-bearing-v1-patch-savings-account-product -->
### `PATCH /v1/savings-accounts/{productId}` — Update savings account product

- **operationId:** `interest-bearing-v1-patch-savings-account-product`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Product`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a savings account product by product ID. Note that product ID is Pismo-generated.<br>
> This endpoint generates the [Savings account product updated](https://developers.pismo.io/events/docs/savings-account-product-update-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `productId` | path | yes | string | Product ID | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `PatchProductRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string | no | Product status | enum: ["CREATED", "ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `reason` | string | no | Status update reason. Required when `status` is provided. | maxLength: 128; example: "Activating product" |
| `min_amount` | number | no | The minimum balance required to earn yield. When provided, must be greater than 0. Applied from the moment of a successful update (Not retroactive. Accounts already opened are not revalidated). | example: 50 |
| `notices` | array of object (schema `MaturityNotice`) | no | Advance maturity notice configurations for deposit products only, rejected for savings‑account products. If this field is included in a savings‑account request, the API returns `HTTP 400`. When provided, the field must contain one to three entries, each with a unique `days_before_maturity` value. If the field is absent or the array is empty, no notices are configured.<br> | maxItems: 3; example: [{"days_before_maturity": 60, "description": "Updated single 60-day notice"}] |
| `accrue_during_grace_period` | boolean | no | Controls whether interest accrual continues during the post‑maturity grace period. Applies only to deposit products. The value is read live and takes effect on the next daily cycle. It does not alter the grace‑period lifecycle. | example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Success |  |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

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

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `savings-account-product-update-1` | https://developers.pismo.io/events/docs/savings-account-product-update-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-interest-management-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/DepositMaturityInstructions -->
### Schema `DepositMaturityInstructions`

Pointer: `#/components/schemas/DepositMaturityInstructions`. Type: object (schema `DepositMaturityInstructions`).

> - If the principal or interest are `ROLLOVER,` the respective amounts is rolled over to a new deposit term.
> - If the principal is `NO_ACTION`, no action is taken with the principal amount at maturity.
> - If the interest is `PAY` and the accrued interest is greater than zero, it's paid to the account's cash balance.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `principal` | string | no | Specifies the status of the principal amount at maturity.<br>- `NO_ACTION`: No action is taken with the principal amount<br>- `ROLLOVER`: The principal amount is rolled over to a new deposit term<br><br>If no value is selected, the principal defaults to `NO_ACTION`.<br> | enum: ["NO_ACTION", "ROLLOVER"]; default: "NO_ACTION"; example: "ROLLOVER" |
| `interest` | string | no | Specifies the status of the accrued interest at maturity.<br>- `PAY`: The accrued interest is paid to the account<br>- `ROLLOVER`: The accrued interest is rolled over and added to the principal<br><br>If no value is selected, the interest defaults to `PAY`.<br> | enum: ["PAY", "ROLLOVER"]; default: "PAY"; example: "PAY" |

<!-- schema: #/components/schemas/DepositPenalties -->
### Schema `DepositPenalties`

Pointer: `#/components/schemas/DepositPenalties`. Type: object (schema `DepositPenalties`).

> Set of penalty configurations that can be applied to a deposit product. Each penalty type corresponds to a specific fee ID and transaction flow within the Pismo platform.
> For details about penalty types, refer to the [Penalty types](doc:penalties-for-cd-accounts#penalty-types) section of Penalties for CD accounts.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `early_withdrawal_after_opening` | object (schema `EarlyWithdrawalAfterOpening`) | no | This penalty corresponds to fee ID `earlyWithdrawalAfterOpeningPenaltyID` and transaction flow `earlyWithdrawalAfterOpeningPenalty` |  |
| `grace_period` | object (schema `GracePeriod`) | no | This penalty corresponds to fee ID `gracePeriodPenaltyID` and trasaction flow `gracePeriodPenalty` |  |
| `tiered_interest_forfeiture` | array of object (schema `TieredInterestForfeitureTier`) | no | This penalty corresponds to fee ID `tieredInterestForfeiturePenaltyID` and transaction flow `tieredInterestForfeiturePenalty` |  |
| `withdrawal_fee` | object (schema `WithdrawalFee`) | no | This penalty corresponds to fee ID `withdrawalFeePenaltyID` and transaction flow `withdrawalFeePenalty` |  |
| `subsequent_withdrawals` | object (schema `SubsequentWithdrawals`) | no | This penalty corresponds to fee ID `subsequentWithdrawalPenaltyID` and transaction flow `subsequentWithdrawalPenalty`.<br><br>Settings for the subsequent withdrawal penalty (Regulation D).<br>A penalty fee is applied when a customer makes a withdrawal within the configured window.<br>The window either resets with each withdrawal (ROLLING) or remains fixed from the first withdrawal (FIXED).<br> |  |

<!-- schema: #/components/schemas/MaturityNotice -->
### Schema `MaturityNotice`

Pointer: `#/components/schemas/MaturityNotice`. Type: object (schema `MaturityNotice`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `days_before_maturity` | integer | yes | Number of days before the account’s maturity date when the notice is sent. The value must be a positive integer greater than zero. Inputs such as zero, negative numbers, decimals, null, or non-numeric values result in `HTTP 400`. Each notice must use a distinct `days_before_maturity` value within the array.<br> | minimum: 1; example: 30 |
| `description` | string | yes | A short, human‑readable label for the notice. Each entry must include one description, and it cannot exceed 128 characters.<br> | maxLength: 128; example: "30-day advance notice" |

<!-- schema: #/components/schemas/DepositProcessingCodes -->
### Schema `DepositProcessingCodes`

Pointer: `#/components/schemas/DepositProcessingCodes`. Type: object (schema `DepositProcessingCodes`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_processing_code` | string | no | Processing code for interest calculation. <br> If you don't specify a value, the default is `009797`. | example: "009797" |
| `detach_processing_code` | string | no | Processing code for detaching deposit feature from a bank account.<br><br>Detaching means the bank removes the deposit feature from the bank account.<br>If you don't specify a value, the default is `009696`.<br> | example: "009696" |

<!-- schema: #/components/schemas/SavingsAccountProcessingCodes -->
### Schema `SavingsAccountProcessingCodes`

Pointer: `#/components/schemas/SavingsAccountProcessingCodes`. Type: object (schema `SavingsAccountProcessingCodes`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `interest_processing_code` | string | no | Processing code for interest calculation. <br> If you don't specify a value, the default is `009797`. | example: "009797" |
| `detach_processing_code` | string | no | Processing code for detaching deposit feature from a bank account.<br><br>Detaching means the bank removes the deposit feature from the bank account.<br>If you don't specify a value, the default is `009696`.<br> | example: "009696" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code | example: "EIBACC0003" |
| `details` | string | no | Error details | example: "error EIBACC0008: Validation error [(Field 'Order' is invalid)]" |
| `message` | string | no | Error message | example: "Bad Request" |

<!-- schema: #/components/schemas/EarlyWithdrawalAfterOpening -->
### Schema `EarlyWithdrawalAfterOpening`

Pointer: `#/components/schemas/EarlyWithdrawalAfterOpening`. Type: object (schema `EarlyWithdrawalAfterOpening`).

> This penalty corresponds to fee ID `earlyWithdrawalAfterOpeningPenaltyID` and transaction flow `earlyWithdrawalAfterOpeningPenalty`

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `applicable_within_days` | integer | yes | Number of days after opening that the penalty is applied | minimum: 0; example: 30 |
| `penalty_interest_days` | integer | yes | Number of days multiplied by the applicable interest or earnings rate to determine the penalty amount. | minimum: 0; example: 90 |

<!-- schema: #/components/schemas/GracePeriod -->
### Schema `GracePeriod`

Pointer: `#/components/schemas/GracePeriod`. Type: object (schema `GracePeriod`).

> This penalty corresponds to fee ID `gracePeriodPenaltyID` and trasaction flow `gracePeriodPenalty`

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `duration_days` | integer | yes | Duration of the grace period in days | minimum: 0; example: 7 |
| `penalty_interest_days` | integer | yes | Number of interest days to forfeit as penalty | minimum: 0; example: 30 |

<!-- schema: #/components/schemas/TieredInterestForfeitureTier -->
### Schema `TieredInterestForfeitureTier`

Pointer: `#/components/schemas/TieredInterestForfeitureTier`. Type: object (schema `TieredInterestForfeitureTier`).

> This penalty corresponds to fee ID `tieredInterestForfeiturePenaltyID` and transaction flow `tieredInterestForfeiturePenalty`

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `min_days_held` | integer | yes | Minimum number of days the deposit must be held | example: 1 |
| `max_days_held` | integer | yes | Maximum number of days the deposit can be held | example: 90 |
| `forfeited_interest_days` | integer | yes | Number of interest days to forfeit as penalty | example: 30 |

<!-- schema: #/components/schemas/WithdrawalFee -->
### Schema `WithdrawalFee`

Pointer: `#/components/schemas/WithdrawalFee`. Type: object (schema `WithdrawalFee`).

> This penalty corresponds to fee ID `withdrawalFeePenaltyID` and transaction flow `withdrawalFeePenalty`

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `type` | string | yes | Withdrawal fee type | enum: ["PERCENTAGE", "FIXED"]; example: "PERCENTAGE" |
| `value` | number | yes | Value of the withdrawal fee | example: 1.5 |

<!-- schema: #/components/schemas/SubsequentWithdrawals -->
### Schema `SubsequentWithdrawals`

Pointer: `#/components/schemas/SubsequentWithdrawals`. Type: object (schema `SubsequentWithdrawals`).

> This penalty corresponds to fee ID `subsequentWithdrawalPenaltyID` and transaction flow `subsequentWithdrawalPenalty`.<br>
> Settings for the subsequent withdrawal penalty (Regulation D).
> A penalty fee is applied when a customer makes a withdrawal within the configured window.
> The window either resets with each withdrawal (ROLLING) or remains fixed from the first withdrawal (FIXED).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `applicable_within_days` | integer | yes | The number of days following a withdrawal during which a subsequent withdrawal triggers the penalty.<br>Must be at least 1.<br> | minimum: 1; example: 30 |
| `window_behavior` | string | yes | Controls how the penalty window is managed after each withdrawal:<br>- `ROLLING`: the window resets on every withdrawal (scheduler is replaced)<br>- `FIXED`: the window is set once on the first withdrawal and does not reset<br> | enum: ["ROLLING", "FIXED"]; example: "ROLLING" |
| `penalty_interest_days` | integer | no | Number of interest days to forfeit as the penalty amount.<br>Must be at least 1 when provided.<br> | minimum: 1; example: 7 |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Interest-bearing_accounts.yaml` | tag `Product`: GET /v1/products, POST /v1/deposits, GET /v1/deposits/{productId}, PATCH /v1/deposits/{productId}, POST /v1/savings-accounts, GET /v1/savings-accounts/{productId}, PATCH /v1/savings-accounts/{productId} | https://github.com/PismoDevEx/pismo-api-specs | `89fc3f8ed0222a57…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-how-overdraft-works` — How overdraft works
- `KU-BANK-interest-bearing-accounts` — Interest-bearing accounts
- `KU-BANK-penalties-for-cd-accounts` — Penalties and taxes for CD accounts
- `KU-ERR-codes-eibacc` — Error codes: EIBACC
- `KU-EVT-catalogue-deposit` — Event catalogue: deposit
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-interest-management-data-events` — Banking - Interest management
