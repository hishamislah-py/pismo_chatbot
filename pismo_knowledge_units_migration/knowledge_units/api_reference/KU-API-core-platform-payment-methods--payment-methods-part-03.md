---
ku_id: KU-API-core-platform-payment-methods--payment-methods-part-03
title: 'API reference: Core platform - Payment methods — Payment methods (part 3 of 3)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Payment_methods.yaml
  sha256: 9b02c87b6e39a1c803b8361362aa5beb50c098580d9549c8f58475df0d91a80e
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
- post-transfers-confirm
related_kus:
- KU-ERR-codes-acq-to-esma
- KU-EVT-catalogue-other-domains
- KU-PAY-payment-methods
specification_version: 1.0.0
---

# API reference: Core platform - Payment methods — Payment methods (part 3 of 3)

**KU ID:** `KU-API-core-platform-payment-methods--payment-methods-part-03` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Payment methods` in `api-specs/Core_platform_-_Payment_methods.yaml` (“Core platform - Payment methods”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage cash-in and cash-out payments and P2P transfers.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /payment-methods/v2/transfers/confirm` | `post-transfers-confirm` | Confirm pre-authorized transfer | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payment-methods/v2/transfers/confirm operationId=post-transfers-confirm -->
### `POST /payment-methods/v2/transfers/confirm` — Confirm pre-authorized transfer

