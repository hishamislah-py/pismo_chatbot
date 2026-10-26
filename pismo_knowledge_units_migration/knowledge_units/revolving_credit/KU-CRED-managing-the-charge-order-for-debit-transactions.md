---
ku_id: KU-CRED-managing-the-charge-order-for-debit-transactions
title: Managing the charge order for debit transactions
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/managing-the-charge-order-for-debit-transactions.md
  sha256: 2a5b7485da45e56da60ae5793083a63da3b52f6d25469984d54d2da2e0e472f4
  url: https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions
  role: primary_guide
  updated_at: '2026-03-18T15:23:46.000Z'
operations:
- account-parameters-find
- account-parameters-update
- createProgramTransactionType
- createTransactionCategory
- updateTransactionCategoryInterest
related_kus:
- KU-API-core-platform-accounts--account-parameters
- KU-API-revolving-credit-configurations--program-transaction-types
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-CRED-full-balance-credit-program
grouping_rationale: single source page
---

# Managing the charge order for debit transactions

**KU ID:** `KU-CRED-managing-the-charge-order-for-debit-transactions` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/managing-the-charge-order-for-debit-transactions.md`:

> The **payment hierarchy** sorts debit transactions into groups, and the Pismo platform discharges all the transactions in one group before it goes on to discharge all the transactions in the next group. For more information, refer to [How the program discharges transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-discharges-transactions).

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/managing-the-charge-order-for-debit-transactions.md`: Managing the charge order for debit transactions; Setting the charge order at the program level; Setting the charge order at the account level

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 5 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/managing-the-charge-order-for-debit-transactions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions · updatedAt: 2026-03-18T15:23:46.000Z

<!-- source:begin path=docs/card-issuing/managing-the-charge-order-for-debit-transactions.md part=0-end -->

# Managing the charge order for debit transactions

The **payment hierarchy** sorts debit transactions into groups, and the Pismo platform discharges all the transactions in one group before it goes on to discharge all the transactions in the next group. For more information, refer to [How the program discharges transactions](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-discharges-transactions).

Within a group, the platform pays off transactions by their **charge order**. It discharges transactions with a lower charge order before transactions with a higher one.

You can set the charge order at the program level or at the account level. A charge order set at the account level takes precedence over a charge order set at the program level.

# Setting the charge order at the program level

At the program level, you can set the charge order for a program transaction type when you create it using the [Create program transaction type](https://developers.pismo.io/pismo-docs/reference/createprogramtransactiontype) endpoint. Pass the value for the charge order in the `charge_order` field.

Alternatively, if a group of program transaction types are in the same program transaction category, you can set the charge order for the entire group by setting it in the `charge_order` field of the program transaction category. You can do this when you create the transaction category using the [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) endpoint, or you can do it for an existing transaction category using the [Update program transaction category](https://developers.pismo.io/pismo-docs/reference/updatetransactioncategoryinterest) endpoint. When you set the `charge_order` in a program transaction category, it overrides any charge order in a program transaction type that references it.

For information about program transaction categories and program transaction types, refer to [How the program uses configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-uses-configurable-entities).

# Setting the charge order at the account level

To set the charge order at the account level, follow these steps.

1. Use the [List parameters](https://developers.pismo.io/pismo-docs/reference/account-parameters-find) endpoint to get the parameter ID for the `SECONDARY_CHARGE_ORDER` parameter.
2. Use this parameter ID with the [Update parameter](https://developers.pismo.io/pismo-docs/reference/account-parameters-update) endpoint to set `SECONDARY_CHARGE_ORDER` to a positive integer of your choice.
3. Create a new category using [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory), and set the `secondary_charge_order` field to the charge order that you want to use when the `SECONDARY_CHARGE_ORDER` parameter is set.

If a transaction belongs to an account for which the `SECONDARY_CHARGE_ORDER` account parameter is set, the value of `secondary_charge_order` in the program transaction category overrides the charge order defined in the program transaction type. (It also overrides the`charge_order` parameter in the program transaction category.)
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /v1/programs/{programId}/program-transaction-types` | `createProgramTransactionType` | Create program transaction type | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-transaction-types |
| `POST /statements-v2/v1/transactions-categories` | `createTransactionCategory` | Create program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` | `updateTransactionCategoryInterest` | Update program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `GET /accounts/v1/accounts/{accountId}/parameters` | `account-parameters-find` | List parameters | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--account-parameters |
| `PUT /accounts/v1/accounts/{accountId}/parameters/{parameterId}` | `account-parameters-update` | Update parameter | `api-specs/Core_platform_-_Accounts.yaml` | no | KU-API-core-platform-accounts--account-parameters |

### Operation essentials

- **`POST /v1/programs/{programId}/program-transaction-types`** (`createProgramTransactionType`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EX0001`, `EX0002`; events none listed.
- **`POST /statements-v2/v1/transactions-categories`** (`createTransactionCategory`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 201, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}`** (`updateTransactionCategoryInterest`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header), `transactionCategoryId` (path); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`GET /accounts/v1/accounts/{accountId}/parameters`** (`account-parameters-find`): security `BearerAuth`; required parameters `accountId` (path); required body fields none declared; response statuses 200, 500; error codes in examples none; events none listed.
- **`PUT /accounts/v1/accounts/{accountId}/parameters/{parameterId}`** (`account-parameters-update`): security `BearerAuth`; required parameters `accountId` (path), `parameterId` (path); required body fields none declared; response statuses 200, 500; error codes in examples none; events none listed.

## Lifecycle status

- `docs/card-issuing/managing-the-charge-order-for-debit-transactions.md`: updatedAt 2026-03-18T15:23:46.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/managing-the-charge-order-for-debit-transactions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions | `2a5b7485da45e56d…` | 2026-03-18T15:23:46.000Z |

## Related knowledge units

- `KU-API-core-platform-accounts--account-parameters` — API reference: Core platform - Accounts — Account parameters
- `KU-API-revolving-credit-configurations--program-transaction-types` — API reference: Revolving credit - Configurations — Program transaction types
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
