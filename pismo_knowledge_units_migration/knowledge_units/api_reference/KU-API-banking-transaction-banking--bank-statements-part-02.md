---
ku_id: KU-API-banking-transaction-banking--bank-statements-part-02
title: 'API reference: Banking - Transaction banking — Bank statements (part 2 of 2)'
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
- list-account-balance-history-configv2
- post-account-balance-history-configv2
- get-account-balance-history-config-by-id-v2
- patch-account-balances-history-configv2
- get-account-balance-history-config-by-target-v2
related_kus:
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-account
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Bank statements (part 2 of 2)

**KU ID:** `KU-API-banking-transaction-banking--bank-statements-part-02` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Bank statements` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Bank statements endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /bank-statements/v2/account-balances/history/config` | `list-account-balance-history-configv2` | List account balance history config v2 | no |
| `POST /bank-statements/v2/account-balances/history/config` | `post-account-balance-history-configv2` | Create account balance history config v2 | no |
| `GET /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` | `get-account-balance-history-config-by-id-v2` | Get account balance history config by ID v2 | no |
| `PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` | `patch-account-balances-history-configv2` | Update account balance history config v2 | no |
| `GET /bank-statements/v2/account-balances/history/config/{targetType}/{targetId}` | `get-account-balance-history-config-by-target-v2` | Get account balance history config by target type v2 | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/bank-statements/v2/account-balances/history/config operationId=list-account-balance-history-configv2 -->
### `GET /bank-statements/v2/account-balances/history/config` — List account balance history config v2

- **operationId:** `list-account-balance-history-configv2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account balance history configurations by division, organization, or program ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `targetType` | query | yes | string | Balance history configuration to list. If you don't specify a type, all types are listed. | enum: ["DIVISION", "ORGANIZATION", "PROGRAM"]; example: "ORGANIZATION" |
| `balanceHistoryConfigOffset` | query | no | integer | Starting point for the results list. Default is `0`. | format: "int32"; example: 10 |
| `balanceHistoryConfigLimit` | query | no | integer | Maximum number of items per page. Defaults to `10` | format: "int32"; example: 10 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Created | `application/json`: object (schema `ListAccountBalanceHistoryConfigurationResponsev2`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `pagination` | object (schema `OffsetPagination`) | no | Data related to list pagination using an offset parameter |  |
| `items` | object | no |  |  |
| `items.id` | string (schema `AccountBalanceConfigId`) | yes | Balance history configuration ID | format: "uuid"; maxLength: 52; example: "ee665f37-340f-461e-b520-af3b1b61c6ee" |
| `items.target_type` | string (schema `AccountBalanceConfigTargetTypev2`) | yes | Account balance history config target type | enum: ["ORGANIZATION", "PROGRAM", "DIVISION"]; example: "DIVISION" |
| `items.target_id` | string (schema `BalanceHistoryTargetID`) | yes | Target ID (`org_id`, `program_id`, or `division_id`) | minLength: 1; maxLength: 52; example: "my-org-123" |
| `items.cycle_closing_time` | string (schema `CycleClosingTimeV2`) | yes | Cycle closing time indicates what time of day the cycle closes for a division, organization, or program. This time uses the timezone configured for the corresponding division, organization, or program. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "23:00:00" |
| `items.cycle_event_delay` | integer (schema `CycleEventDelay`) | yes | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |
| `items.cycle_config_validity` | object (schema `CycleConfigValidity`) | yes | The start and end date/time indicating when the cycle configuration becomes valid or invalid.<br> |  |

200 Example `Created account balance history config successfully`:

```json
{
  "pagination": {
    "has_next": false,
    "limit": 10,
    "offset": 10
  },
  "items": [
    {
      "id": "ee665f37-340f-461e-b520-af3b1b61c6ee",
      "target_type": "PROGRAM",
      "target_id": "42461",
      "cycle_closing_time": "23:59:59",
      "cycle_event_delay": 60,
      "cycle_config_validity": {
        "start": "2026-03-14T03:59:59Z"
      }
    },
    {
      "id": "e1ba8d9a-88b1-4438-b9d9-d35b502bbc73",
      "target_type": "PROGRAM",
      "target_id": "39830",
      "cycle_closing_time": "23:59:59",
      "cycle_event_delay": 60,
      "cycle_config_validity": {
        "start": "2026-02-26T03:59:59Z"
      }
    }
  ]
}
```

##### Response 400

400 Example `division_code is a required field`:

```json
{
  "code": "WCFG0002",
  "message": "division_code is a required field"
}
```

400 Example `division_code exceed size`:

```json
{
  "code": "WCFG0002",
  "message": "division_code must be a maximum of 36 characters in length"
}
```

400 Example `cycle_closing_time is a required field`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time is a required field"
}
```

