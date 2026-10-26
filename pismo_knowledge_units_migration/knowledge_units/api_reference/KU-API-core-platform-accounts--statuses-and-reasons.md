---
ku_id: KU-API-core-platform-accounts--statuses-and-reasons
title: 'API reference: Core platform - Accounts — Statuses and reasons'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Accounts.yaml
  sha256: 3c621106abf11d41435170a356ae695e023a5d963bdb0b1e8772209bf0b88c49
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
- v4-get-account-status
- v4-post-account-status
- patch-accounts-v2-accounts-accountId-status
- patch-v2-accounts-accountId-status-rollback
- v4-get-account-reason
- v4-post-account-reason
- get-accounts-v1-account-status
- get-accounts-v1-accounts-status-reasons
related_kus:
- KU-BANK-dormancy
- KU-BANK-managing-account-statuses
- KU-CARD-card-issuing-basics
- KU-CARD-multivalue-program-parameters
- KU-CORE-accounts-overview
- KU-CORE-legal-blocks
- KU-CRED-account-collection-status
- KU-CRED-full-balance-credit-program
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-EVT-accounts-data-events
- KU-EVT-catalogue-account
- KU-PAY-faster-payment-system
- KU-PAY-multi-leg-payments
- KU-PAY-payment-overview-and-instant-payments
specification_version: 1.0.0
---

# API reference: Core platform - Accounts — Statuses and reasons

