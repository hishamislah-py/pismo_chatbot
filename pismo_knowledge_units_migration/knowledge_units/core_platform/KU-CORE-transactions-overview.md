---
ku_id: KU-CORE-transactions-overview
title: Transactions overview
category: core_platform
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/core-platform/transactions-overview.md
  sha256: 2ba51bcab8baa346f69aaed07f0037efc39d32ec41cad23eec5c3f678c132233
  url: https://developers.pismo.io/pismo-docs/docs/transactions-overview
  role: primary_guide
  updated_at: '2026-08-11T15:59:27.000Z'
operations:
- GetTransactionById
- GetTransactionTypeById
- ListTransactions
- PatchProgramTransactionType
- PatchTransactionType
- SearchTransactionTypes
- SearchTranscationMetaDataCount
- getTransactionTypes_1
- getTransactionsBalance
related_kus:
- KU-API-core-platform-transactions--transaction-types
- KU-API-core-platform-transactions--transactions
- KU-API-revolving-credit-statements--statement
- KU-API-revolving-credit-statements--transaction-types
- KU-CARD-card-network-integration
- KU-CARD-clearing
- KU-CARD-disputes-overview
- KU-CARD-protection-bulletin
- KU-CORE-accounting-overview
- KU-CORE-flex-controls
- KU-CORE-processing-codes-and-transaction-types
- KU-CORE-working-with-limits-objects
- KU-CRED-negotiating-credit-card-debt
- KU-EVT-catalogue-other-domains
- KU-EVT-catalogue-transaction
- KU-PAY-force-operation
- KU-PAY-payments
- KU-PAY-payments-configurations
- KU-PAY-transfers-make-and-cancel
grouping_rationale: single source page
---

# Transactions overview

**KU ID:** `KU-CORE-transactions-overview` · **Category:** Core platform · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/core-platform/transactions-overview.md`:

> Transactions are records of purchases, transfers, payments, or manual adjustments. On the Pismo platform, transactions are triggered by approved authorizations and are the end result of a financial operation.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/core-platform/transactions-overview.md`: Transactions overview; Authorizations vs. transactions; Transaction types; Transaction details; Transaction authorization when issuer is unavailable (Protection Bulletin)

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 9 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/core-platform/transactions-overview.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transactions-overview · updatedAt: 2026-08-11T15:59:27.000Z

<!-- source:begin path=docs/core-platform/transactions-overview.md part=0-end -->

# Transactions overview

Transactions are records of purchases, transfers, payments, or manual adjustments. On the Pismo platform, transactions are triggered by approved authorizations and are the end result of a financial operation.

The following image shows a high-level overview of how financial operations become authorizations and then transactions on the Pismo platform.

<Image align="center" alt="Image shows a high-level overview of how financial operations become authorizations and then transactions on the Pismo platform." src="https://files.readme.io/d85adb0-transactions-journey-A2x.png" title="transactions-journey-A@2x.png" />

