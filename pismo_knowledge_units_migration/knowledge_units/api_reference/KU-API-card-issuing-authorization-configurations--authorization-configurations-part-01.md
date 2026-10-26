---
ku_id: KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01
title: 'API reference: Card issuing - Authorization configurations — Authorization configurations (part 1 of 2)'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Card_issuing_-_Authorization_configurations.yaml
  sha256: 911840638ef9e73e36cef2040f29b29419c8aac62d9fdd06722262946930badb
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
- get-authorization-config-by-tenant
- PutAuthorizationConfigByTenant
- post-authorization-config-by-tenant
- DeleteAuthorizationConfigByTenant
- GetAuthorizationConfigByProgram
- PutAuthorizationConfigByProgram
- PostAuthorizationConfigByProgram
related_kus:
- KU-CARD-authorization-configurations-1
- KU-CARD-run-the-configuration-requests
specification_version: 1.0.0
---

# API reference: Card issuing - Authorization configurations — Authorization configurations (part 1 of 2)

**KU ID:** `KU-API-card-issuing-authorization-configurations--authorization-configurations-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 7 operation(s) tagged `Authorization configurations` in `api-specs/Card_issuing_-_Authorization_configurations.yaml` (“Card issuing - Authorization configurations”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Authorization configurations-related endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/config` | `get-authorization-config-by-tenant` | Get authorization configuration by organization | no |
| `PUT /v1/config` | `PutAuthorizationConfigByTenant` | Update authorization configuration by organization | no |
| `POST /v1/config` | `post-authorization-config-by-tenant` | Create authorization configuration by organization | no |
| `DELETE /v1/config` | `DeleteAuthorizationConfigByTenant` | Delete authorization configuration by organization | no |
| `GET /v1/config/program/{programId}` | `GetAuthorizationConfigByProgram` | Get authorization configuration by program | no |
| `PUT /v1/config/program/{programId}` | `PutAuthorizationConfigByProgram` | Update authorization configuration by program | no |
| `POST /v1/config/program/{programId}` | `PostAuthorizationConfigByProgram` | Create authorization configuration by program | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Card_issuing_-_Authorization_configurations.yaml method=GET path=/v1/config operationId=get-authorization-config-by-tenant -->
### `GET /v1/config` — Get authorization configuration by organization