400 Example `cycle_closing_time exceed size`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time must be a maximum of 8 characters in length"
}
```

400 Example `cycle_closing_time invalid time format`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time has an invalid time format: {cycle_closing_time}"
}
```

400 Example `cycle_event_delay is a required field`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_event_delay is a required field"
}
```

400 Example `cycle_event_delay must be 5 minutes or greater`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_event_delay must be 5 or greater"
}
```

400 Example `cycle_event_delay exceed maximum minutes`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_event_delay must be 1,439 or less"
}
```

400 Example `Invalid JSON payload received`:

```json
{
  "code": "WCFG0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Invalid request filter`:

```json
{
  "code": "WCFG0002",
  "message": "Invalid request filter"
}
```

400 Example `Invalid request`:

```json
{
  "code": "WCFG0002",
  "message": "Invalid request"
}
```

400 Example `Validation error`:

```json
{
  "code": "WCFG0002",
  "message": "Validation error. The limit must be less than or equal to 100"
}
```

##### Response 404

404 Example `Division not found`:

```json
{
  "code": "WCFG0003",
  "message": "Division not found"
}
```

##### Response 409

409 Example `Division already configured`:

```json
{
  "code": "WCFG0004",
  "message": "Division already configured"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "CMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCFG0002` | division_code is a required field |
| 400 | `WCFG0001` | Invalid JSON payload received: Error unmarshalling request |
| 404 | `WCFG0003` | Division not found |
| 409 | `WCFG0004` | Division already configured |
| 500 | `CMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;409;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/bank-statements/v2/account-balances/history/config operationId=post-account-balance-history-configv2 -->
### `POST /bank-statements/v2/account-balances/history/config` — Create account balance history config v2

- **operationId:** `post-account-balance-history-configv2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an account balance history configuration by division, organization, or program ID.
>
> The configuration becomes effective on the day after the cycle closing time plus the cycle event delay.
> Example:
>   - Division timezone: `UTC`
>   - Create account balance history configuration is called at: `2023-05-01T18:00:00Z`
>   - Account balance history configuration `cycle_closing_time` is: `22:00:00`
>   - Account balance history configuration `cycle_event_delay` is: `10`
>   - Account balance history configuration starts at `2023-05-01T22:10:00Z`
>
> This endpoint generates an [Account balance history configuration created](https://developers.pismo.io/events/docs/account-balances-balance-history-config-creation-1) event.

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `CreateAccountBalanceHistoryConfigurationRequestv2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `target_type` | string (schema `AccountBalanceConfigTargetTypev2`) | yes | Account balance history config target type | enum: ["ORGANIZATION", "PROGRAM", "DIVISION"]; example: "DIVISION" |
| `target_id` | string (schema `TargetID`) | yes | Target ID. When `target_type` is `DIVISION`, this value is the division code. Likewise, when `target_type` is `PROGRAM`, the value is the program ID, and so on. | maxLength: 60; example: "my-division-code" |
| `cycle_closing_time` | string (schema `CycleClosingTimeV2`) | yes | Cycle closing time indicates what time of day the cycle closes for a division, organization, or program. This time uses the timezone configured for the corresponding division, organization, or program. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "23:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | yes | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |

Example `Create account balance history config response`:

```json
{
  "target_type": "ORGANIZATION",
  "target_id": "TN-097d9c0e-0331-492a-93e2-95c8c2019fd1",
  "cycle_closing_time": "23:59:59",
  "cycle_event_delay": 60
}
```

Example `Create account balance history config for a division`:

```json
{
  "target_type": "DIVISION",
  "target_id": "my-division-code",
  "cycle_closing_time": "23:59:59",
  "cycle_event_delay": 60
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateAccountBalanceHistoryConfigurationResponseV2`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `BalanceHistoryConfigID`) | no | Balance history configuration ID | format: "uuid"; example: "550e8400-e29b-41d4-a716-446655440000" |
| `target_type` | string (schema `BalanceHistoryTargetType`) | no | The target type of the balance history configuration, based on the hierarchical level it applies to. | enum: ["ORGANIZATION", "PROGRAM", "DIVISION"]; example: "ORGANIZATION" |
| `target_id` | string (schema `BalanceHistoryTargetID`) | no | Target ID (`org_id`, `program_id`, or `division_id`) | minLength: 1; maxLength: 52; example: "my-org-123" |
| `cycle_closing_time` | string (schema `CycleClosingTime`) | no | Time of day the cycle closes for a division. This time follows the timezone configured in division. You can find the division timezone using the [Get division by code](ref:get-division-by-code-v2) endpoint. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "22:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | no | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |
| `cycle_config_validity` | object (schema `CycleConfigValidity`) | no | The start and end date/time indicating when the cycle configuration becomes valid or invalid.<br> |  |

201 Example `Created account balance history configuration successfully`:

```json
{
  "id": "ee665f37-340f-461e-b520-af3b1b61c6ee",
  "target_type": "PROGRAM",
  "target_id": 42461,
  "cycle_closing_time": "23:59:59",
  "cycle_event_delay": 60,
  "cycle_config_validity": {
    "start": "2026-03-14T00:59:59-03:00"
  }
}
```

##### Response 400

400 Example `Invalid JSON payload received`:

```json
{
  "code": "WCFG0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Missing required field`:

```json
{
  "code": "WCFG0002",
  "message": "missing required field: {target_type} or {cycle_closing_time}"
}
```

400 Example `Invalid request`:

```json
{
  "code": "WCFG0002",
  "message": "Request is invalid"
}
```

400 Example `division_code is a required field`:

```json
{
  "code": "WCFG0002",
  "message": "division_code is a required field"
}
```

400 Example `division_code exceed size`:

```json
{
  "code": "WCFG0002",
  "message": "division_code must be a maximum of 36 characters in length"
}
```

400 Example `cycle_closing_time is a required field`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time is a required field"
}
```

400 Example `cycle_closing_time exceed size`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time must be a maximum of 8 characters in length"
}
```

400 Example `cycle_closing_time invalid time format`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time has an invalid time format: {cycle_closing_time}"
}
```

400 Example `cycle_event_delay is a required field`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_event_delay is a required field"
}
```

400 Example `cycle_event_delay must be 5 minutes or greater`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_event_delay must be 5 or greater"
}
```

400 Example `cycle_event_delay exceed maximum minutes`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_event_delay must be 1,439 or less"
}
```

400 Example `Invalid target type`:

```json
{
  "code": "WCFG0010",
  "message": "Invalid target type"
}
```

400 Example `Invalid target ID`:

```json
{
  "code": "WCFG0011",
  "message": "Invalid target ID"
}
```

##### Response 404

404 Example `Division not found`:

```json
{
  "code": "WCFG0003",
  "message": "Division not found"
}
```

404 Example `Program not found`:

```json
{
  "code": "WCFG0006",
  "message": "Program not found"
}
```

404 Example `Organization not found`:

```json
{
  "code": "WCFG0007",
  "message": "Organization not found"
}
```

##### Response 409

409 Example `Division already configured`:

```json
{
  "code": "WCFG0004",
  "message": "Division is already configured"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "CMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCFG0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WCFG0002` | missing required field: {target_type} or {cycle_closing_time} |
| 400 | `WCFG0010` | Invalid target type |
| 400 | `WCFG0011` | Invalid target ID |
| 404 | `WCFG0003` | Division not found |
| 404 | `WCFG0006` | Program not found |
| 404 | `WCFG0007` | Organization not found |
| 409 | `WCFG0004` | Division is already configured |
| 500 | `CMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-history-config-creation-1` | https://developers.pismo.io/events/docs/account-balances-balance-history-config-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId} operationId=get-account-balance-history-config-by-id-v2 -->
### `GET /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` — Get account balance history config by ID v2

- **operationId:** `get-account-balance-history-config-by-id-v2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the current account balance history configuration by ID.
>
> Also returns previous configurations if you pass the query parameter `showPrevious` set to `true`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `balanceHistoryConfigId` | path | yes | string | Balance history configuration ID | format: "uuid"; maxLength: 52; example: "ee665f37-340f-461e-b520-af3b1b61c6ee" |
| `showPrevious` | query | no | boolean | Should the previous account balances history by division code be returned? \\<br>If `true`, returns the previous account balances history configuration by division code. Default is `false`.\\<br>For example, if you use [Update account balance history config](ref:patch-account-balances-history-configv2) to update an existing balance history configuration, specifying `true` in this field returns both the current balance history configuration and the previous ones.\\<br>There is no limit to how many previous balance history configurations can be returned.<br> | default: false; example: true |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetAccountBalanceHistoryConfigurationResponseV2`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `BalanceHistoryConfigID`) | yes | Balance history configuration ID | format: "uuid"; example: "550e8400-e29b-41d4-a716-446655440000" |
| `target_type` | string (schema `BalanceHistoryTargetType`) | yes | The target type of the balance history configuration, based on the hierarchical level it applies to. | enum: ["ORGANIZATION", "PROGRAM", "DIVISION"]; example: "ORGANIZATION" |
| `target_id` | string (schema `BalanceHistoryTargetID`) | yes | Target ID (`org_id`, `program_id`, or `division_id`) | minLength: 1; maxLength: 52; example: "my-org-123" |
| `cycle_closing_time` | string (schema `CycleClosingTimeV2`) | yes | Cycle closing time indicates what time of day the cycle closes for a division, organization, or program. This time uses the timezone configured for the corresponding division, organization, or program. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "23:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | yes | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |
| `cycle_config_validity` | object (schema `CycleConfigValidity`) | yes | The start and end date/time indicating when the cycle configuration becomes valid or invalid.<br> |  |

