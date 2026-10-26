---
ku_id: KU-CRED-discharging-transactions
title: Discharging transactions and the default discharge process
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/discharging-transactions.md
  sha256: 3c3b6342d07938f69f92ad81d8a1e89a355dec3e5dd95dc812aafcca6e426bcc
  url: https://developers.pismo.io/pismo-docs/docs/discharging-transactions
  role: primary_guide
  updated_at: '2026-08-13T14:52:43.000Z'
- path: docs/card-issuing/discharging-transactions-default-process.md
  sha256: 638e1eb348e742147c5663d245b5e8d9ec1492db0c57700a6b0706c0e1302be7
  url: https://developers.pismo.io/pismo-docs/docs/discharging-transactions-default-process
  role: primary_guide
  updated_at: '2026-08-13T14:09:21.000Z'
operations:
- get-corporate-transaction
related_kus:
- KU-API-banking-transaction-banking--transactions
- KU-CRED-managing-the-charge-order-for-debit-transactions
grouping_rationale: One process.
---

# Discharging transactions and the default discharge process

**KU ID:** `KU-CRED-discharging-transactions` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 2 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: One process.

Scope as stated in `docs/card-issuing/discharging-transactions.md`:

> This guide provides an overview of Pismo’s new Discharge and Payment Hierarchy architecture, which is currently available exclusively in the EXT environment. To ensure backward compatibility, the [default payment hierarchy](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#default-payment-hierarchy) maintains the original platform behavior. The sections below describe this behavior and outline the available configuration options supported by the new architecture.

Scope as stated in `docs/card-issuing/discharging-transactions-default-process.md`:

> A new Discharge and Payment Hierarchy architecture is available in the EXT environment. This guide will be superseded by the [Discharging transactions](https://developers.pismo.io/pismo-docs/docs/discharging-transactions) guide as soon as the new architecture becomes available in production.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/discharging-transactions.md`: Discharging transactions; Payment hierarchy; Default payment hierarchy; Custom payment hierarchies; Ordering dimensions; DebitType suborder types; DischargeConfiguration object; PaymentHierarchy object; Configuration resolution order; Account-level configuration; SecondaryChargeOrder dimension; Examples of how the discharge process works; Applying the discharge process in a simple example; Applying the discharge process in a more complex example
- `docs/card-issuing/discharging-transactions-default-process.md`: Discharging transactions—Default process; Payment hierarchy; Applying the discharge process in a simple example; Applying the discharge process in a more complex example

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 1 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/discharging-transactions.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/discharging-transactions · updatedAt: 2026-08-13T14:52:43.000Z

<!-- source:begin path=docs/card-issuing/discharging-transactions.md part=0-end -->

# Discharging transactions

<Callout icon="📘" theme="info">
  This guide provides an overview of Pismo’s new Discharge and Payment Hierarchy architecture, which is currently available exclusively in the EXT environment. To ensure backward compatibility, the [default payment hierarchy](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#default-payment-hierarchy) maintains the original platform behavior. The sections below describe this behavior and outline the available configuration options supported by the new architecture.

  To access the original information about the discharge process (before the implementation of the new architecture), refer to [Discharging transactions—Default process](https://developers.pismo.io/pismo-docs/docs/discharging-transactions-default-process). Once the new architecture is put into production, the [Discharging transactions—Default process](https://developers.pismo.io/pismo-docs/docs/discharging-transactions-default-process) guide will be removed from the Developers Portal.
</Callout>

The **discharge process** is the process that applies credit balances (payments, refunds, and adjustments) to outstanding debit transactions, following a defined order and eligibility logic. The process follows these steps.

1. A credit arrives (payment, refund, or internal adjustment).

2. The Pismo platform selects eligible debit transactions.

3. The platform orders those debits according to a configured payment hierarchy.

4. The platform applies the credit sequentially until it's exhausted or no more debits remain.

When a debit transaction is fully discharged, it's considered to be **paid in full** or **paid off**.

<Callout icon="📘" theme="info">
  The discharge process described here applies to the standard credit-cycle payment flow. Delinquency buckets have their own internal discharge order that is independent of this process.
</Callout>

The discharge process runs on the following occasions.

* **When the platform receives a credit transaction.** The discharge process finds eligible debit transactions with a balance due and begins paying them off one by one, according to the [payment hierarchy](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#payment-hierarchy), until the credit amount is used up or no eligible debits remain. If the credit amount is greater than the total eligible debits, the remainder constitutes a credit balance on the account. This balance gets applied to any future debits.
* **When the platform receives a debit transaction from the customer (a purchase), and the account has an available credit balance.** In this scenario, the Pismo platform uses any available credit to offset the new debit, partially or fully, depending on the debit and credit balance available. In this case, the Pismo platform does not run the entire discharge process—it just applies available credit to the new debit.
* **Immediately before closing the credit cycle.** Some debits, such as fees, don't come from the customer and don't directly trigger the discharge process, so an account could still have both a credit balance and unpaid debits at the end of a cycle. For this reason, the Pismo platform triggers the discharge process immediately before closing the credit cycle.

<Callout icon="🚧" theme="warn">
  In times of high load, there could be a delay before the platform uses a payment to discharge transactions. You should take this into account when designing your credit program.
</Callout>

# Payment hierarchy

The payment hierarchy is the set of rules the Pismo platform uses to determine the order in which unpaid transactions are paid off by the discharge process. The following section describes the default configuration for the payment hierarchy. Later sections explain how you can modify the default configuration to better meet your company's needs.

## Default payment hierarchy

Under the default payment hierarchy, the discharge engine divides transactions into the following groups.

* **Group 1**—Overdue transactions
* **Group 2**—Transactions from the previous cycle that are not yet overdue
* **Group 3**—Transactions from the current credit cycle

Group 1 transactions are fully discharged first, then group 2, and finally group 3. Note that Groups 1, 2, and 3 correspond to the `DebitType` dimension sub-orders `Overdue`, `ClosedNotDue`, and `Current`, respectively, in the [Custom payment hierarchies](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#custom-payment-hierarchies) section.

Within each group, the order in which transactions are paid off is determined by their charge orders and their real due dates. For more information about the charge order, refer to [Managing the charge order for debit transactions](https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions).

The transactions within each group are paid off according to the following rules. Each rule corresponds to one of the [ordering dimensions](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#ordering-dimensions) in the [Custom payment hierarchies](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#custom-payment-hierarchies) section.

* Transactions with the lowest charge orders, as defined in their associated program transaction types, are discharged first. This corresponds to the `ProgramTransactionType` ordering dimension.
* Transactions with the oldest due dates are discharged next. This corresponds to the `StatementDueDate` ordering dimension.
* Transactions with the lowest charge orders, as defined in their associated program transaction categories, are paid off next. Charge orders configured in program transaction types override charge orders configured in program transaction categories. This corresponds to the `TransactionCategory` ordering dimension.
* Any remaining transactions are discharged last, in the order of their transaction event dates. The transaction event date is the date on which the transaction occurred, and it's returned in the `event_date` field of the [Get transaction](https://developers.pismo.io/pismo-docs/reference/get-corporate-transaction) endpoint. This corresponds to the `TransactionDate` ordering dimension.

<Callout icon="📘" theme="info">
  An exception to the above rules can occur when a purchase is canceled. When a cardholder makes a purchase, the resulting debit transaction has an authorization ID (`authorization_id`). Canceling a purchase generates a credit transaction for the same amount and with the same authorization ID. In this case, the debit transaction has priority and is discharged before any other transactions.

  In other words, when a credit transaction has the same authorization ID as a debit transaction, the debit transaction has priority over other transactions. This behavior is captured by the `OriginalDebit` dimension, placed first in the default hierarchy.
</Callout>

## Custom payment hierarchies

The default payment hierarchy applies automatically. To create a custom payment hierarchy, follow these steps.

1. Contact your Pismo representative to review the target discharge behavior and validate it against your market and regulatory context.
2. Define the [`PaymentHierarchy` object](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#dischargeconfiguration-object). To do this, pick the [ordering dimensions](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#ordering-dimensions) you need and the [sub-order values for DebitType](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#debittype-suborder-types) if applicable.
3. Wrap the `PaymentHierarchy` object in a [`DischargeConfiguration` object](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#dischargeconfiguration-object).
4. Create a Service Desk Configuration ticket requesting the change. Your Pismo representative can help you fill out the appropriate fields. By default, a payment hierarchy applies to the all the accounts in a program. If you want the new hierarchy to apply to a specific account, be sure to let your representative know. For more information, refer to [Account-level configuration](https://developers.pismo.io/pismo-docs/docs/discharging-transactions#account-level-configuration). The Pismo team reviews the requested configuration and validates the applicable scope before applying it.

### Ordering dimensions

The Pismo platform uses **ordering dimensions** to determine which debits should be paid off first. The ordering dimension appears in the `PaymentHierarchy` object as `dimension`. Set it to one of the following values.

| Dimension                | Suborder | Description                                                                                                            |
| :----------------------- | :------- | :--------------------------------------------------------------------------------------------------------------------- |
| `OriginalDebit`          | No       | Preserve authorization consistency by clearing the debit tied to the incoming credit (the authorization ID exception). |
| `DebitType`              | Yes      | Orders debits by lifecycle state: Overdue → ClosedNotDue → Current.                                                    |
| `StatementDueDate`       | No       | Orders by statement due date (oldest first).                                                                           |
| `TransactionDate`        | No       | Orders by transaction event timestamp (oldest first).                                                                  |
| `TransactionCategory`    | No       | Orders by program transaction category charge order.                                                                   |
| `ProgramTransactionType` | No       | Orders by program-specific transaction type charge order.                                                              |
| `SecondaryChargeOrder`   | No       | Orders by the transaction category's `secondary_charge_order` value. Categories with no value sort last.               |

### DebitType suborder types

The `DebitType` dimension supports explicit sub-ordering because debit lifecycle state is not inherently sortable without business context.

| Suborder       | Meaning                                                          |
| :------------- | :--------------------------------------------------------------- |
| `Overdue`      | Statement due date is earlier than the credit event date.        |
| `ClosedNotDue` | Statement cycle is closed but the due date has not been reached. |
| `Current`      | Transaction belongs to the current open billing cycle.           |

## DischargeConfiguration object

The `DischargeConfiguration`object binds a scope to a discharge strategy and to exactly one payment hierarchy.

| Field              | Type        | Description                                                                                                                       |
| :----------------- | :---------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| `Strategy`         | String      | Discharge strategy type. Must be set to `Default`.                                                                                |
| `PaymentHierarchy` | JSON object | Reference to a `PaymentHierarchy` ID. Exactly one active hierarchy is supported per scope.                                        |
| `Enabled`          | Boolean     | Controls whether this record is honored at runtime. Used mainly to disable an account-level override without deleting the record. |

### PaymentHierarchy object

The `PaymentHierarchy` JSON object defines the ordered list of dimensions that the discharge engine applies. Each ordering entry has an `order` (lower values have higher priority) and, when supported, an optional `suborder`.

The following JSON code shows how the default `PaymentHierarchy` object is configured internally. Use this as a reference when creating a custom payment hierarchy.

```json
{ 
  "Ordering": [ 
    { "order": 1, "dimension": "OriginalDebit" }, 
    { 
      "order": 2, 
      "dimension": "DebitType", 
      "suborder": { "Overdue": 1, "ClosedNotDue": 2, "Current": 3 } 
    }, 
    { "order": 3, "dimension": "ProgramTransactionType" }, 
    { "order": 4, "dimension": "StatementDueDate" }, 
    { "order": 5, "dimension": "TransactionCategory" }, 
    { "order": 6, "dimension": "TransactionDate" } 
  ] 
}
```

<Callout icon="📘" theme="info">
  Although the schema stores `PaymentHierarchy` as a list, only one hierarchy is active per scope at a time, and the hierarchy never changes mid-discharge.
</Callout>

## Configuration resolution order

When a credit event arrives, the discharge engine resolves the hierarchy in the following order.

1. **Account-level configuration**—If an account-level configuration exists for the account and `Enabled` = `true`, use its payment hierarchy.

2. **Program-level configuration**—Otherwise, if a program-level configuration exists, use its payment hierarchy.

3. **Default payment hierarchy**—If no enabled account-level or program-level configuration exists, or the referenced hierarchy is missing or invalid, use the default payment hierarchy.

## Account-level configuration

The account scope allows an individual account to use a payment hierarchy that overrides the program-level payment hierarchy.

To configure a payment hierarchy for a specific account, first configure the Secondary Charge Order for the account, as described in the [Managing the charge order for debit transactions](https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions#setting-the-charge-order-at-the-account-level) guide.

Next, define the `SecondaryChargeOrder` dimension n the `PaymentHierarchy` object. For example:

```json
{
  "Ordering": [
    {
      "order": 1, "dimension": "OriginalDebit"
    },
    {
      "order": 2, "dimension": "SecondaryChargeOrder"
    },
    {
      "order": 3, "dimension": "StatementDueDate"
    },
    {
      "order": 4, "dimension": "TransactionDate"
    }
  ]
}
```

Finally, just as for a program-level configuration, get your Pismo representative to help you open a Service Desk ticket to implement the configuration. Make sure you explain to your representative that the configuration is for a specific account and provide them with the ID for that account.

## SecondaryChargeOrder dimension

The `SecondaryChargeOrder` dimension makes the category's `secondary_charge_order` value available as an explicit hierarchy entry, so it can be composed with the other dimensions in the payment hierarchy. Use `SecondaryChargeOrder` when the payment hierarchy must prioritize transaction categories by their `secondary_charge_order` value.

Categories that have no `secondary_charge_order` value sort last, which keeps behavior predictable when only a subset of categories is configured.

# Examples of how the discharge process works

The following examples assume the default discharge configuration. This behavior can vary considerably if you use a custom configuration.

### Applying the discharge process in a simple example

The following example shows how the discharge process works in the simplest case.

The cardholder makes a purchase:

| Transaction\_ID | Account\_ID | TransactionType\_ID | Description      | Amount | Balance |
| :-------------- | :---------- | :------------------ | :--------------- | :----- | :------ |
| 1               | 1           | 101                 | PURCHASE ON SITE | $50.00 | $50.00  |

Later, the cardholder makes a payment:

| Transaction\_ID | Account\_ID | TransactionType\_ID | Description | Amount | Balance |
| :-------------- | :---------- | :------------------ | :---------- | :----- | :------ |
| 2               | 1           | 201                 | PAYMENT     | $20.00 | $20.00  |

The Pismo platform performs a discharge. It deducts the balance of transaction 2 from the balance of transaction 1:

| Transaction\_ID | Account\_ID | TransactionType\_ID | Description      | Amount | Balance |
| :-------------- | :---------- | :------------------ | :--------------- | :----- | :------ |
| 1               | 1           | 101                 | PURCHASE ON SITE | $50.00 | $30.00  |
| 2               | 1           | 201                 | PAYMENT          | $20.00 | $0.00   |

The balance for the payment transaction is $0.00. If the payment had been for more than $50.00, then the payment transaction would have been left with a non-zero balance. This remaining balance would be deducted from any future purchases.

### Applying the discharge process in a more complex example

The following example shows how the discharge process works in a more complex case where the debit transaction is associated with a program transaction category.

Suppose you have a program transaction category that defines charge orders for fineable and non-fineable transactions as follows:

| Description               | Charge Order |
| :------------------------ | :----------- |
| Non-fineable transactions | 1            |
| Fineable transactions     | 2            |

Suppose you have transaction types defined for purchase transactions and interest transactions and those types are associated with program transaction categories (via program transaction types) as follows:

| Type     | Category                  |
| :------- | :------------------------ |
| Purchase | Fineable transactions     |
| Interest | Non-fineable transactions |

Now suppose you have the following transactions:

| #  | Date       | Statement | Is overdue? | Type     | Amount |
| :- | :--------- | :-------- | :---------- | :------- | :----- |
| A  | 2023-01-01 | 1         | True        | Purchase | $100   |
| B  | 2023-01-10 | 1         | True        | Interest | $10    |
| C  | 2023-02-01 | 2         | False       | Interest | $20    |

When the account receives a credit, the Pismo platform discharges the transactions in the following order:

1. B (because A and B are in an overdue statement, but the category of transaction B has a charge order lower than the category of transaction A.)
2. A (because transaction A is in an overdue statement and transaction C is not.)
3. C
<!-- source:end -->

### Source 2: `docs/card-issuing/discharging-transactions-default-process.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/discharging-transactions-default-process · updatedAt: 2026-08-13T14:09:21.000Z

<!-- source:begin path=docs/card-issuing/discharging-transactions-default-process.md part=0-end -->

# Discharging transactions—Default process

<Callout icon="📘" theme="info">
  A new Discharge and Payment Hierarchy architecture is available in the EXT environment. This guide will be superseded by the [Discharging transactions](https://developers.pismo.io/pismo-docs/docs/discharging-transactions) guide as soon as the new architecture becomes available in production.
</Callout>

The **discharge process** defines how cardholders' payments are applied to transactions to reduce their debt. When a credit transaction occurs, its value is deducted from the balances of one or more debit transactions. When a debit transaction is fully discharged, it's said to be **paid in full** or **paid off**.

The Pismo platform runs the discharge process on the following occasions.

* **When the platform receives a credit transaction:** In this case, the discharge process finds all the debit transactions with a balance due and begins paying them off one by one, until the money from the credit transaction is used up. If the amount of the received credit is greater than the total debits, the residual credit amount is carried over until the **next time a credit is received** (which triggers the discharge process again) or until **cycle closing** (which also triggers the process).
* **Immediately before closing the credit cycle:** In this case, the discharge process continues paying off the unpaid debit transactions for the closed cycle using the residual credit amount (if any).

<Callout icon="🚧" theme="warn">
  In times of high load, there could be a delay before a payment is used to discharge transactions. You should take this into account when designing your credit program.
</Callout>

### Payment hierarchy

The payment hierarchy is the set of rules that the Pismo platform uses to determine the order in which unpaid transactions are paid off by the discharge process. These rules ensure that overdue transactions are paid off first.

The payment hierarchy divides transactions into these groups:

* **Group 1**—Overdue transactions
* **Group 2**—Transactions from the previous cycle that are not yet overdue
* **Group 3**—Transactions from the current credit cycle

Group 1 transactions are fully discharged first, then group 2, and finally group 3.

<Callout icon="📘" theme="info">
  As noted earlier, there are only two triggers for the discharge process.

  * A new credit is received.
  * The platform is ready to close the cycle.

  So, if there is money left over from a credit after paying off all the debits, and another debit is received, the leftover money is not immediately used to discharge the new debit. But when a new credit is received, or the cycle is about to close, the discharge process is triggered, and the leftover money is then applied to the new debit.
</Callout>

Within each group, the order in which transactions are paid off is determined by their charge orders and their real due dates. For more information about the charge order, refer to [Managing the charge order for debit transactions](https://developers.pismo.io/pismo-docs/docs/managing-the-charge-order-for-debit-transactions). The transactions within each group are paid off in the following order.

1. Transactions with the lowest charge orders, as defined in their associated **program transaction types**, are discharged first.
2. Transactions with the oldest due dates are discharged next.
3. Transactions with the lowest charge orders, as defined in their associated **program transaction categories**, are paid off next. (Charge orders configured in program transaction types override charge orders configured in program transaction categories.)
4. Any remaining transactions are discharged last, in the order of their transaction event dates. The **transaction event date** is the date on which the transaction occurred. It's returned in the `event_date` field of the [Get transaction](https://developers.pismo.io/pismo-docs/reference/get-corporate-transaction) endpoint.

These rules provide the flexibility for you to configure how transactions are paid off within a group.

<Callout icon="🚧" theme="warn">
  An exception to the above rules can occur when a purchase is canceled. When a cardholder makes a purchase, the resulting debit transaction has an authorization ID (`authorization_id`). If the purchase is canceled, this generates a credit transaction for the same amount and with the same authorization ID. In this case, the debit transaction has priority and is discharged before any other transactions.

  In other words, when a credit transaction has the same authorization ID as a debit transaction, the debit transaction has priority over other transactions.
</Callout>

### Applying the discharge process in a simple example

The following example shows how the discharge process works in the simplest case.

The cardholder makes a purchase:

| Transaction\_ID | Account\_ID | TransactionType\_ID | Description      | Amount | Balance |
| :-------------- | :---------- | :------------------ | :--------------- | :----- | :------ |
| 1               | 1           | 101                 | PURCHASE ON SITE | $50.00 | $50.00  |

Later, the cardholder makes a payment:

| Transaction\_ID | Account\_ID | TransactionType\_ID | Description | Amount | Balance |
| :-------------- | :---------- | :------------------ | :---------- | :----- | :------ |
| 2               | 1           | 201                 | PAYMENT     | $20.00 | $20.00  |

The Pismo platform performs a discharge. It deducts the balance of transaction 2 from the balance of transaction 1:

| Transaction\_ID | Account\_ID | TransactionType\_ID | Description      | Amount | Balance |
| :-------------- | :---------- | :------------------ | :--------------- | :----- | :------ |
| 1               | 1           | 101                 | PURCHASE ON SITE | $50.00 | $30.00  |
| 2               | 1           | 201                 | PAYMENT          | $20.00 | $0.00   |

The balance for the payment transaction is $0.00. If the payment had been for more than $50.00, then the payment transaction would have been left with a non-zero balance. This remaining balance would be deducted from any future purchases.

### Applying the discharge process in a more complex example

The following example shows how the discharge process works in a more complex case where the debit transaction is associated with a program transaction category.

Suppose you have a program transaction category that defines charge orders for fineable and non-fineable transactions as follows:

| Description               | Charge Order |
| :------------------------ | :----------- |
| Non-fineable transactions | 1            |
| Fineable transactions     | 2            |

Suppose you have transaction types defined for purchase transactions and interest transactions and those types are associated with program transaction categories (via program transaction types) as follows:

| Type     | Category                  |
| :------- | :------------------------ |
| Purchase | Fineable transactions     |
| Interest | Non-fineable transactions |

Now suppose you have the following transactions:

| #  | Date       | Statement | Is overdue? | Type     | Amount |
| :- | :--------- | :-------- | :---------- | :------- | :----- |
| A  | 2023-01-01 | 1         | True        | Purchase | $100   |
| B  | 2023-01-10 | 1         | True        | Interest | $10    |
| C  | 2023-02-01 | 2         | False       | Interest | $20    |

When the account receives a credit, the Pismo platform discharges the transactions in the following order:

1. B (because A and B are in an overdue statement, but the category of transaction B has a charge order lower than the category of transaction A.)
2. A (because transaction A is in an overdue statement and transaction C is not.)
3. C
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `GET /corporate/v1/corporate-transactions/{transactionId}` | `get-corporate-transaction` | Get transaction (transaction banking) | `api-specs/Banking_-_Transaction_banking.yaml` | no | KU-API-banking-transaction-banking--transactions |

### Operation essentials

- **`GET /corporate/v1/corporate-transactions/{transactionId}`** (`get-corporate-transaction`): security `BearerAuth`; required parameters `transactionId` (path); required body fields none declared; response statuses 200, 400, 401, 403, 404, 500; error codes in examples `WCTR0005`, `WCAC0001`, `WCTR0006`, `ECMN9999`; events none listed.

## Lifecycle status

- `docs/card-issuing/discharging-transactions.md`: updatedAt 2026-08-13T14:52:43.000Z.
- `docs/card-issuing/discharging-transactions-default-process.md`: updatedAt 2026-08-13T14:09:21.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- None identified by the migration checks.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/discharging-transactions.md` | whole document | https://developers.pismo.io/pismo-docs/docs/discharging-transactions | `3c3b6342d07938f6…` | 2026-08-13T14:52:43.000Z |
| `docs/card-issuing/discharging-transactions-default-process.md` | whole document | https://developers.pismo.io/pismo-docs/docs/discharging-transactions-default-process | `638e1eb348e74214…` | 2026-08-13T14:09:21.000Z |

## Related knowledge units

- `KU-API-banking-transaction-banking--transactions` — API reference: Banking - Transaction banking — Transactions
- `KU-CRED-managing-the-charge-order-for-debit-transactions` — Managing the charge order for debit transactions
