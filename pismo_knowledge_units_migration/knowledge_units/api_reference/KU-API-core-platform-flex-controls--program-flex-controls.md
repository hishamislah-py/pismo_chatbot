---
ku_id: KU-API-core-platform-flex-controls--program-flex-controls
title: 'API reference: Core platform - Flex controls — Program flex controls'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Flex_controls.yaml
  sha256: af34d94f331c9b17178fc3eb93eae91bf3149e9f092fdef64d6b4e55ba9ef9a5
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
- get-v1-flex-controls
related_kus:
- KU-ERR-codes-erul
specification_version: 1.0.0
---

# API reference: Core platform - Flex controls — Program flex controls

**KU ID:** `KU-API-core-platform-flex-controls--program-flex-controls` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Program flex controls` in `api-specs/Core_platform_-_Flex_controls.yaml` (“Core platform - Flex controls”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> API endpoints for retrieving flex controls grouped by program.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/flex-controls` | `get-v1-flex-controls` | List program flex controls | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Flex_controls.yaml method=GET path=/v1/flex-controls operationId=get-v1-flex-controls -->
### `GET /v1/flex-controls` — List program flex controls

- **operationId:** `get-v1-flex-controls`
- **Specification:** `api-specs/Core_platform_-_Flex_controls.yaml` (Core platform - Flex controls)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rules`
- **Tags:** `Program flex controls`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List all flex controls grouped by program, with pagination support.
> Results are ordered by program ID in ascending order.
>
> Use the optional `programId` query parameter to filter results to a single program.
> If `programId` is provided and no templates are found for that program, a `404` is returned.
>
> If no `programId` is specified and no templates exist at all, an empty paginated response is returned with status `200`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization ID / tenant identifier. | example: "org-12345" |
| `programId` | query | no | integer | Filter flex controls by a specific program ID. Must be a positive integer greater than 0. | format: "int64"; minimum: 1; example: 123 |
| `page` | query | no | integer | Page number for pagination. Must be greater than or equal to 1. Defaults to 1 when omitted. | default: 1; minimum: 1; example: 1 |
| `perPage` | query | no | integer | Number of programs to return per page. Must be greater than or equal to 1. Defaults to 10 when omitted. | default: 10; minimum: 1; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. Returns paginated flex controls grouped by program. | `application/json`: object (schema `ProgramFlexControlsResponse`) |
| 400 | Bad request. Returned in the following cases:<br>- The `x-tenant` header is missing.<br>- The `programId` query parameter is not a positive integer.<br>- Pagination parameters are zero or cannot be parsed as integers.<br> | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found. Returned when `programId` is specified but no flex controls are found for that program. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error. | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pages` | integer | yes | Total number of pages | example: 5 |
| `current_page` | integer | yes | Current page number | example: 1 |
| `per_page` | integer | yes | Number of programs per page | example: 10 |
| `total_items` | integer | yes | Total number of programs | example: 45 |
| `programs` | array of object (schema `ProgramControlsItem`) | yes | List of programs with their flex controls |  |

##### Response 400

400 Example `missing x-tenant header` — from `#/components/examples/ERUL0101`:

```json
{
  "message": "error validating request header",
  "error_code": "RULVAL0400",
  "details": [
    {
      "location": "header.x-tenant",
      "message": "missing x-tenant"
    }
  ],
  "code": "ERUL0101"
}
```

400 Example `invalid programId` — from `#/components/examples/ERUL0102`:

```json
{
  "message": "error validating request parameter",
  "error_code": "RULVAL0400",
  "details": [
    {
      "location": "query.programId",
      "message": "programId must be a positive integer"
    }
  ],
  "code": "ERUL0102"
}
```

400 Example `invalid pagination params` — from `#/components/examples/ERUL1501`:

```json
{
  "message": "error validating request parameters",
  "error_code": "RULVAL0400",
  "details": [
    {
      "location": "query.page",
      "message": "page must be greater than or equal to 1"
    }
  ],
  "code": "ERUL1501"
}
```

##### Response 404

404 Example `template not found by programId` — from `#/components/examples/ERUL0204`:

