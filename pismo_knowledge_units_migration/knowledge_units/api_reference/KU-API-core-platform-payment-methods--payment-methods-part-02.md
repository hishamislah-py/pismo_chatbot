---
ku_id: KU-API-core-platform-payment-methods--payment-methods-part-02
title: 'API reference: Core platform - Payment methods — Payment methods (part 2 of 3)'
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
- post-payment-confirm
- post-transfers
- post-transfers-cancel
related_kus:
- KU-CORE-transaction-processing-flows
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-wiac-to-wstm
- KU-EVT-catalogue-other-domains
- KU-EVT-client-webhooks-part-01
- KU-PAY-configure-payment-methods
- KU-PAY-payment-configurations
- KU-PAY-payment-methods
specification_version: 1.0.0
---

# API reference: Core platform - Payment methods — Payment methods (part 2 of 3)

**KU ID:** `KU-API-core-platform-payment-methods--payment-methods-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Payment methods` in `api-specs/Core_platform_-_Payment_methods.yaml` (“Core platform - Payment methods”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage cash-in and cash-out payments and P2P transfers.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /payment-methods/v2/payments/confirm` | `post-payment-confirm` | Confirm pre-authorized cash-in or cash-out | no |
| `POST /payment-methods/v2/transfers` | `post-transfers` | Create transfer | no |
| `POST /payment-methods/v2/transfers/cancel` | `post-transfers-cancel` | Cancel transfer | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payment-methods/v2/payments/confirm operationId=post-payment-confirm -->
### `POST /payment-methods/v2/payments/confirm` — Confirm pre-authorized cash-in or cash-out

- **operationId:** `post-payment-confirm`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment methods`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Confirm a pre-authorized payment operation. Use this endpoint only if the created payment operation had the `pre_authorization` set to `true`. 
>
> In the request, provide a new `tracking_id` for the confirmation operation and the `original_tracking_id` of the original payment operation. If you don't provide the `amount`, the platform confirms the total original amount. You can also provide the `amount` to confirm a total, partial, or greater amount.
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
| 200 | Request was processed successfully, existing authorization with the corresponding `tracking_id` returned. | `application/json`: object (schema `v2PaymentsResponse`) |
| 202 | Request was accepted and will be processed asynchronously. The response body is empty (`{}`).<br>The confirmation outcome (`authorization_id`, `tracking_id`, `account_id`, `response_code`,<br>`denial_code`) is not returned on this response — it is delivered through the *Platform<br>authorization created* event (category `CONFIRMATION`). A populated body is only returned on<br>the `200` idempotent-replay response.<br> | `application/json`: object (schema `PaymentsConfirmResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `404Payments`) |
| 409 | Conflict | `application/json`: object (schema `409Payments`) |
| 422 | Unprocessable request | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

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

##### Response 202

**202 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Original authorization cannot be confirmed`:

```json
{
  "code": "WONP0010",
  "message": "Original authorization cannot be confirmed."
}
```

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
| 400 | `WONP0010` | Original authorization cannot be confirmed. |
| 422 | `EPAE0004` | The method provided in the payload does not exist. |
| 500 | `EPAE0001` | Unexpected error while processing the call to the authentication system. |
| 500 | `EPAE0002` | Timeout error while processing the call to the authentication system. |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;202;400;404;409;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CORE-transaction-processing-flows`, `KU-PAY-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payment-methods/v2/transfers operationId=post-transfers -->
### `POST /payment-methods/v2/transfers` — Create transfer

- **operationId:** `post-transfers`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment methods`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a transfer operation between two accounts on the Pismo platform.
>
> With this endpoint, you have the following additional options.
> - Specify the `authentication` method and details.
> - Set `pre_authorization` to `true` for operations that require additional confirmation and then call the [Confirm pre-authorized transfer](ref:post-transfers-confirm) endpoint.
> - Set `validation_rules` in the `From` object to control the rules in this flow, such as disabling a rule, changing the response code and denial code, and forcing a rule.
>
> Refer to the [Payment methods](doc:payment-methods) guide for additional information.
>
> This endpoint generates a [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `TransfersRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number (schema `Amount`) | yes | Credit or debit amount. | format: "float"; example: 100.23 |
| `from` | object (schema `From`) | yes |  |  |
| `to` | object (schema `To`) | yes |  |  |
| `tracking_id` | string (schema `TrackingID`) | yes | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `authentication` | object (schema `Authentication`) | no | Authentication object. |  |
| `description` | string (schema `Description`) | no | Optional text that describes the operation. | example: "Custom purchase." |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Effective payment date in the UTC-0 RFC3339 format, which includes milliseconds (yyyy-MM-ddThh:mm:ss.SSSZ).<br>Payments can be backdated but future dates are not allowed.<br> | format: "date-time"; example: "2023-01-02T07:35:05.125Z" |
| `pre_authorization` | boolean (schema `PreAuthorization`) | no | If set to `true`, this flag indicates that the operation is pre-authorized and requires additional confirmation. | default: false; example: false |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing authorization with the corresponding `tracking_id` returned. | `application/json`: object (schema `TransfersResponse`) |
| 201 | Request was processed successfully, new authorization created. | `application/json`: object (schema `TransfersResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid. | `application/json`: object (schema `401Transfers`) |
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

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | no | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `response_code` | string (schema `ResponseCode`) | no | Alphanumeric two-character standard card network response code or an alternative custom response code, which provides the precise reason for the success or denial of the operation by the card network, platform, or anti-fraud solution.<br> | example: "57" |
| `denial_code` | string (schema `DenialCode`) | no | Denial code. | example: "DAL" |
| `from` | object (schema `v2PaymentsResponse`) | no | Response for a cash-in or cash-out operation. | example: {"authorization_id": 123, "tracking_id": "634c43f2-5b7e-4a80-81c7-e6a7d5edc7fe", "account_id": 456, "amount": 1000, "response_code": "00", "denial_code": "LE003", "validation_results": [{"name": "ACCOUNT", "status": "APPROVED", "reason": "ACCOUNT_FOUND", "description": "Account was found.", "additional_data": {"account_id": 2417}}, {"name": "ACCEPTANCE", "status": "APPROVED", "reason": "ACCEPTANCE_FOUND", "description": "Payment methods acceptances were found."}, {"name": "CONFIG", "status": "APPROVED", "reason": "CONFIG_FOUND", "description": "Payment methods configuration was found."}, {"name": "PAYMENT_DATE", "status": "SKIPPED", "reason": "PAYMENT_DATE_SKIPPED", "description": "Payment date validation was skipped.", "additional_data": {"cause": "Payment date not present."}}, {"name": "PLATFORM_AUTHENTICATION", "status": "APPROVED", "reason": "PLATFORM_AUTHENTICATION_SUCCESSFUL", "description": "Request was authenticated successfully."}, {"name": "ACCOUNT_ID", "status": "APPROVED", "reason": "ACCOUNT_ID_PERMITTED", "description": "Account ID is permitted.", "additional_data": {"document_number": "60XXXXXXXXX19", "external_id": "", "name": "Marcelito"}}, {"name": "PROCESSING_CODE", "status": "APPROVED", "reason": "PROCESSING_CODE_FOUND", "description": "Processing code was found."}, {"name": "PROCESSING_CODE_TYPE", "status": "APPROVED", "reason": "PROCESSING_CODE_TYPE_VALID", "description": "Processing code has a valid balance impact type."}, {"name": "ACCOUNT_LIMITS", "status": "APPROVED", "reason": "ACCOUNT_LIMITS_FOUND", "description": "Account limits were found.", "additional_data": {"available_credit_limit": 746847632710983.1, "available_savings_account_limit": 93477.42, "available_total_installment_credit": -226, "available_withdrawal_credit": -175, "total_credit_limit": 1000, "total_installment_credit_limit": 200, "withdrawal_credit_limit": 300}}, {"name": "ACCOUNT_STATUS", "status": "APPROVED", "reason": "ACCOUNT_STATUS_PERMITTED", "description": "Account status is permitted."}, {"name": "PROGRAM", "status": "APPROVED", "reason": "PROGRAM_FOUND", "description": "Program was found.", "additional_data": {"program_type": "PRE-PAGO"}}, {"name": "BALANCES_CONFIG", "status": "APPROVED", "reason": "BALANCES_CONFIG_FOUND", "description": "Balances configuration was found.", "additional_data": {"amount": "contract_amount", "amount_consider": "principal_amount", "consider": ["AvailableCreditLimit", "OverLimit"], "impact": ["AvailableCreditLimit"], "reset_limit": "last_installment"}}, {"name": "CURRENCY", "status": "APPROVED", "reason": "CURRENCY_FOUND", "description": "Currency was found.", "additional_data": {"code": "BRL", "numeric_code": "986"}}, {"name": "RATES", "status": "APPROVED", "reason": "RATES_APPROVED", "description": "Rates calculation was performed.", "additional_data": {"conversion": {"conversion_rate": 0, "destination": "986", "exchange_rate": 1, "origin": "986", "spread": 0}}}, {"name": "FLEX_CONTROLS", "status": "APPROVED", "reason": "FLEX_CONTROLS_APPROVED", "description": "Authorization passed flex control evaluation.", "additional_data": {"dry_run": false, "evaluated_controls": [{"id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4", "name": "Purchase 1 Month credit card", "evaluation_result": true, "deny_code": "MAX_VALUE_P1M", "response_code": "63", "max_limit": 200000, "accumulated_limit": 135127, "available_limit": 64873}]}}, {"name": "LEDGER", "status": "APPROVED", "reason": "LEDGER_APPROVED", "description": "Ledger was impacted successfully.", "additional_data": {"dry_run": false, "validation_results": null, "account_id": 9999, "available_amounts": {"validation_status": "APPROVED", "details": {"result": {"available_credit_limit": 746847527710892.1, "available_installment_limit": -226, "available_savings_account_limit": 93477.42, "available_withdraw_limit": -175, "held_funds": 91.25, "additional_funds": 0, "overlimit": 2000000, "total_overdraft_limit": 0}}}}, "ledger_operation_status": {"validation_status": "APPROVED"}}, {"name": "AUTHORIZATION", "status": "APPROVED", "reason": "AUTHORIZATION_CREATED", "description": "Authorization was created successfully."}]} |
| `to` | object (schema `v2PaymentsResponse`) | no | Response for a cash-in or cash-out operation. | example: {"authorization_id": 123, "tracking_id": "634c43f2-5b7e-4a80-81c7-e6a7d5edc7fe", "account_id": 456, "amount": 1000, "response_code": "00", "denial_code": "LE003", "validation_results": [{"name": "ACCOUNT", "status": "APPROVED", "reason": "ACCOUNT_FOUND", "description": "Account was found.", "additional_data": {"account_id": 2417}}, {"name": "ACCEPTANCE", "status": "APPROVED", "reason": "ACCEPTANCE_FOUND", "description": "Payment methods acceptances were found."}, {"name": "CONFIG", "status": "APPROVED", "reason": "CONFIG_FOUND", "description": "Payment methods configuration was found."}, {"name": "PAYMENT_DATE", "status": "SKIPPED", "reason": "PAYMENT_DATE_SKIPPED", "description": "Payment date validation was skipped.", "additional_data": {"cause": "Payment date not present."}}, {"name": "PLATFORM_AUTHENTICATION", "status": "APPROVED", "reason": "PLATFORM_AUTHENTICATION_SUCCESSFUL", "description": "Request was authenticated successfully."}, {"name": "ACCOUNT_ID", "status": "APPROVED", "reason": "ACCOUNT_ID_PERMITTED", "description": "Account ID is permitted.", "additional_data": {"document_number": "60XXXXXXXXX19", "external_id": "", "name": "Marcelito"}}, {"name": "PROCESSING_CODE", "status": "APPROVED", "reason": "PROCESSING_CODE_FOUND", "description": "Processing code was found."}, {"name": "PROCESSING_CODE_TYPE", "status": "APPROVED", "reason": "PROCESSING_CODE_TYPE_VALID", "description": "Processing code has a valid balance impact type."}, {"name": "ACCOUNT_LIMITS", "status": "APPROVED", "reason": "ACCOUNT_LIMITS_FOUND", "description": "Account limits were found.", "additional_data": {"available_credit_limit": 746847632710983.1, "available_savings_account_limit": 93477.42, "available_total_installment_credit": -226, "available_withdrawal_credit": -175, "total_credit_limit": 1000, "total_installment_credit_limit": 200, "withdrawal_credit_limit": 300}}, {"name": "ACCOUNT_STATUS", "status": "APPROVED", "reason": "ACCOUNT_STATUS_PERMITTED", "description": "Account status is permitted."}, {"name": "PROGRAM", "status": "APPROVED", "reason": "PROGRAM_FOUND", "description": "Program was found.", "additional_data": {"program_type": "PRE-PAGO"}}, {"name": "BALANCES_CONFIG", "status": "APPROVED", "reason": "BALANCES_CONFIG_FOUND", "description": "Balances configuration was found.", "additional_data": {"amount": "contract_amount", "amount_consider": "principal_amount", "consider": ["AvailableCreditLimit", "OverLimit"], "impact": ["AvailableCreditLimit"], "reset_limit": "last_installment"}}, {"name": "CURRENCY", "status": "APPROVED", "reason": "CURRENCY_FOUND", "description": "Currency was found.", "additional_data": {"code": "BRL", "numeric_code": "986"}}, {"name": "RATES", "status": "APPROVED", "reason": "RATES_APPROVED", "description": "Rates calculation was performed.", "additional_data": {"conversion": {"conversion_rate": 0, "destination": "986", "exchange_rate": 1, "origin": "986", "spread": 0}}}, {"name": "FLEX_CONTROLS", "status": "APPROVED", "reason": "FLEX_CONTROLS_APPROVED", "description": "Authorization passed flex control evaluation.", "additional_data": {"dry_run": false, "evaluated_controls": [{"id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4", "name": "Purchase 1 Month credit card", "evaluation_result": true, "deny_code": "MAX_VALUE_P1M", "response_code": "63", "max_limit": 200000, "accumulated_limit": 135127, "available_limit": 64873}]}}, {"name": "LEDGER", "status": "APPROVED", "reason": "LEDGER_APPROVED", "description": "Ledger was impacted successfully.", "additional_data": {"dry_run": false, "validation_results": null, "account_id": 9999, "available_amounts": {"validation_status": "APPROVED", "details": {"result": {"available_credit_limit": 746847527710892.1, "available_installment_limit": -226, "available_savings_account_limit": 93477.42, "available_withdraw_limit": -175, "held_funds": 91.25, "additional_funds": 0, "overlimit": 2000000, "total_overdraft_limit": 0}}}}, "ledger_operation_status": {"validation_status": "APPROVED"}}, {"name": "AUTHORIZATION", "status": "APPROVED", "reason": "AUTHORIZATION_CREATED", "description": "Authorization was created successfully."}]} |

##### Response 400

400 Example `Amount required`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "amount": "amount is a required field."
  }
}
```

400 Example `Invalid amount`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "amount": "A maximum of 20 digits, including two decimals, is allowed for the amount field."
  }
}
```

400 Example `Invalid account`:

```json
{
  "code": "WONB0001",
  "message": "Authorized account is different from the request."
}
```

400 Example `Invalid currency`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "currency": "Currency is invalid. The field must have the valid ISO 4217 currency code."
  }
}
```

400 Example `Tracking ID required`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "tracking_id": "tracking_id is a required field."
  }
}
```

400 Example `Processing code required`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "processing_code": "processing_code is a required field."
  }
}
```

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
| 400 | `WONP0001` | Payload is invalid. It must be a valid JSON. |
| 400 | `WONB0001` | Authorized account is different from the request. |
| 422 | `EPAE0004` | The method provided in the payload does not exist. |
| 500 | `EPAE0001` | Unexpected error while processing the call to the authentication system. |
| 500 | `EPAE0002` | Timeout error while processing the call to the authentication system. |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;400;401;409;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-EVT-client-webhooks-part-01`, `KU-PAY-configure-payment-methods`, `KU-PAY-payment-configurations`, `KU-PAY-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payment-methods/v2/transfers/cancel operationId=post-transfers-cancel -->
### `POST /payment-methods/v2/transfers/cancel` — Cancel transfer

