---
ku_id: KU-API-core-platform-flex-controls--customer-flex-controls-part-02
title: 'API reference: Core platform - Flex controls — Customer flex controls (part 2 of 2)'
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
- path: api-reference-data/endpoint_event_map.csv
  sha256: 34649b6033098e514ab0440f13d45a56ec7fd2b476137de7f9fa6867034655c2
  url: https://github.com/PismoDevEx/pismo-api-specs
  role: reference_table
  updated_at: '2026-10-13T20:51:51+00:00'
operations:
- get-v1-customers-flex-control
- patch-v1-customers-flex-control
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-ERR-codes-erul
- KU-EVT-catalogue-audit
- KU-EVT-flex-controls-data-events
specification_version: 1.0.0
---

# API reference: Core platform - Flex controls — Customer flex controls (part 2 of 2)

**KU ID:** `KU-API-core-platform-flex-controls--customer-flex-controls-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 2 operation(s) tagged `Customer flex controls` in `api-specs/Core_platform_-_Flex_controls.yaml` (“Core platform - Flex controls”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> API endpoints for managing customer flex controls.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/customers/{customerId}/flex-controls/{flexControlId}` | `get-v1-customers-flex-control` | Get customer flex control | no |
| `PATCH /v1/customers/{customerId}/flex-controls/{flexControlId}` | `patch-v1-customers-flex-control` | Update customer flex control | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Flex_controls.yaml method=GET path=/v1/customers/{customerId}/flex-controls/{flexControlId} operationId=get-v1-customers-flex-control -->
### `GET /v1/customers/{customerId}/flex-controls/{flexControlId}` — Get customer flex control

