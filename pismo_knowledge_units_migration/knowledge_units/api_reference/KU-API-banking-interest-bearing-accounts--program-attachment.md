---
ku_id: KU-API-banking-interest-bearing-accounts--program-attachment
title: 'API reference: Banking - Interest-bearing accounts — Program attachment'
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
- interest-bearing-v1-get-program-attachment
- interest-bearing-v1-deposit-attach-program
- interest-bearing-v1-deposit-update-program-attachment
- interest-bearing-v1-savings-account-attach-program
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-ERR-codes-eibacc
- KU-EVT-catalogue-deposit
- KU-EVT-interest-management-data-events
specification_version: 1.0.0
---

# API reference: Banking - Interest-bearing accounts — Program attachment

**KU ID:** `KU-API-banking-interest-bearing-accounts--program-attachment` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Program attachment` in `api-specs/Banking_-_Interest-bearing_accounts.yaml` (“Banking - Interest-bearing accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that manage program attachments to interest-bearing account products

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/products/attachments/programs/{programId}` | `interest-bearing-v1-get-program-attachment` | Get program attachment | no |
| `POST /v1/deposits/programs/{programId}/attach` | `interest-bearing-v1-deposit-attach-program` | Attach deposit product to program | no |
| `PATCH /v1/deposits/programs/{programId}/attachment` | `interest-bearing-v1-deposit-update-program-attachment` | Update deposit program attachment overrides | no |
| `POST /v1/savings-accounts/programs/{programId}/attach` | `interest-bearing-v1-savings-account-attach-program` | Attach savings accounts to program | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=GET path=/v1/products/attachments/programs/{programId} operationId=interest-bearing-v1-get-program-attachment -->
### `GET /v1/products/attachments/programs/{programId}` — Get program attachment

- **operationId:** `interest-bearing-v1-get-program-attachment`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Program attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a program's attached product.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 123 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `ProgramAttachment`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_type` | string | no | Product type. | enum: ["deposit", "savings-account"] |
| `product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `attachment_date` | string | no | Timestamp that indicates when the attachment was created (when the attach API call was made).<br>The datetime format follows the ISO 8601 standard `yyyy-mm-ddThh:mm:ss.sssZ`.<br> | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `effective_date` | string | no | The effective date of the attachment in `YYYY-MM-DD` format<br>This is the date when the attachment becomes valid. Maturity is calculated from this date.<br>For attachments created in the past, the date defaults to the value of `attachment_date`.<br> | format: "date"; example: "2025-12-01" |
| `fee_model_id` | string | no | Fee model identifier, if applicable. | example: "fee-model-123" |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `interest_capitalization_mode` | string | no | Present only when this program attachment explicitly defines `interest_capitalization_mode`. If the field is missing, the Pismo platform applies `REINVEST` as the default behavior. All accounts linked to the program inherit this value unless an account‑level configuration provides its own setting.<br> | enum: ["PAYOUT", "REINVEST"]; example: "REINVEST" |
| `overrides` | object | no | Optional. Only returned when at least one override is configured for the attachment. |  |
| `overrides.maturity_instructions` | object (schema `MaturityInstructionsOverrideRequest`) | no | Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.<br> |  |
| `overrides.renewal_term` | object (schema `RenewalTermResponse`) | no | Renewal term applied on each rollover. Always returns all three fields together — `unit`, `value` and `renewal_calendar_maturity_date` — regardless of the form the client used to configure it, mirroring `maturity_period`. Legacy terms persisted before the calendar date was stored return only `unit`+`value`.<br> |  |
| `overrides.penalties` | object (schema `PenaltiesOverrideSnapshot`) | no | Persisted penalty overrides for each type. Types appear only when set. Each entry includes `waived`, the relevant type-specific fields, and an optional `valid_until` for scheduling the revert.<br> |  |
| `accrual_model` | string | no | Accrual model inherited from the attached product. `DEPOSIT_BASIS` or `BALANCE_BASIS`. | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; default: "DEPOSIT_BASIS"; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Balance type inherited from the attached product. Only meaningful when `accrual_model` is `BALANCE_BASIS`. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |

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

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/deposits/programs/{programId}/attach operationId=interest-bearing-v1-deposit-attach-program -->
### `POST /v1/deposits/programs/{programId}/attach` — Attach deposit product to program

- **operationId:** `interest-bearing-v1-deposit-attach-program`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Program attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Attach a time deposit product to a program.
> This endpoint generates the [Program attached](https://developers.pismo.io/events/docs/deposit-product-program-attach-1) event.
>
> At the program scope, `deposit_configs.overrides` only accepts `renewal_term`.
> Sending `penalties` returns `400 EIBACC0317` and sending `maturity_instructions`
> returns `400 EIBACC0318` — apply those per-account instead.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 123 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `ProgramDepositAttachRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | yes | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `deposit_configs` | object (schema `ProgramDepositConfigs`) | no |  |  |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>The platform has no control over its content, but rather controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `DepositAttachProgramResponse`) |
| 400 | Bad Request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict. | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | integer | no | Program identifier. | example: 123 |
| `product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `deposit_configs` | object | no |  |  |
| `deposit_configs.maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `deposit_configs.interest_capitalization_mode` | string | no | Present only when the request included `interest_capitalization_mode`. Reflects the value stored on the attachment.<br> | enum: ["PAYOUT", "REINVEST"]; example: "PAYOUT" |
| `deposit_configs.accrual_model` | string | no | Accrual model inherited from the attached product. `DEPOSIT_BASIS` or `BALANCE_BASIS`. | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; default: "DEPOSIT_BASIS"; example: "DEPOSIT_BASIS" |
| `deposit_configs.balance_type` | string | no | Balance type inherited from the attached product. Only meaningful when `accrual_model` is `BALANCE_BASIS`. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |
| `deposit_configs.overrides` | object (schema `AttachmentOverridesSnapshot`) | no | Representation of the persisted overrides, present only when the request defined at least one override. Sub-fields are included only when set. The `renewal_term` always returns all three fields together (`unit`, `value` and `renewal_calendar_maturity_date`), mirroring the behavior of `maturity_period`.<br> |  |

