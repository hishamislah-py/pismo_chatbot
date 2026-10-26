---
ku_id: KU-API-core-platform-transactions--transaction-flows
title: 'API reference: Core platform - Transactions — Transaction flows'
category: api_reference
ku_type: api_reference
lifecycle: current
sources:
- path: api-specs/Core_platform_-_Transactions.yaml
  sha256: 203c22b2f02c342bb5bfee34c8d991ae771dbff84a92772890e033042b03ce31
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
- SearchTransactionFlows
- PostTransactionFlow
- PatchTransactionFlow
related_kus:
- KU-BANK-penalties-for-cd-accounts
- KU-CORE-processing-codes-and-transaction-types
- KU-CRED-agreements
- KU-ERR-codes-esmg-to-whis
- KU-ERR-codes-wtrc
- KU-GS-program-types
- KU-PAY-installments-payment
- KU-PAY-payments-configurations
specification_version: 1.0.0
---

# API reference: Core platform - Transactions — Transaction flows

**KU ID:** `KU-API-core-platform-transactions--transaction-flows` · **Category:** API reference · **Type:** operation contracts · **Status:** current specification

## Purpose and scope

Contracts of 3 operation(s) tagged `Transaction flows` in `api-specs/Core_platform_-_Transactions.yaml` (“Core platform - Transactions”, version `1.0.0`), generated from the OpenAPI document. Methods, paths, operationIds, parameters, request and response fields, required flags, types, enums, defaults and constraints are taken from the specification; examples are shown only where the specification contains a concrete example value.

Tag description (from the specification):

> Endpoints to manage the link between transaction types and processing codes.

## Operations in this unit

| Method and path | operationId | Summary | Deprecated |
| --- | --- | --- | --- |
| `GET /v1/transaction-flow` | `SearchTransactionFlows` | List transaction flows | no |
| `POST /v1/transaction-flow` | `PostTransactionFlow` | Create transaction flow | no |
| `PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId}` | `PatchTransactionFlow` | Update transaction flow | no |

## Authentication

- `BearerAuth`: {"type": "http", "scheme": "bearer", "bearerFormat": "JWT"} — Account access token. Tokens can expire quickly, which can result in an "Unauthorized" error.

## Operation contracts

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=GET path=/v1/transaction-flow operationId=SearchTransactionFlows -->
### `GET /v1/transaction-flow` — List transaction flows