- **operationId:** `get-authorization-config-by-tenant`
- **Specification:** `api-specs/Card_issuing_-_Authorization_configurations.yaml` (Card issuing - Authorization configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/network-transactions-config`
- **Tags:** `Authorization configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the authorization configuration at the org level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | no | string | Organization ID | example: "TN-12345678-9f53-46ce-953b-b81dd1234567" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetNetworkTransactionsConfigResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Authorization_configurations.yaml method=PUT path=/v1/config operationId=PutAuthorizationConfigByTenant -->
### `PUT /v1/config` — Update authorization configuration by organization

- **operationId:** `PutAuthorizationConfigByTenant`
- **Specification:** `api-specs/Card_issuing_-_Authorization_configurations.yaml` (Card issuing - Authorization configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/network-transactions-config`
- **Tags:** `Authorization configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the authorization configuration at the organization (org) level. This operation updates the entire configuration. Therefore, all fields must be sent to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | no | string | Organization ID | example: "TN-12345678-9f53-46ce-953b-b81dd1234567" |

#### Request body

Required: yes

> Create the authorization configuration request body.

**Content type `application/json`** — schema: object (schema `UpdateNetworkTransactionsConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `UpdateNetworkTransactionsConfigResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Authorization_configurations.yaml method=POST path=/v1/config operationId=post-authorization-config-by-tenant -->
### `POST /v1/config` — Create authorization configuration by organization

- **operationId:** `post-authorization-config-by-tenant`
- **Specification:** `api-specs/Card_issuing_-_Authorization_configurations.yaml` (Card issuing - Authorization configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/network-transactions-config`
- **Tags:** `Authorization configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an authorization configuration for an authorization at the organization (org) level. This level can be used as a default configuration for all programs and accounts in this org. An org can only have one configuration. Executing this endpoint on an org that already has a configuration defined for it generates a conflict response.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | no | string | Organization ID | example: "TN-12345678-9f53-46ce-953b-b81dd1234567" |

#### Request body

Required: yes

> Create the Authorization configuration request body.

**Content type `application/json`** — schema: object (schema `CreateNetworkTransactionsConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateNetworkTransactionsConfigResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CARD-authorization-configurations-1`, `KU-CARD-run-the-configuration-requests`.

<!-- op: spec=api-specs/Card_issuing_-_Authorization_configurations.yaml method=DELETE path=/v1/config operationId=DeleteAuthorizationConfigByTenant -->
### `DELETE /v1/config` — Delete authorization configuration by organization

- **operationId:** `DeleteAuthorizationConfigByTenant`
- **Specification:** `api-specs/Card_issuing_-_Authorization_configurations.yaml` (Card issuing - Authorization configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/network-transactions-config`
- **Tags:** `Authorization configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete an authorization configuration for an authorization at the organization (org) level. This level can be used as a default configuration for all programs and accounts in this org.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | no | string | Organization ID | example: "TN-12345678-9f53-46ce-953b-b81dd1234567" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | Deleted |  |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Authorization_configurations.yaml method=GET path=/v1/config/program/{programId} operationId=GetAuthorizationConfigByProgram -->
### `GET /v1/config/program/{programId}` — Get authorization configuration by program

- **operationId:** `GetAuthorizationConfigByProgram`
- **Specification:** `api-specs/Card_issuing_-_Authorization_configurations.yaml` (Card issuing - Authorization configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/network-transactions-config`
- **Tags:** `Authorization configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the authorization configuration at the program level.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | ID of the program to which this configuration should be applied. | format: "int32" |
| `x-tenant` | header | no | string | Organization ID | example: "TN-12345678-9f53-46ce-953b-b81dd1234567" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Retrieved successfully | `application/json`: object (schema `GetNetworkTransactionsConfigResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Authorization_configurations.yaml method=PUT path=/v1/config/program/{programId} operationId=PutAuthorizationConfigByProgram -->
### `PUT /v1/config/program/{programId}` — Update authorization configuration by program

- **operationId:** `PutAuthorizationConfigByProgram`
- **Specification:** `api-specs/Card_issuing_-_Authorization_configurations.yaml` (Card issuing - Authorization configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/network-transactions-config`
- **Tags:** `Authorization configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the authorization configuration at the program level. This operation updates the entire configuration. Therefore, all fields must be sent to avoid data loss.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | ID of the program to which this configuration should be applied. | format: "int32" |
| `x-tenant` | header | no | string | Organization ID | example: "TN-12345678-9f53-46ce-953b-b81dd1234567" |

#### Request body

Required: yes

> Update the authorization configuration request body.

**Content type `application/json`** — schema: object (schema `UpdateNetworkTransactionsConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Updated successfully | `application/json`: object (schema `UpdateNetworkTransactionsConfigResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal server error |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Card_issuing_-_Authorization_configurations.yaml method=POST path=/v1/config/program/{programId} operationId=PostAuthorizationConfigByProgram -->
### `POST /v1/config/program/{programId}` — Create authorization configuration by program

- **operationId:** `PostAuthorizationConfigByProgram`
- **Specification:** `api-specs/Card_issuing_-_Authorization_configurations.yaml` (Card issuing - Authorization configurations)
- **Server base URL(s):** `https://sandbox.pismolabs.io/network-transactions-config`
- **Tags:** `Authorization configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create the authorization configuration at the program level. This level can be used as a default configuration for all accounts in this program and at a more granular level than org. A program can only have one configuration. Executing this endpoint on a program that already has a configuration defined for it generates a conflict response.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `programId` | path | yes | integer | ID of the program to which this configuration should be applied. | format: "int32" |
| `x-tenant` | header | no | string | Organization ID | example: "TN-12345678-9f53-46ce-953b-b81dd1234567" |

#### Request body

Required: yes

> Create the authorization configuration request body.

**Content type `application/json`** — schema: object (schema `CreateNetworkTransactionsConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateNetworkTransactionsConfigResponse`) |
| 400 | Bad request |  |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict |  |
| 500 | Internal server error |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `use_anti_fraud_response_code` | boolean (schema `UseAntiFraudResponseCode`) | no | Flag indicates whether we should use the response code sent in anti-fraud. | default: false; example: true |
| `zero_balance_url` | string (schema `ZeroBalanceURL`) | no | Indicates that it’s a Zero Balance flow, so the URL to call the customer’s service is informed. **NOTE:** This is only required for Zero balance. | default: ""; example: "http://zerobalanceurl" |
| `should_use_anti_fraud_decision` | boolean (schema `ShouldUseAntiFraudDecision`) | no | Flag indicates whether anti-fraud decisions should be used. | default: false; example: true |
| `approve_anti_fraud_unavailable` | boolean (schema `ApproveAntiFraudUnavailable`) | no | If set to `true` when anti-fraud is unavailable, the anti-fraud check is marked as `APPROVED`. If set to `false`, it is marked as `REJECTED`. | default: false; example: true |
| `enabled_partial_authorization` | boolean (schema `EnabledPartialAuthorization`) | no | By default, authorizations don’t validate partial authorization, but if this property is enabled, it allows the platform to process partial authorizations for a given org/program/account. **NOTE:** This property also depends on the merchant, as it is necessary for the merchant to be able to partially authorize. | default: false; example: true |
| `disable_dcc` | boolean (schema `DisableDcc`) | no | This setting indicates whether or not the program allows dynamic currency conversion (DCC) transactions. By default, every program allows DCC transactions. In case it's necessary to block this type of transaction, the configuration must be set to `true`. | default: false; format: "int32"; example: true |
| `deny_all_authorizations` | boolean (schema `DenyAllAuthorizations`) | no | Flag indicates whether authorizations should be denied. This is useful for cases where a product is deprecated or during a migration process. | default: false; example: true |
| `use_settlement_from_network` | boolean (schema `UseSettlementFromNetwork`) | no | By default, in clearing flow for international purchases, the authorizations use the same settlement amount of authorization (online flow). Setting this flag to truemeans the system will use the settlement amount from the clearing message, which can be different from authorization. | default: false; example: true |
| `use_rates_fee_models` | boolean (schema `UseRatesFeeModels`) | no | Flag indicates whether rate fee models should be used. | default: false; example: true |
| `call_anti_fraud_when_cancelling` | boolean (schema `CallAntiFraudWhenCancelling`) | no | Flag indicates whether the anti-fraud API should be called during cancellation. | default: false; example: true |
| `days_to_cancel_pre_authorization` | integer (schema `DaysToCancelPreAuthorization`) | no | Number of days to cancel pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization` | integer (schema `DaysToCancelAuthorization`) | no | Number of days to cancel authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_pre_authorization_migration` | integer (schema `DaysToCancelPreAuthorizationMigration`) | no | Number of days to cancel migrated pre-authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `days_to_cancel_authorization_migration` | integer (schema `DaysToCancelAuthorizationMigration`) | no | Number of days to cancel migrated authorization. **NOTE:** The minimum number of days is 1 and the maximum is 60. | format: "int32"; example: 5 |
| `always_call_ledger_rules` | boolean (schema `AlwaysCallLedgerRules`) | no | Flag indicates whether Ledger API and Rules API should be always called, even when the authorization has already been denied. | default: false; example: true |
| `use_local_amount_when_dcc` | boolean (schema `UseLocalAmountWhenDCC`) | no | Flag to control currency selection for rates lookup in DCC (Dynamic Currency Conversion) scenarios. When enabled, the authorizer uses the local currency amount instead of the settlement amount when calling the rates service. The transaction classification remains international and all existing international processing logic is unchanged - only the currency used for rates calculation is affected. **Note:** This flag must not be `true` when `disable_dcc` is `true`. The API will reject this combination with error code `WNTC0031` (or `WNTC0032` for override_bins). | default: false; example: true |
| `override_bins` | object (map of object (schema `NetworkTransactionsConfigOptions`)) | no | Configurations that can be overwritten individually at the BIN level, applying the default values if absent. | example: {"123456": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}, "12345678": {"use_anti_fraud_response_code": true, "zero_balance_url": "http://zerobalanceurl", "should_use_anti_fraud_decision": true, "approve_anti_fraud_unavailable": true, "enabled_partial_authorization": true, "disable_dcc": true, "deny_all_authorizations": true, "use_settlement_from_network": true, "use_rates_fee_models": true}} |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.


## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Card_issuing_-_Authorization_configurations.yaml` | tag `Authorization configurations`: GET /v1/config, PUT /v1/config, POST /v1/config, DELETE /v1/config, GET /v1/config/program/{programId}, PUT /v1/config/program/{programId}, POST /v1/config/program/{programId} | https://github.com/PismoDevEx/pismo-api-specs | `911840638ef9e73e…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CARD-authorization-configurations-1` — Authorization configurations
- `KU-CARD-run-the-configuration-requests` — Run the configuration requests
