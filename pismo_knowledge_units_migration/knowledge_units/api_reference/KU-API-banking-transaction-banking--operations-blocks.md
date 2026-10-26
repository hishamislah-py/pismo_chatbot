---
ku_id: KU-API-banking-transaction-banking--operations-blocks
title: 'API reference: Banking - Transaction banking — Operations blocks'
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
operations:
- corporate-v2-list-operation-blocks
- corporate-post-v2-operation-blocks
- corporate-get-v2-operation-blocks
- corporate-delete-v2-operation-block-id
- corporate-patch-v2-operation-block-id
related_kus:
- KU-BANK-restrictions
- KU-ERR-codes-acq-to-esma
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wiac-to-wstm
specification_version: 0.9.0
---

# API reference: Banking - Transaction banking — Operations blocks

**KU ID:** `KU-API-banking-transaction-banking--operations-blocks` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Operations blocks` in `api-specs/Banking_-_Transaction_banking.yaml` (“Banking - Transaction banking”, version `0.9.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Operations blocks endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /corporate/v2/operations-blocks` | `corporate-v2-list-operation-blocks` | List operation blocks | no |
| `POST /corporate/v2/operations-blocks` | `corporate-post-v2-operation-blocks` | Create operation block | no |
| `GET /corporate/v2/operations-blocks/{operationsBlockId}` | `corporate-get-v2-operation-blocks` | Get operation block details | no |
| `DELETE /corporate/v2/operations-blocks/{operationsBlockId}` | `corporate-delete-v2-operation-block-id` | Revoke operation block | no |
| `PATCH /corporate/v2/operations-blocks/{operationsBlockId}` | `corporate-patch-v2-operation-block-id` | Update operation block | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"}

## Operation contracts

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v2/operations-blocks operationId=corporate-v2-list-operation-blocks -->
### `GET /corporate/v2/operations-blocks` — List operation blocks

- **operationId:** `corporate-v2-list-operation-blocks`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Operations blocks`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> **NOTE**: This v2 endpoint serves as a replacement for the v1 version.
>
> Lists all operation blocks for an organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `cursor` | query | no | string | Cursor to the next page of results. If no value is specified, it fetches the first page. | example: "1234" |
| `limit` | query | no | integer | Maximum number of items per page. Defaults to `10` | default: 10; format: "int32"; maximum: 20; example: 20 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `ListOperationsBlocksV2`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operation_blocks` | array of object (schema `OperationsBlockV2`) | no | A list of operation blocks |  |
| `pagination` | object (schema `Pagination`) | no | Data related to list pagination using a cursor. |  |

200 Example `Operation blocks`:

```json
{
  "operation_blocks": [
    {
      "block_id": "525f9307-26a7-468b-9428-c7450fc26341",
      "description": "FDIC operation block",
      "status": "DEACTIVATED",
      "created_at": "2025-01-01T12:00:00Z",
      "updated_at": "2025-01-02T12:00:00Z"
    },
    {
      "block_id": "48984e59-33f3-4452-865f-b40181eb1c6d",
      "description": "Division block",
      "division_code": "my-division-code",
      "program_id": 25,
      "status": "ACTIVE",
      "allowed_operations": [
        "EARMARK_CREATE",
        "EARMARK_UPDATE",
        "EARMARK_RELEASE"
      ],
      "created_at": "2025-01-04T12:00:00Z"
    }
  ],
  "pagination": {
    "limit": 10,
    "cursor": "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0="
  }
}
```

##### Response 400

400 Example `invalid cursor`:

```json
{
  "code": "WCMN0004",
  "message": "Invalid cursor"
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
| 400 | `WCMN0004` | Invalid cursor |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;401;403;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-restrictions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=POST path=/corporate/v2/operations-blocks operationId=corporate-post-v2-operation-blocks -->
### `POST /corporate/v2/operations-blocks` — Create operation block

- **operationId:** `corporate-post-v2-operation-blocks`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Operations blocks`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> **NOTE**: This v2 endpoint serves as a replacement for the v1 version.
>
> Creates an operation block for a division or program. This block prevents transactions from being executed within the specified division or program, unless certain operations are explicitly allowed to bypass the restriction.
>
> If neither `division_code` nor `program_id` is provided, the operation block is created for the whole organization.

#### Request body

Required: yes

> Create operation block request body

**Content type `application/json`** — schema: object (schema `CreateOperationsBlockV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `OperationsBlockDescription`) | yes | Operations block description | maxLength: 100; example: "FDIC operations block" |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |
| `program_id` | integer (schema `ProgramID`) | no | Program ID. The program must belong to the organization. Use [List programs](https://developers.pismo.io/pismo-docs/reference/programs-1) to view a list of the program IDs for the organization.<br><br>This program must be bound to the division. You can attach the program with either of the following endpoints:<br>[Create division](ref:post-division-v2)<br>[Patch division](ref:patch-division-v2)<br> | format: "int64"; maximum: 18446744073709552000; example: 8674 |
| `allowed_operations` | array of string (schema `OperationsBlocksOperation`) (schema `AllowedOperations`) | no | List of operations allowed to bypass the block enforcement logic.<br><br>- `EARMARK_RELEASE`: Release an earmark even when an operation block is active.<br>- `EARMARK_UPDATE`: Update an earmark (set amount, increase, or decrease) while the account is blocked by an operation block.<br>- `PAYMENT_DEBIT`: Execute a debit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CREDIT`: Execute a credit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CONFIRM`: Confirm a value transaction while the account is blocked by an operation block.<br>- `PAYMENT_CANCEL`: Cancel an existing transaction while the account is blocked by an operation block.<br>- `ACCOUNT_STATUS_UPDATE`: Change the account status and the associated status reason.<br>- `CHECK_POST`: Post a check while the account is blocked by an operation block.<br>- `CHECK_RELEASE`: Release an uncleared check or operation while the account is blocked by an operation block.<br>- `CHECK_CANCEL`: Cancel an existing check while the account is blocked by an operation block.<br>- `RESTRICTED_FUNDS_CREATE`: Hold a specified amount by transferring it from the available balance to restricted funds.<br>- `RESTRICTED_FUNDS_RELEASE`: Release restricted funds from hold. This transfers funds from restricted funds back to available balance.<br> | example: ["EARMARK_CREATE"]; items.enum: ["EARMARK_CREATE", "EARMARK_RELEASE", "EARMARK_UPDATE", "PAYMENT_DEBIT", "PAYMENT_CREDIT", "PAYMENT_CONFIRM", "PAYMENT_CANCEL", "ACCOUNT_STATUS_UPDATE", "CHECK_POST", "CHECK_RELEASE", "CHECK_CANCEL", "RESTRICTED_FUNDS_CREATE", "RESTRICTED_FUNDS_RELEASE"] |

Example `Operation block`:

```json
{
  "description": "FDIC operation block",
  "division_code": "my-division-code",
  "program_id": 15,
  "allowed_operations": [
    "EARMARK_RELEASE"
  ]
}
```

Example `Operation blocks for the whole organization`:

```json
{
  "description": "FDIC operation block",
  "allowed_operations": [
    "EARMARK_RELEASE"
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `OperationsBlockV2`) |
| 400 | Bad Request | `application/json`: object (schema `ErrorResponse`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 409 | Conflict | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `block_id` | string (schema `OperationsBlockV2ID`) | yes | Operations block ID | format: "uuid"; maxLength: 36; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `description` | string (schema `OperationsBlockDescription`) | yes | Operations block description | maxLength: 100; example: "FDIC operations block" |
| `status` | string (schema `OperationsBlockStatus`) | yes | Status of the operations block.<br> | enum: ["ACTIVE", "DEACTIVATED"]; example: "ACTIVE" |
| `created_at` | string (schema `OperationBlockCreatedAt`) | yes | Operation block creation timestamp (ISO 8601). Format = `YYYY-MM-DDTHH:mm:ss.sssssssssZ`. | format: "date-time"; example: "2024-12-16T06:50:08.83861056Z" |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |
| `program_id` | integer (schema `ProgramID`) | no | Program ID. The program must belong to the organization. Use [List programs](https://developers.pismo.io/pismo-docs/reference/programs-1) to view a list of the program IDs for the organization.<br><br>This program must be bound to the division. You can attach the program with either of the following endpoints:<br>[Create division](ref:post-division-v2)<br>[Patch division](ref:patch-division-v2)<br> | format: "int64"; maximum: 18446744073709552000; example: 8674 |
| `allowed_operations` | array of string (schema `OperationsBlocksOperation`) (schema `AllowedOperations`) | no | List of operations allowed to bypass the block enforcement logic.<br><br>- `EARMARK_RELEASE`: Release an earmark even when an operation block is active.<br>- `EARMARK_UPDATE`: Update an earmark (set amount, increase, or decrease) while the account is blocked by an operation block.<br>- `PAYMENT_DEBIT`: Execute a debit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CREDIT`: Execute a credit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CONFIRM`: Confirm a value transaction while the account is blocked by an operation block.<br>- `PAYMENT_CANCEL`: Cancel an existing transaction while the account is blocked by an operation block.<br>- `ACCOUNT_STATUS_UPDATE`: Change the account status and the associated status reason.<br>- `CHECK_POST`: Post a check while the account is blocked by an operation block.<br>- `CHECK_RELEASE`: Release an uncleared check or operation while the account is blocked by an operation block.<br>- `CHECK_CANCEL`: Cancel an existing check while the account is blocked by an operation block.<br>- `RESTRICTED_FUNDS_CREATE`: Hold a specified amount by transferring it from the available balance to restricted funds.<br>- `RESTRICTED_FUNDS_RELEASE`: Release restricted funds from hold. This transfers funds from restricted funds back to available balance.<br> | example: ["EARMARK_CREATE"]; items.enum: ["EARMARK_CREATE", "EARMARK_RELEASE", "EARMARK_UPDATE", "PAYMENT_DEBIT", "PAYMENT_CREDIT", "PAYMENT_CONFIRM", "PAYMENT_CANCEL", "ACCOUNT_STATUS_UPDATE", "CHECK_POST", "CHECK_RELEASE", "CHECK_CANCEL", "RESTRICTED_FUNDS_CREATE", "RESTRICTED_FUNDS_RELEASE"] |
| `updated_at` | string (schema `OperationBlockUpdatedAt`) | no | Operation block last update timestamp (ISO 8601). Format = `YYYY-MM-DDTHH:mm:ss.sssssssssZ`. | format: "date-time"; example: "2024-12-17T07:50:08.83861056Z" |

##### Response 400

400 Example `Invalid JSON payload`:

```json
{
  "code": "WOBK0001",
  "message": "Invalid JSON payload received: Error unmarshalling request"
}
```

400 Example `description required`:

```json
{
  "code": "WDOR0002",
  "message": "description is a required field"
}
```

400 Example `division not found`:

```json
{
  "code": "WOBK0003",
  "message": "Division not found"
}
```

400 Example `program not found`:

```json
{
  "code": "WOBK0004",
  "message": "Program not found"
}
```

##### Response 409

409 Example `Operations block already exists`:

```json
{
  "code": "WOBK0008",
  "message": "Operations block already exists"
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
| 400 | `WOBK0001` | Invalid JSON payload received: Error unmarshalling request |
| 400 | `WDOR0002` | description is a required field |
| 400 | `WOBK0003` | Division not found |
| 400 | `WOBK0004` | Program not found |
| 409 | `WOBK0008` | Operations block already exists |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;401;403;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-restrictions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=GET path=/corporate/v2/operations-blocks/{operationsBlockId} operationId=corporate-get-v2-operation-blocks -->
### `GET /corporate/v2/operations-blocks/{operationsBlockId}` — Get operation block details

- **operationId:** `corporate-get-v2-operation-blocks`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Operations blocks`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> **NOTE**: This v2 endpoint serves as a replacement for the v1 version.
>
> Gets details about an operation block.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `operationsBlockId` | path | yes | string | Operations block ID | format: "uuid"; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `OperationsBlockV2`) |
| 401 | Access token is missing or invalid |  |
| 403 | The request has been lost |  |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `block_id` | string (schema `OperationsBlockV2ID`) | yes | Operations block ID | format: "uuid"; maxLength: 36; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `description` | string (schema `OperationsBlockDescription`) | yes | Operations block description | maxLength: 100; example: "FDIC operations block" |
| `status` | string (schema `OperationsBlockStatus`) | yes | Status of the operations block.<br> | enum: ["ACTIVE", "DEACTIVATED"]; example: "ACTIVE" |
| `created_at` | string (schema `OperationBlockCreatedAt`) | yes | Operation block creation timestamp (ISO 8601). Format = `YYYY-MM-DDTHH:mm:ss.sssssssssZ`. | format: "date-time"; example: "2024-12-16T06:50:08.83861056Z" |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |
| `program_id` | integer (schema `ProgramID`) | no | Program ID. The program must belong to the organization. Use [List programs](https://developers.pismo.io/pismo-docs/reference/programs-1) to view a list of the program IDs for the organization.<br><br>This program must be bound to the division. You can attach the program with either of the following endpoints:<br>[Create division](ref:post-division-v2)<br>[Patch division](ref:patch-division-v2)<br> | format: "int64"; maximum: 18446744073709552000; example: 8674 |
| `allowed_operations` | array of string (schema `OperationsBlocksOperation`) (schema `AllowedOperations`) | no | List of operations allowed to bypass the block enforcement logic.<br><br>- `EARMARK_RELEASE`: Release an earmark even when an operation block is active.<br>- `EARMARK_UPDATE`: Update an earmark (set amount, increase, or decrease) while the account is blocked by an operation block.<br>- `PAYMENT_DEBIT`: Execute a debit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CREDIT`: Execute a credit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CONFIRM`: Confirm a value transaction while the account is blocked by an operation block.<br>- `PAYMENT_CANCEL`: Cancel an existing transaction while the account is blocked by an operation block.<br>- `ACCOUNT_STATUS_UPDATE`: Change the account status and the associated status reason.<br>- `CHECK_POST`: Post a check while the account is blocked by an operation block.<br>- `CHECK_RELEASE`: Release an uncleared check or operation while the account is blocked by an operation block.<br>- `CHECK_CANCEL`: Cancel an existing check while the account is blocked by an operation block.<br>- `RESTRICTED_FUNDS_CREATE`: Hold a specified amount by transferring it from the available balance to restricted funds.<br>- `RESTRICTED_FUNDS_RELEASE`: Release restricted funds from hold. This transfers funds from restricted funds back to available balance.<br> | example: ["EARMARK_CREATE"]; items.enum: ["EARMARK_CREATE", "EARMARK_RELEASE", "EARMARK_UPDATE", "PAYMENT_DEBIT", "PAYMENT_CREDIT", "PAYMENT_CONFIRM", "PAYMENT_CANCEL", "ACCOUNT_STATUS_UPDATE", "CHECK_POST", "CHECK_RELEASE", "CHECK_CANCEL", "RESTRICTED_FUNDS_CREATE", "RESTRICTED_FUNDS_RELEASE"] |
| `updated_at` | string (schema `OperationBlockUpdatedAt`) | no | Operation block last update timestamp (ISO 8601). Format = `YYYY-MM-DDTHH:mm:ss.sssssssssZ`. | format: "date-time"; example: "2024-12-17T07:50:08.83861056Z" |

##### Response 404

404 Example `Operation block not found`:

```json
{
  "code": "WOBK0006",
  "message": "Operation block not found"
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
| 404 | `WOBK0006` | Operation block not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;401;403;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-restrictions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=DELETE path=/corporate/v2/operations-blocks/{operationsBlockId} operationId=corporate-delete-v2-operation-block-id -->
### `DELETE /corporate/v2/operations-blocks/{operationsBlockId}` — Revoke operation block

- **operationId:** `corporate-delete-v2-operation-block-id`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Operations blocks`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> **NOTE**: This v2 endpoint serves as a replacement for the v1 version.
>
> Cancels a previously configured operation block.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `operationsBlockId` | path | yes | string | Operations block ID | format: "uuid"; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 204 | No Content |  |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 400

400 Example `Operation block is not active`:

```json
{
  "code": "WOBK0009",
  "message": "Operation block is not active"
}
```

400 Example `Invalid id parameter`:

```json
{
  "code": "WOBK0005",
  "message": "Invalid id parameter"
}
```

##### Response 404

404 Example `Operation block not found`:

```json
{
  "code": "WOBK0006",
  "message": "Operation block not found"
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
| 400 | `WOBK0009` | Operation block is not active |
| 400 | `WOBK0005` | Invalid id parameter |
| 404 | `WOBK0006` | Operation block not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `204;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-restrictions`.

<!-- op: spec=api-specs/Banking_-_Transaction_banking.yaml method=PATCH path=/corporate/v2/operations-blocks/{operationsBlockId} operationId=corporate-patch-v2-operation-block-id -->
### `PATCH /corporate/v2/operations-blocks/{operationsBlockId}` — Update operation block

- **operationId:** `corporate-patch-v2-operation-block-id`
- **Specification:** `api-specs/Banking_-_Transaction_banking.yaml` (Banking - Transaction banking)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Operations blocks`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> **NOTE**: This v2 endpoint serves as a replacement for the v1 version.
>
> Updates operation block properties.<br>
> You can use `allowed_operations` to allow certain financial transactions.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `operationsBlockId` | path | yes | string | Operations block ID | format: "uuid"; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |

#### Request body

Required: yes

> Create operation block request body

**Content type `application/json`** — schema: object (schema `PatchOperationsBlockV2Request`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string (schema `OperationsBlockDescription`) | no | Operations block description | maxLength: 100; example: "FDIC operations block" |
| `allowed_operations` | array of string (schema `OperationsBlocksOperation`) (schema `AllowedOperations`) | no | List of operations allowed to bypass the block enforcement logic.<br><br>- `EARMARK_RELEASE`: Release an earmark even when an operation block is active.<br>- `EARMARK_UPDATE`: Update an earmark (set amount, increase, or decrease) while the account is blocked by an operation block.<br>- `PAYMENT_DEBIT`: Execute a debit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CREDIT`: Execute a credit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CONFIRM`: Confirm a value transaction while the account is blocked by an operation block.<br>- `PAYMENT_CANCEL`: Cancel an existing transaction while the account is blocked by an operation block.<br>- `ACCOUNT_STATUS_UPDATE`: Change the account status and the associated status reason.<br>- `CHECK_POST`: Post a check while the account is blocked by an operation block.<br>- `CHECK_RELEASE`: Release an uncleared check or operation while the account is blocked by an operation block.<br>- `CHECK_CANCEL`: Cancel an existing check while the account is blocked by an operation block.<br>- `RESTRICTED_FUNDS_CREATE`: Hold a specified amount by transferring it from the available balance to restricted funds.<br>- `RESTRICTED_FUNDS_RELEASE`: Release restricted funds from hold. This transfers funds from restricted funds back to available balance.<br> | example: ["EARMARK_CREATE"]; items.enum: ["EARMARK_CREATE", "EARMARK_RELEASE", "EARMARK_UPDATE", "PAYMENT_DEBIT", "PAYMENT_CREDIT", "PAYMENT_CONFIRM", "PAYMENT_CANCEL", "ACCOUNT_STATUS_UPDATE", "CHECK_POST", "CHECK_RELEASE", "CHECK_CANCEL", "RESTRICTED_FUNDS_CREATE", "RESTRICTED_FUNDS_RELEASE"] |

Example `Both attributes`:

```json
{
  "description": "FDIC operation block",
  "allowed_operations": [
    "EARMARK_RELEASE"
  ]
}
```

Example `Only description`:

```json
{
  "description": "FDIC operation block"
}
```

Example `Only allowed_operations`:

```json
{
  "allowed_operations": [
    "EARMARK_RELEASE"
  ]
}
```

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `OperationsBlockV2`) |
| 400 | Bad request | `application/json`: object (schema `ErrorResponse`) |
| 404 | Not Found | `application/json`: object (schema `ErrorResponse`) |
| 500 | Internal Server Error | `application/json`: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `block_id` | string (schema `OperationsBlockV2ID`) | yes | Operations block ID | format: "uuid"; maxLength: 36; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `description` | string (schema `OperationsBlockDescription`) | yes | Operations block description | maxLength: 100; example: "FDIC operations block" |
| `status` | string (schema `OperationsBlockStatus`) | yes | Status of the operations block.<br> | enum: ["ACTIVE", "DEACTIVATED"]; example: "ACTIVE" |
| `created_at` | string (schema `OperationBlockCreatedAt`) | yes | Operation block creation timestamp (ISO 8601). Format = `YYYY-MM-DDTHH:mm:ss.sssssssssZ`. | format: "date-time"; example: "2024-12-16T06:50:08.83861056Z" |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |
| `program_id` | integer (schema `ProgramID`) | no | Program ID. The program must belong to the organization. Use [List programs](https://developers.pismo.io/pismo-docs/reference/programs-1) to view a list of the program IDs for the organization.<br><br>This program must be bound to the division. You can attach the program with either of the following endpoints:<br>[Create division](ref:post-division-v2)<br>[Patch division](ref:patch-division-v2)<br> | format: "int64"; maximum: 18446744073709552000; example: 8674 |
| `allowed_operations` | array of string (schema `OperationsBlocksOperation`) (schema `AllowedOperations`) | no | List of operations allowed to bypass the block enforcement logic.<br><br>- `EARMARK_RELEASE`: Release an earmark even when an operation block is active.<br>- `EARMARK_UPDATE`: Update an earmark (set amount, increase, or decrease) while the account is blocked by an operation block.<br>- `PAYMENT_DEBIT`: Execute a debit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CREDIT`: Execute a credit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CONFIRM`: Confirm a value transaction while the account is blocked by an operation block.<br>- `PAYMENT_CANCEL`: Cancel an existing transaction while the account is blocked by an operation block.<br>- `ACCOUNT_STATUS_UPDATE`: Change the account status and the associated status reason.<br>- `CHECK_POST`: Post a check while the account is blocked by an operation block.<br>- `CHECK_RELEASE`: Release an uncleared check or operation while the account is blocked by an operation block.<br>- `CHECK_CANCEL`: Cancel an existing check while the account is blocked by an operation block.<br>- `RESTRICTED_FUNDS_CREATE`: Hold a specified amount by transferring it from the available balance to restricted funds.<br>- `RESTRICTED_FUNDS_RELEASE`: Release restricted funds from hold. This transfers funds from restricted funds back to available balance.<br> | example: ["EARMARK_CREATE"]; items.enum: ["EARMARK_CREATE", "EARMARK_RELEASE", "EARMARK_UPDATE", "PAYMENT_DEBIT", "PAYMENT_CREDIT", "PAYMENT_CONFIRM", "PAYMENT_CANCEL", "ACCOUNT_STATUS_UPDATE", "CHECK_POST", "CHECK_RELEASE", "CHECK_CANCEL", "RESTRICTED_FUNDS_CREATE", "RESTRICTED_FUNDS_RELEASE"] |
| `updated_at` | string (schema `OperationBlockUpdatedAt`) | no | Operation block last update timestamp (ISO 8601). Format = `YYYY-MM-DDTHH:mm:ss.sssssssssZ`. | format: "date-time"; example: "2024-12-17T07:50:08.83861056Z" |

##### Response 400

400 Example `One of the attributes must be provided`:

```json
{
  "code": "WOBK0002",
  "message": "description or allowed_operations must be provided"
}
```

400 Example `Invalid id parameter`:

```json
{
  "code": "WOBK0005",
  "message": "Invalid id parameter"
}
```

400 Example `Not Active`:

```json
{
  "code": "WOBK0009",
  "message": "Operation block is not active"
}
```

##### Response 404

404 Example `Operation block not found`:

```json
{
  "code": "WOBK0006",
  "message": "Operation block not found"
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
| 400 | `WOBK0002` | description or allowed_operations must be provided |
| 400 | `WOBK0005` | Invalid id parameter |
| 400 | `WOBK0009` | Operation block is not active |
| 404 | `WOBK0006` | Operation block not found |
| 500 | `ECMN9999` | Internal error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-restrictions`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/OperationsBlockV2 -->
### Schema `OperationsBlockV2`

Pointer: `#/components/schemas/OperationsBlockV2`. Type: object (schema `OperationsBlockV2`).

> Operations block

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `block_id` | string (schema `OperationsBlockV2ID`) | yes | Operations block ID | format: "uuid"; maxLength: 36; example: "e4adf199-c925-4d11-b002-c5bfd5679030" |
| `description` | string (schema `OperationsBlockDescription`) | yes | Operations block description | maxLength: 100; example: "FDIC operations block" |
| `status` | string (schema `OperationsBlockStatus`) | yes | Status of the operations block.<br> | enum: ["ACTIVE", "DEACTIVATED"]; example: "ACTIVE" |
| `created_at` | string (schema `OperationBlockCreatedAt`) | yes | Operation block creation timestamp (ISO 8601). Format = `YYYY-MM-DDTHH:mm:ss.sssssssssZ`. | format: "date-time"; example: "2024-12-16T06:50:08.83861056Z" |
| `division_code` | string (schema `DivisionCode`) | no | Code used to identify your division within the organization. Division code should only contain letters, numbers, and hyphens.<br><br>This is a client-provided ID and can be changed.<br> | maxLength: 36; example: "US" |
| `program_id` | integer (schema `ProgramID`) | no | Program ID. The program must belong to the organization. Use [List programs](https://developers.pismo.io/pismo-docs/reference/programs-1) to view a list of the program IDs for the organization.<br><br>This program must be bound to the division. You can attach the program with either of the following endpoints:<br>[Create division](ref:post-division-v2)<br>[Patch division](ref:patch-division-v2)<br> | format: "int64"; maximum: 18446744073709552000; example: 8674 |
| `allowed_operations` | array of string (schema `OperationsBlocksOperation`) (schema `AllowedOperations`) | no | List of operations allowed to bypass the block enforcement logic.<br><br>- `EARMARK_RELEASE`: Release an earmark even when an operation block is active.<br>- `EARMARK_UPDATE`: Update an earmark (set amount, increase, or decrease) while the account is blocked by an operation block.<br>- `PAYMENT_DEBIT`: Execute a debit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CREDIT`: Execute a credit transaction while the account is blocked by an operation block.<br>- `PAYMENT_CONFIRM`: Confirm a value transaction while the account is blocked by an operation block.<br>- `PAYMENT_CANCEL`: Cancel an existing transaction while the account is blocked by an operation block.<br>- `ACCOUNT_STATUS_UPDATE`: Change the account status and the associated status reason.<br>- `CHECK_POST`: Post a check while the account is blocked by an operation block.<br>- `CHECK_RELEASE`: Release an uncleared check or operation while the account is blocked by an operation block.<br>- `CHECK_CANCEL`: Cancel an existing check while the account is blocked by an operation block.<br>- `RESTRICTED_FUNDS_CREATE`: Hold a specified amount by transferring it from the available balance to restricted funds.<br>- `RESTRICTED_FUNDS_RELEASE`: Release restricted funds from hold. This transfers funds from restricted funds back to available balance.<br> | example: ["EARMARK_CREATE"]; items.enum: ["EARMARK_CREATE", "EARMARK_RELEASE", "EARMARK_UPDATE", "PAYMENT_DEBIT", "PAYMENT_CREDIT", "PAYMENT_CONFIRM", "PAYMENT_CANCEL", "ACCOUNT_STATUS_UPDATE", "CHECK_POST", "CHECK_RELEASE", "CHECK_CANCEL", "RESTRICTED_FUNDS_CREATE", "RESTRICTED_FUNDS_RELEASE"] |
| `updated_at` | string (schema `OperationBlockUpdatedAt`) | no | Operation block last update timestamp (ISO 8601). Format = `YYYY-MM-DDTHH:mm:ss.sssssssssZ`. | format: "date-time"; example: "2024-12-17T07:50:08.83861056Z" |

<!-- schema: #/components/schemas/Pagination -->
### Schema `Pagination`

Pointer: `#/components/schemas/Pagination`. Type: object (schema `Pagination`).

> Data related to list pagination using a cursor.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `limit` | integer (schema `MaxItemsPerPage`) | no | Maximum number of items per page | format: "int32"; example: 10 |
| `cursor` | string (schema `Cursor`) | no | Cursor pointing to the next page of results | example: "eyJJRCI6IjBjOGVhMTA4LWNhZTYtNDA2Mi1iMmQzLTFhMTZkNmJiNGIyOCIsIk9yZ0lEIjoiMDllYThhMDQtNWY5My0xMWVkLTliNmEtMDI0MmFjMTIwMDAyIn0=" |

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
| `api-specs/Banking_-_Transaction_banking.yaml` | tag `Operations blocks`: GET /corporate/v2/operations-blocks, POST /corporate/v2/operations-blocks, GET /corporate/v2/operations-blocks/{operationsBlockId}, DELETE /corporate/v2/operations-blocks/{operationsBlockId}, PATCH /corporate/v2/operations-blocks/{operationsBlockId} | https://github.com/PismoDevEx/pismo-api-specs | `dec6c4900eb2db35…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-restrictions` — Restrictions: restrict funds, restriction management and operation blocks
- `KU-ERR-codes-acq-to-esma` — Error codes: ACQ to ESMA (32 prefixes)
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wiac-to-wstm` — Error codes: WIAC to WSTM (9 prefixes)