```json
{
  "message": "Flex Controls not found for the specified program",
  "error_code": "RULREP0404",
  "code": "ERUL0204"
}
```

##### Response 500

500 Example `internal server error` — from `#/components/examples/ERUL0001`:

```json
{
  "message": "internal server error",
  "error_code": "RULREP0500",
  "code": "ERUL0001"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERUL0101` | error validating request header |
| 400 | `RULVAL0400` | error validating request header |
| 400 | `ERUL0102` | error validating request parameter |
| 400 | `ERUL1501` | error validating request parameters |
| 404 | `ERUL0204` | Flex Controls not found for the specified program |
| 404 | `RULREP0404` | Flex Controls not found for the specified program |
| 500 | `ERUL0001` | internal server error |
| 500 | `RULREP0500` | internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ProgramControlsItem -->
### Schema `ProgramControlsItem`

Pointer: `#/components/schemas/ProgramControlsItem`. Type: object (schema `ProgramControlsItem`).

> Flex controls for a single program

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `program_id` | integer | yes | Program ID | format: "int64"; example: 1234 |
| `controls` | object (schema `ProgramControls`) | yes | Collection of restriction and accumulator controls |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Error description |  |
| `error_code` | string | no | Error code ID | deprecated: true |
| `code` | string | no | Error code ID |  |

<!-- schema: #/components/schemas/ProgramControls -->
### Schema `ProgramControls`

Pointer: `#/components/schemas/ProgramControls`. Type: object (schema `ProgramControls`).

> Collection of restriction and accumulator controls

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `restriction_controls` | array of object (schema `FlexControlRestrictionControl`) | yes | List of restriction controls |  |
| `accumulator_controls` | array of object (schema `FlexControlAccumulatorControl`) | yes | List of accumulator controls |  |

<!-- schema: #/components/schemas/FlexControlRestrictionControl -->
### Schema `FlexControlRestrictionControl`

Pointer: `#/components/schemas/FlexControlRestrictionControl`. Type: object (schema `FlexControlRestrictionControl`).

> Simplified restriction control for program flex controls

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | Control name | example: "Single POS value card level limit" |
| `type` | string | yes | Control type | example: "restriction" |
| `level` | string | yes | Control level (account or card) | enum: ["account", "card"]; example: "card" |
| `processing_codes` | array of string (schema `ProcessingCodes`) | no | Processing codes list for evaluating flex control conditions. If the value is empty, the flex control applies to any processing code.<br> | example: ["07000", "07001"] |
| `conditions` | array of object (schema `Condition`) | no | List of conditions |  |
| `deny_code` | string | yes | Deny code when control fails | example: "Single_POS_Value" |
| `active` | boolean | yes | Is the control active? | default: true; example: true |

<!-- schema: #/components/schemas/FlexControlAccumulatorControl -->
### Schema `FlexControlAccumulatorControl`

Pointer: `#/components/schemas/FlexControlAccumulatorControl`. Type: object (schema `FlexControlAccumulatorControl`).