- **operationId:** `post-transfers-cancel`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment methods`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel an existing transfer operation. If you don't provide the `amount`, the platform cancels the total original amount. You can also provide the `amount` to cancel a total or partial amount.
>
> Refer to the [Payment methods](doc:payment-methods) guide for additional information.
>
> This endpoint generates a [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `PaymentsCancelRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | yes | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `original_tracking_id` | string (schema `OriginalTrackingID`) | yes | Tracking ID for the original operation. | minLength: 36; maxLength: 50; example: "249fbd1c-cfcd-48aa-8bcb-1ffe3a5f7978" |
| `amount` | number (schema `Amount`) | no | Credit or debit amount. | format: "float"; example: 100.23 |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing authorization with the corresponding `tracking_id` returned. | `application/json`: object (schema `TransfersCancelResponse`) |
| 201 | Request was processed successfully, new authorization created. | `application/json`: object (schema `TransfersCancelResponse`) |
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
| `from` | object (schema `PaymentsCancelResponse`) | no | Response for a cash-in or cash-out cancel operation. | example: {"authorization_id": 124, "tracking_id": "634c43f2-5b7e-4a80-81c7-e6a7d5edc7fe", "account_id": 456, "amount": 1000, "response_code": "00", "denial_code": "PRC", "validation_results": [{"name": "ACCOUNT_ID", "status": "APPROVED", "reason": "ACCOUNT_ID_PERMITTED", "description": "Account ID is permitted.", "additional_data": {"document_number": "6XXXXXXXXXX9", "external_id": "", "name": "Marcelito"}}, {"name": "ORIGINAL_AUTHORIZATION", "status": "APPROVED", "reason": "ORIGINAL_AUTHORIZATION_APPROVED", "description": "Original authorization validation was approved."}, {"name": "PROCESSING_CODE", "status": "APPROVED", "reason": "PROCESSING_CODE_FOUND", "description": "Processing code was found."}, {"name": "PROCESSING_CODE_TYPE", "status": "APPROVED", "reason": "PROCESSING_CODE_TYPE_VALID", "description": "Processing code has a valid balance impact type."}, {"name": "ACCOUNT_LIMITS", "status": "APPROVED", "reason": "ACCOUNT_LIMITS_FOUND", "description": "Account limits were found."}, {"name": "ACCOUNT_STATUS", "status": "SKIPPED", "reason": "ACCOUNT_STATUS_SKIPPED", "description": "Account status validation was skipped.", "additional_data": {"cause": "Cancellations are forced operations and does not need to run this validation"}}, {"name": "PROGRAM", "status": "APPROVED", "reason": "PROGRAM_FOUND", "description": "Program was found.", "additional_data": {"program_type": "PRE-PAGO"}}, {"name": "REMAINING_CANCELLATION_BALANCE", "status": "REJECTED", "reason": "AUTHORIZATION_ALREADY_CANCELLED", "description": "Authorization was already cancelled.", "additional_data": {"denial_code": "PRC", "response_code": "57"}}, {"name": "RATES", "status": "APPROVED", "reason": "RATES_APPROVED", "description": "Rates calculation was performed."}, {"name": "LEDGER", "status": "APPROVED", "reason": "LEDGER_APPROVED", "description": "Ledger was impacted successfully.", "additional_data": {"dry_run": false, "validation_results": null, "account_id": 9999, "available_amounts": {"validation_status": "APPROVED", "details": {"result": {"available_credit_limit": 746847527710892.1, "available_installment_limit": -226, "available_savings_account_limit": 93477.42, "available_withdraw_limit": -175, "held_funds": 91.25, "additional_funds": 0, "overlimit": 2000000, "total_overdraft_limit": 0}}}}, "ledger_operation_status": {"validation_status": "APPROVED"}}, {"name": "FLEX_CONTROLS", "status": "APPROVED", "reason": "FLEX_CONTROLS_APPROVED", "description": "Authorization passed flex control evaluation.", "additional_data": {"dry_run": false, "evaluated_controls": [{"id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4", "name": "Purchase 1 Month credit card", "evaluation_result": true, "deny_code": "MAX_VALUE_P1M", "response_code": "63", "max_limit": 200000, "accumulated_limit": 135127, "available_limit": 64873}]}}, {"name": "AUTHORIZATION", "status": "APPROVED", "reason": "AUTHORIZATION_CREATED", "description": "Authorization was created successfully."}]} |
| `to` | object (schema `PaymentsCancelResponse`) | no | Response for a cash-in or cash-out cancel operation. | example: {"authorization_id": 124, "tracking_id": "634c43f2-5b7e-4a80-81c7-e6a7d5edc7fe", "account_id": 456, "amount": 1000, "response_code": "00", "denial_code": "PRC", "validation_results": [{"name": "ACCOUNT_ID", "status": "APPROVED", "reason": "ACCOUNT_ID_PERMITTED", "description": "Account ID is permitted.", "additional_data": {"document_number": "6XXXXXXXXXX9", "external_id": "", "name": "Marcelito"}}, {"name": "ORIGINAL_AUTHORIZATION", "status": "APPROVED", "reason": "ORIGINAL_AUTHORIZATION_APPROVED", "description": "Original authorization validation was approved."}, {"name": "PROCESSING_CODE", "status": "APPROVED", "reason": "PROCESSING_CODE_FOUND", "description": "Processing code was found."}, {"name": "PROCESSING_CODE_TYPE", "status": "APPROVED", "reason": "PROCESSING_CODE_TYPE_VALID", "description": "Processing code has a valid balance impact type."}, {"name": "ACCOUNT_LIMITS", "status": "APPROVED", "reason": "ACCOUNT_LIMITS_FOUND", "description": "Account limits were found."}, {"name": "ACCOUNT_STATUS", "status": "SKIPPED", "reason": "ACCOUNT_STATUS_SKIPPED", "description": "Account status validation was skipped.", "additional_data": {"cause": "Cancellations are forced operations and does not need to run this validation"}}, {"name": "PROGRAM", "status": "APPROVED", "reason": "PROGRAM_FOUND", "description": "Program was found.", "additional_data": {"program_type": "PRE-PAGO"}}, {"name": "REMAINING_CANCELLATION_BALANCE", "status": "REJECTED", "reason": "AUTHORIZATION_ALREADY_CANCELLED", "description": "Authorization was already cancelled.", "additional_data": {"denial_code": "PRC", "response_code": "57"}}, {"name": "RATES", "status": "APPROVED", "reason": "RATES_APPROVED", "description": "Rates calculation was performed."}, {"name": "LEDGER", "status": "APPROVED", "reason": "LEDGER_APPROVED", "description": "Ledger was impacted successfully.", "additional_data": {"dry_run": false, "validation_results": null, "account_id": 9999, "available_amounts": {"validation_status": "APPROVED", "details": {"result": {"available_credit_limit": 746847527710892.1, "available_installment_limit": -226, "available_savings_account_limit": 93477.42, "available_withdraw_limit": -175, "held_funds": 91.25, "additional_funds": 0, "overlimit": 2000000, "total_overdraft_limit": 0}}}}, "ledger_operation_status": {"validation_status": "APPROVED"}}, {"name": "FLEX_CONTROLS", "status": "APPROVED", "reason": "FLEX_CONTROLS_APPROVED", "description": "Authorization passed flex control evaluation.", "additional_data": {"dry_run": false, "evaluated_controls": [{"id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4", "name": "Purchase 1 Month credit card", "evaluation_result": true, "deny_code": "MAX_VALUE_P1M", "response_code": "63", "max_limit": 200000, "accumulated_limit": 135127, "available_limit": 64873}]}}, {"name": "AUTHORIZATION", "status": "APPROVED", "reason": "AUTHORIZATION_CREATED", "description": "Authorization was created successfully."}]} |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `tracking_id` | string (schema `TrackingID`) | no | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `response_code` | string (schema `ResponseCode`) | no | Alphanumeric two-character standard card network response code or an alternative custom response code, which provides the precise reason for the success or denial of the operation by the card network, platform, or anti-fraud solution.<br> | example: "57" |
| `denial_code` | string (schema `DenialCode`) | no | Denial code. | example: "DAL" |
| `from` | object (schema `PaymentsCancelResponse`) | no | Response for a cash-in or cash-out cancel operation. | example: {"authorization_id": 124, "tracking_id": "634c43f2-5b7e-4a80-81c7-e6a7d5edc7fe", "account_id": 456, "amount": 1000, "response_code": "00", "denial_code": "PRC", "validation_results": [{"name": "ACCOUNT_ID", "status": "APPROVED", "reason": "ACCOUNT_ID_PERMITTED", "description": "Account ID is permitted.", "additional_data": {"document_number": "6XXXXXXXXXX9", "external_id": "", "name": "Marcelito"}}, {"name": "ORIGINAL_AUTHORIZATION", "status": "APPROVED", "reason": "ORIGINAL_AUTHORIZATION_APPROVED", "description": "Original authorization validation was approved."}, {"name": "PROCESSING_CODE", "status": "APPROVED", "reason": "PROCESSING_CODE_FOUND", "description": "Processing code was found."}, {"name": "PROCESSING_CODE_TYPE", "status": "APPROVED", "reason": "PROCESSING_CODE_TYPE_VALID", "description": "Processing code has a valid balance impact type."}, {"name": "ACCOUNT_LIMITS", "status": "APPROVED", "reason": "ACCOUNT_LIMITS_FOUND", "description": "Account limits were found."}, {"name": "ACCOUNT_STATUS", "status": "SKIPPED", "reason": "ACCOUNT_STATUS_SKIPPED", "description": "Account status validation was skipped.", "additional_data": {"cause": "Cancellations are forced operations and does not need to run this validation"}}, {"name": "PROGRAM", "status": "APPROVED", "reason": "PROGRAM_FOUND", "description": "Program was found.", "additional_data": {"program_type": "PRE-PAGO"}}, {"name": "REMAINING_CANCELLATION_BALANCE", "status": "REJECTED", "reason": "AUTHORIZATION_ALREADY_CANCELLED", "description": "Authorization was already cancelled.", "additional_data": {"denial_code": "PRC", "response_code": "57"}}, {"name": "RATES", "status": "APPROVED", "reason": "RATES_APPROVED", "description": "Rates calculation was performed."}, {"name": "LEDGER", "status": "APPROVED", "reason": "LEDGER_APPROVED", "description": "Ledger was impacted successfully.", "additional_data": {"dry_run": false, "validation_results": null, "account_id": 9999, "available_amounts": {"validation_status": "APPROVED", "details": {"result": {"available_credit_limit": 746847527710892.1, "available_installment_limit": -226, "available_savings_account_limit": 93477.42, "available_withdraw_limit": -175, "held_funds": 91.25, "additional_funds": 0, "overlimit": 2000000, "total_overdraft_limit": 0}}}}, "ledger_operation_status": {"validation_status": "APPROVED"}}, {"name": "FLEX_CONTROLS", "status": "APPROVED", "reason": "FLEX_CONTROLS_APPROVED", "description": "Authorization passed flex control evaluation.", "additional_data": {"dry_run": false, "evaluated_controls": [{"id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4", "name": "Purchase 1 Month credit card", "evaluation_result": true, "deny_code": "MAX_VALUE_P1M", "response_code": "63", "max_limit": 200000, "accumulated_limit": 135127, "available_limit": 64873}]}}, {"name": "AUTHORIZATION", "status": "APPROVED", "reason": "AUTHORIZATION_CREATED", "description": "Authorization was created successfully."}]} |
| `to` | object (schema `PaymentsCancelResponse`) | no | Response for a cash-in or cash-out cancel operation. | example: {"authorization_id": 124, "tracking_id": "634c43f2-5b7e-4a80-81c7-e6a7d5edc7fe", "account_id": 456, "amount": 1000, "response_code": "00", "denial_code": "PRC", "validation_results": [{"name": "ACCOUNT_ID", "status": "APPROVED", "reason": "ACCOUNT_ID_PERMITTED", "description": "Account ID is permitted.", "additional_data": {"document_number": "6XXXXXXXXXX9", "external_id": "", "name": "Marcelito"}}, {"name": "ORIGINAL_AUTHORIZATION", "status": "APPROVED", "reason": "ORIGINAL_AUTHORIZATION_APPROVED", "description": "Original authorization validation was approved."}, {"name": "PROCESSING_CODE", "status": "APPROVED", "reason": "PROCESSING_CODE_FOUND", "description": "Processing code was found."}, {"name": "PROCESSING_CODE_TYPE", "status": "APPROVED", "reason": "PROCESSING_CODE_TYPE_VALID", "description": "Processing code has a valid balance impact type."}, {"name": "ACCOUNT_LIMITS", "status": "APPROVED", "reason": "ACCOUNT_LIMITS_FOUND", "description": "Account limits were found."}, {"name": "ACCOUNT_STATUS", "status": "SKIPPED", "reason": "ACCOUNT_STATUS_SKIPPED", "description": "Account status validation was skipped.", "additional_data": {"cause": "Cancellations are forced operations and does not need to run this validation"}}, {"name": "PROGRAM", "status": "APPROVED", "reason": "PROGRAM_FOUND", "description": "Program was found.", "additional_data": {"program_type": "PRE-PAGO"}}, {"name": "REMAINING_CANCELLATION_BALANCE", "status": "REJECTED", "reason": "AUTHORIZATION_ALREADY_CANCELLED", "description": "Authorization was already cancelled.", "additional_data": {"denial_code": "PRC", "response_code": "57"}}, {"name": "RATES", "status": "APPROVED", "reason": "RATES_APPROVED", "description": "Rates calculation was performed."}, {"name": "LEDGER", "status": "APPROVED", "reason": "LEDGER_APPROVED", "description": "Ledger was impacted successfully.", "additional_data": {"dry_run": false, "validation_results": null, "account_id": 9999, "available_amounts": {"validation_status": "APPROVED", "details": {"result": {"available_credit_limit": 746847527710892.1, "available_installment_limit": -226, "available_savings_account_limit": 93477.42, "available_withdraw_limit": -175, "held_funds": 91.25, "additional_funds": 0, "overlimit": 2000000, "total_overdraft_limit": 0}}}}, "ledger_operation_status": {"validation_status": "APPROVED"}}, {"name": "FLEX_CONTROLS", "status": "APPROVED", "reason": "FLEX_CONTROLS_APPROVED", "description": "Authorization passed flex control evaluation.", "additional_data": {"dry_run": false, "evaluated_controls": [{"id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4", "name": "Purchase 1 Month credit card", "evaluation_result": true, "deny_code": "MAX_VALUE_P1M", "response_code": "63", "max_limit": 200000, "accumulated_limit": 135127, "available_limit": 64873}]}}, {"name": "AUTHORIZATION", "status": "APPROVED", "reason": "AUTHORIZATION_CREATED", "description": "Authorization was created successfully."}]} |