##### Response 400

400 Example `validationError` (Generic validation error):

```json
{
  "code": "EIBACC0008",
  "message": "Bad Request"
}
```

400 Example `programLevelPenaltiesNotSupported` (penalties not supported at program-level):

```json
{
  "code": "EIBACC0317",
  "message": "deposit_configs.overrides.penalties is not supported at program-level; apply per-account instead"
}
```

400 Example `programLevelMaturityInstructionsNotSupported` (maturity_instructions not supported at program-level):

```json
{
  "code": "EIBACC0318",
  "message": "deposit_configs.overrides.maturity_instructions is not supported at program-level; apply per-account instead"
}
```

400 Example `overrideValidUntilPast` (valid_until must be a future datetime):

```json
{
  "code": "EIBACC0308",
  "message": "valid_until must be a future datetime"
}
```

400 Example `renewalTermMutuallyExclusive` (renewal_term — calendar date and unit/value are mutually exclusive):

```json
{
  "code": "EIBACC0309",
  "message": "Validation error",
  "details": "renewal_term accepts either renewal_calendar_maturity_date OR unit+value, not both."
}
```

400 Example `renewalTermRequiresRollover` (renewal_term requires ROLLOVER in maturity_instructions):

```json
{
  "code": "EIBACC0310",
  "message": "Validation error",
  "details": "renewal_term requires ROLLOVER configured in maturity_instructions.principal or maturity_instructions.interest (account/program override or product default)."
}
```

400 Example `renewalCalendarMaturityDateNotFuture` (renewal_calendar_maturity_date must be a future date):

```json
{
  "code": "EIBACC0311",
  "message": "Validation error",
  "details": "renewal_calendar_maturity_date must be a future date (after today)"
}
```

400 Example `renewalTermFieldsMissing` (renewal_term requires unit+value or renewal_calendar_maturity_date):

```json
{
  "code": "EIBACC0312",
  "message": "Validation error",
  "details": "renewal_term requires either both unit and value, or renewal_calendar_maturity_date"
}
```

400 Example `capitalizationPayoutRequiresPayoutAccount` (switching to PAYOUT requires a payout_account on the attachment):

