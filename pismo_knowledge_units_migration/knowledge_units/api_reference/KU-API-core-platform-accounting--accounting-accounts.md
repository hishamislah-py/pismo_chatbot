---
ku_id: KU-API-core-platform-accounting--accounting-accounts
title: 'API reference: Core platform - Accounting — Accounting accounts'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Accounting.yaml
  sha256: f0272a891eaca0fedca4fa47cc760ff7fd676f50c94a22aa19ac665fa7017451
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
- SearchAccountingAccounts
- CreateAccountingAccount
- GetAccountingAccountById
- DeleteAccountingAccount
- UpdateAccountingAccount
related_kus:
- KU-CORE-accounting-accounts-and-entries
- KU-CORE-accounting-overview
specification_version: 1.0.0
---

# API reference: Core platform - Accounting — Accounting accounts

**KU ID:** `KU-API-core-platform-accounting--accounting-accounts` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 5 operation(s) tagged `Accounting accounts` in `api-specs/Core_platform_-_Accounting.yaml` (“Core platform - Accounting”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage the accounting plan, which is a set of accounting accounts.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounting-accounts` | `SearchAccountingAccounts` | List accounting accounts | no |
| `POST /v1/accounting-accounts` | `CreateAccountingAccount` | Create accounting account | no |
| `GET /v1/accounting-accounts/{accountingAccountId}` | `GetAccountingAccountById` | Get accounting account | no |
| `DELETE /v1/accounting-accounts/{accountingAccountId}` | `DeleteAccountingAccount` | Delete accounting account | no |
| `PATCH /v1/accounting-accounts/{accountingAccountId}` | `UpdateAccountingAccount` | Update accounting account | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v1/accounting-accounts operationId=SearchAccountingAccounts -->
### `GET /v1/accounting-accounts` — List accounting accounts

- **operationId:** `SearchAccountingAccounts`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List accounting accounts for your organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `account` | query | no | string | Account ID filter to list all accounting accounts related to an account. |  |
| `programId` | query | no | integer | Program ID filter to list all accounting accounts related to a program. |  |
| `pageSize` | query | no | integer | Maximum number of accounting event types per page. |  |
| `pageOffset` | query | no | integer | Number to offset page resuts. For example, value `2` returns the third page. Defaults to `0`, which returns the first page. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Indicates if there are more items to be retrieved. |  |
| `items` | array of object | no | Items retrieved from a given request. |  |
| `items` | array of object (schema `AccountingAccount`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=POST path=/v1/accounting-accounts operationId=CreateAccountingAccount -->
### `POST /v1/accounting-accounts` — Create accounting account

- **operationId:** `CreateAccountingAccount`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an accounting account.
>
> Refer to the [How to create accounting account](doc:create-an-accounting-account) guide for more information.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `AccountingAccountPost`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | yes | Description that helps to identify the accounting account.  Can be `0` or any value if there's no corresponding account. | maxLength: 100 |
| `account` | string | yes | Accounting account number. Can be `0` or any value if there's no corresponding account. | maxLength: 50 |
| `program_id` | integer | yes | Related program ID | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `AccountingAccount`) |
| 400 | Bad request when some provided parameter is invalid. |  |
| 409 | Accounting account already exists. |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Accounting account ID | format: "int64" |
| `description` | string | no | Description of the accounting account | maxLength: 100 |
| `account` | string | no | Accounting account number | maxLength: 50 |
| `program_id` | integer | no | Program ID | format: "int64" |
| `created_at` | string | no | Date and time when the accounting account was created (ISO 8601). | format: "date-time" |
| `deactivated_at` | string | no | Date and time when the accounting account was deactivated (ISO 8601). Filled when the account is deactivated. | format: "date-time" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`, `KU-CORE-accounting-overview`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v1/accounting-accounts/{accountingAccountId} operationId=GetAccountingAccountById -->
### `GET /v1/accounting-accounts/{accountingAccountId}` — Get accounting account

- **operationId:** `GetAccountingAccountById`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a specific accounting account by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountingAccountId` | path | yes | integer | Accounting account ID | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountingAccount`) |
| 404 | Accounting account not found. |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Accounting account ID | format: "int64" |
| `description` | string | no | Description of the accounting account | maxLength: 100 |
| `account` | string | no | Accounting account number | maxLength: 50 |
| `program_id` | integer | no | Program ID | format: "int64" |
| `created_at` | string | no | Date and time when the accounting account was created (ISO 8601). | format: "date-time" |
| `deactivated_at` | string | no | Date and time when the accounting account was deactivated (ISO 8601). Filled when the account is deactivated. | format: "date-time" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=DELETE path=/v1/accounting-accounts/{accountingAccountId} operationId=DeleteAccountingAccount -->
### `DELETE /v1/accounting-accounts/{accountingAccountId}` — Delete accounting account

- **operationId:** `DeleteAccountingAccount`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Delete an accounting account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountingAccountId` | path | yes | integer | Accounting account ID | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: (type not declared) |
| 404 | Accounting account not found |  |
| 409 | Accounting account cannot be deleted, because it's being used by an active accounting script. |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404;409`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=PATCH path=/v1/accounting-accounts/{accountingAccountId} operationId=UpdateAccountingAccount -->
### `PATCH /v1/accounting-accounts/{accountingAccountId}` — Update accounting account

- **operationId:** `UpdateAccountingAccount`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting accounts`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update description of an accounting account.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountingAccountId` | path | yes | integer | Accounting account ID | format: "int64" |

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `AccountingAccountPatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | yes | Description that helps to identify the accounting account | maxLength: 100 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: array of object (schema `AccountingAccount`) |
| 400 | Bad request when a provided parameter is invalid. |  |
| 404 | Accounting account not found. |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountingAccount -->
### Schema `AccountingAccount`

Pointer: `#/components/schemas/AccountingAccount`. Type: object (schema `AccountingAccount`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Accounting account ID | format: "int64" |
| `description` | string | no | Description of the accounting account | maxLength: 100 |
| `account` | string | no | Accounting account number | maxLength: 50 |
| `program_id` | integer | no | Program ID | format: "int64" |
| `created_at` | string | no | Date and time when the accounting account was created (ISO 8601). | format: "date-time" |
| `deactivated_at` | string | no | Date and time when the accounting account was deactivated (ISO 8601). Filled when the account is deactivated. | format: "date-time" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounting.yaml` | tag `Accounting accounts`: GET /v1/accounting-accounts, POST /v1/accounting-accounts, GET /v1/accounting-accounts/{accountingAccountId}, DELETE /v1/accounting-accounts/{accountingAccountId}, PATCH /v1/accounting-accounts/{accountingAccountId} | https://github.com/PismoDevEx/pismo-api-specs | `f0272a891eaca0fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-accounting-accounts-and-entries` — Creating accounting accounts and accounting entries
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