##### Response 400

400 Example `Amount required`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "amount": "amount is a required field."
  }
}
```

400 Example `Invalid amount`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "amount": "A maximum of 20 digits, including two decimals, is allowed for the amount field."
  }
}
```

400 Example `Invalid currency`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "currency": "Currency is invalid. The field must have the valid ISO 4217 currency code."
  }
}
```

400 Example `Tracking ID required`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "tracking_id": "tracking_id is a required field."
  }
}
```

400 Example `Original tracking ID required`:

```json
{
  "code": "WONP0001",
  "message": "Payload is invalid. It must be a valid JSON.",
  "violations": {
    "original_tracking_id": "original_tracking_id is a required field."
  }
}
```

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
| 400 | `WONP0001` | Payload is invalid. It must be a valid JSON. |
| 422 | `EPAE0004` | The method provided in the payload does not exist. |
| 500 | `EPAE0001` | Unexpected error while processing the call to the authentication system. |
| 500 | `EPAE0002` | Timeout error while processing the call to the authentication system. |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;400;404;409;422;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-PAY-payment-methods`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Application-specific error code |  |
| `message` | string | yes | Error explanation |  |
| `violations` | object (map of string) | no | Field-level validation failures (keys are dynamic) |  |

<!-- schema: #/components/schemas/404Payments -->
### Schema `404Payments`

Pointer: `#/components/schemas/404Payments`. Type: object (schema `404Payments`).

