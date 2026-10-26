---
ku_id: KU-CRED-minimum-amount-due-calculation
title: Minimum amount due calculation
category: revolving_credit
ku_type: workflow_guide
lifecycle: current
sources:
- path: docs/card-issuing/minimum-amount-due-calculation.md
  sha256: c0ee25cd1dc7998466b95fabf3c576ed82d76e110682298fb660ff5b184150b8
  url: https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation
  role: primary_guide
  updated_at: '2026-08-20T17:14:12.000Z'
operations:
- createStatementAmountDue
- createTransactionCategory
- setProgramsParameters
- updateTransactionCategoryInterest
related_kus:
- KU-API-platform-setup-programs--parameters
- KU-API-revolving-credit-statements--program-transaction-categories
- KU-API-revolving-credit-statements--statement-minimum-amount-due
- KU-CC-get-started-control-center
- KU-CRED-full-balance-credit-program
grouping_rationale: single source page
---

# Minimum amount due calculation

**KU ID:** `KU-CRED-minimum-amount-due-calculation` · **Category:** Revolving credit · **Type:** workflow / concept guide · **Status:** current documentation

## Purpose and scope

This unit migrates 1 Pismo source document(s) into one implementation-oriented unit. Grouping rationale: single source page

Scope as stated in `docs/card-issuing/minimum-amount-due-calculation.md`:

> In the cycle closing process, the minimum amount due (MAD) is the amount that the cardholder must pay by the statement due date to avoid overdue charges.

## Topics covered

Headings of the source content (levels 1–3), which define the use cases this unit supports:

- `docs/card-issuing/minimum-amount-due-calculation.md`: Minimum amount due calculation; MAD calculation strategy; How to configure the MAD percentage for a program transaction category; Setting the transactions in a category to full-amount; Bypassing the MAD calculation strategy; Examples; Strategy 0 example; Strategy 1 example; Strategy 2 examples; First example; Second example

## Prerequisites and dependencies

- No separate prerequisites section in the source.
- Depends on 4 API operation(s), listed under “API operations referenced”.

## Current implementation guidance (source content, verbatim)

The source text below is reproduced exactly as published (front matter removed). Headings inside it keep their original levels.

### Source 1: `docs/card-issuing/minimum-amount-due-calculation.md`

Source URL: https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation · updatedAt: 2026-08-20T17:14:12.000Z

<!-- source:begin path=docs/card-issuing/minimum-amount-due-calculation.md part=0-end -->

# Minimum amount due calculation

In the cycle closing process, the minimum amount due (MAD) is the amount that the cardholder must pay by the statement due date to avoid overdue charges.

# MAD calculation strategy

There are three strategies for calculating the MAD. All three strategies use a MAD percentage value, but this value is defined slightly differently, depending on the strategy.

* Strategies 0 and 1 use the `minimum_value` field, defined in the program transaction categories, for the MAD percentage.
* Strategy 2 uses the `Percentage for calculating the minimum payment amount` program parameter for the MAD percentage.