200 Example `Example transaction`:

```json
{
  "id": "ee665f37-340f-461e-b520-af3b1b61c6ee",
  "target_type": "PROGRAM",
  "target_id": "42461",
  "cycle_closing_time": "22:00:00",
  "cycle_event_delay": 10,
  "cycle_config_validity": {
    "start": "2023-05-01T22:10:00Z"
  }
}
```

##### Response 400

400 Example `division_code parameter required`:

```json
{
  "code": "WCFG0002",
  "message": "divisionCode is a required parameter"
}
```

400 Example `cycle_closing_time exceed size`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time must be a maximum of 8 characters in length"
}
```

400 Example `cycle_closing_time invalid time format`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time has an invalid time format: {cycle_closing_time}"
}
```

400 Example `cycle_event_delay must be 5 minutes or greater`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_event_delay must be 5 or greater"
}
```

400 Example `cycle_event_delay exceed maximum minutes`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_event_delay must be 1,439 or less"
}
```

400 Example `cycle_closing_time or cycle_event_delay must be provided`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time or cycle_event_delay must be provided"
}
```

400 Example `Missing required parameter`:

```json
{
  "code": "WCFG0002",
  "message": "Missing required parameter {id}"
}
```

400 Example `Pagination limit exceeded`:

```json
{
  "code": "WCFG0002",
  "message": "Pagination must be limited to 20"
}
```

##### Response 404

404 Example `Division not found`:

```json
{
  "code": "WCFG0003",
  "message": "Division [divisionCode] not found"
}
```

404 Example `Account balance history config not found`:

```json
{
  "code": "WCFG0005",
  "message": "Account balance history config not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "CMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCFG0002` | divisionCode is a required parameter |
| 404 | `WCFG0003` | Division [divisionCode] not found |
| 404 | `WCFG0005` | Account balance history config not found |
| 500 | `CMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId} operationId=patch-account-balances-history-configv2 -->
### `PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}` — Update account balance history config v2