- **operationId:** `get-v1-customers-flex-control`
- **Specification:** `api-specs/Core_platform_-_Flex_controls.yaml` (Core platform - Flex controls)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rules`
- **Tags:** `Customer flex controls`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a flex control, given the `customerId` and `flexControlId`.
>
> NOTE: This endpoint requires an account-specific access token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `customerId` | path | yes | number | Customer ID | example: 9999999 |
| `flexControlId` | path | yes | string | Flex control ID | format: "uuid"; example: "84ba9052-31d3-41da-99d2-a1632d5ce2e5" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. Flex control was found. | `application/json`: object (schema `CustomerFlexControlsResponse`) |
| 400 | Bad request. Validation error on request. | `application/json`: object (schema `ErrorResponseWithDetails`) |
| 403 | Forbidden. Authorization error on request. | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found. Flex control for customerId not found. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error. | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | yes | Flex control ID is auto-generated at creation time.<br> | format: "uuid"; example: "89cbdadc-860b-4275-a5cd-d9d892fd3869" |
| `type` | string (schema `CustomerType`) | yes | Flex control scope<br>  * `usage_limit`: Cumulative flex control that increases by one until `max_limit`<br>  * `spending_limit`: Cumulative flex control that increases by the current transaction's `amount` until `max_limit`<br>  * `cumulative_limit`: Cumulative flex control that increases by one transaction or by transaction amount until a condition is met, applies only to flex controls with associated `card_ids`, and requires a `reset_strategy`<br>  * `restriction`: Restriction flex control that only validates specified conditions<br> | enum: ["spending_limit", "usage_limit", "restriction", "cumulative_limit"] |
| `processing_codes` | array of string (schema `ProcessingCodes`) | no | Processing codes list for evaluating flex control conditions. If the value is empty, the flex control applies to any processing code.<br> | example: ["07000", "07001"] |
| `rule_reference_id` | string | no | ID of program-level flex control. Only present in generic flex controls created for the entire program. | example: "purchase-1M" |
| `name` | string (schema `Name`) | no | Flex control name | example: "Purchase 1M limit" |
| `account_id` | integer | yes | Account ID | format: "int64"; example: 8988000 |
| `customer_id` | integer | no | Customer ID | format: "int64"; example: 99999999 |
| `card_ids` | array of number | no | Card ID list | example: [11111, 22222]; items.format: "int64" |
| `currency_code` | string (schema `CurrencyCode`) | no | Flex control currency code (ISO 4217). Defines the precision used for monetary values such as `max_limit`, `available_limit`, and `condition.value`.<br> | example: "BRL" |
| `max_limit` | integer (schema `MaxLimit`) | no | Defines the maximum limit for the control. Its meaning depends on the flex control `type`.<br>  * For `spending_limit` controls, `max_limit` represents the maximum spending amount allowed.<br>  * For `usage_limit` controls, `max_limit` represents the maximum number of transactions allowed.<br><br>Once met or exceeded, any subsequent transactions are declined by evaluation control flow.<br><br>For spending limits, note that this value is an integer. Since global currencies vary in the number of digits that are allowed after the decimal point, you must convert the actual maximum spending limit into an integer value to use in this field. To do this, use the following formula.<br><br>value = floatNumber × 10^X, where X is the number of digits after the decimal separator for the currency as defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for BRL currency transactions, where the number of decimal places is 2, you must set it to `49999` (499.99 × 10²).<br><br>If you want to set the value 499 for JPY currency transactions, where the number of decimal places is 0, you must set it to `4999` (4999.0 × 10^0 = 4999.0 × 1 - in other words, the value doesn't change.)<br><br>This field is **REQUIRED** for flex controls with the `type` of `spending_limit` and `usage_limit`, and it does not apply to flex controls with the `type` of `restriction` and `cumulative_limit`.<br> | format: "int64"; minimum: 1; example: 1000 |
| `max_transactions` | integer (schema `MaxTransactions`) | no | Maximum number of transactions allowed. Once met or exceeded, subsequent transactions are declined by the evaluation control flow. Valid only for flex controls with the `type` of `cumulative_limit`.<br> | format: "int64"; minimum: 1; example: 10 |
| `max_amount` | integer (schema `MaxAmount`) | no | Maximum accumulated amount allowed. Once met or exceeded, subsequent transactions are declined by the evaluation control flow. Valid only for flex controls with the `type` of `cumulative_limit`.<br>Note that the value must be calculated as follows.<br><br>value = floatNumber × 10^X, where X is the number of digits after the decimal separator for the currency defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for USD currency transactions, where the number of decimal places is 2, you must set the value to `49999` (499.99 × 10²).<br><br>If you want to set the value 499 for JPY currency transactions, where the number of decimal places is 0, you must set the value to `499` (499.0 × 10^0 = 499.0 × 1 - in other words, the value doesn't change).<br> | format: "int64"; minimum: 1; example: 100000 |
| `available_amount` | integer (schema `AvailableAmount`) | no | The remaining amount allowed for authorizations under the current flex control. This value decreases with each successful authorization and resets based on the defined reset strategy. Valid only for flex controls with the `type` of `cumulative_limit`.<br> | format: "int64"; example: 100000 |
| `available_transactions` | integer (schema `AvailableTransactions`) | no | The remaining number of transactions allowed for authorizations under the current flex control. This value decreases with each successful authorization and resets based on the defined reset strategy. Valid only for flex controls with the `type` of `cumulative_limit`.<br> | format: "int64"; example: 10 |
| `limit_duration` | string (schema `LimitDuration`) | no | Flex control limit period duration (ISO 8601 format).<br>For example, if a flex control sets a spending limit of $500, and `limit_duration` is set to one month (`P1M`), then the user cannot spend more than $500 from the account in any one month period.<br> | example: "P1M" |
| `reset_datetime` | string (schema `ResetDatetime`) | no | The exact date and time of the next reset for the flex control's spending window, in RFC-3339 format. This value is response-only: it is calculated by the platform and is never accepted in requests.<br><br>When `reset_period` is defined, the reset follows the configured schedule (for example, `month_day: 10` resets on the 10th day of every month). When `reset_period` is omitted, the reset occurs at the control's creation date and time plus `limit_duration`.<br><br>This value is recalculated whenever an authorization is evaluated. If no authorizations have been processed since the last reset, it may still point to a reset datetime that has already passed.<br><br>This field is returned only for flex controls with the `type` of `spending_limit` or `usage_limit`.<br> | format: "date-time"; example: "2022-03-08T21:19:55Z" |
| `time_zone` | string (schema `TimeZone`) | no | IANA Time Zone database, such as "America/New_York".<br>This attribute is used to evaluate the flex control using the desired time zone for condition attributes such as `week_day`, `month_day`, `time_now`, and `reset_period`.<br>If `time_zone` is empty, the control is evaluated using the UTC time zone.<br> | example: "America/Sao_Paulo" |
| `reset_period` | object (schema `ResetPeriod`) | no | Enables the specification of reset periods for accumulators based on the duration in `limit_duration`. When this field is set, it must follow the RFC 3339 pattern from ISO 8601. When `reset_period` changes, the `avaliable_limit` is reset.<br> |  |
| `reset_strategy` | object (schema `ResetStrategy`) | no | The strategy to reset the accumulators. Valid only for flex controls with the `type` of `cumulative_limit`. |  |
| `available_limit` | integer (schema `AvailableLimit`) | no | Represents the remaining limit for the flex control. Its meaning depends on the flex control `type`.<br>  * For `spending_limit` controls, `available_limit` is the remaining spending amount.<br>  * For `usage_limit` controls, `available_limit` is the remaining number of transactions allowed.<br><br>The `available_limit` is calculated by: `max_limit` - `current_spend_limit`. The `current_spend_limit`, an internal field, is the total amount of all approved transactions in the `limit_duration` period. It is reset by the evaluation flow when a new transaction is evaluated in the new period according to the `reset_period`.<br><br>When `available_limit` is set in a PATCH request via [Update account flex control](ref:patch-v1-accounts-flex-control) or [Update customer flex control](ref:patch-v1-customers-flex-control), it resets `current_spend_limit`. In this case, `available_limit` cannot be greater than `max_limit`.<br><br>For spending limits, note that `available_limit` is an integer. Since global currencies vary in the number of digits that are allowed after the decimal point, you must convert the actual maximum spending limit into an integer value to use in this field. To do this, use the following formula:<br><br>value = floatNumber * 10^x,<br>where x is the number of digits for the currency as defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for BRL currency transactions, you must set 49999 = 499.99 * 10^2.<br><br>On the other hand, the Japanese money system doesn't use fractions of a yen (the Japanese currency). So, to set the value at 4999 yen, you must set 4999 = 4999.0 * 10^0 = 4999.0 * 1. (In other words, the value doesn't change.)<br> | format: "int64"; example: 300 |
| `conditions` | array of object (schema `Condition`) | no |  | example: [{"attribute": "balance", "operator": "gt", "value": "10000"}] |
| `active` | boolean (schema `Active`) | no | If not specified, defaults to 'true'. If set to 'false', the flex control is skipped during evaluation. | default: true; example: true |
| `deny_code` | string (schema `DenyCode`) | no | Deny code related to restriction.<br>This code is returned when the evaluation does not meet the conditions.<br> | example: "ERR_VAL_BALANCE" |
| `response_code` | string (schema `ResponseCode`) | no | Alphanumeric two-character response code. This can be the standard card network response code. When the platform denies a transaction, it returns the response code that provides the precise reason for the denial by the card network.<br> | minLength: 2; maxLength: 2; example: "57" |
| `custom_code` | string (schema `CustomCode`) | no | Alphanumeric three-character custom code. This can be an alternative custom code. When the platform denies a control evaluation, it returns the custom code that provides the precise reason for the denial by the anti-fraud solution.<br> | minLength: 1; maxLength: 3; example: "A1B" |
| `evaluation_order` | integer (schema `EvaluationOrder`) | no | Order in which the control is evaluated. If this value is not provided, the control is evaluated after the controls with the configured `evaluation_order` value.<br> | format: "int64"; minimum: 1; maximum: 99 |
| `card_mode` | string (schema `CardMode`) | no | Specifies the operational mode of the card.<br> | enum: ["credit", "debit"]; example: "credit" |
| `customized` | boolean (schema `Customized`) | no | Indicates whether the flex control is updated at the account level or customer level (`true`) or managed at the program level (`false`).<br><br>To revert a customized flex control back to program-level management, call [Update account flex control](ref:patch-v1-accounts-flex-control) or [Update customer flex control](ref:patch-v1-customers-flex-control) and set `customized` as `false`.<br> | example: true |

200 Example `simple customer flex control` — from `#/components/examples/customerFlexControlResponse`:

```json
{
  "id": "84ba9052-31d3-41da-99d2-a1632d5ce2e5",
  "type": "spending_limit",
  "rule_reference_id": "purchase-1M",
  "account_id": 50000001,
  "customer_id": 9999999,
  "name": "Purchase 1 Month credit card",
  "max_limit": 49999,
  "limit_duration": "P1M",
  "available_limit": 49999,
  "card_ids": [
    111111
  ],
  "conditions": [
    {
      "attribute": "balance",
      "operator": "gt",
      "value": "10000"
    }
  ],
  "active": true,
  "customized": true
}
```

##### Response 400

400 Example `Invalid request` — from `#/components/examples/ERUL1301`:

```json
{
  "message": "Invalid request",
  "error_code": "RULVAL0400",
  "details": [
    {
      "location": "payload.limit_duration",
      "message": "`limit_duration` must follow ISO 8601 standard"
    }
  ],
  "code": "ERUL1301"
}
```

400 Example `Error validating request payload to GetCustomerSpendingLimitRule` — from `#/components/examples/ERUL1302`:

```json
{
  "message": "Error validating request payload to GetCustomerSpendingLimitRule",
  "error_code": "RULVAL0400",
  "details": [
    {
      "location": "payload.limit_duration",
      "message": "`limit_duration` must follow ISO 8601 standard"
    }
  ],
  "code": "ERUL1302"
}
```

##### Response 403

403 Example `Operation not allowed` — from `#/components/examples/ERUL0002`:

```json
{
  "message": "operation not allowed",
  "error_code": "RULVAL0403",
  "code": "ERUL0002"
}
```

##### Response 404

404 Example `Rules for customerID not found` — from `#/components/examples/ERUL1204`:

```json
{
  "message": "Rules for customerID not found",
  "error_code": "RULREP0404",
  "code": "ERUL1204"
}
```

404 Example `Customer spending limit rules not found` — from `#/components/examples/ERUL1205`:

```json
{
  "message": "Customer spending limit rules not found.",
  "error_code": "RULVAL0400",
  "code": "ERUL1205"
}
```

##### Response 500

500 Example `Error on repository` — from `#/components/examples/ERUL1203`:

```json
{
  "message": "Error on repository",
  "error_code": "RULREP0500",
  "code": "ERUL1203"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERUL1301` | Invalid request |
| 400 | `RULVAL0400` | Invalid request |
| 400 | `ERUL1302` | Error validating request payload to GetCustomerSpendingLimitRule |
| 403 | `ERUL0002` | operation not allowed |
| 403 | `RULVAL0403` | operation not allowed |
| 404 | `ERUL1204` | Rules for customerID not found |
| 404 | `RULREP0404` | Rules for customerID not found |
| 404 | `ERUL1205` | Customer spending limit rules not found. |
| 404 | `RULVAL0400` | Customer spending limit rules not found. |
| 500 | `ERUL1203` | Error on repository |
| 500 | `RULREP0500` | Error on repository |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

<!-- op: spec=api-specs/Core_platform_-_Flex_controls.yaml method=PATCH path=/v1/customers/{customerId}/flex-controls/{flexControlId} operationId=patch-v1-customers-flex-control -->
### `PATCH /v1/customers/{customerId}/flex-controls/{flexControlId}` — Update customer flex control