- **operationId:** `SearchTransactionFlows`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transaction flows`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> List transaction flow configurations that link transaction types and processing codes.
>
> See [Processing codes and transaction types](doc:processing-codes-and-transaction-types) and [Payments configurations](doc:payments-configurations) for information on processing codes and transaction types, how to create them, and map them to each other.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | query | no | string | Processing code filter |  |
| `transactionTypeId` | query | no | integer | Transaction type ID filter. | format: "int64"; example: 101010 |
| `pageSize` | query | no | integer | Maximum number of items per page. If not provided, defaults to 100. Must be between 1 and 1000. | default: 100; minimum: 1; maximum: 1000 |
| `pageOffset` | query | no | integer | Page offset. Indicates which page to start with when returning the results. Defaults to 0. Must be between 0 and 5000. | default: 0; minimum: 0; maximum: 5000 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `has_next` | boolean | no | Indicates whether there are more pages after the current page |  |
| `items` | array of array of object (schema `TransactionFlow`) | no |  |  |

##### Response 400

400 Example `invalidFilterValue` (Invalid filter value):

```json
{
  "message": "Invalid filter value",
  "error": "Invalid filter value",
  "code": "WTRC00001"
}
```

400 Example `invalidPageSizeExceedsMax` (Page size exceeds maximum):

```json
{
  "message": "pageSize must not exceed 1000",
  "error": "pageSize must not exceed 1000",
  "code": "WTRC00001"
}
```

400 Example `invalidPageSizeNotPositive` (Page size must be positive):

```json
{
  "message": "pageSize must be greater than 0",
  "error": "pageSize must be greater than 0",
  "code": "WTRC00001"
}
```

400 Example `invalidPageSizeNotInteger` (Page size not an integer):

```json
{
  "message": "pageSize should be an integer value",
  "error": "pageSize should be an integer value",
  "code": "WTRC00001"
}
```

400 Example `invalidPageOffsetNegative` (Page offset must not be negative):

```json
{
  "message": "pageOffset must not be negative",
  "error": "pageOffset must not be negative",
  "code": "WTRC00001"
}
```

400 Example `invalidPageOffsetNotInteger` (Page offset not an integer):

```json
{
  "message": "pageOffset should be an integer value",
  "error": "pageOffset should be an integer value",
  "code": "WTRC00001"
}
```

400 Example `invalidPageOffsetExceedsMax` (Page offset exceeds maximum):

```json
{
  "message": "pageOffset must not exceed 5000",
  "error": "pageOffset must not exceed 5000",
  "code": "WTRC00001"
}
```

##### Response 500

500 Example `internalProcessingError` (Internal processing error):

```json
{
  "message": "Internal processing error",
  "error": "Internal processing error",
  "code": "ETRC00001"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WTRC00001` | Invalid filter value |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-payments-configurations`.

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=POST path=/v1/transaction-flow operationId=PostTransactionFlow -->
### `POST /v1/transaction-flow` — Create transaction flow

- **operationId:** `PostTransactionFlow`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transaction flows`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Creates a configuration linking a transaction type with a processing code.
>
> See [Processing codes and transaction types](doc:processing-codes-and-transaction-types) and [Payments configurations](doc:payments-configurations) for information on processing codes and transaction types, how to create them, and map them to each other.

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `TransactionFlowPost`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeId`) | yes | Transaction type ID. Certain IDs are reserved by the platform and cannot be used. | format: "int64"; minimum: 1 |
| `processing_code` | string | yes | Processing code that issues the transaction type. | maxLength: 6 |
| `key` | string | yes | The relation key that links transaction type and processing code.<br><br>* `PRINCIPAL` uses principal amount.<br>* `INSTALLMENT` uses installment amount.<br>* `CONTRACT` uses contract amount.<br>* `OTHER` uses any custom amount, such as fees, taxes, or other charges. When the key is OTHER, you must define the `custom_key` value.<br> | enum: ["PRINCIPAL", "INSTALLMENT", "CONTRACT", "OTHER"] |
| `custom_key` | string | no | The customized relation between transaction type and processing code. This field is tied to the type or ID of a custom fee model that configures fees, taxes, or other charges. REQUIRED if the key is OTHER. | maxLength: 200 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 201 | Created | `application/json`: object (schema `TransactionFlowPost`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 201

**201 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeId`) | yes | Transaction type ID. Certain IDs are reserved by the platform and cannot be used. | format: "int64"; minimum: 1 |
| `processing_code` | string | yes | Processing code that issues the transaction type. | maxLength: 6 |
| `key` | string | yes | The relation key that links transaction type and processing code.<br><br>* `PRINCIPAL` uses principal amount.<br>* `INSTALLMENT` uses installment amount.<br>* `CONTRACT` uses contract amount.<br>* `OTHER` uses any custom amount, such as fees, taxes, or other charges. When the key is OTHER, you must define the `custom_key` value.<br> | enum: ["PRINCIPAL", "INSTALLMENT", "CONTRACT", "OTHER"] |
| `custom_key` | string | no | The customized relation between transaction type and processing code. This field is tied to the type or ID of a custom fee model that configures fees, taxes, or other charges. REQUIRED if the key is OTHER. | maxLength: 200 |

##### Response 400

400 Example `invalidRequestParameters` (Invalid request parameters):

```json
{
  "message": "Invalid request parameters",
  "error": "Invalid request parameters",
  "code": "WTRC00003"
}
```

400 Example `invalidRequestBody` (Invalid request body):

```json
{
  "message": "Invalid request body",
  "error": "Invalid request body",
  "code": "WTRC00005"
}
```

400 Example `invalidKey` (Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER):

```json
{
  "message": "Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER",
  "error": "Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER",
  "code": "WTRC04003"
}
```

400 Example `mandatoryCustomKey` (Custom key is mandatory when key is OTHER):

```json
{
  "message": "custom_key is mandatory when key is OTHER",
  "error": "custom_key is mandatory when key is OTHER",
  "code": "WTRC04004"
}
```

400 Example `emptyCustomKey` (Custom key should not be empty when key is OTHER):

```json
{
  "message": "custom_key should not be empty when key is OTHER",
  "error": "custom_key should not be empty when key is OTHER",
  "code": "WTRC04005"
}
```

400 Example `invalidCustomKey` (Custom key should only be provided when key is OTHER):

```json
{
  "message": "custom_key should only be provided when key is OTHER",
  "error": "custom_key should only be provided when key is OTHER",
  "code": "WTRC04006"
}
```

400 Example `ttDoesntExist` (Transaction type doesn't exist):

```json
{
  "message": "Transaction type doesn't exist",
  "error": "Transaction type doesn't exist",
  "code": "WTRC05003"
}
```

400 Example `pcDoesntExist` (Processing code doesn't exist):

```json
{
  "message": "Processing code doesn't exist",
  "error": "Processing code doesn't exist",
  "code": "WTRC07001"
}
```

##### Response 409

409 Example `invalidRequestParameters` (Relationship between transaction type and processing code already exists):

```json
{
  "message": "Relationship between transaction type and processing code already exists",
  "error": "Relationship between transaction type and processing code already exists",
  "code": "WTRC04001"
}
```

409 Example `amountTypeAlreadyConfigured` (The provided amount type is already configured for the processing code):

```json
{
  "message": "The provided amount type is already configured for the processing code",
  "error": "The provided amount type is already configured for the processing code",
  "code": "ETRC04003"
}
```

409 Example `transactionTypeAlreadyConfigured` (The provided transaction type is already configured for the processing code):

```json
{
  "message": "The provided transaction type is already configured for the processing code",
  "error": "The provided transaction type is already configured for the processing code",
  "code": "ETRC04004"
}
```

409 Example `amountTypeConflicts` (The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract):

```json
{
  "message": "The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract",
  "error": "The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract",
  "code": "ETRC04005"
}
```

409 Example `isCreditBalanceImpactConflicts` (Transaction Type isCredit does not correspond to the processing code balance impact):

```json
{
  "message": "Transaction Type isCredit does not correspond to the processing code balance impact",
  "error": "Transaction Type isCredit does not correspond to the processing code balance impact",
  "code": "ETRC04006"
}
```

409 Example `ttReservedByPlatform` (Transaction type ID is reserved by platform):

```json
{
  "message": "The provided transaction_type_id is reserved by the platform and cannot be used",
  "error": "The provided transaction_type_id is reserved by the platform and cannot be used",
  "code": "WTRC08001"
}
```

##### Response 500

500 Example `internalProcessingError` (Internal processing error):

```json
{
  "message": "Internal processing error",
  "error": "Internal processing error",
  "code": "ETRC00001"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WTRC00003` | Invalid request parameters |
| 400 | `WTRC00005` | Invalid request body |
| 400 | `WTRC04003` | Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER |
| 400 | `WTRC04004` | custom_key is mandatory when key is OTHER |
| 400 | `WTRC04005` | custom_key should not be empty when key is OTHER |
| 400 | `WTRC04006` | custom_key should only be provided when key is OTHER |
| 400 | `WTRC05003` | Transaction type doesn't exist |
| 400 | `WTRC07001` | Processing code doesn't exist |
| 409 | `WTRC04001` | Relationship between transaction type and processing code already exists |
| 409 | `ETRC04003` | The provided amount type is already configured for the processing code |
| 409 | `ETRC04004` | The provided transaction type is already configured for the processing code |
| 409 | `ETRC04005` | The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract |
| 409 | `ETRC04006` | Transaction Type isCredit does not correspond to the processing code balance impact |
| 409 | `WTRC08001` | The provided transaction_type_id is reserved by the platform and cannot be used |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `201;400;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-BANK-penalties-for-cd-accounts`, `KU-CORE-processing-codes-and-transaction-types`, `KU-CRED-agreements`, `KU-GS-program-types`, `KU-PAY-installments-payment`, `KU-PAY-payments-configurations`.

<!-- op: spec=api-specs/Core_platform_-_Transactions.yaml method=PATCH path=/v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId} operationId=PatchTransactionFlow -->
### `PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId}` — Update transaction flow

- **operationId:** `PatchTransactionFlow`
- **Specification:** `api-specs/Core_platform_-_Transactions.yaml` (Core platform - Transactions)
- **Server base URL(s):** `https://sandbox.pismolabs.io/transactions-core`
- **Tags:** `Transaction flows`
- **Deprecated in specification:** no
- **Security requirement:** `BearerAuth`

**Description (from the specification):**

> Update `key` or `custom_key` for the relation between processing code and transaction type ID. You can only use this endpoint to update a transaction flow that is already created.

#### Parameters

| Name | In | Required | Type | Description | Constraints |
| --- | --- | --- | --- | --- | --- |
| `processingCode` | path | yes | string | Processing code for an existing transaction flow, given the transaction type ID. |  |
| `transactionTypeId` | path | yes | integer | Transaction type ID related to the processing code. | format: "int64" |

#### Request body

Required: no

**Content type `application/json`** — schema: object (schema `TransactionFlowPatch`)

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `key` | string | yes | Sets the relation key that links transaction type and processing code.<br><br>* `PRINCIPAL` uses principal amount.<br>* `INSTALLMENT` uses installment amount.<br>* `CONTRACT` uses contract amount.<br>* `OTHER` uses any custom amount, such as fees, taxes, or other charges. When the key is OTHER, you must define the `custom_key` value.<br> | enum: ["PRINCIPAL", "INSTALLMENT", "CONTRACT", "OTHER"] |
| `custom_key` | string | no | Sets a customized relation between transaction type and processing code. This field is tied to the type or ID of a custom fee model that configures fees, taxes, or other charges. REQUIRED if the key is OTHER. | maxLength: 200 |

#### Responses

| Status | Description | Body |
| --- | --- | --- |
| 200 | OK | `application/json`: object (schema `TransactionFlowPost`) |
| 400 | Bad request | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 409 | Conflict | `application/json`: oneOf: object (schema `ErrorResponse`) |
| 500 | Internal error | `application/json`: oneOf: object (schema `ErrorResponse`) |

##### Response 200

**200 `application/json` body fields:**

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `transaction_type_id` | integer (schema `TransactionTypeId`) | yes | Transaction type ID. Certain IDs are reserved by the platform and cannot be used. | format: "int64"; minimum: 1 |
| `processing_code` | string | yes | Processing code that issues the transaction type. | maxLength: 6 |
| `key` | string | yes | The relation key that links transaction type and processing code.<br><br>* `PRINCIPAL` uses principal amount.<br>* `INSTALLMENT` uses installment amount.<br>* `CONTRACT` uses contract amount.<br>* `OTHER` uses any custom amount, such as fees, taxes, or other charges. When the key is OTHER, you must define the `custom_key` value.<br> | enum: ["PRINCIPAL", "INSTALLMENT", "CONTRACT", "OTHER"] |
| `custom_key` | string | no | The customized relation between transaction type and processing code. This field is tied to the type or ID of a custom fee model that configures fees, taxes, or other charges. REQUIRED if the key is OTHER. | maxLength: 200 |

##### Response 400

400 Example `invalidRequestBody` (Invalid request body):

```json
{
  "message": "Invalid request body",
  "error": "Invalid request body",
  "code": "WTRC00005"
}
```

400 Example `ttIsNotANumber` (Transaction type ID is not a number):

```json
{
  "message": "Transaction type ID is not a number",
  "error": "Transaction type ID is not a number",
  "code": "WTRC05007"
}
```

400 Example `invalidKey` (Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER):

```json
{
  "message": "Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER",
  "error": "Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER",
  "code": "WTRC04003"
}
```

400 Example `mandatoryCustomKey` (custom_key is mandatory when key is OTHER):

```json
{
  "message": "custom_key is mandatory when key is OTHER",
  "error": "custom_key is mandatory when key is OTHER",
  "code": "WTRC04004"
}
```

400 Example `invalidCustomKey` (custom_key should only be provided when key is OTHER):

```json
{
  "message": "custom_key should only be provided when key is OTHER",
  "error": "custom_key should only be provided when key is OTHER",
  "code": "WTRC04006"
}
```

400 Example `emptyCustomKey` (custom_key should not be empty when key is OTHER):

```json
{
  "message": "custom_key should not be empty when key is OTHER",
  "error": "custom_key should not be empty when key is OTHER",
  "code": "WTRC04005"
}
```

400 Example `ttDoesntExist` (Transaction type doesn't exist):

```json
{
  "message": "Transaction type doesn't exist",
  "error": "Transaction type doesn't exist",
  "code": "WTRC05003"
}
```

400 Example `tPostingDoesntExist` (The transaction flow mapping configuration between this processing code and transaction type doesn't exist):

```json
{
  "message": "The transaction flow mapping configuration between this processing code and transaction type doesn't exist",
  "error": "The transaction flow mapping configuration between this processing code and transaction type doesn't exist",
  "code": "WTRC04002"
}
```

##### Response 409

409 Example `amountTypeAlreadyConfigured` (The provided amount type is already configured for the processing code):

```json
{
  "message": "The provided amount type is already configured for the processing code",
  "error": "The provided amount type is already configured for the processing code",
  "code": "ETRC04003"
}
```

409 Example `transactionTypeAlreadyConfigured` (The provided transaction type is already configured for the processing code):

```json
{
  "message": "The provided transaction type is already configured for the processing code",
  "error": "The provided transaction type is already configured for the processing code",
  "code": "ETRC04004"
}
```

409 Example `amountTypeConflicts` (The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract):

```json
{
  "message": "The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract",
  "error": "The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract",
  "code": "ETRC04005"
}
```

409 Example `isCreditBalanceImpactConflicts` (Transaction Type isCredit does not correspond to the Processing Code balance impact):

```json
{
  "message": "Transaction Type isCredit does not correspond to the Processing Code balance impact",
  "error": "Transaction Type isCredit does not correspond to the Processing Code balance impact",
  "code": "ETRC04006"
}
```

##### Response 500

500 Example `internalProcessingError` (Internal processing error):

```json
{
  "message": "Internal processing error",
  "error": "Internal processing error",
  "code": "ETRC00001"
}
```


#### Error codes shown in this operation's response examples

| HTTP status | Code | Message |
| --- | --- | --- |
| 400 | `WTRC00005` | Invalid request body |
| 400 | `WTRC05007` | Transaction type ID is not a number |
| 400 | `WTRC04003` | Key should be PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER |
| 400 | `WTRC04004` | custom_key is mandatory when key is OTHER |
| 400 | `WTRC04006` | custom_key should only be provided when key is OTHER |
| 400 | `WTRC04005` | custom_key should not be empty when key is OTHER |
| 400 | `WTRC05003` | Transaction type doesn't exist |
| 400 | `WTRC04002` | The transaction flow mapping configuration between this processing code and transaction type doesn't exist |
| 409 | `ETRC04003` | The provided amount type is already configured for the processing code |
| 409 | `ETRC04004` | The provided transaction type is already configured for the processing code |
| 409 | `ETRC04005` | The provided amount type conflicts with an existing configured amount type for the processing code. Please select either Principal or Contract |
| 409 | `ETRC04006` | Transaction Type isCredit does not correspond to the Processing Code balance impact |
| 500 | `ETRC00001` | Internal processing error |

Catalogue row (api-reference-data/operations_catalog.csv): response codes `200;400;409;500`, has examples `True`, emits events `0`, deprecated `False`.

Guides that link to this operation: `KU-PAY-payments-configurations`.

## Schemas referenced

Each named schema used by the operations above is listed once, with nested named schemas.

<!-- schema: #/components/schemas/ErrorResponse -->
### Schema `ErrorResponse`

Pointer: `#/components/schemas/ErrorResponse`. Type: object (schema `ErrorResponse`).

| Field | Type | Required | Description | Constraints |
| --- | --- | --- | --- | --- |
| `message` | string | no | Error description. |  |
| `error` | string | no | Error description. |  |
| `code` | string | no | Code description. |  |

## Lifecycle status

- No operation in this unit is marked deprecated in the specification.

## Conflicts, caveats and evidence gaps

- Example JSON is re-serialised from the parsed YAML value (2-space indentation); values are unchanged, formatting may differ from the YAML text.
- Event payload fields are not documented in the corpus (event pages are not collected).

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `api-specs/Core_platform_-_Transactions.yaml` | tag `Transaction flows`: GET /v1/transaction-flow, POST /v1/transaction-flow, PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId} | https://github.com/PismoDevEx/pismo-api-specs | `203c22b2f02c342b…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/operations_catalog.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `b218bf75940b0c37…` | 2026-10-13T20:51:51+00:00 |
| `api-reference-data/request_response_examples.csv` | whole document | https://github.com/PismoDevEx/pismo-api-specs | `ac921f2e8d0d1545…` | 2026-10-13T20:51:51+00:00 |

## Related knowledge units

- `KU-BANK-penalties-for-cd-accounts` — Penalties and taxes for CD accounts
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CRED-agreements` — Agreements: compulsory, statement, installment and payment agreements
- `KU-ERR-codes-esmg-to-whis` — Error codes: ESMG to WHIS (30 prefixes)
- `KU-ERR-codes-wtrc` — Error codes: WTRC
- `KU-GS-program-types` — Program types
- `KU-PAY-installments-payment` — Installments payment
- `KU-PAY-payments-configurations` — Payments configurations
