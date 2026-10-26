---
ku_id: KU-API-banking-transaction-banking--bank-statements-part-01
title: 'API reference: Banking - Transaction banking — Bank statements (part 1 of 2)'
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
- post-account-balance-history-configuration
- get-account-balance-history-configuration
- patch-account-balances-history-configuration
- get-account-balances
- get-account-balance-history
related_kus:
- KU-BANK-account-balance-definitions-for-transaction-banking
- KU-BANK-bank-statements-1
- KU-BANK-dated-transactions
- KU-BANK-get-started-transaction-banking
- KU-BANK-penalties-for-cd-accounts
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-EVT-catalogue-account
- KU-EVT-corporate-banking-data-events
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Bank statements (part 1 of 2)

**KU ID:** `KU-API-banking-transaction-banking--bank-statements-part-01` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Bank statements` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Bank statements endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `POST /bank-statements/v1/account-balances/history/config` | `post-account-balance-history-configuration` | Create account balance history config v1 | no |
| `GET /bank-statements/v1/account-balances/history/config/{divisionCode}` | `get-account-balance-history-configuration` | Get account balance history config v1 | no |
| `PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}` | `patch-account-balances-history-configuration` | Update account balance history config v1 | no |
| `GET /bank-statements/v1/account-balances/{externalAccountId}` | `get-account-balances` | Get transaction banking account balance | no |
| `GET /bank-statements/v1/account-balances/{externalAccountId}/history` | `get-account-balance-history` | Get transaction banking account balance history | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/bank-statements/v1/account-balances/history/config operationId=post-account-balance-history-configuration -->
### `POST /bank-statements/v1/account-balances/history/config` — Create account balance history config v1

- **operationId:** `post-account-balance-history-configuration`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an account balance history configuration by division code.
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

**Content type `application/json`** — schema: object (schema `CreateAccountBalanceHistoryConfigurationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `division_code` | string (schema `DivisionCode2`) | yes | Division code registered in the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint. | maxLength: 36; example: "US" |
| `cycle_closing_time` | string (schema `CycleClosingTime`) | yes | Time of day the cycle closes for a division. This time follows the timezone configured in division. You can find the division timezone using the [Get division by code](ref:get-division-by-code-v2) endpoint. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "22:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | yes | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |

Example `Create account balance history configuration`:

```json
{
  "division_code": "my-division",
  "cycle_closing_time": "22:00:00",
  "cycle_event_delay": 15
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `CreateAccountBalanceHistoryConfigurationResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cycle_closing_time` | string (schema `CycleClosingTime`) | no | Time of day the cycle closes for a division. This time follows the timezone configured in division. You can find the division timezone using the [Get division by code](ref:get-division-by-code-v2) endpoint. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "22:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | no | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |
| `cycle_config_validity` | object (schema `CycleConfigValidity`) | no | The start and end date/time indicating when the cycle configuration becomes valid or invalid.<br> |  |

201 Example `Created account balance history configuration successfully`:

```json
{
  "cycle_closing_time": "22:00:00",
  "cycle_event_delay": 10,
  "cycle_config_validity": {
    "start": "2023-05-01T22:10:00Z"
  }
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
  "code": "ECMN9999",
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
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-history-config-creation-1` | https://developers.pismo.io/events/docs/account-balances-balance-history-config-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;404;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-bank-statements-1`, `KU-BANK-dated-transactions`, `KU-BANK-get-started-transaction-banking`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/bank-statements/v1/account-balances/history/config/{divisionCode} operationId=get-account-balance-history-configuration -->
### `GET /bank-statements/v1/account-balances/history/config/{divisionCode}` — Get account balance history config v1

- **operationId:** `get-account-balance-history-configuration`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the current account balance history configuration by division code.
>
> Also returns previous configurations if you pass the query parameter `showPrevious` set to `true`.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `divisionCode` | path | yes | string | Division code registered in the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint. | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 36; example: "my-division-code" |
| `showPrevious` | query | no | boolean | Should the previous account balances history by division code be returned? \\<br>If `true`, returns the previous account balances history configuration by division code. Default is `false`.\\<br>For example, if you use [Update account balance history config](ref:patch-account-balances-history-configv2) to update an existing balance history configuration, specifying `true` in this field returns both the current balance history configuration and the previous ones.\\<br>There is no limit to how many previous balance history configurations can be returned.<br> | default: false; example: true |
| `offset` | query | no | integer | Starting point for the results list. Default is `0` | default: 0; format: "int32"; minimum: 0; example: 1 |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `10` | default: 10; format: "int32"; maximum: 20; example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `GetAccountBalanceHistoryConfigurationResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cycle_closing_time` | string (schema `CycleClosingTime`) | no | Time of day the cycle closes for a division. This time follows the timezone configured in division. You can find the division timezone using the [Get division by code](ref:get-division-by-code-v2) endpoint. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "22:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | no | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |
| `cycle_config_validity` | object (schema `CycleConfigValidity`) | no | The start and end date/time indicating when the cycle configuration becomes valid or invalid.<br> |  |
| `previous` | array of object (schema `PreviousAccountBalanceHistoryConfig`) | no | List of previous configurations of the division account balance history. |  |

200 Example `Example transaction`:

```json
{
  "cycle_closing_time": "22:00:00",
  "cycle_event_delay": 10,
  "cycle_config_validity": {
    "start": "2023-05-01T22:10:00Z"
  },
  "previous": [
    {
      "cycle_closing_time": "23:00:00",
      "cycle_event_delay": 15,
      "cycle_config_validity": {
        "start": "2023-04-01T22:10:00Z",
        "end": "2023-05-01T22:10:00Z"
      }
    }
  ],
  "previous_pagination": {
    "has_next": true,
    "limit": 2,
    "offset": 16
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
  "code": "ECMN9999",
  "message": "Internal error"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WCFG0002` | divisionCode is a required parameter |
| 404 | `WCFG0003` | Division [divisionCode] not found |
| 404 | `WCFG0005` | Account balance history config not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-bank-statements-1`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/bank-statements/v1/account-balances/history/config/{divisionCode} operationId=patch-account-balances-history-configuration -->
### `PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}` — Update account balance history config v1

- **operationId:** `patch-account-balances-history-configuration`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update the account balance history configuration for a division code.
>
> If this endpoint is called when the current datetime is greater than `cycle_config_validity.start`, the new configuration is valid only after the two-cycle closing date.
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
| `divisionCode` | path | yes | string | Division code registered in the [Create division](https://developers.pismo.io/pismo-docs/reference/post-division-v2) endpoint. | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 36; example: "my-division-code" |

#### Request body

Required: yes

> Request body

**Content type `application/json`** — schema: object (schema `UpdateAccountBalanceHistoryConfigurationRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cycle_closing_time` | string (schema `CycleClosingTime`) | no | Time of day the cycle closes for a division. This time follows the timezone configured in division. You can find the division timezone using the [Get division by code](ref:get-division-by-code-v2) endpoint. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "22:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | no | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |

Example `Update account balances history configuration`:

```json
{
  "cycle_closing_time": "22:00:00",
  "cycle_event_delay": 15
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

400 Example `Parameters must be provided`:

```json
{
  "code": "WCFG0002",
  "message": "cycle_closing_time or cycle_event_delay params must be provided"
}
```

400 Example `Invalid JSON payload received`:

```json
{
  "code": "WCFG0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
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
| 400 | `WCFG0002` | cycle_closing_time or cycle_event_delay params must be provided |
| 400 | `WCFG0001` | Invalid JSON payload received: Error unmarshalling request |
| 404 | `WCFG0003` | Division not found |
| 404 | `WCFG0005` | Account balance history config not found |
| 500 | `ECMN9999` | Internal error |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-balances-balance-history-config-change-1` | https://developers.pismo.io/events/docs/account-balances-balance-history-config-change-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-bank-statements-1`, `KU-BANK-dated-transactions`, `KU-EVT-corporate-banking-data-events`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/bank-statements/v1/account-balances/{externalAccountId} operationId=get-account-balances -->
### `GET /bank-statements/v1/account-balances/{externalAccountId}` — Get transaction banking account balance

- **operationId:** `get-account-balances`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get balances associated with a specific account. These balances include available, credit, debit balance, and so on.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountBalanceResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 403 | Forbidden | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `future_dated_credits_balance` | number (schema `FutureDatedCreditsBalance`) | yes | Represents the account balance scheduled to be settled on a future date, after the original posting date. The account's `book_balance` is credited when the settlement occurs.<br><br>The `future_dated_credits_balance` increases when future-dated credits are posted using the [Post payment](ref:corporate-v2-post-payments) endpoint, and decreases when those payments are settled or canceled. This balance is always a positive value.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `future_dated_debits_balance` | number (schema `FutureDatedDebitsBalance`) | yes | Represents the account balance scheduled to be settled on a future date, after the initial posting date. The account’s `book_balance` is debited when the settlement occurs.<br><br>The `future_dated_debits_balance` increases when future-dated debits are posted using the [Post payment](ref:corporate-v2-post-payments) endpoint, and decreases when these payments are settled or canceled. This balance is always a positive value.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1234 |
| `external_account_id` | string (schema `ExternalAccountID`) | no | Custom account ID. Used as the key for all operations (manage accounts, transactions, etc.) on the corporate layer.<br><br>This field is:<br>- Unique within the Organization<br>- Immutable: The field cannot be updated.<br>- Not recyclable: You can't reuse an external account ID, even if the account that was using it has been canceled.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `program_id` | integer (schema `ProgramID3`) | no | Program ID. This is a client-provided ID. | format: "int64"; example: 2222 |
| `currency_numeric_code` | string (schema `AccountNumericCurrencyCode`) | no | Account numeric currency code in ISO 4217 format. If not specified, it's inherited from the program.<br> | minLength: 3; maxLength: 3; example: "840" |
| `currency_alphabetic_code` | string (schema `AccountAlphabeticCurrencyCode`) | no | Account alphabetic currency code in ISO 4217 format. If not specified, it's inherited from the program.<br> | minLength: 3; maxLength: 3; example: "USD" |
| `future_dated_credits_balance` | number (schema `FutureDatedCreditsBalance`) | yes | Represents the account balance scheduled to be settled on a future date, after the original posting date. The account's `book_balance` is credited when the settlement occurs.<br><br>The `future_dated_credits_balance` increases when future-dated credits are posted using the [Post payment](ref:corporate-v2-post-payments) endpoint, and decreases when those payments are settled or canceled. This balance is always a positive value.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `future_dated_debits_balance` | number (schema `FutureDatedDebitsBalance`) | yes | Represents the account balance scheduled to be settled on a future date, after the initial posting date. The account’s `book_balance` is debited when the settlement occurs.<br><br>The `future_dated_debits_balance` increases when future-dated debits are posted using the [Post payment](ref:corporate-v2-post-payments) endpoint, and decreases when these payments are settled or canceled. This balance is always a positive value.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `ledger_balance` | number (schema `LedgerBalance`) | no | Ledger balance.<br><br>Ledger balance is calculated as `book_balance` + `uncleared_funds`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 270.35 |
| `book_balance` | number (schema `BookBalance`) | no | Book balance.<br><br>Book balance is calculated as `credit_balance` - `debit_balance` + `earmarked_balance`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 146.9 |
| `available_balance` | number (schema `AvailableBalance`) | no | Available balance.<br><br>Available balance is calculated as `credit_balance` - `debit_balance` + `overdraft_limit`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 123.45 |
| `credit_balance` | number (schema `CreditBalance`) | no | Credit balance | format: "float"; example: 123.45 |
| `debit_balance` | number (schema `DebitBalance`) | no | Debit balance | format: "float"; example: 123.45 |
| `uncleared_funds` | number (schema `UnclearedFunds`) | no | Uncleared funds amount<br><br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 123.45 |
| `uncleared_checks_balance` | number (schema `UnclearedChecksBalance`) | no | The total value of checks that have been posted to the account but have not yet cleared.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000 |
| `restricted_funds` | number (schema `RestrictedFundsBalance`) | no | The portion of an account balance held under regulatory or operational restrictions and not available for transactions.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `legal_holds` | number (schema `LegalHoldsBalance`) | no | The portion of an account balance held under legal holds (such as court-ordered restrictions) and unavailable for transactions.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `earmarked_balance` | number (schema `EarmarkBalance`) | no | Earmark balance. Initially equal to the earmarked amount and decreases as the reserved funds are used up or decreased in a decrease operation. It can also increase if an increase operation is performed.<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `overdraft_limit` | number (schema `OverdraftLimit`) | no | Account overdraft limit<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `value_dated_balance` | number (schema `ValueDatedBalance`) | no | The value dated balance results from recalculating credit or debit balance based on the back value date. Defaults to the book balance.<br><br>The value dated balance is included in the following events:<br>- [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)<br>- [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1)<br> | format: "float"; example: 123.45 |
| `held_funds` | number (schema `HeldFunds`) | no | Funds that are temporarily restricted due to regulatory or operational requirements, unavailable for transactions, and representing the total amount of earmarked or otherwise restricted balances.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `held_checks_balance` | number (schema `HeldChecksBalance`) | no | The balance from checks that the bank considers available but holds to earn interest. It increases when check holds are applied and decreases when those holds are released or canceled.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `remunerative_interest_accrued` | number (schema `RemunerativeInterestAccrued`) | no | This balance reflects the total interest pending capitalization. It increases as interest accrues and decreases when the accrued interest is added to the principal balance.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |

200 Example `Example account balance`:

```json
{
  "future_dated_credits_balance": 0,
  "future_dated_debits_balance": 0,
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "currency_numeric_code": "840",
  "currency_alphabetic_code": "USD",
  "program_id": 8674,
  "ledger_balance": 110,
  "book_balance": 70,
  "available_balance": 50,
  "credit_balance": 50,
  "debit_balance": 0,
  "uncleared_funds": 40,
  "uncleared_checks_balance": 0,
  "earmarked_balance": 20,
  "overdraft_limit": 0,
  "value_dated_balance": 70,
  "held_funds": 20.55,
  "held_checks_balance": 20.55,
  "restricted_funds": 0,
  "legal_holds": 0,
  "remunerative_interest_accrued": 1.23
}
```

##### Response 400

400 Example `external_account_id validation error`:

```json
{
  "code": "CMN0002",
  "message": "external_account_id must be a maximum of 60 characters in length"
}
```

400 Example `invalid header account`:

```json
{
  "code": "WABL0003",
  "message": "Invalid header account"
}
```

##### Response 401

401 Example `Account not authorized`:

```json
{
  "code": "WABL0002",
  "message": "Account not authorized"
}
```

##### Response 403

403 Example `Forbidden request`:

```json
{
  "message": "access denied"
}
```

##### Response 404

404 Example `Transaction not found`:

```json
{
  "code": "WABL0001",
  "message": "Account balance not found"
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

500 Example `Account balance unknown`:

```json
{
  "code": "EABL0001",
  "message": "Account balance unknown"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `CMN0002` | external_account_id must be a maximum of 60 characters in length |
| 400 | `WABL0003` | Invalid header account |
| 401 | `WABL0002` | Account not authorized |
| 404 | `WABL0001` | Account balance not found |
| 500 | `CMN9999` | Internal error |
| 500 | `EABL0001` | Account balance unknown |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-account-balance-definitions-for-transaction-banking`, `KU-BANK-penalties-for-cd-accounts`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/bank-statements/v1/account-balances/{externalAccountId}/history operationId=get-account-balance-history -->
### `GET /bank-statements/v1/account-balances/{externalAccountId}/history` — Get transaction banking account balance history

- **operationId:** `get-account-balance-history`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Bank statements`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get the balance history for a transaction banking account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `externalAccountId` | path | yes | string | External account ID | minLength: 1; maxLength: 60; example: "12345678901" |
| `startDate` | query | no | string | Starting date of the desired date range for the account balance history. If not provided, it defaults to one month prior to the end date. The total date range cannot exceed three years. | format: "date"; example: "2023-04-03" |
| `endDate` | query | no | string | Ending date of the desired date range for the account balance history. If not provided, it defaults to the current date. The total date range cannot exceed three years. | format: "date"; example: "2023-05-03" |
| `cursor` | query | no | string | Cursor to the next page of results. If no value is specified, it fetches the first page. | example: "1234" |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `100`. Maximum is `500` | default: 100; format: "int32"; maximum: 500; example: 500 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountBalanceHistoryResponse`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Unauthorized | `application/json`: object (schema `ErrorResponse`) |
| 403 | Forbidden | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `account_id` | integer (schema `AccountID`) | no | Account ID | format: "int64"; example: 1234 |
| `external_account_id` | string (schema `ExternalAccountID`) | no | Custom account ID. Used as the key for all operations (manage accounts, transactions, etc.) on the corporate layer.<br><br>This field is:<br>- Unique within the Organization<br>- Immutable: The field cannot be updated.<br>- Not recyclable: You can't reuse an external account ID, even if the account that was using it has been canceled.<br> | pattern: "^[a-zA-Z0-9-]+$"; maxLength: 60; example: "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab" |
| `currency_numeric_code` | string (schema `AccountNumericCurrencyCode`) | no | Account numeric currency code in ISO 4217 format. If not specified, it's inherited from the program.<br> | minLength: 3; maxLength: 3; example: "840" |
| `currency_alphabetic_code` | string (schema `AccountAlphabeticCurrencyCode`) | no | Account alphabetic currency code in ISO 4217 format. If not specified, it's inherited from the program.<br> | minLength: 3; maxLength: 3; example: "USD" |
| `balance_history` | array of object | no |  |  |
| `balance_history[].future_dated_credits_balance` | number (schema `FutureDatedCreditsBalance`) | yes | Represents the account balance scheduled to be settled on a future date, after the original posting date. The account's `book_balance` is credited when the settlement occurs.<br><br>The `future_dated_credits_balance` increases when future-dated credits are posted using the [Post payment](ref:corporate-v2-post-payments) endpoint, and decreases when those payments are settled or canceled. This balance is always a positive value.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `balance_history[].future_dated_debits_balance` | number (schema `FutureDatedDebitsBalance`) | yes | Represents the account balance scheduled to be settled on a future date, after the initial posting date. The account’s `book_balance` is debited when the settlement occurs.<br><br>The `future_dated_debits_balance` increases when future-dated debits are posted using the [Post payment](ref:corporate-v2-post-payments) endpoint, and decreases when these payments are settled or canceled. This balance is always a positive value.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `balance_history[].ledger_balance` | number (schema `LedgerBalance`) | no | Ledger balance.<br><br>Ledger balance is calculated as `book_balance` + `uncleared_funds`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 270.35 |
| `balance_history[].book_balance` | number (schema `BookBalance`) | no | Book balance.<br><br>Book balance is calculated as `credit_balance` - `debit_balance` + `earmarked_balance`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 146.9 |
| `balance_history[].available_balance` | number (schema `AvailableBalance`) | no | Available balance.<br><br>Available balance is calculated as `credit_balance` - `debit_balance` + `overdraft_limit`.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 123.45 |
| `balance_history[].credit_balance` | number (schema `CreditBalance`) | no | Credit balance | format: "float"; example: 123.45 |
| `balance_history[].debit_balance` | number (schema `DebitBalance`) | no | Debit balance | format: "float"; example: 123.45 |
| `balance_history[].uncleared_funds` | number (schema `UnclearedFunds`) | no | Uncleared funds amount<br><br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000; example: 123.45 |
| `balance_history[].uncleared_checks_balance` | number (schema `UnclearedChecksBalance`) | no | The total value of checks that have been posted to the account but have not yet cleared.<br>`minimum: -9223372036854775807`<br>`maximum: 9223372036854775807`<br> | format: "float"; minimum: -9223372036854776000; maximum: 9223372036854776000 |
| `balance_history[].restricted_funds` | number (schema `RestrictedFundsBalance`) | no | The portion of an account balance held under regulatory or operational restrictions and not available for transactions.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `balance_history[].legal_holds` | number (schema `LegalHoldsBalance`) | no | The portion of an account balance held under legal holds (such as court-ordered restrictions) and unavailable for transactions.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `balance_history[].earmarked_balance` | number (schema `EarmarkBalance`) | no | Earmark balance. Initially equal to the earmarked amount and decreases as the reserved funds are used up or decreased in a decrease operation. It can also increase if an increase operation is performed.<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `balance_history[].overdraft_limit` | number (schema `OverdraftLimit`) | no | Account overdraft limit<br><br>`minimum: 0`<br>`maximum: 18446744073709551617`<br> | format: "float"; minimum: 0; maximum: 18446744073709552000; example: 123.45 |
| `balance_history[].value_dated_balance` | number (schema `ValueDatedBalance`) | no | The value dated balance results from recalculating credit or debit balance based on the back value date. Defaults to the book balance.<br><br>The value dated balance is included in the following events:<br>- [Account balance changed](https://developers.pismo.io/events/docs/account-balances-balance-change-1)<br>- [Account balance history generated](https://developers.pismo.io/events/docs/account-balances-balance-history-1)<br> | format: "float"; example: 123.45 |
| `balance_history[].held_funds` | number (schema `HeldFunds`) | no | Funds that are temporarily restricted due to regulatory or operational requirements, unavailable for transactions, and representing the total amount of earmarked or otherwise restricted balances.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `balance_history[].held_checks_balance` | number (schema `HeldChecksBalance`) | no | The balance from checks that the bank considers available but holds to earn interest. It increases when check holds are applied and decreases when those holds are released or canceled.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `balance_history[].remunerative_interest_accrued` | number (schema `RemunerativeInterestAccrued`) | no | This balance reflects the total interest pending capitalization. It increases as interest accrues and decreases when the accrued interest is added to the principal balance.<br>`minimum`: 0<br>`maximum`: 9223372036854775807<br> | format: "float"; minimum: 0; maximum: 9223372036854776000 |
| `balance_history[].date` | string (schema `CurrentBalanceDate`) | no | Date of current balance. Format = yyyy-mm-dd. | example: "2023-06-22" |
| `balance_history[].business_date` | string (schema `BusinessDate`) | no | Specifying a `business_date` value impacts the account balance history.<br><br><b>Notes</b>:<br>  - The business date is in ISO 8601 format.<br>  - The business date allows users to designate the balance history cycle in which a payment is posted.<br>  - You can specify a `business_date` within the current working day or up to one working day before or after.<br> | format: "date"; example: "2023-03-09" |
| `balance_history[].credit_movement` | number (schema `CreditMovement`) | no | Represents the total of all credits processed during the business day. Always expressed as a positive value.<br><br>`minimum`: `0`<br>`maximum`: `9223372036854775807`<br> | minimum: 0; maximum: 9223372036854776000; example: 70 |
| `balance_history[].debit_movement` | number (schema `DebitMovement`) | no | Represents the total of all debits processed during the business day. Always expressed as a positive value.<br><br>`minimum`: `0`<br>`maximum`: `9223372036854775807`<br> | minimum: 0; maximum: 9223372036854776000; example: 70 |
| `balance_history[].net_movement` | number (schema `NetMovement`) | no | The change in an account’s balance between two consecutive business dates.<br>Calculated as: `net_movement` = `credit_movement` - `debit_movement`.<br><br>`minimum`: `-9223372036854775807`<br>`maximum`: `9223372036854775807`<br> | minimum: -9223372036854776000; maximum: 9223372036854776000; example: 70 |
| `pagination` | object (schema `Pagination`) | no | Data related to list pagination using a cursor. |  |

200 Example `Example account balance`:

```json
{
  "account_id": 1234,
  "external_account_id": "b993ba96-b3e8-4ef7-9cf7-7eee5ddafdab",
  "currency_numeric_code": "840",
  "currency_alphabetic_code": "USD",
  "balance_history": [
    {
      "future_dated_credits_balance": 0,
      "future_dated_debits_balance": 0,
      "credit_movement": 50,
      "debit_movement": 0,
      "net_movement": 50,
      "available_balance": 50,
      "debit_balance": 0,
      "credit_balance": 50,
      "earmarked_balance": 20,
      "ledger_balance": 110,
      "book_balance": 70,
      "uncleared_funds": 40,
      "uncleared_checks_balance": 0,
      "overdraft_limit": 0,
      "value_dated_balance": 70,
      "held_funds": 20.55,
      "held_checks_balance": 20.55,
      "cycle_closing_datetime": "2023-01-21T23:00:00Z",
      "date": "2023-06-22",
      "business_date": "2023-06-22",
      "restricted_funds": 0,
      "legal_holds": 0,
      "remunerative_interest_accrued": 1.23
    }
  ],
  "pagination": {
    "limit": 100,
    "cursor": "MjAyMy0wNC0wMQ=="
  }
}
```

##### Response 400

400 Example `external_account_id validation error`:

```json
{
  "code": "CMN0002",
  "message": "external_account_id must be a maximum of 60 characters in length"
}
```

400 Example `Invalid header account`:

```json
{
  "code": "WHIS0002",
  "message": "Invalid header account"
}
```

400 Example `Invalid date format`:

```json
{
  "code": "WHIS0003",
  "message": "Invalid date format"
}
```

400 Example `Invalid date interval`:

```json
{
  "code": "WHIS0004",
  "message": "Invalid date interval"
}
```

400 Example `Max page limit exceeded`:

```json
{
  "code": "WHIS0006",
  "message": "Max page limit exceeded"
}
```

400 Example `Max date range exceeded`:

```json
{
  "code": "WHIS0007",
  "message": "Max query range exceeded"
}
```

400 Example `Cursor is invalid`:

```json
{
  "code": "WHIS0008",
  "message": "Cursor is invalid"
}
```

##### Response 401

401 Example `Account not authorized`:

```json
{
  "code": "WHIS0001",
  "message": "Account not authorized"
}
```

##### Response 403

403 Example `Forbidden request`:

```json
{
  "message": "access denied"
}
```

##### Response 404

404 Example `Transaction not found`:

```json
{
  "code": "WHIS0005",
  "message": "No account balance history found"
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

500 Example `Account balance unknown`:

```json
{
  "code": "EABL0001",
  "message": "Account balance unknown"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `CMN0002` | external_account_id must be a maximum of 60 characters in length |
| 400 | `WHIS0002` | Invalid header account |
| 400 | `WHIS0003` | Invalid date format |
| 400 | `WHIS0004` | Invalid date interval |
| 400 | `WHIS0006` | Max page limit exceeded |
| 400 | `WHIS0007` | Max query range exceeded |
| 400 | `WHIS0008` | Cursor is invalid |
| 401 | `WHIS0001` | Account not authorized |
| 404 | `WHIS0005` | No account balance history found |
| 500 | `CMN9999` | Internal error |
| 500 | `EABL0001` | Account balance unknown |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-account-balance-definitions-for-transaction-banking`, `KU-BANK-bank-statements-1`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

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

<!-- schema: #/components/schemas/PreviousAccountBalanceHistoryConfig -->
### Schema `PreviousAccountBalanceHistoryConfig`

Pointer: `#/components/schemas/PreviousAccountBalanceHistoryConfig`. Type: object (schema `PreviousAccountBalanceHistoryConfig`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `cycle_closing_time` | string (schema `CycleClosingTime`) | no | Time of day the cycle closes for a division. This time follows the timezone configured in division. You can find the division timezone using the [Get division by code](ref:get-division-by-code-v2) endpoint. | format: "time"; pattern: "^(?:([01]?\\\\d\|2[0-3]):([0-5]?\\\\d):)?([0-5]?\\\\d)$"; maxLength: 8; example: "22:00:00" |
| `cycle_event_delay` | integer (schema `CycleEventDelay`) | no | The cycle event delay specifies how many minutes after `cycle_closing_time` the account balance history event is issued for each account in the division. | format: "int32"; minimum: 5; example: 15 |
| `updated_at` | string (schema `ConfigUpdatedAt`) | no | Date/time the configuration was updated. Format is ISO 8601 (`YYYY-MM-DDThh:mm:ss.ffffffz`). | example: "2025-05-19T12:41:18.373248Z" |
| `cycle_config_validity` | object (schema `CycleConfigValidity`) | no | The start and end date/time indicating when the cycle configuration becomes valid or invalid.<br> |  |

<!-- schema: #/components/schemas/Pagination -->
### Schema `Pagination`

Pointer: `#/components/schemas/Pagination`. Type: object (schema `Pagination`).

> Data related to list pagination using a cursor.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `cursor` | string (schema `Cursor`) | no | Cursor pointing to the next page of results | example: "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0=" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Bank statements`: POST /bank-statements/v1/account-balances/history/config, GET /bank-statements/v1/account-balances/history/config/{divisionCode}, PATCH /bank-statements/v1/account-balances/history/config/{divisionCode}, GET /bank-statements/v1/account-balances/{externalAccountId}, GET /bank-statements/v1/account-balances/{externalAccountId}/history | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-account-balance-definitions-for-transaction-banking` — Account balance definitions for transaction banking
- `KU-BANK-bank-statements-1` — Bank statements
- `KU-BANK-dated-transactions` — Business-dated and value-dated transactions
- `KU-BANK-get-started-transaction-banking` — Get started with transaction banking
- `KU-BANK-penalties-for-cd-accounts` — Penalties and taxes for CD accounts
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-EVT-corporate-banking-data-events` — Banking - Transaction banking