- **operationId:** `patch-v1-customers-flex-control`
- **Specification:** `api-specs/Core_platform_-_Flex_controls.yaml` (Core platform - Flex controls)
- **Server base URL(s):** `https://sandbox.pismolabs.io/rules`
- **Tags:** `Customer flex controls`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update a customer flex control. If you want to disable any flex control at the program level, you need to submit a request to the Pismo support team to change the active status parameter to false.
>
> This endpoint generates a [Customer flex control updated](https://developers.pismo.io/events/docs/audit-customer-spending-limit-updated-1) event.
>
> NOTE: This endpoint requires an account-specific access token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `customerId` | path | yes | number | Customer ID | example: 9999999 |
| `flexControlId` | path | yes | string | Flex control ID | example: "84ba9052-31d3-41da-99d2-a1632d5ce2e5" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `PatchCustomerFlexControlRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `Name`) | no | Flex control name | example: "Purchase 1M limit" |
| `beneficiary_id` | string (schema `BeneficiaryId`) | no | Account beneficiary ID | example: "8497225d-2096-4b92-990e-f73bd21bc48c" |
| `override_controls` | array of string (schema `OverrideControls`) | no | List of existing flex control IDs to override.<br>The platform ignores these controls for the beneficiary identified by `beneficiary_id` and only evaluates the new flex control.<br> | example: ["spending-limit-id-1", "spending-limit-id-2"] |
| `processing_codes` | array of string (schema `ProcessingCodes`) | no | Processing codes list for evaluating flex control conditions. If the value is empty, the flex control applies to any processing code.<br> | example: ["07000", "07001"] |
| `currency_code` | string (schema `CurrencyCode`) | no | Flex control currency code (ISO 4217). Defines the precision used for monetary values such as `max_limit`, `available_limit`, and `condition.value`.<br> | example: "BRL" |
| `max_limit` | integer (schema `MaxLimit`) | no | Defines the maximum limit for the control. Its meaning depends on the flex control `type`.<br>  * For `spending_limit` controls, `max_limit` represents the maximum spending amount allowed.<br>  * For `usage_limit` controls, `max_limit` represents the maximum number of transactions allowed.<br><br>Once met or exceeded, any subsequent transactions are declined by evaluation control flow.<br><br>For spending limits, note that this value is an integer. Since global currencies vary in the number of digits that are allowed after the decimal point, you must convert the actual maximum spending limit into an integer value to use in this field. To do this, use the following formula.<br><br>value = floatNumber × 10^X, where X is the number of digits after the decimal separator for the currency as defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for BRL currency transactions, where the number of decimal places is 2, you must set it to `49999` (499.99 × 10²).<br><br>If you want to set the value 499 for JPY currency transactions, where the number of decimal places is 0, you must set it to `4999` (4999.0 × 10^0 = 4999.0 × 1 - in other words, the value doesn't change.)<br><br>This field is **REQUIRED** for flex controls with the `type` of `spending_limit` and `usage_limit`, and it does not apply to flex controls with the `type` of `restriction` and `cumulative_limit`.<br> | format: "int64"; minimum: 1; example: 1000 |
| `max_transactions` | integer (schema `MaxTransactions`) | no | Maximum number of transactions allowed. Once met or exceeded, subsequent transactions are declined by the evaluation control flow. Valid only for flex controls with the `type` of `cumulative_limit`.<br> | format: "int64"; minimum: 1; example: 10 |
| `max_amount` | integer (schema `MaxAmount`) | no | Maximum accumulated amount allowed. Once met or exceeded, subsequent transactions are declined by the evaluation control flow. Valid only for flex controls with the `type` of `cumulative_limit`.<br>Note that the value must be calculated as follows.<br><br>value = floatNumber × 10^X, where X is the number of digits after the decimal separator for the currency defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for USD currency transactions, where the number of decimal places is 2, you must set the value to `49999` (499.99 × 10²).<br><br>If you want to set the value 499 for JPY currency transactions, where the number of decimal places is 0, you must set the value to `499` (499.0 × 10^0 = 499.0 × 1 - in other words, the value doesn't change).<br> | format: "int64"; minimum: 1; example: 100000 |
| `limit_duration` | string (schema `LimitDuration`) | no | Flex control limit period duration (ISO 8601 format).<br>For example, if a flex control sets a spending limit of $500, and `limit_duration` is set to one month (`P1M`), then the user cannot spend more than $500 from the account in any one month period.<br> | example: "P1M" |
| `reset_period` | object (schema `ResetPeriod`) | no | Enables the specification of reset periods for accumulators based on the duration in `limit_duration`. When this field is set, it must follow the RFC 3339 pattern from ISO 8601. When `reset_period` changes, the `avaliable_limit` is reset.<br> |  |
| `reset_strategy` | object (schema `ResetStrategy`) | no | The strategy to reset the accumulators. Valid only for flex controls with the `type` of `cumulative_limit`. |  |
| `time_zone` | string (schema `TimeZone`) | no | IANA Time Zone database, such as "America/New_York".<br>This attribute is used to evaluate the flex control using the desired time zone for condition attributes such as `week_day`, `month_day`, `time_now`, and `reset_period`.<br>If `time_zone` is empty, the control is evaluated using the UTC time zone.<br> | example: "America/Sao_Paulo" |
| `available_limit` | integer (schema `AvailableLimit`) | no | Represents the remaining limit for the flex control. Its meaning depends on the flex control `type`.<br>  * For `spending_limit` controls, `available_limit` is the remaining spending amount.<br>  * For `usage_limit` controls, `available_limit` is the remaining number of transactions allowed.<br><br>The `available_limit` is calculated by: `max_limit` - `current_spend_limit`. The `current_spend_limit`, an internal field, is the total amount of all approved transactions in the `limit_duration` period. It is reset by the evaluation flow when a new transaction is evaluated in the new period according to the `reset_period`.<br><br>When `available_limit` is set in a PATCH request via [Update account flex control](ref:patch-v1-accounts-flex-control) or [Update customer flex control](ref:patch-v1-customers-flex-control), it resets `current_spend_limit`. In this case, `available_limit` cannot be greater than `max_limit`.<br><br>For spending limits, note that `available_limit` is an integer. Since global currencies vary in the number of digits that are allowed after the decimal point, you must convert the actual maximum spending limit into an integer value to use in this field. To do this, use the following formula:<br><br>value = floatNumber * 10^x,<br>where x is the number of digits for the currency as defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for BRL currency transactions, you must set 49999 = 499.99 * 10^2.<br><br>On the other hand, the Japanese money system doesn't use fractions of a yen (the Japanese currency). So, to set the value at 4999 yen, you must set 4999 = 4999.0 * 10^0 = 4999.0 * 1. (In other words, the value doesn't change.)<br> | format: "int64"; example: 300 |
| `conditions` | array of object (schema `Condition`) | no |  |  |
| `active` | boolean (schema `Active`) | no | If not specified, defaults to 'true'. If set to 'false', the flex control is skipped during evaluation. | default: true; example: true |
| `deny_code` | string (schema `DenyCode`) | no | Deny code related to restriction.<br>This code is returned when the evaluation does not meet the conditions.<br> | example: "ERR_VAL_BALANCE" |
| `card_ids` | array of integer | no | Card ID list | items.format: "int64" |
| `response_code` | string (schema `ResponseCode`) | no | Alphanumeric two-character response code. This can be the standard card network response code. When the platform denies a transaction, it returns the response code that provides the precise reason for the denial by the card network.<br> | minLength: 2; maxLength: 2; example: "57" |
| `custom_code` | string (schema `CustomCode`) | no | Alphanumeric three-character custom code. This can be an alternative custom code. When the platform denies a control evaluation, it returns the custom code that provides the precise reason for the denial by the anti-fraud solution.<br> | minLength: 1; maxLength: 3; example: "A1B" |
| `evaluation_order` | integer (schema `EvaluationOrder`) | no | Order in which the control is evaluated. If this value is not provided, the control is evaluated after the controls with the configured `evaluation_order` value.<br> | format: "int64"; minimum: 1; maximum: 99 |
| `card_mode` | string (schema `CardMode`) | no | Specifies the operational mode of the card.<br> | enum: ["credit", "debit"]; example: "credit" |

Example `PatchCustomerFlexControlRequest` — from `#/components/examples/PatchCustomerFlexControlRequest`:

```json
{
  "name": "Purchase 1 Month credit card",
  "max_limit": 49999,
  "limit_duration": "P1M",
  "available_limit": 5000,
  "conditions": [
    {
      "attribute": "balance",
      "operator": "gt",
      "value": "10000"
    }
  ],
  "active": true,
  "deny_code": "ERR_VAL_BALANCE",
  "card_ids": [
    11111,
    22222
  ]
}
```

Example `patchOnlyMaxLimitCustomerFlexControlRequest` — from `#/components/examples/patchOnlyMaxLimitCustomerFlexControlRequest`:

```json
{
  "max_limit": 49999
}
```

Example `PatchCustomerFlexControlRequestInactive` — from `#/components/examples/PatchCustomerFlexControlRequestInactive`:

```json
{
  "active": false
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK. Successful spending limit patch. | `application/json`: object (schema `CustomerFlexControlsResponse`) |
| 400 | Bad request. Validation error on request. | `application/json`: object (schema `ErrorResponseWithDetails`) |
| 403 | Forbidden. Authorization error on request. | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found. Rules for customerID not found. | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error. | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | yes | Flex control ID is auto-generated at creation time.<br> | format: "uuid"; example: "89cbdadc-860b-4275-a5cd-d9d892fd3869" |
| `type` | string (schema `CustomerType`) | yes | Flex control scope<br>  * `usage_limit`: Cumulative flex control that increases by one until `max_limit`<br>  * `spending_limit`: Cumulative flex control that increases by the current transaction's `amount` until `max_limit`<br>  * `cumulative_limit`: Cumulative flex control that increases by one transaction or by transaction amount until a condition is met, applies only to flex controls with associated `card_ids`, and requires a `reset_strategy`<br>  * `restriction`: Restriction flex control that only validates specified conditions<br> | enum: ["spending_limit", "usage_limit", "restriction", "cumulative_limit"] |
| `processing_codes` | array of string (schema `ProcessingCodes`) | no | Processing codes list for evaluating flex control conditions. If the value is empty, the flex control applies to any processing code.<br> | example: ["07000", "07001"] |
| `rule_reference_id` | string | no | ID of program-level flex control. Only present in generic flex controls created for the entire program. | example: "purchase-1M" |
| `name` | string (schema `Name`) | no | Flex control name | example: "Purchase 1M limit" |
| `account_id` | integer | yes | Account ID | format: "int64"; example: 8988000 |
| `customer_id` | integer | no | Customer ID | format: "int64"; example: 99999999 |
| `card_ids` | array of number | no | Card ID list | example: [11111, 22222]; items.format: "int64" |
| `currency_code` | string (schema `CurrencyCode`) | no | Flex control currency code (ISO 4217). Defines the precision used for monetary values such as `max_limit`, `available_limit`, and `condition.value`.<br> | example: "BRL" |
| `max_limit` | integer (schema `MaxLimit`) | no | Defines the maximum limit for the control. Its meaning depends on the flex control `type`.<br>  * For `spending_limit` controls, `max_limit` represents the maximum spending amount allowed.<br>  * For `usage_limit` controls, `max_limit` represents the maximum number of transactions allowed.<br><br>Once met or exceeded, any subsequent transactions are declined by evaluation control flow.<br><br>For spending limits, note that this value is an integer. Since global currencies vary in the number of digits that are allowed after the decimal point, you must convert the actual maximum spending limit into an integer value to use in this field. To do this, use the following formula.<br><br>value = floatNumber × 10^X, where X is the number of digits after the decimal separator for the currency as defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for BRL currency transactions, where the number of decimal places is 2, you must set it to `49999` (499.99 × 10²).<br><br>If you want to set the value 499 for JPY currency transactions, where the number of decimal places is 0, you must set it to `4999` (4999.0 × 10^0 = 4999.0 × 1 - in other words, the value doesn't change.)<br><br>This field is **REQUIRED** for flex controls with the `type` of `spending_limit` and `usage_limit`, and it does not apply to flex controls with the `type` of `restriction` and `cumulative_limit`.<br> | format: "int64"; minimum: 1; example: 1000 |
| `max_transactions` | integer (schema `MaxTransactions`) | no | Maximum number of transactions allowed. Once met or exceeded, subsequent transactions are declined by the evaluation control flow. Valid only for flex controls with the `type` of `cumulative_limit`.<br> | format: "int64"; minimum: 1; example: 10 |
| `max_amount` | integer (schema `MaxAmount`) | no | Maximum accumulated amount allowed. Once met or exceeded, subsequent transactions are declined by the evaluation control flow. Valid only for flex controls with the `type` of `cumulative_limit`.<br>Note that the value must be calculated as follows.<br><br>value = floatNumber × 10^X, where X is the number of digits after the decimal separator for the currency defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for USD currency transactions, where the number of decimal places is 2, you must set the value to `49999` (499.99 × 10²).<br><br>If you want to set the value 499 for JPY currency transactions, where the number of decimal places is 0, you must set the value to `499` (499.0 × 10^0 = 499.0 × 1 - in other words, the value doesn't change).<br> | format: "int64"; minimum: 1; example: 100000 |
| `available_amount` | integer (schema `AvailableAmount`) | no | The remaining amount allowed for authorizations under the current flex control. This value decreases with each successful authorization and resets based on the defined reset strategy. Valid only for flex controls with the `type` of `cumulative_limit`.<br> | format: "int64"; example: 100000 |
| `available_transactions` | integer (schema `AvailableTransactions`) | no | The remaining number of transactions allowed for authorizations under the current flex control. This value decreases with each successful authorization and resets based on the defined reset strategy. Valid only for flex controls with the `type` of `cumulative_limit`.<br> | format: "int64"; example: 10 |
| `limit_duration` | string (schema `LimitDuration`) | no | Flex control limit period duration (ISO 8601 format).<br>For example, if a flex control sets a spending limit of $500, and `limit_duration` is set to one month (`P1M`), then the user cannot spend more than $500 from the account in any one month period.<br> | example: "P1M" |
| `reset_datetime` | string (schema `ResetDatetime`) | no | The exact date and time of the next reset for the flex control's spending window, in RFC-3339 format. This value is response-only: it is calculated by the platform and is never accepted in requests.<br><br>When `reset_period` is defined, the reset follows the configured schedule (for example, `month_day: 10` resets on the 10th day of every month). When `reset_period` is omitted, the reset occurs at the control's creation date and time plus `limit_duration`.<br><br>This value is recalculated whenever an authorization is evaluated. If no authorizations have been processed since the last reset, it may still point to a reset datetime that has already passed.<br><br>This field is returned only for flex controls with the `type` of `spending_limit` or `usage_limit`.<br> | format: "date-time"; example: "2022-03-08T21:19:55Z" |
| `time_zone` | string (schema `TimeZone`) | no | IANA Time Zone database, such as "America/New_York".<br>This attribute is used to evaluate the flex control using the desired time zone for condition attributes such as `week_day`, `month_day`, `time_now`, and `reset_period`.<br>If `time_zone` is empty, the control is evaluated using the UTC time zone.<br> | example: "America/Sao_Paulo" |
| `reset_period` | object (schema `ResetPeriod`) | no | Enables the specification of reset periods for accumulators based on the duration in `limit_duration`. When this field is set, it must follow the RFC 3339 pattern from ISO 8601. When `reset_period` changes, the `avaliable_limit` is reset.<br> |  |
| `reset_strategy` | object (schema `ResetStrategy`) | no | The strategy to reset the accumulators. Valid only for flex controls with the `type` of `cumulative_limit`. |  |
| `available_limit` | integer (schema `AvailableLimit`) | no | Represents the remaining limit for the flex control. Its meaning depends on the flex control `type`.<br>  * For `spending_limit` controls, `available_limit` is the remaining spending amount.<br>  * For `usage_limit` controls, `available_limit` is the remaining number of transactions allowed.<br><br>The `available_limit` is calculated by: `max_limit` - `current_spend_limit`. The `current_spend_limit`, an internal field, is the total amount of all approved transactions in the `limit_duration` period. It is reset by the evaluation flow when a new transaction is evaluated in the new period according to the `reset_period`.<br><br>When `available_limit` is set in a PATCH request via [Update account flex control](ref:patch-v1-accounts-flex-control) or [Update customer flex control](ref:patch-v1-customers-flex-control), it resets `current_spend_limit`. In this case, `available_limit` cannot be greater than `max_limit`.<br><br>For spending limits, note that `available_limit` is an integer. Since global currencies vary in the number of digits that are allowed after the decimal point, you must convert the actual maximum spending limit into an integer value to use in this field. To do this, use the following formula:<br><br>value = floatNumber * 10^x,<br>where x is the number of digits for the currency as defined in ISO 4217.<br><br>For example, if you want to set the value 499.99 for BRL currency transactions, you must set 49999 = 499.99 * 10^2.<br><br>On the other hand, the Japanese money system doesn't use fractions of a yen (the Japanese currency). So, to set the value at 4999 yen, you must set 4999 = 4999.0 * 10^0 = 4999.0 * 1. (In other words, the value doesn't change.)<br> | format: "int64"; example: 300 |
| `conditions` | array of object (schema `Condition`) | no |  | example: [{"attribute": "balance", "operator": "gt", "value": "10000"}] |
| `active` | boolean (schema `Active`) | no | If not specified, defaults to 'true'. If set to 'false', the flex control is skipped during evaluation. | default: true; example: true |
| `deny_code` | string (schema `DenyCode`) | no | Deny code related to restriction.<br>This code is returned when the evaluation does not meet the conditions.<br> | example: "ERR_VAL_BALANCE" |
| `response_code` | string (schema `ResponseCode`) | no | Alphanumeric two-character response code. This can be the standard card network response code. When the platform denies a transaction, it returns the response code that provides the precise reason for the denial by the card network.<br> | minLength: 2; maxLength: 2; example: "57" |
| `custom_code` | string (schema `CustomCode`) | no | Alphanumeric three-character custom code. This can be an alternative custom code. When the platform denies a control evaluation, it returns the custom code that provides the precise reason for the denial by the anti-fraud solution.<br> | minLength: 1; maxLength: 3; example: "A1B" |
| `evaluation_order` | integer (schema `EvaluationOrder`) | no | Order in which the control is evaluated. If this value is not provided, the control is evaluated after the controls with the configured `evaluation_order` value.<br> | format: "int64"; minimum: 1; maximum: 99 |
| `card_mode` | string (schema `CardMode`) | no | Specifies the operational mode of the card.<br> | enum: ["credit", "debit"]; example: "credit" |
| `customized` | boolean (schema `Customized`) | no | Indicates whether the flex control is updated at the account level or customer level (`true`) or managed at the program level (`false`).<br><br>To revert a customized flex control back to program-level management, call [Update account flex control](ref:patch-v1-accounts-flex-control) or [Update customer flex control](ref:patch-v1-customers-flex-control) and set `customized` as `false`.<br> | example: true |

200 Example `simple customer flex control` — from `#/components/examples/customerFlexControlResponse`:

```json
{
  "id": "84ba9052-31d3-41da-99d2-a1632d5ce2e5",
  "type": "spending_limit",
  "rule_reference_id": "purchase-1M",
  "account_id": 50000001,
  "customer_id": 9999999,
  "name": "Purchase 1 Month credit card",
  "max_limit": 49999,
  "limit_duration": "P1M",
  "available_limit": 49999,
  "card_ids": [
    111111
  ],
  "conditions": [
    {
      "attribute": "balance",
      "operator": "gt",
      "value": "10000"
    }
  ],
  "active": true,
  "customized": true
}
```

##### Response 400

400 Example `Invalid request` — from `#/components/examples/ERUL1401`:

```json
{
  "message": "Invalid request",
  "error_code": "RULVAL0400",
  "details": [
    {
      "location": "payload.limit_duration",
      "message": "`limit_duration` must follow ISO 8601 standard"
    }
  ],
  "code": "ERUL1401"
}
```

400 Example `Error parsing payload` — from `#/components/examples/ERUL1402`:

```json
{
  "message": "Error parsing payload.",
  "error_code": "RULVAL0400",
  "code": "ERUL1402"
}
```

400 Example `Error validating request payload to PatchCustomerSpendingLimitRule` — from `#/components/examples/ERUL1403`:

```json
{
  "message": "Error validating request payload to PatchCustomerSpendingLimitRule",
  "error_code": "RULVAL0400",
  "details": [
    {
      "location": "payload.limit_duration",
      "message": "`limit_duration` must follow ISO 8601 standard"
    }
  ],
  "code": "ERUL1403"
}
```

400 Example `Error building new spending limit from request payload` — from `#/components/examples/ERUL1406`:

```json
{
  "message": "Error building new spending limit from request payload",
  "error_code": "RULVAL0400",
  "details": [
    {
      "location": "payload.restriction_rules[].conditions[].attribute",
      "message": "attribute should be one of (balance, amount, merchant_category_code, week_day, month_day, entry_mode, merchant_id)"
    }
  ],
  "code": "ERUL1406"
}
```

##### Response 403

403 Example `Operation not allowed` — from `#/components/examples/ERUL0002`:

```json
{
  "message": "operation not allowed",
  "error_code": "RULVAL0403",
  "code": "ERUL0002"
}
```

##### Response 404

404 Example `Rules for customerID not found` — from `#/components/examples/ERUL1204`:

```json
{
  "message": "Rules for customerID not found",
  "error_code": "RULREP0404",
  "code": "ERUL1204"
}
```

404 Example `Customer spending limit rules not found` — from `#/components/examples/ERUL1205`:

```json
{
  "message": "Customer spending limit rules not found.",
  "error_code": "RULVAL0400",
  "code": "ERUL1205"
}
```

##### Response 500

500 Example `Error on repository` — from `#/components/examples/ERUL1203`:

```json
{
  "message": "Error on repository",
  "error_code": "RULREP0500",
  "code": "ERUL1203"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `ERUL1401` | Invalid request |
| 400 | `RULVAL0400` | Invalid request |
| 400 | `ERUL1402` | Error parsing payload. |
| 400 | `ERUL1403` | Error validating request payload to PatchCustomerSpendingLimitRule |
| 400 | `ERUL1406` | Error building new spending limit from request payload |
| 403 | `ERUL0002` | operation not allowed |
| 403 | `RULVAL0403` | operation not allowed |
| 404 | `ERUL1204` | Rules for customerID not found |
| 404 | `RULREP0404` | Rules for customerID not found |
| 404 | `ERUL1205` | Customer spending limit rules not found. |
| 404 | `RULVAL0400` | Customer spending limit rules not found. |
| 500 | `ERUL1203` | Error on repository |
| 500 | `RULREP0500` | Error on repository |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `audit-customer-spending-limit-updated-1` | https://developers.pismo.io/events/docs/audit-customer-spending-limit-updated-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;403;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`, `KU-EVT-flex-controls-data-events`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ResetPeriod -->
### Schema `ResetPeriod`

Pointer: `#/components/schemas/ResetPeriod`. Type: object (schema `ResetPeriod`).

> Enables the specification of reset periods for accumulators based on the duration in `limit_duration`. When this field is set, it must follow the RFC 3339 pattern from ISO 8601. When `reset_period` changes, the `avaliable_limit` is reset.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `month_day` | number | no | Month day to reset. Can only be used when `limit_duration` is monthly or yearly (in the yearly case, it must be combined with the `month` parameter). | minimum: 1; maximum: 28 |
| `month` | number | no | Numeric day of the month to reset the flex control. Can only be used when `limit_duration` is yearly. | minimum: 1; maximum: 12 |
| `week_day` | string | no | Week day to reset. Can only be used when `limit_duration` is weekly. | enum: ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]; example: "monday" |
| `time` | string | no | Time to reset flex control in time zone defined by control. Include only hours, minutes, and AM/PM. For example, `11:00PM` for 11PM or `00:00AM` for midnight. You can use `12` in hours as an alternative to `00` (for example,`12:59AM` is the same as `00:59AM`).<br> | example: "3:00AM" |
| `utc_time` | string | no | *Note: This field has been deprecated, use `time` instead.*<br>Time to reset the flex control in the UTC 0 time. Include only hours, minutes, and AM/PM. For example, `11:00PM` for 11PM or `00:00AM` for midnight. You can use `12` in hours as an alternative to `00` (for example,`12:59AM` is the same as `00:59AM`).<br> | deprecated: true; example: "3:00AM" |

