---
ku_id: KU-API-core-platform-accounting--accounting-scripts-v2
title: 'API reference: Core platform - Accounting — Accounting scripts V2'
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
- listAccountingScriptsV2
- CreateAccountingScriptV2
- getAccountingScriptByIdV2
related_kus:
- KU-CORE-create-an-accounting-script
specification_version: 1.0.0
---

# API reference: Core platform - Accounting — Accounting scripts V2

**KU ID:** `KU-API-core-platform-accounting--accounting-scripts-v2` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Accounting scripts V2` in `api-specs/Core_platform_-_Accounting.yaml` (“Core platform - Accounting”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage accounting scripts V2

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v2/accounting-scripts` | `listAccountingScriptsV2` | List accounting scripts V2 | no |
| `POST /v2/accounting-scripts` | `CreateAccountingScriptV2` | Create accounting script V2 | no |
| `GET /v2/accounting-scripts/{accountingScriptId}` | `getAccountingScriptByIdV2` | Get accounting script V2 | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v2/accounting-scripts operationId=listAccountingScriptsV2 -->
### `GET /v2/accounting-scripts` — List accounting scripts V2

- **operationId:** `listAccountingScriptsV2`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V2`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List existing accounting scripts for your organization.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `pageSize` | query | no | integer | Maximum number of accounting event types per page. |  |
| `pageOffset` | query | no | integer | Number to offset page resuts. For example, value `2` returns the third page. Defaults to `0`, which returns the first page. |  |
| `debitAccountingAccount` | query | no | string | List all accounting scripts related to a debit accounting account |  |
| `creditAccountingAccount` | query | no | string | List all accounting scripts related to a credit accounting account |  |
| `programId` | query | no | integer | List all accounting scripts related to a program | format: "int64" |
| `eventTypeId` | query | no | integer | List all accounting scripts related to an event type | format: "int64" |
| `entryTypeId` | query | no | integer | List all accounting scripts related to an entry type | format: "int64" |
| `cashInBucketName` | query | no | integer | List all accounting scripts related to a cash-in bucket name | format: "int64" |
| `cashOutBucketName` | query | no | integer | List all accounting scripts related to a cash-out bucket name | format: "int64" |
| `isStage` | query | no | string | List all accounting scripts in production or staging environment |  |

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
| `items` | array of object (schema `AccountingScriptV2`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=POST path=/v2/accounting-scripts operationId=CreateAccountingScriptV2 -->
### `POST /v2/accounting-scripts` — Create accounting script V2

- **operationId:** `CreateAccountingScriptV2`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V2`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an accounting script.
>
> Refer to the [How to create accounting script](doc:create-an-accounting-script) guide for more information.

#### Request body

Required: yes

