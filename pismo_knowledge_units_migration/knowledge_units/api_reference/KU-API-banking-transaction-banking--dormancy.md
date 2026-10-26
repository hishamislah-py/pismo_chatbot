---
ku_id: KU-API-banking-transaction-banking--dormancy
title: 'API reference: Banking - Transaction banking — Dormancy'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Banking_-_Transaction_banking.yaml
  sha256: dec6c4900eb2db35c29c0f0380763da5ae0e1a18c4ad1e293216b2b6effdab56
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
- post-dormancy-config-v2
- list-dormancy-configs
- getDormancyConfig
- patch-dormancy-config-v2
- getAccountDormancy
related_kus:
- KU-BANK-dormancy
- KU-BANK-get-started-transaction-banking
- KU-BANK-managing-account-statuses
- KU-BANK-restrictions
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wcac
- KU-EVT-catalogue-corporate
- KU-EVT-corporate-banking-data-events
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Dormancy

**KU ID:** `KU-API-banking-transaction-banking--dormancy` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Dormancy` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Dormancy endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /corporate/v2/dormancy-config` | `post-dormancy-config-v2` | Create dormancy configuration | no |
| `GET /corporate/v1/dormancy-config` | `list-dormancy-configs` | List dormancy configurations | no |
| `GET /corporate/v1/dormancy-config/{dormancyConfigId}` | `getDormancyConfig` | Get dormancy configuration | no |
| `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` | `patch-dormancy-config-v2` | Update dormancy configuration | no |
| `GET /corporate/v1/account-dormancy/{externalAccountId}` | `getAccountDormancy` | Get account dormancy | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/dormancy-config operationId=post-dormancy-config-v2 -->
### `POST /corporate/v2/dormancy-config` — Create dormancy configuration