The strategies are defined as follows.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Minimum payment calculation method
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        0
      </td>

      <td>
        The Pismo platform applies the MAD percentage to individual transactions from the current cycle and 100% of everything else outstanding.

        The following formula is applied to each transaction:\
        MAD percentage × debit transaction balance.\
        The results are added up and then added to 100% of the closing balances from previous cycles to get the MAD.
      </td>
    </tr>

    <tr>
      <td>
        1
      </td>

      <td>
        The Pismo platform applies the MAD percentage to individual transactions from both the current and previous cycles.

        The following formula is applied to each transaction:\
        MAD percentage × debit transaction balance.\
        The results are added up to  get the MAD.
      </td>
    </tr>

    <tr>
      <td>
        2
      </td>

      <td>
        The Pismo platform applies the MAD percentage to the total balance (sum of transaction amounts), instead of to individual transactions.

        In this strategy, the MAD includes the full overdue and over-limit amounts. The `Percentage for calculating the minimum payment amount` program parameter represents the MAD percentage in this case, and it's applied only to the remainder of the **total** current balance. So, the formula is:\
        (current balance - overdue amount - over-limit amount) × `Percentage for calculating the minimum payment amount` + overdue amount + over-limit amount

        * *Note:*\* The calculations for Strategy 2 must be adjusted if there are [full-amount transactions](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#full-amount-transactions)  involved.
      </td>
    </tr>
  </tbody>
</Table>

Use [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) or the [Update program(s) parameters](https://developers.pismo.io/pismo-docs/reference/setprogramsparameters) endpoint, to set `Minimum payment calculation method` to 0, 1, or 2.

If you select Strategy 0 or 1, you must configure the MAD percentage for the program transaction categories of all your debit transaction types. For more information, refer to [How to configure the MAD percentage for a program transactions category](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#how-to-configure-the-mad-percentage-for-a-program-transaction-category).

<Callout icon="📘" theme="info">
  If you don't configure the MAD percentage for a category, it defaults to 0.
</Callout>

If you select Strategy 2, use [Pismo Control Center](https://developers.pismo.io/pismo-docs/docs/get-started-with-control-center) or the [Update program(s) parameters](https://developers.pismo.io/pismo-docs/reference/setprogramsparameters) endpoint to set the value of `Percentage for calculating the minimum payment amount` to the MAD percentage.

# How to configure the MAD percentage for a program transaction category

Use either [Create program transaction category](https://developers.pismo.io/pismo-docs/reference/createtransactioncategory) or [Update program transaction category](https://developers.pismo.io/pismo-docs/reference/updatetransactioncategoryinterest) to set the MAD percentage in the `minimum_value` field of the transaction category. One category can apply to any number of transaction types.

<Callout icon="📘" theme="info">
  For Strategy 2 in the previous section, if `minimum_value` is set to 1 (100%), this overrides the value in the `Percentage for calculating the minimum payment amount` program parameter. For more information, refer to [Full-amount transactions](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#full-amount-transactions).
</Callout>

**Example program transaction categories**

The following table demonstrates  how MAD percentages could be assigned to program transaction categories.

| Category ID | Description          | MAD percentage |
| :---------- | :------------------- | :------------- |
| 1           | Internal             | 5%             |
| 2           | Financial            | 5%             |
| 3           | Non-financial        | 5%             |
| 4           | Withdrawal           | 5%             |
| 5           | Installment purchase | 100%           |

**Example transaction types**

Your transaction types could be assigned to program transaction categories as follows. See [How the program uses configurable entities](https://developers.pismo.io/pismo-docs/docs/full-balance-credit-program#how-the-program-uses-configurable-entities) for more information.

| Transaction type ID | Description            | Program transaction category |
| :------------------ | :--------------------- | :--------------------------- |
| 101                 | Purchase               | 2                            |
| 102                 | International purchase | 2                            |
| 123                 | Withdrawal             | 4                            |
| 201                 | Payment                | 2                            |
| 404                 | International fee      | 3                            |
| 405                 | Revolving interest     | 3                            |
| 407                 | Withdrawal fee         | 3                            |
| 112                 | Installment purchase   | 5                            |

# Setting the transactions in a category to full-amount

In some cases, you might not want the debit transactions in a program transaction category to be subject to refinancing. In such cases, the full amount of such a transaction must be included in the MAD, so these are called **full-amount transactions**. To make the transactions in a program transaction category full-amount, you set the `minimum_value` field of the category to 1.

For Strategies 0 and 1, having full-amount transactions in the cycle doesn’t change the calculation of the MAD, because the formula is applied to each transaction separately. Since the MAD percentage for a full-amount transaction is 100% (`minimum_value` = 1), applying the formula results in the entire amount of the transaction being included in the MAD.

For Strategy 2, however, if the current cycle includes full-amount transactions, the calculation is first done without including the full-value transactions. That is, the amounts of the full-amount transactions are subtracted from the current balance and the resulting adjusted balance is used in the formula. Next, the amounts of the full-amount transactions are added to the result returned by the formula to get the actual MAD. **Second example** in [Strategy 2 examples](https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation#strategy-2-examples) shows how this works.

# Bypassing the MAD calculation strategy

You can use the [Create or update statement minimum amount due](https://developers.pismo.io/pismo-docs/reference/createstatementamountdue) endpoint to bypass the MAD calculation strategy for the current cycle.

# Examples

## Strategy 0 example

This example applies when `Minimum payment calculation method` is set to 0.

**Cycle 1 statement**\
(Assume MAD percentage = 5%.)

| Transaction ID | Transaction type | Transaction balance | Minimum payment per transaction |
| :------------- | :--------------- | :------------------ | :------------------------------ |
| 1              | 101              | $200                | 0.05 × 200 = $10                |
| 2              | 123              | $100                | 0.05 × 100 = $5                 |
| 3              | 407              | $2                  | 0.05 × 2 = $0.10                |
| **Totals**     |                  | **$302.00**         | **$15.10**                      |

Previous balance: $0.00\
Current balance (total amount due): $302.00\
SUM(minimum per transaction): $15.10 **Minimum amount due (MAD):** $15.10

**Cycle 2 statement**\
Assume MAD percentage is 5%.

| Transaction ID | Transaction type | Transaction balance | Minimum payment per transaction |
| :------------- | :--------------- | :------------------ | :------------------------------ |
| 4              | 101              | $100                | 0.05 × 100 = $5                 |
| 5              | 123              | $100                | 0.05 × 100 = $5                 |
| 6              | 102              | $100                | 0.05 × 100 = $5                 |
| 7              | 101              | $0                  | 0.05 × 0 = $0                   |
| 8              | 407              | $2                  | 0.05 × 2 = $0.10                |
| 9              | 404              | $2                  | 0.05 × 2 = $0.10                |
|                | **Totals**       | **$304**            | **$15.20**                      |

Previous balance: $302.00\
Current balance (total amount due): 302.00 + 304.00 = $606.00\
SUM(minimum per transaction): $15.20\
**If no payments were made:**\
**Minimum amount due (MAD):** 302.00 + 15.20 = $317.20 (previous closing balance + MAD)

## Strategy 1 example

This example applies when `Minimum payment calculation method` is set to 1.

**Cycle 1 statement**\
(Assume MAD percentage = 5%.)

| Transaction ID | Transaction type | Transaction balance | Minimum payment per transaction |
| :------------- | :--------------- | :------------------ | :------------------------------ |
| 1              | 101              | $200                | 0.05 × 200 = $10                |
| 2              | 123              | $100                | 0.05 × 100 =$5                  |
| 3              | 407              | $2                  | 0.05 × 2 =$0.10                 |
| **Totals**     |                  | **$302**            | **$15.10**                      |

Previous balance: $0.00\
Current balance (total amount due): $302.00\
SUM(minimum per transaction): $15.10 **Minimum amount due (MAD):** $15.10

**Cycle 2 statement**\
(Assume MAD percentage = 5%.)

| Transaction ID | Transaction type | Transaction balance | Minimum payment per transaction |
| :------------- | :--------------- | :------------------ | :------------------------------ |
| 4              | 101              | $100                | 0.05 × 100 = $5                 |
| 5              | 123              | $100                | 0.05 × 100 =$5                  |
| 6              | 102              | $100                | 0.05 × 100 =$5                  |
| 7              | 101              | $0                  | 0.05 × 0 =$0                    |
| 8              | 407              | $2                  | 0.05 × 2 =$0.10                 |
| 9              | 404              | $2                  | 0.05 × 2 =$0.10                 |
| **Totals**     |                  | **$304**            | **$15.20**                      |

Previous balance: $302.00\
Current balance (total amount due): 302.00 + 304.00 = $606.00\
SUM(minimum per transaction): $15.20\
**If no payments were made:**\
**Minimum amount due (MAD):** 15.10 + 15.20 = $30.30

## Strategy 2 examples

These examples apply when `Minimum payment calculation method` is set to 2.

### First example

In Strategy 2, the Pismo platform calculates the overdue amount using the following formula.\
overdue amount = MAD from previous cycle - credits of type 7253 (Payment received) from current cycle

The over-limit amount is calculated at cycle closing as over-limit amount = current balance − max credit limit or 0 if current balance − max credit limit is negative. This amount is included in full (100%) in the MAD, independently of the over-limit fee. Separately, if the program parameter `Overlimit fee amount` is greater than zero, and the account exceeded its limit during the cycle, the platform posts a fee transaction (once per cycle) in the statement being closed.

The Pismo platform uses these results as follows to calculate the MAD.\
MAD = (current balance - overdue amount - over-limit amount) × MAD percentage + overdue amount + over-limit amount

**Cycle 1 statement**\
(Assume `Percentage for calculating the minimum payment amount` = 10%.)

| Transaction ID | Transaction type | Transaction balance |
| :------------- | :--------------- | :------------------ |
| 1              | 101              | $200                |
| 2              | 123              | $100                |
| 3              | 407              | $2                  |
| 4              | 112              | $300                |
| **Total**      |                  | **$602**            |

Previous balance: $0.00\
Current balance (total amount due): $602.00\
**Minimum amount due (MAD):** 602.00 × `Percentage for calculating the minimum payment amount` = 602.00 × 0.1 = $60.20

**Cycle 2 statement**\
(Assume `Percentage for calculating the minimum payment amount` = 10% and max credit limit = $1000.)

| Transaction ID | Transaction type | Transaction balance |
| :------------- | :--------------- | :------------------ |
| 5              | 101              | $100                |
| 6              | 123              | $150                |
| 7              | 102              | $200                |
| 8              | 112              | $300                |
| 9              | 201 (payment)    | ($100)              |
| **Total**      |                  | **$650**            |

Previous balance: $602.00\
Current balance (total amount due): 602.00 +  650.00 = $1252.00\
Overdue amount: $0 (since the payment of $100 was greater than the MAD for the previous cycle)\
Over-limit amount: 1252.00 - 1000.00 = $252.00\
**Calculate MAD:**\
(current balance - overdue amount - over-limit amount) × `Percentage for calculating the minimum payment amount` + overdue amount + over-limit amount = (1252.00 - 0 - 252.00) × 0.1 + 0 + 252.00 = 352.00\
**Minimum amount due (MAD):** $352.00

### Second example

The calculation is different if the account is overdue and there was an over-limit on the previous statement. In this case:\
MAD = (current balance - overdue amount - current debits amount) × `Percentage for calculating the minimum payment amount` + overdue amount + current debits amount. **Note:** In the following example, this condition only occurs in cycle 3, so the above formula is only used in that cycle.

**Cycle 1 statement**\
(Assume `Percentage for calculating the minimum payment amount` = 10% and account credit limit = $1000.)

| Transaction ID | Transaction type | Transaction balance | Full-amount? |
| :------------- | :--------------- | :------------------ | :----------- |
| 1              | 101              | $100                | No           |
| 2              | 123              | $380                | No           |
| 3              | 407              | $125                | No           |
| 4              | 101              | $100                | No           |
| **Total**      |                  | **$705**            |              |

Total credit: $0\
Previous balance: $0\
Current balance (total amount due): $705.00\
Overdue amount: $0\
Over-limit amount: $0\
**Calculate MAD:**\
(current balance - overdue amount - over-limit amount) × `Percentage for calculating the minimum payment amount` + overdue amount + over-limit amount = (705.00 - 0 - 0) × 0.1 + 0 + 0 = 70.50\
**Minimum amount due (MAD):** $70.50

**Cycle 2 statement**\
(Assume `Percentage for calculating the minimum payment amount`= 10% and account credit limit = $1000.)

| Transaction ID | Transaction type | Transaction balance | Full-amount? |
| :------------- | :--------------- | :------------------ | :----------- |
| 5              | 101              | $100                | No           |
| 6              | 123              | $150                | No           |
| 7              | 102              | $200                | No           |
| 8              | 101              | $100                | No           |
| 9              | 112              | $20                 | Yes          |
| 10             | 7253             | ($70.50)            | No (credit)  |
| **Total**      |                  | **$499.50**         |              |

Total credit: $70.50\
MAD from previous statement: $70.50\
Previous Balance: $705.00\
Current balance (total amount due): 705.00 + 499.50 = $1204.50\
Overdue amount: $0\
Over-limit amount: $204.50 (current balance - overdue amount - over-limit amount) × `Percentage for calculating the minimum payment amount` + overdue amount + over-limit amount = (1204.50 - 0 - 204.50) ×0.1 + 0 + 204.50 = 304.50\
**Calculate MAD:**\
Since one transaction (for $20) is configured to use 100%, this value must be removed from the current balance when performing the calculation. The formula is applied to this adjusted balance, and $20 is added to the result to get the actual MAD:\
Step 1: Adjusted balance = 1204.50 - 20.00 = 1184.50\
Step 2: Apply the formula. (adjusted balance - overdue amount - over-limit amount) × `Percentage for calculating the minimum payment amount` + overdue amount + over-limit amount = (1184.50 - 0 - 204.50) × 0.1 + 0 + 204.50 = 302.50\
Step 3: Add the full-amount transactions to the result. 302.50 + 20.00 = 322.50\
**Minimum amount due (MAD):** $322.50

**Cycle 3 statement**\
(Assume `Percentage for calculating the minimum payment amount` = 10% and account credit limit = $1000.)

| Transaction ID | Transaction type | Transaction balance | Full amount? (100%) |
| :------------- | :--------------- | :------------------ | :------------------ |
| 11             | 101              | $100                | No                  |
| **Total**      |                  | **$100.00**         |                     |

Total credits: $0\
Minimum previous statement: $322.50\
Previous balance: $1204.50\
Current balance (total amount due): 705 + 499.50 + 100 = $1304.50\
Overdue amount: $322.50\
Over-limit amount: $304.50\
**Calculate MAD:**\
(current balance - overdue amount - current debits amount) × `Percentage for calculating the minimum payment amount` + overdue amount + current debits amount = (1304.50  - 322.50 - 100) × 0.1 + 322.50 + 100 = 510.70\
**Minimum amount due (MAD):** $510.70
<!-- source:end -->

## API operations referenced

Operations linked from the source text, resolved by exact (case-insensitive) match of the link slug to an `operationId` in the current OpenAPI specifications. Full contracts are in the linked API-reference KUs.

| Method and path | operationId | Summary | Specification | Deprecated in spec | API-reference KU |
| --- | --- | --- | --- | --- | --- |
| `POST /programs/v1/programs/parameters/batch` | `setProgramsParameters` | Update program(s) parameters | `api-specs/Platform_setup_-_Programs.yaml` | no | KU-API-platform-setup-programs--parameters |
| `POST /statements-v2/v1/transactions-categories` | `createTransactionCategory` | Create program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}` | `updateTransactionCategoryInterest` | Update program transaction category | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--program-transaction-categories |
| `POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due` | `createStatementAmountDue` | Create or update statement minimum amount due | `api-specs/Revolving_credit_-_Statements.yaml` | no | KU-API-revolving-credit-statements--statement-minimum-amount-due |

### Operation essentials

- **`POST /programs/v1/programs/parameters/batch`** (`setProgramsParameters`): security `S2SAuthentication`; required parameters none declared; required body fields none declared; response statuses 204, 400; error codes in examples none; events none listed.
- **`POST /statements-v2/v1/transactions-categories`** (`createTransactionCategory`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 201, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`PUT /statements-v2/v1/transactions-categories/{transactionCategoryId}`** (`updateTransactionCategoryInterest`): security `BearerAuth`; required parameters `Authorization` (header), `program-id` (header), `transactionCategoryId` (path); required body fields `default_rate`, `fine_rate`, `minimum_value`, `overdue_rate_after_due_date`, `refinancing_rate_after_due_date`; response statuses 200, 400, 404, 500; error codes in examples `EX0002`, `EX0001`, `GN0001`; events none listed.
- **`POST /statements-v2/v1/accounts/{accountId}/minimum-amount-due`** (`createStatementAmountDue`): security `BearerAuth`; required parameters `accountId` (path), `Authorization` (header); required body fields `amount_type`, `minimum_amount_due`; response statuses 201, 400, 404, 500; error codes in examples `EX0002`, `CE0001`, `GN0001`; events none listed.

## Lifecycle status

- `docs/card-issuing/minimum-amount-due-calculation.md`: updatedAt 2026-08-20T17:14:12.000Z.
- No deprecation, removal or beta marker was found in the source or its linked operations.

## Conflicts, caveats and evidence gaps

- Source content contains MDX/HTML components (for example `<Table>`, `<HTMLBlock>`, `<Callout>`, `<details>`). They are preserved exactly as published; tables inside them were not converted to Markdown.

## Source references

| Source file | Section / operation | Source URL | SHA-256 | updatedAt |
| --- | --- | --- | --- | --- |
| `docs/card-issuing/minimum-amount-due-calculation.md` | whole document | https://developers.pismo.io/pismo-docs/docs/minimum-amount-due-calculation | `c0ee25cd1dc79984…` | 2026-08-20T17:14:12.000Z |

## Related knowledge units

- `KU-API-platform-setup-programs--parameters` — API reference: Platform setup - Programs — Parameters
- `KU-API-revolving-credit-statements--program-transaction-categories` — API reference: Revolving credit - Statements — Program transaction categories
- `KU-API-revolving-credit-statements--statement-minimum-amount-due` — API reference: Revolving credit - Statements — Statement minimum amount due
- `KU-CC-get-started-control-center` — Get started with Control Center
- `KU-CRED-full-balance-credit-program` — Full balance credit programs: concepts and configuration