**Content type `application/json`** — schema: object (schema `AccountingScriptPostV2`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credit_accounting` | object (schema `AccountingAccountAccountSctiptPost`) | yes |  | example: {"description": "SAMPLE ACCOUNT", "account": "123123132-x"} |
| `debit_accounting` | object (schema `AccountingAccountAccountSctiptPost`) | yes |  | example: {"description": "SAMPLE ACCOUNT", "account": "123123132-x"} |
| `entry_type_id` | object (schema `EntryTypePost`) | yes |  |  |
| `expression` | string | yes | Expression to calculate the value of the accounting entry.<br>It can be a simple mathematical expression or a more complex one using functions.<br>Identifiers must belong to the evaluator vocabulary: AMOUNT, INTEREST, FEE, BUCKET,<br>TRANSACTIONS, DISCHARGE_AMOUNT, BALANCE_AMOUNT, MDR_AMOUNT, SETTLEMENT_AMOUNT (and the<br>SUM function); quoted map keys such as FEE['iof'] are allowed. Unknown identifiers<br>(e.g. V1 entry-name strings like amount-dueDate) are rejected with ET0007.<br> |  |
| `cash_in_bucket` | object (schema `AccountingScriptBucket`) | no |  |  |
| `cash_out_bucket` | object (schema `AccountingScriptBucket`) | no |  |  |
| `cost_center` | object (schema `CostCenterAccountingScriptPost`) | no |  | example: {"debit_org": "999999", "credit_org": "999999", "debit_cost": "999999", "credit_cost": "999999"} |
| `event_type_id` | integer | no | Event type ID | format: "int64" |
| `except_program_ids` | array of integer | no |  | example: [78, 91] |
| `fee_information` | object | no | Information about the fee applied to the accounting entry.<br>It can include details such as fee type, amount, and currency.<br> |  |
| `is_database_stage` | string | no | Is this accounting script for database staging?<br>If yes, the script is used for testing purposes and does not affect production data.<br> | default: "no"; example: "yes" |
| `max_days_due` | integer | no | Maximum number of days for the due date | format: "int64"; example: 90 |
| `min_days_due` | integer | no | Minimum number of days for the due date | format: "int64"; example: 30 |
| `parameters` | object (schema `AccountingScriptParameters`) | no |  |  |
| `processing_code` | string | no | Processing code |  |
| `program_id` | integer | no | Program ID | format: "int64" |
| `program_list_id` | array of integer | no |  | example: [12, 34, 56] |
| `program_types` | array of string | no |  | example: ["CREDIT", "DEBIT"] |
| `reason` | string (schema `HistoryReason`) | no | Reason for the operation. | maxLength: 250; example: "Creation of a new entry type configuration." |
| `responsible` | string (schema `HistoryResponsible`) | no | User name or ID of the person performing the operation. | maxLength: 100; example: "John Doe" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: array of object (schema `AccountingScriptV2`) |
| 400 | Bad request |  |
| 409 | Conflict |  |

##### Response 201

**201 `application/json` body fields:**

_No fields declared in the schema._


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-create-an-accounting-script`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v2/accounting-scripts/{accountingScriptId} operationId=getAccountingScriptByIdV2 -->
### `GET /v2/accounting-scripts/{accountingScriptId}` — Get accounting script V2

- **operationId:** `getAccountingScriptByIdV2`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V2`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Get a specific accounting script by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountingScriptId` | path | yes | integer | Accounting script ID | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Accounting script found | `application/json`: object (schema `AccountingScriptV2`) |
| 404 | Not found |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Accounting script ID | format: "int64" |
| `program_id` | integer | no | Program ID | format: "int64" |
| `event_type_id` | integer | no | Event type ID | format: "int64" |
| `entry_type_id` | integer | no | Entry type ID | format: "int64" |
| `debit_accounting` | object (schema `AccountingAccountAccountSctiptPost`) | no |  | example: {"description": "SAMPLE ACCOUNT", "account": "123123132-x"} |
| `credit_accounting` | object (schema `AccountingAccountAccountSctiptPost`) | no |  | example: {"description": "SAMPLE ACCOUNT", "account": "123123132-x"} |
| `cost_center` | object (schema `CostCenterAccountingScriptPost`) | no |  | example: {"debit_org": "999999", "credit_org": "999999", "debit_cost": "999999", "credit_cost": "999999"} |
| `processing_code` | string | no | Processing code |  |
| `expression` | string | no | Expression to calculate the value of the accounting entry.<br>It can be a simple mathematical expression or a more complex one using functions.<br>Identifiers must belong to the evaluator vocabulary: AMOUNT, INTEREST, FEE, BUCKET,<br>TRANSACTIONS, DISCHARGE_AMOUNT, BALANCE_AMOUNT, MDR_AMOUNT, SETTLEMENT_AMOUNT (and the<br>SUM function); quoted map keys such as FEE['iof'] are allowed. Unknown identifiers<br>(e.g. V1 entry-name strings like amount-dueDate) are rejected with ET0007.<br> |  |
| `fee_information` | object | no | Information about the fee applied to the accounting entry.<br>It can include details such as fee type, amount, and currency.<br> |  |
| `parameters` | object (schema `AccountingScriptParameters`) | no |  |  |
| `cash_in_bucket` | object (schema `AccountingScriptBucket`) | no |  |  |
| `cash_out_bucket` | object (schema `AccountingScriptBucket`) | no |  |  |
| `is_database_stage` | string | no | Indicates if the accounting script is for a database stage.<br>If yes, the script is used for testing purposes and does not affect production data.<br> | default: "no"; example: "yes" |
| `min_days_due` | integer | no | Minimum number of days for the due date | format: "int64"; example: 30 |
| `max_days_due` | integer | no | Maximum number of days for the due date | format: "int64"; example: 90 |
| `history` | object (schema `History`) | no | Historical information for auditing the entity. |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `False`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountingScriptV2 -->
### Schema `AccountingScriptV2`

Pointer: `#/components/schemas/AccountingScriptV2`. Type: object (schema `AccountingScriptV2`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer | no | Accounting script ID | format: "int64" |
| `program_id` | integer | no | Program ID | format: "int64" |
| `event_type_id` | integer | no | Event type ID | format: "int64" |
| `entry_type_id` | integer | no | Entry type ID | format: "int64" |
| `debit_accounting` | object (schema `AccountingAccountAccountSctiptPost`) | no |  | example: {"description": "SAMPLE ACCOUNT", "account": "123123132-x"} |
| `credit_accounting` | object (schema `AccountingAccountAccountSctiptPost`) | no |  | example: {"description": "SAMPLE ACCOUNT", "account": "123123132-x"} |
| `cost_center` | object (schema `CostCenterAccountingScriptPost`) | no |  | example: {"debit_org": "999999", "credit_org": "999999", "debit_cost": "999999", "credit_cost": "999999"} |
| `processing_code` | string | no | Processing code |  |
| `expression` | string | no | Expression to calculate the value of the accounting entry.<br>It can be a simple mathematical expression or a more complex one using functions.<br>Identifiers must belong to the evaluator vocabulary: AMOUNT, INTEREST, FEE, BUCKET,<br>TRANSACTIONS, DISCHARGE_AMOUNT, BALANCE_AMOUNT, MDR_AMOUNT, SETTLEMENT_AMOUNT (and the<br>SUM function); quoted map keys such as FEE['iof'] are allowed. Unknown identifiers<br>(e.g. V1 entry-name strings like amount-dueDate) are rejected with ET0007.<br> |  |
| `fee_information` | object | no | Information about the fee applied to the accounting entry.<br>It can include details such as fee type, amount, and currency.<br> |  |
| `parameters` | object (schema `AccountingScriptParameters`) | no |  |  |
| `cash_in_bucket` | object (schema `AccountingScriptBucket`) | no |  |  |
| `cash_out_bucket` | object (schema `AccountingScriptBucket`) | no |  |  |
| `is_database_stage` | string | no | Indicates if the accounting script is for a database stage.<br>If yes, the script is used for testing purposes and does not affect production data.<br> | default: "no"; example: "yes" |
| `min_days_due` | integer | no | Minimum number of days for the due date | format: "int64"; example: 30 |
| `max_days_due` | integer | no | Maximum number of days for the due date | format: "int64"; example: 90 |
| `history` | object (schema `History`) | no | Historical information for auditing the entity. |  |

<!-- schema: #/components/schemas/AccountingAccountAccountSctiptPost -->
### Schema `AccountingAccountAccountSctiptPost`

Pointer: `#/components/schemas/AccountingAccountAccountSctiptPost`. Type: object (schema `AccountingAccountAccountSctiptPost`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `description` | string | yes | Description that helps to identify the accounting account.  Can be `0` or any value if there's no corresponding account. | maxLength: 100 |
| `account` | string | yes | Accounting account number.  Can be `0` or any value if there's no corresponding account. | maxLength: 50 |

<!-- schema: #/components/schemas/EntryTypePost -->
### Schema `EntryTypePost`

Pointer: `#/components/schemas/EntryTypePost`. Type: object (schema `EntryTypePost`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `id` | integer (schema `EntryTypeID`) | yes | Entry type ID | format: "int64"; example: 101 |
| `description` | string (schema `EntryTypeDescription`) | yes | Entry type description. | maxLength: 250; example: "CREDIT" |
| `type` | string (schema `EntryTypeType`) | yes | Set the entry type:<br><br>* `CREATION`: Default value for new entries. Also, this value is assumed when type is not provided.<br>* `DUE_DATE`: Used only with a credit program to indicate a due date entry.<br> | enum: ["DUE_DATE", "CREATION"]; maxLength: 100; example: "DUE_DATE" |
| `reason` | string (schema `HistoryReason`) | yes | Reason for the operation. | maxLength: 250; example: "Creation of a new entry type configuration." |
| `responsible` | string (schema `HistoryResponsible`) | no | User name or ID of the person performing the operation. | maxLength: 100; example: "John Doe" |

<!-- schema: #/components/schemas/AccountingScriptBucket -->
### Schema `AccountingScriptBucket`

Pointer: `#/components/schemas/AccountingScriptBucket`. Type: object (schema `AccountingScriptBucket`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | no | Bucket name | example: "bacen_pre_2039" |
| `account` | integer | no | Account ID | format: "int64"; example: 123456 |

<!-- schema: #/components/schemas/CostCenterAccountingScriptPost -->
### Schema `CostCenterAccountingScriptPost`

Pointer: `#/components/schemas/CostCenterAccountingScriptPost`. Type: object (schema `CostCenterAccountingScriptPost`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `debit_org` | string | yes | Number of your Org’s debit accounting account | maxLength: 50 |
| `credit_org` | string | yes | Number of your Org’s credit accounting account | maxLength: 50 |
| `debit_cost` | string | yes | Number of the cost center of the debit accounting account | maxLength: 50 |
| `credit_cost` | string | yes | Number of the cost center of the credit accounting account | maxLength: 50 |

<!-- schema: #/components/schemas/AccountingScriptParameters -->
### Schema `AccountingScriptParameters`

Pointer: `#/components/schemas/AccountingScriptParameters`. Type: object (schema `AccountingScriptParameters`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `name` | string | yes | Parameter name [pismo:timing or bacen:classification] | example: "pismo:timing" |
| `value` | string | yes | Parameter value [REGULAR, DUEDATE, TRUE, or 3] | example: "REGULAR, DUEDATE" |

<!-- schema: #/components/schemas/History -->
### Schema `History`

Pointer: `#/components/schemas/History`. Type: object (schema `History`).

> Historical information for auditing the entity.

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `org_id` | string (schema `OrgID`) | no | Organization ID | example: "TN-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" |
| `action` | string | no | Action performed on the entity. | example: "Created" |
| `reason` | string (schema `HistoryReason`) | no | Reason for the operation. | maxLength: 250; example: "Creation of a new entry type configuration." |
| `responsible` | string (schema `HistoryResponsible`) | no | User name or ID of the person performing the operation. | maxLength: 100; example: "John Doe" |
| `version` | integer | no | Entity version. | format: "int64"; example: 1 |
| `jsonb` | string | no | JSON representation of the request body. | example: "{\\"id\\": 101, \\"description\\": \\"CREDIT\\", \\"type\\": \\"DUE_DATE\\", \\"reason\\": \\"Creation of a new entry type configuration.\\", \\"responsible\\": \\"John Doe\\", \\"created_at\\": \\"2021-10-10T10:10:00Z\\"}" |
| `created_at` | string | no | Date and time when the history was created (ISO 8601). Format: YYYY-MM-DDThh:mm:ssZ. | format: "date-time"; example: "2021-10-10T10:10:00Z" |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounting.yaml` | tag `Accounting scripts V2`: GET /v2/accounting-scripts, POST /v2/accounting-scripts, GET /v2/accounting-scripts/{accountingScriptId} | https://github.com/PismoDevEx/pismo-api-specs | `f0272a891eaca0fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-create-an-accounting-script` — Create accounting scripts