- **operationId:** `patch-account-balances-history-configv2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the account balance history configuration.
>
> When you call this endpoint after `cycle_config_validity.start`, the new configuration is valid only after the two-cycle closing date.
> Example:
>   - division timezone: UTC
>   - Update account balance history configuration called at: `2023-05-01T18:00:00Z`
>   - current cycle closing time: 22:00:00
>   - current cycle closing date: 2023-04-30 (from `2023-04-30T22:00:00Z` to `2023-05-01T22:00:00Z`)
>   - cycle config validity start datetime of the new config: `2023-05-02T22:00:00Z`
>   - current config stays valid until `2023-05-02T22:00:00Z`
>
> If this endpoint is called when the current datetime is less than or equal to `cycle_config_validity.start` of the most recent configuration, the new configuration overrides the the most recent configuration.
> Example:
>   - division timezone: UTC
>   - Update account balance history configuration called at: `2023-05-01T19:00:00Z`
>   - Cycle config validity start datetime of the most recent configuration: `2023-05-02T22:00:00Z`
>   - New config overrides the most recent configuration settings, keeping the same cycle config validity start date: `2023-05-01T22:00:00Z`
>
> This endpoint generates an [Account balance history configuration changed](https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `balanceHistoryConfigId` | path | yes | string | Balance history configuration ID | format: "uuid"; maxLength: 52; example: "ee665f37-340f-461e-b520-af3b1b61c6ee" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateAccountBalanceHistoryConfigurationRequestV2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cycle_closing_time` | string (schema `CycleClosingTimeV2`) | no | Cycle closing time indicates what time of day the cycle closes for a division, organization, or program. This time uses the timezone configured for the corresponding division, organization, or program. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "23:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | no | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |

Example `Update account balances history config response`:

```json
{
  "cycle_closing_time": "22:01:00",
  "cycle_event_delay": 30
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Invalid JSON payload received`:

```json
{
  "code": "WCFG0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `Missing required parameter`:

```json
{
  "code": "WCFG0002",
  "message": "Missing required parameter {id}"
}
```

400 Example `Missing cycle_closing_time and cycle_event_delay`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time or cycle_event_delay must be provided"
}
```

400 Example `Validation error`:

```json
{
  "code": "WCFG0002",
  "message": "validation error: {message}"
}
```

400 Example `Invalid target type`:

```json
{
  "code": "WCFG0010",
  "message": "Invalid target type"
}
```

400 Example `Invalid target ID`:

```json
{
  "code": "WCFG0011",
  "message": "Invalid target ID"
}
```

##### Response 404

404 Example `Division not found`:

```json
{
  "code": "WCFG0003",
  "message": "Division not found"
}
```

404 Example `Account balance history config not found`:

```json
{
  "code": "WCFG0005",
  "message": "Account balance history config not found"
}
```

404 Example `Program not found`:

```json
{
  "code": "WCFG0006",
  "message": "Program not found"
}
```

404 Example `Organization not found`:

```json
{
  "code": "WCFG0007",
  "message": "Organization not found"
}
```

##### Response 500

500 Example `Generic internal error`:

```json
{
  "code": "CMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCFG0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WCFG0002` | Missing required parameter {id} |
| 400 | `WCFG0010` | Invalid target type |
| 400 | `WCFG0011` | Invalid target ID |
| 404 | `WCFG0003` | Division not found |
| 404 | `WCFG0005` | Account balance history config not found |
| 404 | `WCFG0006` | Program not found |
| 404 | `WCFG0007` | Organization not found |
| 500 | `CMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-history-config-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/bank-statements/v2/account-balances/history/config/{targetType}/{targetId} operationId=get-account-balance-history-config-by-target-v2 -->
### `GET /bank-statements/v2/account-balances/history/config/{targetType}/{targetId}` — Get account balance history config by target type v2

- **operationId:** `get-account-balance-history-config-by-target-v2`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the latest valid account balance history configuration for a specific target (organization, program, or division).

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `targetType` | path | yes | string | Target type of the balance history configuration | enum: ["ORGANIZATION", "PROGRAM", "DIVISION"]; example: "ORGANIZATION" |
| `targetId` | path | yes | string | Target ID (either `org_id`, `program_id`, or `division_id`). When `targetType` is `DIVISION`, the division code is also accepted. | minLength: 1; maxLength: 52; example: "my-org-123" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `BalanceHistoryConfigItemV2`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | string (schema `BalanceHistoryConfigID`) | yes | Balance history configuration ID | format: "uuid"; example: "550e8400-e29b-41d4-a716-446655440000" |
| `target_type` | string (schema `BalanceHistoryTargetType`) | yes | The target type of the balance history configuration, based on the hierarchical level it applies to. | enum: ["ORGANIZATION", "PROGRAM", "DIVISION"]; example: "ORGANIZATION" |
| `target_id` | string (schema `BalanceHistoryTargetID`) | yes | Target ID (`org_id`, `program_id`, or `division_id`) | minLength: 1; maxLength: 52; example: "my-org-123" |
| `cycle_closing_time` | string (schema `CycleClosingTimeV2`) | yes | Cycle closing time indicates what time of day the cycle closes for a division, organization, or program. This time uses the timezone configured for the corresponding division, organization, or program. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "23:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | yes | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |
| `cycle_config_validity` | object (schema `CycleConfigValidity`) | yes | The start and end date/time indicating when the cycle configuration becomes valid or invalid.<br> |  |

200 Example `Get config for Organization`:

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "target_type": "ORGANIZATION",
  "target_id": "my-org",
  "cycle_closing_time": "23:59:59",
  "cycle_event_delay": 60,
  "cycle_config_validity": {
    "start": "2023-05-01T22:10:00Z"
  }
}
```

