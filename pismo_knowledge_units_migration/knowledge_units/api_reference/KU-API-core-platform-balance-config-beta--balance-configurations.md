---
ku_id: KU-API-core-platform-balance-config-beta--balance-configurations
title: 'API reference: Core platform - Balance configurations — Balance configurations'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Balance_config_Beta.yaml
  sha256: 76e234253e991b9887c9a5b3d0ca67692155b9edf0b8d4326bbfc54a742c0aef
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
- get-v1-balances-config
- post-v1-balances-config
- get-v1-balances-config-by-id
- put-v1-balances-config
related_kus:
- KU-BANK-funds-coverage
- KU-CORE-balance-configurations
- KU-CORE-commercial-cards
- KU-CORE-over-limit-fee
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
specification_version: 1.0.0
---

# API reference: Core platform - Balance configurations — Balance configurations

**KU ID:** `KU-API-core-platform-balance-config-beta--balance-configurations` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 4 operation(s) tagged `Balance configurations` in `api-specs/Core_platform_-_Balance_config_Beta.yaml` (“Core platform - Balance configurations”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage account balance configurations.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/balances-config` | `get-v1-balances-config` | List balance configurations | no |
| `POST /v1/balances-config` | `post-v1-balances-config` | Create balance configuration | no |
| `GET /v1/balances-config/{configId}` | `get-v1-balances-config-by-id` | Get balance configuration | no |
| `PUT /v1/balances-config/{configId}` | `put-v1-balances-config` | Replace balance configuration | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Balance_config_Beta.yaml method=GET path=/v1/balances-config operationId=get-v1-balances-config -->
### `GET /v1/balances-config` — List balance configurations

- **operationId:** `get-v1-balances-config`
- **Specification:** `api-specs/Core_platform_-_Balance_config_Beta.yaml` (Core platform - Balance configurations)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/balances-config`
- **Tags:** `Balance configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List balance configurations available for the organization. You can also filter the results by program or account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | query | no | integer | Account ID | example: 1234 |
| `programId` | query | no | integer | Program ID | example: 1234 |
| `x-tenant` | header | yes | string | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `x-cid` | header | no | string | The Correlation Identifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated. | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object |
| 400 | Bad request | `application/json`: object (schema `ErrorWithDetails`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `invalidProgramId` (Invalid ProgramID):

```json
{
  "code": "WBLC0020",
  "message": "Error parsing program ID to integer number."
}
```

##### Response 500

500 Example `internalServerError` (Internal server error):

```json
{
  "code": "EBLC9999",
  "message": "An Internal Server Error found, please contact the administrator"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBLC0020` | Error parsing program ID to integer number. |
| 500 | `EBLC9999` | An Internal Server Error found, please contact the administrator |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Balance_config_Beta.yaml method=POST path=/v1/balances-config operationId=post-v1-balances-config -->
### `POST /v1/balances-config` — Create balance configuration

- **operationId:** `post-v1-balances-config`
- **Specification:** `api-specs/Core_platform_-_Balance_config_Beta.yaml` (Core platform - Balance configurations)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/balances-config`
- **Tags:** `Balance configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a balance configuration that determines how authorizations on the Pismo platform impact account balances and limits. 
> To create a balance configuration, define its applicability level, filters, conditions, and results. 
> For more information, refer to the [Balance configurations overview](doc:balances-configurations-overview) guide.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `x-tenant` | header | yes | string | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `x-cid` | header | no | string | The Correlation Identifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated. | example: "12345" |

#### Request body

Required: yes

> Balance configuration creation request.
> **Important:** Each config must have either `filters` (inline) OR `filter_template_id` (reference), but not both.

**Content type `application/json`** — schema: object (schema `CreateBalancesConfig`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `level` | string (schema `Level`) | no | Level to apply the balance configuration. (Note: `tenant` indicates an organization.) If `level` is `tenant`, the organization ID is parsed from the access token.<br>You can implement the following operations for all levels:<br>* Impact different balances.<br>* Define the amount to impact balance.<br>* Validate different balances or limits.<br>* Define the amount to validate.<br>* Define when the limit will be reset.<br><br>On the account level, two additional features are available:<br>* Impact a related account.<br>* Define a counterpart account.<br> | enum: ["tenant", "program", "account"]; example: "program" |
| `program_id` | integer (schema `ProgramId`) | no | Program ID. **REQUIRED** if `level` is `program`. | example: 999 |
| `account_id` | integer (schema `AccountId`) | no | Account ID. **REQUIRED** if `level` is `account`. | example: 999 |
| `global_configs` | object (schema `GlobalConfig`) | no | Global configuration settings that always apply regardless of the filter. |  |
| `configs` | array of object | no | Array of balance configurations |  |
| `configs[].name` | string (schema `Name`) | no | Configuration name. | example: "Config-multiple-accounts" |
| `configs[].is_active` | boolean (schema `IsActive`) | no | Indicates active configuration. | example: true |
| `configs[].filter_template_id` | string | no | Reference to a filter template ID. Use this to apply a predefined filter template instead of defining filters inline.<br>**Cannot be used together with `filters`.**<br> | example: "test-1" |
| `configs[].filters` | object | no | Inline filter criteria for the configuration. <br>**Cannot be used together with `filter_template_id`.**<br> |  |
| `configs[].filters.processing_codes` | array of string (schema `ProcessingCodes`) | no | A processing code defines how the Pismo platform handles a certain financial operation type. For more information, refer to [Processing codes and transaction types](doc:processing-codes-and-transaction-types). | example: ["01", "03"] |
| `configs[].filters.min_installments` | integer (schema `MinInstallments`) | no | Min installments to validate. | example: 1 |
| `configs[].filters.max_installments` | integer (schema `MaxInstallments`) | no | Max installments to validate. | example: 12 |
| `configs[].filters.mcc` | array of string (schema `MCC`) | no | Merchant category codes to validate. | example: ["1234", "2626"] |
| `configs[].filters.account_type` | string (schema `AccountType`) | no | Account type that impacts limit or different account.<br>Account types:<br>"00" = Non-specified account<br>"10" = Savings account<br>"20" = Checking account<br>"30" = Credit card account<br> | enum: ["00", "10", "20", "30"]; example: "00" |
| `configs[].filters.currency_code` | string (schema `CurrencyCode`) | no | Alphanumeric ISO 4217 standard currency code that impacts different limits or accounts. | example: "USD" |
| `configs[].scenarios` | array of object | no | Balance configuration scenarios. Scenarios determine how the evaluated transactions impact balances and limits. |  |
| `configs[].scenarios[].condition` | object | no | Evaluated condition. |  |
| `configs[].scenarios[].condition.order` | integer (schema `Order`) | yes | Condition priority order. The lower the number, the higher the priority. | example: 1 |
| `configs[].scenarios[].condition.type` | string (schema `Type`) | yes | Condition type: `default` or `custom`. `custom` allows for available balance or limit validation, `default` does not. If `default` is used, the `consider` field is not used to validate. The validation stops when `default` is used. | enum: ["default", "custom"]; example: "custom" |
| `configs[].scenarios[].condition.amount_to_check_balance` | string (schema `AmountToCheckBalance`) | no | Amount to check for available balance: `amount` or `installment_amount`. `amount` is the principal amount. This field is **REQUIRED** if `type` is `custom`. | enum: ["amount", "installment_amount"]; example: "amount" |
| `configs[].scenarios[].result` | object (schema `ConditionResult`) | no | Expected result described at evaluated conditions. |  |

Example `withInlineFilters` (Configuration with inline filters):

```json
{
  "level": "program",
  "program_id": 123456,
  "configs": [
    {
      "name": "Retail transactions",
      "is_active": true,
      "filters": {
        "processing_codes": [
          "555"
        ],
        "mcc": [
          "ABC01"
        ]
      },
      "scenarios": [
        {
          "condition": {
            "order": 1,
            "type": "default"
          },
          "result": {
            "impact": [
              "AvailableCreditLimit"
            ],
            "consider": [
              "AvailableCreditLimit"
            ],
            "amount": "contract_amount",
            "amount_consider": "principal_amount",
            "reset_limit": "never"
          }
        }
      ]
    }
  ]
}
```

Example `withFilterTemplate` (Configuration with filter template reference):

```json
{
  "level": "program",
  "program_id": 123456,
  "configs": [
    {
      "name": "Standard retail",
      "is_active": true,
      "filter_template_id": "test-1",
      "scenarios": [
        {
          "condition": {
            "order": 1,
            "type": "default"
          },
          "result": {
            "impact": [
              "AvailableCreditLimit"
            ],
            "consider": [
              "AvailableCreditLimit"
            ],
            "amount": "contract_amount",
            "amount_consider": "principal_amount",
            "reset_limit": "never"
          }
        }
      ]
    }
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object |
| 400 | Bad request | `application/json`: object (schema `ErrorWithDetails`) |
| 404 | Filter template not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `config_id` | string (schema `ConfigId`) | no | Balance configuration ID | example: "041ee495-268a-4267-b53a-5b9532a53e45" |

##### Response 400

400 Example `conflictFiltersAndTemplate` (Both filters and filter_template_id provided):

```json
{
  "code": "EBCF0321",
  "message": "Cannot provide both filters and filter_template_id in the same configuration"
}
```

400 Example `missingFilters` (Missing both filters and filter_template_id):

```json
{
  "code": "EBCF0320",
  "message": "Configuration at index 0 must have either filter_template_id or filters.processing_codes"
}
```

##### Response 404

404 Example `filterTemplateNotFound` (Referenced filter template does not exist):

```json
{
  "code": "EBCF0317",
  "message": "Filter template with ID test-1 not found"
}
```

##### Response 500

500 Example `internalServerError` (Internal server error):

```json
{
  "code": "EBLC9999",
  "message": "An Internal Server Error found, please contact the administrator"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EBCF0321` | Cannot provide both filters and filter_template_id in the same configuration |
| 400 | `EBCF0320` | Configuration at index 0 must have either filter_template_id or filters.processing_codes |
| 404 | `EBCF0317` | Filter template with ID test-1 not found |
| 500 | `EBLC9999` | An Internal Server Error found, please contact the administrator |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-funds-coverage`, `KU-CORE-balance-configurations`, `KU-CORE-commercial-cards`, `KU-CORE-over-limit-fee`.

<!-- op: spec=api-specs/Core_platform_-_Balance_config_Beta.yaml method=GET path=/v1/balances-config/{configId} operationId=get-v1-balances-config-by-id -->
### `GET /v1/balances-config/{configId}` — Get balance configuration

- **operationId:** `get-v1-balances-config-by-id`
- **Specification:** `api-specs/Core_platform_-_Balance_config_Beta.yaml` (Core platform - Balance configurations)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/balances-config`
- **Tags:** `Balance configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a balance configuration by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `configId` | path | yes | string | Balance configuration ID | example: "66954f26-aaef-49c2-b195-47a8f8410df1" |
| `x-tenant` | header | yes | string | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `x-cid` | header | no | string | The Correlation Identifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated. | example: "12345" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `BalancesConfig`) |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 404 | Not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `level` | string (schema `Level`) | no | Level to apply the balance configuration. (Note: `tenant` indicates an organization.) If `level` is `tenant`, the organization ID is parsed from the access token.<br>You can implement the following operations for all levels:<br>* Impact different balances.<br>* Define the amount to impact balance.<br>* Validate different balances or limits.<br>* Define the amount to validate.<br>* Define when the limit will be reset.<br><br>On the account level, two additional features are available:<br>* Impact a related account.<br>* Define a counterpart account.<br> | enum: ["tenant", "program", "account"]; example: "program" |
| `program_id` | integer (schema `ProgramId`) | no | Program ID. **REQUIRED** if `level` is `program`. | example: 999 |
| `account_id` | integer (schema `AccountId`) | no | Account ID. **REQUIRED** if `level` is `account`. | example: 999 |
| `config_id` | string (schema `ConfigId`) | no | Balance configuration ID | example: "041ee495-268a-4267-b53a-5b9532a53e45" |
| `global_configs` | object (schema `GlobalConfig`) | no | Global configuration settings that always apply regardless of the filter. |  |
| `configs` | array of object | no | Array of balance configurations |  |
| `configs[].name` | string (schema `Name`) | no | Configuration name. | example: "Config-multiple-accounts" |
| `configs[].is_active` | boolean (schema `IsActive`) | no | Indicates active configuration. | example: true |
| `configs[].filter_template_id` | string | no | Reference to a filter template ID. Use this to apply a predefined filter template instead of defining filters inline.<br>**Cannot be used together with `filters`.**<br> | example: "test-1" |
| `configs[].filters` | object | no | Inline filter criteria for the configuration. <br>**Cannot be used together with `filter_template_id`.**<br> |  |
| `configs[].filters.processing_codes` | array of string (schema `ProcessingCodes`) | no | A processing code defines how the Pismo platform handles a certain financial operation type. For more information, refer to [Processing codes and transaction types](doc:processing-codes-and-transaction-types). | example: ["01", "03"] |
| `configs[].filters.min_installments` | integer (schema `MinInstallments`) | no | Min installments to validate. | example: 1 |
| `configs[].filters.max_installments` | integer (schema `MaxInstallments`) | no | Max installments to validate. | example: 12 |
| `configs[].filters.mcc` | array of string (schema `MCC`) | no | Merchant category codes to validate. | example: ["1234", "2626"] |
| `configs[].filters.account_type` | string (schema `AccountType`) | no | Account type that impacts limit or different account.<br>Account types:<br>"00" = Non-specified account<br>"10" = Savings account<br>"20" = Checking account<br>"30" = Credit card account<br> | enum: ["00", "10", "20", "30"]; example: "00" |
| `configs[].filters.currency_code` | string (schema `CurrencyCode`) | no | Alphanumeric ISO 4217 standard currency code that impacts different limits or accounts. | example: "USD" |
| `configs[].scenarios` | array of object | no | Balance configuration scenarios. Scenarios determine how the evaluated transactions impact balances and limits. |  |
| `configs[].scenarios[].condition` | object | no | Evaluated condition. |  |
| `configs[].scenarios[].condition.order` | integer (schema `Order`) | yes | Condition priority order. The lower the number, the higher the priority. | example: 1 |
| `configs[].scenarios[].condition.type` | string (schema `Type`) | yes | Condition type: `default` or `custom`. `custom` allows for available balance or limit validation, `default` does not. If `default` is used, the `consider` field is not used to validate. The validation stops when `default` is used. | enum: ["default", "custom"]; example: "custom" |
| `configs[].scenarios[].condition.amount_to_check_balance` | string (schema `AmountToCheckBalance`) | no | Amount to check for available balance: `amount` or `installment_amount`. `amount` is the principal amount. This field is **REQUIRED** if `type` is `custom`. | enum: ["amount", "installment_amount"]; example: "amount" |
| `configs[].scenarios[].result` | object (schema `ConditionResult`) | no | Expected result described at evaluated conditions. |  |

##### Response 400

400 Example `invalidAccountId` (Invalid account ID):

```json
{
  "code": "WBLC0020",
  "message": "Error parsing account ID to integer number."
}
```

##### Response 404

404 Example `noAccountLimitsFound` (Balance configuration not found):

```json
{
  "code": "WBLC0022",
  "message": "Balance configuration not found."
}
```

##### Response 500

500 Example `internalServerError` (Internal server error):

```json
{
  "code": "EBLC9999",
  "message": "Internal server error."
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WBLC0020` | Error parsing account ID to integer number. |
| 404 | `WBLC0022` | Balance configuration not found. |
| 500 | `EBLC9999` | Internal server error. |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Balance_config_Beta.yaml method=PUT path=/v1/balances-config/{configId} operationId=put-v1-balances-config -->
### `PUT /v1/balances-config/{configId}` — Replace balance configuration

- **operationId:** `put-v1-balances-config`
- **Specification:** `api-specs/Core_platform_-_Balance_config_Beta.yaml` (Core platform - Balance configurations)
- **Server base URL(s):** `https://api-sandbox.pismolabs.io/balances-config`
- **Tags:** `Balance configurations`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Replace an exiting balance configuration.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `configId` | path | yes | string | Balance configuration ID | example: "66954f26-aaef-49c2-b195-47a8f8410df1" |
| `x-tenant` | header | yes | string | Organization ID | example: "20167751b-efd4-494c-9e4f-4b939560ff05" |
| `x-cid` | header | no | string | The Correlation Identifier UUID field links related API requests and events. The `x-cid` can help the Pismo engineering team track everything related to a call. If not passed, this field is automatically generated. | example: "12345" |

#### Request body

Required: yes

> Body description to update a balance configuration.

**Content type `application/json`** — schema: object (schema `PUTBalancesConfigRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `global_configs` | object (schema `GlobalConfig`) | no | Global configuration settings that always apply regardless of the filter. |  |
| `configs` | array of object | no | Array of balance configurations |  |
| `configs[].name` | string (schema `Name`) | no | Configuration name. | example: "Config-multiple-accounts" |
| `configs[].is_active` | boolean (schema `IsActive`) | no | Indicates active configuration. | example: true |
| `configs[].filter_template_id` | string | no | Reference to a filter template ID. Use this to apply a predefined filter template instead of defining filters inline.<br>**Cannot be used together with `filters`.**<br> | example: "test-1" |
| `configs[].filters` | object | no | Inline filter criteria for the configuration. <br>**Cannot be used together with `filter_template_id`.**<br> |  |
| `configs[].filters.processing_codes` | array of string (schema `ProcessingCodes`) | no | A processing code defines how the Pismo platform handles a certain financial operation type. For more information, refer to [Processing codes and transaction types](doc:processing-codes-and-transaction-types). | example: ["01", "03"] |
| `configs[].filters.min_installments` | integer (schema `MinInstallments`) | no | Min installments to validate. | example: 1 |
| `configs[].filters.max_installments` | integer (schema `MaxInstallments`) | no | Max installments to validate. | example: 12 |
| `configs[].filters.mcc` | array of string (schema `MCC`) | no | Merchant category codes to validate. | example: ["1234", "2626"] |
| `configs[].filters.account_type` | string (schema `AccountType`) | no | Account type that impacts limit or different account.<br>Account types:<br>"00" = Non-specified account<br>"10" = Savings account<br>"20" = Checking account<br>"30" = Credit card account<br> | enum: ["00", "10", "20", "30"]; example: "00" |
| `configs[].filters.currency_code` | string (schema `CurrencyCode`) | no | Alphanumeric ISO 4217 standard currency code that impacts different limits or accounts. | example: "USD" |
| `configs[].scenarios` | array of object | no | Balance configuration scenarios. Scenarios determine how the evaluated transactions impact balances and limits. |  |
| `configs[].scenarios[].condition` | object | no | Evaluated condition. |  |
| `configs[].scenarios[].condition.order` | integer (schema `Order`) | yes | Condition priority order. The lower the number, the higher the priority. | example: 1 |
| `configs[].scenarios[].condition.type` | string (schema `Type`) | yes | Condition type: `default` or `custom`. `custom` allows for available balance or limit validation, `default` does not. If `default` is used, the `consider` field is not used to validate. The validation stops when `default` is used. | enum: ["default", "custom"]; example: "custom" |
| `configs[].scenarios[].condition.amount_to_check_balance` | string (schema `AmountToCheckBalance`) | no | Amount to check for available balance: `amount` or `installment_amount`. `amount` is the principal amount. This field is **REQUIRED** if `type` is `custom`. | enum: ["amount", "installment_amount"]; example: "amount" |
| `configs[].scenarios[].result` | object (schema `ConditionResult`) | no | Expected result described at evaluated conditions. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No content |  |
| 400 | Bad request | `application/json`: object (schema `Error`) |
| 404 | Not found | `application/json`: object (schema `Error`) |
| 500 | Internal server error | `application/json`: object (schema `Error`) |

##### Response 404

404 Example `noAccountLimitsFound` (Config not found):

```json
{
  "code": "WBLC0022",
  "message": "No config found"
}
```

##### Response 500

500 Example `internalServerError` (Internal server error):

```json
{
  "code": "EBLC9999",
  "message": "Internal server error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 404 | `WBLC0022` | No config found |
| 500 | `EBLC9999` | Internal server error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-commercial-cards`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorWithDetails -->
### Schema `ErrorWithDetails`

Pointer: `#/components/schemas/ErrorWithDetails`. Type: object (schema `ErrorWithDetails`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message that describes the error. | example: "An Internal Server Error found, please contact the administrator" |
| `code` | string | no | Code that identifies the error type. | example: "EBLC9999" |
| `details` | array of object (schema `ErrorDetails`) | no |  |  |

<!-- schema: #/components/schemas/Error -->
### Schema `Error`

Pointer: `#/components/schemas/Error`. Type: object (schema `Error`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Message that describes the error. | example: "An Internal Server Error found, please contact the administrator" |
| `code` | string | no | Code that identifies the error type. | example: "EBLC9999" |

<!-- schema: #/components/schemas/GlobalConfig -->
### Schema `GlobalConfig`

Pointer: `#/components/schemas/GlobalConfig`. Type: object (schema `GlobalConfig`).

> Global configuration settings that always apply regardless of the filter.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `impact_parent_accounts` | boolean (schema `ImpactParentAccounts`) | no | Indicates that the ledger should impact parent accounts also. | example: true |

<!-- schema: #/components/schemas/ConditionResult -->
### Schema `ConditionResult`

Pointer: `#/components/schemas/ConditionResult`. Type: object (schema `ConditionResult`).

> Expected result described at evaluated conditions.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `amount` | string (schema `Amount`) | yes | Amount used to credit or debit the account balances or limits. *  `principal_amount`: Original amount, excluding any interest or fees. *  `contract_amount`: Final amount, including any interest or fees. *  `installment_amount`: Amount of each portion of an installment plan.<br> | enum: ["principal_amount", "contract_amount", "installment_amount"]; example: "contract_amount" |
| `impact` | array of string (schema `Impact`) | yes | Limits or balances credited or debited. Can be none when the condition doesn't impact any balances or limits. | example: ["AvailableCreditLimit"]; items.enum: ["AvailableCreditLimit", "AvailableTotalInstallmentCredit", "AvailableWithdrawalCredit", "AvailableSavingsAccountLimit", "AdditionalFunds", "HeldFunds"] |
| `consider` | array of string (schema `Consider`) | no | Limits or balances summed for authorization.<br><br>If `type` = `custom`:<br>  * The sum is validated against `amount_to_check_balance`.<br>  * If this field is not passed, what's in `impact` is summed instead and used for validation.<br>  <br>If `type` = `default`:<br>  * This object is ignored and no validation is done.<br>  * Since no validation is done, `impact` is not used instead if this object is not passed.<br> | example: ["OverLimit", "AvailableCreditLimit"]; items.enum: ["AvailableCreditLimit", "OverLimit", "AvailableSavingsAccountLimit", "AvailableWithdrawalCredit", "AvailableTotalInstallmentCredit"] |
| `amount_consider` | string (schema `AmountConsider`) | no | Amount considered to validate whether the account has sufficient limit or balance. *  `principal_amount`: Original amount, excluding any interest or fees. *  `contract_amount`: Final amount, including any interest or fees. *  `installment_amount`: Amount of each portion of an installment plan.<br> | enum: ["principal_amount", "contract_amount", "installment_amount"]; example: "principal_amount" |
| `reset_limit` | string (schema `ResetLimit`) | no | Indicates when the limit resets. * `never`: Limit referenced in the authorization is never reset. * `payment`: Limit resets when the client pays the credit card bill. * `last_installment`: Limit resets after last customer installment payment.<br> | enum: ["never", "payment", "last_installment"]; example: "never" |
| `impact_account` | object (schema `ImpactAccount`) | no | Impacted account with credit or debit applied. `impact_account` must be related to the principal account. Only available for account-level configurations. For more information, refer to [Related accounts](doc:related-accounts). |  |
| `counterpart_account` | object (schema `CounterpartAccount`) | no | This counter account must be related to the principal account. This account is impacted in the same amount with an opposite transaction operation from the operation for the `impact_account`. For example, if `impact_account` is debited $100, `counterpart_account` is credited $100. Only available for account-level configurations. For more information, refer to [Related accounts](doc:related-accounts). |  |
| `confirmation` | object (schema `Confirmation`) | no | Confirmation indicates which balances must be impacted upon confirmation in dual message scenarios where authorization impacts one balance but confirmation should impact a different balance. |  |
| `opposite_impact` | array of string (schema `MainOppositeImpact`) | no | This field contains a list of limits that should be oppositely impacted in response to the `operation_type`. For instance, if a credit operation affects `AvailableCreditLimit`, the limits specified in this list will be debited to counterbalance the credit impact. | example: ["HeldFunds"]; items.enum: ["AvailableCreditLimit", "AvailableSavingsAccountLimit", "AvailableWithdrawalCredit", "AvailableTotalInstallmentCredit", "HeldFunds", "AdditionalFunds"] |

<!-- schema: #/components/schemas/ErrorDetails -->
### Schema `ErrorDetails`

Pointer: `#/components/schemas/ErrorDetails`. Type: object (schema `ErrorDetails`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `location` | string | no | Location describes the attribute when the error is present. | example: "payload.attribute" |
| `message` | string | no | Message that describes the error detail. | example: "attribute is null" |

<!-- schema: #/components/schemas/ImpactAccount -->
### Schema `ImpactAccount`

Pointer: `#/components/schemas/ImpactAccount`. Type: object (schema `ImpactAccount`).

> Impacted account with credit or debit applied. `impact_account` must be related to the principal account. Only available for account-level configurations. For more information, refer to [Related accounts](doc:related-accounts).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountId`) | no | Account ID. **REQUIRED** if `level` is `account`. | example: 999 |
| `customer_id` | integer | no | Impacted customer ID. | example: 5678 |

<!-- schema: #/components/schemas/CounterpartAccount -->
### Schema `CounterpartAccount`

Pointer: `#/components/schemas/CounterpartAccount`. Type: object (schema `CounterpartAccount`).

> This counter account must be related to the principal account. This account is impacted in the same amount with an opposite transaction operation from the operation for the `impact_account`. For example, if `impact_account` is debited $100, `counterpart_account` is credited $100. Only available for account-level configurations. For more information, refer to [Related accounts](doc:related-accounts).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountId`) | no | Account ID. **REQUIRED** if `level` is `account`. | example: 999 |
| `processing_code` | string | no | Counterpart account processing code. | example: "007700" |

<!-- schema: #/components/schemas/Confirmation -->
### Schema `Confirmation`

Pointer: `#/components/schemas/Confirmation`. Type: object (schema `Confirmation`).

> Confirmation indicates which balances must be impacted upon confirmation in dual message scenarios where authorization impacts one balance but confirmation should impact a different balance.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `impact` | array of string (schema `Impact`) | no | Limits or balances credited or debited. Can be none when the condition doesn't impact any balances or limits. | example: ["AvailableCreditLimit"]; items.enum: ["AvailableCreditLimit", "AvailableTotalInstallmentCredit", "AvailableWithdrawalCredit", "AvailableSavingsAccountLimit", "AdditionalFunds", "HeldFunds"] |
| `opposite_impact` | array of string (schema `MainOppositeImpact`) | no | This field contains a list of limits that should be oppositely impacted in response to the `operation_type`. For instance, if a credit operation affects `AvailableCreditLimit`, the limits specified in this list will be debited to counterbalance the credit impact. | example: ["HeldFunds"]; items.enum: ["AvailableCreditLimit", "AvailableSavingsAccountLimit", "AvailableWithdrawalCredit", "AvailableTotalInstallmentCredit", "HeldFunds", "AdditionalFunds"] |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Balance_config_Beta.yaml` | tag `Balance configurations`: GET /v1/balances-config, POST /v1/balances-config, GET /v1/balances-config/{configId}, PUT /v1/balances-config/{configId} | https://github.com/PismoDevEx/pismo-api-specs | `76e234253e991b98…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-funds-coverage` — Funds coverage
- `KU-CORE-balance-configurations` — Balance configurations and filter templates
- `KU-CORE-commercial-cards` — Commercial cards programs
- `KU-CORE-over-limit-fee` — Over-limit fees
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