<!-- schema: #/components/schemas/ResetStrategy -->
### Schema `ResetStrategy`

Pointer: `#/components/schemas/ResetStrategy`. Type: object (schema `ResetStrategy`).

> The strategy to reset the accumulators. Valid only for flex controls with the `type` of `cumulative_limit`.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reset_trigger` | object | no | Trigger that resets the accumulators |  |
| `reset_trigger.is_password_present` | boolean | no | Indicates whether the client entered a password.<br><br>When the cardholder completes an authorization, the control accumulators for transactions and/or amount are reset if the transaction's `is_password_present` matches the configured trigger value.<br> |  |
| `reset_trigger.is_pin_validated_offline` | boolean | no | Indicates whether the pin was validated offline, triggering a reset of the accumulator when true |  |
| `reset_trigger.authentication_method` | array of string | no | Indicates which authentication methods should trigger a reset of the flex-control accumulator. | example: ["05"]; items.format: "text" |

<!-- schema: #/components/schemas/Condition -->
### Schema `Condition`

Pointer: `#/components/schemas/Condition`. Type: object (schema `Condition`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string | no | Condition ID | format: "uuid"; example: "b4930a4d-e2c4-4fdc-9803-c83dec3a30d1" |
| `attribute` | string | yes | Attribute to evaluate in the condition.<br>* `amount`: Numeric value that indicates the amount of the operation performed by the user<br>* `balance`: Maximum balance amount allowed in an account. Due to fiscal restrictions in some countries, the user cannot have more than a certain amount in the account. When the balance value is defined, the control validates any process of entering money into that account, evaluates the account balance at the time of the transaction, and denies any inflow of money above the amount defined in the balance value.<br>* `country_code`: Three-letter country code (ISO 3166-1) indicating the location where the transaction is initiated or processed.<br>* `entry_mode`: A code used to establish the mode of purchase. Valid only for card network operations. For a control to be valid, it must be a code defined by the entire Field 22 (Visa) or DE 22 (Mastercard) or as specified by each card network.<br>    * Visa: Field 22 contains a 4-digit code indicating the method used to enter the account number and card expiration date (positions 1 and 2) and, if an electronic terminal is used, the capability of the terminal to capture online PINs (position 3) and the last digit (position 4) equal to 0 (unused) for transactions processed through VisaNet. This field is fixed-length with three subfields.<br>    * Mastercard: DE 22 contains a 3-digit code indicating the method used to enter the account number and card expiration date (positions 1 and 2) and, if an electronic terminal is used, the capability of the terminal to capture online PINs (position 3).<br>* `is_device_registered`: Boolean that indicates whether the device used for the operation is registered according to the financial institution's security policies.<br>* `is_password_present`: Boolean that indicates whether a valid password is present in the evaluation request. Valid only for card network operations.<br>* `is_pin_validated_offline`: Boolean that indicates whether the pin was validated offline in the evaluation request. This is commonly used for offline PIN verification scenarios. Valid only for card network operations.<br>* `is_physical_card_present`: Boolean that indicates whether a physical card is present in the evaluation request. Valid only for card network operations. Digital wallet transactions are treated as physical card transactions. To exclude digital wallet transactions, combine this condition with `is_token_present` as `true`.<br>* `is_tra_exemption_requested`: Boolean that indicates whether a TRA (Transaction Risk Assessment) exemption is requested for the transaction. Valid only for card network operations.<br>* `merchant_category_code`: Merchant Category Code (MCC) is a four-digit number used to describe a merchant's primary business activities. Valid only for card network operations. For a control to be valid, you must enter a code specified by the Mastercard/Visa card network.<br>* `merchant_id`: Merchant ID. Valid only for card network operations. For a control to be valid, you must enter a code specified by the Mastercard/Visa card network.<br>* `month_day`: Day of the month when the operation is performed. Commonly used to limit operations on holidays. The format is MMM-DD. For example, enter January 25 as "JAN-25".<br>* `number_of_installments`: Number of installments in the operation<br>* `time_now`: Restriction window used to establish the time when the operation is performed, defined in the Coordinated Universal Time (UTC 0) zone. For example, a 10:59 PM-06:59 AM window specifies restrictions that apply from 11 PM to 7 AM in the UTC 0 time.<br>* `week_day`: Day of the week when the operation occurs. Use the full lowercase weekday name. Valid values: sunday, monday, tuesday, wednesday, thursday, friday, saturday.<br>* `authentication_method`:  Determine whether restrictions should be applied for specific authentication methods. For a control to be valid, it must be a code defined by the Field 60.8/Positions 9-10 for Visa operations or as specified by each card network. Valid only for card network operations.<br>* `is_token_present`: Boolean that indicates whether a token card is present in the evaluation request. Valid only for card network operations.<br>* `initiation_mode`: Payment initiation mode. Valid only for card network operations.<br>   - `moto`: Payments made through mail order or telephone.<br>   - `mit`: Merchant-initiated transactions.<br>* `acquirer_country_code`: Three-letter country code (ISO 3166-1) representing the location of the acquiring bank or financial institution. Valid only for card network operations.<br>* `is_cavv_present`: Boolean indicating that the CAVV field is present. CAVV stands for cardholder authentication verification value. Valid only for card network operations.<br>* `avr`: String indicating that the transaction is a card network Account Verification Request (AVR) transaction. AVR transactions differ from standard authorizations in that they are typically zero-value and are used for card network verification flows. Currently, the only supported value for this attribute is `mtt`, which is the Mobility & Transport Transaction (MTT) type.<br>* `operation_type`: Type of operation being performed. Allowed values are:<br>  - `debit` - debit transaction<br>  - `credit` - credit transaction<br>  - `none` -  transaction that doesn't have a financial impact on the account balance, even though an authorization event occurs. These transactions still exist in the authorization flow, but they don't generate balance movement. AVR (Account Verification Request) is one example of this type of transaction with a zero‑amount authorization.<br> | enum: ["balance", "amount", "merchant_category_code", "week_day", "month_day", "time_now", "entry_mode", "merchant_id", "country_code", "number_of_installments", "is_physical_card_present", "is_device_registered", "is_tra_exemption_requested", "is_pin_validated_offline", "authentication_method", "is_token_present", "initiation_mode", "acquirer_country_code", "is_cavv_present", "avr", "operation_type"] |
| `operator` | string | yes | Condition type evaluation<br>* eq - equal to value<br>* neq - not equal to value<br>* lt - lower than value<br>* lte - lower than or equal to value<br>* gt - greater than value<br>* gte - greater than or equal to value<br>* in - includes value<br>* nin - does not include value<br>* bt - between two values<br>* in_group - in attribute group<br>* not_in_group - not in attribute group<br> | enum: ["eq", "neq", "lt", "lte", "gt", "gte", "in", "nin", "bt", "in_group", "not_in_group"] |
| `value` | string | yes | Value to compare | example: "10000" |