200 Example `Get config for Program`:

```json
{
  "id": "660e8400-e29b-41d4-a716-446655440001",
  "target_type": "PROGRAM",
  "target_id": "100",
  "cycle_closing_time": "22:00:00",
  "cycle_event_delay": 30,
  "cycle_config_validity": {
    "start": "2023-04-01T22:10:00Z"
  }
}
```

##### Response 400

400 Example `Invalid attribute`:

```json
{
  "code": "WCFG0002",
  "message": "Invalid attribute: targetType or targetID is empty"
}
```

400 Example `Invalid target type`:

```json
{
  "code": "WCFG0010",
  "message": "Invalid target type: must be ORGANIZATION, PROGRAM, or DIVISION"
}
```

##### Response 404

404 Example `Config not found`:

```json
{
  "code": "WCFG0005",
  "message": "Config not found"
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
| 400 | `WCFG0002` | Invalid attribute: targetType or targetID is empty |
| 400 | `WCFG0010` | Invalid target type: must be ORGANIZATION, PROGRAM, or DIVISION |
| 404 | `WCFG0005` | Config not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/OffsetPagination -->
### Schema `OffsetPagination`

Pointer: `#/components/schemas/OffsetPagination`. Type: object (schema `OffsetPagination`).

> Data related to list pagination using an offset parameter

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean (schema `HasNext`) | no | Whether there are more pages after the current page (`true`) or not (`false`). | example: true |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `offset` | integer (schema `Offset`) | no | Starting index of the result list. Default is 0. | format: "int32"; example: 10 |

<!-- schema: #/components/schemas/CycleConfigValidity -->
### Schema `CycleConfigValidity`

Pointer: `#/components/schemas/CycleConfigValidity`. Type: object (schema `CycleConfigValidity`).

> The start and end date/time indicating when the cycle configuration becomes valid or invalid.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `start` | string | no | The date and time when the configuration becomes valid. Format = `yyyy-mm-dd:hr:mm:ss`. | format: "date-time"; example: "2023-04-01T22:10:00Z" |
| `end` | string | no | The date and time when the configuration ends. Format = `yyyy-mm-dd:hr:mm:ss`. | format: "date-time"; example: "2023-05-01T22:10:00Z" |

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ErrorCode`) | no | Error code<br>`minLength: 1`<br>`maxLength: 12`<br> | minLength: 1; maxLength: 12; example: "WPMT0017" |
| `message` | string (schema `ErrorMessage`) | no | Error message<br>`minLength: 1`<br>`maxLength: 1000`<br> | minLength: 1; maxLength: 1000; example: "Invalid JSON payload received: Error unmarshalling request" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Bank statements`: GET /bank-statements/v2/account-balances/history/config, POST /bank-statements/v2/account-balances/history/config, GET /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}, PATCH /bank-statements/v2/account-balances/history/config/{balanceHistoryConfigId}, GET /bank-statements/v2/account-balances/history/config/{targetType}/{targetId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-account` — Event catalogue: account
