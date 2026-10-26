---
ku_id: KU-CARD-transaction-categories
title: Transaction categories
category: card_issuing
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/transaction-category-structure.md
  sha256: e575e45dc34cfac60ed27695cd04845b1064bf960951c1706f006c5d0287cc4f
  url: https://developers.pismo.io/pismo-docs/docs/transaction-category-structure
  role: primary_guide
  updated_at: '2026-05-08T17:53:40.000Z'
- path: docs/control-center/cc-manage-transaction-categories.md
  sha256: 00965d0a0d50b2b700505feaec52e3134cdccfefa0c700de714f6723c6d72020
  url: https://developers.pismo.io/pismo-docs/docs/cc-manage-transaction-categories
  role: primary_guide
  updated_at: '2026-03-18T15:10:10.000Z'
operations:
- cancelAccountTransactionCategory
- createProgramTransactionType
- createTransactionCategory
- getAccountsTransactionsInterest_1
- listTransactionCategoryInterest
- saveAccountTransactionInterest
- updateTransactionCategoryInterest
related_kus:
- KU-API-revolving-credit-configurations--program-transaction-types
- KU-API-revolving-credit-statements--account-transaction-categories
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-CARD-program-transaction-types
- KU-CRED-accrual-rate-types-and-limits
- KU-CRED-configuring-accrual-rates
- KU-CRED-full-balance-credit-program
grouping_rationale: Same title in two areas (API and Control Center).
---

# Transaction categories

**KU ID:** `KU-CARD-transaction-categories` · **Category:** Card issuing · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: Same title in two areas (API and Control Center).

Scope as stated in `docs/card-issuing/transaction-category-structure.md`:

> A transaction category is a grouping of related transaction types. You can use it to manage properties such as accrual rates for all the transaction types in the category.

Scope as stated in `docs/control-center/cc-manage-transaction-categories.md`:

> A transaction category is a grouping of related transaction types that can be used to manage interest rates. Use transaction categories to configure credit refinancing and overdue accrual types at the program level. A program transaction type associates a transaction type with a transaction category and can also be used to set the charge order. Use Control Center to add or edit transaction categories and to add a transaction type to a transaction category.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/transaction-category-structure.md`: Transaction categories; Program transaction categories; Configuring and managing rates at the program level; Account transaction categories; Configuring and managing rates at the account level
- `docs/control-center/cc-manage-transaction-categories.md`: Transaction categories; Add a transaction category; Add a transaction type to a transaction category; Edit a transaction category

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 7 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/transaction-category-structure.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/transaction-category-structure · updatedAt: 2026-05-08T17:53:40.000Z

<!-- source:begin path=docs/card-issuing/transaction-category-structure.md part=0-end -->

# Transaction categories

A transaction category is a grouping of related transaction types. You can use it to manage properties such as accrual rates for all the transaction types in the category.

<Callout icon="📘" theme="info">
  **Accrual type rates**  enable you to configure additional accrual rates not available in transaction categories. For more information, refer to [Accrual type rates](https://developers.pismo.io/pismo-docs/docs/accrual-type-rate-structures#configuring-accrual-types-at-the-program-level).
</Callout>

The Pismo platform defines two types of transaction categories.

* [Program transaction categories](https://developers.pismo.io/pismo-docs/docs/transaction-category-structure#program-transaction-categories)
* [Account transaction categories](https://developers.pismo.io/pismo-docs/docs/transaction-category-structure#account-transaction-categories)

# Program transaction categories

A program transaction category is defined at the program level and is used to group transaction types. It has parameters that determine the charge order of transactions and rates for interest, fines, and taxes.

You can use the [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) endpoint to create your own categories. However, the following categories are automatically created as part of each new program in order to streamline customer onboarding. (These are listed by the value of their `description` parameter.)

* **Financeable transactions**—For transactions where the issuer allows the cardholder to pay less than the full amount, applying interest to the remaining balance.\
  Examples: Purchases, international purchases, installments purchase
* **Internal transactions**—Treatment varies by issuer. Some might require full payment, while others might not apply interest.\
  Examples: Adjustments such as debits from back-office operations
* **Non-financeable transactions**—For transactions that cannot be financed. Issuers typically require full payment, and don't apply interest.\
  Examples: Taxes, interest charges
* **Credit card cash advance rate transactions**—For transactions that might have different interest rate structures, often higher or with specific minimums, depending on the issuer.\
  Examples: Bill payments, cash withdrawals

<Callout icon="📘" theme="info">
  If you create your own program transaction category, you must also create program transaction types to link it to transaction types. For more information, refer to [Program transaction types](https://developers.pismo.io/pismo-docs/docs/program-transaction-types).
</Callout>

## Configuring and managing rates at the program level

Configure rates at the program level using the following endpoints.

* [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory)—Create a new program transaction category. After you create a new program transaction category, you must use [create a program transaction type](https://developers.pismo.io/pismo-docs/reference/createprogramtransactiontype) to link it to a transaction type. You can link one transaction category to multiple transaction types. For more information, refer to [How the program uses configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-uses-configurable-entities).
* [List program transaction categories](https://developers.pismo.io/pismo-docs/reference/listtransactioncategoryinterest)—List your existing program transaction categories.
* [Update program transaction category](https://developers.pismo.io/pismo-docs/reference/updatetransactioncategoryinterest)—Update the fields for an existing program transaction category. This can be one of the automatically created categories or one that you created using the [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) endpoint.

# Account transaction categories

Account level transaction categories, when defined, take precedence over program transaction categories. You can use them to configure certain accrual types at the account level.

## Configuring and managing rates at the account level

To configure rates at the account level, first configure them at the program level. Next, use the [Configure account transaction category rates](https://developers.pismo.io/pismo-docs/reference/saveaccounttransactioninterest) endpoint to create an account transaction category for the account in question and link it to the program transaction category. This endpoint enables you to configure rates for the account transaction category. These rates override the rates configured in the transaction category for the specified account.

Use [List account transaction category rates](https://developers.pismo.io/pismo-docs/reference/getaccountstransactionsinterest_1) to view the rates set in an account transaction category. Use [Cancel account transaction category](https://developers.pismo.io/pismo-docs/reference/cancelaccounttransactioncategory) to delete an account transaction category.
<!-- source:end -->

### Source 2: `docs/control-center/cc-manage-transaction-categories.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/cc-manage-transaction-categories · updatedAt: 2026-03-18T15:10:10.000Z

<!-- source:begin path=docs/control-center/cc-manage-transaction-categories.md part=0-end -->

# Transaction categories

A transaction category is a grouping of related transaction types that can be used to manage interest rates. Use transaction categories to configure credit refinancing and overdue accrual types at the program level. A program transaction type associates a transaction type with a transaction category and can also be used to set the charge order. Use Control Center to add or edit transaction categories and to add a transaction type to a transaction category.

> 📘
>
> Credit program types require you to provide transaction categories.

To view the list of transaction categories through the Control Center, go to the main menu and select **Configurations > Transaction categories**. Select any transaction category to view its details.

