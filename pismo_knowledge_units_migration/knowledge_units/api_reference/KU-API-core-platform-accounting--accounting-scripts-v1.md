---
ku_id: KU-API-core-platform-accounting--accounting-scripts-v1
title: 'API reference: Core platform - Accounting — Accounting scripts V1'
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
- SearchAccountingScript
- CreateAccountingScript
- BatchUpdateAccountingScript
- GetAccountingScriptById
- DeactivateAccountingScript
- UpdateAccountingScript
related_kus:
- KU-CORE-accounting-accounts-and-entries
- KU-CORE-accounting-overview
- KU-CORE-create-an-accounting-script
specification_version: 1.0.0
---

# API reference: Core platform - Accounting — Accounting scripts V1

**KU ID:** `KU-API-core-platform-accounting--accounting-scripts-v1` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 6 operation(s) tagged `Accounting scripts V1` in `api-specs/Core_platform_-_Accounting.yaml` (“Core platform - Accounting”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage accounting scripts V1

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/accounting-scripts` | `SearchAccountingScript` | List accounting scripts V1 | no |
| `POST /v1/accounting-scripts` | `CreateAccountingScript` | Create accounting script V1 | no |
| `PATCH /v1/accounting-scripts/batch` | `BatchUpdateAccountingScript` | Update accounting scripts V1 | no |
| `GET /v1/accounting-scripts/{accountingScriptId}` | `GetAccountingScriptById` | Get accounting script V1 | no |
| `DELETE /v1/accounting-scripts/{accountingScriptId}` | `DeactivateAccountingScript` | Deactivate accounting script V1 | no |
| `PATCH /v1/accounting-scripts/{accountingScriptId}` | `UpdateAccountingScript` | Update accounting script V1 | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v1/accounting-scripts operationId=SearchAccountingScript -->
### `GET /v1/accounting-scripts` — List accounting scripts V1

- **operationId:** `SearchAccountingScript`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V1`
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
| `items` | array of object (schema `AccountingScript`) | no |  |  |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=POST path=/v1/accounting-scripts operationId=CreateAccountingScript -->
### `POST /v1/accounting-scripts` — Create accounting script V1

- **operationId:** `CreateAccountingScript`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V1`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Create an accounting script.
>
> Refer to the [How to create accounting script](doc:create-an-accounting-script) guide for more information.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `AccountingScriptPost`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `entry_type_id` | integer | yes | Related entry type ID | format: "int64" |
| `event_type_id` | integer | yes | Related event type ID | format: "int64" |
| `credit_accounting_account_id` | integer | yes | Accounting account ID assigned as credit account | format: "int64" |
| `debit_accounting_account_id` | integer | yes | Accounting account ID assigned as debit account | format: "int64" |
| `program_id` | integer | yes | Related program ID | format: "int64" |
| `cost_center` | object (schema `CostCenter`) | no |  | example: {"debit_org": "999999", "credit_org": "999999", "debit_cost": "999999", "credit_cost": "999999", "deactivated_at": "2021-10-10T10:10:00.000Z"} |
| `entry_name` | string | no | Base entry ID. If not provided, defaults to 'amount'.<br>* `amount`: Principal amount of the transaction on the event date. It usually represents the gross value of the operation associated with the corresponding flow/`entry_type`.<br>* `amount-advancement`: Principal amount of the advance (excluding interest/charges), that is, the principal being advanced (for example, installment agreement advance, invoice advance, receivables advance).<br>* `amount-advancement-dueDate`: Principal amount of the advance, posted on the due date of the cycle to which the transaction was advanced.<br>* `amount-advancement-shift`: Principal amount of the advance using the “shift” API (date change / flow adjustment), for example advance of an installment or invoice where there is a replacement/change of the original flow. Used to represent the principal of the installment/amount that is being moved from a future date to a present date through an advance.<br>* `amount-advancement-shift-dueDate`: Same concept as `amount-advancement-shift`, but related to the due date. It represents the principal of the advance associated with the original due date of the obligation that was “shifted” (moved/adjusted) by the advance process.<br>* `amount-anticipation`: This amount name is deprecated. Standard routings that were eventually created with it are deprecated and have corresponding routings with `-advancement` amount values.<br>* `amount-cancelment-anticipation`: This amount name is deprecated. Standard routings that were created with it are deprecated and have corresponding routings with `-advancement` amount values.<br>* `amount-clearing`: Amount used exclusively for configuring the posting of the installment principal (without interest) upon the clearing arrival of each installment.<br>* `amount-contract`: This amount name is deprecated. Standard routings that were created with it are deprecated and have corresponding routings with `amount` values.<br>* `amount-dueDate`: Principal amount of the transaction related to the due date (for example, an installment or invoice that is due). Used when the amount to be posted is linked to a specific due date, even if the event occurs before that date. It represents the due date posting of the `amount`.<br>* `amount-dueDate-cancelment`: This amount name is deprecated.<br>* `amount-reversal`: This amount name is deprecated and has no corresponding movement, as there are no mapped usage scenarios for it.<br>* `contractAmount`: This amount is deprecated. The transactions for which it may be configured are transactions 608 and 612. If it is currently used, the recommendation is to create routings with `amount`, which will return the total transaction value. Used as a reference for the total obligation assumed at the time of contracting.<br>* `daily-interest`: Amount of daily interest calculated for a period (for example, between two specific dates), usually used in scenarios such as pro-rata interest calculation.<br>* `fine`: Fine amount included in a payment (amount that is discharged). This type should only be used when linked to transaction 201 (payment). When used, it provides details of how much of that payment corresponds to the fine.<br>* `interest`: Amount of interest calculated/incurred on the transaction, whether it is a contract transaction or an installment. Important: this should only be used if the interest is included together with the transaction's total amount, so that the `interest` is explicitly identified as such. If the interest is already in a separate transaction, `amount` should be used instead.<br>* `interest-advancement`: Interest amount related to the advance operation, for example, interest amount of an advanced installment.<br>* `interest-advancement-dueDate`: Interest amount of the advance, posted on the due date of the cycle to which the transaction was advanced.<br>* `interest-anticipation`: This amount name is deprecated. Standard routings that were created with it are deprecated and have corresponding routings with `-advancement` amount values.<br>* `interest-dueDate`: Interest amount of an operation at the due date. The usage logic is the same as for `interest`, but in this case the posting occurs on the due date.<br>* `interest-not-appropriated`: Amount exclusively used for posting interest from transaction 706 (invoice installment cancellation). It obtains the interest amount to be posted from the original contracting transaction.<br>* `interest-partial`: This amount name is deprecated and has been replaced by `daily-interest`.<br>* `iof`: IOF amount (financial transactions tax) associated with the event operation. As with interest, the same logic applies: if the IOF is already in a specific and separate transaction, this option should not be used, and `amount` is the correct option.<br>* `iof-dueDate`: IOF amount (financial transactions tax) associated with the event operation. As with interest, the same logic applies: if the IOF is already in a specific and separate transaction, this option should not be used, and `amount`` is the correct option. This due-date option posts the value on the due date of the invoice that contains the transaction.<br>* `overdue`: Late interest (penalty interest) amount included in a payment (amount that is discharged). This type should only be used when linked to transaction 201 (payment). When used, it provides details of how much of that payment corresponds to late interest.<br> | enum: ["amount", "amount-advancement", "amount-advancement-dueDate", "amount-advancement-shift", "amount-advancement-shift-dueDate", "amount-anticipation", "amount-cancelment-anticipation", "amount-clearing", "amount-clearing-without-match", "amount-contract", "amount-dueDate", "amount-dueDate-cancelment", "amount-interest-iof", "amount-interest-iof-dueDate", "amount-principal", "amount-reversal", "contractAmount", "daily-interest", "fine", "interest", "interest-advancement", "interest-advancement-dueDate", "interest-advancement-shift", "interest-advancement-shift-dueDate", "interest-anticipation", "interest-dueDate", "interest-not-appropriated", "interest-partial", "iof", "iof-dueDate", "overdue", "fine"]; default: "amount" |
| `processing_code` | string | no | Processint code. When the script is based on a processing code, this field is **REQUIRED**. | maxLength: 6 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | OK | `application/json`: object (schema `AccountingScript`) |
| 400 | Bad request — one or more parameters are invalid. Every 4xx body carries the descriptive<br>`error` string plus the `cid` correlation ID. Depending on the failure scenario, the body<br>may also carry `invalid_fields` (positive-integer aggregator) enumerating the offending<br>top-level fields. Refer to `AccountingScriptV1CreateError` for the full contract.<br> | `application/json`: object (schema `AccountingScriptV1CreateError`) |
| 409 | Accounting script already exists — the tuple (program_id, event_type_id, entry_type_id, entry_name) already has an active script for the tenant. |  |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credit_accounting` | object (schema `AccountingAccount`) | no |  | example: {"id": 1, "description": "SAMPLE ACCOUNT", "account": "123123132-x", "program_id": 12, "created_at": "2021-10-10T10:10:00.000Z"} |
| `cost_center` | object (schema `CostCenter`) | no |  | example: {"debit_org": "999999", "credit_org": "999999", "debit_cost": "999999", "credit_cost": "999999", "deactivated_at": "2021-10-10T10:10:00.000Z"} |
| `debit_accounting` | object (schema `AccountingAccount`) | no |  | example: {"id": 1, "description": "SAMPLE ACCOUNT", "account": "123123132-x", "program_id": 12, "created_at": "2021-10-10T10:10:00.000Z"} |
| `entry_name` | string | no | Base entry ID |  |
| `entry_type_id` | integer | no | Related entry type ID | format: "int64" |
| `event_type_id` | integer | no | Related event type ID | format: "int64" |
| `id` | integer | no | Account script ID | format: "int64" |
| `processing_code` | string | no | Processing code. When the script is based on a processing code, this field is **REQUIRED**. |  |
| `program_id` | integer | no | Related program ID | format: "int64" |

##### Response 400

400 Example `entryTypeNotFound` (Entry type not found for the tenant):

```json
{
  "error": "Validation error, entry Type doesn't exist: entry_type_id 300 not found for the tenant",
  "cid": "b0d4d7fb-1f38-4c3f-8b3b-8f4f0b2c1a20"
}
```

400 Example `invalidPositiveIDs` (One or more required IDs are non-positive):

```json
{
  "error": "the following fields must be positive integers greater than zero: entry_type_id, program_id",
  "invalid_fields": [
    "entry_type_id",
    "program_id"
  ],
  "cid": "c1e5b7f9-2a44-4b3d-9e1b-3f2a0c4d5e6f"
}
```

400 Example `debitAccountNotFound` (Debit accounting account not found for the tenant):

```json
{
  "error": "Validation error, debit account doesn't exist: debit_accounting_account_id 987 not found for the tenant",
  "cid": "d2f6c8a0-3b55-4c4e-af2c-4a3b1d5e6f70"
}
```

400 Example `invalidEntryName` (entry_name is not in the accepted allow-list):

```json
{
  "error": "Validation error, invalid entry name: accepted values: [amount, amount-advancement, ...]",
  "cid": "e3a7d9b1-4c66-4d5f-b03d-5b4c2e6f7081"
}
```

400 Example `tenantNotOnboarded` (Tenant has no accounting company configured):

```json
{
  "error": "Validation error, invalid company: onboard the tenant via /v1/accounting-companies before creating accounting scripts",
  "cid": "f4b8eac2-5d77-4e60-c14e-6c5d3f708192"
}
```

400 Example `jsonTypeMismatch` (A field was sent with the wrong JSON type (see V1BindTypeMismatchError)):

```json
{
  "error": "field 'debit_accounting_account_id' must be of type integer number (unquoted) but received a string value",
  "invalid_field": "debit_accounting_account_id",
  "cid": "6fdd31b0-c5b9-911a-a713-10158c1fd6ea"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`, `KU-CORE-create-an-accounting-script`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=PATCH path=/v1/accounting-scripts/batch operationId=BatchUpdateAccountingScript -->
### `PATCH /v1/accounting-scripts/batch` — Update accounting scripts V1

- **operationId:** `BatchUpdateAccountingScript`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V1`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update accounting scripts.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `BatchAccountingScriptPatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `operations` | array of object | no |  |  |
| `operations[].accounting_script_id` | integer | no | Accounting script ID | format: "int64" |
| `operations[].set` | object (schema `AccountingScriptPatch`) | no | Fields to update on an accounting script. At least one recognized field with a non-zero/non-empty value MUST be provided; otherwise the API returns 400 with `ErrNoChangesProvided` (PISMO-376794 silent-clone guard).<br>Unknown JSON fields are silently ignored by the decoder, so a body composed exclusively of unknown fields is treated as "no changes provided".<br> |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (map of object) (schema `AccountingScriptPatchResponse`) |
| 400 | Bad request — validation failure, any operation error other than not-found/deactivated,<br>or no changes provided in any operation payload (PISMO-376794). When the body itself fails<br>to deserialize because a field was sent with the wrong JSON type, the response is the<br>shared `V1BindTypeMismatchError` shape (`error`, `cid`, `invalid_field`) instead of the<br>per-item map below.<br> | `application/json`: object (map of object) (schema `AccountingScriptPatchResponse`) |
| 404 | Every failing operation targets a missing or deactivated accounting script | `application/json`: object (map of object) (schema `AccountingScriptPatchResponse`) |
| 500 | Internal server error (client receives generic "something went wrong") |  |

##### Response 200

**200 `application/json` body fields:**

_No fields declared in the schema._

200 Example `example`:

```json
{
  "393028": {
    "has_error": false,
    "new_id": 403948
  }
}
```

##### Response 400

400 Example `example`:

```json
{
  "393028": {
    "has_error": true,
    "error_message": "Debit account not found"
  }
}
```

##### Response 404

404 Example `example`:

```json
{
  "393028": {
    "has_error": true,
    "error_message": "Accounting Script doesn't exist, impossible to update"
  }
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=GET path=/v1/accounting-scripts/{accountingScriptId} operationId=GetAccountingScriptById -->
### `GET /v1/accounting-scripts/{accountingScriptId}` — Get accounting script V1

- **operationId:** `GetAccountingScriptById`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V1`
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
| 200 | OK | `application/json`: object (schema `AccountingScript`) |
| 404 | Accounting script not found |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credit_accounting` | object (schema `AccountingAccount`) | no |  | example: {"id": 1, "description": "SAMPLE ACCOUNT", "account": "123123132-x", "program_id": 12, "created_at": "2021-10-10T10:10:00.000Z"} |
| `cost_center` | object (schema `CostCenter`) | no |  | example: {"debit_org": "999999", "credit_org": "999999", "debit_cost": "999999", "credit_cost": "999999", "deactivated_at": "2021-10-10T10:10:00.000Z"} |
| `debit_accounting` | object (schema `AccountingAccount`) | no |  | example: {"id": 1, "description": "SAMPLE ACCOUNT", "account": "123123132-x", "program_id": 12, "created_at": "2021-10-10T10:10:00.000Z"} |
| `entry_name` | string | no | Base entry ID |  |
| `entry_type_id` | integer | no | Related entry type ID | format: "int64" |
| `event_type_id` | integer | no | Related event type ID | format: "int64" |
| `id` | integer | no | Account script ID | format: "int64" |
| `processing_code` | string | no | Processing code. When the script is based on a processing code, this field is **REQUIRED**. |  |
| `program_id` | integer | no | Related program ID | format: "int64" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `False`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-CORE-accounting-accounts-and-entries`, `KU-CORE-accounting-overview`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=DELETE path=/v1/accounting-scripts/{accountingScriptId} operationId=DeactivateAccountingScript -->
### `DELETE /v1/accounting-scripts/{accountingScriptId}` — Deactivate accounting script V1

- **operationId:** `DeactivateAccountingScript`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V1`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Deactivate an accounting script by its ID.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountingScriptId` | path | yes | integer | Numeric ID of the accounting script. | format: "int64" |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | Ok | `application/json`: object (schema `AccountingScript`) |
| 404 | Accounting script not found |  |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credit_accounting` | object (schema `AccountingAccount`) | no |  | example: {"id": 1, "description": "SAMPLE ACCOUNT", "account": "123123132-x", "program_id": 12, "created_at": "2021-10-10T10:10:00.000Z"} |
| `cost_center` | object (schema `CostCenter`) | no |  | example: {"debit_org": "999999", "credit_org": "999999", "debit_cost": "999999", "credit_cost": "999999", "deactivated_at": "2021-10-10T10:10:00.000Z"} |
| `debit_accounting` | object (schema `AccountingAccount`) | no |  | example: {"id": 1, "description": "SAMPLE ACCOUNT", "account": "123123132-x", "program_id": 12, "created_at": "2021-10-10T10:10:00.000Z"} |
| `entry_name` | string | no | Base entry ID |  |
| `entry_type_id` | integer | no | Related entry type ID | format: "int64" |
| `event_type_id` | integer | no | Related event type ID | format: "int64" |
| `id` | integer | no | Account script ID | format: "int64" |
| `processing_code` | string | no | Processing code. When the script is based on a processing code, this field is **REQUIRED**. |  |
| `program_id` | integer | no | Related program ID | format: "int64" |


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;404`, has examples `False`, emits events `0`, deprecated `False`.

<!-- op: spec=api-specs/Core_platform_-_Accounting.yaml method=PATCH path=/v1/accounting-scripts/{accountingScriptId} operationId=UpdateAccountingScript -->
### `PATCH /v1/accounting-scripts/{accountingScriptId}` — Update accounting script V1

- **operationId:** `UpdateAccountingScript`
- **Specification:** `api-specs/Core_platform_-_Accounting.yaml` (Core platform - Accounting)
- **Server base URL(s):** `https://sandbox.pismolabs.io/accounting`
- **Tags:** `Accounting scripts V1`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update accounting script.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `accountingScriptId` | path | yes | integer | Accounting script ID | format: "int64" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `AccountingScriptPatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `debit_accounting_account_id` | integer | no | Debit accounting account ID | format: "int64" |
| `credit_accounting_account_id` | integer | no | Credit accounting account ID | format: "int64" |
| `debit_cost` | string | no | Debit cost center |  |
| `credit_cost` | string | no | Credit cost center |  |
| `entry_name` | string | no | New entry name (e.g., "amount", "interest", "iof"). Must match the allow-list from `POST /v1/accounting-scripts`. |  |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `AccountingScriptSinglePatchResponse`) |
| 400 | Bad request — validation failure (invalid entry name, missing/deactivated debit or credit<br>account, invalid company, or no changes provided in the payload — PISMO-376794). A JSON<br>field type mismatch in the body returns the shared `V1BindTypeMismatchError` shape<br>(`error`, `cid`, `invalid_field`).<br> | `application/json`: no schema |
| 404 | Accounting Script not found or already deactivated | `application/json`: no schema |
| 500 | Internal server error (client receives generic "something went wrong") | `application/json`: no schema |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `new_id` | integer | no | Unique identifier of the newly created accounting script. (The old one will be deactivated) | format: "int64" |

200 Example `example`:

```json
{
  "new_id": 403948
}
```

##### Response 400

400 Example `validation` (Validation failure):

```json
{
  "message": "Validation error, credit account doesn't exist: account not found"
}
```

400 Example `jsonTypeMismatch` (A field was sent with the wrong JSON type (see V1BindTypeMismatchError)):

```json
{
  "error": "field 'credit_accounting_account_id' must be of type integer number (unquoted) but received a string value",
  "invalid_field": "credit_accounting_account_id",
  "cid": "6fdd31b0-c5b9-911a-a713-10158c1fd6ea"
}
```

##### Response 404

404 Example `example`:

```json
{
  "message": "Accounting Script doesn't exist, impossible to update"
}
```

##### Response 500

500 Example `example`:

```json
{
  "message": "something went wrong"
}
```


Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;404;500`, has examples `True`, emits events `0`, deprecated `False`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/AccountingScript -->
### Schema `AccountingScript`

Pointer: `#/components/schemas/AccountingScript`. Type: object (schema `AccountingScript`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `credit_accounting` | object (schema `AccountingAccount`) | no |  | example: {"id": 1, "description": "SAMPLE ACCOUNT", "account": "123123132-x", "program_id": 12, "created_at": "2021-10-10T10:10:00.000Z"} |
| `cost_center` | object (schema `CostCenter`) | no |  | example: {"debit_org": "999999", "credit_org": "999999", "debit_cost": "999999", "credit_cost": "999999", "deactivated_at": "2021-10-10T10:10:00.000Z"} |
| `debit_accounting` | object (schema `AccountingAccount`) | no |  | example: {"id": 1, "description": "SAMPLE ACCOUNT", "account": "123123132-x", "program_id": 12, "created_at": "2021-10-10T10:10:00.000Z"} |
| `entry_name` | string | no | Base entry ID |  |
| `entry_type_id` | integer | no | Related entry type ID | format: "int64" |
| `event_type_id` | integer | no | Related event type ID | format: "int64" |
| `id` | integer | no | Account script ID | format: "int64" |
| `processing_code` | string | no | Processing code. When the script is based on a processing code, this field is **REQUIRED**. |  |
| `program_id` | integer | no | Related program ID | format: "int64" |

<!-- schema: #/components/schemas/CostCenter -->
### Schema `CostCenter`

Pointer: `#/components/schemas/CostCenter`. Type: object (schema `CostCenter`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `debit_org` | string | yes | Number of your Org’s debit accounting account | maxLength: 50 |
| `credit_org` | string | yes | Number of your Org’s credit accounting account | maxLength: 50 |
| `debit_cost` | string | yes | Number of the cost center of the debit accounting account | maxLength: 50 |
| `credit_cost` | string | yes | Number of the cost center of the credit accounting account | maxLength: 50 |
| `deactivated_at` | string | no | Date and time when the cost center was deactivated (ISO 8601). Filled when the account is deactivated. | format: "date-time" |

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

<!-- schema: #/components/schemas/AccountingScriptV1CreateError -->
### Schema `AccountingScriptV1CreateError`

Pointer: `#/components/schemas/AccountingScriptV1CreateError`. Type: object (schema `AccountingScriptV1CreateError`).

> V1 error response for `POST /v1/accounting-scripts`.
> The `error` field carries a **descriptive** message: it wraps a stable sentinel prefix with a
> contextual detail that always includes the offending **numeric ID** (`program_id`,
> `event_type_id`, `entry_type_id`, `debit_accounting_account_id`,
> `credit_accounting_account_id`) or the offending **field name** (`entry_name`, `cost_center.*`,
> `debit_account.account`, etc.) so the caller can self-serve the fix.
> User-supplied **string values** (account numbers, cosif, descriptions, tenant identifiers) are
> **never echoed back** — they remain in server-side logs and can be correlated with the `cid`
> field also echoed in every 4xx/5xx response body. When a scenario names multiple offenders,
> the additional structured field `invalid_fields` accompanies the `error` string.
> When the request body fails to deserialize because a field was sent with the **wrong JSON
> type** (e.g. a numeric ID sent as a quoted string), the `error` names the offending field and
> the expected/received JSON type and the singular `invalid_field` key carries that field name
> (see `V1BindTypeMismatchError`, which describes the same shape shared across all V1 JSON body
> endpoints).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `error` | string | no | Descriptive error message wrapping a sentinel prefix and a contextual detail. Examples:<br>  - `the following fields must be positive integers greater than zero: entry_type_id, program_id`<br>  - `Validation error, entry Type doesn't exist: entry_type_id 300 not found for the tenant`<br>  - `Validation error, invalid programId: program_id 42 not found for the tenant`<br>  - `Validation error, debit account doesn't exist: debit_accounting_account_id 987 not found for the tenant`<br>  - `Validation error, credit account doesn't exist: credit_accounting_account_id 987 is deactivated for the tenant`<br>  - `Validation error, invalid entry name: accepted values: [amount, amount-advancement, ...]`<br>  - `Validation error, invalid company: onboard the tenant via /v1/accounting-companies before creating accounting scripts`<br>  - `Accounting Script already exists`<br> | example: "Validation error, entry Type doesn't exist: entry_type_id 300 not found for the tenant" |
| `cid` | string | no | Correlation ID echoed in every 4xx/5xx response body so support can locate the offending user-supplied strings in server-side logs. |  |
| `invalid_fields` | array of string | no | Present on the positive-integer aggregator branch of `POST /v1/accounting-scripts`.<br>Enumerates every top-level field that violated the "must be a positive integer greater<br>than zero" rule, so the caller can fix them all in a single retry.<br> | example: ["entry_type_id", "program_id"] |
| `invalid_field` | string | no | Present when the request body could not be deserialized because a field was sent with the<br>wrong JSON type (a `*json.UnmarshalTypeError`). Carries the JSON path of the offending<br>field. See `V1BindTypeMismatchError`.<br> | example: "credit_accounting_account_id" |

<!-- schema: #/components/schemas/AccountingScriptPatch -->
### Schema `AccountingScriptPatch`

Pointer: `#/components/schemas/AccountingScriptPatch`. Type: object (schema `AccountingScriptPatch`).

> Fields to update on an accounting script. At least one recognized field with a non-zero/non-empty value MUST be provided; otherwise the API returns 400 with `ErrNoChangesProvided` (PISMO-376794 silent-clone guard).
> Unknown JSON fields are silently ignored by the decoder, so a body composed exclusively of unknown fields is treated as "no changes provided".

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `debit_accounting_account_id` | integer | no | Debit accounting account ID | format: "int64" |
| `credit_accounting_account_id` | integer | no | Credit accounting account ID | format: "int64" |
| `debit_cost` | string | no | Debit cost center |  |
| `credit_cost` | string | no | Credit cost center |  |
| `entry_name` | string | no | New entry name (e.g., "amount", "interest", "iof"). Must match the allow-list from `POST /v1/accounting-scripts`. |  |

<!-- schema: #/components/schemas/AccountingScriptPatchResponse -->
### Schema `AccountingScriptPatchResponse`

Pointer: `#/components/schemas/AccountingScriptPatchResponse`. Type: object (map of object) (schema `AccountingScriptPatchResponse`).

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Accounting.yaml` | tag `Accounting scripts V1`: GET /v1/accounting-scripts, POST /v1/accounting-scripts, PATCH /v1/accounting-scripts/batch, GET /v1/accounting-scripts/{accountingScriptId}, DELETE /v1/accounting-scripts/{accountingScriptId}, PATCH /v1/accounting-scripts/{accountingScriptId} | https://github.com/PismoDevEx/pismo-api-specs | `f0272a891eaca0fe…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-CORE-accounting-accounts-and-entries` — Creating accounting accounts and accounting entries
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-CORE-create-an-accounting-script` — Create accounting scripts