> Simplified accumulator control for program flex controls

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | Control name | example: "Cumulative POS value card level limit" |
| `type` | string | yes | Control type | example: "spending_limit" |
| `level` | string | yes | Control level (account or card) | enum: ["account", "card"]; example: "account" |
| `processing_codes` | array of string (schema `ProcessingCodes`) | no | Processing codes list for evaluating flex control conditions. If the value is empty, the flex control applies to any processing code.<br> | example: ["07000", "07001"] |
| `max_limit` | integer (schema `MaxLimit`) | no | Defines the maximum limit for the control. Its meaning depends on the flex control `type`.<br>  * For `spending_limit` controls, `max_limit` represents the maximum spending amount allowed.<br>  * For `usage_limit` controls, `max_limit` represents the maximum number of transactions allowed.<br><br>Once met or exceeded, any subsequent transactions are declined by evaluation control flow.<br><br>For spending limits, note that this value is an integer. Since global currencies vary in the number of digits that are allowed after the decimal point, you must convert the actual maximum spending limit into an integer value to use in this field. To do this, use the following formula.<br><br>value = floatNumber × 10^X, where X is the number of digits after the decimal separator for the currency as defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for BRL currency transactions, where the number of decimal places is 2, you must set it to `49999` (499.99 × 10²).<br><br>If you want to set the value 499 for JPY currency transactions, where the number of decimal places is 0, you must set it to `4999` (4999.0 × 10^0 = 4999.0 × 1 - in other words, the value doesn't change.)<br><br>This field is **REQUIRED** for flex controls with the `type` of `spending_limit` and `usage_limit`, and it does not apply to flex controls with the `type` of `restriction` and `cumulative_limit`.<br> | format: "int64"; minimum: 1; example: 1000 |
| `max_amount` | integer (schema `MaxAmount`) | no | Maximum accumulated amount allowed. Once met or exceeded, subsequent transactions are declined by the evaluation control flow. Valid only for flex controls with the `type` of `cumulative_limit`.<br>Note that the value must be calculated as follows.<br><br>value = floatNumber × 10^X, where X is the number of digits after the decimal separator for the currency defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for USD currency transactions, where the number of decimal places is 2, you must set the value to `49999` (499.99 × 10²).<br><br>If you want to set the value 499 for JPY currency transactions, where the number of decimal places is 0, you must set the value to `499` (499.0 × 10^0 = 499.0 × 1 - in other words, the value doesn't change).<br> | format: "int64"; minimum: 1; example: 100000 |
| `max_transactions` | integer (schema `MaxTransactions`) | no | Maximum number of transactions allowed. Once met or exceeded, subsequent transactions are declined by the evaluation control flow. Valid only for flex controls with the `type` of `cumulative_limit`.<br> | format: "int64"; minimum: 1; example: 10 |
| `limit_duration` | string (schema `LimitDuration`) | no | Flex control limit period duration (ISO 8601 format).<br>For example, if a flex control sets a spending limit of $500, and `limit_duration` is set to one month (`P1M`), then the user cannot spend more than $500 from the account in any one month period.<br> | example: "P1M" |
| `conditions` | array of object (schema `Condition`) | no | List of conditions |  |
| `deny_code` | string | yes | Deny code when control fails | example: "CUM_POS_Value" |
| `active` | boolean | yes | Is the control active? | default: true; example: true |

<!-- schema: #/components/schemas/Condition -->
### Schema `Condition`

Pointer: `#/components/schemas/Condition`. Type: object (schema `Condition`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Condition ID | format: "uuid"; example: "b4930a4d-e2c4-4fdc-9803-c83dec3a30d1" |
| `attribute` | string | yes | Attribute to evaluate in the condition.<br>* `amount`: Numeric value that indicates the amount of the operation performed by the user<br>* `balance`: Maximum balance amount allowed in an account. Due to fiscal restrictions in some countries, the user cannot have more than a certain amount in the account. When the balance value is defined, the control validates any process of entering money into that account, evaluates the account balance at the time of the transaction, and denies any inflow of money above the amount defined in the balance value.<br>* `country_code`: Three-letter country code (ISO 3166-1) indicating the location where the transaction is initiated or processed.<br>* `entry_mode`: A code used to establish the mode of purchase. Valid only for card network operations. For a control to be valid, it must be a code defined by the entire Field 22 (Visa) or DE 22 (Mastercard) or as specified by each card network.<br>    * Visa: Field 22 contains a 4-digit code indicating the method used to enter the account number and card expiration date (positions 1 and 2) and, if an electronic terminal is used, the capability of the terminal to capture online PINs (position 3) and the last digit (position 4) equal to 0 (unused) for transactions processed through VisaNet. This field is fixed-length with three subfields.<br>    * Mastercard: DE 22 contains a 3-digit code indicating the method used to enter the account number and card expiration date (positions 1 and 2) and, if an electronic terminal is used, the capability of the terminal to capture online PINs (position 3).<br>* `is_device_registered`: Boolean that indicates whether the device used for the operation is registered according to the financial institution's security policies.<br>* `is_password_present`: Boolean that indicates whether a valid password is present in the evaluation request. Valid only for card network operations.<br>* `is_pin_validated_offline`: Boolean that indicates whether the pin was validated offline in the evaluation request. This is commonly used for offline PIN verification scenarios. Valid only for card network operations.<br>* `is_physical_card_present`: Boolean that indicates whether a physical card is present in the evaluation request. Valid only for card network operations. Digital wallet transactions are treated as physical card transactions. To exclude digital wallet transactions, combine this condition with `is_token_present` as `true`.<br>* `is_tra_exemption_requested`: Boolean that indicates whether a TRA (Transaction Risk Assessment) exemption is requested for the transaction. Valid only for card network operations.<br>* `merchant_category_code`: Merchant Category Code (MCC) is a four-digit number used to describe a merchant's primary business activities. Valid only for card network operations. For a control to be valid, you must enter a code specified by the Mastercard/Visa card network.<br>* `merchant_id`: Merchant ID. Valid only for card network operations. For a control to be valid, you must enter a code specified by the Mastercard/Visa card network.<br>* `month_day`: Day of the month when the operation is performed. Commonly used to limit operations on holidays. The format is MMM-DD. For example, enter January 25 as "JAN-25".<br>* `number_of_installments`: Number of installments in the operation<br>* `time_now`: Restriction window used to establish the time when the operation is performed, defined in the Coordinated Universal Time (UTC 0) zone. For example, a 10:59 PM-06:59 AM window specifies restrictions that apply from 11 PM to 7 AM in the UTC 0 time.<br>* `week_day`: Day of the week when the operation occurs. Use the full lowercase weekday name. Valid values: sunday, monday, tuesday, wednesday, thursday, friday, saturday.<br>* `authentication_method`:  Determine whether restrictions should be applied for specific authentication methods. For a control to be valid, it must be a code defined by the Field 60.8/Positions 9-10 for Visa operations or as specified by each card network. Valid only for card network operations.<br>* `is_token_present`: Boolean that indicates whether a token card is present in the evaluation request. Valid only for card network operations.<br>* `initiation_mode`: Payment initiation mode. Valid only for card network operations.<br>   - `moto`: Payments made through mail order or telephone.<br>   - `mit`: Merchant-initiated transactions.<br>* `acquirer_country_code`: Three-letter country code (ISO 3166-1) representing the location of the acquiring bank or financial institution. Valid only for card network operations.<br>* `is_cavv_present`: Boolean indicating that the CAVV field is present. CAVV stands for cardholder authentication verification value. Valid only for card network operations.<br>* `avr`: String indicating that the transaction is a card network Account Verification Request (AVR) transaction. AVR transactions differ from standard authorizations in that they are typically zero-value and are used for card network verification flows. Currently, the only supported value for this attribute is `mtt`, which is the Mobility & Transport Transaction (MTT) type.<br>* `operation_type`: Type of operation being performed. Allowed values are:<br>  - `debit` - debit transaction<br>  - `credit` - credit transaction<br>  - `none` -  transaction that doesn't have a financial impact on the account balance, even though an authorization event occurs. These transactions still exist in the authorization flow, but they don't generate balance movement. AVR (Account Verification Request) is one example of this type of transaction with a zero‑amount authorization.<br> | enum: ["balance", "amount", "merchant_category_code", "week_day", "month_day", "time_now", "entry_mode", "merchant_id", "country_code", "number_of_installments", "is_physical_card_present", "is_device_registered", "is_tra_exemption_requested", "is_pin_validated_offline", "authentication_method", "is_token_present", "initiation_mode", "acquirer_country_code", "is_cavv_present", "avr", "operation_type"] |
| `operator` | string | yes | Condition type evaluation<br>* eq - equal to value<br>* neq - not equal to value<br>* lt - lower than value<br>* lte - lower than or equal to value<br>* gt - greater than value<br>* gte - greater than or equal to value<br>* in - includes value<br>* nin - does not include value<br>* bt - between two values<br>* in_group - in attribute group<br>* not_in_group - not in attribute group<br> | enum: ["eq", "neq", "lt", "lte", "gt", "gte", "in", "nin", "bt", "in_group", "not_in_group"] |
| `value` | string | yes | Value to compare | example: "10000" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Flex_controls.yaml` | tag `Program flex controls`: GET /v1/flex-controls | https://github.com/PismoDevEx/pismo-api-specs | `af34d94f331c9b17…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-erul` — Error codes: ERUL