- **operationId:** `post-transfers-confirm`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment methods`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Confirm a pre-authorized transfer operation. Use this endpoint only if the created transfer operation had the `pre_authorization` set to `true`. 
>
> In the request, provide a new `tracking_id` for the confirmation operation and the `original_tracking_id` of the original transfer operation. If you don't provide the `amount`, the platform confirms the total original amount. You can also provide the `amount` to confirm a total, partial, or greater amount.
>
> Refer to the [Payment methods](doc:payment-methods) guide for additional information.
>
> This endpoint generates a [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PaymentsConfirmRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `original_tracking_id` | string (schema `OriginalTrackingID`) | yes | Tracking ID for the original operation. | minLength: 36; maxLength: 50; example: "249fbd1c-cfcd-48aa-8bcb-1ffe3a5f7978" |
| `amount` | number (schema `Amount`) | no | Credit or debit amount. | format: "float"; example: 100.23 |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing authorization with the corresponding `tracking_id` returned. | `application/json`: object (schema `TransfersResponse`) |
| 202 | Request was accepted and will be processed asynchronously. The response body is empty (`{}`).<br>The confirmation outcome (`authorization_id`, `tracking_id`, `account_id`, `response_code`,<br>`denial_code`) is not returned on this response — it is delivered through the *Platform<br>authorization created* event (category `CONFIRMATION`). A populated body is only returned on<br>the `200` idempotent-replay response.<br> | `application/json`: object (schema `PaymentsConfirmResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Access token is missing or invalid. | `application/json`: object (schema `404Transfers`) |
| 409 | Conflict | `application/json`: object (schema `409Transfers`) |
| 422 | Unprocessable request | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | no | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `response_code` | string (schema `ResponseCode`) | no | Alphanumeric two-character standard card network response code or an alternative custom response code, which provides the precise reason for the success or denial of the operation by the card network, platform, or anti-fraud solution.<br> | example: "57" |
| `denial_code` | string (schema `DenialCode`) | no | Denial code. | example: "DAL" |
| `from` | object (schema `v2PaymentsResponse`) | no | Response for a cash-in or cash-out operation. | example: {"authorization_id": 123, "tracking_id": "634c43f2-5b7e-4a80-81c7-e6a7d5edc7fe", "account_id": 456, "amount": 1000, "response_code": "00", "denial_code": "LE003", "validation_results": [{"name": "ACCOUNT", "status": "APPROVED", "reason": "ACCOUNT_FOUND", "description": "Account was found.", "additional_data": {"account_id": 2417}}, {"name": "ACCEPTANCE", "status": "APPROVED", "reason": "ACCEPTANCE_FOUND", "description": "Payment methods acceptances were found."}, {"name": "CONFIG", "status": "APPROVED", "reason": "CONFIG_FOUND", "description": "Payment methods configuration was found."}, {"name": "PAYMENT_DATE", "status": "SKIPPED", "reason": "PAYMENT_DATE_SKIPPED", "description": "Payment date validation was skipped.", "additional_data": {"cause": "Payment date not present."}}, {"name": "PLATFORM_AUTHENTICATION", "status": "APPROVED", "reason": "PLATFORM_AUTHENTICATION_SUCCESSFUL", "description": "Request was authenticated successfully."}, {"name": "ACCOUNT_ID", "status": "APPROVED", "reason": "ACCOUNT_ID_PERMITTED", "description": "Account ID is permitted.", "additional_data": {"document_number": "60XXXXXXXXX19", "external_id": "", "name": "Marcelito"}}, {"name": "PROCESSING_CODE", "status": "APPROVED", "reason": "PROCESSING_CODE_FOUND", "description": "Processing code was found."}, {"name": "PROCESSING_CODE_TYPE", "status": "APPROVED", "reason": "PROCESSING_CODE_TYPE_VALID", "description": "Processing code has a valid balance impact type."}, {"name": "ACCOUNT_LIMITS", "status": "APPROVED", "reason": "ACCOUNT_LIMITS_FOUND", "description": "Account limits were found.", "additional_data": {"available_credit_limit": 746847632710983.1, "available_savings_account_limit": 93477.42, "available_total_installment_credit": -226, "available_withdrawal_credit": -175, "total_credit_limit": 1000, "total_installment_credit_limit": 200, "withdrawal_credit_limit": 300}}, {"name": "ACCOUNT_STATUS", "status": "APPROVED", "reason": "ACCOUNT_STATUS_PERMITTED", "description": "Account status is permitted."}, {"name": "PROGRAM", "status": "APPROVED", "reason": "PROGRAM_FOUND", "description": "Program was found.", "additional_data": {"program_type": "PRE-PAGO"}}, {"name": "BALANCES_CONFIG", "status": "APPROVED", "reason": "BALANCES_CONFIG_FOUND", "description": "Balances configuration was found.", "additional_data": {"amount": "contract_amount", "amount_consider": "principal_amount", "consider": ["AvailableCreditLimit", "OverLimit"], "impact": ["AvailableCreditLimit"], "reset_limit": "last_installment"}}, {"name": "CURRENCY", "status": "APPROVED", "reason": "CURRENCY_FOUND", "description": "Currency was found.", "additional_data": {"code": "BRL", "numeric_code": "986"}}, {"name": "RATES", "status": "APPROVED", "reason": "RATES_APPROVED", "description": "Rates calculation was performed.", "additional_data": {"conversion": {"conversion_rate": 0, "destination": "986", "exchange_rate": 1, "origin": "986", "spread": 0}}}, {"name": "FLEX_CONTROLS", "status": "APPROVED", "reason": "FLEX_CONTROLS_APPROVED", "description": "Authorization passed flex control evaluation.", "additional_data": {"dry_run": false, "evaluated_controls": [{"id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4", "name": "Purchase 1 Month credit card", "evaluation_result": true, "deny_code": "MAX_VALUE_P1M", "response_code": "63", "max_limit": 200000, "accumulated_limit": 135127, "available_limit": 64873}]}}, {"name": "LEDGER", "status": "APPROVED", "reason": "LEDGER_APPROVED", "description": "Ledger was impacted successfully.", "additional_data": {"dry_run": false, "validation_results": null, "account_id": 9999, "available_amounts": {"validation_status": "APPROVED", "details": {"result": {"available_credit_limit": 746847527710892.1, "available_installment_limit": -226, "available_savings_account_limit": 93477.42, "available_withdraw_limit": -175, "held_funds": 91.25, "additional_funds": 0, "overlimit": 2000000, "total_overdraft_limit": 0}}}}, "ledger_operation_status": {"validation_status": "APPROVED"}}, {"name": "AUTHORIZATION", "status": "APPROVED", "reason": "AUTHORIZATION_CREATED", "description": "Authorization was created successfully."}]} |
| `to` | object (schema `v2PaymentsResponse`) | no | Response for a cash-in or cash-out operation. | example: {"authorization_id": 123, "tracking_id": "634c43f2-5b7e-4a80-81c7-e6a7d5edc7fe", "account_id": 456, "amount": 1000, "response_code": "00", "denial_code": "LE003", "validation_results": [{"name": "ACCOUNT", "status": "APPROVED", "reason": "ACCOUNT_FOUND", "description": "Account was found.", "additional_data": {"account_id": 2417}}, {"name": "ACCEPTANCE", "status": "APPROVED", "reason": "ACCEPTANCE_FOUND", "description": "Payment methods acceptances were found."}, {"name": "CONFIG", "status": "APPROVED", "reason": "CONFIG_FOUND", "description": "Payment methods configuration was found."}, {"name": "PAYMENT_DATE", "status": "SKIPPED", "reason": "PAYMENT_DATE_SKIPPED", "description": "Payment date validation was skipped.", "additional_data": {"cause": "Payment date not present."}}, {"name": "PLATFORM_AUTHENTICATION", "status": "APPROVED", "reason": "PLATFORM_AUTHENTICATION_SUCCESSFUL", "description": "Request was authenticated successfully."}, {"name": "ACCOUNT_ID", "status": "APPROVED", "reason": "ACCOUNT_ID_PERMITTED", "description": "Account ID is permitted.", "additional_data": {"document_number": "60XXXXXXXXX19", "external_id": "", "name": "Marcelito"}}, {"name": "PROCESSING_CODE", "status": "APPROVED", "reason": "PROCESSING_CODE_FOUND", "description": "Processing code was found."}, {"name": "PROCESSING_CODE_TYPE", "status": "APPROVED", "reason": "PROCESSING_CODE_TYPE_VALID", "description": "Processing code has a valid balance impact type."}, {"name": "ACCOUNT_LIMITS", "status": "APPROVED", "reason": "ACCOUNT_LIMITS_FOUND", "description": "Account limits were found.", "additional_data": {"available_credit_limit": 746847632710983.1, "available_savings_account_limit": 93477.42, "available_total_installment_credit": -226, "available_withdrawal_credit": -175, "total_credit_limit": 1000, "total_installment_credit_limit": 200, "withdrawal_credit_limit": 300}}, {"name": "ACCOUNT_STATUS", "status": "APPROVED", "reason": "ACCOUNT_STATUS_PERMITTED", "description": "Account status is permitted."}, {"name": "PROGRAM", "status": "APPROVED", "reason": "PROGRAM_FOUND", "description": "Program was found.", "additional_data": {"program_type": "PRE-PAGO"}}, {"name": "BALANCES_CONFIG", "status": "APPROVED", "reason": "BALANCES_CONFIG_FOUND", "description": "Balances configuration was found.", "additional_data": {"amount": "contract_amount", "amount_consider": "principal_amount", "consider": ["AvailableCreditLimit", "OverLimit"], "impact": ["AvailableCreditLimit"], "reset_limit": "last_installment"}}, {"name": "CURRENCY", "status": "APPROVED", "reason": "CURRENCY_FOUND", "description": "Currency was found.", "additional_data": {"code": "BRL", "numeric_code": "986"}}, {"name": "RATES", "status": "APPROVED", "reason": "RATES_APPROVED", "description": "Rates calculation was performed.", "additional_data": {"conversion": {"conversion_rate": 0, "destination": "986", "exchange_rate": 1, "origin": "986", "spread": 0}}}, {"name": "FLEX_CONTROLS", "status": "APPROVED", "reason": "FLEX_CONTROLS_APPROVED", "description": "Authorization passed flex control evaluation.", "additional_data": {"dry_run": false, "evaluated_controls": [{"id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4", "name": "Purchase 1 Month credit card", "evaluation_result": true, "deny_code": "MAX_VALUE_P1M", "response_code": "63", "max_limit": 200000, "accumulated_limit": 135127, "available_limit": 64873}]}}, {"name": "LEDGER", "status": "APPROVED", "reason": "LEDGER_APPROVED", "description": "Ledger was impacted successfully.", "additional_data": {"dry_run": false, "validation_results": null, "account_id": 9999, "available_amounts": {"validation_status": "APPROVED", "details": {"result": {"available_credit_limit": 746847527710892.1, "available_installment_limit": -226, "available_savings_account_limit": 93477.42, "available_withdraw_limit": -175, "held_funds": 91.25, "additional_funds": 0, "overlimit": 2000000, "total_overdraft_limit": 0}}}}, "ledger_operation_status": {"validation_status": "APPROVED"}}, {"name": "AUTHORIZATION", "status": "APPROVED", "reason": "AUTHORIZATION_CREATED", "description": "Authorization was created successfully."}]} |

