---
ku_id: KU-API-core-platform-payment-methods--payment-methods-part-01
title: 'API reference: Core platform - Payment methods — Payment methods (part 1 of 3)'
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
- post-authorization
- post-payments
- post-payments-cancel
related_kus:
- KU-CORE-fee-models-create-and-simulate
- KU-CORE-transaction-processing-flows
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-wiac-to-wstm
- KU-ERR-codes-wona
- KU-EVT-catalogue-other-domains
- KU-EVT-client-webhooks-part-01
- KU-PAY-configure-payment-methods
- KU-PAY-payment-configurations
- KU-PAY-payment-methods
- KU-SELL-how-merchant-settlements-are-processed
- KU-SELL-managing-merchant-transactions
- KU-SELL-seller-marketplace-implementation-steps
specification_version: 1.0.0
---

# API reference: Core platform - Payment methods — Payment methods (part 1 of 3)

**KU ID:** `KU-API-core-platform-payment-methods--payment-methods-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Payment methods` in `api-specs/Core_platform_-_Payment_methods.yaml` (“Core platform - Payment methods”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage cash-in and cash-out payments and P2P transfers.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /payment-methods/v1/authorization` | `post-authorization` | Request authorization | no |
| `POST /payment-methods/v2/payments` | `post-payments` | Create cash-in or cash-out | no |
| `POST /payment-methods/v2/payments/cancel` | `post-payments-cancel` | Cancel cash-in or cash-out | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payment-methods/v1/authorization operationId=post-authorization -->
### `POST /payment-methods/v1/authorization` — Request authorization

- **operationId:** `post-authorization`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment methods`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Use this endpoint to request a new authorization, cancel an existing authorization, or confirm an existing authorization.
>
> With this endpoint, you can set `validation_rules` to control the rules in this flow, such as disabling a rule, changing the response code and denial code, and forcing a rule.
>
> Refer to the [Payment methods](doc:payment-methods) guide for additional information.
>
> This endpoint generates [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) and [Payment methods authorization created](https://developers.pismo.io/events/docs/payment-methods-authorization-1) events.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Request authorization processing body.

**Content type `application/json`** — schema: object (schema `PaymentMethodsAuthorizationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | number | no | Total amount of the authorization being requested in the local currency of the acquirer or source location of the transaction.<br><br>**REQUIRED** in authorization requests, and optional in cancellation and confirmation requests. If this amount is omitted, the platform confirms or cancels the same amount as the original authorization. If the original authorization is not available and a forced confirmation is requested, this field is also required.<br> | example: 100 |
| `currency_code` | string | yes | ISO-4217 alphabetic or numeric (3 characters) authorization currency code. For example, either BRL or 986 for Brazilian real. | example: "986" |
| `mti` | string | yes | Message type identifier. Indicates if this is an authorization, cancellation, or confirmation request.<br>- `0100` - authorization request<br>- `0120` - authorization advice request (coming soon)<br>- `0200` - authorization SMS request<br>- `0202` - confirmation request<br>- `0400` - cancellation request<br>- `0402` - confirmation of cancellation<br>- `0420` - cancellation advice request (coming soon)<br> | enum: ["0100", "0120", "0200", "0202", "0400", "0402", "0420"] |
| `network` | string | yes | Network originating this request. | example: "Mastercard" |
| `account_id` | integer | no | Pismo ID of the account to be used as the owner of this request. <br><br>**REQUIRED** if `document_number`, card information (`card.pan` or `card.stored_id`), bank information (`bank.account` and `bank.branch`) are not provided.<br> | example: 123 |
| `authentication` | object (schema `Authentication`) | no | Authentication object. |  |
| `authorization_code` | string | no | Alphanumeric code generated in an authorization request and assigned to the authorization response. | example: "ABC123" |
| `authorization_datetime` | string | no | Date and time when the authorization request took place outside the Pismo platform, formatted in UTC-0 RFC3339 with milliseconds (yyyy-MM-ddThh:mm:ss.SSSZ). | format: "date-time"; example: "2023-01-01T00:00:00.000Z" |
| `authorization_mode` | string | no | Defines the mode of the authorization being requested. Credit cards can operate only in `CREDIT` mode while debit cards (from savings or checking accounts) can operate only in `DEBIT` code. Combo and multi-application cards can operate in both modes. <br><br>**REQUIRED** for card authorization requests (idenfified by `card.pan` or `card.stored_id`) with the `mti` values `0100` and `0120`.<br> | enum: ["CREDIT", "DEBIT"] |
| `bank` | object | no | Identifies bank's information. If provided, both bank `account` and `branch` fields are **REQUIRED**. |  |
| `bank.account` | string | no | Identifies the bank's account. This field should be used in the requests authorized based on the client's bank. <br><br>**REQUIRED** together with the `bank.branch` field if `account_id`, `document_number`, or card information (`card.pan` or `card.stored_id`) are not provided.<br> | example: "2146125" |
| `bank.branch` | string | no | Identifies the bank's branch. This field should be used in requests authorized based on the client's bank. <br><br>**REQUIRED** together with the `bank.account` field if `account_id`, `document_number`, or card information (`card.pan` or `card.stored_id`) are not provided.<br> | example: "15235" |
| `beneficiary_id` | string | no | Unique string identifier for the beneficiary associated with the account. | example: "2c298321-bc21-4039-9c45-780cc6d4ec46" |
| `calculated_amounts` | object (schema `CalculatedAmountsAuthorization`) | no | Calculated amounts for the authorization. |  |
| `card` | object | no | Contains all information related to the card used to perform this authorization. <br><br>**REQUIRED** if `account_id`, `document_number`, or bank information (`bank.account` and `bank.branch`) are not provided.<br> |  |
| `card.pan` | string | no | Primary account number of the card being used for authorization. Either this field or `stored_id` is **REQUIRED** to identify the card to be used in the authorization process. | example: "5555550000000001" |
| `card.stored_id` | string | no | ID of the card-on-file stored in the platform. Either this field or `pan` is **REQUIRED** to identify the card to be used in the authorization process. | example: "652973000071210932" |
| `card.expiration_date` | string | no | Card expiration date in the YYMM format entered by the cardholder at the authorization request. | example: "2601" |
| `card.cvv2` | string | no | CVV2 entered by the cardholder at the authorization request. | example: "123" |
| `card.track1_data` | string | no | Track1 data captured at the terminal while performing an authorization with magnet stripe. | example: "123" |
| `card.track2_data` | string | no | Track2 data captured at the terminal while performing an authorization with magnet stripe. |  |
| `card.pin_block` | string | no | Pin block related to the password entered by the cardholder at the authorization request. |  |
| `card.cryptogram_data` | object | no | Cryptogram data captured at the terminal while performing an authorization using chip. |  |
| `card.cryptogram_data.amount_authorized` | string | no | Amount authorized referring to the tag 9F02. |  |
| `card.cryptogram_data.application_cryptogram` | string | no | Application cryptogram information referring to the tag 9F26. |  |
| `card.cryptogram_data.application_interchange_profile` | string | no | Application interchange profile referring to the tag 82. |  |
| `card.cryptogram_data.application_transaction_counter` | string | no | Application transaction counter referring to the tag 9F36. |  |
| `card.cryptogram_data.application_version_number` | string | no | Application version number referring to the tag 9F09. |  |
| `card.cryptogram_data.cardholder_verification_method` | string | no | Cardholder verification method (CVM) results referring to the tag 9F34. |  |
| `card.cryptogram_data.cryptogram_information_data` | string | no | Cryptogram information data referring to the tag 9F27. |  |
| `card.cryptogram_data.dedicated_file_name` | string | no | Dedicated file name referring to the tag 84. |  |
| `card.cryptogram_data.interface_device_serial_number` | string | no | Interface device serial number referring to the tag 9F1E. |  |
| `card.cryptogram_data.issuer_application_data` | string | no | Issuer application data referring to the tag 9F10. |  |
| `card.cryptogram_data.issuer_authentication_data` | string | no | Issuer authentication data referring to the tag 91. |  |
| `card.cryptogram_data.issuer_script_template` | string | no | Issuer script template referring to the tag 71. |  |
| `card.cryptogram_data.pan_sequence_number` | string | no | Pan sequence number referring to the tag 5F34. |  |
| `card.cryptogram_data.terminal_capabilities` | string | no | Terminal capabilities information referring to the tag 9F33. |  |
| `card.cryptogram_data.terminal_country_code` | string | no | Application interchange profile referring to the tag 9F1A. |  |
| `card.cryptogram_data.terminal_type` | string | no | Terminal type referring to the tag 9F35. |  |
| `card.cryptogram_data.terminal_verification_result` | string | no | Terminal verification result (TVR) referring to the tag 95. |  |
| `card.cryptogram_data.transaction_category_code` | string | no | Transaction category code referring to the tag 9F53. |  |
| `card.cryptogram_data.transaction_currency_code` | string | no | Transaction currency code referring to the tag 5F2A. |  |
| `card.cryptogram_data.transaction_date` | string | no | Transaction date referring to the tag 9A. |  |
| `card.cryptogram_data.transaction_sequence_counter` | string | no | Transaction sequence counter referring to the tag 9F41. |  |
| `card.cryptogram_data.transaction_type` | string | no | Transaction type referring to the tag 9C. |  |
| `card.cryptogram_data.unpredictable_number` | string | no | Unpredictable number referring to the tag 9F37. |  |
| `clearing_type` | string | no | Defines whether confirmation is performed at request time (`ONLINE`) or pending a confirmation request (`OFFLINE`). If not provided, the platform uses the `mti` value to define this behavior (`0100` for `OFFLINE` and `0200` for `ONLINE`). | enum: ["ONLINE", "OFFLINE"] |
| `document_number` | string | no | Document number related to the account owner of this request. Used in the requests authorized based on client document number. <br><br>**REQUIRED** if `account_id`, card information (`card.pan` or `card.stored_id`), or bank information (`bank.account` and `bank.branch`) are not provided.<br> | example: "39947739977" |
| `description` | string | no | Optional text that describes the operation and appears on the customer's statement as a descriptive line for the transaction. If provided, this value populates the `soft_descriptor` field of the resulting transactions. If not provided, the `soft_descriptor` field for the transaction inherits its value from the transaction type’s `description` field. | example: "Custom purchase." |
| `entry_mode` | string | no | Defines the authorization entry mode (two first characters) and pin entry capability (third character). This field should have either two or three digits depending on the usage of the information. <br><br>**REQUIRED** for authorization requests with the `mti` values `0100`, `0120` and `0200`.<br> | example: "051 # 05 - Chip / 1 - Pin supported" |
| `has_error` | boolean | no | This flag must be used only in the confirmation flow (`mti` - `0202`). If set to `true`, this indicates that the confirmation operation has an error and the platform will cancel any approved authorization related to this request instead of confirming it. | default: false; example: true |
| `installment_plan_id` | string | no | ID of the installment plan that should be used to calculate this purchase. | example: "PLAN_0_24" |
| `merchant` | object | no | All information related to the merchant where the authorization took place. <br><br>Only used for authorization requests with the `mti` values `0100` and `0120`.<br> |  |
| `merchant.id` | string | no | Identifies the card acceptor that defines the point of the transaction in both local and interchange environments. This is used as a merchant ID to uniquely identify the merchant in a POS transaction.<br><br>**REQUIRED** if the `merchant` object is filled in.<br> | example: "12399" |
| `merchant.category_code` | string | no | Merchant category code (MCC) of the merchant’s type of business or service. <br><br>**REQUIRED** if the `merchant` object is filled in.<br> | example: "5099" |
| `merchant.name` | string | no | Name of the merchant where the authorization is performed. <br><br>**REQUIRED** if the `merchant` object is filled in.<br> | example: "Acme" |
| `merchant.city` | string | no | City of the merchant where the authorization is performed. | example: "San Diego" |
| `merchant.country` | string | no | Country code of the merchant where the authorization is performed. <br><br>**REQUIRED** if the `merchant` object is filled in.<br> | example: "USA" |
| `merchant.terminal_id` | string | no | ID of the terminal at the card acceptor location. | example: "12345699" |
| `merchant.marketplace_id` | string | no | ID of the marketplace where this purchase took place.<br><br>**REQUIRED** if the `merchant` object is filled in.<br> | example: "mk123456" |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `nsu` | string | no | Sequential unique number that identifies this authorization. | example: "12789223" |
| `number_of_installments` | integer | no | Number of installments in this authorization request. Purchases without installments should have the value 1. | minimum: 1; maximum: 100; example: 12 |
| `original_authorization_id` | integer | no | This field can be used to match the original authorization in cancellation and confirmation requests. This should contain the same value received in the `authorization_id` field for the authorization response. <br><br>**REQUIRED** for cancellation and confirmation requests with the `mti` values `0400`, `0420`, `0402` and `0202` if the `original_tracking_id` is not provided.<br>**NOT REQUIRED** for confirmation requests when the force original authorization configuration is enabled.<br> | example: 58799254 |
| `original_tracking_id` | string | no | This field can be used to match the original authorization in cancellation and confirmation requests. This should contain the same value received in the `tracking_id` field for the authorization response. <br><br>**REQUIRED** for cancellation and confirmation requests with the `mti` values `0400`, `0420`, `0402` and `0202` if the `original_authorization_id` is not provided.<br>**NOT REQUIRED** for confirmation requests when the force original authorization configuration is enabled.<br> | example: "ab879e9e-433b-499f-a77b-4e90ab509afd" |
| `posting_date` | string | no | Date of the statement when the authorization will be posted. <br>For authorization with installments, this is where the first installment will be posted being followed by the other installments on next statements.<br>This field will be ignored if a `statement_id` is provided.<br>If there is an external calculation call, the response of that calculation will take precedence over this field.<br> | format: "date"; example: "2023-01-01T00:00:00.000Z" |
| `pre_authorization` | boolean (schema `PreAuthorization`) | no | If set to `true`, this flag indicates that the operation is pre-authorized and requires additional confirmation. | default: false; example: false |
| `processing_code` | string | no | Unique alphanumeric identifier that defines how the Pismo platform handles this financial authorization. <br><br>**Required when:**  <br>  - `mti` is `0100`, `0120`, or `0200`<br>  - `mti` is `0202` or `0402` and force original authorization configuration is enabled<br> | example: "00AB01" |
| `program_id` | integer | no | This field is used for authorizations that are based on a document number. If this field is provided, the platform uses it to determine which account to use for the authorization with the same `program_id` or decline if there is no account in this program. If this field is not provided, the platform selects the account based on the configurations.<br> | example: 123 |
| `statement_id` | integer | no | Pismo internal ID of the statement when the authorization will be posted. <br>For authorization with installments, this is where the first installment will be posted being followed by the other installments on next statements.<br>This field takes precedence over the `posting_date` when both are present.<br>If there is an external calculation call, the response of that calculation takes precendence over this field.<br> | example: 1234455 |
| `tid` | string | no | Transaction ID received with the authorization message. | example: "10119031908214800419" |
| `tracking_id` | string | no | Unique tracking ID used to identify the authorization request. If not provided, the platform generates a new one and the request is handled as a new request. Different requests using the same tracking ID are considered to be the same request and return the same result. | example: "ab879e9e-433b-499f-a77b-4e90ab509afd" |
| `validation_rules` | object (map of object (schema `RuleConfig`)) (schema `ValidationRules`) | no | Validation rules performed in the flow. Each key is a rule name (such as `ACCOUNT_STATUS` or `LEDGER`) and the value is its configuration. | example: {"ACCOUNT_STATUS": {"disable": false, "force": false, "denial_reasons": {"ACCOUNT_STATUS_NOT_PERMITTED": {"response_code": "57", "denial_code": "DAL"}}}, "LEDGER": {"denial_reasons": {"LEDGER_INSUFFICIENT_FUNDS": {"response_code": "51", "denial_code": "DAL"}, "LEDGER_NOT_ALLOWED_OPERATION": {"response_code": "57", "denial_code": "DAL"}}}} |
| `authorization_validations` | object (schema `AuthorizationValidations`) | no | Contains additional data to be used in the authorization flow. This field is only considered for authorizations. Cancellations and confirmations will retrieve it based on the original authorization. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Authorization was processed successfully, existing authorization with the corresponding `tracking_id` returned. | `application/json`: object (schema `PaymentMethodsAuthorizationResponse`) |
| 201 | Authorization request was processed successfully | `application/json`: object (schema `PaymentMethodsAuthorizationResponse`) |
| 400 | Bad Request | `application/json`: array of object (schema `NewErrorModel`) (schema `ErrorsResponse`) |
| 401 | Unauthorized | `application/json`: object |
| 403 | Forbidden | `application/json`: object |
| 422 | Unprocessable request | `application/json`: array of object (schema `NewErrorModel`) (schema `ErrorsResponse`) |
| 500 | Internal server error | `application/json`: array of object (schema `NewErrorModel`) (schema `ErrorsResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | yes | Pismo ID of the account assigned as the owner of this request. | example: 123 |
| `authorization_code` | string | yes | Alphanumeric code generated in an authorization request and assigned to the authorization response. Used on cancellation or confirmation requests to match the original authorization. | example: "ABC123" |
| `authorization_id` | integer | yes | Pismo ID of the authorization created for this request. |  |
| `calculated_amounts` | object | yes |  |  |
| `calculated_amounts.contract_amount` | number | no | Total amount of the authorization after calculation with the addition of any necessary fees. | example: 100 |
| `calculated_amounts.principal_amount` | number | no | Total amount of the authorization after calculation without the addition of any necessary fees. | example: 100 |
| `calculated_amounts.postings` | object (map of number) | no | Information about the applied fee or tax. |  |
| `calculated_amounts.rates` | object (map of number) | no | Rates used to calculate fees and taxes represented on Postings object. |  |
| `number_of_installments` | integer | yes | Number of installments in this authorization request. Purchases without installments should have the value `1`. | example: 12 |
| `response_code` | string | yes | Response code indicating the decision for the authorization request. Refer to [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations) for details. | example: "00" |
| `tracking_id` | string | yes | Tracking ID used to identify the authorization request. | example: "ab879e9e-433b-499f-a77b-4e90ab509afd" |
| `validation_results` | array of object (schema `ValidationResults`) | yes |  |  |
| `validation_results[].name` | string | no | Name of the evaluated rule. | example: "LEDGER" |
| `validation_results[].status` | string | no | Identifies if the rule was approved, rejected, or skipped during the validation flow. | enum: ["APPROVED", "REJECTED", "SKIPPED"]; example: "REJECTED" |
| `validation_results[].reason` | string | no | Status reason why the specific rule was approved, rejected, or skipped. | example: "LEDGER_INSUFFICIENT_FUNDS" |
| `validation_results[].description` | string | no | Description of the validation result. | example: "The authorization amount is greater than the account available limit." |
| `validation_results[].additional_data` | object | no | Additional data for the validation result. This varies from validation to validation, but every denied validation has the `denial_code` and `response_code` fields. |  |
| `custom_message` | string | no | Message customized to describe the authorization response. | example: "Custom message" |
| `denial_code` | string | no | Denial code that indicates the reason why the request was denied. | example: "ABC" |
| `datetime_utc` | string | no | Date and time when the authorization is created inside the Pismo platform in the UTC 0 time zone. | format: "date-time"; example: "2023-01-01T00:00:00.000Z" |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer | yes | Pismo ID of the account assigned as the owner of this request. | example: 123 |
| `authorization_code` | string | yes | Alphanumeric code generated in an authorization request and assigned to the authorization response. Used on cancellation or confirmation requests to match the original authorization. | example: "ABC123" |
| `authorization_id` | integer | yes | Pismo ID of the authorization created for this request. |  |
| `calculated_amounts` | object | yes |  |  |
| `calculated_amounts.contract_amount` | number | no | Total amount of the authorization after calculation with the addition of any necessary fees. | example: 100 |
| `calculated_amounts.principal_amount` | number | no | Total amount of the authorization after calculation without the addition of any necessary fees. | example: 100 |
| `calculated_amounts.postings` | object (map of number) | no | Information about the applied fee or tax. |  |
| `calculated_amounts.rates` | object (map of number) | no | Rates used to calculate fees and taxes represented on Postings object. |  |
| `number_of_installments` | integer | yes | Number of installments in this authorization request. Purchases without installments should have the value `1`. | example: 12 |
| `response_code` | string | yes | Response code indicating the decision for the authorization request. Refer to [Authorization validation rules for platform operations](https://developers.pismo.io/pismo-docs/docs/authorization-validation-rules-for-platform-operations) for details. | example: "00" |
| `tracking_id` | string | yes | Tracking ID used to identify the authorization request. | example: "ab879e9e-433b-499f-a77b-4e90ab509afd" |
| `validation_results` | array of object (schema `ValidationResults`) | yes |  |  |
| `validation_results[].name` | string | no | Name of the evaluated rule. | example: "LEDGER" |
| `validation_results[].status` | string | no | Identifies if the rule was approved, rejected, or skipped during the validation flow. | enum: ["APPROVED", "REJECTED", "SKIPPED"]; example: "REJECTED" |
| `validation_results[].reason` | string | no | Status reason why the specific rule was approved, rejected, or skipped. | example: "LEDGER_INSUFFICIENT_FUNDS" |
| `validation_results[].description` | string | no | Description of the validation result. | example: "The authorization amount is greater than the account available limit." |
| `validation_results[].additional_data` | object | no | Additional data for the validation result. This varies from validation to validation, but every denied validation has the `denial_code` and `response_code` fields. |  |
| `custom_message` | string | no | Message customized to describe the authorization response. | example: "Custom message" |
| `denial_code` | string | no | Denial code that indicates the reason why the request was denied. | example: "ABC" |
| `datetime_utc` | string | no | Date and time when the authorization is created inside the Pismo platform in the UTC 0 time zone. | format: "date-time"; example: "2023-01-01T00:00:00.000Z" |

201 Example `Create authorization request`:

```json
{
  "authorization_id": 123,
  "tracking_id": "auth-9944",
  "account_id": 8899,
  "authorization_code": "MQ94GG",
  "response_code": "00",
  "denial_code": "",
  "custom_message": "",
  "datetime_utc": "2025-07-15T05:50:47.049Z",
  "number_of_installments": 2,
  "calculated_amounts": {
    "contract_amount": 10510,
    "principal_amount": 10000,
    "installment_amount": 5255,
    "additional_financial_details": {},
    "postings": {
      "fixed_amount": 10,
      "percentage_amount": 500
    },
    "rates": {
      "conversion_rate": 1
    },
    "installments": [
      {
        "number": 1,
        "installment_amount": 5255,
        "principal_amount": 5000
      },
      {
        "number": 2,
        "installment_amount": 5255,
        "principal_amount": 5000
      }
    ]
  },
  "validation_results": [
    {
      "name": "CARD",
      "status": "APPROVED",
      "reason": "CARD_FOUND",
      "description": "Card was found.",
      "additional_data": {
        "card_hash": "9XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX="
      }
    },
    {
      "name": "CARD_AUTHORIZATION_MODE",
      "status": "APPROVED",
      "reason": "CARD_AUTHORIZATION_MODE_VALID",
      "description": "Card has authorization mode enabled.",
      "additional_data": {
        "authorization_mode": "CREDIT"
      }
    },
    {
      "name": "BANK_ACCOUNT",
      "status": "APPROVED",
      "reason": "BANK_ACCOUNT_FOUND",
      "description": "Bank account was found.",
      "additional_data": {
        "account_id": 99999
      }
    },
    {
      "name": "ACCOUNT",
      "status": "APPROVED",
      "reason": "ACCOUNT_FOUND",
      "description": "Account was found.",
      "additional_data": {
        "account_id": 2417
      }
    },
    {
      "name": "DOCUMENT_NUMBER",
      "status": "APPROVED",
      "reason": "DOCUMENT_NUMBER_FOUND",
      "description": "Account was found successfully based on document number.",
      "additional_data": {
        "document_number_present": true
      }
    },
    {
      "name": "PROCESSING_CODE_MAPPER",
      "status": "APPROVED",
      "reason": "PROCESSING_CODE_MAPPED",
      "description": "Processing code was mapped successfully.",
      "additional_data": {
        "mapped_processing_code": "2XXXX0",
        "original_processing_code": "2XXXX0"
      }
    },
    {
      "name": "ACCEPTANCE",
      "status": "APPROVED",
      "reason": "ACCEPTANCE_FOUND",
      "description": "Payment methods acceptances were found."
    },
    {
      "name": "CONFIG",
      "status": "APPROVED",
      "reason": "CONFIG_FOUND",
      "description": "Payment methods configuration was found."
    },
    {
      "name": "PLATFORM_AUTHENTICATION",
      "status": "APPROVED",
      "reason": "PLATFORM_AUTHENTICATION_SUCCESSFUL",
      "description": "Request was authenticated successfully."
    },
    {
      "name": "PROGRAM_PARAMETER",
      "status": "APPROVED",
      "reason": "PROGRAM_PARAMETER_FOUND",
      "description": "Program parameters were found successfully.",
      "additional_data": {
        "program_id": 99
      }
    },
    {
      "name": "MERCHANT",
      "status": "APPROVED",
      "reason": "MERCHANT_VALID_STATUS",
      "description": "Merchant has valid status.",
      "additional_data": {
        "marketplace_id": "FL-123456",
        "status": "ACTIVE",
        "merchant_external_id": "102030"
      }
    },
    {
      "name": "CARD_ARQC",
      "status": "SKIPPED",
      "reason": "CARD_ARQC_SKIPPED",
      "description": "ARQC validation was skipped.",
      "additional_data": {
        "arqc_presence": false,
        "cause": "Authorization is not performed using a card."
      }
    },
    {
      "name": "CARD_PIN",
      "status": "SKIPPED",
      "reason": "CARD_PIN_SKIPPED",
      "description": "PIN validation was skipped.",
      "additional_data": {
        "pin_presence": false,
        "cause": "Authorization is not performed using a card."
      }
    },
    {
      "name": "CARD_CVV",
      "status": "SKIPPED",
      "reason": "CARD_CVV_SKIPPED",
      "description": "CVV validation was skipped.",
      "additional_data": {
        "track1_presence": false,
        "track2_presence": false,
        "cause": "Authorization is not performed using a card.",
        "code": ""
      }
    },
    {
      "name": "CARD_CVV2",
      "status": "SKIPPED",
      "reason": "CARD_CVV2_SKIPPED",
      "description": "CVV2 validation was skipped.",
      "additional_data": {
        "cvv2_presence": false,
        "entered_expiration_date": "2806",
        "cause": "Authorization is not performed using a card.",
        "code": ""
      }
    },
    {
      "name": "CARD_STATUS",
      "status": "APPROVED",
      "reason": "CARD_STATUS_VALID",
      "description": "Card is in valid status.",
      "additional_data": {
        "card_status": "NORMAL"
      }
    },
    {
      "name": "CARD_ENTERED_EXPIRATION_DATE",
      "status": "APPROVED",
      "reason": "CARD_ENTERED_EXPIRATION_DATE_VALID",
      "description": "Entered expiration date matches card expiration date.",
      "additional_data": {
        "card_expiration_date": "2806",
        "entered_expiration_date": "2806"
      }
    },
    {
      "name": "CARD_EXPIRATION_DATE",
      "status": "APPROVED",
      "reason": "CARD_NOT_EXPIRED",
      "description": "Card is not expired.",
      "additional_data": {
        "card_expiration_date": "2806"
      }
    },
    {
      "name": "CARD_PASSWORD_TRIES",
      "status": "APPROVED",
      "reason": "CARD_PASSWORD_TRIES_ALLOWED",
      "description": "Password tries are within configured threshold.",
      "additional_data": {
        "current_password_tries": 0,
        "password_tries_allowed": 3
      }
    },
    {
      "name": "CARD_ATC",
      "status": "APPROVED",
      "reason": "CARD_ATC_WITHIN_ALLOWED_RANGE",
      "description": "ATC is within allowed range.",
      "additional_data": {
        "current_atc": "10",
        "previous_atc": "[9,8,7,5,1]",
        "min_offset_parameter": "5",
        "max_offset_parameter": "15"
      }
    },
    {
      "name": "EXTERNAL_CALCULATION",
      "status": "APPROVED",
      "reason": "EXTERNAL_CALCULATION_SUCCESSFUL",
      "description": "External calculation was performed successfully."
    },
    {
      "name": "PAYMENT_METHODS_INTEGRITY",
      "status": "APPROVED",
      "reason": "PAYMENT_METHODS_INTEGRITY_CREATED",
      "description": "Payment methods integrity message was created successfully."
    },
    {
      "name": "ACCOUNT_ID",
      "status": "APPROVED",
      "reason": "ACCOUNT_ID_PERMITTED",
      "description": "Account ID is permitted.",
      "additional_data": {
        "document_number": "6XXXXXXXXXXX9",
        "external_id": "",
        "name": "Marcelito"
      }
    },
    {
      "name": "PROCESSING_CODE",
      "status": "APPROVED",
      "reason": "PROCESSING_CODE_FOUND",
      "description": "Processing code was found."
    },
    {
      "name": "PROCESSING_CODE_TYPE",
      "status": "APPROVED",
      "reason": "PROCESSING_CODE_TYPE_VALID",
      "description": "Processing code has a valid balance impact type."
    },
    {
      "name": "ACCOUNT_LIMITS",
      "status": "APPROVED",
      "reason": "ACCOUNT_LIMITS_FOUND",
      "description": "Account limits were found.",
      "additional_data": {
        "available_credit_limit": 746847632710901.1,
        "available_savings_account_limit": 93477.42,
        "available_total_installment_credit": -226,
        "available_withdrawal_credit": -175,
        "total_credit_limit": 1000,
        "total_installment_credit_limit": 200,
        "withdrawal_credit_limit": 300
      }
    },
    {
      "name": "ACCOUNT_STATUS",
      "status": "APPROVED",
      "reason": "ACCOUNT_STATUS_PERMITTED",
      "description": "Account status is permitted."
    },
    {
      "name": "PROGRAM",
      "status": "APPROVED",
      "reason": "PROGRAM_FOUND",
      "description": "Program was found.",
      "additional_data": {
        "program_type": "PRE-PAGO"
      }
    },
    {
      "name": "BALANCES_CONFIG",
      "status": "APPROVED",
      "reason": "BALANCES_CONFIG_FOUND",
      "description": "Balances configuration was found.",
      "additional_data": {
        "amount": "contract_amount",
        "amount_consider": "principal_amount",
        "consider": [
          "AvailableCreditLimit",
          "OverLimit"
        ],
        "impact": [
          "AvailableCreditLimit"
        ],
        "reset_limit": "last_installment"
      }
    },
    {
      "name": "CURRENCY",
      "status": "APPROVED",
      "reason": "CURRENCY_FOUND",
      "description": "Currency was found.",
      "additional_data": {
        "code": "BRL",
        "numeric_code": "986"
      }
    },
    {
      "name": "RATES",
      "status": "APPROVED",
      "reason": "RATES_APPROVED",
      "description": "Rates calculation was performed.",
      "additional_data": {
        "conversion": {
          "conversion_rate": 0,
          "destination": "986",
          "exchange_rate": 1,
          "origin": "986",
          "spread": 0
        }
      }
    },
    {
      "name": "FLEX_CONTROLS",
      "status": "APPROVED",
      "reason": "FLEX_CONTROLS_APPROVED",
      "description": "Authorization passed flex control evaluation.",
      "additional_data": {
        "dry_run": false,
        "evaluated_controls": [
          {
            "id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4",
            "name": "Purchase 1 Month credit card",
            "evaluation_result": true,
            "deny_code": "MAX_VALUE_P1M",
            "response_code": "63",
            "max_limit": 200000,
            "accumulated_limit": 135127,
            "available_limit": 64873
          }
        ]
      }
    },
    {
      "name": "LEDGER",
      "status": "APPROVED",
      "reason": "LEDGER_APPROVED",
      "description": "Ledger was impacted successfully.",
      "additional_data": {
        "dry_run": false,
        "validation_results": null,
        "account_id": 9999,
        "available_amounts": {
          "validation_status": "APPROVED",
          "details": {
            "result": {
              "available_credit_limit": 746847527710892.1,
              "available_installment_limit": -226,
              "available_savings_account_limit": 93477.42,
              "available_withdraw_limit": -175,
              "held_funds": 91.25,
              "additional_funds": 0,
              "overlimit": 2000000,
              "total_overdraft_limit": 0
            }
          }
        }
      },
      "ledger_operation_status": {
        "validation_status": "APPROVED"
      }
    },
    {
      "name": "ANTI_FRAUD",
      "status": "APPROVED",
      "reason": "ANTI_FRAUD_APPROVED",
      "description": "Authorization passed anti-fraud evaluation.",
      "additional_data": {
        "executed_steps": [],
        "force_approve": false,
        "override": false,
        "override_type": "NONE"
      }
    },
    {
      "name": "AUTHORIZATION",
      "status": "APPROVED",
      "reason": "AUTHORIZATION_CREATED",
      "description": "Authorization was created successfully."
    },
    {
      "name": "PAYMENT_METHODS_PERSISTENCE",
      "status": "APPROVED",
      "reason": "PAYMENT_METHODS_PERSISTENCE_CREATED",
      "description": "Payment methods record was created successfully."
    }
  ]
}
```

201 Example `Confirm authorization request`:

```json
{
  "authorization_id": 2413411561,
  "tracking_id": "3277a9b7-81cd-403c-852a-d632b47fbcae",
  "account_id": 2417,
  "authorization_code": "MMEYFR",
  "response_code": "00",
  "denial_code": "",
  "custom_message": "",
  "datetime_utc": "2025-07-15T13:34:57.221Z",
  "number_of_installments": 2,
  "calculated_amounts": {
    "contract_amount": 10000,
    "principal_amount": 10000,
    "installment_amount": 5000,
    "additional_financial_details": null,
    "postings": {},
    "rates": {
      "conversion_rate": 1
    },
    "installments": [
      {
        "number": 1,
        "installment_amount": 5000,
        "principal_amount": 5000,
        "amortization_amount": 0
      },
      {
        "number": 2,
        "installment_amount": 5000,
        "principal_amount": 5000,
        "amortization_amount": 0
      }
    ]
  },
  "validation_results": [
    {
      "name": "CARD",
      "status": "APPROVED",
      "reason": "CARD_FOUND",
      "description": "Card was found successfully.",
      "additional_data": {
        "card_hash": "9XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX="
      }
    },
    {
      "name": "CARD_AUTHORIZATION_MODE",
      "status": "APPROVED",
      "reason": "CARD_AUTHORIZATION_MODE_VALID",
      "description": "Card has authorization mode enabled.",
      "additional_data": {
        "authorization_mode": "CREDIT"
      }
    },
    {
      "name": "BANK_ACCOUNT",
      "status": "APPROVED",
      "reason": "BANK_ACCOUNT_FOUND",
      "description": "Bank account was found.",
      "additional_data": {
        "account_id": 9999
      }
    },
    {
      "name": "ACCOUNT",
      "status": "APPROVED",
      "reason": "ACCOUNT_FOUND",
      "description": "Account was found.",
      "additional_data": {
        "account_id": 2417
      }
    },
    {
      "name": "AUTHORIZATION_RETRIEVAL",
      "status": "APPROVED",
      "reason": "AUTHORIZATION_RETRIEVAL_SUCCESSFUL",
      "description": "Authorization was retrieved successfully."
    },
    {
      "name": "DOCUMENT_NUMBER",
      "status": "APPROVED",
      "reason": "DOCUMENT_NUMBER_FOUND",
      "description": "Account was found successfully based on document number.",
      "additional_data": {
        "document_number_present": true
      }
    },
    {
      "name": "PROCESSING_CODE_MAPPER",
      "status": "APPROVED",
      "reason": "PROCESSING_CODE_MAPPED",
      "description": "Processing code was mapped successfully.",
      "additional_data": {
        "mapped_processing_code": "218327",
        "original_processing_code": "218327"
      }
    },
    {
      "name": "ACCEPTANCE",
      "status": "APPROVED",
      "reason": "ACCEPTANCE_FOUND",
      "description": "Payment methods acceptances were found."
    },
    {
      "name": "CONFIG",
      "status": "APPROVED",
      "reason": "CONFIG_FOUND",
      "description": "Payment methods configuration was found."
    },
    {
      "name": "MERCHANT",
      "status": "APPROVED",
      "reason": "MERCHANT_VALID_STATUS",
      "description": "Merchant has valid status.",
      "additional_data": {
        "merchant_external_id": "FL-123456",
        "status": "ACTIVE",
        "marketplace_id": "102030"
      }
    },
    {
      "name": "EXTERNAL_CALCULATION",
      "status": "APPROVED",
      "reason": "EXTERNAL_CALCULATION_SUCCESSFUL",
      "description": "External calculation was performed successfully."
    },
    {
      "name": "PAYMENT_METHODS_INTEGRITY",
      "status": "APPROVED",
      "reason": "PAYMENT_METHODS_INTEGRITY_CREATED",
      "description": "Payment methods integrity message was created successfully."
    },
    {
      "name": "PAYMENT_METHODS_PERSISTENCE",
      "status": "APPROVED",
      "reason": "PAYMENT_METHODS_PERSISTENCE_CREATED",
      "description": "Payment methods record was created successfully."
    },
    {
      "name": "ACCOUNT_ID",
      "status": "APPROVED",
      "reason": "ACCOUNT_ID_PERMITTED",
      "description": "Account ID is permitted.",
      "additional_data": {
        "document_number": "6XXXXXXXXXX9",
        "external_id": "",
        "name": "Test org"
      }
    },
    {
      "name": "ORIGINAL_AUTHORIZATION",
      "status": "APPROVED",
      "reason": "ORIGINAL_AUTHORIZATION_APPROVED",
      "description": "Original authorization validation was approved."
    },
    {
      "name": "PROCESSING_CODE",
      "status": "APPROVED",
      "reason": "PROCESSING_CODE_FOUND",
      "description": "Processing code was found."
    },
    {
      "name": "PROCESSING_CODE_TYPE",
      "status": "APPROVED",
      "reason": "PROCESSING_CODE_TYPE_VALID",
      "description": "Processing code has a valid balance impact type."
    },
    {
      "name": "ACCOUNT_LIMITS",
      "status": "APPROVED",
      "reason": "ACCOUNT_LIMITS_FOUND",
      "description": "Account limits were found."
    },
    {
      "name": "PROGRAM",
      "status": "APPROVED",
      "reason": "PROGRAM_FOUND",
      "description": "Program was found.",
      "additional_data": {
        "program_type": "PRE-PAGO"
      }
    }
  ]
}
```

201 Example `Cancel authorization response`:

```json
{
  "authorization_id": 2413411561,
  "tracking_id": "3277a9b7-81cd-403c-852a-d632b47fbcae",
  "account_id": 2417,
  "authorization_code": "MMEYFR",
  "response_code": "00",
  "denial_code": "",
  "custom_message": "",
  "datetime_utc": "2025-07-15T13:34:57.221Z",
  "number_of_installments": 2,
  "calculated_amounts": {
    "contract_amount": 10000,
    "principal_amount": 10000,
    "installment_amount": 5000,
    "additional_financial_details": null,
    "postings": {},
    "rates": {
      "conversion_rate": 1
    },
    "installments": [
      {
        "number": 1,
        "installment_amount": 5000,
        "principal_amount": 5000,
        "amortization_amount": 0
      },
      {
        "number": 2,
        "installment_amount": 5000,
        "principal_amount": 5000,
        "amortization_amount": 0
      }
    ]
  },
  "validation_results": [
    {
      "name": "CARD",
      "status": "APPROVED",
      "reason": "CARD_FOUND",
      "description": "Card was found.",
      "additional_data": {
        "card_hash": "9XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX="
      }
    },
    {
      "name": "CARD_AUTHORIZATION_MODE",
      "status": "APPROVED",
      "reason": "CARD_AUTHORIZATION_MODE_VALID",
      "description": "Card has authorization mode enabled.",
      "additional_data": {
        "authorization_mode": "CREDIT"
      }
    },
    {
      "name": "BANK_ACCOUNT",
      "status": "APPROVED",
      "reason": "BANK_ACCOUNT_FOUND",
      "description": "Bank account was found.",
      "additional_data": {
        "account_id": 99999
      }
    },
    {
      "name": "ACCOUNT",
      "status": "APPROVED",
      "reason": "ACCOUNT_FOUND",
      "description": "Account was found.",
      "additional_data": {
        "account_id": 2417
      }
    },
    {
      "name": "AUTHORIZATION_RETRIEVAL",
      "status": "APPROVED",
      "reason": "AUTHORIZATION_RETRIEVAL_SUCCESSFUL",
      "description": "Authorization was retrieved successfully."
    },
    {
      "name": "DOCUMENT_NUMBER",
      "status": "APPROVED",
      "reason": "DOCUMENT_NUMBER_FOUND",
      "description": "Account was found successfully based on document number.",
      "additional_data": {
        "document_number_present": true
      }
    },
    {
      "name": "ACCEPTANCE",
      "status": "APPROVED",
      "reason": "ACCEPTANCE_FOUND",
      "description": "Payment methods acceptances were found."
    },
    {
      "name": "CONFIG",
      "status": "APPROVED",
      "reason": "CONFIG_FOUND",
      "description": "Payment methods configuration was found."
    },
    {
      "name": "MERCHANT",
      "status": "APPROVED",
      "reason": "MERCHANT_VALID_STATUS",
      "description": "Merchant has valid status.",
      "additional_data": {
        "marketplace_id": "FL-123456",
        "status": "ACTIVE",
        "merchant_external_id": "102030"
      }
    },
    {
      "name": "EXTERNAL_CALCULATION",
      "status": "APPROVED",
      "reason": "EXTERNAL_CALCULATION_SUCCESSFUL",
      "description": "External calculation was performed successfully."
    },
    {
      "name": "PAYMENT_METHODS_INTEGRITY",
      "status": "APPROVED",
      "reason": "PAYMENT_METHODS_INTEGRITY_CREATED",
      "description": "Payment methods integrity message was created successfully."
    },
    {
      "name": "PAYMENT_METHODS_PERSISTENCE",
      "status": "APPROVED",
      "reason": "PAYMENT_METHODS_PERSISTENCE_CREATED",
      "description": "Payment methods record was created successfully."
    },
    {
      "name": "ACCOUNT_ID",
      "status": "APPROVED",
      "reason": "ACCOUNT_ID_PERMITTED",
      "description": "Account ID is permitted.",
      "additional_data": {
        "document_number": "6XXXXXXXXXXX9",
        "external_id": "",
        "name": "Marcelito"
      }
    },
    {
      "name": "ORIGINAL_AUTHORIZATION",
      "status": "APPROVED",
      "reason": "ORIGINAL_AUTHORIZATION_APPROVED",
      "description": "Original authorization validation was approved."
    },
    {
      "name": "PROCESSING_CODE",
      "status": "APPROVED",
      "reason": "PROCESSING_CODE_FOUND",
      "description": "Processing code was found."
    },
    {
      "name": "PROCESSING_CODE_TYPE",
      "status": "APPROVED",
      "reason": "PROCESSING_CODE_TYPE_VALID",
      "description": "Processing code has a valid balance impact type."
    },
    {
      "name": "ACCOUNT_LIMITS",
      "status": "APPROVED",
      "reason": "ACCOUNT_LIMITS_FOUND",
      "description": "Account limits were found."
    },
    {
      "name": "ACCOUNT_STATUS",
      "status": "SKIPPED",
      "reason": "ACCOUNT_STATUS_SKIPPED",
      "description": "Account status validation was skipped.",
      "additional_data": {
        "cause": "Cancellations are forced operations and does not need to run this validation."
      }
    },
    {
      "name": "PROGRAM",
      "status": "APPROVED",
      "reason": "PROGRAM_FOUND",
      "description": "Program was found.",
      "additional_data": {
        "program_type": "PRE-PAGO"
      }
    },
    {
      "name": "REMAINING_CANCELLATION_BALANCE",
      "status": "APPROVED",
      "reason": "REMAINING_CANCELLATION_BALANCE_APPROVED",
      "description": "Remaining cancellation balance validation for this authorization was approved."
    },
    {
      "name": "RATES",
      "status": "APPROVED",
      "reason": "RATES_APPROVED",
      "description": "Rates calculation was performed.",
      "additional_data": {
        "conversion": {
          "conversion_rate": 0,
          "destination": "986",
          "exchange_rate": 1,
          "origin": "986",
          "spread": 0
        }
      }
    },
    {
      "name": "FLEX_CONTROLS",
      "status": "APPROVED",
      "reason": "FLEX_CONTROLS_APPROVED",
      "description": "Authorization passed flex control evaluation.",
      "additional_data": {
        "dry_run": false,
        "evaluated_controls": [
          {
            "id": "bb975c75-ae31-48e8-ac0b-57c677fdd0e4",
            "name": "Purchase 1 Month credit card",
            "evaluation_result": true,
            "deny_code": "MAX_VALUE_P1M",
            "response_code": "63",
            "max_limit": 200000,
            "accumulated_limit": 135127,
            "available_limit": 64873
          }
        ]
      }
    },
    {
      "name": "LEDGER",
      "status": "APPROVED",
      "reason": "LEDGER_APPROVED",
      "description": "Ledger was impacted successfully.",
      "additional_data": {
        "dry_run": false,
        "validation_results": null,
        "account_id": 9999,
        "available_amounts": {
          "validation_status": "APPROVED",
          "details": {
            "result": {
              "available_credit_limit": 746847527710892.1,
              "available_installment_limit": -226,
              "available_savings_account_limit": 93477.42,
              "available_withdraw_limit": -175,
              "held_funds": 91.25,
              "additional_funds": 0,
              "overlimit": 2000000,
              "total_overdraft_limit": 0
            }
          }
        }
      },
      "ledger_operation_status": {
        "validation_status": "APPROVED"
      }
    },
    {
      "name": "AUTHORIZATION",
      "status": "APPROVED",
      "reason": "AUTHORIZATION_CREATED",
      "description": "Authorization was created successfully."
    },
    {
      "name": "PAYMENT_METHODS_PERSISTENCE",
      "status": "APPROVED",
      "reason": "PAYMENT_METHODS_PERSISTENCE_CREATED",
      "description": "Payment methods record was created successfully."
    }
  ]
}
```

##### Response 400

400 Example `Invalid authorization payload`:

```json
[
  {
    "code": "WONA0001",
    "message": "Authorization Payload is invalid. It must be a valid JSON."
  }
]
```

400 Example `MTI required`:

```json
[
  {
    "code": "WONA0004",
    "message": "MTI is required.",
    "details": "Field: mti"
  }
]
```

400 Example `Entry mode required`:

```json
[
  {
    "code": "WONA0005",
    "message": "Entry mode is required.",
    "details": "Field: entry_mode"
  }
]
```

400 Example `Processing code required`:

```json
[
  {
    "code": "WONA0006",
    "message": "Processing code is required.",
    "details": "Field: processing_code"
  }
]
```

400 Example `Installment number required`:

```json
[
  {
    "code": "WONA0011",
    "message": "Number of installments is required and must be greater than 0.",
    "details": "Field: number_of_installments"
  }
]
```

400 Example `Amount required`:

```json
[
  {
    "code": "WONA0012",
    "message": "Amount is required.",
    "details": "Field: amount"
  }
]
```

400 Example `Amount can't be negative`:

```json
[
  {
    "code": "WONA0013",
    "message": "Amount can't be negative.",
    "details": "Field: amount"
  }
]
```

400 Example `Initiator ID required`:

```json
[
  {
    "code": "WONA0015",
    "message": "Card ID, card number, document number, bank account, bank branch, or account ID is required to identify the account holder.\""
  }
]
```

400 Example `Network required`:

```json
[
  {
    "code": "WONA0016",
    "message": "Network is required.",
    "details": "Field: network"
  }
]
```

400 Example `Invalid mti`:

```json
[
  {
    "code": "WONA0018",
    "message": "Invalid MTI.",
    "details": "Field: mti"
  }
]
```

400 Example `Invalid entry mode`:

```json
[
  {
    "code": "WONA0019",
    "message": "Entry mode is invalid. It should have two or three characters.",
    "details": "Field: entry_mode"
  }
]
```

400 Example `Original identifier required`:

```json
[
  {
    "code": "WONA0020",
    "message": "Original tracking ID or original authorization ID is required to identify the authorization.",
    "details": "Field: original_tracking_id or original_authorization_id"
  }
]
```

400 Example `Amount must be greater than zero`:

```json
[
  {
    "code": "WONA0032",
    "message": "Amount must be greater than zero.",
    "details": "Field: amount"
  }
]
```

400 Example `Beneficiary ID must be UUID`:

```json
[
  {
    "code": "WONA0033",
    "message": "Beneficiary_id must be a valid UUID.",
    "details": "Field: beneficiary_id"
  }
]
```

400 Example `Invalid clearing type`:

```json
[
  {
    "code": "WONA0036",
    "message": "Invalid Clearing Type. It must be ONLINE or OFFLINE.",
    "details": "Field: clearing_type"
  }
]
```

400 Example `Max amount exceeded`:

```json
[
  {
    "code": "WONA039",
    "message": "A maximum of 20 digits including two decimals is allowed for the amount field.",
    "details": "Field: amount"
  }
]
```

400 Example `Invalid amount decimal places`:

```json
[
  {
    "code": "WONA040",
    "message": "The amount must have a maximum of two decimal places.",
    "details": "Field: amount"
  }
]
```

400 Example `Invalid tracking ID size`:

```json
[
  {
    "code": "WONA041",
    "message": "Tracking ID must not have more than 50 characters.",
    "details": "Field: tracking_id"
  }
]
```

400 Example `Invalid authorization date time format`:

```json
[
  {
    "code": "WONA042",
    "message": "Authorization date time must be in the UTC-0 RFC3339 format.",
    "details": "Field: authorization_datetime"
  }
]
```

400 Example `Invalid posting date format`:

```json
[
  {
    "code": "WONA043",
    "message": "Authorization posting date must be in the YYYY-MM-DD format.",
    "details": "Field: posting_date"
  }
]
```

400 Example `External calculation invalid contract amount`:

```json
[
  {
    "code": "EINS0004",
    "message": "Contract amount cannot be negative and must contain at most 2 decimal places.",
    "details": "Field: contract_amount"
  }
]
```

400 Example `External calculation invalid principal amount`:

```json
[
  {
    "code": "EINS0005",
    "message": "Principal amount cannot be negative and must contain at most 2 decimal places.",
    "details": "Field: principal_amount"
  }
]
```

400 Example `External calculation principal greater than contract amount`:

```json
[
  {
    "code": "EINS0006",
    "message": "Principal amount cannot be greater than contract amount.",
    "details": "Field: principal_amount"
  }
]
```

400 Example `External calculation invalid installment number`:

```json
[
  {
    "code": "EINS0010",
    "message": "Number of installments should be greater than 0.",
    "details": "Field: number_of_installments"
  }
]
```

400 Example `External calculation invalid installment info size`:

```json
[
  {
    "code": "EINS0011",
    "message": "Number of installments must be equal to the installments details provided."
  }
]
```

400 Example `External calculation invalid installment amounts`:

```json
[
  {
    "code": "EINS0012",
    "message": "All installments amounts must be greater than 0 and must contain at most 2 decimal places."
  }
]
```

400 Example `External calculation invalid sum installment`:

```json
[
  {
    "code": "EINS0015",
    "message": "Added installment amounts don't match the contract amount."
  }
]
```

400 Example `External calculation invalid first payment date`:

```json
[
  {
    "code": "EINS0016",
    "message": "First payment date in the additional financial details is invalid.",
    "details": "Field: first_payment_date"
  }
]
```

##### Response 401

401 Example `Unauthorized`:

```json
{
  "message": "Access token is missing or invalid."
}
```

##### Response 403

403 Example `Forbidden`:

```json
{
  "message": "The request has been lost."
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
| 400 | `WONA0001` | Authorization Payload is invalid. It must be a valid JSON. |
| 400 | `WONA0004` | MTI is required. |
| 400 | `WONA0005` | Entry mode is required. |
| 400 | `WONA0006` | Processing code is required. |
| 400 | `WONA0011` | Number of installments is required and must be greater than 0. |
| 400 | `WONA0012` | Amount is required. |
| 400 | `WONA0013` | Amount can't be negative. |
| 400 | `WONA0015` | Card ID, card number, document number, bank account, bank branch, or account ID is required to identify the account holder." |
| 400 | `WONA0016` | Network is required. |
| 400 | `WONA0018` | Invalid MTI. |
| 400 | `WONA0019` | Entry mode is invalid. It should have two or three characters. |
| 400 | `WONA0020` | Original tracking ID or original authorization ID is required to identify the authorization. |
| 400 | `WONA0032` | Amount must be greater than zero. |
| 400 | `WONA0033` | Beneficiary_id must be a valid UUID. |
| 400 | `WONA0036` | Invalid Clearing Type. It must be ONLINE or OFFLINE. |
| 400 | `WONA039` | A maximum of 20 digits including two decimals is allowed for the amount field. |
| 400 | `WONA040` | The amount must have a maximum of two decimal places. |
| 400 | `WONA041` | Tracking ID must not have more than 50 characters. |
| 400 | `WONA042` | Authorization date time must be in the UTC-0 RFC3339 format. |
| 400 | `WONA043` | Authorization posting date must be in the YYYY-MM-DD format. |
| 400 | `EINS0004` | Contract amount cannot be negative and must contain at most 2 decimal places. |
| 400 | `EINS0005` | Principal amount cannot be negative and must contain at most 2 decimal places. |
| 400 | `EINS0006` | Principal amount cannot be greater than contract amount. |
| 400 | `EINS0010` | Number of installments should be greater than 0. |
| 400 | `EINS0011` | Number of installments must be equal to the installments details provided. |
| 400 | `EINS0012` | All installments amounts must be greater than 0 and must contain at most 2 decimal places. |
| 400 | `EINS0015` | Added installment amounts don't match the contract amount. |
| 400 | `EINS0016` | First payment date in the additional financial details is invalid. |
| 422 | `EPAE0004` | The method provided in the payload does not exist. |
| 500 | `EPAE0001` | Unexpected error while processing the call to the authentication system. |
| 500 | `EPAE0002` | Timeout error while processing the call to the authentication system. |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `payment-methods-authorization-1` | https://developers.pismo.io/events/docs/payment-methods-authorization-1 |
| `platform-authorization-platform-authorization-1` | https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;201;400;401;403;422;500`, has examples `True`, emits events `2`, deprecated `False`.

Guides that link to this operation: `KU-CORE-fee-models-create-and-simulate`, `KU-CORE-transaction-processing-flows`, `KU-EVT-client-webhooks-part-01`, `KU-PAY-configure-payment-methods`, `KU-PAY-payment-configurations`, `KU-PAY-payment-methods`, `KU-SELL-how-merchant-settlements-are-processed`, `KU-SELL-managing-merchant-transactions`, `KU-SELL-seller-marketplace-implementation-steps`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payment-methods/v2/payments operationId=post-payments -->
### `POST /payment-methods/v2/payments` — Create cash-in or cash-out

- **operationId:** `post-payments`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment methods`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a cash-in or cash-out payment operation. The type of operation depends on the processing code (credit for cash-in and debit for cash-out). 
> - For cash-in operations, the processing code must be of credit type. When [creating a processing code](ref:createprocessingcode), ensure that the `balance_impact` is `1` (credit).
> - For cash-out operations, the processing code must be of debit type. When [creating a processing code](ref:createprocessingcode), ensure that the `balance_impact` is `-1` (debit).
>
> With this endpoint, you have the following additional options.
> - Specify the `authentication` method and details.
> - Set `pre_authorization` to `true` for operations that require additional confirmation and then call the [Confirm pre-authorized cash-in or cash-out](ref:post-payment-confirm) endpoint.
> - Set `validation_rules` to control the rules in this flow, such as disabling a rule, changing the response code and denial code, and forcing a rule.
>
> Refer to the [Payment methods](doc:payment-methods) and [Payment configurations](doc:payments-configurations) guides for additional information.
>
> This endpoint generates a [Platform authorization created](https://developers.pismo.io/events/docs/platform-authorization-platform-authorization-1) event.
>
> **Note:** This is a PCI endpoint, use the https://gw-pci.pismolabs.io environment.

#### Request body

Required: yes

> Request processing body.

**Content type `application/json`** — schema: object (schema `PaymentsRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | yes | Pismo account ID. | format: "int64"; example: 8675309 |
| `beneficiary_id` | string (schema `BeneficiaryID`) | no | UUID for the beneficiary related to the account. | minLength: 36; maxLength: 50; example: "2c298321-bc21-4039-9c45-780cc6d4ec46" |
| `amount` | number (schema `Amount`) | yes | Credit or debit amount. | format: "float"; example: 100.23 |
| `currency_code` | string (schema `CurrencyPismoHierarchy`) | no | ISO-4217 alphabetic or numeric (3 characters) authorization currency code. For example, either BRL or 986 for Brazilian real. If you don't provide the currency, the platform uses the currency registered in the Pismo hierarchy (first looking at the account, then program, and then Org levels). | example: "BRL" |
| `processing_code` | string (schema `ProcessingCode`) | yes | Unique processing code that identifies the credit or debit operation. | example: "219803" |
| `tracking_id` | string (schema `TrackingID`) | yes | Unique tracking ID for this operation. | minLength: 36; maxLength: 50; example: "0b6995e5-b417-9be4-92b3-3677f4440ebe" |
| `authentication` | object (schema `Authentication`) | no | Authentication object. |  |
| `description` | string (schema `Description`) | no | Optional text that describes the operation. | example: "Custom purchase." |
| `metadata` | object (schema `Metadata`) | no | This optional user-defined key-value object field can be used with external operations to provide additional context or supplementary custom information for the operation. <br><br>The Pismo platform does not perform any validation or processing on this field but passes this object to the acquirer in transactions involving calls to the acquirer and sends it in the events related to the stream of data produced at the end of the request.<br><br>**Note**: This field must not be used to send Personally Identifiable Information (PII), Payment Card Industry (PCI) data, or any sensitive/regulated information. Metadata fields are intended for operational, non-sensitive data only. For sensitive data, use the specific parameters designed for that purpose. For more information, refer to [Get started with Pismo APIs](ref:get-started-with-pismo-apis#metadata).<br> | example: {"any-key": "any-value"} |
| `payment_datetime` | string (schema `PaymentDatetime`) | no | Effective payment date in the UTC-0 RFC3339 format, which includes milliseconds (yyyy-MM-ddThh:mm:ss.SSSZ).<br>Payments can be backdated but future dates are not allowed.<br> | format: "date-time"; example: "2023-01-02T07:35:05.125Z" |
| `pre_authorization` | boolean (schema `PreAuthorization`) | no | If set to `true`, this flag indicates that the operation is pre-authorized and requires additional confirmation. | default: false; example: false |
| `validation_rules` | object (map of object (schema `RuleConfig`)) (schema `ValidationRules`) | no | Validation rules performed in the flow. Each key is a rule name (such as `ACCOUNT_STATUS` or `LEDGER`) and the value is its configuration. | example: {"ACCOUNT_STATUS": {"disable": false, "force": false, "denial_reasons": {"ACCOUNT_STATUS_NOT_PERMITTED": {"response_code": "57", "denial_code": "DAL"}}}, "LEDGER": {"denial_reasons": {"LEDGER_INSUFFICIENT_FUNDS": {"response_code": "51", "denial_code": "DAL"}, "LEDGER_NOT_ALLOWED_OPERATION": {"response_code": "57", "denial_code": "DAL"}}}} |
| `authorization_validations` | object (schema `AuthorizationValidations`) | no | Contains additional data to be used in the authorization flow. This field is only considered for authorizations. Cancellations and confirmations will retrieve it based on the original authorization. |  |
| `original_authorization` | object (schema `OriginalAuthorization`) | no | This optional field identifies the original authorization to be linked. <br>When this object is provided, both the `id` and `type` fields need to be filled.<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Request was processed successfully, existing authorization with the corresponding `tracking_id` returned. | `application/json`: object (schema `v2PaymentsResponse`) |
| 201 | Request was processed successfully, new authorization created. | `application/json`: object (schema `v2PaymentsResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid. | `application/json`: object (schema `401Payments`) |
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

##### Response 201

**201 `application/json` body fields:**

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

Guides that link to this operation: `KU-CORE-transaction-processing-flows`, `KU-EVT-client-webhooks-part-01`, `KU-PAY-payment-configurations`, `KU-PAY-payment-methods`.

<!-- op: spec=api-specs/Core_platform_-_Payment_methods.yaml method=POST path=/payment-methods/v2/payments/cancel operationId=post-payments-cancel -->
### `POST /payment-methods/v2/payments/cancel` — Cancel cash-in or cash-out

- **operationId:** `post-payments-cancel`
- **Specification:** `api-specs/Core_platform_-_Payment_methods.yaml` (Core platform - Payment methods)
- **Server base URL(s):** `https://sandbox.pismolabs.io`, `https://gw-pci.pismolabs.io`
- **Tags:** `Payment methods`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Cancel an existing payment operation. If you don't provide the `amount`, the platform cancels the total original amount. You can also provide the `amount` to cancel a total or partial amount.
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
| 200 | Request was processed successfully, existing authorization with the corresponding `tracking_id` returned. | `application/json`: object (schema `PaymentsCancelResponse`) |
| 201 | Request was processed successfully, new authorization created. | `application/json`: object (schema `PaymentsCancelResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not found | `application/json`: object (schema `404Payments`) |
| 409 | Conflict | `application/json`: object (schema `409Payments`) |
| 422 | Unprocessable request | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal server error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

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

##### Response 201

**201 `application/json` body fields:**

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

Guides that link to this operation: `KU-CORE-transaction-processing-flows`, `KU-PAY-payment-methods`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

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

<!-- schema: #/components/schemas/CalculatedAmountsAuthorization -->
### Schema `CalculatedAmountsAuthorization`

Pointer: `#/components/schemas/CalculatedAmountsAuthorization`. Type: object (schema `CalculatedAmountsAuthorization`).

> Calculated amounts for the authorization.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `contract_amount` | number | no | Total amount of the authorization after calculation and addition of any necessary fees. | example: 110 |
| `description` | string | no | Description of the plan. | example: "0+24 with interest" |
| `fees` | array of object (schema `Fee`) | no | List of applied fees on this calculation. |  |
| `fees[].type` | string | no | Type of applied fee. For example, fixed, percentage, or any other type. | minLength: 2; maxLength: 30; example: "fixed" |
| `fees[].amount` | number | no | Calculated amount of this fee. | example: 10 |
| `fees[].rate` | number | no | When using a percentage fee, this is the percentage rate used for calculating this fee. For example, the value `10` indicates 10%. | minimum: 0; example: 10 |
| `interests` | array of object (schema `Interest`) | no | List of interests applied to this calculation. |  |
| `interests[].type` | string | no | Type of applied interest. For example, weekly, monthly, annually, or any other type. | minLength: 2; maxLength: 30; example: "monthly" |
| `interests[].amount` | number | no | Calculated amount of this interest. | example: 8.73 |
| `interests[].rate` | number | no | Percentage rate used for calculating this interest. For example, the value `9.99` indicates 9.99%. | minimum: 0; example: 9.99 |
| `installments` | array of object (schema `InstallmentsAuthorization`) | no | List and details for each installment. |  |
| `installments[].number` | integer | no | Order number of this installment in the hierarchy. | minimum: 1; maximum: 100; example: 1 |
| `installments[].contract_amount` | number | no | Total amount of the installment after calculation and addition of any necessary fees. | example: 11 |
| `installments[].principal_amount` | number | no | Total amount of the installment after calculation without the addition of any fees. | example: 10 |
| `installments[].amortization_amount` | number | no | Amortization amount related to this installment. | example: 7.5 |
| `installments[].fees` | array of object (schema `Fee`) | no | List of applied fees on this calculation. |  |
| `installments[].fees[].type` | string | no | Type of applied fee. For example, fixed, percentage, or any other type. | minLength: 2; maxLength: 30; example: "fixed" |
| `installments[].fees[].amount` | number | no | Calculated amount of this fee. | example: 10 |
| `installments[].fees[].rate` | number | no | When using a percentage fee, this is the percentage rate used for calculating this fee. For example, the value `10` indicates 10%. | minimum: 0; example: 10 |
| `installments[].interests` | array of object (schema `Interest`) | no | List of interests applied to this calculation. |  |
| `installments[].interests[].type` | string | no | Type of applied interest. For example, weekly, monthly, annually, or any other type. | minLength: 2; maxLength: 30; example: "monthly" |
| `installments[].interests[].amount` | number | no | Calculated amount of this interest. | example: 8.73 |
| `installments[].interests[].rate` | number | no | Percentage rate used for calculating this interest. For example, the value `9.99` indicates 9.99%. | minimum: 0; example: 9.99 |
| `installments[].taxes` | array of object (schema `Tax`) | no | List of applied taxes on this calculation. |  |
| `installments[].taxes[].type` | string | no | Type of applied tax. For example, DAILY_IOF, FIXED_IOF, INTERNATIONAL_IOF (taxes on financial operations) in Brazil, SDRT (stamp duty reserve tax) in United Kingdom, FTT (financial transaction tax) in European Union, STT (securities transaction tax) in India, or any other type. | minLength: 2; maxLength: 50; example: "INTERNATIONAL_IOF" |
| `installments[].taxes[].amount` | number | no | Calculated amount of this tax. | example: 0.38 |
| `installments[].taxes[].rate` | number | no | Percentage rate used for calculating this tax. For example, the value `0.38` indicates 0.38%. | minimum: 0; example: 0.38 |
| `number_of_installments` | integer | no | Number of installments in this calculation. | minimum: 2; maximum: 100; example: 12 |
| `plan_id` | string | no | ID of the plan used to perform this calculation. | example: "PLAN_ID_1" |
| `principal_amount` | number | no | Total amount of the authorization after calculation without the addition of any fees. | example: 100 |
| `taxes` | array of object (schema `Tax`) | no | List of applied taxes on this calculation. |  |
| `taxes[].type` | string | no | Type of applied tax. For example, DAILY_IOF, FIXED_IOF, INTERNATIONAL_IOF (taxes on financial operations) in Brazil, SDRT (stamp duty reserve tax) in United Kingdom, FTT (financial transaction tax) in European Union, STT (securities transaction tax) in India, or any other type. | minLength: 2; maxLength: 50; example: "INTERNATIONAL_IOF" |
| `taxes[].amount` | number | no | Calculated amount of this tax. | example: 0.38 |
| `taxes[].rate` | number | no | Percentage rate used for calculating this tax. For example, the value `0.38` indicates 0.38%. | minimum: 0; example: 0.38 |
| `total_annual_rate` | number | no | Total interest percentage rate applied to this contract annually. | minimum: 0; example: 27 |
| `total_monthly_rate` | number | no | Total interest percentage rate applied to this contract monthly. | minimum: 0; example: 9.99 |
| `additional_financial_details` | object (schema `AdditionalFinancialDetails`) | no | Additional information related to the authorization. |  |

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

<!-- schema: #/components/schemas/ErrorsResponse -->
### Schema `ErrorsResponse`

Pointer: `#/components/schemas/ErrorsResponse`. Type: array of object (schema `NewErrorModel`) (schema `ErrorsResponse`).

<!-- schema: #/components/schemas/OriginalAuthorization -->
### Schema `OriginalAuthorization`

Pointer: `#/components/schemas/OriginalAuthorization`. Type: object (schema `OriginalAuthorization`).

> This optional field identifies the original authorization to be linked. 
> When this object is provided, both the `id` and `type` fields need to be filled.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | yes | Original authorization ID in the Pismo platform. | example: 101 |
| `type` | string | yes | Original authorization type. | enum: ["NETWORK", "PLATFORM"]; example: "NETWORK" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | yes | Application-specific error code |  |
| `message` | string | yes | Error explanation |  |
| `violations` | object (map of string) | no | Field-level validation failures (keys are dynamic) |  |

<!-- schema: #/components/schemas/401Payments -->
### Schema `401Payments`

Pointer: `#/components/schemas/401Payments`. Type: object (schema `401Payments`).

> Error codes available:
>   * WONP0005 - Authentication is required but no authentication method was provided.
>   * WONP0006 - Authentication is required but it was not performed.
>   * WONP0007 - Request was not authenticated.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | enum: ["WONP0005", "WONP0006", "WONP0007"]; example: "WONP0005" |
| `message` | string | no |  | enum: ["Authentication is required but no authentication method was provided.", "Authentication is required but it was not performed.", "Request was not authenticated."]; example: "Authentication is required but no authentication method was provided." |

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

<!-- schema: #/components/schemas/404Payments -->
### Schema `404Payments`

Pointer: `#/components/schemas/404Payments`. Type: object (schema `404Payments`).

> * WONP0009 - Original authorization not found.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string | no |  | example: "WONP0009" |
| `message` | string | no |  | example: "Original authorization not found." |

<!-- schema: #/components/schemas/AdditionalFinancialDetails -->
### Schema `AdditionalFinancialDetails`

Pointer: `#/components/schemas/AdditionalFinancialDetails`. Type: object (schema `AdditionalFinancialDetails`).

> Additional information related to the authorization.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `effective_annual_cost` | number | no | Total annual finance charge expressed as a percentage rate. | example: 0.13 |
| `effective_monthly_cost` | number | no | Total monthly finance charge expressed as a percentage rate. | example: 0.13 |
| `annual_interest_rate` | number | no | Percentage of interest charged over the course of a year. | example: 10 |

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
| `api-specs/Core_platform_-_Payment_methods.yaml` | tag `Payment methods`: POST /payment-methods/v1/authorization, POST /payment-methods/v2/payments, POST /payment-methods/v2/payments/cancel | https://github.com/PismoDevEx/pismo-api-specs | `9b02c87b6e39a1c8…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-fee-models-create-and-simulate` — Creating, applying and simulating fee models
- `KU-CORE-transaction-processing-flows` — Transaction processing flows
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
- `KU-ERR-codes-wona` — Error codes: WONA
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-client-webhooks-part-01` — Client webhooks (part 1 of 14)
- `KU-PAY-configure-payment-methods` — Configure payment methods
- `KU-PAY-payment-configurations` — Payment methods configurations overview
- `KU-PAY-payment-methods` — Payment methods
- `KU-SELL-how-merchant-settlements-are-processed` — How merchant settlements and installments are processed
- `KU-SELL-managing-merchant-transactions` — Managing merchant transactions
- `KU-SELL-seller-marketplace-implementation-steps` — Seller marketplace implementation steps 1 to 6