**KU ID:** `KU-API-core-platform-accounts--statuses-and-reasons` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 8 operation(s) tagged `Statuses and reasons` in `api-specs/Core_platform_-_Accounts.yaml` (“Core platform - Accounts”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to configure accounts, statuses, and reasons.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /accounts/v4/statuses` | `v4-get-account-status` | List statuses | no |
| `POST /accounts/v4/statuses` | `v4-post-account-status` | Create status | no |
| `PATCH /accounts/v2/accounts/{accountId}/status` | `patch-accounts-v2-accounts-accountId-status` | Update status | no |
| `PATCH /accounts/v2/accounts/{accountId}/status/rollback` | `patch-v2-accounts-accountId-status-rollback` | Roll back status | no |
| `GET /accounts/v4/reasons` | `v4-get-account-reason` | List status reasons | no |
| `POST /accounts/v4/reasons` | `v4-post-account-reason` | Create status reason | no |
| `GET /accounts/v1/account-status` | `get-accounts-v1-account-status` | List statuses V1 (deprecated) | **yes** |
| `GET /accounts/v1/accounts-status/reasons` | `get-accounts-v1-accounts-status-reasons` | List status reasons V1 (deprecated) | **yes** |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v4/statuses operationId=v4-get-account-status -->
### `GET /accounts/v4/statuses` — List statuses

- **operationId:** `v4-get-account-status`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statuses and reasons`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account statuses registered for the organization. The org ID is parsed from the access token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `nextCursor` | query | no | string | Cursor value used to get the next page. This is the `next_cursor` value returned in the response. | example: "MEgCQQCo9..." |
| `maxItems` | query | no | integer | Number of items on current page. `200` maximum. Default is `200`. | format: "int32"; minimum: 1; maximum: 200; example: 100 |
| `page` | query | no | integer | Requested page | format: "int32"; minimum: 1; example: 1 |
| `perPage` | query | no | integer | Items per page. | default: 10; format: "int32"; minimum: 1; maximum: 100; example: 100 |
| `name` | query | no | string | Account status name filter.  Pre-defined account statuses include `DEBIT_ONLY`, `NORMAL`, `BLOCKED` and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | pattern: "^[A-Z_]+$"; example: "NORMAL" |
| `state` | query | no | array of string | Filter by `ACTIVE` or `INACTIVE`. Default is `ACTIVE`. | items.enum: ["ACTIVE", "INACTIVE"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `StatusesResponse`) |
| 400 | Bad request | `application/json`: object (schema `MessageResponse`) |
| 500 | Internal server error | `application/json`: object (schema `MessageResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `next_cursor` | string (schema `NextCursor`) | no | Cursor value for the next page | example: "MEgCQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnxS30WAvQCCo2yU1orfgqr41mM70MBAgMBAAE=" |
| `has_next` | boolean (schema `HasNext`) | no | Are there more results (retrieved using the `next_cursor` value)? | example: true |
| `count` | integer (schema `CurrentPageCount`) | no | Number of items on the current page | format: "int32"; example: 100 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page. 100 maximum. | format: "int64"; example: 100 |
| `pages` | integer (schema `NumberOfPages`) | no | Total pages | format: "int32"; example: 100 |
| `total_items` | integer (schema `TotalItems`) | no | Total items | format: "int32"; example: 500 |
| `items` | array of object (schema `StatusResponse`) | no | List of result items |  |

200 Example `Default response`:

```json
{
  "next_cursor": "MEgCQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnxS30WAvQCCo2yU1orfgqr41mM70MBAgMBAAE=",
  "has_next": true,
  "count": 100,
  "current_page": 1,
  "per_page": 100,
  "pages": 1,
  "total_items": 3,
  "items": [
    {
      "status_id": 1,
      "name": "CANCELLED",
      "description": "Cancelled account with no operations available.",
      "state": "ACTIVE",
      "is_final": true,
      "allowed_operations": "NO_OPERATIONS"
    },
    {
      "status_id": 2,
      "name": "NORMAL",
      "description": "Active account with full operations available.",
      "state": "ACTIVE",
      "is_final": false,
      "allowed_operations": "ALL_OPERATIONS"
    },
    {
      "status_id": 3,
      "name": "BLOCKED",
      "description": "Blocked account that can only receive credit operations.",
      "state": "ACTIVE",
      "is_final": false,
      "allowed_operations": "CREDIT_ONLY"
    }
  ]
}
```

##### Response 400

400 Example `Invalid page parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "page",
        "message": "Value must be greater than zero"
      }
    ]
  }
}
```

400 Example `Invalid per page parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "perPage",
        "message": "Value is not a number"
      }
    ]
  }
}
```

400 Example `Invalid state parameter`:

```json
{
  "code": "EACC0018",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "state",
        "message": "Value should be one of: ACTIVE, INACTIVE"
      }
    ]
  }
}
```

400 Example `Invalid next_cursor parameter`:

```json
{
  "code": "WACC0011",
  "message": "Invalid cursor value"
}
```

400 Example `Invalid maxItems parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "maxItems",
        "message": "Value must be greater than zero"
      }
    ]
  }
}
```

##### Response 500

500 Example `Timeout execution`:

```json
{
  "code": "EACC0000",
  "message": "Timeout while executing the request"
}
```

500 Example `Generic message`:

```json
{
  "code": "EACC9999",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EACC0005` | One or more parameters with invalid format |
| 400 | `EACC0018` | One or more parameters with invalid format |
| 400 | `WACC0011` | Invalid cursor value |
| 500 | `EACC0000` | Timeout while executing the request |
| 500 | `EACC9999` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounts-overview`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/accounts/v4/statuses operationId=v4-post-account-status -->
### `POST /accounts/v4/statuses` — Create status

- **operationId:** `v4-post-account-status`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statuses and reasons`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an account status on the platform.
>
> When a new account status is created, its initial `state` (see response) is `ACTIVE`.
>
> This endpoint generates an [Account status created](https://developers.pismo.io/events/docs/account-status-creation-1) event.
>
> Refer to the [Account status](doc:accounts-overview#account-status) guide section for more information.

#### Request body

Required: yes

> Account status details

**Content type `application/json`** — schema: object (schema `StatusCreate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `AccountStatusName2`) | yes | Account status name. Pre-defined account statuses include `DEBIT_ONLY`, `NORMAL`, `BLOCKED` and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | pattern: "^[A-Z_]+$"; maxLength: 200; example: "NORMAL" |
| `allowed_operations` | string (schema `AllowedOperations`) | yes | Allowed operations for this status.<br><br>Possible values:<br>* `ALL_OPERATIONS`&mdash;Both credit and debit operations are allowed.<br>* `CREDIT_ONLY`&mdash;Only credit operations allowed.<br>* `DEBIT_ONLY`&mdash;Only debit operations allowed.<br>* `NO_OPERATIONS`&mdash;Neither account credit nor debit operations allowed.<br> | enum: ["ALL_OPERATIONS", "CREDIT_ONLY", "DEBIT_ONLY", "NO_OPERATIONS"]; example: "ALL_OPERATIONS" |
| `description` | string (schema `AccountStatusDescription`) | no | Account status description | maxLength: 500; example: "Full operational account" |
| `is_final` | boolean (schema `IsFinalStatus`) | no | Is this a final status? An account with a final status cannot have its status updated. Defaults to `false`.<br><br>**Note:** Even if a status is final, it can still be [rolled back](ref:patch-v2-accounts-accountid-status-rollback).<br> | example: false |

Example `Required payload`:

```json
{
  "name": "NORMAL",
  "allowed_operations": "ALL_OPERATIONS"
}
```

Example `Full payload`:

```json
{
  "name": "NORMAL",
  "description": "Active account with all operations available.",
  "is_final": false,
  "allowed_operations": "ALL_OPERATIONS"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `StatusResponse`) |
| 400 | Bad request | `application/json`: object (schema `MessageResponse`) |
| 409 | Conflict | `application/json`: object (schema `MessageResponse`) |
| 500 | Internal server error | `application/json`: object (schema `MessageResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status_id` | integer (schema `AccountStatusID`) | no | Account status ID | format: "int64"; example: 1234567890 |
| `name` | string (schema `AccountStatusName2`) | no | Account status name. Pre-defined account statuses include `DEBIT_ONLY`, `NORMAL`, `BLOCKED` and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | pattern: "^[A-Z_]+$"; maxLength: 200; example: "NORMAL" |
| `description` | string (schema `AccountStatusDescription`) | no | Account status description | maxLength: 500; example: "Full operational account" |
| `state` | string (schema `StatusState`) | no | Status state | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `is_final` | boolean (schema `IsFinalStatus`) | no | Is this a final status? An account with a final status cannot have its status updated. Defaults to `false`.<br><br>**Note:** Even if a status is final, it can still be [rolled back](ref:patch-v2-accounts-accountid-status-rollback).<br> | example: false |
| `allowed_operations` | string (schema `AllowedOperations`) | no | Allowed operations for this status.<br><br>Possible values:<br>* `ALL_OPERATIONS`&mdash;Both credit and debit operations are allowed.<br>* `CREDIT_ONLY`&mdash;Only credit operations allowed.<br>* `DEBIT_ONLY`&mdash;Only debit operations allowed.<br>* `NO_OPERATIONS`&mdash;Neither account credit nor debit operations allowed.<br> | enum: ["ALL_OPERATIONS", "CREDIT_ONLY", "DEBIT_ONLY", "NO_OPERATIONS"]; example: "ALL_OPERATIONS" |

201 Example `Default response`:

```json
{
  "status_id": 2,
  "group": "ALL_OPERATIONS",
  "name": "NORMAL",
  "description": "Active account with all operations available.",
  "state": "ACTIVE",
  "is_final": false
}
```

##### Response 400

400 Example `Invalid payload`:

```json
{
  "code": "EACC0004",
  "message": "Failed during validation of request payload",
  "detail": {
    "payload": [
      {
        "field": "group",
        "message": "Value should be one of: ALL_OPERATIONS, CREDIT_ONLY, DEBIT_ONLY, and NO_OPERATIONS"
      },
      {
        "field": "name",
        "message": "Field is required"
      }
    ]
  }
}
```

##### Response 409

409 Example `Duplicated name`:

```json
{
  "code": "EACC0018",
  "message": "Account status already exists with key(s): 'NORMAL'"
}
```

##### Response 500

500 Example `Timeout execution`:

```json
{
  "code": "EACC0000",
  "message": "Timeout while executing the request"
}
```

500 Example `Invalid payload`:

```json
{
  "code": "EACC0003",
  "message": "Failed to parse request payload"
}
```

500 Example `Generic message`:

```json
{
  "code": "EACC9999",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EACC0004` | Failed during validation of request payload |
| 409 | `EACC0018` | Account status already exists with key(s): 'NORMAL' |
| 500 | `EACC0000` | Timeout while executing the request |
| 500 | `EACC0003` | Failed to parse request payload |
| 500 | `EACC9999` | Something went wrong, please try again later |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-status-creation-1` | https://developers.pismo.io/events/docs/account-status-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounts-overview`, `KU-CRED-account-collection-status`, `KU-CRED-full-balance-credit-program`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PATCH path=/accounts/v2/accounts/{accountId}/status operationId=patch-accounts-v2-accounts-accountId-status -->
### `PATCH /accounts/v2/accounts/{accountId}/status` — Update status

- **operationId:** `patch-accounts-v2-accounts-accountId-status`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statuses and reasons`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update account status.
>
> This endpoint generates an [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2) event.
>
> Refer to the [Account status](doc:accounts-overview#account-status) guide for more information.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |

#### Request body

Required: yes

> Status to update

**Content type `application/json`** — schema: object (schema `UpdateAccountStatusRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string (schema `AccountStatus4`) | yes | Account status. The pre-defined account statuses are `DEBIT_ONLY`, `NORMAL`, `BLOCKED`, and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | pattern: "^[A-Z_]+$"; maxLength: 200; example: "BLOCKED" |
| `reason_id` | integer (schema `StatusReasonID`) | no | ID of the reason why the account is in its current status. You can create reasons with the [Create status reason](ref:v4-post-account-reason) endpoint.<br> | format: "int64"; minimum: 1; example: 123 |
| `description` | string (schema `StatusReasonDescription`) | no | Description of why the account is in its current status | maxLength: 80; example: "Registration restriction" |
| `update_children` | boolean (schema `UpdateChildren`) | no | Should all the account's children linked through the field `parent_account_id` also be updated? Default is `false`. | default: false; example: true |

Example `Account freeze`:

```json
{
  "status": "BLOCKED"
}
```

Example `Reverse account freeze`:

```json
{
  "status": "NORMAL"
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | OK |  |
| 400 | Status not found | `application/json`: object (schema `SimpleError`) |
| 404 | Account not found | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 400

400 Example `Status not found`:

```json
{
  "message": "Status not found"
}
```

##### Response 404

404 Example `Account not found`:

```json
{
  "message": "Account not found"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error changing account status"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-status-change-2` | https://developers.pismo.io/events/docs/account-status-change-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-BANK-managing-account-statuses`, `KU-CARD-card-issuing-basics`, `KU-CORE-accounts-overview`, `KU-CORE-legal-blocks`, `KU-CRED-full-balance-credit-program`, `KU-EVT-accounts-data-events`, `KU-PAY-faster-payment-system`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=PATCH path=/accounts/v2/accounts/{accountId}/status/rollback operationId=patch-v2-accounts-accountId-status-rollback -->
### `PATCH /accounts/v2/accounts/{accountId}/status/rollback` — Roll back status

- **operationId:** `patch-v2-accounts-accountId-status-rollback`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statuses and reasons`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Reset account status to `NORMAL`.
>
> This endpoint generates an [Account status changed](https://developers.pismo.io/events/docs/account-status-change-2) event.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 123 |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `RollbackAccountStatusRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status` | string | no | Status to update. Pre-defined account statuses include `DEBIT_ONLY`, `NORMAL`, `BLOCKED`, and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | example: "NORMAL" |
| `reason_id` | integer (schema `StatusReasonID`) | no | ID of the reason why the account is in its current status. You can create reasons with the [Create status reason](ref:v4-post-account-reason) endpoint.<br> | format: "int64"; minimum: 1; example: 123 |
| `description` | string (schema `RollbackAccountStatusDescription`) | no | Account rollback status description | maxLength: 500; example: "Rollback of account cancellation" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | OK |  |
| 404 | Not found | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 404

404 Example `Account not found`:

```json
{
  "message": "Account or status not found"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Internal server error"
}
```


#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-status-change-2` | https://developers.pismo.io/events/docs/account-status-change-2 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;404;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounts-overview`, `KU-CRED-full-balance-credit-program`, `KU-EVT-accounts-data-events`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v4/reasons operationId=v4-get-account-reason -->
### `GET /accounts/v4/reasons` — List status reasons

- **operationId:** `v4-get-account-reason`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statuses and reasons`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account status reasons for the Organization. The Org ID is parsed from the access token.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `nextCursor` | query | no | string | Cursor value used to get the next page. This is the `next_cursor` value returned in the response. | example: "MEgCQQCo9..." |
| `maxItems` | query | no | integer | Number of items on current page. `200` maximum. Default is `200`. | format: "int32"; minimum: 1; maximum: 200; example: 100 |
| `page` | query | no | integer | Requested page | format: "int32"; minimum: 1; example: 1 |
| `perPage` | query | no | integer | Items per page. | default: 10; format: "int32"; minimum: 1; maximum: 100; example: 100 |
| `name` | query | no | string | Reason name filter | example: "Unblocked" |
| `state` | query | no | array of string | Filter by `ACTIVE` or `INACTIVE`. Default is `ACTIVE`. | items.enum: ["ACTIVE", "INACTIVE"] |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ReasonsResponse`) |
| 400 | Bad request | `application/json`: object (schema `MessageResponse`) |
| 500 | Internal server error | `application/json`: object (schema `MessageResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `next_cursor` | string (schema `NextCursor`) | no | Cursor value for the next page | example: "MEgCQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnxS30WAvQCCo2yU1orfgqr41mM70MBAgMBAAE=" |
| `has_next` | boolean (schema `HasNext`) | no | Are there more results (retrieved using the `next_cursor` value)? | example: true |
| `count` | integer (schema `CurrentPageCount`) | no | Number of items on the current page | format: "int32"; example: 100 |
| `current_page` | integer (schema `CurrentPage`) | no | Current page | format: "int32"; example: 1 |
| `per_page` | integer (schema `PerPage`) | no | Maximum items per page. 100 maximum. | format: "int64"; example: 100 |
| `pages` | integer (schema `NumberOfPages`) | no | Total pages | format: "int32"; example: 100 |
| `total_items` | integer (schema `TotalItems`) | no | Total items | format: "int32"; example: 500 |
| `items` | array of object (schema `ReasonResponse`) | no | List of result items |  |

200 Example `Default response`:

```json
{
  "next_cursor": "MEgCQQCo9+BpMRYQ/dL3DS2CyJxRF+j6ctbT3/Qp84+KeFhnii7NT7fELilKUSnxS30WAvQCCo2yU1orfgqr41mM70MBAgMBAAE=",
  "has_next": true,
  "count": 100,
  "current_page": 1,
  "per_page": 100,
  "pages": 1,
  "total_items": 3,
  "items": [
    {
      "reason_id": 1,
      "name": "Unblocked",
      "description": "Unblocked account after settling the account.",
      "allowed_operations": "ALL_OPERATIONS",
      "state": "ACTIVE"
    },
    {
      "reason_id": 2,
      "name": "Active",
      "description": "Default active reason for an account.",
      "allowed_operations": "CREDIT_ONLY",
      "state": "ACTIVE"
    },
    {
      "reason_id": 3,
      "name": "Judicial block",
      "description": "Blocked account by judicial order.",
      "allowed_operations": "DEBIT_ONLY",
      "state": "ACTIVE"
    }
  ]
}
```

##### Response 400

400 Example `Invalid page parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "page",
        "message": "Value must be greater than zero"
      }
    ]
  }
}
```

400 Example `Invalid per page parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "perPage",
        "message": "Value is not a number"
      }
    ]
  }
}
```

400 Example `Invalid state parameter`:

```json
{
  "code": "EACC0018",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "state",
        "message": "Value should be one of: ACTIVE, INACTIVE"
      }
    ]
  }
}
```

400 Example `Invalid next_cursor parameter`:

```json
{
  "code": "WACC0011",
  "message": "Invalid cursor value"
}
```

400 Example `Invalid maxItems parameter`:

```json
{
  "code": "EACC0005",
  "message": "One or more parameters with invalid format",
  "detail": {
    "parameters": [
      {
        "field": "maxItems",
        "message": "Value must be greater than zero"
      }
    ]
  }
}
```

##### Response 500

500 Example `Timeout execution`:

```json
{
  "code": "EACC0000",
  "message": "Timeout while executing the request"
}
```

500 Example `Generic message`:

```json
{
  "code": "EACC9999",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EACC0005` | One or more parameters with invalid format |
| 400 | `EACC0018` | One or more parameters with invalid format |
| 400 | `WACC0011` | Invalid cursor value |
| 500 | `EACC0000` | Timeout while executing the request |
| 500 | `EACC9999` | Something went wrong, please try again later |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounts-overview`, `KU-PAY-multi-leg-payments`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=POST path=/accounts/v4/reasons operationId=v4-post-account-reason -->
### `POST /accounts/v4/reasons` — Create status reason

- **operationId:** `v4-post-account-reason`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statuses and reasons`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an account status reason on the platform.
>
> This endpoint generates a [Reason created](https://developers.pismo.io/events/docs/account-reason-creation-1) event.
>
> For more information, refer to the [Account status](doc:accounts-overview#account-status) guide section.

#### Request body

Required: yes

> Account reason details

**Content type `application/json`** — schema: object (schema `ReasonCreate`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string (schema `CreateAccountReasonName`) | yes | Reason name | maxLength: 60; example: "Unblocked" |
| `description` | string (schema `CreateAccountReasonDescription`) | no | Reason description | maxLength: 80; example: "Unblocked account after settling the account." |
| `allowed_operations` | string (schema `AllowedOperations`) | no | Allowed operations for this status.<br><br>Possible values:<br>* `ALL_OPERATIONS`&mdash;Both credit and debit operations are allowed.<br>* `CREDIT_ONLY`&mdash;Only credit operations allowed.<br>* `DEBIT_ONLY`&mdash;Only debit operations allowed.<br>* `NO_OPERATIONS`&mdash;Neither account credit nor debit operations allowed.<br> | enum: ["ALL_OPERATIONS", "CREDIT_ONLY", "DEBIT_ONLY", "NO_OPERATIONS"]; example: "ALL_OPERATIONS" |
| `external_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |

Example `Required Payload`:

```json
{
  "name": "Unblocked"
}
```

Example `Full Payload`:

```json
{
  "name": "Unblocked",
  "description": "Unblocked account after settling the account."
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `ReasonResponse`) |
| 400 | Bad request | `application/json`: object (schema `MessageResponse`) |
| 409 | Conflict | `application/json`: object (schema `MessageResponse`) |
| 500 | Internal server error | `application/json`: object (schema `MessageResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason_id` | integer (schema `CreateAccountReasonID`) | no | Reason ID | format: "int64"; example: 1234567890 |
| `name` | string (schema `CreateAccountReasonName`) | no | Reason name | maxLength: 60; example: "Unblocked" |
| `description` | string (schema `CreateAccountReasonDescription`) | no | Reason description | maxLength: 80; example: "Unblocked account after settling the account." |
| `allowed_operations` | string (schema `AllowedOperations`) | no | Allowed operations for this status.<br><br>Possible values:<br>* `ALL_OPERATIONS`&mdash;Both credit and debit operations are allowed.<br>* `CREDIT_ONLY`&mdash;Only credit operations allowed.<br>* `DEBIT_ONLY`&mdash;Only debit operations allowed.<br>* `NO_OPERATIONS`&mdash;Neither account credit nor debit operations allowed.<br> | enum: ["ALL_OPERATIONS", "CREDIT_ONLY", "DEBIT_ONLY", "NO_OPERATIONS"]; example: "ALL_OPERATIONS" |
| `state` | string (schema `ReasonState`) | no | Reason state | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `external_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |

201 Example `Default response`:

```json
{
  "reason_id": 1,
  "name": "Unblocked",
  "description": "Unblocked account after settling the account.",
  "state": "ACTIVE"
}
```

##### Response 400

400 Example `Invalid payload`:

```json
{
  "code": "EACC0004",
  "message": "Failed during validation of request payload",
  "detail": {
    "payload": [
      {
        "field": "name",
        "message": "Field is required"
      }
    ]
  }
}
```

##### Response 409

409 Example `Duplicated name`:

```json
{
  "code": "EACC0018",
  "message": "Account reason already exists with key(s): 'Unblocked'"
}
```

##### Response 500

500 Example `Timeout execution`:

```json
{
  "code": "EACC0000",
  "message": "Timeout while executing the request"
}
```

500 Example `Invalid payload`:

```json
{
  "code": "EACC0003",
  "message": "Failed to parse request payload"
}
```

500 Example `Generic message`:

```json
{
  "code": "EACC9999",
  "message": "Something went wrong, please try again later"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `EACC0004` | Failed during validation of request payload |
| 409 | `EACC0018` | Account reason already exists with key(s): 'Unblocked' |
| 500 | `EACC0000` | Timeout while executing the request |
| 500 | `EACC0003` | Failed to parse request payload |
| 500 | `EACC9999` | Something went wrong, please try again later |

#### Events emitted (api-reference-data/endpoint_event_map.csv)

| Event slug | Event page |
| --- | --- |
| `account-reason-creation-1` | https://developers.pismo.io/events/docs/account-reason-creation-1 |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `1`, deprecated `False`.

Guides that link to this operation: `KU-CARD-multivalue-program-parameters`, `KU-CORE-accounts-overview`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/account-status operationId=get-accounts-v1-account-status -->
### `GET /accounts/v1/account-status` — List statuses V1 (deprecated)

- **operationId:** `get-accounts-v1-account-status`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statuses and reasons`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List account statuses registered for the organization.

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object |
| 404 | Account status not found |  |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Status list`:

```json
[
  {
    "id": 1,
    "name": "ACCOUNT_CANCELLATION",
    "group": "BLOCKED"
  }
]
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error retrieving account status list"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `True`.

<!-- op: spec=api-specs/Core_platform_-_Accounts.yaml method=GET path=/accounts/v1/accounts-status/reasons operationId=get-accounts-v1-accounts-status-reasons -->
### `GET /accounts/v1/accounts-status/reasons` — List status reasons V1 (deprecated)

- **operationId:** `get-accounts-v1-accounts-status-reasons`
- **Specification:** `api-specs/Core_platform_-_Accounts.yaml` (Core platform - Accounts)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Statuses and reasons`
- **Deprecated in specification:** **yes**
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List available reasons for the specific account status, with several filtering options.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `showUser` | query | no | boolean | Filter by "show to user" flag | example: false |
| `accountStatusId` | query | no | integer | Account status ID filter | format: "int64"; minimum: 1; example: 123 |
| `accountStatusName` | query | no | string | Account status name filter. Pre-defined account statuses include `DEBIT_ONLY`, `NORMAL`, `BLOCKED` and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | example: "NORMAL" |
| `description` | query | no | string | Account reason description filter | example: "Restrictions" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object |
| 404 | Not found | `application/json`: object (schema `SimpleError`) |
| 500 | Internal server error | `application/json`: object (schema `SimpleError`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `Reasons list`:

```json
[
  {
    "code": "11",
    "reason_id": 6,
    "description": "Registration restrictions"
  }
]
```

##### Response 404

404 Example `Empty list`:

```json
{
  "message": "No reasons found"
}
```

##### Response 500

500 Example `Internal server error`:

```json
{
  "message": "Error retrieving reasons list"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;500`, has examples `True`, emits events `0`, deprecated `True`.

Guides that link to this operation: `KU-BANK-dormancy`, `KU-BANK-managing-account-statuses`, `KU-PAY-payment-overview-and-instant-payments`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/StatusResponse -->
### Schema `StatusResponse`

Pointer: `#/components/schemas/StatusResponse`. Type: object (schema `StatusResponse`).

> Object response for account status

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `status_id` | integer (schema `AccountStatusID`) | no | Account status ID | format: "int64"; example: 1234567890 |
| `name` | string (schema `AccountStatusName2`) | no | Account status name. Pre-defined account statuses include `DEBIT_ONLY`, `NORMAL`, `BLOCKED` and `CANCELLED`. You can create your own account statuses with the [Create status](ref:v4-post-account-status) endpoint.<br> | pattern: "^[A-Z_]+$"; maxLength: 200; example: "NORMAL" |
| `description` | string (schema `AccountStatusDescription`) | no | Account status description | maxLength: 500; example: "Full operational account" |
| `state` | string (schema `StatusState`) | no | Status state | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `is_final` | boolean (schema `IsFinalStatus`) | no | Is this a final status? An account with a final status cannot have its status updated. Defaults to `false`.<br><br>**Note:** Even if a status is final, it can still be [rolled back](ref:patch-v2-accounts-accountid-status-rollback).<br> | example: false |
| `allowed_operations` | string (schema `AllowedOperations`) | no | Allowed operations for this status.<br><br>Possible values:<br>* `ALL_OPERATIONS`&mdash;Both credit and debit operations are allowed.<br>* `CREDIT_ONLY`&mdash;Only credit operations allowed.<br>* `DEBIT_ONLY`&mdash;Only debit operations allowed.<br>* `NO_OPERATIONS`&mdash;Neither account credit nor debit operations allowed.<br> | enum: ["ALL_OPERATIONS", "CREDIT_ONLY", "DEBIT_ONLY", "NO_OPERATIONS"]; example: "ALL_OPERATIONS" |

<!-- schema: #/components/schemas/MessageResponse -->
### Schema `MessageResponse`

Pointer: `#/components/schemas/MessageResponse`. Type: object (schema `MessageResponse`).

> Object response for user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `UserMessageCode`) | no | Code that identifies the user message | example: "EACC0000" |
| `message` | string (schema `UserMessage`) | no | User message | example: "Timeout while executing the request" |
| `details` | object (schema `MessageDetailsResponse`) | no | Object response for a user message |  |

<!-- schema: #/components/schemas/SimpleError -->
### Schema `SimpleError`

Pointer: `#/components/schemas/SimpleError`. Type: object (schema `SimpleError`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message |  |

<!-- schema: #/components/schemas/ReasonResponse -->
### Schema `ReasonResponse`

Pointer: `#/components/schemas/ReasonResponse`. Type: object (schema `ReasonResponse`).

> Object response for account reason

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `reason_id` | integer (schema `CreateAccountReasonID`) | no | Reason ID | format: "int64"; example: 1234567890 |
| `name` | string (schema `CreateAccountReasonName`) | no | Reason name | maxLength: 60; example: "Unblocked" |
| `description` | string (schema `CreateAccountReasonDescription`) | no | Reason description | maxLength: 80; example: "Unblocked account after settling the account." |
| `allowed_operations` | string (schema `AllowedOperations`) | no | Allowed operations for this status.<br><br>Possible values:<br>* `ALL_OPERATIONS`&mdash;Both credit and debit operations are allowed.<br>* `CREDIT_ONLY`&mdash;Only credit operations allowed.<br>* `DEBIT_ONLY`&mdash;Only debit operations allowed.<br>* `NO_OPERATIONS`&mdash;Neither account credit nor debit operations allowed.<br> | enum: ["ALL_OPERATIONS", "CREDIT_ONLY", "DEBIT_ONLY", "NO_OPERATIONS"]; example: "ALL_OPERATIONS" |
| `state` | string (schema `ReasonState`) | no | Reason state | enum: ["ACTIVE", "INACTIVE"]; example: "ACTIVE" |
| `external_id` | string (schema `AccountExternalId`) | no | <br>Client-created ID from an external system or application. **REQUIRED** for `VIRTUAL` accounts.<br> | maxLength: 60; example: "8c8a4dd7-e48f-4c15-85b7-9d12f401057f" |

<!-- schema: #/components/schemas/MessageDetailsResponse -->
### Schema `MessageDetailsResponse`

Pointer: `#/components/schemas/MessageDetailsResponse`. Type: object (schema `MessageDetailsResponse`).

> Object response for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `payload` | array of object (schema `MessagePayloadResponse`) | no | Details for the request payload errors |  |
| `parameters` | array of object (schema `MessageParameterResponse`) | no | Details for the query parameter errors |  |
| `external` | array of object (schema `MessageExternalResponse`) | no | Details for the external service error |  |

<!-- schema: #/components/schemas/MessagePayloadResponse -->
### Schema `MessagePayloadResponse`

Pointer: `#/components/schemas/MessagePayloadResponse`. Type: object (schema `MessagePayloadResponse`).

> Object response for detailing request payload errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string (schema `ValidationErrorField`) | no | Non-valid field |  |
| `message` | string (schema `ValidationErrorMessage`) | no | Validation error description |  |

<!-- schema: #/components/schemas/MessageParameterResponse -->
### Schema `MessageParameterResponse`

Pointer: `#/components/schemas/MessageParameterResponse`. Type: object (schema `MessageParameterResponse`).

> Object response for detailing query parameters errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `field` | string (schema `ValidationErrorField`) | no | Non-valid field |  |
| `message` | string (schema `ValidationErrorMessage`) | no | Validation error description |  |

<!-- schema: #/components/schemas/MessageExternalResponse -->
### Schema `MessageExternalResponse`

Pointer: `#/components/schemas/MessageExternalResponse`. Type: object (schema `MessageExternalResponse`).

> Object response for detailing external errors for a user message

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `code` | string (schema `ExternalServiceCode`) | no | Code returned from the external service |  |
| `message` | string | no | Message description from the external service |  |

## Lifecycle status

- `GET /accounts/v1/account-status` (`get-accounts-v1-account-status`) is marked `deprecated: true` in the specification.
- `GET /accounts/v1/accounts-status/reasons` (`get-accounts-v1-accounts-status-reasons`) is marked `deprecated: true` in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounts.yaml` | tag `Statuses and reasons`: GET /accounts/v4/statuses, POST /accounts/v4/statuses, PATCH /accounts/v2/accounts/{accountId}/status, PATCH /accounts/v2/accounts/{accountId}/status/rollback, GET /accounts/v4/reasons, POST /accounts/v4/reasons, GET /accounts/v1/account-status, GET /accounts/v1/accounts-status/reasons | https://github.com/PismoDevEx/pismo-api-specs | `3c621106abf11d41…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/endpoint_event_map.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `34649b6033098e51…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-dormancy` — Dormancy and dormancy reactivation exceptions
- `KU-BANK-managing-account-statuses` — Manage account statuses
- `KU-CARD-card-issuing-basics` — Card issuing reference
- `KU-CARD-multivalue-program-parameters` — Multivalue program parameters
- `KU-CORE-accounts-overview` — Accounts
- `KU-CORE-legal-blocks` — Legal blocks (outdated)
- `KU-CRED-account-collection-status` — Account collection status
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-EVT-accounts-data-events` — Core platform - Accounts
- `KU-EVT-catalogue-account` — Event catalogue: account
- `KU-PAY-faster-payment-system` — Faster Payments (UK)
- `KU-PAY-multi-leg-payments` — Multi-leg payments
- `KU-PAY-payment-overview-and-instant-payments` — Banking payment overview, instant payments and integrated payments