```json
{
  "code": "EIBACC0379",
  "message": "interest_capitalization_mode PAYOUT requires a fully resolved payout_account",
  "details": "A payout_account must be configured on the attachment before interest_capitalization_mode can be set to PAYOUT."
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

409 Example `invalidRequestBody` (Bad Request.):

```json
{
  "code": "EIBACC0106",
  "message": "The product ID provided is already attached"
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

500 Example `penaltyOverrideScheduleError` (Failed to schedule override expiration):

```json
{
  "code": "EIBACC0304",
  "message": "Failed to schedule override expiration"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBACC0008` | Bad Request |
| 400 | `EIBACC0317` | deposit_configs.overrides.penalties is not supported at program-level; apply per-account instead |
| 400 | `EIBACC0318` | deposit_configs.overrides.maturity_instructions is not supported at program-level; apply per-account instead |
| 400 | `EIBACC0308` | valid_until must be a future datetime |
| 400 | `EIBACC0309` | Validation error |
| 400 | `EIBACC0310` | Validation error |
| 400 | `EIBACC0311` | Validation error |
| 400 | `EIBACC0312` | Validation error |
| 400 | `EIBACC0379` | interest_capitalization_mode PAYOUT requires a fully resolved payout_account |
| 404 | `EIBACC0064` | Product not found |
| 409 | `EIBACC0106` | The product ID provided is already attached |
| 500 | `EIBACC0007` | Internal error |
| 500 | `EIBACC0304` | Failed to schedule override expiration |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `deposit-product-program-attach-1` | https://developers.pismo.io/events/docs/deposit-product-program-attach-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-interest-management-data-events`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=PATCH path=/v1/deposits/programs/{programId}/attachment operationId=interest-bearing-v1-deposit-update-program-attachment -->
### `PATCH /v1/deposits/programs/{programId}/attachment` — Update deposit program attachment overrides

- **operationId:** `interest-bearing-v1-deposit-update-program-attachment`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Program attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Partially updates `deposit_configs.overrides` and `deposit_configs.interest_capitalization_mode` on an active deposit program attachment. Each field follows three‑state `PATCH` rules, allowing values to be set, changed, or cleared. At the program level, the only supported override inside `overrides` is `renewal_term`.
>   * **Omitted**: Keeps the current value
>   * `null`: Removes the override; falls back through the cascade (product)
>   * **Value**: Replaces the current value
>
> **NOTES**:
> * At least one of `deposit_configs.overrides` or `deposit_configs.interest_capitalization_mode` must be provided.
> * Sending `penalties` inside `overrides` returns `400 EIBACC0317`
> * Sending `maturity_instructions` inside `overrides` results in a `400 EIBACC0318` error. This field cannot be modified at the program level and must be configured on each account attachment instead.
> * An empty `overrides` envelope returns `400 EIBACC0315`
> * `renewal_term` still requires `ROLLOVER` configured in `maturity_instructions` somewhere in the fallback sequence (`400 EIBACC0310` otherwise)
>
> This endpoint generates a [Program attachment updated](https://developers.pismo.io/events/docs/deposit-product-program-attachment-updated-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 123 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `UpdateProgramAttachmentRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `deposit_configs` | object | yes | At least one of `overrides` or `interest_capitalization_mode` must be provided.<br> |  |
| `deposit_configs.interest_capitalization_mode` | string \\\| null | no | Updates the program-level default capitalization mode. Inherited by all accounts attached to this program unless overridden at account level.<br><br>Send `null` to remove the program-level value and revert to the product default.<br> | enum: ["PAYOUT", "REINVEST", null]; example: "PAYOUT" |
| `deposit_configs.overrides` | object (schema `ProgramAttachmentOverridesPatchRequest`) | no | PATCH envelope for program-level `deposit_configs.overrides`.<br><br>**NOTES**:<br>  * Only `renewal_term` is valid and uses three-state semantics: omit for no change, `null` to clear the override, or supply a value to replace it<br>  * `penalties` and `maturity_instructions` are not allowed and produce `400 EIBACC0317` and `EIBACC0318`<br>  * An empty `overrides` object is rejected with `400 EIBACC0315`<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ProgramAttachment`) |
| 400 | Bad Request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_type` | string | no | Product type. | enum: ["deposit", "savings-account"] |
| `product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `attachment_date` | string | no | Timestamp that indicates when the attachment was created (when the attach API call was made).<br>The datetime format follows the ISO 8601 standard `yyyy-mm-ddThh:mm:ss.sssZ`.<br> | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `effective_date` | string | no | The effective date of the attachment in `YYYY-MM-DD` format<br>This is the date when the attachment becomes valid. Maturity is calculated from this date.<br>For attachments created in the past, the date defaults to the value of `attachment_date`.<br> | format: "date"; example: "2025-12-01" |
| `fee_model_id` | string | no | Fee model identifier, if applicable. | example: "fee-model-123" |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `interest_capitalization_mode` | string | no | Present only when this program attachment explicitly defines `interest_capitalization_mode`. If the field is missing, the Pismo platform applies `REINVEST` as the default behavior. All accounts linked to the program inherit this value unless an account‑level configuration provides its own setting.<br> | enum: ["PAYOUT", "REINVEST"]; example: "REINVEST" |
| `overrides` | object | no | Optional. Only returned when at least one override is configured for the attachment. |  |
| `overrides.maturity_instructions` | object (schema `MaturityInstructionsOverrideRequest`) | no | Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.<br> |  |
| `overrides.renewal_term` | object (schema `RenewalTermResponse`) | no | Renewal term applied on each rollover. Always returns all three fields together — `unit`, `value` and `renewal_calendar_maturity_date` — regardless of the form the client used to configure it, mirroring `maturity_period`. Legacy terms persisted before the calendar date was stored return only `unit`+`value`.<br> |  |
| `overrides.penalties` | object (schema `PenaltiesOverrideSnapshot`) | no | Persisted penalty overrides for each type. Types appear only when set. Each entry includes `waived`, the relevant type-specific fields, and an optional `valid_until` for scheduling the revert.<br> |  |
| `accrual_model` | string | no | Accrual model inherited from the attached product. `DEPOSIT_BASIS` or `BALANCE_BASIS`. | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; default: "DEPOSIT_BASIS"; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Balance type inherited from the attached product. Only meaningful when `accrual_model` is `BALANCE_BASIS`. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |

##### Response 400

400 Example `emptyOverridesEnvelope` (deposit_configs.overrides must contain at least one field):

```json
{
  "code": "EIBACC0315",
  "message": "deposit_configs.overrides must contain at least one field"
}
```

400 Example `programLevelPenaltiesNotSupported` (penalties not supported at program-level):

```json
{
  "code": "EIBACC0317",
  "message": "deposit_configs.overrides.penalties is not supported at program-level; apply per-account instead"
}
```

400 Example `programLevelMaturityInstructionsNotSupported` (maturity_instructions not supported at program-level):

```json
{
  "code": "EIBACC0318",
  "message": "deposit_configs.overrides.maturity_instructions is not supported at program-level; apply per-account instead"
}
```

400 Example `renewalTermRequiresRollover` (renewal_term requires ROLLOVER in maturity_instructions):

```json
{
  "code": "EIBACC0310",
  "message": "Validation error",
  "details": "renewal_term requires ROLLOVER configured in maturity_instructions.principal or maturity_instructions.interest (account/program override or product default)."
}
```

##### Response 404

404 Example `attachmentNotFound` (Active deposit attachment not found for this program):

```json
{
  "code": "EIBACC0113",
  "message": "Product attachment not found"
}
```

##### Response 409

409 Example `attachmentNotActive` (Attachment is not active):

```json
{
  "code": "EIBACC0301",
  "message": "Product attachment is not active"
}
```

409 Example `optimisticLock` (Product attachment was modified concurrently):

```json
{
  "code": "EIBACC0314",
  "message": "Product attachment was modified concurrently; retry with the latest state"
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

500 Example `attachmentOverridesUpdate` (Failed to update attachment overrides):

```json
{
  "code": "EIBACC0316",
  "message": "Failed to update attachment overrides"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EIBACC0315` | deposit_configs.overrides must contain at least one field |
| 400 | `EIBACC0317` | deposit_configs.overrides.penalties is not supported at program-level; apply per-account instead |
| 400 | `EIBACC0318` | deposit_configs.overrides.maturity_instructions is not supported at program-level; apply per-account instead |
| 400 | `EIBACC0310` | Validation error |
| 404 | `EIBACC0113` | Product attachment not found |
| 409 | `EIBACC0301` | Product attachment is not active |
| 409 | `EIBACC0314` | Product attachment was modified concurrently; retry with the latest state |
| 500 | `EIBACC0007` | Internal error |
| 500 | `EIBACC0316` | Failed to update attachment overrides |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `deposit-product-program-attachment-updated-1` | https://developers.pismo.io/events/docs/deposit-product-program-attachment-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/savings-accounts/programs/{programId}/attach operationId=interest-bearing-v1-savings-account-attach-program -->
### `POST /v1/savings-accounts/programs/{programId}/attach` — Attach savings accounts to program

- **operationId:** `interest-bearing-v1-savings-account-attach-program`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Program attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Attach a savings accounts product to a program.
> This endpoint generates the [Program attached](https://developers.pismo.io/events/docs/deposit-product-program-attach-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | Program ID | example: 123 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `SavingsAccountAttachRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | yes | Product ID | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that offer additional context or custom information.<br><br>The platform has no control over its content, it's controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Success - No Content |  |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
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
| `deposit-product-program-attach-1` | https://developers.pismo.io/events/docs/deposit-product-program-attach-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-interest-management-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/MaturityPeriod -->
### Schema `MaturityPeriod`

Pointer: `#/components/schemas/MaturityPeriod`. Type: object (schema `MaturityPeriod`).

> Defines when the deposit matures. There are three usage modes:
>
> * **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).
> * **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).
> * **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.
>
> **NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.
>
> In the **attach** endpoints, the response returns exactly what was sent in the request:
> * Send `unit` + `value` returns `unit` + `value`
> * Send `calendar_maturity_date` returns `calendar_maturity_date`
> * Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`
>
> **NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `unit` | string (schema `MaturityPeriodUnit`) | no | Time unit for the relative maturity period. It's used together with `value` and cannot coincide with `calendar_maturity_date`.<br><br>- `DAYS`: Uses `value` directly. Example: `value=90` → 90 days.<br>- `WEEKS`: Multiplies `value` by 7. Example: `value=4` → 28 days.<br>- `MONTHS`: Calculates calendar-month with end-of-month (EOM) clamping when the target day does not exist. Example: `2024-01-31` + 1 month = `2024-02-29` (leap year) or `2025-02-28` (non-leap year).<br>- `YEARS`: Calculates calendar-year, for example: `2024-02-29` + 1 year = `2025-02-28`. Note that there is no Feb 29 in 2025.<br><br>For `WEEKS`, `MONTHS`, and `YEARS`, the resulting calendar date is converted back to a day count to validate against the product's configured minimum or maximum term.<br> | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `value` | integer (schema `MaturityPeriodValue`) | no | Number of time units until maturity. Must be greater than `0`. Mutually exclusive with `calendar_maturity_date`.<br> | minimum: 1; example: 6 |
| `calendar_maturity_date` | string (schema `CalendarMaturityDate`) | no | Maturity date. Format is `YYYY-MM-DD`. The date must be a future date.<br><br>This date cannot coincide with `unit`/`value`, sending both in the same request returns a `400` validation error.<br> | format: "date"; example: "2027-06-15" |

<!-- schema: #/components/schemas/PayoutAccount -->
### Schema `PayoutAccount`

Pointer: `#/components/schemas/PayoutAccount`. Type: object (schema `PayoutAccount`).

> The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br>
>
> * **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.
> * **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.
>
> Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `label` | string | no | Label to identify the account<br> | example: "My payout account" |
| `type` | string | no | Payout account type, either `INTERNAL` or `EXTERNAL`<br> | enum: ["INTERNAL", "EXTERNAL"]; example: "INTERNAL" |
| `internal_account_id` | number | no | Internal account ID for the account that receives the payments.<br>Required for type `INTERNAL` and not allowed for `EXTERNAL`.<br> | example: 123456 |
| `external_account` | object | no | Contains user-defined key-value pairs that identify the external account receiving the payments.<br>Note that external account information is client-provided.<br><br>Required for type `EXTERNAL` and not allowed for `INTERNAL`.<br> | example: {"key": "value"} |

<!-- schema: #/components/schemas/MaturityInstructionsOverrideRequest -->
### Schema `MaturityInstructionsOverrideRequest`

Pointer: `#/components/schemas/MaturityInstructionsOverrideRequest`. Type: object (schema `MaturityInstructionsOverrideRequest`).

> Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `principal` | string | no | Specifies how the principal is handled once the deposit matures. | enum: ["ROLLOVER", "PAY"]; example: "ROLLOVER" |
| `interest` | string | no | Specifies how the interest is handled once the deposit matures. | enum: ["ROLLOVER", "PAY"]; example: "PAY" |
| `reason` | string | no | Optional audit-trail reason. | maxLength: 100; example: "Customer preference at onboarding" |

<!-- schema: #/components/schemas/RenewalTermResponse -->
### Schema `RenewalTermResponse`

Pointer: `#/components/schemas/RenewalTermResponse`. Type: object (schema `RenewalTermResponse`).

> Renewal term applied on each rollover. Always returns all three fields together — `unit`, `value` and `renewal_calendar_maturity_date` — regardless of the form the client used to configure it, mirroring `maturity_period`. Legacy terms persisted before the calendar date was stored return only `unit`+`value`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `unit` | string | no |  | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `value` | integer | no |  | minimum: 1; example: 6 |
| `renewal_calendar_maturity_date` | string | no | Returned only when the request uses the calendar format. Format = `YYYY-MM-DD`. | format: "date"; example: "2027-05-22" |

<!-- schema: #/components/schemas/PenaltiesOverrideSnapshot -->
### Schema `PenaltiesOverrideSnapshot`

Pointer: `#/components/schemas/PenaltiesOverrideSnapshot`. Type: object (schema `PenaltiesOverrideSnapshot`).

> Persisted penalty overrides for each type. Types appear only when set. Each entry includes `waived`, the relevant type-specific fields, and an optional `valid_until` for scheduling the revert.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason` | string | no |  | example: "Q4 2026 VIP retention package" |
| `grace_period` | object (schema `GracePeriodOverrideRequest`) | no | Grace period override. Type-specific fields are optional pointers, when omitted, the Pismo platform follows the normal fallback sequence, moving from the account level to the program and then to the product defaults. |  |
| `early_withdrawal_after_opening` | object (schema `EarlyWithdrawalAfterOpeningOverrideRequest`) | no | Override for early withdrawal after account opening. |  |
| `withdrawal_fee` | object (schema `WithdrawalFeeOverrideRequest`) | no | Withdrawal fee override. |  |
| `tiered_interest_forfeiture` | object (schema `TieredInterestForfeitureOverrideRequest`) | no | Tiered interest forfeiture override. Tiers replace the product's tiers when provided. |  |
| `subsequent_withdrawals` | object (schema `SubsequentWithdrawalsOverrideRequest`) | no | Subsequent withdrawals (Regulation D) override. |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no | Error type code | example: "EIBACC0003" |
| `details` | string | no | Error details | example: "error EIBACC0008: Validation error [(Field 'Order' is invalid)]" |
| `message` | string | no | Error message | example: "Bad Request" |

<!-- schema: #/components/schemas/ProgramDepositConfigs -->
### Schema `ProgramDepositConfigs`

Pointer: `#/components/schemas/ProgramDepositConfigs`. Type: object (schema `ProgramDepositConfigs`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `interest_capitalization_mode` | string | no | Program‑level setting that defines how capitalized interest should be treated.<br><br><br>* `REINVEST` (default): The Pismo platform adds the capitalized amount to the principal.<br>* `PAYOUT`: The capitalized amount is routed to the `payout_account` configured at account level.<br><br>Both values are allowed at the program level without `payout_account` validation. The `payout_account` binding (`EIBACC0379`) applies only at the account level because `payout_account` is not part of the program attachment. All accounts under the program follow this behavior unless an account‑level configuration replaces it.<br><br>If the field is not provided, it is omitted from the attachment and the Pismo platform applies `REINVEST` at runtime.<br> | enum: ["REINVEST", "PAYOUT"]; default: "REINVEST"; example: "REINVEST" |
| `overrides` | object (schema `ProgramAttachmentOverridesRequest`) | no | Defines the per‑attachment overrides permitted at program scope. Only `renewal_term` is valid. `penalties` and `maturity_instructions` result in `400` responses (`EIBACC0317` and `EIBACC0318`) and must be provided at the account level.<br> |  |

<!-- schema: #/components/schemas/AttachmentOverridesSnapshot -->
### Schema `AttachmentOverridesSnapshot`

Pointer: `#/components/schemas/AttachmentOverridesSnapshot`. Type: object (schema `AttachmentOverridesSnapshot`).

> Representation of the persisted overrides, present only when the request defined at least one override. Sub-fields are included only when set. The `renewal_term` always returns all three fields together (`unit`, `value` and `renewal_calendar_maturity_date`), mirroring the behavior of `maturity_period`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maturity_instructions` | object (schema `MaturityInstructionsOverrideRequest`) | no | Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.<br> |  |
| `renewal_term` | object (schema `RenewalTermResponse`) | no | Renewal term applied on each rollover. Always returns all three fields together — `unit`, `value` and `renewal_calendar_maturity_date` — regardless of the form the client used to configure it, mirroring `maturity_period`. Legacy terms persisted before the calendar date was stored return only `unit`+`value`.<br> |  |
| `penalties` | object (schema `PenaltiesOverrideSnapshot`) | no | Persisted penalty overrides for each type. Types appear only when set. Each entry includes `waived`, the relevant type-specific fields, and an optional `valid_until` for scheduling the revert.<br> |  |

<!-- schema: #/components/schemas/ProgramAttachmentOverridesPatchRequest -->
### Schema `ProgramAttachmentOverridesPatchRequest`

Pointer: `#/components/schemas/ProgramAttachmentOverridesPatchRequest`. Type: object (schema `ProgramAttachmentOverridesPatchRequest`).

> PATCH envelope for program-level `deposit_configs.overrides`.<br>
> **NOTES**:
>   * Only `renewal_term` is valid and uses three-state semantics: omit for no change, `null` to clear the override, or supply a value to replace it
>   * `penalties` and `maturity_instructions` are not allowed and produce `400 EIBACC0317` and `EIBACC0318`
>   * An empty `overrides` object is rejected with `400 EIBACC0315`

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `renewal_term` | object | no |  |  |
| `renewal_term.unit` | string | no | Time unit of the renewal term. Required together with `value` when calendar form is not used. | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `renewal_term.value` | integer | no | Number of units. Required together with `unit` when calendar form is not used. | minimum: 1; example: 6 |
| `renewal_term.renewal_calendar_maturity_date` | string | no | Explicit calendar date (`YYYY-MM-DD`), the date must be a future date, and does not coincide with `unit`+`value`. | format: "date"; example: "2027-05-22" |

<!-- schema: #/components/schemas/GracePeriodOverrideRequest -->
### Schema `GracePeriodOverrideRequest`

Pointer: `#/components/schemas/GracePeriodOverrideRequest`. Type: object (schema `GracePeriodOverrideRequest`).

> Grace period override. Type-specific fields are optional pointers, when omitted, the Pismo platform follows the normal fallback sequence, moving from the account level to the program and then to the product defaults.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes | `true` = fully exempt; `false` = penalty active (customize via the fields below). |  |
| `duration_days` | integer | no |  | minimum: 0 |
| `penalty_interest_days` | integer | no |  | minimum: 0 |
| `valid_until` | string | no | Schedules the revert of this override via EventBridge. This value must be a future date and follows the ISO 8601 standard. | format: "date-time" |

<!-- schema: #/components/schemas/EarlyWithdrawalAfterOpeningOverrideRequest -->
### Schema `EarlyWithdrawalAfterOpeningOverrideRequest`

Pointer: `#/components/schemas/EarlyWithdrawalAfterOpeningOverrideRequest`. Type: object (schema `EarlyWithdrawalAfterOpeningOverrideRequest`).

> Override for early withdrawal after account opening.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes |  |  |
| `applicable_within_days` | integer | no |  | minimum: 0 |
| `penalty_interest_days` | integer | no |  | minimum: 0 |
| `valid_until` | string | no |  | format: "date-time" |

<!-- schema: #/components/schemas/WithdrawalFeeOverrideRequest -->
### Schema `WithdrawalFeeOverrideRequest`

Pointer: `#/components/schemas/WithdrawalFeeOverrideRequest`. Type: object (schema `WithdrawalFeeOverrideRequest`).

> Withdrawal fee override.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes |  |  |
| `type` | string | no |  | enum: ["PERCENTAGE", "FIXED"] |
| `value` | number | no |  | exclusiveMinimum: 0 |
| `valid_until` | string | no |  | format: "date-time" |

<!-- schema: #/components/schemas/TieredInterestForfeitureOverrideRequest -->
### Schema `TieredInterestForfeitureOverrideRequest`

Pointer: `#/components/schemas/TieredInterestForfeitureOverrideRequest`. Type: object (schema `TieredInterestForfeitureOverrideRequest`).

> Tiered interest forfeiture override. Tiers replace the product's tiers when provided.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes |  |  |
| `tiers` | array of object (schema `TieredInterestForfeitureTierRequest`) | no |  |  |
| `valid_until` | string | no |  | format: "date-time" |

<!-- schema: #/components/schemas/SubsequentWithdrawalsOverrideRequest -->
### Schema `SubsequentWithdrawalsOverrideRequest`

Pointer: `#/components/schemas/SubsequentWithdrawalsOverrideRequest`. Type: object (schema `SubsequentWithdrawalsOverrideRequest`).

> Subsequent withdrawals (Regulation D) override.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `waived` | boolean | yes |  |  |
| `applicable_within_days` | integer | no |  | minimum: 1 |
| `penalty_interest_days` | integer | no |  | minimum: 1 |
| `window_behavior` | string | no |  | enum: ["ROLLING", "FIXED"] |
| `valid_until` | string | no |  | format: "date-time" |

<!-- schema: #/components/schemas/ProgramAttachmentOverridesRequest -->
### Schema `ProgramAttachmentOverridesRequest`

Pointer: `#/components/schemas/ProgramAttachmentOverridesRequest`. Type: object (schema `ProgramAttachmentOverridesRequest`).

> Defines the per‑attachment overrides permitted at program scope. Only `renewal_term` is valid. `penalties` and `maturity_instructions` result in `400` responses (`EIBACC0317` and `EIBACC0318`) and must be provided at the account level.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `renewal_term` | object (schema `RenewalTermOverrideRequest`) | no | Specifies the recurring rollover term, not to be confused with the initial `maturity_period`.<br><br>You must provide either `unit` with `value` or `renewal_calendar_maturity_date`.<br><br>A `ROLLOVER` configuration in principal or interest is required.<br><br>When you pass `renewal_calendar_maturity_date`, the Pismo platform converts the interval from today into a day count and stores it at attach time in normalized form: `{unit: DAYS, value: <calculated>}`.<br> |  |

<!-- schema: #/components/schemas/TieredInterestForfeitureTierRequest -->
### Schema `TieredInterestForfeitureTierRequest`

Pointer: `#/components/schemas/TieredInterestForfeitureTierRequest`. Type: object (schema `TieredInterestForfeitureTierRequest`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `min_days_held` | integer | yes |  | minimum: 0 |
| `max_days_held` | integer | no | Optional. Open-ended tier when omitted. | minimum: 0 |
| `forfeited_interest_days` | integer | yes |  | minimum: 0 |

<!-- schema: #/components/schemas/RenewalTermOverrideRequest -->
### Schema `RenewalTermOverrideRequest`

Pointer: `#/components/schemas/RenewalTermOverrideRequest`. Type: object (schema `RenewalTermOverrideRequest`).

> Specifies the recurring rollover term, not to be confused with the initial `maturity_period`.
>
> You must provide either `unit` with `value` or `renewal_calendar_maturity_date`.
>
> A `ROLLOVER` configuration in principal or interest is required.
>
> When you pass `renewal_calendar_maturity_date`, the Pismo platform converts the interval from today into a day count and stores it at attach time in normalized form: `{unit: DAYS, value: <calculated>}`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `unit` | string | no | Time unit of the renewal term. Required together with `value` when calendar form is not used. | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `value` | integer | no | Number of units. Required together with `unit` when calendar form is not used. | minimum: 1; example: 6 |
| `renewal_calendar_maturity_date` | string | no | Explicit calendar date (`YYYY-MM-DD`), the date must be a future date, and does not coincide with `unit`+`value`. | format: "date"; example: "2027-05-22" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Interest-bearing_accounts.yaml` | tag `Program attachment`: GET /v1/products/attachments/programs/{programId}, POST /v1/deposits/programs/{programId}/attach, PATCH /v1/deposits/programs/{programId}/attachment, POST /v1/savings-accounts/programs/{programId}/attach | https://github.com/PismoDevEx/pismo-api-specs | `89fc3f8ed0222a57…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-ERR-codes-eibacc` — Error codes: EIBACC
- `KU-EVT-catalogue-deposit` — Event catalogue: deposit
- `KU-EVT-interest-management-data-events` — Banking - Interest management