- **operationId:** `post-dormancy-config-v2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Dormancy`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create a dormancy configuration at the division or program level. This configuration sets the days of inactivity required for accounts to switch to a dormant status and the reason for the switch.
> The dormancy configuration is applied to all accounts under the specified division or program.
> Automated dormancy checks are performed according to the number of days specified in the dormancy configuration.
>
> For information about dormancy, refer to [Dormancy overview](doc:dormancy-overview).
>
> This endpoint generates a [Dormancy configuration created](https://developers.pismo.io/events/docs/corporate-dormancy-config-creation-1) event.

#### Request body

Required: yes

> Create dormancy configuration request body

**Content type `application/json`** — schema: object (schema `CreateDormancyConfigRequestv2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_time` | string (schema `DormancyCheckTime`) | yes | Dormancy check time<br><br><b>Note</b>: The timezone is inherited from the customer's divisions or programs.<br> | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "09:00:00" |
| `target_type` | string (schema `DormancyTargetType`) | yes | Dormancy configuration target | enum: ["DIVISION", "PROGRAM"]; example: "DIVISION" |
| `target_id` | string (schema `TargetID`) | yes | Target ID. When `target_type` is `DIVISION`, this value is the division code. Likewise, when `target_type` is `PROGRAM`, the value is the program ID, and so on. | maxLength: 60; example: "my-division-code" |
| `statuses` | array of object | yes | List of objects containing all the information pertinent to an organization's valid account status |  |
| `statuses[].status` | string (schema `AccountStatus`) | yes | Account status<br><br>`minLength: 1`<br>`maxLength: 9`<br> | minLength: 1; maxLength: 9; example: "DORMANT" |
| `statuses[].days` | integer (schema `InactivityDays`) | yes | Days the account must be inactive before it is transitioned to the specified status. | format: "int32"; example: 19 |
| `statuses[].reason_external_id` | string (schema `AccountStatusReasonExternalID`) | yes | External reason ID specifying account restrictions<br><br>`minimum: 1`<br>`maximum: 120`<br> | minLength: 1; maxLength: 120; example: "CREDIT_ONLY" |
| `statuses[].reactivation_with_last_restriction` | boolean (schema `ReactivationWithLastRestriction`) | no | Whether the account should be reactivated to `normal` with its last manual change restriction (`true`) or not (`false`). | example: false |
| `statuses[].restrictions` | array of object (schema `DormancyRestrictionsv2`) | no | Objects that contain the information related to account dormancy restrictions.<br> |  |
| `statuses[].restrictions[].current_reason_external_id` | string (schema `CurrentReasonExternalID`) | no | The custom reason ID related to the `current_reason_id` specified in the dormancy restrictions.<br>The dormancy configuration checks to see whether the current `reason_external_id` matches the one in the configuration. If yes, the new `reason_external_id` is the `new_reason_external_id`.<br> | example: "CREDIT_ONLY" |
| `statuses[].restrictions[].new_reason_external_id` | string (schema `NewReasonExternalID`) | no | The custom reason ID related to the `new_reason_id` specified in the dormancy restrictions.<br> | example: "DEBIT_ONLY" |
| `dormant_processing_codes` | array of string (schema `ValidProcessingCode`) (schema `DormantProcessingCodes`) | no | List of processing codes that prevent account reactivation. If there are financial transactions in an account that were made with any of these codes, the account cannot be reactivated. | items.minLength: 1; items.maxLength: 6 |
| `deny_forced_transaction_reactivation` | boolean (schema `DenyForcedTransactionReactivation`) | no | Whether an account under that dormancy configuration should be reactivated when a forced transaction is made to that account (`true`) or not (`false`). | default: false; example: true |
| `check_timezone_origin` | string (schema `CheckTimezoneOrigin`) | no | Specify whether the dormancy check uses the timezone of the account’s program or division. If not specified, the timezone of `target_id` is used. | enum: ["PROGRAM", "DIVISION"]; example: "PROGRAM" |
| `reactivation_exceptions_config` | object (schema `ReactivationExceptionsConfig`) | no | Specifies configuration rules that allow certain transactions to bypass dormancy reactivation based on defined transaction attributes and their corresponding values. |  |

Example `Example dormancy configuration structure`:

```json
{
  "check_time": "22:00:00",
  "target_type": "DIVISION",
  "target_id": "abc-0001",
  "statuses": [
    {
      "status": "INACTIVE",
      "days": 60,
      "reason_id": 1,
      "reason_external_id": "01",
      "restrictions": [
        {
          "current_reason_id": 13
        },
        {
          "new_reason_id": 16
        }
      ],
      "reactivation_with_last_restriction": true
    },
    {
      "status": "UNCLAIMED",
      "days": 120,
      "reason_id": 2,
      "reason_external_id": "02",
      "reactivation_with_last_restriction": false
    },
    {
      "status": "DORMANT",
      "days": 180,
      "reason_id": 3,
      "reason_external_id": "03",
      "reactivation_with_last_restriction": false
    }
  ],
  "dormant_processing_codes": [
    "100000",
    "100001"
  ],
  "deny_forced_transaction_reactivation": true,
  "reactivation_exceptions_config": {
    "field": "soft_descriptor",
    "values": [
      "001",
      "002",
      "003"
    ]
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateDormancyConfigResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_time` | string (schema `DormancyCheckTime`) | yes | Dormancy check time<br><br><b>Note</b>: The timezone is inherited from the customer's divisions or programs.<br> | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "09:00:00" |
| `target_type` | string (schema `DormancyTargetType`) | yes | Dormancy configuration target | enum: ["DIVISION", "PROGRAM"]; example: "DIVISION" |
| `target_id` | string (schema `TargetID`) | yes | Target ID. When `target_type` is `DIVISION`, this value is the division code. Likewise, when `target_type` is `PROGRAM`, the value is the program ID, and so on. | maxLength: 60; example: "my-division-code" |
| `statuses` | array of object | yes | List of objects containing all the information pertinent to an organization's valid account status |  |
| `statuses[].status` | string (schema `AccountStatus`) | yes | Account status<br><br>`minLength: 1`<br>`maxLength: 9`<br> | minLength: 1; maxLength: 9; example: "DORMANT" |
| `statuses[].days` | integer (schema `InactivityDays`) | yes | Days the account must be inactive before it is transitioned to the specified status. | format: "int32"; example: 19 |
| `statuses[].reactivation_with_last_restriction` | boolean (schema `ReactivationWithLastRestriction`) | no | Whether the account should be reactivated to `normal` with its last manual change restriction (`true`) or not (`false`). | example: false |
| `statuses[].reason_id` | integer (schema `AccountStatusReasonID`) | yes | Account status reason ID<br><br>`minimum: 1`<br> | format: "int64"; minimum: 1; example: 1438 |
| `statuses[].reason_external_id` | string (schema `AccountStatusReasonExternalID`) | no | External reason ID specifying account restrictions<br><br>`minimum: 1`<br>`maximum: 120`<br> | minLength: 1; maxLength: 120; example: "CREDIT_ONLY" |
| `statuses[].restrictions` | array of object (schema `DormancyRestrictions`) | no | List of objects that contains the information related to account dormancy restrictions.<br><br>If there is a restriction in the list and the account's current reason is different from the value in `current_reason_id`, the dormancy configuration sets the reason to the value of the `reason_id` field. However, If the account's current reason is identical to the one in `current_reason_id`, the dormancy configuration sets the value to the `new_reason_id` field; in other words, the value in `new_reason_id` is the result of `reason_id` plus `current_reason_id`.<br> |  |
| `statuses[].restrictions[].current_reason_id` | integer (schema `CurrentReasonID`) | yes | The dormancy configuration checks whether the current account `reason_id` is the same as the current account reason. If they are different, the dormancy configuration sets the reason to the value in the `reason_id` field. | example: 13 |
| `statuses[].restrictions[].new_reason_id` | integer (schema `NewReasonID`) | yes | This is the reason ID when the current account `reason_id` value is the same as `current_reason_id`. | example: 16 |
| `statuses[].restrictions[].current_reason_external_id` | string (schema `CurrentReasonExternalID`) | no | The custom reason ID related to the `current_reason_id` specified in the dormancy restrictions.<br>The dormancy configuration checks to see whether the current `reason_external_id` matches the one in the configuration. If yes, the new `reason_external_id` is the `new_reason_external_id`.<br> | example: "CREDIT_ONLY" |
| `statuses[].restrictions[].new_reason_external_id` | string (schema `NewReasonExternalID`) | no | The custom reason ID related to the `new_reason_id` specified in the dormancy restrictions.<br> | example: "DEBIT_ONLY" |
| `dormancy_config_validity` | object (schema `DormancyConfigValidityWithoutEnd`) | yes | The datetimes for dormancy configuration validity |  |
| `dormant_processing_codes` | array of string (schema `ValidProcessingCode`) (schema `DormantProcessingCodes`) | no | List of processing codes that prevent account reactivation. If there are financial transactions in an account that were made with any of these codes, the account cannot be reactivated. | items.minLength: 1; items.maxLength: 6 |
| `deny_forced_transaction_reactivation` | boolean (schema `DenyForcedTransactionReactivation`) | no | Whether an account under that dormancy configuration should be reactivated when a forced transaction is made to that account (`true`) or not (`false`). | default: false; example: true |
| `id` | string (schema `DormancyConfigID`) | no | Dormancy configuration ID generated internally | format: "uuid"; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `check_timezone_origin` | string (schema `CheckTimezoneOrigin`) | no | Specify whether the dormancy check uses the timezone of the account’s program or division. If not specified, the timezone of `target_id` is used. | enum: ["PROGRAM", "DIVISION"]; example: "PROGRAM" |
| `reactivation_exceptions_config` | object (schema `ReactivationExceptionsConfig`) | no | Specifies configuration rules that allow certain transactions to bypass dormancy reactivation based on defined transaction attributes and their corresponding values. |  |

201 Example `Dormancy configuration`:

```json
{
  "id": "c49cf5f4-762a-429b-83cc-3a1bf2969e2e",
  "check_time": "09:00:00",
  "target_type": "DIVISION",
  "target_id": "my-division-code",
  "statuses": [
    {
      "status": "DORMANT",
      "days": 1,
      "reason_id": 1618,
      "reason_external_id": "CREDIT_ONLY",
      "restrictions": [
        {
          "current_reason_id": 1421,
          "new_reason_id": 1618,
          "current_reason_external_id": "DEBIT_ONLY",
          "new_reason_external_id": "CREDIT_ONLY"
        }
      ],
      "reactivation_with_last_restriction": false
    }
  ],
  "dormant_processing_codes": [
    "220040"
  ],
  "dormancy_config_validity": {
    "start": "2024-11-06T20:04:25.800Z"
  },
  "deny_forced_transaction_reactivation": false,
  "check_timezone_origin": "PROGRAM",
  "reactivation_exceptions_config": {
    "field": "soft_descriptor",
    "values": [
      "001",
      "002",
      "003"
    ]
  }
}
```

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WDOR0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `check_time required`:

```json
{
  "code": "WDOR0002",
  "message": "check_time is a required field"
}
```

400 Example `check_time invalid format`:

```json
{
  "code": "WDOR0002",
  "message": "check_time has invalid format"
}
```

400 Example `target_type required`:

```json
{
  "code": "WDOR0002",
  "message": "target_type is a required field"
}
```

400 Example `target_type one of`:

```json
{
  "code": "WDOR0002",
  "message": "target_type must be one of [DIVISION PROGRAM]"
}
```

400 Example `target_id required`:

```json
{
  "code": "WDOR0002",
  "message": "target_id is a required field. If the target_type is DIVISION the target_id is the division code. If target_type is PROGRAM the target_id will be the program ID."
}
```

400 Example `statuses.status must be unique`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.status must be unique in the statuses list"
}
```

400 Example `statuses.days must be unique`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.days must be unique in the statuses list"
}
```

400 Example `statuses.days must be greater than 0`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.days must be greater than 0"
}
```

400 Example `statuses should have at least 1 item`:

```json
{
  "code": "WDOR0002",
  "message": "statuses should have at least 1 item"
}
```

400 Example `dormant_processing_codes[i] must be at least 1 character in length`:

```json
{
  "code": "WDOR0002",
  "message": "dormant_processing_codes[i] must be at least 1 character in length"
}
```

400 Example `dormant_processing_codes[i] must be a maximum of 6 characters in length`:

```json
{
  "code": "WDOR0002",
  "message": "dormant_processing_codes[i] must be a maximum of 6 characters in length"
}
```

400 Example `dormant_processing_codes must contain only unique values`:

```json
{
  "code": "WDOR0002",
  "message": "dormant_processing_codes must contain only unique values"
}
```

400 Example `Invalid restrictions.current_reason_external_id field`:

```json
{
  "code": "WDOR0010",
  "message": "Invalid current_reason_external_id, the current_reason_external_id you entered does not exist."
}
```

400 Example `Invalid Restrictions.new_reason_external_id field`:

```json
{
  "code": "WDOR0011",
  "message": "Invalid new_reason_external_id, the new_reason_external_id you entered does not exist."
}
```

400 Example `statuses.status invalid status`:

```json
{
  "code": "WDOR0005",
  "message": "Invalid status {status}"
}
```

400 Example `statuses.reason_external_id invalid reason`:

```json
{
  "code": "WDOR0006",
  "message": "Invalid reason_external_id {reason_id}"
}
```

400 Example `Dormancy configuration already exists`:

```json
{
  "code": "WDOR0008",
  "message": "Dormancy configuration with ID {dormancyID} already exists"
}
```

400 Example `Invalid dormant processing code`:

```json
{
  "code": "WDOR0009",
  "message": "Invalid dormant processing code [{dormant_processing_code}]"
}
```

400 Example `Invalid timezone origin`:

```json
{
  "code": "WDOR0002",
  "message": "check_timezone_origin must be one of [DIVISION PROGRAM]"
}
```

400 Example `Invalid statuses.days`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.days must be less than or equal to 2147483647"
}
```