<!-- schema: #/components/schemas/ErrorResponseWithDetails -->
### Schema `ErrorResponseWithDetails`

Pointer: `#/components/schemas/ErrorResponseWithDetails`. Type: object (schema `ErrorResponseWithDetails`).

> Error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Error description |  |
| `details` | array of object (schema `ErrorDetail`) | no | Provides more information about the error message. |  |
| `error_code` | string | no | Error code ID | deprecated: true |
| `code` | string | no | Error code ID |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Error description |  |
| `error_code` | string | no | Error code ID | deprecated: true |
| `code` | string | no | Error code ID |  |

<!-- schema: #/components/schemas/ErrorDetail -->
### Schema `ErrorDetail`

Pointer: `#/components/schemas/ErrorDetail`. Type: object (schema `ErrorDetail`).

> Error detail.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `location` | string | no | Identifies where the request is causing an error. | example: "payload.entity_type" |
| `message` | string | no | Description of error | example: "`entity_type` should be `legal_person` or `natural_person`" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Flex_controls.yaml` | tag `Customer flex controls`: GET /v1/customers/{customerId}/flex-controls/{flexControlId}, PATCH /v1/customers/{customerId}/flex-controls/{flexControlId} | https://github.com/PismoDevEx/pismo-api-specs | `af34d94f331c9b17…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-ERR-codes-erul` — Error codes: ERUL
- `KU-EVT-catalogue-audit` — Event catalogue: audit
- `KU-EVT-flex-controls-data-events` — Core platform - Flex controls