You can also use the [List transaction categories](https://developers.pismo.io/pismo-docs/reference/listtransactioncategoryinterest) API to view the full list of transaction categories.

For information about transaction categories on the Pismo platform, refer to:

* [Using configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#using-configurable-entities) with the Full balance credit program
* [Transaction category structure](https://developers.pismo.io/pismo-docs/docs/configuring-accrual-rates#transaction-category-structure) related to accrual rate configuration

# Add a transaction category

Credit programs are the only program type that require you to provide transaction categories.

To add a transaction category:

1. From the main menu, select **Configurations** > **Transaction categories**.

2. On the **Transaction categories** screen, select **Create**.

3. On the **Create a transaction category** screen, type a description and enter the default percentage rates for each displayed field.\
   For **Charge order**, enter an integer to determine the priority order when discharging transaction balances (**1** is the highest priority).

4. Select **Next**.

5. On the **Program** screen, select **Add**, select the programs to apply the category, and select **Next**.

6. On the **Review** screen, verify that the information you provided is correct and select **Finish**.

After you create a transaction category, you can add a transaction type to it.

# Add a transaction type to a transaction category

To add a transaction type to a transaction category:

1. From the main menu, select **Configurations** > **Transaction categories**.

2. On the **Transaction categories** screen, select the category that you want to modify.

3. On the **Transaction category details** screen, select **Add transaction types**.

4. On the **Add transaction types** screen, select the **Add** button for the transaction type that you want to add.\
   Note: If the transaction type is already associated with a transaction category, Control Center displays a notification dialog. If you proceed, the transaction type is unlinked from its current category and linked with the new one.

5. Select **Next**.

6. On the **Review** screen, verify that the information you provided is correct and select **Finish**.

# Edit a transaction category

To edit a transaction category:

1. From the main menu, select **Configurations** > **Transaction categories**.

2. On the **Transaction categories** screen, select the transaction category you want to modify.

3. On the **Transaction category details** screen, select **Edit** for the value you want to change.

4. Enter the new value and select **Save**.
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /statements-v2/v1/transactions-categories` | `createTransactionCategory` | Create program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `POST /v1/programs/{programId}/program-transaction-types` | `createProgramTransactionType` | Create program transaction type | `api-specs/Revolving_credit_-_Configurations.yaml` | no | KU-API-revolving-credit-configurations--program-transaction-types |
| `GET /statements-v2/v1/transactions-categories` | `listTransactionCategoryInterest` | List program transaction categories | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` | `updateTransactionCategoryInterest` | Update program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` | `saveAccountTransactionInterest` | Create or update account transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `GET /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories` | `getAccountsTransactionsInterest_1` | List account transaction category rates | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |
| `DELETE /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId}` | `cancelAccountTransactionCategory` | Cancel account transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--account-transaction-categories |

### Operation essentials

- **`POST /statements-v2/v1/transactions-categories`** (`createTransactionCategory`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 201, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`POST /v1/programs/{programId}/program-transaction-types`** (`createProgramTransactionType`): security `BearerAuth`; required parameters `programId` (path); required body fields none declared; response statuses 201, 400, 404, 500; error codes in examples `EX0001`, `EX0002`; events none listed.
- **`GET /statements-v2/v1/transactions-categories`** (`listTransactionCategoryInterest`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header); required body fields none declared; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}`** (`updateTransactionCategoryInterest`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header), `transactionCategoryId` (path); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`POST /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories`** (`saveAccountTransactionInterest`): security `BearerAuth`; required parameters `Authorization` (header), `accountId` (path); required body fields `transaction_category_id`; response statuses 201, 400, 423, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`GET /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories`** (`getAccountsTransactionsInterest_1`): security `BearerAuth`; required parameters `program-id` (header), `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.
- **`DELETE /statements-v2/v1/accounts/{accountId}/accounts-transactions-categories/{accountTransactionCategoryId}`** (`cancelAccountTransactionCategory`): security `BearerAuth`; required parameters `accountTransactionCategoryId` (path), `accountId` (path); required body fields none declared; response statuses 200, 400, 500; error codes in examples `EX0002`, `GN0001`; events none listed.

## Lifecycle status

- `docs/card-issuing/transaction-category-structure.md`: updatedAt 2026-05-08T17:53:40.000Z.
- `docs/control-center/cc-manage-transaction-categories.md`: updatedAt 2026-03-18T15:10:10.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/transaction-category-structure.md` | whole document | https://developers.pismo.io/pismo-docs/docs/transaction-category-structure | `e575e45dc34cfac6…` | 2026-05-08T17:53:40.000Z |
| `docs/control-center/cc-manage-transaction-categories.md` | whole document | https://developers.pismo.io/pismo-docs/docs/cc-manage-transaction-categories | `00965d0a0d50b2b7…` | 2026-03-18T15:10:10.000Z |

## Related knowledge units

- `KU-API-revolving-credit-configurations--program-transaction-types` — API reference: Revolving credit - Configurations — Program transaction types
- `KU-API-revolving-credit-statements--account-transaction-categories` — API reference: Revolving credit - Statements — Account transaction categories
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-CARD-program-transaction-types` — Program transaction types
- `KU-CRED-accrual-rate-types-and-limits` — Accrual rate types, accrual-free transaction types and accrual-day limits
- `KU-CRED-configuring-accrual-rates` — Configuring accrual rates
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
