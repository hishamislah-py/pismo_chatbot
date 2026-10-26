---
ku_id: KU-API-banking-interest-bearing-accounts--account-attachment
title: 'API reference: Banking - Interest-bearing accounts — Account attachment'
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
- interest-bearing-v1-get-account-attachment
- interest-bearing-v1-deposit-attach-account
- interest-bearing-v1-deposit-detach-account
- interest-bearing-v1-deposit-update-payout-account
- interest-bearing-v1-savings-account-attach-account
- interest-bearing-v1-savings-account-detach-account
- interest-bearing-v1-savings-account-update-payout-account
- interest-bearing-v1-deposit-update-account-attachment
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-BANK-interest-bearing-accounts
- KU-CC-deposit-products
- KU-ERR-codes-eibacc
- KU-EVT-catalogue-deposit
- KU-EVT-interest-management-data-events
specification_version: 1.0.0
---

# API reference: Banking - Interest-bearing accounts — Account attachment

**KU ID:** `KU-API-banking-interest-bearing-accounts--account-attachment` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 8 operation(s) tagged `Account attachment` in `api-specs/Banking_-_Interest-bearing_accounts.yaml` (“Banking - Interest-bearing accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints that manage account attachments to interest-bearing account products

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/products/attachments/accounts/{accountId}` | `interest-bearing-v1-get-account-attachment` | Get account attachment | no |
| `POST /v1/deposits/accounts/{accountId}/attach` | `interest-bearing-v1-deposit-attach-account` | Attach deposit to account | no |
| `POST /v1/deposits/accounts/{accountId}/detach` | `interest-bearing-v1-deposit-detach-account` | Detach deposit from account | no |
| `PATCH /v1/deposits/accounts/{accountId}` | `interest-bearing-v1-deposit-update-payout-account` | Update payout account for deposit account | no |
| `POST /v1/savings-accounts/accounts/{accountId}/attach` | `interest-bearing-v1-savings-account-attach-account` | Attach savings account to account | no |
| `POST /v1/savings-accounts/accounts/{accountId}/detach` | `interest-bearing-v1-savings-account-detach-account` | Detach savings account from account | no |
| `PATCH /v1/savings-accounts/accounts/{accountId}` | `interest-bearing-v1-savings-account-update-payout-account` | Update payout account for savings account | no |
| `PATCH /v1/deposits/accounts/{accountId}/attachment` | `interest-bearing-v1-deposit-update-account-attachment` | Update deposit account attachment overrides | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=GET path=/v1/products/attachments/accounts/{accountId} operationId=interest-bearing-v1-get-account-attachment -->
### `GET /v1/products/attachments/accounts/{accountId}` — Get account attachment

- **operationId:** `interest-bearing-v1-get-account-attachment`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Account attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get an account's attached product
>
> `accountId` accepts either the Pismo `account_id` or your `external_account_id`.
>
> Which ID you can use is determined by the access token, so send the same ID the token was generated with. To address the account by `external_account_id`, the token must be created with that external account ID; a token generated with a Pismo account ID accepts only the numeric `account_id`. Sending an ID that doesn’t match the token returns `403`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `Authorization` | header | yes | string | Account token. Token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a 401 Unauthorized error.<br> | example: "1234" |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Success | `application/json`: object (schema `AccountAttachment`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_type` | string | no | Product type. | enum: ["deposit", "savings-account"] |
| `product_id` | string | no | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `external_account_id` | string (schema `ExternalAccountId`) | no | External account ID. Returned only when the account has an external account identifier. | example: "ext-acct-001" |
| `interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `attachment_date` | string | no | Timestamp that indicates when the attachment was created (when the attach API call was made).<br>The datetime format follows the ISO 8601 standard `yyyy-mm-ddThh:mm:ss.sssZ`.<br> | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `effective_date` | string | no | The effective date of the attachment in `YYYY-MM-DD` format<br>This is the date when the attachment becomes valid. Maturity is calculated from this date.<br>For attachments created in the past, the date defaults to the value of `attachment_date`.<br> | format: "date"; example: "2025-12-01" |
| `fee_model_id` | string | no | Fee model identifier, if applicable. | example: "fee-model-123" |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `interest_capitalization_mode` | string | no | Present only when this account attachment explicitly defines `interest_capitalization_mode`. If the field is missing, the effective value is `REINVEST`, inherited from the program configuration or, if the program does not specify it, from the product’s default settings.<br> | enum: ["PAYOUT", "REINVEST"]; example: "REINVEST" |
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

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/deposits/accounts/{accountId}/attach operationId=interest-bearing-v1-deposit-attach-account -->
### `POST /v1/deposits/accounts/{accountId}/attach` — Attach deposit to account

- **operationId:** `interest-bearing-v1-deposit-attach-account`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Account attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Attach a time deposit product to an account.
> This endpoint generates the [Account attached](https://developers.pismo.io/events/docs/deposit-product-account-attach-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `DepositAttachRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | yes | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `effective_date` | string | no | Backdated effective date for the attachment in `YYYY-MM-DD` format. This is the date starting from which the attachment is considered valid.<br>- If omitted, it defaults to the current date<br>- Must be less than or equal to the current date (cannot be in the future)<br>- Cannot be more than `ATTACHMENT_MAX_BACKDATING_DAYS` (default: 90 days) in the past<br>- Maturity date is calculated from this date, not from the date when you call the API.<br>- No retroactive interest accrual, capitalization, or postings are triggered<br> | format: "date"; example: "2025-12-01" |
| `deposit_configs` | object (schema `DepositConfigs`) | no |  |  |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that provide additional context or custom information.<br><br>The platform has no control over its content, but rather controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `DepositAttachAccountResponse`) |
| 400 | Bad Request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | no | Account ID | example: 123456 |
| `product_id` | string | no | Product ID | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `external_account_id` | string (schema `ExternalAccountId`) | no | External account ID. Returned only when the account has an external account identifier. | example: "ext-acct-001" |
| `effective_date` | string | no | The effective value date of the attachment. Format is `YYYY-MM-DD`.<br>This is the date when the attachment becomes valid. Maturity is calculated from this date.<br> | format: "date"; example: "2025-12-01" |
| `deposit_configs` | object | no |  |  |
| `deposit_configs.maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `deposit_configs.interest_capitalization_mode` | string | no | Present only when the request included `interest_capitalization_mode`. Reflects the value stored on the attachment.<br> | enum: ["PAYOUT", "REINVEST"]; example: "REINVEST" |
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

400 Example `capitalizationPayoutRequiresPayoutAccount` (interest_capitalization_mode PAYOUT requires a payout_account):

```json
{
  "code": "EIBACC0379",
  "message": "interest_capitalization_mode PAYOUT requires a fully resolved payout_account",
  "details": "payout_account is required when interest_capitalization_mode is PAYOUT."
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
| 400 | `EIBACC0308` | valid_until must be a future datetime |
| 400 | `EIBACC0309` | Validation error |
| 400 | `EIBACC0310` | Validation error |
| 400 | `EIBACC0311` | Validation error |
| 400 | `EIBACC0312` | Validation error |
| 400 | `EIBACC0379` | interest_capitalization_mode PAYOUT requires a fully resolved payout_account |
| 404 | `EIBACC0064` | Product not found |
| 409 | `EIBACC0114` | Product is already detached |
| 500 | `EIBACC0007` | Internal error |
| 500 | `EIBACC0304` | Failed to schedule override expiration |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `deposit-product-account-attach-1` | https://developers.pismo.io/events/docs/deposit-product-account-attach-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-interest-bearing-accounts`, `KU-CC-deposit-products`, `KU-EVT-interest-management-data-events`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/deposits/accounts/{accountId}/detach operationId=interest-bearing-v1-deposit-detach-account -->
### `POST /v1/deposits/accounts/{accountId}/detach` — Detach deposit from account

- **operationId:** `interest-bearing-v1-deposit-detach-account`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Account attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Detach a time deposit product from an account.
> This endpoint generates the [Account detached](https://developers.pismo.io/events/docs/deposit-product-account-detach-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `DetachRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | yes | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that offer additional context or custom information.<br><br>The platform has no control over its content, but rather controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Success - No Content |  |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict. | `application/json`: oneOf: object (schema `ErrorResponse`) |
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

409 Example `invalidRequestBody` (Bad Request.):

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
| `deposit-product-account-detach-1` | https://developers.pismo.io/events/docs/deposit-product-account-detach-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-interest-management-data-events`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=PATCH path=/v1/deposits/accounts/{accountId} operationId=interest-bearing-v1-deposit-update-payout-account -->
### `PATCH /v1/deposits/accounts/{accountId}` — Update payout account for deposit account

- **operationId:** `interest-bearing-v1-deposit-update-payout-account`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Account attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the payout account configuration for an attached deposit account.
> The payout account specifies where interest payments and maturity proceeds are sent.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `UpdatePayoutAccountRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payout_account` | object (schema `PayoutAccount`) | yes | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Payout account updated successfully | `application/json`: object (schema `UpdatePayoutAccountResponse`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 403 | Forbidden |  |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `updated_at` | string | no | The date and time when the payout account was updated | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `external_account_id` | string (schema `ExternalAccountId`) | no | External account ID. Returned only when the account has an external account identifier. | example: "ext-acct-001" |

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

##### Response 422

422 Example `invalidInternalAccount` (Internal account validation failed):

```json
{
  "code": "EIBACC0302",
  "message": "Internal payout account validation failed. Account does not exist"
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
| 422 | `EIBACC0302` | Internal payout account validation failed. Account does not exist |
| 500 | `EIBACC0007` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-interest-bearing-accounts`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/savings-accounts/accounts/{accountId}/attach operationId=interest-bearing-v1-savings-account-attach-account -->
### `POST /v1/savings-accounts/accounts/{accountId}/attach` — Attach savings account to account

- **operationId:** `interest-bearing-v1-savings-account-attach-account`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Account attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Attach a savings account product to an account.
> This endpoint generates the [Account attached](https://developers.pismo.io/events/docs/deposit-product-account-attach-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | example: 123456 |

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
| `deposit-product-account-attach-1` | https://developers.pismo.io/events/docs/deposit-product-account-attach-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;409;500`, has examples `False`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-BANK-interest-bearing-accounts`, `KU-EVT-interest-management-data-events`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=POST path=/v1/savings-accounts/accounts/{accountId}/detach operationId=interest-bearing-v1-savings-account-detach-account -->
### `POST /v1/savings-accounts/accounts/{accountId}/detach` — Detach savings account from account

- **operationId:** `interest-bearing-v1-savings-account-detach-account`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Account attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Detach a savings account product from an account.
> This endpoint generates the [Account detached](https://developers.pismo.io/events/docs/deposit-product-account-detach-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | example: 123456 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `DetachRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `product_id` | string | yes | Product identifier. | example: "2c336e9d-d04f-4fd0-8f6e-25808f48d70c" |
| `metadata` | object | no | The metadata object contains user-defined key-value pairs that offer additional context or custom information.<br><br>The platform has no control over its content, but rather controlled by the user.<br><br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"key": "value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Success - No Content |  |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict. | `application/json`: oneOf: object (schema `ErrorResponse`) |
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

409 Example `invalidRequestBody` (Bad Request.):

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
| `deposit-product-account-detach-1` | https://developers.pismo.io/events/docs/deposit-product-account-detach-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-interest-management-data-events`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=PATCH path=/v1/savings-accounts/accounts/{accountId} operationId=interest-bearing-v1-savings-account-update-payout-account -->
### `PATCH /v1/savings-accounts/accounts/{accountId}` — Update payout account for savings account

- **operationId:** `interest-bearing-v1-savings-account-update-payout-account`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Account attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the payout account configuration for an attached savings account.
> The payout account specifies where interest payments are sent.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `UpdatePayoutAccountRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payout_account` | object (schema `PayoutAccount`) | yes | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Payout account updated successfully | `application/json`: object (schema `UpdatePayoutAccountResponse`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 403 | Forbidden |  |
| 404 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 422 | Unprocessable Entity | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `updated_at` | string | no | The date and time when the payout account was updated | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `external_account_id` | string (schema `ExternalAccountId`) | no | External account ID. Returned only when the account has an external account identifier. | example: "ext-acct-001" |

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

##### Response 422

422 Example `invalidInternalAccount` (Internal account validation failed):

```json
{
  "code": "EIBACC0302",
  "message": "Internal payout account validation failed. Account does not exist"
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
| 422 | `EIBACC0302` | Internal payout account validation failed. Account does not exist |
| 500 | `EIBACC0007` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;409;422;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-interest-bearing-accounts`.

<!-- op: spec=api-specs/Banking_-_Interest-bearing_accounts.yaml method=PATCH path=/v1/deposits/accounts/{accountId}/attachment operationId=interest-bearing-v1-deposit-update-account-attachment -->
### `PATCH /v1/deposits/accounts/{accountId}/attachment` — Update deposit account attachment overrides

- **operationId:** `interest-bearing-v1-deposit-update-account-attachment`
- **Specification:** `api-specs/Banking_-_Interest-bearing_accounts.yaml` (Banking - Interest-bearing accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io/savings-products`
- **Tags:** `Account attachment`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Partially updates `deposit_configs.maturity_period`, `deposit_configs.overrides` and `deposit_configs.interest_capitalization_mode` on an active deposit account attachment. The `overrides` fields are processed using three‑state `PATCH` semantics, allowing values to be added, changed, or cleared as part of the update.
>   * **Omitted**: Keeps the current value
>   * `null`: Removes the override; falls back through the cascade (program → product)
>   * **Value**: Replaces the current override with the supplied value
>
> **NOTES**:
>
> * At least one of `deposit_configs.maturity_period`, `deposit_configs.overrides` or `deposit_configs.interest_capitalization_mode` must be provided. A payload carrying only `maturity_period` is valid.
> * The `overrides` envelope, if provided, must contain at least one field. Sending an empty object returns `400 EIBACC0315`.
> * `renewal_term` still requires `ROLLOVER` configured in `maturity_instructions` somewhere in the fallback sequence (`400 EIBACC0310` otherwise).
> * `maturity_period` changes the term **in force** and takes effect immediately, recalculating the current cycle's maturity date from the attachment's `effective_date`. It's accepted in both documented forms (`unit`+`value` or `calendar_maturity_date`) and doesn't follow the three-state semantics above: `null` is a no-op, not a removal.
> * `maturity_period` and `overrides.renewal_term` are independent. `renewal_term` keeps applying at rollover only and never recalculates the current cycle's maturity date.
> * When `maturity_period` changes, the schedules driven by the maturity date (maturity instruction, maturity notices) are re-evaluated against the new date.
> * `product_id` and `payout_account` stay fixed after attach and are ignored if included in the request body. To change the payout account, use [Update payout account for deposit account](ref:interest-bearing-v1-deposit-update-payout-account).
>
> This endpoint generates an [Account attachment updated](https://developers.pismo.io/events/docs/deposit-product-account-attachment-updated-1) event that includes the active term in `data.maturity_period`. If the account has an external account ID, the event also includes it in `data.external_account_id`.
>
> The response returns `external_account_id` whenever the account has one; it is omitted for an account with no external identifier.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | string | Account ID. Accepts either the Pismo `account_id` or your `external_account_id`. Send the same ID used to generate the access token.<br> | maxLength: 60; example: "123456" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `UpdateAccountAttachmentRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `deposit_configs` | object | yes | At least one of `maturity_period`, `overrides` or `interest_capitalization_mode` must be provided.<br> |  |
| `deposit_configs.maturity_period` | object | no | Defines the term currently in force and recalculates the cycle’s maturity date immediately. The update takes effect at once; it does not wait for the next cycle or rollover.<br><br>Accepts the same mutually exclusive forms as the attach endpoint:<br>  * **Relative period**: `unit` + `value` (for example, `MONTHS` + `18`)<br>  * **Explicit date**: `calendar_maturity_date` (for example, `2026‑12‑31`)<br><br>* **Anchor date**: the term is always recalculated from the attachment’s `effective_date`, exactly as at attach time. The `PATCH` execution date does not shift the cycle start date, it only updates the cycle end date. Because of this anchor, shortening a term on an attachment with an old `effective_date` can produce a maturity date that is already in the past, which is rejected.<br><br>* **Maturity‑date boundary**: the resolved maturity date must be today or later. Any value that resolves to a past date returns `400 EIBACC0306`, regardless of form.<br><br>* **Grace‑period behavior**: updates made during the grace‑period window apply immediately to the cycle that began on the first day of that window. They are never deferred to a later rollover.<br><br>* **`null` and omission**: `maturity_period` represents the term itself, not an override. `null`, an empty object, or omission all leave the persisted term unchanged. Only an explicit value recalculates the term, so an incomplete payload cannot revert the term to the product default.<br><br>* **Response shape**: the response returns the resolved term with unit, value, and `calendar_maturity_date` populated together. Requests sent in explicit‑date form are normalized to {`unit`: `DAYS`, `value`: `<days>`, `calendar_maturity_date`: `<date>`}.<br><br>Do not confuse this field with `overrides.renewal_term`. `renewal_term` applies only at rollover and never recalculates the current cycle’s maturity date. Both fields are independent and might appear in the same request.<br> |  |
| `deposit_configs.maturity_period.unit` | string (schema `MaturityPeriodUnit`) | no | Time unit for the relative maturity period. It's used together with `value` and cannot coincide with `calendar_maturity_date`.<br><br>- `DAYS`: Uses `value` directly. Example: `value=90` → 90 days.<br>- `WEEKS`: Multiplies `value` by 7. Example: `value=4` → 28 days.<br>- `MONTHS`: Calculates calendar-month with end-of-month (EOM) clamping when the target day does not exist. Example: `2024-01-31` + 1 month = `2024-02-29` (leap year) or `2025-02-28` (non-leap year).<br>- `YEARS`: Calculates calendar-year, for example: `2024-02-29` + 1 year = `2025-02-28`. Note that there is no Feb 29 in 2025.<br><br>For `WEEKS`, `MONTHS`, and `YEARS`, the resulting calendar date is converted back to a day count to validate against the product's configured minimum or maximum term.<br> | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `deposit_configs.maturity_period.value` | integer (schema `MaturityPeriodValue`) | no | Number of time units until maturity. Must be greater than `0`. Mutually exclusive with `calendar_maturity_date`.<br> | minimum: 1; example: 6 |
| `deposit_configs.maturity_period.calendar_maturity_date` | string (schema `CalendarMaturityDate`) | no | Maturity date. Format is `YYYY-MM-DD`. The date must be a future date.<br><br>This date cannot coincide with `unit`/`value`, sending both in the same request returns a `400` validation error.<br> | format: "date"; example: "2027-06-15" |
| `deposit_configs.interest_capitalization_mode` | string \\\| null | no | Updates how capitalized interest is treated on this attachment.<br><br><br>* `PAYOUT` (explicit): Switching to this mode requires the attachment to already have a valid `payout_account`. If none is configured, the request returns `400 EIBACC0379`—set the `payout_account` first via `PATCH /v1/deposits/accounts/{accountId}`, then switch to this mode.<br>* `REINVEST`: The Pismo platform adds the capitalized amount to the principal. No `payout_account` is required.<br>* `Omitted`: The current mode is left unchanged.<br>* `null`: Clears the account‑level value and restores the inherited behavior from the program and then the product default. When the value is missing at all levels, the Pismo platform applies `REINVEST`.<br><br>This field applies only to the capitalization flow. The maturity instruction flow always uses `payout_account` regardless of the setting.<br> | enum: ["PAYOUT", "REINVEST", null]; example: "REINVEST" |
| `deposit_configs.overrides` | object (schema `AttachmentOverridesPatchRequest`) | no | PATCH envelope for account‑level `deposit_configs.overrides`. Fields support three‑state semantics, omission preserves the current value, `null` removes the override and restores the inherited configuration, and a provided value replaces it. The envelope must define at least one field, an empty overrides object returns a `400` error: `EIBACC0315`.<br> |  |

Example `maturityPeriodRelativeForm` (maturity_period — relative period (unit + value)):

```json
{
  "deposit_configs": {
    "maturity_period": {
      "unit": "MONTHS",
      "value": 18
    }
  }
}
```

Example `maturityPeriodCalendarForm` (maturity_period — explicit date (calendar_maturity_date)):

```json
{
  "deposit_configs": {
    "maturity_period": {
      "calendar_maturity_date": "2026-12-31"
    }
  }
}
```

Example `maturityPeriodWithOverrides` (maturity_period together with overrides):

```json
{
  "deposit_configs": {
    "maturity_period": {
      "unit": "MONTHS",
      "value": 18
    },
    "interest_capitalization_mode": "REINVEST",
    "overrides": {
      "maturity_instructions": {
        "principal": "ROLLOVER",
        "interest": "PAY",
        "reason": "Customer opted-in via self-service"
      },
      "renewal_term": {
        "unit": "MONTHS",
        "value": 12
      }
    }
  }
}
```

Example `overridesOnly` (overrides only — term left untouched):

```json
{
  "deposit_configs": {
    "overrides": {
      "penalties": {
        "reason": "Q4 2026 regulatory adjustment",
        "grace_period": {
          "waived": true
        }
      }
    }
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountAttachment`) |
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
| `external_account_id` | string (schema `ExternalAccountId`) | no | External account ID. Returned only when the account has an external account identifier. | example: "ext-acct-001" |
| `interest_plan_id` | string | no | Interest rate plan ID. This corresponds to the ID you created using the [Create interest plan version](ref:patch-v1-interest-plan)) endpoint. | example: "263d509a-d5d0-4b3a-b909-ce1b9174beff" |
| `maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `attachment_date` | string | no | Timestamp that indicates when the attachment was created (when the attach API call was made).<br>The datetime format follows the ISO 8601 standard `yyyy-mm-ddThh:mm:ss.sssZ`.<br> | format: "date-time"; example: "2024-01-23T13:26:25.000Z" |
| `effective_date` | string | no | The effective date of the attachment in `YYYY-MM-DD` format<br>This is the date when the attachment becomes valid. Maturity is calculated from this date.<br>For attachments created in the past, the date defaults to the value of `attachment_date`.<br> | format: "date"; example: "2025-12-01" |
| `fee_model_id` | string | no | Fee model identifier, if applicable. | example: "fee-model-123" |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `interest_capitalization_mode` | string | no | Present only when this account attachment explicitly defines `interest_capitalization_mode`. If the field is missing, the effective value is `REINVEST`, inherited from the program configuration or, if the program does not specify it, from the product’s default settings.<br> | enum: ["PAYOUT", "REINVEST"]; example: "REINVEST" |
| `overrides` | object | no | Optional. Only returned when at least one override is configured for the attachment. |  |
| `overrides.maturity_instructions` | object (schema `MaturityInstructionsOverrideRequest`) | no | Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.<br> |  |
| `overrides.renewal_term` | object (schema `RenewalTermResponse`) | no | Renewal term applied on each rollover. Always returns all three fields together — `unit`, `value` and `renewal_calendar_maturity_date` — regardless of the form the client used to configure it, mirroring `maturity_period`. Legacy terms persisted before the calendar date was stored return only `unit`+`value`.<br> |  |
| `overrides.penalties` | object (schema `PenaltiesOverrideSnapshot`) | no | Persisted penalty overrides for each type. Types appear only when set. Each entry includes `waived`, the relevant type-specific fields, and an optional `valid_until` for scheduling the revert.<br> |  |
| `accrual_model` | string | no | Accrual model inherited from the attached product. `DEPOSIT_BASIS` or `BALANCE_BASIS`. | enum: ["DEPOSIT_BASIS", "BALANCE_BASIS"]; default: "DEPOSIT_BASIS"; example: "DEPOSIT_BASIS" |
| `balance_type` | string | no | Balance type inherited from the attached product. Only meaningful when `accrual_model` is `BALANCE_BASIS`. | enum: ["VALUE_DATED_BALANCE", "LEDGER_BALANCE"]; default: "VALUE_DATED_BALANCE"; example: "VALUE_DATED_BALANCE" |

200 Example `relativeForm` (Term updated with unit + value):

```json
{
  "product_type": "deposit",
  "product_id": "2c336e9d-d04f-4fd0-8f6e-25808f48d70c",
  "external_account_id": "ext-acct-001",
  "interest_plan_id": "a3c73958-e2bd-4b8b-ab72-1ae6c0b5aade",
  "maturity_period": {
    "unit": "MONTHS",
    "value": 18,
    "calendar_maturity_date": "2025-11-28"
  },
  "attachment_date": "2024-05-29T14:00:00Z",
  "effective_date": "2024-05-29",
  "interest_capitalization_mode": "REINVEST"
}
```

200 Example `calendarForm` (Term updated with calendar_maturity_date (normalized in the response)):

```json
{
  "product_type": "deposit",
  "product_id": "2c336e9d-d04f-4fd0-8f6e-25808f48d70c",
  "external_account_id": "ext-acct-001",
  "interest_plan_id": "a3c73958-e2bd-4b8b-ab72-1ae6c0b5aade",
  "maturity_period": {
    "unit": "DAYS",
    "value": 365,
    "calendar_maturity_date": "2026-12-31"
  },
  "attachment_date": "2026-01-01T14:00:00Z",
  "effective_date": "2026-01-01"
}
```

##### Response 400

400 Example `emptyOverridesEnvelope` (deposit_configs.overrides must contain at least one field):

```json
{
  "code": "EIBACC0315",
  "message": "deposit_configs.overrides must contain at least one field"
}
```

400 Example `overrideValidUntilPast` (valid_until must be a future datetime):

```json
{
  "code": "EIBACC0308",
  "message": "valid_until must be a future datetime"
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

400 Example `maturityPeriodMutuallyExclusive` (maturity_period — calendar_maturity_date and unit/value are mutually exclusive):

```json
{
  "code": "EIBACC0307",
  "message": "Validation error",
  "details": "maturity_period accepts either calendar_maturity_date OR unit+value, not both. Choose one: send calendar_maturity_date for an explicit date, or unit+value for a relative period."
}
```

400 Example `maturityPeriodResolvesToPastDate` (maturity_period resolves to a maturity date in the past):

```json
{
  "code": "EIBACC0306",
  "message": "Validation error",
  "details": "maturity_period resolves to a maturity date in the past. Measured from the attachment's effective_date, the resolved date must be the current date or later."
}
```

400 Example `maturityPeriodInvalidFormat` (maturity_period — calendar_maturity_date is not in YYYY-MM-DD format):

```json
{
  "code": "EIBACC0305",
  "message": "Validation error",
  "details": "calendar_maturity_date must be in YYYY-MM-DD format"
}
```

400 Example `maturityPeriodInvalidValue` (maturity_period — value must be a positive integer):

```json
{
  "code": "EIBACC0299",
  "message": "Validation error",
  "details": "maturity_period value must be a positive integer (>= 1)"
}
```

400 Example `maturityPeriodInvalidUnit` (maturity_period — unit is not supported):

```json
{
  "code": "EIBACC0298",
  "message": "Validation error",
  "details": "Invalid maturity_period unit. Supported values: DAYS, WEEKS, MONTHS, YEARS"
}
```

400 Example `maturityPeriodBelowMinTerm` (maturity_period is below the product's configured min_term):

```json
{
  "code": "EIBACC0109",
  "message": "Maturity period is below the configured MinTerm of the product"
}
```

400 Example `maturityPeriodAboveMaxTerm` (maturity_period is above the product's configured max_term):

```json
{
  "code": "EIBACC0110",
  "message": "Maturity period is above the configured MaxTerm of the product"
}
```

##### Response 404

404 Example `attachmentNotFound` (Active deposit attachment not found for this account):

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
| 400 | `EIBACC0308` | valid_until must be a future datetime |
| 400 | `EIBACC0310` | Validation error |
| 400 | `EIBACC0307` | Validation error |
| 400 | `EIBACC0306` | Validation error |
| 400 | `EIBACC0305` | Validation error |
| 400 | `EIBACC0299` | Validation error |
| 400 | `EIBACC0298` | Validation error |
| 400 | `EIBACC0109` | Maturity period is below the configured MinTerm of the product |
| 400 | `EIBACC0110` | Maturity period is above the configured MaxTerm of the product |
| 404 | `EIBACC0113` | Product attachment not found |
| 409 | `EIBACC0301` | Product attachment is not active |
| 409 | `EIBACC0314` | Product attachment was modified concurrently; retry with the latest state |
| 500 | `EIBACC0007` | Internal error |
| 500 | `EIBACC0316` | Failed to update attachment overrides |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `deposit-product-account-attachment-updated-1` | https://developers.pismo.io/events/docs/deposit-product-account-attachment-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-interest-bearing-accounts`.

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

<!-- schema: #/components/schemas/DepositConfigs -->
### Schema `DepositConfigs`

Pointer: `#/components/schemas/DepositConfigs`. Type: object (schema `DepositConfigs`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maturity_period` | object (schema `MaturityPeriod`) | no | Defines when the deposit matures. There are three usage modes:<br><br>* **Relative period**: Sends `unit` + `value` (e.g. `MONTHS` + `6`).<br>* **Explicit date**: Sends `calendar_maturity_date` (e.g. `2027-06-15`).<br>* **Default**: Omits the field or sends `{}`. The product's configured default maturity term (`PRODUCT_DEFAULT_MATURITY_DATE_DAYS`, typically `10950` days ≈ 30 years) is applied.<br><br>**NOTE**: `calendar_maturity_date` and `unit`/`value` are mutually exclusive, sending both in the same request returns a `400` validation error.<br><br>In the **attach** endpoints, the response returns exactly what was sent in the request:<br>* Send `unit` + `value` returns `unit` + `value`<br>* Send `calendar_maturity_date` returns `calendar_maturity_date`<br>* Send nothing (default fallback applied) returns `unit=DAYS` and `value` equal to the product's configured `PRODUCT_DEFAULT_MATURITY_DATE_DAYS`<br><br>**NOTE**: this behavior applies only to attach. The `GET` attachment endpoints and `PATCH /v1/deposits/accounts/{accountId}/attachment` return the resolved term, with `unit`, `value`, and `calendar_maturity_date` populated together. A `PATCH` sent in explicit‑date form is returned normalized as `{unit: DAYS, value: <days>, calendar_maturity_date: <date>}`.<br> |  |
| `payout_account` | object (schema `PayoutAccount`) | no | The payout account defines where outbound payments are sent, and it is used in two operational contexts.<br><br><br>* **Capitalization flow**: When the capitalization mode is set to `PAYOUT`, the capitalized interest is directed to this account. If the mode is `REINVEST`, the payout account is not involved because the interest is added to the principal instead.<br>* **Maturity instruction flow**: At maturity, this account receives principal or interest whenever the maturity instructions specify `PAY` for either `maturity_instructions.principal` or `maturity_instructions.interest`. This flow always relies on the payout account, regardless of how capitalization is configured.<br><br>Both flows reference the same payout account settings. Choosing `REINVEST` for capitalization does not remove or disable the payout account, and it remains fully available for maturity‑related payments.<br> |  |
| `interest_capitalization_mode` | string | no | Controls the treatment of capitalized interest. Optional field.<br><br><br>* `REINVEST` (default): The Pismo platform adds the capitalized amount to the principal. The new principal becomes the foundation for the next accrual cycle. No `payout_account` is required.<br>* `PAYOUT` (explicit): The capitalized amount is routed to `payout_account`. A valid `payout_account` is **required** in this request when this value is passed explicitly—omitting it returns `400 EIBACC0379`.<br>* `Omitted`: The Pismo platform applies `REINVEST`. Both the GET operation and events return `REINVEST`.<br><br>This setting affects only the capitalization process. The maturity instruction flow always uses `payout_account`, regardless of the value of this field.<br> | enum: ["REINVEST", "PAYOUT"]; default: "REINVEST"; example: "REINVEST" |
| `overrides` | object (schema `AttachmentOverridesRequest`) | no | Per-attachment overrides applied on top of the product defaults. All sub-fields are optional.<br>This object contains the per‑attachment overrides that supplement the product defaults. All sub‑fields are optional. Omitting a section causes the Pismo platform to follow the normal fallback sequence, moving from the account level to the program and then to the product defaults. Each penalty type provides `waived` as a required field, optional type‑specific fields, and an optional `valid_until` to schedule the revert.<br> |  |

<!-- schema: #/components/schemas/AttachmentOverridesSnapshot -->
### Schema `AttachmentOverridesSnapshot`

Pointer: `#/components/schemas/AttachmentOverridesSnapshot`. Type: object (schema `AttachmentOverridesSnapshot`).

> Representation of the persisted overrides, present only when the request defined at least one override. Sub-fields are included only when set. The `renewal_term` always returns all three fields together (`unit`, `value` and `renewal_calendar_maturity_date`), mirroring the behavior of `maturity_period`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maturity_instructions` | object (schema `MaturityInstructionsOverrideRequest`) | no | Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.<br> |  |
| `renewal_term` | object (schema `RenewalTermResponse`) | no | Renewal term applied on each rollover. Always returns all three fields together — `unit`, `value` and `renewal_calendar_maturity_date` — regardless of the form the client used to configure it, mirroring `maturity_period`. Legacy terms persisted before the calendar date was stored return only `unit`+`value`.<br> |  |
| `penalties` | object (schema `PenaltiesOverrideSnapshot`) | no | Persisted penalty overrides for each type. Types appear only when set. Each entry includes `waived`, the relevant type-specific fields, and an optional `valid_until` for scheduling the revert.<br> |  |

<!-- schema: #/components/schemas/AttachmentOverridesPatchRequest -->
### Schema `AttachmentOverridesPatchRequest`

Pointer: `#/components/schemas/AttachmentOverridesPatchRequest`. Type: object (schema `AttachmentOverridesPatchRequest`).

> PATCH envelope for account‑level `deposit_configs.overrides`. Fields support three‑state semantics, omission preserves the current value, `null` removes the override and restores the inherited configuration, and a provided value replaces it. The envelope must define at least one field, an empty overrides object returns a `400` error: `EIBACC0315`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maturity_instructions` | object | no |  |  |
| `maturity_instructions.principal` | string | no | Specifies how the principal is handled once the deposit matures. | enum: ["ROLLOVER", "PAY"]; example: "ROLLOVER" |
| `maturity_instructions.interest` | string | no | Specifies how the interest is handled once the deposit matures. | enum: ["ROLLOVER", "PAY"]; example: "PAY" |
| `maturity_instructions.reason` | string | no | Optional audit-trail reason. | maxLength: 100; example: "Customer preference at onboarding" |
| `renewal_term` | object | no |  |  |
| `renewal_term.unit` | string | no | Time unit of the renewal term. Required together with `value` when calendar form is not used. | enum: ["DAYS", "WEEKS", "MONTHS", "YEARS"]; example: "MONTHS" |
| `renewal_term.value` | integer | no | Number of units. Required together with `unit` when calendar form is not used. | minimum: 1; example: 6 |
| `renewal_term.renewal_calendar_maturity_date` | string | no | Explicit calendar date (`YYYY-MM-DD`), the date must be a future date, and does not coincide with `unit`+`value`. | format: "date"; example: "2027-05-22" |
| `penalties` | object (schema `PenaltiesPatchRequest`) | no | PATCH envelope for `deposit_configs.overrides.penalties`. Penalty types support three‑state semantics: omit to retain the existing value, use `null` to clear the override and restore the inherited configuration, or provide a value object to replace it. `reason` is optional metadata.<br> |  |

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

<!-- schema: #/components/schemas/AttachmentOverridesRequest -->
### Schema `AttachmentOverridesRequest`

Pointer: `#/components/schemas/AttachmentOverridesRequest`. Type: object (schema `AttachmentOverridesRequest`).

> Per-attachment overrides applied on top of the product defaults. All sub-fields are optional.
> This object contains the per‑attachment overrides that supplement the product defaults. All sub‑fields are optional. Omitting a section causes the Pismo platform to follow the normal fallback sequence, moving from the account level to the program and then to the product defaults. Each penalty type provides `waived` as a required field, optional type‑specific fields, and an optional `valid_until` to schedule the revert.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `maturity_instructions` | object (schema `MaturityInstructionsOverrideRequest`) | no | Overrides the deposit’s behavior at maturity. If a field is omitted, the Pismo platform uses the value defined at the higher‑level configuration that governs this deposit.<br> |  |
| `renewal_term` | object (schema `RenewalTermOverrideRequest`) | no | Specifies the recurring rollover term, not to be confused with the initial `maturity_period`.<br><br>You must provide either `unit` with `value` or `renewal_calendar_maturity_date`.<br><br>A `ROLLOVER` configuration in principal or interest is required.<br><br>When you pass `renewal_calendar_maturity_date`, the Pismo platform converts the interval from today into a day count and stores it at attach time in normalized form: `{unit: DAYS, value: <calculated>}`.<br> |  |
| `penalties` | object (schema `PenaltiesOverrideRequest`) | no | Per-type penalty overrides. Each type independently uses three-state semantics:<br>omit (inherit) · `{waived: true}` (exempt) · `{waived: false, <fields>}` (customize).<br> |  |

<!-- schema: #/components/schemas/PenaltiesPatchRequest -->
### Schema `PenaltiesPatchRequest`

Pointer: `#/components/schemas/PenaltiesPatchRequest`. Type: object (schema `PenaltiesPatchRequest`).

> PATCH envelope for `deposit_configs.overrides.penalties`. Penalty types support three‑state semantics: omit to retain the existing value, use `null` to clear the override and restore the inherited configuration, or provide a value object to replace it. `reason` is optional metadata.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason` | string | no |  | maxLength: 100; example: "Update — Q1 2027 VIP retention package" |
| `grace_period` | object | no |  |  |
| `grace_period.waived` | boolean | yes | `true` = fully exempt; `false` = penalty active (customize via the fields below). |  |
| `grace_period.duration_days` | integer | no |  | minimum: 0 |
| `grace_period.penalty_interest_days` | integer | no |  | minimum: 0 |
| `grace_period.valid_until` | string | no | Schedules the revert of this override via EventBridge. This value must be a future date and follows the ISO 8601 standard. | format: "date-time" |
| `early_withdrawal_after_opening` | object | no |  |  |
| `early_withdrawal_after_opening.waived` | boolean | yes |  |  |
| `early_withdrawal_after_opening.applicable_within_days` | integer | no |  | minimum: 0 |
| `early_withdrawal_after_opening.penalty_interest_days` | integer | no |  | minimum: 0 |
| `early_withdrawal_after_opening.valid_until` | string | no |  | format: "date-time" |
| `withdrawal_fee` | object | no |  |  |
| `withdrawal_fee.waived` | boolean | yes |  |  |
| `withdrawal_fee.type` | string | no |  | enum: ["PERCENTAGE", "FIXED"] |
| `withdrawal_fee.value` | number | no |  | exclusiveMinimum: 0 |
| `withdrawal_fee.valid_until` | string | no |  | format: "date-time" |
| `tiered_interest_forfeiture` | object | no |  |  |
| `tiered_interest_forfeiture.waived` | boolean | yes |  |  |
| `tiered_interest_forfeiture.tiers` | array of object (schema `TieredInterestForfeitureTierRequest`) | no |  |  |
| `tiered_interest_forfeiture.valid_until` | string | no |  | format: "date-time" |
| `subsequent_withdrawals` | object | no |  |  |
| `subsequent_withdrawals.waived` | boolean | yes |  |  |
| `subsequent_withdrawals.applicable_within_days` | integer | no |  | minimum: 1 |
| `subsequent_withdrawals.penalty_interest_days` | integer | no |  | minimum: 1 |
| `subsequent_withdrawals.window_behavior` | string | no |  | enum: ["ROLLING", "FIXED"] |
| `subsequent_withdrawals.valid_until` | string | no |  | format: "date-time" |

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

<!-- schema: #/components/schemas/PenaltiesOverrideRequest -->
### Schema `PenaltiesOverrideRequest`

Pointer: `#/components/schemas/PenaltiesOverrideRequest`. Type: object (schema `PenaltiesOverrideRequest`).

> Per-type penalty overrides. Each type independently uses three-state semantics:
> omit (inherit) · `{waived: true}` (exempt) · `{waived: false, <fields>}` (customize).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason` | string | no | Optional audit-trail reason for the entire penalties block. | maxLength: 100; example: "Q4 2026 VIP retention package" |
| `grace_period` | object (schema `GracePeriodOverrideRequest`) | no | Grace period override. Type-specific fields are optional pointers, when omitted, the Pismo platform follows the normal fallback sequence, moving from the account level to the program and then to the product defaults. |  |
| `early_withdrawal_after_opening` | object (schema `EarlyWithdrawalAfterOpeningOverrideRequest`) | no | Override for early withdrawal after account opening. |  |
| `withdrawal_fee` | object (schema `WithdrawalFeeOverrideRequest`) | no | Withdrawal fee override. |  |
| `tiered_interest_forfeiture` | object (schema `TieredInterestForfeitureOverrideRequest`) | no | Tiered interest forfeiture override. Tiers replace the product's tiers when provided. |  |
| `subsequent_withdrawals` | object (schema `SubsequentWithdrawalsOverrideRequest`) | no | Subsequent withdrawals (Regulation D) override. |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Interest-bearing_accounts.yaml` | tag `Account attachment`: GET /v1/products/attachments/accounts/{accountId}, POST /v1/deposits/accounts/{accountId}/attach, POST /v1/deposits/accounts/{accountId}/detach, PATCH /v1/deposits/accounts/{accountId}, POST /v1/savings-accounts/accounts/{accountId}/attach, POST /v1/savings-accounts/accounts/{accountId}/detach, PATCH /v1/savings-accounts/accounts/{accountId}, PATCH /v1/deposits/accounts/{accountId}/attachment | https://github.com/PismoDevEx/pismo-api-specs | `89fc3f8ed0222a57…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-BANK-interest-bearing-accounts` — Interest-bearing accounts
- `KU-CC-deposit-products` — Control Center deposit products and interest plans
- `KU-ERR-codes-eibacc` — Error codes: EIBACC
- `KU-EVT-catalogue-deposit` — Event catalogue: deposit
- `KU-EVT-interest-management-data-events` — Banking - Interest management