400 Example `Invalid restrictions.current_reason_external_id`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.restrictions.current_reason_external_id must be unique in the restrictions list"
}
```

400 Example `reactivation_exceptions_config.field must be soft_descriptor or metadata.*`:

```json
{
  "code": "WDOR0002",
  "message": "reactivation_exceptions_config.field must be soft_descriptor or metadata.*"
}
```

##### Response 404

404 Example `program not found`:

```json
{
  "code": "WDOR0004",
  "message": "Program with program_id {targetID} not found"
}
```

404 Example `division not found`:

```json
{
  "code": "WDOR0003",
  "message": "Division with division_code {targetID} not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WDOR0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WDOR0002` | check_time is a required field |
| 400 | `WDOR0010` | Invalid current_reason_external_id, the current_reason_external_id you entered does not exist. |
| 400 | `WDOR0011` | Invalid new_reason_external_id, the new_reason_external_id you entered does not exist. |
| 400 | `WDOR0005` | Invalid status {status} |
| 400 | `WDOR0006` | Invalid reason_external_id {reason_id} |
| 400 | `WDOR0008` | Dormancy configuration with ID {dormancyID} already exists |
| 400 | `WDOR0009` | Invalid dormant processing code [{dormant_processing_code}] |
| 404 | `WDOR0004` | Program with program_id {targetID} not found |
| 404 | `WDOR0003` | Division with division_code {targetID} not found |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `corporate-dormancy-config-creation-1` | https://developers.pismo.io/events/docs/corporate-dormancy-config-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-dormancy`, `KU-BANK-get-started-transaction-banking`, `KU-BANK-managing-account-statuses`, `KU-BANK-restrictions`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/dormancy-config operationId=list-dormancy-configs -->
### `GET /corporate/v1/dormancy-config` — List dormancy configurations

- **operationId:** `list-dormancy-configs`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Dormancy`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Lists all dormancy configurations for an organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cursor` | query | no | string | Cursor to the next page of results. If no value is specified, it fetches the first page. | example: "1234" |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `10` | default: 10; format: "int32"; example: 20 |
| `targetType` | query | no | string | Type of dormancy configuration to list. If you don't specify a type, all types are listed. | enum: ["DIVISION", "PROGRAM"]; example: "DIVISION" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListDormancyConfigResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | The specified resource was not found |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `dormancy_configs` | array of object | no | List of dormancy configurations |  |
| `dormancy_configs[].id` | string (schema `DormancyConfigID`) | no | Dormancy configuration ID generated internally | format: "uuid"; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `dormancy_configs[].check_time` | string (schema `DormancyCheckTime`) | no | Dormancy check time<br><br><b>Note</b>: The timezone is inherited from the customer's divisions or programs.<br> | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "09:00:00" |
| `dormancy_configs[].target_type` | string (schema `DormancyTargetType`) | no | Dormancy configuration target | enum: ["DIVISION", "PROGRAM"]; example: "DIVISION" |
| `dormancy_configs[].target_id` | string (schema `TargetID`) | no | Target ID. When `target_type` is `DIVISION`, this value is the division code. Likewise, when `target_type` is `PROGRAM`, the value is the program ID, and so on. | maxLength: 60; example: "my-division-code" |
| `dormancy_configs[].statuses` | array of object | no | List of objects containing all the information pertinent to an organization's valid account status |  |
| `dormancy_configs[].statuses[].reactivation_with_last_restriction` | boolean (schema `ReactivationWithLastRestriction`) | no | Whether the account should be reactivated to `normal` with its last manual change restriction (`true`) or not (`false`). | example: false |
| `dormancy_configs[].statuses[].status` | string (schema `AccountStatus`) | no | Account status<br><br>`minLength: 1`<br>`maxLength: 9`<br> | minLength: 1; maxLength: 9; example: "DORMANT" |
| `dormancy_configs[].statuses[].days` | integer (schema `InactivityDays`) | no | Days the account must be inactive before it is transitioned to the specified status. | format: "int32"; example: 19 |
| `dormancy_configs[].statuses[].reason_id` | integer (schema `AccountStatusReasonID`) | no | Account status reason ID<br><br>`minimum: 1`<br> | format: "int64"; minimum: 1; example: 1438 |
| `dormancy_configs[].statuses[].reason_external_id` | string (schema `AccountStatusReasonExternalID`) | no | External reason ID specifying account restrictions<br><br>`minimum: 1`<br>`maximum: 120`<br> | minLength: 1; maxLength: 120; example: "CREDIT_ONLY" |
| `dormancy_configs[].statuses[].restrictions` | array of object (schema `DormancyRestrictions`) | no | List of objects that contains the information related to account dormancy restrictions.<br><br>If there is a restriction in the list and the account's current reason is different from the value in `current_reason_id`, the dormancy configuration sets the reason to the value of the `reason_id` field. However, If the account's current reason is identical to the one in `current_reason_id`, the dormancy configuration sets the value to the `new_reason_id` field; in other words, the value in `new_reason_id` is the result of `reason_id` plus `current_reason_id`.<br> |  |
| `dormancy_configs[].statuses[].restrictions[].current_reason_id` | integer (schema `CurrentReasonID`) | yes | The dormancy configuration checks whether the current account `reason_id` is the same as the current account reason. If they are different, the dormancy configuration sets the reason to the value in the `reason_id` field. | example: 13 |
| `dormancy_configs[].statuses[].restrictions[].new_reason_id` | integer (schema `NewReasonID`) | yes | This is the reason ID when the current account `reason_id` value is the same as `current_reason_id`. | example: 16 |
| `dormancy_configs[].statuses[].restrictions[].current_reason_external_id` | string (schema `CurrentReasonExternalID`) | no | The custom reason ID related to the `current_reason_id` specified in the dormancy restrictions.<br>The dormancy configuration checks to see whether the current `reason_external_id` matches the one in the configuration. If yes, the new `reason_external_id` is the `new_reason_external_id`.<br> | example: "CREDIT_ONLY" |
| `dormancy_configs[].statuses[].restrictions[].new_reason_external_id` | string (schema `NewReasonExternalID`) | no | The custom reason ID related to the `new_reason_id` specified in the dormancy restrictions.<br> | example: "DEBIT_ONLY" |
| `dormancy_configs[].dormant_processing_codes` | array of string (schema `ValidProcessingCode`) (schema `DormantProcessingCodes`) | no | List of processing codes that prevent account reactivation. If there are financial transactions in an account that were made with any of these codes, the account cannot be reactivated. | items.minLength: 1; items.maxLength: 6 |
| `dormancy_configs[].dormancy_config_validity` | object (schema `DormancyConfigValidityWithEnd`) | no | The datetimes for dormancy configuration validity |  |
| `dormancy_configs[].deny_forced_transaction_reactivation` | boolean (schema `DenyForcedTransactionReactivation`) | no | Whether an account under that dormancy configuration should be reactivated when a forced transaction is made to that account (`true`) or not (`false`). | default: false; example: true |
| `dormancy_configs[].check_timezone_origin` | string (schema `CheckTimezoneOrigin`) | no | Specify whether the dormancy check uses the timezone of the account’s program or division. If not specified, the timezone of `target_id` is used. | enum: ["PROGRAM", "DIVISION"]; example: "PROGRAM" |
| `pagination` | object (schema `Pagination`) | no | Data related to list pagination using a cursor. |  |

200 Example `Dormancy configuration`:

```json
{
  "dormancy_configs": [
    {
      "id": "11bb6f64-15de-4d88-b77a-988f3e30dc55",
      "check_time": "09:00:00",
      "target_type": "DIVISION",
      "target_id": "my-division-code",
      "statuses": [
        {
          "status": "DORMANT",
          "days": 99,
          "reason_id": 1419,
          "reason_external_id": "01",
          "restrictions": [
            {
              "current_reason_id": 1421,
              "new_reason_id": 1618,
              "current_reason_external_id": "02",
              "new_reason_external_id": "03"
            }
          ],
          "reactivation_with_last_restriction": false
        },
        {
          "status": "INACTIVE",
          "days": 120,
          "reason_id": 1419,
          "reason_external_id": "01",
          "restrictions": [
            {
              "current_reason_id": 1618,
              "new_reason_id": 1619,
              "current_reason_external_id": "03",
              "new_reason_external_id": "04"
            }
          ],
          "reactivation_with_last_restriction": true
        }
      ],
      "dormant_processing_codes": [
        "220040",
        "220042"
      ],
      "dormancy_config_validity": {
        "start": "2024-10-08T17:02:28.441Z",
        "end": "2024-10-08T17:03:31.878Z"
      },
      "deny_forced_transaction_reactivation": true,
      "check_timezone_origin": "PROGRAM"
    }
  ],
  "pagination": {
    "limit": 10,
    "cursor": "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0="
  }
}
```

##### Response 400

400 Example `targetType one of`:

```json
{
  "code": "WDOR0002",
  "message": "targetType param must be one of [DIVISION PROGRAM]"
}
```

400 Example `invalid cursor`:

```json
{
  "code": "WCMN0004",
  "message": "Invalid cursor"
}
```

400 Example `limit exceeded maximum value`:

```json
{
  "code": "WCMN0006",
  "message": "Limit must be less than or equal to 100"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WDOR0002` | targetType param must be one of [DIVISION PROGRAM] |
| 400 | `WCMN0004` | Invalid cursor |
| 400 | `WCMN0006` | Limit must be less than or equal to 100 |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/dormancy-config/{dormancyConfigId} operationId=getDormancyConfig -->
### `GET /corporate/v1/dormancy-config/{dormancyConfigId}` — Get dormancy configuration

- **operationId:** `getDormancyConfig`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Dormancy`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieves a dormancy configuration by its ID. Also returns past configurations if you include a `showPrevious` query parameter set to 'true'.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `dormancyConfigId` | path | yes | string | Dormancy configuration ID. This is the ID that the Pismo platform generates when you use [Create dormancy configuration](ref:post-dormancy-config-v2) to set up dormancy. | example: "1234" |
| `showPrevious` | query | no | boolean | If `true`, returns the previous dormancy configurations.<br>For example, if you use [Update dormancy configuration](ref:patch-dormancy-config-v2) to update an existing dormancy configuration, specifying `true` in this field returns both the current dormancy configuration and the previous ones.<br><br>There is no limit to how many previous dormancy configurations can be returned.<br> | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetDormancyConfigResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | DormancyConfig Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `DormancyConfigID`) | no | Dormancy configuration ID generated internally | format: "uuid"; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `check_time` | string (schema `DormancyCheckTime`) | no | Dormancy check time<br><br><b>Note</b>: The timezone is inherited from the customer's divisions or programs.<br> | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "09:00:00" |
| `target_type` | string (schema `DormancyTargetType`) | no | Dormancy configuration target | enum: ["DIVISION", "PROGRAM"]; example: "DIVISION" |
| `target_id` | string (schema `TargetID`) | no | Target ID. When `target_type` is `DIVISION`, this value is the division code. Likewise, when `target_type` is `PROGRAM`, the value is the program ID, and so on. | maxLength: 60; example: "my-division-code" |
| `statuses` | array of object | no | List of objects containing all the information pertinent to an organization's valid account status |  |
| `statuses[].status` | string (schema `AccountStatus`) | yes | Account status<br><br>`minLength: 1`<br>`maxLength: 9`<br> | minLength: 1; maxLength: 9; example: "DORMANT" |
| `statuses[].days` | integer (schema `InactivityDays`) | yes | Days the account must be inactive before it is transitioned to the specified status. | format: "int32"; example: 19 |
| `statuses[].reactivation_with_last_restriction` | boolean (schema `ReactivationWithLastRestriction`) | no | Whether the account should be reactivated to `normal` with its last manual change restriction (`true`) or not (`false`). | example: false |
| `statuses[].reason_id` | integer (schema `AccountStatusReasonID`) | no | Account status reason ID<br><br>`minimum: 1`<br> | format: "int64"; minimum: 1; example: 1438 |
| `statuses[].reason_external_id` | string (schema `AccountStatusReasonExternalID`) | no | External reason ID specifying account restrictions<br><br>`minimum: 1`<br>`maximum: 120`<br> | minLength: 1; maxLength: 120; example: "CREDIT_ONLY" |
| `statuses[].restrictions` | array of object (schema `DormancyRestrictions`) | no | List of objects that contains the information related to account dormancy restrictions.<br><br>If there is a restriction in the list and the account's current reason is different from the value in `current_reason_id`, the dormancy configuration sets the reason to the value of the `reason_id` field. However, If the account's current reason is identical to the one in `current_reason_id`, the dormancy configuration sets the value to the `new_reason_id` field; in other words, the value in `new_reason_id` is the result of `reason_id` plus `current_reason_id`.<br> |  |
| `statuses[].restrictions[].current_reason_id` | integer (schema `CurrentReasonID`) | yes | The dormancy configuration checks whether the current account `reason_id` is the same as the current account reason. If they are different, the dormancy configuration sets the reason to the value in the `reason_id` field. | example: 13 |
| `statuses[].restrictions[].new_reason_id` | integer (schema `NewReasonID`) | yes | This is the reason ID when the current account `reason_id` value is the same as `current_reason_id`. | example: 16 |
| `statuses[].restrictions[].current_reason_external_id` | string (schema `CurrentReasonExternalID`) | no | The custom reason ID related to the `current_reason_id` specified in the dormancy restrictions.<br>The dormancy configuration checks to see whether the current `reason_external_id` matches the one in the configuration. If yes, the new `reason_external_id` is the `new_reason_external_id`.<br> | example: "CREDIT_ONLY" |
| `statuses[].restrictions[].new_reason_external_id` | string (schema `NewReasonExternalID`) | no | The custom reason ID related to the `new_reason_id` specified in the dormancy restrictions.<br> | example: "DEBIT_ONLY" |
| `dormant_processing_codes` | array of string (schema `ValidProcessingCode`) (schema `DormantProcessingCodes`) | no | List of processing codes that prevent account reactivation. If there are financial transactions in an account that were made with any of these codes, the account cannot be reactivated. | items.minLength: 1; items.maxLength: 6 |
| `dormancy_config_validity` | object (schema `DormancyConfigValidityWithoutEnd`) | no | The datetimes for dormancy configuration validity |  |
| `previous` | array of object (schema `DormancyConfigResponse`) (schema `PreviousDormancyConfigs`) | no | List of previous dormancy configurations. This field is returned only if you pass the query string with `showPrevious` set to `true`. |  |
| `deny_forced_transaction_reactivation` | boolean (schema `DenyForcedTransactionReactivation`) | no | Whether an account under that dormancy configuration should be reactivated when a forced transaction is made to that account (`true`) or not (`false`). | default: false; example: true |
| `check_timezone_origin` | string (schema `CheckTimezoneOrigin`) | no | Specify whether the dormancy check uses the timezone of the account’s program or division. If not specified, the timezone of `target_id` is used. | enum: ["PROGRAM", "DIVISION"]; example: "PROGRAM" |
| `reactivation_exceptions_config` | object (schema `ReactivationExceptionsConfig`) | no | Specifies configuration rules that allow certain transactions to bypass dormancy reactivation based on defined transaction attributes and their corresponding values. |  |

200 Example `Dormancy configuration`:

```json
{
  "id": "72e32c36-b91d-4e87-9a23-923ef4e9a7e7",
  "check_time": "08:00:00",
  "target_type": "DIVISION",
  "target_id": "my-division-code",
  "statuses": [
    {
      "status": "DORMANT",
      "days": 19,
      "reason_id": 1438,
      "reason_external_id": "CREDIT_ONLY_NO_FORCE_DEBIT_ALLOWED",
      "restrictions": [
        {
          "current_reason_id": 1421,
          "new_reason_id": 1620,
          "current_reason_external_id": "DEBIT_ONLY",
          "new_reason_external_id": "NONE"
        }
      ],
      "reactivation_with_last_restriction": false
    },
    {
      "status": "INACTIVE",
      "days": 110,
      "reason_id": 1441,
      "reason_external_id": "NONE_NO_FORCE_ALLOWED",
      "restrictions": [
        {
          "current_reason_id": 1619,
          "new_reason_id": 1620,
          "current_reason_external_id": "ALL",
          "new_reason_external_id": "NONE"
        }
      ],
      "reactivation_with_last_restriction": true
    }
  ],
  "dormant_processing_codes": [
    "220040",
    "220042"
  ],
  "dormancy_config_validity": {
    "start": "2024-10-18T17:45:26.930Z"
  },
  "reactivation_exceptions_config": {
    "field": "soft_descriptor",
    "values": [
      "001",
      "002",
      "003"
    ]
  },
  "previous": [
    {
      "id": "11bb6f64-15de-4d88-b77a-988f3e30dc55",
      "check_time": "09:00:00",
      "target_type": "DIVISION",
      "target_id": "my-division-code",
      "statuses": [
        {
          "status": "DORMANT",
          "days": 199,
          "reason_id": 1419,
          "reason_external_id": "01",
          "restrictions": {
            "current_reason_id": 1421,
            "new_reason_id": 1618,
            "current_reason_external_id": "02",
            "new_reason_external_id": "03"
          },
          "reactivation_with_last_restriction": false
        },
        {
          "status": "INACTIVE",
          "days": 110,
          "reason_id": 1419,
          "reason_external_id": "01",
          "restrictions": {
            "current_reason_id": 1618,
            "new_reason_id": 1438,
            "current_reason_external_id": "03",
            "new_reason_external_id": "05"
          },
          "reactivation_with_last_restriction": true
        }
      ],
      "dormant_processing_codes": [
        "220040",
        "220042"
      ],
      "dormancy_config_validity": {
        "start": "2024-10-08T17:54:21.540Z",
        "end": "2024-10-18T17:45:26.922Z"
      },
      "deny_forced_transaction_reactivation": true,
      "check_timezone_origin": "PROGRAM",
      "reactivation_exceptions_config": {
        "field": "soft_descriptor",
        "values": [
          "001",
          "002",
          "003"
        ]
      }
    }
  ]
}
```

##### Response 400

400 Example `Missing HTTP parameters`:

```json
{
  "code": "WCMN0003",
  "message": "Missing HTTP parameters"
}
```

##### Response 404

404 Example `DormancyConfig Not Found`:

```json
{
  "code": "WDOR0007",
  "message": "Dormancy configuration with ID {dormancyConfigId} not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCMN0003` | Missing HTTP parameters |
| 404 | `WDOR0007` | Dormancy configuration with ID {dormancyConfigId} not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v2/dormancy-config/{dormancyConfigId} operationId=patch-dormancy-config-v2 -->
### `PATCH /corporate/v2/dormancy-config/{dormancyConfigId}` — Update dormancy configuration

- **operationId:** `patch-dormancy-config-v2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Dormancy`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Updates a dormancy configuration for a division or program.
>
> This endpoint generates a [Dormancy configuration updated](https://developers.pismo.io/events/docs/corporate-dormancy-config-change-1) event.
> See [Data and reporting](doc:data-reporting-overview) for more information about events and setting up event notifications.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `dormancyConfigId` | path | yes | string | Dormancy configuration ID. This is the ID that the Pismo platform generates when you use [Create dormancy configuration](ref:post-dormancy-config-v2) to set up dormancy. | example: "1234" |

#### Request body

Required: yes

> Dormancy configuration request body

**Content type `application/json`** — schema: object (schema `UpdateDormancyConfigRequestv2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `check_time` | string (schema `DormancyCheckTime`) | no | Dormancy check time<br><br><b>Note</b>: The timezone is inherited from the customer's divisions or programs.<br> | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "09:00:00" |
| `statuses` | array of object | no | List of objects containing information related to an organization's valid account status | maxItems: 3 |
| `statuses[].status` | string (schema `AccountStatus`) | yes | Account status<br><br>`minLength: 1`<br>`maxLength: 9`<br> | minLength: 1; maxLength: 9; example: "DORMANT" |
| `statuses[].days` | integer (schema `InactivityDays`) | yes | Days the account must be inactive before it is transitioned to the specified status. | format: "int32"; example: 19 |
| `statuses[].reason_external_id` | string (schema `StatusReasonExternalID`) | yes | Custom reason ID for the specified status. This field is unique within the organization and is related to the `reason_id` field. | example: "CREDIT ONLY" |
| `statuses[].reactivation_with_last_restriction` | boolean (schema `ReactivationWithLastRestriction`) | no | Whether the account should be reactivated to `normal` with its last manual change restriction (`true`) or not (`false`). | example: false |
| `statuses[].restrictions` | array of object (schema `DormancyRestrictionsv2`) | no | Objects that contain the information related to account dormancy restrictions.<br> |  |
| `statuses[].restrictions[].current_reason_external_id` | string (schema `CurrentReasonExternalID`) | no | The custom reason ID related to the `current_reason_id` specified in the dormancy restrictions.<br>The dormancy configuration checks to see whether the current `reason_external_id` matches the one in the configuration. If yes, the new `reason_external_id` is the `new_reason_external_id`.<br> | example: "CREDIT_ONLY" |
| `statuses[].restrictions[].new_reason_external_id` | string (schema `NewReasonExternalID`) | no | The custom reason ID related to the `new_reason_id` specified in the dormancy restrictions.<br> | example: "DEBIT_ONLY" |
| `dormant_processing_codes` | array of string (schema `ValidProcessingCode`) (schema `DormantProcessingCodes`) | no | List of processing codes that prevent account reactivation. If there are financial transactions in an account that were made with any of these codes, the account cannot be reactivated. | items.minLength: 1; items.maxLength: 6 |
| `deny_forced_transaction_reactivation` | boolean (schema `DenyForcedTransactionReactivation`) | no | Whether an account under that dormancy configuration should be reactivated when a forced transaction is made to that account (`true`) or not (`false`). | default: false; example: true |
| `reactivation_exceptions_config` | object (schema `ReactivationExceptionsConfig`) | no | Specifies configuration rules that allow certain transactions to bypass dormancy reactivation based on defined transaction attributes and their corresponding values. |  |

Example `New dormancy-config`:

```json
{
  "check_time": "22:00:01",
  "statuses": [
    {
      "status": "INACTIVE",
      "days": 60,
      "reason_id": 3,
      "reason_external_id": "03",
      "restrictions": [
        {
          "current_reason_id": 13
        },
        {
          "new_reason_id": 16
        }
      ],
      "reactivation_with_last_restriction": true
    },
    {
      "status": "UNCLAIMED",
      "days": 120,
      "reason_id": 2,
      "reason_external_id": "02",
      "reactivation_with_last_restriction": false
    },
    {
      "status": "DORMANT",
      "days": 180,
      "reason_id": 1,
      "reason_external_id": "01",
      "reactivation_with_last_restriction": false
    }
  ],
  "dormant_processing_codes": [
    "100000",
    "100001"
  ],
  "deny_forced_transaction_reactivation": true,
  "reactivation_exceptions_config": {
    "field": "soft_descriptor",
    "values": [
      "001",
      "002",
      "003"
    ]
  }
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WDOR0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `check_time required`:

```json
{
  "code": "WDOR0002",
  "message": "check_time is a required field"
}
```

400 Example `check_time invalid format`:

```json
{
  "code": "WDOR0002",
  "message": "check_time has invalid format"
}
```

400 Example `statuses.status must be unique`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.status must be unique in the statuses list"
}
```

400 Example `statuses.days must be unique`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.days must be unique in the statuses list"
}
```

400 Example `statuses.days must be greater than 0`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.days must be greater than 0"
}
```

400 Example `statuses should have at least 1 item`:

```json
{
  "code": "WDOR0002",
  "message": "statuses should have at least 1 item"
}
```

400 Example `dormant_processing_codes[i] must be at least 1 character in length`:

```json
{
  "code": "WDOR0002",
  "message": "dormant_processing_codes[i] must be at least 1 character in length"
}
```

400 Example `dormant_processing_codes[i] must be a maximum of 6 characters in length`:

```json
{
  "code": "WDOR0002",
  "message": "dormant_processing_codes[i] must be a maximum of 6 characters in length"
}
```

400 Example `dormant_processing_codes must contain only unique values`:

```json
{
  "code": "WDOR0002",
  "message": "dormant_processing_codes must contain only unique values"
}
```

400 Example `Invalid Restrictions.current_reason_external_id field`:

```json
{
  "code": "WDOR0010",
  "message": "Invalid current_reason_external_id, the current_reason_external_id you entered does not exist."
}
```

400 Example `Invalid Restrictions.new_reason_external_id field`:

```json
{
  "code": "WDOR0011",
  "message": "Invalid new_reason_external_d, the new_reason_external_id you entered does not exist."
}
```

400 Example `statuses.status invalid status`:

```json
{
  "code": "WDOR0005",
  "message": "Invalid status {status}"
}
```

400 Example `statuses.reason_external_id invalid reason`:

```json
{
  "code": "WDOR0006",
  "message": "Invalid reason_external_id {reason_id}"
}
```

400 Example `Invalid dormant processing code`:

```json
{
  "code": "WDOR0009",
  "message": "Invalid dormant processing code [{dormant_processing_code}]"
}
```

400 Example `Invalid timezone origin`:

```json
{
  "code": "WDOR0002",
  "message": "check_timezone_origin must be one of [DIVISION PROGRAM]"
}
```

400 Example `Invalid statuses.days`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.days must be less than or equal to 2147483647"
}
```

400 Example `Invalid restrictions.current_reason_external_id`:

```json
{
  "code": "WDOR0002",
  "message": "statuses.restrictions.current_reason_external_id must be unique in the restrictions list"
}
```

400 Example `reactivation_exceptions_config.field must be soft_descriptor or metadata.*`:

```json
{
  "code": "WDOR0002",
  "message": "reactivation_exceptions_config.field must be soft_descriptor or metadata.*"
}
```

##### Response 404

404 Example `DormancyConfig not found`:

```json
{
  "code": "WDOR0007",
  "message": "Dormancy configuration with ID {dormancyConfigId} not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WDOR0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WDOR0002` | check_time is a required field |
| 400 | `WDOR0010` | Invalid current_reason_external_id, the current_reason_external_id you entered does not exist. |
| 400 | `WDOR0011` | Invalid new_reason_external_d, the new_reason_external_id you entered does not exist. |
| 400 | `WDOR0005` | Invalid status {status} |
| 400 | `WDOR0006` | Invalid reason_external_id {reason_id} |
| 400 | `WDOR0009` | Invalid dormant processing code [{dormant_processing_code}] |
| 404 | `WDOR0007` | Dormancy configuration with ID {dormancyConfigId} not found |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `corporate-dormancy-config-change-1` | https://developers.pismo.io/events/docs/corporate-dormancy-config-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;401;403;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-dormancy`, `KU-BANK-managing-account-statuses`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v1/account-dormancy/{externalAccountId} operationId=getAccountDormancy -->
### `GET /corporate/v1/account-dormancy/{externalAccountId}` — Get account dormancy

- **operationId:** `getAccountDormancy`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Dormancy`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Retrieves an account dormancy configuration by the account external ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetAccountDormancyResponse`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `DormancyControlID`) | no | Account dormancy control ID generated internally | format: "uuid" |
| `external_account_id` | string (schema `ExternalAccountID`) | no | Custom account ID. Used as the key for all operations (manage accounts, transactions, etc.) on the corporate layer.<br><br>This field is:<br>- Unique within the Organization<br>- Immutable: The field cannot be updated.<br>- Not recyclable: You can't reuse an external account ID, even if the account that was using it has been canceled.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1234 |
| `dormancy_config_id` | string (schema `DormancyConfigID`) | no | Dormancy configuration ID generated internally | format: "uuid"; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `inactive_since` | string (schema `InactiveSince`) | no | Date of the last time the account had any activities. Format = yyyy-mm-dd:hr:mm:ss. | example: "2023-08-04T15:00:44.704Z" |
| `inactivity_time` | integer (schema `InactivityTime`) | no | Number of days the account has been inactive.<br><br>`inactivity_time` is calculated as `current_datetime` - `inactive_since` in UTC timezone.<br> | format: "int32"; example: 10 |
| `target_type` | string (schema `DormancyTargetType`) | no | Dormancy configuration target | enum: ["DIVISION", "PROGRAM"]; example: "DIVISION" |
| `target_id` | string (schema `TargetID`) | no | Target ID. When `target_type` is `DIVISION`, this value is the division code. Likewise, when `target_type` is `PROGRAM`, the value is the program ID, and so on. | maxLength: 60; example: "my-division-code" |

##### Response 400

400 Example `Invalid header account`:

```json
{
  "code": "WCAC0002",
  "message": "Invalid header account"
}
```

400 Example `Account not authorized`:

```json
{
  "code": "WCAC0001",
  "message": "Account not authorized"
}
```

##### Response 404

404 Example `Account Dormancy Control not found: {externalAccountId}`:

```json
{
  "code": "WADC0002",
  "message": "Account Dormancy Control not found: {externalAccountId}"
}
```

404 Example `Account not found:`:

```json
{
  "code": "WADC0003",
  "message": "Corporate account not found"
}
```

404 Example `Division code not found:`:

```json
{
  "code": "WADC0004",
  "message": "Division with division_code {%s} not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCAC0002` | Invalid header account |
| 400 | `WCAC0001` | Account not authorized |
| 404 | `WADC0002` | Account Dormancy Control not found: {externalAccountId} |
| 404 | `WADC0003` | Corporate account not found |
| 404 | `WADC0004` | Division with division_code {%s} not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ReactivationExceptionsConfig -->
### Schema `ReactivationExceptionsConfig`

Pointer: `#/components/schemas/ReactivationExceptionsConfig`. Type: object (schema `ReactivationExceptionsConfig`).

> Specifies configuration rules that allow certain transactions to bypass dormancy reactivation based on defined transaction attributes and their corresponding values.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string (schema `DormancyExceptionField`) | yes | Specifies which transaction attribute is checked in order to determine whether a transaction is exempt from reactivating a dormant account. | minLength: 1; maxLength: 100; example: "soft_descriptor" |
| `values` | array of string (schema `ValidExceptionValue`) (schema `DormancyExceptionValues`) | yes | Lists the values that, when present in the specified field, prevent the account from being reactivated by that transaction. | maxItems: 30; items.minLength: 1; items.maxLength: 100 |

<!-- schema: #/components/schemas/DormancyConfigValidityWithoutEnd -->
### Schema `DormancyConfigValidityWithoutEnd`

Pointer: `#/components/schemas/DormancyConfigValidityWithoutEnd`. Type: object (schema `DormancyConfigValidityWithoutEnd`).

> The datetimes for dormancy configuration validity

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `start` | string (schema `DormancyConfigStartValid`) | no | Date and time the dormancy configuration starts to be valid. Format = yyyy-mm-dd:hr:mm:ss. | example: "2024-10-18T17:45:26.930Z" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

<!-- schema: #/components/schemas/DormancyConfigValidityWithEnd -->
### Schema `DormancyConfigValidityWithEnd`

Pointer: `#/components/schemas/DormancyConfigValidityWithEnd`. Type: object (schema `DormancyConfigValidityWithEnd`).

> The datetimes for dormancy configuration validity

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `start` | string (schema `DormancyConfigStartValid`) | no | Date and time the dormancy configuration starts to be valid. Format = yyyy-mm-dd:hr:mm:ss. | example: "2024-10-18T17:45:26.930Z" |
| `end` | string (schema `DormancyConfigEndValid`) | no | Date and time the dormancy configuration ceased to be valid. The field is omitted from the response if empty. Format = yyyy-mm-dd:hr:mm:ss. | example: "2023-08-14T22:12:48.961Z" |

<!-- schema: #/components/schemas/Pagination -->
### Schema `Pagination`

Pointer: `#/components/schemas/Pagination`. Type: object (schema `Pagination`).

> Data related to list pagination using a cursor.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `cursor` | string (schema `Cursor`) | no | Cursor pointing to the next page of results | example: "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0=" |

<!-- schema: #/components/schemas/DormancyConfigResponse -->
### Schema `DormancyConfigResponse`

Pointer: `#/components/schemas/DormancyConfigResponse`. Type: object (schema `DormancyConfigResponse`).

> Dormancy-config response object

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `DormancyConfigID`) | no | Dormancy configuration ID generated internally | format: "uuid"; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `check_time` | string (schema `DormancyCheckTime`) | no | Dormancy check time<br><br><b>Note</b>: The timezone is inherited from the customer's divisions or programs.<br> | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "09:00:00" |
| `target_type` | string (schema `DormancyTargetType`) | no | Dormancy configuration target | enum: ["DIVISION", "PROGRAM"]; example: "DIVISION" |
| `target_id` | string (schema `TargetID`) | no | Target ID. When `target_type` is `DIVISION`, this value is the division code. Likewise, when `target_type` is `PROGRAM`, the value is the program ID, and so on. | maxLength: 60; example: "my-division-code" |
| `statuses` | array of object | no | List of objects that contains all the information pertinent to an organization's valid account status |  |
| `statuses[].status` | string (schema `AccountStatus`) | yes | Account status<br><br>`minLength: 1`<br>`maxLength: 9`<br> | minLength: 1; maxLength: 9; example: "DORMANT" |
| `statuses[].days` | integer (schema `InactivityDays`) | yes | Days the account must be inactive before it is transitioned to the specified status. | format: "int32"; example: 19 |
| `statuses[].reason_id` | integer (schema `AccountStatusReasonID`) | yes | Account status reason ID<br><br>`minimum: 1`<br> | format: "int64"; minimum: 1; example: 1438 |
| `dormant_processing_codes` | array of string (schema `ValidProcessingCode`) (schema `DormantProcessingCodes`) | no | List of processing codes that prevent account reactivation. If there are financial transactions in an account that were made with any of these codes, the account cannot be reactivated. | items.minLength: 1; items.maxLength: 6 |
| `dormancy_config_validity` | object (schema `DormancyConfigValidityWithEnd`) | no | The datetimes for dormancy configuration validity |  |
| `deny_forced_transaction_reactivation` | boolean (schema `DenyForcedTransactionReactivation`) | no | Whether an account under that dormancy configuration should be reactivated when a forced transaction is made to that account (`true`) or not (`false`). | default: false; example: true |
| `reactivation_exceptions_config` | object (schema `ReactivationExceptionsConfig`) | no | Specifies configuration rules that allow certain transactions to bypass dormancy reactivation based on defined transaction attributes and their corresponding values. |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Dormancy`: POST /corporate/v2/dormancy-config, GET /corporate/v1/dormancy-config, GET /corporate/v1/dormancy-config/{dormancyConfigId}, PATCH /corporate/v2/dormancy-config/{dormancyConfigId}, GET /corporate/v1/account-dormancy/{externalAccountId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-dormancy` — Dormancy and dormancy reactivation exceptions
- `KU-BANK-get-started-transaction-banking` — Get started with transaction banking
- `KU-BANK-managing-account-statuses` — Manage account statuses
- `KU-BANK-restrictions` — Restrictions: restrict funds, restriction management and operation blocks
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wcac` — Error codes: WCAC
- `KU-EVT-catalogue-corporate` — Event catalogue: corporate
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
