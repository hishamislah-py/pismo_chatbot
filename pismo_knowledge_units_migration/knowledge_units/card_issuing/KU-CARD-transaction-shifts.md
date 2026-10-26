---
ku_id: KU-CARD-transaction-shifts
title: Transaction shifts
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/transaction-shifts.md
  sha256: 5578b21406b226600b042d686538e6740bc359740ffa22ae77cc61f9427f85c6
  url: https://developers.pismo.io/pismo-docs/docs/transaction-shifts
  role: primary_guide
  updated_at: '2026-03-18T15:22:44.000Z'
operations:
- getTransactionShift
- post-shift-transactions
related_kus:
- KU-API-revolving-credit-statements--transaction-shift
- KU-CRED-negotiating-credit-card-debt
- KU-EVT-catalogue-balance
- KU-EVT-catalogue-transaction
grouping_rationale: single source page
---

# Transaction shifts

**KU ID:** `KU-CARD-transaction-shifts` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/transaction-shifts.md`:

> Transaction shifts enable you to move a customer's purchase installment freely between statements as long as the source and destination statements are valid and open.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/transaction-shifts.md`: Transaction shifts; Managing transaction shifts

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 2 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/transaction-shifts.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transaction-shifts · updatedAt: 2026-03-18T15:22:44.000Z

<!-- source:begin path=docs/card-issuing/transaction-shifts.md part=0-end -->

# Transaction shifts

Transaction shifts enable you to move a customer's purchase installment freely between statements as long as the source and destination statements are valid and open.

A transaction shift is similar to an [installment advancement](https://developers.pismo.io/pismo-docs/docs/negotiating-credit-card-debt#installment-advancement), but differs in two respects.

* An installment advancement can only move installments from future statements to the current one. A transaction shift can move installments in either direction.
* A transaction shift does not change the interest on an installment. An installment advancement reduces it.

A transaction *cannot* be shifted in the following circumstances.

* It's a credit transaction. You can only shift debit transactions.
* The transaction has already been discharged.
* The transaction is not posted to a statement.
* The source statement and destination statements are the same.
* The source statement is closed.
* The destination statement is closed.

## Managing transaction shifts

Use the [Shift transactions](https://developers.pismo.io/pismo-docs/reference/post-shift-transactions) endpoint to move transactions. This endpoint takes an array of transactions. For each transaction in the array, you must specify the statement that you want to move the transaction to. To do this, provide either the ID of the statement (`new_statement_id`) or the cycle closing date (`desired_cycle_date`). You can move a maximum of 24 transactions per request.

> 🚧
>
> If you provide a `desired_cycle_date` that does not match any cycle closing date, the Pismo platform tries to find the closest cycle closing date after `desired_cycle_date` and moves the transaction to that statement.

To view the record for a performed transaction shift, use the [Get transaction shift](https://developers.pismo.io/pismo-docs/reference/gettransactionshift) endpoint.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /statements-v2/v1/accounts/{accountId}/transactions/shifts` | `post-shift-transactions` | Shift transactions | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--transaction-shift |
| `GET /statements-v2/v1/accounts/{accountId}/transactions/shifts/{transactionShiftId}` | `getTransactionShift` | Get transaction shift | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--transaction-shift |

### Operation essentials

- **`POST /statements-v2/v1/accounts/{accountId}/transactions/shifts`** (`post-shift-transactions`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `GN0001`; events `balance-shift-transactions-1`, `transaction-update-1`.
- **`GET /statements-v2/v1/accounts/{accountId}/transactions/shifts/{transactionShiftId}`** (`getTransactionShift`): security `BearerAuth`; required parameters `accountId` (path), `transactionShiftId` (path); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `GN0001`; events none listed.

## Events

Events emitted by the referenced operations (`api-reference-data/endpoint_event_map.csv`):

| Operation | Event slug |
| --- | --- |
| `post-shift-transactions` | `balance-shift-transactions-1` |
| `post-shift-transactions` | `transaction-update-1` |

Event payload fields: not documented in the available source corpus.

## Lifecycle status

- `docs/card-issuing/transaction-shifts.md`: updatedAt 2026-03-18T15:22:44.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/transaction-shifts.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transaction-shifts | `5578b21406b22660…` | 2026-03-18T15:22:44.000Z |

## Related knowledge units

- `KU-API-revolving-credit-statements--transaction-shift` — API reference: Revolving credit - Statements — Transaction shift
- `KU-CRED-negotiating-credit-card-debt` — Credit card refinancing
- `KU-EVT-catalogue-balance` — Event catalogue: balance
- `KU-EVT-catalogue-transaction` — Event catalogue: transaction