##### Response 202

**202 `application/json` body fields:**

_No fields declared in the schema._

##### Response 422

422 Example `Unprocessable authentication method`:

```json
[
  {
    "code": "EPAE0004",
    "message": "The method provided in the payload does not exist."
  }
]
```

##### Response 500

500 Example `Platform authentication unexpected error`:

```json
[
  {
    "code": "EPAE0001",
    "message": "Unexpected error while processing the call to the authentication system."
  }
]
```

500 Example `Platform authentication timeout error`:

```json
[
  {
    "code": "EPAE0002",
    "message": "Timeout error while processing the call to the authentication system."
  }
]
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 422 | `EPAE0004` | The method provided in the payload does not exist. |
| 500 | `EPAE0001` | Unexpected error while processing the call to the authentication system. |
| 500 | `EPAE0002` | Timeout error while processing the call to the authentication system. |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;404;409;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-payment-methods`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/v2PaymentsResponse -->
### Schema `v2PaymentsResponse`

Pointer: `#/components/schemas/v2PaymentsResponse`. Type: object (schema `v2PaymentsResponse`).

> Response for a cash-in or cash-out operation.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | yes | Credit or debit amount. | format: "float"; example: 100.23 |
| `authorization_id` | integer (schema `AuthorizationID`) | yes | Unique Pismo-generated ID of the authorization created for this request. Returned on 200 and 201 responses, including idempotent replays. | format: "int64"; example: 123 |
| `response_code` | string (schema `ResponseCode`) | yes | Alphanumeric two-character standard card network response code or an alternative custom response code, which provides the precise reason for the success or denial of the operation by the card network, platform, or anti-fraud solution.<br> | example: "57" |
| `tracking_id` | string (schema `TrackingID`) | yes | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID. | format: "int64"; example: 8675309 |
| `denial_code` | string (schema `DenialCode`) | no | Denial code. | example: "DAL" |
| `validation_results` | array of object (schema `ValidationResults`) | no |  |  |
| `validation_results[].name` | string | no | Name of the evaluated rule. | example: "LEDGER" |
| `validation_results[].status` | string | no | Identifies if the rule was approved, rejected, or skipped during the validation flow. | enum: ["APPROVED", "REJECTED", "SKIPPED"]; example: "REJECTED" |
| `validation_results[].reason` | string | no | Status reason why the specific rule was approved, rejected, or skipped. | example: "LEDGER_INSUFFICIENT_FUNDS" |
| `validation_results[].description` | string | no | Description of the validation result. | example: "The authorization amount is greater than the account available limit." |
| `validation_results[].additional_data` | object | no | Additional data for the validation result. This varies from validation to validation, but every denied validation has the `denial_code` and `response_code` fields. |  |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Application-specific error code |  |
| `message` | string | yes | Error explanation |  |
| `violations` | object (map of string) | no | Field-level validation failures (keys are dynamic) |  |

<!-- schema: #/components/schemas/404Transfers -->
### Schema `404Transfers`

Pointer: `#/components/schemas/404Transfers`. Type: object (schema `404Transfers`).

> * WONT0009 - Original authorization not found.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "WONT0009" |
| `message` | string | no |  | example: "Original authorization not found." |

<!-- schema: #/components/schemas/409Transfers -->
### Schema `409Transfers`

Pointer: `#/components/schemas/409Transfers`. Type: object (schema `409Transfers`).

> Error codes available:
>   * WONT0003 - Tracking ID was already used.
>   * WONT0004 - Tracking ID is already in use by an ongoing request.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | enum: ["WONT0003", "WONT0004"]; example: "WONT0003" |
| `message` | string | no |  | enum: ["Tracking ID was already used.", "Tracking ID is already in use by an ongoing request."]; example: "Tracking ID is already in use by an ongoing request." |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_methods.yaml` | tag `Payment methods`: POST /payment-methods/v2/transfers/confirm | https://github.com/PismoDevEx/pismo-api-specs | `9b02c87b6e39a1c8…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-PAY-payment-methods` — Payment methods