1. A financial operation is any operation that triggers money movement on a customer account, such as a withdrawal, purchase, payment, cash-in, or transfer.
2. The authorization step performs a number of validations, including

   * Is the account or card valid?
   * Is the operation allowed based on configured [flexible transaction controls](https://developers.pismo.io/pismo-docs/docs/flex-controls)?
   * Are the [account limits](https://developers.pismo.io/pismo-docs/docs/working-with-limits-objects) within allowable range?
   * Is there any fraudulent activity?

     <Callout icon="📘" theme="info">
       This step should take only milliseconds. If the authorization succeeds, the platform updates the customer timeline. It may also affect the credit limit (if related to a credit program) or the account balance (if related to a debit or prepaid program).
     </Callout>
3. A confirmation step occurs next, but only if the transaction applies to card network operations that require a [dual-message clearing model](https://developers.pismo.io/pismo-docs/docs/clearingbase).
4. An authorization generates one or several transactions (for example, one transaction for a principal amount and another transaction for an additional fee). These transactions can be of different types, either debit or credit transactions. An adjustment made by the issuer (such as non-event authorizations) may also create a transaction. Transactions may affect bank or credit card statements. Some transaction type also may have [accounting](https://developers.pismo.io/pismo-docs/docs/accounting-overview) implications.

# Authorizations vs. transactions

Authorizations and transactions are two major components of a transaction lifecycle on the Pismo platform.

First, the platform evaluates any operation request and creates an **authorization**, which generates an [Authorization created](https://developers.pismo.io/events/docs/authorization-authorization-event-1) event.

Then, the platform uses this authorization and a predefined mapping between [processing code and corresponding transaction type](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) to create at least one **transaction**. The platform also generates a [Transaction created](https://developers.pismo.io/events/docs/transaction-creation-1) event for each created transaction.

# Transaction types

Transaction type represents the transaction characteristics that are created from an authorized financial operation. The transaction type identifies a transaction as either a credit or a debit and determines whether the transaction has a financial impact on the customer account. The processing code can have one or more transaction types configured, depending on whether one or more transactions can be created through the processing code. You can create custom transaction types on the Pismo platform to represent different kinds of financial operations as applicable to your organization. The Pismo platform supports different types of financial operations. These fall into two major categories:

* **[Platform operations (payments and transfers)](https://developers.pismo.io/pismo-docs/docs/payments)**:
  * [Peer-to-peer (P2P)](https://developers.pismo.io/pismo-docs/docs/make-transfer#transfer-p2p)
  * [Transfer from card](https://developers.pismo.io/pismo-docs/docs/make-transfer#transfer-from-card)
  * [Cash-in](https://developers.pismo.io/pismo-docs/docs/make-transfer#cash-in)
  * [Cash-out](https://developers.pismo.io/pismo-docs/docs/make-transfer#cash-out)
  * [Forced credit or debit operations](https://developers.pismo.io/pismo-docs/docs/force-operation)
  * Card on file (COF) operations
  * Purchases
* **[Card network operations](https://developers.pismo.io/pismo-docs/docs/card-network-integration)**

> 📘 Installment purchases
>
> The option to make payments in installments is available for transactions only within Brazil. The Pismo platform does not support this payment method for other countries and denies authorizations for all international installment purchases.

Based on these types of financial operations, the Pismo platform has predefined transaction types (for example, 101 - purchase, 102 - international purchase, 123 - withdrawal, and so on) but you can also create custom transaction types based on your needs. The platform uses the configured processing codes and their mappings to transaction types to generate transactions. For more information, see [Processing codes and transaction types](https://developers.pismo.io/pismo-docs/docs/processing-codes-and-transaction-types) and [Payments configurations](https://developers.pismo.io/pismo-docs/docs/payments-configurations#create-transaction-type).

To list transaction types that match your search criteria, use [List transaction types](https://developers.pismo.io/pismo-docs/reference/searchtransactiontypes). To list the program's transaction types, use [List program transaction types](https://developers.pismo.io/pismo-docs/reference/gettransactiontypes_1). To get the transaction type by its ID, use [Get transaction type](https://developers.pismo.io/pismo-docs/reference/gettransactiontypebyid).

You can also update a transaction type description [for the specific transaction type by its ID](https://developers.pismo.io/pismo-docs/reference/patchtransactiontype) or [for the specific program](https://developers.pismo.io/pismo-docs/reference/patchprogramtransactiontype).

# Transaction details

To search for transactions based on various criteria, use [List transactions](https://developers.pismo.io/pismo-docs/reference/listtransactions). You can search for transactions by customer, authorization, debit/credit operation, specific statement, and a number of other filters. This endpoint returns all matching transactions without their metadata and is useful for:

* Learning about a product's performance
* Calculating financial revenues
* Informing customers about their statements

To get details and metadata for a specific transaction by its ID, use [Get transaction](https://developers.pismo.io/pismo-docs/reference/gettransactionbyid).

To get the total number of transactions that match your criteria, use [Get transaction count](https://developers.pismo.io/pismo-docs/reference/searchtranscationmetadatacount).

If you need to see the credit card balance and details of a card network transaction, use [List transactions balance](https://developers.pismo.io/pismo-docs/reference/gettransactionsbalance).  This might be helpful if your customer has a [dispute](https://developers.pismo.io/pismo-docs/docs/disputes-overview) or needs [credit card refinancing](https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt).

<br />

# Transaction authorization when issuer is unavailable (Protection Bulletin)

Occasionally, a card issuer could go off offline or be otherwise unavailable. A mechanism known as the *Protection Bulletin* is used in this situation. Refer to [Protection Bulletin](https://developers.pismo.io/pismo-docs/docs/protection-bulletin) for more information.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /v1/transaction-types` | `SearchTransactionTypes` | List transaction types | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `GET /statements-v2/v1/programs-transactions-types` | `getTransactionTypes_1` | List program transaction types | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--transaction-types |
| `GET /v1/transaction-type/{transactionTypeId}` | `GetTransactionTypeById` | Get transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `PATCH /v1/transaction-types/{transactionTypeId}` | `PatchTransactionType` | Update transaction type | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId}` | `PatchProgramTransactionType` | Update program transaction type description | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transaction-types |
| `GET /v2/transactions` | `ListTransactions` | List transactions | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `GET /v2/transactions/{transactionId}` | `GetTransactionById` | Get transaction | `api-specs/Core_platform_-_Transactions.yaml` | no | KU-API-core-platform-transactions--transactions |
| `GET /v2/transactions/total-items` | `SearchTranscationMetaDataCount` | Get transaction count (deprecated) | `api-specs/Core_platform_-_Transactions.yaml` | **yes** | KU-API-core-platform-transactions--transactions |
| `GET /statements-v2/v1/accounts/{accountId}/transactions-balance` | `getTransactionsBalance` | List transaction balances | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement |

### Operation essentials

- **`GET /v1/transaction-types`** (`SearchTransactionTypes`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `WTRC00001`, `ETRC05001`, `ETRC00001`; events none listed.
- **`GET /statements-v2/v1/programs-transactions-types`** (`getTransactionTypes_1`): security `BearerAuth`; required parameters `program-id` (header); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`GET /v1/transaction-type/{transactionTypeId}`** (`GetTransactionTypeById`): security `BearerAuth`; required parameters `transactionTypeId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WTRC05004`, `WTRC05005`, `ETRC00001`; events none listed.
- **`PATCH /v1/transaction-types/{transactionTypeId}`** (`PatchTransactionType`): security `BearerAuth`; required parameters `transactionTypeId` (path); required body fields `description`; response statuses 200, 400, 409, 500; error codes in examples `WTRC00005`, `WTRC05001`, `ETRC00001`; events none listed.
- **`PATCH /v1/programs/{programId}/transaction-types/{transactionTypeId}`** (`PatchProgramTransactionType`): security `BearerAuth`; required parameters `programId` (path), `transactionTypeId` (path); required body fields `description`; response statuses 200, 400, 404, 500; error codes in examples `WTRC00003`, `WTRC00005`, `WTRC03001`, `ETRC03002`; events none listed.
- **`GET /v2/transactions`** (`ListTransactions`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `WTRC00002`, `WTRC00003`, `WTRC00001`, `ETRC00001`; events none listed.
- **`GET /v2/transactions/{transactionId}`** (`GetTransactionById`): security `BearerAuth`; required parameters `transactionId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `WTRC00002`, `WTRC00003`, `WTRC01003`, `WTRC01001`, `ETRC00001`; events none listed.
- **`GET /v2/transactions/total-items`** (`SearchTranscationMetaDataCount`): security `BearerAuth`; required parameters none declared; required body fields none declared; response statuses 200, 400, 500; error codes in examples `WTRC00002`, `WTRC00003`, `WTRC00001`, `ETRC00001`; events none listed.
- **`GET /statements-v2/v1/accounts/{accountId}/transactions-balance`** (`getTransactionsBalance`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.

## Events

Event types linked from the source text (`api-reference-data/event_type_inventory.csv`):

| Event slug | Domain (inventory guess) | Version (inventory guess) | Event page | Emitting operations | Catalogue KU |
| --- | --- | --- | --- | --- | --- |
| `authorization-authorization-event-1` | authorization | 1 | https://developers.pismo.io/events/docs/authorization-authorization-event-1 | 9 | KU-EVT-catalogue-other-domains |
| `transaction-creation-1` | transaction | 1 | https://developers.pismo.io/events/docs/transaction-creation-1 | 7 | KU-EVT-catalogue-transaction |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/core-platform/transactions-overview.md`: updatedAt 2026-08-11T15:59:27.000Z.
- Links to `SearchTranscationMetaDataCount`, which is marked `deprecated: true` in `api-specs/Core_platform_-_Transactions.yaml`.

## Conflicts, caveats and evidence gaps

- The source links to 2 event page(s) under `/events/`. Event payload definitions are not part of the corpus (robots.txt disallows `/events/`), so payload fields are not documented here.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/core-platform/transactions-overview.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transactions-overview | `2ba51bcab8baa346…` | 2026-08-11T15:59:27.000Z |

## Related knowledge units

- `KU-API-core-platform-transactions--transaction-types` — API reference: Core platform - Transactions — Transaction types
- `KU-API-core-platform-transactions--transactions` — API reference: Core platform - Transactions — Transactions
- `KU-API-revolving-credit-statements--statement` — API reference: Revolving credit - Statements — Statement
- `KU-API-revolving-credit-statements--transaction-types` — API reference: Revolving credit - Statements — Transaction types
- `KU-CARD-card-network-integration` — Card network integration and certification
- `KU-CARD-clearing` — Clearing: Base II and the clearing rules engine
- `KU-CARD-disputes-overview` — Disputes overview
- `KU-CARD-protection-bulletin` — Protection Bulletin
- `KU-CORE-accounting-overview` — Accounting overview and accounting event types
- `KU-CORE-flex-controls` — Flexible transaction controls: concepts, examples and simulation
- `KU-CORE-processing-codes-and-transaction-types` — Processing codes
- `KU-CORE-working-with-limits-objects` — Account limits
- `KU-CRED-negotiating-credit-card-debt` — Credit card refinancing
- `KU-EVT-catalogue-other-domains` — Event catalogue: other event domains (accounting, authorization, availables, average, bulletin, cash, delinquent, fraud, instantpay, intl, ledger, networktransactions, onboarding, orgs, payment, platform, programs, rules, savings, statement)
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
- `KU-PAY-force-operation` — Force operation
- `KU-PAY-payments` — Payments and transfers
- `KU-PAY-payments-configurations` — Payments configurations
- `KU-PAY-transfers-make-and-cancel` — Transfers: making and cancelling transfers