> * WONP0009 - Original authorization not found.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "WONP0009" |
| `message` | string | no |  | example: "Original authorization not found." |

<!-- schema: #/components/schemas/409Payments -->
### Schema `409Payments`

Pointer: `#/components/schemas/409Payments`. Type: object (schema `409Payments`).

> Error codes available:
>   * WONP0003 - Tracking ID was already used.
>   * WONP0004 - Tracking ID is already in use by an ongoing request.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | enum: ["WONP0003", "WONP0004"]; example: "WONP0003" |
| `message` | string | no |  | enum: ["Tracking ID was already used.", "Tracking ID is already in use by an ongoing request."]; example: "Tracking ID was already used." |

<!-- schema: #/components/schemas/From -->
### Schema `From`

Pointer: `#/components/schemas/From`. Type: object (schema `From`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Pismo account ID. | format: "int64"; example: 8675309 |
| `currency` | string (schema `CurrencyPismoHierarchy`) | no | ISO-4217 alphabetic or numeric (3 characters) authorization currency code. For example, either BRL or 986 for Brazilian real. If you don't provide the currency, the platform uses the currency registered in the Pismo hierarchy (first looking at the account, then program, and then Org levels). | example: "BRL" |
| `processing_code` | string (schema `ProcessingCode`) | yes | Unique processing code that identifies the credit or debit operation. | example: "219803" |
| `validation_rules` | object (map of object (schema `RuleConfig`)) (schema `ValidationRules`) | no | Validation rules performed in the flow. Each key is a rule name (such as `ACCOUNT_STATUS` or `LEDGER`) and the value is its configuration. | example: {"ACCOUNT_STATUS": {"disable": false, "force": false, "denial_reasons": {"ACCOUNT_STATUS_NOT_PERMITTED": {"response_code": "57", "denial_code": "DAL"}}}, "LEDGER": {"denial_reasons": {"LEDGER_INSUFFICIENT_FUNDS": {"response_code": "51", "denial_code": "DAL"}, "LEDGER_NOT_ALLOWED_OPERATION": {"response_code": "57", "denial_code": "DAL"}}}} |
| `authorization_validations` | object (schema `AuthorizationValidations`) | no | Contains additional data to be used in the authorization flow. This field is only considered for authorizations. Cancellations and confirmations will retrieve it based on the original authorization. |  |

<!-- schema: #/components/schemas/To -->
### Schema `To`

Pointer: `#/components/schemas/To`. Type: object (schema `To`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Pismo account ID. | format: "int64"; example: 8675309 |
| `beneficiary_id` | string (schema `BeneficiaryID`) | no | UUID for the beneficiary related to the account. | minLength: 36; maxLength: 50; example: "2c298321-bc21-4039-9c45-780cc6d4ec46" |
| `currency` | string (schema `CurrencyPismoHierarchy`) | no | ISO-4217 alphabetic or numeric (3 characters) authorization currency code. For example, either BRL or 986 for Brazilian real. If you don't provide the currency, the platform uses the currency registered in the Pismo hierarchy (first looking at the account, then program, and then Org levels). | example: "BRL" |
| `processing_code` | string (schema `ProcessingCode`) | yes | Unique processing code that identifies the credit or debit operation. | example: "219803" |
| `validation_rules` | object (map of object (schema `RuleConfig`)) (schema `ValidationRules`) | no | Validation rules performed in the flow. Each key is a rule name (such as `ACCOUNT_STATUS` or `LEDGER`) and the value is its configuration. | example: {"ACCOUNT_STATUS": {"disable": false, "force": false, "denial_reasons": {"ACCOUNT_STATUS_NOT_PERMITTED": {"response_code": "57", "denial_code": "DAL"}}}, "LEDGER": {"denial_reasons": {"LEDGER_INSUFFICIENT_FUNDS": {"response_code": "51", "denial_code": "DAL"}, "LEDGER_NOT_ALLOWED_OPERATION": {"response_code": "57", "denial_code": "DAL"}}}} |
| `authorization_validations` | object | no | Contains additional data to be used in the authorization flow. This field is only considered for authorizations. Cancellations and confirmations will retrieve it based on the original authorization. |  |
| `authorization_validations.associated_ids` | object (schema `AssociatedIDs`) | no | External IDs used in the authorization flow. |  |

<!-- schema: #/components/schemas/Authentication -->
### Schema `Authentication`

Pointer: `#/components/schemas/Authentication`. Type: object (schema `Authentication`).

> Authentication object.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `method` | string | no | Authentication method. <br>- `otp` is when the operation needs to be authenticated.<br>- `transaction_signing` is when the operation has been authenticated already but needs to be validated.<br> | example: "otp" |
| `parameters` | object | no | Authentication parameters will vary, depending on type of the method used. |  |
| `parameters.device_id` | string | no | Device ID. Used in the `otp` authentication method. | example: "abc" |
| `parameters.token` | string | no | Authentication token. Used in the `otp` authentication method. | example: "123456" |
| `parameters.user_id` | string | no | User ID. Used in the `otp` authentication method. | example: "123456789" |
| `parameters.hash` | string | no | Value generated at the time of authentication via OTP and intended for authentication via signing. Used in the `transaction_signing` authentication method. |  |
| `parameters.signing_data` | object | no | Object that contains authorization information provided at time of signing. Used in the `transaction_signing` authentication method. |  |

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

<!-- schema: #/components/schemas/401Transfers -->
### Schema `401Transfers`

Pointer: `#/components/schemas/401Transfers`. Type: object (schema `401Transfers`).

> Error codes available:
>   * WONT0005 - Authentication is required but no authentication method was provided.
>   * WONT0006 - Authentication is required but it was not performed.
>   * WONT0007 - Request was not authenticated.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | enum: ["WONT0005", "WONT0006", "WONT0007"]; example: "WONT0005" |
| `message` | string | no |  | enum: ["Authentication is required but no authentication method was provided.", "Authentication is required but it was not performed.", "Request was not authenticated."]; example: "Authentication is required but no authentication method was provided." |

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

<!-- schema: #/components/schemas/PaymentsCancelResponse -->
### Schema `PaymentsCancelResponse`

Pointer: `#/components/schemas/PaymentsCancelResponse`. Type: object (schema `PaymentsCancelResponse`).

> Response for a cash-in or cash-out cancel operation.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `authorization_id` | integer (schema `AuthorizationID`) | yes | Unique Pismo-generated ID of the authorization created for this request. Returned on 200 and 201 responses, including idempotent replays. | format: "int64"; example: 123 |
| `tracking_id` | string (schema `TrackingID`) | yes | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `account_id` | integer (schema `AccountID`) | no | Pismo account ID. | format: "int64"; example: 8675309 |
| `response_code` | string (schema `ResponseCode`) | yes | Alphanumeric two-character standard card network response code or an alternative custom response code, which provides the precise reason for the success or denial of the operation by the card network, platform, or anti-fraud solution.<br> | example: "57" |
| `denial_code` | string (schema `DenialCode`) | no | Denial code. | example: "DAL" |
| `validation_results` | array of object (schema `ValidationResults`) | no |  |  |
| `validation_results[].name` | string | no | Name of the evaluated rule. | example: "LEDGER" |
| `validation_results[].status` | string | no | Identifies if the rule was approved, rejected, or skipped during the validation flow. | enum: ["APPROVED", "REJECTED", "SKIPPED"]; example: "REJECTED" |
| `validation_results[].reason` | string | no | Status reason why the specific rule was approved, rejected, or skipped. | example: "LEDGER_INSUFFICIENT_FUNDS" |
| `validation_results[].description` | string | no | Description of the validation result. | example: "The authorization amount is greater than the account available limit." |
| `validation_results[].additional_data` | object | no | Additional data for the validation result. This varies from validation to validation, but every denied validation has the `denial_code` and `response_code` fields. |  |

<!-- schema: #/components/schemas/404Transfers -->
### Schema `404Transfers`

Pointer: `#/components/schemas/404Transfers`. Type: object (schema `404Transfers`).

> * WONT0009 - Original authorization not found.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "WONT0009" |
| `message` | string | no |  | example: "Original authorization not found." |

<!-- schema: #/components/schemas/ValidationRules -->
### Schema `ValidationRules`

Pointer: `#/components/schemas/ValidationRules`. Type: object (map of object (schema `RuleConfig`)) (schema `ValidationRules`).

> Validation rules performed in the flow. Each key is a rule name (such as `ACCOUNT_STATUS` or `LEDGER`) and the value is its configuration.

<!-- schema: #/components/schemas/AuthorizationValidations -->
### Schema `AuthorizationValidations`

Pointer: `#/components/schemas/AuthorizationValidations`. Type: object (schema `AuthorizationValidations`).

> Contains additional data to be used in the authorization flow. This field is only considered for authorizations. Cancellations and confirmations will retrieve it based on the original authorization.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `is_device_registered` | boolean | no | Indicates whether the device used for the operation is registered according to the financial institution's security policies. | example: true |
| `associated_ids` | object (schema `AssociatedIDs`) | no | External IDs used in the authorization flow. |  |

<!-- schema: #/components/schemas/AssociatedIDs -->
### Schema `AssociatedIDs`

Pointer: `#/components/schemas/AssociatedIDs`. Type: object (schema `AssociatedIDs`).

> External IDs used in the authorization flow.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payment_id` | string | no | External ID associated with the authorization. | example: "319d00f5-48de-4c71-ad47-40b1e9c4e37f" |
| `origin_id` | string | no | External ID of the origin of the authorization. | example: "CUSTOM_ORIGIN" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Payment_methods.yaml` | tag `Payment methods`: POST /payment-methods/v2/payments/confirm, POST /payment-methods/v2/transfers, POST /payment-methods/v2/transfers/cancel | https://github.com/PismoDevEx/pismo-api-specs | `9b02c87b6e39a1c8…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-transaction-processing-flows` — Transaction processing flows
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-PAY-configure-payment-methods` — Configure payment methods
- `KU-PAY-payment-configurations` — Payment methods configurations overview
- `KU-PAY-payment-methods` — Payment methods
