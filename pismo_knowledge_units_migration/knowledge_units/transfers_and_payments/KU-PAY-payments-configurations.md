---
ku_id: KU-PAY-payments-configurations
title: Payments configurations
category: transfers_and_payments
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/payments-configurations.md
  sha256: 796fd4472b207011d5ee3468dc6f0d49b9ede710267c299f791b8ae5f87cbc4e
  url: https://developers.pismo.io/pismo-docs/docs/payments-configurations
  role: primary_guide
  updated_at: '2026-09-25T19:26:28.000Z'
operations:
- CreateProcessingCode
- PatchTransactionFlow
- PostSetupTransactionType
- PostTransactionFlow
- ProcessingCodeList
- ProcessingCodeUpdate
- SearchTransactionFlows
related_kus:
- KU-API-core-platform-transactions--transaction-flows
- KU-API-core-platform-transactions--transaction-types
- KU-API-platform-setup-orgs-operation--processing-codes
- KU-CORE-fee-models
- KU-CORE-processing-codes-and-transaction-types
- KU-CRED-full-balance-credit-program
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-PAY-hold-funds
grouping_rationale: single source page
---

# Payments configurations

**KU ID:** `KU-PAY-payments-configurations` · **Category:** Transfers and payments · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/payments-configurations.md`:

> The payments configuration API allows you to configure how the Pismo platform processes operations in the payments flows.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/payments-configurations.md`: Payments configurations; Processing code configurations; Create or update processing code; Create transaction type; Map processing code to transaction type; Map transaction type to program transaction category

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/payments-configurations.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/payments-configurations · updatedAt: 2026-09-25T19:26:28.000Z

<!-- source:begin path=docs/core-platform/payments-configurations.md part=0-end -->

# Payments configurations

The payments configuration API allows you to configure how the Pismo platform processes operations in the payments flows.

## Processing code configurations

A [processing code](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) is a custom alphanumeric identifier that defines how the Pismo platform handles a certain financial operation type. Every processing code is associated with at least one transaction type. To set up this relationship,  perform the following steps:

1. [Create or update processing code](https://developers.pismo.io/pismo-docs/docs/payments-configurations#create-or-update-processing-code).
2. [Create transaction type](https://developers.pismo.io/pismo-docs/docs/payments-configurations#create-transaction-type).
3. [Map processing code to transaction type](https://developers.pismo.io/pismo-docs/docs/payments-configurations#map-processing-code-to-transaction-type).\
   *If you plan to use the processing code in network transaction operations for a full balance credit program, an additional step is required:*
4. [Map transaction type to program transaction category](https://developers.pismo.io/pismo-docs/docs/payments-configurations#map-transaction-type-to-program-transaction-category).

### Create or update processing code

When configuring processing codes for your organization, you have the following options:

* Create one new processing code for a financial operation.
* Create two new related processing codes: one for a financial operation and another for its reversal.
* Update an existing processing code with another existing processing code that reverses this operation.

Use the [List processing codes](https://developers.pismo.io/pismo-docs/reference/processingcodelist) endpoint to list all processing codes defined for an organization. You can also filter this list by processing code or its description.

To create one processing code for a financial operation, use the [Create processing code](https://developers.pismo.io/pismo-docs/reference/createprocessingcode) endpoint and provide the required body parameters in the request.

| Field             | Description                                                                                                                        |
| :---------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| `processing_code` | Unique alphanumeric identifier.                                                                                                    |
| `description`     | Description for this operation.                                                                                                    |
| `balance_impact`  | Use **1** for credit/cash-in operations, **-1** for debit/cash-out operations, and **0** for operations that don't impact balance. |

If the processing code is going to be used to [hold funds](https://developers.pismo.io/pismo-docs/docs/hold-funds) on the account, set `operation_type` parameter to `HOLD_FUNDS`. By default, this value is `NORMAL` for all other types of processing codes.

To create two new related processing codes, use the \[Create processing code]\(ref: createprocessingcode) endpoint and, in addition to the required fields for the first processing code,  provide values in the optional `undo_processing_code` and `undo_description` fields to create the second processing code for this operation's reversal.

To update the existing processing code with the existing processing code that reverses this operation, use the [Update processing code](https://developers.pismo.io/pismo-docs/reference/processingcodeupdate) endpoint and provide the  `undo_processing_code` value. You should also mention this endpoint in the original processing code's `description`.

### Create transaction type

To create a transaction type, use the [Create transaction type](https://developers.pismo.io/pismo-docs/reference/postsetuptransactiontype) endpoint and provide the required body parameters in the request.

| Field                 | Description                                                                                                                           |
| :-------------------- | :------------------------------------------------------------------------------------------------------------------------------------ |
| `transaction_type_id` | Transaction type identifier with a value of **7000** or above. Values below 7000 are reserved for internal Pismo platform operations. |
| `description`         | Description for this transaction type.                                                                                                |
| `credit`              | Defines whether this transaction type is a credit (true) or debit (false) operation.                                                  |
| `posted_transaction`  | Indicates if transactions will be posted on statement (true) or not (false).                                                          |

### Map processing code to transaction type

Use the [List transaction flows](https://developers.pismo.io/pismo-docs/reference/searchtransactionflows) endpoint to list all transaction flow configurations that have been defined for your organization or filter them by processing code or transaction type ID. This is a convenient way to see mappings between processing codes and transaction types.

To map processing codes to transaction types, you need to create a new transaction flow configuration. A transaction flow is a separate object that maps a processing code to a  transaction type. Use the [Create transaction flow](https://developers.pismo.io/pismo-docs/reference/posttransactionflow) endpoint and provide the required body parameters.

| Field                 | Description                                                                                      |
| :-------------------- | :----------------------------------------------------------------------------------------------- |
| `transaction_type_id` | Transaction type identifier with a value of **7000** or above.                                   |
| `processing_code`     | Processing code identifier of the operation that should issue a transaction of this  type.       |
| `key`                 | Links transaction type and processing code by PRINCIPAL, INSTALLMENT, CONTRACT, or OTHER amount. |

If the `key` is OTHER, you must define the `custom_key` also. This `custom_key` field ties to the `type` or `id` of a custom [fee model](https://developers.pismo.io/pismo-docs/docs/fee-models).

In the following example, you create three requests to map processing code 00AB11 to three transaction types: 7001 that uses principal amount, 7002 that uses state tax, and 7003 that uses a custom fee.

```json
{
  	"transaction_type_id": 7001,
  	"processing_code": "00AB11",
  	"key": "PRINCIPAL"
	}
```

```json
{
    "transaction_type_id": 7002,
    "processing_code": "00AB11",
    "key": "OTHER",
    "custom_key": "state_tax"
}
```

```json
{
    "transaction_type_id": 7003,
    "processing_code": "00AB11",
    "key": "OTHER",
    "custom_key": "custom_fee"
}
```

To update the `key` or `custom_key`  of the existing transaction flow, use the [Update transaction flow](https://developers.pismo.io/pismo-docs/reference/patchtransactionflow) endpoint. You can only use this endpoint to update a transaction flow that has been created already.

### Map transaction type to program transaction category

In a [full balance credit program](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program), a cardholder uses their credit card to make purchases on their credit account, accumulating a debt that they are expected to pay off. Unpaid debt can result in the cardholder accumulating additional debt in the form of interest, late fees, refinancing charges, and so on. You configure these charges by mapping transaction types onto program transaction categories. For more information, refer to [Using configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#using-configurable-entities).
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /orgs-operation/v1/processing-codes` | `ProcessingCodeList` | List processing codes | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /orgs-operation/v1/processing-codes` | `CreateProcessingCode` | Create processing code | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `PATCH /orgs-operation/v1/processing-codes/{processingCode}` | `ProcessingCodeUpdate` | Update processing code | `api-specs/Platform_setup_-_Orgs_Operation.yaml` | no | KU-API-platform-setup-orgs-operation--processing-codes |
| `POST /v1/transaction-types` | `PostSetupTransactionType` | Create transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `GET /v1/transaction-flow` | `SearchTransactionFlows` | List transaction flows | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `POST /v1/transaction-flow` | `PostTransactionFlow` | Create transaction flow | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |
| `PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId}` | `PatchTransactionFlow` | Update transaction flow | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-flows |

### Operation essentials

- **`GET /orgs-operation/v1/processing-codes`** (`ProcessingCodeList`): security `S2SAuthentication`; required parameters none declared; required body fields none declared; response statuses 200, 400; error codes in examples none; events none listed.
- **`POST /orgs-operation/v1/processing-codes`** (`CreateProcessingCode`): security `S2SAuthentication`; required parameters none declared; required body fields `processing_code`, `balance_impact`, `description`, `reversal_processing_code`; response statuses 201, 400; error codes in examples none; events `orgs-operation-create-1`.
- **`PATCH /orgs-operation/v1/processing-codes/{processingCode}`** (`ProcessingCodeUpdate`): security `S2SAuthentication`; required parameters `processingCode` (path); required body fields none declared; response statuses 204, 400, 404; error codes in examples none; events `orgs-operation-update-1`.
- **`POST /v1/transaction-types`** (`PostSetupTransactionType`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `description`, `credit`, `posted_transaction`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05001`, `WTRC08001`, `ETRC00001`; events `transaction-types-creation-1`.
- **`GET /v1/transaction-flow`** (`SearchTransactionFlows`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `WTRC00001`, `ETRC00001`; events none listed.
- **`POST /v1/transaction-flow`** (`PostTransactionFlow`): security `BearerAuth`; required parameters none declared; required body fields `transaction_type_id`, `processing_code`, `key`; response statuses 201, 400, 409, 500; error codes in examples `WTRC00003`, `WTRC00005`, `WTRC04003`, `WTRC04004`, `WTRC04005`, `WTRC04006`, `WTRC05003`, `WTRC07001`, `WTRC04001`, `ETRC04003`, `ETRC04004`, `ETRC04005`, `ETRC04006`, `WTRC08001`, `ETRC00001`; events none listed.
- **`PATCH /v1/transaction-flow/processing-code/{processingCode}/transaction-type/{transactionTypeId}`** (`PatchTransactionFlow`): security `BearerAuth`; required parameters `processingCode` (path), `transactionTypeId` (path); required body fields `key`; response statuses 200, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05007`, `WTRC04003`, `WTRC04004`, `WTRC04006`, `WTRC04005`, `WTRC05003`, `WTRC04002`, `ETRC04003`, `ETRC04004`, `ETRC04005`, `ETRC04006`, `ETRC00001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `CreateProcessingCode` | `orgs-operation-create-1` |
| `ProcessingCodeUpdate` | `orgs-operation-update-1` |
| `PostSetupTransactionType` | `transaction-types-creation-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/payments-configurations.md`: updatedAt 2026-09-25T19:26:28.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/payments-configurations.md` | whole document | https://developers.pismo.io/pismo-docs/docs/payments-configurations | `796fd4472b207011…` | 2026-09-25T19:26:28.000Z |

## Related knowledge units

- `KU-API-core-platform-transactions--transaction-flows` — API reference: Core platform - Transactions — Transaction flows
- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-platform-setup-orgs-operation--processing-codes` — API reference: Platform setup - Orgs operation — Processing codes
- `KU-CORE-fee-models` — Fee management and fee models
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-PAY-hold-funds` — Hold funds
