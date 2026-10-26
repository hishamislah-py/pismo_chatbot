---
ku_id: KU-API-revolving-credit-statements--account
title: 'API reference: Revolving credit - Statements — Account'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Revolving_credit_-_Statements.yaml
  sha256: 2ffe392a0e56ae3b5bf71474f241d08b9b078bb852ffaeff142b4dd32d278fd1
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
- ChangeAccountCollectionStatus
related_kus:
- KU-AUTH-account-and-external-id-tokens
- KU-ERR-codes-esmg-to-whis
specification_version: 2.74.0
---

# API reference: Revolving credit - Statements — Account

**KU ID:** `KU-API-revolving-credit-statements--account` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 1 operation(s) tagged `Account` in `api-specs/Revolving_credit_-_Statements.yaml` (“Revolving credit - Statements”, version `2.74.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> General revolving credit account endpoints

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `PATCH /statements-v2/v1/accounts/{accountId}` | `ChangeAccountCollectionStatus` | Update account collection status | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "Account JWT"}

## Operation contracts

<!-- op: spec=api-specs/Revolving_credit_-_Statements.yaml method=PATCH path=/statements-v2/v1/accounts/{accountId} operationId=ChangeAccountCollectionStatus -->
### `PATCH /statements-v2/v1/accounts/{accountId}` — Update account collection status

- **operationId:** `ChangeAccountCollectionStatus`
- **Specification:** `api-specs/Revolving_credit_-_Statements.yaml` (Revolving credit - Statements)
- **Server base URL(s):** `https://sandbox.pismolabs.io`
- **Tags:** `Account`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Change an account's collection status from `NORMAL` to `OVERDUE` or vice-versa. `OVERDUE` accounts cannot do cash-outs (purchases, cash withdrawals, and so on).
>
> When you try to change an account's collection status to `OVERDUE`, the Pismo platform first verifies that `OpenDueDate` is not `NULL` and that it is a date in the past. If this test fails, it returns `400 Bad request`.
>
> No validations are done when you change the collection status to `NORMAL`.
>
> Changing the account collection status does not affect the [account status](doc:managing-account-statuses#account-statuses-common-to-all-accounts). So, for example, changing the account collection status from `NORMAL` to `OVERDUE` does not cause the account status to change to `BLOCKED`, even though it does prevent cash-outs by blocking the ledger itself. When you change the account collection status from `OVERDUE` to `NORMAL`, the ledger is unblocked and the account is again able to do cash-outs, assuming the account status is not `BLOCKED`. The two fields are not linked.
>
> <table>
>   <thead>
>     <tr>
>       <th>Collection status</th>
>       <th>Account status</th>
>       <th>Result</th>
>     </tr>           
>   </thead>
>   <tbody>
>     <tr>
>       <td><b>`NORMAL`</b>
>       <td><b>`NORMAL`</b></td>
>       <td>Account is usable.</td>
>     </tr>
>     <tr>
>       <td><b>`NORMAL`</b>
>       <td><b>`BLOCKED`</b></td>
>       <td>Account is not usable.</td>
>     </tr>
>     <tr>
>       <td><b>`OVERDUE`</b>
>       <td><b>`NORMAL`</b></td>
>       <td>Account is not usable.</td>
>     </tr>
>     <tr>
>       <td><b>`OVERDUE`</b>
>       <td><b>`BLOCKED`</b></td>
>       <td>Account is not usable.</td>
>     </tr>               
>   </tbody>
> </table>
>
> For more information about the account collection status, refer to the [Credit liquidation](doc:credit-liquidation) guide.
>
> **Note:** This endpoint requires an account token - an access token encoded with a Pismo account ID. Tokens can expire quickly, which can result in a **401 Unauthorized** message.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountId` | path | yes | integer | Account ID | format: "int64"; minimum: 1; example: 101 |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `AccountCollectionStatusV1PatchRequest`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `collection_status` | string (schema `CollectionStatus`) | no | Collection status:<br>* NORMAL<br>* OVERDUE<br><br>If a customer fails to pay at least the minimum amount due on their credit account by a specified number of days after the due date, the account's `collection_status` is set to `OVERDUE`. In all other cases, it should be `NORMAL`. For more information, refer to [Credit liquidation](doc:credit-liquidation).<br> | enum: ["NORMAL", "OVERDUE"]; example: "OVERDUE" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: oneOf: object (schema `AccountCollectionStatusV1PatchResponse`) |
| 400 | Bad request | `application/json`: anyOf: object (schema `ErrorResponse`), object (schema `InvalidFieldErrorResponse`) |
| 500 | Internal Server Error | `application/json`: anyOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

##### Response 400

400 Example `Account Not Found` — from `#/components/examples/AccountNotFound`:

```json
{
  "message": "Account not found."
}
```

400 Example `Invalid Account ID` — from `#/components/examples/InvalidAccountId`:

```json
{
  "message": "Invalid Long value for account_id parameter."
}
```

400 Example `Invalid Status`:

```json
{
  "message": "invalid collection-status"
}
```

##### Response 500

500 Example `Internal Server Error`:

```json
{
  "code": "GN0001",
  "message": "Service is unavailable"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 500 | `GN0001` | Service is unavailable |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-AUTH-account-and-external-id-tokens`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Internal error" |

<!-- schema: #/components/schemas/InvalidFieldErrorResponse -->
### Schema `InvalidFieldErrorResponse`

Pointer: `#/components/schemas/InvalidFieldErrorResponse`. Type: object (schema `InvalidFieldErrorResponse`).

> Standard error response

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | yes | Error message | example: "Amount must not be empty." |
| `field` | string | yes | Field where error occurred. | example: "amount" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Revolving_credit_-_Statements.yaml` | tag `Account`: PATCH /statements-v2/v1/accounts/{accountId} | https://github.com/PismoDevEx/pismo-api-specs | `2ffe392a0e56ae3b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-AUTH-account-and-external-id-tokens` — Endpoints that require account-specific or external-ID tokens
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
